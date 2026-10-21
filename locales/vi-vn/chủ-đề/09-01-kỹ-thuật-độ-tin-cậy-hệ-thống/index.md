# 9.1 Kỹ thuật độ tin cậy hệ thống

## Tổng quan và động lực

[Kỹ thuật độ tin cậy hệ thống](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) áp dụng thực hành kỹ thuật phần mềm vào việc chạy các hệ thống sản xuất. Thay vì coi vận hành là công việc thủ công, theo phiếu, tách biệt khỏi phát triển, SRE coi độ tin cậy là một bài toán kỹ thuật bạn giải bằng mã, đo lường và các mục tiêu dịch vụ rõ ràng. Ý tưởng cốt lõi, được Google phổ biến nhưng nay đã lan rộng, đơn giản: những người giữ hệ thống chạy nên dành phần lớn thời gian xây tự động hóa và cải thiện hệ thống, không phải chữa cháy cùng những thất bại bằng tay hết lần này đến lần khác.

Với các đội lớn, điều này quan trọng vì quy mô nâng cả giá trị của độ tin cậy lẫn chi phí của việc làm sai. Khi một dịch vụ hỗ trợ hàng triệu người dùng hoặc hàng nghìn người tiêu dùng nội bộ, một giờ ngừng hoạt động nghĩa là mất doanh thu, giao dịch bị lỡ và lòng tin bị xói mòn. Vận hành thủ công vốn ổn với một nhúm máy chủ sụp đổ dưới hàng trăm dịch vụ và [triển khai liên tục](https://en.wikipedia.org/wiki/Continuous_deployment). SRE cho bạn ngôn ngữ chung về độ tin cậy, một cách làm tường minh sự đánh đổi giữa phát hành tính năng và giữ mọi thứ ổn định, và một cách giữ lằn ranh đó nhất quán qua nhiều đội.

Bối cảnh doanh nghiệp và chính phủ thêm trọng lượng. Các ngành chịu quy định như ngân hàng, y tế và dịch vụ công thường mang cam kết sẵn sàng theo luật hoặc hợp đồng, yêu cầu kiểm toán, và ít khoan dung với ngừng hoạt động ảnh hưởng công dân hay an toàn. Các dịch vụ số của chính phủ ngày càng công bố mục tiêu độ tin cậy và dữ liệu hiệu năng công khai. SRE cho bạn một cách chặt chẽ, dựa trên bằng chứng để xác định "đủ tin cậy" nghĩa là gì, đo nó trung thực, và bảo vệ các ưu tiên kỹ thuật trước lãnh đạo và cơ quan giám sát bằng dữ liệu thay vì ý kiến.

*Xem thêm:* chương 9.2 (khả năng quan sát và giám sát), chương 9.3 (quản lý sự cố), và chương 3.5 (khả năng mở rộng, hiệu năng và khả năng phục hồi).

## Các nguyên tắc chính

- **Độ tin cậy là tính năng quan trọng nhất.** Một hệ thống không hoạt động là vô giá trị bất kể nó có bao nhiêu tính năng, nhưng độ tin cậy hoàn hảo vừa không đạt được vừa không đáng chi phí của nó.
- **Xác định độ tin cậy bằng mục tiêu đo được.** Chỉ báo (SLI), mục tiêu (SLO) và thỏa thuận (SLA) mức dịch vụ biến kỳ vọng mơ hồ thành con số mọi người đồng ý.
- **100 phần trăm là mục tiêu sai.** Người dùng không phân biệt được hệ thống rất đáng tin với hệ thống hoàn toàn đáng tin, nên hãy nhắm đến "đủ tin cậy" và dành ngân sách còn lại cho vận tốc.
- **Ngân sách lỗi căn chỉnh khuyến khích.** Khoảng cách giữa SLO và 100 phần trăm là ngân sách rủi ro mà lập trình viên và người vận hành chia sẻ, thay tranh cãi bằng số học.
- **Lao động nhàm chán là kẻ thù.** Công việc vận hành thủ công, lặp lại, tự động hóa được nên được đo, giới hạn và loại bỏ có hệ thống.
- **Tự động hóa có chủ đích.** Tự động hóa là cách một đội nhỏ vận hành hệ thống lớn; đầu tư vào nó là hoạt động kỹ thuật hạng nhất.
- **Học không đổ lỗi.** Thất bại được coi là cơ hội cải thiện hệ thống và quy trình, không phải trừng phạt cá nhân.

## Khuyến nghị

### Xác định SLI, SLO và SLA có chủ đích

Hãy bắt đầu từ góc nhìn của người dùng. Một **[chỉ báo mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_indicator)** là phép đo định lượng về hành vi của dịch vụ, như tỷ lệ yêu cầu được phục vụ dưới 300 mili giây hoặc phần phản hồi thành công. Chọn một số ít SLI phản ánh thực sự sự hài lòng của người dùng: tính sẵn sàng, độ trễ, tính đúng và độ mới là những cái phổ biến. Một **[mục tiêu mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_objective)** là giá trị hoặc khoảng mục tiêu cho một SLI, ví dụ "99,9 phần trăm yêu cầu thành công trong cửa sổ cuốn 28 ngày." Một **[thỏa thuận mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_agreement)** là hợp đồng với hậu quả (hoàn tiền, phạt) gắn với một mức đã hứa. Hãy giữ SLO của bạn chặt hơn SLA, để bạn có cảnh báo trước khi vi phạm một cam kết. Công bố SLO của bạn, rà soát hằng quý, và coi chúng là tài liệu sống thắt chặt hoặc nới lỏng khi bạn học.

### Áp dụng ngân sách lỗi và thực thi chúng

Ngân sách lỗi là `100% trừ SLO`. Nếu SLO của bạn là 99,9 phần trăm, ngân sách của bạn là 0,1 phần trăm không tin cậy mỗi cửa sổ, khoảng 43 phút mỗi tháng. Hãy tiêu nó cho rủi ro có kế hoạch: bản phát hành táo bạo, thí nghiệm, và kiểm thử thất bại có kiểm soát. Khi ngân sách khỏe, các đội có thể phát hành nhanh. Khi nó cạn, chính sách nên tự động chuyển ưu tiên sang công việc độ tin cậy và tạm dừng thay đổi rủi ro cho đến khi hệ thống phục hồi. Sức mạnh của ngân sách lỗi là bạn thỏa thuận nó trước, nên nó loại cảm xúc và chính trị ra khỏi khoảnh khắc ngừng hoạt động.

### Đo và giảm lao động nhàm chán

Lao động nhàm chán là công việc vận hành thủ công, lặp lại, tự động hóa được, chiến thuật, và lớn lên theo hệ thống. Hãy theo dõi phần trăm thời gian SRE dành cho lao động nhàm chán và đặt trần, thường khoảng 50 phần trăm, để ít nhất một nửa thời gian kỹ thuật của bạn đi vào các cải thiện bền vững. Giữ tồn đọng các dự án giảm lao động nhàm chán, ưu tiên theo tần suất nhân chi phí, và ăn mừng việc giết một tác vụ lặp lại ngang với phát hành tính năng mới. Một **sứ mệnh tự động hóa** làm điều này tường minh: bất kỳ quy trình thủ công nào bạn thực hiện nhiều hơn một số lần đặt trước trở thành ứng viên cho tự động hóa hoặc công cụ tự phục vụ.

### Hoạch định năng lực và dự báo nhu cầu

Hãy mô hình hóa tải kỳ vọng của bạn từ xu hướng lịch sử, lần ra mắt có kế hoạch và dự phóng kinh doanh. Kết hợp dự báo tăng trưởng tự nhiên với sự kiện một lần như chiến dịch tiếp thị, hạn nộp thuế, hay kỳ ghi danh trợ cấp, vốn quan trọng lớn trong chính phủ. Giữ dư địa trên đỉnh, kiểm thử tải để kiểm tra các giả định, và tự động hóa co giãn nơi có thể trong khi giữ một [kế hoạch năng lực](https://en.wikipedia.org/wiki/Capacity_planning) được con người rà soát cho các cam kết lớn. Theo dõi thời gian chờ cung cấp để một sự thiếu hụt không bao giờ bắt bạn bất ngờ.

### Coi độ tin cậy là tính năng có chi phí thực

Mỗi "số chín" sẵn sàng thêm thường tốn nhiều hơn hẳn về dư thừa, kiểm thử và độ tinh vi vận hành so với cái trước. Hãy làm chi phí của các số chín tường minh, để chủ sản phẩm chọn mục tiêu với mắt mở. Thiết kế cho suy giảm êm, để thất bại một phần cho dịch vụ giảm thay vì ngừng hoạt động hoàn toàn. Đầu tư dư thừa và chuyển dự phòng tương xứng với SLO, không đồng đều qua mọi thành phần.

### Chọn mô hình tổ chức SRE

Không có cấu trúc đúng duy nhất. Một đội SRE **tập trung** cho bạn tính nhất quán, chuyên môn sâu và công cụ dùng chung, nhưng nó có thể thành nút thắt hoặc bãi rác cho vấn đề của người khác. Mô hình **nhúng** đặt SRE bên trong các đội sản phẩm để cộng tác chặt chẽ, nhưng rủi ro không nhất quán và cô lập. Nhiều tổ chức lớn dùng mô hình lai: một đội nền tảng và tiêu chuẩn trung tâm cộng kỹ sư độ tin cậy nhúng, với mô hình tham gia rõ ràng xác định khi nào một dịch vụ đủ điều kiện nhận hỗ trợ SRE và thanh sẵn sàng sản xuất nào nó phải vượt trước.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| SLO chặt (nhiều số chín hơn) | Lòng tin người dùng cao hơn, đáp ứng hợp đồng | Chi phí tăng, phân phối tính năng chậm hơn |
| SLO lỏng (ít số chín hơn) | Phát hành nhanh hơn, chi phí thấp hơn | Rủi ro người dùng rời bỏ và phạt SLA |
| SRE tập trung | Nhất quán, chuyên môn dùng chung | Nút thắt, xa sản phẩm |
| SRE nhúng | Cộng tác chặt chẽ, ngữ cảnh | Không nhất quán, khó bố trí nhân sự |
| Đầu tư tự động hóa nặng | Mở rộng, giảm lao động nhàm chán | Chi phí ban đầu, tự động hóa cũng có thể hỏng |

Kỹ thuật độ tin cậy thực ra là tiêu nguồn lực hữu hạn một cách khôn ngoan. Đuổi theo một số chín thêm mà người dùng thậm chí không cảm nhận được lãng phí tiền có thể tài trợ tính năng hoặc hạ giá. Đi hướng ngược lại và đầu tư thiếu vào một hệ thống mà thất bại gây hại thật, đó là cẩu thả. Khung ngân sách lỗi tồn tại chính để làm đánh đổi này hiển thị và thương lượng được thay vì ngầm và gây tranh cãi. Đánh đổi mô hình tổ chức cũng thật như vậy: câu trả lời đúng phụ thuộc vào quy mô công ty, độ trưởng thành kỹ thuật, và dịch vụ của bạn đồng đều đến đâu.

## Câu hỏi để thảo luận với đội của bạn

1. **SLI chính xác nào phản ánh điều người dùng của bạn thực sự cảm nhận, và bạn có chứng minh được nó không phải chỉ số phù phiếm?** Chọn sai chỉ báo và mọi bảng điều khiển đều xanh trong khi người dùng chịu khổ, là cái bẫy SLI phù phiếm mà chương này cảnh báo. Hãy mang dữ liệu thật vào cuộc thảo luận: đo cùng một hành trình người dùng từ một đường yêu cầu thật (đăng nhập đến bảng điều khiển, thanh toán đến xác nhận) thay vì CPU máy chủ hay kiểm tra sức khỏe backend. Với một đội lớn, một SLI tồi lan truyền: hàng chục dịch vụ thừa hưởng nó, cảnh báo kích hoạt trên sai thứ, và ngân sách lỗi thôi có nghĩa. Trong bối cảnh doanh nghiệp và chính phủ nơi một SLA mang hoàn tiền hay tác động công dân, SLI của bạn là bằng chứng bạn bảo vệ trước kiểm toán viên, nên nó phải truy trực tiếp về thành công người dùng nhìn thấy. Nếu bạn không vẽ được đường từ con số đến trải nghiệm của người dùng, hãy thay con số.

2. **Một dịch vụ phải chứng minh gì trước khi đội SRE của bạn nhận trực ca nó, và ai nói không?** Không có thanh sẵn sàng sản xuất, một đội SRE trung tâm thành bãi rác cho mọi dịch vụ không ổn định và chìm trong nợ kỹ thuật của người khác. Hãy viết ra tiêu chí đầu vào: một SLO có chủ, sổ tay vận hành hoạt động, cảnh báo hành động được, dư địa năng lực, và một đường triển khai-và-hoàn-tác đã chứng minh. Với một tổ chức lớn mô hình tham gia này là thứ giữ đội độ tin cậy khỏi thành nút thắt làm chậm mọi người. Trong bối cảnh chịu quy định, rà soát sẵn sàng đồng thời là một kiểm soát bạn trình cho cơ quan giám sát. Hãy quyết định ai nắm thẩm quyền từ chối làm quen, vì một thanh không ai thực thi không phải là thanh, và câu trả lời thay đổi liệu SRE mở rộng hay sụp đổ dưới nỗi đau thừa kế.

3. **Bạn cung cấp trước bao lâu cho đỉnh dự đoán được lớn nhất của mình, và bạn có biết thời gian chờ cung cấp không?** Giả định tính đàn hồi đám mây là tức thì và vô hạn mời gọi thiếu hụt trong chính những đỉnh quan trọng nhất, và những đỉnh đó (hạn thuế, kỳ ghi danh, sự kiện giảm giá) là những khoảnh khắc thất bại hiển thị nhất và tốn kém nhất. Hãy mang con số: tải đỉnh lịch sử, tăng trưởng dự báo, bội số bạn kiểm thử tải đến, và thời gian chờ thực để có được năng lực đặt trước lớn hoặc thể hiện chuyên biệt. Với dịch vụ theo mùa của chính phủ, đỉnh có thể gấp nhiều lần tải bình thường và không thể bỏ lỡ về chính trị, nên cung cấp trước vài tuần thắng hy vọng co giãn tự động theo kịp. Câu trả lời nên đặt một lịch cụ thể: khi nào bạn kiểm thử tải, khi nào bạn khóa năng lực, và ai sở hữu quyết định đi.

4. **Khi ngân sách lỗi của bạn cạn, điều gì thực sự xảy ra, và ai có tư cách thực thi nó?** Một ngân sách lỗi không bao giờ được hành động khi cạn chỉ là đồ trang trí, và khoảnh khắc ngừng hoạt động là lúc tệ nhất để thương lượng chính sách từ đầu. Lực kéo đối lập là thật: một lần ra mắt đã cam kết, hạn doanh thu, hay thông báo công khai sẽ ép mạnh lên một lần đóng băng thay đổi rủi ro. Hãy mang dữ liệu tốc độ đốt, văn bản chính sách đã thống nhất trước, và bản ghi vài lần gần đây ngân sách bị vi phạm, để bạn thấy liệu lần đóng băng có thực sự giữ. Với một đội lớn ngân sách chỉ căn chỉnh khuyến khích nếu mọi nhóm thừa hưởng cùng sự thực thi, nên hãy quyết định trước ai ký duyệt một lần ghi đè và ngoại lệ đó được ghi thế nào. Trong bối cảnh doanh nghiệp và chính phủ nơi một SLA mang phạt hay tác động công dân, dấu vết ghi đè thành hiện vật kiểm toán, nên hãy nêu chủ sở hữu chịu trách nhiệm ngay bây giờ thay vì ứng biến khi ngân sách đã hết.

5. **Phần nào trong tuần của đội SRE là lao động nhàm chán, và đó là con số được đo hay cảm giác?** Lao động nhàm chán không ai đếm lặng lẽ nở ra cho đến khi đội dành toàn bộ thời gian chữa cháy và không xây cải thiện bền vững, chính là cái bẫy mà SRE tồn tại để thoát. Căng thẳng là đo lao động nhàm chán tự nó là công việc, và kỹ sư dưới áp lực hạn chót chống lại việc ghi giờ của họ đi đâu. Hãy mang một mẫu trung thực: một hai tuần thời gian được theo dõi so với định nghĩa chung về lao động nhàm chán (thủ công, lặp lại, tự động hóa được, chiến thuật, và mở rộng theo hệ thống), cộng tồn đọng các dự án tự động hóa xếp hạng theo tần suất nhân chi phí. Với một tổ chức lớn trần 50 phần trăm chỉ có nghĩa nếu nó được báo cáo và bảo vệ từng đội, nên hãy thống nhất ai rà soát con số và điều gì xảy ra khi một đội vi phạm nó. Trong bối cảnh chịu quy định và chính phủ, giới hạn lao động nhàm chán giải phóng chuyên gia khan hiếm cho công việc kiểm soát và kiểm toán mà vận hành thủ công chèn ép, nên hãy coi con số lao động nhàm chán là tín hiệu năng lực mà lãnh đạo nên thấy.

6. **Bạn chạy mô hình tổ chức SRE nào, và bằng chứng nào sẽ cho bạn biết nó đã thôi phù hợp?** Một đội tập trung cho tính nhất quán và công cụ dùng chung nhưng có thể thành nút thắt; mô hình nhúng cho ngữ cảnh nhưng trôi vào không nhất quán; mô hình lai mà hầu hết tổ chức lớn đáp xuống cần một mô hình tham gia rõ ràng nếu không nó thừa hưởng điểm yếu của cả hai. Hãy mang các tín hiệu cho thấy căng thẳng: dịch vụ chờ hỗ trợ SRE bao lâu, thực hành độ tin cậy khác nhau bao nhiêu giữa các đội, và kỹ sư nhúng có cảm thấy bị cắt khỏi cộng đồng chuyên môn không. Câu trả lời đúng phụ thuộc vào quy mô công ty, độ trưởng thành kỹ thuật, và dịch vụ của bạn đồng đều đến đâu, nên hãy xem xét lại khi những thứ đó đổi thay vì coi lựa chọn đầu tiên là vĩnh viễn. Với một cơ quan doanh nghiệp hay chính phủ nhiều đội và yêu cầu đồng nhất nghiêm ngặt, một nhóm tiêu chuẩn-và-nền-tảng trung tâm cộng kỹ sư độ tin cậy nhúng thường cân bằng nhất quán với ngữ cảnh cục bộ, nhưng chỉ khi mô hình tham gia và thanh sẵn sàng sản xuất được viết ra và có người sở hữu.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không có đường băng cho đội độ tin cậy chuyên trách, hãy chọn một SLO trên hành trình người dùng quan trọng nhất và chia sẻ trực ca qua cả đội. Dựa vào dịch vụ được quản lý và giám sát dựng sẵn của nhà cung cấp đám mây thay vì xây hạ tầng quan sát, và viết rút kinh nghiệm ngắn trong tài liệu chung để bản sửa bám. Tốc độ quan trọng hơn quy trình ở đây: một SLO lỏng bạn thực sự thực thi thắng một cái cầu kỳ không ai theo dõi.

**Doanh nghiệp nhỏ.** Không có chuyên gia chạy độ tin cậy, hãy coi nó là kỷ luật bạn mua vào qua nền tảng của mình: giám sát thời gian hoạt động lưu trữ, cơ sở dữ liệu được quản lý, và công cụ trang trạng thái thay vì một ngăn xếp đặt riêng. Đặt một hai SLO gắn với các giao dịch trả hóa đơn, và quyết định trung thực thất bại nào sẽ tốn bạn một khách hàng. Mua khả năng phục hồi nơi nó rẻ hơn xây, và giữ gánh nặng vận hành đủ nhẹ để các kỹ sư hiện có của bạn gánh được cùng công việc tính năng.

**Doanh nghiệp lớn.** Thách thức là nhất quán qua nhiều đội: một từ vựng SLO dùng chung, một chính sách ngân sách lỗi chung, và một thanh sẵn sàng sản xuất mà mọi dịch vụ vượt trước khi SRE nhận trực ca. Một nhóm nền tảng-và-tiêu-chuẩn trung tâm cộng kỹ sư độ tin cậy nhúng giữ thực hành đồng đều mà không thành nút thắt, và quản trị cần ngân sách lỗi được báo cáo và thực thi giống nhau ở mọi nơi. Hãy lập ngân sách tường minh cho hạ tầng quan sát và khoản đầu tư tự động hóa, và quản lý độ tin cậy như một danh mục với chỉ số mà lãnh đạo thấy được.

**Chính phủ.** Dịch vụ công thường mang mục tiêu sẵn sàng đã công bố, cam kết theo luật và nghĩa vụ kiểm toán, nên SLO và quyết định ngân sách lỗi trở thành hồ sơ bạn bảo vệ trước cơ quan giám sát. Quy tắc mua sắm có thể ràng buộc giám sát và lưu trữ bạn dùng được, và kỳ vọng minh bạch đẩy bạn công bố dữ liệu độ tin cậy trên một bảng điều khiển trạng thái công khai. Hãy lên kế hoạch cho đỉnh theo mùa cực đoan như hạn thuế và kỳ ghi danh trợ cấp trước nhiều tuần, và giữ văn hóa rút kinh nghiệm không đổ lỗi để thất bại công khai thúc đẩy cải thiện hệ thống thay vì đổ lỗi cá nhân.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười người chạy một ứng dụng web duy nhất và chia sẻ trực ca qua ba kỹ sư. Thay vì xây đội độ tin cậy họ không gánh nổi, họ chọn một SLO có ý nghĩa: 99,5 phần trăm thành công trên luồng đăng nhập-đến-bảng-điều-khiển, đo từ yêu cầu người dùng thật. Khi một API bên thứ ba chập chờn bắt đầu ăn ngân sách đó, đội dành một ngày thứ Sáu thêm một lần thử lại và bộ nhớ đệm thay vì phát hành tính năng kế tiếp, rồi viết một bản rút kinh nghiệm hai đoạn trong tài liệu chung để bản sửa bám.

**Doanh nghiệp lớn.** Một công ty thanh toán toàn cầu đặt SLO sẵn sàng 99,99 phần trăm cho API giao dịch của mình, cho ngân sách lỗi khoảng bốn phút mỗi tháng. Một đội nền tảng SRE trung tâm sở hữu [khả năng quan sát](https://en.wikipedia.org/wiki/Observability_(software)) dùng chung, công cụ sự cố và chính sách ngân sách lỗi, trong khi kỹ sư độ tin cậy nhúng làm việc bên trong mỗi nhóm sản phẩm. Khi một tính năng phát hiện gian lận mới đốt một nửa ngân sách hằng tháng trong một tuần, chính sách đã thống nhất trước đóng băng các bản phát hành không trọng yếu cho đến khi công việc độ tin cậy phục hồi dư địa. Ban điều hành chấp nhận điều này không tranh cãi, vì họ đã phê chuẩn chính sách từ trước.

**Chính phủ.** Một cơ quan thuế quốc gia chạy dịch vụ khai thuế trực tuyến với đỉnh theo mùa cực đoan quanh hạn hằng năm. Đội SRE của nó dự báo nhu cầu từ các năm trước cộng thay đổi dân số và chính sách, kiểm thử tải đến nhiều lần đỉnh bình thường, và cung cấp trước năng lực nhiều tuần. SLO hướng công chúng về tính sẵn sàng và độ trễ trang lên một bảng điều khiển trạng thái. Văn hóa [rút kinh nghiệm](https://en.wikipedia.org/wiki/Postmortem_documentation) không đổ lỗi (rà soát thất bại để cải thiện hệ thống thay vì quy lỗi cá nhân) và sứ mệnh tự động hóa đều đặn cắt các can thiệp thủ công từng chi phối mùa khai thuế, giải phóng nhân viên để cải thiện hệ thống thay vì chăm sóc nó qua mỗi hạn.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của SRE đến từ ba nguồn: ngừng hoạt động tránh được, ít lao động vận hành hơn, và phân phối an toàn nhanh hơn. Ngừng hoạt động của một dịch vụ lớn có thể tốn hàng nghìn đến hàng triệu mỗi giờ doanh thu mất, tiền phạt và khắc phục, nên ngay cả cải thiện độ tin cậy khiêm tốn cũng nhanh chóng trả giá cho một đội. Giảm lao động nhàm chán biến chi phí thủ công lặp lại thành khoản đầu tư tự động hóa một lần, nên tổng chi phí sở hữu giảm khi quy mô lớn lên thay vì leo theo nó. Ngân sách lỗi cho doanh nghiệp phát hành nhanh hơn khi độ tin cậy khỏe, nắm bắt giá trị tính năng mà vận hành quá thận trọng sẽ bỏ lại.

Chi phí áp dụng là thật. SRE cần kỹ sư có kỹ năng, hạ tầng quan sát, và thay đổi văn hóa cạnh tranh với hạn chót tính năng. Nhưng chi phí của việc không áp dụng cao hơn ở quy mô: nhân sự vận hành không giới hạn, ngừng hoạt động khó đoán, nhân viên kiệt sức và nghỉ việc, và thiệt hại danh tiếng khó định lượng nhưng dễ chịu. Để lập luận với ban lãnh đạo, hãy đóng khung SRE là quản lý rủi ro với lợi tức đo được. Trình bày chi phí hiện tại của sự cố và vận hành thủ công, các mục tiêu SLO gắn với cam kết kinh doanh, và mức giảm dự kiến của cả hai. Neo lập luận vào ngân sách lỗi như công cụ quản trị cho lãnh đạo một đòn bẩy trên đánh đổi giữa độ tin cậy và vận tốc.

## Phản mẫu và cạm bẫy

- **SRE như vận hành đổi tên.** Đổi tên một đội vận hành mà không có thời gian kỹ thuật, sứ mệnh tự động hóa và thẩm quyền phản đối thì không đổi gì.
- **Nhắm đến 100 phần trăm.** Đuổi theo độ tin cậy hoàn hảo lãng phí tiền và chặn phân phối vì lợi ích người dùng không cảm nhận được.
- **SLI phù phiếm.** Đo CPU máy chủ thay vì thành công người dùng nhìn thấy cho con số trông tốt trong khi người dùng chịu khổ.
- **Ngân sách lỗi không có răng.** Một ngân sách không bao giờ được thực thi khi cạn chỉ là đồ trang trí.
- **Lao động nhàm chán không đo.** Nếu bạn không theo dõi lao động nhàm chán, nó lặng lẽ ngốn đội cho đến khi không còn công việc cải thiện nào xảy ra.
- **SRE như bãi rác.** Các đội tập trung thừa hưởng mọi dịch vụ không ổn định mà không có thanh sẵn sàng chìm trong nợ kỹ thuật của người khác.
- **Phớt lờ thời gian chờ năng lực.** Giả định tính đàn hồi đám mây tức thì và vô hạn mời gọi thiếu hụt trong chính những đỉnh quan trọng nhất.

## Mô hình trưởng thành

**Mức 1, Khởi đầu.** Vận hành thủ công và phản ứng. Không có SLO chính thức, độ tin cậy là vấn đề ý kiến, và cùng sự cố tái diễn trong khi chữa cháy chi phối. Mọi tự động hóa là tình cờ, và không ai sở hữu độ tin cậy như mối quan tâm kỹ thuật.

**Mức 2, Phát triển.** Một số dịch vụ có SLI và SLO cơ bản cùng giám sát và cảnh báo thô sơ, nhưng thực hành khác nhau nhiều giữa các đội. Lao động nhàm chán được thừa nhận nhưng không đo, tự động hóa tùy nghi, và rút kinh nghiệm diễn ra không nhất quán. Độ tin cậy cải thiện ở những túi nơi cá nhân thúc đẩy nó, không phải vì tổ chức đòi hỏi.

**Mức 3, Chuẩn hóa.** SLI, SLO và chính sách ngân sách lỗi được lập tài liệu và áp dụng nhất quán qua các đội. Lao động nhàm chán được xác định và theo dõi, hoạch định năng lực là thường lệ, mô hình tham gia SRE với rà soát sẵn sàng sản xuất tồn tại, và tự động hóa là luồng công việc được tài trợ thay vì dự án phụ. Thực hành độ tin cậy được viết ra và thực thi toàn tổ chức.

**Mức 4, Quản lý.** Chương trình độ tin cậy được đo và kiểm soát bằng dữ liệu theo đường cơ sở. Tốc độ đốt ngân sách lỗi, phần trăm lao động nhàm chán, mức đạt SLO, thời gian phục hồi trung bình và thời gian chờ cung cấp được theo dõi như chỉ số, rà soát theo nhịp cố định, và dùng để giữ các đội theo mục tiêu. Vi phạm ngân sách kích hoạt lần đóng băng đã thống nhất, năng lực được dự báo theo mô hình nhu cầu, và mỗi quyết định tiếp tục hay dừng dựa trên bằng chứng thay vì ý kiến.

**Mức 5, Điều phối.** Kỹ thuật độ tin cậy được tích hợp trong toàn tổ chức và cải thiện liên tục. Chính sách ngân sách lỗi được tự động hóa và tôn trọng ở mọi nơi, hầu hết vận hành là tự phục vụ, năng lực được cung cấp chủ động, và dữ liệu độ tin cậy thúc đẩy đánh đổi thích ứng giữa vận tốc và ổn định. Tổ chức thường xuyên thu hẹp phạm vi SLO, cho nghỉ hưu lao động nhàm chán, và cân bằng lại đầu tư độ tin cậy khi doanh nghiệp và bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

- Một tổ chức nên đặt SLO đầu tiên thế nào khi nó không có dữ liệu độ tin cậy lịch sử để neo?
- Khi ngân sách lỗi cạn nhưng một lần ra mắt lớn đã cam kết, ai có thẩm quyền ghi đè lần đóng băng, và quyết định đó được ghi lại thế nào?
- Mô hình SRE tập trung, nhúng hay lai phù hợp với tổ chức của bạn, và cái gì sẽ kích hoạt thay đổi?
- Bạn định giá một số chín sẵn sàng thêm so với các tính năng mà cùng khoản đầu tư có thể tài trợ thế nào?
- Cái gì được tính là lao động nhàm chán trong bối cảnh của bạn, và lằn ranh giữa phán đoán thủ công có giá trị và sự lặp lại loại bỏ được nằm ở đâu?
- Mục tiêu độ tin cậy nên khác nhau thế nào giữa dịch vụ chính phủ hướng công dân và công cụ doanh nghiệp nội bộ?

## Những điểm cần ghi nhớ

- SRE áp dụng kỹ thuật phần mềm vào vận hành, coi độ tin cậy là tính năng đo được, tài trợ được.
- SLI, SLO và SLA biến độ tin cậy từ ý kiến thành con số đã thống nhất; giữ SLO chặt hơn SLA.
- Ngân sách lỗi căn chỉnh lập trình viên và người vận hành bằng cách làm đánh đổi độ tin cậy-so-với-vận-tốc tường minh và được thương lượng trước.
- Đo và giới hạn lao động nhàm chán, và coi tự động hóa là kỹ thuật hạng nhất để vận hành mở rộng dưới tuyến tính.
- Hoạch định năng lực từ dự báo nhu cầu và tôn trọng thời gian chờ cung cấp, đặc biệt cho đỉnh theo mùa.
- Chọn mô hình tổ chức SRE có chủ đích và xác định mô hình tham gia rõ ràng cùng thanh sẵn sàng sản xuất.

## Tài liệu tham khảo và đọc thêm

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (biên tập), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
