# 5.7 Phát triển ứng dụng di động

## Tổng quan và động lực

[Phát triển ứng dụng di động](https://en.wikipedia.org/wiki/Mobile_app_development) là kỷ luật xây phần mềm cho điện thoại và máy tính bảng. Với nhiều người, điện thoại nay là chiếc máy tính chính hoặc duy nhất họ sở hữu. Điều đó khiến ứng dụng di động là cửa trước dẫn đến dịch vụ của bạn, và thường là bề mặt nơi người dùng đánh giá cả tổ chức của bạn.

Di động là một môi trường kỹ thuật riêng biệt, không phải một phiên bản nhỏ của web hay máy tính để bàn. Thiết bị chạy trong túi, bằng pin, qua các kết nối lúc có lúc không. Màn hình nhỏ. Hệ điều hành kiểm soát những gì ứng dụng của bạn được phép làm. Có hai nền tảng thống trị ([iOS](https://en.wikipedia.org/wiki/IOS) của Apple và [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29) của Google), mỗi cái có ngôn ngữ, quy tắc thiết kế và cửa hàng riêng. Bạn không thể đơn giản phát hành một bản cập nhật bất cứ khi nào mình thích, vì một cửa hàng rà soát nó trước, và người dùng chọn khi nào cài đặt. Chương này xây trên kỹ thuật giao diện người dùng (chương 5.6), nền tảng UX (chương 5.1) và khả năng tiếp cận (chương 5.3), và dựa vào bảo mật ứng dụng (chương 4.2) cùng CI/CD và phân phối (chương 8.1).

Sự liên quan với doanh nghiệp và chính phủ là cao. Doanh nghiệp phát hành ứng dụng khách hàng và ứng dụng nội bộ cho lực lượng lao động của mình, thường được quản lý qua [quản lý thiết bị di động](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: phần mềm trung tâm cấu hình và bảo mật thiết bị công ty). Chính phủ xây ứng dụng hướng công dân cho trợ cấp, y tế, danh tính và thanh toán, và phải phục vụ mọi người, bao gồm người dùng thiết bị cũ và kết nối chậm, dưới luật khả năng tiếp cận. Trong cả hai bối cảnh, di động là một cam kết nghiêm túc, sống lâu, nên hãy đối xử với nó bằng sự chặt chẽ như bất kỳ hệ thống sản xuất nào khác.

## Các nguyên tắc chính

- Thiết kế cho thiết bị: màn hình nhỏ, pin, và một mạng lúc có lúc không.
- Giả định kết nối gián đoạn; ưu tiên ngoại tuyến trước và đồng bộ khi bạn có thể.
- Tôn trọng quy ước thiết kế và tương tác của từng nền tảng.
- Bạn không kiểm soát thời điểm phát hành; cửa hàng và người dùng làm vậy.
- Phân mảnh là bình thường; hỗ trợ một dải thiết bị và phiên bản hệ điều hành thực.
- Lưu dữ liệu an toàn trên thiết bị, vì thiết bị bị mất và bị đánh cắp.
- Khả năng tiếp cận là yêu cầu, không phải nét hoàn thiện.
- Chọn cách tiếp cận dựng cho toàn bộ vòng đời của ứng dụng, không chỉ ngày ra mắt.

## Khuyến nghị

### Chọn cách tiếp cận dựng có chủ đích

Có ba cách tiếp cận rộng, và mỗi cái phù hợp với nhu cầu khác nhau.

[Phát triển bản địa](https://en.wikipedia.org/wiki/Mobile_app_development) nghĩa là viết riêng cho từng nền tảng bằng công cụ riêng của nó: Swift cho iOS, Kotlin cho Android. Bạn có hiệu năng tốt nhất, truy cập tính năng thiết bị đầy đủ nhất, và cảm giác nền tảng trung thực nhất, với cái giá là xây và duy trì hai cơ sở mã.

[Khung phát triển đa nền tảng](https://en.wikipedia.org/wiki/Cross-platform_software) cho phép một cơ sở mã nhắm cả hai nền tảng. [React Native](https://en.wikipedia.org/wiki/React_Native) dùng JavaScript và kết xuất các thành phần bản địa thật. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) dùng ngôn ngữ Dart và tự vẽ widget của nó. Những thứ này giảm công sức trùng lặp và có thể tăng tốc phân phối, nhưng thêm một phụ thuộc vào sức khỏe của khung phát triển và có thể tụt hậu so với các tính năng nền tảng mới nhất.

Một [ứng dụng web tiến bộ](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: một trang web có thể cài đặt và hoạt động ngoại tuyến) không cần cửa hàng và cập nhật tức thì, nhưng có truy cập hạn chế đến một số tính năng thiết bị và sự hiện diện yếu hơn trên màn hình chính.

Hãy chọn dựa trên các tính năng thiết bị cần thiết, hồ sơ hiệu năng, chân trời bảo trì, kỹ năng bạn có thể tuyển, và tầm với bạn cần. Một ứng dụng tiêu dùng hiệu năng cao có thể biện minh cho bản địa. Một ứng dụng nội dung-và-biểu mẫu với đội nhỏ có thể vừa với đa nền tảng hoặc PWA.

### Theo hướng dẫn thiết kế nền tảng

Mỗi nền tảng có quy ước chi tiết đã công bố. Apple cung cấp [Hướng dẫn Giao diện Con người](https://en.wikipedia.org/wiki/Human_interface_guidelines), và Google cung cấp [Material Design](https://en.wikipedia.org/wiki/Material_Design). Chúng bao quát điều hướng, cử chỉ, kiểu chữ, khoảng cách và hành vi hệ thống. Theo chúng làm ứng dụng của bạn cảm thấy quen thuộc, điều hạ công sức người dùng bỏ ra để học nó. Chống lại chúng làm một ứng dụng cảm thấy xa lạ và vụng về. Một cơ sở mã đa nền tảng vẫn cần tôn trọng quy ước theo từng nền tảng ở nơi chúng khác nhau, thay vì ép diện mạo của một nền tảng lên nền tảng kia.

### Thiết kế cho ràng buộc di động

Hãy xây ưu tiên-ngoại-tuyến: để các nhiệm vụ lõi hoạt động không cần kết nối, lưu thay đổi cục bộ, và đồng bộ khi mạng quay lại. Xử lý xung đột cẩn thận khi cùng dữ liệu thay đổi ở hai nơi. Tiết kiệm pin và dữ liệu: gộp lệnh gọi mạng, tránh vị trí hay công việc nền liên tục, nén tải trọng, và tôn trọng thiết lập tiết kiệm dữ liệu của người dùng. Lên kế hoạch cho phân mảnh, dải rộng kích thước màn hình, sức mạnh thiết bị và phiên bản hệ điều hành. Chọn dải hỗ trợ dựa trên dữ liệu sử dụng thực, và kiểm thử trên phần cứng khiêm tốn, không chỉ máy hàng đầu. Thiết kế cho màn hình nhỏ với phân cấp rõ ràng, mục tiêu cảm ứng lớn, và nội dung thích ứng với các kích thước và hướng khác nhau.

### Hoạch định phân phối, phiên bản và cập nhật

Xuất bản đi qua [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) và [Google Play](https://en.wikipedia.org/wiki/Google_Play), mỗi nơi có quy trình rà soát và chính sách có thể trì hoãn hoặc từ chối một bản phát hành. Hãy đưa thời gian rà soát vào lịch trình, và đọc chính sách sớm. Vì người dùng chọn khi nào cập nhật, bạn sẽ luôn có nhiều phiên bản ngoài hiện trường cùng lúc. Giữ ứng dụng của bạn tương thích ngược với máy khách cũ hơn, và đánh phiên bản API của bạn (chương 2.3) để một ứng dụng cũ tiếp tục hoạt động. Cung cấp cách bắt buộc cập nhật khi bạn phải làm, ví dụ một lời nhắc cập nhật bắt buộc khi một phiên bản không an toàn hoặc không còn được hỗ trợ, và dùng nó tiết kiệm. Doanh nghiệp cũng có thể phân phối ứng dụng nội bộ qua MDM hoặc kênh riêng thay vì cửa hàng công khai.

### Dùng thông báo đẩy và liên kết sâu cẩn thận

[Thông báo đẩy](https://en.wikipedia.org/wiki/Push_technology) cho phép bạn tiếp cận người dùng khi ứng dụng đóng. Hãy dùng chúng cho giá trị thực, tôn trọng sự đồng ý của người dùng và quyền nền tảng, và tránh nhiễu, vì người ta tắt thông báo từ các ứng dụng làm quá. [Liên kết sâu](https://en.wikipedia.org/wiki/Deep_linking) đưa người dùng thẳng đến một màn hình cụ thể từ một liên kết hay thông báo. Hãy cấu hình chúng để một liên kết mở đúng nơi trong ứng dụng, và quay về web nhẹ nhàng khi ứng dụng chưa được cài.

### Bảo mật ứng dụng và dữ liệu của nó

Hãy coi thiết bị là không đáng tin và có thể bị mất. Lưu dữ liệu nhạy cảm trong kho lưu trữ an toàn của nền tảng ([Keychain của iOS](https://en.wikipedia.org/wiki/Keychain_%28software%29) hoặc Keystore của Android), không bao giờ trong tệp thuần. Cung cấp [xác thực sinh trắc học](https://en.wikipedia.org/wiki/Biometrics) (vân tay hoặc khuôn mặt) để mở khóa hành động nhạy cảm, hậu thuẫn bằng mật mã. Cân nhắc [ghim chứng chỉ](https://en.wikipedia.org/wiki/Public_key_pinning) (kiểm tra rằng máy chủ xuất trình một chứng chỉ kỳ vọng) cho các kết nối giá trị cao, và lên kế hoạch xoay vòng các chứng chỉ đó. Tối thiểu hóa những gì bạn lưu trên thiết bị, bảo vệ bí mật, và theo hướng dẫn rộng hơn trong bảo mật ứng dụng (chương 4.2).

### Xây một đường ống kiểm thử và phân phối thực

Hãy kiểm thử trên thiết bị thật, không chỉ [trình giả lập](https://en.wikipedia.org/wiki/Emulator) và trình mô phỏng, vì phần cứng, cảm biến và hiệu năng khác nhau. Dùng một phòng thí nghiệm thiết bị hoặc một trang trại thiết bị đám mây để bao quát một dải đại diện các mẫu và phiên bản hệ điều hành. Tự động hóa bản dựng, kiểm thử, ký và nộp lên cửa hàng qua [tích hợp và phân phối liên tục](https://en.wikipedia.org/wiki/CI/CD) (chương 8.1), bao gồm phân phối beta cho người kiểm thử trước khi phát hành công khai. Quản lý an toàn khóa ký và thông tin xác thực cửa hàng là một phần của đường ống này.

### Biến khả năng tiếp cận thành yêu cầu

Hãy hỗ trợ các tính năng khả năng tiếp cận của từng nền tảng: trình đọc màn hình ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) trên iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) trên Android), cỡ chữ động, độ tương phản màu đủ, và mục tiêu cảm ứng lớn. Gắn nhãn điều khiển để công nghệ hỗ trợ mô tả được chúng. Kiểm thử với công cụ hỗ trợ thực, không chỉ kiểm tra tự động. Đặc biệt với chính phủ, khả năng tiếp cận là yêu cầu pháp lý bắt buộc, và chi tiết nằm trong khả năng tiếp cận (chương 5.3).

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Bản địa (Swift, Kotlin) | Hiệu năng tốt nhất, truy cập thiết bị đầy đủ, cảm giác nền tảng đúng nghĩa | Hai cơ sở mã, chi phí cao hơn, nhiều nhân sự hơn |
| React Native | Một cơ sở mã JavaScript, thành phần bản địa thật, lặp nhanh | Phụ thuộc khung phát triển, độ phức tạp cầu nối, tụt hậu tính năng |
| Flutter | Một cơ sở mã, UI nhất quán, hiệu năng mạnh | Kỹ năng Dart ít phổ biến hơn, kích thước ứng dụng lớn hơn, mô hình widget riêng |
| Ứng dụng web tiến bộ | Không cần cửa hàng, cập nhật tức thì, một cơ sở mã web | Tính năng thiết bị hạn chế, hiện diện yếu hơn, giới hạn nền tảng |
| Cập nhật bắt buộc | Loại bỏ nhanh các phiên bản cũ không an toàn | Làm phiền người dùng nếu lạm dụng; có thể chặn truy cập |
| Ghim chứng chỉ | Bảo vệ mạnh chống chặn đường truyền | Hỏng nếu chứng chỉ xoay vòng mà không cập nhật ứng dụng |

Đánh đổi lặp lại là tầm với và tốc độ phân phối so với chiều sâu và độ trung thực. Bản địa cho trải nghiệm phong phú nhất, trung thực nhất nhưng tốn nhất để xây và duy trì. Các cách tiếp cận đa nền tảng và PWA tiết kiệm công sức và mở rộng tầm với, với một ít chi phí về cảm giác nền tảng hay truy cập thiết bị. Với một đội nhỏ phát hành biểu mẫu và nội dung, chia sẻ một cơ sở mã thường là khôn ngoan. Với một ứng dụng tiêu dùng đòi hỏi cao, chiều sâu bản địa có thể xứng đáng với giá. Hãy quyết định với toàn bộ vòng đời của ứng dụng trong tầm mắt, không chỉ ngày ra mắt.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta hỗ trợ máy khách cũ ngoài hiện trường bao lâu, và API của chúng ta có được đánh phiên bản để giữ chúng hoạt động không?** Vì người dùng chọn khi nào cập nhật, bạn luôn có nhiều phiên bản ứng dụng được cài đặt cùng lúc, và một thay đổi backend giả định mọi người đều hiện hành sẽ làm hỏng cái đuôi dài các máy khách cũ hơn. Hãy quyết định cửa sổ tương thích ngược của bạn, đánh phiên bản API để một ứng dụng cũ tiếp tục hoạt động, và giữ một đường cập nhật bắt buộc hiếm dùng cho các phiên bản thực sự không an toàn. Điều này quan trọng với cả ứng dụng công dân của chính phủ lẫn ứng dụng lực lượng lao động doanh nghiệp, nơi những người dùng thiết bị cũ không thể hoặc không muốn nâng cấp theo lịch của bạn. Hãy mang dữ liệu phân bố phiên bản hiện tại của bạn và hỏi cái gì hỏng với máy khách cũ nhất vẫn đang được dùng thực. Nếu bạn không biết phân bố đó, hãy đo đạc nó trước khi phát hành thay đổi phá vỡ kế tiếp.

2. **Ngưỡng của chúng ta để gửi một thông báo đẩy là gì, và ai quyết định điều gì đáng làm gián đoạn người dùng?** Thông báo đẩy tiếp cận mọi người khi ứng dụng đóng, khiến chúng mạnh và dễ bị lạm dụng, và người dùng tắt thông báo (hoặc xóa ứng dụng) từ các sản phẩm làm quá. Hãy thống nhất cái gì cấu thành giá trị thực, người dùng kiểm soát tần suất và kênh thế nào, và bạn tôn trọng sự đồng ý của nền tảng ra sao thay vì liên tục đòi quyền. Không có ngưỡng chung, mọi đội có chỉ số cần đạt sẽ với tới một thông báo đẩy, và cả kênh thoái hóa thành nhiễu. Hãy mang các thông báo bạn đã gửi trong tháng qua và hỏi cái nào người dùng sẽ cảm ơn bạn. Nếu hầu hết là quảng cáo, hãy siết chính sách trước khi tỷ lệ chọn không tham gia làm điều đó thay bạn.

3. **Đường ống phân phối di động của chúng ta có thật, bao quát ký, trang trại thiết bị và phân phối beta, hay phát hành là một cuộc chạy vạy thủ công căng thẳng?** Di động thêm những mối nguy mà web không có: rà soát cửa hàng có thể trì hoãn hoặc từ chối một bản phát hành, khóa ký và thông tin xác thực cửa hàng phải được xử lý an toàn, và phần cứng cùng cảm biến khác nhau đủ để trình giả lập che giấu các vấn đề thực. Tự động hóa bản dựng, kiểm thử, ký và nộp lên cửa hàng qua CI/CD, với phân phối beta cho người kiểm thử và một trang trại thiết bị đám mây bao quát các mẫu máy người dùng của bạn thực sự mang, là thứ biến phát hành từ anh hùng thành thường lệ. Hãy quyết định ai sở hữu đường ống và khóa ký, và thời gian rà soát cửa hàng được đưa vào mỗi kế hoạch phát hành thế nào. Hãy mang câu chuyện về bản phát hành gần nhất của bạn và đếm các bước thủ công. Mỗi bước là một nơi một lần phát hành căng thẳng có thể hỏng dưới hạn chót.

4. **Chúng ta đã chọn bản địa, đa nền tảng hay ứng dụng web tiến bộ cho toàn bộ vòng đời của sản phẩm này, hay chỉ cho ngày ra mắt?** Cách tiếp cận dựng là đòn bẩy lớn nhất đơn lẻ lên chi phí và năng lực của một ứng dụng di động trong nhiều năm, và một lựa chọn đưa ra để phát hành nhanh có thể mắc kẹt bạn: bản địa mua truy cập thiết bị phong phú nhất và cảm giác nền tảng với giá hai cơ sở mã và hai bộ kỹ năng, trong khi đa nền tảng và PWA chia sẻ mã nhưng thêm phụ thuộc khung phát triển hoặc mất truy cập một số tính năng thiết bị. Với một đội lớn, quyết định này thúc đẩy tuyển dụng, ngân sách bảo trì, và bạn có thể áp dụng mỗi bản hệ điều hành hằng năm nhanh thế nào, nên nó xứng đáng có chủ sở hữu tường minh thay vì mặc định do ai viết bản mẫu đầu tiên đặt ra. Hãy mang các tính năng thiết bị cần thiết, hồ sơ hiệu năng, chân trời bảo trì, và kỹ năng bạn thực sự tuyển được, và trung thực về tính năng nền tảng nào bạn sẽ mất theo mỗi lựa chọn. Trong bối cảnh doanh nghiệp và chính phủ, hãy cân nhắc liệu ứng dụng có là cam kết sống lâu phải sống sót qua sự luân chuyển nhân sự và một thập kỷ thay đổi nền tảng, và ghi lại quyết định cùng lý do để một đội tương lai không phải đoán vì sao cơ sở mã trông như vậy.

5. **Dải hỗ trợ thiết bị và phiên bản hệ điều hành nào mà người dùng thực của chúng ta cần, và chúng ta có đang kiểm thử trên phần cứng họ thực sự mang thay vì điện thoại trên bàn của chúng ta không?** Phân mảnh là điều kiện bình thường của di động: người dùng trải qua một dải rộng kích thước màn hình, sức mạnh thiết bị và phiên bản hệ điều hành, và một ứng dụng được điều chỉnh trên máy hàng đầu của đội sẽ được phát hành chậm chạp hoặc hỏng trên phần cứng khiêm tốn mà phần lớn đối tượng của bạn sở hữu. Đặt dải hỗ trợ là một đánh đổi giữa tầm với và công sức, vì mỗi mẫu cũ và phiên bản hệ điều hành bạn hứa hỗ trợ mở rộng ma trận kiểm thử và gánh nặng bảo trì, nên dải phải đến từ dữ liệu sử dụng thực thay vì giả định. Hãy mang phân bố thiết bị và phiên bản hệ điều hành của bạn, các mẫu mà một trang trại thiết bị đám mây hay phòng thí nghiệm hiện bao quát, và hiệu năng bạn đã đo trên phần cứng cấp thấp, không chỉ trình mô phỏng. Với ứng dụng công dân của chính phủ điều này gần như không thể thương lượng, vì bạn phải phục vụ mọi người bao gồm người dùng thiết bị cũ và kết nối chậm theo nghĩa vụ khả năng tiếp cận, và với đội thiết bị doanh nghiệp bạn nên kiểm thử chính xác các máy cầm tay chắc chắn mà nhân viên mang thay vì một mẫu chung.

6. **Dữ liệu nhạy cảm nào sống trên thiết bị, và mỗi mảnh có được bảo vệ chống một chiếc điện thoại bị mất, bị đánh cắp, hay nằm trong tay người khác không?** Một thiết bị di động đi trong túi và bị mất hoặc bị đánh cắp, nên bất kỳ dữ liệu hay bí mật nào lưu trong tệp thuần chỉ cách việc đánh rơi một chiếc điện thoại là bị phơi bày, và bán kính ảnh hưởng lớn lên với mỗi người dùng. Các cân nhắc kéo nhau: lưu đệm dữ liệu trên thiết bị là thứ làm ưu-tiên-ngoại-tuyến hoạt động và giữ ứng dụng nhanh, vậy mà mỗi mục được lưu đệm là một khoản nợ phải nằm trong kho lưu trữ an toàn của nền tảng (Keychain của iOS hoặc Keystore của Android), được tối thiểu hóa, và lý tưởng là được khóa sau sinh trắc học hay mật mã. Hãy mang bản kiểm kê chính xác những gì ứng dụng lưu bền cục bộ, mỗi mục được lưu ở đâu, cái gì mở khóa nó, và liệu các kết nối giá trị cao có dùng ghim chứng chỉ với kế hoạch xoay vòng khả thi không. Trong bối cảnh doanh nghiệp, hãy gắn điều này với chính sách quản lý thiết bị di động và xóa từ xa, và trong bối cảnh chính phủ hãy coi dữ liệu cá nhân trên thiết bị là một sự phơi nhiễm quyền riêng tư và pháp lý phải được biện minh, lập tài liệu và bảo vệ được dưới kiểm toán.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với đội nhỏ xíu và đường băng ít ỏi, bạn hiếm khi gánh nổi hai cơ sở mã bản địa hay hai bộ kỹ năng, nên một khung phát triển đa nền tảng hoặc thậm chí một PWA đến cả hai cửa hàng từ một cơ sở mã thường thắng. Hãy phát hành ưu-tiên-ngoại-tuyến cho nhiệm vụ lõi duy nhất quan trọng, giữ bất kỳ token nào trong kho lưu trữ an toàn thay vì tệp thuần, và đưa thời gian rà soát cửa hàng vào mỗi bản phát hành để một lần từ chối không phá hỏng ngày ra mắt. Bỏ qua cập nhật bắt buộc, ghim chứng chỉ và trang trại thiết bị cho đến khi việc sử dụng thực biện minh.

**Doanh nghiệp nhỏ.** Không có chuyên gia di động riêng và ngân sách eo hẹp, hãy nghiêng mạnh về mua hơn xây: một công cụ dựng ứng dụng không mã, một ứng dụng nhãn trắng từ nhà cung cấp điểm bán hàng hay đặt chỗ, hoặc một PWA tốt từ trang web hiện có của bạn thường thắng một ứng dụng theo yêu cầu mà bạn không bảo trì nổi. Nếu bạn đặt hàng một ứng dụng, hãy tự sở hữu khóa ký và tài khoản cửa hàng để nhà thầu không thể giữ sự hiện diện của bạn làm con tin, và kiên quyết đòi khả năng tiếp cận cùng lưu trữ an toàn trên thiết bị trong hợp đồng. Giữ phạm vi ở một hai nhiệm vụ khách hàng thực sự làm trên điện thoại.

**Doanh nghiệp lớn.** Ở quy mô lớn, ứng dụng là cam kết sống lâu qua nhiều đội, vì vậy hãy chuẩn hóa cách tiếp cận dựng, mẫu lưu trữ an toàn, đường ống CI/CD, và chính sách đánh phiên bản API thay vì để mỗi sản phẩm phát minh lại. Ứng dụng lực lượng lao động nội bộ thường chảy qua quản lý thiết bị di động để cài đặt, cấu hình, xóa từ xa và chính sách, trong khi ứng dụng khách hàng cần một trang trại thiết bị bao quát việc sử dụng thực và khả năng tiếp cận cùng bảo mật được kiểm toán. Hãy quản trị khóa ký, thông tin xác thực cửa hàng và thời điểm phát hành tập trung để một thay đổi backend phá vỡ không bao giờ bỏ rơi cái đuôi dài các máy khách cũ.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Bạn phải phục vụ mọi người, bao gồm người dùng thiết bị cũ và kết nối chậm, nên khả năng tiếp cận là yêu cầu pháp lý bắt buộc được xác minh bằng công cụ hỗ trợ thực, và một dải hỗ trợ thiết bị rộng gần như không thể thương lượng. Hãy ưu tiên cách tiếp cận và hợp đồng tránh khóa chặt nhà cung cấp, giữ dữ liệu di động được, và cho công chúng kiểm tra ứng dụng làm gì với dữ liệu của họ, và coi dữ liệu cá nhân trên thiết bị là sự phơi nhiễm bạn phải biện minh và lập tài liệu dưới kiểm toán.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp ba người xây ứng dụng theo dõi thói quen phải tiếp cận cả iOS và Android nhưng không gánh nổi hai cơ sở mã bản địa hay hai bộ kỹ năng. Họ chọn một khung phát triển đa nền tảng để một đội nhỏ phát hành lên cả hai cửa hàng, và thiết kế ưu-tiên-ngoại-tuyến từ đầu để người dùng ghi một thói quen trên tàu điện ngầm không có sóng và đồng bộ sau. Họ giữ token đăng nhập trong kho lưu trữ an toàn của nền tảng thay vì tệp thuần, đưa thời gian rà soát cửa hàng vào mỗi kế hoạch phát hành, và kiểm thử trên vài chiếc điện thoại cũ rẻ cùng với máy của chính họ, điều bắt được hiệu năng chậm chạp mà lẽ ra họ đã phát hành.

**Doanh nghiệp lớn.** Một công ty hậu cần xây ứng dụng nội bộ cho tài xế và nhân viên kho. Vì kho và tuyến giao hàng có sóng chập chờn, đội chọn thiết kế ưu-tiên-ngoại-tuyến: quét và cập nhật trạng thái lưu cục bộ và đồng bộ khi kết nối quay lại. Họ dùng một khung phát triển đa nền tảng để phục vụ một cơ sở mã cho cả hai nền tảng với một đội nhỏ. Ứng dụng được phân phối qua quản lý thiết bị di động thay vì cửa hàng công khai, nên CNTT kiểm soát cài đặt, cấu hình và chính sách bảo mật trên thiết bị công ty. Thông tin xác thực nhạy cảm sống trong kho lưu trữ an toàn của nền tảng, và sinh trắc học mở khóa ứng dụng. Một trang trại thiết bị đám mây kiểm thử một dải đại diện các máy cầm tay chắc chắn mà nhân viên thực sự mang.

**Chính phủ.** Một cơ quan quốc gia phát hành ứng dụng hướng công dân cho danh tính và trợ cấp. Khả năng tiếp cận là yêu cầu cứng từ ngày đầu: hỗ trợ trình đọc màn hình đầy đủ, cỡ chữ động, và độ tương phản mạnh, được kiểm thử bằng công cụ hỗ trợ thật để đáp ứng luật. Vì công dân dùng một dải thiết bị khổng lồ, đội hỗ trợ một dải rộng các mẫu cũ và kết nối chậm, và giữ nhiệm vụ lõi hoạt động ngoại tuyến. Dữ liệu nhạy cảm ở trong kho lưu trữ thiết bị an toàn, sinh trắc học bảo vệ truy cập, và các kết nối giá trị cao dùng ghim chứng chỉ với quy trình xoay vòng đã lên kế hoạch. Đánh phiên bản API giữ các ứng dụng cài đặt cũ hoạt động, và một đường cập nhật bắt buộc hiếm dùng tồn tại cho bản sửa bảo mật. Mốc thời gian rà soát cửa hàng được đưa vào mỗi kế hoạch phát hành.

## Luận chứng kinh doanh: động lực, ROI và TCO

Di động là nơi nhiều người dùng gặp dịch vụ của bạn, nên ứng dụng ảnh hưởng đến việc áp dụng, sự hài lòng và hoàn thành các nhiệm vụ quan trọng với tổ chức của bạn. Một ứng dụng nhanh, đáng tin, thiết kế tốt tăng việc sử dụng và giảm tải hỗ trợ. Với doanh nghiệp, một ứng dụng di động nội bộ có thể làm lực lượng lao động di động năng suất hơn một cách đo được và cắt giấy tờ. Với chính phủ, một ứng dụng công dân dùng được mở rộng tiếp cận và giảm nhu cầu tổng đài và trực tiếp.

Về tổng chi phí sở hữu (TCO), lựa chọn cách tiếp cận là đòn bẩy lớn nhất. Bản địa nghĩa là trả cho hai cơ sở mã và hai bộ kỹ năng suốt vòng đời của ứng dụng. Đa nền tảng đánh đổi một phần đó lấy một phụ thuộc bạn phải giữ hiện hành. Ngoài mã, hãy ngân sách cho phí cửa hàng và chu kỳ rà soát, một phòng thí nghiệm hay trang trại đám mây kiểm thử thiết bị, hỗ trợ phiên bản hệ điều hành liên tục khi các nền tảng phát hành hằng năm, và công việc bảo mật mà di động đòi hỏi. Chi phí của việc đầu tư thiếu hiện ra là sập trên thiết bị không được hỗ trợ, sự cố bảo mật từ dữ liệu trên thiết bị không được bảo vệ, bản phát hành bị từ chối hoặc trì hoãn, và người dùng bỏ một ứng dụng chậm hoặc vụng về.

Để trình bày lập luận với ban lãnh đạo, hãy nối ứng dụng với kết quả cụ thể: hoàn thành nhiệm vụ, giữ chân, năng suất lực lượng lao động, hay giảm chi phí hỗ trợ. Hãy định giá quyết định cách tiếp cận đầy đủ qua vòng đời của ứng dụng, không chỉ bản phát hành đầu, và nêu tên các rủi ro (bảo mật, luật khả năng tiếp cận, từ chối cửa hàng) mà một thực hành di động nghiêm túc giảm thiểu.

## Phản mẫu và cạm bẫy

- **Coi di động là một trang web thu nhỏ**: bỏ qua cảm ứng, cử chỉ và quy ước nền tảng.
- **Giả định mạng hoàn hảo**: không xử lý ngoại tuyến, nên ứng dụng hỏng ngay khi mất sóng.
- **Chỉ kiểm thử trên máy hàng đầu mới nhất**: che giấu hiệu năng kém trên thiết bị người dùng thực mang.
- **Lưu bí mật trong tệp thuần**: dữ liệu nhạy cảm bị phơi bày khi thiết bị bị mất hoặc bị đánh cắp.
- **Quá tải thông báo**: quá nhiều thông báo đẩy, nên người dùng tắt tiếng hoặc xóa ứng dụng.
- **Bỏ qua thời gian rà soát cửa hàng**: kế hoạch phát hành giả định xuất bản tức thì rồi trượt.
- **Không có đường cập nhật bắt buộc**: các phiên bản cũ không an toàn sống tiếp mà không có cách loại bỏ.
- **Hao pin và dữ liệu**: công việc nền liên tục và mạng lắm lời mà người dùng nhận ra.
- **Khả năng tiếp cận như chuyện nghĩ sau**: loại trừ người dùng và, với chính phủ, vi phạm luật.
- **Một cơ sở mã bị ép trông giống hệt nhau ở mọi nơi**: một ứng dụng cảm thấy xa lạ trên cả hai nền tảng.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Di động là tùy nghi và phản ứng. Ứng dụng được xây như một trang web, kiểm thử trên điện thoại của chính đội, và thường hỏng khi ngoại tuyến. Ít suy nghĩ dành cho lưu trữ an toàn, khả năng tiếp cận hay mốc thời gian rà soát cửa hàng. Phát hành là một cuộc chạy vạy thủ công căng thẳng, và không ai sở hữu cách tiếp cận dựng hay khóa ký.

**Mức 2: Phát triển.** Các thực hành cơ bản xuất hiện, nhưng không nhất quán qua các đội và sản phẩm. Một cách tiếp cận dựng được chọn cho một ứng dụng nhất định, nó theo những điều cơ bản của nền tảng và được kiểm thử trên vài thiết bị thật, và một số xử lý ngoại tuyến cùng lưu trữ an toàn tồn tại. Bản dựng được tự động một phần và ai đó sở hữu việc nộp cửa hàng, nhưng ứng dụng của đội khác có thể vẫn làm tất cả những điều này khác đi hoặc không hề.

**Mức 3: Chuẩn hóa.** Thực hành tốt được lập tài liệu và thực thi toàn tổ chức. Ưu-tiên-ngoại-tuyến là mặc định, một dải hỗ trợ thiết bị có tài liệu được kiểm thử trên phòng thí nghiệm thiết bị hay trang trại đám mây, và hướng dẫn thiết kế nền tảng cùng khả năng tiếp cận được theo và xác minh bằng công cụ hỗ trợ thật. Lưu trữ an toàn, sinh trắc học và đánh phiên bản API là tiêu chuẩn, CI/CD tự động hóa bản dựng, kiểm thử, ký và phân phối beta, và thời gian rà soát cửa hàng được hoạch định vào mỗi bản phát hành.

**Mức 4: Quản lý.** Chất lượng di động được đo và kiểm soát theo các đường cơ sở. Sập, hiệu năng khởi động nguội và kết xuất màn hình, mức dùng pin và dữ liệu, và tỷ lệ hoàn thành nhiệm vụ được nắm bắt liên tục từ thiết bị thật và theo dõi theo mục tiêu, với bảng phân tích theo từng mẫu và phiên bản hệ điều hành để một hồi quy trên phần cứng cấp thấp được bắt, không được phát hành. Khả năng tiếp cận và bảo mật được kiểm toán thay vì giả định, tỷ lệ chọn không nhận thông báo và tỷ lệ áp dụng cập nhật được giám sát, và dải hỗ trợ cùng cách tiếp cận dựng được rà soát trên bằng chứng này. Quyết định loại bỏ hay sửa một bản phát hành dựa trên các chỉ số, không phải cảm giác ứng dụng trên điện thoại của người dẫn đầu.

**Mức 5: Điều phối.** Di động được cải thiện liên tục và tích hợp trong toàn tổ chức, và nó thích ứng khi bối cảnh thiết bị dịch chuyển. Xoay vòng chứng chỉ, đường cập nhật bắt buộc và hoàn tác là thường lệ, dải hỗ trợ và cách tiếp cận dựng được điều chỉnh phạm vi dựa trên bằng chứng khi các nền tảng phát hành hằng năm, và toàn bộ dải người dùng cùng thiết bị được coi là hạng nhất. Hoạch định di động được nối với thực hành bảo mật, khả năng tiếp cận, API và phân phối, để một thay đổi hệ điều hành, một bậc thiết bị mới, hay một dịch chuyển chính sách được hấp thụ như công việc thường lệ thay vì khẩn cấp.

## Ý tưởng để thảo luận

- Làm sao bạn quyết định giữa bản địa, đa nền tảng và ứng dụng web tiến bộ cho một sản phẩm nhất định?
- Dải hỗ trợ thiết bị và phiên bản hệ điều hành nào khớp dữ liệu người dùng thực của bạn, và làm sao bạn giữ nó hiện hành?
- Ưu-tiên-ngoại-tuyến thiết yếu ở đâu trong ứng dụng của bạn, và bạn sẽ xử lý xung đột đồng bộ thế nào?
- Khi nào cập nhật bắt buộc được biện minh, và làm sao bạn tránh chặn người dùng một cách không công bằng?
- Bạn sẽ kiểm thử trên thiết bị thật ở quy mô phản ánh người dùng của bạn thế nào?
- Dữ liệu nhạy cảm nào sống trên thiết bị, và mỗi mảnh được bảo vệ thế nào?
- Làm sao bạn tôn trọng quy ước của từng nền tảng từ một cơ sở mã dùng chung?

## Những điểm cần ghi nhớ

- Chọn cách tiếp cận dựng (bản địa, đa nền tảng hay PWA) cho toàn bộ vòng đời của ứng dụng.
- Theo hướng dẫn thiết kế nền tảng để ứng dụng cảm thấy quen thuộc và hạ công sức của người dùng.
- Thiết kế cho ràng buộc di động: ưu-tiên-ngoại-tuyến, tiết kiệm pin và dữ liệu, phân mảnh, màn hình nhỏ.
- Bạn không kiểm soát thời điểm phát hành; hãy lên kế hoạch cho rà soát cửa hàng, phiên bản và cập nhật bắt buộc.
- Dùng thông báo đẩy và liên kết sâu một cách kiềm chế và có sự đồng ý.
- Bảo mật dữ liệu trên thiết bị bằng lưu trữ an toàn, sinh trắc học, và, ở nơi cần, ghim chứng chỉ.
- Kiểm thử trên thiết bị thật và tự động hóa đường ống di động qua CI/CD.
- Biến khả năng tiếp cận thành yêu cầu, mà với chính phủ là yêu cầu pháp lý bắt buộc.

## Tài liệu tham khảo và đọc thêm

- Apple, *Human Interface Guidelines*
- Google, hướng dẫn *Material Design*
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies và tài liệu nhà phát triển Android*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* và *Mobile Security Testing Guide*
- Tài liệu dự án React Native
- Tài liệu dự án Flutter
- Google, hướng dẫn *web.dev* về ứng dụng web tiến bộ
- Section 508 của Hoa Kỳ và WCAG (Web Content Accessibility Guidelines) tham chiếu cho khả năng tiếp cận di động
- NIST, *Guidelines on mobile device security and management*
