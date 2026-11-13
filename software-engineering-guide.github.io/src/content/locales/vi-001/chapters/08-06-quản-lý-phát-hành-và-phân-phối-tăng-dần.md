# 8.6 Quản lý phát hành và phân phối tăng dần

## Tổng quan và động lực

Ý tưởng hữu ích nhất trong quản lý phát hành hiện đại cũng là ý tưởng đơn giản nhất: phát hành mã và phơi bày một tính năng là hai sự kiện khác nhau, và bạn nên làm được cái này mà không cần cái kia. Chương 8.1 (CI/CD và phân phối) đưa thay đổi của bạn được dựng một lần, kiểm thử và thăng cấp như một hiện vật bất biến. Chương này nói về điều xảy ra tiếp theo: bạn biến mã đã triển khai đó thành trải nghiệm trực tiếp cho người dùng thật thế nào, dần dần, an toàn, và với một đường quay lui nhanh. **Triển khai** nghĩa là cài mã lên máy chủ. **Phát hành** nghĩa là cho người dùng tiếp cận một năng lực. Khi bạn tách chúng, một lần triển khai trở nên thường lệ và nhàm chán, và một lần phát hành trở thành một quyết định được kiểm soát, đảo ngược được.

Với các đội lớn, sự tách biệt này đổi nhiệt độ cảm xúc của việc phát hành. Khi hàng chục dịch vụ và hàng trăm kỹ sư thay đổi môi trường sản xuất mỗi ngày, mô hình ghép "triển khai bằng phát hành" nghĩa là mọi thay đổi hướng người dùng là một sự kiện rủi ro, tất-cả-cùng-lúc. Tách rời cho phép bạn hợp nhất công việc dở dang sau một công tắc, tung một tính năng cho một phần trăm lưu lượng, theo dõi con số, và mở rộng hoặc rút lui mà không chạm vào bản dựng. **Phân phối tăng dần** là thuật ngữ bao trùm cho điều này: phát hành một thay đổi cho khán giả ngày càng rộng trong khi các kiểm tra tự động quyết định có tiếp tục không.

Bối cảnh doanh nghiệp và chính phủ thêm phối hợp và bằng chứng. Một nền tảng thanh toán phát hành qua nhiều dịch vụ phải thống nhất về lược đồ. Một cơ quan công hoạt động dưới thẩm quyền vận hành và kiểm soát thay đổi chính thức, và kiểm toán viên muốn bằng chứng chính xác ai đã được phơi bày với cái gì, và khi nào. Làm tốt, phân phối tăng dần thỏa mãn cả mong muốn đi nhanh lẫn nghĩa vụ chứng minh kiểm soát, vì cùng cơ chế giới hạn bán kính ảnh hưởng cũng tạo ra bản ghi kiểm toán được về việc tung ra.

## Các nguyên tắc chính

- **Triển khai không phải phát hành.** Phát hành mã trong bóng tối, rồi bật nó có chủ đích.
- **Bán kính ảnh hưởng nhỏ trước.** Phơi bày một thay đổi cho vài người trước khi phơi bày cho tất cả.
- **Mỗi bản phát hành có số lùi.** Nếu bạn không hoàn tác được trong vài giây, bạn chưa thiết kế xong bản phát hành.
- **Để tín hiệu thúc đẩy thăng cấp.** Chỉ số sức khỏe và ngân sách lỗi, không phải lịch hay sự lạc quan, quyết định việc tung ra có tiến không.
- **Một cờ là khoản nợ cho đến khi bị gỡ.** Mỗi công tắc là mã bạn phải bảo trì và cuối cùng xóa.
- **Làm thay đổi cơ sở dữ liệu sống sót cả hai chiều.** Việc tung ra và hoàn tác đều phải an toàn với cùng một lược đồ.
- **Phê duyệt nên ghi lại, không cản trở.** Bằng chứng kiểm toán là sản phẩm phụ của đường ống, không phải cuộc họp hằng tuần.

## Khuyến nghị

### Tách triển khai khỏi phát hành bằng cờ tính năng

Một [công tắc tính năng](https://en.wikipedia.org/wiki/Feature_toggle), hay cờ tính năng, là công tắc thời gian chạy quyết định một đường mã có hoạt động không, mà không triển khai lại. Hãy coi cờ như một từ vựng có kiểu, vì tuổi thọ của chúng khác nhau. **Cờ phát hành** giấu công việc đang tiến hành và sống từ vài ngày đến vài tuần. **Cờ vận hành** (công tắc ngắt) cho phép bạn vô hiệu hóa một hệ thống con dưới tải và có thể sống vô thời hạn. **Cờ thử nghiệm** chia lưu lượng cho một bài kiểm thử có đối chứng và sống trong suốt thời gian thử nghiệm. **Cờ quyền** chặn một năng lực theo gói hay vai trò và thực chất là vĩnh viễn. Hãy cho mỗi cờ một chủ sở hữu, một kiểu, một mặc định, và một ngày dự kiến gỡ bỏ. Mặc định nên là mặc định an toàn, để một sự cố dịch vụ cờ thất bại đóng về hành vi tốt đã biết thay vì mở ra các đường chưa kiểm thử.

### Chọn mẫu phân phối tăng dần theo bậc dịch vụ

Hãy khớp cơ chế tung ra với bán kính ảnh hưởng, như chương 8.1 lập luận về chiến lược triển khai. Một [phát hành canary](https://en.wikipedia.org/wiki/Feature_toggle#Canary_release) định tuyến một lát lưu lượng nhỏ đến phiên bản mới và chỉ mở rộng nếu sức khỏe giữ vững. Một [triển khai xanh-lam](https://en.wikipedia.org/wiki/Blue-green_deployment) giữ hai môi trường sản xuất và chuyển lưu lượng giữa chúng để chuyển và đảo ngược tức thì. Một **triển khai cuốn chiếu** thay các thể hiện theo lô. Một **triển khai theo vòng** mở rộng qua các khán giả có tên: người dùng nội bộ trước, rồi nhóm beta, rồi một khu vực nhỏ, rồi mọi người. Vòng là cách đóng khung hữu ích nhất cho tổ chức lớn vì chúng gọi tên ai được phơi bày ở mỗi bước, chính xác điều cả kiểm toán viên lẫn người ứng phó sự cố muốn biết. Nền tảng container và điều phối (chương 8.3) cung cấp các nguyên thủy định hình lưu lượng làm các mẫu này rẻ để chạy.

### Chặn cổng việc tung ra bằng kiểm tra sức khỏe và hoàn tác tự động

Hãy xác định tiêu chí sức khỏe khách quan trước bản phát hành, không phải trong sự cố. Phân tích tự động so sánh canary với đường cơ sở về tỷ lệ lỗi, độ trễ và độ bão hòa, và hoặc thăng cấp hoặc hoàn nguyên mà không chờ con người nhận ra. Hãy gắn thăng cấp với [mục tiêu mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_objective) và ngân sách lỗi từ kỹ thuật độ tin cậy site (chương 9.1): khi ngân sách khỏe bạn phát hành tự do, và khi nó cạn đường ống từ chối tiến cho đến khi dịch vụ ổn định. Hoàn tác tự động quan trọng nhất vì nó loại bỏ sự do dự biến một hồi quy nhỏ thành ngừng hoạt động lớn. Đảo ngược nhanh cũng là kiểm soát sự cố rẻ nhất của bạn: một lần hoàn tác mất vài giây thu nhỏ bán kính ảnh hưởng trước khi quy trình sự cố của bạn (chương 9.3) kịp khởi động đầy đủ. Tỷ lệ thay đổi thất bại và thời gian phục hồi bạn cải thiện theo cách này chính là các tín hiệu luồng và ổn định mà đường ống phân phối của bạn theo dõi (chương 11.2).

### Dùng phát hành trong bóng tối và lưu lượng bóng để giảm rủi ro

Một số thay đổi quá hệ quả để lần đầu gặp người dùng thật ở mức phơi bày đầy đủ. **Phát hành trong bóng tối** phát hành một tính năng ở trạng thái tắt, rồi thử nó nội bộ hoặc trên một phần môi trường sản xuất trước khi ai thấy. **Lưu lượng bóng** sao chép các yêu cầu trực tiếp đến đường mã mới và bỏ các phản hồi, để bạn đo tải thật và tính đúng với tác động người dùng bằng không. Những kỹ thuật này cho phép bạn xác thực một lần viết lại hay phụ thuộc mới dưới lưu lượng đích thực, điều không môi trường staging nào tái tạo trung thực. Hãy ghép chúng với cùng phân tích sức khỏe bạn dùng cho canary.

### Chạy thử nghiệm có đối chứng qua cùng hệ thống cờ

Cờ thử nghiệm là nơi kỹ thuật phát hành gặp việc học của sản phẩm. Một phép chia [kiểm thử A/B](https://en.wikipedia.org/wiki/A/B_testing) phục vụ các biến thể cho các nhóm so sánh được và đo một kết quả đã chọn, nuôi thực hành phân tích sản phẩm của chương 7.4. Hãy tái sử dụng một hệ thống cờ và nhắm mục tiêu cho cả tung ra an toàn lẫn thử nghiệm, để bạn có một dấu vết kiểm toán và một công tắc ngắt thay vì hai ngăn xếp công tắc song song bất đồng về ai ở nhóm nào.

### Giữ cơ sở dữ liệu tương thích ngược với mở rộng và thu hẹp

Việc tung ra và hoàn tác chỉ an toàn nếu lược đồ chịu được cả mã cũ lẫn mới cùng lúc, điều không tránh khỏi trong bất kỳ lần tung ra dần dần nào. Hãy dùng mẫu **mở rộng và thu hẹp** (thay đổi song song): trước hết *mở rộng* bằng cách thêm cột hoặc bảng mới trong một di chuyển tương thích ngược, rồi triển khai mã ghi vào cả hình dạng cũ lẫn mới, rồi điền bù, rồi chuyển các lần đọc sang, và chỉ rất muộn sau đó mới *thu hẹp* bằng cách bỏ hình dạng cũ khi không mã nào đang chạy phụ thuộc vào nó. Đừng bao giờ kết hợp một di chuyển phá hủy với lần triển khai cần nó. Kỷ luật này là thứ cho phép bạn hoàn tác mã mà không có cơ sở dữ liệu đã đi tiếp, và nó nối trực tiếp với chiến lược kiểm thử của bạn (chương 2.4), vốn phải bao quát cửa sổ phiên bản hỗn hợp.

### Làm quản lý thay đổi ghi lại thay vì cản trở

Hãy dung hòa kiểm toán với luồng bằng cách phê duyệt trước các lớp thay đổi. Xác định các loại thay đổi chuẩn, rủi ro thấp chảy qua đường ống tự động, nắm bắt ai đã phê duyệt, kiểm thử nào đã chạy, hiện vật nào đã triển khai, và khán giả nào đã được phơi bày ở mỗi vòng. Dành rà soát tư vấn thay đổi của con người cho các thay đổi thực sự rủi ro cao. Một hội đồng [kiểm soát thay đổi](https://en.wikipedia.org/wiki/Change_control) truyền thống kiểm tra mọi lần triển khai thường lệ trở thành nút thắt đẩy các đội về lô lớn hơn, rủi ro hơn, ngược với điều nó định làm. Trong chính phủ, thẩm quyền vận hành và kiểm soát thay đổi chính thức có thể cùng tồn tại với phân phối tăng dần khi công cụ tung ra phát ra bằng chứng mà khung kiểm soát yêu cầu, nên bản ghi theo vòng là hiện vật kiểm toán.

## Đánh đổi: ưu và nhược điểm

| Mẫu | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Canary | Dựa trên dữ liệu, bán kính ảnh hưởng nhỏ | Cần chỉ số tốt và khối lượng lưu lượng | Dịch vụ hướng người dùng lớn |
| Xanh-lam | Chuyển và hoàn tác tức thì | Nhân đôi chi phí môi trường lúc chuyển | Dịch vụ trọng yếu cần hoàn nguyên nhanh |
| Cuốn chiếu | Rẻ, đơn giản, không môi trường thêm | Hoàn tác chậm, phiên bản hỗn hợp chạy | Dịch vụ nội bộ không trạng thái |
| Theo vòng | Khán giả có tên, dấu vết kiểm toán rõ | Tung ra đầy đủ chậm hơn; phối hợp nhiều hơn | Hệ sinh thái chịu quy định và đa dịch vụ |
| Cờ tính năng | Tách triển khai khỏi phát hành; công tắc ngắt tức thì | Nợ cờ; ma trận kiểm thử phình | Đội phát hành an toàn công việc chưa hoàn tất |
| Chuyến tàu phát hành | Nhịp khả đoán, phối hợp dễ | Ghép nhiều thay đổi; chờ chuyến tàu | Nhiều đội chia sẻ một bản phát hành |
| Phát hành theo yêu cầu | Lô nhỏ, phản hồi nhanh | Phối hợp xuyên đội khó hơn | Đội phân phối liên tục tin cậy cao |

Căng thẳng trung tâm là giữa phối hợp và độc lập. **Chuyến tàu phát hành** gom thay đổi của nhiều đội vào một lịch cố định, dễ suy luận nhưng buộc một thay đổi đã xong phải chờ và ghép công việc không liên quan vào một sự kiện. **Phát hành theo yêu cầu** để mỗi đội phát hành khi sẵn sàng, nhanh hơn nhưng đòi dịch vụ giữ triển khai độc lập và tương thích ngược. Cách giải quyết thường là tách ở cấp hiện vật và lược đồ để các đội *có thể* phát hành theo yêu cầu, rồi dùng cờ và vòng để phối hợp khoảnh khắc *hiển thị cho người dùng* khi một tính năng xuyên dịch vụ thực sự bật. Như vậy bản phát hành kỹ thuật và lần ra mắt sản phẩm là hai quyết định riêng, và không cái nào chặn cái kia.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi một bản phát hành hỏng lúc 2 giờ sáng, mất bao nhiêu giây để đảo ngược, và ai hay cái gì bóp cò?** Câu trả lời trung thực tiết lộ liệu bạn đã thực sự tách triển khai khỏi phát hành hay chỉ thêm cờ lên một quy trình ghép. Một lần hoàn tác đòi dựng lại, một di chuyển cơ sở dữ liệu để hoàn tác, hoặc một người bị gọi để quyết định không phải là hoàn tác, mà là sự cố thứ hai. Hãy mang cơ chế thực cho ba dịch vụ hàng đầu của bạn: cờ hoặc dịch chuyển lưu lượng đảo ngược phơi bày, tín hiệu sức khỏe kích hoạt nó tự động, và bảo đảm lược đồ làm việc đảo ngược an toàn. Với một hệ sinh thái lớn điều này quyết định bán kính ảnh hưởng thực của bạn, vì đảo ngược tự động nhanh là thứ giữ một hồi quy khỏi thành ngừng hoạt động. Nếu câu trả lời đo bằng cuộc họp thay vì giây, đó là việc đầu tiên cần sửa.

2. **Chính sách của bạn để cho nghỉ hưu cờ là gì, và bạn đang mang bao nhiêu nợ cờ ngay bây giờ?** Mỗi cờ tính năng là một ngã rẽ trong mã nhân số trạng thái bạn phải suy luận và kiểm thử, và một cờ sống lâu hơn mục đích của nó là khoản nợ thuần túy. Hãy quyết định quy tắc ngay bây giờ: mỗi cờ phát hành có chủ sở hữu và ngày hết hạn, cờ cũ nổi lên trên bảng điều khiển, và gỡ chúng là công việc có kế hoạch thay vì dọn dẹp một ngày nào đó. Hãy mang số cờ đang sống, tuổi của chúng, và bao nhiêu cái quá ngày gỡ dự kiến. Trong một cơ sở mã lớn, cờ không kiểm soát trở thành độ phức tạp có điều kiện vĩnh viễn mà không ai dám xóa, và cơ chế an toàn biến thành nguồn lỗi. Mức chịu đựng của đội với con số đó thực ra là một phát biểu về việc nó coi trọng vệ sinh vận hành đến đâu.

3. **Quy trình phê duyệt thay đổi của bạn làm bản phát hành an toàn hơn, hay chỉ chậm hơn?** Nhiều tổ chức chạy một hội đồng tư vấn thay đổi rà soát mọi lần triển khai, và câu hỏi khó chịu là liệu nó đã từng thực sự chặn một thay đổi tồi hay chỉ thêm độ trễ. Hãy mang dữ liệu: độ trễ phê duyệt trung vị, tỷ lệ thay đổi thất bại cho thay đổi do hội đồng rà soát so với được phê duyệt trước, và rà soát gom thay đổi nhỏ thành lớn hơn, rủi ro hơn bao lâu một lần. Mục tiêu là dành rà soát con người cho thay đổi thực sự rủi ro cao trong khi để thay đổi chuẩn chảy qua đường ống với nắm bắt bằng chứng tự động. Với bối cảnh chịu quy định và chính phủ, hãy xác minh công cụ tung ra tạo bản ghi kiểm toán mà khung kiểm soát cần, để kiểm soát thành sản phẩm phụ của việc phát hành thay vì cổng đứng trước nó. Nếu rà soát thêm trễ mà không giảm thất bại, nó là sân khấu mặc áo tuân thủ.

4. **Tín hiệu sức khỏe khách quan nào bạn sẵn lòng để máy hành động, và mọi dịch vụ bậc cao nhất có thực sự có chỉ số đủ tốt để chặn cổng không?** Phân tích canary tự động và chặn cổng ngân sách lỗi chỉ hoạt động nếu tỷ lệ lỗi, độ trễ và độ bão hòa được đo đủ sạch để tin một thăng cấp hay hoàn tác mà không cần con người trong vòng lặp, và nhiều đội phát hiện giữa sự cố rằng tín hiệu của họ quá nhiễu hoặc quá thưa để quyết định. Với một hệ sinh thái lớn điều này quyết định bao nhiêu khối lượng phát hành của bạn chảy an toàn mà không cần trông nom thủ công, là sự khác biệt giữa nền tảng mở rộng được và nền tảng cần một người theo dõi mọi lần tung ra. Hãy mang bảng điều khiển thực cho ba dịch vụ trọng yếu nhất: chỉ số bạn chặn cổng theo, khối lượng lưu lượng làm canary có ý nghĩa thống kê, và tỷ lệ dương tính giả của phân tích tự động. Trong bối cảnh chịu quy định và chính phủ, cùng tín hiệu nuôi bản ghi kiểm toán được, nên khả năng quan sát kém vừa là khoảng trống độ tin cậy vừa là khoảng trống tuân thủ, và tài trợ chất lượng chỉ số nên là một dòng có tên trong kế hoạch thay vì năng lực được giả định.

5. **Thay đổi lược đồ của bạn có thực sự sống sót qua hoàn tác không, và bạn chứng minh cửa sổ phiên bản hỗn hợp an toàn thế nào trước khi phát hành?** Phân phối tăng dần hứa một số lùi nhanh, nhưng một di chuyển phá hủy ghép với một tính năng lặng lẽ vô hiệu lời hứa đó, vì hoàn tác mã để nó trỏ vào một cơ sở dữ liệu đã đi tiếp. Với một tổ chức lớn nơi nhiều dịch vụ chia sẻ một lược đồ, rủi ro cộng dồn: bước thu hẹp của một đội có thể làm kẹt hoàn tác của đội khác, nên kỷ luật mở rộng và thu hẹp phải là tiêu chuẩn chung chứ không phải thói quen cục bộ. Hãy mang sổ tay di chuyển của bạn và bằng chứng nó được theo: bạn tách mở rộng khỏi thu hẹp thế nào, ghi kép và điền bù có được kiểm thử dưới tải không, và bộ kiểm thử của bạn thực hành mã cũ với lược đồ mới và mã mới với lược đồ cũ thế nào. Với các hệ sinh thái doanh nghiệp và chính phủ mang dữ liệu sống lâu và kiểm soát thay đổi chính thức, một di chuyển không đảo ngược được không chỉ là rủi ro ngừng hoạt động, mà là phơi nhiễm toàn vẹn dữ liệu và kiểm toán mà một cửa sổ bảo trì lên lịch sẽ không cứu được.

6. **Khi một tính năng xuyên dịch vụ trải qua các đội phát hành ở tốc độ khác nhau, ai sở hữu khoảnh khắc nó bật, và bạn phối hợp thế nào mà không ghép các lần triển khai của họ?** Toàn bộ ý nghĩa của việc tách triển khai khỏi phát hành là mỗi đội có thể phát hành hiện vật của mình độc lập trong khi một cờ duy nhất kiểm soát lần ra mắt hiển thị cho người dùng, nhưng điều đó chỉ đúng nếu ai đó sở hữu quyết định ra mắt và việc nhắm mục tiêu cờ qua ranh giới dịch vụ. Với một đội lớn kiểu thất bại là một chuyến tàu phát hành de facto không ai chọn: một dịch vụ chậm buộc mọi đội khác chờ, hoặc một lần lật cờ không phối hợp phơi bày một tính năng nối dở. Hãy mang bản đồ phụ thuộc cho lần ra mắt đa dịch vụ kế tiếp, chủ sở hữu cờ ra mắt, và các bảo đảm tương thích ngược cho phép mỗi dịch vụ triển khai theo đồng hồ riêng. Trong các chương trình doanh nghiệp và chính phủ có phê duyệt ra mắt chính thức, hãy nêu ai ký duyệt lần bật xuyên dịch vụ và họ thấy bằng chứng gì, để lần ra mắt phối hợp là quyết định có chủ đích, được ghi lại thay vì tai nạn của người hợp nhất sau cùng.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tách triển khai khỏi phát hành đáng làm ngay cả với ba kỹ sư, nhưng giữ nó rẻ. Hãy bọc công việc mới trong cờ phát hành mặc định tắt, phát hành lên thân cây, và bật tính năng cho chính bạn trước khách hàng, để một thay đổi chưa xong không bao giờ chặn một lần triển khai. Bỏ qua nền tảng phân tích canary nặng bạn không bố trí nhân sự nổi: một dịch vụ cờ lưu trữ và công tắc ngắt cứng mua phần lớn sự an toàn, và một người sở hữu nghi thức dọn cờ hằng tuần giữ nợ khỏi nuốt tốc độ của bạn.

**Doanh nghiệp nhỏ.** Không có kỹ sư phát hành và ngân sách eo hẹp, hãy dựa vào bất cứ phân phối tăng dần nào nền tảng hiện có của bạn đã cho, thay vì xây hệ thống tung ra. Lưu trữ được quản lý, một SaaS cờ tính năng, hay tung ra theo giai đoạn dựng sẵn của khung phát triển thường bao quát bán kính ảnh hưởng nhỏ bạn cần. Coi số lùi là thứ bạn phải làm đúng: một thay đổi bạn tắt được trong vài giây quan trọng hơn nhiều so với phân tích tự động tinh vi bạn không có thời gian điều chỉnh.

**Doanh nghiệp lớn.** Vấn đề là nhất quán qua nhiều đội và dịch vụ: một từ vựng cờ dùng chung với chủ sở hữu, kiểu và hết hạn, tung ra theo vòng chuẩn, và chặn cổng ngân sách lỗi áp dụng giống nhau ở mọi nơi để các nhóm thôi phát minh ngăn xếp công tắc đối thủ. Hãy quản trị nợ cờ như chỉ số toàn hệ sinh thái, chuẩn hóa di chuyển mở rộng và thu hẹp để thay đổi lược đồ của một đội không bao giờ làm kẹt hoàn tác của đội khác, và biến bản ghi tung ra kiểm toán được thành sản phẩm phụ mà mọi dịch vụ phát ra cùng hình dạng. Phê duyệt trước thay đổi chuẩn và dành rà soát con người cho cái thực sự rủi ro cao, để kiểm soát mở rộng mà không có hội đồng trên đường trọng yếu.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi bản phát hành. Hãy biến công cụ tung ra thành nguồn bằng chứng kiểm toán, để mỗi lần mở rộng vòng ghi lại thẩm quyền phê duyệt, kiểm thử đã chạy, băm hiện vật, và chính xác quần thể được phơi bày, và thẩm quyền vận hành cùng tồn tại với phân phối tăng dần thay vì chống lại nó. Ưu tiên mẫu xanh-lam hoặc theo vòng có khán giả có tên mà kiểm toán viên và người ứng phó sự cố đều đọc được, xác thực thay đổi hệ quả bằng lưu lượng bóng trên ca thực trước khi bất kỳ công dân nào bị ảnh hưởng, và giữ bản ghi kiểm toán được làm hiện vật mà khung kiểm soát chấp nhận thay cho một cửa sổ big-bang lên lịch.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty SaaS mười người phát hành lên thân cây nhiều lần một ngày và bọc mọi năng lực mới trong cờ phát hành mặc định tắt. Một tích hợp thanh toán mới rủi ro ra mắt trong bóng tối: họ chạy lưu lượng bóng trên nó trong một tuần, xem nó xử lý hình dạng yêu cầu thật mà không tác động khách hàng, rồi tung ra từng vòng, bắt đầu từ tài khoản của chính họ và một nhúm khách hàng beta thân thiện. Khi tỷ lệ lỗi vọt ở vòng năm phần trăm, một kiểm tra tự động lật cờ tắt trong vài giây, và họ gỡ lỗi bình tĩnh vào thứ Hai. Một kỹ sư sở hữu nghi thức dọn cờ hằng tuần để công tắc không bao giờ chất đống.

**Doanh nghiệp lớn.** Một công ty thanh toán toàn cầu phối hợp một thay đổi trải qua sáu dịch vụ và một lược đồ dùng chung. Mỗi đội triển khai hiện vật của mình độc lập và tương thích ngược bằng mở rộng và thu hẹp, nên các cột mới tồn tại và được ghi kép từ lâu trước khi bất kỳ người dùng nào thấy tính năng. Lần ra mắt hiển thị cho người dùng là một cờ thử nghiệm duy nhất, tung qua các vòng gắn với sức khỏe ngân sách lỗi: nội bộ, rồi một quốc gia nhỏ, rồi tỷ lệ phần trăm mở rộng, với phân tích canary tự động thăng cấp hoặc hoàn nguyên ở mỗi bước. Một dịch vụ quản trị cờ thực thi chủ sở hữu, kiểu và hết hạn qua hệ sinh thái, và thay đổi chuẩn được phê duyệt trước chảy mà không có hội đồng trong khi chỉ bước thu hẹp lược đồ nhận rà soát con người. Mọi chuyển vòng được ghi nhật ký, nên dấu vết kiểm toán tự viết.

**Chính phủ.** Một cơ quan trợ cấp quốc gia hoạt động dưới thẩm quyền vận hành và kiểm soát thay đổi chính thức. Thay vì coi phân phối tăng dần là rủi ro tuân thủ, nó biến công cụ tung ra thành nguồn bằng chứng kiểm toán: mỗi lần mở rộng vòng ghi lại thẩm quyền phê duyệt, kiểm thử đã chạy, băm hiện vật, và chính xác quần thể được phơi bày. Một phép tính đủ điều kiện mới ra mắt trong bóng tối và được xác thực bằng lưu lượng bóng trên ca thực, rồi tung ra từng khu vực sau một cờ với chuyển xanh-lam để đảo ngược tức thì. Thay đổi chuẩn được phân loại trước để công việc thường lệ không xếp hàng sau hội đồng, trong khi thay đổi chính sách rủi ro cao vẫn nhận rà soát chính thức. Bản ghi tung ra kiểm toán được thỏa mãn khung kiểm soát đầy đủ hơn bản phát hành big-bang hằng quý trước đây từng làm.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của phân phối tăng dần bị chi phối bởi sự cố tránh được và mức độ nghiêm trọng thu nhỏ của chúng. Một thay đổi đến một phần trăm người dùng và tự hoàn nguyên tốn một sai số làm tròn, trong khi cùng lỗi ở mức phơi bày đầy đủ có thể nghĩa là hàng giờ ngừng hoạt động, ứng phó khẩn cấp và thiệt hại danh tiếng. Tách triển khai khỏi phát hành cũng biến chính bản phát hành từ sự kiện lên lịch, căng thẳng thành sự kiện thường lệ, giảm thuế phối hợp lớn lên phi tuyến với kích thước đội. Tách quyết định ra mắt khỏi triển khai cho sản phẩm và kỹ thuật di chuyển theo đồng hồ riêng, nên một ngày tiếp thị không bao giờ buộc một lần đóng băng mã rủi ro.

Tổng chi phí sở hữu là thật nhưng khiêm tốn so với lợi ích đó. Bạn đầu tư vào nền tảng cờ, công cụ phân tích canary, chỉ số sức khỏe đủ tốt để chặn cổng, và kỷ luật thay đổi lược đồ tương thích ngược. Chi phí lặp lại là vệ sinh cờ và ma trận kiểm thử lớn hơn mà cờ tạo ra, đó là lý do hệ sinh thái cờ không được quản lý là cách chính để thực hành này thành đắt. Chi phí của việc không áp dụng được trả bằng bán kính ảnh hưởng: mỗi bản phát hành là tất-cả-hoặc-không, hoàn tác chậm, và một lần triển khai tồi duy nhất có thể làm sập mọi người cùng lúc. Với các tổ chức chịu quy định, cổ tức tuân thủ mang tính quyết định, vì cùng cơ chế giới hạn phơi bày cũng tạo ra bằng chứng kiểm toán được mà nếu không sẽ phải lắp ráp bằng tay.

## Phản mẫu và cạm bẫy

- **Triển khai bằng phát hành.** Ghép hai thứ làm mỗi thay đổi hướng người dùng thành sự kiện rủi ro, tất-cả-cùng-lúc không có số lùi.
- **Nợ cờ.** Công tắc sống lâu hơn mục đích thành độ phức tạp có điều kiện vĩnh viễn không ai dám xóa.
- **Cờ thất bại mở.** Một sự cố dịch vụ cờ mặc định về đường mới, chưa kiểm thử biến trục trặc nhỏ thành ngừng hoạt động.
- **Hoàn tác cần hoàn tác lược đồ.** Một di chuyển phá hủy phát hành cùng tính năng của nó khiến bạn không hoàn nguyên mã an toàn được.
- **Thăng cấp thủ công theo cảm tính.** Tiến một lần tung ra vì nó "trông ổn" thay vì theo tiêu chí sức khỏe và ngân sách lỗi xác định.
- **Tung ra không có kế hoạch hoàn tác.** Thiết kế cách bật một tính năng mà không thiết kế cách tắt nó.
- **Hội đồng thay đổi đóng dấu.** Một rà soát không bao giờ từ chối gì thêm chậm trễ mà không thêm an toàn và đẩy các đội về lô lớn.
- **Cờ thử nghiệm và an toàn ở hệ thống riêng.** Hai ngăn xếp công tắc bất đồng về ai ở nhóm nào, nhân đôi bề mặt kiểm toán.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Triển khai và phát hành là cùng một sự kiện. Thay đổi đi ra tất cả cùng lúc, hoàn tác nghĩa là triển khai lại bản dựng cũ bằng tay, và di chuyển lược đồ phá hủy và ghép với tính năng. Mọi phơi bày dần dần là tùy nghi, phản ứng và không có tài liệu.
- **Mức 2, Phát triển:** Cờ tính năng tồn tại cho một số đội và giấu công việc chưa xong, nhưng thiếu chủ sở hữu, kiểu và hết hạn, và nợ đang tích tụ. Canary hay xanh-lam được dùng cho vài dịch vụ trọng yếu, áp dụng không nhất quán theo từng đội. Hoàn tác được viết thành tập lệnh nhưng do con người kích hoạt, và thay đổi lược đồ chỉ đôi khi tương thích ngược.
- **Mức 3, Chuẩn hóa:** Triển khai và phát hành được tách theo mặc định toàn tổ chức. Cờ có kiểu, có chủ sở hữu, và hết hạn, với mặc định an toàn, theo một tiêu chuẩn có tài liệu và được thực thi. Phân phối tăng dần với tung ra theo vòng và phân tích canary tự động là chuẩn mực, di chuyển mở rộng-và-thu hẹp là bắt buộc, và thay đổi chuẩn chảy qua đường ống với nắm bắt bằng chứng tự động.
- **Mức 4, Quản lý:** Quy trình phát hành được đo và kiểm soát bằng dữ liệu. Tỷ lệ thay đổi thất bại, thời gian khôi phục trung bình, độ trễ hoàn tác, tuổi và số cờ, và tỷ lệ dương tính giả của canary được theo dõi theo đường cơ sở và ngân sách lỗi, và việc tung ra được chặn cổng theo các SLO đó (chương 9.1) để thăng cấp và hoàn tác hành động tự động trên tín hiệu sức khỏe xác định. Nợ cờ được báo cáo như chỉ số toàn hệ sinh thái và được cho nghỉ hưu theo lịch, và sai lệch khỏi tiêu chuẩn tung ra nổi lên trên bảng điều khiển thay vì trong một buổi rút kinh nghiệm.
- **Mức 5, Điều phối:** Phân phối tăng dần được cải thiện liên tục và tích hợp trong toàn tổ chức. Phát hành trong bóng tối và lưu lượng bóng giảm rủi ro thay đổi lớn một cách thường lệ, thử nghiệm và tung ra an toàn dùng chung một hệ thống cờ và dấu vết kiểm toán, và chính sách phát hành thích ứng với trạng thái ngân sách lỗi theo thời gian thực. Bản ghi tung ra kiểm toán được thỏa mãn kiểm soát thay đổi (chương 9.3) như sản phẩm phụ, và tổ chức điều chỉnh vòng, cổng và ngưỡng từ bằng chứng khi hệ sinh thái và bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

1. Với dịch vụ trọng yếu nhất của bạn, ranh giới đúng giữa hoàn tác tự động được chặn cổng sức khỏe và quyết định của con người nằm ở đâu, và tín hiệu nào bạn tin đủ để cho máy hành động một mình?
2. Cờ thử nghiệm và cờ phát hành có nên dùng chung một nền tảng và một công tắc ngắt, hay kết hợp chúng tạo thêm rủi ro hơn là loại bỏ?
3. Làm sao bạn quyết định giữa chuyến tàu phát hành và phát hành theo yêu cầu khi một tính năng trải qua nhiều đội phát hành ở tốc độ khác nhau?
4. Chu kỳ bán rã trung thực của một cờ phát hành trong cơ sở mã của bạn là bao lâu, và cái gì làm việc gỡ bỏ thường lệ như việc tạo ra?
5. Trạng thái ngân sách lỗi nên thay đổi ai được phép phát hành thế nào, và ai sở hữu quyết định đóng băng phát hành khi ngân sách cạn?
6. Trong bối cảnh chịu quy định của bạn, bằng chứng cụ thể nào một lần tung ra phải phát ra để khung kiểm soát chấp nhận phân phối tăng dần thay vì cửa sổ phát hành lên lịch?

## Những điểm cần ghi nhớ

- **Tách triển khai khỏi phát hành.** Phát hành mã và phơi bày một tính năng là các quyết định khác nhau, và cờ là thứ tách chúng.
- **Tung ra dần dần.** Mẫu canary, xanh-lam, cuốn chiếu và theo vòng giới hạn bán kính ảnh hưởng; chọn theo bậc dịch vụ theo rủi ro.
- **Chặn cổng theo sức khỏe và ngân sách lỗi.** Để tín hiệu và SLO xác định (chương 9.1) thúc đẩy thăng cấp và hoàn tác tự động, không phải lịch hay sự lạc quan.
- **Thiết kế số lùi trước.** Hoàn tác nhanh, an toàn thu nhỏ bán kính ảnh hưởng trước khi quy trình sự cố của bạn (chương 9.3) tham gia đầy đủ.
- **Đặt kiểu, chủ sở hữu và hết hạn cho mọi cờ.** Cờ phát hành, vận hành, thử nghiệm và quyền có tuổi thọ khác nhau; cờ không được quản lý thành nợ.
- **Làm thay đổi lược đồ tương thích ngược.** Dùng mở rộng và thu hẹp để cả tung ra lẫn hoàn tác vẫn an toàn qua cửa sổ phiên bản hỗn hợp (chương 2.4).
- **Để phê duyệt ghi lại, không cản trở.** Phê duyệt trước thay đổi chuẩn và dành rà soát con người cho rủi ro cao, để bản ghi tung ra là bằng chứng kiểm toán.

## Tài liệu tham khảo và đọc thêm

- Jez Humble và David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois và John Willis, *The DevOps Handbook*.
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (tiểu luận trên martinfowler.com).
- Danilo Sato, "Canary Release" và Martin Fowler, "BlueGreenDeployment" (tiểu luận trên martinfowler.com).
- Sam Newman, *Building Microservices: Designing Fine-Grained Systems* (mở rộng-và-thu hẹp và khả năng triển khai độc lập).
- Pramod Sadalage và Scott Ambler, *Refactoring Databases: Evolutionary Database Design* (di chuyển lược đồ thay đổi song song).
- Ron Kohavi, Diane Tang và Ya Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*.
- James Governor, "Progressive Delivery" (RedMonk, nơi đặt ra thuật ngữ).
