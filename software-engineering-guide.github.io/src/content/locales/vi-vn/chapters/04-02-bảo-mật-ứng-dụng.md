# 4.2 Bảo mật ứng dụng

## Tổng quan và động lực

Bảo mật ứng dụng là nơi các mối đe dọa trừu tượng gặp mã cụ thể. Hầu hết các vụ xâm phạm lên tiêu đề báo đều truy về một lỗi ở tầng ứng dụng: một lần chèn mã, một luồng xác thực hỏng, một bí mật bị phơi bày, hay một phụ thuộc bị xâm phạm. Với các đội lớn phát hành nhiều dịch vụ, phần khó không phải là biết những lỗi này tồn tại. Mà là ngăn chúng một cách nhất quán qua một cơ sở mã trải rộng do hàng nghìn bàn tay viết qua nhiều năm.

Với doanh nghiệp, bảo mật ứng dụng là vấn đề niềm tin của khách hàng và nghĩa vụ quy định. Một lỗi trong luồng đăng nhập hay đường thanh toán có thể kích hoạt gian lận, tiền phạt và công bố xâm phạm bắt buộc. Hệ thống chính phủ đối mặt cùng rủi ro kỹ thuật với dữ liệu có rủi ro cao hơn: tư cách hưởng trợ cấp, hồ sơ thuế, dữ liệu tư pháp hình sự và hạ tầng quốc gia. Trong cả hai bối cảnh, ứng dụng là cửa trước, và kẻ tấn công dò xét nó liên tục và tự động.

Chương này bao quát các thực hành giữ cho ứng dụng có khả năng chống chịu: biết và phòng thủ các lớp lỗ hổng phổ biến, xác thực đầu vào và mã hóa đầu ra, làm đúng xác thực và cấp quyền, quản lý bí mật, và bảo mật chuỗi cung ứng phần mềm vốn ngày càng quyết định bề mặt tấn công thực của bạn.

*Xem thêm:* chương 4.1 (nền tảng bảo mật, mô hình hóa mối đe dọa và vòng đời phát triển an toàn), chương 10.3 (chuỗi cung ứng mã nguồn mở và giấy phép), và chương 10.2 (SBOM, rủi ro và bảo đảm).

## Các nguyên tắc chính

- **Không bao giờ tin đầu vào.** Coi mọi dữ liệu băng qua ranh giới tin cậy là thù địch cho đến khi được xác thực.
- **Mặc định an toàn.** Con đường an toàn nên là con đường dễ; hành vi không an toàn nên đòi hỏi nỗ lực có chủ đích, hiển thị.
- **Thất bại theo hướng đóng.** Khi một kiểm tra bảo mật không thể hoàn tất, hãy từ chối truy cập thay vì cho phép.
- **Phòng thủ theo chiều sâu ở tầng ứng dụng.** Kết hợp xác thực, mã hóa, tham số hóa và bảo vệ của khung phát triển; đừng dựa vào một cái.
- **Đặc quyền tối thiểu cho danh tính và token.** Giới hạn thông tin xác thực hẹp và cho chúng hết hạn nhanh.
- **Các phụ thuộc của bạn là mã của bạn.** Bạn chịu trách nhiệm về tính bảo mật của mọi thứ bạn phát hành, bao gồm các thành phần bên thứ ba và mã nguồn mở.
- **Tiêu chuẩn hơn ứng biến.** Dùng các khung đã được thẩm định như ASVS của [OWASP](https://en.wikipedia.org/wiki/OWASP) (Dự án Bảo mật Ứng dụng Mở Toàn cầu) thay vì tự phát minh biện pháp kiểm soát bảo mật.

## Khuyến nghị

### Biết và phòng thủ OWASP Top 10, xác minh bằng ASVS

OWASP Top 10 là danh sách đường cơ sở của ngành về các rủi ro quan trọng nhất của ứng dụng web: kiểm soát truy cập hỏng, thất bại mật mã, chèn mã, thiết kế không an toàn, cấu hình bảo mật sai, thành phần có lỗ hổng, thất bại xác thực, thất bại toàn vẹn dữ liệu, thất bại ghi nhật ký, và giả mạo yêu cầu phía máy chủ. Hãy coi nó là kiến thức bắt buộc cho mọi kỹ sư, không chỉ là tài liệu tham khảo tuân thủ để cất đi.

Để có một tiêu chuẩn chặt chẽ, kiểm thử được, hãy áp dụng **Tiêu chuẩn Xác minh Bảo mật Ứng dụng OWASP (ASVS)**. ASVS định nghĩa các yêu cầu bảo mật ở ba mức bảo đảm, cho bạn các biện pháp kiểm soát cụ thể, kiểm toán được để thiết kế và kiểm thử đối chiếu. Hãy chọn mức phù hợp với rủi ro của từng ứng dụng, và xác minh theo nó.

### Xác thực đầu vào và mã hóa đầu ra

Lỗi chèn mã vẫn nằm trong số những lỗi gây hại nhất chính vì chúng quá dễ đưa vào. Hãy phòng thủ bằng các biện pháp kiểm soát nhiều tầng:

- **Xác thực đầu vào** đối chiếu với danh sách cho phép chặt chẽ (kiểu, độ dài, định dạng, phạm vi kỳ vọng). Từ chối thay vì làm sạch ở nơi bạn có thể.
- **Dùng truy vấn tham số hóa** và [câu lệnh chuẩn bị sẵn](https://en.wikipedia.org/wiki/Prepared_statement) cho mọi truy cập cơ sở dữ liệu; không bao giờ dựng SQL bằng nối chuỗi. Dùng đúng các bộ dựng truy vấn an toàn và ORM (ánh xạ đối tượng-quan hệ).
- **Mã hóa đầu ra** theo ngữ cảnh. HTML, thuộc tính HTML, JavaScript, URL và CSS mỗi loại đòi hỏi mã hóa khác nhau. Dựa vào tự động thoát của khung phát triển và hiểu giới hạn của nó.
- **Ngăn [tấn công kịch bản chéo trang](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** bằng mã hóa đầu ra cộng một Chính sách Bảo mật Nội dung mạnh làm tầng thứ hai.
- **Ngăn chèn lệnh và chèn mẫu** bằng cách tránh gọi shell với dữ liệu không đáng tin và dùng các mẫu không logic hoặc có sandbox.

### Làm đúng xác thực và cấp quyền

Xác thực chứng minh một người dùng là ai. Cấp quyền quyết định họ được làm gì. Cả hai đều thất bại thường xuyên, vì vậy hãy làm cho đúng.

- Ưu tiên các giao thức đã được thiết lập: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** cho cấp quyền ủy thác và **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** cho xác thực. Đừng xây những thứ này từ đầu.
- Thực thi **[xác thực đa yếu tố](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, đặc biệt cho truy cập đặc quyền và quản trị.
- Chỉ lưu mật khẩu dưới dạng băm có muối dùng một thuật toán hiện đại, chậm, tốn bộ nhớ (như [Argon2](https://en.wikipedia.org/wiki/Argon2) hay [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Không bao giờ lưu hay ghi nhật ký thông tin xác thực dạng văn bản thuần.
- Quản lý **phiên** cẩn thận: tạo token mạnh về mật mã, đặt cờ cookie secure và HttpOnly, xoay vòng khi đổi đặc quyền, và cho phiên nhàn rỗi hết hạn.
- Thực thi **cấp quyền ở máy chủ cho mọi yêu cầu**, kiểm tra rằng chủ thể đã xác thực sở hữu hoặc được truy cập tài nguyên cụ thể. Cấp quyền mức đối tượng hỏng (truy cập bản ghi của người dùng khác bằng cách đổi một ID) là một trong những lỗi API phổ biến và nghiêm trọng nhất.
- Tập trung logic cấp quyền ở nơi thực tế để chính sách nhất quán và kiểm toán được.

### Quản lý bí mật và xoay vòng khóa

Bí mật được mã hóa cứng trong mã nguồn là nguyên nhân lâu năm của các vụ xâm phạm. Hãy xây một thói quen có kỷ luật quanh quản lý bí mật:

- Lưu bí mật trong một trình quản lý bí mật hoặc kho chuyên dụng, không bao giờ trong mã nguồn, tệp cấu hình, hay biến môi trường được đưa vào quản lý phiên bản.
- Tự động quét commit và kho tìm bí mật bị rò rỉ, và chặn các lần hợp nhất đưa chúng vào.
- Xoay vòng khóa và thông tin xác thực đều đặn và ngay lập tức khi nghi ngờ bị phơi bày. Ưu tiên thông tin xác thực sống ngắn, được cấp tự động hơn các thông tin tĩnh sống lâu.
- Áp dụng đặc quyền tối thiểu cho mọi bí mật: giới hạn nó vào đúng thứ nó cần.
- Mã hóa bí mật khi lưu và khi truyền, và kiểm toán việc truy cập chúng.

### Bảo mật chuỗi cung ứng phần mềm

Các ứng dụng hiện đại chủ yếu được lắp ráp từ thành phần bên thứ ba, khiến chuỗi cung ứng thành bề mặt tấn công chính.

- Duy trì một **[Danh mục Vật liệu Phần mềm](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** cho mọi ứng dụng để bạn biết chính xác mình phát hành gì và có thể phản ứng nhanh khi một lỗ hổng mới xuất hiện.
- Liên tục quét phụ thuộc (Phân tích Thành phần Phần mềm, hay SCA) và khắc phục kịp thời các thành phần có lỗ hổng đã biết.
- Ghim và xác minh phiên bản phụ thuộc; dùng tệp khóa và kho đăng ký đáng tin.
- Áp dụng **SLSA** (Các Mức Chuỗi cung ứng cho Sản phẩm Phần mềm) để nâng tính toàn vẹn bản dựng, và tạo các chứng thực **nguồn gốc** mô tả cách các sản phẩm được dựng.
- **Ký các sản phẩm** và xác minh chữ ký trước khi triển khai để bạn tin rằng thứ chạy là thứ bạn đã dựng.
- Bảo mật chính hệ thống dựng; một đường ống CI bị xâm phạm có thể tiêm mã độc vào mọi bên tiêu thụ hạ nguồn.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Mua/áp dụng nhà cung cấp danh tính (OIDC) | Đã qua thử thách, tích hợp MFA, ít mã cần bảo mật hơn | Phụ thuộc nhà cung cấp, công sức tích hợp, chi phí |
| Tự xây xác thực | Kiểm soát toàn bộ, không phụ thuộc bên ngoài | Cực kỳ dễ làm sai, bảo trì cao |
| Xác thực danh sách cho phép chặt chẽ | Chặn cả lớp lỗ hổng | Có thể làm hỏng các trường hợp biên chính đáng, nhiều việc ban đầu hơn |
| Thông tin xác thực sống ngắn | Cửa sổ xâm phạm nhỏ, tự động thu hồi | Đòi hỏi hạ tầng cấp phát vững |
| Cập nhật phụ thuộc quyết liệt | Ít lỗ hổng đã biết hơn | Xáo động, thay đổi phá vỡ tiềm tàng, gánh nặng kiểm thử |
| SBOM + ký + nguồn gốc | Ứng phó sự cố nhanh, niềm tin xác minh được | Đầu tư công cụ và quy trình, thay đổi văn hóa |

Đánh đổi lặp lại là sự chặt chẽ ban đầu so với phơi nhiễm liên tục. Tự xây xác thực hoặc bỏ qua vệ sinh phụ thuộc cảm thấy nhanh hơn hôm nay và tốn của bạn khủng khiếp sau này. Áp dụng các tiêu chuẩn đã thẩm định và kiểm soát chuỗi cung ứng tự động tốn công sức bây giờ, nhưng biến một rủi ro không giới hạn, không thể đoán trước thành một rủi ro được quản lý, có giới hạn. Với các đội lớn, hệ số nhân từ tự động hóa quan trọng nhất: một biện pháp kiểm soát được áp dụng một lần trong mẫu đường lát sẵn bảo vệ mọi dịch vụ dùng nó.

## Câu hỏi để thảo luận với đội của bạn

1. **Những biện pháp kiểm soát ASVS nào bạn sẽ nướng vào khung đường lát sẵn để kỹ sư nhận được miễn phí?** Nước đi có đòn bẩy cao nhất cho một đội lớn là làm cho con đường an toàn thành mặc định, để một biện pháp kiểm soát được viết một lần trong khung dùng chung bảo vệ mọi dịch vụ áp dụng nó. Hãy quyết định yêu cầu ASVS nào (truy vấn tham số hóa, mã hóa đầu ra, cờ phiên an toàn, kiểm tra cấp quyền phía máy chủ) thuộc về mẫu thay vì trí nhớ của từng kỹ sư. Với danh mục doanh nghiệp và chính phủ, cũng hãy quyết định ứng dụng nào cần ASVS Mức 2 so với Mức 3, và gắn điều đó với độ nhạy cảm của dữ liệu mỗi cái chạm vào. Hãy mang danh sách các dịch vụ của bạn và đánh dấu cái nào đã thừa hưởng các mặc định này và cái nào cài đặt lại bảo mật bằng tay, vì những cái làm tay là nơi chèn mã và kiểm soát truy cập hỏng ẩn nấp. Nếu mặc định an toàn chỉ sống trong một trang wiki, chúng sẽ bị bỏ qua dưới áp lực phân phối, vì vậy hãy đặt chúng vào mã.

2. **Làm thế nào bạn sẽ tìm và sửa cấp quyền mức đối tượng hỏng trên mọi API, không chỉ các API mới?** Truy cập bản ghi của người dùng khác bằng cách đổi một ID là một trong những lỗi API phổ biến và nghiêm trọng nhất, và nó ẩn trong các điểm cuối cũ hơn có trước các tiêu chuẩn hiện tại của bạn. Cấp quyền phía máy chủ trên mọi yêu cầu và mọi đối tượng là quy tắc, nhưng phần khó là xác minh nó đứng vững trên một cơ sở mã trải rộng, nhiều năm tuổi do nhiều bàn tay viết. Hãy quyết định liệu bạn sẽ tập trung logic cấp quyền, thêm kiểm thử tự động cố truy cập xuyên người thuê, hay chạy kiểm thử có mục tiêu đối với các API rủi ro cao nhất của bạn trước. Hãy mang bản kiểm kê các điểm cuối phơi bày định danh đối tượng và xếp hạng chúng theo độ nhạy cảm của những gì chúng trả về. Không có một cuộc quét có chủ đích, bạn sẽ tiếp tục phát hành lỗi này và chỉ phát hiện khi một nhà nghiên cứu hay kẻ tấn công phát hiện.

3. **Kế hoạch của bạn cho lỗ hổng phụ thuộc lan rộng kế tiếp là gì: bạn tìm và vá mọi dịch vụ bị ảnh hưởng nhanh đến đâu?** Khi một lỗi nghiêm trọng xuất hiện trong một thư viện phổ biến, các công ty có SBOM chính xác xác định dịch vụ bị ảnh hưởng trong vài giờ trong khi những công ty khác mất hàng tuần tìm kiếm, và khoảng cách tốc độ đó quyết định bạn chịu bao nhiêu thiệt hại. Hãy quyết định ngay bây giờ liệu bạn có tạo Danh mục Vật liệu Phần mềm cho mọi sản phẩm không, quét phụ thuộc có chạy trong mọi đường ống không, và ai sở hữu quyết định vá khẩn cấp. Với người mua chịu quy định và chính phủ, SBOM và nguồn gốc có ký ngày càng là điều kiện để làm ăn, nên sự sẵn sàng này cũng bảo vệ doanh thu. Hãy mang câu trả lời trung thực cho một cuộc diễn tập: chọn một thư viện bạn dùng rộng rãi và đo mất bao lâu để liệt kê mọi dịch vụ phát hành nó. Nếu câu trả lời tính bằng ngày, hãy đầu tư vào kiểm kê và ký trước khi sự cố kế tiếp buộc bạn làm.

4. **Làm thế nào bạn sẽ chuyển từ bí mật tĩnh sống lâu sang thông tin xác thực sống ngắn, được cấp tự động, và hệ thống nào đang chặn điều đó hôm nay?** Bí mật được mã hóa cứng và sống lâu là nguyên nhân lâu năm của xâm phạm, và cách sửa, thông tin xác thực sống ngắn được cấp theo yêu cầu, phụ thuộc vào hạ tầng cấp phát mà các hệ thống cũ thường không dùng được. Với một đội lớn, mối nguy là áp dụng không đồng đều: một nền tảng hiện đại xoay vòng khóa hằng giờ trong khi một dịch vụ cũ vẫn phát hành một mật khẩu cơ sở dữ liệu tĩnh trong tệp cấu hình. Hãy quyết định khối lượng công việc nào có thể tiêu thụ trình quản lý bí mật hoặc hệ thống danh tính khối lượng công việc ngay bây giờ, cái nào cần đầu tư trước, và ai sở hữu sổ tay xoay vòng ngay khoảnh khắc một khóa bị nghi rò rỉ. Hãy mang bản kiểm kê mọi thông tin xác thực đang dùng, thời gian sống, bán kính ảnh hưởng nếu bị phơi bày, và liệu quét commit có bắt được nó trước khi hợp nhất không. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn điều này với kiểm toán: người kiểm tra ngày càng mong bằng chứng về xoay vòng, truy cập có phạm vi và ghi nhật ký truy cập cho mọi bí mật, và một thông tin xác thực tĩnh mà bạn không thể xoay vòng mà không có thời gian ngừng là một phát hành chờ được viết thành báo cáo.

5. **Bạn vẫn chạy xác thực tự chế hoặc không nhất quán ở đâu, và kế hoạch hợp nhất vào các giao thức đã thẩm định là gì?** Xây xác thực là một trong những cách dễ nhất để đưa vào các lỗi tinh vi, khai thác được, vậy mà hầu hết các hệ sinh thái lớn mang ít nhất một luồng đăng nhập cũ có trước quyết định chuẩn hóa trên OAuth 2.0 và OIDC. Các áp lực cạnh tranh là thật: di chuyển một luồng cũ mạo hiểm làm hỏng người dùng và tích hợp hiện có, trong khi để nguyên giữ một mục tiêu giá trị cao được phòng thủ thiếu. Hãy quyết định liệu bạn có hợp nhất trên một nhà cung cấp danh tính duy nhất, thực thi MFA đồng nhất, và đặt hạn chót để loại bỏ từng luồng theo yêu cầu riêng, hay chấp nhận các ngoại lệ có tài liệu với biện pháp kiểm soát bù. Hãy mang bản đồ mọi đường xác thực trong đội hình, cái nào thực thi MFA, cái nào lưu mật khẩu bằng băm tốn bộ nhớ hiện đại, và cái nào là tùy chỉnh. Với danh mục doanh nghiệp và chính phủ, hãy thêm góc độ tuân thủ: các tiêu chuẩn như NIST SP 800-63 đặt ra kỳ vọng cụ thể về bảo đảm danh tính, và một luồng tự chế không thể chứng minh chúng sẽ không sống sót qua một cuộc kiểm toán hay rà soát cấp phép vận hành.

6. **Làm sao bạn xác minh rằng các biện pháp kiểm soát này thực sự đứng vững trên môi trường thực, và bạn có thể chứng minh bằng bằng chứng thay vì khẳng định không?** Viết một mặc định an toàn không giống với việc biết mọi dịch vụ vẫn tôn trọng nó, và các biện pháp kiểm soát lặng lẽ mục nát khi mã thay đổi, ngoại lệ chất đống, và điểm cuối mới được phát hành. Với một đội lớn câu hỏi là độ bao phủ: dịch vụ nào chạy phân tích tĩnh, quét phụ thuộc, và kiểm thử động hay xâm nhập, và làm sao bạn biết những cái bỏ qua chúng không phải là ứng dụng rủi ro cao nhất của bạn? Hãy quyết định xác minh nào là bắt buộc trong đường ống so với định kỳ, ai phân loại phát hiện, và bạn giữ bằng chứng nào để cho thấy một biện pháp kiểm soát đã được kiểm thử và đạt vào một ngày nhất định. Hãy mang bản đồ độ bao phủ hiện tại, thời gian trung bình để khắc phục theo mức nghiêm trọng, và danh sách các ứng dụng không có kiểm thử gần đây. Trong bối cảnh chịu quy định và chính phủ, bằng chứng này không tùy chọn: kiểm toán viên, viên chức cấp phép và người điều tra xâm phạm đều hỏi bằng chứng rằng các biện pháp kiểm soát đã được xác minh, và một chính sách không có hồ sơ kiểm thử hiếm khi làm họ hài lòng.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với hai hoặc ba kỹ sư và không có chuyên gia bảo mật, đòn bẩy của bạn là thừa hưởng bảo mật thay vì xây nó: áp dụng nhà cung cấp danh tính OIDC được quản lý, dựa vào một khung phát triển có ORM tham số hóa truy vấn theo mặc định, và giữ bí mật trong trình quản lý bí mật của nền tảng thay vì các tệp `.env` mà đồng đội có thể vô tình commit. Bật quét phụ thuộc tự động mở các pull request vá, và coi đó là đủ bây giờ. Đừng xây xác thực hay mật mã riêng, vì một truy vấn bị chèn hay một khóa bị rò rỉ có thể kết thúc công ty trước khi nó có khách hàng.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia bảo mật ứng dụng và ngân sách eo hẹp, vì vậy hãy mua các biện pháp kiểm soát nhúng trong công cụ và nền tảng bạn đã trả tiền thay vì bố trí nhân sự cho một chức năng riêng. Chọn một nhà cung cấp danh tính được lưu trữ có MFA đi kèm, một cơ sở dữ liệu được quản lý đẩy bạn về truy cập tham số hóa, và một máy chủ kho mã quét commit tìm bí mật rò rỉ ngay từ đầu. Hãy tập trung sự chú ý khan hiếm vào những điều cơ bản của OWASP Top 10 gây ra hầu hết các vụ xâm phạm thực tế, và ưu tiên nhà cung cấp phát hành mặc định an toàn mà bạn không thể tắt một cách tùy tiện.

**Doanh nghiệp lớn.** Qua nhiều đội thách thức là sự nhất quán: nướng các biện pháp kiểm soát ASVS vào khung đường lát sẵn để mọi dịch vụ mới thừa hưởng truy vấn tham số hóa, mã hóa đầu ra, phiên an toàn và cấp quyền phía máy chủ miễn phí. Chạy SBOM chính xác và quét phụ thuộc toàn đội hình để lỗ hổng thư viện lan rộng kế tiếp là chuyện của vài giờ, không phải vài tuần, và tập trung chính sách cấp quyền để truy cập xuyên người thuê trở nên kiểm thử được. Chuẩn hóa trên một nhà cung cấp danh tính với MFA được thực thi, và quản lý bảo mật ứng dụng như một danh mục được quản trị với các mức ASVS phân bậc theo rủi ro và bằng chứng được kiểm toán.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình các biện pháp kiểm soát bạn phải chứng minh, không chỉ cài đặt. Hãy xác minh các dịch vụ hướng đến công dân đối chiếu với OWASP ASVS ở mức khớp với độ nhạy cảm của dữ liệu, ký mọi sản phẩm được triển khai và chứng thực nguồn gốc của nó theo SLSA để thỏa mãn các yêu cầu bắt buộc về chuỗi cung ứng, và cấp thông tin xác thực sống ngắn từ một kho trung tâm với ghi nhật ký truy cập đầy đủ. Hãy kỳ vọng phải cho kiểm toán viên và viên chức cấp phép thấy một chuỗi bảo quản có tài liệu từ mã nguồn đến môi trường thực, và căn chỉnh bảo đảm danh tính theo các tiêu chuẩn đã công bố như NIST SP 800-63.

## Ví dụ

**Công ty khởi nghiệp.** Một đội SaaS ba kỹ sư bỏ qua việc tự xây đăng nhập và áp dụng một nhà cung cấp OIDC được quản lý ngay ngày đầu, có được MFA và đặt lại mật khẩu an toàn mà không phải viết mã quan trọng về bảo mật mà họ không thể gánh làm sai. Họ dựa vào ORM của khung phát triển để truy vấn được tham số hóa theo mặc định, giữ bí mật trong trình quản lý bí mật của nền tảng thay vì các tệp `.env` mà đồng đội có thể vô tình commit, và bật quét phụ thuộc tự động mở một pull request khi một thư viện cần vá. Không điều nào trong số này làm đội chậm lại, và nó có nghĩa là một khóa bị rò rỉ hay một truy vấn bị chèn không kết thúc công ty trước khi nó có khách hàng.

**Doanh nghiệp lớn.** Một nền tảng bán lẻ phục vụ hàng chục triệu người mua chuẩn hóa xác thực trên OIDC qua một nhà cung cấp danh tính duy nhất, thực thi MFA cho nhân viên và xác thực nâng bậc cho các thay đổi tài khoản giá trị cao. Mọi truy cập cơ sở dữ liệu đi qua một ORM được cấu hình để tham số hóa truy vấn, và một Chính sách Bảo mật Nội dung hỗ trợ mã hóa đầu ra. Sau một lỗ hổng được công bố rộng rãi trong một thư viện ghi nhật ký phổ biến, SBOM của công ty cho phép xác định mọi dịch vụ bị ảnh hưởng trong vài giờ và vá chúng trong hai ngày, trong khi các đối thủ không có bản kiểm kê mất hàng tuần tìm kiếm.

**Chính phủ.** Một cơ quan trợ cấp liên bang xây các dịch vụ hướng đến công dân được xác minh đối chiếu với OWASP ASVS Mức 2, với Mức 3 cho các thành phần xử lý hồ sơ nhạy cảm nhất. Bí mật sống trong một kho trung tâm cấp thông tin xác thực sống ngắn; quét commit chặn bất kỳ khóa nào bị rò rỉ. Mọi sản phẩm được triển khai đều được ký và nguồn gốc của nó được chứng thực theo SLSA, thỏa mãn một yêu cầu bắt buộc của liên bang về chuỗi cung ứng phần mềm xác minh được và cho kiểm toán viên một chuỗi bảo quản rõ ràng từ mã nguồn đến môi trường thực.

## Luận chứng kinh doanh: động lực, ROI và TCO

Chi tiêu cho bảo mật ứng dụng mua giảm loại xâm phạm có khả năng cao nhất và đắt nhất. Tổng chi phí sở hữu bao gồm công cụ (bộ quét, trình quản lý bí mật, nhà cung cấp danh tính), thời gian kỹ sư để khắc phục phát hiện, và ma sát nhẹ của mặc định an toàn. Đối lại, hãy cân nhắc chi phí của việc bỏ qua: các vụ xâm phạm chèn mã và kiểm soát truy cập hỏng thường xuyên phơi bày hàng triệu bản ghi, kích hoạt tiền phạt quy định, thông báo bắt buộc, tổn thất gian lận, các đợt chạy nước rút khắc phục, và thiệt hại danh tiếng kìm hãm doanh thu nhiều năm.

ROI mạnh nhất khi các biện pháp kiểm soát được tự động hóa và tái sử dụng. Một tích hợp danh tính cấu hình tốt, một tầng truy vấn được gia cố trong khung dùng chung, và một đường ống chặn phụ thuộc có lỗ hổng bảo vệ cả đội hình với chi phí biên theo từng dịch vụ. Các biện pháp kiểm soát chuỗi cung ứng đặc biệt đã đi từ tùy chọn sang thiết yếu: một phụ thuộc bị xâm phạm có thể biến mọi khách hàng của bạn thành nạn nhân, và cơ quan quản lý cùng người mua doanh nghiệp ngày càng yêu cầu SBOM và nguồn gốc có ký như điều kiện để làm ăn. Khi bạn trình bày lập luận với ban lãnh đạo, hãy gắn khoản đầu tư với các rủi ro cụ thể, có tên và với yêu cầu mua sắm cùng tuân thủ chặn doanh thu nếu bạn không đáp ứng.

## Phản mẫu và cạm bẫy

- **Tự viết mật mã hay xác thực.** Hầu như luôn tạo ra các lỗi tinh vi, khai thác được.
- **Xác thực chỉ phía máy khách.** Bị vượt qua dễ dàng; máy chủ phải xác thực lại mọi thứ.
- **Làm sạch theo danh sách chặn.** Cố loại bỏ ký tự "xấu" thay vì cho phép ký tự tốt; kẻ tấn công tìm ra khoảng trống.
- **Bí mật trong mã nguồn hoặc tệp môi trường.** Nguyên nhân phổ biến nhất của rò rỉ thông tin xác thực.
- **Bỏ qua cấp quyền trên truy cập đối tượng.** Giả định một người dùng đã xác thực có thể truy cập bất kỳ đối tượng nào mà họ đoán được ID.
- **Phụ thuộc cài-rồi-quên.** Không bao giờ cập nhật thành phần bên thứ ba cho đến khi một vụ xâm phạm buộc phải làm.
- **Coi Top 10 là vạch đích.** Đó là sàn, không phải tiêu chuẩn toàn diện; hãy dùng ASVS để có chiều sâu.
- **Ghi nhật ký dữ liệu nhạy cảm.** Mật khẩu, token và PII (thông tin nhận dạng cá nhân) trong nhật ký là một vụ xâm phạm đang chờ xảy ra.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Bảo mật ứng dụng phụ thuộc vào kiến thức của từng lập trình viên và chỉ phản ứng sau sự cố. Không có biện pháp kiểm soát tiêu chuẩn. Bí mật nằm trong mã nguồn. Phụ thuộc hiếm khi được cập nhật. Xác thực là tùy chỉnh và tùy nghi, và lỗi chèn mã hay kiểm soát truy cập hỏng được tìm thấy do may mắn hơn là quy trình.

**Mức 2: Phát triển.** Các thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Nhận thức về OWASP Top 10 lan rộng, một số bảo vệ cấp khung phát triển có mặt, và một trình quản lý bí mật tồn tại nhưng được dùng không đều. Quét phụ thuộc chạy thỉnh thoảng. Hệ thống mới áp dụng nhà cung cấp danh tính chuẩn, trong khi dịch vụ cũ giữ nguyên các luồng đăng nhập tự chế.

**Mức 3: Chuẩn hóa.** Các biện pháp kiểm soát được lập tài liệu và thực thi trong toàn tổ chức. Yêu cầu dựa trên ASVS được đặt theo từng bậc rủi ro, truy vấn tham số hóa và mã hóa đầu ra là chuẩn mực, và một nhà cung cấp danh tính trung tâm với MFA là bắt buộc. Bí mật được quản lý và quét tự động, SBOM được tạo, và quét phụ thuộc chạy trong mọi đường ống.

**Mức 4: Quản lý.** Thực hành được đo và kiểm soát theo các đường cơ sở. Độ bao phủ quét và kiểm thử, thời gian trung bình để khắc phục theo mức nghiêm trọng, tỷ lệ dịch vụ thừa hưởng mặc định đường lát sẵn, tuổi xoay vòng thông tin xác thực và bí mật, và sự phù hợp ASVS đều được theo dõi trên bảng điều khiển. Ngoại lệ được ghi lại với ngày hết hạn, sự trôi khỏi đường cơ sở kích hoạt hành động, và các bản phát hành bị kiểm soát bằng ngưỡng bảo mật xác định thay vì các phán đoán.

**Mức 5: Điều phối.** Bảo mật được cải thiện liên tục và tích hợp trong toàn tổ chức. Mặc định an toàn được dựng vào khung đường lát sẵn để con đường an toàn là tự động, thông tin xác thực sống ngắn được dùng ở mọi nơi, và bảo đảm chuỗi cung ứng đầy đủ với ký và nguồn gốc (SLSA) là tiêu chuẩn. Xác minh là liên tục, phản ứng với lỗ hổng mới nhanh chóng và được đo, và mỗi sự cố phản hồi vào các mẫu dùng chung để một bản sửa đơn lẻ gia cố cả đội hình.

## Ý tưởng để thảo luận

1. Logic cấp quyền nên sống ở đâu để vừa nhất quán vừa bảo trì được qua nhiều dịch vụ?
2. Bạn nên cập nhật phụ thuộc quyết liệt đến mức nào khi cân nhắc đánh đổi giữa phơi nhiễm và xáo động?
3. Mức ASVS nào phù hợp cho từng lớp ứng dụng trong danh mục của bạn?
4. Làm sao bạn loại bỏ bí mật sống lâu mà không tạo ra hạ tầng cấp phát mong manh?
5. Cần gì để tổ chức của bạn tạo và tiêu thụ SBOM cùng nguồn gốc cho mọi sản phẩm?
6. Làm sao bạn giữ mặc định an toàn không bị tắt dưới áp lực phân phối?

## Những điểm cần ghi nhớ

- OWASP Top 10 là kiến thức thiết yếu; ASVS cung cấp tiêu chuẩn kiểm thử được.
- Xếp tầng xác thực đầu vào, tham số hóa và mã hóa đầu ra để đánh bại chèn mã và XSS.
- Dùng các giao thức đã thẩm định (OAuth 2.0, OIDC) và thực thi MFA; không bao giờ tự xây xác thực từ đầu.
- Thực thi cấp quyền phía máy chủ cho mọi yêu cầu và mọi đối tượng.
- Giữ bí mật ngoài mã nguồn, quản lý chúng tập trung, và xoay vòng sang thông tin xác thực sống ngắn.
- Chuỗi cung ứng là bề mặt tấn công chính; hãy dùng SBOM, SCA, ký và nguồn gốc (SLSA).
- Các biện pháp kiểm soát tự động, tái sử dụng bảo vệ cả đội hình với chi phí biên theo từng dịch vụ.

## Tài liệu tham khảo và đọc thêm

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard và Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation và OpenSSF, *SLSA framework* và hướng dẫn *Supply-chain Security*
