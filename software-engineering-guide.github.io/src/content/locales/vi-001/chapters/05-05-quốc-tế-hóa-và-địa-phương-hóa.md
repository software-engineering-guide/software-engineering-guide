# 5.5 Quốc tế hóa và địa phương hóa

## Tổng quan và động lực

[Quốc tế hóa](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) là công việc kỹ thuật xây phần mềm để nó có thể thích ứng với bất kỳ ngôn ngữ, khu vực và văn hóa nào mà không đổi mã. Địa phương hóa (l10n) là công việc theo sau: thực sự điều chỉnh một sản phẩm cho một miền địa phương cụ thể bằng cách dịch văn bản, định dạng ngày và số, điều chỉnh bố cục, và tính đến kỳ vọng văn hóa. Hai thứ khác nhau. Quốc tế hóa được làm một lần, trong kiến trúc. Địa phương hóa được làm nhiều lần, trong nội dung. Làm đúng kiến trúc ngay từ đầu và mỗi lần địa phương hóa đều rẻ. Làm sai và mỗi lần trở thành một cuộc trang bị bổ sung đau đớn, dễ lỗi.

Với các đội lớn, i18n là một quyết định kiến trúc nền tảng. Nó chạm vào mọi tầng: lưu trữ dữ liệu, xử lý chuỗi, bố cục và đường ống nội dung. Nếu bạn không thiết lập nó sớm và thực thi nó qua thư viện dùng chung và quy tắc lint, các đội mã hóa cứng chuỗi tiếng Anh, nối các mảnh đã dịch, và giả định chữ viết Latin. Khoản nợ đó phải được gỡ trước khi sản phẩm vào được bất kỳ thị trường mới nào. Một khung i18n dùng chung và quy trình địa phương hóa cho phép hàng chục đội phát hành sản phẩm bằng nhiều ngôn ngữ mà không mỗi đội phát minh lại hệ thống ống nước.

Sự liên quan với doanh nghiệp và chính phủ là trực tiếp. Doanh nghiệp đa quốc gia phải phục vụ khách hàng và nhân viên qua các quốc gia, ngôn ngữ và chế độ quy định. Chính phủ phải phục vụ các quần thể đa dạng về ngôn ngữ. Nhiều quốc gia chính thức đa ngôn ngữ, và nhiều nước bị luật yêu cầu cung cấp dịch vụ bằng nhiều ngôn ngữ, bao gồm chữ viết [phải-sang-trái](https://en.wikipedia.org/wiki/Bidirectional_text) và ngôn ngữ bản địa hay thiểu số. Với dịch vụ công, tiếp cận ngôn ngữ là vấn đề công bằng và pháp lý: một công dân không đọc được ngôn ngữ duy nhất có sẵn thực tế bị từ chối dịch vụ.

## Các nguyên tắc chính

- Quốc tế hóa kiến trúc một lần; địa phương hóa nội dung nhiều lần.
- Không bao giờ mã hóa cứng văn bản hướng người dùng; tách mọi chuỗi vào tài nguyên được quản lý.
- Dùng [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) ở mọi nơi; giả định văn bản có thể ở bất kỳ chữ viết nào.
- Không bao giờ nối các mảnh đã dịch; ngữ pháp và thứ tự từ khác nhau theo ngôn ngữ.
- Lên kế hoạch cho sự giãn nở văn bản, chữ viết phải-sang-trái, và quy tắc số nhiều cùng giới tính phức tạp.
- Định dạng ngày, số, tiền tệ và tên theo miền địa phương, không phải theo mã.
- Tách nội dung dịch được khỏi mã để người dịch không bao giờ chạm vào nguồn.
- Địa phương hóa là văn hóa, không chỉ ngôn ngữ: màu sắc, hình ảnh và ví dụ đều quan trọng.

## Khuyến nghị

### Xây một kiến trúc quốc tế hóa vững chắc

Hãy lưu và xử lý mọi văn bản dưới dạng Unicode (UTF-8) từ đầu đến cuối (cơ sở dữ liệu, API và UI) để bất kỳ chữ viết nào cũng biểu diễn được. Tách mọi chuỗi hướng người dùng vào tệp tài nguyên hoặc danh mục thông điệp khóa theo định danh, không bao giờ nhúng trong mã hay đánh dấu. Biểu diễn một miền địa phương là ngôn ngữ cộng khu vực (và chữ viết ở nơi cần) để bạn phân biệt được, ví dụ, các biến thể của một ngôn ngữ qua các quốc gia. Giữ logic định dạng trong một thư viện quốc tế hóa đã được kiểm thử tốt thay vì tự làm định dạng ngày, số và tiền tệ. Lưu dữ liệu ở dạng trung tính, rõ ràng (dấu thời gian UTC, mã quốc gia và tiền tệ ISO, đơn vị cơ sở) và chỉ định dạng ở tầng trình bày.

### Xử lý đúng độ phức tạp của ngôn ngữ

Đừng giả định độ dài văn bản; hãy để chỗ rộng rãi vì bản dịch thường dài hơn tiếng Anh nhiều, và thiết kế bố cục tự chảy lại thay vì cắt hay chồng lấn. Hỗ trợ chữ viết hai chiều (phải-sang-trái) bằng cách dùng thuộc tính bố cục logic thay vì vật lý và phản chiếu giao diện ở nơi phù hợp. Dùng quy tắc số nhiều của miền địa phương qua thư viện i18n của bạn (các ngôn ngữ có từ một đến sáu dạng số nhiều) thay vì logic số ít/số nhiều ngây thơ. Xử lý giới tính và sự hòa hợp ngữ pháp ở nơi ngôn ngữ đòi hỏi. Không bao giờ dựng câu bằng nối; hãy dùng mẫu thông điệp đầy đủ, có tham số để người dịch kiểm soát thứ tự từ.

### Thiết lập quy trình địa phương hóa và quản lý dịch thuật

Hãy coi địa phương hóa là một đường ống liên tục, không phải một lô trước ra mắt. Trích xuất chuỗi tự động, đẩy chúng vào một [hệ thống quản lý dịch thuật](https://en.wikipedia.org/wiki/Translation_management_system), và kéo bản dịch đã hoàn thành về, lý tưởng là tích hợp với CI để chuỗi mới được đánh dấu và các phiên bản địa phương hóa giữ đồng bộ. Cho người dịch ngữ cảnh: ảnh chụp màn hình, mô tả, giới hạn ký tự, và một bảng thuật ngữ cùng hướng dẫn phong cách cho từng ngôn ngữ để giữ thuật ngữ và giọng điệu nhất quán. Dùng [bộ nhớ dịch](https://en.wikipedia.org/wiki/Translation_memory) để tái sử dụng công việc trước và cắt chi phí. Hãy quyết định có chủ đích nơi [dịch máy](https://en.wikipedia.org/wiki/Machine_translation) chấp nhận được (nội dung rủi ro thấp, khối lượng cao) và nơi cần dịch thuật con người cùng rà soát (pháp lý, y tế, an toàn, quan trọng với thương hiệu). [Giả địa phương hóa](https://en.wikipedia.org/wiki/Pseudolocalization) sớm, thay chuỗi bằng văn bản giữ chỗ kéo dài, có dấu, để bắt chuỗi mã hóa cứng, bị cắt và lỗi mã hóa trước khi dịch thật bắt đầu.

### Địa phương hóa định dạng, văn hóa và nội dung, không chỉ từ ngữ

Hãy định dạng ngày, giờ, số, tiền tệ, địa chỉ, số điện thoại và tên theo miền địa phương, tôn trọng quy ước địa phương (thứ tự ngày, dấu phân cách thập phân và nhóm, vị trí tiền tệ, thứ tự tên). Điều chỉnh hình ảnh, biểu tượng, màu sắc, ví dụ và ẩn dụ theo ý nghĩa văn hóa địa phương, vì biểu tượng và màu sắc mang hàm ý khác nhau qua các nền văn hóa. Tính đến khác biệt nội dung pháp lý và quy định địa phương. Phân biệt sự nhất quán toàn cầu (thương hiệu, chức năng cốt lõi) với điều chỉnh khu vực (nội dung, ví dụ, tuân thủ) và quyết định tường minh yếu tố nào cố định và yếu tố nào linh hoạt.

### Quản trị i18n như hạ tầng dùng chung

Hãy cung cấp một thư viện i18n dùng chung, quy tắc lint tách chuỗi, và một cơ chế giải quyết miền địa phương chuẩn để các đội không thể vô tình mã hóa cứng văn bản. Thiết lập quyền sở hữu đường ống địa phương hóa và bảng thuật ngữ. Kiểm thử trong nhiều miền địa phương trong CI, bao gồm một miền phải-sang-trái và một miền giả văn bản dài, để hồi quy được bắt tự động.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Quốc tế hóa từ ngày đầu | Vào thị trường sau này rẻ, không trang bị bổ sung | Chi phí ban đầu ngay cả trước khi cần miền địa phương thứ hai |
| Trang bị i18n sau | Hoãn chi phí nếu nhu cầu toàn cầu chưa chắc | Rất đắt và rủi ro để gỡ các giả định mã hóa cứng |
| Dịch thuật con người | Chất lượng cao, chính xác về văn hóa | Chậm hơn và tốn hơn |
| Dịch máy | Nhanh, rẻ, mở rộng đến khối lượng khổng lồ | Rủi ro chất lượng và chính xác; không phù hợp nội dung rủi ro cao |
| Đường ống địa phương hóa liên tục | Các miền địa phương giữ đồng bộ, không chạy nước rút ra mắt | Đầu tư công cụ và quy trình |
| Điều chỉnh văn hóa sâu theo khu vực | Phù hợp địa phương và niềm tin tốt hơn | Nhiều biến thể nội dung hơn để xây và duy trì |

Đánh đổi then chốt là khi nào đầu tư vào quốc tế hóa. Trang bị i18n vào một sản phẩm đầy mã hóa cứng, nối chuỗi, giả định Latin là một trong những dạng nợ kỹ thuật tốn kém hơn để trả. Với bất kỳ tổ chức nào có tham vọng quốc tế hay đa ngôn ngữ hợp lý, bao gồm gần như mọi doanh nghiệp lớn và chính phủ đa ngôn ngữ, quốc tế hóa kiến trúc sớm rẻ hơn nhiều so với trang bị bổ sung, dù phần thưởng bị trì hoãn.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta có thực thi tách chuỗi bằng quy tắc lint không, và giả địa phương hóa có chạy trong CI trước bất kỳ bản dịch thật nào không?** Khoản nợ khiến quốc tế hóa đắt (chuỗi tiếng Anh mã hóa cứng, mảnh câu nối, giả định chữ viết Latin) tích tụ trong im lặng trừ khi công cụ chặn nó lúc commit. Quy tắc lint đánh dấu văn bản người dùng mã hóa cứng, cộng một miền giả có dấu, văn bản dài chạy trong CI, bắt cắt cụt, chồng lấn và lỗi mã hóa khi chúng còn rẻ để sửa. Đây là thứ cho phép hàng chục đội phát hành một sản phẩm bằng nhiều ngôn ngữ mà không mỗi đội phát minh lại hệ thống ống nước hay gỡ giả định trong hạn chót sau này. Hãy mang một lần tìm kiếm chuỗi mã hóa cứng và hỏi liệu có đội nào có thể vô tình phát hành một cái hôm nay không. Nếu không có gì trong đường ống bắt được, đó là khoảng trống cần đóng đầu tiên.

2. **Chúng ta lưu dữ liệu chuẩn ở đâu, và định dạng có được giới hạn ở tầng trình bày không?** Lưu dấu thời gian là UTC, quốc gia và tiền tệ là mã ISO, và số tiền ở đơn vị cơ sở nghĩa là bất kỳ miền địa phương nào cũng định dạng chúng đúng ở rìa, trong khi logic định dạng nướng vào tầng dữ liệu tạo ra lỗi đau đớn để gỡ. Hãy thống nhất rằng ngày, số, tiền tệ, địa chỉ và tên chỉ được định dạng lúc trình bày, qua một thư viện đã kiểm thử tốt thay vì mã tự làm. Điều này quan trọng với doanh nghiệp đa quốc gia và chính phủ đa ngôn ngữ nơi một công dân phải thấy đúng thứ tự ngày, dấu phân cách thập phân và thứ tự tên theo quy ước của họ. Hãy mang một ví dụ về giá trị hệ thống của bạn lưu đã định dạng sẵn và truy cái gì hỏng khi một miền địa phương mới cần nó khác đi. Nếu dữ liệu và trình bày bị rối, hãy quyết định bạn gỡ rối thế nào trước khi thêm miền địa phương.

3. **Dịch máy chấp nhận được chính xác ở đâu, và đường ống địa phương hóa của chúng ta được giữ liên tục thay vì theo lô thế nào?** Dịch máy nhanh và rẻ cho nội dung rủi ro thấp, khối lượng cao nhưng không phù hợp với văn bản pháp lý, y tế, an toàn hay quan trọng với thương hiệu nơi một bản dịch sai gây hại thực, nên ranh giới cần là một chính sách tường minh, không phải đoán theo từng đội. Tương tự, coi địa phương hóa là một lô trước ra mắt bảo đảm một cuộc chạy vạy dịch thuật, trong khi trích xuất chuỗi tự động và đồng bộ qua một hệ thống quản lý dịch thuật giữ mọi miền địa phương hiện hành. Hãy quyết định ai sở hữu đường ống, bảng thuật ngữ, và cổng rà soát của con người cho chuỗi rủi ro cao. Hãy mang một bản phát hành gần đây và hỏi chuỗi mới của nó mất bao lâu để xuất hiện trong mọi ngôn ngữ. Nếu các miền địa phương trôi khỏi đồng bộ giữa các bản phát hành, đường ống của bạn là theo lô trá hình.

4. **Chúng ta có kiểm thử tự động một miền phải-sang-trái và một miền giả văn bản dài, hay đang lặng lẽ giả định chữ viết Latin và bố cục độ dài tiếng Anh?** Hỗ trợ hai chiều (phải-sang-trái) và sự giãn nở văn bản là những giả định vỡ rõ nhất ở một thị trường mới: giao diện phản chiếu chưa bao giờ được phản chiếu, và nút bị cắt khi tiếng Đức hay Phần Lan dài hơn tiếng Anh bốn mươi phần trăm. Lực kéo đối lập là tốc độ, vì xây trên thuộc tính bố cục logic thay vì vật lý và nối một miền giả có dấu vào tích hợp liên tục (CI) tốn công sức trước khi bất kỳ khách hàng thật nào cần. Hãy mang ảnh chụp màn hình các màn hình bận nhất của bạn được kết xuất trong miền phải-sang-trái và trong miền giả kéo dài, và đếm chồng lấn, nhãn bị cắt và mũi tên bị kẹt. Với một doanh nghiệp đa quốc gia hay chính phủ bị luật yêu cầu phục vụ một ngôn ngữ phải-sang-trái hoặc thiểu số, một bố cục không phản chiếu được không phải khiếm khuyết thẩm mỹ, mà là thị trường hay nghĩa vụ luật định bạn không thể đáp ứng nếu không xây lại.

5. **Phần nào của sản phẩm cố định toàn cầu và phần nào linh hoạt theo khu vực, và ai có thẩm quyền quyết định?** Địa phương hóa là văn hóa, không chỉ ngôn ngữ, nên màu sắc, hình ảnh, ví dụ, kính ngữ, và thậm chí tính năng nào được cung cấp có thể khác theo thị trường, vậy mà mỗi biến thể khu vực bạn cho phép là một sản phẩm nữa để xây, dịch, rà soát và duy trì mãi mãi. Căng thẳng là giữa sự phù hợp địa phương, xây niềm tin và chuyển đổi, và sự nhất quán, giữ thương hiệu mạch lạc và gánh nặng bảo trì có giới hạn. Hãy mang một danh sách cụ thể về cái một miền địa phương mới đề xuất sẽ thay đổi ngoài chuỗi đã dịch, và định giá chi phí duy trì liên tục của mỗi biến thể, không chỉ lần xây đầu. Trong một doanh nghiệp lớn quyết định này cần một chủ sở hữu có tên để các đội khu vực không thể rẽ nhánh sản phẩm tùy nghi, và trong chính phủ nó phải tôn trọng quy tắc nội dung pháp lý và khả năng tiếp cận khác nhau theo quyền tài phán và không tùy chọn.

6. **Chúng ta thực sự cam kết những miền địa phương nào, làm sao giữ thuật ngữ nhất quán qua chúng, và bằng chứng nào dẫn dắt danh sách đó?** Thêm một ngôn ngữ thì dễ hứa và tốn kém để duy trì, vì mỗi cái cần một bảng thuật ngữ, một hướng dẫn phong cách, rà soát của con người cho chuỗi rủi ro cao, và xử lý số nhiều cùng giới tính đúng mà logic số-ít-hay-số-nhiều ngây thơ làm sai ở hầu hết ngôn ngữ. Các cân nhắc cạnh tranh là tầm với so với chi phí: một thị trường hay quần thể được phục vụ tồi có thể tệ hơn một cái không được phục vụ. Hãy mang dân số hay doanh thu đằng sau mỗi miền địa phương ứng viên, độ bao phủ quy tắc số nhiều và định dạng mà thư viện của bạn cung cấp cho nó, và ai sở hữu bảng thuật ngữ của nó. Với một doanh nghiệp đa quốc gia động lực là thị trường có thể với tới và chi phí hỗ trợ mỗi ngôn ngữ, trong khi với chính phủ nó là nghĩa vụ tiếp cận ngôn ngữ theo luật và công bằng, được định lượng bằng số cư dân chỉ có thể giao dịch bằng ngôn ngữ đó.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy đưa ra các lựa chọn kiến trúc rẻ ngay ngày đầu và dừng ở đó: UTF-8 từ đầu đến cuối, mọi chuỗi hướng người dùng trong một danh mục thông điệp, và ngày, số, tiền tệ được định dạng qua một thư viện nhận biết miền địa phương. Những thứ này tốn gần như không gì khi bạn phát hành bằng một ngôn ngữ và tiết kiệm một lần viết lại khi khách hàng lớn đầu tiên của bạn muốn ngôn ngữ thứ hai. Đừng dựng đường ống dịch thuật hay hỗ trợ miền địa phương mà chưa ai trả tiền; giữ cửa mở, không phải trang bị cả ngôi nhà.

**Doanh nghiệp nhỏ.** Không có chuyên gia quốc tế hóa và ngân sách eo hẹp, hãy dựa vào các tính năng i18n đã có trong khung phát triển của bạn và một dịch vụ quản lý dịch thuật được lưu trữ thay vì tự xây đường ống. Dùng dịch máy cho nội dung rủi ro thấp, khối lượng cao và chỉ trả tiền cho dịch thuật con người nơi một sai lầm sẽ khiến bạn mất khách hàng hay vi phạm quy tắc, như văn bản pháp lý, an toàn hay thanh toán. Chỉ cam kết một miền địa phương khi một thị trường cụ thể rõ ràng biện minh cho chi phí dịch và rà soát liên tục.

**Doanh nghiệp lớn.** Vấn đề là quản trị qua nhiều đội: một thư viện i18n dùng chung, quy tắc lint từ chối chuỗi mã hóa cứng, một đường ống địa phương hóa liên tục với bộ nhớ dịch và bảng thuật ngữ theo từng ngôn ngữ, và CI đa miền địa phương bao gồm một miền phải-sang-trái và một miền giả văn bản dài. Hãy chạy địa phương hóa như hạ tầng dùng chung với chủ sở hữu rõ ràng để các nhóm thôi phát minh lại hệ thống ống nước hay trôi khỏi đồng bộ. Đo độ bao phủ ngôn ngữ, chất lượng địa phương hóa, và thời gian ra mắt một miền địa phương mới, và quản lý danh mục miền địa phương theo những con số đó thay vì ra mắt thị trường tùy nghi.

**Chính phủ.** Tiếp cận ngôn ngữ thường là nghĩa vụ pháp lý, bao quát ngôn ngữ chính thức, chữ viết phải-sang-trái, và ngôn ngữ bản địa hay thiểu số, nên minh bạch và công bằng định hình mọi lựa chọn. Hãy xây một khung i18n và quy trình dịch dùng chung qua các cơ quan, yêu cầu rà soát của con người cho thuật ngữ pháp lý và an toàn, và công bố bảng thuật ngữ để thuật ngữ nhất quán giữa các dịch vụ. Mua sắm nên đòi hỏi hỗ trợ miền địa phương, phải-sang-trái và khả năng tiếp cận trong hợp đồng, và quần thể được phục vụ trong mỗi ngôn ngữ là chỉ số biện minh khoản chi với công chúng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp nhỏ chỉ phát hành bằng tiếng Anh vẫn đưa ra vài lựa chọn kiến trúc rẻ ngay ngày đầu: UTF-8 ở mọi nơi, mọi chuỗi hướng người dùng được kéo vào một danh mục thông điệp thay vì mã hóa cứng, và ngày cùng tiền tệ được định dạng qua một thư viện nhận biết miền địa phương. Nó tốn họ gần như không gì khi chỉ có một ngôn ngữ. Một năm sau, khi khách hàng tiềm năng lớn nhất của họ yêu cầu phiên bản tiếng Pháp và tiếng Đức, thêm các miền địa phương đó chủ yếu là một bài tập dịch giao cho nhà thầu, không phải viết lại, và họ chốt thương vụ trong vài tuần thay vì hoãn nó cả một quý công việc kỹ thuật.

**Doanh nghiệp lớn.** Một công ty thương mại điện tử toàn cầu quốc tế hóa nền tảng của mình sớm: UTF-8 xuyên suốt, chuỗi được tách, một thư viện định dạng nhận biết miền địa phương, và một đường ống địa phương hóa liên tục với bộ nhớ dịch và bảng thuật ngữ theo từng ngôn ngữ. Vào một thị trường mới phần lớn trở thành một bài tập nội dung (dịch, rà soát, điều chỉnh hình ảnh) thay vì một dự án kỹ thuật, cho phép công ty ra mắt ở các miền địa phương mới trong vài tuần. Hỗ trợ phải-sang-trái xây trên thuộc tính bố cục logic nghĩa là các thị trường Ả Rập và Do Thái cần ít công việc UI mới.

**Chính phủ.** Một chính phủ quốc gia bị luật yêu cầu cung cấp dịch vụ bằng nhiều ngôn ngữ chính thức, bao gồm một chữ viết phải-sang-trái và ngôn ngữ thiểu số, xây một khung i18n và quy trình dịch dùng chung qua các cơ quan. Giả địa phương hóa trong CI bắt chuỗi mã hóa cứng và cắt cụt trước ra mắt; một bảng thuật ngữ dùng chung giữ thuật ngữ pháp lý nhất quán qua các dịch vụ và ngôn ngữ. Công dân có thể hoàn thành giao dịch thuế, y tế và trợ cấp bằng ngôn ngữ của chính họ với định dạng ngày, số và tên đúng, thỏa mãn luật tiếp cận ngôn ngữ và cải thiện công bằng cho người nói ngôn ngữ không phải đa số.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của quốc tế hóa là tiếp cận thị trường và tốc độ. Một sản phẩm được quốc tế hóa tốt có thể vào các quốc gia và thị trường ngôn ngữ mới nhanh và rẻ, biến mỗi miền địa phương mới thành doanh thu gia tăng hay tầm với công dân thay vì một dự án lớn. Chất lượng địa phương hóa thúc đẩy chuyển đổi, niềm tin và chi phí hỗ trợ ở mỗi thị trường: người dùng giao dịch nhiều hơn và liên hệ hỗ trợ ít hơn khi sản phẩm nói ngôn ngữ của họ đúng và tôn trọng quy ước của họ.

Về TCO, chi phí áp dụng là kỹ thuật ban đầu để quốc tế hóa, cộng chi phí dịch thuật và đường ống liên tục. Chi phí của việc không áp dụng là cuộc trang bị bổ sung đắt đỏ: gỡ chuỗi mã hóa cứng, nối chuỗi, lỗi mã hóa và giả định bố cục qua cả một cơ sở mã, thường trong hạn chót do một thị trường hay yêu cầu pháp lý thúc đẩy. Địa phương hóa kém cũng mang chi phí ẩn: doanh số mất ở các thị trường bị phục vụ tồi, gánh nặng hỗ trợ từ định dạng gây rối, và thiệt hại pháp lý hay danh tiếng từ nội dung rủi ro cao bị dịch sai. Địa phương hóa liên tục tránh các cuộc chạy vạy dịch thuật tốn kém trước ra mắt.

Để trình bày lập luận với ban lãnh đạo, hãy đóng khung quốc tế hóa là một quyền chọn trên các thị trường tương lai. Đó là một khoản đầu tư ban đầu khiêm tốn hạ đáng kể chi phí và thời gian của mọi lần vào thị trường tương lai. Với chính phủ, động lực là nghĩa vụ tiếp cận ngôn ngữ theo luật và công bằng, được định lượng bằng quần thể được phục vụ trong mỗi ngôn ngữ.

## Phản mẫu và cạm bẫy

- **Chuỗi mã hóa cứng**: văn bản người dùng nướng vào mã, buộc phải đổi mã theo từng miền địa phương.
- **Nối chuỗi**: dựng câu từ các mảnh, làm hỏng ngữ pháp và thứ tự từ.
- **Giả định phi Unicode**: lỗi mã hóa, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (văn bản rối do mã hóa ký tự không khớp), và không biểu diễn được chữ viết.
- **Giả định độ dài văn bản tiếng Anh**: bố cục bị cắt hoặc chồng lấn khi dịch.
- **Bỏ qua phải-sang-trái**: dùng bố cục trái/phải vật lý không phản chiếu được.
- **Số nhiều ngây thơ**: logic số ít/số nhiều sai ở hầu hết ngôn ngữ.
- **Định dạng mù miền địa phương**: định dạng ngày, số và tiền tệ mã hóa cứng.
- **Dịch không có ngữ cảnh**: người dịch đoán nghĩa, tạo ra lỗi.
- **Địa phương hóa theo lô, phút chót**: cuộc chạy vạy trước ra mắt thay vì đường ống liên tục.
- **Thiếu nhạy cảm văn hóa**: hình ảnh, màu sắc hay ví dụ gây xúc phạm hoặc rối ở địa phương.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Một ngôn ngữ, chuỗi mã hóa cứng, giả định phi Unicode, và văn bản dựng bằng nối. Quốc tế hóa là phản ứng: mỗi miền địa phương mới có nghĩa là đổi mã, và lỗi mã hóa cùng bố cục được tìm thấy tình cờ trên môi trường thực.

**Mức 2: Phát triển.** Một số chuỗi được tách và Unicode được dùng ở vài nơi, nhưng thực hành không nhất quán qua các đội. Địa phương hóa là nỗ lực thủ công, theo lô, trước ra mắt, và định dạng, xử lý số nhiều, và hỗ trợ phải-sang-trái được xử lý khác nhau (hoặc không hề) từ đội này sang đội khác.

**Mức 3: Chuẩn hóa.** Một kiến trúc i18n dùng chung và thư viện định dạng nhận biết miền địa phương là tiêu chuẩn được lập tài liệu, thực thi toàn tổ chức. Việc tách chuỗi được kiểm tra bằng quy tắc lint, một hệ thống quản lý dịch thuật và đường ống liên tục có mặt cùng bảng thuật ngữ và bộ nhớ dịch, và giả địa phương hóa cộng kiểm thử đa miền địa phương (bao gồm một miền phải-sang-trái và một miền văn bản dài) chạy trong CI.

**Mức 4: Quản lý.** Chương trình địa phương hóa được đo và kiểm soát theo các đường cơ sở. Các đội theo dõi độ bao phủ ngôn ngữ, chất lượng và tỷ lệ lỗi địa phương hóa, độ trễ đồng bộ chuỗi từ commit đến bản phát hành đã dịch, lỗi cắt cụt và kết xuất phải-sang-trái bắt được mỗi bản phát hành, chi phí dịch mỗi miền địa phương, và thời gian ra mắt một miền địa phương mới, và các chỉ số này kiểm soát bản phát hành và dẫn dắt nơi đầu tư rà soát của con người so với dịch máy.

**Mức 5: Điều phối.** Quốc tế hóa và địa phương hóa được cải thiện liên tục và tích hợp trong toàn tổ chức. Địa phương hóa là liên tục, dịch máy và dịch con người được chọn có chủ đích theo từng lớp nội dung, và điều chỉnh văn hóa có hệ thống. Tổ chức thêm, loại bỏ và điều chỉnh phạm vi các miền địa phương để đáp ứng bằng chứng thị trường và công bằng, và các miền địa phương mới ra mắt nhanh ở chất lượng cao mà không phải trang bị bổ sung.

## Ý tưởng để thảo luận

- Một sản phẩm nên quốc tế hóa sớm đến mức nào nếu nhu cầu quốc tế chưa chắc chắn?
- Dịch máy chấp nhận được ở đâu, và con người phải rà soát ở đâu?
- Làm sao bạn giữ thuật ngữ nhất quán qua nhiều ngôn ngữ và đội?
- Bao nhiêu điều chỉnh văn hóa khu vực đáng với việc duy trì thêm biến thể?
- Hỗ trợ phải-sang-trái và ngôn ngữ thiểu số nên được ưu tiên và kiểm thử thế nào?
- Làm sao bạn cho người dịch đủ ngữ cảnh mà không làm chậm đường ống?

## Những điểm cần ghi nhớ

- Quốc tế hóa kiến trúc một lần; địa phương hóa nội dung nhiều lần.
- Dùng Unicode ở mọi nơi, tách mọi chuỗi, và không bao giờ nối bản dịch.
- Lên kế hoạch cho sự giãn nở văn bản, chữ viết phải-sang-trái, và quy tắc số nhiều cùng định dạng đặc thù miền địa phương.
- Chạy một đường ống địa phương hóa liên tục với bộ nhớ dịch, bảng thuật ngữ và ngữ cảnh.
- Giả địa phương hóa sớm trong CI để bắt lỗi i18n trước khi dịch thật.
- Địa phương hóa là văn hóa, không chỉ ngôn ngữ.
- Quốc tế hóa sớm rẻ hơn nhiều so với trang bị bổ sung; với chính phủ nó là yêu cầu công bằng pháp lý.

## Tài liệu tham khảo và đọc thêm

- The Unicode Consortium, *The Unicode Standard* và Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, kỹ thuật và thực hành tốt nhất
- Richard Ishida, các bài viết và hướng dẫn quốc tế hóa của W3C
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (đánh dấu dữ liệu miền địa phương) và tài liệu thư viện ICU
- IETF BCP 47 language tags
- Hướng dẫn dịch vụ đa ngôn ngữ và tiếp cận ngôn ngữ của chính phủ
- Các bài viết của Nielsen Norman Group và W3C về RTL, giãn nở văn bản và UX địa phương hóa
