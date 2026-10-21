# 4.4 Vận hành bảo mật

## Tổng quan và động lực

Phòng ngừa là cần thiết, nhưng không bao giờ đủ. Kẻ thù kiên quyết, lỗ hổng mới lạ và sai sót của con người đơn thuần nghĩa là một số mối đe dọa sẽ lọt qua phòng thủ của bạn. Vận hành bảo mật là kỷ luật tìm chúng nhanh, phản ứng tốt, và đưa những gì bạn học được trở lại thành phòng thủ mạnh hơn. Đó là sự khác biệt giữa một sự cố được khoanh vùng trong vài phút và một sự cố âm ỉ hàng tháng trước khi ai nhận ra.

Trong một tổ chức lớn, vận hành bảo mật phải hoạt động ở quy mô và tốc độ. Hàng nghìn dịch vụ tạo ra những đại dương nhật ký. Hàng trăm lỗ hổng mới được công bố mỗi tuần. Triển khai không bao giờ dừng. Vận hành thủ công, thủ công mỹ nghệ đơn giản là không theo kịp. Câu trả lời là nhúng bảo mật vào đường ống phân phối ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), tự động hóa phát hiện và phản ứng, và xây dựng cơ bắp để xử lý sự cố bình tĩnh khi chúng ập đến. Với chính phủ, vận hành bảo mật còn mang nghĩa vụ luật định: thời hạn báo cáo sự cố bắt buộc, công bố lỗ hổng có phối hợp, và sự chặt chẽ pháp y có thể chịu được sự soi xét pháp lý.

Chương này bao quát tích hợp bảo mật vào đường ống, quản lý lỗ hổng và vá lỗi, ứng phó sự cố và thực hiện pháp y, vận hành phát hiện qua [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) và SOAR, và xác thực phòng thủ qua đội đỏ, đội tím và [kiểm thử xâm nhập](https://en.wikipedia.org/wiki/Penetration_test).

## Các nguyên tắc chính

- **Tự động hóa việc thường lệ.** Máy móc xử lý quét, tương quan và phản ứng lặp lại để con người tập trung vào phán đoán.
- **Dịch chuyển bảo mật vào đường ống.** Kiểm thử và cổng chặn sống trong [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (tích hợp liên tục và phân phối liên tục), cho phản hồi nhanh nơi kỹ sư đã làm việc.
- **Giả định bị xâm phạm và chuẩn bị.** Diễn tập ứng phó sự cố trước khi bạn cần; sự cố không phải lúc để ứng biến.
- **Đo và giảm thời gian.** Thời gian trung bình để phát hiện và thời gian trung bình để phản ứng là các chỉ số quan trọng nhất.
- **Học hỏi không đổ lỗi.** Mỗi sự cố và lần suýt xảy ra trở thành bài học gia cố hệ thống, không phải cuộc tìm người để trừng phạt.
- **Xác thực phòng thủ theo hướng đối kháng.** Kiểm thử bảo mật của bạn theo cách kẻ tấn công thật sẽ làm, rồi sửa những gì họ tìm thấy.
- **Kỹ thuật phát hiện là một sản phẩm.** Coi các quy tắc phát hiện là mã: được quản lý phiên bản, kiểm thử và liên tục cải thiện.

## Khuyến nghị

### Xây dựng DevSecOps vào đường ống

Hãy tích hợp kiểm thử bảo mật tự động trực tiếp vào tích hợp và phân phối liên tục để phản hồi đến kỹ sư trong vài phút:

- **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Kiểm thử Bảo mật Ứng dụng Tĩnh) phân tích mã nguồn tìm các mẫu dễ bị tổn thương khi nó được commit.
- **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Kiểm thử Bảo mật Ứng dụng Động) dò ứng dụng đang chạy tìm lỗi khai thác được.
- **SCA** (Phân tích Thành phần Phần mềm) đánh dấu các phụ thuộc có lỗ hổng đã biết.
- **Quét IaC** kiểm tra hạ tầng-dưới-dạng-mã tìm cấu hình không an toàn trước khi chúng triển khai.
- **Quét bí mật** chặn thông tin xác thực vào kho mã.

Hãy điều chỉnh những công cụ này một cách tàn nhẫn để kiểm soát dương tính giả. Một bộ quét kêu sói bị phớt lờ. Hãy đặt các cổng dựa trên rủi ro: chặn với các phát hiện mức nghiêm trọng cao, độ tin cậy cao, và theo dõi phần còn lại mà không dừng phân phối. Bạn muốn một tín hiệu nhanh, đáng tin, không phải một bức tường nhiễu.

### Quản lý lỗ hổng và vá lỗi có hệ thống

Một dòng đều đặn lỗ hổng đòi hỏi một quy trình có hệ thống, có ưu tiên, không phải một cơn hoảng loạn mới với mỗi tiêu đề.

- Duy trì một bản kiểm kê tài sản chính xác để bạn biết cái gì có thể bị ảnh hưởng bởi bất kỳ lỗ hổng nào.
- Ưu tiên khắc phục theo rủi ro thực: kết hợp mức nghiêm trọng, khả năng khai thác (nó có đang bị khai thác ngoài thực tế không?), mức phơi bày và mức độ quan trọng của tài sản thay vì vá chỉ theo điểm số thô.
- Xác định và thực thi **SLA khắc phục** (thỏa thuận mức dịch vụ) theo bậc nghiêm trọng, và đo mức tuân thủ.
- Tự động hóa việc vá ở nơi bạn có thể một cách an toàn, đặc biệt cho hạ tầng và phụ thuộc.
- Chạy một chương trình **công bố lỗ hổng có phối hợp** với kênh tiếp nhận rõ ràng và, ở nơi phù hợp, một [chương trình thưởng lỗi](https://en.wikipedia.org/wiki/Bug_bounty_program), để các nhà nghiên cứu bên ngoài có thể báo cáo lỗi một cách có trách nhiệm thay vì ném chúng ra công khai.

### Chuẩn bị và vận hành ứng phó sự cố

Khi một sự cố ập đến, một quy trình đã diễn tập đáng giá hơn bất kỳ công cụ nào.

- Duy trì một **kế hoạch ứng phó sự cố** với các vai trò xác định (chỉ huy sự cố, phụ trách truyền thông, điều tra viên), phân loại mức nghiêm trọng và đường leo thang.
- Thiết lập các giai đoạn rõ ràng: **chuẩn bị, phát hiện và phân tích, khoanh vùng, loại bỏ, khôi phục, và rà soát sau sự cố.**
- Bảo quản bằng chứng đúng cách cho **[pháp y](https://en.wikipedia.org/wiki/Digital_forensics)**: thu thập nhật ký, bộ nhớ và ảnh đĩa với chuỗi bảo quản có tài liệu để các phát hiện đứng vững về mặt pháp lý và phân tích đáng tin.
- Lập kế hoạch **truyền thông xâm phạm** từ trước: ai thông báo cho khách hàng, cơ quan quản lý và công chúng, theo mốc thời gian nào, với sự tham gia của pháp lý và PR. Đồng hồ quy định (thường 72 giờ hoặc ít hơn) bắt đầu chạy từ lúc phát hiện.
- Chạy **bài tập bàn giấy** đều đặn để đội biết kế hoạch trước một khủng hoảng thực, và thực hiện các buổi rà soát sau sự cố không đổ lỗi tạo ra cải tiến cụ thể.

### Vận hành phát hiện với SIEM và SOAR, và kỹ thuật hóa các phát hiện

Hãy gom các tín hiệu bảo mật của bạn lại và hành động trên chúng ở quy mô lớn.

- Dùng một **SIEM** (Quản lý Thông tin và Sự kiện Bảo mật) để tổng hợp và tương quan nhật ký cùng sự kiện từ khắp hệ sinh thái, phơi bày các mẫu đáng ngờ.
- Dùng **SOAR** (Điều phối, Tự động hóa và Ứng phó Bảo mật) để tự động hóa phân loại và sổ tay phản ứng: làm giàu cảnh báo, cô lập máy chủ, vô hiệu hóa thông tin xác thực, và mở hồ sơ mà không chờ con người cho các bước thường lệ.
- Thực hành **kỹ thuật phát hiện**: coi các quy tắc phát hiện là mã có phiên bản, được kiểm thử căn chỉnh với một khung như [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), đo tỷ lệ dương tính thật và giả của chúng, và liên tục cải thiện độ bao phủ các kỹ thuật thực của kẻ thù.
- Bảo đảm ghi nhật ký toàn diện, chống can thiệp qua ứng dụng và hạ tầng; bạn không thể phát hiện những gì bạn không ghi.

### Xác thực phòng thủ bằng đội đỏ, đội tím và kiểm thử xâm nhập

Kiểm thử phòng thủ của bạn theo cách kẻ tấn công sẽ làm là cách duy nhất để biết chúng thực sự hoạt động.

- **Kiểm thử xâm nhập** cung cấp đánh giá tập trung, tại một thời điểm về các hệ thống cụ thể, thường cho tuân thủ.
- **[Đội đỏ](https://en.wikipedia.org/wiki/Red_team)** mô phỏng một kẻ thù thực tế theo đuổi mục tiêu qua môi trường của bạn, kiểm thử phát hiện và phản ứng cũng như phòng ngừa.
- **Đội tím** đưa kẻ tấn công (đỏ) và người phòng thủ (xanh) lại cùng nhau hợp tác để mỗi cuộc tấn công mô phỏng lập tức cải thiện phát hiện và biện pháp kiểm soát, biến một bài tập thành năng lực bền vững.
- Đưa mọi phát hiện trở lại kỹ thuật phát hiện, khắc phục và đào tạo.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Cổng đường ống chặn | Ngăn các vấn đề đã biết được phát hành | Ma sát, dương tính giả làm các đội bực |
| Quét không chặn | Ma sát thấp, phân phối nhanh | Vấn đề có thể được phát hành; cần kỷ luật để sửa |
| SOC nội bộ | Ngữ cảnh sâu, kiểm soát toàn bộ | Đắt, khó bố trí nhân sự 24/7 |
| Phát hiện/ứng phó được quản lý | Bao phủ 24/7, chuyên môn sẵn có | Ít ngữ cảnh hơn, phụ thuộc nhà cung cấp |
| Vá tự động | Nhanh, đóng cửa sổ nhanh | Rủi ro thay đổi phá vỡ |
| Đội đỏ thường xuyên | Xác thực thực tế, tìm khoảng trống thật | Tốn kém, nhiều tài nguyên |
| Chương trình thưởng lỗi | Phát hiện từ cộng đồng, bao phủ tốt | Gánh nặng phân loại, chi phí chi trả, nhiễu |

Căng thẳng cốt lõi là tốc độ so với sự bảo đảm, và độ bao phủ so với chi phí. Cổng chặn và vá tự động tối đa hóa sự bảo đảm nhưng thêm ma sát và rủi ro. Các cách tiếp cận không chặn di chuyển nhanh hơn nhưng phụ thuộc vào sự theo đuổi đến cùng. Phát hiện suốt ngày đêm là thiết yếu ở quy mô lớn nhưng đắt để xây nội bộ, điều đẩy nhiều tổ chức về các mô hình lai. Con đường bền vững tự động hóa việc thường lệ có độ tin cậy cao, dành sự chú ý con người cho phán đoán thực sự, và tiếp tục điều chỉnh cán cân bằng kết quả đo được thay vì nỗi sợ.

## Câu hỏi để thảo luận với đội của bạn

1. **SLA khắc phục của bạn theo mức nghiêm trọng là gì, và cái gì thực sự thực thi chúng?** Một dòng đều đặn lỗ hổng cần một quy trình có hệ thống, có ưu tiên, không phải một cơn hoảng loạn mới với mỗi tiêu đề, và SLA theo bậc nghiêm trọng là cách bạn theo kịp. Hãy quyết định đồng hồ của bạn (ví dụ, nghiêm trọng trong vài ngày, cao trong vài tuần) và, quan trọng không kém, cách bạn đo mức tuân thủ và ai chịu trách nhiệm khi một hạn chót bị trượt. Hãy ưu tiên theo rủi ro thực, kết hợp mức nghiêm trọng với khả năng khai thác ngoài thực tế, mức phơi bày và mức độ quan trọng của tài sản, thay vì vá chỉ theo điểm CVSS thô. Hãy mang tồn đọng hiện tại các phát hiện mở của bạn được sắp theo tuổi và mức nghiêm trọng, vì các lỗi nghiêm trọng chưa vá nằm quá cửa sổ là bằng chứng quan trọng. Nếu SLA không có thực thi và không có chủ sở hữu, nó là một điều ước, và quét mà không khắc phục chỉ xây nợ kiểm toán và cảm giác an toàn giả.

2. **Khi một sự cố ập đến lúc 2 giờ sáng, ai là chỉ huy sự cố và đồng hồ quy định bắt đầu nhanh đến đâu?** Một quy trình đã diễn tập đáng giá hơn bất kỳ công cụ nào, nên bạn cần các vai trò có tên (chỉ huy sự cố, phụ trách truyền thông, điều tra viên), mức nghiêm trọng xác định và đường leo thang được viết ra trước khủng hoảng. Đồng hồ quy định thường chạy 72 giờ hoặc ít hơn và bắt đầu từ lúc phát hiện, nên hãy quyết định trước ai thông báo cho khách hàng, cơ quan quản lý và công chúng, và xác nhận pháp lý cùng PR được cập nhật. Bảo quản bằng chứng pháp y với chuỗi bảo quản có tài liệu phải xảy ra trước khi bất kỳ ai dựng lại một máy chủ bị xâm phạm, nếu không bạn mất khả năng hiểu hay chứng minh điều đã xảy ra. Hãy mang ngày của bài tập bàn giấy gần nhất của bạn, vì nếu nó từ lâu hoặc chưa bao giờ, kế hoạch của bạn chưa được kiểm thử. Với các đội chính phủ, thời hạn báo cáo luật định khiến điều này không tùy chọn, vì vậy hãy diễn tập đường thông báo, không chỉ phản ứng kỹ thuật.

3. **Những hành động phản ứng thường lệ nào bạn sẽ để SOAR thực hiện mà không có con người trong vòng lặp?** Tự động hóa là hệ số nhân sức mạnh cho phép một đội mỏng bao phủ một hệ sinh thái lớn, và chỉ số quan trọng là thời gian trung bình để phản ứng, mà các sổ tay tự động có thể cắt từ hàng giờ xuống vài phút. Hãy quyết định hành động có độ tin cậy cao nào (cô lập một máy chủ, thu hồi một thông tin xác thực, mở một hồ sơ) bạn tin để chạy tự động, và cái nào cần phán đoán của con người trước. Rủi ro là một dương tính giả kích hoạt một hành động gây gián đoạn, nên hãy gắn tự động hóa với chất lượng phát hiện và điều chỉnh tàn nhẫn, vì một hệ thống kêu sói bị tắt. Hãy mang khối lượng cảnh báo hiện tại và tỷ lệ dương tính giả của bạn, vì những con số đó cho bạn biết sổ tay nào an toàn để tự động hóa hôm nay. Nếu mọi bước phản ứng chờ con người, bạn sẽ không theo kịp ở quy mô lớn, và thời gian lưu trú, thứ thúc đẩy chi phí xâm phạm, sẽ vẫn cao.

4. **Phát hiện nào của đường ống chặn một bản phát hành, cái nào chỉ được theo dõi, và ai giữ tỷ lệ dương tính giả đủ thấp để kỹ sư vẫn tin cổng?** Một bộ quét kêu sói bị phớt lờ, và khi kỹ sư mất niềm tin vào một cổng họ vận động để gỡ nó, nên giá trị của DevSecOps nằm ở chất lượng tín hiệu hơn là độ bao phủ thô. Căng thẳng là thật: chặn quá ít thì mã dễ tổn thương được phát hành; chặn quá nhiều thì bạn thêm ma sát, làm chậm phân phối, và đốt thiện chí. Hãy mang tỷ lệ dương tính thật và giả của từng bộ quét (SAST, DAST, SCA, IaC và quét bí mật), tần suất các đội ghi đè hoặc dập một cổng, và tuổi của các phát hiện mà bạn chỉ theo dõi mà không sửa. Với một doanh nghiệp hay cơ quan chính phủ chạy hàng trăm đường ống, hãy đặt chính sách chặn-so-với-theo-dõi tập trung và điều chỉnh nó bằng dữ liệu, vì các cổng khác nhau tùy tiện giữa các đội tạo ra cả khoảng trống kiểm toán lẫn cảm giác bảo mật là thất thường.

5. **Bạn tự tin đến đâu rằng các phát hiện của mình vẫn bao phủ các kỹ thuật mà kẻ tấn công thật sẽ dùng, và ai sở hữu chúng như mã có kiểm thử, có phiên bản?** Phát hiện phân rã lặng lẽ khi môi trường và kẻ thù của bạn tiến hóa, nên một bộ quy tắc trông toàn diện năm ngoái có thể mất độ bao phủ từ lâu trước khi một sự cố cuối cùng phơi bày khoảng trống. Coi phát hiện là mã, được quản lý phiên bản, kiểm thử và ánh xạ với một khung như MITRE ATT&CK, là thứ phân biệt một thực hành kỹ thuật với một đống cảnh báo cũ, vậy mà nó cạnh tranh cùng thời gian phân tích viên khan hiếm với phân loại trực tiếp. Hãy mang bản đồ độ bao phủ ATT&CK hiện tại, tỷ lệ dương tính thật và giả đo được của các phát hiện hàng đầu, và kết quả của bài tập đội tím gần nhất, vì kiểm thử đỏ-và-xanh hợp tác là cách nhanh nhất để chứng minh phát hiện nào thực sự kích hoạt. Trong bối cảnh doanh nghiệp và chính phủ nơi một khung có thể bị bắt buộc, hãy gắn mỗi phát hiện với một chủ sở hữu có tên và nhịp rà soát, vì độ bao phủ không ai duy trì là độ bao phủ bạn chỉ phát hiện đã mất sau vụ xâm phạm.

6. **Bạn xây phát hiện và ứng phó nội bộ, mua phát hiện và ứng phó được quản lý, hay pha trộn cả hai, và bạn đã định giá chi phí của bao phủ thực sự suốt ngày đêm chưa?** Thời gian lưu trú thúc đẩy chi phí xâm phạm, nên những giờ không được bao phủ (đêm, cuối tuần, ngày lễ) chính là lúc kẻ xâm nhập chưa bị phát hiện gây thiệt hại nhiều nhất, vậy mà bố trí nhân sự cho một trung tâm vận hành bảo mật 24/7 nội bộ thì đắt và khó duy trì. Đánh đổi là ngữ cảnh và kiểm soát so với chi phí và tốc độ đến bao phủ: một đội nội bộ biết sâu hệ sinh thái của bạn nhưng chậm và tốn kém để xây, trong khi một nhà cung cấp được quản lý cho chuyên môn tức thì suốt ngày đêm với cái giá là ngữ cảnh mỏng hơn và phụ thuộc nhà cung cấp. Hãy mang giờ bao phủ hiện tại, thời gian trung bình để phát hiện và phản ứng ngoài giờ, khối lượng cảnh báo, và một đánh giá trung thực về việc bạn có thể tuyển và giữ chân các phân tích viên mà một trung tâm tự chạy cần không. Với chính phủ và doanh nghiệp chịu quy định, hãy cân nhắc nơi lưu trữ dữ liệu, thẩm tra nhân sự, và nghĩa vụ báo cáo luật định mà nhà cung cấp phải đáp ứng được, và xác nhận hợp đồng bảo tồn sự chặt chẽ pháp y và chuỗi bảo quản mà các thủ tục pháp lý đòi hỏi.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ và sự sống còn đến trước, nên hãy mua bảo mật như sản phẩm phụ của công cụ bạn đã chạy thay vì bố trí nhân sự vận hành. Nối các bộ quét miễn phí vào CI để chặn rò rỉ bí mật và phụ thuộc có lỗ hổng đã biết lúc commit, chuyển tiếp nhật ký đến một dịch vụ được quản lý chi phí thấp với một nhúm cảnh báo giá trị cao, và viết một kế hoạch sự cố một trang (gọi ai, xoay vòng thông tin xác thực thế nào, chụp ảnh trước khi dựng lại) trước khi bạn cần nó. Nguồn lực khan hiếm nhất của bạn là sự chú ý kỹ thuật, nên hãy tự động hóa việc thường lệ và cưỡng lại việc dựng một trung tâm vận hành bảo mật mà bạn không thể duy trì chạy.

**Doanh nghiệp nhỏ.** Không có chuyên gia bảo mật riêng và ngân sách eo hẹp, hãy dựa vào phát hiện và ứng phó được quản lý và vào các tính năng bảo mật đã tích hợp trong nền tảng của bạn. Hãy coi vá lỗi và kiểm kê tài sản là các thói quen có đòn bẩy cao nhất: biết bạn chạy gì, giữ nó cập nhật, và thực thi hạn chót khắc phục đơn giản theo mức nghiêm trọng. Ưu tiên nhà cung cấp xử lý giám sát suốt ngày đêm, tiếp nhận công bố có phối hợp và thu thập pháp y giúp bạn, và diễn tập điều duy nhất bạn không thể thuê ngoài, là quyết định ai tuyên bố một sự cố và ai nói chuyện với khách hàng.

**Doanh nghiệp lớn.** Thách thức là sự nhất quán qua nhiều đội và hàng trăm đường ống: một chính sách cổng chặn-so-với-theo-dõi dùng chung, SLA khắc phục được thực thi toàn tổ chức, một nền tảng SIEM và SOAR với phát hiện được đo, và đội tím biến mỗi bài tập thành độ bao phủ mới. Hãy quản lý vận hành bảo mật như một danh mục với bảng điều khiển cho thời gian trung bình để phát hiện và phản ứng, mức tuân thủ SLA, và độ chính xác phát hiện, và quyết định có chủ đích nơi chiều sâu nội bộ thắng quy mô được quản lý. Hãy ngân sách tường minh chi phí giám sát của con người cho phân loại và điều chỉnh, vì tự động hóa dịch chuyển công sức chứ không loại bỏ nó.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Thời hạn báo cáo sự cố luật định và công bố lỗ hổng có phối hợp là nghĩa vụ chứ không phải lựa chọn, vì vậy hãy diễn tập đường thông báo đến cơ quan quốc gia cẩn thận như phản ứng kỹ thuật, và bảo quản bằng chứng pháp y dưới một chuỗi bảo quản chịu được sự soi xét pháp lý. Hãy ưu tiên hợp đồng giữ logic phát hiện và dữ liệu di động được, đòi hỏi bất kỳ nhà cung cấp được quản lý nào đáp ứng yêu cầu về nơi lưu trữ và thẩm tra nhân sự, và kỳ vọng các đánh giá đội đỏ và quét liên tục nuôi một quy trình cấp phép mà công chúng có thể tin.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp không có trung tâm vận hành bảo mật nối các bộ quét miễn phí vào đường ống CI để rò rỉ bí mật và phụ thuộc có lỗ hổng đã biết bị bắt lúc commit, chỉ chặn với các phát hiện độ tin cậy cao để hai kỹ sư không bị nhấn chìm trong nhiễu. Họ viết một kế hoạch sự cố một trang trước khi cần: gọi ai, xoay vòng thông tin xác thực thế nào, và chụp ảnh một máy chủ bị xâm phạm trước khi dựng lại nó để họ có thể tìm hiểu điều đã xảy ra. Họ chuyển tiếp nhật ký đến một dịch vụ được quản lý chi phí thấp và đặt một vài cảnh báo trên các sự kiện sẽ thực sự báo hiệu một vụ xâm phạm, nên một vấn đề hiện ra sau vài giờ thay vì vài tháng cần để nhận ra do tình cờ.

**Doanh nghiệp lớn.** Một công ty phần mềm-như-một-dịch-vụ chạy SAST, SCA, IaC và quét bí mật trong mọi đường ống, chỉ chặn với các phát hiện mức nghiêm trọng cao, độ tin cậy cao và theo dõi phần còn lại trên bảng điều khiển với SLA khắc phục. Một SIEM nuôi một nền tảng SOAR tự động cô lập máy chủ và thu hồi thông tin xác thực với các cảnh báo độ tin cậy cao, cắt thời gian trung bình để phản ứng từ hàng giờ xuống vài phút. Các bài tập đội tím hằng quý đối chiếu với kỹ thuật MITRE ATT&CK trực tiếp tạo ra quy tắc phát hiện mới, đều đặn đóng các khoảng trống độ bao phủ.

**Chính phủ.** Một cơ quan liên bang vận hành một trung tâm vận hành bảo mật (SOC) với báo cáo sự cố bắt buộc cho một cơ quan an ninh mạng quốc gia trong các thời hạn luật định. Nó chạy một chương trình công bố lỗ hổng có phối hợp với kênh tiếp nhận công khai theo yêu cầu của chính sách, và bảo quản bằng chứng pháp y dưới các thủ tục chuỗi bảo quản nghiêm ngặt phù hợp cho thủ tục pháp lý. Các đánh giá đội đỏ hằng năm và quét lỗ hổng liên tục nuôi sự cấp phép liên tục của cơ quan và các SLA khắc phục dựa trên rủi ro của nó.

## Luận chứng kinh doanh: động lực, ROI và TCO

Gần như mọi thứ về luận chứng cho vận hành bảo mật quy về thời gian lưu trú: kẻ tấn công không bị phát hiện càng lâu, vụ xâm phạm càng tốn kém. Các nghiên cứu liên tục cho thấy các sự cố được khoanh vùng nhanh tốn ít hơn hẳn những sự cố kéo dài hàng tháng. Tổng chi phí sở hữu bao gồm công cụ (SIEM, SOAR, bộ quét), nhân sự hoặc dịch vụ được quản lý cho phát hiện và ứng phó, và thời gian để xây dựng và diễn tập quy trình sự cố. Đối lại là chi phí của việc không đầu tư: một vụ xâm phạm phát hiện muộn, lan qua các hệ thống, kéo theo tiền phạt quy định, thông báo bắt buộc, kiện tụng và thiệt hại danh tiếng, tất cả tệ hơn bởi sự hỗn loạn của một phản ứng chưa diễn tập.

ROI đến từ phát hiện và phản ứng nhanh hơn, tự động hóa cho phép một đội mỏng bao phủ một hệ sinh thái lớn, và các cải tiến phòng ngừa phản hồi từ mọi sự cố và bài tập. Đặc biệt DevSecOps hoàn vốn bằng cách bắt vấn đề trong đường ống nơi chúng rẻ, thay vì trên môi trường thực nơi chúng đắt và công khai. Khi bạn trình bày lập luận với ban lãnh đạo, hãy đặt con số lên thời gian trung bình hiện tại của bạn để phát hiện và phản ứng, cho thấy chúng gắn với thời gian lưu trú và chi phí thế nào, và đóng khung tự động hóa là hệ số nhân sức mạnh tránh tăng biên chế đồng bộ với hệ sinh thái. Với chính phủ, hãy nhấn mạnh rằng nghĩa vụ báo cáo và công bố luật định khiến vận hành trưởng thành không tùy chọn.

## Phản mẫu và cạm bẫy

- **Mệt mỏi vì cảnh báo.** Quá nhiều cảnh báo đến mức phân tích viên lờ đi và bỏ sót cái thật.
- **Quét không khắc phục.** Tạo ra các phát hiện không ai sửa, tạo cảm giác an toàn giả và nợ kiểm toán.
- **Không có kế hoạch sự cố.** Ứng biến trong khủng hoảng, lãng phí những phút quan trọng và xử lý sai bằng chứng.
- **Phá hủy bằng chứng.** Dựng lại một máy chủ bị xâm phạm trước khi thu thập pháp y, mất khả năng hiểu hay chứng minh điều đã xảy ra.
- **Văn hóa đổ lỗi trong rà soát.** Trừng phạt người ứng phó để sự cố kế tiếp bị giấu hoặc xử lý một cách phòng thủ.
- **Kiểm thử xâm nhập chỉ vì tuân thủ.** Một bài kiểm thử hằng năm duy nhất để thỏa mãn kiểm toán viên, với các phát hiện bị bỏ qua đến năm sau.
- **Cổng chặn với dương tính giả cao.** Xói mòn niềm tin cho đến khi kỹ sư đòi loại bỏ hoàn toàn các cổng.
- **Phát hiện cài-rồi-quên.** Các quy tắc phân rã khi môi trường và kẻ thù tiến hóa, âm thầm mất độ bao phủ.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Vận hành bảo mật là tùy nghi và phản ứng. Kiểm thử bảo mật là thủ công và hiếm, và không có ghi nhật ký trung tâm hay SIEM. Không có kế hoạch sự cố, nên phản ứng được ứng biến ngay lúc đó. Vá lỗi chỉ xảy ra khi một tiêu đề buộc phải làm, và phòng thủ không bao giờ được kiểm thử theo hướng đối kháng.

**Mức 2: Phát triển.** Các thực hành cơ bản xuất hiện nhưng không nhất quán giữa các đội. Một số đường ống chạy bộ quét trong khi số khác không chạy gì, và ghi nhật ký trung tâm tồn tại từng mảng. Một kế hoạch sự cố cơ bản được lập tài liệu nhưng hiếm khi diễn tập, vá lỗi theo mốc thời gian lỏng lẻo, và một bài kiểm thử xâm nhập hằng năm thỏa mãn tuân thủ mà không thay đổi nhiều. Độ bao phủ và sự chặt chẽ phụ thuộc vào bạn hỏi đội nào.

**Mức 3: Chuẩn hóa.** Các thực hành được lập tài liệu và thực thi toàn tổ chức. Quét DevSecOps đầy đủ với cổng dựa trên rủi ro được áp dụng nhất quán, một SIEM tương quan sự kiện, và các sổ tay SOAR ban đầu chạy. Ứng phó sự cố được diễn tập bằng bài tập bàn giấy và rà soát không đổ lỗi, SLA khắc phục theo mức nghiêm trọng được thực thi với chủ sở hữu có tên, và công bố lỗ hổng có phối hợp cùng đội đỏ thường xuyên là chuẩn mực chứ không phải ngoại lệ.

**Mức 4: Quản lý.** Vận hành được đo và kiểm soát theo các đường cơ sở. Thời gian trung bình để phát hiện và phản ứng, mức tuân thủ SLA theo bậc nghiêm trọng, độ bao phủ quét, tỷ lệ dương tính thật và giả của phát hiện, và thời gian lưu trú được theo dõi trên bảng điều khiển và rà soát theo nhịp. Phát hiện mang độ chính xác và độ phủ đo được ánh xạ với MITRE ATT&CK, quyết định tự động hóa được kiểm soát bằng dữ liệu dương tính giả thay vì hy vọng, và một chỉ số trôi quá đường cơ sở kích hoạt một phản ứng xác định thay vì không được để ý.

**Mức 5: Điều phối.** Vận hành bảo mật được cải thiện liên tục, tích hợp trong toàn tổ chức và thích ứng. Kỹ thuật phát hiện, đội tím, khắc phục và rà soát sự cố nuôi một vòng lặp thích ứng với kỹ thuật kẻ thù mới khi chúng xuất hiện. Các sổ tay tự động xử lý việc thường lệ khắp hệ sinh thái để con người tập trung vào phán đoán, bảo mật được hoạch định cùng phân phối và rủi ro, và mỗi sự cố cùng bài tập gia cố hệ thống một cách đo được trong khi các chỉ số cốt lõi tiếp tục xu hướng đi xuống.

## Ý tưởng để thảo luận

1. Phát hiện nào của đường ống nên chặn một bản phát hành, và cái nào chỉ nên được theo dõi?
2. Xây một SOC nội bộ, dùng phát hiện và ứng phó được quản lý, hay pha trộn cả hai, và vì sao?
3. Làm sao bạn giữ quy tắc phát hiện không phân rã khi môi trường của bạn tiến hóa?
4. Vá lỗi nên được tự động hóa quyết liệt đến mức nào xét rủi ro thay đổi phá vỡ?
5. Một buổi rà soát sau sự cố thực sự không đổ lỗi trông như thế nào trong văn hóa của bạn?
6. Làm sao bạn đo liệu đội đỏ và đội tím có thực sự cải thiện phòng thủ của bạn?

## Những điểm cần ghi nhớ

- Phòng ngừa cuối cùng sẽ thất bại; vận hành tồn tại để phát hiện và phản ứng nhanh.
- Nhúng SAST, DAST, SCA, IaC và quét bí mật vào đường ống với cổng dựa trên rủi ro.
- Ưu tiên vá theo khả năng khai thác thực và mức độ quan trọng của tài sản, dưới SLA được thực thi.
- Diễn tập ứng phó sự cố, bảo quản bằng chứng pháp y, và lập kế hoạch truyền thông xâm phạm từ trước.
- Dùng SIEM và SOAR để tương quan và tự động hóa; coi phát hiện là mã được kỹ thuật hóa, kiểm thử.
- Xác thực phòng thủ bằng kiểm thử xâm nhập, đội đỏ và đội tím hợp tác.
- Thời gian lưu trú thúc đẩy chi phí xâm phạm, nên thời gian trung bình để phát hiện và phản ứng là các chỉ số quan trọng.

## Tài liệu tham khảo và đọc thêm

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin và những người khác, *Logging and Log Management* / tài liệu về SIEM
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, hướng dẫn *Coordinated Vulnerability Disclosure* và đặc tả *CVSS*
