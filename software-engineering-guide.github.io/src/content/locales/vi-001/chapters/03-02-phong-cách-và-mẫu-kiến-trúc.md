# 3.2 Phong cách và mẫu kiến trúc

## Tổng quan và động lực

Một phong cách kiến trúc là một hình dạng rộng, tái sử dụng được để tổ chức một hệ thống: nó được phân rã thế nào, các phần giao tiếp với nhau ra sao, và các ranh giới rơi vào đâu. Chọn một phong cách là một trong những quyết định hệ trọng nhất (và bị hiểu lầm nhiều nhất) mà một tổ chức lớn đưa ra. Quá thường xuyên, lựa chọn theo mốt ("ai cũng đang dùng [vi dịch vụ](https://en.wikipedia.org/wiki/Microservices)") thay vì theo các ràng buộc thực của đội, miền nghiệp vụ và thực tế vận hành. Bạn kết thúc với một trong hai mớ hỗn độn: một hệ thống phân tán mà tổ chức không vận hành được, hoặc một [khối đơn](https://en.wikipedia.org/wiki/Monolithic_application) rối rắm mà không ai thay đổi an toàn được. Không cái nào là lỗi của phong cách. Cả hai đều đến từ việc khớp sai phong cách với tình huống.

Với các đội phát triển lớn, phong cách quan trọng trên hết vì [Định luật Conway](https://en.wikipedia.org/wiki/Conway%27s_law): cấu trúc của một hệ thống có xu hướng phản chiếu cấu trúc giao tiếp của tổ chức xây dựng nó. Vì vậy một phong cách kiến trúc cũng là một quyết định thiết kế tổ chức. Chia một hệ thống thành các dịch vụ thực ra là một quyết định về chia đội, quyền sở hữu và trách nhiệm trực ca. Các doanh nghiệp có hàng trăm kỹ sư có thể gánh được (và thường cần) các dịch vụ chi tiết với triển khai độc lập, vì sự độc lập đó là cách nhiều đội phát hành mà không chặn nhau. Ép cùng mẫu đó lên một đội nhỏ duy nhất, và nó thừa hưởng toàn bộ thuế vận hành mà không có lợi ích tổ chức nào.

Bối cảnh chính phủ và doanh nghiệp chồng thêm nhiều ràng buộc: tuổi thọ hệ thống dài, kiểm soát thay đổi nghiêm ngặt, chu kỳ mua sắm, tích hợp với các hệ thống ghi nhận lâu đời, và khả năng kiểm toán. Những điều này ưu ái các phong cách giữ ranh giới tường minh và các phụ thuộc dễ kiểm tra. Chương này khảo sát các phong cách chính: khối đơn qua vi dịch vụ, [kiến trúc hướng sự kiện](https://en.wikipedia.org/wiki/Event-driven_architecture) với [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation) và event sourcing, các mẫu [lưới dịch vụ](https://en.wikipedia.org/wiki/Service_mesh) và cổng, [serverless](https://en.wikipedia.org/wiki/Serverless_computing), và các kỷ luật nội bộ của kiến trúc [lục giác](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) và kiến trúc sạch. Quan trọng hơn, nó giúp bạn nhận ra khi nào mỗi cái phù hợp.

*Xem thêm:* chương 2.2 (nguyên tắc thiết kế phần mềm, bao gồm [Thiết kế hướng miền](https://en.wikipedia.org/wiki/Domain-driven_design)), chương 3.1 (nền tảng kiến trúc), và chương 3.3 (hệ thống phân tán).

## Các nguyên tắc chính

- **Phong cách đi theo các lực, không phải mốt.** Chọn dựa trên quy mô đội, độ phức tạp miền, tải và độ trưởng thành vận hành, không bao giờ vì một công nghệ đang phổ biến.
- **Độ liên kết mới là kẻ thù thực sự, không phải số lượng đơn vị triển khai.** Một khối đơn được mô-đun hóa tốt thắng một quả bóng bùn lớn phân tán.
- **Phân tán là chi phí bạn trả cho sự độc lập.** Chỉ tách khi giá trị của triển khai, mở rộng hoặc cô lập lỗi độc lập vượt chi phí của lệnh gọi mạng, thất bại một phần và nhất quán dữ liệu qua các dịch vụ.
- **Ranh giới nên đi theo miền kinh doanh.** Căn chỉnh dịch vụ và mô-đun với các ngữ cảnh giới hạn (mỗi cái là một mô hình miền tự chứa với ranh giới tường minh riêng), không phải với các tầng kỹ thuật.
- **Thiết kế bên trong tốt bất kể bên ngoài.** Phân tầng lục giác/sạch giữ logic nghiệp vụ độc lập khỏi khung phát triển và hạ tầng trong mọi phong cách.
- **Định luật Conway là không thể tránh, vì vậy hãy dùng nó.** Thiết kế ranh giới đội và kiến trúc cùng nhau.
- **Bắt đầu đơn giản hơn bạn nghĩ cần.** Bạn có thể trích xuất dịch vụ từ một khối đơn mô-đun tốt; gỡ phân tán một đống vi dịch vụ non vội khó hơn nhiều.

## Khuyến nghị

### Mặc định là khối đơn mô-đun; tách khi có bằng chứng

Hãy bắt đầu hầu hết các hệ thống như một đơn vị triển khai duy nhất với ranh giới mô-đun nội bộ mạnh: giao diện rõ ràng, không với vào dữ liệu của mô-đun khác, và quy tắc phụ thuộc được thực thi. Bạn có giao dịch đơn giản, tái cấu trúc dễ dàng, và một thứ duy nhất để triển khai và quan sát. Chỉ tách một mô-đun thành dịch vụ riêng khi bạn có lý do cụ thể: một phần phải mở rộng riêng, một đội cần triển khai theo nhịp riêng, một miền lỗi bạn phải cô lập, hoặc một yêu cầu công nghệ khác với phần còn lại. Khi bạn tách, hãy tách theo ranh giới ngữ cảnh giới hạn để mỗi dịch vụ sở hữu dữ liệu của nó và phơi bày một hợp đồng ổn định.

### Biết khi nào vi dịch vụ xứng đáng với chỗ đứng của chúng

Vi dịch vụ cho bạn khả năng triển khai độc lập, mở rộng độc lập, cô lập lỗi, và sự tự do pha trộn công nghệ. Đổi lại chúng đòi hỏi CI/CD (tích hợp liên tục và phân phối liên tục) trưởng thành, hạ tầng tự động, truy vết phân tán, khám phá dịch vụ và một văn hóa trực ca. Hãy tự hỏi trung thực: tổ chức của bạn có thể vận hành hàng chục dịch vụ được triển khai độc lập trên môi trường thực một cách đáng tin cậy không? Nếu nền tảng và độ trưởng thành vận hành chưa có, vi dịch vụ chỉ nhân lên các chế độ thất bại của bạn mà không mang lại lợi ích. Nhiều tổ chức làm tốt nhất với một nhúm dịch vụ hạt thô căn chỉnh với các miền chính thay vì một bầy dịch vụ tí hon.

### Dùng kiến trúc hướng sự kiện ở nơi tách rời và bất đồng bộ hoàn vốn

Kiến trúc hướng sự kiện cho phép bên sản xuất phát ra các sự kiện mà không cần biết ai tiêu thụ chúng. Điều đó mua cho bạn liên kết lỏng, bộ đệm cho các đợt tăng tải, và cách dễ dàng để thêm bên tiêu thụ mới. Hãy dùng nó ở nơi các quy trình công việc vốn bất đồng bộ và phản ứng. **CQRS** (Phân tách Trách nhiệm Lệnh và Truy vấn) tách mô hình ghi khỏi một hoặc nhiều mô hình đọc, có ích khi tải hoặc hình dạng đọc và ghi khác nhau mạnh. **Event sourcing** lưu trạng thái dưới dạng nhật ký chỉ-thêm các sự kiện thay vì trạng thái hiện tại, cho bạn dấu vết kiểm toán hoàn hảo và du hành thời gian. Điều đó mạnh với tài chính và chính phủ, nơi "chúng ta đã đến giá trị này bằng cách nào?" là một câu hỏi pháp lý, nhưng nó thêm độ phức tạp thực trong việc đánh phiên bản sự kiện, dựng lại các phép chiếu, và suy luận về nhất quán cuối cùng. Hãy với tới chúng có chủ đích, không phải theo mặc định.

### Áp dụng các mẫu cổng, BFF và lưới để quản lý nhiều dịch vụ

Một **cổng API** cho máy khách bên ngoài một điểm vào duy nhất, xử lý xác thực, giới hạn tốc độ, định tuyến và kết thúc [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Bảo mật Tầng Vận chuyển). Một **Backend-for-Frontend (BFF)** cho mỗi loại máy khách (web, di động, API đối tác) tầng tổng hợp riêng được điều chỉnh của nó, để bạn tránh một API cồng kềnh một-cỡ-cho-tất-cả. Một **lưới dịch vụ** chuyển các mối quan tâm xuyên suốt (TLS tương hỗ, thử lại, thời gian chờ, chuyển dịch lưu lượng và đo đạc từ xa) vào một tầng hạ tầng sidecar, để các đội ứng dụng không phải cài đặt lại chúng. Chỉ thêm một lưới khi số lượng dịch vụ khiến việc xử lý những mối quan tâm này theo từng dịch vụ không quản lý nổi. Với vài dịch vụ, một lưới là gánh nặng vận hành hơn mức nó đáng.

### Cân nhắc serverless một cách trung thực

Hàm-như-một-dịch-vụ và các nền tảng serverless được quản lý gỡ bỏ việc quản lý máy chủ khỏi đĩa của bạn, mở rộng về không, và tính phí theo mức dùng, tuyệt vời cho các khối lượng công việc đột biến, hướng sự kiện hoặc đường cơ sở thấp và cho các đội nhỏ. Những đánh đổi là thật: độ trễ khởi động lạnh, giới hạn thời gian thực thi và tài nguyên, kiểm thử cục bộ khó hơn, có thể bị khóa chặt vào nhà cung cấp, và chi phí có thể vượt hạ tầng được cấp phát ở khối lượng cao bền vững. Hãy dùng serverless ở nơi kinh tế học và sự đơn giản vận hành của nó rõ ràng thắng. Đừng ép các hệ thống lõi ổn định, thông lượng cao vào nó vì sự nhiệt tình.

### Giữ logic nghiệp vụ sạch bên trong mọi dịch vụ

Dù phong cách bên ngoài là gì, hãy giữ bên trong sạch bằng kiến trúc **lục giác (cổng và bộ điều hợp)** hoặc **kiến trúc sạch**: quy tắc nghiệp vụ ở trung tâm, chỉ phụ thuộc vào các trừu tượng; khung phát triển, cơ sở dữ liệu và nhắn tin ở rìa như các bộ điều hợp có thể thay thế. Điều này giữ logic miền có giá trị của bạn kiểm thử được mà không cần hạ tầng và di động qua các thay đổi công nghệ: một lợi thế quyết định cho các hệ thống chính phủ và doanh nghiệp tồn tại lâu sẽ sống lâu hơn nhiều thế hệ khung.

## Đánh đổi: ưu và nhược điểm

| Phong cách | Phù hợp nhất khi | Ưu điểm | Nhược điểm |
|---|---|---|---|
| Khối đơn mô-đun | Hầu hết hệ thống, đặc biệt sớm | Vận hành đơn giản, giao dịch và tái cấu trúc dễ | Đơn vị triển khai duy nhất; mở rộng như một; rủi ro xói mòn |
| Vi dịch vụ | Nhiều đội, quy mô lớn, nền tảng trưởng thành | Triển khai/mở rộng độc lập, cô lập lỗi | Độ phức tạp phân tán, nhất quán dữ liệu, chi phí vận hành cao |
| Hướng sự kiện / CQRS / event sourcing | Quy trình bất đồng bộ, nhu cầu kiểm toán, đọc/ghi phân kỳ | Liên kết lỏng, khả năng kiểm toán, đọc mở rộng được | Nhất quán cuối cùng, đánh phiên bản sự kiện, gỡ lỗi khó hơn |
| Serverless | Công việc đột biến hoặc đường cơ sở thấp, hướng sự kiện | Không quản lý máy chủ, mở rộng về không, trả theo mức dùng | Khởi động lạnh, giới hạn, bị khóa chặt, chi phí ở tải bền vững cao |

Chủ đề lặp lại: bạn mua sự linh hoạt và độc lập bằng độ phức tạp vận hành và nhận thức. Các phong cách phân tán và hướng sự kiện từ bỏ sự đơn giản của một ngăn xếp gọi và một giao dịch duy nhất để đổi lấy khả năng mở rộng, triển khai và thất bại độc lập. Sự đánh đổi đó hoàn vốn ở quy mô lớn và với một nền tảng trưởng thành. Không có nó, nó là tai họa. Các kỷ luật nội bộ (lục giác/sạch) hầu như luôn đáng làm, vì chúng tốn ít và giữ các lựa chọn của bạn mở để đổi phong cách sau này.

## Câu hỏi để thảo luận với đội của bạn

1. **Trước khi bạn tách dịch vụ tiếp theo, bạn có tách đội sở hữu nó không, và ai có thẩm quyền làm điều đó?** Định luật Conway nghĩa là một ranh giới dịch vụ thực ra là một ranh giới đội, nên một lần tách mà sơ đồ tổ chức không hậu thuẫn tạo ra một khối đơn phân tán: hai đơn vị triển khai, một đoàn tàu phát hành, trực ca dùng chung. Trong một doanh nghiệp lớn, thẩm quyền định hình lại các đội thường nằm ở trên kỹ thuật, với đường báo cáo, tài chính và nhân sự, đó là lý do kiến trúc và thiết kế tổ chức phải được quyết định cùng nhau. Hãy mang bằng chứng đến cuộc thảo luận: dịch vụ được đề xuất có một đội có thể sở hữu nó từ đầu đến cuối, bố trí trực ca riêng, và triển khai theo nhịp riêng không? Nếu câu trả lời là không, hoặc tài trợ cho đội hoặc giữ năng lực đó như một mô-đun trong khối đơn. Tách mã mà không tách quyền sở hữu mua mọi chi phí của phân tán và không có sự độc lập nào.

2. **Bạn có thể triển khai độc lập từng dịch vụ hôm nay không, hay chúng bí mật phát hành đồng loạt?** Khối đơn phân tán là kết quả tệ nhất trong chương này: bạn trả cho lệnh gọi mạng, thất bại một phần và nhất quán dữ liệu qua các dịch vụ, nhưng vẫn không thể phát hành một cái mà không có những cái khác. Những dấu hiệu nhận biết là một cơ sở dữ liệu dùng chung, một thư viện dùng chung buộc phải nâng cấp phối hợp, và các bài kiểm thử tích hợp phải chạy cả hệ thống cùng nhau. Với một đội lớn điều này âm thầm giới hạn thông lượng, vì mọi đội xếp hàng sau một bản phát hành duy nhất dù sơ đồ cho thấy sự độc lập. Hãy lấy một thay đổi gần đây và đếm có bao nhiêu dịch vụ phải triển khai cùng nhau để an toàn; nếu con số đó lớn hơn một cho một thay đổi chạm vào một năng lực duy nhất, ranh giới của bạn sai. Cách sửa thường là cho mỗi dịch vụ dữ liệu riêng và một hợp đồng ổn định, có phiên bản, không phải thêm dịch vụ.

3. **Những lần tách dịch vụ hiện có nào của bạn đã ngừng hoàn vốn, và bạn có hợp nhất chúng lại không?** Thói quen nâng cao nhất của chương là coi các quyết định phong cách là có thể đảo ngược: trích xuất khi một động lực xuất hiện, và gộp lại khi động lực biến mất. Hầu hết các tổ chức chỉ bao giờ tách, nên các dịch vụ tí hon và dịch vụ thực thể lắm lời tích tụ cho đến khi điều phối và chi phí mạng làm nhỏ bé công việc mỗi dịch vụ làm. Hãy tìm các dịch vụ luôn triển khai cùng nhau, tồn tại vì một bảng cơ sở dữ liệu thay vì một năng lực kinh doanh, hoặc có các bước nhảy mạng nay chi phối độ trễ của một yêu cầu. Trong các hệ thống doanh nghiệp và chính phủ, nơi biên chế và ngân sách bị soi xét, gấp hai dịch vụ mỏng trở lại thành một dịch vụ hạt thô là một bước đi chính đáng, tiết kiệm chi phí, không phải thừa nhận thất bại. Hãy đặt việc hợp nhất lại lên bàn công khai như việc trích xuất, và quyết định cả hai bằng cùng một bằng chứng.

4. **Nền tảng và độ trưởng thành trực ca của bạn có thực sự hỗ trợ phong cách bạn đề xuất không, và bạn có thể gọi tên các khoảng trống cụ thể trước khi cam kết không?** Vi dịch vụ, lưới và xương sống hướng sự kiện chỉ mang lại lợi ích trên nền CI/CD trưởng thành, truy vết phân tán, khám phá dịch vụ và một văn hóa trực ca có thể suy luận về thất bại một phần. Một tổ chức lớn có xu hướng quyết định phong cách mục tiêu trong một diễn đàn kiến trúc và khám phá nền tảng thiếu sau, khi hàng chục dịch vụ đã ở trên môi trường thực và mọi sự cố mất hàng giờ để chẩn đoán. Hãy cân nhắc sức hấp dẫn của triển khai và mở rộng độc lập đối chiếu với câu hỏi tỉnh táo về ai vận hành nó lúc 3 giờ sáng: cùng lần tách giải phóng các đội để phát hành song song cũng nhân lên các chế độ thất bại mà mỗi đội phải hiểu. Hãy mang một bản kiểm kê trung thực đến cuộc thảo luận: tần suất triển khai hiện tại, thời gian phục hồi trung bình, bạn có truy vết qua ranh giới dịch vụ không, và một đội có thể thực tế vận hành bao nhiêu dịch vụ. Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm thời gian chờ mua sắm và tuyển dụng cho các năng lực nền tảng bạn thiếu, vì một phong cách giả định một lưới và một đội nền tảng bạn chưa tài trợ là một kế hoạch vận hành một hệ thống không thể hỗ trợ.

5. **Phần nào của miền nghiệp vụ cần một dấu vết kiểm toán event-sourced đầy đủ như một điều bắt buộc về pháp lý chứ không phải sự tiện lợi, và ai có thẩm quyền quyết định?** Event sourcing và CQRS mua cho bạn một lịch sử hoàn hảo, dựng lại được và các mô hình đọc mở rộng độc lập, nhưng chúng tốn của bạn việc đánh phiên bản sự kiện, dựng lại phép chiếu, và suy luận về nhất quán cuối cùng suốt vòng đời hệ thống. Áp dụng cho một miền không bao giờ cần dấu vết kiểm toán, độ phức tạp đó là thuế thuần túy; bị giữ lại ở một miền nơi "chúng ta đã đến giá trị này bằng cách nào?" là một câu hỏi pháp lý, sự vắng mặt của nó là một thất bại tuân thủ. Những cân nhắc đối lập là khả năng kiểm toán và khả năng mở rộng truy vấn ở một bên, và độ khó gỡ lỗi cùng tải nhận thức của lập trình viên ở bên kia, nên quyết định thuộc về những người hiểu cả nghĩa vụ quy định và gánh nặng vận hành, không phải ai nhiệt tình nhất với mẫu. Hãy mang các yêu cầu lưu giữ và dựng lại pháp lý hoặc hợp đồng cụ thể, khối lượng sự kiện kỳ vọng, và một ước tính trung thực về công việc đánh phiên bản và phép chiếu. Trong tài chính, thuế và chính phủ, nơi dựng lại một quyết định nhiều năm sau có thể là nghĩa vụ theo luật định, hãy nêu tên chủ sở hữu chịu trách nhiệm ký duyệt rằng một ngữ cảnh giới hạn nhất định có, hoặc không, cần một nhật ký sự kiện bất biến.

6. **Làm thế nào bạn ngăn khối đơn mô-đun xói mòn để việc trích xuất sau này vẫn rẻ, và cái gì sẽ thực thi các ranh giới?** Toàn bộ lập luận để bắt đầu với một khối đơn mô-đun dựa trên lời hứa rằng ranh giới nội bộ sạch làm cho việc trích xuất dịch vụ sau này phải chăng, nhưng những ranh giới đó phân rã âm thầm khoảnh khắc một hạn chót cám dỗ một mô-đun với vào dữ liệu của mô-đun khác. Với một đội lớn có nhiều người đóng góp, thiện chí và đánh giá mã một mình sẽ không giữ được lằn ranh; không có cơ chế thực thi, khối đơn âm thầm trở thành quả bóng bùn lớn mà phong cách này nhằm tránh. Hãy cân nhắc ma sát của quy tắc phụ thuộc và giao diện mô-đun được thực thi đối chiếu với chi phí khám phá, nhiều năm sau, rằng không ranh giới nào là thật và mỗi lần trích xuất nghĩa là gỡ trạng thái dùng chung. Hãy mang bằng chứng: ranh giới mô-đun có được thực thi bởi công cụ dựng, phân tích tĩnh, hay cấu trúc gói, hay chỉ là quy ước có tài liệu mà sáu lần hợp nhất gần nhất đã phớt lờ? Trong các hệ thống doanh nghiệp và chính phủ tồn tại lâu phải sống sót qua kiểm soát thay đổi nghiêm ngặt và nhiều thế hệ khung, hãy coi việc thực thi ranh giới là một biện pháp kiểm soát có thể kiểm toán, để tùy chọn phân tán sau này là thứ bạn thực sự đã bảo tồn thay vì thứ bạn giả định vẫn còn nắm giữ.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy mặc định một khối đơn mô-đun duy nhất và cưỡng lại sức hút của vi dịch vụ, vì nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ thuật và một bầy dịch vụ là thuế vận hành bạn không thể gánh trước khi có sự phù hợp sản phẩm-thị trường. Giữ ranh giới mô-đun sạch để bạn có thể trích xuất sau, và với tới serverless ở nơi mở rộng về không và trả theo mức dùng phù hợp với tải đột biến, đường cơ sở thấp của bạn. Chỉ tách đúng một thứ khi một động lực cụ thể xuất hiện, như bộ gửi thông báo đột biến, và không bao giờ sớm hơn.

**Doanh nghiệp nhỏ.** Không có đội nền tảng và ngân sách eo hẹp, hãy ưu tiên một khối đơn hoặc một nhúm dịch vụ hạt thô trên một nền tảng được quản lý, và mua hạ tầng lưu trữ thay vì tự xây lưới, truy vết và khám phá dịch vụ. Hãy cân nhắc serverless và cơ sở dữ liệu được quản lý như cách tránh hoàn toàn việc vận hành máy chủ, và đề phòng một thiết kế phân tán mà gánh nặng vận hành bạn không có ai gánh. Kiến trúc đúng là kiến trúc mà một hoặc hai người thực sự có thể triển khai, quan sát và phục hồi.

**Doanh nghiệp lớn.** Vấn đề thực sự là nhiều đội và Định luật Conway: căn chỉnh các dịch vụ hạt thô với các ngữ cảnh giới hạn và với quyền sở hữu của đội, và đầu tư có chủ đích vào nền tảng (CI/CD, truy vết, lưới và khám phá dịch vụ) khiến phân tán an toàn. Chuẩn hóa các mẫu cổng, BFF và kiến trúc sạch nội bộ để các nhóm thôi phát minh lại chúng, và quản trị việc trích xuất cùng hợp nhất lại như các quyết định danh mục dựa trên bằng chứng thay vì sở thích cục bộ. Hãy ngân sách tường minh chi phí vận hành của mọi lần tách, vì ở quy mô của bạn thất bại khối đơn phân tán đắt và chậm để gỡ.

**Chính phủ.** Tuổi thọ hệ thống dài, kiểm soát thay đổi nghiêm ngặt, chu kỳ mua sắm và khả năng kiểm toán định hình lựa chọn: ưu tiên các phong cách có ranh giới tường minh, kiểm tra được và hợp đồng bền vững tồn tại lâu hơn nhà cung cấp và các thế hệ khung. Event sourcing xứng đáng với độ phức tạp của nó ở nơi dựng lại một quyết định hướng đến công dân là nghĩa vụ theo luật định, vì vậy hãy dùng nó có chủ đích cho các sổ cái lõi và giữ kiến trúc sạch bên trong mọi dịch vụ để cô lập các quy tắc thay đổi theo mỗi ngân sách. Hãy coi tính di động và lối thoát khỏi serverless hoặc nền tảng nhà cung cấp độc quyền là yêu cầu mua sắm, không phải chuyện nghĩ đến sau.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người xây dựng sản phẩm lập lịch cảm thấy áp lực phải bắt đầu với vi dịch vụ vì một đối thủ đã viết blog về chúng, nhưng cưỡng lại. Họ phát hành một khối đơn mô-đun duy nhất với ranh giới nội bộ rõ ràng (lập lịch, thanh toán, thông báo) như các mô-đun riêng trong một đơn vị triển khai, để một kỹ sư có thể chạy toàn bộ cục bộ và một bản phát hành là một lần đẩy. Khi sản phẩm có sức hút, chỉ bộ gửi thông báo, vốn phân phối đến email và SMS dưới tải đột biến, được kéo ra thành dịch vụ riêng. Họ không thừa hưởng thuế vận hành nào của một chục dịch vụ trong khi vẫn đang săn tìm sự phù hợp sản phẩm-thị trường.

**Doanh nghiệp lớn.** Một công ty thương mại điện tử lớn bắt đầu như một khối đơn mô-đun. Khi lưu lượng tăng và các đội nhân lên, họ kéo ra các miền tải cao nhất, tiến hóa độc lập nhất (danh mục, giỏ hàng, thanh toán và tìm kiếm) thành các dịch vụ riêng, mỗi cái sở hữu dữ liệu của nó. Thanh toán phát ra các sự kiện mà kho hàng, hoàn tất đơn hàng và phân tích tiêu thụ qua một xương sống sự kiện, để các bên tiêu thụ mới (phát hiện gian lận, khách hàng thân thiết) có thể gắn vào mà không chạm vào thanh toán. Một cổng API xử lý xác thực và giới hạn tốc độ, và một BFF điều chỉnh tải trọng cho di động. Các miền lưu lượng thấp hơn còn lại ở trong khối đơn, tránh sự phân mảnh không cần thiết.

**Chính phủ.** Một cơ quan thuế xây dựng nền tảng đánh giá trên event sourcing cho sổ cái lõi, vì mọi thay đổi đối với nghĩa vụ của một người nộp thuế phải dựng lại được và có thể kiểm toán về mặt pháp lý trong nhiều năm. Các lệnh (nộp tờ khai, áp dụng thanh toán, phát hành điều chỉnh) tạo ra các sự kiện bất biến, và các mô hình đọc chiếu số dư hiện tại cho viên chức và công dân. CQRS cho phép phía truy vấn hướng đến công chúng mở rộng độc lập cho mùa nộp tờ khai cao điểm mà không đặt phía ghi vào rủi ro. Bên trong, mỗi dịch vụ theo kiến trúc sạch, để các quy tắc đánh giá, vốn thay đổi theo mỗi ngân sách, được cô lập khỏi công nghệ lưu trữ và nhắn tin.

## Luận chứng kinh doanh: động lực, ROI và TCO

Số tiền bị đặt cược trong một lựa chọn phong cách là rất lớn, vì quyết định tốn kém để đảo ngược. Áp dụng vi dịch vụ quá sớm và bạn thổi phồng tổng chi phí sở hữu qua xây dựng nền tảng, hạ tầng trùng lặp, gỡ lỗi phân tán, và gánh nặng vận hành nặng hơn: những chi phí đi cùng bạn suốt vòng đời hệ thống. Từ chối tách một khối đơn thực sự quá tải và bạn giới hạn thông lượng phân phối: các đội xếp hàng sau một bản phát hành dùng chung, và mọi thay đổi đặt cả hệ thống vào rủi ro. Cuộc trò chuyện ROI thực sự là về việc khớp chi tiêu vận hành với nhu cầu tổ chức.

Hãy trình bày lập luận với ban lãnh đạo bằng thông lượng và rủi ro, không phải công nghệ. Khả năng triển khai độc lập nghĩa là nhiều đội phát hành song song hơn và thời gian dẫn ngắn hơn: vận tốc kinh doanh đo được. Cô lập lỗi nghĩa là ít sự cố ngừng hoạt động tổng thể hơn và bán kính ảnh hưởng nhỏ hơn: tính sẵn sàng và bảo vệ danh tiếng đo được. Nhưng cũng hãy trung thực ngang nhau về khoản đầu tư nền tảng mà mỗi phong cách đòi hỏi: một lưới, truy vết và độ trưởng thành CI/CD là điều kiện tiên quyết, không phải phụ kiện tùy chọn, và chi phí của chúng thuộc về TCO. Với nhiều tổ chức, con đường rẻ nhất là một khối đơn được mô-đun hóa tốt ngay bây giờ, với ranh giới nội bộ sạch khiến việc trích xuất sau này rẻ. Điều đó mua cho bạn tùy chọn phân tán mà không phải trả cho nó trước khi bạn cần.

## Phản mẫu và cạm bẫy

- **Khối đơn phân tán.** Các dịch vụ phải được triển khai cùng nhau và dùng chung cơ sở dữ liệu: toàn bộ chi phí của phân tán, không có sự độc lập nào.
- **Dịch vụ tí hon.** Các dịch vụ chi tiết đến mức điều phối và chi phí mạng làm nhỏ bé công việc chúng làm.
- **Vi dịch vụ không có nền tảng.** Tách trước khi bạn có CI/CD, truy vết và độ trưởng thành trực ca; các chế độ thất bại nhân lên.
- **Dịch vụ thực thể.** Tách theo bảng cơ sở dữ liệu ("dịch vụ Người dùng", "dịch vụ Đơn hàng") thay vì theo năng lực kinh doanh, buộc các lệnh gọi liên dịch vụ lắm lời cho mọi thao tác.
- **Event sourcing ở khắp nơi.** Áp dụng nó cho các miền không cần dấu vết kiểm toán, trả thuế phức tạp mà không có lợi ích.
- **Cổng như một khối đơn.** Đặt logic nghiệp vụ vào cổng API, tái tạo một nút thắt trung tâm.
- **Lõi gắn với khung.** Logic nghiệp vụ rối với khung web hoặc ORM (ánh xạ đối tượng-quan hệ), khiến cả kiểm thử lẫn thay đổi công nghệ đau đớn.

## Mô hình trưởng thành

- **Mức 1: Khởi đầu.** Phong cách được chọn theo mốt hoặc tình cờ. Bạn có một khối đơn rối rắm hoặc một mớ phân tán tình cờ, ranh giới đi theo tầng kỹ thuật hoặc lịch sử thay vì miền, và các lần tách xảy ra phản ứng khi có gì đó hỏng.
- **Mức 2: Phát triển.** Một số đội vẽ ranh giới mô-đun có chủ đích bên trong khối đơn hoặc dựng vài dịch vụ hạt thô, và một số mối quan tâm xuyên suốt được xử lý nhất quán. Thực hành không đồng đều: một nhóm căn chỉnh dịch vụ với các ngữ cảnh giới hạn trong khi nhóm khác vẫn tách theo bảng cơ sở dữ liệu, và việc trích xuất vẫn tùy nghi.
- **Mức 3: Chuẩn hóa.** Một cách tiếp cận có tài liệu được thực thi trong toàn tổ chức: dịch vụ căn chỉnh với các ngữ cảnh giới hạn và sở hữu dữ liệu của chúng, các mẫu cổng và BFF được dùng ở nơi phù hợp, phân tầng sạch hoặc lục giác nội bộ là tiêu chuẩn, và mỗi lần tách đòi hỏi một động lực đã nêu. Ranh giới mô-đun được thực thi bằng công cụ, không chỉ bằng quy ước.
- **Mức 4: Quản lý.** Các quyết định phong cách được đo và kiểm soát theo các đường cơ sở. Bạn theo dõi tần suất triển khai và thời gian dẫn cho mỗi dịch vụ, thời gian phục hồi trung bình, bao nhiêu dịch vụ phải triển khai cùng nhau cho một thay đổi điển hình, và độ trễ bước nhảy mạng, rồi so sánh chi phí của mỗi lần tách với sự độc lập nó nhằm mua. Bằng chứng, không phải sở thích, quyết định liệu một ranh giới có sống sót không, và sự trôi dạt về khối đơn phân tán bị bắt bằng chỉ số thay vì một sự cố.
- **Mức 5: Điều phối.** Kiến trúc được tích hợp với thiết kế tổ chức và thích ứng liên tục. Một nền tảng trưởng thành (CI/CD, truy vết, và lưới ở nơi có lý do) làm cho cả phân tán lẫn hợp nhất lại đều rẻ, các đội thường xuyên trích xuất khi một động lực xuất hiện và gấp dịch vụ trở lại khi một động lực biến mất, và các lựa chọn phong cách được cân bằng lại khi cấu trúc đội, tải và bức tranh rủi ro dịch chuyển qua cả hệ thống.

## Ý tưởng để thảo luận

1. Ở đâu trong hệ thống của bạn một khối đơn thực sự là điểm mạnh, và ở đâu nó là nút thắt thực sự?
2. Động lực cụ thể nào sẽ biện minh cho việc trích xuất dịch vụ tiếp theo của bạn, và bạn có thể gọi tên nó trước khi xây không?
3. Tổ chức của bạn có độ trưởng thành vận hành mà vi dịch vụ đòi hỏi không? Còn thiếu gì?
4. Với phần nào của miền nghiệp vụ, một dấu vết kiểm toán event-sourced đầy đủ là điều bắt buộc về pháp lý hay kinh doanh so với điều tốt nếu có?
5. Ranh giới dịch vụ hiện tại của bạn phản chiếu ranh giới đội tốt đến đâu, và sự căn chỉnh đó đang giúp hay hại?
6. Nếu bạn phải đổi khung web hay cơ sở dữ liệu năm tới, bạn phải viết lại bao nhiêu logic nghiệp vụ?

## Những điểm cần ghi nhớ

- Chọn phong cách kiến trúc từ các lực thực (quy mô đội, miền, tải, độ trưởng thành vận hành), không phải từ mốt.
- Khối đơn mô-đun là mặc định đúng cho hầu hết hệ thống; chỉ trích xuất dịch vụ khi có động lực cụ thể và theo ranh giới ngữ cảnh giới hạn.
- Vi dịch vụ đánh đổi độ phức tạp vận hành và nhận thức lấy triển khai, mở rộng và cô lập lỗi độc lập; chúng đòi hỏi một nền tảng trưởng thành.
- Hướng sự kiện, CQRS và event sourcing mang lại tách rời và khả năng kiểm toán với cái giá là nhất quán cuối cùng và độ phức tạp đánh phiên bản; hãy áp dụng có chủ đích.
- Cổng, BFF và lưới thuần hóa các hệ thống nhiều dịch vụ nhưng thêm trọng lượng; hãy đưa chúng vào khi quy mô đòi hỏi, không sớm hơn.
- Áp dụng kiến trúc lục giác/sạch bên trong mọi dịch vụ để giữ logic nghiệp vụ có giá trị kiểm thử được và bền vững qua thay đổi công nghệ.

## Tài liệu tham khảo và đọc thêm

- Sam Newman, *Building Microservices* và *Monolith to Microservices*
- Chris Richardson, *Microservices Patterns*
- Eric Evans, *Domain-Driven Design*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Robert C. Martin, *Clean Architecture*
- Alistair Cockburn, "Hexagonal Architecture (Ports and Adapters)"
- Gregor Hohpe và Bobby Woolf, *Enterprise Integration Patterns*
- Martin Fowler, *Patterns of Enterprise Application Architecture* (và các bài viết về CQRS và Event Sourcing)
- Matthew Skelton và Manuel Pais, *Team Topologies*
