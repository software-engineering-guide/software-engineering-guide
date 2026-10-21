# 4.8 Mật mã học và quản lý khóa

## Tổng quan và động lực

Gần như mọi hệ thống bạn xây đã phụ thuộc vào [mật mã học](https://en.wikipedia.org/wiki/Cryptography), thực hành bảo vệ thông tin bằng các kỹ thuật toán học để chỉ các bên dự định mới đọc hoặc tin được nó. Lưu lượng web của bạn đi trên các kênh được mã hóa, mật khẩu của bạn được băm, các bản cập nhật phần mềm được ký, và dữ liệu khách hàng nằm được mã hóa trên đĩa. Tin tốt cho hầu hết kỹ sư là bạn không bị yêu cầu phát minh bất cứ thứ gì trong số này. Phần khó không phải là toán học. Mà là dùng các khối xây dựng đã được thẩm định một cách đúng đắn và, trên hết, quản lý các khóa mà các khối xây dựng đó phụ thuộc vào.

Chương này được viết cho các kỹ sư không phải nhà mật mã học, tức gần như tất cả chúng ta. Bạn cần đủ hiểu biết để đưa ra lựa chọn đúng đắn, biết mỗi công cụ bảo đảm gì, và tránh những sai lầm biến các thuật toán mạnh thành sự an ủi giả. Chương 4.3 (bảo mật hạ tầng và đám mây) nhắc đến mã hóa và quản lý khóa thoáng qua; ở đây chúng ta đi sâu hơn vào cái gì cần mã hóa, mã hóa thế nào, và cách vận hành vòng đời khóa khiến nó thành hiện thực.

Với các doanh nghiệp lớn, mật mã học lan khắp hàng nghìn dịch vụ, chứng chỉ và khóa, và một chứng chỉ hết hạn hay một khóa bị mất đơn lẻ có thể đánh sập một hệ thống quan trọng hoặc làm rò rỉ một kho dữ liệu. Với chính phủ, mật mã học thường bị bắt buộc, xác nhận và kiểm toán, với quy tắc phân loại dữ liệu quyết định chính xác khóa nào bảo vệ bí mật nào và ai được giữ chúng. Trong cả hai bối cảnh, thất bại lặp lại là giống nhau: thuật toán tốt bị phá hỏng bởi quản lý khóa cẩu thả.

## Các nguyên tắc chính

- **Đừng tự viết mật mã.** Dùng các thư viện đã được thẩm định, rà soát rộng rãi và thuật toán chuẩn. Các lược đồ mới lạ thất bại theo cách chỉ chuyên gia mới bắt được.
- **Thuật toán là phần dễ; khóa là phần khó.** Vòng đời của một khóa là nơi hầu hết thất bại thực tế sống.
- **Biết mỗi nguyên thủy bảo đảm gì.** Tính bảo mật, toàn vẹn và xác thực là các thuộc tính khác nhau đòi hỏi công cụ khác nhau.
- **Mã hóa khi truyền và khi lưu theo mặc định.** Làm cho bảo vệ là tiêu chuẩn, không phải tùy chọn chọn tham gia.
- **Tách việc giữ khóa khỏi truy cập dữ liệu.** Ai quản lý một khóa không nên tự động đọc được dữ liệu nó bảo vệ.
- **Lên kế hoạch cho thay đổi.** Thuật toán suy yếu, khóa rò rỉ, và tiêu chuẩn tiến hóa. Hãy xây cho xoay vòng và di chuyển ngay từ ngày đầu.
- **Ưu tiên các cài đặt đã được xác nhận ở nơi quan trọng.** Với công việc chịu quy định và chính phủ, hãy chọn các mô-đun có xác nhận được công nhận.

## Khuyến nghị

### Đừng tự viết mật mã

Đây là quy tắc vàng, và đáng được nêu đầu tiên. Không bao giờ thiết kế thuật toán mã hóa riêng, phát minh giao thức riêng, hay tự tay cài đặt một nguyên thủy từ một bài báo. Mật mã hoạt động trông đơn giản và giấu những chế độ thất bại tinh vi (kênh phụ thời gian, oracle đệm, tính ngẫu nhiên yếu) chỉ sống sót qua nhiều năm rà soát của chuyên gia. Hãy dùng các thư viện đã được thiết lập như mô-đun mật mã chuẩn của nền tảng hay một thư viện được đánh giá cao, và dùng chúng ở mức trừu tượng cao nhất có sẵn. Hãy với tới các chế độ mã hóa có xác thực và các giao diện "dễ" khiến lựa chọn an toàn là mặc định, thay vì tự lắp ráp các mảnh cấp thấp.

### Khớp nguyên thủy với bảo đảm bạn cần

Các công cụ khác nhau cung cấp các bảo đảm khác nhau, và nhầm lẫn chúng là sai lầm phổ biến và nguy hiểm. Hãy học ba họ chính.

- **Mật mã [khóa đối xứng](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)** dùng một khóa bí mật chung để cả mã hóa lẫn giải mã. Nó nhanh và bảo vệ **tính bảo mật**, nhưng cả hai bên phải đã chia sẻ khóa. AES là con ngựa thồ chuẩn.
- **Mật mã [khóa công khai](https://en.wikipedia.org/wiki/Public-key_cryptography)** dùng một cặp khóa liên kết toán học: một khóa công khai mà bất kỳ ai cũng có thể giữ và một khóa riêng bạn giữ bí mật. Nó giải quyết phân phối khóa và cho phép **chữ ký số**, chứng minh **tính xác thực** (ai gửi) và **toàn vẹn** (nó không bị thay đổi).
- Một **[hàm băm mật mã](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** tạo ra một dấu vân tay kích thước cố định của dữ liệu và cung cấp kiểm tra **toàn vẹn**. Băm là một chiều và không phải mã hóa. Để lưu mật khẩu, hãy dùng một hàm băm mật khẩu chậm, có muối, không bao giờ một hàm băm nhanh thông thường (xem chương 4.2 về bảo mật ứng dụng).

Bài học thực tế: mã hóa giấu dữ liệu nhưng không chứng minh ai gửi, và một hàm băm phát hiện can thiệp nhưng không giấu gì. Hầu hết hệ thống thực kết hợp chúng, đúng là lý do bạn nên dựa vào các thư viện gói chúng lại đúng cách.

### Mã hóa khi truyền bằng TLS hiện hành

Hãy bảo vệ mọi bước nhảy mạng bằng [Bảo mật Tầng Vận chuyển](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), giao thức bảo mật dữ liệu khi nó di chuyển giữa các hệ thống. Yêu cầu các phiên bản TLS hiện đại, tắt các phiên bản lỗi thời, chọn bộ mật mã mạnh, và xác thực chứng chỉ đúng cách thay vì tắt kiểm tra để "cho nó chạy." Cũng mã hóa lưu lượng dịch vụ-với-dịch vụ nội bộ, không chỉ rìa công khai, vì tư thế không tin cậy giả định mạng nội bộ là thù địch. Hãy tự động hóa cấp và gia hạn chứng chỉ để TLS là mặc định dễ dàng ở mọi nơi.

### Mã hóa khi lưu bằng mã hóa phong bì

Hãy mã hóa dữ liệu được lưu theo mặc định: cơ sở dữ liệu, lưu trữ đối tượng, bản sao lưu và nhật ký. Mẫu chuẩn là **mã hóa phong bì**, nơi một **khóa mã hóa dữ liệu (DEK)** mã hóa dữ liệu thực, và một **khóa mã hóa khóa (KEK)** do một dịch vụ quản lý khóa nắm giữ mã hóa DEK. Điều này cho phép bạn xoay vòng khóa chủ mà không phải mã hóa lại hàng terabyte dữ liệu, và giữ khóa gốc mạnh bên trong một ranh giới được gia cố. Chỉ lưu DEK đã bọc cạnh dữ liệu, và lấy rồi mở bọc nó lúc sử dụng.

### Vận hành vòng đời khóa có chủ đích

Vòng đời của một khóa là phần thực sự khó của mật mã học, và là nơi hầu hết xâm phạm và sự cố bắt nguồn. Hãy quản lý mọi giai đoạn có chủ đích:

- **Tạo:** tạo khóa từ nguồn ngẫu nhiên mạnh, ở độ mạnh phù hợp.
- **Phân phối:** đưa khóa đến các hệ thống cần chúng mà không phơi bày chúng trong mã, tệp cấu hình hay chat.
- **Xoay vòng:** thay khóa theo lịch, và có thể xoay vòng nhanh khi nghi ngờ bị xâm phạm.
- **Thu hồi:** vô hiệu hóa một khóa hay chứng chỉ bị xâm phạm nhanh chóng, và bảo đảm các hệ thống tôn trọng việc thu hồi.
- **Hủy:** gỡ bỏ an toàn vật liệu khóa cũ để nó không thể khôi phục.

Hãy dùng một **dịch vụ quản lý khóa (KMS)** để tập trung điều này, và dùng một [mô-đun bảo mật phần cứng](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), một thiết bị chống can thiệp tạo và canh giữ khóa để chúng không bao giờ rời đi ở dạng văn bản thuần, cho các khóa bảo đảm cao nhất của bạn. Hãy tách ai có thể quản lý khóa khỏi ai có thể đọc dữ liệu được bảo vệ, để việc giữ khóa thực thi sự tách biệt nhiệm vụ. Điều này liên kết trực tiếp với quy tắc phân loại dữ liệu và giữ khóa trong chương 4.5 (quyền riêng tư và bảo vệ dữ liệu).

### Phân biệt quản lý bí mật với quản lý khóa

Hai thứ chồng lấn nhưng không giống nhau. **Quản lý khóa** điều chỉnh các khóa mật mã và vòng đời của chúng, thường bên trong một KMS hay HSM thực hiện các thao tác mật mã giúp bạn để khóa thô không bao giờ rời đi. **Quản lý bí mật** điều chỉnh thông tin xác thực ứng dụng (mật khẩu cơ sở dữ liệu, token API, chứng chỉ) mà dịch vụ cần lấy và dùng ở dạng văn bản thuần, thường từ một kho bí mật với truy cập sống ngắn, được kiểm toán. Hãy dùng KMS cho khóa, trình quản lý bí mật cho thông tin xác thực, và không bao giờ dán cái nào vào mã nguồn hay tệp môi trường được đưa vào quản lý phiên bản.

### Tự động hóa PKI và vòng đời chứng chỉ

**Hạ tầng khóa công khai (PKI)** là hệ thống các cơ quan chứng thực, chứng chỉ và chuỗi tin cậy gắn khóa công khai với danh tính. Ở quy mô lớn, rủi ro PKI chi phối là việc chứng chỉ hết hạn bất ngờ đánh sập một dịch vụ. Hãy duy trì bản kiểm kê mọi chứng chỉ, giám sát ngày hết hạn, và tự động hóa cấp cùng gia hạn để không con người nào phải nhớ. Chứng chỉ sống ngắn được gia hạn tự động an toàn hơn những cái sống lâu được chăm sóc bằng tay, vì tự động hóa loại bỏ điểm lỗi đơn của con người. Các giao thức chuẩn ở đây hỗ trợ khả năng tương tác qua các nhà cung cấp (chương 3.8 về khả năng tương tác và tiêu chuẩn mở).

### Xây dựng cho tính linh hoạt mật mã và di chuyển hậu lượng tử

Thuật toán suy yếu theo thời gian, và tiêu chuẩn dịch chuyển. **Tính linh hoạt mật mã** nghĩa là thiết kế hệ thống để bạn có thể đổi thuật toán và kích thước khóa mà không phải viết lại đau đớn: trừu tượng hóa mật mã sau một giao diện nhỏ, đánh phiên bản dữ liệu được mã hóa của bạn để biết thuật toán nào tạo ra nó, và giữ bản kiểm kê mật mã về những gì bạn dùng ở đâu. Điều này quan trọng bây giờ vì [mật mã hậu lượng tử](https://en.wikipedia.org/wiki/Post-quantum_cryptography), họ thuật toán mới được thiết kế để chống chịu máy tính lượng tử tương lai. Kẻ thù có thể thu hoạch dữ liệu mã hóa hôm nay để giải mã sau, nên các bí mật sống lâu cần một kế hoạch di chuyển. Bạn không cần hoảng loạn, nhưng bạn nên biết bản kiểm kê của mình và sẵn sàng áp dụng các thuật toán hậu lượng tử được chuẩn hóa khi các nền tảng phát hành chúng.

### Ưu tiên các cài đặt đã xác nhận ở nơi được yêu cầu

Với các hệ thống chịu quy định và chính phủ, dùng một thuật toán mạnh là chưa đủ; cài đặt phải được xác nhận. **FIPS 140** (Tiêu chuẩn Xử lý Thông tin Liên bang 140) là tiêu chuẩn Hoa Kỳ để xác nhận các mô-đun mật mã, và nhiều hợp đồng yêu cầu mật mã được xác nhận FIPS. Công việc chính phủ cũng có thể theo hướng dẫn quốc gia như bộ Thuật toán An ninh Quốc gia Thương mại (CNSA) của NSA cho các hệ thống mật. Hãy kiểm tra chế độ nào áp dụng trước khi bạn xây, vì trang bị bổ sung các mô-đun đã xác nhận muộn thì tốn kém. Điều này gắn với bằng chứng tuân thủ và quản trị (chương 4.6).

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| KMS do nhà cung cấp quản lý | Dễ, tích hợp, gánh nặng vận hành thấp | Nhà cung cấp giữ khóa; ít kiểm soát trực tiếp hơn |
| Khóa do khách hàng quản lý / HSM | Giữ khóa đầy đủ, đáp ứng yêu cầu nghiêm ngặt | Chi phí vận hành, rủi ro mất khóa |
| Chứng chỉ sống ngắn tự động | Không hết hạn bất ngờ, thu hồi nhanh | Cần đầu tư tự động hóa trước |
| Chứng chỉ sống lâu | Đơn giản, ít bộ phận chuyển động | Hết hạn do con người quản lý gây sự cố |
| Mã hóa phong bì | Xoay vòng khóa rẻ, bảo vệ khóa chủ | Nhiều bộ phận chuyển động hơn để hiểu |
| Tính linh hoạt mật mã từ đầu | Di chuyển tương lai rẻ | Thêm trừu tượng và công sức thiết kế bây giờ |
| Áp dụng hậu lượng tử sớm | Bảo vệ bí mật sống lâu | Công cụ chưa trưởng thành, khóa lớn hơn, một số rủi ro |

Căng thẳng trung tâm là kiểm soát so với gánh nặng vận hành. Tự giữ khóa trong HSM cho bạn quyền giữ khóa tối đa và thỏa mãn các yêu cầu nghiêm ngặt nhất, nhưng nó đòi hỏi chuyên môn và tạo ra một rủi ro thảm khốc mới: mất khóa là mất dữ liệu, không thể khôi phục. Các dịch vụ do nhà cung cấp quản lý gỡ bỏ gánh nặng đó nhưng đặt quyền giữ khóa với nhà cung cấp. Hãy giải quyết bằng cách xếp tầng: dùng các dịch vụ được quản lý với mặc định hợp lý cho hầu hết hệ thống, và dành khóa do khách hàng quản lý cùng HSM cho dữ liệu phân loại cao nhất nơi sự kiểm soát thêm đáng với chi phí và rủi ro.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn có bản kiểm kê đầy đủ các khóa, chứng chỉ và thuật toán bạn dựa vào không?** Bạn không thể xoay vòng, di chuyển hay kiểm toán những gì bạn không thấy, và hầu hết các tổ chức phát hiện họ có vật liệu mật mã rải rác qua các dịch vụ nhiều hơn hẳn bất kỳ ai theo dõi. Một bản kiểm kê là điều kiện tiên quyết cho mọi quyết định sau: giám sát hết hạn chứng chỉ, xoay vòng khóa, xác định phạm vi FIPS và hoạch định hậu lượng tử đều phụ thuộc vào nó. Hãy mang danh sách các chứng chỉ hiện tại và ngày hết hạn của chúng, và hỏi ai sở hữu từng cái và cái gì hỏng khi nó lỡ hạn. Với một hệ sinh thái lớn, câu trả lời trung thực thường là không có nguồn sự thật duy nhất nào tồn tại, và xây một cái là bước đầu có đòn bẩy cao nhất. Nếu bạn không liệt kê được mật mã của mình hôm nay, tính linh hoạt và xoay vòng là khát vọng, không phải năng lực.

2. **Bạn có thể xoay vòng hay thu hồi một khóa bị xâm phạm nhanh không, và bạn đã từng thực hành chưa?** Xoay vòng và thu hồi là những phần của vòng đời khóa chỉ quan trọng dưới áp lực, và các đội thường xuyên phát hiện trong một sự cố rằng một khóa được mã hóa cứng ở cả chục nơi hoặc việc thu hồi thực sự không lan truyền. Hãy quyết định thời gian mục tiêu của bạn để xoay vòng một khóa và thu hồi một chứng chỉ, rồi diễn tập nó trước khi bạn cần. Hãy mang câu chuyện về lần phơi bày thông tin xác thực gần nhất của bạn và đi qua điều xoay vòng đòi hỏi trong thực tế. Với các hệ thống doanh nghiệp và chính phủ, một lần xoay vòng chưa diễn tập có thể nghĩa là chọn giữa phơi nhiễm kéo dài và sự cố tự gây ra. Nếu xoay vòng chưa bao giờ được kiểm thử, hãy giả định nó không hoạt động.

3. **Việc giữ khóa nằm ở đâu, và nó có thực thi sự tách biệt nhiệm vụ không?** Ai có thể quản lý một khóa và ai có thể đọc dữ liệu nó bảo vệ không nên là cùng một người, vì gộp những quyền đó lặng lẽ phá hỏng mục đích của mã hóa khi lưu. Lựa chọn này cũng quyết định bạn dùng khóa do nhà cung cấp quản lý, khóa do khách hàng quản lý, hay HSM, mỗi loại có kiểm soát khác nhau và rủi ro vận hành khác nhau. Hãy mang các chính sách khóa hiện tại và kiểm tra xem có danh tính đơn lẻ nào vừa quản trị một khóa vừa truy cập văn bản thuần đằng sau nó không, một khoảng trống im lặng phổ biến. Với dữ liệu chịu quy định và mật, quy tắc giữ khóa có thể bị quyết định bởi phân loại dữ liệu (chương 4.5) và bởi yêu cầu bắt buộc. Nếu việc giữ khóa và truy cập không được tách, mã hóa của bạn đang bảo vệ bạn ít hơn bảng điều khiển gợi ý.

4. **Bạn sẽ khôi phục thế nào nếu khóa chủ bảo vệ mã hóa phong bì của bạn bị mất hay bị hủy?** Khóa do khách hàng quản lý và HSM cho bạn quyền giữ khóa, nhưng chúng trao cho bạn một chế độ thất bại thảm khốc mới: mất khóa mã hóa khóa và mọi khóa mã hóa dữ liệu nó bọc trở nên không đọc được vĩnh viễn, cùng với dữ liệu đằng sau chúng. Hãy cân nhắc điều này đối lập với rủi ro đối nghịch của một bản sao lưu quá rộng lặng lẽ tái tạo chính vấn đề giữ khóa bạn đang cố giải quyết. Hãy mang các thỏa thuận sao lưu và ký quỹ khóa hiện tại của bạn, bán kính ảnh hưởng của mỗi khóa chủ, và bằng chứng rằng một lần khôi phục đã thực sự được thực hiện thay vì chỉ được lập tài liệu. Với các hệ sinh thái doanh nghiệp và chính phủ, hãy gắn điều này với quy tắc phân loại dữ liệu của bạn: các khóa nhạy cảm nhất thường cấm các bản sao tùy tiện, nên khôi phục phải được thiết kế có chủ đích, kiểm thử theo lịch, và dung hòa với bất kỳ yêu cầu quy định nào về chứng minh rằng vật liệu khóa đã gỡ bỏ bị hủy.

5. **Hệ thống của bạn sẵn sàng đến đâu cho một cuộc di chuyển hậu lượng tử, và bí mật sống lâu nào bạn sẽ di chuyển đầu tiên?** Kẻ thù có thể thu hoạch lưu lượng và kho lưu trữ mã hóa hôm nay và giải mã chúng khi máy tính lượng tử trưởng thành, nên bất kỳ bí mật nào phải giữ bảo mật nhiều năm đã bị phơi bày với một tương lai bạn không thấy. Áp lực cạnh tranh là công cụ hậu lượng tử còn non, khóa lớn hơn, và di chuyển quá sớm mạo hiểm đặt cược vào một thuật toán thay đổi trước khi nó ổn định. Hãy mang bản kiểm kê mật mã của bạn, danh sách bí mật được xếp hạng theo thời gian chúng phải giữ bảo mật, và một đánh giá trung thực về việc kiến trúc của bạn có thể đổi thuật toán mà không viết lại không. Với công việc chính phủ và chịu quy định, các hồ sơ có yêu cầu bảo mật nhiều thập kỷ khiến điều này cụ thể thay vì lý thuyết, và mua sắm có thể sớm yêu cầu một kế hoạch di chuyển có tài liệu cùng hỗ trợ cho các thuật toán hậu lượng tử được chuẩn hóa.

6. **Khi quy định yêu cầu mật mã được xác nhận, bạn có biết chính xác mô-đun nào thuộc phạm vi và chúng có đủ điều kiện không?** Dùng một thuật toán mạnh không giống với dùng một cài đặt được xác nhận, và các đội thường xuyên phát hiện muộn rằng một thư viện, một môi trường chạy ngôn ngữ, hay một dịch vụ đám mây không nằm trong ranh giới FIPS 140 mà một hợp đồng đòi hỏi. Căng thẳng là các mô-đun được xác nhận có thể tụt hậu so với thư viện hiện hành về tính năng và tốc độ, nên chọn chúng ràng buộc ngăn xếp của bạn theo cách quan trọng cho kỹ thuật. Hãy mang danh sách các mô-đun mật mã mà mỗi hệ thống chịu quy định thực sự gọi, các chứng chỉ xác nhận bao quát chúng, và yêu cầu bắt buộc cụ thể (FIPS 140, CNSA, hay quy tắc ngành) áp dụng. Với các chương trình doanh nghiệp và chính phủ, hãy quyết định điều này trước khi bạn xây, vì trang bị bổ sung các mô-đun đã xác nhận và cấp phép lại một hệ thống sau sự việc là tốn kém, chậm, và thường buộc phải thiết kế lại chính các thành phần bạn tưởng đã xong.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy hoàn toàn dựa vào mặc định đã thẩm định của nền tảng và dành không thời gian kỹ thuật nào cho mật mã tùy chỉnh. Bật mã hóa khi lưu được quản lý, kết thúc TLS với chứng chỉ gia hạn tự động, băm mật khẩu bằng hàm chậm chuẩn, và giữ bí mật trong trình quản lý bí mật của nền tảng thay vì kho mã. Quyết định thiết kế duy nhất của bạn là một giao diện mỏng quanh nhúm trường bạn mã hóa trong ứng dụng, để một lần chuyển khỏi khóa do nhà cung cấp quản lý sau này không phải viết lại.

**Doanh nghiệp nhỏ.** Bạn không có nhà mật mã học và ít hứng thú vận hành HSM, vì vậy hãy mua việc giữ khóa thay vì xây nó: dùng KMS và trình quản lý bí mật do nhà cung cấp quản lý đi kèm đám mây hay công cụ SaaS của bạn. Hãy đóng khung công việc là vệ sinh, tức là không khóa trong mã, mã hóa bật ở mọi nơi theo mặc định, và ngày hết hạn chứng chỉ được giám sát để không gì lỡ hạn bất ngờ. Dành khóa do khách hàng quản lý cho dữ liệu hiếm mà hợp đồng hay cơ quan quản lý thực sự đòi hỏi chúng.

**Doanh nghiệp lớn.** Vấn đề là quy mô và sự nhất quán qua hàng nghìn dịch vụ, chứng chỉ và khóa. Hãy chạy một KMS tập trung với mã hóa phong bì, tự động hóa toàn bộ vòng đời chứng chỉ để không ngày hết hạn nào được chăm sóc bằng tay, và duy trì một bản kiểm kê mật mã duy nhất nuôi xoay vòng, xác định phạm vi FIPS và hoạch định hậu lượng tử. Hãy tách việc giữ khóa khỏi truy cập dữ liệu như một biện pháp kiểm soát toàn tổ chức, và biến mã hóa thành năng lực nền tảng mà mọi đội thừa hưởng thay vì nhiệm vụ mỗi đội phát minh lại.

**Chính phủ.** Mua sắm, xác nhận và kiểm toán định hình mọi lựa chọn. Hãy dùng các mô-đun được xác nhận FIPS 140 và theo hướng dẫn quốc gia như CNSA cho các hệ thống mật, gắn việc giữ khóa với phân loại dữ liệu để các khóa nhạy cảm nhất nằm với nhân sự được thẩm tra dưới sự tách biệt nhiệm vụ nghiêm ngặt, và tạo bằng chứng liên tục về mật mã được xác nhận cho sự cấp phép liên tục. Hãy lập tài liệu một kế hoạch di chuyển hậu lượng tử cho các hồ sơ phải giữ bảo mật hàng thập kỷ, và yêu cầu nhà cung cấp công khai mô-đun nào được xác nhận trước khi bạn cam kết.

## Ví dụ

**Công ty khởi nghiệp.** Một đội nhỏ xây ứng dụng theo dõi sức khỏe hoàn toàn dựa vào mặc định đã thẩm định. Họ kết thúc TLS với chứng chỉ gia hạn tự động, bật mã hóa khi lưu trên cơ sở dữ liệu và lưu trữ đối tượng được quản lý bằng KMS của nhà cung cấp, và băm mật khẩu bằng hàm chậm, có muối từ thư viện chuẩn. Thay vì tự viết bất kỳ mật mã nào, họ dùng một lệnh gọi mã hóa có xác thực cấp cao cho trường duy nhất họ phải mã hóa trong ứng dụng. Bí mật sống trong trình quản lý bí mật của nền tảng, không bao giờ trong kho mã. Nó tốn vài buổi chiều và loại bỏ cả một loại sai lầm thảm khốc.

**Doanh nghiệp lớn.** Một ngân hàng toàn cầu chạy một KMS tập trung và một đội HSM, với bản kiểm kê mật mã theo dõi mọi khóa và chứng chỉ qua hàng nghìn dịch vụ. Mã hóa phong bì bảo vệ dữ liệu khách hàng, với khóa dữ liệu được bọc bởi khóa chủ xoay vòng theo lịch trong khi dữ liệu giữ nguyên. Cấp và gia hạn chứng chỉ được tự động hóa hoàn toàn sau khi một sự cố hướng công chúng dạy họ chi phí của một chứng chỉ hết hạn đơn lẻ. Quản trị viên khóa là đội riêng với kỹ sư ứng dụng, nên việc giữ khóa thực thi tách biệt nhiệm vụ, và một tầng linh hoạt mật mã cho phép họ bắt đầu thí điểm các thuật toán hậu lượng tử cho kho lưu trữ sống lâu.

**Chính phủ.** Một cơ quan quốc gia xử lý hồ sơ mật chỉ dùng các mô-đun mật mã được xác nhận FIPS 140 và theo hướng dẫn CNSA của NSA cho các hệ thống phân loại cao nhất. Khóa được tạo và giữ trong HSM không bao giờ phát hành vật liệu khóa văn bản thuần, và việc giữ khóa được gắn với phân loại dữ liệu để các khóa nhạy cảm nhất nằm với nhân sự được thẩm tra dưới sự tách biệt nhiệm vụ nghiêm ngặt. Chứng chỉ chạy trên một PKI nội bộ được quản lý với vòng đời tự động, và bằng chứng liên tục về mật mã được xác nhận nuôi sự cấp phép liên tục của cơ quan. Một kế hoạch di chuyển hậu lượng tử có tài liệu bảo vệ các hồ sơ phải giữ bảo mật hàng thập kỷ.

## Luận chứng kinh doanh: động lực, ROI và TCO

Mật mã học là một lĩnh vực nữa nơi một khoản đầu tư khiêm tốn ngăn chặn các tổn thất thảm khốc, cỡ tiêu đề báo. Tổng chi phí sở hữu bao gồm KMS hay HSM, công cụ quản lý bí mật và chứng chỉ, và thời gian kỹ thuật để thiết kế vòng đời và giữ bản kiểm kê hiện hành. Những chi phí này là thật nhưng có giới hạn. Chi phí của việc bỏ qua là một vụ xâm phạm dữ liệu không mã hóa, một sự cố nhiều giờ do chứng chỉ hết hạn, hay mất dữ liệu không thể khôi phục do xử lý sai một khóa, mỗi cái mang tiền phạt quy định, chi phí thông báo và thiệt hại danh tiếng lâu dài.

ROI mạnh nhất đến từ tự động hóa và tái sử dụng. Vòng đời chứng chỉ tự động loại bỏ sự cố tự gây ra phổ biến nhất. Quản lý khóa tập trung với mặc định hợp lý nghĩa là mọi dịch vụ mới thừa hưởng mã hóa khi truyền và khi lưu mà không cần công sức theo từng đội, biến mật mã học từ một khoản thuế lặp lại thành một năng lực nền tảng. Với công việc chịu quy định và chính phủ, các mô-đun được xác nhận và bằng chứng tự động cũng hạ chi phí kiểm toán và cấp phép. Khi bạn trình bày lập luận với ban lãnh đạo, hãy đóng khung nó thẳng thắn: thuật toán miễn phí và đã được chứng minh, rủi ro sống trong quản lý khóa và vận hành chứng chỉ, và một khoản đầu tư nhỏ, tự động ở đó ngăn các thất bại đắt đỏ.

## Phản mẫu và cạm bẫy

- **Tự viết mật mã.** Thuật toán tùy chỉnh hay giao thức tự xây thất bại theo cách tinh vi, chỉ chuyên gia thấy.
- **Khóa và bí mật được mã hóa cứng.** Thông tin xác thực dán vào mã nguồn, tệp cấu hình hay chat, nơi chúng rò rỉ và không thể xoay vòng.
- **Mã hóa không có kỷ luật khóa.** Bật mã hóa nhưng để quyền truy cập khóa mở rộng hoặc không bao giờ xoay vòng.
- **Nhầm băm với mã hóa.** Coi một hàm băm là đảo ngược được, hoặc lưu mật khẩu bằng hàm băm nhanh thay vì hàm chậm, có muối.
- **Roulette chứng chỉ.** Không kiểm kê, không giám sát hết hạn, và các sự cố bất ngờ định kỳ khi một chứng chỉ lỡ hạn.
- **Gộp việc giữ khóa và truy cập dữ liệu.** Một danh tính vừa quản lý một khóa vừa đọc dữ liệu nó bảo vệ.
- **Không có kế hoạch xoay vòng.** Khóa chưa bao giờ được xoay vòng và không thể xoay vòng nhanh dưới áp lực.
- **Mật mã không linh hoạt.** Thuật toán được đi dây sâu đến mức đổi chúng đòi hỏi viết lại, chặn mọi cuộc di chuyển tương lai.
- **Bỏ qua yêu cầu xác nhận.** Dùng thuật toán mạnh trong các mô-đun chưa xác nhận nơi FIPS hay xác nhận tương tự được yêu cầu.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Mã hóa không nhất quán và thường vắng mặt, áp dụng phản ứng khi ai đó nhận ra khoảng trống. Khóa và bí mật được mã hóa cứng hoặc chia sẻ không chính thức qua chat và tệp cấu hình. Không có kiểm kê, không xoay vòng, và chứng chỉ hết hạn bất ngờ, và các đội thỉnh thoảng tự viết mật mã.
- **Mức 2, Phát triển:** TLS và mã hóa khi lưu được bật cho các hệ thống chính, và một KMS hay trình quản lý bí mật tồn tại, nhưng việc áp dụng không đều và khác nhau theo đội. Một số chứng chỉ được giám sát trong khi số khác không, xoay vòng là thủ công và hiếm, và không có bản kiểm kê mật mã hoàn chỉnh gắn kết tất cả.
- **Mức 3, Chuẩn hóa:** Mã hóa khi truyền và khi lưu là mặc định được lập tài liệu và thực thi toàn tổ chức. Khóa sống trong một KMS với xoay vòng theo lịch và mã hóa phong bì, việc giữ khóa tách biệt khỏi truy cập dữ liệu, vòng đời chứng chỉ được tự động hóa, một bản kiểm kê mật mã được duy trì, và các mô-đun được xác nhận được dùng ở bất cứ nơi nào quy định yêu cầu.
- **Mức 4, Quản lý:** Hệ sinh thái mật mã được đo và kiểm soát theo các đường cơ sở. Bạn theo dõi thời gian dẫn trước hết hạn chứng chỉ, phần trăm khóa được xoay vòng đúng lịch, thời gian trung bình để thu hồi một khóa bị xâm phạm, số lần phát hiện bí mật-trong-mã mỗi kỳ, và độ bao phủ kiểm kê, và rà soát các chỉ số này theo mục tiêu. Xoay vòng và thu hồi được diễn tập theo nhịp với thời gian được ghi lại, và sai lệch kích hoạt hành động khắc phục thay vì không được để ý.
- **Mức 5, Điều phối:** Mật mã học là năng lực nền tảng mà mọi dịch vụ thừa hưởng theo mặc định, và nó được cải thiện liên tục và tích hợp trong toàn tổ chức. Xoay vòng và thu hồi nhanh và được thực hành thường xuyên, HSM bảo vệ các khóa bảo đảm cao nhất, và tính linh hoạt mật mã cùng một kế hoạch di chuyển hậu lượng tử đang hoạt động giữ hệ sinh thái thích ứng khi thuật toán và yêu cầu bắt buộc dịch chuyển. Bằng chứng tuân thủ được tạo tự động và nuôi sự cấp phép liên tục.

## Ý tưởng để thảo luận

1. Hệ thống nào trong hệ sinh thái của bạn biện minh cho khóa do khách hàng quản lý hay HSM xét chi phí vận hành và rủi ro mất mát thảm khốc của chúng?
2. Bạn sẽ xây và duy trì một nguồn sự thật duy nhất cho mọi khóa và chứng chỉ bạn sở hữu thế nào?
3. Thời gian thực tế của bạn để xoay vòng một khóa bị xâm phạm hôm nay là bao nhiêu, và điều gì làm nó chậm?
4. Kiến trúc của bạn làm việc đổi một thuật toán mật mã khó ở đâu, và bạn sẽ sửa điều đó thế nào trước một cuộc di chuyển bị ép buộc?
5. Bí mật sống lâu nào của bạn sẽ quan trọng nếu một kẻ thù thu hoạch chúng bây giờ và giải mã nhiều năm sau?
6. Bí mật và khóa có bao giờ lọt vào mã, cấu hình hay nhật ký không, và làm sao bạn biết?

## Những điểm cần ghi nhớ

- **Đừng tự viết mật mã.** Dùng các thư viện đã thẩm định và thuật toán chuẩn ở mức trừu tượng an toàn cao nhất.
- **Thuật toán dễ; quản lý khóa khó.** Vòng đời của một khóa (tạo, phân phối, xoay vòng, thu hồi, hủy) là nơi thất bại thực tế sống.
- **Biết các bảo đảm của bạn:** mã hóa đối xứng và khóa công khai bảo vệ tính bảo mật, chữ ký chứng minh tính xác thực và toàn vẹn, và băm phát hiện can thiệp nhưng không phải mã hóa.
- **Mã hóa khi truyền bằng TLS hiện hành và khi lưu bằng mã hóa phong bì**, như mặc định cho mọi hệ thống.
- **Tách việc giữ khóa khỏi truy cập dữ liệu**, dùng KMS cho khóa và trình quản lý bí mật cho thông tin xác thực, và không bao giờ mã hóa cứng cái nào.
- **Tự động hóa vòng đời chứng chỉ** để diệt sự cố hết hạn bất ngờ, và giữ một bản kiểm kê mật mã.
- **Xây cho tính linh hoạt mật mã** và bắt đầu một kế hoạch di chuyển hậu lượng tử cho bí mật sống lâu.
- **Ưu tiên các cài đặt đã xác nhận** (FIPS 140 và hướng dẫn quốc gia áp dụng) ở nơi quy định hay phân loại yêu cầu.

## Tài liệu tham khảo và đọc thêm

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, các tiêu chuẩn mật mã hậu lượng tử (FIPS 203, 204 và 205).
- Niels Ferguson, Bruce Schneier và Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* và *Transport Layer Protection Cheat Sheet*.
- National Security Agency, hướng dẫn bộ *Commercial National Security Algorithm (CNSA) Suite*.
