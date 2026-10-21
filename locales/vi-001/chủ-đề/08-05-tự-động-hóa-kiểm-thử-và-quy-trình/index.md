# 8.5 Tự động hóa kiểm thử và quy trình

## Tổng quan và động lực

Tự động hóa kiểm thử và quy trình là thực hành thay công việc kỹ thuật và vận hành thủ công, lặp đi lặp lại bằng các quy trình đáng tin cậy do máy thực thi. Về phía kiểm thử, điều này nghĩa là [tự động hóa kiểm thử](https://en.wikipedia.org/wiki/Test_automation): các bộ kiểm thử tự động chạy liên tục để xác minh tính đúng, hiệu năng và bảo mật. Về phía quy trình, nó mở rộng sang bộ máy xung quanh của phân phối và vận hành phần mềm: thu thập bằng chứng tuân thủ, thực thi sổ tay vận hành, khắc phục các vấn đề đã biết, và thực thi các kiểm soát quản trị, bảo mật và chi phí. Ý tưởng thống nhất đơn giản. Bất cứ thứ gì làm lặp đi lặp lại và khả đoán nên được mã hóa, để nó chạy nhất quán, nhanh chóng và không cần lao động nhàm chán của con người.

Với các đội lớn, tự động hóa là cách duy nhất để giữ chất lượng và kiểm soát không sụp đổ dưới quy mô. Kiểm thử thủ công không theo kịp hàng trăm kỹ sư thực hiện hàng nghìn thay đổi. Nó trở thành nút thắt, và độ phủ của nó trở nên không nhất quán và không đáng tin. Quy trình vận hành thủ công cũng chịu thiệt. Khởi động lại một dịch vụ, xoay vòng thông tin xác thực, và thu thập bằng chứng kiểm toán đều trở nên chậm và dễ lỗi khi những con người mệt mỏi làm chúng dưới áp lực qua một hệ sinh thái lớn. Tự động hóa công việc này làm kết quả lặp lại được. Nó cũng giải phóng các kỹ sư có kỹ năng để tập trung vào những vấn đề đòi phán đoán thực sự cần hiểu biết của con người.

Trong bối cảnh doanh nghiệp và chính phủ, tự động hóa cũng là chìa khóa để làm tuân thủ bền vững. Các tổ chức chịu quy định phải liên tục chứng minh các kiểm soát đã được áp dụng và bằng chứng được thu thập. Làm điều này bằng tay thì đắt, chậm và dễ có khoảng trống. Tự động hóa việc thu thập bằng chứng và thực thi kiểm soát biến tuân thủ từ một cuộc diễn tập cháy định kỳ thành một thuộc tính liên tục, kiểm chứng được của hệ thống. Cách tiếp cận "tuân thủ dưới dạng mã" này vừa giảm chi phí vừa củng cố sự bảo đảm mà kiểm toán viên và cơ quan quản lý đòi hỏi.

## Các nguyên tắc chính

- Tự động hóa công việc lặp lại, khả đoán và dựa trên quy tắc; dành công sức con người cho phán đoán.
- Làm các kiểm thử tự động nhanh, đáng tin và tất định, nếu không chúng sẽ bị phớt lờ.
- Chạy kiểm thử song song và dịch chúng sớm hơn để phản hồi vẫn nhanh khi bộ kiểm thử lớn lên.
- Mã hóa quy trình vận hành thành [sổ tay vận hành](https://en.wikipedia.org/wiki/Runbook)-dưới-dạng-mã để chúng có phiên bản, kiểm thử được và thực thi được.
- Ưu tiên tự động hóa tích hợp tốt hơn tập lệnh giòn bắt vít vào hệ thống từ bên ngoài.
- Tạo bằng chứng tuân thủ tự động như sản phẩm phụ của quy trình bình thường.
- Giữ một con người trong vòng lặp cho hành động rủi ro cao; tự động hóa cái an toàn và thường lệ trước.

## Khuyến nghị

### Xây hạ tầng kiểm thử nhanh, đáng tin, song song

Một bộ kiểm thử chỉ có giá trị nếu kỹ sư tin nó và nó trả phản hồi nhanh. Hãy đầu tư vào hạ tầng kiểm thử chạy các bộ song song qua nhiều worker, để tổng thời gian đồng hồ vẫn thấp ngay cả khi số kiểm thử lớn lên hàng nghìn. Cấu trúc bộ kiểm thử như một kim tự tháp: nhiều [kiểm thử đơn vị](https://en.wikipedia.org/wiki/Unit_testing) nhanh, ít kiểm thử tích hợp hơn, và một số nhỏ kiểm thử đầu-đến-cuối. Khi đó phần lớn phản hồi đến trong vài giây. Hãy loại bỏ kiểm thử chập chờn không thương tiếc. Một kiểm thử thất bại ngắt quãng tệ hơn không có kiểm thử, vì nó dạy kỹ sư phớt lờ thất bại. Cung cấp môi trường kiểm thử tạm thời, theo yêu cầu để kiểm thử tích hợp và đầu-đến-cuối chạy trên hạ tầng thực tế, cô lập.

### Tự động hóa phát hành, tuân thủ và thu thập bằng chứng

Hãy mở rộng tự động hóa vượt khỏi kiểm thử sang quy trình phát hành và tuân thủ. Để đường ống tự động tạo các hiện vật mà kiểm toán viên cần: bản ghi ai đã phê duyệt một thay đổi, kiểm thử nào đã chạy và đạt, quét bảo mật tìm thấy gì, và chính xác hiện vật nào đã được triển khai. Coi kiểm soát là mã, để các kiểm tra bắt buộc được thực thi đồng đều và kết quả của chúng được ghi nhật ký. "Tuân thủ dưới dạng mã" này biến việc thu thập bằng chứng từ một cuộc chạy vạy thủ công trước kiểm toán thành một bản ghi liên tục, luôn hiện hành. Nó cũng làm tư thế tuân thủ của hệ thống quan sát được bất cứ lúc nào.

### Áp dụng ChatOps và sổ tay vận hành dưới dạng mã

Hãy mã hóa quy trình vận hành thành sổ tay thực thi được giữ trong quản lý phiên bản, thay vì tài liệu văn xuôi lỗi thời dần. Nơi một quy trình an toàn và được hiểu rõ, hãy nối nó vào tự động hóa có thể chạy theo yêu cầu. ChatOps đưa các thao tác này vào giao diện trò chuyện dùng chung, để người vận hành kích hoạt và quan sát hành động tự động trong một cuộc trò chuyện minh bạch, cộng tác, có ghi nhật ký. Điều này làm vận hành hiển thị với cả đội và tạo bản ghi tự động về những gì đã làm. Nó cũng hạ rào cản để kỹ sư ít kinh nghiệm hơn chạy quy trình an toàn, vì tự động hóa mã hóa các bước đúng.

### Triển khai khắc phục tự động cẩn thận

Với các vấn đề lặp lại, được hiểu rõ, hãy xây khắc phục tự động phát hiện một điều kiện và áp dụng bản sửa đã biết, như khởi động lại tiến trình hỏng, co giãn lên khi tải cao, dọn đĩa đầy, hay chuyển dự phòng một thành phần. Bắt đầu với các khắc phục rủi ro thấp, tin cậy cao. Yêu cầu con người xác nhận cho bất cứ thứ gì có bán kính ảnh hưởng đáng kể. Khắc phục tự động giảm thời gian phục hồi trung bình và loại bỏ mệt mỏi cảnh báo lặp lại. Nhưng nó phải được xây trên phát hiện vững chắc và có biện pháp bảo vệ, vì tự động hóa hành động trên một tín hiệu giả có thể khuếch đại một sự cố. Hãy ghi nhật ký mọi hành động tự động, để người vận hành giữ đầy đủ khả năng nhìn thấy và có thể can thiệp.

### Đặt tự động hóa quy trình bằng robot (RPA) đúng chỗ

[Tự động hóa quy trình bằng robot](https://en.wikipedia.org/wiki/Robotic_process_automation) điều khiển giao diện người dùng và ứng dụng hiện có để tự động hóa nhiệm vụ, bắt chước các cú nhấp và gõ phím mà con người thực hiện. RPA có chỗ chính đáng như một cây cầu cho hệ thống cũ hoặc bên thứ ba không phơi API và không thể tích hợp theo cách nào khác. Hãy dùng nó thực dụng cho những trường hợp đó, nhưng biết giới hạn của nó. Tự động hóa dựa trên giao diện vốn giòn: nó vỡ bất cứ khi nào giao diện đổi, và nó không giải quyết sự thiếu tích hợp cơ bản. Nơi có API hay tích hợp đúng nghĩa, hãy ưu tiên nó. Coi RPA là giải pháp tạm chiến thuật, không phải nền tảng chiến lược, và lên kế hoạch thay thế khi hệ thống hiện đại hóa.

### Tự động hóa kiểm soát quản trị, bảo mật và chi phí

Hãy mã hóa kiểm soát tổ chức thành các kiểm tra tự động chạy liên tục: chính sách dưới dạng mã cho lan can hạ tầng, quét bảo mật tự động trong đường ống, và phát hiện tự động bất thường chi phí và tài nguyên nhàn rỗi. Tự động hóa quản trị làm kiểm soát đồng đều và không bỏ qua được, và nó mở rộng đến khối lượng thay đổi mà rà soát thủ công không bao giờ bao quát nổi. Cùng cách tiếp cận thực thi một chính sách bảo mật có thể gắn cờ một hóa đơn đám mây mất kiểm soát hay một thẻ bắt buộc bị thiếu. Quản trị chuyển từ kiểm toán thủ công định kỳ sang lan can tự động liên tục.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Kiểm thử tự động rộng | Phản hồi nhanh, nhất quán; cho phép thay đổi | Chi phí xây và bảo trì; rủi ro chập chờn | Mọi đội ở quy mô |
| Tuân thủ dưới dạng mã | Bằng chứng liên tục, sẵn sàng kiểm toán | Kỹ thuật ban đầu để mã hóa kiểm soát | Tổ chức chịu quy định |
| Sổ tay vận hành dưới dạng mã + ChatOps | Vận hành lặp lại được, hiển thị, có nhật ký | Công sức mã hóa và bảo trì | Đội có tải vận hành thực |
| Khắc phục tự động | Phục hồi nhanh hơn; ít lao động nhàm chán | Rủi ro nếu phát hiện sai | Vấn đề lặp lại, được hiểu rõ |
| RPA (tự động hóa giao diện) | Bắc cầu hệ thống không có API | Giòn; che giấu khoảng trống tích hợp | Hệ thống cũ như giải pháp tạm |
| Quản trị tự động | Kiểm soát đồng đều, không bỏ qua được | Công sức viết và điều chỉnh chính sách | Hệ sinh thái lớn, được quản trị |

Đánh đổi trung tâm là đầu tư ban đầu so với lao động nhàm chán và rủi ro liên tục. Tự động hóa luôn tốn công sức xây và bảo trì. Tự động hóa xây kém, dù là kiểm thử chập chờn, RPA giòn, hay khắc phục kích hoạt bởi tín hiệu xấu, có thể tệ hơn không có, vì nó xói mòn lòng tin hoặc khuếch đại thất bại. Kỷ luật gồm ba phần: tự động hóa cái thực sự lặp lại và đáng tin, đầu tư làm tự động hóa đó đáng tin cậy, và giữ con người trong vòng lặp nơi phán đoán hay rủi ro cao đòi hỏi. Làm tốt, tự động hóa sinh lời nhiều lần. Làm cẩu thả, nó trở thành khoản nợ của chính nó.

## Câu hỏi để thảo luận với đội của bạn

1. **Kiểm thử tích hợp và đầu-đến-cuối của bạn chạy trên môi trường thực tế, tạm thời, hay trên một hộp staging dùng chung mà mọi người tranh giành?** Môi trường cô lập theo yêu cầu cho mỗi pull request cho phép kiểm thử tích hợp và đầu-đến-cuối thực hành trên hạ tầng thực tế mà các đội không chặn nhau hay làm ô nhiễm trạng thái chung. Một môi trường staging dùng chung duy nhất thành nút thắt và nguồn thất bại chập chờn, phụ thuộc thứ tự khi nhiều đội chồng lên. Hãy quyết định bạn có dựng được môi trường tạm thời không, chúng tốn bao nhiêu, và kiểm thử nào thực sự cần chúng so với một vật thay thế nhanh trong bộ nhớ. Hãy mang dữ liệu: staging bị tranh chấp bao lâu một lần, bao nhiêu thất bại truy về nhiễu loạn môi trường dùng chung, và thời gian đồng hồ hiện tại của tầng tích hợp. Câu trả lời định hình cả độ tin cậy kiểm thử lẫn việc các tầng trên của kim tự tháp trả phản hồi nhanh đến đâu.

2. **Quy trình vận hành được mã hóa thành sổ tay vận hành dưới dạng mã và đưa ra qua ChatOps, hay chúng vẫn sống như văn xuôi lỗi thời dần?** Sổ tay được mã hóa, có quản lý phiên bản thì kiểm thử được và thực thi được, và chạy chúng qua giao diện trò chuyện dùng chung làm mọi hành động hiển thị và tự động ghi nhật ký. Điều đó hạ rào cản để một kỹ sư trực ít kinh nghiệm hơn hành động an toàn, vì tự động hóa mã hóa các bước đúng thay vì dựa vào trí nhớ truyền miệng. Hãy quyết định quy trình nào đủ an toàn và được hiểu rõ để nối trước, và bạn giữ con người can thiệp được thế nào. Với một hệ sinh thái lớn sự minh bạch này đồng thời là bản ghi kiểm toán về ai đã làm gì và khi nào. Hãy mang sổ tay hiện tại của bạn, ghi chú cái nào đã cũ, và xác định hai ba quy trình chạy nhiều nhất để mã hóa trước.

3. **Trong đường ống của bạn, quét bảo mật và kiểm tra chính sách nào chặn một lần hợp nhất, và cái nào chỉ cảnh báo?** Quản trị tự động chỉ đáng xây nếu các kiểm soát không bỏ qua được, vì một kiểm tra chỉ cảnh báo bị phớt lờ dưới áp lực hạn chót đúng như chính sách trong wiki. Hãy quyết định, từng kiểm soát một, cái gì chặn và cái gì cảnh báo: một lỗ hổng nghiêm trọng hay thẻ mã hóa bị thiếu có lẽ chặn, trong khi phát hiện kiểu phong cách mức thấp hơn có thể cảnh báo. Ở quy mô đây là cách bạn thực thi lan can bảo mật và chi phí đồng đều qua khối lượng thay đổi mà rà soát thủ công không bao quát nổi. Hãy mang bản kiểm kê các kiểm tra hiện tại và đánh dấu mỗi cái là chặn hay khuyến cáo, rồi thảo luận tỷ lệ dương tính giả, vì một kiểm tra chặn ồn ào dạy mọi người đòi ngoại lệ. Lằn ranh giữa chặn và cảnh báo là nơi quản trị của bạn có răng hay không.

4. **Khắc phục tự động nào chúng ta sẵn lòng để hành động mà không có con người xác nhận trước, và bán kính ảnh hưởng là gì nếu phát hiện sai?** Khắc phục tự động cắt thời gian phục hồi và mệt mỏi cảnh báo, nhưng một bản sửa kích hoạt bởi tín hiệu giả có thể biến một trục trặc nhỏ thành ngừng hoạt động hoàn toàn, nên quyết định cái gì chạy không giám sát là quyết định rủi ro, không phải sự tiện lợi. Hãy cân nhắc các lực kéo đối lập: hành động không giám sát nhanh nhất nhưng rủi ro nhất, trong khi xác nhận có con người trong vòng lặp an toàn hơn nhưng tái đưa vào độ trễ và lao động nhàm chán mà bạn định loại bỏ. Hãy mang các khắc phục ứng viên được xếp hạng theo tần suất và theo bán kính ảnh hưởng xấu nhất, tỷ lệ dương tính giả lịch sử của phát hiện đằng sau mỗi cái, và liệu mọi hành động có được ghi nhật ký và đảo ngược được. Với một hệ sinh thái doanh nghiệp hay chính phủ lớn, hãy thêm một thẩm quyền thay đổi chính thức và kế hoạch hoàn tác cho bất cứ thứ gì chạm dữ liệu sản xuất hay dịch vụ hướng công dân, vì một khắc phục tự động không kiểm toán hay hoàn tác được là cái cơ quan quản lý sẽ buộc bạn tắt.

5. **Chúng ta tài trợ và giao quyền sở hữu để bảo trì tự động hóa thế nào để nó không mục rữa thành khoản nợ?** Kiểm thử, sổ tay vận hành, kiểm tra chính sách và bot RPA đều mục rữa khi hệ thống xung quanh đổi, và tự động hóa bị bỏ bê tệ hơn không có: một sổ tay cũ cho sự tự tin giả trong khủng hoảng và một bot RPA hỏng lặng lẽ làm rơi công việc. Căng thẳng là bảo trì cạnh tranh với công việc tính năng cho cùng các kỹ sư, và nó vô hình cho đến khi có gì đó hỏng, nên là thứ đầu tiên bị cắt dưới áp lực hạn chót. Hãy mang bản kiểm kê hiện tại các tài sản tự động hóa, tồn đọng kiểm thử chập chờn và bot hỏng, và ước tính trung thực giờ kỹ sư đã dành cho bảo dưỡng so với những gì được lập ngân sách. Trong bối cảnh doanh nghiệp hay chính phủ, hãy nêu chủ sở hữu chịu trách nhiệm cho mỗi tự động hóa trọng yếu và tài trợ việc bảo trì nó như một dòng khoản mục tường minh, vì kiểm toán viên và rà soát sự cố sẽ hỏi ai chịu trách nhiệm khi một kiểm soát không được bảo trì thất bại thầm lặng.

6. **Với mỗi hệ thống cũ chúng ta tự động hóa bằng RPA, kế hoạch cụ thể và kích hoạt để cho nghỉ hưu RPA đó nhường chỗ cho tích hợp thật là gì?** RPA là cây cầu chính đáng cho hệ thống không phơi API, nhưng một cây cầu không có kế hoạch thoát lặng lẽ cứng lại thành hạ tầng vĩnh viễn, giòn, vỡ ở mỗi thay đổi giao diện và củng cố chính khoảng trống tích hợp mà nó định bắc qua. Đánh đổi là thật: RPA mang giá trị nhanh và rẻ bây giờ, trong khi tích hợp API đúng nghĩa tốn hơn ban đầu nhưng bền, nên kỷ luật là coi RPA như một khoản vay có hạn, không phải một món mua. Hãy mang danh sách bot RPA trong môi trường sản xuất, hệ thống mỗi cái phụ thuộc, mỗi cái hỏng bao lâu một lần, và liệu một nỗ lực hiện đại hóa hay tích hợp có thực sự được tài trợ và lên lịch cho hệ thống bên dưới. Với các hệ sinh thái doanh nghiệp và chính phủ mang ứng dụng lõi hàng thập kỷ tuổi, hãy gắn mỗi bot RPA với một cột mốc hiện đại hóa có tên, vì RPA lặng lẽ thành trọng yếu mà không có ngày nghỉ hưu là nợ kỹ thuật cộng dồn mỗi năm giao diện nó cạo cứ tiếp tục đổi.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với hai ba kỹ sư và không có thời gian xây hạ tầng, hãy giữ một kim tự tháp kiểm thử nhỏ, nhanh chạy trong vài phút ở mỗi thay đổi, và coi mọi kiểm thử chập chờn là lỗi thật cần sửa hoặc xóa trong tuần đó. Bỏ qua công cụ tuân thủ nặng và chính sách dưới dạng mã bạn chưa cần, và chỉ mã hóa hai ba bản sửa vận hành chạy nhiều nhất của bạn thành tập lệnh đơn giản kích hoạt từ trò chuyện. Hãy tự động hóa thứ loại bỏ lao động nhàm chán hằng ngày, và chống lại việc xây bộ máy quản trị trước khi bạn có vấn đề quản trị.

**Doanh nghiệp nhỏ.** Không có chuyên gia kiểm thử hay nền tảng riêng, hãy dựa vào tự động hóa dựng sẵn trong công cụ bạn đã trả tiền: bộ chạy kiểm thử tích hợp của dịch vụ CI, phần bổ sung quét của nó, và môi trường được quản lý thay vì xây hạ tầng kiểm thử đặt riêng. Đóng khung lựa chọn mua-so-với-xây quanh bảo trì bạn duy trì được thực tế, vì một đường ống tùy chỉnh khéo léo không ai bảo trì được là kết quả tệ hơn một đường ống lưu trữ giản dị hơn. Dùng RPA tiết kiệm và chỉ nơi một công cụ nhà cung cấp bắc cầu một hệ thống bạn không tích hợp được cách nào khác.

**Doanh nghiệp lớn.** Qua nhiều đội mục tiêu là kiểm soát đồng đều, không bỏ qua được ở quy mô rà soát thủ công không bao quát nổi: hạ tầng kiểm thử song song dùng chung với môi trường tạm thời, lan can chính sách dưới dạng mã, và bằng chứng tuân thủ tạo tự động từ mọi lần chạy đường ống. Chuẩn hóa giao diện để các đội tái sử dụng công cụ khắc phục và sổ tay vận hành thay vì mỗi đội phát minh lại tập lệnh giòn, và quản lý tự động hóa như một danh mục có chủ, được tài trợ với ngân sách bảo trì rõ ràng. Hãy để ý rằng một kiểm tra chỉ cảnh báo ở một đội không bị coi là chặn ở đội khác, vì thực thi không nhất quán làm suy yếu sự bảo đảm bạn đang trả tiền.

**Chính phủ.** Quy tắc mua sắm, nghĩa vụ minh bạch và các yêu cầu giám sát liên tục khiến tuân thủ dưới dạng mã gần như thiết yếu: mỗi lần chạy đường ống nên ghi lại các kiểm soát đã kiểm tra, quét đã thực hiện, và phê duyệt đã cấp như bằng chứng chống giả mạo, sẵn sàng kiểm toán. Ưu tiên tự động hóa mở, di chuyển được hơn khóa chặt độc quyền để một hợp đồng tương lai có thể chuyển sang nhà cung cấp khác, và giữ một con người chịu trách nhiệm cho bất kỳ khắc phục nào chạm dịch vụ hướng công dân. Nơi một hệ thống hàng thập kỷ tuổi buộc dùng RPA, hãy lập tài liệu nó là cây cầu tạm thời, có chủ đích với kế hoạch hiện đại hóa công khai, và giữ kiểm tra quản trị theo đường cơ sở bảo mật bắt buộc ở mọi thay đổi.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bảy người giữ một kim tự tháp kiểm thử gọn gồm chủ yếu kiểm thử đơn vị nhanh cộng vài kiểm thử tích hợp, tất cả chạy song song để toàn bộ bộ kiểm thử xong dưới ba phút ở mỗi pull request. Khi một kiểm thử bắt đầu chập chờn, họ coi nó là lỗi thật và sửa hoặc xóa trong tuần đó, vì với đội nhỏ như vậy một bản dựng đỏ bị phớt lờ sẽ xói mòn lòng tin vào cả bộ kiểm thử. Họ cũng mã hóa hai bản sửa vận hành phổ biến nhất, khởi động lại worker bị kẹt và dọn đĩa đầy, thành tập lệnh nhỏ kích hoạt từ Slack, để ai trực cũng chạy chúng an toàn được mà không gọi một kỹ sư viết ra chúng.

**Doanh nghiệp lớn.** Một công ty thương mại điện tử lớn chạy bộ kiểm thử hàng chục nghìn kiểm thử, song song hóa qua một đội worker để toàn bộ bộ xong trong vài phút. Môi trường tạm thời dựng lên cho mỗi pull request để kiểm thử tích hợp thực tế. Vận hành chạy qua ChatOps: kỹ sư trực kích hoạt sổ tay đã mã hóa từ trò chuyện, và các sự cố phổ biến như dịch vụ quá tải được khắc phục tự động, với hành động được ghi nhật ký để rà soát. Đường ống thu thập tự động bằng chứng quét bảo mật và phê duyệt, nên kiểm toán hằng năm dựa vào một bản ghi luôn hiện hành thay vì cuộc săn bằng chứng thủ công.

**Chính phủ.** Một cơ quan công chịu yêu cầu giám sát liên tục nghiêm ngặt triển khai tuân thủ dưới dạng mã. Mỗi lần chạy đường ống ghi lại các kiểm soát đã kiểm tra, quét đã thực hiện, và phê duyệt đã cấp, tạo bằng chứng chống giả mạo thỏa mãn kiểm toán viên theo yêu cầu. Vì một hệ thống lõi của nó là ứng dụng hàng thập kỷ tuổi không có API, cơ quan dùng RPA như cây cầu có chủ đích để tự động hóa nhập dữ liệu vào nó trong khi nỗ lực hiện đại hóa tiến hành, với kế hoạch tường minh cho nghỉ hưu RPA một khi tích hợp đúng nghĩa tồn tại. Kiểm tra quản trị tự động thực thi đường cơ sở bảo mật bắt buộc ở mọi thay đổi hạ tầng.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của tự động hóa kiểm thử và quy trình hiện ra là thời gian kỹ sư thu hồi, phân phối nhanh hơn và an toàn hơn, phục hồi sự cố nhanh hơn, và chi phí tuân thủ thấp hơn đáng kể. Kiểm thử tự động cho phép thay đổi nhanh, tự tin làm nền tảng cho hiệu suất phân phối. Vận hành và khắc phục tự động cắt lao động nhàm chán và thời gian ngừng hoạt động làm kiệt sức đội và ngân sách. Tuân thủ dưới dạng mã có thể biến một cuộc kiểm toán từ nhiều tuần chuẩn bị thủ công thành một truy vấn thường lệ, một khoản tiết kiệm vừa về tài chính vừa về danh tiếng.

So sánh TCO cân nhắc chi phí thật, liên tục của việc xây và bảo trì tự động hóa với chi phí của việc không tự động hóa. Kiểm thử và vận hành thủ công không chỉ tốn giờ đã bỏ ra. Chúng còn tốn lỗi lọt, sự cố kéo dài, kiểm toán ngốn nhân viên chuyên môn, và sự kiệt sức của kỹ sư làm lao động nhàm chán lặp lại. Với ban lãnh đạo, lập luận thẳng thắn: tự động hóa chuyển chi phí vận hành lặp lại và rủi ro thành khoản đầu tư một lần cộng bảo trì mở rộng được, và nó làm chất lượng cùng tuân thủ liên tục thay vì từng đợt. Một lưu ý đáng nói thẳng. Tự động hóa phải được bảo trì và tin cậy; tự động hóa không được tài trợ, bị bỏ bê mục rữa thành khoản nợ.

## Phản mẫu và cạm bẫy

- **Kiểm thử chập chờn được chấp nhận.** Thất bại ngắt quãng phá hủy lòng tin và dạy kỹ sư phớt lờ kết quả đỏ.
- **Tự động hóa một quy trình hỏng.** Tự động hóa quy trình tồi chỉ làm mớ hỗn độn xảy ra nhanh hơn; hãy sửa quy trình trước.
- **RPA như chiến lược.** Dựa vào tự động hóa giao diện giòn như giải pháp vĩnh viễn che giấu và củng cố khoảng trống tích hợp.
- **Khắc phục không có phát hiện vững.** Bản sửa tự động kích hoạt bởi tín hiệu xấu có thể khuếch đại sự cố.
- **Sổ tay vận hành như văn xuôi cũ.** Quy trình sống trong tài liệu lỗi thời cho sự tự tin giả trong khủng hoảng.
- **Bằng chứng tuân thủ thu thập thủ công.** Các cuộc săn bằng chứng thủ công định kỳ tốn kém và để lại khoảng trống giữa các kỳ kiểm toán.
- **Không có con người trong vòng lặp cho hành động rủi ro cao.** Tự động hóa hoàn toàn các thao tác nguy hiểm loại bỏ phán đoán ngăn thảm họa.

## Mô hình trưởng thành

**Mức 1, Khởi đầu.** Kiểm thử và vận hành phần lớn thủ công và phản ứng. Độ phủ tùy nghi, quy trình sống trong đầu người hoặc tài liệu cũ, khắc phục diễn ra bằng tay trong sự cố, và bằng chứng tuân thủ được lắp ráp trong cuộc chạy vạy trước mỗi kiểm toán.

**Mức 2, Phát triển.** Kiểm thử tự động tồn tại nhưng chậm, chập chờn hoặc chạy không nhất quán, và thực hành khác nhau nhiều giữa các đội. Một số tập lệnh vận hành và sổ tay tồn tại rải rác, nhưng khắc phục vẫn thủ công và quản trị được thực thi bằng rà soát định kỳ thay vì kiểm tra liên tục.

**Mức 3, Chuẩn hóa.** Hạ tầng kiểm thử nhanh, song song, đáng tin là tiêu chuẩn có tài liệu toàn tổ chức. Sổ tay dưới dạng mã và ChatOps được dùng phổ biến, bằng chứng tuân thủ được tạo tự động từ các lần chạy đường ống, và kiểm soát quản trị chạy như kiểm tra tự động được thực thi áp dụng nhất quán qua các đội.

**Mức 4, Quản lý.** Chính tự động hóa được đo và kiểm soát theo đường cơ sở. Bạn theo dõi tỷ lệ kiểm thử chập chờn, thời gian đồng hồ của bộ, thời gian phục hồi trung bình của sự cố được khắc phục tự động, phần kiểm soát có bằng chứng tự động, và tỷ lệ dương tính giả trên kiểm tra chặn, và bạn giữ mỗi chỉ số theo một mục tiêu thống nhất. Quyết định khắc phục và độ phủ dựa trên dữ liệu này, và mọi hành động tự động được ghi nhật ký để xu hướng và hồi quy hiển thị thay vì đoán.

**Mức 5, Điều phối.** Tự động hóa được cải thiện liên tục và tích hợp trong toàn tổ chức. Khắc phục tự động xử lý sự cố thường lệ với biện pháp bảo vệ đã chứng minh, tuân thủ liên tục và luôn sẵn sàng kiểm toán, và bộ công cụ kiểm thử, vận hành và quản trị thích ứng khi hệ thống đổi, với cầu RPA được tích cực cho nghỉ hưu khi tích hợp trưởng thành. Con người tập trung vào phán đoán trong khi máy móc xử lý phần lặp lại được, và toàn bộ hệ thống cân bằng lại dựa trên bằng chứng.

## Ý tưởng để thảo luận

- Quy trình vận hành nào an toàn để tự động hóa hoàn toàn, và cái nào phải giữ một con người trong vòng lặp?
- Làm sao bạn giữ một bộ kiểm thử lớn nhanh và không chập chờn khi nó lớn lên?
- RPA là cầu nối chính đáng cho hệ thống cũ của bạn ở đâu, và kế hoạch cho nghỉ hưu nó là gì?
- Kiểm soát nào bạn có thể chuyển từ kiểm toán thủ công sang tuân thủ liên tục dưới dạng mã trước?
- Làm sao bạn xây lòng tin vào khắc phục tự động mà không rủi ro sự cố bị khuếch đại?
- Làm sao bạn tài trợ bảo trì liên tục mà tự động hóa đòi hỏi để nó không mục rữa thành khoản nợ?

## Những điểm cần ghi nhớ

- Tự động hóa cái lặp lại, khả đoán và dựa trên quy tắc; dành công sức con người cho phán đoán và quyết định rủi ro cao.
- Làm kiểm thử tự động nhanh, song song và đáng tin, và loại bỏ tính chập chờn không thương tiếc.
- Mã hóa vận hành thành sổ tay dưới dạng mã và đưa ra qua ChatOps để hiển thị và có bản ghi.
- Tạo bằng chứng tuân thủ tự động để kiểm toán dựa vào bản ghi liên tục, hiện hành.
- Chỉ dùng RPA như cây cầu tạm thời, có chủ đích cho hệ thống không có API, và lên kế hoạch cho nghỉ hưu nó.
- Thực thi kiểm soát quản trị, bảo mật và chi phí như kiểm tra tự động liên tục, với con người giám sát các hành động rủi ro.

## Tài liệu tham khảo và đọc thêm

- Lisa Crispin và Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble và David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering* (xem chương về loại bỏ lao động nhàm chán).
- Gene Kim, Jez Humble, Patrick Debois và John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 và 800-137 (giám sát liên tục).
- Tài liệu Open Policy Agent (chính sách dưới dạng mã).
