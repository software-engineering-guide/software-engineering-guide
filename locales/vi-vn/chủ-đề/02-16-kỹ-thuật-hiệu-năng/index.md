# 2.16 Kỹ thuật hiệu năng

## Tổng quan và động lực

Kỹ thuật hiệu năng là nghề thủ công làm cho mã đủ nhanh, một cách có chủ đích, bằng đo lường thay vì trực giác. Chương này làm việc ở cấp độ mã và thành phần: hàm, vòng lặp, cấu trúc dữ liệu, truy vấn, cấp phát bộ nhớ, và cách một dịch vụ đơn lẻ tiêu tốn thời gian của nó. Nó là chương bạn đồng hành của chương 3.5, vốn xử lý hiệu năng ở cấp hệ thống (mở rộng ra, cân bằng tải, năng lực và khả năng phục hồi). Khi một hệ thống chậm, chương 3.5 hỏi bạn cần bao nhiêu máy; chương này hỏi vì sao một máy lại làm nhiều việc đến vậy ngay từ đầu. Bạn thường sẽ cần cả hai, và góc nhìn cấp mã là nơi một lượng chi phí và độ trễ đáng ngạc nhiên thực sự ẩn náu.

Với các đội lớn, kỷ luật này quan trọng vì hiệu năng phân rã một cách lặng lẽ. Không commit đơn lẻ nào làm một dịch vụ chậm, nhưng một nghìn commit nhỏ, mỗi cái thêm một lệnh gọi cơ sở dữ liệu hay một vòng lặp không giới hạn, sẽ làm vậy. Không có phương pháp chung để đo, lập ngân sách và đặt cổng cho hiệu năng, bạn chỉ phát hiện sự mục nát khi một khách hàng phàn nàn hoặc một lần ra mắt tan chảy. Một phương pháp biến hiệu năng từ một cuộc chữa cháy anh hùng thành một thuộc tính thường lệ mà bạn bảo vệ.

Với các doanh nghiệp, hiệu năng là tiền: mã nhanh hơn nghĩa là ít máy hơn, hóa đơn đám mây thấp hơn, và khả năng đáp ứng một [thỏa thuận mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) về độ trễ mà không cấp phát dư thừa. Với chính phủ, hiệu năng là sự tiếp cận: một trang tải được trên một chiếc điện thoại cũ qua kết nối di động yếu là sự khác biệt giữa một công dân hoàn thành yêu cầu trợ cấp và bỏ cuộc. Các hệ thống công cũng cần bằng chứng điểm chuẩn tái tạo được, vì mua sắm và cơ quan giám sát sẽ yêu cầu bạn chứng minh các con số, không chỉ khẳng định.

## Các nguyên tắc chính

- **Đo trước khi tối ưu.** Nút thắt hầu như không bao giờ nằm ở nơi bạn đoán. Hãy lập hồ sơ hiệu năng, rồi mới hành động.
- **Tránh tối ưu hóa sớm.** Lời cảnh báo của Donald Knuth vẫn đúng: tối ưu hóa mã không quan trọng tốn sự rõ ràng và không mua được gì.
- **Xác định "đủ nhanh" bằng một con số.** Một ngân sách hiệu năng với mục tiêu và phân vị biến ý kiến thành đạt hoặc không đạt.
- **Trung bình nói dối; phân vị nói sự thật.** Cái đuôi (p99) là thứ người dùng cảm nhận, không phải giá trị trung bình.
- **Chiến thắng về thuật toán thắng chỉnh vi mô.** Một lớp độ phức tạp tốt hơn vượt mọi sự khéo léo về hằng số.
- **Độ trễ và thông lượng là những mục tiêu khác nhau.** Cải thiện cái này có thể làm cái kia xấu đi; hãy biết bạn đang mua cái gì.
- **Đo điểm chuẩn trung thực hoặc đừng làm.** Khởi động, phương sai và khối lượng công việc đại diện phân biệt số liệu thật với hư cấu.
- **Đặt cổng hiệu năng trong CI, theo dõi nó trên môi trường thực.** Hồi quy bị bắt trước khi hợp nhất thì rẻ; bị người dùng bắt thì đắt.

## Khuyến nghị

### Đo trước, và lập hồ sơ hiệu năng trước khi chạm vào một dòng

Quy tắc cổ nhất trong lĩnh vực này là quy tắc bị phớt lờ nhiều nhất: tìm nút thắt trước khi bạn tối ưu. Hãy với tới một [trình lập hồ sơ hiệu năng](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), một công cụ lấy mẫu hoặc trang bị một chương trình đang chạy để cho thấy nó tiêu tốn thời gian và bộ nhớ ở đâu. Lập hồ sơ CPU (hàm nào đốt chu kỳ), bộ nhớ và cấp phát (cái gì được cấp phát và thường xuyên đến đâu, vì sự xáo trộn cấp phát gây ra các khoảng dừng thu gom rác), và I/O (thời gian chờ đĩa, mạng hoặc cơ sở dữ liệu). Một [biểu đồ ngọn lửa](https://en.wikipedia.org/wiki/Flame_graph), một hình ảnh trực quan xếp chồng trong đó mỗi ô là một hàm và độ rộng của nó là thời gian tiêu tốn, làm cho chi phí chi phối hiện rõ chỉ trong nháy mắt: hãy tìm các ô rộng nhất, không phải các ngăn xếp sâu nhất. Tối ưu hóa chi phí lớn nhất trước, đo lại, và dừng khi bạn đạt ngân sách. Điều này kết nối với các thực hành về khả năng quan sát của chương 9.2, vì một hồ sơ hiệu năng trên môi trường thực thắng mọi phỏng đoán từ laptop.

Cũng hãy đề phòng sai lầm ngược lại. Câu đầy đủ của Knuth là tối ưu hóa sớm là gốc rễ của nhiều điều xấu, và ông muốn nói đến những sự kém hiệu quả nhỏ cám dỗ bạn hy sinh mã dễ đọc cho tốc độ tưởng tượng. Hãy viết phiên bản rõ ràng trước, đo, và chỉ tối ưu hóa mã mà trình lập hồ sơ buộc tội.

### Xác định "đủ nhanh" nghĩa là gì bằng ngân sách hiệu năng

Tốc độ không phải đức tính trong trừu tượng; nó là mục tiêu bạn hoặc đạt hoặc trượt. Hãy đặt một **ngân sách hiệu năng**: một giới hạn cụ thể như "độ trễ thanh toán p99 dưới 300 ms" hoặc "điểm cuối này cấp phát dưới 1 MB mỗi yêu cầu". Gắn nó với thứ người dùng hoặc doanh nghiệp cảm nhận, và diễn đạt nó dưới dạng **phân vị**, không phải trung bình, vì giá trị trung bình che giấu cái đuôi chậm nơi người dùng thực sống. Nếu 1% yêu cầu mất 5 giây, trung bình của bạn có thể trông ổn trong khi một lát đáng kể khách hàng chịu khổ. Ngân sách cho một đội một định nghĩa hoàn thành chung, không thể tranh cãi và một lằn ranh mà hồi quy vượt qua một cách rõ ràng.

### Với tới hiệu quả thuật toán trước khi chỉnh vi mô

Những chiến thắng lớn nhất, rẻ nhất đến từ [hiệu quả thuật toán](https://en.wikipedia.org/wiki/Algorithmic_efficiency), công việc tăng thế nào khi đầu vào tăng, được mô tả bằng [ký hiệu Big O](https://en.wikipedia.org/wiki/Big_O_notation) (một cách phân loại tốc độ tăng trưởng, để một phép sắp xếp O(n log n) mở rộng tốt hơn nhiều so với O(n bình phương)). Một vòng lặp lồng nhau vô hình ở mười phần tử trở thành thảm họa ở mười nghìn. Trước khi bạn chỉnh tay một hàm nóng, hãy hỏi liệu nó có đang làm về cơ bản quá nhiều việc không: một truy vấn N+1 vô tình, một lần quét tuyến tính lẽ ra là tra cứu bảng băm, hoặc công việc lặp lại có thể ghi nhớ. Điều này liên kết với nền tảng thuật toán trong chương 2.13. Không lượng chỉnh hằng số nào cứu được lớp độ phức tạp sai.

### Phân biệt độ trễ với thông lượng, và tôn trọng cái đuôi

**Độ trễ** là thời gian một thao tác kéo dài; **thông lượng** là số thao tác hoàn thành trong một đơn vị thời gian. Chúng không phải cùng một mục tiêu, và tối ưu hóa cái này có thể hại cái kia. Gom lô cải thiện thông lượng nhưng thêm độ trễ cho phần tử đầu tiên trong lô; thêm các worker song song tăng thông lượng nhưng có thể làm tệ độ trễ đuôi do tranh chấp. Hãy quyết định người dùng của bạn thực sự cần cái nào. Và luôn theo dõi cái đuôi: độ trễ p95 và p99, 5% và 1% yêu cầu chậm nhất, vì ở quy mô lớn một người dùng thực hiện nhiều yêu cầu và gặp cái đuôi thường xuyên. Hãy báo cáo phân vị, cảnh báo trên chúng, và lập ngân sách cho chúng.

### Biết giới hạn của song song hóa

Khi bạn song song hóa, hãy nhớ [định luật Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): mức tăng tốc từ việc thêm bộ xử lý bị giới hạn bởi phần công việc phải chạy tuần tự. Nếu 10% một công việc vốn mang tính tuần tự, không số lõi nào đưa bạn vượt qua mức tăng tốc 10 lần. Đồng thời (cấu trúc công việc để các nhiệm vụ có thể tiến triển độc lập) và song song (thực sự thực thi chúng cùng lúc) thêm độ phức tạp thực, từ điều kiện chạy đua đến chi phí điều phối. Hãy đo phần tuần tự trước khi bạn cho rằng thêm luồng sẽ cứu bạn, và hãy thành thật rằng phiên bản đúng đơn giản nhất thường đã đủ nhanh.

### Dùng bộ nhớ đệm và tính cục bộ dữ liệu, và tôn trọng chi phí của chúng

Một [bộ nhớ đệm](https://en.wikipedia.org/wiki/Cache_(computing)), một kho nhanh các kết quả được tính gần đây hoặc tốn kém, là công cụ hiệu năng mạnh nhất bạn có và cũng nguy hiểm nhất. Câu đùa của Phil Karlton rằng hai vấn đề khó trong khoa học máy tính là vô hiệu hóa bộ nhớ đệm và đặt tên là một lời cảnh báo: một bộ nhớ đệm lỗi thời phục vụ câu trả lời sai, và logic vô hiệu hóa là nơi các lỗi tinh vi sinh sôi. Hãy lưu đệm có chủ đích, đặt thời hạn, và biết câu chuyện về tính đúng đắn của bạn trước khi tối ưu tỷ lệ trúng. Ở mức thấp nhất, [tính cục bộ tham chiếu](https://en.wikipedia.org/wiki/Locality_of_reference), giữ dữ liệu được dùng cùng nhau gần nhau trong bộ nhớ, khai thác phân cấp bộ nhớ đệm CPU và có thể làm mã nhanh gấp nhiều lần mà không cần thay đổi thuật toán, bằng cách biến trượt bộ nhớ đệm thành trúng. Các mảng liên tục thắng các cấu trúc đuổi theo con trỏ vì lý do này. Điều này giao với các lựa chọn bố cục dữ liệu trong chương 3.4.

### Đo điểm chuẩn trung thực và nghi ngờ các vi điểm chuẩn

Một điểm chuẩn nói dối còn tệ hơn không có, vì nó mang lại sự tự tin sai. Hãy khởi động trước khi đo, để bạn đo hành vi trạng thái ổn định thay vì khởi động một lần và biên dịch đúng lúc. Chạy nhiều lần lặp và báo cáo phương sai, không phải một con số may mắn duy nhất. Dùng khối lượng công việc đại diện với kích thước và phân phối dữ liệu thực tế, vì một vi điểm chuẩn trên đầu vào đồ chơi thường đo khả năng của trình biên dịch xóa bài kiểm thử của bạn chứ không phải tốc độ thực của mã. Hãy coi chừng các cạm bẫy kinh điển: một giá trị mà bộ tối ưu chứng minh không dùng và xóa đi, một vòng lặp mà môi trường chạy nhấc ra ngoài, hoặc một bộ nhớ đệm nóng trong điểm chuẩn và lạnh trên môi trường thực. Khi nghi ngờ, hãy đo toàn bộ đường đi, không phải hàm bị cô lập.

### Đặt cổng hiệu năng trong CI và theo dõi nó trên môi trường thực

Hãy biến hiệu năng thành thuộc tính mà đường ống bảo vệ. Thêm các bài kiểm thử hiệu năng vào chiến lược của chương 2.4, với các cổng hồi quy làm hỏng bản dựng khi một điểm chuẩn hoặc ngân sách chính xấu đi vượt ngưỡng. Điều này bắt sự len lỏi chậm chạp trước khi nó hợp nhất. Rồi khép vòng trên môi trường thực với đo đạc từ xa của chương 9.2: theo dõi các phân vị độ trễ thực, tỷ lệ cấp phát, và truy vấn chậm đối chiếu với ngân sách của bạn, vì lưu lượng môi trường thực tìm ra những trường hợp mà điểm chuẩn của bạn chưa bao giờ hình dung.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Tối ưu ngay, dựa trên trực giác | Có cảm giác năng suất; thỉnh thoảng thắng may mắn | Thường chỉnh sai mã; thêm độ phức tạp mà không có lợi ích |
| Đo trước, rồi tối ưu | Nhắm vào nút thắt thực; dựa trên bằng chứng | Cần công cụ và kỷ luật; bắt đầu chậm hơn |
| Lưu đệm | Lợi ích lớn về độ trễ và thông lượng | Lỗi vô hiệu hóa; dữ liệu lỗi thời; chi phí bộ nhớ |
| Nhiều song song hơn | Thông lượng cao hơn trên công việc song song | Trần Amdahl; tranh chấp; lỗi đồng thời |
| Tối ưu vi mô | Vắt các hằng số | Trần thấp; hại khả năng đọc; thường là nhiễu |
| Cải thiện thuật toán | Lợi ích tăng theo kích thước đầu vào | Cần phân tích; đôi khi là viết lại lớn hơn |
| Cổng hiệu năng trong CI | Ngăn hồi quy sớm và rẻ | Điểm chuẩn chập chờn làm xói mòn niềm tin; cần môi trường ổn định |

Căng thẳng trung tâm là công sức so với lợi ích, và lời giải là đo lường. Công việc hiệu năng có lợi suất giảm dần mạnh: bản sửa dẫn dắt bởi hồ sơ đầu tiên có thể giảm một nửa độ trễ, bản thứ mười có thể cắt một phần trăm trong khi nhân đôi độ phức tạp của mã. Bạn giải quyết nó bằng cách từ chối tối ưu hóa mà không có một con số trong tay và một ngân sách để đạt. Hãy đo để tìm bản sửa đáng làm, và dừng ngay khi bạn vượt ngân sách thay vì chạy theo tốc độ vì chính nó.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn có ngân sách hiệu năng bằng văn bản cho các đường quan trọng của mình không, và nó có được diễn đạt dưới dạng phân vị không?** Nhiều đội có cảm giác mơ hồ rằng mọi thứ nên "nhanh" nhưng không có con số nào ai đó có thể làm trượt, nghĩa là hiệu năng không phải việc của ai cho đến khi nó hỏng. Một ngân sách như "p99 dưới 300 ms" làm mục tiêu cụ thể, cho người đánh giá thứ để thực thi, và biến một hồi quy thành một sự kiện hiển thị thay vì một cú trượt chậm. Nó quan trọng nhất trong các đội lớn, nơi độ trễ len lỏi qua nhiều bàn tay và không tác giả đơn lẻ nào thấy chi phí tích lũy. Hãy mang dữ liệu độ trễ hiện tại của bạn và hỏi bạn đang báo cáo trung bình, vốn tâng bốc bạn, hay phân vị, vốn nói sự thật. Nếu bạn không thể nói "đủ nhanh" nghĩa là gì dưới dạng một con số, đó là điều đầu tiên cần sửa.

2. **Lần cuối bạn tối ưu hóa một thứ gì, một trình lập hồ sơ đã cho bạn biết nơi cần nhìn, hay bạn đoán?** Nút thắt nổi tiếng là nằm ở nơi khác với nơi các kỹ sư có kinh nghiệm mong đợi, và thời gian dành để chỉnh sai mã là thời gian mất hai lần, một lần trong công việc và một lần trong độ phức tạp thêm vào. Một văn hóa lập hồ sơ trước dành công sức ở nơi nó hoàn vốn và để mã rõ ràng yên. Hãy nhờ đội bạn nhớ lại ba bản sửa hiệu năng gần nhất và liệu mỗi bản có bắt đầu từ một phép đo hay một linh cảm. Hãy cân nhắc liệu bạn có thể lập hồ sơ trên môi trường thực, hoặc một môi trường dàn dựng thực tế, vì hồ sơ từ laptop có thể gây hiểu lầm nghiêm trọng. Câu trả lời tiết lộ công việc hiệu năng của bạn là kỹ thuật hay truyền miệng.

3. **Điều gì ngăn một hồi quy hiệu năng đến được môi trường thực hôm nay?** Trong một đội đang lớn, câu trả lời trung thực thường là "một lời phàn nàn của khách hàng", nghĩa là người dùng là bài kiểm thử hồi quy của bạn. Một cổng CI làm hỏng bản dựng khi một điểm chuẩn hoặc ngân sách xấu đi bắt vấn đề khi nó còn rẻ để sửa và tác giả vẫn nhớ thay đổi. Hãy thảo luận liệu các điểm chuẩn của bạn có đủ ổn định để đặt cổng không, vì một bài kiểm thử hiệu năng chập chờn kêu sói sẽ bị bỏ qua hoặc tắt. Hãy nói về những gì bạn theo dõi trên môi trường thực nữa, vì một số hồi quy chỉ xuất hiện dưới lưu lượng và dữ liệu thực. Mục tiêu là biến hiệu năng thành thuộc tính mà hệ thống tự động bảo vệ, không phải thứ bạn khám phá lại trong một sự cố.

4. **Bạn tối ưu cho độ trễ hay thông lượng trên mỗi đường quan trọng, và có ai đã viết lựa chọn đó ra không?** Đây là những mục tiêu khác nhau kéo ngược chiều nhau: gom lô và các worker song song nâng thông lượng nhưng có thể thêm độ trễ cho từng yêu cầu riêng lẻ, nên một đội tối ưu theo bản năng thường mua sai trục và bắt người dùng chờ để tiết kiệm thời gian máy mà không ai thiếu. Trong một đội lớn mối nguy nhân lên, vì một nhóm chỉnh một dịch vụ dùng chung cho thông lượng hàng loạt trong khi nhóm khác phụ thuộc vào nó cho độ trễ tương tác, và không bên nào biết mục tiêu của bên kia. Hãy mang mẫu sử dụng thực tế của mỗi đường (yêu cầu tương tác so với lô nền), độ trễ phân vị hiện tại, và thông lượng bền vững bạn cần, rồi quyết định trục một cách tường minh thay vì để một mặc định nổi lên. Với một hệ thống doanh nghiệp hoặc chính phủ dưới SLA, hãy nêu tên chỉ số nào thỏa thuận được viết dựa trên, vì tối ưu trục không được đo có thể vi phạm hợp đồng trong khi bảng điều khiển của bạn trông khỏe mạnh.

5. **Làm sao bạn biết các điểm chuẩn của mình đo công việc thực chứ không phải bộ tối ưu xóa bài kiểm thử của bạn?** Một điểm chuẩn nói dối còn tệ hơn không có, vì nó trao cho đội sự tự tin sai rồi một hồi quy vẫn được phát hành. Các đội thường xuyên báo cáo một con số may mắn duy nhất từ một lần chạy lạnh trên đầu vào đồ chơi, vốn đo khởi động, biên dịch đúng lúc, và khả năng của trình biên dịch loại bỏ mã không dùng thay vì hành vi người dùng thực sự gặp. Hãy mang một điểm chuẩn mẫu và thẩm vấn nó: nó có khởi động, chạy nhiều lần lặp, báo cáo phương sai, dùng kích thước và phân phối dữ liệu đại diện, và đánh bại việc loại bỏ mã chết trên kết quả của nó không. Lực kéo đối lập là các điểm chuẩn trung thực chậm hơn để viết và chạy so với vi điểm chuẩn nhanh, nên hãy thống nhất nơi các phép xấp xỉ rẻ là chấp nhận được và nơi bạn đòi hỏi sự chặt chẽ. Trong bối cảnh công hoặc chịu quy định nơi mua sắm và cơ quan giám sát sẽ yêu cầu bạn tái tạo các con số, hãy ghi lại thiết bị, khối lượng công việc và môi trường cùng với kết quả để khẳng định có thể được xác minh thay vì chỉ được khẳng định.

6. **Khi công việc hiệu năng cạnh tranh với tính năng cho cùng những kỹ sư, bạn quyết định thế nào, và ai nắm thẩm quyền ngân sách?** Hiệu năng có lợi suất giảm dần mạnh, nên bản sửa dẫn dắt bởi hồ sơ đầu tiên có thể giảm một nửa độ trễ trong khi bản thứ mười cắt một phần trăm với cái giá gấp đôi độ phức tạp của mã, và không có quy tắc thì tiếng nói to nhất hoặc hạn chót gần nhất thắng. Những cân nhắc đối lập là thật: nợ hiệu năng chưa sửa cộng dồn lặng lẽ và ngày càng đắt để bổ sung sau, nhưng chạy theo tốc độ vượt ngân sách làm đói lộ trình sản phẩm và thêm độ phức tạp làm chậm công việc tương lai. Hãy mang trạng thái ngân sách hiện tại cho mỗi đường quan trọng, chi phí ước tính của hiện trạng tính bằng máy hoặc chuyển đổi mất đi, và lợi ích biên của lần tối ưu hóa tiếp theo, để sự đánh đổi được thực hiện dựa trên bằng chứng thay vì áp lực. Với một doanh nghiệp lớn hoặc chương trình chính phủ, hãy nêu tên ai sở hữu ngân sách hiệu năng và ai có thể ủy quyền chi thời gian kỹ thuật cho nó, vì một mục tiêu không ai chịu trách nhiệm bảo vệ là mục tiêu âm thầm xói mòn.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ phân phối thắng quy trình, vì vậy hãy cưỡng lại việc viết lại và các khung hiệu năng hoành tráng. Hãy dành một buổi chiều với trình lập hồ sơ trên đường mà người dùng thực sự phàn nàn, sửa chi phí lớn nhất (thường là truy vấn N+1 hoặc một lần quét tuyến tính vô tình), và thêm một ngân sách phân vị nhẹ vào CI để chiến thắng không thể âm thầm hồi quy. Dành tối ưu hóa sâu cho khoảnh khắc một con số thực, không phải linh cảm, nói rằng mã quá chậm.

**Doanh nghiệp nhỏ.** Không có chuyên gia hiệu năng và ngân sách eo hẹp, hãy dựa vào các công cụ bạn đã trả tiền: trình lập hồ sơ trong môi trường chạy của bạn, các phân vị độ trễ trong bảng điều khiển lưu trữ, và bộ phân tích truy vấn tích hợp trong cơ sở dữ liệu. Đặt một hoặc hai ngân sách đơn giản gắn với thứ khách hàng cảm nhận, như thời gian tải trang hoặc thanh toán, và coi một vi phạm là tín hiệu để mua một bậc nhanh hơn hoặc sửa truy vấn tệ nhất thay vì khởi động một dự án tinh chỉnh mà bạn không thể bố trí nhân sự.

**Doanh nghiệp lớn.** Ở quy mô đội máy, hiệu năng là chi phí trực tiếp, vì vậy hãy quản trị nó như một kỷ luật chung: công cụ lập hồ sơ chuẩn, ngân sách phân vị gắn với các chỉ số kinh doanh, và các cổng hồi quy CI được áp dụng nhất quán để sự len lỏi chậm của không đội nào thổi phồng cả hóa đơn đám mây. Theo dõi độ trễ, cấp phát và thông lượng đối chiếu với đường cơ sở qua các dịch vụ, và giữ bằng chứng điểm chuẩn tái tạo được, vì mức giảm 30% CPU trên một đội máy lớn là khoản tiết kiệm lặp lại đáng được kiểm toán và bảo vệ trước các khoản phạt SLA.

**Chính phủ.** Hiệu năng là một đảm bảo tiếp cận: một trang tải được trên một chiếc điện thoại cũ qua kết nối yếu quyết định liệu một công dân có hoàn thành yêu cầu trợ cấp hay không. Hãy đặt ngân sách tường minh đối chiếu với các thiết bị cấp thấp thực tế và mạng bị bóp băng thông, và công bố kết quả điểm chuẩn tái tạo được ghi lại thiết bị, mạng và khối lượng công việc, để mua sắm và cơ quan giám sát có thể xác minh các con số thay vì tin vào lời. Ưu tiên đo lường minh bạch, có thể kiểm toán hơn khẳng định của nhà cung cấp, và yêu cầu các nhà cung cấp cung cấp cùng bằng chứng tái tạo được.

## Ví dụ

**Công ty khởi nghiệp.** Một đội SaaS nhỏ nhận thấy bảng điều khiển của họ ì ạch và bị cám dỗ viết lại nó bằng một khung nhanh hơn. Thay vào đó họ dành một buổi chiều với trình lập hồ sơ và biểu đồ ngọn lửa, cho thấy 70% thời gian yêu cầu là một điểm cuối duy nhất phát ra một truy vấn cơ sở dữ liệu cho mỗi hàng, mẫu N+1 kinh điển. Họ thay nó bằng một truy vấn gom lô duy nhất, độ trễ giảm từ 1,2 giây xuống 90 mili giây, và họ thêm ngân sách p99 200 ms vào một điểm chuẩn CI nhẹ để bản sửa không thể âm thầm hồi quy. Không viết lại, một buổi chiều, một chiến thắng gấp mười lần.

**Doanh nghiệp lớn.** Một nền tảng bán lẻ vận hành hàng nghìn phiên bản, và hóa đơn đám mây của nó bị chi phối bởi một dịch vụ gợi ý duy nhất. Một chiến dịch lập hồ sơ tìm thấy sự xáo trộn cấp phát nặng gây ra các khoảng dừng thu gom rác thường xuyên, cộng với một bộ nhớ đệm có tỷ lệ trúng kém. Chỉnh cấu trúc dữ liệu cho tính cục bộ và sửa các khóa bộ nhớ đệm cắt 40% CPU mỗi yêu cầu, cho phép đội chạy cùng lưu lượng trên ít máy hơn 40%. Khoản tiết kiệm hoàn vốn công sức kỹ thuật trong vài tuần, và một SLA độ trễ p99 thỉnh thoảng bị vi phạm giờ giữ vững thoải mái, tránh các khoản phạt hợp đồng.

**Chính phủ.** Một cơ quan thuế quốc gia phải phục vụ công dân trên thiết bị cũ và kết nối nông thôn chậm. Đội đặt một ngân sách tường minh: trang kê khai phải trở nên tương tác được dưới 3 giây trên một chiếc điện thoại cấp thấp qua cấu hình 3G bị bóp băng thông. Họ lập hồ sơ trang, cắt bỏ công việc chặn tương tác, và công bố kết quả điểm chuẩn tái tạo được, ghi lại thiết bị, mạng và khối lượng công việc, để các cơ quan giám sát và kiểm toán viên khả năng tiếp cận có thể xác minh khẳng định thay vì tin vào lời. Hiệu năng ở đây không phải đòn bẩy chi phí mà là đảm bảo tiếp cận giữ cho dịch vụ dùng được cho mọi người.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của kỹ thuật hiệu năng thể hiện ở ba sổ cái. Thứ nhất là chi phí hạ tầng: mã nhanh hơn làm cùng công việc trên ít máy hơn, và với một đội máy lớn, mức giảm 30% CPU là khoản tiết kiệm trực tiếp, lặp lại vượt xa công sức kỹ thuật một lần. Thứ hai là doanh thu và sự hài lòng: độ trễ tương quan với chuyển đổi, bỏ cuộc và niềm tin của người dùng, nên cắt cái đuôi là đòn bẩy tăng trưởng, không chỉ là việc vệ sinh. Thứ ba là rủi ro được tránh: một vi phạm SLA mang tiền phạt, và một lần ra mắt tan chảy dưới tải mang thiệt hại danh tiếng và chi phí chữa cháy.

Tổng chi phí sở hữu khiêm tốn và dồn về phía trước. Bạn đầu tư vào công cụ lập hồ sơ, môi trường đo điểm chuẩn ổn định và các cổng CI, cộng với kỷ luật viết ngân sách và đọc hồ sơ. Chi phí ẩn lớn hơn là phương án thay thế: nợ hiệu năng cộng dồn lặng lẽ, và bổ sung tốc độ vào một hệ thống chậm sau khi ra mắt đắt hơn nhiều so với bảo vệ nó liên tục. Hãy trình bày lập luận với ban lãnh đạo bằng đơn vị của họ. Dịch độ trễ thành tỷ lệ chuyển đổi hoặc hoàn thành của công dân, dịch CPU thành chi tiêu đám mây hằng tháng, và dịch một cổng hồi quy thành số sự cố được tránh. Lập luận mạnh nhất là hiệu năng rẻ để bảo vệ từng commit một và tai hại để khôi phục sau khi nó đã mục nát.

## Phản mẫu và cạm bẫy

- **Tối ưu hóa mà không lập hồ sơ.** Chỉnh mã không phải nút thắt trong khi chi phí thực không được chạm đến.
- **Tối ưu hóa sớm.** Hy sinh sự rõ ràng cho tốc độ tưởng tượng mà trình lập hồ sơ sẽ không bao giờ đánh dấu.
- **Báo cáo trung bình.** Che giấu một cái đuôi đau đớn sau một giá trị trung bình thoải mái; người dùng cảm nhận p99, không phải trung bình.
- **Sân khấu vi điểm chuẩn.** Số liệu từ một khối lượng công việc đồ chơi mà bộ tối ưu đã xóa một nửa, không có khởi động hay phương sai được báo cáo.
- **Bộ nhớ đệm không có câu chuyện vô hiệu hóa.** Chạy theo tỷ lệ trúng trong khi phục vụ dữ liệu lỗi thời hoặc sai.
- **Cho rằng thêm luồng giúp ích.** Phớt lờ định luật Amdahl và phần tuần tự, rồi chìm trong tranh chấp.
- **Không có cổng hồi quy.** Để người dùng là bài kiểm thử hiệu năng vì không có gì trong CI bảo vệ ngân sách.
- **Tối ưu sai trục.** Mua thông lượng bằng gom lô khi người dùng cần độ trễ thấp, hoặc ngược lại.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Hiệu năng chỉ được xử lý khi có gì đó hỏng. Không có ngân sách, không có thói quen lập hồ sơ, không có điểm chuẩn. Tối ưu hóa là đoán mò dẫn dắt bởi trực giác, và trung bình là chỉ số duy nhất mà bất kỳ ai báo cáo.
- **Mức 2, Phát triển:** Một số đội lập hồ sơ trong các sự cố và giữ vài điểm chuẩn, nhưng thực hành không nhất quán và phụ thuộc vào sự nhiệt tình cá nhân. Ngân sách tồn tại không chính thức cho một hoặc hai đường quan trọng, và phân vị xuất hiện trên một số bảng điều khiển, nhưng không gì chặn một hồi quy trước khi nó được phát hành và mỗi đội phát minh lại cách tiếp cận riêng.
- **Mức 3, Chuẩn hóa:** Các đường quan trọng mang ngân sách phân vị bằng văn bản, và lập hồ sơ là bước đầu tiên được lập thành tài liệu, được kỳ vọng trước khi bất kỳ ai tối ưu hóa. CI bao gồm các bài kiểm thử hiệu năng với cổng hồi quy, các quy tắc đo điểm chuẩn trung thực (khởi động, phương sai, dữ liệu đại diện) được viết ra và thực thi toàn tổ chức, và mọi đội theo cùng một phương pháp thay vì phương pháp riêng.
- **Mức 4, Quản lý:** Tổ chức đo hiệu năng như một thuộc tính được kiểm soát. Phân vị độ trễ, thông lượng, tỷ lệ cấp phát và số truy vấn chậm được theo dõi đối chiếu với đường cơ sở tường minh trên môi trường thực và CI, hồi quy được định lượng đối chiếu với ngưỡng thay vì tranh cãi, và ngân sách gắn với các chỉ số kinh doanh như chuyển đổi hoặc chi tiêu đám mây để một vi phạm kích hoạt một quyết định dựa trên dữ liệu. Bằng chứng điểm chuẩn tái tạo được và được ghi lại cùng thiết bị, khối lượng công việc và môi trường để kiểm toán.
- **Mức 5, Điều phối:** Hiệu năng được cải tiến liên tục và tích hợp trong toàn tổ chức. Ngân sách, lập hồ sơ, đo điểm chuẩn trung thực và phân tích biểu đồ ngọn lửa là các kỹ năng thường lệ, các cổng hồi quy ổn định và đáng tin cậy, và dữ liệu môi trường thực cùng CI khép vòng một cách tự động. Tổ chức điều chỉnh ngân sách khi lưu lượng, phần cứng và ưu tiên kinh doanh dịch chuyển, cân bằng lại công sức về phía các đường có lợi ích cao nhất, và bảo vệ hiệu năng như một thuộc tính thường trực thay vì một chiến dịch định kỳ.

## Ý tưởng để thảo luận

1. Đường quan trọng nào của bạn hiện có một ngân sách bằng văn bản, dựa trên phân vị, và đường nào chỉ được bảo vệ bằng hy vọng?
2. Lần cuối một trình lập hồ sơ làm bạn ngạc nhiên là khi nào, và điều đó dạy bạn gì về nơi bạn cho rằng thời gian đi?
3. Các điểm chuẩn của bạn có khởi động, báo cáo phương sai và dùng dữ liệu đại diện, hay chúng đang đo bộ tối ưu?
4. Bạn đang chi máy móc để che đậy mã mà một chiến dịch lập hồ sơ có thể làm rẻ hơn ở đâu?
5. Với khối lượng công việc song song hóa nhiều nhất của bạn, phần tuần tự là bao nhiêu, và định luật Amdahl có giới hạn mức tăng tốc bạn đang theo đuổi không?
6. Nếu một đồng đội hợp nhất một thay đổi làm gấp đôi độ trễ p99, mất bao lâu trước khi có ai nhận ra, và họ sẽ phát hiện bằng cách nào?

## Những điểm cần ghi nhớ

- Đo trước khi tối ưu; nút thắt hiếm khi ở nơi bạn đoán, và tối ưu hóa sớm tốn sự rõ ràng mà không có lợi ích.
- Xác định "đủ nhanh" là một ngân sách phân vị, vì trung bình che giấu cái đuôi nơi người dùng thực sống.
- Ưu tiên chiến thắng về thuật toán (lớp Big O tốt hơn) hơn chỉnh vi mô, và biết bạn cần độ trễ hay thông lượng.
- Tôn trọng giới hạn của song song hóa (định luật Amdahl) và hiểm họa của bộ nhớ đệm (vô hiệu hóa và lỗi thời).
- Đo điểm chuẩn trung thực với khởi động, phương sai và khối lượng công việc đại diện, và nghi ngờ vi điểm chuẩn.
- Đặt cổng hiệu năng trong CI (chương 2.4) và theo dõi nó trên môi trường thực (chương 9.2); bổ sung cho góc nhìn cấp hệ thống trong chương 3.5.
- Hiệu năng là chi phí với doanh nghiệp, là sự tiếp cận với chính phủ, và rẻ để bảo vệ liên tục nhưng đắt để bổ sung sau.

## Tài liệu tham khảo và đọc thêm

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (lập hồ sơ, biểu đồ ngọn lửa và phương pháp).
- Brendan Gregg, *BPF Performance Tools* (khả năng quan sát và lập hồ sơ thực tế trên Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): nguồn của châm ngôn tối ưu hóa sớm.
- Donald E. Knuth, *The Art of Computer Programming* (phân tích thuật toán và độ phức tạp).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest và Clifford Stein, *Introduction to Algorithms* (Big O và hiệu quả thuật toán).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): nguồn gốc của định luật Amdahl.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (phân cấp bộ nhớ và tính cục bộ dữ liệu).
- Martin Kleppmann, *Designing Data-Intensive Applications* (độ trễ, thông lượng và hành vi đuôi trong hệ thống).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (thực hành đo điểm chuẩn trung thực trên các môi trường chạy được quản lý).
- Ilya Grigorik, *High Performance Browser Networking* (hiệu năng phía máy khách và mạng cho người dùng băng thông thấp).
