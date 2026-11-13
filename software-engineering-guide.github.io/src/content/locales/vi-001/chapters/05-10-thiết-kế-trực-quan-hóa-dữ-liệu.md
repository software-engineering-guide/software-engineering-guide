# 5.10 Thiết kế trực quan hóa dữ liệu

## Tổng quan và động lực

Một biểu đồ là một lập luận làm bằng mực. Khi bạn vẽ dữ liệu, bạn đang chọn điều người đọc sẽ chú ý đầu tiên, điều họ sẽ so sánh, và kết luận họ sẽ đi đến trong hai giây trước khi chuyển sang việc khác. Làm tốt thì một câu hỏi khó tự trả lời: xu hướng hiển nhiên, giá trị ngoại lai nhảy ra, hai nhóm khác nhau rõ ràng. Làm tồi thì cùng dữ liệu đó gây hiểu lầm, rối rắm, hoặc đơn giản là nhàm chán, và quyết định nó định giúp thông tin được đưa ra bằng cảm tính. [Trực quan hóa dữ liệu](https://en.wikipedia.org/wiki/Data_and_information_visualization) là nghề thiết kế biến những con số thành hình ảnh để người ta thấy được các con số có nghĩa gì.

Chương này nói về nghề đó: chọn đúng biểu đồ, mã hóa dữ liệu trung thực, dùng màu sắc và bố cục để mắt rơi đúng chỗ, và giữ toàn bộ dễ tiếp cận. Nó nằm trong Phần 5 vì một biểu đồ là một giao diện, và nó thừa hưởng mọi thứ từ phần còn lại của phần này. Nó xây trên nền tảng [trải nghiệm người dùng](https://en.wikipedia.org/wiki/User_experience) (UX) của chương 5.1, mượn token và thành phần từ hệ thống thiết kế của chương 5.2, phải đáp ứng nghĩa vụ khả năng tiếp cận của chương 5.3, và nói bằng giọng giản dị, có mục đích của thiết kế nội dung trong chương 5.4. Nó cố ý tránh phần đường ống. Các đường ống dữ liệu, kho dữ liệu và công cụ báo cáo của phân tích và trí tuệ kinh doanh (chương 7.3) là một chủ đề khác, cũng như khoa học quyết định và văn hóa dữ liệu rộng hơn của chương 7.5. Ở đây bạn học cách làm cho bức tranh tốt, dù dữ liệu đến từ đâu.

Với các đội lớn, rủi ro là phối hợp và niềm tin. Khi mỗi nhóm tự tạo kiểu biểu đồ của mình, một công ty kết thúc với năm mươi phương ngữ của "doanh thu theo thời gian," mỗi cái có trục, màu và làm tròn khác nhau, và các giám đốc học cách không tin tất cả. Trong bối cảnh doanh nghiệp, một bảng điều khiển gây hiểu lầm đẩy ngân sách thật đi sai hướng. Trong chính phủ, một biểu đồ công khai là một hành động giao tiếp với công dân và là vấn đề của truyền thông với các bên liên quan trong chương 10.16: một trục bị cắt cụt trên một đồ họa y tế công cộng có thể gây hoảng loạn hoặc trấn an sai cho hàng triệu người, và khả năng tiếp cận là nghĩa vụ pháp lý, không phải sở thích. Thiết kế trực quan hóa tốt là cách dữ liệu giành được quyền được tin.

## Các nguyên tắc chính

- Bắt đầu từ câu hỏi người đọc có, rồi chọn biểu đồ trả lời nó.
- Khớp mã hóa trực quan với kiểu dữ liệu: vị trí cho so sánh chính xác, sắc độ cho danh mục.
- Tối đa hóa tỷ lệ mực mang dữ liệu; xóa trang trí không mang gì.
- Dùng thuộc tính tiền chú ý có chủ đích để mắt rơi vào điểm cần thấy trước.
- Chọn bảng màu theo vai trò dữ liệu (tuần tự, phân kỳ, danh mục) và giữ chúng an toàn cho người mù màu.
- Không bao giờ chỉ dựa vào màu sắc; cung cấp văn bản, cấu trúc và bảng dự phòng.
- Nói sự thật về thang đo: không cắt cụt trục, không diện tích gây hiểu lầm, không trục kép vô cớ.
- Chú thích hiểu biết; đừng bắt người đọc đi tìm nó.

## Khuyến nghị

### Bắt đầu từ câu hỏi, rồi chọn biểu đồ

Mọi biểu đồ tốt bắt đầu bằng một câu hỏi, không phải một tập dữ liệu. Trước khi với tới một loại biểu đồ, hãy nêu câu hỏi của người đọc trong một câu, rồi khớp nó với một nhiệm vụ. So sánh ("cái nào lớn hơn?") cần một [biểu đồ cột](https://en.wikipedia.org/wiki/Bar_chart), nơi độ dài nằm trên một đường cơ sở chung và mắt xếp hạng chúng không tốn sức. Xu hướng theo thời gian ("nó đang đi hướng nào?") cần một [biểu đồ đường](https://en.wikipedia.org/wiki/Line_chart), vì một đường nối liền được đọc là thay đổi liên tục. Phân phối ("nó phân bố thế nào?") cần biểu đồ tần suất hoặc biểu đồ hộp, cho thấy hình dạng, tâm và giá trị ngoại lai. Bộ phận-trên-tổng thể ("mỗi phần chiếm bao nhiêu?") thường được phục vụ tốt hơn bằng cột chồng so với tròn, vì người ta so sánh độ dài chính xác hơn nhiều so với góc; hãy dành [biểu đồ tròn](https://en.wikipedia.org/wiki/Pie_chart) cho hai hoặc ba lát nơi sự chia tách là toàn bộ câu chuyện. Quan hệ ("hai thứ này có di chuyển cùng nhau không?") cần một [biểu đồ phân tán](https://en.wikipedia.org/wiki/Scatter_plot), biểu đồ duy nhất phơi bày tương quan và cụm trong nháy mắt.

Kỷ luật là để câu hỏi chọn biểu đồ, không bao giờ ngược lại. Một loại biểu đồ được chọn vì trông ấn tượng (một biểu đồ tròn 3D bung ra, một biểu đồ radar, một vành khuyên với con số ở giữa lỗ) là quyết định đưa ra vì lợi ích của nhà thiết kế, không phải người đọc. Khi một bảng trả lời câu hỏi nhanh hơn (người đọc cần số chính xác cho bốn hàng không cần biểu đồ), hãy dùng bảng. Biểu đồ chỉ được biện minh khi một bức tranh phơi bày một mẫu mà các chữ số trên lưới sẽ che giấu.

### Khớp mã hóa trực quan với dữ liệu

Một biểu đồ hoạt động bằng cách ánh xạ dữ liệu sang thuộc tính trực quan, và các thuộc tính đó không bằng nhau. Nhiều thập kỷ nghiên cứu nhận thức xếp hạng chúng. Vị trí trên một thang chung là kênh chính xác nhất con người có, đó là lý do cột và chấm trên một trục chung thắng mọi thứ khác về so sánh. Độ dài đến kế tiếp, rồi góc và độ dốc, rồi diện tích, rồi cường độ màu, và cuối cùng sắc độ, gần như vô dụng để đánh giá số lượng nhưng tuyệt vời để gắn nhãn danh mục. Hãy dành kênh chính xác nhất của bạn cho đại lượng quan trọng nhất.

Hãy khớp kênh với kiểu dữ liệu nữa. Dữ liệu định lượng (số đếm, số tiền, thời lượng) thuộc về vị trí, độ dài, hoặc một dải màu tuần tự. Dữ liệu thứ tự (nhỏ, vừa, lớn) có thể dùng kích thước có thứ tự hoặc dải từ sáng đến tối. Dữ liệu danh mục (khu vực, dòng sản phẩm, đảng phái) thuộc về sắc độ hoặc hình dạng, không bao giờ về kích thước ngụ ý một danh mục "nhiều hơn" cái khác. Lỗi kinh điển là mã hóa một danh mục bằng cầu vồng để mắt người đọc tự bịa ra một thứ tự mà dữ liệu không có. Hãy mã hóa số lượng nơi mắt đọc số lượng, và danh tính nơi mắt đọc danh tính.

### Theo đuổi sự xuất sắc đồ họa: tối đa hóa mực dữ liệu

Edward Tufte đã trao cho trực quan hóa đạo đức thiết kế rõ ràng nhất, và đáng để thấm nhuần. Thước đo trung tâm của ông là [tỷ lệ mực-dữ liệu](https://en.wikipedia.org/wiki/Data-ink_ratio): trong tất cả mực (hay điểm ảnh) trên trang, phần nào thực sự mã hóa dữ liệu? Mọi thứ còn lại (đường lưới đậm, viền khung, đổ bóng, tô nền, chú giải thừa, 3D trang trí) là thuế đánh vào sự chú ý của người đọc. Tufte gọi sự trang trí này là rác biểu đồ, và chỉ dẫn thẳng thừng: hãy xóa nó. Làm nhạt đường lưới đến khi chúng thì thầm, bỏ viền biểu đồ, gắn nhãn dữ liệu trực tiếp thay vì buộc phải ghé chú giải, và để dữ liệu đứng gần như một mình. Một biểu đồ hoàn thành không phải khi không còn gì để thêm mà khi không còn gì để bỏ mà không mất nghĩa.

Một ý tưởng của Tufte đáng được nhắc đặc biệt cho các đội: bội số nhỏ. Thay vì nhồi tám chuỗi vào một biểu đồ đường rối, hãy vẽ tám biểu đồ nhỏ trong một lưới, mỗi cái có cùng trục và thang, mỗi chuỗi một cái. Mắt quét lưới và phát hiện cái khác thường ngay lập tức, vì mọi ô đều so sánh trực tiếp được. Bội số nhỏ biến "quá nhiều đường để đọc" thành "một trang bạn lướt được," và chúng mở rộng tốt hơn nhiều so với việc chất thêm màu và thêm mục chú giải lên một biểu đồ quá tải.

### Dùng thuộc tính tiền chú ý và phân cấp trực quan

Một số khác biệt trực quan được ghi nhận trước sự chú ý có ý thức, trong một phần giây, mà người đọc không "tìm" chúng. Những thuộc tính tiền chú ý này (một chấm đỏ giữa những chấm xám, một cột dài hơn, một mục tách riêng trong không gian) là công cụ mạnh nhất bạn có để hướng mắt. Hãy dùng chúng có chủ đích. Nếu điểm của biểu đồ là một khu vực đang tụt lại, hãy tô màu khu vực đó và làm xám phần còn lại; người đọc thấy thông điệp trước khi đọc tiêu đề. Nếu mọi thứ đều sáng và đậm thì không có gì nổi, vì tương phản là tương đối và một trang đầy nhấn mạnh là một trang đầy nhiễu.

Đây là phân cấp trực quan áp dụng cho dữ liệu: quyết định một điều người đọc nên chú ý đầu tiên, và dành tín hiệu mạnh nhất của bạn ở đó. Tiêu đề và chú thích nêu điều rút ra bằng lời. Màu sắc và độ đậm chỉ vào bằng chứng. Mọi thứ phụ trợ (trục, đường lưới, chuỗi thứ yếu) lùi về màu xám để tiền cảnh lên tiếng. Một biểu đồ không có phân cấp yêu cầu người đọc làm việc của nhà thiết kế là tìm ra cái gì quan trọng.

### Chọn màu theo vai trò, và làm cho nó an toàn với người mù màu

Màu sắc là kênh bị dùng sai nhiều nhất, nên hãy coi nó là một hệ thống với ba họ. Bảng màu tuần tự chạy từ sáng đến tối trong một sắc độ và mã hóa số lượng đi từ thấp đến cao (mật độ dân số, doanh thu). Bảng màu phân kỳ có hai sắc độ gặp nhau ở một điểm giữa trung tính và mã hóa độ lệch khỏi một tâm (dị thường nhiệt độ, lãi và lỗ quanh số không, mức đồng ý khảo sát quanh trung lập). Bảng màu danh mục là một tập sắc độ riêng biệt để gắn nhãn các nhóm không có thứ tự; hãy giữ nó ở khoảng bảy màu, vì hơn thế người đọc không phân biệt được. Chọn sai họ (cầu vồng danh mục cho một số lượng, dải tuần tự cho các danh mục không thứ tự) chống lại nhận thức của người đọc.

Rồi làm cho nó dễ tiếp cận, vì khoảng một trong mười hai nam giới có một dạng [mù màu](https://en.wikipedia.org/wiki/Color_blindness). Đỏ và xanh lá là cái bẫy kinh điển: một biểu đồ đỏ-xấu, xanh-tốt vô hình với dạng khiếm khuyết phổ biến nhất. Hãy chọn bảng màu an toàn cho người mù màu (các lược đồ phân kỳ xanh dương-cam và các bộ danh mục được kiểm thử kỹ từ công cụ như ColorBrewer là điểm khởi đầu an toàn), và xác minh bằng cách mô phỏng các khiếm khuyết thường gặp trước khi phát hành. Kiểm tra cả độ tương phản, để văn bản và dấu hiệu đạt các tỷ lệ yêu cầu bởi tiêu chuẩn khả năng tiếp cận trong chương 5.3. Màu sắc nên củng cố một thông điệp vốn đã sống sót không cần nó.

### Không chỉ dựa vào màu sắc; cung cấp lựa chọn thay thế

Khả năng tiếp cận trong trực quan hóa dữ liệu vượt ra ngoài việc chọn bảng màu. Quy tắc cốt lõi từ [Hướng dẫn Khả năng Tiếp cận Nội dung Web](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) là màu sắc không bao giờ được là cách duy nhất truyền thông tin. Vậy hãy ghép màu với một dấu hiệu thứ hai: nhãn trực tiếp, hình dạng hay điểm đánh dấu riêng biệt trên biểu đồ phân tán, kiểu đường khác nhau (liền, đứt nét) trên biểu đồ đường, hoặc một nhãn văn bản trên cột quan trọng. Một người đọc không phân biệt được sắc độ của bạn vẫn nên nhận được trọn thông điệp từ mã hóa dư thừa.

Hãy cung cấp một văn bản thay thế thật sự và một phương án dự phòng. Một ảnh biểu đồ cần alt text nêu điều rút ra, không phải "biểu đồ doanh số," và một mô tả dài hơn hoặc chú thích gọi tên xu hướng. Bất cứ nơi nào khả thi, hãy cung cấp dữ liệu nền dưới dạng một bảng dễ tiếp cận, để người dùng trình đọc màn hình và nhà phân tích quen bảng tính đều nhận được các con số trực tiếp. Điều này phản chiếu kỷ luật "giải một lần trong một thành phần" của chương 5.2: hãy xây các thành phần biểu đồ dễ tiếp cận với vai trò đúng, tiêu điểm bàn phím cho phần tử tương tác, và chế độ xem bảng tích hợp sẵn, để mọi đội thừa hưởng khả năng tiếp cận thay vì phát minh lại cho từng bảng điều khiển.

### Biết bạn đang khám phá, giải thích, hay giám sát

Biểu đồ phục vụ ba việc khác nhau, và nhầm chúng tạo ra công việc tồi. Trực quan hóa khám phá dành cho bạn, nhà phân tích, săn tìm điều thú vị trong dữ liệu; nó có thể nhanh, dày đặc và xấu, vì khán giả là một chuyên gia sẽ lặp lại. Trực quan hóa giải thích dành cho một khán giả, truyền đạt một phát hiện cụ thể bạn đã hiểu; nó có chủ đích, được chú thích, và lột còn một thông điệp duy nhất, và nó thuộc về kể chuyện của chương 10.16. Một bảng điều khiển là điều thứ ba: một màn hình bền vững, nhìn lướt được để giám sát các chỉ số đã biết theo thời gian, tối ưu cho "có gì sai ngay bây giờ không?" thay vì cho một lập luận một lần.

Hãy khớp thiết kế với công việc. Một biểu đồ giải thích với tiêu đề và một chuỗi được tô sáng là sai cho một bảng điều khiển giám sát, nơi người đọc cần nhiều chỉ số trong nháy mắt và vị trí nhất quán để mắt họ học được bố cục. Một bảng điều khiển nhồi chú thích tường thuật thì mệt mỏi để kiểm tra mỗi sáng. Và một sổ tay khám phá đầy các biểu đồ thô không bao giờ nên được trao cho giám đốc như thể đó là lời giải thích. Hãy quyết định công việc trước; thiết kế theo sau.

### Đừng bao giờ gây hiểu lầm: thang trung thực, diện tích trung thực

Cách nhanh nhất để phá hủy niềm tin là một biểu đồ nói dối trong khi trông thật thà. Lời nói dối phổ biến nhất là trục bị cắt cụt: bắt đầu trục y của biểu đồ cột ở 90 thay vì 0 biến chênh lệch 2% thành vách đá, vì độ dài cột không còn ánh xạ với giá trị. Cột phải bắt đầu từ số không, luôn luôn; biểu đồ đường, mã hóa thay đổi thay vì độ lớn, có thể dùng đường cơ sở khác không nếu bạn ghi nhãn rõ. Cái bẫy thứ hai là trục kép: hai thang y trên một biểu đồ cho phép bạn chế ra bất kỳ tương quan nào bạn muốn bằng cách trượt các thang, và người đọc hiếm khi nhận ra. Hãy ưu tiên hai biểu đồ căn thẳng hàng hoặc một chế độ xem chỉ số hóa. Cái thứ ba là diện tích gây hiểu lầm: khi bạn co giãn một biểu tượng hoặc bong bóng theo cả chiều rộng và chiều cao để biểu diễn một giá trị, diện tích tăng theo bình phương và phóng đại chênh lệch dữ dội; hãy co giãn theo diện tích, không phải theo chiều dài cạnh.

Hãy coi những điều này là quy tắc liêm chính, không phải sở thích phong cách. Một biểu đồ là một tuyên bố bạn yêu cầu người đọc tin, và mỗi biến dạng này khai thác cách nhận thức hoạt động để làm một thứ nhỏ trông lớn hay một thứ không liên quan trông có liên hệ. Các ví dụ chính phủ và doanh nghiệp dưới đây cho thấy sự phản bội đó tốn kém thế nào khi khán giả là công chúng hay hội đồng quản trị.

### Chú thích hiểu biết và thêm tương tác có kiềm chế

Một biểu đồ bắt người đọc tự tìm điểm mới xong một nửa. Hãy chú thích nó: một tiêu đề nêu phát hiện ("Đăng ký tăng gấp đôi sau đợt ra mắt tháng Ba") thay vì chủ đề ("Đăng ký theo thời gian"), một ghi chú trên sự kiện then chốt, một đường tham chiếu cho mục tiêu hay trung bình. Chú thích là nơi thiết kế trong chương 5.4 gặp bức tranh; lời nói mang lập luận và dấu hiệu cung cấp bằng chứng.

Tương tác chỉ xứng đáng có chỗ khi nó trả lời một câu hỏi theo dõi thực. Chú giải công cụ cho giá trị chính xác, lọc theo phân khúc, và đào sâu vào chi tiết đều giúp ích khi người đọc có câu hỏi kế tiếp mà biểu đồ tĩnh không chứa nổi. Nhưng tương tác là một chi phí: nó giấu thông tin sau một lần di chuột, hỏng trên cảm ứng và với người dùng bàn phím, và có thể kéo hiệu năng xuống mức bò. Trên web, hãy theo dõi ngân sách kết xuất từ chương 5.6: hàng chục nghìn điểm cần canvas hoặc một chế độ xem gộp, không phải hàng chục nghìn phần tử tài liệu riêng lẻ. Hãy làm chế độ xem tĩnh mặc định kể trọn câu chuyện cốt lõi, và để tương tác tiết lộ chiều sâu bên dưới.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Xây trực quan hóa trong sản phẩm của bạn | Kiểm soát đầy đủ thiết kế, khả năng tiếp cận, tương tác | Tốn thời gian kỹ thuật; bạn sở hữu hiệu năng và bảo trì |
| Dùng biểu đồ của công cụ BI | Nhanh, rẻ, nối với kho dữ liệu | Diện mạo chung chung; kiểm soát khả năng tiếp cận và chú thích hạn chế |
| Biểu đồ tương tác | Trả lời câu hỏi theo dõi; khám phá tại chỗ | Chậm hơn, khó làm dễ tiếp cận hơn, hỏng khi in và cảm ứng |
| Biểu đồ tĩnh | Nhanh, dễ tiếp cận, sẵn sàng in, không mơ hồ | Không trả lời được câu hỏi kế tiếp của người đọc |
| Bảng điều khiển | Giám sát nhìn lướt được nhiều chỉ số đã biết | Kém cho lập luận một lần; dễ lan tràn chỉ số |
| Biểu đồ giải thích | Truyền một thông điệp mạnh mẽ | Sai cho giám sát hoặc khám phá mở |
| Màu sắc và hiệu ứng phong phú | Bắt mắt; cảm giác chỉn chu | Rác biểu đồ; hại tỷ lệ mực-dữ liệu và khả năng tiếp cận |

Căng thẳng lặp lại là tính biểu đạt so với sự trung thực và rõ ràng. Mỗi tính năng làm biểu đồ phong phú hơn (trục thứ hai, dải màu chuyển, phối cảnh 3D, hoạt ảnh) cũng thêm một cách gây hiểu lầm hay chôn vùi điểm chính. Hãy giải quyết bằng cách mặc định ít hơn: biểu đồ đơn giản nhất trả lời câu hỏi, với ít màu nhất, với thang đo nói sự thật. Chỉ thêm tính biểu đạt khi một câu hỏi cụ thể của người đọc đòi hỏi, và trả chi phí khả năng tiếp cận và hiệu năng một cách có ý thức. Đánh đổi thường trực khác là xây so với mua. Một công cụ BI đưa biểu đồ lên màn hình trong vài phút và là lựa chọn đúng cho giám sát nội bộ; một trực quan hóa nhúng trong sản phẩm hướng khách hàng thường cần sự kiểm soát về thiết kế, khả năng tiếp cận và hiệu năng mà chỉ một thành phần chuyên dụng mới cho bạn.

## Câu hỏi để thảo luận với đội của bạn

1. **Biểu đồ của chúng ta có chia sẻ một ngôn ngữ trực quan hay mỗi đội tự phát minh ngôn ngữ riêng?** Khi mỗi nhóm chọn màu, quy ước trục, làm tròn và loại biểu đồ của riêng mình, tổ chức tích lũy các phương ngữ lặng lẽ làm xói mòn niềm tin: hai bảng điều khiển hiển thị "người dùng hoạt động" với thang và sắc xanh khác nhau dạy các giám đốc rằng không thể dựa vào dữ liệu. Hãy mang ba biểu đồ của cùng một chỉ số từ ba đội và đặt chúng cạnh nhau. Những khoảng cách bạn tìm thấy (một trục cắt cụt ở đây, một cầu vồng danh mục ở kia, doanh thu tính bằng nghìn ở cái này và triệu ở cái kia) là lập luận cho một thư viện thành phần biểu đồ dùng chung với bảng màu thống nhất, quy tắc trục mặc định, và khả năng tiếp cận tích hợp, được quản trị như hệ thống thiết kế trong chương 5.2. Mục tiêu là bất kỳ biểu đồ nào trong công ty đọc đúng ngay khi nhìn, vì ngữ pháp được chia sẻ.

2. **Các biểu đồ quan trọng nhất của chúng ta có sống sót được với người đọc mù màu và trình đọc màn hình không?** Khả năng tiếp cận trong trực quan hóa dữ liệu dễ bị bỏ qua vì biểu đồ vẫn trông ổn với những người xây chúng, và đó chính là cái bẫy. Hãy lấy ba biểu đồ ban lãnh đạo thấy thường xuyên nhất và chạy chúng qua một trình mô phỏng mù màu, rồi thử hiểu chúng khi tắt màn hình, chỉ dùng alt text và bất kỳ bảng dự phòng nào. Nếu một biểu đồ trạng thái đỏ-xanh bị phẳng đi, nếu alt text chỉ nói "biểu đồ" và không gì hơn, hoặc nếu không có cách chạm đến các con số nền mà không dùng chuột, bạn đã tìm thấy một nhóm người đọc bạn đang loại trừ, mà trong công việc khu vực công là rủi ro pháp lý theo các tiêu chuẩn trong chương 5.3. Hãy quyết định ai sở hữu việc sửa và liệu bản sửa có thuộc về một thành phần dùng chung để nó được giải một lần.

3. **Với mỗi biểu đồ thúc đẩy một quyết định, chúng ta có chỉ ra được câu hỏi nó trả lời và xác nhận nó không gây hiểu lầm không?** Nhiều biểu đồ tồn tại vì ai đó từng làm ra chúng, không phải vì chúng trả lời một câu hỏi đang sống, và một số cái được xem nhiều nhất bóp méo thang đo mà không ai nhận ra. Hãy đi qua các biểu đồ trên bảng điều khiển chính của bạn và, với mỗi cái, nêu quyết định nó cung cấp thông tin và kiểm tra tính liêm chính của nó: cột từ số không, không trục kép vô cớ, diện tích co giãn trung thực, tiêu đề nêu phát hiện thay vì chủ đề. Những biểu đồ không trả lời câu hỏi hiện tại là ứng viên để xóa, và những cái gây hiểu lầm là ứng viên để sửa khẩn cấp, vì một biểu đồ lặng lẽ phóng đại chênh lệch còn tệ hơn không có biểu đồ. Điều này nối trực tiếp với văn hóa quyết định của chương 7.5: một đội tin biểu đồ của mình đưa ra các quyết định nhanh hơn, có nền tảng tốt hơn.

4. **Khi một đội cần biểu đồ, chúng ta với tới biểu đồ dựng sẵn của công cụ BI trước hay một thư viện thành phần được quản trị, và ai quyết định?** Lực kéo về công cụ BI là có thật: nó nhanh, rẻ, và đã nối sẵn với kho dữ liệu, nên hầu hết bảng điều khiển giám sát thuộc về đó. Nhưng các mặc định chung chung của nó là nơi phương ngữ và rác biểu đồ len vào, và các kiểm soát khả năng tiếp cận và chú thích thường yếu, điều quan trọng nhất với các biểu đồ hướng khách hàng và công khai mang danh tiếng của bạn. Với một tổ chức lớn mối nguy là mặc định không bao giờ được quyết định, nên mỗi đội trôi về bất cứ thứ gì dễ nhất và hệ sinh thái bị phân mảnh. Hãy mang một bản kiểm kê biểu đồ hiện được xây ở đâu, vài ví dụ cạnh nhau từ công cụ BI so với một thành phần chuyên dụng, và các khoảng trống khả năng tiếp cận trong từng cái. Trong bối cảnh doanh nghiệp và chính phủ, hãy tính thực tế mua sắm: bạn thường bị khóa vào một nền tảng BI trong nhiều năm, nên hãy biết chính xác những biểu đồ nào nó kết xuất được một cách trung thực và dễ tiếp cận và những cái nào cần thành phần được quản trị, trước hợp đồng, không phải sau.

5. **Ai được phép xuất bản một biểu đồ cho khán giả bên ngoài hoặc giám đốc, và nó phải qua rà soát gì trước?** Phân tích tự phục vụ là một điều tốt thực sự, nhưng nó nghĩa là một biểu đồ gây hiểu lầm có thể đến hội đồng quản trị hay công chúng mà không có cặp mắt thứ hai, và một trục cắt cụt hay một đỉnh không nhãn trên đồ họa công khai khó gỡ hơn nhiều so với ngăn ngừa. Căng thẳng là tốc độ và tự chủ so với liêm chính và niềm tin: chặn quá chặt và người ta đi vòng bạn, chặn quá ít và bạn phát hành biểu đồ gây hoảng loạn cho một thị trường hay một nhóm cử tri. Hãy mang đường xuất bản hiện tại cho các biểu đồ dễ thấy nhất của bạn, ví dụ đã đến khán giả bên ngoài mà không rà soát, và bằng chứng về việc phương pháp và độ bất định có được chú thích trên chính biểu đồ không. Trong công việc khu vực công và chịu quy định điều này cấp bách: một thống kê chính thức là một giao tiếp với công dân và là vấn đề của niềm tin các bên liên quan trong chương 10.16, nên hãy nêu ai ký duyệt, họ áp dụng danh mục kiểm liêm chính và khả năng tiếp cận nào, và trách nhiệm nằm ở đâu khi một biểu đồ gây hiểu lầm.

6. **Chúng ta đã thêm tương tác ở đâu, và chế độ xem tĩnh mặc định có còn kể trọn câu chuyện mà không cần chuột không?** Tương tác quyến rũ và đắt: nó giấu giá trị sau một lần di chuột, hỏng trên cảm ứng và với người dùng bàn phím, và có thể kéo ngân sách kết xuất xuống mức bò trên tập dữ liệu lớn, như chương 5.6 cảnh báo. Cân nhắc đối lập là một câu hỏi theo dõi thực (một giá trị chính xác, một đào sâu, một phân khúc đã lọc) đôi khi đáng chi phí, nên mục tiêu là kiềm chế thay vì cấm đoán. Hãy mang danh sách biểu đồ tương tác bạn phát hành, kết quả thử từng cái khi không có chuột và trên điện thoại, và số liệu hiệu năng khi dữ liệu lớn lên đến hàng chục nghìn điểm. Với khán giả doanh nghiệp và chính phủ, góc độ khả năng tiếp cận là nghĩa vụ pháp lý theo các tiêu chuẩn trong chương 5.3, và biểu đồ được đọc trên ki-ốt, bản in, và công nghệ hỗ trợ, nên mặc định tĩnh, có chú thích phải mang thông điệp cốt lõi và tương tác chỉ thêm chiều sâu bên dưới.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ thắng, vì vậy hãy dựa vào các biểu đồ đã có trong công cụ BI của bạn hoặc một thư viện vẽ biểu đồ nhẹ thay vì xây một hệ sinh thái thành phần trực quan hóa bạn không đủ người vận hành. Quyết định rẻ duy nhất sinh lợi về sau là chọn một bảng màu an toàn cho người mù màu và thói quen cột-từ-số-không ngay ngày đầu, để bạn không tích lũy cả chục phương ngữ của cùng một chỉ số trước khi có mười khách hàng. Hãy ưu tiên một biểu đồ tĩnh, có chú thích nêu phát hiện của nó hơn là một biểu đồ tương tác bạn sẽ không có thời gian làm cho dễ tiếp cận.

**Doanh nghiệp nhỏ.** Không có chuyên gia dữ liệu và ngân sách eo hẹp, hãy coi trực quan hóa là thứ bạn lấy từ các công cụ bạn đã trả tiền: bảng tính, SaaS phân tích, bảng điều khiển trong CRM của bạn. Hãy học một nhúm quy tắc liêm chính quan trọng (cột bắt đầu từ số không, không cầu vồng cho một số lượng, không biểu đồ tròn chín lát) và áp dụng một bảng màu an toàn cho người mù màu làm sẵn thay vì đặt làm riêng. Hãy mua biểu đồ, đừng xây, và dành sự chú ý của bạn để đọc nó cho đúng.

**Doanh nghiệp lớn.** Vấn đề là sự nhất quán qua nhiều đội, vì vậy hãy quản trị trực quan hóa như một hệ thống thiết kế: một thư viện thành phần biểu đồ dùng chung với bảng màu tuần tự, phân kỳ và danh mục đã thống nhất, mặc định trục trung thực, định dạng số chuẩn, và khả năng tiếp cận được nướng vào. Hãy thực thi nó bằng kiểm tra hồi quy trực quan và liêm chính trong đường ống phân phối của chương 8.1, để một biểu đồ cắt cụt trục hoặc trượt độ tương phản bị chặn trước khi phát hành. Lợi ích là biểu đồ từ bất kỳ đội nào đọc đúng ngay khi nhìn và ban lãnh đạo thôi hỏi nên tin phiên bản nào của một con số.

**Chính phủ.** Mọi biểu đồ công khai là một hành động giao tiếp và chịu trách nhiệm giải trình công, nên thang trung thực và khả năng tiếp cận WCAG là nghĩa vụ, không phải sở thích. Hãy bắt buộc cột từ số không, diện tích mã hóa bằng diện tích, bảng màu an toàn cho người mù màu, tiêu đề ngôn ngữ đơn giản nêu phát hiện, và một bảng dễ tiếp cận tải về được bên cạnh mỗi biểu đồ. Hãy chú thích phương pháp và độ bất định trên chính biểu đồ để một con số gây tranh cãi không thể bị rút gọn thành một tiêu đề gây hiểu lầm, và bảo đảm mọi công cụ BI bạn mua sắm đáp ứng được các tiêu chuẩn này, vì nghĩa vụ là của bạn bất kể nhà cung cấp.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp phân tích mười người phát hành bảng điều khiển sử dụng hướng khách hàng. Phiên bản đầu dùng chủ đề mặc định của công cụ BI: cầu vồng màu danh mục, đường lưới khắp nơi, và một biểu đồ tròn chín lát không ai đọc được. Người dùng phàn nàn các con số cảm thấy không đáng tin. Đội xây lại nó thành các thành phần nhúng với một bảng màu nhỏ an toàn cho người mù màu, thay biểu đồ tròn bằng biểu đồ cột đã sắp xếp, làm nhạt đường lưới, và thêm nhãn trực tiếp để chú giải biến mất. Họ đặt tiêu đề nêu phát hiện và thêm alt text cùng công tắc bảng cho mọi biểu đồ. Mức độ tương tác với bảng điều khiển tăng vì khách hàng cuối cùng đọc được nó trong nháy mắt, và thiết kế gọn hơn trở thành điểm bán hàng trong các buổi demo.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia có hàng trăm bảng điều khiển nội bộ do hàng chục đội xây, mỗi cái có màu và thói quen trục riêng, và các giám đốc thường xuyên không tin chúng vì cùng một chỉ số trông khác nhau trong mỗi bộ slide. Công ty giới thiệu một thư viện biểu đồ được quản trị phía trên nền tảng BI: bảng màu tuần tự, phân kỳ và danh mục đã thống nhất; một quy tắc cứng rằng trục cột bắt đầu từ số không; định dạng số chuẩn; và khả năng tiếp cận nướng vào mọi thành phần. Một kiểm tra hồi quy trực quan trong đường ống phân phối của chương 8.1 chặn các biểu đồ vi phạm tiêu chuẩn. Trong vòng một năm, biểu đồ từ bất kỳ đội nào đọc đúng ngay khi nhìn, và ban lãnh đạo thôi hỏi "tôi nên tin phiên bản nào của con số này?"

**Chính phủ.** Một cơ quan thống kê quốc gia công bố dữ liệu công khai về kinh tế, y tế và dân số, và biểu đồ của nó được đọc bởi nhà báo, nhà hoạch định chính sách và công dân không thể xác minh các con số nền. Cơ quan coi mọi biểu đồ là một giao tiếp với công chúng và là vấn đề của niềm tin các bên liên quan trong chương 10.16. Họ bắt buộc thang trung thực (cột từ số không, không trục kép gây hiểu lầm, diện tích mã hóa bằng diện tích), bảng màu phân kỳ an toàn cho người mù màu cho so sánh khu vực, tiêu đề ngôn ngữ đơn giản nêu phát hiện, và một bảng dễ tiếp cận tải về được bên cạnh mỗi biểu đồ để đáp ứng WCAG. Khi một con số gây tranh cãi được công bố, chú thích giải thích phương pháp và độ bất định trên chính biểu đồ, để một trục cắt cụt hay một đỉnh không nhãn không bao giờ trở thành tiêu đề gây hiểu lầm làm xói mòn niềm tin công chúng.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của thiết kế trực quan hóa tốt là quyết định nhanh hơn, tốt hơn và ít sai lầm tốn kém hơn. Một bảng điều khiển phơi bày vấn đề trong nháy mắt rút ngắn thời gian từ tín hiệu đến hành động, và một biểu đồ nói sự thật ngăn ngân sách đuổi theo ảo ảnh mà một trục cắt cụt chế ra. Những lợi ích này khó đưa lên hóa đơn, nhưng là thật: mỗi cuộc họp lãnh đạo dành để tranh cãi nên tin biểu đồ nào, mỗi chiến lược xây trên một xu hướng bị đọc sai, và mỗi khách hàng rời bỏ vì phân tích trong sản phẩm của bạn không đọc được là một chi phí mà thiết kế rõ ràng loại bỏ. Nơi biểu đồ thúc đẩy tiền thật, như trong ví dụ ngân hàng, giá trị của những con số đáng tin lấn át chi phí xây chúng cho tốt.

Chi phí áp dụng chủ yếu là một lần và dùng chung. Bạn xác định bảng màu, quy tắc trục và định dạng, và mặc định khả năng tiếp cận đã thống nhất, rồi mã hóa chúng vào một thư viện thành phần biểu đồ để các đội thừa hưởng thay vì quyết định lại cho từng bảng điều khiển. Chi phí sở hữu liên tục là thật nhưng khiêm tốn: bảo trì thư viện, giữ nó dễ tiếp cận khi tiêu chuẩn tiến hóa, và chống lại sự lan tràn của các biểu đồ tùy chỉnh một lần. Chi phí của sự bỏ bê cộng dồn lặng lẽ: biểu đồ không nhất quán, gây hiểu lầm, không dễ tiếp cận xói mòn niềm tin vào mọi dữ liệu của bạn, mời rủi ro pháp lý trong bối cảnh chịu quy định và khu vực công, và đẩy người ta trở lại bảng tính thô, làm lãng phí toàn bộ khoản đầu tư vào nền tảng phân tích của chương 7.3. Để trình bày lập luận với ban lãnh đạo, hãy gắn chất lượng trực quan hóa với kết quả họ đã theo dõi: tốc độ quyết định, niềm tin vào báo cáo, và, trong khu vực công, tuân thủ khả năng tiếp cận.

## Phản mẫu và cạm bẫy

- **Trục cột bị cắt cụt:** bắt đầu cột trên số không để chênh lệch nhỏ trông như vực thẳm; lời nói dối biểu đồ phổ biến nhất.
- **Trục kép vô cớ:** hai thang y trên một biểu đồ, trượt để chế ra bất kỳ tương quan nào tác giả muốn cho thấy.
- **Diện tích gây hiểu lầm:** co giãn biểu tượng hoặc bong bóng theo chiều dài cạnh để diện tích, và giá trị cảm nhận, tăng theo bình phương.
- **Cầu vồng cho số lượng:** mã hóa một số lượng có thứ tự bằng sắc độ danh mục không thứ tự, nên mắt không đọc được độ lớn.
- **Biểu đồ tròn nhiều lát:** hơn ba lát, buộc người đọc so sánh các góc họ không đánh giá được; hãy dùng cột đã sắp xếp.
- **Rác biểu đồ:** đường lưới đậm, viền, 3D và đổ bóng làm giảm tỷ lệ mực-dữ liệu và chôn vùi tín hiệu.
- **Màu là dấu hiệu duy nhất:** trạng thái đỏ-xanh không nhãn hay hình dạng, vô hình với người mù màu và trình đọc màn hình.
- **Săn chú giải:** buộc phải ghé một chú giải ở xa nơi một nhãn trực tiếp trên đường hay cột là đủ.
- **Nhấn mạnh mọi thứ:** mọi chuỗi đều đậm và sáng, nên tương phản sụp đổ và không gì nổi bật.
- **Biểu đồ nơi bảng thắng:** một bức tranh cho bốn con số chính xác mà người đọc cần đọc cho đúng.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Biểu đồ được làm tùy nghi bằng công cụ nào tiện tay. Màu, trục và định dạng khác nhau theo tác giả, trục cắt cụt và danh mục cầu vồng phổ biến, khả năng tiếp cận không được cân nhắc, và người đọc không tin kết quả.
- **Mức 2, Phát triển:** Một số đội áp dụng thực hành cơ bản, nhưng không nhất quán toàn tổ chức. Cột bắt đầu từ số không ở vài nơi, rác biểu đồ lộ liễu bị can ngăn khi rà soát, và một bảng màu nhà tồn tại ở vài đội, nhưng một đội khác cuối hành lang vẫn phát hành biểu đồ tròn chín lát và biểu đồ trạng thái đỏ-xanh.
- **Mức 3, Chuẩn hóa:** Một thư viện thành phần biểu đồ dùng chung mã hóa bảng màu tuần tự, phân kỳ và danh mục đã thống nhất, quy tắc trục trung thực, định dạng chuẩn, và khả năng tiếp cận (an toàn cho người mù màu, alt text, bảng dự phòng). Các tiêu chuẩn được lập tài liệu và thực thi toàn tổ chức, và các công dụng giải thích, khám phá và bảng điều khiển được phân biệt bằng thiết kế.
- **Mức 4, Quản lý:** Chất lượng trực quan hóa được đo và kiểm soát theo đường cơ sở. Các kiểm tra khả năng tiếp cận và liêm chính biểu đồ chạy trong đường ống phân phối và báo cáo tỷ lệ đạt; tỷ lệ biểu đồ có cột từ số không, màu tuân thủ tương phản, và bảng dự phòng được theo dõi như một chỉ số; khả năng hiểu được kiểm thử với người đọc thật theo đường cơ sở; và số phương ngữ khác nhau của mỗi chỉ số then chốt được theo dõi khi nó tiến dần về một. Biểu đồ vi phạm tiêu chuẩn bị bắt trước khi phát hành, và các con số, không phải ý kiến, thúc đẩy nơi thư viện cần làm việc.
- **Mức 5, Điều phối:** Trực quan hóa được cải thiện liên tục và tích hợp trong toàn tổ chức. Tiêu chuẩn thích ứng khi yêu cầu khả năng tiếp cận và nhu cầu người đọc thay đổi, bảng màu, thành phần và quy ước được tinh chỉnh từ bằng chứng đo được, chú thích và tường thuật là chuẩn mực, và thực hành được dệt vào văn hóa phân tích và quyết định để biểu đồ từ bất kỳ đội nào đọc đúng ngay khi nhìn và ngôn ngữ trực quan tiến hóa khi tổ chức học hỏi.

## Ý tưởng để thảo luận

1. Biểu đồ nào trên bảng điều khiển chính của bạn sẽ trông khác nếu trục của nó bắt đầu từ số không, và điều đó có đổi câu chuyện không?
2. Hãy chọn biểu đồ quan trọng nhất của bạn: thông điệp của nó có sống sót trong thang xám không, và nếu không, dấu hiệu dư thừa nào sẽ sửa được?
3. Bạn đang dùng biểu đồ tương tác ở đâu khi một biểu đồ tĩnh, có chú thích sẽ kể trọn câu chuyện nhanh hơn?
4. Tiêu đề biểu đồ của bạn nêu phát hiện hay chủ đề, và ai sẽ nhận ra nếu một con số tiêu đề lặng lẽ đảo ngược?
5. Biểu đồ nào của bạn không trả lời quyết định hiện tại nào, và cần gì để xóa nó mà không ai nhớ?
6. Khi nào một đội nên xây trực quan hóa trong sản phẩm so với dùng công cụ BI, và bạn có quy tắc viết sẵn để chọn không?

## Những điểm cần ghi nhớ

- Bắt đầu từ câu hỏi của người đọc, rồi chọn biểu đồ: cột cho so sánh, đường cho xu hướng, phân tán cho quan hệ, tần suất cho phân phối, cột đã sắp xếp thay vì tròn cho bộ phận-trên-tổng thể.
- Khớp mã hóa với dữ liệu: dành vị trí và độ dài cho đại lượng quan trọng nhất, và dùng sắc độ cho danh mục, không bao giờ cho độ lớn.
- Theo đuổi sự xuất sắc đồ họa: tối đa hóa tỷ lệ mực-dữ liệu, xóa rác biểu đồ, dùng bội số nhỏ, và hướng mắt bằng tương phản tiền chú ý cùng phân cấp rõ ràng.
- Coi màu sắc là một hệ thống (tuần tự, phân kỳ, danh mục), giữ nó an toàn cho người mù màu, và không bao giờ chỉ dựa vào màu sắc; cung cấp nhãn, alt text và bảng dự phòng.
- Nói sự thật về thang đo (cột từ số không, diện tích trung thực, không trục kép vô cớ), chú thích hiểu biết, và chỉ thêm tương tác khi một câu hỏi theo dõi thực đòi hỏi.

## Tài liệu tham khảo và đọc thêm

- Edward R. Tufte, *The Visual Display of Quantitative Information*
- Edward R. Tufte, *Envisioning Information*
- Stephen Few, *Show Me the Numbers: Designing Tables and Graphs to Enlighten*
- Stephen Few, *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring*
- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualisation Guide for Business Professionals*
- Alberto Cairo, *The Truthful Art: Data, Charts, and Maps for Communication*
- Alberto Cairo, *How Charts Lie: Getting Smarter about Visual Information*
- William S. Cleveland, *The Elements of Graphing Data*
- Jacques Bertin, *Semiology of Graphics: Diagrams, Networks, Maps*
- Tamara Munzner, *Visualisation Analysis and Design*
- Cynthia A. Brewer, ColorBrewer: Colour Advice for Cartography (colorbrewer2.org)
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*
