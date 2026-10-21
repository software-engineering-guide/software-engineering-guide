# 3.15 Bộ nhớ đệm và phân phối nội dung

## Tổng quan và động lực

Một [bộ nhớ đệm](https://en.wikipedia.org/wiki/Cache_(computing)) là một bản sao dữ liệu được giữ ở nơi nhanh hơn hoặc gần hơn bản gốc, để bạn trả lời một yêu cầu mà không phải làm lại toàn bộ công việc đắt đỏ. Gần như mọi hệ thống có cảm giác nhanh đều nhanh nhờ lưu đệm. Truy vấn cơ sở dữ liệu lẽ ra mất 40 mili giây trả về trong chưa đầy một khi kết quả của nó đã nằm sẵn trong bộ nhớ. Bức ảnh lẽ ra phải băng qua một đại dương được phục vụ từ một máy trong cùng thành phố. Lưu đệm là kỹ thuật hiệu năng có đòn bẩy cao nhất bạn có, và cũng là kỹ thuật dễ trao cho bạn một lỗi tinh vi, điên đầu nhất.

Chương này đi sâu vào chiến lược lưu đệm. Chương 3.4 (kiến trúc và lưu trữ dữ liệu) giới thiệu bộ nhớ đệm và mạng phân phối nội dung như một mối quan tâm lưu trữ giữa nhiều mối quan tâm khác, và chương 3.13 (mạng và kết nối) bao quát đường mạng mà chúng đi trên đó. Ở đây bạn nhận các quyết định: đặt bộ đệm ở đâu, đặt khóa thế nào, khi nào vô hiệu hóa, bảo vệ nó dưới tải ra sao, và suy luận về độ cũ mà bạn đang đổi lấy tốc độ. Lưu đệm chạm vào kỹ thuật hiệu năng (chương 2.16), khả năng mở rộng và phục hồi (chương 3.5), thực tế thất bại một phần của hệ thống phân tán (chương 3.3), và, vì một bộ đệm bị đầu độc có thể phục vụ một cuộc tấn công cho hàng nghìn người dùng, bảo mật ứng dụng (chương 4.2).

Động lực quy về ba đòn bẩy. Lưu đệm cắt giảm độ trễ, để người dùng chờ ít hơn. Nó cắt giảm tải, để nguồn gốc của bạn phục vụ nhiều lưu lượng hơn trên cùng phần cứng. Và nó cắt giảm chi phí, vì một yêu cầu được trả lời ở rìa không bao giờ chạm vào cơ sở dữ liệu, tính toán, hay hóa đơn đi ra của bạn. Với các đội lớn, một chiến lược lưu đệm dùng chung là sự khác biệt giữa một nền tảng mở rộng có thể dự đoán và một nền tảng nơi mọi dịch vụ phát minh lại việc vô hiệu hóa và làm sai. Trong các hệ thống doanh nghiệp và chính phủ, nơi lưu lượng tăng vọt vào hạn nộp hồ sơ và ngày ra mắt, một bộ đệm được thiết kế tốt thường là thứ đứng giữa một cổng thông tin hoạt động và một thất bại công khai.

## Các nguyên tắc chính

- Lưu đệm để cắt giảm độ trễ, tải và chi phí, và biết bạn đang mua cái nào.
- Đặt bộ đệm ở đúng tầng của hệ thống phân cấp, gần nơi chúng giúp ích nhất.
- Coi vô hiệu hóa là phần khó; hãy thiết kế khóa và thời gian sống trước khi bạn lưu đệm.
- Bảo vệ bộ đệm dưới tải bằng hợp nhất yêu cầu, nhiễu (jitter) và phòng thủ chống giẫm đạp.
- Chọn mẫu ghi có chủ đích: nhất quán và tốc độ kéo ngược nhau.
- Đo tỷ lệ trúng, độ cũ và tải nguồn; một bộ đệm không đo là một khoản nợ.
- Coi nội dung được lưu đệm là bề mặt tấn công; một bộ đệm bị đầu độc phục vụ mọi người.

## Khuyến nghị

### Hiểu hệ thống phân cấp bộ nhớ đệm

Lưu đệm không phải một thứ ở một nơi. Nó là một hệ thống phân cấp các bản sao, mỗi cái gần người dùng hơn cái trước, và bạn thiết kế xuyên suốt tất cả. Gần người dùng nhất là bộ đệm máy khách: bộ đệm HTTP của trình duyệt, kho cục bộ của ứng dụng di động, bộ đệm bộ nhớ trong tiến trình. Kế tiếp là [mạng phân phối nội dung](https://en.wikipedia.org/wiki/Content_delivery_network) (CDN), một đội máy chủ phân bố khắp thế giới giữ các bản sao nội dung của bạn ở rìa mạng, gần người dùng. Phía sau đó là bộ đệm proxy ngược hoặc cổng, một bộ đệm dùng chung phía trước các máy chủ của bạn. Rồi đến bộ đệm ứng dụng: một kho khóa-giá trị nhanh như lưới dữ liệu trong bộ nhớ giữ kết quả đã tính, phiên và các mảnh đã kết xuất. Cuối cùng là bộ đệm truy vấn và bộ đệm vùng đệm riêng của cơ sở dữ liệu, giữ các trang nóng trong bộ nhớ để đĩa ít bị chạm hơn.

Mỗi tầng phục vụ một công việc riêng: bộ đệm máy khách loại bỏ hoàn toàn yêu cầu, CDN hấp thụ lưu lượng đọc toàn cầu, proxy ngược che chắn nguồn gốc của bạn khỏi công việc giống hệt lặp lại, bộ đệm ứng dụng tiết kiệm tính toán lại, và bộ đệm cơ sở dữ liệu giữ cho kho phản hồi nhanh. Một yêu cầu trượt mọi tầng và đến cơ sở dữ liệu là đường chậm nhất, đắt nhất bạn có, nên mục đích của hệ thống phân cấp là trả lời càng cao và càng ra ngoài càng tốt trong chừng mực an toàn. Hãy thiết kế nó như một hệ thống, vì một mảnh được lưu đệm ở tầng ứng dụng và một bản sao CDN cũ phía trên nó có thể bất đồng theo cách làm người dùng bối rối.

### Coi vô hiệu hóa là vấn đề khó

Có một câu đùa cũ rằng hai vấn đề khó nhất trong khoa học máy tính là đặt tên, [vô hiệu hóa bộ đệm](https://en.wikipedia.org/wiki/Cache_invalidation), và lỗi lệch một. Câu đùa tồn tại vì vô hiệu hóa thực sự khó: bộ đệm là một bản sao, và ngay khoảnh khắc bản gốc thay đổi, mọi bản sao là một lời nói dối tiềm tàng. Bạn có ba chiến lược rộng. Hết hạn theo thời gian với thời gian sống (TTL), khoảng thời gian một mục còn hợp lệ trước khi bị coi là cũ, là đơn giản nhất: bạn chấp nhận độ cũ có giới hạn và để các mục già đi rồi hết hạn. Vô hiệu hóa tường minh thanh trừ hoặc cập nhật các mục khi dữ liệu nền thay đổi, chính xác nhưng đòi hỏi bạn biết mọi nơi một bản sao sống. Vô hiệu hóa hướng sự kiện đăng ký các bộ đệm vào sự kiện thay đổi để chúng tự làm mới, mở rộng tốt hơn qua nhiều bộ đệm nhưng thêm một phụ thuộc nhắn tin.

Hầu hết hệ thống thực pha trộn những thứ này: TTL ngắn cho dữ liệu đổi thường xuyên và chịu được vài giây cũ, TTL dài cộng thanh trừ tường minh cho dữ liệu hiếm đổi nhưng phải đúng khi nó đổi, và khóa bộ đệm có phiên bản cho nội dung bất biến khi đã được xuất bản. Mẹo khóa có phiên bản đáng ghi nhớ: thay vì vô hiệu hóa, bạn đổi khóa. Một bảng định kiểu được phục vụ dưới tên `app.v187.css` không bao giờ cần thanh trừ, vì một phiên bản mới là một khóa mới và cái cũ đơn giản thôi được yêu cầu. Bất cứ khi nào bạn có thể biến một vấn đề vô hiệu hóa thành vấn đề đặt tên, hãy làm.

### Thiết kế khóa bộ đệm và TTL có chủ đích

Một bộ đệm chỉ tốt bằng khóa của nó. [Khóa bộ đệm](https://en.wikipedia.org/wiki/Cache_(computing)) là định danh dưới đó một giá trị được lưu và tra cứu, và làm sai gây ra hai thất bại đối nghịch. Quá thô, và bạn phục vụ dữ liệu của người dùng này cho người khác: một trang cá nhân hóa được lưu đệm dưới một URL bỏ qua danh tính người dùng là một rò rỉ dữ liệu. Quá mịn, và tỷ lệ trúng của bạn sụp đổ vì không hai yêu cầu nào chia sẻ khóa. Hãy quyết định có chủ đích cái gì thuộc về khóa: danh tính tài nguyên cộng bất cứ thứ gì chính đáng làm thay đổi phản hồi (ngôn ngữ, tiền tệ, loại thiết bị) và không có gì khác. Chuẩn hóa khóa để các khác biệt vụn vặt như thứ tự tham số truy vấn không làm phân mảnh bộ đệm.

TTL xứng đáng được nghĩ kỹ như vậy. Một TTL là lời hứa về độ cũ tối đa bạn sẽ phục vụ, nên hãy đặt nó từ mức chịu đựng thực của dữ liệu, không phải một con số tròn ai đó đoán: một bảng giá chứng khoán chịu được vài giây, một danh mục sản phẩm vài phút, một quy định đã xuất bản hàng giờ hoặc một khóa có phiên bản và không hết hạn gì cả. Thêm một độ trải ngẫu nhiên nhỏ, gọi là nhiễu (jitter), để một lô mục được ghi cùng nhau không hết hạn đúng một khoảnh khắc và giẫm đạp lên nguồn gốc. Hãy ghi những lựa chọn này ra, vì một TTL không có lý do là con số mà kỹ sư kế tiếp sẽ sợ đổi.

### Bảo vệ chống giẫm đạp và hợp nhất yêu cầu

Khi một mục được lưu đệm phổ biến hết hạn, mọi yêu cầu muốn nó cùng trượt một lúc và đổ xô vào nguồn gốc cùng nhau. Đây là [giẫm đạp bộ đệm](https://en.wikipedia.org/wiki/Cache_stampede), còn gọi là bầy đàn xô đẩy, và nó có thể làm đổ chính cơ sở dữ liệu mà bộ đệm đang bảo vệ. Hãy xây phòng thủ một lần và tái sử dụng ở mọi nơi. Hợp nhất yêu cầu (single-flight) cho phép chỉ yêu cầu đầu tiên đối với một khóa bị thiếu tính lại giá trị trong khi những yêu cầu khác chờ kết quả của nó, nên một nghìn lần trượt đồng thời chỉ gây ra một lệnh gọi nguồn gốc. Tính lại sớm theo xác suất làm mới một mục nóng ngẫu nhiên hơi trước khi nó hết hạn, để một yêu cầu nền gia hạn nó trước khi đám đông thấy một lần trượt. Chính sách stale-while-revalidate phục vụ ngay bản sao hơi cũ và làm mới nó bất đồng bộ, để người dùng không bao giờ chờ một lần trượt.

Những mẫu này quan trọng nhất chính xác khi bạn cần bộ đệm nhất, dưới tải đỉnh, vì vậy hãy xác thực chúng ở quy mô thực tế: một phòng thủ hoạt động với mười người dùng vẫn có thể thất bại với mười nghìn. Hãy kết hợp chúng với các mẫu khả năng phục hồi của chương 3.5, đặc biệt là thời gian chờ và bộ ngắt mạch, để khi nguồn gốc thực sự chậm tầng bộ đệm che chắn cho nó thay vì chất thêm. Mục tiêu là một bộ đệm hành xử tốt nhất dưới áp lực, không phải một bộ đệm khuếch đại một đợt tăng đột biến thành sự cố.

### Chọn mẫu ghi có chủ đích

Cách bạn xử lý ghi quyết định bộ đệm tươi đến đâu và bạn mạo hiểm bao nhiêu khi thất bại. Có bốn mẫu phổ biến. Trong [cache-aside](https://en.wikipedia.org/wiki/Cache_(computing)) (nạp lười), ứng dụng kiểm tra bộ đệm, và khi trượt đọc nguồn gốc, điền bộ đệm, rồi trả giá trị; ghi đi đến nguồn gốc và vô hiệu hóa mục. Nó là mặc định vì lý do chính đáng: đơn giản, và bộ đệm chỉ giữ những gì được yêu cầu. Trong ghi xuyên suốt (write-through), mọi lần ghi đi đến bộ đệm và nguồn gốc cùng nhau, nên bộ đệm luôn hiện hành, với cái giá là độ trễ ghi và lưu đệm dữ liệu có thể không bao giờ được đọc. Trong ghi sau (write-back, write-behind), ghi chạm bộ đệm trước và xả sang nguồn gốc bất đồng bộ, làm ghi nhanh nhưng mạo hiểm mất mát nếu bộ đệm chết trước khi xả. Trong ghi vòng (write-around), ghi đi thẳng đến nguồn gốc và bỏ qua bộ đệm, tránh khuấy động từ dữ liệu nặng ghi hiếm khi đọc, với cái giá là một lần trượt chắc chắn ở lần đọc đầu.

Hãy chọn theo từng khối lượng công việc, không phải một lần cho cả hệ thống. Một danh mục nặng đọc hợp với cache-aside hoặc write-through. Một luồng nhật ký hay chỉ số nặng ghi hợp với write-around, để bộ đệm không bị khuấy động bởi dữ liệu không ai đọc lại. Write-back hợp với ghi thông lượng cao nơi một rủi ro mất mát nhỏ, được hiểu rõ là chấp nhận được và độ bền được xử lý ở nơi khác. Hãy nêu mẫu cho mỗi bộ đệm một cách tường minh, vì một người đọc giả định cache-aside khi mã làm write-back sẽ đánh giá sai cả độ tươi lẫn hành vi thất bại.

### Khớp chính sách loại bỏ với mẫu truy cập của bạn

Một bộ đệm có kích thước cố định, nên khi nó đầy, một thứ gì đó phải đi. Chính sách loại bỏ quyết định thứ gì. [Ít được dùng gần đây nhất](https://en.wikipedia.org/wiki/Cache_replacement_policies) (LRU) loại bỏ mục không được chạm lâu nhất, đánh cược rằng việc dùng gần đây dự đoán việc dùng tương lai, và là mặc định hợp lý. Ít được dùng thường xuyên nhất (LFU) loại bỏ mục có ít lượt trúng nhất, phù hợp với các tập nóng ổn định nơi một vài mục luôn phổ biến nhưng có thể bám lấy các mục từng nóng một lần và không bao giờ thích ứng. Các biến thể như LRU phân đoạn và chính sách thích ứng pha trộn tính gần đây và tần suất; vào-trước-ra-trước và hết hạn theo thời gian đơn giản rẻ hơn nhưng cùn hơn.

Hãy khớp chính sách với cách dữ liệu của bạn được truy cập: LFU hoặc chính sách nhận biết tần suất cho một tập nóng nhỏ hiếm khi dịch chuyển, LRU ở nơi độ phổ biến di chuyển theo thời gian như tin tức hay nội dung xu hướng. Dù bạn chọn gì, hãy định cỡ bộ đệm để tập nóng vừa vặn, vì một bộ đệm quá nhỏ để giữ tập làm việc sẽ đập liên hồi, loại bỏ các mục ngay trước khi chúng được cần lại. Hãy theo dõi tỷ lệ loại bỏ như một chỉ số hạng nhất, vì một đợt tăng đột ngột thường có nghĩa bộ đệm bị định cỡ thiếu hoặc một vụ bùng nổ khóa đang phân mảnh nó.

### Dùng đúng ngữ nghĩa lưu đệm HTTP

Web có một mô hình lưu đệm trưởng thành, được chuẩn hóa, tích hợp sẵn trong [HTTP](https://en.wikipedia.org/wiki/HTTP), và dùng nó tốt cho bạn lưu đệm máy khách và CDN miễn phí. Tiêu đề `Cache-Control` là bề mặt điều khiển: `max-age` đặt thời gian sống tươi, `public` và `private` nói liệu các bộ đệm dùng chung có được lưu phản hồi không, `no-store` cấm lưu đệm, và `stale-while-revalidate` cho phép phục vụ bản sao cũ trong khi làm mới. Xác thực cho phép một bộ đệm kiểm tra độ tươi rẻ mà không tải lại phần thân. Một [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) (thẻ thực thể) là một định danh phiên bản mờ mà máy chủ gắn vào phản hồi; máy khách gửi lại nó trong tiêu đề `If-None-Match`, và máy chủ trả lời `304 Not Modified` không có phần thân nếu không có gì đổi. `Last-Modified` với `If-Modified-Since` làm điều tương tự bằng dấu thời gian.

Kỷ luật thực tế là tường minh. Đặt `Cache-Control` trên mọi phản hồi thay vì để các bộ đệm đoán bằng heuristic. Đánh dấu các phản hồi riêng tư, theo từng người dùng là `private` hoặc `no-store` để một proxy dùng chung không bao giờ lưu chúng, một sai lầm phổ biến và nguy hiểm. Dùng URL có phiên bản với max-age dài và chỉ thị `immutable` cho tài sản tĩnh, và xác thực bằng ETag cho nội dung đổi không đoán trước. Làm đúng các tiêu đề này biến toàn bộ tầng máy khách và CDN thành một bộ đệm đúng, dựa trên tiêu chuẩn mà bạn không phải tự xây.

### Đẩy công việc ra rìa với CDN và điện toán rìa

Một CDN khởi đầu như cách lưu đệm tệp tĩnh gần người dùng, và nó vẫn làm điều đó xuất sắc: hình ảnh, tập lệnh, video và tải xuống được phục vụ từ một vị trí rìa cách vài mili giây thay vì một nguồn gốc xa. Các CDN hiện đại đi xa hơn. Chúng lưu đệm nội dung động và cá nhân hóa với khóa mịn, kết thúc TLS ở rìa, hấp thụ các đợt tăng lưu lượng và tấn công từ chối dịch vụ phân tán, và ngày càng chạy mã của bạn. [Điện toán rìa](https://en.wikipedia.org/wiki/Edge_computing) thực thi logic tại chính các vị trí rìa, để bạn có thể cá nhân hóa một phản hồi, kiểm tra cấp quyền, hay lắp ráp một mảnh trang mà không cần một vòng đi về đến một vùng trung tâm.

Hãy dựa vào điều này cho các lần đọc chi phối hầu hết hệ thống. Đặt tài sản tĩnh sau CDN với URL có phiên bản sống lâu, lưu đệm phản hồi API ở rìa nơi độ tươi cho phép (đặt khóa cẩn thận để cá nhân hóa không rò rỉ), và dùng tính toán rìa cho logic nhẹ, nhạy cảm với độ trễ gần người dùng. Đánh đổi là tầm với so với kiểm soát: rìa nhanh và gần nhưng xa dữ liệu của bạn và khó gỡ lỗi hơn, nên hãy giữ bất cứ thứ gì đòi hỏi nhất quán mạnh hoặc trạng thái có thẩm quyền mới ở nguồn gốc và để rìa xử lý lượng lưu lượng đọc khổng lồ, lưu đệm được.

### Coi bộ đệm là bề mặt tấn công

Một bộ đệm phục vụ cùng một phản hồi đã lưu cho nhiều người dùng, khiến nó thành mục tiêu. [Đầu độc bộ đệm](https://en.wikipedia.org/wiki/Cache_poisoning) là một cuộc tấn công trong đó một yêu cầu được chế tạo để bộ đệm lưu một phản hồi có hại hoặc do kẻ tấn công kiểm soát rồi phục vụ nó cho mọi người theo sau. Nó thường khai thác một đầu vào không có khóa: một tiêu đề mà ứng dụng phản chiếu vào phản hồi nhưng bộ đệm bỏ qua khi dựng khóa. Tấn công lừa dối bộ đệm web liên quan lừa một bộ đệm lưu phản hồi riêng tư của nạn nhân dưới một URL công khai. Cả hai là thất bại của việc đặt khóa và tin đầu vào, được bao quát rộng hơn trong chương 4.2.

Hãy phòng thủ có chủ đích. Đưa vào khóa bộ đệm mọi đầu vào có thể thay đổi phản hồi, và từ chối phản chiếu các tiêu đề không có khóa vào phần thân được lưu đệm. Không bao giờ để một bộ đệm dùng chung lưu các phản hồi đã xác thực, theo từng người dùng dưới một khóa dùng chung. Chuẩn hóa và xác thực đường dẫn và tham số yêu cầu trước khi lưu đệm. Đặt `Vary` đúng để các bộ đệm phân vùng phản hồi theo những tiêu đề thực sự quan trọng, như mã hóa nội dung hay ngôn ngữ. Vì một mục bị đầu độc đơn lẻ gây hại cho mọi người dùng hạ nguồn, hãy coi cấu hình bộ đệm là mã nhạy cảm về bảo mật và rà soát nó như vậy.

### Làm hành vi bộ đệm quan sát được

Bạn không thể quản lý một bộ đệm bạn không thấy. Chỉ số chính là tỷ lệ trúng: tỷ lệ yêu cầu được phục vụ từ bộ đệm thay vì nguồn gốc. Một tỷ lệ trúng lặng lẽ giảm từ 95 xuống 70 phần trăm có thể nhân tải nguồn gốc lên nhiều lần và báo trước một sự cố, và bạn chỉ bắt được sớm nếu theo dõi nó. Đo đạc từng tầng riêng biệt, vì một tỷ lệ trúng CDN khỏe mạnh có thể che giấu một tỷ lệ trúng bộ đệm ứng dụng đang sụp đổ bên dưới. Đây là gương mặt riêng của lưu đệm trong các thực hành quan sát ở chương 9.2.

Hãy theo dõi nhiều hơn lượt trúng: tỷ lệ loại bỏ và áp lực bộ nhớ để bắt định cỡ thiếu, độ trễ ở mỗi tầng để xác nhận bộ đệm thực sự nhanh hơn, tốc độ yêu cầu nguồn gốc để thấy bộ đệm hấp thụ bao nhiêu tải, và độ cũ (các mục được phục vụ cũ bao nhiêu) để xác nhận bạn tôn trọng lời hứa về độ tươi. Hãy cảnh báo trên các tỷ lệ báo trước rắc rối, đặc biệt là tỷ lệ trúng giảm hoặc tỷ lệ loại bỏ tăng, để bạn biết về một bộ đệm đang suy giảm từ bảng điều khiển thay vì từ người dùng. Một bộ đệm được quan sát là tài sản bạn điều chỉnh được; một bộ đệm không được quan sát là một phụ thuộc ẩn đang chờ làm bạn bất ngờ.

## Đánh đổi: ưu và nhược điểm

Lưu đệm mua tốc độ và quy mô bằng đồng tiền của độ tươi và độ phức tạp. Mỗi bộ đệm là một canh bạc rằng cũ-nhưng-nhanh thắng tươi-nhưng-chậm cho dữ liệu cụ thể này, và nghệ thuật là đặt canh bạc đó một cách có ý thức thay vì theo mặc định. Bảng dưới đây tóm tắt các lựa chọn chính.

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Cache-aside | Đơn giản; chỉ lưu đệm những gì được đọc | Lần đọc đầu luôn trượt; rủi ro cũ ngắn sau khi ghi |
| Write-through | Bộ đệm luôn hiện hành khi ghi | Ghi chậm hơn; lưu đệm dữ liệu có thể không bao giờ được đọc |
| Write-back | Ghi rất nhanh; hấp thụ các đợt bùng nổ | Rủi ro mất dữ liệu nếu bộ đệm hỏng trước khi xả |
| Write-around | Tránh khuấy động bộ đệm với dữ liệu nặng ghi | Lần đọc đầu chắc chắn trượt |
| TTL ngắn | Độ cũ nhỏ, có giới hạn | Tỷ lệ trúng thấp hơn; nhiều tải nguồn gốc hơn |
| TTL dài / khóa có phiên bản | Tỷ lệ trúng cao; tải nguồn gốc thấp | Cũ trừ khi vô hiệu hóa; cần khóa có kỷ luật |
| CDN và rìa | Độ trễ thấp toàn cầu; hấp thụ tăng đột biến | Xa dữ liệu; khó gỡ lỗi và vô hiệu hóa hơn |
| Loại bỏ LRU | Thích ứng với độ phổ biến dịch chuyển | Có thể loại bỏ tập nóng ổn định dưới tải nặng quét |
| Loại bỏ LFU | Bảo vệ tập nóng ổn định | Chậm thích ứng; bám lấy các mục từng nóng |

Căng thẳng lặp lại là nhất quán so với hiệu năng. Một bộ đệm với TTL dài và tỷ lệ trúng cao nhanh và rẻ và có thể phục vụ dữ liệu cũ; một bộ đệm với TTL ngắn và vô hiệu hóa quyết liệt thì tươi và đúng và làm nguồn gốc làm việc nhiều hơn. Không có câu trả lời đúng phổ quát, chỉ có câu trả lời đúng cho từng phần dữ liệu, được đặt bởi mức chịu đựng thực của nó với độ cũ. Căng thẳng thứ hai là đơn giản so với tầm với: một bộ đệm ứng dụng gần dữ liệu của bạn và dễ suy luận, trong khi rìa thì xa, nhanh, và khó vô hiệu hóa hơn. Hãy giải quyết cả hai bằng cách phân loại dữ liệu theo nhu cầu độ tươi và khối lượng đọc, rồi đặt và cấu hình từng lớp một cách có chủ đích.

## Câu hỏi để thảo luận với đội của bạn

1. **Mức chịu đựng độ cũ thực của từng loại dữ liệu chúng ta lưu đệm là gì, và chúng ta đã đặt TTL cùng vô hiệu hóa từ mức chịu đựng đó thay vì từ thói quen chưa?** Hầu hết các đội lưu đệm với một TTL ai đó chọn một lần và không bao giờ xem lại, nên một số dữ liệu được phục vụ cũ hơn mức doanh nghiệp chấp nhận trong khi dữ liệu khác hết hạn quyết liệt đến mức bộ đệm hầu như không giúp gì. Hãy mang mười tài nguyên được lưu đệm hàng đầu của bạn và, với mỗi cái, hỏi những người sở hữu dữ liệu đó nó có thể cũ bao nhiêu một cách an toàn: vài giây, vài phút, vài giờ, hay không bao giờ khi đã xuất bản. Bạn thường sẽ thấy các câu trả lời khác nhau rất nhiều và các TTL hiện tại của bạn không khớp với chúng. Kết quả bạn muốn là một phân loại độ tươi ngắn, mỗi lớp ánh xạ với một cách tiếp cận (TTL ngắn, TTL dài cộng thanh trừ, hay khóa bất biến có phiên bản), để các quyết định lưu đệm theo từ ngữ nghĩa dữ liệu thay vì đoán mò.

2. **Nếu mục bộ đệm phổ biến nhất của chúng ta hết hạn ngay bây giờ dưới lưu lượng đỉnh, điều gì sẽ xảy ra với nguồn gốc?** Câu hỏi này phơi bày bạn có bảo vệ chống giẫm đạp thực sự hay chỉ có hy vọng. Nhiều hệ thống chạy tốt cho đến khi một khóa nóng hết hạn trong lúc lưu lượng đỉnh và mọi yêu cầu giẫm đạp cơ sở dữ liệu cùng lúc, biến bộ đệm từ một tấm khiên thành một kích hoạt. Hãy đi qua đường đi cụ thể cho điểm cuối bận rộn nhất của bạn: có hợp nhất yêu cầu để chỉ một lần trượt đến nguồn gốc không, có nhiễu để các mục không hết hạn đồng loạt không, có chính sách stale-while-revalidate để người dùng không bao giờ chờ một lần nạp lại không? Hãy mang bằng chứng kiểm thử tải, không phải trực giác, vì một phòng thủ chống giẫm đạp giữ được ở mười người dùng vẫn có thể sụp đổ ở mười nghìn. Nếu bạn không thể trả lời tự tin, khoản đầu tư khả năng phục hồi kế tiếp của bạn vừa tìm thấy bạn.

3. **Chúng ta có chắc rằng không bộ đệm dùng chung nào lưu dữ liệu riêng tư của một người dùng dưới một khóa mà người dùng khác có thể truy cập không?** Đây là sai lầm lưu đệm trở thành sự cố bảo mật và tiêu đề báo. Nó xảy ra khi một phản hồi cá nhân hóa hay đã xác thực được lưu đệm dưới một khóa bỏ qua danh tính người dùng, hoặc khi một tiêu đề `Cache-Control` định giữ một phản hồi riêng tư bị thiếu, để một proxy dùng chung hay CDN lưu nó và phục vụ cho người kế tiếp. Hãy kiểm toán phản hồi nào có thể lưu đệm ở các tầng dùng chung, xác nhận mọi phản hồi theo từng người dùng được đánh dấu `private` hoặc `no-store`, và xác nhận mọi khóa bộ đệm bao gồm mọi đầu vào làm thay đổi phản hồi. Hãy coi đây là rà soát bảo mật, vì bán kính ảnh hưởng là mọi người dùng hạ nguồn, và kết nối nó với các thực hành trong chương 4.2.

4. **Mỗi bộ đệm của chúng ta thực sự dùng mẫu ghi nào, và có ai chọn nó có chủ đích không?** Cache-aside, write-through, write-back và write-around đưa ra các lời hứa trái ngược về độ tươi và về những gì bạn mất khi bộ đệm hỏng, vậy mà trong hầu hết cơ sở mã mẫu là bất cứ thứ gì tác giả đầu tiên tình cờ sao chép. Với một đội lớn điều này quan trọng vì một dịch vụ giả định độ tươi cache-aside trong khi dịch vụ khác lặng lẽ chạy write-back có thể tạo ra dữ liệu trông như bị hỏng nhưng chỉ là cũ, và kỹ sư trực ca mất hàng giờ đuổi theo một bóng ma. Hãy mang bản kiểm kê theo từng bộ đệm: mẫu ghi, độ tươi nó bảo đảm, và điều gì xảy ra với các lần ghi chưa xả nếu tiến trình chết. Ở nơi bất kỳ bộ đệm nào dùng write-back, hãy mang câu chuyện về độ bền hậu thuẫn nó. Trong các hệ thống doanh nghiệp và chính phủ xử lý dữ liệu tài chính hay hồ sơ, một bộ đệm write-back không có bảo đảm hậu thuẫn là một phát hiện kiểm toán đang chờ, nên cuộc thảo luận nên kết thúc với mẫu của mỗi bộ đệm được gọi tên, biện minh và ghi lại.

5. **Khi chúng ta triển khai hoặc đổi dữ liệu, mọi tầng bộ đệm liên quan có vô hiệu hóa đúng không, hay chúng ta dựa vào ai đó nhớ thanh trừ?** Vô hiệu hóa là phần khó, và chế độ thất bại thì im lặng: một giá trị đã sửa vẫn sai hàng giờ vì một tầng của hệ thống phân cấp, một CDN, một proxy ngược, hay một bộ đệm ứng dụng, không bao giờ nhận được thông báo. Một tổ chức lớn nhân rủi ro này lên, vì một thay đổi logic đơn lẻ có thể cần lan truyền qua nhiều bộ đệm ở nhiều vùng do các đội khác nhau sở hữu. Hãy mang một dấu vết cụ thể của một thay đổi dữ liệu gần đây và theo nó qua mọi tầng bộ đệm, hỏi ở mỗi tầng: cái gì kích hoạt vô hiệu hóa ở đây, và mất bao lâu? Hãy ưu tiên các thiết kế biến vô hiệu hóa thành đặt tên (khóa có phiên bản) hoặc thành sự kiện (một thay đổi công bố một thanh trừ) hơn sổ tay vận hành thủ công. Trong các hệ thống khu vực công nơi một con số được công bố sai, một mức thuế hay một khoản trợ cấp, có thể mang sức nặng pháp lý, một khoảng trống vô hiệu hóa không phải phiền toái mà là mức độ phơi nhiễm tuân thủ, nên kết quả nên là một đường vô hiệu hóa được ánh xạ cho mọi lớp dữ liệu được lưu đệm.

6. **Chúng ta đang coi lưu đệm là hạ tầng nền tảng dùng chung, hay mỗi đội tự phát minh lại khóa, vô hiệu hóa và bảo vệ chống giẫm đạp?** Lưu đệm làm tốt là một tập nhỏ các vấn đề khó được giải một lần: khóa chuẩn hóa, vô hiệu hóa hướng sự kiện, hợp nhất yêu cầu, ngữ nghĩa HTTP đúng, và khả năng quan sát theo từng tầng. Khi mỗi đội ứng biến những thứ này, một tổ chức lớn trả giá cho cùng những sai lầm lặp đi lặp lại, và một lỗi đầu độc hay rò rỉ dữ liệu riêng tư được sửa ở một dịch vụ âm thầm tồn tại ở mười dịch vụ khác. Hãy mang một bản đồ trung thực về ai sở hữu quy ước lưu đệm hôm nay và có bao nhiêu mã lưu đệm trùng lặp qua các dịch vụ. Cân nhắc đối lập là quyền tự chủ: các đội cưỡng lại một thư viện dùng chung bị bắt buộc, nên hãy cân nhắc một mặc định đường lát sẵn dễ áp dụng so với một tiêu chuẩn cứng được thực thi. Với một nhóm nền tảng doanh nghiệp hay chính phủ, một năng lực lưu đệm dùng chung, được kiểm thử tốt cũng là cách rẻ nhất để làm cho yêu cầu bảo mật và kiểm toán đứng vững một cách đồng đều, nên cuộc thảo luận nên quyết định cái gì trở thành hạ tầng dùng chung và ai tài trợ.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Lưu đệm là con đường rẻ nhất của bạn để sống sót qua một đợt tăng lưu lượng mà bạn chưa thể gánh để mở rộng, vì vậy hãy dành ít thời gian bạn có cho một vài vị trí đòn bẩy cao: một CDN với URL có phiên bản cho tài sản tĩnh, và một tầng cache-aside duy nhất với TTL ngắn và nhiễu phía trước truy vấn nóng nhất của bạn. Hãy dựa vào dịch vụ CDN và bộ đệm được quản lý thay vì tự chạy, và thêm hợp nhất yêu cầu sớm, vì một đợt giẫm đạp ngày ra mắt vào một cơ sở dữ liệu nhỏ là thất bại có khả năng nhất làm một ngày tốt kết thúc tồi. Bỏ qua các lược đồ vô hiệu hóa công phu cho đến khi bạn có dữ liệu cho thấy chúng quan trọng.

**Doanh nghiệp nhỏ.** Không có chuyên gia lưu đệm và ngân sách eo hẹp, hãy ưu tiên mua lưu đệm bạn có miễn phí bên trong các công cụ bạn đã chạy: một CDN đi kèm hosting, tiêu đề HTTP `Cache-Control` trên phản hồi của khung web, và bộ đệm truy vấn tích hợp sẵn của cơ sở dữ liệu. Quyết định xây-so-với-mua gần như luôn nghiêng về mua ở đây, vì một bộ đệm đặt sai khóa làm rò rỉ dữ liệu của khách hàng này cho khách hàng khác tốn nhiều hơn hẳn dịch vụ được quản lý mà bạn đã né. Hãy làm đúng hai thắng lợi rẻ, tiêu đề HTTP đúng và không bao giờ lưu đệm trang đã xác thực ở các tầng dùng chung, và để yên các mẫu kỳ lạ.

**Doanh nghiệp lớn.** Ở quy mô lớn qua nhiều đội rủi ro dịch chuyển từ bất kỳ bộ đệm đơn lẻ nào sang sự không nhất quán giữa chúng: lược đồ khóa phân kỳ, vô hiệu hóa không đồng đều, và rò rỉ dữ liệu riêng tư xuất hiện ở một dịch vụ mà không ở dịch vụ khác. Hãy cung cấp lưu đệm như hạ tầng nền tảng dùng chung với mặc định đường lát sẵn cho khóa, vô hiệu hóa, bảo vệ chống giẫm đạp và khả năng quan sát từng tầng, để tỷ lệ trúng, loại bỏ và độ cũ hiển thị ở một nơi và được quản trị đồng đều. Hãy làm cấu hình bộ đệm có thể rà soát như mã nhạy cảm về bảo mật, và coi vô hiệu hóa xuyên vùng là vấn đề thiết kế hạng nhất thay vì sổ tay vận hành của từng đội.

**Chính phủ.** Ràng buộc mua sắm và minh bạch định hình cái bạn có thể lưu đệm và cách bạn chứng minh nó an toàn. Hãy lưu đệm nội dung công khai quyết liệt, hướng dẫn, biểu mẫu và bảng mức phí sau một CDN với TTL dài, để một đợt tăng đột biến hạn nộp hồ sơ được hấp thụ xa nguồn gốc, và lập tài liệu cấu hình đó cho kiểm toán. Các trang đã xác thực hiển thị hồ sơ riêng của một công dân không bao giờ được chạm vào bộ đệm dùng chung, và quy tắc đó nên kiểm chứng được, không chỉ được khẳng định. Ở nơi một CDN hay dịch vụ lưu đệm được mua từ nhà cung cấp, hãy yêu cầu hợp đồng phơi bày các điều khiển bạn cần (đặt khóa, thanh trừ và ghi nhật ký) và tránh khóa chặt sẽ mắc kẹt dữ liệu công sau các định dạng bộ đệm độc quyền.

## Ví dụ

**Công ty khởi nghiệp.** Một ứng dụng tiêu dùng nhỏ chạy danh mục sản phẩm qua một tầng cache-aside được hậu thuẫn bởi một kho trong bộ nhớ, với TTL 60 giây và nhiễu để các mục không hết hạn cùng nhau. Tài sản tĩnh đi tới một CDN với tên tệp có phiên bản và max-age một năm, nên một lần triển khai đổi bảng định kiểu phục vụ một URL mới và không bao giờ cần thanh trừ. Khi một đợt ra mắt trên một podcast nổi tiếng gửi một đợt tăng lưu lượng, hợp nhất single-flight nghĩa là hàng nghìn lần trượt trang chủ đồng thời gây ra một lần đọc cơ sở dữ liệu, không phải hàng nghìn. Những người sáng lập chi gần như không gì cho lưu đệm mà vẫn xử lý được một đợt tăng đột biến lẽ ra đã làm tan cơ sở dữ liệu nhỏ của họ, vì họ đặt một vài bộ đệm được chọn tốt có chủ đích.

**Doanh nghiệp lớn.** Một nhà bán lẻ toàn cầu phục vụ hàng triệu người mua qua một bộ đệm nhiều tầng: một CDN cho hình ảnh và phản hồi API lưu đệm được, một bộ đệm proxy ngược dùng chung ở mỗi vùng, và một bộ đệm ứng dụng cho các mảnh giá và hàng tồn kho đã tính. Khóa bộ đệm được chuẩn hóa và bao gồm tiền tệ, ngôn ngữ và loại thiết bị, nên cá nhân hóa không bao giờ rò rỉ và tỷ lệ trúng giữ cao. Dữ liệu sản phẩm dùng TTL ngắn với vô hiệu hóa hướng sự kiện, nên một thay đổi giá công bố lên một bus thông điệp thanh trừ các khóa bị ảnh hưởng qua các vùng trong vài giây. Mọi tầng báo cáo tỷ lệ trúng, tỷ lệ loại bỏ và độ cũ cho nền tảng quan sát của chương 9.2, và một cảnh báo về tỷ lệ trúng giảm từng bắt được một bộ đệm định cỡ thiếu trước khi nó thành sự cố thanh toán.

**Chính phủ.** Một cơ quan thuế quốc gia chạy một cổng nộp hồ sơ yên ắng phần lớn năm và bị áp đảo gần hạn chót. Đội lưu đệm quyết liệt ở nơi an toàn và không bao giờ ở nơi không. Nội dung công khai (trang hướng dẫn, biểu mẫu, bảng mức thuế) được phục vụ từ một CDN với TTL dài và URL có phiên bản, hấp thụ đợt tăng đọc ngày hạn chót xa nguồn gốc. Các trang đã xác thực hiển thị hồ sơ khai của riêng một công dân được đánh dấu `no-store` và không bao giờ chạm vào bộ đệm dùng chung, nên không người nộp thuế nào bị phục vụ dữ liệu của người khác. Cấu hình bộ đệm được rà soát như mã nhạy cảm về bảo mật theo các thực hành trong chương 4.2, và bảo vệ chống giẫm đạp được kiểm thử tải ở quy mô hạn chót nhiều tháng trước, nên cổng từng sụp vào ngày bận nhất năm nay vững vàng.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của lưu đệm trực tiếp và dễ định lượng một cách bất thường. Một bộ đệm nâng tỷ lệ trúng từ 80 lên 95 phần trăm cắt giảm lưu lượng nguồn gốc ba phần tư, có thể nghĩa là hoãn một lần nâng cấp cơ sở dữ liệu, chạy ít máy chủ ứng dụng hơn, hoặc sống sót qua một đợt tăng lưu lượng lẽ ra đòi hỏi mở rộng khẩn cấp. Cải thiện độ trễ chuyển thành doanh thu trong thương mại và thành sự hài lòng cùng tỷ lệ hoàn thành trong dịch vụ công, nơi nghiên cứu từ lâu đã liên hệ trang nhanh hơn với chuyển đổi cao hơn và bỏ dở thấp hơn. Chi phí đi ra và tính toán giảm vì một yêu cầu được phục vụ từ rìa không bao giờ trả băng thông hay xử lý nguồn gốc. Với các hệ thống nặng đọc, tức hầu hết hệ thống, lưu đệm thường là hiệu năng rẻ nhất bạn có thể mua.

Hãy cân nhắc tổng chi phí sở hữu một cách trung thực. Chi phí trực tiếp là khiêm tốn: hạ tầng CDN và bộ đệm rẻ so với năng lực nguồn gốc chúng tiết kiệm. Chi phí thực là kỷ luật kỹ thuật, vì một bộ đệm sai tệ hơn không có bộ đệm. Lỗi cũ, sai lầm vô hiệu hóa và lỗ hổng đầu độc bộ đệm đều mang chi phí thực, và chúng tăng khi lưu đệm được ứng biến theo từng đội thay vì được cung cấp như một năng lực dùng chung, được kiểm thử tốt. Luận chứng kinh doanh mạnh nhất tài trợ một lượng nhỏ hạ tầng và quy ước lưu đệm dùng chung (khóa chuẩn, vô hiệu hóa, bảo vệ chống giẫm đạp và khả năng quan sát) để mọi đội nhận lợi ích mà không lặp lại sai lầm. Được đóng khung cho ban lãnh đạo, lưu đệm kết nối với các chỉ số họ đã theo dõi: chi phí hạ tầng, độ trễ trang, tỷ lệ chuyển đổi và hoàn thành, và tần suất sự cố trong các sự kiện cao điểm.

## Phản mẫu và cạm bẫy

- **Lưu đệm không có vô hiệu hóa:** đặt TTL dài mà không có cách thanh trừ, nên một giá trị đã sửa vẫn sai hàng giờ.
- **Khóa quá thô:** lưu đệm phản hồi cá nhân hóa dưới khóa dùng chung, làm rò rỉ dữ liệu của người dùng này cho người khác.
- **Khóa quá mịn:** đưa đầu vào dễ biến động vào khóa nên không hai yêu cầu nào từng khớp và tỷ lệ trúng sụp đổ.
- **Không bảo vệ chống giẫm đạp:** một khóa nóng hết hạn dưới tải và mọi yêu cầu đổ xô vào nguồn gốc cùng lúc.
- **Hết hạn đồng bộ:** một lô mục được ghi cùng nhau hết hạn đúng một khoảnh khắc không có nhiễu, gây bầy đàn xô đẩy định kỳ.
- **Lưu đệm dữ liệu riêng tư ở tầng dùng chung:** thiếu `Cache-Control: private` hoặc `no-store`, nên một proxy hay CDN lưu phản hồi đã xác thực.
- **Bỏ qua đầu vào không có khóa:** phản chiếu một tiêu đề vào phần thân phản hồi nhưng bỏ nó khỏi khóa, mở cửa cho đầu độc bộ đệm.
- **Bộ đệm định cỡ thiếu:** một bộ đệm quá nhỏ để giữ tập làm việc đập liên hồi và loại bỏ các mục ngay trước khi chúng được cần.
- **Bộ đệm không đo:** không có chỉ số tỷ lệ trúng hay loại bỏ, nên một bộ đệm suy giảm vô hình cho đến khi nó thành sự cố.
- **Write-back không có độ bền:** ghi nhanh biến mất khi bộ đệm chết trước khi xả, không có bảo đảm hậu thuẫn.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Lưu đệm là tùy nghi và theo từng lập trình viên, được thêm phản ứng khi có gì đó cảm thấy chậm. TTL được đoán, khóa không nhất quán, vô hiệu hóa thủ công hoặc vắng mặt, và dữ liệu cũ cùng lỗi bí ẩn là phổ biến. Không ai theo dõi tỷ lệ trúng, và một đợt tăng lưu lượng mà bộ đệm lẽ ra hấp thụ lại gây ra một sự cố.
- **Mức 2, Phát triển:** Các đội lưu đệm ở những nơi hiển nhiên và dùng CDN cho tài sản tĩnh. TTL cơ bản và cache-aside xuất hiện, nhưng quy ước khác nhau giữa các dịch vụ, vô hiệu hóa không nhất quán, bảo vệ chống giẫm đạp thiếu, quy tắc lưu đệm riêng-so-với-dùng-chung không chính thức, và khả năng quan sát giới hạn ở những lần kiểm tra điểm thỉnh thoảng.
- **Mức 3, Chuẩn hóa:** Một chiến lược lưu đệm được lập tài liệu và thực thi trong toàn tổ chức. Khóa bộ đệm được chuẩn hóa, TTL theo một phân loại độ tươi dùng chung, vô hiệu hóa hướng sự kiện ở nơi quan trọng, bảo vệ chống giẫm đạp và ngữ nghĩa HTTP đúng là tiêu chuẩn, dữ liệu riêng tư không bao giờ được lưu đệm ở các tầng dùng chung, và mọi tầng báo cáo tỷ lệ trúng và loại bỏ cho một đường ống quan sát chung.
- **Mức 4, Quản lý:** Lưu đệm được đo và kiểm soát theo các đường cơ sở. Mỗi tầng có tỷ lệ trúng mục tiêu, ngân sách độ cũ và ngưỡng loại bỏ, và bảng điều khiển cảnh báo khi tỷ lệ trúng giảm hoặc tỷ lệ loại bỏ tăng vượt đường cơ sở. Phòng thủ chống giẫm đạp được kiểm thử tải ở quy mô đỉnh, mức giảm tải nguồn gốc được định lượng theo từng bộ đệm, TTL và chính sách loại bỏ được điều chỉnh từ mẫu truy cập đo được, và cấu hình bộ đệm được rà soát như mã nhạy cảm về bảo mật trước khi phát hành.
- **Mức 5, Điều phối:** Lưu đệm được cải thiện liên tục và tích hợp trong toàn tổ chức. Vị trí, khóa và TTL thích ứng với lưu lượng dịch chuyển, tính toán rìa được dùng ở nơi nó xứng đáng với chỗ đứng, hoạch định năng lực và mô hình chi phí dựa vào chỉ số bộ đệm, và bài học từ sự cố của một đội nuôi quy ước dùng chung. Tổ chức coi lưu đệm là một năng lực được thiết kế, đo đạc và thích ứng thay vì một bộ sưu tập các mẹo cục bộ.

## Ý tưởng để thảo luận

1. Bộ đệm đơn lẻ nào trong hệ thống của bạn, nếu nó nguội ngay bây giờ, sẽ gây nguy hiểm nhiều nhất cho nguồn gốc, và cái gì bảo vệ nó?
2. Với mỗi tầng của hệ thống phân cấp bộ đệm, bạn có thể nêu tỷ lệ trúng hiện tại của nó từ trí nhớ không, và nếu không, điều đó nói gì với bạn?
3. Bạn đã biến một vấn đề vô hiệu hóa thành vấn đề đặt tên bằng khóa có phiên bản ở đâu, và bạn vẫn có thể làm vậy ở đâu?
4. Đường ghi nào của bạn dùng cache-aside, write-through, write-back hay write-around, và mỗi cái có được chọn có chủ đích không?
5. Nếu một kẻ tấn công kiểm soát một tiêu đề yêu cầu, họ có thể đầu độc bất kỳ phản hồi được lưu đệm nào mà người dùng của bạn dùng chung không?
6. Làm sao bạn biết, trong vài phút, rằng tỷ lệ trúng của mình đã lặng lẽ tụt hai mươi điểm?

## Những điểm cần ghi nhớ

- Lưu đệm cắt giảm độ trễ, tải và chi phí, và hệ thống phân cấp bộ đệm (máy khách, CDN và rìa, proxy ngược, ứng dụng, cơ sở dữ liệu) cho phép bạn trả lời càng cao và càng ra ngoài càng tốt trong chừng mực an toàn.
- Vô hiệu hóa là phần khó; hãy thiết kế khóa bộ đệm và TTL có chủ đích, và biến các vấn đề vô hiệu hóa thành vấn đề đặt tên bằng khóa có phiên bản bất cứ khi nào bạn có thể.
- Bảo vệ bộ đệm dưới tải bằng hợp nhất yêu cầu, nhiễu và stale-while-revalidate, vì một bộ đệm được cần nhất đúng lúc một đợt giẫm đạp có thể làm nó vỡ.
- Chọn mẫu ghi và chính sách loại bỏ theo từng khối lượng công việc, và dùng ngữ nghĩa lưu đệm HTTP (`Cache-Control`, ETag, xác thực) một cách tường minh thay vì để các bộ đệm đoán.
- Coi nội dung được lưu đệm là bề mặt tấn công và đo tỷ lệ trúng, loại bỏ và độ cũ, vì một bộ đệm không được quan sát hoặc đặt khóa sai là một khoản nợ ẩn, không phải tài sản.

## Tài liệu tham khảo và đọc thêm

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew S. Tanenbaum và Herbert Bos, *Modern Operating Systems*
- John L. Hennessy và David A. Patterson, *Computer Architecture: A Quantitative Approach*
- Roy T. Fielding và Julian Reschke, "Hypertext Transfer Protocol (HTTP/1.1): Caching," RFC 7234, IETF
- Mark Nottingham, "Caching Tutorial for Web Authors and Webmasters"
- James Kettle, "Practical Web Cache Poisoning," PortSwigger Research
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering: How Google Runs Production Systems*
- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
