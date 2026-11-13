# 10.15 Ước lượng và dự báo

## Tổng quan và động lực

Mọi đội phần mềm đều bị hỏi cùng một câu: khi nào xong? Đằng sau câu hỏi đó là [ước lượng công sức phát triển phần mềm](https://en.wikipedia.org/wiki/Software_development_effort_estimation), thực hành dự đoán một việc sẽ tốn bao nhiêu công trước khi bạn làm nó. Đó là một trong những việc khó nhất chúng ta làm, và một trong những việc dễ làm tệ nhất. Rắc rối là phần mềm là công việc khám phá. Bạn đang xây thứ chưa từng tồn tại, và phần lớn những gì bạn sẽ học về vấn đề chỉ trở nên hiển thị khi bạn xây. Dự đoán công sức của việc học thực sự khác với dự đoán công sức của việc lặp lại một tác vụ đã biết.

Vì sao coi đây là kỷ luật riêng thay vì một góc của quản lý dự án (chương 10.6)? Vì các thất bại quá nhất quán và quá đắt. Các đội thường xuyên cam kết những ngày đơn mà họ không có bằng chứng, rồi bảo vệ những ngày đó rất lâu sau khi thực tế đã mâu thuẫn chúng. Lãnh đạo nhầm ước tính với lời hứa. Hợp đồng đóng băng một con số tạo ra trong một buổi chiều và buộc người ta theo nó cả năm. Kết quả là giao trễ, lòng tin xói mòn, và một văn hóa nơi không ai nói điều họ thực sự tin. Làm đúng điều này ít liên quan đến toán tốt hơn mà nhiều đến sự trung thực: tách cái bạn biết khỏi cái bạn hy vọng, và truyền đạt độ bất định như độ bất định.

Rủi ro tăng mạnh trong bối cảnh doanh nghiệp và chính phủ. Doanh nghiệp tài trợ danh mục các sáng kiến đan xen so với ngân sách hằng năm và kỳ vọng con số chắc để phân bổ vốn (chương 10.1). Chính phủ đưa ra cam kết công khai dưới quy tắc phân bổ ngân sách, ký hợp đồng giá cố định, và chịu trách nhiệm trước nhà lập pháp khi một ngày trượt. Ở cả hai thế giới, áp lực đưa ra một con số đơn tự tin là rất lớn, và độ bất định sâu khiến con số đó không đáng tin không biến mất chỉ vì ai đó quan trọng muốn sự chắc chắn. Chương này lập luận cho một tư thế khác: ước lượng khi nó giúp bạn quyết định, dự báo bằng bằng chứng thay vì lạc quan, và nói sự thật về khoảng.

## Các nguyên tắc chính

- **Ước tính là dự đoán, không phải lời hứa.** Giữ nó tách biệt khỏi mục tiêu và cam kết.
- **Bất định là thật, nên hãy diễn đạt nó.** Một khoảng với xác suất thắng một ngày đơn giả.
- **Quá khứ dự đoán tương lai tốt hơn sự lạc quan.** Ưu tiên lịch sử đã đo hơn phỏng đoán mới.
- **Phân rã để hiểu, dự báo để cam kết.** Lát cắt nhỏ giảm cả rủi ro lẫn nhu cầu ước lượng.
- **Nhìn từ bên ngoài.** So với những nỗ lực tương tự trong quá khứ trước khi tin câu chuyện bên trong của bạn.
- **Dự báo lại liên tục.** Một dự đoán đưa ra một lần và không bao giờ cập nhật chỉ là đồ trang trí.
- **Chỉ ước lượng khi câu trả lời sẽ đổi một quyết định.** Nếu không, đó là lãng phí.

## Khuyến nghị

### Tách ước tính, mục tiêu và cam kết

Nước đi hữu ích nhất trong cả chương này không tốn gì: giữ ba ý tưởng tách biệt. Một **ước tính** là dự đoán trung thực của bạn về việc gì đó mất bao lâu, kèm độ bất định của nó. Một **mục tiêu** là mục tiêu kinh doanh bạn muốn đạt, như lần ra mắt ở hội chợ hay hạn chót quy định. Một **cam kết** là lời hứa bạn đưa ra với người khác mà bạn định giữ. Đây là ba thứ khác nhau, và gộp chúng là cách các dự án bắt đầu nói dối chính mình. Khi một lãnh đạo nghe "khoảng ba đến năm tháng" và ghi xuống "ba tháng," và đội bán hàng hứa với khách "mười hai tuần," một ước tính đã lặng lẽ trở thành cam kết mà không ai quyết định chấp nhận rủi ro.

Hãy nói rõ bạn đang đưa cái nào, mỗi lần. Nếu được hỏi một ngày, hãy trả lời bằng ước tính diễn đạt dưới dạng khoảng, rồi để doanh nghiệp đặt mục tiêu so với nó và quyết định, có chủ đích, cam kết gì. Một cam kết nên là lựa chọn được đưa ra với mắt mở, cân nhắc độ bất định của ước tính so với chi phí của việc trượt. Kỷ luật này nối trực tiếp với cách tổ chức bạn đưa ra và ghi lại quyết định (chương 1.5): một cam kết là một quyết định, và nó xứng đáng sự nghiêm ngặt của một quyết định thay vì một cái gật đầu ngoài hành lang.

### Hiểu vì sao ước tính sai, và theo hướng nào

Ước tính phần mềm không sai ngẫu nhiên. Chúng sai theo những cách có thể dự đoán, có hệ thống, và biết mẫu hình cho phép bạn hiệu chỉnh. Đầu bất kỳ nỗ lực nào bạn ngồi bên trong [hình nón bất định](https://en.wikipedia.org/wiki/Cone_of_Uncertainty): lúc ban đầu ước tính của bạn có thể dễ dàng lệch gấp bốn lần theo cả hai hướng, và khoảng chỉ thu hẹp khi bạn xây và học. Cam kết một con số chính xác ở miệng rộng của hình nón là cam kết một con số bạn chưa thể chống đỡ.

Trên sự bất định cấu trúc đó là một thiên kiến của con người. [Ngụy biện hoạch định](https://en.wikipedia.org/wiki/Planning_fallacy) là xu hướng đáng tin cậy của chúng ta đánh giá thấp thời gian, chi phí và rủi ro của kế hoạch của chính mình trong khi tưởng tượng trường hợp tốt nhất. Chúng ta hình dung con đường suôn sẻ, quên các ngắt quãng, bất ngờ tích hợp và ngày ốm, và tạo ra con số giả định không có gì sai. Đệm là phản ứng phòng thủ thông thường, nhưng đệm thêm theo cảm giác chỉ là phỏng đoán thứ hai chồng lên phỏng đoán thứ nhất, và nó bị thương lượng bỏ ngay khi lịch trình thắt lại. Thuốc chữa không phải ý chí mạnh hơn; mà là phương pháp. Hãy dựa dự đoán vào cái công việc tương tự thực sự mất, không phải cảm giác của công việc này từ bên trong.

### Dùng phân rã và phán đoán chuyên gia, và biết giới hạn của chúng

Các kỹ thuật trụ cột đáng biết và đáng giới hạn. **Phân rã** chia một sản phẩm bàn giao lớn thành các mảnh nhỏ hơn bạn lập luận được, rồi cộng các mảnh lên. Nó giúp vì người ta ước lượng những thứ nhỏ, quen thuộc tốt hơn nhiều so với thứ lớn, mơ hồ, và vì cộng nhiều mục độc lập cho phép một số ước tính cao bù một số ước tính thấp. Giới hạn của nó là phân rã bỏ sót công việc giữa các hộp: tích hợp, phối hợp, và các tác vụ bạn không nghĩ đến để liệt kê. **Phán đoán chuyên gia** và ước lượng **tương tự** ("cái này giống mô-đun báo cáo chúng ta xây năm ngoái, mất hai tháng") nhanh và thường tốt đáng ngạc nhiên, nhưng chúng thừa hưởng sự lạc quan và điểm mù của người ước lượng.

Với bất cứ thứ gì bạn phải đặt một con số, hãy ưu tiên [ước lượng ba điểm](https://en.wikipedia.org/wiki/Three-point_estimation), yêu cầu một con số lạc quan, khả dĩ nhất và bi quan rồi kết hợp chúng, thường là trung bình có trọng số PERT (lạc quan cộng bốn lần khả dĩ nhất cộng bi quan, chia sáu). Giá trị không phải công thức chính xác. Mà là ước lượng ba điểm buộc bạn nói to độ bất định của mình và tạo ra một khoảng thay vì một điểm giả. Các phương pháp định cỡ tương đối như **điểm story** và **cỡ áo thun** (nhỏ, vừa, lớn, rất lớn) né cái bẫy dự đoán giờ chính xác bằng cách so các mục với nhau. Chúng hiệu quả cho sắp thứ tự và năng lực thô, nhưng hãy coi chúng là đầu vào của dự báo, không phải tiền tệ. Điểm không phải giờ, và nhân vận tốc với điểm để ra một ngày đưa lại mọi vấn đề mà định cỡ tương đối được tạo ra để tránh.

### Dự báo xác suất từ dữ liệu luồng của chính bạn

Đây là bước chuyển thay đổi mọi thứ: thôi yêu cầu mọi người đoán công việc sẽ mất bao lâu, và bắt đầu đo đội của bạn thực sự hoàn thành công việc nhanh đến đâu. Đường ống phân phối của bạn (chương 11.2) đã tạo ra dữ liệu bạn cần. Nếu bạn theo dõi [thông lượng](https://en.wikipedia.org/wiki/Throughput), số mục đội hoàn thành mỗi tuần, bạn có thể dự báo tương lai từ quá khứ thay vì từ hy vọng. Một đội đã đóng sáu đến mười một mục mỗi tuần trong ba tháng qua sẽ, với xác suất cao, mất khoảng bốn đến bảy tuần để hoàn thành bốn mươi mục còn lại. Dự báo đó dựa trên bằng chứng, và nó tự cập nhật mỗi tuần khi dữ liệu mới đến.

Phiên bản nghiêm ngặt chạy mô phỏng [phương pháp Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method): lấy mẫu từ thông lượng hằng tuần lịch sử của bạn hàng nghìn lần để xây phân phối các ngày kết thúc có thể, rồi đọc câu trả lời dưới dạng xác suất. "Chúng tôi có 85% khả năng xong trước 14 tháng Ba, và 50% trước 28 tháng Hai" hữu ích hơn nhiều và trung thực hơn nhiều so với "nó sẽ xong ngày 1 tháng Ba." Cách tiếp cận này nối trực tiếp với lý thuyết hàng đợi (chương 11.3): thời gian chờ bằng công việc đang làm chia cho thông lượng, nên cùng các chỉ số luồng chi phối cách công việc di chuyển cũng chi phối khi nào nó đến. Dự báo xác suất cần lịch sử và quy trình khá ổn định, chính xác là lý do nó thưởng cho các đội giữ công việc nhỏ và luồng ổn định. Nó cũng lặng lẽ loại bỏ phần lớn nghi thức ước lượng, vì bạn không còn cần định cỡ từng mục để biết khi nào lô sẽ đến.

### Nhìn từ bên ngoài cho các chương trình lớn

Với các chương trình lớn, dài, đắt, ước tính riêng lẻ và thậm chí dự báo luồng có thể gây hiểu lầm, vì một chương trình mới chưa có lịch sử thông lượng và câu chuyện bên trong của nó chính xác là nơi ngụy biện hoạch định cắn mạnh nhất. Thuốc giải là [dự báo theo lớp tham chiếu](https://en.wikipedia.org/wiki/Reference_class_forecasting): tìm một lớp tham chiếu gồm các nỗ lực tương tự đã hoàn thành, xem chúng thực sự mất bao lâu và bao nhiêu, và đặt chương trình của bạn vào phân phối đó trước khi tin kế hoạch từ dưới lên của chính mình. Nếu các cuộc thay thế nền tảng tương đương ở công ty bạn đã vượt ước tính ban đầu trung bình 60%, con số đó là bằng chứng tốt hơn về chương trình của bạn so với kế hoạch gọn gàng đội bạn vừa lắp. Cái nhìn từ bên ngoài làm xì hơi, và đó chính xác là giá trị của nó: nó chống lại sự lạc quan mà mọi kế hoạch mới mang theo. Hãy dùng nó cho tài trợ danh mục và lập ngân sách siêu chương trình (chương 10.1), nơi chi phí của một cú vượt có hệ thống được đo bằng hàng triệu và bằng uy tín.

### Ước lượng ít hơn bằng cách cắt nhỏ hơn, và sắp thứ tự theo chi phí trì hoãn

Đôi khi lượng ước lượng đúng gần như bằng không. Lập luận **#NoEstimates**, ở lõi hợp lý của nó, quan sát rằng nếu bạn cắt công việc thành các mảnh đủ nhỏ để mỗi mảnh mất một hai ngày, ước tính của bất kỳ mảnh đơn lẻ nào thôi quan trọng. Bạn đơn giản đếm thông lượng và dự báo từ số đếm. Khi các lát cắt đồng đều và nhỏ, định cỡ cầu kỳ là lãng phí: nó tiêu công sức tạo độ chính xác mà dự báo không cần. Đây không phải lập luận chống nghĩ trước. Đó là lập luận cho việc làm các dự đoán riêng lẻ rẻ bằng cách làm các mảnh riêng lẻ nhỏ.

Cái vẫn cần quyết định là thứ tự. Khi bạn không thể làm mọi thứ cùng lúc, hãy sắp thứ tự theo **chi phí trì hoãn**: giá trị bạn mất cho mỗi đơn vị thời gian một phần công việc nhất định bị trễ. Một tính năng mở khóa hợp đồng lớn quý sau có chi phí trì hoãn cao và nên nhảy lên trước một thứ-nên-có không có chi phí đó, dù thứ-nên-có dễ hơn. Cân nhắc chi phí trì hoãn so với công sức (heuristic "công việc ngắn nhất có trọng số trước" từ tư duy tinh gọn) cho bạn biết làm gì tiếp theo đáng tin cậy hơn nhiều so với tồn đọng sắp theo cảm giác. Lưu ý điều này đóng khung lại cả cuộc trò chuyện: thay vì "khi nào mọi thứ xong," mời gọi độ chính xác giả, bạn hỏi "thứ có giá trị nhất để hoàn thành tiếp theo là gì," điều bạn thực sự trả lời được.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Ước tính ngày đơn** | Đơn giản; điều các bên liên quan hỏi | Sai một cách chính xác; giấu rủi ro; trở thành cam kết tình cờ |
| **Ước tính ba điểm / PERT** | Buộc bất định ra ánh sáng; rẻ | Vẫn là phỏng đoán; công thức ngụ ý độ nghiêm ngặt giả |
| **Điểm story / cỡ áo thun** | Nhanh; tốt cho sắp thứ tự và năng lực thô | Không phải giờ; toán vận tốc lén đưa ngày đơn trở lại |
| **Dự báo luồng xác suất** | Dựa trên bằng chứng; tự cập nhật; khoảng trung thực | Cần lịch sử và luồng ổn định; trông kém "chắc chắn" |
| **Dự báo theo lớp tham chiếu** | Hiệu chỉnh sự lạc quan trên chương trình lớn | Cần các nỗ lực quá khứ so sánh được; nghe thì xì hơi |
| **#NoEstimates (lát cắt nhỏ)** | Loại lãng phí; dự báo bằng đếm | Cần cắt lát có kỷ luật; làm nhà tài trợ muốn một con số thấy bất an |

Căng thẳng trung tâm là **sự chắc chắn người ta muốn so với sự trung thực công việc đòi hỏi**. Nhà tài trợ, lãnh đạo, hợp đồng và nhà lập pháp xin một ngày đơn chắc vì một ngày đơn dễ lập ngân sách, hứa và bảo vệ. Phần mềm hiếm khi hỗ trợ một ngày như vậy. Hãy giải quyết căng thẳng không bằng bịa sự chắc chắn và cũng không bằng từ chối trả lời, mà bằng trả lời bằng tiền tệ của xác suất: một khoảng với mức tin cậy, dự báo lại khi bằng chứng đến. Ghép nó với lát cắt nhỏ để các lần giao hàng sớm, thật thay thế những lần xa, tưởng tượng làm thứ người ta tin. Một phần tăng trưởng được trình diễn đáng giá hơn bất kỳ ước tính nào.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi ai đó hỏi bạn một ngày, bạn đang đưa ước tính, mục tiêu hay cam kết, và mọi người trong phòng có biết là cái nào không?** Đây là câu hỏi ngăn nhiều thiệt hại nhất với ít công sức nhất. Ở hầu hết tổ chức ba thứ này sụp thành một con số ngay khoảnh khắc nó rời miệng đội, và không ai quyết định chấp nhận rủi ro rằng một dự đoán đã thành lời hứa. Hãy mang một ví dụ thật: lấy hạn chót đã cam kết gần nhất của bạn và truy ngược về cuộc trò chuyện nơi nó được thốt ra lần đầu, và hỏi liệu nó có bao giờ là gì khác ngoài một phỏng đoán đầy hy vọng khoác bộ vest. Câu trả lời nên đổi ngôn ngữ của bạn vĩnh viễn, để ước tính đi ra dưới dạng khoảng, mục tiêu được gọi tên là mong muốn kinh doanh, và cam kết được đưa ra có chủ đích với độ bất định được cân nhắc và ghi lại như một quyết định (chương 1.5). Nếu đội bạn không chỉ ra được nơi một cam kết được chấp nhận có ý thức, bạn đang hứa hẹn một cách tình cờ.

2. **Bạn có thể dự báo bản phát hành tiếp theo từ thông lượng đo được thay vì từ ước tính mới không, và cái gì đang cản bạn?** Hầu hết các đội đã có dữ liệu để trả lời "khi nào xong" theo kinh nghiệm, nằm không dùng trong công cụ theo dõi công việc của họ. Nếu bạn biết đội đã hoàn thành bao nhiêu mục mỗi tuần trong quý vừa rồi, bạn có thể mô phỏng phân phối ngày kết thúc và báo một xác suất thay vì một mong ước. Hãy mang lịch sử thông lượng thực và số mục còn lại, và so dự báo dựa trên luồng với bất cứ ngày nào đội ước tính theo cảm giác; khoảng cách thường mang tính chỉ dạy. Nếu rào cản là các mục của bạn có kích thước rất khác nhau hoặc luồng của bạn thất thường, đó tự nó là phát hiện, vì luồng không ổn định là vấn đề phân phối đáng sửa dù sao (chương 11.2, 11.3). Chuyển từ ước lượng sang đo lường thường là quyết định tin lịch sử của chính bạn hơn sự lạc quan hơn là thay đổi công cụ.

3. **Với chương trình lớn nhất hiện tại của bạn, bạn đã nhìn từ bên ngoài, hay chỉ xây kế hoạch bên trong?** Chương trình lớn là nơi sự lạc quan cộng dồn thành cú vượt đắt đỏ, và là nơi một kế hoạch từ dưới lên tự tin quyến rũ nhất và kém đáng tin nhất. Kỷ luật là nêu một lớp tham chiếu gồm các nỗ lực tương tự đã hoàn thành trong hoặc ngoài tổ chức, tìm xem chúng thực sự tốn bao nhiêu và mất bao lâu, và định vị chương trình của bạn một cách trung thực trong phân phối đó trước khi bảo vệ con số của chính bạn. Hãy mang dữ liệu: các sáng kiến tương đương ở đây đã vượt ước tính đầu tiên thế nào, và kế hoạch hiện tại của bạn có lặng lẽ giả định bạn sẽ vượt mọi cái trong số đó không? Nếu có, bạn đang cược vào việc mình là ngoại lệ, canh bạc mà tỷ lệ cơ sở thua đáng tin cậy. Cái nhìn từ bên ngoài sẽ làm dự báo của bạn kém tâng bốc và bảo vệ được hơn nhiều trước các nhà tài trợ và kiểm toán viên sẽ nhớ con số bạn đã đưa (chương 10.1).

4. **Khi nhà tài trợ, hợp đồng hay nhà lập pháp đòi một ngày cố định, bạn trả lời thế nào mà không nói dối cũng không từ chối?** Đây là nơi áp lực dữ dội nhất và là nơi các đội trung thực thường nhượng bộ nhất, vì "70% khả năng trước tháng Chín" nghe lẩn tránh cạnh lời "tháng Chín" tự tin của đối thủ. Với tổ chức lớn rủi ro nhân lên: một ngày cố định lan vào ngân sách, các chương trình phụ thuộc và lời hứa công khai, nên một con số chọn cho thoải mái thành khoản nợ hệ thống ngay khi nó trượt. Hãy mang ngôn ngữ bạn thực sự định dùng, một ví dụ làm việc về khoảng kèm mức tin cậy, và một phần tăng trưởng sớm nhỏ bạn có thể cam kết chắc trong khi để phạm vi sau như một khoảng được tài trợ. Cân nhắc đối lập là thật, vì một số hạn chót (chuyển đổi quy định, lần ra mắt hội chợ) thực sự cố định, và nước đi đúng ở đó là cố định ngày và co giãn phạm vi thay vì giả vờ công sức chắc chắn. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn điều này với cách hợp đồng được định hình: một thỏa thuận mô-đun, tài trợ theo phần tăng trưởng cho phép bạn cam kết trung thực với một lõi có giá trị, trong khi một hợp đồng giá cố định, phạm vi cố định neo vào cột mốc xa buộc chính sự chắc chắn giả tạo ra cú vượt và tiêu đề báo.

5. **Đội bạn quyết định xây gì tiếp theo thế nào, và việc sắp thứ tự tường minh theo chi phí trì hoãn có đổi thứ tự không?** Hầu hết tồn đọng được sắp theo hỗn hợp cảm giác, ai hét to nhất và công sức thô, lặng lẽ tối ưu cho chiến thắng dễ thay vì có giá trị. Chi phí trì hoãn, giá trị bạn mất cho mỗi đơn vị thời gian một phần công việc bị trễ, đóng khung lại câu hỏi từ "khi nào mọi thứ xong" sang "thứ có giá trị nhất để hoàn thành tiếp theo là gì," điều bạn thực sự trả lời được bằng bằng chứng. Hãy mang ba bốn mục tồn đọng thật với ước tính trung thực về giá trị mỗi cái mở khóa và khi nào giá trị đó hết hạn, rồi xếp hạng chúng theo giá-trị-mất-mỗi-tuần so với công sức và so thứ tự đó với kế hoạch hiện tại; sự sắp xếp lại thường gây ngạc nhiên và khó bác bỏ. Cân nhắc đối lập là chi phí trì hoãn tự nó là một ước tính và có thể bị ai muốn mục của họ lên đầu thao túng, nên hãy nêu ai sở hữu các con số và chúng bị thách thức thế nào. Với danh mục doanh nghiệp hay chương trình chính phủ, kỷ luật này là thứ cho phép bạn bảo vệ quyết định sắp thứ tự trước các bên liên quan mỗi người tin sáng kiến của họ nên đi đầu, vì thứ tự dựa trên giá trị đã nêu thay vì chính trị.

6. **Ai dự báo lại, bao lâu một lần, và ai chịu trách nhiệm hành động khi dự báo dịch chuyển?** Một dự đoán đưa ra một lần lúc khởi động và không bao giờ xem lại là đồ trang trí, và những độ trượt đắt nhất là những cái một dự báo sống lẽ ra đã cho thấy nhiều tháng trước khi hạn chót làm chúng không thể phủ nhận. Với đội lớn, thất bại hiếm khi là thiếu dữ liệu và thường là thiếu nhịp thường trực và chủ sở hữu có tên: thông lượng trôi, phân phối ngày kết thúc dịch sang phải, và không ai có việc để ý đang nhìn. Hãy mang nhịp dự báo lại thực của bạn (hoặc thừa nhận không có), lần cuối một dự báo đổi một quyết định, và độ trôi bạn đã thấy kể từ khi cam kết hiện tại được đặt. Cân nhắc đối lập là mệt mỏi dự báo, vì dự báo lại quá ồn mời gọi vật vã và xói mòn lòng tin, nên hãy thống nhất một khoảng thời gian hợp lý và ngưỡng kích hoạt leo thang thay vì phản ứng với mọi dao động. Trong bối cảnh doanh nghiệp và chính phủ, hãy nối điều này với giám sát: báo cáo cho các cơ quan quản trị khoảng xác suất cập nhật theo lịch cố định, để một độ trượt nổi lên như một dự báo lại được quản lý mà lãnh đạo hành động theo được thay vì bất ngờ lộ ra ở cột mốc.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy bỏ qua nghi thức ước lượng gần như hoàn toàn. Cắt công việc thành mảnh một đến hai ngày, đếm cái bạn hoàn thành mỗi tuần, và báo với những người sáng lập và nhà đầu tư một khoảng thu hẹp dần thay vì một ngày đơn anh hùng. Lịch sử của bạn ngắn và quy trình của bạn biến động, nên hãy dựa vào hình nón bất định như lời giải thích trung thực thay vì cái cớ, và dự báo lại mỗi thứ Sáu khi bức tranh sắc nét hơn.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia ước lượng và không có hứng thú với các buổi định cỡ, nên hãy để công cụ bạn đã chạy làm việc: hầu hết trình theo dõi tác vụ cho thông lượng miễn phí, và một dự báo nhẹ từ đó thắng một hạn chót đoán mò. Chống lại thôi thúc mua phần mềm hoạch định nặng mà bạn không bố trí nhân sự nổi; đếm hằng tuần các mục hoàn thành và một khoảng đơn giản trả lời "khi nào xong" đủ tốt cho những cam kết bạn thực sự đưa ra cho khách hàng.

**Doanh nghiệp lớn.** Vấn đề là nhất quán qua nhiều đội tài trợ danh mục theo chu kỳ vốn hằng năm (chương 10.1). Hãy chuẩn hóa theo khoảng với mức tin cậy thay vì ngày đơn, yêu cầu so sánh lớp tham chiếu cho chương trình lớn, và dựng chỉ số luồng để phỏng đoán nhường chỗ cho dự báo dựa trên thông lượng trong vòng một quý. Quản trị ước lượng như thực hành chung với định nghĩa rõ ràng về ước tính, mục tiêu và cam kết, để một con số tạo ra ở một bộ phận có cùng nghĩa khi nó đến hội đồng quản trị.

**Chính phủ.** Quy tắc mua sắm và trách nhiệm giải trình công định hình mọi thứ. Một ngày công khai bị trượt trở thành tiêu đề và phát hiện kiểm toán, nên hãy ưu tiên hợp đồng mô-đun, tài trợ theo phần tăng trưởng hơn một cam kết giá cố định, phạm vi cố định neo vào cột mốc xa. Báo cáo cho cơ quan giám sát bằng dự báo xác suất và bằng chứng lớp tham chiếu bằng ngôn ngữ đơn giản, công bố mức tin cậy một cách trung thực, và để các phần tăng trưởng hoạt động được trình diễn thành bằng chứng mà công chúng và kiểm toán viên tin thay vì chữ ký của nhà thầu trên một kế hoạch lạc quan.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp chín người chuẩn bị cho bản trình diễn Series A cần biết một tích hợp then chốt có sẵn sàng không. Thay vì để những người sáng lập hứa với nhà đầu tư một ngày, trưởng nhóm báo một ước tính dưới dạng khoảng và giải thích hình nón bất định đằng sau nó. Đội đã đóng năm đến chín mục tồn đọng mỗi tuần, nên họ chạy nhanh một dự báo Monte Carlo trên công việc còn lại và báo "80% khả năng trước tuần thứ ba của quý, ngang cơ hội sớm hơn một tuần." Họ cắt tích hợp thành các mảnh hai ngày để không ước tính đơn lẻ nào quan trọng nhiều, sắp thứ tự theo chi phí trì hoãn để xây con đường nhà đầu tư thấy được trước, và dự báo lại mỗi thứ Sáu. Nhà đầu tư nhận một dự phóng trung thực, thu hẹp dần thay vì một con số tự tin sẽ trượt.

**Doanh nghiệp lớn.** Một nhà bán lẻ thay nền tảng quản lý đơn hàng phải tài trợ chương trình qua chu kỳ vốn hằng năm đòi một con số. Văn phòng chương trình cưỡng lại thôi thúc bảo vệ kế hoạch từ dưới lên gọn gàng và thay vào đó xây một lớp tham chiếu từ ba cuộc thay thế nền tảng tương đương, hai nội bộ và một được ghi chép công khai, đã vượt ước tính ban đầu 50% đến 80%. Họ tài trợ theo con số nhìn từ bên ngoài, diễn đạt lịch trình dưới dạng khoảng xác suất thay vì ngày vận hành cố định, và dựng chỉ số luồng từ đội giao hàng đầu tiên để trong vòng một quý phỏng đoán được thay bằng dự báo dựa trên thông lượng cập nhật hằng tháng. Khi một dòng chạy nóng, dự báo lại cho thấy sớm, và lãnh đạo cân bằng lại thay vì phát hiện độ trượt ở hạn chót.

**Chính phủ.** Một cơ quan hiện đại hóa hệ thống trợ cấp hoạt động dưới phân bổ ngân sách và sự soi xét công khai, nơi một ngày công khai bị trượt là tiêu đề. Thay vì một hợp đồng giá cố định, phạm vi cố định neo vào một cột mốc xa, nó mua sắm các phần tăng trưởng mô-đun và cam kết công khai một lõi có giá trị được giao sớm, với phạm vi sau được diễn đạt như một khoảng được tài trợ thay vì lời hứa. Lãnh đạo chương trình báo cáo cho cơ quan giám sát bằng dự báo xác suất và so sánh lớp tham chiếu, giải thích mức tin cậy bằng ngôn ngữ đơn giản, để "70% trước tháng Chín" được hiểu đúng là như vậy. Các phần tăng trưởng hoạt động được trình diễn trở thành bằng chứng công chúng tin, vững chắc hơn bất kỳ ước tính nào nhà thầu có thể ký.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của ước lượng và dự báo trung thực bị chi phối bởi thảm họa tránh được. Các nỗ lực phần mềm lớn vượt hoặc thất bại thường xuyên hơn nhiều so với đạt kế hoạch cố định ban đầu, và tổn thất cộng dồn: chi phí chìm, giá trị bị bỏ lỡ từ giao trễ, chi tiêu khẩn cấp để phục hồi, và sự xói mòn lòng tin theo sau một cam kết công khai bị phá. Các thực hành ở đây (tách ước tính khỏi cam kết, dự báo từ thông lượng thật, nhìn từ bên ngoài trên chương trình lớn) là những thực hành đưa một chương trình ra khỏi đường cong thất bại đó. Bạn không mua một quả cầu pha lê chính xác hơn. Bạn mua thông tin sớm hơn, đúng hơn về vị trí của mình, cho phép bạn sửa khi việc sửa còn rẻ.

Về tổng chi phí sở hữu, việc chuyển từ nghi thức ước lượng sang dự báo đo được thường hạ chi phí thay vì tăng. Ước lượng cầu kỳ từ đầu tốn kém để tạo và phai ngay khi công việc bắt đầu, trong khi dự báo dựa trên thông lượng gần như miễn phí một khi đường ống phân phối của bạn phát ra dữ liệu. Cả hai thái cực đều tốn tiền: ước lượng thừa (các buổi định cỡ bất tận tạo độ chính xác không ai dùng) và dự báo thiếu (cam kết mù và trả giá cho cú vượt sau đó). Để lập luận với ban lãnh đạo, hãy đặt chi phí toàn phần của cú vượt lớn gần nhất bên cạnh chi phí gần bằng không của việc theo dõi thông lượng và báo khoảng, và cho thấy một dự báo nhìn từ bên ngoài lẽ ra đã đặt kỳ vọng tài trợ được ngay từ đầu.

## Phản mẫu và cạm bẫy

- **Cam kết ngày đơn:** một khoảng bị thu thành một con số, rồi được bảo vệ quá bằng chứng.
- **Rửa ước tính:** một phỏng đoán đầy hy vọng được chuyển lên chuỗi cho đến khi nó cứng thành lời hứa hợp đồng.
- **Vận tốc như động cơ lịch trình:** nhân điểm story với vận tốc để chế ra một ngày chính xác.
- **Đệm theo cảm giác:** phỏng đoán thứ hai chồng lên cái thứ nhất, bị thương lượng bỏ dưới áp lực.
- **Chỉ nhìn bên trong:** tin một kế hoạch từ dưới lên mới trong khi phớt lờ những gì các chương trình tương tự thực sự mất.
- **Ước lượng mọi thứ:** định cỡ các lát cắt nhỏ, đồng đều mà ước tính riêng lẻ không đổi quyết định nào.
- **Dự báo đóng băng:** một dự đoán đưa ra một lần lúc khởi động và không bao giờ cập nhật khi thực tế đến.
- **Sân khấu độ chính xác:** báo giờ đến hai chữ số thập phân ở miệng rộng của hình nón bất định.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Ước tính là ngày đơn tạo ra bằng cảm giác và bị coi là lời hứa; không phân biệt ước tính, mục tiêu và cam kết; dự báo phản ứng và tùy nghi; cú vượt làm mọi người ngạc nhiên và bị đổ cho đội.
- **Mức 2, Phát triển:** Một số ước lượng có cấu trúc tồn tại (phân rã, điểm story, con số ba điểm), nhưng thực hành khác nhau theo đội; ước tính vẫn chủ yếu là con số đơn; vận tốc được dùng để dự phóng ngày; dự báo được đưa ra một lần lúc khởi động và hiếm khi xem lại.
- **Mức 3, Chuẩn hóa:** Một tiêu chuẩn có tài liệu được thực thi toàn tổ chức: ước tính được diễn đạt dưới dạng khoảng với bất định đã nêu, ước tính, mục tiêu và cam kết được giữ tách biệt theo định nghĩa, các đội theo dõi thông lượng và dự báo lại theo nhịp đặt sẵn, và chương trình lớn được yêu cầu dùng so sánh lớp tham chiếu.
- **Mức 4, Quản lý:** Thực hành được đo và kiểm soát bằng dữ liệu. Độ chính xác dự báo được theo dõi so với kết quả thực và độ hiệu chỉnh được kiểm tra, để bạn nói được ngày "80% trước" của mình có thực sự đáp tám lần trong mười không; đường cơ sở thông lượng và thời gian chu kỳ được duy trì; chi phí trì hoãn được định lượng; độ trôi dự báo được giám sát theo ngưỡng và kích hoạt leo thang; cam kết được đưa ra dựa trên bằng chứng thay vì lạc quan.
- **Mức 5, Điều phối:** Dự báo xác suất từ dữ liệu luồng là liên tục và đáng tin vì lịch sử hiệu chỉnh đã chứng minh nó trung thực; cam kết là quyết định có chủ đích cân nhắc độ tin cậy so với chi phí; công việc được cắt đủ nhỏ để ước lượng tối thiểu và chi phí trì hoãn thúc đẩy thứ tự; ước lượng được tích hợp với tài trợ danh mục và hoạch định rủi ro, và tổ chức thường lệ thu hẹp phạm vi và cân bằng lại khi dự báo dịch chuyển, thích ứng kế hoạch theo bằng chứng thay vì bảo vệ con số ban đầu.

## Ý tưởng để thảo luận

1. Điều gì sẽ đổi trong tổ chức của bạn nếu mọi ước tính phải rời đội dưới dạng khoảng với mức tin cậy, và ngày đơn bị cấm?
2. Bạn đang tiêu công sức ước lượng công việc đã đủ nhỏ và đồng đều để dự báo bằng đếm ở đâu?
3. Nếu bạn đưa thông lượng hai quý gần nhất vào mô phỏng Monte Carlo, dự báo có đồng ý với các ngày bạn thực sự đã cam kết không?
4. Với chương trình lớn nhất của bạn, lớp tham chiếu trung thực là gì, và tỷ lệ cơ sở mâu thuẫn kế hoạch hiện tại của bạn tệ đến đâu?
5. Đội bạn quyết định thứ tự hôm nay thế nào, và sắp thứ tự tường minh theo chi phí trì hoãn có đổi cái bạn xây tiếp theo không?
6. Khi một cam kết được chấp nhận trong tổ chức của bạn, độ bất định có được ghi lại như một phần của quyết định, hay nó biến mất ngay khi ngày được viết xuống?

## Những điểm cần ghi nhớ

- Giữ **ước tính, mục tiêu và cam kết** tách biệt; gộp chúng là cách các dự án bắt đầu nói dối chính mình.
- Ước tính sai có hệ thống theo các hướng đã biết: **hình nón bất định** mở rộng công việc ban đầu, và **ngụy biện hoạch định** làm sự lạc quan thành mặc định.
- Ưu tiên **dự báo xác suất từ thông lượng đo được** hơn phỏng đoán mới; báo khoảng và mức tin cậy, và dự báo lại liên tục.
- **Nhìn từ bên ngoài** bằng dự báo theo lớp tham chiếu trên các chương trình lớn, nơi sự lạc quan đắt nhất (chương 10.1).
- **Cắt nhỏ** để ước tính riêng lẻ thôi quan trọng, và **sắp thứ tự theo chi phí trì hoãn** thay vì cảm giác.
- Chỉ ước lượng khi nó đổi một quyết định; nếu không, đó là lãng phí. Xem các chương 10.6 (quản lý dự án), 11.2 (phân phối), 11.3 (lý thuyết hàng đợi) và 1.5 (ra quyết định và quản trị).

## Tài liệu tham khảo và đọc thêm

- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* và *When Will It Be Done?* (dự báo xác suất từ dữ liệu luồng).
- Troy Magennis, *Forecasting and Simulating Software Development Projects* (phương pháp Monte Carlo).
- Bent Flyvbjerg và Dan Gardner, *How Big Things Get Done* (dự báo theo lớp tham chiếu và siêu dự án).
- Daniel Kahneman, *Thinking, Fast and Slow* (ngụy biện hoạch định và cái nhìn từ bên ngoài).
- Donald Reinertsen, *The Principles of Product Development Flow* (chi phí trì hoãn và kinh tế hàng đợi).
- Vasco Duarte, *NoEstimates: How to Measure Project Progress Without Estimating*.
- Frederick Brooks, *The Mythical Man-Month* (vì sao lịch trình phần mềm sai).
- Todd Little, "Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty" (*IEEE Software*, 2006).
