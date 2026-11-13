# 7.9 Quản lý dữ liệu chủ và dữ liệu tham chiếu

## Tổng quan và động lực

Hãy hỏi năm hệ thống tổ chức có bao nhiêu khách hàng, và bạn nhận được năm con số khác nhau. Một hệ thống đếm địa chỉ email, một đếm hợp đồng, một đếm lượt đăng nhập, và hai hệ thống bất đồng về việc "Acme Corp" và "ACME Corporation" có phải cùng một công ty hay không. [Quản lý dữ liệu chủ](https://en.wikipedia.org/wiki/Master_data_management) (MDM) là kỷ luật đối chiếu các thực thể cốt lõi mà doanh nghiệp dùng chung, khách hàng, sản phẩm, nhà cung cấp, nhân viên, địa điểm, thành một phiên bản có thẩm quyền duy nhất mà mọi hệ thống tin được.

Hãy bắt đầu bằng việc phân loại dữ liệu của bạn thành ba loại, vì chúng cần được đối xử khác nhau. Dữ liệu chủ mô tả các danh từ của doanh nghiệp: con người, địa điểm và sự vật mà nhiều quy trình tham chiếu. Dữ liệu tham chiếu là từ vựng được kiểm soát mà các quy trình đó dùng: mã tiền tệ, mã quốc gia, danh sách đơn vị đo, danh mục sản phẩm. Dữ liệu giao dịch ghi lại các động từ: một đơn hàng được đặt, một khoản thanh toán được thực hiện, một lô hàng được gửi. Dữ liệu chủ và dữ liệu tham chiếu có khối lượng thấp hơn giao dịch nhưng được tham chiếu ở khắp nơi, nên một lỗi trong chúng làm nhiễm mọi thứ hạ nguồn.

Chi phí của việc làm sai là cụ thể. Khi cùng một khách hàng tồn tại như bốn bản ghi hơi khác nhau, bạn gửi bốn cuốn catalog, bạn không thấy được một mối quan hệ đáng giữ, và con số doanh thu-trên-mỗi-khách-hàng của bạn lặng lẽ sai. Một [bản ghi vàng](https://en.wikipedia.org/wiki/Single_source_of_truth), phiên bản đáng tin duy nhất của một thực thể được lắp ráp từ nhiều nguồn, là thứ thay thế những bản sao xung đột đó, để mọi tích hợp thôi giải lại cùng một bài toán đối sánh.

Với các doanh nghiệp đối chiếu những hệ thống tích tụ qua nhiều thập kỷ tăng trưởng và mua lại, MDM là sự khác biệt giữa một cái nhìn khách hàng mạch lạc và một khoản thuế đối chiếu vĩnh viễn. Với chính phủ, rủi ro tăng lên: một công dân xuất hiện như ba người khác nhau ở ba cơ quan có thể bị từ chối một khoản trợ cấp, bị đánh thuế hai lần, hoặc lạc giữa các bộ. Chương này bổ sung cho chiến lược và quản trị dữ liệu (chương 7.1), đặt ra quyền sở hữu và chính sách; mô hình hóa dữ liệu và lớp ngữ nghĩa (chương 7.7), xác định các thực thể có nghĩa gì; và chất lượng cùng khả năng quan sát dữ liệu (chương 7.8), giữ bản ghi sạch theo thời gian.

## Các nguyên tắc chính

- Phân loại dữ liệu của bạn thành chủ, tham chiếu và giao dịch; mỗi loại cần xử lý khác nhau.
- Một bản ghi vàng cho mỗi thực thể thế giới thực, được lắp ráp có chủ đích, không phải khám phá tình cờ.
- Chọn kiểu kiến trúc MDM phù hợp nhu cầu kiểm soát và độ trễ của bạn, không theo mốt.
- Đối sánh và quyền sống sót là quy tắc kinh doanh, vì vậy hãy viết chúng ra và để quản lý viên điều chỉnh.
- Dữ liệu tham chiếu là từ vựng dùng chung; đánh phiên bản và công bố nó như một API.
- Quản trị và quản lý viên là động cơ của MDM; phần mềm chỉ là công cụ.
- Lan truyền bản ghi vàng dưới dạng sự kiện để các hệ thống hạ nguồn luôn đồng bộ, không cũ.
- Đo MDM bằng quyết định được cải thiện và bản trùng được loại bỏ, không phải bản ghi được tải.

## Khuyến nghị

### Phân loại dữ liệu chủ, tham chiếu và giao dịch trước

Bạn không quản lý được thứ bạn chưa phân loại, vì vậy hãy bắt đầu bằng việc phân loại các miền dữ liệu của bạn. Một phép thử hữu ích cho dữ liệu chủ là liệu một giá trị sai có lan truyền: nếu một địa chỉ xấu gợn sóng vào thanh toán, vận chuyển và thông báo pháp lý, bạn đang nhìn vào dữ liệu chủ. Điều này dẫn dắt khoản đầu tư của bạn: bạn xây công cụ đối sánh cho thực thể khách hàng, không phải dòng hàng của đơn hàng. Hãy gọi tên các miền tường minh, xếp hạng chúng theo mức đau mà sự trùng lặp gây ra, và bắt đầu với một hai cái đau nhất, thường là khách hàng và sản phẩm vì chúng chạm trực tiếp vào doanh thu.

### Chọn kiểu kiến trúc MDM có chủ đích

Có bốn kiểu kiến trúc phổ biến, và kiểu đúng phụ thuộc vào mức thẩm quyền bạn có thể tập trung hóa và thay đổi phải lan truyền nhanh đến đâu. Kiểu sổ đăng ký để dữ liệu trong hệ thống nguồn và chỉ xây một chỉ mục các định danh đã đối sánh, nên nó trả lời được "năm bản ghi này là cùng một khách hàng" mà không di chuyển dữ liệu nào; nó rẻ và ít rủi ro, nhưng chỉ đọc, nên không sửa được nguồn. Kiểu hợp nhất kéo các bản sao vào một trung tâm và gộp chúng thành bản ghi vàng cho báo cáo, nhưng không đẩy sửa chữa ngược lại, nên nguồn vẫn lộn xộn. Kiểu cùng tồn tại đi xa hơn: nó đồng bộ giá trị đã làm sạch trở lại hệ thống nguồn, để nguồn cải thiện theo thời gian trong khi vẫn hoạt động độc lập. Kiểu trung tâm tập trung hay giao dịch biến chính trung tâm MDM thành hệ thống ghi nhận, nơi các thực thể được tạo và sửa trực tiếp và mọi hệ thống khác tiêu thụ từ nó; điều này cho tính nhất quán và kiểm soát mạnh nhất, và là kiểu khó áp dụng nhất vì nó đổi nơi công việc diễn ra. Nhiều tổ chức tiến từ một sổ đăng ký chứng minh giá trị sang cùng tồn tại khi lòng tin lớn lên, và chạy nhiều hơn một kiểu qua các miền khác nhau.

### Đối sánh, gộp và đặt quy tắc quyền sống sót tường minh

Trái tim của MDM là quyết định khi nào hai bản ghi mô tả cùng một thứ thế giới thực. Đây là [liên kết bản ghi](https://en.wikipedia.org/wiki/Record_linkage), hiếm khi đơn giản như khớp khóa chính xác vì dữ liệu thật đầy lỗi gõ, viết tắt và trường thiếu. Đối sánh tất định dùng quy tắc chính xác trên các trường được chọn (cùng mã số thuế, hoặc cùng email cộng mã bưu chính). Đối sánh xác suất chấm điểm độ tương tự qua nhiều trường bằng [đối sánh chuỗi xấp xỉ](https://en.wikipedia.org/wiki/Approximate_string_matching) và trọng số, để "Bob Smith, 12 Main St" và "Robert Smith, 12 Main Street" có thể được đánh giá là khả năng khớp trên một ngưỡng. Quyết định bản ghi nào chỉ cùng một thực thể gọi là phân giải danh tính, và nó vận hành mọi thứ từ cái nhìn khách hàng đến phát hiện gian lận.

Khi các bản ghi khớp, bạn phải quyết định giá trị nào sống sót vào bản ghi vàng. Các quy tắc quyền sống sót này là logic kinh doanh, nên hãy làm chúng tường minh: ưu tiên giá trị gần nhất cho số điện thoại, giá trị đầy đủ nhất cho địa chỉ, nguồn đáng tin nhất cho tên pháp lý. Đặt một dải ngưỡng nơi các khớp được tự động gộp, một dải thấp hơn nơi chúng được tự động từ chối, và một dải giữa nơi con người quyết định, là nơi quản lý viên sống. Giữ mọi lần gộp đảo ngược được và ghi nhật ký, vì một lần gộp sai hợp nhất hai khách hàng thật còn tệ hơn một lần bỏ sót.

### Coi dữ liệu tham chiếu là từ vựng dùng chung có phiên bản

Dữ liệu tham chiếu là từ vựng dùng chung mà hệ thống của bạn nói, và từ vựng trôi gây lệch lạc thầm lặng: khi một hệ thống dùng mã quốc gia ISO "GB" và hệ thống khác dùng "UK," phép nối thất bại và số đếm phân kỳ. Hãy duy trì mỗi danh sách tham chiếu ở một nơi được quản trị, công bố nó cho mọi người tiêu dùng, và, quan trọng, đánh phiên bản nó. Mã được thêm, ngừng dùng, tách và gộp theo thời gian, và nếu bạn ghi đè danh sách tại chỗ, bạn phá hỏng báo cáo lịch sử vốn đúng theo các mã cũ.

Hãy coi một tập dữ liệu tham chiếu như một API với hợp đồng. Công bố nó với ngày có hiệu lực để người tiêu dùng hỏi được "mã khu vực hợp lệ vào ngày này là gì," giữ các mã đã ngừng dùng thay vì xóa chúng, và ghi lại ánh xạ khi một mã đổi nghĩa. Ưu tiên các tiêu chuẩn bên ngoài được công nhận nơi chúng tồn tại, như mã quốc gia và tiền tệ ISO, vì tiêu chuẩn cho bạn khả năng tương tác miễn phí và nối với kỷ luật tiêu chuẩn mở trong chương 3.8.

### Mô hình hóa phân cấp và quan hệ, không chỉ bản ghi phẳng

Dữ liệu chủ không phải đống hàng độc lập; nó là một mạng lưới quan hệ. Một khách hàng thuộc về một hộ gia đình và một công ty mẹ. Một sản phẩm gộp vào một danh mục và một thương hiệu. Các phân cấp này mang ý nghĩa kinh doanh thực: gộp doanh số theo công ty mẹ và bức tranh thay đổi hoàn toàn so với gộp theo từng tài khoản. Hãy mô hình hóa các quan hệ này tường minh để người tiêu dùng duyệt chúng nhất quán thay vì mỗi đội phát minh cách gộp riêng.

Hãy để ý trường hợp một thực thể cần nhiều phân cấp cùng lúc. Một sản phẩm có thể gộp theo một cách cho tài chính và cách khác cho kinh doanh hàng hóa, và cả hai đều chính đáng, nên hãy hỗ trợ nhiều phân cấp có tên thay vì ép một cây thật duy nhất. Quan hệ giữa các miền cũng quan trọng, như nhà cung cấp nào cung cấp sản phẩm nào.

### Nối bản ghi vàng vào lớp ngữ nghĩa và chất lượng dữ liệu

Các bản ghi vàng mà MDM tạo ra là những thực thể đáng tin mà lớp ngữ nghĩa của chương 7.7 tham chiếu khi nó xác định chỉ số: "khách hàng hoạt động" chỉ có nghĩa khi "khách hàng" không mơ hồ. Hãy nuôi bản ghi vàng của bạn vào lớp ngữ nghĩa để mọi chỉ số đếm cùng các thực thể đã loại trùng, đã phân giải.

MDM và chất lượng dữ liệu (chương 7.8) là hai mặt của một đồng xu: kiểm tra chất lượng phát hiện bản trùng, giá trị null và vi phạm định dạng mà MDM rồi phân giải, và việc đối sánh của MDM làm lộ vấn đề chất lượng mà các kiểm tra bỏ sót. Hãy chạy giám sát chất lượng liên tục trên dữ liệu chủ của bạn một cách riêng biệt: tỷ lệ trùng, phân phối độ tin cậy đối sánh, độ đầy đủ của các trường then chốt, và kích thước hàng đợi rà soát, để độ trôi nổi lên trước khi người tiêu dùng thấy.

### Lan truyền bản ghi vàng qua sự kiện

Một bản ghi vàng không hệ thống hạ nguồn nào thấy thì không giúp ai. Mẫu mạnh nhất là lan truyền hướng sự kiện: khi một thực thể được tạo, gộp hay sửa, trung tâm MDM xuất bản một sự kiện thay đổi, và các hệ thống đăng ký cập nhật bản sao cục bộ. Điều này xây trên [kiến trúc hướng sự kiện](https://en.wikipedia.org/wiki/Event-driven_architecture) và các mẫu luồng của chương 7.2, giữ hàng chục hệ thống nhất quán mà không cần đồng bộ lô qua đêm giòn khiến mọi người cũ một ngày.

Hãy xuất bản các sự kiện với đủ ngữ cảnh để hữu ích: định danh thực thể, cái gì thay đổi, các giá trị sống sót mới, và một phiên bản để người tiêu dùng sắp thứ tự cập nhật và phát hiện những cái họ bỏ lỡ. Làm người tiêu dùng lũy đẳng để phát lại một sự kiện không gây hại, và cung cấp một API cho các hệ thống không đăng ký được. Nguyên tắc từ kiến trúc dữ liệu và lưu trữ (chương 3.4) áp dụng: hãy thiết kế để bản ghi vàng chảy, vì một cái không ai tiêu thụ chỉ là một bảng tính đắt tiền.

### Giao quản lý viên và quản trị trước công cụ

MDM thất bại như một dự án công nghệ và thành công như một dự án quản trị. Vai trò then chốt là [quản lý viên dữ liệu](https://en.wikipedia.org/wiki/Data_steward), một người chịu trách nhiệm về chất lượng và quy tắc của một miền cụ thể, người giải quyết các khớp mơ hồ, điều chỉnh quy tắc quyền sống sót, và phân xử khi hai phòng ban bất đồng về "nhà cung cấp" nghĩa là gì. Quản lý viên thường là người làm kinh doanh có kiến thức miền sâu, không phải kỹ sư, và họ cần thẩm quyền thực và thời gian được phân bổ, vì quản lý bán thời gian không có nhiệm vụ tạo ra đúng sự trôi mà MDM định ngăn.

Hãy bọc quản lý viên trong cấu trúc quản trị từ chương 7.1: một chủ sở hữu dữ liệu chịu trách nhiệm cho mỗi miền, một hội đồng giải quyết tranh chấp xuyên miền, và chính sách rõ ràng về ai được tạo hay gộp bản ghi chủ. Lập tài liệu các quyết định, vì quy tắc đối sánh một khách hàng là tri thức thể chế phải sống sót qua luân chuyển nhân sự. Công cụ phục vụ quản trị; mua một nền tảng MDM trước khi bạn nêu tên quản lý viên là mua một động cơ không có người lái.

## Đánh đổi: ưu và nhược điểm

| Kiểu MDM | Ưu điểm | Nhược điểm |
|---|---|---|
| Sổ đăng ký (chỉ mục) | Rẻ, ít rủi ro, nguồn không bị chạm | Chỉ đọc; không sửa được dữ liệu nguồn |
| Hợp nhất (bản sao trung tâm) | Bản ghi sạch cho phân tích nhanh | Nguồn vẫn lộn xộn; không ghi ngược |
| Cùng tồn tại (đồng bộ ngược về nguồn) | Nguồn cải thiện; kiểm soát cân bằng | Tích hợp nhiều hơn; xung đột đồng bộ phải quản lý |
| Trung tâm tập trung / giao dịch | Nhất quán và kiểm soát mạnh nhất | Chi phí cao nhất; đổi nơi công việc diễn ra |
| Đối sánh tất định | Khả đoán, giải thích được, kiểm toán được | Bỏ sót lỗi gõ, biến thể và dữ liệu lộn xộn |
| Đối sánh xác suất | Bắt được biến thiên thực tế | Cần điều chỉnh; gộp sai nếu cẩu thả |

Căng thẳng trung tâm trong MDM là kiểm soát so với gián đoạn. Các kiểu cho dữ liệu sạch nhất, nhất quán nhất (cùng tồn tại và trung tâm tập trung) chính là những kiểu xâm phạm nhiều nhất cách hệ thống nguồn và chủ sở hữu của chúng làm việc, và sự xâm phạm đó là nơi các chương trình MDM đình trệ. Con đường thực dụng là giành lòng tin bằng kiểu ít rủi ro và tiến tới kiểm soát mạnh hơn chỉ nơi lập luận kinh doanh rõ ràng. Đánh đổi đối sánh chạy song song: quy tắc tất định kiểm toán được nhưng giòn, chấm điểm xác suất mạnh nhưng đòi quản lý viên và sự chịu đựng cho lần gộp sai thỉnh thoảng. Hầu hết chương trình trưởng thành pha trộn cả hai.

## Câu hỏi để thảo luận với đội của bạn

1. **Miền dữ liệu chủ nào thực sự gây đau cho chúng ta, và chúng ta đã xếp hạng chúng theo chi phí thay vì xử lý tất cả cùng lúc chưa?** Nhiều chương trình MDM sụp đổ dưới chính tham vọng của chúng, cố làm chủ mọi thực thể trong doanh nghiệp cùng lúc và không giao được gì trong hai năm. Nước đi hiệu quả là tìm một hai miền nơi sự trùng lặp và xung đột tốn bạn tiền hoặc lòng tin thật, thường là khách hàng hoặc sản phẩm, và định lượng chi phí đó: thư gửi lãng phí, giờ đối chiếu, con số doanh thu sai, phát hiện kiểm toán. Hãy mang ví dụ cụ thể về cùng một thực thể xuất hiện nhiều cách qua các hệ thống, và để thứ hạng đó cho bạn biết bắt đầu ở đâu, vì một chiến thắng hẹp, đo được xây dựng uy tín bạn cần để mở rộng.

2. **Ai sở hữu mỗi miền dữ liệu chủ, và quản lý viên của chúng ta có thẩm quyền và thời gian để thực sự làm việc không?** Công cụ MDM không có quản lý viên được trao quyền là một chiếc xe không người lái, và kiểu thất bại phổ biến nhất là nêu tên một quản lý viên trên slide trong khi không trao nhiệm vụ thực và giờ được phân bổ. Những người giải quyết khớp mơ hồ và dàn xếp tranh cãi "cái gì được tính là khách hàng" cần chuyên môn miền, thẩm quyền quyết định, và thời gian được bảo vệ. Hãy mang sơ đồ tổ chức và hỏi, với miền hàng đầu của bạn, chính xác ai quyết định khi hai bản ghi là cùng một người và ai phân xử khi bán hàng và tài chính bất đồng. Nếu bạn không nêu được người đó và chỉ ra thời gian được phân bổ của họ, bạn đã tìm thấy khoảng trống sẽ nhấn chìm chương trình.

3. **Khi chúng ta gộp hai bản ghi thành bản ghi vàng, chúng ta có giải thích và đảo ngược được quyết định không, và các giá trị sống sót đến từ đâu?** Quy tắc quyền sống sót là logic kinh doanh mà hầu hết đội chưa bao giờ viết ra, nghĩa là việc gộp xảy ra do ngẫu nhiên của thứ tự tải hoặc mặc định công cụ, và một lần gộp sai hợp nhất hai khách hàng thật rất đau để gỡ. Hãy mang một bản ghi đã gộp thật và truy từng trường sống sót về nguồn và quy tắc của nó: vì sao địa chỉ này, vì sao tên này, vì sao số điện thoại này. Xác nhận mọi lần gộp được ghi nhật ký và đảo ngược được, và một dải giữa các khớp không chắc chắn đi tới một con người thay vì tự động gộp. Nếu bạn không giải thích được một bản ghi vàng cụ thể, quản lý viên của bạn không bảo vệ nó được trước kiểm toán viên hay một khách hàng bị oan.

4. **Kiểu kiến trúc MDM nào phù hợp với mỗi miền chúng ta định làm chủ, và chúng ta có bảo vệ được lựa chọn đó trước sự gián đoạn nó áp đặt lên chủ sở hữu hệ thống nguồn không?** Kiểu bạn chọn quyết định bạn làm sạch dữ liệu được bao nhiêu và xâm phạm các đội sở hữu nguồn bao nhiêu, và chọn theo mốt hay lời chào của nhà cung cấp thay vì thực tế kiểm soát-so-với-gián-đoạn là cách các chương trình đình trệ giữa chừng. Một sổ đăng ký chứng minh giá trị rẻ nhưng không bao giờ sửa nguồn; một trung tâm tập trung cho tính nhất quán mạnh nhất nhưng dời nơi bản ghi được tạo, là một thay đổi tổ chức ngụy trang thành kỹ thuật. Hãy mang, cho mỗi miền ứng viên, một cái đọc trung thực về bạn thực sự có bao nhiêu thẩm quyền đối với chủ sở hữu nguồn, các bản sao hạ nguồn phải mới đến đâu, và việc ghi ngược sẽ làm hỏng gì trong quy trình hiện có. Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm chi phí di chuyển và quản lý thay đổi của việc dời hệ thống ghi nhận, vì các đội có công việc hằng ngày bị dời sẽ chống một trung tâm họ không được hỏi ý kiến, và một lần triển khai cùng tồn tại đình trệ đắt hơn một sổ đăng ký khiêm tốn mà phát hành được.

5. **Chúng ta điều chỉnh ngưỡng đối sánh thế nào, và chúng ta đã thống nhất tỷ lệ gộp sai và khớp bỏ sót mà chúng ta chịu được ở mỗi miền chưa?** Mọi công cụ đối sánh xác suất đánh đổi gộp sai (hợp nhất hai thực thể thật) với khớp bỏ sót (để một thực thể bị tách), và sự cân bằng là quyết định kinh doanh, không phải mặc định ai đó để lại trong công cụ. Đặt dải tự động gộp và tự động từ chối quá rộng và bạn làm hỏng bản ghi vàng thầm lặng; đặt quá hẹp và hàng đợi rà soát của con người lớn nhanh hơn quản lý viên dọn được. Hãy mang phân phối độ tin cậy hiện tại, kích thước và tuổi của hàng đợi rà soát, và các lỗi mẫu của cả hai loại để căn phòng thấy chi phí thật của mỗi hướng. Trong miền danh tính của chính phủ, hãy nghiêng mạnh về khớp bỏ sót và rà soát của con người, vì một lần gộp sai có thể từ chối một khoản trợ cấp hay phơi bày dữ liệu của một công dân cho người khác, và chi phí khiếu nại cùng kiểm toán của lỗi đó lấn át chi phí của một bản trùng mà quản lý viên giải quyết tuần sau.

6. **Các hệ thống hạ nguồn biết một bản ghi vàng thay đổi thế nào, và mỗi cái có thể cũ đến đâu trước khi một quyết định đi sai?** Một bản ghi vàng được phân giải hoàn hảo mà không hệ thống nào tiêu thụ là một bảng tính đắt tiền, và cơ chế lan truyền, dù là sự kiện thay đổi, API đăng ký hay lô qua đêm, lặng lẽ đặt mức hiện hành của mọi quyết định phụ thuộc. Lan truyền hướng sự kiện giữ hàng chục người tiêu dùng gần thời gian thực nhưng đòi người tiêu dùng lũy đẳng và sự kiện có phiên bản; đồng bộ qua đêm đơn giản hơn nhưng để mọi người cũ một ngày, có thể ổn cho danh sách tiếp thị và nguy hiểm cho kiểm tra gian lận. Hãy mang danh sách các hệ thống tiêu thụ, độ mới mỗi cái thực sự cần, và một người tiêu dùng bỏ lỡ một cập nhật hôm nay phục hồi thế nào. Với một tổ chức lớn hay công, hãy nêu ai sở hữu hợp đồng cho các sự kiện này và một người đăng ký phát hiện một thông điệp bị rơi thế nào, vì một thay đổi thực thể lặng lẽ không đến được một cơ quan tái tạo chính sự phân mảnh mà MDM được tài trợ để loại bỏ.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không có đường băng dư, đừng mua nền tảng MDM. Hãy làm chủ thực thể duy nhất đang làm hỏng con số của bạn, thường là khách hàng bị trùng giữa tự phục vụ và bán hàng, bằng một công việc đối sánh trong kho dữ liệu bạn đã chạy và một người rà soát các khớp không chắc chắn hằng tuần. Giữ mọi lần gộp được ghi nhật ký và đảo ngược được để một quy tắc tồi tốn một buổi chiều, không phải một mối quan hệ khách hàng, và chỉ xem xét lại công cụ nặng hơn khi hàng đợi rà soát thủ công vượt quá một người rà soát.

**Doanh nghiệp nhỏ.** Bạn không có quản lý viên dữ liệu và ngân sách eo hẹp, vì vậy hãy coi đây là quyết định mua-không-xây và dựa vào các tiêu chuẩn bạn nhận miễn phí. Ưu tiên các công cụ đã loại trùng liên hệ và nói mã quốc gia và tiền tệ ISO hơn là một trung tâm đặt riêng bạn không bảo trì nổi, và chọn một miền, thường là khách hàng hoặc sản phẩm, nơi bản trùng tốn bạn tiền thật. Giao trách nhiệm cho một chủ sở hữu có tên dù đó chỉ là một phần nhỏ tuần làm việc của một người, vì từ vựng trôi mà không ai theo dõi là thứ lặng lẽ làm hỏng báo cáo của bạn.

**Doanh nghiệp lớn.** Qua cả chục hệ thống ERP và CRM tích tụ qua mua lại, công việc là quản trị danh mục: xếp hạng các miền theo chi phí trùng lặp của chúng, dựng quản lý viên được trao quyền trong kinh doanh, và chuẩn hóa quy tắc quyền sống sót và đánh phiên bản dữ liệu tham chiếu để các nhóm thôi giải lại cùng bài toán đối sánh. Lập ngân sách tường minh cho chi phí tích hợp và quản lý viên thường trực, lan truyền bản ghi vàng như sự kiện có phiên bản để nguồn cải thiện theo thời gian, và quản lý MDM như một chương trình được đo với tỷ lệ trùng và chỉ số hàng đợi rà soát thay vì dọn dẹp một lần.

**Chính phủ.** Quy tắc mua sắm, luật chia sẻ dữ liệu nghiêm ngặt và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy khóa thực thể người theo một định danh quốc gia được quản trị, đánh phiên bản dữ liệu tham chiếu theo ngày có hiệu lực để bản ghi lịch sử vẫn đúng, và làm phân giải danh tính thận trọng có chủ đích: các khớp không chắc chắn đi tới quản lý viên được đào tạo, không bao giờ gộp tự động, vì một lần gộp sai có thể từ chối một khoản trợ cấp hay làm rò dữ liệu của một công dân cho người khác. Ghi nhật ký mọi lần khớp cho kiểm toán và khiếu nại, đòi khả năng di chuyển dữ liệu và logic đối sánh được tiết lộ từ nhà cung cấp, và giữ toàn bộ năng lực trong các tiêu chuẩn khả năng tương tác mà khu vực công đã cam kết.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty phần mềm tăng trưởng nhanh bán qua cả đăng ký tự phục vụ và đội bán hàng, và hai kênh tạo cùng một khách hàng hai lần dưới tên công ty hơi khác nhau. Doanh thu-trên-mỗi-tài-khoản trông sai và đội bán hàng cứ gọi lạnh những người dùng hiện có. Thay vì mua một nền tảng nặng, họ bắt đầu với một sổ đăng ký nhẹ: một công việc đối sánh trong kho dữ liệu liên kết bản ghi theo miền email và tên công ty đã chuẩn hóa, với một quản lý viên bán thời gian rà soát các khớp không chắc chắn hằng tuần. Nó tốn ít, sửa lỗi báo cáo, và chứng minh giá trị biện minh cho thêm đầu tư khi họ lớn lên.

**Doanh nghiệp lớn.** Một nhà sản xuất toàn cầu lớn lên qua mua lại và chạy cả chục hệ thống ERP và CRM, mỗi cái có bản ghi nhà cung cấp riêng, nên cùng một nhà cung cấp xuất hiện mười lăm cách và công ty không thương lượng được như một người mua duy nhất hay thấy được chi tiêu thực. Họ dựng một trung tâm MDM kiểu cùng tồn tại cho các miền nhà cung cấp và sản phẩm, dùng đối sánh tất định trên mã số thuế và đăng ký cộng chấm điểm xác suất trên tên và địa chỉ. Quản lý viên có tên trong mua sắm điều chỉnh quy tắc quyền sống sót và xử lý hàng đợi rà soát, và bản ghi vàng được xuất bản như sự kiện thay đổi chảy ngược vào mọi ERP để dữ liệu đã làm sạch cải thiện nguồn. Khả năng nhìn thấy chi tiêu hợp nhất mở ra điều khoản hợp đồng tốt hơn, và khoản thuế đối chiếu từng ngốn tài chính mỗi quý giảm mạnh.

**Chính phủ.** Một chính phủ quốc gia muốn các cơ quan coi một công dân là một người thay vì một người lạ ở mỗi quầy, trong khi tôn trọng các giới hạn pháp lý nghiêm ngặt về chia sẻ dữ liệu. Họ xây một trung tâm dữ liệu chủ tập trung cho thực thể người, khóa theo một định danh quốc gia được quản trị, với dữ liệu tham chiếu được đánh phiên bản theo ngày có hiệu lực để bản ghi lịch sử vẫn đúng. Phân giải danh tính thận trọng có chủ đích: các khớp không chắc chắn đi tới quản lý viên được đào tạo thay vì gộp tự động, vì một lần gộp sai có thể từ chối ai đó một khoản trợ cấp hay phơi bày dữ liệu của họ, và mọi lần khớp được ghi nhật ký cho kiểm toán và khiếu nại. Lợi ích là ít bản ghi trùng hơn, ít gian lận hơn từ danh tính bị tách, và một công dân không phải chứng minh mình là ai ở mỗi cửa, trong các tiêu chuẩn khả năng tương tác của chương 3.8.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của MDM đến từ việc loại bỏ một khoản thuế mà hầu hết tổ chức trả mà không gọi tên. Bản ghi trùng và xung đột tốn tiền theo những cách hiển nhiên (tiếp thị lãng phí cho cùng một người năm lần, lỗi vận chuyển từ địa chỉ cũ, bỏ lỡ chiết khấu khối lượng) và theo những cách kém hiển nhiên (nhà phân tích đối chiếu số đếm, giám đốc quyết định trên những con số lặng lẽ sai, kiểm toán viên tính giờ để gỡ xem bản ghi nào là thật). Một cái nhìn nhà cung cấp hợp nhất thường tự trả giá cho cả chương trình chỉ nhờ điều khoản hợp đồng tốt hơn.

Tổng chi phí sở hữu có ba phần: nền tảng hoặc xây dựng, tích hợp với nguồn và người tiêu dùng, và, lớn nhất về lâu dài, quản lý viên liên tục. Chi phí tích hợp dễ bị đánh giá thấp, vì nối cả chục hệ thống nguồn cũ là nơi các chương trình MDM chảy máu lịch trình và ngân sách, và chi phí quản lý viên dễ bị quên, vì nó là chi phí vận hành thường trực, không phải xây một lần. Để lập luận với ban lãnh đạo, hãy gắn MDM với các con số họ đã theo dõi: độ chính xác doanh thu, hiệu quả tiếp thị, tiết kiệm mua sắm, chi phí kiểm toán và rủi ro quy định, rồi bắt đầu hẹp và để một chiến thắng đo được trên một miền đau cao tài trợ cho việc mở rộng.

## Phản mẫu và cạm bẫy

- **Phạm vi đun sôi đại dương:** làm chủ mọi miền cùng lúc, không giao được gì trong nhiều năm, và mất sự bảo trợ trước chiến thắng đầu tiên.
- **Công cụ trước quản trị:** mua nền tảng MDM trước khi nêu tên quản lý viên và chủ sở hữu, nên động cơ không có người lái.
- **Quản lý viên bán thời gian không thẩm quyền:** giao quản lý trên slide mà không trao nhiệm vụ thực hay thời gian được bảo vệ.
- **Quyền sống sót thầm lặng:** gộp bản ghi theo mặc định công cụ hay thứ tự tải, không có quy tắc bằng văn bản và không cách giải thích một bản ghi vàng.
- **Gộp không đảo ngược:** tự động gộp các khớp không chắc chắn không có hoàn tác, nên một lần hợp nhất sai hai thực thể thật thành thiệt hại vĩnh viễn.
- **Dữ liệu tham chiếu bị ghi đè tại chỗ:** sửa danh sách mã mà không đánh phiên bản, phá hỏng mọi báo cáo lịch sử vốn đúng theo các mã cũ.
- **Bản ghi vàng không ai tiêu thụ:** xây một trung tâm nguyên sơ mà không hệ thống hạ nguồn nào đăng ký, nên dữ liệu sạch không bao giờ đến quyết định.
- **Phát minh lại mã chuẩn:** tự tạo danh sách quốc gia hay tiền tệ khi tiêu chuẩn ISO tồn tại, và mất khả năng tương tác vô cớ.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Dữ liệu chủ và tham chiếu không được quản lý. Cùng một thực thể tồn tại nhiều lần không có phiên bản có thẩm quyền, danh sách mã phân kỳ, đối sánh thủ công và phản ứng, và không ai sở hữu vấn đề, nên số đếm các thực thể cốt lõi bất đồng và không ai nói được cái nào đúng.
- **Mức 2, Phát triển:** Các miền chính được nhận ra và ai đó loại trùng chúng, thường trong kho dữ liệu cho báo cáo. Đối sánh tất định cơ bản tồn tại, danh sách tham chiếu được thu thập, và vài người làm quản lý viên không chính thức, nhưng thực hành khác nhau theo từng đội, nguồn vẫn lộn xộn, và quy tắc sống trong đầu người thay vì trên giấy.
- **Mức 3, Chuẩn hóa:** MDM là chương trình được quản trị áp dụng nhất quán toàn tổ chức. Các miền chủ có chủ sở hữu có tên và quản lý viên được trao quyền, quy tắc đối sánh và quyền sống sót được lập tài liệu và thực thi, bản ghi vàng được tạo và lan truyền đến người tiêu dùng, và dữ liệu tham chiếu được đánh phiên bản và công bố với ngày có hiệu lực như một API.
- **Mức 4, Quản lý:** Chương trình được đo và kiểm soát theo đường cơ sở. Tỷ lệ trùng, phân phối độ tin cậy đối sánh, tỷ lệ gộp sai và khớp bỏ sót, độ đầy đủ của trường then chốt, và kích thước cùng tuổi của hàng đợi rà soát được theo dõi như chỉ số; ngưỡng được điều chỉnh theo các con số đó thay vì theo cảm giác; và giá trị MDM (độ chính xác doanh thu, tiết kiệm mua sắm, chi phí rà soát) được định lượng và báo cáo cho chủ sở hữu theo nhịp cố định.
- **Mức 5, Điều phối:** Bản ghi vàng chảy như sự kiện có phiên bản gần thời gian thực, nuôi lớp ngữ nghĩa, và được tin cậy toàn tổ chức. Đối sánh được cải thiện liên tục theo kết quả đo được, việc làm chủ mở rộng sang miền mới như một năng lực lặp lại được, và MDM được tích hợp với quản trị và hoạch định rủi ro để chương trình thích ứng khi nguồn, tiêu chuẩn và bối cảnh thực thể dịch chuyển.

## Ý tưởng để thảo luận

1. Nếu hai hệ thống của bạn bất đồng về việc bạn có bao nhiêu khách hàng, cái nào đúng, và bạn chứng minh thế nào?
2. Miền dữ liệu chủ nào sẽ mang lại chiến thắng đo được lớn nhất nếu bạn làm chủ nó trước, và chiến thắng đó đáng giá bao nhiêu?
3. Đối sánh xác suất sẽ giúp bạn ở đâu hôm nay, và bạn có thoải mái với lần gộp sai thỉnh thoảng nó hàm ý không?
4. Bạn đánh phiên bản dữ liệu tham chiếu thế nào, và cái gì hỏng trong báo cáo lịch sử của bạn khi một mã đổi nghĩa?
5. Ai là quản lý viên có tên cho thực thể quan trọng nhất của bạn, và họ có thẩm quyền cùng thời gian để thực sự làm việc không?
6. Khi một bản ghi vàng thay đổi, các hệ thống hạ nguồn của bạn biết thế nào, và chúng có thể cũ đến đâu trước khi gây đau?

## Những điểm cần ghi nhớ

- Phân loại dữ liệu của bạn thành chủ, tham chiếu và giao dịch; đầu tư đối sánh và quản trị nơi sự trùng lặp tốn nhất.
- Tạo một bản ghi vàng cho mỗi thực thể thế giới thực, được lắp ráp bằng quy tắc quyền sống sót tường minh, đảo ngược được, có nhật ký.
- Chọn kiểu kiến trúc MDM (sổ đăng ký, hợp nhất, cùng tồn tại hay trung tâm tập trung) để phù hợp khẩu vị kiểm soát và gián đoạn của bạn.
- Coi dữ liệu tham chiếu là từ vựng dùng chung có phiên bản, ưu tiên tiêu chuẩn được công nhận, và đừng bao giờ ghi đè danh sách mã tại chỗ.
- MDM thành công nhờ quản trị và quản lý viên, không phải công cụ; lan truyền bản ghi vàng như sự kiện và đo chương trình bằng quyết định được cải thiện.

## Tài liệu tham khảo và đọc thêm

- David Loshin, *Master Data Management*
- Alex Berson và Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi và Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball và Margy Ross, *The Data Warehouse Toolkit*
