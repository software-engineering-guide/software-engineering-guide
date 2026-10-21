# 10.10 Kinh tế học kỹ thuật phần mềm

## Tổng quan và động lực

Kinh tế học kỹ thuật phần mềm là kỷ luật đưa ra các quyết định kỹ thuật theo giá trị và chi phí, dưới độ bất định, theo thời gian. Đó là lập luận trả lời những câu hỏi mà lãnh đạo thực sự đặt ra. Cái này có đáng xây không? Trong ba phương án này, phương án nào cho lợi tức tốt nhất? Chúng ta sẽ tốn bao nhiêu để sở hữu hệ thống này trong thập kỷ tới, không chỉ để phát hành nó trong quý này? Chúng ta nên trả bớt [nợ kỹ thuật](https://en.wikipedia.org/wiki/Technical_debt) này ngay bây giờ, hay hoãn nó và trả lãi? Mọi lộ trình, mua sắm, khoản đầu tư nền tảng và chương trình hiện đại hóa, ở bên dưới, là một lập luận kinh tế. Chương này nêu tên kỷ luật làm những lập luận đó tường minh, so sánh được và bảo vệ được.

Với một đội đơn lẻ, lập luận kinh tế có thể giữ không chính thức, vì chi phí của một quyết định sai nhỏ và được sửa nhanh. Với một tổ chức doanh nghiệp hay chính phủ, rủi ro lớn, tiền là của người khác, và các quyết định bị tài chính, kiểm toán viên và công chúng soi xét. Một chương trình trông rẻ vì ai đó chỉ đếm chi phí xây dựng, và bỏ qua nhiều năm vận hành, cấp phép, hỗ trợ và thay thế cuối cùng, sẽ vượt ngân sách với độ tin cậy đáng ngại. Một đề xuất hứa hẹn lợi tức nhưng không bao giờ nêu giả định thì không thể bị thách thức, so sánh hay buộc chịu trách nhiệm. Kinh tế học kỹ thuật phần mềm cho bạn một ngôn ngữ định lượng chung, để vốn khan hiếm chảy tới công việc tạo ra nhiều giá trị nhất.

Chương này là xương sống phân tích của lập luận [lợi tức đầu tư](https://en.wikipedia.org/wiki/Return_on_investment) (ROI) và [tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO) được dùng xuyên suốt cẩm nang này. Quản lý danh mục và chương trình (chương 10.1) quyết định *tài trợ gì*; chương này cung cấp phương pháp kinh tế cho việc *quyết định thế nào*. Nó nối với mua sắm (chương 10.3), nơi những phép tính này biện minh cho lựa chọn mua-so-với-xây và hợp đồng; với chi phí, FinOps (vận hành tài chính, tức quản lý có kỷ luật chi tiêu đám mây và thời gian chạy), và phần mềm xanh (chương 9.4), biến kinh tế chi phí vận hành thành thực hành vận hành; với đường ống khám phá và kết quả (chương 11.1), nơi các giả thuyết giá trị được hình thành và kiểm thử; với nợ kỹ thuật trong ra quyết định và quản trị (chương 1.5); và với bảo trì phần mềm (chương 3.7), nơi cái đuôi dài của chi phí sở hữu thực sự đáp xuống.

## Các nguyên tắc chính

- **Giá trị và chi phí đều là ước tính.** Coi mỗi con số là một khoảng với các giả định, không phải sự thật. Bất định trung thực thắng độ chính xác giả.
- **Tiền có giá trị thời gian.** Một đô la hôm nay đáng hơn một đô la năm sau; hãy chiết khấu dòng tiền tương lai trước khi so sánh các phương án.
- **Quyết định theo tổng chi phí sở hữu, không phải giá mua.** Bản xây là khoản trả trước; vận hành, hỗ trợ và duy trì là khoản thế chấp.
- **Chỉ chi phí và lợi ích tương lai mới quan trọng với một quyết định.** [Chi phí chìm](https://en.wikipedia.org/wiki/Sunk_cost) đã mất; hãy bỏ qua chúng khi chọn làm gì tiếp theo.
- **Mọi lựa chọn đều có [chi phí cơ hội](https://en.wikipedia.org/wiki/Opportunity_cost).** So sánh thích hợp luôn là cách sử dụng thay thế tốt nhất cho cùng tiền, con người và thời gian.
- **Trì hoãn có giá.** [Chi phí trì hoãn](https://en.wikipedia.org/wiki/Cost_of_delay), giá trị bị bỏ lỡ trong khi một quyết định hay bàn giao phải chờ, thường là con số lớn nhất và bị bỏ qua nhiều nhất trong mô hình.
- **Làm luận chứng kinh doanh có thể bị bác bỏ.** Nêu giả định rõ đến mức thực tế sau này có thể chứng minh chúng đúng hay sai.

## Khuyến nghị

### Đặt quyết định trên nền tảng kinh tế học

Hãy xây từ vựng chung trước khi xây bảng tính. Phân biệt *giá trị* (lợi ích một bên liên quan nhận được) với *chi phí* (cái bị tiêu thụ để tạo ra nó), và diễn đạt cả hai dưới dạng *dòng tiền*, tiền vào hay ra tại những thời điểm cụ thể. Vì một khoản thanh toán năm sau đáng giá ít hơn một khoản hôm nay, hãy áp dụng *[giá trị thời gian của tiền](https://en.wikipedia.org/wiki/Time_value_of_money)*: chiết khấu dòng tiền tương lai về giá trị hiện tại bằng tỷ lệ chiết khấu phản ánh [chi phí vốn](https://en.wikipedia.org/wiki/Cost_of_capital) của bạn hoặc một tỷ lệ chính thức. Một *đề xuất* khi đó là sự so sánh có cấu trúc các dòng tiền của các phương án cạnh tranh trong một chân trời xác định. Hãy khăng khăng rằng mọi đề xuất đáng kể nêu chân trời, tỷ lệ chiết khấu và giả định trên một trang, để người rà soát tranh luận về bản chất thay vì dịch ngược phép toán.

### Quyết định tường minh dưới độ bất định và rủi ro

Quyết định phần mềm được đưa ra với thông tin không đầy đủ. Giả vờ khác đi là sai lầm. Hãy mô hình hóa độ bất định thay vì giấu nó. Dùng ước tính ba điểm (lạc quan, khả dĩ, bi quan) thay cho con số đơn, và tính một *[giá trị kỳ vọng](https://en.wikipedia.org/wiki/Expected_value)* bằng cách gán trọng số cho các kết quả theo xác suất của chúng. Với các lựa chọn hệ trọng, hãy chạy [phân tích độ nhạy](https://en.wikipedia.org/wiki/Sensitivity_analysis): thay đổi hai hoặc ba đầu vào quan trọng nhất và xem khuyến nghị có đảo không. Phân biệt *rủi ro* (xác suất định lượng được) với *bất định* sâu (xác suất không biết), và ưu tiên các phương án bảo toàn tính linh hoạt khi độ bất định cao. Một cam kết theo giai đoạn cho phép bạn dừng, xoay hay tăng cược sau khi học thường đáng giá hơn một canh bạc ăn cả ngã về không rẻ hơn.

### Khớp phương pháp quyết định với bối cảnh vì lợi nhuận và công

Các tổ chức vì lợi nhuận thường tối ưu lợi tức tài chính, dùng [giá trị hiện tại ròng](https://en.wikipedia.org/wiki/Net_present_value), ROI và thời gian hoàn vốn, so với chi phí vốn. Các tổ chức phi lợi nhuận và khu vực công tối ưu giá trị sứ mệnh, kết quả dịch vụ, công bằng và quản gia tiền công, và họ không thể quy mọi lợi ích về doanh thu. Hãy dùng cùng bộ máy phân tích ở cả hai bối cảnh, nhưng chọn hàm mục tiêu một cách trung thực. Trong chính phủ, phân tích [chi phí-lợi ích](https://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis) và hiệu quả chi phí, tỷ lệ chiết khấu chính thức, và tính chi phí toàn vòng đời thường bị bắt buộc. Hãy tiền tệ hóa những gì tiền tệ hóa được, và với phần còn lại dùng tiêu chí phi tài chính tường minh, có tài liệu thay vì lén đưa chúng vào như hệ số bù. Ở cả hai thế giới, kỷ luật là như nhau: làm mục tiêu và các đánh đổi hiển thị.

### Ước tính chi phí bằng nhiều hơn một phương pháp

Không cách tiếp cận ước lượng đơn lẻ nào đáng tin một mình, nên hãy tam giác hóa. Kết hợp *tương tự* (so với công việc tương tự trong quá khứ), *phán đoán chuyên gia* (đầu vào có cấu trúc từ kỹ sư giàu kinh nghiệm, ví dụ Delphi băng rộng hay planning poker), *phân rã* (chia nhỏ công việc và cộng ước tính lên, từ dưới lên), và *mô hình tham số* (dựa trên công thức, như [COCOMO II](https://en.wikipedia.org/wiki/COCOMO), được hiệu chỉnh theo dữ liệu của bạn). Nơi bạn có thông lượng thực nghiệm, hãy ưu tiên dữ liệu luồng lịch sử hơn định cỡ suy đoán. Luôn diễn đạt ước tính dưới dạng khoảng với độ tin cậy, ước tính lại khi bạn học, và tách ước tính *công sức* khỏi cam kết một *ngày*. Trộn lẫn hai thứ đó là cách ước tính trở thành lời hứa bị phá.

### Tính TCO, ROI, NPV và hoàn vốn nhất quán

Hãy áp dụng một bộ công cụ nhỏ, tiêu chuẩn và dùng nó đồng đều, để các phương án so sánh được qua danh mục. *Tổng chi phí sở hữu* cộng mọi chi phí qua toàn bộ vòng đời: xây dựng, triển khai, cấp phép, vận hành, hỗ trợ, bảo mật và loại bỏ. *ROI* diễn đạt lợi ích ròng dưới dạng phần trăm của chi phí. *Giá trị hiện tại ròng (NPV)* chiết khấu mọi dòng tiền tương lai về hôm nay và cộng chúng; NPV dương nghĩa là phương án tạo giá trị ở tỷ lệ chiết khấu của bạn. *[Thời gian hoàn vốn](https://en.wikipedia.org/wiki/Payback_period)* là thời gian thu hồi khoản chi ban đầu. Nó đơn giản và trực quan, nhưng mù với mọi thứ sau điểm hòa vốn và với giá trị thời gian của tiền, nên chỉ dùng nó cùng NPV. Chuẩn hóa chân trời và tỷ lệ chiết khấu qua các phương án được so sánh, nếu không phép so sánh vô nghĩa.

### Định giá nợ kỹ thuật và chi phí trì hoãn

Hãy làm hai chi phí thường vô hình trở nên tường minh. *Nợ kỹ thuật* hành xử như nợ tài chính: lối tắt vay tốc độ bây giờ và tính lãi về sau, dưới dạng phân phối chậm hơn, nhiều lỗi hơn và chi phí vận hành cao hơn. Hãy ước tính lãi, nợ đánh thuế mỗi bản phát hành tương lai bao nhiêu, để lựa chọn gánh hay trả nó thành quyết định kinh tế thay vì đạo đức (xem chương 1.5 và 3.7). *Chi phí trì hoãn* là giá trị mất cho mỗi đơn vị thời gian một thứ có giá trị bị trễ. Định lượng nó biến bản năng mơ hồ "chúng ta nên vội" thành ưu tiên thật, trực tiếp nhất qua sắp thứ tự Công-việc-ngắn-nhất-có-trọng-số-trước. Các đội định giá trì hoãn thôi tối ưu mức sử dụng và bắt đầu tối ưu giá trị.

### Định giá cái vô hình và xây dựng luận chứng kinh doanh

Nhiều lợi ích lớn nhất không chịu một con số đô la gọn: giảm rủi ro, cải thiện tư thế bảo mật, năng suất nhà phát triển, lòng tin thương hiệu, kết quả sứ mệnh, tính linh hoạt lựa chọn. Giả vờ chúng bằng không làm thiên lệch mọi quyết định về phía hữu hình. Hãy định giá chúng dù sao. Tiền tệ hóa qua đại diện nơi đáng tin (chi phí một vụ vi phạm tránh được, giờ tiết kiệm nhân với mức lương toàn phần). Nơi bạn không thể, hãy chấm điểm tường minh theo tiêu chí có tên và mang chúng cạnh mô hình tài chính. Lắp tất cả thành một *luận chứng kinh doanh*: vấn đề, các phương án đã xem xét (gồm không làm gì), chi phí và lợi ích qua chân trời, giả định và rủi ro then chốt, khuyến nghị, và các thước đo bạn sẽ dùng sau này để đánh giá nó có hiệu quả không. Giữ nó sống, và xem xét lại so với thực tế để tổ chức của bạn học ước lượng tốt hơn.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Mô hình hóa định lượng chi tiết (NPV, TCO) | Nghiêm ngặt, so sánh được, kiểm toán được; buộc giả định ra ánh sáng | Tốn thời gian; độ chính xác giả nếu đầu vào yếu; có thể loại trừ cái không đo được |
| Quy tắc kinh nghiệm nhẹ (hoàn vốn, chi phí trì hoãn) | Nhanh, trực quan, dễ truyền đạt | Bỏ qua giá trị thời gian hay chi phí đuôi dài; thô cho cam kết lớn |
| Ước tính con số đơn | Đơn giản, dứt khoát, dễ hoạch định quanh | Giấu bất định; thành lời hứa giả; trừng phạt sự trung thực |
| Khoảng và giá trị kỳ vọng | Trung thực về rủi ro; hỗ trợ quyết định theo giai đoạn | Khó truyền đạt hơn; có thể cảm giác lẩn tránh với các bên muốn một con số |
| Tiền tệ hóa cái vô hình qua đại diện | Giữ lợi ích lớn trong mô hình; cho phép đánh đổi | Đại diện gây tranh cãi; rủi ro bịa con số tiện lợi |
| Phân tích TCO toàn vòng đời đầy đủ | Ngăn bất ngờ xây-rẻ-chạy-đắt | Cần dữ liệu chi phí vận hành mà nhiều đội thiếu lúc đầu |

Căng thẳng lặp lại là giữa độ nghiêm ngặt và tốc độ. Mô hình hóa tài chính nặng cải thiện các quyết định lớn, không đảo ngược, đắt đỏ, nhưng lãng phí, thậm chí có hại, với các quyết định nhỏ, đảo ngược được, nơi nó chỉ rửa một câu trả lời định sẵn bằng uy quyền bảng tính. Các tổ chức trưởng thành điều chỉnh phân tích cho vừa mức rủi ro: một lập luận chi phí trì hoãn một trang cho tính năng thường lệ, một luận chứng NPV-và-TCO đầy đủ cho nền tảng hay mua sắm nhiều năm. Căng thẳng thứ hai là giữa độ chính xác và sự trung thực. Một con số tự tin duy nhất dễ hành động hơn nhưng thường sai. Một khoảng thì trung thực nhưng khó cam kết hơn. Cách giải quyết là quyết định bằng khoảng và giá trị kỳ vọng, rồi cam kết theo phần tăng trưởng từng giai đoạn, để bạn giữ lựa chọn sửa hướng khi bằng chứng đến.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta có tách ước tính công sức khỏi cam kết ngày, và có tam giác hóa ước tính thay vì tin một con số không?** Một con số tự tin duy nhất dễ hoạch định quanh và thường sai, và khoảnh khắc một ước tính công sức theo khoảng cứng thành ngày cố định, sự trung thực bị trừng phạt và ước tính trở thành lời hứa bị phá. Hãy tam giác hóa: kết hợp tương tự, phán đoán chuyên gia, phân rã và thông lượng lịch sử, và ưu tiên dữ liệu luồng thật hơn định cỡ suy đoán. Diễn đạt ước tính dưới dạng khoảng với độ tin cậy, và ước tính lại khi bạn học. Với chương trình lớn dưới sự soi xét của tài chính và kiểm toán, đây là sự khác biệt giữa dự báo bảo vệ được và con số không ai thách thức nổi. Hãy mang một ước tính gần đây đã trượt và hỏi liệu đó có phải ước tính công sức bị quản lý theo lịch không.

2. **Chúng ta có định giá chi phí trì hoãn và dùng nó để sắp thứ tự công việc, hay vẫn tối ưu mức sử dụng?** Chi phí trì hoãn, giá trị mất cho mỗi đơn vị thời gian một thứ có giá trị bị trễ, thường là con số lớn nhất và bị bỏ qua nhiều nhất trong mô hình. Các đội không bao giờ định giá nó tối ưu việc giữ mọi người bận, lặng lẽ bỏ đói công việc giá trị cao nhất. Hãy định lượng nó và sắp thứ tự bằng Công-việc-ngắn-nhất-có-trọng-số-trước để công việc mất nhiều giá trị nhất khi chờ đi trước. Điều này sắp xếp lại lộ trình và đóng khung lại "chúng ta nên vội" thành ưu tiên thật. Hãy mang hai ba sáng kiến đang tiến hành và ước tính mỗi cái tốn bao nhiêu cho mỗi tuần trì hoãn; nếu bạn không làm được, đó là khoảng trống cần đóng.

3. **Luận chứng kinh doanh của chúng ta có quyết định theo TCO toàn vòng đời so với đường cơ sở không-làm-gì, và độ nghiêm ngặt có vừa mức rủi ro không?** Bản xây là khoản trả trước; vận hành, cấp phép, hỗ trợ và thay thế cuối cùng là khoản thế chấp, và một chương trình chỉ đếm chi phí xây sẽ vượt ngân sách với độ tin cậy đáng ngại. Mọi đề xuất nghiêm túc nên so sánh các phương án (gồm không làm gì) qua một chân trời tiêu chuẩn ở tỷ lệ chiết khấu chung, và nêu giả định trên một trang để người rà soát tranh luận bản chất thay vì số học. Điều chỉnh công sức cho vừa: một lập luận chi phí trì hoãn một trang cho tính năng thường lệ, một luận chứng NPV-và-TCO đầy đủ cho nền tảng hay mua sắm nhiều năm. Mô hình hóa nặng một quyết định nhỏ, đảo ngược được chỉ rửa một câu trả lời định sẵn bằng uy quyền bảng tính. Hãy mang một quyết định gần đây và hỏi liệu chi phí vận hành, không phải giá niêm yết, có thúc đẩy nó không.

4. **Chúng ta dùng tỷ lệ chiết khấu nào để so sánh các phương án theo thời gian, và đã kiểm thử khuyến nghị có sống sót qua một tỷ lệ khác chưa?** Giá trị thời gian của tiền nghĩa là một đô la năm thứ năm không phải một đô la hôm nay, vậy mà nhiều đề xuất hoặc bỏ qua chiết khấu hoàn toàn hoặc chôn một tỷ lệ không ai đồng ý. Hãy chuẩn hóa một tỷ lệ và một chân trời qua các phương án được so sánh, nếu không phép so sánh là số học khoác lên áo hiểu biết. Cân nhắc đối lập là bản thân tỷ lệ gây tranh cãi: quá thấp và bạn tâng bốc các siêu dự án dài hạn, quá cao và bạn bỏ đói các khoản đầu tư hoàn vốn chậm. Hãy mang tỷ lệ bạn đã dùng, nó đến từ đâu (chi phí vốn của bạn, hay một tỷ lệ chính thức đã công bố), và một phân tích độ nhạy cho thấy ở tỷ lệ nào khuyến nghị đảo chiều. Với tài chính doanh nghiệp và đặc biệt chính phủ, tỷ lệ thường bị bắt buộc, ví dụ tỷ lệ thẩm định chính thức, và một tỷ lệ không có tài liệu hay không nhất quán chính xác là thứ kiểm toán viên sẽ thách thức trước tiên.

5. **Khi một sáng kiến kém hiệu quả, chúng ta có quyết định theo giá trị tương lai kỳ vọng và bỏ qua cái đã chi, và chúng ta đã cấu trúc tài trợ để thực sự dừng được chưa?** Chi phí chìm đã mất, nhưng chúng có sức kéo mạnh: các đội bảo vệ nỗ lực thất bại bằng số tiền đã đổ vào thay vì giá trị còn ở phía trước. Áp lực đối lập là thật, vì dừng trông như thừa nhận lãng phí và mang chi phí chính trị, nên kỷ luật phải được xây vào cách bạn tài trợ thay vì để cho cảm giác của ai đó vào lúc đó. Hãy ưu tiên cam kết theo giai đoạn độc lập có giá trị và cho phép bạn dừng, xoay hay tăng cược sau mỗi phần tăng trưởng, thay vì một canh bạc không đảo ngược. Hãy mang một nỗ lực đang tiến hành bị chậm, chi phí còn lại để hoàn thành đặt cạnh lợi ích còn lại kỳ vọng, và điểm mà cổng tài trợ tiếp theo rơi vào. Trong danh mục doanh nghiệp hay chính phủ, hãy nêu ai giữ thẩm quyền ngừng một chương trình và liệu cấu trúc tài trợ có cho họ một điểm quyết định thật không, vì một cam kết không có cổng là cam kết không ai dừng được.

6. **Chúng ta có trung thực về hàm mục tiêu của mình, và có định giá cái vô hình tường minh thay vì coi chúng bằng không không?** Một số lợi ích lớn nhất, giảm rủi ro, tư thế bảo mật, năng suất nhà phát triển, kết quả sứ mệnh và tính linh hoạt lựa chọn, không chịu một con số đô la gọn, và giả vờ chúng bằng không làm thiên lệch mọi quyết định về phía hữu hình và ngắn hạn. Rủi ro đối lập là sai lầm ngược lại: bịa một con số tiện lợi và khoác một phỏng đoán bằng độ chính xác giả. Hãy quyết định có chủ đích những lợi ích nào bạn sẽ tiền tệ hóa qua đại diện đáng tin (một vụ vi phạm tránh được, giờ tiết kiệm nhân với mức lương toàn phần) và những lợi ích nào bạn sẽ chấm theo tiêu chí phi tài chính có tên mang cạnh mô hình. Hãy mang một quyết định gần đây nơi một thứ vô hình quan trọng và hỏi nó được định giá, chấm điểm, hay lặng lẽ bị bỏ. Với cơ quan khu vực công điều này còn sắc hơn: giá trị sứ mệnh, công bằng và quản gia tiền công không thể quy hết về doanh thu, nên hãy chọn hàm mục tiêu công khai và lập tài liệu các tiêu chí phi tài chính thay vì lén đưa chúng vào như hệ số bù.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với vài tháng đường băng, con số kinh tế chi phối là chi phí trì hoãn: mỗi tuần vài kỹ sư của bạn dành ngoài sản phẩm cốt lõi là doanh thu và việc học bị hoãn. Giữ phân tích trong một trang và ưu tiên mua năng lực hàng hóa thông dụng hơn xây chúng, để sự chú ý khan hiếm của kỹ sư ở lại với yếu tố tạo khác biệt. Bỏ qua các mô hình NPV cầu kỳ; một so sánh toàn vòng đời thô và trần chi tiêu cứng là đủ để bắt cái bẫy xây-rẻ-chạy-đắt trước khi nó cắn.

**Doanh nghiệp nhỏ.** Bạn không có nhà phân tích tài chính, nên hãy giữ phương pháp đơn giản và trung thực: so sánh chi phí sở hữu đầy đủ của từng phương án, đăng ký cộng giờ nhân viên nó tiêu tốn, với không làm gì. Quyết định mua-so-với-xây hầu như luôn nghiêng về mua, vì một hệ thống bạn không bảo trì được trở thành chi phí vận hành không có ngân sách lặng lẽ lớn dần. Đánh giá đầu tư theo thời gian hoàn vốn ngắn, trực quan thay vì mô hình chiết khấu, và coi chừng giá theo ghế trông rẻ cho đến khi bạn mở rộng.

**Doanh nghiệp lớn.** Thách thức là khả năng so sánh qua nhiều đội và một danh mục dài: chuẩn hóa một tỷ lệ chiết khấu, một chân trời và một bộ công cụ (NPV, TCO, chi phí trì hoãn) để các đề xuất cạnh tranh được xếp hạng trên cùng cơ sở. Định giá tường minh lãi nợ kỹ thuật và chi phí trì hoãn, vì ở quy mô chúng lấn át chi phí xây dựng tiêu đề. Làm luận chứng kinh doanh thành tài liệu sống được xem xét lại so với thực tế, để độ chính xác ước lượng cải thiện và tài chính cùng kiểm toán thấy được vì sao vốn chảy tới nơi nó chảy.

**Chính phủ.** Phân tích chi phí-lợi ích, tỷ lệ chiết khấu chính thức và tính chi phí toàn vòng đời thường bị bắt buộc, và mục tiêu là giá trị công thay vì doanh thu, nên hãy tiền tệ hóa những gì bạn đáng tin cậy làm được và chấm điểm phần còn lại theo tiêu chí tường minh, đã công bố. Nêu mọi giả định công khai so với đường cơ sở không-làm-gì, vì kiểm toán viên và công chúng sẽ kiểm thử chúng. Cấu trúc tài trợ thành các phần tăng trưởng độc lập có giá trị để lợi ích của mỗi giai đoạn được hiện thực hóa và đo trước khi cái tiếp theo được cam kết, và để một chương trình có thể bị dừng mà không bỏ rơi tiền công đã chìm.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người với chín tháng đường băng tranh luận có nên xây hệ thống thanh toán riêng hay trả tiền cho một hệ thống lưu trữ. Trên một trang, những người sáng lập so sánh hai phương án trong chân trời mười tám tháng: bản xây trông rẻ hơn trên giấy nhưng tốn ba tháng-kỹ-sư ngay từ đầu, và chi phí trì hoãn (doanh thu bị hoãn trong khi các kỹ sư đó không phát hành sản phẩm cốt lõi) lấn át phí đăng ký. Họ mua thanh toán lưu trữ, bảo vệ thời gian kỹ thuật khan hiếm cho yếu tố tạo khác biệt, và chỉ xem xét lại quyết định nếu giá hay khối lượng đổi phép toán.

**Doanh nghiệp lớn.** Một nhà bán lẻ cân nhắc chuyển nền tảng thương mại điện tử so với tiếp tục vá hệ thống hiện tại. Đội kỹ thuật-và-tài chính xây một mô hình năm năm ở tỷ lệ chiết khấu của công ty, so sánh ba phương án (không làm gì, tái cấu trúc gia tăng, và chuyển nền tảng đầy đủ) về TCO qua xây dựng, chi phí chạy đám mây, cấp phép và hỗ trợ. Họ định lượng lãi nợ kỹ thuật của hiện trạng (tỷ lệ sự cố tăng và nhịp phát hành chậm lại) và chi phí trì hoãn của các tính năng mà ngăn xếp cũ không hỗ trợ được. Việc chuyển nền tảng cho thấy chi phí ban đầu cao hơn nhưng NPV dương vào năm thứ ba và chi phí vận hành thấp hơn sau đó. Phân tích độ nhạy xác nhận khuyến nghị đứng vững trừ khi giá đám mây tăng mạnh. Họ tài trợ theo giai đoạn gắn với cột mốc thay vì một cam kết không đảo ngược.

**Chính phủ.** Một cơ quan hiện đại hóa hệ thống trợ cấp được yêu cầu nộp phân tích chi phí-lợi ích dùng tỷ lệ chiết khấu chính thức và tính chi phí toàn vòng đời. Vì lợi ích chính là kết quả sứ mệnh (dịch vụ nhanh hơn, chính xác hơn, công bằng hơn), đội tiền tệ hóa những gì họ đáng tin cậy làm được (giảm tải tổng đài, ít khoản chi sai hơn, gian lận tránh được) và chấm điểm phần còn lại theo tiêu chí giá trị công tường minh thay vì bịa số đô la. Luận chứng kinh doanh trình bày đường cơ sở không-làm-gì, nêu giả định công khai cho kiểm toán, và cấu trúc tài trợ thành các phần tăng trưởng độc lập có giá trị, để lợi ích của mỗi giai đoạn được hiện thực hóa và đo trước khi cái tiếp theo được cam kết.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của việc thực hành kinh tế học kỹ thuật phần mềm là phân bổ vốn tốt hơn: tiền, con người và thời gian chảy tới công việc tạo ra nhiều giá trị nhất. Cơ chế gồm ba phần. Thứ nhất, lãng phí tránh được: các đề xuất trượt phép thử NPV hay TCO trung thực bị từ chối trước khi tiêu tốn nhiều năm chi tiêu. Thứ hai, sắp thứ tự tốt hơn: định giá chi phí trì hoãn đẩy công việc giá trị cao nhất lên trước, cộng dồn lợi tức qua danh mục. Thứ ba, ít bất ngờ đắt đỏ hơn: tính chi phí toàn vòng đời ngăn thất bại kinh điển là tài trợ một bản xây rẻ và bị phục kích bởi vận hành đắt.

Chi phí của thực hành là khiêm tốn: thời gian nhà phân tích để xây mô hình, kỷ luật nêu giả định, và công việc văn hóa khiến lãnh đạo quyết định theo con số toàn vòng đời đã chiết khấu thay vì giá tiêu đề. Chi phí của việc *không* thực hành lớn hơn nhưng phân tán. Bạn đánh giá quá cao một cách có hệ thống cái hữu hình và ngắn hạn, định giá thấp nợ và trì hoãn, và chỉ phát hiện chi phí vận hành khi chúng đã không thể tránh. Hãy đóng khung kỷ luật với lãnh đạo là kiểm soát chất lượng trên mọi quyết định đầu tư khác. Nó không thêm một dòng chi tiêu mới mà làm mọi dòng chi tiêu hiện có chịu trách nhiệm. Một chương trình giá trị thấp duy nhất tránh được, hoặc một dự báo TCO chính xác ngăn một cú vượt chi phí vận hành, hoàn vốn cho cả thực hành nhiều lần.

## Phản mẫu và cạm bẫy

- **Giá mua như tổng chi phí.** Quyết định theo phí xây hay cấp phép trong khi bỏ qua nhiều năm vận hành, hỗ trợ và thay thế cuối cùng.
- **Cam kết chi phí chìm.** Tiếp tục một nỗ lực thất bại vì tiền đã chi thay vì giá trị tương lai kỳ vọng.
- **Sân khấu độ chính xác.** Bảng tính mười chữ số thập phân xây trên đầu vào phỏng đoán, tạo uy quyền giả cho kết luận định sẵn.
- **Phớt lờ giá trị thời gian của tiền.** So sánh dòng tiền gần và xa như thể một đô la năm thứ năm bằng một đô la hôm nay.
- **Cái vô hình bằng không.** Loại trừ rủi ro, bảo mật, năng suất và giá trị sứ mệnh vì chúng khó định giá, làm thiên lệch mọi quyết định về phía đo được.
- **Ước tính như lời hứa.** Coi ước tính công sức theo khoảng như cam kết ngày cố định, rồi quản lý theo lịch.
- **Nợ kỹ thuật không định giá.** Đi lối tắt mà không tính lãi, cho đến khi thuế cộng dồn lên phân phối thành khủng hoảng.
- **Mù chi phí trì hoãn.** Tối ưu mức sử dụng đội và chi phí đơn vị trong khi bỏ qua giá trị mất lớn hơn nhiều vì sự trễ.

## Mô hình trưởng thành

**Mức 1 (Khởi đầu).** Quyết định được biện minh bằng giá tiêu đề và cảm tính, phản ứng và từng trường hợp. Không chiết khấu, không TCO, không giả định được nêu. Ước tính là con số đơn bị coi là lời hứa. Nợ kỹ thuật và chi phí trì hoãn vô hình trong mọi mô hình.

**Mức 2 (Phát triển).** Các khoản đầu tư lớn hơn mang luận chứng kinh doanh thô với một số chi phí và lợi ích, và một số chi phí vận hành được xem xét. Hoàn vốn hay ROI đơn giản xuất hiện, nhưng giá trị thời gian của tiền và tính chi phí toàn vòng đời được áp dụng không đồng đều và khác nhau theo đội. Ước tính đôi khi mang khoảng, dù thực hành không nhất quán.

**Mức 3 (Chuẩn hóa).** Bộ công cụ kinh tế tiêu chuẩn (NPV, TCO, ROI, chi phí trì hoãn) với tỷ lệ chiết khấu và chân trời chung được lập tài liệu và áp dụng nhất quán qua danh mục. Độ bất định được mô hình hóa bằng khoảng và giá trị kỳ vọng. Nợ kỹ thuật được ước tính và ưu tiên. Luận chứng kinh doanh so sánh đường cơ sở không-làm-gì, nêu giả định, và kiểm toán được.

**Mức 4 (Quản lý).** Dự báo được đo so với thực tế và kiểm soát bằng dữ liệu. Độ chính xác ước lượng, ROI thực hiện, chi phí vận hành so với dự phóng, và kết quả chi phí trì hoãn được theo dõi theo đường cơ sở, và phương sai đáng kể kích hoạt rà soát. Luận chứng kinh doanh mang thước đo thành công xác định và tiêu chí khai tử được thực thi dựa trên bằng chứng thay vì cảm xúc, và giả định tỷ lệ chiết khấu và độ nhạy được xác thực theo kết quả lịch sử, để các con số được kiểm soát thay vì chỉ được tạo ra.

**Mức 5 (Điều phối).** Lập luận kinh tế là liên tục, được hiệu chỉnh và tích hợp với hoạch định danh mục, mua sắm và rủi ro. Luận chứng kinh doanh là tài liệu sống được xem xét lại khi bằng chứng đến, và độ chính xác ước lượng cải thiện theo thời gian vì kết quả được phản hồi. Chi phí trì hoãn thúc đẩy sắp thứ tự, cái vô hình được định giá tường minh, và tài trợ theo giai đoạn bảo toàn tính linh hoạt lựa chọn, để tổ chức cân bằng lại vốn một cách thích ứng về phía công việc tạo ra nhiều giá trị nhất khi điều kiện dịch chuyển.

## Ý tưởng để thảo luận

- Bao nhiêu độ nghiêm ngặt tài chính đáng áp dụng cho một quyết định đảo ngược được, chi phí thấp trước khi phân tích tốn hơn chính quyết định?
- Tổ chức của bạn nên dùng tỷ lệ chiết khấu nào, và khuyến nghị đổi bao nhiêu khi bạn thay đổi nó?
- Khi nào tiền tệ hóa một thứ vô hình là hiểu biết thật, và khi nào đó là bịa một con số tiện lợi?
- Làm sao bạn định giá lãi của nợ kỹ thuật đủ thuyết phục để lãnh đạo tài trợ việc trả nó?
- Trong bối cảnh khu vực công, bạn cân nhắc thế nào công bằng và kết quả sứ mệnh không chịu tiền tệ hóa so với các phương án có lợi tức tài chính gọn hơn?
- Luận chứng kinh doanh có nên được xem xét lại so với thực tế không, và ai chịu trách nhiệm khi giá trị thực hiện lệch khỏi dự báo?

## Những điểm cần ghi nhớ

- Kinh tế học kỹ thuật phần mềm làm các đánh đổi giá trị-và-chi phí tường minh, so sánh được và bảo vệ được: nó là xương sống phân tích của lập luận ROI và TCO được dùng xuyên suốt cẩm nang này.
- Quyết định theo tổng chi phí sở hữu qua toàn bộ vòng đời, không phải giá mua, và chiết khấu dòng tiền tương lai để giá trị thời gian của tiền được tôn trọng.
- Coi ước tính là khoảng dưới bất định, tam giác hóa chi phí bằng nhiều phương pháp, và đừng bao giờ để ước tính công sức cứng thành lời hứa ngày cố định.
- Định giá các chi phí thường vô hình, nợ kỹ thuật như lãi và chi phí trì hoãn như giá trị bị bỏ lỡ, vì chúng thường là những con số lớn nhất trong mô hình.
- Định giá cái vô hình tường minh thay vì coi chúng bằng không, và chọn hàm mục tiêu vì lợi nhuận hay công một cách trung thực.
- Xây luận chứng kinh doanh sống nêu giả định và các phương án gồm không-làm-gì, điều chỉnh độ nghiêm ngặt cho vừa mức rủi ro, và xem xét lại dự báo so với thực tế để tổ chức học ước lượng tốt hơn.

## Tài liệu tham khảo và đọc thêm

- Barry W. Boehm, *Software Engineering Economics*
- Barry W. Boehm et al., *Software Cost Estimation with COCOMO II*
- IEEE Computer Society, *SWEBOK Guide* (lĩnh vực tri thức Kinh tế Kỹ thuật Phần mềm)
- Donald G. Reinertsen, *The Principles of Product Development Flow* (chi phí trì hoãn, WSJF)
- Steve McConnell, *Software Estimation: Demystifying the Black Art*
- Douglas W. Hubbard, *How to Measure Anything: Finding the Value of Intangibles in Business*
- Ward Cunningham, "The WyCash Portfolio Management System" (ẩn dụ nợ kỹ thuật)
- Philippe Kruchten, Robert Nord và Ipek Ozkaya, *Managing Technical Debt*
- Mark Schwartz, *The Art of Business Value* và *A Seat at the Table*
- U.S. Office of Management and Budget, Circular A-94 (hướng dẫn và tỷ lệ chiết khấu cho phân tích lợi ích-chi phí)
- HM Treasury, *The Green Book: Central Government Guidance on Appraisal and Evaluation*
