# 8.1 CI/CD và phân phối

## Tổng quan và động lực

[Tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) và [phân phối liên tục](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) là mô liên kết giữa việc viết mã và đưa nó đến người dùng một cách an toàn. Tích hợp liên tục nghĩa là mọi thay đổi được hợp nhất thường xuyên vào nhánh chính dùng chung, rồi được dựng và kiểm thử tự động, để các vấn đề tích hợp nổi lên trong vài phút thay vì ở cuối một chu kỳ phát hành dài. Phân phối liên tục nghĩa là mọi thay đổi vượt qua đường ống được giữ ở trạng thái triển khai được, để phát hành lên môi trường sản xuất trở thành một quyết định kinh doanh thay vì một cuộc chạy vạy kỹ thuật. [Triển khai liên tục](https://en.wikipedia.org/wiki/Continuous_deployment) đi thêm một bước và phát hành tự động mọi thay đổi vượt qua, không có cổng con người.

Với các đội lớn, những phân biệt này cực kỳ quan trọng. Khi hàng trăm kỹ sư commit vào các hệ thống chồng lấn, chi phí tích hợp thủ công và kiểm thử thủ công tăng phi tuyến. Một đường ống tự động, dùng chung là cách thực tế duy nhất để cho nhiều người đóng góp phản hồi nhanh, đáng tin và để thay đổi của đội này không lặng lẽ làm hỏng đội khác. Đường ống trở thành nguồn sự thật duy nhất về việc phần mềm có khỏe không, và nó thực thi một sự nhất quán mà không lượng tài liệu hay thiện chí nào bảo đảm được ở quy mô.

Bối cảnh doanh nghiệp và chính phủ thêm một chiều nữa: khả năng kiểm toán và kiểm soát thay đổi. Cơ quan quản lý, cán bộ bảo mật và kiểm toán viên cần bằng chứng rằng thay đổi đã được rà soát, kiểm thử và phê duyệt, và rằng hiện vật chạy trong môi trường sản xuất chính là hiện vật đã được dựng và thẩm định. Một đường ống CI/CD thiết kế tốt biến những nghĩa vụ tuân thủ này từ gánh nặng giấy tờ thành sản phẩm phụ tự động của quy trình kỹ thuật bình thường. Làm tốt, phân phối trở nên nhanh hơn và an toàn hơn cùng lúc, là kết quả quan trọng nhất với ban lãnh đạo.

*Xem thêm:* chương 8.4 (kỹ thuật nền tảng và trải nghiệm lập trình viên), chương 8.5 (tự động hóa kiểm thử và quy trình), và chương 7.4 (phân tích sản phẩm và thử nghiệm) về [cờ tính năng](https://en.wikipedia.org/wiki/Feature_toggle) (công tắc thời gian chạy phơi bày chức năng cho người dùng mà không triển khai lại) và các thực hành thử nghiệm mà phân phối tăng dần (phát hành một thay đổi dần dần trong khi tự động theo dõi các chỉ số sức khỏe của nó) cho phép.

## Các nguyên tắc chính

- Tích hợp thay đổi nhỏ thường xuyên; nhánh sống lâu là kẻ thù của tích hợp liên tục.
- Dựng hiện vật một lần và thăng cấp đúng hiện vật đó qua mọi môi trường.
- Biến đường ống thành cổng có thẩm quyền: nếu nó xanh, thay đổi phát hành được; nếu nó đỏ, công việc dừng cho đến khi sửa xong.
- Tối ưu không ngừng cho phản hồi nhanh để lập trình viên giữ được dòng chảy và lỗi bị bắt khi ngữ cảnh còn tươi.
- Tự động hóa mọi thứ lặp lại, gồm kiểm thử, quét bảo mật, cung cấp và triển khai.
- Coi định nghĩa đường ống là mã có quản lý phiên bản chịu rà soát, không phải cấu hình bảng điều khiển nhấp chuột.
- Thiết kế cho các bản phát hành an toàn, đảo ngược được để mọi triển khai có thể được hoàn tác nhanh.
- Tách triển khai (cài mã) khỏi phát hành (phơi bày nó cho người dùng) bằng cờ tính năng.

## Khuyến nghị

### Thiết kế đường ống như một chuỗi cổng chất lượng

Hãy cấu trúc đường ống thành các giai đoạn tiến từ rẻ và nhanh đến đắt và kỹ lưỡng: biên dịch và kiểm thử đơn vị trước, rồi kiểm thử tích hợp, quét bảo mật và giấy phép, và cuối cùng là triển khai lên staging và môi trường sản xuất. Mỗi giai đoạn là một cổng mà thay đổi phải qua. Sắp thứ tự các cổng để các kiểm tra nhanh nhất, có khả năng thất bại nhất chạy trước, cho lập trình viên phản hồi trong thời gian ngắn nhất có thể. Giữ vòng phản hồi giai đoạn commit dưới mười phút bất cứ khi nào có thể. Quá mức đó, lập trình viên chuyển ngữ cảnh và năng suất giảm.

### Dựng một lần, thăng cấp khắp nơi

Hãy tạo một hiện vật bất biến duy nhất trong giai đoạn dựng và thăng cấp đúng hiện vật đó qua kiểm thử, staging và môi trường sản xuất. Đừng bao giờ dựng lại cho từng môi trường, vì dựng lại có thể lặng lẽ đưa vào khác biệt. Cấu hình thay đổi theo môi trường nên được tiêm lúc triển khai, không nướng vào các bản dựng riêng. Thực hành này cũng là thứ cho phép bạn nói với kiểm toán viên, chắc chắn, rằng tệp nhị phân trong môi trường sản xuất là tệp đã vượt qua mọi cổng.

### Biến đường ống thành điểm thực thi chính sách

Hãy mã hóa các kiểm tra bắt buộc (phê duyệt rà soát mã, ngưỡng độ phủ kiểm thử, kết quả quét bảo mật, commit đã ký) trực tiếp vào đường ống và quy tắc bảo vệ nhánh. Chính sách thủ công sống trong wiki thường xuyên bị bỏ qua dưới áp lực hạn chót. Chính sách được mã hóa trong đường ống được áp dụng đồng đều và tự động cho mọi thay đổi.

### Giữ nhánh chính luôn phát hành được

Hãy dùng phát triển dựa trên thân cây, tích hợp mọi công việc vào một nhánh dùng chung duy nhất với ít hoặc không có nhánh sống lâu, hoặc dùng nhánh tính năng sống ngắn, và dựa vào cờ tính năng để giấu công việc chưa hoàn tất thay vì nhánh sống lâu. Điều này giữ xung đột hợp nhất nhỏ và giữ nhánh chính luôn ở trạng thái triển khai được, là điều kiện tiên quyết cho phân phối liên tục đích thực.

### Chọn chiến lược triển khai có chủ đích

Hãy khớp chiến lược triển khai với rủi ro và bán kính ảnh hưởng của dịch vụ:

- Triển khai **cuốn chiếu** thay các thể hiện dần dần và là mặc định hợp lý cho dịch vụ không trạng thái.
- **[Xanh-lam](https://en.wikipedia.org/wiki/Blue-green_deployment)** duy trì hai môi trường giống hệt nhau và chuyển lưu lượng cùng lúc, cho một đường hoàn tác tức thì.
- Phát hành **canary** định tuyến một phần trăm nhỏ lưu lượng đến phiên bản mới, theo dõi chỉ số sức khỏe, và chỉ mở rộng nếu tín hiệu tốt.
- **Cờ tính năng** tách phát hành khỏi triển khai, cho phép bạn bật chức năng cho người dùng hay nhóm cụ thể mà không triển khai lại.

### Áp dụng phân phối tăng dần với hoàn tác tự động

Phân phối tăng dần kết hợp phát hành canary với phân tích tự động các chỉ số như tỷ lệ lỗi, độ trễ và độ bão hòa. Hãy xác định tiêu chí sức khỏe khách quan từ trước, rồi để hệ thống tự thăng cấp hoặc hoàn tác dựa trên các tín hiệu đó. Hoàn tác tự động loại bỏ sự do dự của con người vốn biến một sự cố nhỏ thành lớn.

### Cung cấp quản lý phát hành và kiểm soát thay đổi cho môi trường chịu quy định

Trong bối cảnh chịu quy định, hãy giữ một hồ sơ quản lý thay đổi nhẹ nhưng thật. Tự động nắm bắt ai đã phê duyệt mỗi thay đổi, kiểm thử nào đã chạy, và hiện vật nào đã được triển khai. Dùng quy trình tư vấn thay đổi cho các thay đổi thực sự rủi ro cao, nhưng chỉ dành cho những trường hợp đó. Đưa mọi thay đổi thường lệ qua một hội đồng hằng tuần phá hủy giá trị của tự động hóa. Thay vào đó hãy nhắm đến các loại thay đổi chuẩn, được phê duyệt trước chảy qua đường ống mà không nghi thức.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Phân phối liên tục (cổng phát hành thủ công) | Doanh nghiệp kiểm soát thời điểm; mạnh cho cửa sổ phát hành chịu quy định | Đòi kỷ luật để giữ nhánh chính phát hành được | Doanh nghiệp có cửa sổ thay đổi |
| Triển khai liên tục (hoàn toàn tự động) | Phản hồi nhanh nhất; lô nhỏ nhất | Đòi kiểm thử và khả năng quan sát trưởng thành | Đội tin cậy cao, tần suất cao |
| Xanh-lam | Hoàn tác tức thì; mô hình tư duy đơn giản | Nhân đôi chi phí môi trường lúc chuyển | Dịch vụ trọng yếu cần hoàn nguyên nhanh |
| Canary + phân phối tăng dần | Giới hạn bán kính ảnh hưởng; dựa trên dữ liệu | Phức tạp để xây; cần chỉ số tốt | Hệ thống hướng người dùng quy mô lớn |
| Cờ tính năng | Tách triển khai khỏi phát hành | Nợ cờ nếu không dọn | Đội phát hành an toàn công việc chưa hoàn tất |

Đánh đổi trung tâm là tốc độ so với kiểm soát, nhưng đó thường là lựa chọn sai. Tự động hóa trưởng thành mang lại cả hai: bản phát hành nhanh hơn vì chúng nhỏ hơn, và an toàn hơn vì mỗi cái được xác minh và đảo ngược được. Chi phí thực là khoản đầu tư ban đầu vào độ phủ kiểm thử, khả năng quan sát và kỹ thuật đường ống, cộng kỷ luật liên tục để giữ chúng khỏe. Các tổ chức keo kiệt khoản đầu tư đó có tốc độ mà không có sự an toàn, còn tệ hơn một quy trình thủ công chậm.

## Câu hỏi để thảo luận với đội của bạn

1. **Mục tiêu thời gian phản hồi giai đoạn commit của bạn là gì, và cái gì bị cắt khi bộ kiểm thử vượt quá mười phút?** Một giai đoạn commit chậm lặng lẽ giết tích hợp liên tục, vì lập trình viên thôi chờ xanh và bắt đầu gom thay đổi. Hãy quyết định con số ngay bây giờ (chương này lập luận dưới mười phút) và quyết định cơ chế để giữ nó: worker song song, kim tự tháp kiểm thử nghiêm ngặt, và chuyển kiểm tra tích hợp chậm sang giai đoạn sau. Ở quy mô doanh nghiệp đây là quyết định nền tảng, vì hàng trăm kỹ sư dùng chung đường ống và mỗi phút thêm nhân lên qua mọi commit. Hãy mang dữ liệu thật đến cuộc họp: thời lượng đường ống p50 và p95 hiện tại, mười kiểm thử chậm nhất, và mọi người chạy lại bao nhiêu lần thay vì chờ. Nếu bạn không nêu được mục tiêu và bảo vệ nó bằng con số, đường ống của bạn đang trôi về một quy trình lô khoác áo CI.

2. **Mỗi dịch vụ dùng chiến lược triển khai nào, và ai chịu trách nhiệm về lựa chọn đó?** Cuốn chiếu, xanh-lam và canary không thay thế được cho nhau: chúng đánh đổi chi phí, tốc độ hoàn tác và độ phức tạp khác nhau, và lựa chọn đúng phụ thuộc vào bán kính ảnh hưởng của dịch vụ. Xanh-lam mua hoàn tác tức thì với giá môi trường nhân đôi lúc chuyển, đáng với hệ thống thanh toán và lãng phí với một bảng điều khiển nội bộ. Canary giới hạn phơi nhiễm nhưng đòi chỉ số sức khỏe tốt và nhiều kỹ thuật đường ống hơn. Với một hệ sinh thái lớn hay chịu quy định, để thói quen của từng đội quyết định tạo ra sự không nhất quán nổi lên trong một sự cố, nên hãy thống nhất mặc định theo từng bậc dịch vụ và ghi lại quyết định. Hãy mang danh mục dịch vụ và gắn thẻ mỗi dịch vụ với chiến lược, đường hoàn tác và người sở hữu quyết định đó.

3. **Làm sao bạn chứng minh hiện vật trong môi trường sản xuất chính là cái đã vượt qua mọi cổng?** Dựng một lần và thăng cấp đúng hiện vật đó là toàn bộ cuộc chơi cho khả năng kiểm toán, và nó vỡ ngay khi ai đó dựng lại theo từng môi trường hoặc vá một máy đang chạy. Trong bối cảnh doanh nghiệp và chính phủ, kiểm toán viên sẽ yêu cầu bạn truy một tệp nhị phân đang chạy về commit, rà soát và phê duyệt của nó, và bạn muốn câu trả lời mất vài giây, không phải một tuần. Hãy quyết định bạn thực thi nó thế nào: hiện vật bất biến, ảnh đã ký, xác minh chữ ký lúc triển khai, và cấu hình được tiêm lúc triển khai thay vì nướng vào các bản dựng riêng. Hãy mang các khoảng trống hiện tại đến bàn, như bất kỳ giai đoạn nào dựng lại, bất kỳ đường vá nóng thủ công nào, và bất cứ nơi nào cấu hình phân nhánh hiện vật. Câu trả lời quyết định bằng chứng tuân thủ của bạn là sản phẩm phụ của đường ống hay cuộc chạy vạy thủ công trước mỗi cuộc kiểm toán.

4. **Khi nhánh chính đỏ, cái gì thực sự dừng, và bạn xử lý kiểm thử chập chờn thế nào?** Một đường ống chỉ là cổng có thẩm quyền nếu một bản dựng đỏ thực sự dừng công việc, vậy mà nhiều tổ chức lặng lẽ chấp nhận nhánh chính hỏng và tồn đọng thất bại ngắt quãng, dạy lập trình viên chạy lại cho đến khi xanh và phát hành chồng lên thất bại. Với một đội lớn sự mục rữa này cộng dồn, vì kiểm thử chập chờn bị phớt lờ của một đội thành cái cớ cho mọi người bỏ qua cổng, và lòng tin vào đường ống giữ rẻ hơn nhiều so với xây lại. Hãy cân nhắc các lực kéo đối lập: quy tắc dừng dây chuyền nghiêm ngặt bảo vệ chất lượng nhưng có thể chặn hàng trăm kỹ sư vì một commit tồi, trong khi chính sách lỏng giữ thông lượng và xói mòn cổng. Hãy mang bằng chứng vào cuộc thảo luận: thời gian đỏ nhánh chính hiện tại, số kiểm thử bị cách ly hoặc chập chờn, tỷ lệ chạy lại, và bao nhiêu lần thay đổi được hợp nhất trên một kiểm tra thất bại. Trong bối cảnh doanh nghiệp và chính phủ, hãy nêu ai sở hữu phân loại chập chờn và ai có thẩm quyền đóng băng hợp nhất, vì một cổng không ai chịu trách nhiệm thực thi là cổng mà kiểm toán viên sẽ thấy đã bị ghi đè thường xuyên.

5. **Vòng đời cờ tính năng của bạn là gì, và ai chịu trách nhiệm cho nghỉ hưu chúng?** Cờ là thứ cho phép bạn tách triển khai khỏi phát hành và giấu công việc chưa hoàn tất, nhưng mỗi cờ là một nhánh trong mã không tự dọn, và cờ không được quản lý tích tụ thành độ phức tạp có điều kiện mà không ai dám chạm. Trong một hệ sinh thái lớn khoản nợ này nguy hiểm, vì một cờ cũ có thể lặng lẽ chặn một bản sửa bảo mật hoặc lật các đường mã chưa kiểm thử vào môi trường sản xuất, và người tạo ra nó thường đã chuyển đi. Hãy cân bằng căng thẳng: cờ mua cho bạn phân phối tăng dần an toàn, nên mục tiêu không phải ít cờ hơn mà là một vòng đời có kỷ luật với chủ sở hữu, kỳ vọng hết hạn và công cụ làm lộ cờ cũ. Hãy mang bản kiểm kê hiện tại đến cuộc họp: bao nhiêu cờ đang sống, cờ cũ nhất bao nhiêu tuổi, cái nào không có chủ sở hữu, và liệu có cờ sống lâu nào nay hoạt động như cấu hình vĩnh viễn thuộc về nơi khác. Với môi trường chịu quy định, hãy thêm ai được đổi cờ trong môi trường sản xuất và liệu thay đổi đó có được ghi nhật ký chặt chẽ như một lần triển khai, vì một lần lật cờ là một bản phát hành ngay cả khi đường ống không bao giờ chạy.

6. **Ranh giới giữa phân phối liên tục với cổng con người và triển khai liên tục hoàn toàn nằm ở đâu, và ai đặt ngưỡng hoàn tác?** Phân phối liên tục giữ một người kiểm soát thời điểm phát hành, phù hợp cửa sổ thay đổi theo luật và hệ thống bán kính ảnh hưởng lớn, trong khi triển khai liên tục phát hành tự động mọi thay đổi vượt qua và đòi kiểm thử trưởng thành, khả năng quan sát và hoàn tác tự động để an toàn. Với một tổ chức lớn hay chịu quy định câu trả lời hiếm khi đồng nhất: trang tiếp thị của bạn có thể triển khai liên tục trong khi lõi thanh toán giữ cổng con người có tài liệu, và vạch lằn ranh đó theo từng bậc dịch vụ ngăn cả ma sát không cần thiết lẫn tự động hóa liều lĩnh. Các cân nhắc đối lập là tốc độ và kích thước lô so với kiểm soát và khả năng kiểm toán, cộng chi phí kỹ thuật của các chỉ số sức khỏe mà hoàn tác tự động đòi hỏi. Hãy mang bằng chứng: tỷ lệ thay đổi thất bại mỗi dịch vụ, thời gian phục hồi trung bình, nhịp phát hành hiện tại, và các tín hiệu khách quan (tỷ lệ lỗi, độ trễ, độ bão hòa) bạn tin để thăng cấp hay hoàn tác mà không cần con người. Trong bối cảnh chính phủ và doanh nghiệp, hãy gắn mỗi bậc với ai sở hữu ngưỡng hoàn tác và ai ký duyệt bất kỳ bước chuyển nào từ phát hành có cổng sang tự động hóa hoàn toàn, để quyết định có chủ đích thay vì trôi.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy dựa vào CI/CD được quản lý từ ngày đầu: một runner lưu trữ, một đường ống, một ảnh bất biến, và tự động triển khai lên staging khi hợp nhất. Đừng xây hạ tầng đường ống rồi phải bảo trì nó. Cờ tính năng cho hai ba kỹ sư hợp nhất công việc dở dang an toàn và phát hành nhiều lần một ngày, và một lần triển khai môi trường sản xuất bằng một cú nhấp cộng tắt cờ nhanh là toàn bộ kiểm soát thay đổi bạn cần cho đến khi quy mô buộc thêm.

**Doanh nghiệp nhỏ.** Không có kỹ sư nền tảng hay phát hành riêng, hãy ưu tiên đường ống mà nơi lưu mã nguồn của bạn cung cấp (Actions dựng sẵn hoặc tương đương) và chiến lược triển khai mặc định của nó hơn bất cứ thứ gì tùy chỉnh. Hãy đóng khung lựa chọn mua-so-với-xây một cách trung thực: một đường ống được quản lý và nền tảng lưu trữ có hoàn tác dựng sẵn tốn ít hơn giờ kỹ sư mà một thiết lập đặt riêng ngốn. Giữ những điều cốt yếu, là dựng một lần, thăng cấp cùng hiện vật, và hoàn nguyên dễ dàng, và bỏ qua bộ máy phân phối tăng dần cho đến khi khối lượng biện minh.

**Doanh nghiệp lớn.** Vấn đề cốt lõi là nhất quán qua nhiều đội: hãy chuẩn hóa một mẫu đường ống dùng chung thực thi rà soát, quét, hiện vật bất biến đã ký, và chiến lược triển khai theo bậc, để chất lượng không thay đổi theo từng đội. Coi định nghĩa đường ống là mã được rà soát, nắm bắt bằng chứng kiểm soát thay đổi tự động, và quản lý cờ tính năng cùng ngưỡng hoàn tác như tài sản được quản trị thay vì thói quen riêng của mỗi đội. Lợi ích là phân phối nhanh hơn và bằng chứng kiểm toán được tạo ra như sản phẩm phụ thay vì cuộc chạy vạy hằng quý.

**Chính phủ.** Quy tắc mua sắm, cửa sổ thay đổi theo luật và trách nhiệm giải trình công định hình đường ống. Hãy ưu tiên phân phối liên tục với cổng phát hành con người có tài liệu hơn tự động hóa hoàn toàn cho hệ thống hệ quả, phân loại công việc thường lệ là thay đổi chuẩn được phê duyệt trước, và giữ đường hoàn tác tức thì (xanh-lam hoặc canary tự động) cho dịch vụ mà công dân phụ thuộc trong các cửa sổ hằng năm hẹp. Bảo đảm đường ống ghi lại ai đã phê duyệt mỗi thay đổi, kiểm thử nào đã chạy, và hiện vật nào đã triển khai, để nghĩa vụ minh bạch và kiểm toán được đáp ứng bởi quy trình bình thường thay vì giấy tờ thủ công.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp SaaS bốn người dựng một đường ống GitHub Actions duy nhất chạy kiểm thử đơn vị, dựng một ảnh Docker, và triển khai cùng ảnh đó lên staging tự động ở mỗi lần hợp nhất vào main. Triển khai môi trường sản xuất là một cú nhấp, và những người sáng lập dựa vào cờ tính năng để hợp nhất công việc dở dang sau một cờ thay vì giữ một nhánh sống hàng tuần. Khi một bản phát hành tồi lọt qua, họ tắt cờ trong vài giây và sửa bình tĩnh, giữ đội nhỏ xíu của họ phát hành nhiều lần một ngày mà không cần người vận hành riêng.

**Doanh nghiệp lớn.** Một ngân hàng toàn cầu hợp nhất hàng chục công việc Jenkins riêng cho từng đội thành một mẫu đường ống chuẩn hóa mà mọi đội sản phẩm thừa hưởng. Mẫu thực thi phân tích tĩnh, quét phụ thuộc, và một hiện vật bất biến đã ký, và nó triển khai qua canary với hoàn tác tự động gắn với ngưỡng tỷ lệ lỗi và độ trễ. Vì cùng hiện vật được thăng cấp từ kiểm thử lên môi trường sản xuất và mọi cổng đều được ghi nhật ký, kiểm toán viên của ngân hàng truy vết bất kỳ tệp nhị phân sản xuất nào về commit, rà soát và phê duyệt của nó trong vài giây, thay một bài tập thu thập bằng chứng thủ công hằng quý.

**Chính phủ.** Một cơ quan thuế quốc gia hiện đại hóa hệ thống khai thuế áp dụng phân phối liên tục với một cổng phát hành con người tường minh, để tôn trọng cửa sổ thay đổi theo luật trong mùa khai thuế. Thay đổi thường lệ được phân loại là thay đổi chuẩn được phê duyệt trước chảy tự động lên staging. Phát hành lên môi trường sản xuất đòi một phê duyệt có tài liệu duy nhất mà đường ống ghi lại. Triển khai xanh-lam cho cơ quan một đường hoàn tác tức thì nếu một lỗi đến môi trường sản xuất, điều trọng yếu khi hàng triệu công dân phụ thuộc dịch vụ trong một cửa sổ hằng năm hẹp.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức đầu tư CI/CD hiện ra là thời gian chờ cho thay đổi giảm, tỷ lệ thay đổi thất bại thấp hơn, và phục hồi nhanh hơn khi có sự cố: các chỉ số mà nghiên cứu liên tục gắn với cả hiệu suất phân phối lẫn kết quả tổ chức. Bản phát hành nhỏ hơn, nhanh hơn cắt chi phí phối hợp ngốn năng lực kỹ thuật ở quy mô, và xác minh tự động cắt công việc tốn kém, làm nản chí của chữa cháy lỗi sản xuất.

Tổng chi phí sở hữu cân nhắc chi phí áp dụng so với chi phí của việc không áp dụng. Chi phí áp dụng gồm xây dựng và bảo trì đường ống, mở rộng độ phủ kiểm thử, và đầu tư vào khả năng quan sát và nhân sự nền tảng. Chi phí của việc không áp dụng lớn hơn nhưng ít hiển thị hơn: phát hành thủ công chậm, đau đớn tích hợp, sự cố sản xuất gây hại danh tiếng, và, trong bối cảnh chịu quy định, kiểm toán thất bại và khắc phục. Với ban lãnh đạo, lập luận được đóng khung tốt nhất theo giảm rủi ro và năng lực. Tự động hóa chuyển thời gian kỹ sư cấp cao khan hiếm từ lao động phát hành lặp lại sang công việc sản phẩm, trong khi làm sự cố hiếm hơn và ngắn hơn.

## Phản mẫu và cạm bẫy

- **Đường ống bông tuyết.** Mỗi đội tự xây một đường ống độc nhất, nên cải tiến và bản sửa không chia sẻ được và chất lượng thay đổi mạnh.
- **Dựng lại theo môi trường.** Dựng lại cho mỗi giai đoạn phá vỡ bảo đảm "dựng một lần" và để khác biệt tinh vi đến môi trường sản xuất.
- **Bản dựng đỏ bị phớt lờ.** Chấp nhận một nhánh chính hỏng dai dẳng phá hủy lòng tin vào đường ống và bình thường hóa việc phát hành chồng lên thất bại.
- **Kiểm thử chập chờn không được xử lý.** Thất bại ngắt quãng dạy lập trình viên chạy lại cho đến khi xanh, làm mất mục đích của cổng.
- **Sân khấu phê duyệt thủ công.** Một hội đồng tư vấn thay đổi đóng dấu mọi thứ thêm chậm trễ mà không thêm an toàn.
- **Nợ cờ.** Cờ tính năng không bao giờ bị gỡ tích tụ thành độ phức tạp có điều kiện không bảo trì nổi.
- **Triển khai bằng phát hành.** Ghép hai thứ nghĩa là mỗi thay đổi hướng người dùng đòi một lần triển khai lại rủi ro.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Bản dựng và triển khai phần lớn thủ công, tùy nghi và phản ứng. Tích hợp xảy ra muộn, phát hành hiếm và căng thẳng, hoàn tác nghĩa là triển khai lại phiên bản cũ bằng tay, và không có khái niệm chung về cổng đường ống.

**Mức 2: Phát triển.** Bản dựng tự động và kiểm thử đơn vị chạy ở mỗi commit, nhưng thực hành khác nhau theo từng đội. Triển khai được viết thành tập lệnh nhưng vẫn được kích hoạt và giám sát thủ công, một số môi trường nhất quán, và hiện vật có thể vẫn được dựng lại mỗi giai đoạn. Nơi có đường ống, nó thường là bông tuyết không chia sẻ được.

**Mức 3: Chuẩn hóa.** Một mẫu đường ống chuẩn hóa, có tài liệu được thực thi qua các đội. Nó thăng cấp một hiện vật bất biến duy nhất qua mọi môi trường, áp dụng cổng chất lượng và bảo mật tự động, mã hóa các kiểm tra bắt buộc như phê duyệt rà soát và kết quả quét, và nắm bắt hồ sơ thay đổi tự động. Chiến lược triển khai như canary hay xanh-lam được chọn có chủ đích theo từng bậc dịch vụ.

**Mức 4: Quản lý.** Phân phối được đo và kiểm soát theo đường cơ sở. Tổ chức theo dõi thời gian chờ cho thay đổi, tần suất triển khai, tỷ lệ thay đổi thất bại và thời gian phục hồi trung bình, cùng thời lượng đường ống p50 và p95, tỷ lệ kiểm thử chập chờn và chạy lại, và tuổi cờ tính năng. Ngưỡng hoàn tác được đặt từ dữ liệu tỷ lệ lỗi, độ trễ và độ bão hòa quan sát được, cổng được thực thi dựa trên bằng chứng thay vì thói quen, và mỗi chỉ số có chủ sở hữu hành động khi nó lệch mục tiêu.

**Mức 5: Điều phối.** Phân phối cải thiện liên tục và được tích hợp trong toàn tổ chức. Phân phối tăng dần với hoàn tác tự động dựa trên chỉ số là chuẩn mực, phát hành được tách khỏi triển khai qua cờ được quản trị tốt, và bằng chứng tuân thủ được tạo tự động như sản phẩm phụ. Đường ống thích ứng khi hệ sinh thái thay đổi, và chỉ số phân phối nuôi hoạch định kinh doanh và rủi ro để đầu tư chảy đến các cải tiến đòn bẩy cao nhất.

## Ý tưởng để thảo luận

- Ranh giới đúng giữa phân phối liên tục với cổng con người và triển khai liên tục hoàn toàn cho các hệ thống trọng yếu nhất của bạn nằm ở đâu?
- Làm sao bạn giữ một quy trình quản lý thay đổi bắt buộc có ý nghĩa mà không biến nó thành sân khấu đóng dấu?
- Chỉ số sức khỏe khách quan nào nên chi phối hoàn tác tự động, và ai sở hữu ngưỡng của chúng?
- Các đội nền tảng nên cân bằng mẫu đường ống chuẩn hóa với nhu cầu chính đáng của các đội có yêu cầu bất thường thế nào?
- Chính sách và công cụ của bạn để nghỉ hưu cờ tính năng trước khi chúng thành nợ là gì?
- Làm sao bạn đo liệu phân phối nhanh hơn thực sự cải thiện kết quả kinh doanh hay chỉ phát hành nhiều hơn?

## Những điểm cần ghi nhớ

- CI, CD và triển khai liên tục là riêng biệt; hãy chọn mức tự động hóa khớp với khả năng chịu rủi ro và độ trưởng thành của bạn.
- Dựng hiện vật một lần và thăng cấp đúng hiện vật đó qua mọi môi trường.
- Thiết kế đường ống như các cổng chất lượng có thứ tự tối ưu cho phản hồi nhanh, và coi nó là quyết định phát hành có thẩm quyền.
- Chọn chiến lược triển khai có chủ đích, và áp dụng phân phối tăng dần với hoàn tác tự động để giới hạn bán kính ảnh hưởng.
- Tách phát hành khỏi triển khai bằng cờ tính năng, và quản lý nợ cờ.
- Trong môi trường chịu quy định, nắm bắt bằng chứng kiểm soát thay đổi tự động thay vì qua giấy tờ thủ công.

## Tài liệu tham khảo và đọc thêm

- Jez Humble và David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois và John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr và George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (tiểu luận).
- ITIL (Information Technology Infrastructure Library), hướng dẫn quản lý thay đổi.
