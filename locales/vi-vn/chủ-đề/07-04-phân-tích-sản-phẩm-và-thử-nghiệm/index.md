# 7.4 Phân tích sản phẩm và thử nghiệm

## Tổng quan và động lực

Phân tích sản phẩm là thực hành hiểu người ta thực sự dùng một sản phẩm thế nào bằng cách nắm bắt và phân tích hành vi của họ: họ chạm vào tính năng nào, họ thành công ở đâu, họ rời bỏ ở đâu, và điều gì giữ họ quay lại. Thử nghiệm là kỷ luật thiết lập quan hệ nhân quả bằng cách chạy các thử nghiệm có đối chứng, phổ biến nhất là [thử nghiệm A/B](https://en.wikipedia.org/wiki/A/B_testing) (so sánh ngẫu nhiên đối đầu giữa hai biến thể), để bạn đánh giá thay đổi sản phẩm bằng tác động thực của chúng thay vì bằng ý kiến hay trực giác. Cùng nhau chúng chuyển quyết định sản phẩm từ "chúng tôi nghĩ" sang "chúng tôi biết," hay ít nhất là "chúng tôi đã đo."

Với các đội lớn, những thực hành này mang tính quyết định. Khi hàng chục nhóm phát hành thay đổi cho một sản phẩm được hàng triệu người dùng, trực giác không có định hướng tạo ra một dòng thay đổi mà tác động ròng không ai đo được, và giọng to nhất thắng những cuộc tranh cãi mà dữ liệu nên giải quyết. Doanh nghiệp dùng thử nghiệm để bảo vệ doanh thu và chuyển đổi ở quy mô, bắt các thay đổi có hại trước khi triển khai đầy đủ. Các dịch vụ số của chính phủ ngày càng dùng các phương pháp tương tự để cải thiện mức tiếp nhận và hoàn thành các dịch vụ thiết yếu (đơn xin trợ cấp, khai thuế, gia hạn giấy phép), nơi một cải thiện nhỏ về tỷ lệ hoàn thành chuyển thành lợi ích lớn về kết quả của công dân và giảm tải tổng đài.

Giá trị của phân tích sản phẩm phụ thuộc hoàn toàn vào chất lượng gắn công cụ đo và độ chặt chẽ của phân tích. Theo dõi sự kiện cẩu thả tạo ra dữ liệu không ai tin. Thử nghiệm chạy kém tạo ra kết luận tự tin nhưng sai. Và vì dữ liệu này mang tính hành vi và thường cá nhân, bạn phải thu thập nó theo cách tôn trọng quyền riêng tư và nhận biết sự đồng ý, một yêu cầu pháp lý ở nhiều khu vực pháp lý và nghĩa vụ đạo đức ở mọi nơi. Chương này bao quát gắn công cụ đo, các phân tích hành vi cốt lõi, thử nghiệm chặt chẽ, chọn chỉ số quan trọng, và làm tất cả một cách tôn trọng.

## Các nguyên tắc chính

- Gắn công cụ đo có chủ đích với một kế hoạch theo dõi có tài liệu và phân loại nhất quán.
- Ưu tiên thử nghiệm có đối chứng hơn ý kiến cho các câu hỏi nhân quả.
- Sự chặt chẽ thống kê là không thể thương lượng; các thử nghiệm thiếu năng lực hoặc bị nhìn trộm gây hiểu lầm.
- Neo vào một chỉ số sao bắc đẩu gắn với giá trị thực, không phải số phù phiếm.
- Đo [giữ chân](https://en.wikipedia.org/wiki/Customer_retention) và mức độ tương tác, không chỉ thu hút.
- Thu thập dữ liệu hành vi tối thiểu cần thiết, với sự đồng ý rõ ràng.
- Coi gắn công cụ đo là sản phẩm có chủ sở hữu và kiểm tra chất lượng.
- Một kết quả thử nghiệm âm hoặc phẳng là phát hiện có giá trị, không phải thất bại.

## Khuyến nghị

### Gắn công cụ đo với kế hoạch theo dõi và phân loại

Trước khi thêm sự kiện, hãy thiết kế một kế hoạch theo dõi: các sự kiện bạn sẽ nắm bắt, thuộc tính của chúng, quy ước đặt tên, và các câu hỏi mỗi cái trả lời. Thực thi một phân loại nhất quán (một sơ đồ đặt tên ổn định cho sự kiện và thuộc tính) để dữ liệu vẫn phân tích được qua các đội và thời gian. Hãy coi kế hoạch theo dõi như lược đồ được quản trị: đánh phiên bản, rà soát thay đổi, và xác thực sự kiện theo nó, để bạn bắt các sự kiện sai định dạng hay bất ngờ lúc thu nạp thay vì phát hiện chúng như những khoảng trống nhiều tháng sau. Không có kỷ luật này, dữ liệu sản phẩm trở thành một mớ không dùng được gồm sự kiện không nhất quán, trùng lặp và không tài liệu.

### Phân tích phễu, nhóm đối tượng, giữ chân và tương tác

Hãy dùng phễu để thấy người dùng rời bỏ ở đâu trong các luồng then chốt và nhắm cải thiện. Dùng [phân tích nhóm đối tượng](https://en.wikipedia.org/wiki/Cohort_analysis) để so sánh các nhóm được xác định theo khi nào họ gia nhập hoặc họ đã làm gì, điều tiết lộ liệu thay đổi có thực sự cải thiện hành vi theo thời gian. Đo giữ chân (người dùng có quay lại không) vì thu hút mà không giữ chân là một cái xô rò. Mô tả mức độ tương tác trung thực, với định nghĩa có ý nghĩa về người dùng hoạt động thay vì số đếm tâng bốc. Những phân tích này, đặt trên nền gắn công cụ đo sạch, cho bạn biết điều gì thực sự đang xảy ra trong sản phẩm.

### Chạy thử nghiệm chặt chẽ

Với các câu hỏi nhân quả, hãy chạy thử nghiệm có đối chứng: gán ngẫu nhiên người dùng vào các biến thể và so sánh kết quả. Sự chặt chẽ đòi hỏi vài kỷ luật. Tính cỡ mẫu và thời lượng cần cho [năng lực thống kê](https://en.wikipedia.org/wiki/Power_%28statistics%29) đầy đủ trước khi bắt đầu. Đừng dừng sớm chỉ vì một kết quả trông có ý nghĩa: nhìn trộm làm tăng dương tính giả. Xác định trước chỉ số chính và giả thuyết của bạn, để tránh câu cá tìm kết quả có ý nghĩa nào đó qua nhiều chỉ số. Kiểm tra rằng việc ngẫu nhiên hóa vững chắc và các chỉ số lan can (hiệu năng, doanh thu, khiếu nại) không bị hại. Dùng một nền tảng thử nghiệm để chuẩn hóa việc gán, phân tích và lan can, để mọi đội chạy các thử nghiệm vững chắc thay vì phát minh lại thống kê một cách tồi.

### Chọn chỉ số sao bắc đẩu và tránh chỉ số phù phiếm

Hãy chọn một chỉ số sao bắc đẩu nắm bắt giá trị cốt lõi sản phẩm mang lại cho người dùng, và báo hiệu thành công thực khi nó tăng, không phải số phù phiếm tăng mà không có giá trị tương ứng. Tổng số người dùng đăng ký, lượt xem trang thô và tổng lượt tải là các chỉ số phù phiếm kinh điển: chúng chỉ đi lên và hiếm khi phản ánh sức khỏe. Ưu tiên các chỉ số gắn với giá trị được giao và giữ lại, và bao quanh sao bắc đẩu bằng một tập nhỏ chỉ số đầu vào mà các đội thực sự ảnh hưởng được. Cẩn thận đừng tối ưu một đại diện quá mạnh đến mức làm hại mục tiêu thật.

### Tôn trọng quyền riêng tư và sự đồng ý

Dữ liệu hành vi là dữ liệu cá nhân. Chỉ thu thập những gì bạn cần cho một mục đích xác định, có được và tôn trọng sự đồng ý theo yêu cầu của luật, và trao cho người dùng sự minh bạch và quyền kiểm soát. Ưu tiên phân tích tổng hợp và giả danh hóa nơi chúng đủ, tối thiểu hóa lưu giữ, và áp dụng cùng quản trị, phân loại và kiểm soát truy cập như bất kỳ tập dữ liệu nhạy cảm nào. Tôn trọng quyền riêng tư làm nhiều hơn thỏa mãn các chế độ như [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (Quy định Bảo vệ Dữ liệu Chung của EU): nó duy trì lòng tin của người dùng mà sản phẩm phụ thuộc vào. Hãy thiết kế phân tích để một người dùng từ chối theo dõi vẫn có một sản phẩm hoạt động.

### Coi gắn công cụ đo và thử nghiệm là sản phẩm

Hãy giao cho gắn công cụ đo một chủ sở hữu chịu trách nhiệm về chất lượng, độ phủ và tài liệu của nó, và giám sát sự kiện hỏng hoặc thiếu như bạn giám sát đường ống. Xây một văn hóa thử nghiệm với nền tảng dùng chung, rà soát thiết kế thử nghiệm, và một kho các kết quả trước đây để tổ chức học tích lũy thay vì lặp lại thử nghiệm và quên kết quả.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Gắn công cụ đo nặng | Hiểu biết hành vi phong phú | Chi phí, phơi nhiễm quyền riêng tư, nhiễu | Sản phẩm dựa trên dữ liệu |
| Gắn công cụ đo tối thiểu | Rẻ, rủi ro quyền riêng tư thấp | Điểm mù, phân tích yếu | Sản phẩm giai đoạn đầu hoặc rủi ro thấp |
| Thử nghiệm A/B | Chắc chắn nhân quả, bảo vệ chỉ số | Cần lưu lượng, thời gian, sự chặt chẽ | Sản phẩm lưu lượng cao |
| Phát hành-và-quan-sát | Nhanh, không ngưỡng lưu lượng | Bị nhiễu, không có nhân quả | Thay đổi lưu lượng thấp hoặc đảo ngược được |
| Tập trung sao bắc đẩu | Căn chỉnh, ưu tiên rõ ràng | Đơn giản hóa quá mức, rủi ro thao túng | Hầu hết đội sản phẩm |
| Nhiều KPI | Sắc thái | Tập trung phân tán, mục tiêu xung đột | Tổ chức phân tích trưởng thành |

Đánh đổi trung tâm là tốc độ so với sự chắc chắn, được trung gian bởi lưu lượng. Thử nghiệm cho sự chắc chắn nhân quả, nhưng chúng đòi đủ người dùng và đủ kiên nhẫn để đạt năng lực thống kê. Với các tính năng lưu lượng thấp hoặc thay đổi rõ ràng đảo ngược được, phát hành-và-quan-sát có kỷ luật có thể thực dụng. Gắn công cụ đo đánh đổi hiểu biết lấy chi phí và phơi nhiễm quyền riêng tư, nên hãy thu thập có mục đích thay vì tích trữ. Và một chỉ số sao bắc đẩu đánh đổi sắc thái lấy căn chỉnh: mạnh cho tập trung, nguy hiểm nếu bị thao túng, nên hãy ghép nó với lan can.

## Câu hỏi để thảo luận với đội của bạn

1. **Ai sở hữu kế hoạch theo dõi của bạn, và bạn có xác thực sự kiện theo nó lúc thu nạp để dữ liệu sai định dạng thất bại nhanh thay vì nổi lên như khoảng trống nhiều tháng sau không?** Chương coi kế hoạch theo dõi như lược đồ được quản trị: có phiên bản, được rà soát, được xác thực, với phân loại nhất quán để dữ liệu vẫn phân tích được qua các đội và thời gian. Không có kỷ luật đó, dữ liệu sản phẩm thoái hóa thành một mớ không dùng được gồm sự kiện không nhất quán, trùng lặp và không tài liệu, và bạn chỉ phát hiện các lỗ hổng khi cố trả lời một câu hỏi. Với một sản phẩm có hàng chục nhóm chạm vào và hàng triệu người dùng, một kế hoạch theo dõi không chủ sở hữu nghĩa là mỗi đội đặt tên sự kiện khác nhau và không phân tích xuyên đội nào đứng vững. Hãy mang bằng chứng: chọn một phễu then chốt và kiểm tra liệu các sự kiện của nó có được lập tài liệu và đặt tên nhất quán. Nếu quyền sở hữu không rõ, hãy giao nó, và giám sát sự kiện hỏng hoặc thiếu như bạn giám sát đường ống.

2. **Mọi đội của bạn có chạy thử nghiệm qua một nền tảng dùng chung với tính toán năng lực và lan can, hay mỗi đội phát minh lại thống kê một cách tồi?** Chương nói thẳng rằng sự chặt chẽ là không thể thương lượng: tính cỡ mẫu và thời lượng cho năng lực thống kê đầy đủ trước khi bắt đầu, xác định trước chỉ số chính và giả thuyết, không nhìn trộm và dừng sớm, và theo dõi các chỉ số lan can như hiệu năng, doanh thu và khiếu nại. Một nền tảng thử nghiệm dùng chung chuẩn hóa việc gán, phân tích và lan can để mọi đội chạy các thử nghiệm vững chắc thay vì mỗi nhóm nhìn trộm cho đến khi gì đó trông có ý nghĩa. Với các sản phẩm doanh nghiệp lưu lượng cao, một lần ngăn được một bản ra mắt tồi (một thiết kế lại lặng lẽ hại việc giữ chân) có thể tự trả giá cho cả chương trình. Hãy mang một tín hiệu: các đội hiện có tính năng lực, hay dừng khi kết quả trông tốt? Nếu là cái sau, một nền tảng chung và rà soát thiết kế là cách sửa.

3. **Sản phẩm của bạn vẫn hoạt động thế nào với người dùng từ chối theo dõi, và bạn có chỉ thu thập dữ liệu hành vi tối thiểu cho một mục đích xác định không?** Chương coi dữ liệu hành vi là dữ liệu cá nhân: chỉ thu thập những gì một mục đích xác định cần, có được và tôn trọng sự đồng ý theo luật, tối thiểu hóa lưu giữ, và áp dụng cùng phân loại và kiểm soát truy cập như bất kỳ tập dữ liệu nhạy cảm nào. Tôn trọng điều này duy trì lòng tin của người dùng mà sản phẩm phụ thuộc, và theo GDPR và các chế độ tương tự đó là yêu cầu pháp lý, không phải phép lịch sự. Áp lực đối lập là thôi thúc gắn công cụ đo nặng để có hiểu biết phong phú hơn, làm tăng chi phí, nhiễu và phơi nhiễm quyền riêng tư. Hãy mang bằng chứng: liệt kê những gì bạn thu thập và gắn mỗi sự kiện với câu hỏi nó trả lời, rồi kiểm tra rằng từ chối theo dõi vẫn cho một sản phẩm hoạt động. Nếu một số thu thập không có mục đích hoặc làm hỏng trải nghiệm, hãy cắt nó, và thiết kế phân tích để suy giảm êm cho người dùng chọn không tham gia.

4. **Chỉ số sao bắc đẩu duy nhất nào nắm bắt giá trị sản phẩm của bạn mang lại, và làm sao bạn ngăn các đội thao túng đại diện cho đến khi mục tiêu thật bị hại?** Một chỉ số sao bắc đẩu căn chỉnh nhiều đội quanh một định nghĩa thành công, vậy mà chương cảnh báo một đại diện được tối ưu quá mạnh có thể hại mục tiêu nó định đại diện, và các con số phù phiếm như tổng người dùng đăng ký hay tổng lượt tải chỉ leo lên mà không phản ánh sức khỏe. Với một tổ chức lớn nơi hàng chục nhóm mỗi nhóm theo đuổi mục tiêu riêng, một sao bắc đẩu không rõ hoặc thao túng được tạo ra chiến thắng cục bộ cộng lại không thành cải thiện thực, hoặc tệ hơn, tác hại lặng lẽ mà không ai nhận ra. Hãy mang ứng viên sao bắc đẩu hiện tại, tập nhỏ chỉ số đầu vào mà các đội thực sự ảnh hưởng được, và các lan can bắt được thao túng, rồi thử sức chịu đựng từng chỉ số được báo cáo bằng cách hỏi liệu nó có thể tăng trong khi người dùng tệ hơn. Trong bối cảnh doanh nghiệp và chính phủ, nơi một chỉ số tiêu đề có thể thúc đẩy ngân sách và báo cáo công khai, hãy gắn sao bắc đẩu với định nghĩa giá trị được giữ lại hoặc kết quả hoàn thành để không ai thổi phồng nó bằng cách theo đuổi lượt đăng ký hay nhấp chuột không bao giờ chuyển đổi.

5. **Với các tính năng lưu lượng thấp, ranh giới trung thực giữa phát hành-và-quan-sát có kỷ luật và một thử nghiệm có đối chứng đầy đủ nằm ở đâu, và ai quyết định?** Thử nghiệm cho sự chắc chắn nhân quả, nhưng cần đủ người dùng và đủ kiên nhẫn để đạt năng lực thống kê, và ép một thử nghiệm thiếu năng lực lên một luồng lưu lượng mỏng đốt nhiều tuần để tạo ra kết quả không phát hiện được hiệu ứng nó tìm. Rủi ro đối lập là phát hành-và-quan-sát bị nhiễu và không chứng minh gì về nhân quả, nên coi nó tương đương thử nghiệm để các đội tuyên bố chiến thắng thực ra là tính thời vụ hay một thay đổi trùng thời điểm. Hãy mang khối lượng lưu lượng và chuyển đổi của luồng đang xét, hiệu ứng tối thiểu phát hiện được bạn quan tâm, và khả năng đảo ngược của thay đổi, rồi thống nhất một quy tắc: thử nghiệm trên một ngưỡng lưu lượng, phát hành-và-quan-sát với lan can rõ ràng dưới nó. Với sản phẩm doanh nghiệp bảo vệ doanh thu và dịch vụ chính phủ nơi một hồi quy hại công dân, hãy nêu ai nắm thẩm quyền miễn một thử nghiệm, và yêu cầu các thay đổi đảo ngược được vẫn thực sự đảo ngược được để một lần phát hành-và-quan-sát tồi có thể bị rút nhanh.

6. **Bạn có ghi kết quả thử nghiệm âm và phẳng trong một kho dùng chung, hay tổ chức cứ khám phá lại cùng những ngõ cụt?** Chương nói rõ rằng một kết quả phẳng hay âm là bằng chứng có giá trị, không phải thất bại, vậy mà không có kho kết quả tìm kiếm được, bài học bay hơi và một đội khác chạy lại cùng thử nghiệm thua cuộc một năm sau. Với một tổ chức lớn điều này cộng dồn, vì học tích lũy là toàn bộ lợi tức của một văn hóa thử nghiệm, và nó chỉ tích tụ nếu thiết kế và kết quả thử nghiệm được viết ra nơi đội kế tiếp sẽ tìm thấy. Hãy mang số thử nghiệm đã chạy quý trước, bao nhiêu kết quả được lập tài liệu và khám phá được, và liệu có ai thực sự kiểm tra kho trước khi thiết kế thử nghiệm mới. Trong bối cảnh doanh nghiệp và chính phủ, một bản ghi bền vững cũng phục vụ kiểm toán và trách nhiệm giải trình, cho thấy một quyết định dựa trên bằng chứng thay vì ý kiến và trao cho người rà soát một dấu vết bảo vệ được khi một thay đổi hướng công chúng bị chất vấn.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy viết một kế hoạch theo dõi một trang cho các sự kiện kích hoạt và phiên đầu tiên của bạn trước khi thêm bất cứ gì khác, để dữ liệu sớm nhất vẫn sạch khi đội lớn lên. Dành thử nghiệm A/B thật cho luồng lưu lượng cao nhất của bạn và dùng phát hành-và-quan-sát cẩn thận ở nơi khác, mua một công cụ phân tích và thử nghiệm lưu trữ thay vì xây, và bám vào một chỉ số sao bắc đẩu duy nhất như kích hoạt. Chỉ thu thập các sự kiện trả lời một câu hỏi đang sống, để bạn không trả chi phí lưu trữ hay rủi ro quyền riêng tư cho dữ liệu bạn không bao giờ đọc.

**Doanh nghiệp nhỏ.** Không có nhà phân tích riêng và ngân sách eo hẹp, hãy dựa vào phân tích tích hợp sẵn trong các công cụ bạn đã chạy và coi thử nghiệm là bài tập thỉnh thoảng, giá trị cao hơn là chương trình thường trực. Lựa chọn thường là mua hơn xây: một cái nhìn phễu và nhóm đối tượng nhúng thắng một đường ống đặt riêng bạn không bảo trì nổi. Hãy tập trung vài thử nghiệm bạn chạy vào luồng duy nhất thúc đẩy doanh thu, và xử lý sự đồng ý đơn giản và trung thực để một khách hàng từ chối theo dõi vẫn có một sản phẩm hoạt động.

**Doanh nghiệp lớn.** Ở quy mô lớn qua nhiều đội, quản trị là vấn đề: một kế hoạch theo dõi có phiên bản được xác thực lúc thu nạp, một nền tảng thử nghiệm dùng chung chuẩn hóa việc gán, tính toán năng lực và lan can, và một kho kết quả để các nhóm học tích lũy thay vì lặp lại thử nghiệm. Hãy giao cho gắn công cụ đo một chủ sở hữu có tên được giám sát như đường ống, thống nhất một chỉ số sao bắc đẩu được bao quanh bởi các đầu vào ảnh hưởng được, và áp dụng cùng phân loại dữ liệu và kiểm soát truy cập cho dữ liệu hành vi như cho bất kỳ tập dữ liệu nhạy cảm nào, với dấu vết kiểm toán cho các quyết định ra mắt hệ quả.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy thu thập dữ liệu hành vi tối thiểu cho một mục đích xác định, có được và tôn trọng sự đồng ý, và công bố bằng ngôn ngữ đơn giản những gì bạn theo dõi và vì sao, trao cho mọi người một dịch vụ hoạt động nếu họ từ chối. Chạy thử nghiệm có đối chứng trên cách diễn đạt và bố cục biểu mẫu để nâng tỷ lệ hoàn thành các dịch vụ thiết yếu, giữ một bản ghi có tài liệu, bảo vệ được về mỗi thử nghiệm để kiểm toán, và yêu cầu bất kỳ nhà cung cấp phân tích nào tiết lộ cách xử lý dữ liệu và trao khả năng di chuyển để bạn tránh khóa chặt.

## Ví dụ

**Công ty khởi nghiệp.** Một ứng dụng tiêu dùng nhỏ viết một kế hoạch theo dõi ngắn, có tài liệu cho các sự kiện đăng ký và phiên đầu tiên của mình trước khi thêm bất kỳ phân tích mới nào, để dữ liệu vẫn sạch khi đội lớn lên. Một phễu cho thấy hầu hết người dùng mới rời bỏ ở bước xác minh tài khoản, và một thử nghiệm A/B đơn giản trên cách diễn đạt rõ ràng hơn nâng việc giữ chân tuần đầu. Với lưu lượng khiêm tốn, đội chỉ chạy thử nghiệm trên các luồng khối lượng cao nhất và dùng phát hành-và-quan-sát cẩn thận cho các thay đổi nhỏ hơn, trong khi giữ kích hoạt làm chỉ số sao bắc đẩu.

**Doanh nghiệp lớn.** Một dịch vụ phát trực tuyến theo đăng ký gắn một kế hoạch theo dõi được quản trị và chạy mọi thay đổi có ý nghĩa qua một nền tảng thử nghiệm với chỉ số xác định trước, tính toán năng lực và lan can về hiệu năng phát và tỷ lệ rời bỏ. Một luồng làm quen được thiết kế lại trông tốt hơn trong các lần rà soát, nhưng một thử nghiệm có đối chứng cho thấy nó giảm việc giữ chân tuần đầu, nên đội hoàn tác nó trước khi triển khai rộng, một lần cứu đáng giá hơn nhiều chi phí của nền tảng.

**Chính phủ.** Một cơ quan dịch vụ số gắn công cụ đo cho luồng đơn xin trợ cấp của mình bằng một kế hoạch theo dõi tôn trọng quyền riêng tư, nhận biết sự đồng ý và chạy thử nghiệm có đối chứng trên cách diễn đạt và bố cục biểu mẫu. Một phân tích phễu cho thấy một bước cụ thể nơi một phần ba người nộp đơn bỏ dở. Một thử nghiệm trên hướng dẫn rõ ràng hơn đã tăng đáng kể tỷ lệ hoàn thành, giảm cả đơn không hoàn chỉnh lẫn khối lượng tổng đài trong khi chỉ thu thập dữ liệu hành vi tối thiểu cần thiết.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của phân tích sản phẩm và thử nghiệm hiện ra trực tiếp trong kết quả: chuyển đổi, giữ chân và hoàn thành cao hơn, và, quan trọng, chi phí tránh được của việc phát hành các thay đổi có hại. Thử nghiệm là một trong số ít thực hành định lượng giá trị của chính nó, vì mỗi thử nghiệm báo cáo mức tăng hay mất mà nó ngăn được. Gắn công cụ đo tốt nhân lợi tức của mọi quyết định sản phẩm bằng cách thay phỏng đoán bằng bằng chứng, và một chỉ số sao bắc đẩu căn chỉnh nhiều đội quanh cùng định nghĩa thành công.

Chi phí áp dụng gồm công cụ phân tích và thử nghiệm, công sức kỹ thuật để gắn công cụ đo tốt, kỹ năng phân tích để chạy thử nghiệm chặt chẽ, và chi phí chung của chương trình quyền riêng tư cho sự đồng ý. Hãy cân nhắc nó so với chi phí của việc không áp dụng: phát hành thay đổi có tác động chưa biết, thắng tranh cãi bằng thâm niên thay vì bằng chứng, theo đuổi chỉ số phù phiếm tâng bốc trong khi sản phẩm đình trệ, và phơi nhiễm quy định từ thu thập dữ liệu cẩu thả. Với ban lãnh đạo, điểm chào là thử nghiệm biến phát triển sản phẩm thành quá trình đo được, tự điều chỉnh, và lần ngăn một bản ra mắt tồi đầu tiên thường tự trả giá cho cả chương trình.

## Phản mẫu và cạm bẫy

- Thêm sự kiện không có kế hoạch theo dõi, tạo ra dữ liệu không nhất quán, không dùng được.
- Nhìn trộm thử nghiệm và dừng khi chúng trông có ý nghĩa, làm tăng dương tính giả.
- Kiểm thử nhiều chỉ số và ăn mừng cái nào tình cờ có ý nghĩa.
- Chạy các thử nghiệm thiếu năng lực không phát hiện được hiệu ứng chúng tìm.
- Tối ưu chỉ số phù phiếm tăng mà không phản ánh giá trị thực.
- Thao túng một chỉ số đại diện quá mạnh đến mức mục tiêu thật bị hại.
- Tích trữ dữ liệu hành vi không có sự đồng ý hay mục đích xác định.
- Quên ghi lại kết quả âm, nên tổ chức lặp lại các thử nghiệm thất bại.

## Mô hình trưởng thành

1. **Khởi đầu.** Gắn công cụ đo thưa thớt hoặc không nhất quán, quyết định theo ý kiến và thâm niên, không chạy thử nghiệm, và báo cáo chỉ số phù phiếm như tổng đăng ký. Sự đồng ý được xử lý cẩu thả.
2. **Phát triển.** Một số sự kiện được theo dõi, nhưng phân loại trôi giữa các đội. Thỉnh thoảng chạy thử nghiệm A/B tùy nghi không có tính toán năng lực, phễu và giữ chân được xem không chính thức, và một chỉ số sao bắc đẩu được đề xuất nhưng chưa được nhúng.
3. **Chuẩn hóa.** Một kế hoạch theo dõi được quản trị và phân loại nhất quán được lập tài liệu, có phiên bản và xác thực lúc thu nạp qua mọi đội. Phễu, nhóm đối tượng và giữ chân được phân tích thường xuyên, thử nghiệm chạy trên nền tảng dùng chung với chỉ số xác định trước, tính toán năng lực và lan can, và quyền riêng tư cùng sự đồng ý được xử lý đúng đắn toàn tổ chức.
4. **Quản lý.** Thực hành được đo theo đường cơ sở: độ phủ gắn công cụ đo và tỷ lệ lỗi chất lượng sự kiện được theo dõi, tốc độ thử nghiệm và tỷ lệ bản ra mắt được chặn cổng bởi một thử nghiệm được báo cáo, vi phạm lan can và nhìn trộm được bắt tự động, và chỉ số sao bắc đẩu cùng các chỉ số đầu vào của nó được giám sát với ngưỡng khai tử tường minh. Chất lượng dữ liệu và tuân thủ quyền riêng tư được kiểm toán theo nhịp cố định thay vì giả định.
5. **Điều phối.** Thử nghiệm là mặc định cho mọi thay đổi có ý nghĩa, gắn công cụ đo được sở hữu và giám sát như đường ống, và một kho kết quả dùng chung gồm cả kết quả âm và phẳng cho phép tổ chức học tích lũy và cho nghỉ hưu ngõ cụt. Phân tích được tích hợp với hoạch định sản phẩm và rủi ro, tôn trọng quyền riêng tư ngay từ thiết kế, và tập chỉ số được liên tục thu hẹp phạm vi khi sản phẩm, thị trường và quy định dịch chuyển.

## Ý tưởng để thảo luận

- Chỉ số sao bắc đẩu thực sự của sản phẩm bạn là gì, và mọi người có đồng ý về nó không?
- Chỉ số được báo cáo nào của bạn là số phù phiếm chỉ đi lên?
- Các đội của bạn có tính năng lực thống kê trước khi chạy thử nghiệm, hay nhìn trộm và dừng?
- Gắn công cụ đo của bạn có điểm mù nào che giấu nỗi đau của người dùng?
- Làm sao bạn giữ phân tích tôn trọng quyền riêng tư mà vẫn học được điều bạn cần?
- Với các tính năng lưu lượng thấp, khi nào phát hành-và-quan-sát là chấp nhận được so với một thử nghiệm đầy đủ?

## Những điểm cần ghi nhớ

- Gắn công cụ đo có chủ đích với một kế hoạch theo dõi được quản trị và phân loại nhất quán.
- Phân tích phễu, nhóm đối tượng, giữ chân và tương tác, không chỉ thu hút.
- Chạy thử nghiệm chặt chẽ: tính toán năng lực, chỉ số xác định trước, không nhìn trộm.
- Neo vào một chỉ số sao bắc đẩu gắn với giá trị thực và đề phòng chỉ số phù phiếm.
- Thu thập dữ liệu hành vi tối thiểu với sự đồng ý rõ ràng và quản trị mạnh.
- Coi gắn công cụ đo là sản phẩm và xây một văn hóa thử nghiệm tích lũy.
- Một kết quả thử nghiệm phẳng hay âm là bằng chứng có giá trị, không phải thất bại.

## Tài liệu tham khảo và đọc thêm

- Ron Kohavi, Diane Tang và Ya Xu, "Trustworthy Online Controlled Experiments."
- Alistair Croll và Benjamin Yoskovitz, "Lean Analytics."
- Eric Ries, "The Lean Startup."
- Avinash Kaushik, "Web Analytics 2.0."
- Georgi Georgiev, "Statistical Methods in Online A/B Testing."
- Quy định (EU) 2016/679, Quy định Bảo vệ Dữ liệu Chung (GDPR).
- Douglas W. Hubbard, "How to Measure Anything."
