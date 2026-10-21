# 10.11 Chủ quyền số

## Tổng quan và động lực

[Chủ quyền số](https://en.wikipedia.org/wiki/Digital_sovereignty) là mức độ mà một tổ chức, quốc gia hay khối giữ được quyền kiểm soát có ý nghĩa đối với dữ liệu, phần mềm và hạ tầng của chính mình. Điều đó nghĩa là kiểm soát dữ liệu nằm vật lý ở đâu, luật nào và chính phủ nào có thể buộc truy cập vào nó, và liệu các hệ thống trọng yếu có tiếp tục vận hành được mà không phụ thuộc vào một cường quốc nước ngoài hay một nhà cung cấp duy nhất. Nó có nhiều chiều: **[chủ quyền dữ liệu](https://en.wikipedia.org/wiki/Data_sovereignty)** (thẩm quyền và luật nào chi phối dữ liệu), **chủ quyền vận hành** (khả năng chạy và quản trị hệ thống mà không cần sự cho phép hay hiện diện của bên thứ ba), **chủ quyền phần mềm** (quyền tiếp cận và kiểm soát mã nguồn và sự tiến hóa của nó), và **chủ quyền chuỗi cung ứng** (thoát khỏi các điểm nghẽn trong phần cứng, dịch vụ và phụ thuộc). Chương này nằm trong phần quản lý vì chủ quyền về bản chất là quyết định chiến lược, mua sắm và rủi ro (chương 10.1–10.3) với hệ quả kỹ thuật sâu sắc.

Động lực đã chuyển từ lý thuyết sang cấp bách. [Điện toán đám mây](https://en.wikipedia.org/wiki/Cloud_computing) tập trung phần lớn hạ tầng thế giới vào một nhúm nhà cung cấp, chủ yếu dưới thẩm quyền của một quốc gia. Các luật có hiệu lực ngoài lãnh thổ như [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) của Hoa Kỳ (có thể buộc nhà cung cấp tiết lộ dữ liệu bất kể nó được lưu ở đâu) va chạm với các chế độ như [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) của EU, một căng thẳng được kết tinh bởi phán quyết *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)* vô hiệu hóa Privacy Shield EU-Hoa Kỳ. Thêm các cú sốc địa chính trị, trừng phạt, và rủi ro một nhà cung cấp bị cắt, phụ thuộc trở thành điểm yếu chiến lược, không chỉ là chú thích quản lý nhà cung cấp. Chủ quyền là kỷ luật quyết định, có chủ đích, các hệ thống và dữ liệu trọng yếu nhất của bạn có thể gánh an toàn bao nhiêu phụ thuộc đó.

Với doanh nghiệp và đặc biệt chính phủ, rủi ro là trực tiếp. Các tập đoàn đa quốc gia phải hòa giải các chế độ bảo vệ dữ liệu mâu thuẫn và tránh khóa chặt mà cơ quan quản lý hay một biến cố địa chính trị có thể biến thành cuộc di chuyển sinh tử. Chính phủ nắm dữ liệu (hồ sơ y tế, thuế, quốc phòng, danh tính công dân) mà việc phơi nhiễm trước thẩm quyền nước ngoài là câu hỏi an ninh quốc gia và lòng tin công. Đó là lý do các dịch vụ "đám mây chủ quyền", sáng kiến như [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X) của EU, và chứng nhận quốc gia như SecNumCloud của Pháp xuất hiện. Mục tiêu không phải tự cung tự cấp. Đó là kiểm soát tương xứng khớp với độ nhạy cảm của cái đang bị đe dọa.

## Các nguyên tắc chính

- **Chủ quyền là một phổ, không phải công tắc.** Khớp mức kiểm soát với độ nhạy cảm của dữ liệu và khối lượng công việc.
- **Vị trí không phải thẩm quyền.** Dữ liệu lưu cục bộ vẫn có thể bị chính phủ nước ngoài với tới về mặt pháp lý; chỉ cư trú không phải chủ quyền.
- **Thiết kế cho lối thoát.** Khả năng rời một nhà cung cấp là thước đo chân thực nhất của chủ quyền.
- **[Tiêu chuẩn mở](https://en.wikipedia.org/wiki/Open_standard) và [mã nguồn mở](https://en.wikipedia.org/wiki/Open-source_software) giảm phụ thuộc:** chúng là công cụ tự chủ chiến lược, không chỉ tiết kiệm chi phí.
- **Kiểm soát khóa.** Ai giữ và kiểm soát khóa mã hóa thường quan trọng hơn nơi các byte nằm.
- **Tránh đổi một khóa chặt lấy khóa chặt khác.** Một nhà cung cấp "chủ quyền" duy nhất có thể bị giam cầm như một hyperscaler.
- **Hãy tương xứng.** Chủ quyền có chi phí thật; xoay quá mức ở mọi nơi phí tiền và làm chậm phân phối.

## Khuyến nghị

### Phân loại dữ liệu và khối lượng công việc theo độ nhạy chủ quyền

Không phải mọi thứ cần cùng mức bảo vệ. Hãy phân loại dữ liệu và hệ thống theo hậu quả của việc thẩm quyền nước ngoài truy cập hoặc mất nhà cung cấp. Khối lượng công việc công khai và rủi ro thấp có thể nằm trên hạ tầng hyperscale toàn cầu vì quy mô và chi phí. Dữ liệu rất nhạy cảm (an ninh quốc gia, y tế, danh tính công dân, hồ sơ bị quản lý) đáng được kiểm soát chủ quyền mạnh hơn. Việc phân bậc này, cùng logic dựa trên rủi ro như phân loại dữ liệu ở chương 4.5, là thứ giữ chủ quyền trong tầm chi trả, tập trung kiểm soát đắt đỏ vào nơi chúng được biện minh thay vì nội địa hóa mọi thứ.

### Hiểu thẩm quyền, không chỉ cư trú

**Cư trú dữ liệu** (vị trí vật lý hay địa lý nơi dữ liệu được lưu) cần thiết nhưng chưa đủ. Điều quan trọng về mặt pháp lý là *thẩm quyền*: chính phủ nào có thể buộc tiết lộ, và theo luật nào. Một tập dữ liệu được giữ trong trung tâm dữ liệu trong nước do nhà cung cấp có trụ sở nước ngoài vận hành vẫn có thể bị với tới theo luật của quốc gia sở tại nhà cung cấp (vấn đề CLOUD Act). Hãy lập bản đồ phơi nhiễm pháp lý của từng hệ thống: trụ sở nhà cung cấp, luật áp dụng, và mọi quyết định về mức độ đầy đủ hay cơ chế chuyển giao (Điều khoản Hợp đồng Tiêu chuẩn, Khung Bảo mật Dữ liệu EU-Hoa Kỳ). Rồi coi bản đồ pháp lý đó là phần hạng nhất của kiến trúc (chương 4.5, 4.6).

### Thiết kế cho khả năng di chuyển và đảo ngược

Kiểm soát chủ quyền bền vững nhất là một lối thoát đáng tin. Ưu tiên tiêu chuẩn mở và định dạng di chuyển được (chương 3.8). Đóng gói khối lượng công việc vào container để chúng di chuyển được. Giữ hạ tầng dưới dạng mã (chương 8.2) để một môi trường được dựng lại ở nơi khác. Tránh phụ thuộc sâu vào dịch vụ độc quyền của một nhà cung cấp duy nhất cho các hệ thống trọng yếu nhất. Duy trì và định kỳ *kiểm thử* một kế hoạch thoát, một ký quỹ dữ liệu và cấu hình cùng một con đường đã diễn tập tới phương án thay thế, để "chúng ta có thể rời đi nếu phải" là sự thật đã chứng minh, không phải hy vọng. Đây là thuốc giải cho **[khóa chặt nhà cung cấp](https://en.wikipedia.org/wiki/Vendor_lock-in)**, tình trạng không thể đổi nhà cung cấp mà không có chi phí hay gián đoạn cấm đoán.

### Dùng hạ tầng chủ quyền và kiểm soát khóa nơi cần thiết

Với bậc nhạy cảm nhất, có những kiểm soát kỹ thuật mạnh hơn: dịch vụ **đám mây chủ quyền** (vùng đám mây do các thực thể trong thẩm quyền vận hành hoặc hợp tác, đôi khi được chứng nhận như SecNumCloud), **[điện toán bảo mật](https://en.wikipedia.org/wiki/Confidential_computing)** (thực thi tin cậy dựa trên phần cứng giữ dữ liệu được mã hóa ngay cả khi đang được xử lý), và khóa mã hóa do khách hàng kiểm soát: **mang khóa của riêng bạn (BYOK)** và, mạnh hơn, **tự giữ khóa của bạn (HYOK)**, nơi nhà cung cấp không bao giờ có quyền truy cập vào các khóa mở dữ liệu. Kiểm soát khóa có thể mang lại phần lớn lợi ích thực tiễn của chủ quyền ngay cả trên hạ tầng dùng chung. Dữ liệu mà nhà cung cấp không giải mã được là dữ liệu họ không thể tiết lộ một cách có ý nghĩa.

### Ưu tiên mã nguồn mở và hệ sinh thái mở cho tự chủ chiến lược

Phần mềm mã nguồn mở và tiêu chuẩn mở nằm trong những đòn bẩy chủ quyền mạnh nhất, vì chúng loại bỏ công tắc tiêu diệt của một nhà cung cấp duy nhất. Mã nguồn có thể được chạy, kiểm toán, rẽ nhánh và bảo trì độc lập với bất kỳ nhà cung cấp nào (chương 10.3, 3.8). Các chính sách "tiền công, mã công" của khu vực công và sáng kiến như Gaia-X phản ánh điều này. Mã nguồn mở không tự động có chủ quyền. Nó vẫn cần người có kỹ năng để chạy và hỗ trợ, và chuỗi cung ứng của nó cần được bảo mật (chương 4.2). Nhưng nó biến phụ thuộc vào một nhà cung cấp thành phụ thuộc vào một cộng đồng và năng lực của chính bạn, dễ kiểm soát hơn nhiều.

### Quản trị chủ quyền như rủi ro tương xứng, không phải tuyệt đối

Hãy lập một khung rủi ro chủ quyền cạnh quản trị khác của bạn (chương 10.2, 1.5). Đánh giá rủi ro tập trung và thẩm quyền của các nền tảng lớn. Quyết định mức chủ quyền mục tiêu cho từng bậc dữ liệu, và cân nhắc chúng so với chi phí, năng lực và tốc độ phân phối. Mục đích là một lập trường bảo vệ được, có tài liệu ("các khối lượng công việc này chấp nhận phụ thuộc hyperscale; những cái này đòi kiểm soát trong thẩm quyền; đây là tư thế thoát của chúng ta"), được xem xét lại khi địa chính trị và quy định thay đổi, không phải lập trường tuyệt đối một lần.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Đám mây hyperscale toàn cầu** | Quy mô, tính năng, chi phí thấp, tốc độ | Phơi nhiễm thẩm quyền; rủi ro tập trung và khóa chặt |
| **Đám mây chủ quyền / nhà cung cấp trong thẩm quyền** | Kiểm soát pháp lý; khớp an ninh quốc gia; lòng tin | Chi phí cao hơn; ít tính năng hơn; thường quy mô nhỏ hơn; khóa chặt mới |
| **Kiểm soát khóa (BYOK/HYOK) trên hạ tầng dùng chung** | Phần lớn lợi ích với chi phí thấp hơn; giữ quy mô | Phức tạp vận hành; rủi ro quản lý khóa; không tuyệt đối |
| **Mã nguồn mở / tự lưu trữ** | Kiểm toán được, rẽ nhánh được, không có công tắc tiêu diệt nhà cung cấp | Cần năng lực nội bộ; bạn sở hữu vận hành và bảo mật |
| **Mệnh lệnh nội địa hóa dữ liệu** | Tuân thủ quy định; đảm bảo chính trị | Tốn kém; phân mảnh dữ liệu; có thể giảm khả năng phục hồi và tiện ích |

Căng thẳng định nghĩa là **kiểm soát so với năng lực và chi phí**. Chủ quyền tối đa (tự lưu trữ, trong thẩm quyền, mã nguồn mở, hoàn toàn di chuyển được) hy sinh quy mô, tính năng và vận tốc của các nền tảng toàn cầu. Năng lực tối đa chấp nhận phụ thuộc và phơi nhiễm thẩm quyền. Cách giải quyết là phân bậc: trả tiền cho chủ quyền nơi hậu quả biện minh nó, và chấp nhận phụ thuộc thực dụng nơi không.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta đã phân bậc dữ liệu và khối lượng công việc theo độ nhạy chủ quyền chưa, để kiểm soát đắt đỏ chỉ đáp xuống nơi chúng được biện minh?** Chủ quyền là một phổ, không phải công tắc, và nội địa hóa mọi thứ đốt tiền, mất năng lực, và thậm chí có thể giảm khả năng phục hồi bằng cách thu hẹp các lựa chọn của bạn. Hãy phân loại từng hệ thống theo hậu quả của việc thẩm quyền nước ngoài truy cập hoặc mất nhà cung cấp: khối lượng công việc công khai và rủi ro thấp có thể nằm trên hạ tầng hyperscale toàn cầu, trong khi dữ liệu an ninh quốc gia, y tế hay danh tính công dân đáng được kiểm soát mạnh hơn. Đây là cùng logic dựa trên rủi ro như phân loại dữ liệu, và là thứ giữ chủ quyền trong tầm chi trả. Hãy mang các hệ thống viên ngọc quý và nơi lưu trữ hiện tại của chúng, và hỏi mức bảo vệ có khớp với độ nhạy cảm không. Nếu bạn đang bảo vệ mọi thứ như nhau, gần như chắc chắn bạn đang trả thừa ở đâu đó và bị phơi nhiễm ở chỗ khác.

2. **Tiêu chuẩn mở và mã nguồn mở có là một phần chiến lược chủ quyền của chúng ta, hay chúng ta chỉ coi chúng là công cụ tiết kiệm chi phí?** Mã nguồn bạn có thể chạy, kiểm toán, rẽ nhánh và bảo trì loại bỏ công tắc tiêu diệt của một nhà cung cấp duy nhất, một trong những đòn bẩy tự chủ mạnh nhất bạn có. Tiêu chuẩn mở và định dạng di chuyển được là thứ làm một lối thoát đáng tin khả thi, và lối thoát đáng tin là thước đo chân thực nhất của chủ quyền. Cái bẫy tinh tế hơn là thoát khỏi một hyperscaler chỉ để hoàn toàn bị giam cầm bởi một nhà cung cấp "chủ quyền" không có lối thoát: bạn đã đổi một khóa chặt lấy khóa chặt khác. Hãy mang các nền tảng trọng yếu nhất của bạn và hỏi mỗi cái bị trói chặt thế nào vào dịch vụ độc quyền của một nhà cung cấp. Nơi câu trả lời là "rất chặt," tiêu chuẩn mở và môi trường đóng gói container, dựng lại được là cách rẻ nhất để nới lỏng cái kẹp.

3. **Ai sở hữu khung rủi ro chủ quyền của chúng ta, và bao lâu chúng ta xem xét lại lập trường khi luật và địa chính trị dịch chuyển?** Một lập trường chủ quyền đặt một lần và không bao giờ xem lại trở thành hư cấu ngay khi một phán quyết, lệnh trừng phạt hay luật mới đáp xuống, và những cú sốc đó nay đến đều đặn. Hãy lập một khung sống cạnh quản trị khác của bạn: đánh giá rủi ro tập trung và thẩm quyền của các nền tảng lớn, đặt mức chủ quyền mục tiêu cho từng bậc dữ liệu, và lập tài liệu một lập trường bảo vệ được mà bạn có thể trình cơ quan quản lý. Nêu tên chủ sở hữu và nhịp xem xét. Hãy mang câu hỏi một lệnh trừng phạt hay phán quyết bất lợi với nhà cung cấp chính của bạn sẽ tác động các dịch vụ trọng yếu của bạn thế nào vào tuần tới; nếu không ai trả lời được, khung chưa tồn tại.

4. **Ai giữ khóa mã hóa cho dữ liệu nhạy cảm nhất của chúng ta, và nhà cung cấp có thể bị buộc giao dữ liệu đó dưới dạng đọc được không?** Cư trú và thậm chí một vùng "chủ quyền" có ít giá trị nếu nhà vận hành giữ khóa, vì lệnh tiết lộ khi đó với tới dữ liệu đã giải mã bất kể các byte nằm đâu. Tự kiểm soát khóa, qua mang khóa của riêng bạn hoặc mạnh hơn là tự giữ khóa của bạn nơi nhà cung cấp không bao giờ thấy chúng, thường mang lại phần lớn lợi ích thực tiễn của chủ quyền trên hạ tầng dùng chung với một phần nhỏ chi phí di dời mọi thứ. Cân nhắc đối lập mang tính vận hành: quản lý khóa không khoan nhượng, và một khóa mất hoặc xử lý sai có thể khóa bạn khỏi dữ liệu của chính mình chắc chắn như bất kỳ lệnh trừng phạt nào. Hãy mang bản kiểm kê tập dữ liệu nào được mã hóa, ai thực sự giữ từng khóa, và con đường khôi phục của bạn nếu một khóa bị mất, rồi ánh xạ nó với các bậc chủ quyền của bạn. Với doanh nghiệp và chính phủ, hãy coi quyền giữ khóa là lằn ranh quyết định liệu lệnh tiết lộ nước ngoài trả về bản mã hay bản rõ, và biến nó thành yêu cầu mua sắm thay vì trang bị về sau.

5. **Chúng ta có thực sự rời được nhà cung cấp chính trong khung thời gian có ý nghĩa không, và lần cuối chúng ta diễn tập là khi nào?** Một lối thoát đáng tin là thước đo chân thực nhất của chủ quyền, vậy mà hầu hết kế hoạch thoát nằm trên giấy và chưa bao giờ được chạy, nên khả năng di chuyển vẫn là hy vọng thay vì sự thật đã chứng minh. Căng thẳng là chi phí và sự tập trung: diễn tập lối thoát, giữ khối lượng công việc đóng gói container, và giữ ký quỹ dữ liệu và cấu hình đều tiêu tốn sự chú ý kỹ thuật mà áp lực phân phối muốn dùng ở nơi khác. Hãy mang hệ thống trọng yếu nhất của bạn, ước tính trung thực một cuộc di chuyển bị ép mất bao lâu, danh sách dịch vụ độc quyền nó phụ thuộc vào, và ngày diễn tập thực sự gần nhất của bạn (nếu có). Với tổ chức lớn hay công mang nghĩa vụ thoát nhiều năm trong hợp đồng, một lối thoát chưa diễn tập là cam kết bạn có thể không đáp ứng được về mặt pháp lý, nên hãy coi nhịp diễn tập là một phần chi phí vận hành của hệ thống, không phải bài tập tùy chọn.

6. **Với mỗi hệ thống viên ngọc quý, chúng ta có biết chính phủ nào có thể buộc truy cập nó một cách hợp pháp hôm nay, bất kể dữ liệu nằm vật lý ở đâu không?** Vị trí không phải thẩm quyền: dữ liệu trong trung tâm dữ liệu trong nước vẫn có thể bị với tới theo luật quốc gia sở tại của nhà vận hành có trụ sở nước ngoài, và các đội thường xuyên nhầm cư trú với bảo vệ pháp lý. Phần khó là câu trả lời đòi đầu vào pháp lý và mua sắm, không chỉ sơ đồ kiến trúc, và bản đồ dịch chuyển khi các quyết định về mức độ đầy đủ, phán quyết và cơ chế chuyển giao thay đổi. Hãy mang, cho mỗi tập dữ liệu trọng yếu, trụ sở nhà cung cấp, các luật với tới nó, và cơ chế chuyển giao bạn dựa vào, và trung thực nơi thực sự không ai biết. Trong bối cảnh bị quản lý và công, một phơi nhiễm pháp lý chưa lập bản đồ trên dữ liệu công dân hay an ninh quốc gia là phát hiện đang chờ ở lần kiểm toán tới, nên hãy tài trợ việc lập bản đồ pháp lý tường minh như bạn tài trợ hạ tầng.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ và đường băng chi phối, nên hãy mua chủ quyền như một tính năng mỏng thay vì xây một ngăn xếp chủ quyền bạn không bố trí nhân sự nổi. Nếu thẩm quyền của khách hàng là ràng buộc, hãy triển khai tới tùy chọn trong vùng của nhà cung cấp hiện có, giữ khóa mã hóa của riêng bạn để nhà vận hành không giải mã được hồ sơ nhạy cảm, và giữ khối lượng công việc đóng gói container để nó vẫn di chuyển được. Điều đó chốt thỏa thuận ở chi phí giai đoạn hạt giống và tránh một cuộc tái kiến trúc mà bạn không có đường băng cho.

**Doanh nghiệp nhỏ.** Không có chuyên gia chủ quyền và ngân sách eo hẹp, hãy coi đây là câu hỏi rà soát hợp đồng và chọn nhà cung cấp, không phải chương trình kỹ thuật. Ưu tiên nhà cung cấp cung cấp vùng trong thẩm quyền, điều khoản xử lý dữ liệu minh bạch, và khóa do khách hàng giữ như tính năng tiêu chuẩn, và đọc điều khoản nhà thầu phụ và tiết lộ trước khi ký. Tự lưu trữ vì chủ quyền hiếm khi đáng ở đây: bạn sẽ thừa hưởng gánh nặng vận hành và bảo mật mà không có người để gánh.

**Doanh nghiệp lớn.** Nhiệm vụ là quản trị danh mục qua nhiều đội: một phân bậc chung về dữ liệu theo độ nhạy chủ quyền, một cái nhìn rủi ro tập trung về bao nhiêu tải trọng yếu nằm trên một nhà cung cấp hay một thẩm quyền, và kiểm soát khóa, khả năng di chuyển và diễn tập thoát được chuẩn hóa để mỗi nhóm thôi đặt cược riêng không phối hợp. Hãy lập ngân sách tường minh cho chi phí cao hơn và gánh nặng vận hành của bậc nhạy cảm, và giữ một lập trường có tài liệu, kiểm toán được mà bạn có thể trình cơ quan quản lý. Quản lý chủ quyền như rủi ro sống với chỉ số và nhịp xem xét, không phải một lần di chuyển.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Ưu tiên hạ tầng chủ quyền được chứng nhận (ví dụ chứng nhận kiểu SecNumCloud) và tiêu chuẩn mở cùng mã nguồn mở để nền tảng được bảo trì độc lập với bất kỳ nhà cung cấp đơn lẻ nào, và yêu cầu khả năng di chuyển và tiết lộ phơi nhiễm pháp lý ngay trong hợp đồng. Hãy công bố mô tả bằng ngôn ngữ đơn giản về nơi dữ liệu công dân nằm và ai có thể với tới nó, dành các kiểm soát chủ quyền đắt đỏ cho bậc thực sự nhạy cảm, và giữ các dịch vụ công ít nhạy cảm hơn trên hạ tầng toàn cầu rẻ hơn.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp công nghệ y tế nhỏ giành được khách hàng bệnh viện đầu tiên ở Đức, đòi dữ liệu bệnh nhân ở lại dưới thẩm quyền EU. Thay vì xây quá mức một ngăn xếp chủ quyền mà họ không đủ sức, những người sáng lập triển khai tới vùng EU của nhà cung cấp đám mây hiện có, giữ khóa mã hóa của riêng họ để nhà cung cấp không giải mã được hồ sơ nhạy cảm, và giữ khối lượng công việc đóng gói container để nó vẫn di chuyển được. Điều này mua phần lớn lợi ích chủ quyền khách hàng cần với chi phí một đội giai đoạn hạt giống gánh được, và chốt thỏa thuận mà không cần tái kiến trúc toàn bộ.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia phải giữ một số dữ liệu khách hàng trong EU và ngoài tầm với của luật tiết lộ nước ngoài. Thay vì bỏ nhà cung cấp đám mây toàn cầu, nó phân bậc tài sản của mình. Khối lượng công việc chung ở lại các vùng hyperscale vì quy mô. Dữ liệu khách hàng bị quản lý chạy ở các vùng EU với mã hóa **tự giữ khóa của bạn** (nhà cung cấp không giải mã được) và kế hoạch thoát đã kiểm thử tới nhà cung cấp thay thế. Điều này thỏa mãn cơ quan quản lý và khẩu vị rủi ro tập trung của chính ngân sách (chương 10.2) mà không cần cuộc di chuyển toàn bộ, hủy diệt năng lực.

**Chính phủ.** Một dịch vụ y tế quốc gia giữ hồ sơ y tế của công dân và đánh giá phơi nhiễm trước thẩm quyền nước ngoài là không chấp nhận được. Nó mua sắm một đám mây chủ quyền, nghĩa là hạ tầng do thực thể trong nước vận hành dưới chứng nhận quốc gia (ví dụ kiểu SecNumCloud), với điện toán bảo mật cho xử lý nhạy cảm nhất, và bắt buộc tiêu chuẩn mở (chương 3.8) và thành phần mã nguồn mở để nền tảng được bảo trì độc lập với bất kỳ nhà cung cấp đơn lẻ nào. Chi phí cao hơn và bộ tính năng hẹp hơn được chấp nhận làm giá của kiểm soát an ninh quốc gia và lòng tin công. Trong khi đó, các dịch vụ ít nhạy cảm hơn (một cổng thông tin công cộng) vẫn ở trên hạ tầng toàn cầu rẻ hơn.

## Luận chứng kinh doanh: động lực, ROI và TCO

Kinh tế của chủ quyền số là bất đối xứng, và được đóng khung tốt nhất như bảo hiểm chống lại các sự kiện xác suất thấp, tác động cao. Chi phí là hiển thị và lặp lại: hạ tầng chủ quyền và trong thẩm quyền thường đắt hơn, cung cấp ít dịch vụ được quản lý hơn, và đòi hỏi nhiều năng lực vận hành nội bộ hơn, tất cả đều nâng tổng chi phí sở hữu và có thể làm chậm phân phối. Lợi ích chủ yếu là thảm họa tránh được: tiền phạt quản lý và tái kiến trúc bị ép sau một phán quyết như *Schrems II*, mất quyền truy cập kết thúc doanh nghiệp nếu một nhà cung cấp bị trừng phạt hay bị cắt, hoặc thiệt hại danh tiếng và an ninh quốc gia khi dữ liệu nhạy cảm bị tiết lộ cho nước ngoài. Vì những rủi ro đuôi đó nghiêm trọng và ngày càng hợp lý, đầu tư tương xứng vào chủ quyền, đặc biệt các kiểm soát rẻ nhưng mạnh như quyền sở hữu khóa, khả năng di chuyển và tiêu chuẩn mở, thường có giá trị kỳ vọng dương mạnh, dù nó trông như chi phí thuần trên bảng tính trạng thái ổn định.

Cái bẫy ở cả hai phía là mất cân đối. *Đầu tư thiếu* để dữ liệu và hệ thống trọng yếu phơi nhiễm trước một thẩm quyền hay nhà cung cấp duy nhất không có lối thoát, biến rủi ro quản lý được thành sinh tử. *Đầu tư thừa*, bằng cách nội địa hóa mọi thứ và từ chối mọi nền tảng toàn cầu, đốt tiền, mất năng lực, và có thể *giảm* khả năng phục hồi bằng cách thu hẹp lựa chọn của bạn. Để lập luận với ban lãnh đạo, hãy gắn chi tiêu chủ quyền với phân bậc rủi ro dữ liệu và khối lượng công việc. Định lượng phơi nhiễm tập trung và thẩm quyền của các hệ thống viên ngọc quý. Định giá các kiểm soát rẻ (khóa, khả năng di chuyển, diễn tập thoát) giảm rủi ro cho chúng. Dành hạ tầng chủ quyền đắt đỏ cho bậc thực sự xứng đáng.

## Phản mẫu và cạm bẫy

- **Sân khấu chủ quyền:** quảng cáo cư trú dữ liệu trong nước trong khi nhà cung cấp có trụ sở nước ngoài vẫn giữ quyền truy cập pháp lý vào dữ liệu.
- **Nhầm mã hóa với chủ quyền:** mã hóa dữ liệu nhưng để nhà cung cấp giữ khóa, nên họ vẫn có thể bị buộc giải mã.
- **Xoay quá mức:** nội địa hóa và tự lưu trữ mọi thứ với chi phí hủy hoại và năng lực giảm, bất kể độ nhạy cảm.
- **Khóa chặt đơn mới:** thoát khỏi hyperscaler bằng cách hoàn toàn bị giam cầm bởi một nhà cung cấp "chủ quyền" không có lối thoát.
- **Không có lối thoát đã kiểm thử:** một kế hoạch thoát tồn tại trên giấy nhưng chưa từng diễn tập, nên khả năng di chuyển chưa được chứng minh.
- **Phớt lờ chuỗi cung ứng con người:** giả định mã nguồn mở hay tự lưu trữ trao chủ quyền mà không có người có kỹ năng để chạy nó.
- **Lập trường tĩnh:** đặt một vị thế chủ quyền một lần và không bao giờ xem lại khi luật và địa chính trị dịch chuyển.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** Chủ quyền không được xem xét và phản ứng; dữ liệu và hệ thống trọng yếu nằm ở nơi rẻ nhất, không có bản đồ rủi ro thẩm quyền hay tập trung và không có chủ sở hữu.
- **Mức 2 (Phát triển):** Cư trú dữ liệu được giải quyết cho dữ liệu bị quản lý rõ ràng nhất ở một số dự án, nhưng thẩm quyền, kiểm soát khóa và lối thoát không được xem xét có hệ thống; thực hành khác nhau theo đội, và việc dựa vào các nhà cung cấp đơn lẻ không được xem xét.
- **Mức 3 (Chuẩn hóa):** Dữ liệu và khối lượng công việc được phân bậc theo độ nhạy chủ quyền dưới chính sách có tài liệu áp dụng toàn tổ chức; thẩm quyền được lập bản đồ; kiểm soát khóa, khả năng di chuyển và tiêu chuẩn mở được yêu cầu ở các bậc nhạy cảm; kế hoạch thoát tồn tại và được bắt buộc thay vì tùy chọn.
- **Mức 4 (Quản lý):** Lập trường được đo và kiểm soát theo đường cơ sở: rủi ro tập trung (tỷ lệ khối lượng công việc trọng yếu trên một nhà cung cấp hay thẩm quyền), độ phủ quyền sở hữu khóa qua các tập dữ liệu nhạy cảm, độ hoàn chỉnh của bản đồ thẩm quyền, và thời gian thoát đã diễn tập được theo dõi như chỉ số, báo cáo cho quản trị, và thực thi theo ngưỡng, nên một phụ thuộc đang trôi kích hoạt hành động dựa trên bằng chứng thay vì sau một cú sốc.
- **Mức 5 (Điều phối):** Chủ quyền được cải thiện liên tục và tích hợp trong toàn tổ chức: khung rủi ro sống nuôi kiến trúc, mua sắm và hoạch định rủi ro theo mặc định, lối thoát được diễn tập thường lệ, và tổ chức thích ứng thu hẹp phạm vi các bậc, cân bằng lại nhà cung cấp và sửa đổi lập trường khi phán quyết, lệnh trừng phạt và quy định dịch chuyển.

## Ý tưởng để thảo luận

1. Với tập dữ liệu nhạy cảm nhất của bạn, chính phủ nào có thể buộc truy cập nó một cách hợp pháp hôm nay, và bạn có biết không?
2. Cư trú dữ liệu của bạn là chủ quyền thật, hay một nhà cung cấp có trụ sở nước ngoài vẫn giữ khóa và phơi nhiễm pháp lý?
3. Bạn có thực sự rời được nhà cung cấp đám mây chính nếu phải không, và bạn đã bao giờ kiểm thử chưa?
4. Khối lượng công việc nào của bạn thực sự cần hạ tầng chủ quyền, và cái nào bạn đang bảo vệ quá mức với chi phí không cần thiết?
5. Kiểm soát khóa mã hóa của riêng bạn sẽ mang lại phần lớn lợi ích chủ quyền với một phần nhỏ chi phí ở đâu?
6. Một lệnh trừng phạt, sự cố hay phán quyết pháp lý với nhà cung cấp chính sẽ ảnh hưởng thế nào đến các dịch vụ trọng yếu của bạn vào tuần tới?

## Những điểm cần ghi nhớ

- Chủ quyền số là kiểm soát tương xứng đối với dữ liệu, phần mềm và hạ tầng của bạn, qua các chiều dữ liệu, vận hành, phần mềm và chuỗi cung ứng.
- **Vị trí không phải thẩm quyền:** chỉ cư trú không ngăn truy cập pháp lý nước ngoài; hãy lập bản đồ ai có thể buộc tiết lộ.
- **Thiết kế cho lối thoát** và **kiểm soát khóa của bạn:** khả năng di chuyển và quyền sở hữu khóa là kiểm soát đòn bẩy cao nhất, chi phí thấp nhất.
- **Tiêu chuẩn mở và mã nguồn mở** là công cụ tự chủ chiến lược; hãy dành **đám mây chủ quyền** đắt đỏ cho bậc xứng đáng.
- Quản trị chủ quyền như **rủi ro sống, tương xứng** (chương 10.2, 10.3, 4.5, 4.6, 3.8), tránh cả bảo vệ thiếu lẫn xoay quá mức hủy hoại.
- ROI là bảo hiểm chống rủi ro đuôi nghiêm trọng (quy định, địa chính trị và khóa chặt) được định giá so với chi phí thật, lặp lại.

## Tài liệu tham khảo và đọc thêm

- European Court of Justice, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Regulation (EU) 2016/679, *General Data Protection Regulation (GDPR)*; Regulation (EU) 2023/2854, *Data Act*.
- U.S. *Clarifying Lawful Overseas Use of Data (CLOUD) Act* (2018).
- ANSSI, khung chứng nhận *SecNumCloud* (Pháp).
- Gaia-X European Association for Data and Cloud (sáng kiến Gaia-X).
- ENISA, các báo cáo về bảo mật đám mây và chứng nhận an ninh mạng EU (EUCS).
- Julia Pohle và Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, các bài viết về tự chủ số châu Âu và sự phụ thuộc vào nhà cung cấp nước ngoài.
- Kai Zenner và những người khác, các phân tích về chính sách chủ quyền số của EU (để tham khảo ngữ cảnh; hãy xác minh nguồn hiện hành).
