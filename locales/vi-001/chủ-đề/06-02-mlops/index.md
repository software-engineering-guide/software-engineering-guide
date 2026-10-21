# 6.2 Kỹ thuật học máy (MLOps)

## Tổng quan và động lực

Kỹ thuật học máy, thường gọi là [MLOps](https://en.wikipedia.org/wiki/MLOps), là kỷ luật đưa [học máy](https://en.wikipedia.org/wiki/Machine_learning) ra khỏi sổ tay và thí nghiệm để vào các hệ thống sản xuất đáng tin cậy, quan sát được, bảo trì được. Phần mềm truyền thống hành xử như mã của nó nói. Một hệ thống ML hành xử như mã của nó, dữ liệu của nó, và các tham số mô hình đã học của nó cùng nói. Điều đó khiến hệ thống ML khó kiểm thử hơn, khó tái lập hơn, và dễ hỏng lặng lẽ khi thế giới trôi xa khỏi dữ liệu chúng được huấn luyện. MLOps mang sự chặt chẽ của kỹ thuật phần mềm (quản lý phiên bản, kiểm thử, phân phối liên tục và giám sát) vào thực tế ba phần này của mã cộng dữ liệu cộng mô hình.

Với các đội lớn, MLOps là thứ phân biệt một mô hình một lần gây choáng trong demo với một đội mô hình mà nhiều nhóm có thể xây, triển khai và vận hành an toàn. Không có nền tảng và thực hành dùng chung, mỗi nhóm phát minh lại đường ống dữ liệu, vòng huấn luyện và triển khai, và bạn kết thúc với các hệ thống giòn mà sáu tháng sau không ai tái lập được. Doanh nghiệp dựa vào MLOps để mở rộng qua hàng chục mô hình, đáp ứng mục tiêu mức dịch vụ, và thỏa mãn kiểm toán viên hỏi một dự đoán cụ thể được tạo ra thế nào.

Trong chính phủ và các ngành chịu quy định, MLOps thường là một yêu cầu tuân thủ ngụy trang. Khả năng tái lập, dòng gốc và đánh phiên bản là thứ cho phép một cơ quan trả lời một câu hỏi có ý nghĩa pháp lý: chính xác mô hình nào, được huấn luyện trên dữ liệu nào, với mã nào, đã tạo ra quyết định ảnh hưởng đến một công dân? Một thực hành MLOps trưởng thành giữ câu hỏi đó trả lời được nhiều năm sau, vừa là kỹ thuật tốt vừa là một biện pháp bảo vệ pháp lý.

*Xem thêm:* chương 8.1 (CI/CD và phân phối), chương 9.2 (quan sát và giám sát), và chương 6.6 (hạ tầng và vận hành AI).

## Các nguyên tắc chính

- Coi dữ liệu, mã và mô hình là các hiện vật được đánh phiên bản chung; thay đổi bất kỳ cái nào cũng thay đổi hành vi hệ thống.
- Tự động hóa đường đi từ dữ liệu đến mô hình đã huấn luyện đến triển khai để nó lặp lại được và kiểm toán được.
- Làm mọi mô hình truy vết được đến chính xác dữ liệu, mã và cấu hình đã tạo ra nó.
- Đánh giá mô hình trên dữ liệu đại diện, được giữ riêng trước khi triển khai, và tiếp tục đánh giá sau đó.
- Giả định mô hình suy giảm; giám sát độ trôi (sự phân kỳ dần của dữ liệu trực tiếp hoặc quan hệ đầu vào-đầu ra khỏi những gì mô hình được huấn luyện), vấn đề chất lượng dữ liệu, và suy giảm hiệu năng từ ngày đầu.
- Ưu tiên các đường ống nhàm chán, tái lập được hơn các thí nghiệm thông minh, không tái lập được.
- Tách các mối quan tâm về tốc độ thí nghiệm và độ tin cậy sản xuất, và bắc cầu giữa chúng có chủ đích.

## Khuyến nghị

### Quản lý tường minh toàn bộ vòng đời ML

Hãy xác định và gắn công cụ đo cho từng giai đoạn: thu nạp và xác thực dữ liệu, [kỹ thuật đặc trưng](https://en.wikipedia.org/wiki/Feature_engineering), huấn luyện, đánh giá, triển khai và giám sát. Làm ranh giới giữa các giai đoạn tường minh để mỗi cái có thể được kiểm thử, thử lại và kiểm toán. Tránh thất bại phổ biến khi một mô hình được huấn luyện trong một sổ tay tùy nghi rồi ném qua tường cho vận hành. Thay vào đó, hãy bọc vòng đời trong một đường ống được điều phối mà bất kỳ kỹ sư được ủy quyền nào cũng chạy được từ một bản checkout sạch.

### Dùng kho đặc trưng, theo dõi thí nghiệm và sổ đăng ký mô hình

Một **kho đặc trưng** tập trung hóa định nghĩa đặc trưng để cùng các phép biến đổi chạy ở cả huấn luyện và phục vụ. Điều này loại bỏ độ lệch huấn luyện-phục vụ (sự không nhất quán giữa cách đặc trưng được tính cho huấn luyện so với cho dự đoán trực tiếp) và cho phép các đội tái sử dụng đặc trưng thay vì tính lại. **Theo dõi thí nghiệm** ghi lại tham số, phiên bản mã, phiên bản dữ liệu và chỉ số của mỗi lần chạy huấn luyện, để kết quả so sánh được và tái lập được. Một **sổ đăng ký mô hình** là hệ thống ghi nhận cho các mô hình đã huấn luyện, giữ phiên bản, dòng gốc, kết quả đánh giá, trạng thái phê duyệt và giai đoạn triển khai. Cùng nhau, chúng cho bạn trả lời "cái gì đã đổi?" khi hành vi dịch chuyển, và thăng cấp hoặc hoàn tác mô hình qua các giai đoạn được quản trị.

### Làm dữ liệu và mô hình tái lập được và có phiên bản với dòng gốc

Hãy đánh phiên bản tập dữ liệu của bạn, không chỉ mã. Dùng lưu trữ định địa chỉ theo nội dung hoặc công cụ đánh phiên bản dữ liệu để một lần chạy huấn luyện tham chiếu một ảnh chụp bất biến. Ghim mã bằng commit git, và ghim môi trường bằng phụ thuộc đã khóa và ảnh container. Nắm bắt dòng gốc đầu-đến-cuối: dữ liệu thô nào nuôi đặc trưng nào, đặc trưng và mã nào tạo ra mô hình nào, và mô hình đó được triển khai ở đâu. Khi một sự cố hay kiểm toán ập đến, dòng gốc biến cơn ác mộng pháp y thành một truy vấn đơn giản. Hãy ghi lại tính ngẫu nhiên (hạt giống) và phần cứng ở bất cứ đâu kết quả phụ thuộc vào chúng.

### Chọn mẫu triển khai khớp với khối lượng công việc

- **Theo lô** chấm điểm theo lịch trên các tập dữ liệu lớn; đơn giản nhất để vận hành, chịu được độ trễ, lý tưởng cho báo cáo và quyết định định kỳ.
- **Trực tuyến (thời gian thực)** phục vụ phản hồi các yêu cầu riêng lẻ trong ngân sách độ trễ chặt; cần truy xuất đặc trưng độ trễ thấp và hoạch định năng lực cẩn thận.
- **Luồng** chấm điểm sự kiện liên tục khi chúng đến; phù hợp phát hiện gian lận và giám sát nơi độ mới là then chốt.
- **Biên** chạy mô hình trên thiết bị hoặc phần cứng tại chỗ vì lý do độ trễ, quyền riêng tư, kết nối hoặc chủ quyền dữ liệu, phổ biến trong chính phủ và bối cảnh hiện trường.

Hãy chọn mẫu đơn giản nhất đáp ứng yêu cầu, và thiết kế việc triển khai với triển khai bóng, canary và hoàn tác tức thì.

### Giám sát độ trôi, suy giảm và chất lượng dữ liệu

Hãy gắn công cụ đo cho đầu vào và đầu ra trong môi trường sản xuất. Theo dõi **độ trôi dữ liệu** (phân phối đầu vào dịch chuyển), **[độ trôi khái niệm](https://en.wikipedia.org/wiki/Concept_drift)** (quan hệ giữa đầu vào và mục tiêu thay đổi), thất bại **chất lượng dữ liệu** (giá trị null, thay đổi lược đồ, nguồn thượng nguồn hỏng), và **suy giảm hiệu năng** đo so với sự thật nền bị trì hoãn nơi bạn có. Hãy đặt ngưỡng cảnh báo, viết sổ tay vận hành, và nối giám sát với các kích hoạt huấn luyện lại. Suy giảm thầm lặng là kiểu thất bại ML kinh điển, và giám sát là sự phòng thủ duy nhất của bạn.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Lựa chọn A | Lựa chọn B | Đánh đổi |
|---|---|---|---|
| Mẫu phục vụ | Theo lô | Trực tuyến | Đơn giản và chi phí so với độ mới và độ trễ |
| Tính đặc trưng | Kho đặc trưng | Đường ống theo từng mô hình | Nhất quán và tái sử dụng so với chi phí thiết lập |
| Nền tảng | Mua nền tảng MLOps được quản lý | Lắp ráp công cụ mã nguồn mở | Tốc độ và hỗ trợ so với linh hoạt và khóa chặt |
| Huấn luyện lại | Theo lịch | Kích hoạt bởi độ trôi | Khả đoán so với khả năng đáp ứng và độ phức tạp |
| Độ chặt chẽ tái lập | Đánh phiên bản dữ liệu đầy đủ | Theo dõi nhẹ | Sức mạnh kiểm toán so với lưu trữ và công sức |

Đánh đổi bao trùm là đầu tư bây giờ so với sự mong manh về sau. Hạ tầng tái lập và giám sát nặng tốn công sức ban đầu, nhưng chúng ngăn chi phí lớn hơn nhiều của các thất bại không giải thích được, mô hình không tái lập được, và niềm tin bị xói mòn. Nền tảng được quản lý giúp các đội nhanh hơn nhưng có thể tạo khóa chặt; ngăn xếp mã nguồn mở cho kiểm soát với giá công việc tích hợp. Các tổ chức lớn thường hưởng lợi từ một đội nền tảng dùng chung che giấu sự phức tạp này sau các mặc định đường lát sẵn.

## Câu hỏi để thảo luận với đội của bạn

1. **Làm sao chúng ta biết một mô hình đã triển khai suy giảm thầm lặng trước khi một khách hàng hay công dân bị hại, và ai sở hữu cảnh báo đó?** Suy giảm thầm lặng là kiểu thất bại ML kinh điển: mã vẫn chạy, mô hình vẫn trả điểm tự tin, và chất lượng trượt khi thế giới trôi khỏi dữ liệu huấn luyện. Với một đội lớn chạy nhiều mô hình, bạn cần câu này được trả lời cho từng mô hình, không phải một lần cho cả đội, vì mỗi cái có hồ sơ độ trôi và độ trễ sự thật nền riêng. Hãy mang các bộ giám sát hiện tại của bạn cho độ trôi dữ liệu, độ trôi khái niệm và đứt gãy chất lượng dữ liệu, ngưỡng cảnh báo, và sổ tay vận hành nói ai phản ứng. Trong bối cảnh chịu quy định nơi nhãn đến muộn hàng tuần, hãy thảo luận các tín hiệu thay thế bạn có thể theo dõi trong thời gian chờ, vì chờ sự thật nền bị trì hoãn nghĩa là chờ để phát hiện tác hại. Nếu không có chủ sở hữu duy nhất được nêu tên cho cảnh báo độ trôi của một mô hình, mô hình đó thực chất không được giám sát.

2. **Nếu một kiểm toán viên yêu cầu chúng ta tái lập một dự đoán cụ thể từ mười tám tháng trước, chúng ta có thực sự làm được đầu-đến-cuối không?** Khả năng tái lập là yêu cầu tuân thủ ẩn trong kỹ thuật tốt: nó cho phép một cơ quan trả lời chính xác mô hình nào, được huấn luyện trên dữ liệu nào, với mã nào, đã tạo ra một quyết định ảnh hưởng đến ai đó. Hãy mang một ví dụ thật và thử truy vết: ảnh chụp dữ liệu bất biến, commit git, phụ thuộc đã khóa và ảnh container, hạt giống đã ghi, và dòng gốc từ dữ liệu thô qua đặc trưng đến mô hình đã triển khai. Tín hiệu là liệu có mắt xích nào trong chuỗi đó bị thiếu hay thủ công. Với chính phủ và các ngành chịu quy định, hãy quyết định thời hạn lưu giữ mà luật thực sự yêu cầu và xác nhận kho lưu trữ của bạn giữ dòng gốc trả lời được suốt cả cửa sổ đó, vì một khoảng trống biến một truy vấn thường lệ thành khẩn cấp pháp y.

3. **Quy tắc của chúng ta để thăng cấp một mô hình lên môi trường sản xuất và hoàn tác nó là gì, và nó được thực thi bởi sổ đăng ký hay chỉ bằng lòng tin?** Thăng cấp không được quản trị là cách các thí nghiệm sổ tay rò vào môi trường sản xuất và cách một mô hình tồi nấn ná vì không ai hoàn tác được gọn gàng. Với nhiều đội, sự khác biệt giữa trưởng thành và mong manh là liệu sổ đăng ký mô hình có chặn cổng thăng cấp bằng phê duyệt và đánh giá bắt buộc, hay một kỹ sư có thể đẩy trọng số bằng tay. Hãy mang đường thăng cấp hiện tại, cơ chế hoàn tác, và bằng chứng rằng triển khai bóng hay canary thực sự chạy trước khi toàn bộ lưu lượng. Hãy thảo luận liệu huấn luyện lại là theo lịch hay kích hoạt bởi độ trôi, và liệu mô hình được huấn luyện lại có qua cổng xác thực trước khi triển khai, vì huấn luyện lại trên dữ liệu trực tiếp mà không xác thực khuếch đại độ trôi hay đầu độc. Câu trả lời nên được thực thi trong nền tảng, không phải trong một trang wiki mà người ta được tin sẽ làm theo.

4. **Chúng ta xây nền tảng MLOps trên công cụ mã nguồn mở, mua một nền tảng được quản lý, hay pha trộn cả hai, và ai đã cân nhắc khóa chặt?** Lựa chọn này đặt trần cho tốc độ mọi mô hình tương lai được phát hành và bao nhiêu kiểm soát bạn giữ đối với dữ liệu và đường ống. Một nền tảng được quản lý đưa các đội đến môi trường sản xuất nhanh và mang hỗ trợ, nhưng nó có thể bẫy định nghĩa đặc trưng, bản ghi dòng gốc và hiện vật mô hình của bạn trong một định dạng độc quyền bạn không dễ rời; một ngăn xếp mã nguồn mở lắp ráp giữ bạn di chuyển được với giá tích hợp và lao động bảo trì thực. Hãy mang tổng chi phí sở hữu của mỗi con đường (giấy phép hoặc xây, lưu trữ, tính toán cho huấn luyện lại, và nhân sự nền tảng để vận hành), một cái đọc trung thực về năng lực đội bạn chạy hạ tầng, và một bài kiểm tra thoát cụ thể: bạn có thể xuất sổ đăng ký, kho đặc trưng và dòng gốc rồi xây lại ở nơi khác không? Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm ràng buộc mua sắm và quy tắc chủ quyền dữ liệu, vì một nền tảng lưu dữ liệu huấn luyện ở khu vực hay định dạng mà cơ quan quản lý của bạn cấm sẽ bị loại bất kể nó tiện đến đâu.

5. **Kho đặc trưng và sổ đăng ký mô hình của chúng ta nên là một nền tảng tập trung hay liên bang theo từng đội, và độ lệch huấn luyện-phục vụ hôm nay tốn của chúng ta bao nhiêu?** Tập trung hóa định nghĩa đặc trưng loại bỏ độ lệch nơi một đặc trưng được tính một cách trong huấn luyện và một cách khác trong phục vụ, là nguồn mất độ chính xác thầm lặng và đắt đỏ, nhưng một nền tảng duy nhất có thể thành nút thắt làm chậm mọi đội. Liên bang trao tự chủ cho các đội trong khi nhân lên đường ống và khả năng hai đội định nghĩa cùng một đặc trưng không nhất quán. Hãy mang bằng chứng về nơi độ lệch đã cắn bạn, bao nhiêu đội tái sử dụng đặc trưng so với xây lại, và các mặc định đường lát sẵn mà một đội nền tảng dùng chung có thể cung cấp. Với một tổ chức lớn, hãy cân nhắc lợi ích quản trị của một hệ thống ghi nhận kiểm toán được so với chi phí phân phối của một hàng đợi trung tâm, và trong bối cảnh chịu quy định hãy ưu tiên dòng gốc tập trung cho phép kiểm toán viên truy vết mọi dự đoán đến chính mã đặc trưng đã tạo ra nó.

6. **Chúng ta đã khớp mẫu triển khai của mỗi mô hình với nhu cầu độ trễ, độ mới và chủ quyền thực của nó, hay mặc định mọi thứ vào một hình dạng?** Theo lô, trực tuyến, luồng và biên mỗi cái mang chi phí vận hành và độ phức tạp rất khác nhau, và chọn sai hoặc là chi quá mức cho hạ tầng thời gian thực mà một báo cáo hằng đêm chưa bao giờ cần hoặc bỏ đói một bộ chấm điểm gian lận khỏi độ mới nó phụ thuộc. Hãy quyết định theo từng khối lượng công việc mẫu nào yêu cầu thực sự biện minh, và chống lại việc chuẩn hóa trên lựa chọn phức tạp nhất vì nó cảm thấy hiện đại. Hãy mang ngân sách độ trễ, khối lượng, chi phí của một câu trả lời cũ, và độ trễ sự thật nền cho từng mô hình. Trong chính phủ và bối cảnh hiện trường, hãy cân nhắc có chủ đích triển khai biên và tại chỗ, vì quy tắc chủ quyền dữ liệu hay kết nối gián đoạn có thể buộc mô hình lên phần cứng cục bộ, và lựa chọn đó định hình lại cách bạn đánh phiên bản, giám sát và hoàn tác mọi mô hình bạn đẩy tới đó.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư, vì vậy hãy giữ MLOps nhẹ và mua nó. Hãy theo dõi thí nghiệm trong một công cụ lưu trữ đơn giản, ghim mỗi mô hình đã triển khai vào ảnh chụp dữ liệu huấn luyện và commit mã trong git, và thêm một kiểm tra độ trôi rẻ thay vì một nền tảng. Bỏ qua kho đặc trưng và đường ống đặt riêng cho đến khi mô hình thứ hai hay thứ ba khiến việc tái sử dụng đáng giá; một ngăn xếp mong manh bạn không bảo trì nổi sẽ nhấn chìm bạn nhanh hơn một năng lực bị thiếu.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia nền tảng ML và ngân sách eo hẹp, vì vậy hãy coi MLOps là thứ nhúng trong các công cụ bạn đã chạy thay vì một hệ thống bạn bố trí nhân sự. Ưu tiên một dịch vụ được quản lý xử lý đánh phiên bản, triển khai và giám sát giúp bạn, và đóng khung kỷ luật như câu hỏi về vệ sinh dữ liệu và khả năng tái lập: biết mô hình và dữ liệu nào tạo ra một kết quả nhất định, và giữ khả năng hoàn tác. Ưu tiên nhà cung cấp cho bạn xuất dữ liệu và mô hình để việc chuyển sau này vẫn khả thi.

**Doanh nghiệp lớn.** Vấn đề là quy mô qua hàng chục mô hình và nhiều đội: một kho đặc trưng dùng chung, theo dõi thí nghiệm, và sổ đăng ký mô hình với thăng cấp được quản trị để các nhóm thôi phát minh lại đường ống. Hãy lập ngân sách cho một đội nền tảng cung cấp mặc định đường lát sẵn, chuẩn hóa dòng gốc và giám sát để mọi mô hình kiểm toán được và mọi sự cố giải thích được, và quản lý xây-so-với-mua cùng khóa chặt có chủ đích sau một giao diện giữ các công cụ bên dưới thay thế được. Hãy thực thi cổng xác thực và hoàn tác trong nền tảng, không phải bằng quy ước.

**Chính phủ.** Khả năng tái lập, dòng gốc và đánh phiên bản là các yêu cầu tuân thủ ngụy trang, vì vậy hãy coi chúng là hạng nhất từ ngày đầu. Hãy đánh phiên bản chính xác tập dữ liệu và mã đằng sau mọi mô hình đã triển khai, lưu giữ dòng gốc đó trong thời hạn luật yêu cầu, và có khả năng tái lập mọi dự đoán lịch sử đã ảnh hưởng đến một công dân. Giữ một con người rà soát các quyết định hệ quả, cân nhắc triển khai biên và tại chỗ nơi quy tắc chủ quyền dữ liệu đòi hỏi, và yêu cầu mọi nền tảng nhà cung cấp trao đầy đủ khả năng di chuyển dữ liệu, đặc trưng và dòng gốc của bạn.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp phân tích nhỏ phát hành mô hình dự đoán rời bỏ đầu tiên với một nhà khoa học dữ liệu và một thiết lập nhẹ. Họ theo dõi thí nghiệm trong một công cụ lưu trữ đơn giản, ghim mỗi mô hình đã triển khai vào ảnh chụp dữ liệu huấn luyện và commit mã trong git, và thêm một tác vụ hằng tuần cơ bản so sánh đầu vào gần đây với phân phối huấn luyện. Khi một nguồn dữ liệu đổi định dạng ngày và các dự đoán bắt đầu trôi, kiểm tra đơn giản đó bắt được trong vài ngày thay vì sau một cuộc gọi khách hàng giận dữ, và đội tái lập được mô hình tốt gần nhất và hoàn tác.

**Doanh nghiệp lớn.** Một ngân hàng bán lẻ chạy hàng chục mô hình tín dụng và gian lận. Họ chuẩn hóa trên một kho đặc trưng dùng chung qua các đội, một dịch vụ theo dõi thí nghiệm, và một sổ đăng ký mô hình với cổng phê duyệt bắt buộc. Mọi mô hình trong môi trường sản xuất truy vết về ảnh chụp dữ liệu huấn luyện và commit mã của nó. Mô hình gian lận triển khai như bộ chấm điểm luồng; mô hình tín dụng chạy theo lô. Một tầng giám sát theo dõi độ trôi đầu vào và cảnh báo khi lược đồ nguồn dữ liệu thay đổi, từng bắt được một nguồn cấp thượng nguồn hỏng trước khi nó làm hỏng các quyết định.

**Chính phủ.** Một cơ quan trợ cấp công dùng một mô hình ML để ưu tiên rà soát hồ sơ. Vì các quyết định đó ảnh hưởng đến quyền tiếp cận dịch vụ của công dân, cơ quan đánh phiên bản chính xác tập dữ liệu và mã đằng sau mọi mô hình đã triển khai, giữ dòng gốc này trong thời hạn luật yêu cầu, và có thể tái lập mọi dự đoán lịch sử theo yêu cầu. Mô hình triển khai theo lô với một con người rà soát các ca bị gắn cờ, và một bộ giám sát độ trôi buộc đánh giá lại bắt buộc bất cứ khi nào quần thể đầu vào dịch chuyển, để mô hình không bao giờ bị áp dụng lặng lẽ ngoài các điều kiện nó được xác thực.

## Luận chứng kinh doanh: động lực, ROI và TCO

MLOps tự trả giá bằng cách biến các thí nghiệm mong manh thành tài sản đáng tin cậy. ROI đến từ thời gian ra môi trường sản xuất nhanh hơn cho mô hình mới, ít sự cố tốn kém hơn, ít hạ tầng trùng lặp hơn, và khả năng vận hành nhiều mô hình với một đội nền tảng nhỏ. Một kho đặc trưng và sổ đăng ký dùng chung có thể cắt thời gian phân phối mỗi mô hình đáng kể, vì các đội thôi xây lại cùng một đường ống.

TCO bao gồm xây dựng hoặc giấy phép nền tảng, lưu trữ cho dữ liệu và mô hình có phiên bản, tính toán cho huấn luyện lại, và nhân sự vận hành tất cả. Hãy cân nhắc điều đó so với chi phí của việc không áp dụng: mô hình bạn không tái lập hay kiểm toán được, thất bại thầm lặng gây hại cho khách hàng hay công dân, và kết luận của cơ quan quản lý. Trong bối cảnh chịu quy định, chi phí của một mô hình không giải thích được trong kiểm toán có thể lấn át toàn bộ khoản đầu tư MLOps. Hãy lập luận với ban lãnh đạo bằng cách đóng khung MLOps là giảm rủi ro và tăng tốc phân phối, không phải chi phí chung: một con đường lát sẵn mà mọi mô hình tương lai sẽ đi.

## Phản mẫu và cạm bẫy

- **Bước nhảy từ sổ tay sang môi trường sản xuất.** Triển khai mô hình huấn luyện trong sổ tay không được quản trị, không có khả năng tái lập.
- **Độ lệch huấn luyện-phục vụ.** Mã đặc trưng khác nhau ở huấn luyện và phục vụ, gây mất độ chính xác thầm lặng.
- **Không đánh phiên bản dữ liệu.** Đánh phiên bản mã nhưng không dữ liệu, nên các lần chạy không tái lập được.
- **Triển khai rồi quên.** Phát hành mô hình không giám sát, chỉ phát hiện suy giảm khi người dùng phàn nàn.
- **Huấn luyện lại tự động.** Tự động huấn luyện lại trên dữ liệu trực tiếp mà không xác thực, khuếch đại độ trôi hay đầu độc.
- **Hạ tầng một lần.** Mỗi đội xây đường ống riêng, nhân lên chi phí và sự mong manh.
- **Phớt lờ nhãn bị trì hoãn.** Giả định bạn đo độ chính xác ngay lập tức khi sự thật nền đến sau nhiều tuần.

## Mô hình trưởng thành

1. **Khởi đầu.** Mô hình xây tùy nghi trong sổ tay; triển khai thủ công; không đánh phiên bản dữ liệu hay mô hình; không giám sát; tái lập một dự đoán quá khứ là đoán mò.
2. **Phát triển.** Một số theo dõi thí nghiệm và sổ đăng ký mô hình xuất hiện, nhưng thực hành khác nhau theo đội; triển khai bán tự động; giám sát cơ bản bao quát vài mô hình; đánh phiên bản dữ liệu một phần và dòng gốc có lỗ hổng.
3. **Chuẩn hóa.** Một nền tảng dùng chung với kho đặc trưng, sổ đăng ký, đường ống tái lập được và dòng gốc đầu-đến-cuối được lập tài liệu và thực thi toàn tổ chức; giám sát độ trôi và chất lượng dữ liệu chạy qua các mô hình; thăng cấp và hoàn tác theo một đường được quản trị mà mọi đội dùng.
4. **Quản lý.** Cả đội mô hình được đo theo đường cơ sở: tỷ lệ trôi, đứt gãy chất lượng dữ liệu, độ chính xác mô hình so với sự thật nền bị trì hoãn, độ lệch huấn luyện-phục vụ, thời gian ra môi trường sản xuất, và chi phí vận hành mỗi mô hình được theo dõi như chỉ số; ngưỡng cảnh báo và cổng xác thực được thực thi dựa trên bằng chứng, và sức khỏe của mỗi mô hình được rà soát theo nhịp cố định với một chủ sở hữu có tên.
5. **Điều phối.** Vòng đời được tự động hóa hoàn toàn, kiểm toán được và thích ứng; huấn luyện lại kích hoạt bởi độ trôi chạy sau cổng xác thực; các đường lát sẵn tự phục vụ cho phép các đội phát hành an toàn; đánh giá liên tục gắn hiệu năng mô hình với chỉ số kinh doanh, và nền tảng tích hợp với phân phối, rủi ro và tuân thủ để mô hình thường xuyên được cho nghỉ hưu, thay thế và thu hẹp phạm vi khi dữ liệu và điều kiện dịch chuyển.

## Ý tưởng để thảo luận

- Làm sao bạn cân bằng tự do thí nghiệm với khả năng tái lập trong môi trường sản xuất?
- Kích hoạt huấn luyện lại đúng (lịch, độ trôi, hay suy giảm hiệu năng) cho các trường hợp sử dụng của bạn là gì?
- Bạn phải lưu giữ dòng gốc dữ liệu và mô hình bao lâu, và cái gì thúc đẩy yêu cầu đó?
- Kho đặc trưng và sổ đăng ký nên là nền tảng tập trung hay liên bang theo từng đội?
- Làm sao bạn giám sát độ chính xác khi nhãn sự thật nền đến với độ trễ dài?
- Khi nào triển khai biên đáng với độ phức tạp vận hành thêm của nó?

## Những điểm cần ghi nhớ

- Hành vi ML đến từ mã cộng dữ liệu cộng mô hình; hãy đánh phiên bản và quản trị cả ba cùng nhau.
- Kho đặc trưng, theo dõi thí nghiệm và sổ đăng ký là xương sống của ML tái lập được.
- Dòng gốc làm mô hình kiểm toán được và sự cố giải thích được: thiết yếu trong bối cảnh chịu quy định.
- Chọn theo lô, trực tuyến, luồng hay biên để khớp nhu cầu độ trễ, độ mới và chủ quyền.
- Mô hình suy giảm; giám sát độ trôi, chất lượng dữ liệu và suy giảm không phải tùy chọn.

## Tài liệu tham khảo và đọc thêm

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson và Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
