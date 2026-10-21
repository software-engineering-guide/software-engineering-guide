# 10.3 Mua sắm, mã nguồn mở và cấp phép

## Tổng quan và động lực

Gần như mọi hệ thống phần mềm hiện đại được lắp ráp phần lớn từ các thành phần do người khác viết. [Phần mềm nguồn mở](https://en.wikipedia.org/wiki/Open-source_software) tạo nên nền móng của hệ điều hành, ngôn ngữ, khung phát triển, cơ sở dữ liệu và hạ tầng đám mây. Nó vào doanh nghiệp theo hai đường: qua [mua sắm](https://en.wikipedia.org/wiki/Procurement) có chủ đích, và qua những câu lệnh `import` tình cờ của từng nhà phát triển. Chương này nói về việc thực hiện sự tiêu thụ đó (và, nơi phù hợp, đóng góp) một cách có chủ đích. Điều đó nghĩa là có chiến lược, tuân thủ giấy phép, hiểu nghĩa vụ và rủi ro copyleft, và có kế hoạch cho [hết vòng đời](https://en.wikipedia.org/wiki/End-of-life_(product)) không thể tránh của các thành phần bạn phụ thuộc.

Với các đội lớn, rủi ro đồng thời mang tính pháp lý, vận hành và chiến lược. Về pháp lý, [giấy phép](https://en.wikipedia.org/wiki/Software_license) mã nguồn mở là hợp đồng có hiệu lực thi hành với nghĩa vụ thật. Làm sai [copyleft](https://en.wikipedia.org/wiki/Copyleft) (cấp phép có thể buộc các tác phẩm phái sinh phải được chia sẻ theo cùng điều khoản) có thể, trong trường hợp xấu nhất, buộc phải tiết lộ mã nguồn độc quyền hoặc kích hoạt kiện tụng. Vi phạm giấy phép thậm chí có thể chặn một thương vụ mua lại hay đợt chào bán công khai trong [thẩm định](https://en.wikipedia.org/wiki/Due_diligence). Về vận hành, phụ thuộc không được quản lý mục rữa: thành phần không còn được bảo trì, tích lũy lỗ hổng, và hết vòng đời khi vẫn nằm sâu trong môi trường sản xuất. Về chiến lược, mã nguồn mở không chỉ là đầu vào tiết kiệm chi phí. Nó là cách tránh [khóa chặt](https://en.wikipedia.org/wiki/Vendor_lock-in), thu hút nhân tài, và định hình các hệ sinh thái bạn phụ thuộc, những lợi thế bạn chỉ nắm được nếu tham gia có chủ đích.

Chính phủ có thêm một chiều. Nhiều khu vực pháp lý nay có chính sách tường minh ưu tiên mã nguồn mở, tiêu chuẩn mở và chia sẻ mã giữa các cơ quan. Chúng thường được diễn đạt là "tiền công, mã công": nguyên tắc rằng phần mềm do người đóng thuế tài trợ nên, theo mặc định, sẵn có cho công chúng. Vì vậy kỹ sư khu vực công phải điều hướng cả tuân thủ giấy phép lẫn các nhiệm vụ chủ động ưu tiên, công bố và tái sử dụng mã nguồn mở. Chương này nhằm làm tất cả những điều đó quản lý được ở quy mô.

## Các nguyên tắc chính

- **Mã nguồn mở là chuỗi cung ứng, không phải đồ miễn phí.** Hãy đối xử với thành phần tiêu thụ với cùng sự nghiêm ngặt như bất kỳ nhà cung cấp trọng yếu nào.
- **Giấy phép là nghĩa vụ, không phải cho phép để phớt lờ.** Mọi phụ thuộc mang điều khoản; hãy biết chúng trước khi phát hành.
- **Copyleft là ràng buộc thiết kế, không phải điều cấm kỵ.** Giấy phép copyleft dùng được và có giá trị; chúng chỉ đòi bạn hiểu cách kết hợp và phân phối phần mềm.
- **Tiêu thụ có chủ đích, đóng góp có chiến lược.** Quyết định đưa gì vào và, nơi có lợi, đầu tư vào đóng góp ngược dòng thay vì rẽ nhánh.
- **Kiểm kê mọi thứ.** Bạn không tuân thủ, bảo mật hay cập nhật được cái bạn không thấy; SBOM (danh mục vật liệu phần mềm, bản kiểm kê đầy đủ các thành phần trong phần mềm của bạn) là điều kiện tối thiểu.
- **Lên kế hoạch cho hết vòng đời từ đầu.** Mọi phụ thuộc một ngày sẽ không còn được bảo trì; hãy biết lối thoát trước khi bị buộc vào một lối.
- **Trong chính phủ, mặc định là mở.** Ưu tiên [tiêu chuẩn mở](https://en.wikipedia.org/wiki/Open_standard) và mã nguồn mở, và công bố mã tiền công trừ khi có lý do cụ thể không làm vậy.

## Khuyến nghị

### Đặt chiến lược mã nguồn mở và chính sách tiêu thụ

Hãy công bố chính sách rõ ràng về cách nhà phát triển được đưa mã nguồn mở vào tổ chức: giấy phép nào được phê duyệt trước, cái nào cần rà soát, và cái nào bị cấm cho các trường hợp sử dụng của bạn. Cung cấp đường phê duyệt nhanh, ít ma sát. Một chính sách chậm hơn sao chép mã sẽ đơn giản bị phớt lờ. Phân biệt ngữ cảnh, vì cùng một giấy phép hành xử khác nhau khi một thành phần được dùng nội bộ như dịch vụ, nhúng trong sản phẩm được phân phối, hay liên kết vào ứng dụng độc quyền. Làm đường dễ thành đường tuân thủ: một kho nội bộ được tuyển chọn gồm các thành phần đã thẩm định, quét tự động trong đường ống, và hướng dẫn rõ ràng nhà phát triển làm theo được mà không cần gọi luật sư cho các trường hợp thường lệ.

### Quản lý tuân thủ giấy phép, nghĩa vụ và rủi ro copyleft

Hãy làm quen các họ giấy phép và nghĩa vụ của chúng. [Giấy phép cho phép rộng rãi](https://en.wikipedia.org/wiki/Permissive_software_license) (như MIT, BSD và Apache 2.0) chủ yếu đòi ghi công và giữ nguyên thông báo; Apache 2.0 thêm cấp phép bằng sáng chế tường minh. Copyleft yếu (như [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) và MPL) đòi bạn chia sẻ các sửa đổi với các tệp được bao phủ nhưng nhìn chung cho phép kết hợp với mã độc quyền. Copyleft mạnh (như [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License)) có thể đòi toàn bộ tác phẩm được phân phối phải được cung cấp theo cùng điều khoản. Copyleft mạng ([AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)) mở rộng nghĩa vụ đó sang phần mềm được cung cấp qua mạng, không chỉ phân phối dưới dạng nhị phân. Các nghĩa vụ quan trọng nhất xoay quanh hai điều: bạn có phân phối phần mềm không, và bạn kết hợp các thành phần chặt đến đâu. Tự động hóa tuân thủ: quét phụ thuộc để tìm giấy phép, tạo và phát hành các tệp ghi công và thông báo bắt buộc, và chặn bản dựng theo chính sách để một giấy phép bị cấm không lặng lẽ vào môi trường sản xuất.

### Thiết lập Văn phòng chương trình mã nguồn mở (OSPO)

Nếu bạn tiêu thụ mã nguồn mở ở quy mô, hãy tạo một đầu mối, một OSPO, sở hữu chiến lược mã nguồn mở, chính sách, công cụ tuân thủ, quản trị đóng góp và quan hệ cộng đồng. OSPO kiềm chế sự hỗn loạn khi mỗi đội tự quyết. Nó cung cấp chuyên môn mà từng đội không duy trì được. Và nó nắm giữ giá trị chiến lược: quyết định đầu tư vào dự án nào, khi nào đóng góp ngược dòng, và cách phát hành tốt các dự án mã nguồn mở của chính bạn. Ngay cả một OSPO nhỏ (đôi khi một người cộng một nhóm làm việc liên chức năng) cũng cải thiện đáng kể tính nhất quán và giảm rủi ro pháp lý so với tình trạng tự do.

### Quản trị đóng góp và, nơi phù hợp, công bố

Hãy quyết định có chủ đích khi nào đóng góp ngược lại. Đóng góp ngược dòng các bản sửa và tính năng cho dự án bạn phụ thuộc giảm gánh nặng bảo trì, vì bạn thôi mang các bản vá riêng. Nó cũng xây thiện chí và ảnh hưởng, và củng cố các thành phần trọng yếu với bạn. Cung cấp cho nhà phát triển một quy trình rõ ràng, nhanh cho các đóng góp đã được phê duyệt, gồm cách xử lý sở hữu trí tuệ và thỏa thuận người đóng góp. Khi phát hành dự án mã nguồn mở của chính bạn, hãy làm cho đúng: chọn giấy phép phù hợp, lập tài liệu quản trị, và cam kết quản gia. Một dự án bị bỏ rơi hại danh tiếng của bạn hơn là không có dự án nào.

### Đáp ứng nhiệm vụ mã nguồn mở của chính phủ và "tiền công, mã công"

Các đội khu vực công nên coi sự cởi mở là mặc định. Ưu tiên tiêu chuẩn mở để tránh khóa chặt và làm việc qua các cơ quan và nhà cung cấp. Công bố công khai mã nguồn phát triển bằng quỹ công, trừ khi áp dụng một ngoại lệ cụ thể, có tài liệu: cho thành phần nhạy cảm bảo mật, quyền bên thứ ba, hay mối quan ngại về riêng tư. Tái sử dụng trước khi xây: kiểm tra xem cơ quan khác đã phát hành mã phù hợp chưa. Đưa các kỳ vọng này vào mua sắm, để nhà cung cấp giao mã mở, tái sử dụng được, được lập tài liệu tốt với chính phủ giữ các quyền thích hợp, thay vì hộp đen độc quyền mà cơ quan không bảo trì hay chia sẻ được.

### Quản lý phụ thuộc và phần mềm hết vòng đời

Hãy duy trì bản kiểm kê sống (SBOM) về mọi thành phần và phiên bản, giấy phép và trạng thái bảo trì của nó. Giữ phụ thuộc khá cập nhật. Cập nhật nhỏ, thường xuyên rẻ và an toàn hơn nhiều so với những bước nhảy khổng lồ hiếm hoi. Theo dõi các dự án ngược dòng để biết thông báo hết vòng đời và cửa sổ hỗ trợ bảo mật, và lập kế hoạch di chuyển trước khi hỗ trợ kết thúc, không phải sau khi một lỗ hổng buộc phải chạy đua. Với các thành phần trọng yếu có nguy cơ bị bỏ rơi, hãy quyết định trước bạn sẽ tài trợ người bảo trì, tự đóng góp bảo trì, rẽ nhánh, hay thay thế. Theo dõi hết vòng đời cho cả phần mềm thương mại và nguồn mở, và coi việc hết hỗ trợ theo cùng tiêu chuẩn như bất kỳ rủi ro vận hành nào khác.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Tiêu thụ mã nguồn mở tự do | Phân phối nhanh; đòn bẩy lớn; không phí giấy phép | Nghĩa vụ giấy phép, bảo mật và bảo trì giờ bạn sở hữu |
| Danh sách cho phép giấy phép nghiêm ngặt | Rủi ro pháp lý thấp; khả đoán | Làm chậm các đội; có thể loại trừ thành phần thực sự hữu ích |
| Chỉ giấy phép cho phép rộng rãi | Nghĩa vụ tối thiểu; dễ kết hợp | Bỏ qua các dự án copyleft có giá trị; ít có đi có lại |
| Chấp nhận copyleft nơi phù hợp | Tiếp cận hệ sinh thái mạnh; lợi ích có đi có lại | Cần cẩn trọng khi kết hợp và phân phối |
| Đóng góp ngược dòng | Ít gánh nặng bản vá riêng; ảnh hưởng; thiện chí | Công sức liên tục; chi phí chung về SHTT và quy trình |
| Xây độc quyền thay thế | Kiểm soát đầy đủ; không nghĩa vụ bên ngoài | Chi phí cao; phát minh lại hàng hóa thông dụng; bạn bảo trì mãi mãi |
| Chính phủ công bố theo mặc định | Minh bạch; tái sử dụng; tránh khóa chặt | Công sức công bố; rà soát bảo mật; quản gia bền vững |

Căng thẳng trung tâm là giữa vận tốc nhà phát triển và kiểm soát. Khóa mọi thứ sau rà soát nặng, và nhà phát triển đi vòng chính sách. Điều đó tạo ra phụ thuộc bóng không được quản lý, tệ hơn cách tiếp cận dễ dãi nhưng hiển thị. Để hoàn toàn không kiểm soát, và bạn tích lũy nợ pháp lý và bảo mật vô hình. Cách giải quyết là tự động hóa và tuyển chọn: làm đường tuân thủ thành đường nhanh nhất, qua thành phần đã thẩm định trước, quét đường ống và mặc định rõ ràng, để bạn có kiểm soát mà không ma sát. Về copyleft, đánh đổi không phải "rủi ro so với an toàn" mà là "được hiểu so với không." Copyleft hoàn toàn dùng được một khi bạn biết cách kết hợp và phân phối.

## Câu hỏi để thảo luận với đội của bạn

1. **Quy tắc tường minh của bạn cho copyleft mạnh và copyleft mạng qua ngữ cảnh nội bộ, phân phối và phục vụ qua mạng là gì?** Copyleft là ràng buộc thiết kế, không phải điều cấm kỵ, và các nghĩa vụ xoay quanh hai điều: bạn có phân phối phần mềm không và bạn kết hợp các thành phần chặt đến đâu. GPL trong một công cụ nội bộ hành xử rất khác với GPL liên kết vào sản phẩm bạn phát hành, và AGPL mở rộng nghĩa vụ tiết lộ sang phần mềm bạn chỉ cung cấp qua mạng, điều đổi phép tính xây-so-với-áp-dụng của bạn cho bất cứ thứ gì bạn chạy như dịch vụ. Hãy viết quy tắc theo từng ngữ cảnh, để nhà phát triển biết mà không cần gọi luật sư rằng (ví dụ) cho phép rộng rãi được phê duyệt trước ở mọi nơi, copyleft mạnh ổn nội bộ nhưng bị chặn khỏi sản phẩm phát hành, và AGPL cần rà soát trước khi chạm vào dịch vụ nối mạng. Hãy mang bằng chứng: quét cây phụ thuộc hiện tại của bạn và tìm xem các thành phần copyleft đã nằm đâu so với ranh giới phân phối của bạn. Rồi chặn bản dựng theo chính sách đó, vì một quy tắc không máy quét nào thực thi là quy tắc nhà phát triển sẽ vô tình phá.

2. **Bạn có cần Văn phòng chương trình mã nguồn mở không, và hôm nay ai sở hữu chính sách giấy phép, quét và quyết định đóng góp?** Nếu câu trả lời trung thực là "không ai" hoặc "mỗi đội tự quyết," bạn đang chạy tình trạng tự do tích lũy nợ pháp lý và bảo mật vô hình. Một OSPO, dù chỉ một người cộng một nhóm làm việc liên chức năng, kiềm chế sự hỗn loạn đó và nắm giữ giá trị chiến lược: dự án ngược dòng nào để đầu tư, khi nào đóng góp, và cách phát hành tốt các dự án của chính bạn. Hãy mang bằng chứng đến cuộc họp: có ai đưa ra được danh sách giấy phép được phê duyệt hiện tại, SBOM, và tên người sẽ tiếp câu hỏi copyleft trong thẩm định mua lại không? Câu trả lời nên giao quyền sở hữu rõ ràng và làm đường tuân thủ thành đường nhanh nhất, qua thành phần đã thẩm định trước và quét đường ống, để nhà phát triển có kiểm soát mà không ma sát. Một chính sách chậm hơn sao chép mã sẽ đơn giản bị phớt lờ.

3. **Phụ thuộc nào sẽ gây đau nhất nếu bị bỏ rơi ngày mai, và phản ứng định trước của bạn cho mỗi cái là gì?** Mọi phụ thuộc cuối cùng đều hết vòng đời, và phiên bản đắt đỏ của sự kiện đó là phát hiện một thành phần cốt lõi đã mất hỗ trợ từ nhiều tháng, chỉ khi một lỗ hổng buộc chú ý. Với các thành phần trọng yếu có nguy cơ bị bỏ rơi, hãy quyết định trước bạn sẽ tài trợ người bảo trì, tự đóng góp bảo trì, rẽ nhánh, hay thay thế. Hãy mang bằng chứng: từ SBOM của bạn, liệt kê các thành phần mà sự cố sẽ dừng một dịch vụ doanh thu hay sứ mệnh trọng yếu, và ghi trạng thái bảo trì cùng cửa sổ hỗ trợ bảo mật của từng cái. Câu trả lời nên biến hết vòng đời từ bất ngờ thành rủi ro vận hành được theo dõi với di chuyển có kế hoạch, theo cùng tiêu chuẩn như bất kỳ rủi ro nào khác. Giữ phụ thuộc cập nhật theo bước nhỏ, thường xuyên rẻ hơn nhiều so với bước nhảy khổng lồ, bị ép, hiếm hoi.

4. **Bạn có tạo được một SBOM đầy đủ, hiện hành đi hết xuống cây phụ thuộc bắc cầu không, và nhanh đến đâu?** Khi một lỗ hổng gây chú ý đáp xuống một thư viện được dùng rộng rãi, câu hỏi đầu tiên của lãnh đạo là "chúng ta có phơi nhiễm không, và ở đâu?" Một đội không trả lời được trong vài giờ đã tụt hậu, vì rủi ro thật thường ẩn vài tầng sâu trong các phụ thuộc không ai cố ý chọn. Cân nhắc đối lập là chi phí và nhiễu: kiểm kê bắc cầu đầy đủ qua nhiều dịch vụ tạo danh sách lớn, biến động, và cảnh báo quá mức dạy mọi người phớt lờ nó, nên bạn phải quyết định độ sâu nào và mức nghiêm trọng nào thực sự kích hoạt hành động. Hãy mang bằng chứng vào cuộc thảo luận: thử tạo SBOM mới cho một dịch vụ sản xuất ngay bây giờ, đếm bao nhiêu thành phần trực tiếp so với bắc cầu, và đo mất bao lâu. Với tổ chức doanh nghiệp hay chính phủ, hãy gắn điều này với mục tiêu ứng phó sự cố cụ thể và với bất kỳ nghĩa vụ pháp lý nào phải tiết lộ thành phần bị ảnh hưởng, vì nhiệm vụ báo cáo phơi nhiễm bạn không liệt kê được là nhiệm vụ bạn sẽ vi phạm.

5. **Khi nào một phụ thuộc trọng yếu đáng được tài trợ, đóng góp hay quản gia, thay vì coi là miễn phí?** Hầu hết tổ chức tiêu thụ mã nguồn mở như một tiện ích, rồi bị sốc khi một thành phần nâng đỡ một dịch vụ doanh thu hóa ra là một tình nguyện viên không lương. Quyết định có chủ đích tài trợ người bảo trì, đóng góp bản sửa ngược dòng, hoặc phát hành và quản gia dự án của chính bạn biến một đầu vào miễn phí mong manh thành đầu vào bền vững, có ảnh hưởng, và nó ngăn kỹ sư của bạn mang bản vá riêng qua mỗi lần nâng cấp. Căng thẳng là đóng góp và quản gia tốn thời gian kỹ thuật thật, liên tục và mang chi phí chung về sở hữu trí tuệ và quy trình, nên bạn không làm được cho mọi thứ. Hãy mang bằng chứng: từ SBOM của bạn, đánh dấu vài thành phần mà sự cố sẽ dừng một dịch vụ trọng yếu sứ mệnh, và ghi số người bảo trì, tài trợ của từng cái, và bạn đã mang bao nhiêu bản vá riêng chống lại nó. Với tổ chức lớn hay công, hãy cân nhắc chi phí danh tiếng của một bản phát hành mã nguồn mở bị bỏ rơi mà bạn đã công bố rầm rộ, và, trong chính phủ, hãy coi quản gia bền vững mã tiền công đã công bố là một phần của phân phối, không phải phần thêm tùy chọn.

6. **Mua sắm của bạn có thực sự giao mã mở, tái sử dụng được, lập tài liệu tốt với các quyền bạn cần, hay hộp đen độc quyền bạn không bảo trì hay thoát được?** Hợp đồng viết không có chuyên môn mã nguồn mở thường xuyên trao cho nhà cung cấp quyền kiểm soát mà bạn sẽ hối tiếc: định dạng đóng, không có quyền công bố hay sửa đổi, và phụ thuộc mà cơ quan không vá được khi nhà cung cấp đi tiếp. Làm đúng sớm rẻ hơn nhiều so với phát hiện lúc gia hạn rằng bạn không rời đi được. Các cân nhắc đối lập là tốc độ và lựa chọn nhà cung cấp: đòi sản phẩm bàn giao mở và khả năng di chuyển có thể thu hẹp thị trường và làm chậm việc trao thầu, và một số nhà cung cấp thực sự hữu ích kháng cự điều đó. Hãy mang bằng chứng: lấy hai hợp đồng gần đây và kiểm tra chúng có quy định điều khoản giấy phép, giao mã nguồn, tiêu chuẩn tài liệu, cung cấp SBOM, và các quyền tổ chức giữ lại không. Với mua sắm doanh nghiệp, hãy nối điều này với phân tích khóa chặt và tổng chi phí; với chính phủ, nối nó với mặc định mở và nhiệm vụ "tiền công, mã công", và với quy trình ngoại lệ có tài liệu cho phép bạn chỉ đóng các phần nhạy cảm bảo mật thay vì cả hệ thống.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Bạn lắp ráp gần như mọi thứ từ mã nguồn mở và không có luật sư, nên hãy giữ quy tắc trong một trang: giấy phép cho phép rộng rãi như MIT và Apache 2.0 được phê duyệt trước, copyleft mạnh ổn cho công cụ nội bộ nhưng bị chặn khỏi sản phẩm phát hành, và bất cứ thứ gì lạ được người sáng lập rà soát nhanh. Thêm quét giấy phép và lỗ hổng vào đường ống và giữ SBOM từ ngày đầu, vì thời điểm rẻ nhất để làm đúng là trước khi thẩm định của bên mua lại lục soát cây phụ thuộc của bạn. Đừng cấm copyleft vì sợ; hãy hiểu nó, và đi tiếp.

**Doanh nghiệp nhỏ.** Không có chuyên gia mã nguồn mở và ngân sách eo hẹp, hãy dựa vào công cụ hơn nhân sự: một máy quét trong bản dựng và danh sách giấy phép được phê duyệt ngắn làm phần lớn việc một người sẽ làm. Đóng khung tiêu thụ là mua-so-với-xây một cách trung thực, vì phát minh lại một thành phần mở được bảo trì tốt thường là lựa chọn đắt, nhưng phụ thuộc vào một cái bạn không bao giờ kiểm kê cũng vậy. Giữ bản ghi đơn giản về cái bạn dùng và theo giấy phép nào, để bảng câu hỏi bảo mật của khách hàng hay cảnh báo lỗ hổng không thành cuộc chạy đua.

**Doanh nghiệp lớn.** Ở quy mô, vấn đề là nhất quán qua nhiều đội, nên hãy lập một OSPO sở hữu chính sách, quét tự động, tạo ghi công và quản trị đóng góp, và làm đường tuân thủ thành đường nhanh nhất qua các thành phần được tuyển chọn, đã thẩm định trước. Thực thi quy tắc copyleft theo ngữ cảnh trong đường ống, duy trì SBOM qua các dịch vụ, và quản lý độ cập nhật phụ thuộc và hết vòng đời như rủi ro vận hành được theo dõi. Coi mã nguồn mở là quản lý chuỗi cung ứng cho phần lớn cơ sở mã của bạn, với bằng chứng sẵn sàng cho kiểm toán trong thẩm định mua lại.

**Chính phủ.** Sự cởi mở thường được bắt buộc, không tùy chọn, nên mặc định là tiêu chuẩn mở và công bố mã tiền công trừ khi áp dụng ngoại lệ có tài liệu cho bảo mật, quyền bên thứ ba hay riêng tư. Tái sử dụng trước khi xây bằng cách kiểm tra danh mục xuyên chính phủ, và đưa sản phẩm bàn giao mở, tái sử dụng được, lập tài liệu tốt cùng quyền được giữ lại vào mua sắm để bạn nhận mã bảo trì được thay vì hộp đen độc quyền. Giữ mã đã công bố theo quản gia thực sự, và giữ quy trình ngoại lệ hẹp và minh bạch để nó chỉ đóng những gì buộc phải đóng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người xây ứng dụng di động lắp ráp gần như mọi thứ từ mã nguồn mở và không có luật sư trong nhân sự. Thay vì cấm copyleft vì sợ, những người sáng lập viết chính sách một trang: giấy phép cho phép rộng rãi như MIT và Apache 2.0 được phê duyệt trước, copyleft mạnh như GPL ổn cho công cụ nội bộ nhưng bị chặn khỏi ứng dụng phát hành để tránh nghĩa vụ tiết lộ, và bất cứ thứ gì bất thường được người sáng lập rà soát nhanh. Họ thêm quét giấy phép và lỗ hổng vào đường ống để một giấy phép bị cấm không lọt vào bản phát hành, giữ SBOM từ ngày đầu, và đóng góp ngược dòng một bản sửa nhỏ cho một thư viện trọng yếu để thôi mang bản vá riêng qua mỗi lần nâng cấp. Làm đúng sớm cũng giúp họ khỏi bất ngờ đau đớn khi thẩm định của bên mua lại cuối cùng lục soát cây phụ thuộc.

**Doanh nghiệp lớn.** Một nhà cung cấp phần mềm phát hành sản phẩm phân phối chạy một OSPO. OSPO duy trì danh sách giấy phép được phê duyệt, một kho thành phần được tuyển chọn nội bộ, và quét giấy phép và lỗ hổng tự động trong mọi đường ống. Khi nhà phát triển kéo vào một phụ thuộc mới, đường ống kiểm tra giấy phép của nó theo chính sách, tạo thông báo ghi công phát hành cùng sản phẩm, và gắn cờ bất cứ thứ gì cần rà soát. Thành phần copyleft mạnh được cho phép cho công cụ nội bộ nhưng bị chặn khỏi sản phẩm phân phối, để tránh nghĩa vụ tiết lộ. Công ty đóng góp ngược dòng bản sửa cho một vài phụ thuộc trọng yếu. Điều đó xóa sạch tồn đọng bản vá riêng mà kỹ sư của họ từng mang qua mỗi lần nâng cấp.

**Chính phủ.** Một dịch vụ số quốc gia vận hành theo chính sách "tiền công, mã công". Dịch vụ mới được xây trên tiêu chuẩn mở, phát triển công khai trên kho mã công cộng theo mặc định, và tái sử dụng qua các cơ quan. Mẫu mua sắm của nó yêu cầu nhà cung cấp giao mã mở, lập tài liệu tốt, tái sử dụng được, với chính phủ giữ quyền công bố và sửa đổi. Trước khi bắt đầu một thành phần mới, các đội tìm trong danh mục xuyên chính phủ mã tái sử dụng sẵn có. Các mô-đun nhạy cảm bảo mật được miễn công bố qua quy trình có tài liệu, thay vì làm cả hệ thống đóng.

## Luận chứng kinh doanh: động lực, ROI và TCO

Quản lý mã nguồn mở tốt là sự khác biệt giữa nắm lấy đòn bẩy khổng lồ của nó và trả chi phí ẩn của nó. Mã nguồn mở cho phép một tổ chức lớn đứng trên nền móng nó không bao giờ đủ khả năng xây. Nhưng [tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership) gồm tuân thủ, vá bảo mật và di chuyển cuối cùng, những chi phí đến dù bạn có lên kế hoạch hay không. Quản lý có chủ đích biến các khủng hoảng khó đoán, đắt đỏ thành các chi phí nhỏ, đều, có kế hoạch. Các khủng hoảng đó gồm vi phạm copyleft bị phát hiện trong thẩm định mua lại, di chuyển khẩn cấp khỏi thành phần bị bỏ rơi, hay lỗ hổng trong phụ thuộc không ai biết có ở đó.

Chi phí áp dụng khiêm tốn so với phơi nhiễm: một OSPO hay nhóm làm việc, công cụ quét, và kỷ luật giữ bản kiểm kê. Chi phí của việc *không* áp dụng hiện ra là trách nhiệm pháp lý, thẩm định thất bại, sự cố bảo mật truy về phụ thuộc chưa vá, và chi phí cộng dồn của nâng cấp bị hoãn cuối cùng buộc phải di chuyển đại bùng nổ đau đớn. Khi lập luận với ban lãnh đạo, hãy đóng khung quản lý mã nguồn mở là quản lý chuỗi cung ứng cho phần lớn cơ sở mã của bạn. Cũng lưu ý lợi thế chiến lược: tránh khóa chặt, phân phối nhanh hơn, thu hút nhân tài, và ảnh hưởng lên các hệ sinh thái bạn phụ thuộc. Trong chính phủ, thêm chiều nhiệm vụ. Sự cởi mở thường được yêu cầu, không tùy chọn, và làm tốt tránh được cả không tuân thủ lẫn chi tiêu công trùng lặp.

## Phản mẫu và cạm bẫy

- **Cấp phép sao chép-dán.** Nhà phát triển kéo thành phần vào mà không kiểm tra giấy phép, chỉ phát hiện nghĩa vụ lúc kiểm toán hay mua lại.
- **Không có bản kiểm kê.** Không trả lời được "chúng ta đang dùng gì và theo giấy phép nào?" khi một lỗ hổng hay câu hỏi giấy phép nổ ra.
- **Hoảng loạn copyleft.** Cấm mọi copyleft vì sợ thay vì hiểu, bỏ qua các hệ sinh thái có giá trị.
- **Bản phát hành mã nguồn mở bị bỏ rơi.** Công bố một dự án rầm rộ rồi không bao giờ bảo trì, làm hại danh tiếng.
- **Phớt lờ phụ thuộc bắc cầu.** Thẩm định phụ thuộc trực tiếp trong khi rủi ro thật ẩn vài tầng sâu.
- **Bất ngờ hết vòng đời.** Phát hiện một thành phần cốt lõi đã mất hỗ trợ từ nhiều tháng, chỉ khi một lỗ hổng buộc chú ý.
- **Chính sách chậm hơn sao chép.** Quy trình tuân thủ nặng đến mức nhà phát triển đi vòng, tạo phụ thuộc bóng vô hình.
- **Hộp đen chính phủ.** Mua hệ thống độc quyền mà cơ quan không bảo trì, chia sẻ hay thoát được, vi phạm nguyên tắc mặc định mở.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Nhà phát triển thêm mã nguồn mở tự do mà không có chính sách hay bản kiểm kê. Giấy phép không được xem xét và nghĩa vụ copyleft không được biết. Hết vòng đời bị phát hiện tình cờ, thường khi một lỗ hổng buộc chú ý. Không ai sở hữu chiến lược mã nguồn mở.

**Mức 2: Phát triển.** Một chính sách cơ bản và danh sách giấy phép được phê duyệt tồn tại, và một số đội tuân theo. Quét có xảy ra, nhưng thường thủ công, muộn, hoặc chỉ trên vài dự án. Bản kiểm kê được giữ cho hệ thống lớn trong khi phụ thuộc bắc cầu không được ánh xạ. Đóng góp và xử lý hết vòng đời là tùy nghi và không nhất quán giữa các đội.

**Mức 3: Chuẩn hóa.** Một OSPO hoặc tương đương sở hữu chiến lược, chính sách và công cụ toàn tổ chức. Quét giấy phép và lỗ hổng được tự động hóa trong mọi đường ống, tệp ghi công và thông báo được tạo tự động, và bản dựng bị chặn để giấy phép bị cấm không vào được. SBOM được duy trì xuống cây bắc cầu, đóng góp theo quy trình có tài liệu, hết vòng đời được theo dõi với di chuyển có kế hoạch, và các đội chính phủ công bố theo mặc định.

**Mức 4: Quản lý.** Chương trình được đo và kiểm soát theo đường cơ sở. Bạn theo dõi độ phủ quét chính sách qua các dịch vụ, thời gian trung bình để vá một lỗ hổng phụ thuộc đã công bố, tỷ lệ thành phần nằm trong cửa sổ hỗ trợ bảo mật, tỷ lệ vi phạm giấy phép lọt qua, độ trễ cập nhật phụ thuộc, và số bản vá riêng được đóng góp ngược dòng. Vị trí copyleft so với ranh giới phân phối được giám sát, và các chỉ số so với mục tiêu thúc đẩy mỗi quyết định tiếp tục hay dừng thay vì ý kiến.

**Mức 5: Điều phối.** Mã nguồn mở là tài sản chiến lược được cải thiện liên tục, tích hợp trong toàn tổ chức. Tuân thủ được tự động hóa hoàn toàn và thành phần không tuân thủ không đến được môi trường sản xuất. Bạn đầu tư có chủ đích vào các dự án ngược dòng trọng yếu, đóng góp thường xuyên, và quản gia các dự án chạy tốt của chính bạn. Độ cập nhật phụ thuộc và hết vòng đời được quản lý thích ứng khi rủi ro và chỉ số dịch chuyển, và sự cởi mở trở thành lợi thế cạnh tranh và công dân thực sự.

## Ý tưởng để thảo luận

- Lằn ranh đúng giữa mặc định cho phép rộng rãi nhanh và kiểm soát cần thiết để tránh nợ pháp lý và bảo mật nằm ở đâu?
- Khi nào một tổ chức nên tài trợ hoặc bảo trì một phụ thuộc ngược dòng trọng yếu thay vì coi nó là miễn phí?
- Làm sao bạn quyết định thành phần nào của chính mình đáng phát hành và quản gia như mã nguồn mở?
- Với chính phủ, quy trình bảo vệ được để miễn thành phần khỏi công bố theo mặc định mà không xói mòn nguyên tắc là gì?
- Rà soát giấy phép và bảo mật phải đi sâu vào phụ thuộc bắc cầu đến đâu một cách thực tế?
- Copyleft mạng (AGPL) có đổi phép tính xây-so-với-áp-dụng của bạn cho phần mềm bạn cung cấp như dịch vụ không?

## Những điểm cần ghi nhớ

- Mã nguồn mở là phần lớn của hầu hết cơ sở mã và phải được quản lý như chuỗi cung ứng, không coi là miễn phí và không hệ quả.
- Giấy phép mang nghĩa vụ thật; hãy hiểu các họ cho phép rộng rãi, copyleft yếu, copyleft mạnh và copyleft mạng, và cách phân phối và kết hợp kích hoạt nghĩa vụ.
- Làm đường tuân thủ thành đường nhanh nhất qua tuyển chọn, quét tự động và mặc định rõ ràng, nếu không nhà phát triển sẽ đi vòng chính sách.
- Lập một OSPO để sở hữu chiến lược, tuân thủ, đóng góp và quản gia ở quy mô.
- Duy trì SBOM, giữ phụ thuộc cập nhật theo bước nhỏ, và lên kế hoạch cho hết vòng đời trước khi nó buộc thành khủng hoảng.
- Trong chính phủ, mặc định là tiêu chuẩn mở và công bố mã tiền công, tái sử dụng trước khi xây.

## Tài liệu tham khảo và đọc thêm

- Heather Meeker, *Open (Source) for Business* và *Open Source for Business*
- Van Lindberg, *Intellectual Property and Open Source*
- The Linux Foundation và TODO Group, *OSPO guides* và *Open Source Program Office resources*
- OpenChain (ISO/IEC 5230), *Open Source Licence Compliance*
- Software Package Data Exchange (SPDX, ISO/IEC 5962) specification
- CycloneDX SBOM specification
- Free Software Foundation, *GNU General Public Licence* và *GPL FAQ*
- Open Source Initiative, *The Open Source Definition* và danh sách giấy phép được phê duyệt
- Free Software Foundation Europe, *Public Money, Public Code*
- U.S. Federal Source Code Policy và hướng dẫn Code.gov
- UK Government, *Technology Code of Practice* và các nguyên tắc tiêu chuẩn mở
