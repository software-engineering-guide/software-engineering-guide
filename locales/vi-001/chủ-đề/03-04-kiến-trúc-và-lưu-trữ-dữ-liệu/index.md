# 3.4 Kiến trúc và lưu trữ dữ liệu

## Tổng quan và động lực

Dữ liệu sống lâu hơn mã. Ứng dụng được viết lại sau mỗi vài năm, nhưng dữ liệu chúng quản lý (hồ sơ khách hàng, sổ cái tài chính, lịch sử trợ cấp, hồ sơ sức khỏe) tồn tại hàng thập kỷ. Nó thường là tài sản có giá trị nhất và chịu quy định nhiều nhất của tổ chức. Kiến trúc dữ liệu là kỷ luật quyết định dữ liệu đó được mô hình hóa thế nào, lưu ở đâu, được giữ nhất quán ra sao, tiến hóa thế nào, và được phục vụ đủ nhanh ở quy mô lớn như thế nào. Với một tổ chức lớn, những quyết định này là nền tảng. Lựa chọn công cụ lưu trữ và mô hình dữ liệu của bạn ràng buộc những gì doanh nghiệp có thể làm, nó di chuyển nhanh đến đâu và tốn bao nhiêu, suốt vòng đời của hệ thống.

Rủi ro cao nhất ở doanh nghiệp và chính phủ vì quy mô, tuổi thọ và quy định. Kho giao dịch của một ngân hàng không bao giờ được mất hay đếm đôi một xu. Một sổ đăng ký chính phủ phải lưu giữ hồ sơ theo các thời hạn luật định và chứng minh tính toàn vẹn của chúng với kiểm toán viên. Một hệ thống y tế phải thực thi các quy tắc truy cập chi tiết và nơi lưu trữ dữ liệu. Đồng thời, các tổ chức này phục vụ khối lượng đọc và ghi khổng lồ và không thể để mọi truy vấn đánh vào một [cơ sở dữ liệu quan hệ](https://en.wikipedia.org/wiki/Relational_database) duy nhất. Vì vậy kiến trúc dữ liệu phải dung hòa tính đúng đắn và độ bền với hiệu năng và quy mô, và làm điều đó trong khi lược đồ liên tục thay đổi để đáp ứng các yêu cầu bắt buộc mới.

Chương này bao quát các mô hình lưu trữ chính và khi nào dùng mỗi loại, kỷ luật [lưu trữ đa ngữ](https://en.wikipedia.org/wiki/Polyglot_persistence), mô hình hóa dữ liệu và vấn đề thường bị đánh giá thấp là tiến hóa lược đồ và di chuyển, [bộ nhớ đệm](https://en.wikipedia.org/wiki/Cache_(computing)) và [CDN](https://en.wikipedia.org/wiki/Content_delivery_network) (mạng phân phối nội dung) cùng bài toán vô hiệu hóa nổi tiếng là khó, và cách giao dịch, khóa và đồng thời hành xử khi bạn đẩy chúng đến quy mô lớn. Sợi chỉ xuyên suốt rất đơn giản: không có cơ sở dữ liệu phổ quát. Chỉ có các đánh đổi, và kiến trúc dữ liệu tốt nghĩa là chọn chúng một cách có ý thức, từng khối lượng công việc một.

## Các nguyên tắc chính

- **Mô hình hóa dữ liệu cho khớp với các mẫu truy cập, không phải ngược lại.** Thiết kế lưu trữ quanh cách dữ liệu sẽ được đọc và ghi, không phải quanh một mô hình "đúng" trừu tượng.
- **Không có một cơ sở dữ liệu thống trị tất cả.** Các khối lượng công việc khác nhau muốn các công cụ khác nhau; lưu trữ đa ngữ là bình thường ở quy mô lớn.
- **Tính đúng đắn trước tiên với các hệ thống ghi nhận.** Với dữ liệu có thẩm quyền, độ bền và nhất quán là không thể thương lượng; tối ưu hiệu năng xung quanh chúng, không phải xuyên qua chúng.
- **Lược đồ sẽ thay đổi, vì vậy hãy lên kế hoạch.** Di chuyển là hoạt động kỹ thuật hạng nhất, liên tục, không phải việc làm một lần.
- **Sở hữu dữ liệu của bạn sau một ranh giới dịch vụ.** Mỗi ngữ cảnh giới hạn (một mô hình miền tự chứa với ranh giới tường minh riêng) sở hữu dữ liệu của nó; dùng chung cơ sở dữ liệu ghép các đội và phá hủy quyền tự chủ.
- **Bộ nhớ đệm là một vấn đề đúng đắn trá hình thành một lợi ích hiệu năng.** Mỗi bộ đệm đưa vào rủi ro cũ và vô hiệu hóa; hãy xử lý nó có chủ đích.
- **Phi chuẩn hóa là một đánh đổi, không phải tội lỗi.** Nhân đôi dữ liệu để đọc nhanh là chính đáng nếu bạn chịu trách nhiệm về hệ quả nhất quán.
- **Nhất quán và quy mô đánh đổi lẫn nhau.** Bảo đảm giao dịch càng mạnh thì càng khó phân tán; chỉ mua những gì khối lượng công việc cần.

## Khuyến nghị

### Chọn mô hình lưu trữ từ khối lượng công việc

Hãy khớp mỗi khối lượng công việc với mô hình phù hợp. Cơ sở dữ liệu **quan hệ** cho nhất quán mạnh, phép nối và giao dịch trưởng thành; chúng là mặc định cho các hệ thống ghi nhận và bất cứ thứ gì có quy tắc toàn vẹn phức tạp. Kho **[tài liệu](https://en.wikipedia.org/wiki/Document-oriented_database)** phù hợp với dữ liệu phân cấp, lược đồ linh hoạt được đọc như một đơn vị (cả một đơn hàng, cả một hồ sơ). Kho **[khóa-giá trị](https://en.wikipedia.org/wiki/Key-value_database)** cho tốc độ cực cao cho các tra cứu đơn giản (phiên, cờ tính năng, bộ đệm). Cơ sở dữ liệu **[đồ thị](https://en.wikipedia.org/wiki/Graph_database)** vượt trội ở nơi các mối quan hệ chính là truy vấn (vòng gian lận, sơ đồ tổ chức, quyền hạn, chuỗi cung ứng). Kho **[cột](https://en.wikipedia.org/wiki/Column-oriented_DBMS)** vận hành các truy vấn phân tích quét ít cột trên hàng tỷ hàng (kho dữ liệu, báo cáo). Cơ sở dữ liệu **[chuỗi thời gian](https://en.wikipedia.org/wiki/Time_series_database)** tối ưu cho dữ liệu nặng chỉ-thêm, có dấu thời gian (chỉ số, đo đạc từ xa, cảm biến [Internet vạn vật](https://en.wikipedia.org/wiki/Internet_of_things) (IoT), dữ liệu thị trường). Hãy cưỡng lại việc ép một công cụ làm mọi việc. Dùng cơ sở dữ liệu quan hệ làm hàng đợi, hay kho tài liệu làm sổ cái, là rước đau đớn vào thân.

### Áp dụng lưu trữ đa ngữ một cách có chủ đích

Các hệ thống lớn dùng nhiều kho một cách chính đáng: một hệ thống ghi nhận quan hệ, một chỉ mục tìm kiếm, một bộ đệm, một kho phân tích, và có thể một công cụ đồ thị hoặc chuỗi thời gian. Đây là **lưu trữ đa ngữ**, và là mẫu đúng khi các khối lượng công việc thực sự khác nhau. Chi phí là vận hành, vì giờ bạn có nhiều công cụ hơn để chạy, bảo mật, sao lưu và bố trí nhân sự. Hãy quản lý chi phí đó bằng cách coi mỗi kho là do một dịch vụ sở hữu, chuẩn hóa công cụ vận hành, và giữ số lượng công nghệ ở những cái xứng đáng với chỗ đứng. Hãy đề phòng việc áp dụng một cơ sở dữ liệu mới cho mỗi nhu cầu nhỏ. Mỗi cái là một cam kết vận hành vĩnh viễn.

### Mô hình hóa dữ liệu và coi tiến hóa lược đồ là liên tục

Hãy đầu tư vào mô hình hóa dữ liệu ngay từ đầu cho các hệ thống ghi nhận. Chuẩn hóa để bảo vệ tính toàn vẹn, rồi phi chuẩn hóa có chọn lọc cho các điểm nóng đọc đã được chứng minh. Dù mô hình thế nào, **lược đồ tiến hóa mãi mãi**, vì vậy hãy làm cho di chuyển an toàn và thường lệ. Dùng các tập lệnh di chuyển có phiên bản, tự động, chỉ-tiến được đưa vào quản lý mã nguồn và áp dụng qua đường ống triển khai. Với các thay đổi không thời gian chết trên bảng lớn, hãy dùng mẫu **mở rộng-co lại (thay đổi song song)**: thêm cột hoặc bảng mới, điền bù và ghi kép, di chuyển bên đọc, rồi gỡ bỏ hình dạng cũ. Không bao giờ là một lệnh alter phá vỡ duy nhất. Làm cho thay đổi lược đồ tương thích ngược qua các lần triển khai để mã cũ và mới chạy cùng lúc. Trong các hệ thống event-sourced hoặc dựa trên thông điệp, hãy đánh phiên bản tường minh lược đồ sự kiện và thông điệp của bạn và hỗ trợ nâng cấp sự kiện cũ (biến đổi chúng sang lược đồ hiện tại khi đọc).

### Thiết kế bộ nhớ đệm và vô hiệu hóa với đôi mắt mở

Bộ nhớ đệm và CDN là công cụ hiệu năng có đòn bẩy cao nhất. Một CDN phục vụ nội dung tĩnh và có thể lưu đệm từ rìa gần người dùng, và bộ đệm ứng dụng giúp cơ sở dữ liệu khỏi các lần đọc lặp lại. Nhưng phần khó là vô hiệu hóa: biết khi nào dữ liệu được lưu đệm đã cũ. Hãy chọn một chiến lược cho từng trường hợp. Dùng hết hạn theo thời gian (TTL) ở nơi chấp nhận được độ cũ nhẹ và đơn giản nhất. Dùng vô hiệu hóa tường minh hoặc ghi xuyên suốt ở nơi độ mới quan trọng. Dùng cache-aside ở nơi ứng dụng quản lý việc điền. Đặt TTL có ý thức, bảo vệ chống **giẫm đạp bộ đệm** (nhiều máy khách dựng lại cùng một mục đã hết hạn cùng lúc) bằng khóa hoặc hợp nhất yêu cầu, và ngăn **bầy đàn xô đẩy** trên các bộ đệm lạnh. Không bao giờ lưu đệm dữ liệu mà độ cũ của nó có thể gây ra thất bại về đúng đắn hoặc tuân thủ (quyền hạn, số dư, sự đồng ý) mà không có một đường vô hiệu hóa tường minh, đã được kiểm thử. Hãy coi khóa bộ đệm, TTL và vô hiệu hóa là các sản phẩm được thiết kế, không phải cấu hình ngẫu nhiên.

### Quản lý giao dịch, khóa và đồng thời cho quy mô

Hãy hiểu các mức cô lập và chọn mức yếu nhất vẫn đúng cho từng giao dịch, vì cô lập cao hơn tốn đồng thời. Ưu tiên **[đồng thời lạc quan](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)** (kiểm tra phiên bản khi ghi) cho các khối lượng công việc ít tranh chấp, nặng đọc, và chỉ với tới **khóa bi quan** dưới tranh chấp nóng thực sự, giữ khóa ngắn và có thứ tự nhất quán để tránh bế tắc. Khi mở rộng, một cơ sở dữ liệu ghi được duy nhất trở thành nút thắt. Hãy đưa vào bản sao đọc để mở rộng đọc (chấp nhận độ trễ sao chép), và **[phân mảnh](https://en.wikipedia.org/wiki/Shard_(database_architecture))/phân vùng** theo một khóa phân bố tải đều và giữ dữ liệu liên quan cùng nhau để tránh giao dịch xuyên mảnh. Hãy nhớ rằng phân mảnh đánh đổi việc mất các phép nối xuyên mảnh dễ dàng và các giao dịch [ACID](https://en.wikipedia.org/wiki/ACID) (Tính nguyên tử, Nhất quán, Cô lập, Bền vững) đa mảnh, đó thường là lý do saga và phi chuẩn hóa xuất hiện. Chỉ đưa các kỹ thuật này vào khi khối lượng công việc đòi hỏi. Phân mảnh sớm thêm độ phức tạp vĩnh viễn.

## Đánh đổi: ưu và nhược điểm

| Loại kho | Tốt nhất cho | Điểm mạnh | Điểm yếu |
|---|---|---|---|
| Quan hệ | Hệ thống ghi nhận, toàn vẹn phức tạp | ACID, phép nối, công cụ trưởng thành | Khó mở rộng ghi theo chiều ngang hơn |
| Tài liệu | Đọc tổng hợp, lược đồ linh hoạt | Đọc/ghi cả đối tượng nhanh, linh hoạt | Phép nối/giao dịch xuyên tài liệu yếu |
| Khóa-giá trị | Phiên, bộ đệm, tra cứu đơn giản | Tốc độ và quy mô cực cao | Không truy vấn được ngoài khóa |
| Đồ thị | Truy vấn nặng về quan hệ | Duyệt nhanh, biểu đạt tốt | Kỹ năng vận hành ngách, giới hạn mở rộng |
| Cột | Phân tích, báo cáo | Quét tổng hợp nhanh, nén tốt | Kém cho ghi giao dịch mức hàng |
| Chuỗi thời gian | Chỉ số, đo đạc từ xa, IoT | Thêm và truy vấn thời gian hiệu quả | Mục đích hẹp |

Đánh đổi chủ đạo là nhất quán cùng truy vấn phong phú so với khả năng mở rộng ngang và tốc độ. Các hệ thống quan hệ cho bảo đảm mạnh nhất và truy vấn linh hoạt nhất, nhưng khó nhất để mở rộng ghi qua nhiều máy. Các họ [NoSQL](https://en.wikipedia.org/wiki/NoSQL) (phi quan hệ) nới lỏng phép nối, giao dịch hoặc lược đồ để đạt quy mô và tốc độ. Bộ nhớ đệm đổi độ mới lấy độ trễ. Phân mảnh đổi giao dịch xuyên phân vùng lấy thông lượng ghi. Không cái nào đúng một cách phổ quát. Nghệ thuật là đặt mỗi khối lượng công việc lên điểm trên đường cong mà nhu cầu đúng đắn và hiệu năng của nó thực sự đòi hỏi.

## Câu hỏi để thảo luận với đội của bạn

1. **Với mỗi bộ dữ liệu quan trọng, mọi người có gọi tên được một hệ thống ghi nhận duy nhất không, hay bộ đệm và phép chiếu âm thầm bị coi là sự thật?** Dữ liệu sống lâu hơn mã, và các sự cố dữ liệu gây hại nhất đến từ sự trôi dạt: một bộ đệm, chỉ mục tìm kiếm hay phép chiếu đọc bị nhầm là có thẩm quyền và âm thầm phân kỳ khỏi nguồn thật. Trong một đội lớn điều này xảy ra khi quyền sở hữu mờ nhạt và nhiều dịch vụ ghi các bản sao chồng lấn, nên không ai nói được giá trị nào đúng trong một sự cố. Hãy mang một bản đồ dữ liệu quan trọng của bạn và, với mỗi mục, kho duy nhất có thẩm quyền cộng các bản sao phái sinh phải dựng lại được từ nó. Trong tài chính và chính phủ, chứng minh được bản ghi nào là nguồn pháp lý và dựng lại phần còn lại thường là yêu cầu quy định, không phải sự tiện lợi. Bất cứ thứ gì bạn không thể dựng lại từ hệ thống ghi nhận chính nó là một hệ thống ghi nhận, dù bạn có định thế hay không.

2. **Mỗi công cụ cơ sở dữ liệu trong hệ sinh thái của bạn thực sự tốn bao nhiêu để vận hành, bảo mật và sao lưu, và mỗi cái có còn xứng đáng với chỗ đứng không?** Lưu trữ đa ngữ là đúng khi các khối lượng công việc thực sự khác nhau, nhưng mỗi công cụ là một cam kết vận hành vĩnh viễn: vá lỗi, sao lưu, giám sát, rà soát bảo mật, và nhân sự biết nó lúc 3 giờ sáng. Một tổ chức lớn có thể trôi vào một vườn thú các kho được áp dụng cho từng tính năng, và cái biên thêm chi phí mãi mãi trong khi phục vụ khối lượng công việc mà một kho bạn đã chạy có thể xử lý. Hãy liệt kê mọi công cụ, khối lượng công việc biện minh cho nó, và ai trực ca cho nó, rồi đánh dấu bất kỳ cái nào được áp dụng cho nhu cầu mà một kho chính nay có thể đáp ứng. Việc áp dụng cơ sở dữ liệu mới nên vượt một ngưỡng cao, vì gỡ một cái sau này nghĩa là thêm một đợt di chuyển. Chuẩn hóa công cụ vận hành qua các kho bạn giữ là cách giữ chi phí thấp mà không ép một công cụ làm mọi việc.

3. **Ở đâu một người dùng có thể đọc giá trị cũ từ bản sao ngay sau lần ghi của chính họ, và điều đó có phá vỡ một lời hứa bạn đã đưa ra không?** Bản sao đọc mở rộng đọc nhưng trễ so với bản chính, nên một người dùng cập nhật hồ sơ rồi tải lại ngay có thể thấy giá trị cũ, trông như một lỗi hoặc, với số dư hay cờ đồng ý, một thất bại tuân thủ. Hãy quyết định theo từng luồng xem đọc-ghi-của-chính-mình có quan trọng không, và định tuyến các lần đọc đó đến bản chính hoặc dùng cơ chế nhất quán phiên. Hãy mang danh sách các luồng được phục vụ từ bản sao và đánh dấu luồng nào người dùng hành động ngay sau khi ghi. Với số dư, quyền hạn và sự đồng ý, hãy coi đọc cũ là thất bại về đúng đắn, không phải thẩm mỹ. Điểm chính là mua sự nhất quán mà mỗi khối lượng công việc thực sự cần, và làm cho độ cũ bạn chấp nhận là tường minh thay vì ngẫu nhiên.

4. **Bạn có thể đổi lược đồ của bảng lớn nhất, bận rộn nhất hôm nay mà không có thời gian chết không, và ai thực sự đã diễn tập các bước mở rộng-co lại?** Lược đồ tiến hóa mãi mãi, và thất bại đau nhất là một lệnh alter nổ lớn khóa một bảng khổng lồ, đóng băng dịch vụ và không thể hoàn tác sạch sẽ. Trong một đội lớn rủi ro nhân lên vì nhiều dịch vụ đọc cùng một hình dạng, nên một thay đổi phá vỡ cần mã cũ và mới chạy song song qua một lần triển khai theo giai đoạn. Lực kéo đối lập là tốc độ: một lệnh alter đơn viết nhanh, trong khi mở rộng-co lại (thêm hình dạng mới, điền bù, ghi kép, di chuyển bên đọc, bỏ hình dạng cũ) nhiều bước hơn và cần kiên nhẫn hơn. Hãy mang bảng lớn nhất của bạn, một ước tính trung thực về lệnh alter ngây thơ sẽ khóa nó bao lâu, và một cuộc di chuyển cụ thể mà ai đó đã chạy từ đầu đến cuối trong diễn tập chứ không phải trên lý thuyết. Trong các hệ thống doanh nghiệp và chính phủ chạy liên tục và mang mục tiêu sẵn sàng theo luật định, thời gian chết cho một cuộc di chuyển là vi phạm, nên kỷ luật mở rộng-co lại là cái giá để được phép thay đổi lược đồ.

5. **Những giá trị được lưu đệm hoặc sao chép nào, nếu được phục vụ khi đã cũ, sẽ gây thất bại tuân thủ hoặc an toàn thay vì thẩm mỹ, và mọi đường vô hiệu hóa đó có được kiểm thử không?** Bộ nhớ đệm là một vấn đề đúng đắn mặc trang phục hiệu năng: mối nguy không phải là chậm mà là phục vụ một quyền hạn, số dư, cờ đồng ý hay quyết định truy cập sau khi nó đã thay đổi. Với một tổ chức lớn, mối nguy này phân tán, vì bộ đệm và các tầng rìa tích tụ qua các đội và không ai có thể liệt kê được cái gì được lưu đệm ở đâu hay khi nào nó xóa. Căng thẳng là thật: lưu đệm quyết liệt và TTL dài mua độ trễ và bảo vệ cơ sở dữ liệu, trong khi độ mới nghiêm ngặt tốn cả hai. Hãy mang bản kiểm kê dữ liệu được lưu đệm và phục vụ qua CDN, đánh dấu những mục nào mang hệ quả tuân thủ hoặc an toàn, cùng bằng chứng rằng đường vô hiệu hóa cho từng mục đó đã được thực hành chứ không chỉ cấu hình. Trong bối cảnh chịu quy định và công, một giá trị đồng ý hoặc tư cách cũ là một thất bại có thể kiểm toán, nên các mục đó cần một đường vô hiệu hóa tường minh, đã kiểm thử hoặc không nên được lưu đệm.

6. **Chiến lược lưu giữ, lưu trữ lâu dài và nơi lưu trữ dữ liệu của bạn cho từng kho có thẩm quyền là gì, và bạn có thể chứng minh nó với kiểm toán viên không?** Dữ liệu sống lâu hơn mã và thường lâu hơn cả đội đã viết nó, nên tăng trưởng không giới hạn và các quy tắc nơi lưu trữ mơ hồ âm thầm trở thành vấn đề không ai sở hữu cho đến khi một bảng không quản lý nổi hoặc một bản ghi nằm sai quyền tài phán. Một tổ chức lớn trải rộng nhiều kho và vùng, và các cân nhắc đối lập là chi phí (lưu trữ nóng đắt, nên hãy lưu trữ lâu dài và phân tầng), hiệu năng (bảng phình to làm chậm mọi thứ), và nghĩa vụ pháp lý (sàn lưu giữ luật định và trần nơi lưu trữ có thể xung đột). Hãy mang, cho mỗi bộ dữ liệu có thẩm quyền, thời hạn lưu giữ, nơi dữ liệu thực sự cư trú, cơ chế lưu trữ lâu dài và xóa, và tên người chịu trách nhiệm. Với các hệ thống doanh nghiệp và đặc biệt là chính phủ, lưu giữ và nơi lưu trữ thường là các yêu cầu pháp lý với đòi hỏi kiểm toán và chủ quyền, nên chứng minh được mỗi bản ghi nằm đâu, được giữ bao lâu, và khi nào bị hủy là giấy phép hoạt động, không phải điều dễ chịu.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Chạy một cơ sở dữ liệu và cưỡng lại vườn thú. Một kho quan hệ được quản lý duy nhất cho bạn giao dịch, một thứ để sao lưu, và một nơi để suy luận về nhất quán, đúng là thứ một đội ba người có thể giữ trong đầu. Chỉ thêm bộ đệm, bản sao đọc hay chỉ mục tìm kiếm khi một truy vấn chậm cụ thể hoặc khối lượng đọc thực sự buộc phải thế, để độ phức tạp đến cùng một lý do trả tiền. Hãy giữ di chuyển có phiên bản từ ngày đầu, vì áp kỷ luật di chuyển vào một sản phẩm đang chạy khó hơn nhiều so với bắt đầu với nó.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia cơ sở dữ liệu và không có thời gian vận hành nhiều công cụ, vì vậy hãy ưu tiên một kho được quản lý và để nhà cung cấp nền tảng xử lý sao lưu, vá lỗi và sao chép. Coi việc chọn kho là một quyết định mua: chọn công cụ nhàm chán, được hỗ trợ tốt mà các công cụ của bạn đã tích hợp thay vì công cụ nhanh nhất trong một bài đo hiệu năng. Đặt một chính sách lưu giữ và sao lưu đơn giản mà bạn thực sự xác minh được, và không bao giờ lưu đệm bất cứ thứ gì gắn với tiền hay quyền hạn mà không có cách xóa rõ ràng, vì một mức giá hay quyền hạn cũ khiến bạn mất khách hàng.

**Doanh nghiệp lớn.** Thách thức cốt lõi là lưu trữ đa ngữ qua nhiều đội: một hệ thống ghi nhận quan hệ cộng tìm kiếm, bộ đệm, kho dữ liệu, và có thể đồ thị hoặc chuỗi thời gian, mỗi cái do một dịch vụ sở hữu thay vì dùng chung. Hãy chuẩn hóa công cụ vận hành, sao lưu và giám sát qua các kho bạn giữ, giữ việc áp dụng công cụ mới ở ngưỡng cao, và biến di chuyển mở rộng-co lại cùng vô hiệu hóa bộ đệm tường minh thành mặc định. Quản lý hệ sinh thái như một danh mục với quyền sở hữu dữ liệu rõ ràng, để không công cụ nào sống lâu hơn khối lượng công việc đã biện minh cho nó và không đội nào bị ghép qua cơ sở dữ liệu dùng chung.

**Chính phủ.** Nơi lưu trữ dữ liệu, lưu giữ luật định và tính toàn vẹn chứng minh được định hình mọi lựa chọn. Hãy cung cấp mọi kho ở các vùng có chủ quyền, cấu hình CDN chỉ lưu đệm dữ liệu không cá nhân, và giữ lịch sử kiểm toán bất biến cho các bản ghi phải dựng lại được cho cơ quan quản lý. Các cuộc di chuyển do luật mới bắt buộc phải được áp dụng tương thích ngược qua đường ống để dịch vụ vẫn khả dụng qua các hạn chót lập pháp, và hệ thống ghi nhận phải xác định được để bạn chứng minh giá trị nào là nguồn pháp lý và dựng lại mọi bản sao phái sinh từ nó.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp giai đoạn hạt giống chạy mọi thứ trên một thể hiện PostgreSQL được quản lý duy nhất và cưỡng lại ham muốn thêm công cụ tìm kiếm, bộ đệm và kho dữ liệu riêng trước khi cần. Một cơ sở dữ liệu nghĩa là một thứ để sao lưu, một nơi để suy luận về nhất quán, và giao dịch hoạt động đúng, điều quan trọng khi cả đội chỉ có ba kỹ sư. Họ chỉ thêm bộ đệm Redis và một bản sao đọc khi một truy vấn chậm cụ thể và khối lượng đọc thực sự biện minh cho nó, để độ phức tạp đến cùng một lý do trả tiền thay vì đến trước nó.

**Doanh nghiệp lớn.** Một ngân hàng bán lẻ giữ sổ cái có thẩm quyền trong cơ sở dữ liệu quan hệ nhất quán mạnh: mỗi bút toán là một giao dịch ACID đúng nghĩa, được phân mảnh theo dải tài khoản để mở rộng ghi. Xung quanh là một hệ sinh thái đa ngữ: một chỉ mục tìm kiếm để tra cứu khách hàng, một bộ đệm Redis (ghi xuyên suốt, TTL ngắn) cho tóm tắt tài khoản trên ứng dụng di động, một kho dữ liệu cột cho báo cáo quy định và phân tích, và một cơ sở dữ liệu đồ thị để phát hiện gian lận mạng giao dịch. Thay đổi lược đồ cho sổ cái dùng mở rộng-co lại với ghi kép để hệ thống 24/7 không bao giờ ngừng hoạt động vì một cuộc di chuyển.

**Chính phủ.** Một cơ quan đăng ký phương tiện quốc gia lưu hồ sơ có thẩm quyền trong một hệ thống ghi nhận quan hệ với lưu giữ luật định và lịch sử kiểm toán đầy đủ. Các tra cứu "kiểm tra một phương tiện" hướng đến công chúng được phục vụ từ một bản sao đọc và một bộ đệm rìa với TTL ngắn, vì dữ liệu công khai hơi cũ là chấp nhận được và khối lượng đọc vượt xa ghi. Luật về nơi lưu trữ dữ liệu yêu cầu mọi bản ghi ở lại trong nước, nên mọi kho được cung cấp trong các vùng có chủ quyền và CDN được cấu hình chỉ lưu đệm dữ liệu không cá nhân. Các cuộc di chuyển để thêm trường mới do chính sách giao thông bắt buộc được áp dụng tương thích ngược qua đường ống để dịch vụ vẫn khả dụng trong các hạn chót lập pháp.

## Luận chứng kinh doanh: động lực, ROI và TCO

Các quyết định kiến trúc dữ liệu có một trong những cái đuôi chi phí dài nhất và lớn nhất trong phần mềm, vì dữ liệu và lược đồ của nó là những thứ khó thay đổi nhất khi các hệ thống và tích hợp đã phụ thuộc vào chúng. Chi phí áp dụng thực hành tốt (chọn kho có chủ đích, di chuyển có kỷ luật, lưu đệm được thiết kế, và phân mảnh phù hợp) chủ yếu là thời gian kỹ sư cấp cao và một ít công cụ vận hành bổ sung. Chi phí của việc *không* áp dụng hiện ra là một cơ sở dữ liệu quá tải làm nghẹt cả doanh nghiệp, tái nền tảng khẩn cấp khi kho sai được phát hiện quá muộn, các sự cố kéo dài do di chuyển hỏng, và gây hại nhất là hỏng dữ liệu hoặc vi phạm tuân thủ từ một bộ đệm vô hiệu hóa sai hoặc một giao dịch bị mất.

Hãy trình bày lập luận với ban lãnh đạo bằng khoảng dư mở rộng, rủi ro sự cố và mức độ phơi nhiễm quy định. Lựa chọn lưu trữ đúng là thứ cho phép doanh nghiệp tăng khối lượng đọc và ghi mà không phải viết lại. Di chuyển có kỷ luật là thứ cho phép lược đồ theo kịp các yêu cầu mới mà không có thời gian chết. Lưu đệm đúng là thứ mang lại trải nghiệm người dùng nhanh mà không có lỗi cũ âm thầm. Hãy định lượng TCO qua vòng đời hệ thống. Một kiến trúc dữ liệu được chọn tốt tránh chi phí lặp lại của việc xoay xở quanh một kiến trúc tồi, và một sự cố hỏng dữ liệu được ngăn chặn thường vượt xa toàn bộ chi phí làm tốt. Trong các lĩnh vực chịu quy định, khả năng chứng minh tính toàn vẹn và nơi lưu trữ dữ liệu không phải trung tâm chi phí mà là giấy phép hoạt động.

## Phản mẫu và cạm bẫy

- **Cơ sở dữ liệu dùng chung qua các dịch vụ.** Nhiều dịch vụ đọc và ghi một lược đồ, ghép các đội và biến mọi thay đổi thành khủng hoảng phối hợp.
- **Một cơ sở dữ liệu cho mọi thứ.** Ép phân tích, hàng đợi, tìm kiếm và giao dịch vào một công cụ quan hệ duy nhất cho đến khi nó sụp đổ.
- **Di chuyển nổ lớn.** Thay đổi lược đồ phá vỡ đơn lẻ đòi hỏi thời gian chết và không thể hoàn tác an toàn.
- **Lưu đệm không có chiến lược vô hiệu hóa.** Dữ liệu cũ được phục vụ vô thời hạn, hoặc lỗi đúng đắn vì không ai sở hữu khi nào bộ đệm xóa.
- **Phân mảnh sớm.** Phân tán dữ liệu trước khi tải đòi hỏi, mất vĩnh viễn phép nối và giao dịch mà không có lợi ích.
- **Bỏ qua độ trễ sao chép.** Đọc lần ghi của chính mình từ bản sao đang trễ và nhận dữ liệu cũ, phá vỡ kỳ vọng người dùng.
- **Tăng trưởng dữ liệu không giới hạn.** Không có chiến lược lưu trữ lâu dài hay lưu giữ, nên bảng lớn dần cho đến khi hiệu năng và chi phí không thể chịu nổi.
- **Lưu dữ liệu phái sinh như sự thật.** Coi một bộ đệm, chỉ mục hay phép chiếu là hệ thống ghi nhận, rồi phát hiện nó đã trôi dạt.

## Mô hình trưởng thành

- **Mức 1: Khởi đầu.** Một cơ sở dữ liệu được dùng cho mọi mục đích. Thay đổi lược đồ thủ công và tùy nghi, không có kỷ luật di chuyển. Lưu đệm là ngẫu nhiên và vô hiệu hóa là chuyện nghĩ sau. Vấn đề hiệu năng được giải quyết phản ứng bằng cách mua máy lớn hơn, và không ai gọi tên đáng tin cậy được hệ thống ghi nhận cho một bộ dữ liệu nhất định.
- **Mức 2: Phát triển.** Một số lựa chọn lưu trữ có chủ đích và một bộ đệm hoặc kho dữ liệu đã xuất hiện, nhưng thực hành khác nhau theo đội. Di chuyển có phiên bản nhưng đôi khi đòi hỏi thời gian chết, và mở rộng-co lại được dùng bởi ai tình cờ biết nó. Nhiều dịch vụ vẫn dùng chung cơ sở dữ liệu, và chiến lược lưu đệm khác nhau từ đội này sang đội khác.
- **Mức 3: Chuẩn hóa.** Lưu trữ đa ngữ được khớp với khối lượng công việc, mỗi kho do một dịch vụ sở hữu và không bao giờ dùng chung. Di chuyển mở rộng-co lại tự động, tương thích ngược, không thời gian chết là tiêu chuẩn có tài liệu, được thực thi toàn tổ chức. Chiến lược lưu đệm, TTL và đường vô hiệu hóa là các sản phẩm thiết kế tường minh, và hệ thống ghi nhận duy nhất cho mỗi bộ dữ liệu được lập tài liệu, với các bản sao phái sinh dựng lại được từ nó.
- **Mức 4: Quản lý.** Hệ sinh thái dữ liệu được đo và kiểm soát theo các đường cơ sở. Bạn theo dõi thời lượng di chuyển và tỷ lệ hoàn tác, độ trễ sao chép so với yêu cầu đọc-ghi-của-chính-mình, tỷ lệ trúng bộ đệm và sự cố dữ liệu cũ, chi phí vận hành từng kho, và độ trễ truy vấn ở các phân vị mục tiêu, rồi hành động theo các con số. Lưu giữ và nơi lưu trữ được kiểm toán theo yêu cầu luật định, tính đúng của dữ liệu phái sinh được xác minh liên tục, và mọi công cụ phải biện minh chi phí so với khối lượng công việc nó phục vụ.
- **Mức 5: Điều phối.** Kiến trúc dữ liệu được cải thiện liên tục và tích hợp với hoạch định năng lực, chi phí và rủi ro trong toàn tổ chức. Các lựa chọn phân mảnh, lưu đệm và nhất quán được cân bằng lại theo từng khối lượng công việc khi mẫu truy cập và chi phí dịch chuyển, và các kho không còn xứng đáng với chỗ đứng được loại bỏ qua các cuộc di chuyển có kế hoạch. Tiến hóa lược đồ, lưu trữ lâu dài và nơi lưu trữ được tự động hóa hoàn toàn và thích ứng, để hệ sinh thái tự định hình lại theo yêu cầu mới và tải mà không cần tái nền tảng khẩn cấp.

## Ý tưởng để thảo luận

1. Kho nào hiện tại của bạn đang làm công việc chúng không được thiết kế cho, và công cụ đúng sẽ là gì?
2. Bạn có thể thực hiện thay đổi lược đồ trên bảng lớn nhất của mình hôm nay với không thời gian chết không? Nếu không, vì sao?
3. Hệ thống của bạn lưu đệm dữ liệu ở đâu mà độ cũ của nó có thể gây thất bại về tuân thủ hoặc đúng đắn?
4. Dịch vụ nào dùng chung cơ sở dữ liệu, và cần gì để cho mỗi dịch vụ cơ sở dữ liệu riêng?
5. Ở đâu một cơ sở dữ liệu ghi được duy nhất là trần mở rộng của bạn, và sao chép đọc hay phân mảnh là bước tiếp theo đúng?
6. Chiến lược lưu giữ và lưu trữ lâu dài của bạn là gì, và ai chịu trách nhiệm về nó?

## Những điểm cần ghi nhớ

- Dữ liệu sống lâu hơn mã; các quyết định lưu trữ và mô hình hóa ràng buộc doanh nghiệp suốt vòng đời hệ thống.
- Khớp mỗi khối lượng công việc với mô hình lưu trữ phù hợp với mẫu truy cập của nó; kỳ vọng lưu trữ đa ngữ ở quy mô lớn.
- Cho mỗi dịch vụ quyền sở hữu dữ liệu của nó; không bao giờ ghép các đội qua cơ sở dữ liệu dùng chung.
- Coi tiến hóa lược đồ là liên tục và dùng các di chuyển mở rộng-co lại tương thích ngược, không thời gian chết.
- Bộ nhớ đệm là vấn đề đúng đắn: thiết kế TTL, vô hiệu hóa và bảo vệ chống giẫm đạp có chủ đích, và không bao giờ lưu đệm dữ liệu quan trọng với tuân thủ mà không có đường vô hiệu hóa đã kiểm thử.
- Chỉ mua nhất quán và bảo đảm giao dịch mà mỗi khối lượng công việc cần; phân mảnh và sao chép đổi giao dịch xuyên phân vùng lấy quy mô.

## Tài liệu tham khảo và đọc thêm

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Pramod Sadalage và Martin Fowler, *NoSQL Distilled*
- Pramod Sadalage và Scott Ambler, *Refactoring Databases: Evolutionary Database Design*
- C. J. Date, *An Introduction to Database Systems*
- Joe Celko, *SQL for Smarties*
- Vlad Mihalcea, *High-Performance Java Persistence* (giao dịch, cô lập, đồng thời)
- Eric Evans, *Domain-Driven Design* (ngữ cảnh giới hạn và quyền sở hữu dữ liệu)
- Werner Vogels, "Eventually Consistent"
