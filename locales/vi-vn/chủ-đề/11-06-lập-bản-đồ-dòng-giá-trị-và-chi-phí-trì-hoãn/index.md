# 11.6 Lập bản đồ dòng giá trị và chi phí trì hoãn

## Tổng quan và động lực

Hãy hỏi mười người trong một đội phân phối thời gian đi đâu giữa một ý tưởng và một kết quả trong sản xuất, và bạn sẽ nhận mười phỏng đoán khác nhau. Hầu hết sẽ sai, và hầu hết sẽ lạc quan. Lý do là mọi người thấy bước của chính mình rõ ràng và sự chờ đợi giữa các bước thì không hề thấy. Một nhà phát triển biết một tính năng mất hai ngày để viết mã. Không ai theo dõi mười một ngày sau đó nó nằm trong hàng đợi rà soát, một lần đặt môi trường kiểm thử, một hội đồng phê duyệt thay đổi, và một cửa sổ phát hành. Công việc được làm trong vài giờ và mất trong hàng đợi. Chương này trao cho bạn hai lăng kính để thấy toàn bộ bức tranh đó và hành động theo nó: [lập bản đồ dòng giá trị](https://en.wikipedia.org/wiki/Value-stream_mapping), làm dòng chảy từ ý tưởng đến giá trị hiển thị, và [chi phí trì hoãn](https://en.wikipedia.org/wiki/Cost_of_delay), đặt một cái giá kinh tế lên sự chờ đợi để bạn ưu tiên bằng tiền thay vì ý kiến.

Hai lăng kính này bổ sung cho phần còn lại của Phần 11. Chương 11.1 mô tả quy trình khám phá quyết định xây gì, và chương 11.2 mô tả quy trình phân phối phát hành nó. Lập bản đồ dòng giá trị trải qua cả hai, coi toàn bộ con đường từ ý nghĩ đầu tiên đến kết quả đã đo là một hệ thống để thấy và cải thiện. Chương 11.3 cho bạn toán học của hàng đợi; chương này cho bạn thực hành tìm xem các hàng đợi đó thực sự hình thành ở đâu trong tổ chức của bạn và chúng tốn gì. Trong khi 11.4 (OKR) và 11.5 (KPI) nói với bạn cái tốt trông thế nào, chi phí trì hoãn nói với bạn thứ tự để theo đuổi nó.

Với các đội lớn, lợi ích là khổng lồ. Phối hợp qua hàng chục đội nhân lên các bàn giao, và mỗi bàn giao là một nơi công việc chờ. Trong bối cảnh doanh nghiệp, một tính năng có thể đi qua một đội sản phẩm, một đội nền tảng, một rà soát bảo mật, và một chức năng quản lý phát hành trước khi đến khách hàng, và thời gian chờ giữa các nhóm đó thường lấn át công việc bên trong chúng. Trong chính phủ, các chương trình nhiều năm cam kết tiền công theo hạn chót do luật định, và một dòng giá trị chưa lập bản đồ giấu cả lãng phí lẫn rủi ro khỏi những người chịu trách nhiệm về khoản chi. Làm dòng chảy hiển thị và định giá trì hoãn một cách trung thực là cách các tổ chức lớn thôi tranh cãi từ giai thoại và bắt đầu quyết định từ bằng chứng.

## Các nguyên tắc chính

- Thấy toàn bộ dòng chảy từ ý tưởng đến giá trị, không chỉ bước bạn sở hữu.
- Tách thời gian xử lý (công việc thật) khỏi thời gian chờ (trì hoãn thuần túy); khoảng cách là cơ hội của bạn.
- Đo hiệu quả luồng, và kỳ vọng nó thấp đến sốc trước khi bạn cải thiện.
- Tìm một nút thắt duy nhất chi phối thông lượng, và thôi tối ưu ở mọi nơi khác.
- Định giá trì hoãn bằng tiền để ưu tiên trở thành quyết định kinh tế, không phải cuộc thi âm lượng.
- Sắp thứ tự công việc theo chi phí trì hoãn chia cho thời lượng, không phải theo ai tranh luận to nhất.
- Coi quản lý dòng giá trị là thực hành liên tục, không phải buổi hội thảo một lần.

## Khuyến nghị

### Lập bản đồ dòng giá trị từ ý tưởng đến giá trị

Một [dòng giá trị](https://en.wikipedia.org/wiki/Value_stream) là chuỗi đầy đủ các bước tổ chức của bạn thực hiện để biến một yêu cầu thành giá trị được giao. Lập bản đồ nó nghĩa là đi qua chuỗi đó và viết xuống mỗi bước, ai làm nó, và với mỗi cái, hai con số: thời gian xử lý (thời gian công việc đang được làm tích cực) và thời gian chờ (tổng thời gian trôi qua từ khi bước có thể bắt đầu đến khi nó bàn giao, gồm mọi sự chờ đợi). Hãy làm điều này cho một mục công việc đại diện, từ khoảnh khắc ý tưởng được chấp nhận đến khoảnh khắc hiệu ứng của nó được đo trong sản xuất. Gồm các bước khám phá từ chương 11.1 và các bước phân phối từ chương 11.2. Kết quả là một sơ đồ duy nhất của hệ thống thật của bạn, không phải cái trên sơ đồ tổ chức.

Chống lại thôi thúc lập bản đồ quy trình lý tưởng hóa. Hãy lập bản đồ cái thực sự xảy ra với ba bốn mục gần đây, dùng dấu thời gian từ công cụ của bạn thay vì trí nhớ. Bạn đang tìm sự thật, và sự thật sống trong khoảng trống giữa các bước. Lần đầu một đội làm điều này trung thực, luôn có ai đó nói một phiên bản của "tôi không biết nó nằm đó cả tuần." Phản ứng đó là mục đích. Bạn không thể cải thiện một dòng chảy bạn chưa bao giờ thấy trọn vẹn.

### Tách thời gian xử lý khỏi thời gian chờ, và tính hiệu quả luồng

Khi bạn có các con số, hãy cộng chúng. [Hiệu quả luồng](https://en.wikipedia.org/wiki/Value-stream_mapping) là tỷ lệ giữa thời gian tạo giá trị với tổng thời gian chờ: tổng thời gian xử lý chia cho tổng thời gian trôi qua từ đầu đến cuối. Nếu một tính năng mất 40 giờ công việc thực nhưng 20 ngày làm việc để đi qua dòng, hiệu quả luồng của nó xấp xỉ 40 chia 160, hay 25 phần trăm, và điều đó sẽ là tốt bất thường. Nhiều dòng thật rơi vào khoảng 5 đến 15 phần trăm. Phần còn lại là chờ đợi thuần túy: công việc nằm trong hàng đợi, bị chặn bởi một phụ thuộc, hoặc đậu trong hộp thư của ai đó.

Con số này đóng khung lại mọi cuộc trò chuyện cải thiện. Khi hiệu quả luồng là 15 phần trăm, làm chính công việc nhanh hơn 20 phần trăm chỉ cải thiện tổng thêm ba điểm, trong khi loại bỏ một nửa sự chờ gần như nhân đôi tốc độ của bạn. Các đội theo bản năng cố viết mã nhanh hơn, rà soát nhanh hơn, kiểm thử nhanh hơn. Bản đồ cho bạn biết rằng đòn bẩy hầu như không bao giờ nằm ở các bước làm việc và hầu như luôn nằm ở sự chờ đợi giữa chúng. Hãy đuổi theo khoảng trắng, không phải các hộp.

### Gọi tên các bàn giao và vòng làm lại

Hai cấu trúc trên bản đồ xứng đáng sự chú ý đặc biệt. Bàn giao là những điểm nơi công việc chuyển từ một người hay đội sang người hay đội khác, và mỗi cái là một hàng đợi nơi một mục chờ bên tiếp theo có năng lực. Mỗi bàn giao cũng mất ngữ cảnh, nên bên nhận tiêu thời gian dựng lại điều bên gửi đã biết. Vòng làm lại là những mũi tên đi ngược: một kiểm thử thất bại trả mã về nhà phát triển, một thay đổi bị từ chối quay về hội đồng rà soát, một sự làm rõ đưa một câu chuyện về lại sản phẩm. Vòng làm lại đắt gấp đôi, vì chúng tiêu năng lực và vì mục được làm lại nhập lại một hàng đợi ở cuối hàng.

Hãy đếm cả hai. Một dòng có chín bàn giao và ba vòng làm lại sẽ có hiệu quả luồng tệ bất kể con người giỏi đến đâu, vì chính cấu trúc sản xuất ra sự chờ đợi. Giảm bàn giao (bằng cách trao cho một đội quyền sở hữu đầu-cuối) và loại bỏ nguyên nhân làm lại (bằng cách chuyển kiểm tra chất lượng sớm hơn, theo chương 11.2) thường thắng bất kỳ nỗ lực nào để tăng tốc từng bước riêng lẻ.

### Tìm nút thắt và tôn trọng lý thuyết ràng buộc

Mọi dòng giá trị có đúng một bước giới hạn thông lượng của nó, như điểm hẹp nhất trong một đường ống giới hạn dòng chảy. [Lý thuyết ràng buộc](https://en.wikipedia.org/wiki/Theory_of_constraints), của Eliyahu Goldratt, cho bạn một kỷ luật cho nó: xác định ràng buộc, khai thác nó (bảo đảm nó không bao giờ nhàn rỗi và không bao giờ làm sai việc), phụ thuộc mọi thứ khác vào nó (đừng nuôi nó nhanh hơn nó hấp thụ được), nâng nó lên (thêm năng lực), rồi lặp lại, vì ràng buộc sẽ đã dịch chuyển. Quy tắc then chốt và phản trực giác là cải thiện bất kỳ bước nào khác ràng buộc không cải thiện gì. Tăng tốc một bước không phải nút thắt chỉ dồn hàng tồn trước nút thắt nhanh hơn.

Hãy tìm ràng buộc của bạn trên bản đồ: đó là bước có hàng đợi dài nhất và dai dẳng nhất phía trước. Trong phần mềm nó thường là một tài nguyên dùng chung, chuyên biệt như một chức năng rà soát bảo mật duy nhất, một chuyên gia cơ sở dữ liệu đơn độc, hay một môi trường kiểm thử khan hiếm. Một khi bạn biết nó, hãy bảo vệ nó. Đừng để nó nhàn rỗi chờ đầu vào, đừng bắt nó làm việc mà một bước rẻ hơn có thể làm, và hãy suy nghĩ kỹ trước khi tối ưu bất cứ thứ gì hạ nguồn hay thượng nguồn của nó. Cả hệ thống di chuyển theo nhịp của một bước đó.

### Dùng chi phí trì hoãn để ưu tiên bằng kinh tế

Chi phí trì hoãn là tiền bạn mất, hoặc không thu được, cho mỗi đơn vị thời gian một phần công việc chưa được giao. Đó là trọng lượng kinh tế của "sau này." Một tính năng sẽ kiếm 100.000 đô la mỗi tháng, bị trễ hai tháng, tốn 200.000 đô la dù con số đó có bao giờ xuất hiện trong ngân sách hay không. Làm điều này tường minh là thuốc giải mạnh nhất đơn lẻ cho bệnh lý "mọi thứ đều ưu tiên một" hành hạ các tồn đọng lớn. Khi mọi bên liên quan khăng khăng mục của họ là khẩn cấp, bạn không giải quyết được bằng âm lượng; bạn giải quyết bằng hỏi từng người, "Một tháng trì hoãn tốn chúng ta bao nhiêu?" và đặt các câu trả lời cạnh nhau.

Ước tính chi phí trì hoãn không đòi độ chính xác. Một con số thô, được thống nhất bởi những người hiểu giá trị, thắng một đồng thuận giả rằng mọi thứ quan trọng như nhau. Hãy xét ba thành phần: bản thân giá trị (doanh thu, tiết kiệm chi phí, giảm rủi ro), độ nhạy thời gian (giá trị có phai nếu chúng ta chờ không?), và bất kỳ hạn chót cứng nào (một quy định, một hợp đồng, một cửa sổ theo mùa). Điều này nối trực tiếp với kỷ luật ước lượng và dự báo của chương 10.15: bạn đang dự báo giá trị rủi ro, không chỉ công sức. Con số không cần đúng đến từng đô la. Nó cần đủ đúng để đổi thứ tự bạn làm việc.

### Sắp thứ tự bằng CD3 và công-việc-ngắn-nhất-có-trọng-số-trước

Chi phí trì hoãn cho bạn biết cái gì đắt để trì hoãn, nhưng tự nó không cho bạn biết làm gì trước, vì một mục giá trị khổng lồ mất sáu tháng có thể là lựa chọn đầu tiên tệ hơn một mục giá trị vừa phải bạn hoàn thành tuần này. Quy tắc giải quyết điều này là chi phí trì hoãn chia cho thời lượng, viết là CD3. Bạn tính chi phí trì hoãn cho mỗi mục, chia cho thời gian mục đó mất, và làm tỷ lệ cao nhất trước. Đây là ứng dụng phần mềm của [công-việc-ngắn-nhất-có-trọng-số-trước](https://en.wikipedia.org/wiki/Weighted_shortest_job_first) (WSJF), một kết quả lập lịch chứng minh rằng chia chi phí trì hoãn cho độ dài công việc tối thiểu hóa tổng chi phí kinh tế qua cả hàng đợi công việc.

Hiểu biết mà WSJF mã hóa là công việc ngắn, có giá trị nên nhảy hàng, vì hoàn thành chúng nhanh giải phóng hàng đợi và bắt đầu giá trị của chúng sớm hơn mà hầu như không làm trễ gì khác. Một công việc dài, dù có giá trị, giữ chân mọi thứ phía sau. Trong thực hành bạn ước tính chi phí trì hoãn và thời lượng trên các thang tương đối đơn giản, tính tỷ lệ, và để nó sắp thứ tự tồn đọng của bạn. Khung được nhiều tổ chức quy mô lớn dùng diễn đạt WSJF là chi phí trì hoãn (xây từ giá trị kinh doanh, tính cấp bách thời gian, và khả năng thực hiện rủi ro-hoặc-cơ hội) chia cho kích thước công việc, cùng ý tưởng với các thành phần có tên.

### Đọc hồ sơ cấp bách của từng mục

Không phải mọi chi phí trì hoãn hành xử như nhau theo thời gian, và hình dạng quan trọng ngang kích thước. Một hồ sơ cấp bách mô tả chi phí trì hoãn đổi thế nào khi bạn chờ. Một số giá trị xấp xỉ tuyến tính: bạn mất lượng tương tự mỗi tuần vô hạn. Một số có ngày cố định, hàm bậc thang, nơi trì hoãn không tốn gì cho đến hạn chót rồi tốn rất nhiều cùng lúc (chuyển đổi quy định, ngày vận hành hợp đồng). Một số phai: cửa sổ thị trường hay lợi thế người đi đầu cạnh tranh đáng cả gia tài bây giờ và ít sau sáu tháng. Và một số gần như phẳng, đáng như nhau bất cứ khi nào bạn phát hành.

Biết hồ sơ đổi cách bạn sắp thứ tự. Một mục giá trị phai dốc nên đi ngay, trước khi giá trị xói mòn. Một mục ngày cố định có thể chờ cho đến khi chỉ còn đủ thời gian dẫn, rồi không được trượt. Vẽ hồ sơ cấp bách cho các sáng kiến lớn của bạn, dù thô, cho bạn biết không chỉ trì hoãn tốn bao nhiêu mà khi nào chi phí đáp xuống, chính xác là cái bạn cần để lên lịch dưới cạnh tranh.

### Nối chỉ số luồng với DORA và Định luật Little

Lập bản đồ dòng giá trị tạo ra bốn chỉ số luồng liên tục đáng theo dõi: thời gian chờ (thời gian trôi qua từ đầu đến xong), thời gian chu kỳ (thời gian trôi qua cho một giai đoạn cụ thể, thường là phần phân phối tích cực), công việc đang làm (WIP, số mục đang bay), và thông lượng (số mục hoàn thành trên đơn vị thời gian). Chúng bị ràng buộc với nhau bởi Định luật Little từ chương 11.3: thời gian chờ trung bình bằng WIP trung bình chia cho thông lượng trung bình. Phương trình đó là đòn bẩy thực tế nhất của bạn, vì nó nói nếu bạn không dễ nâng thông lượng, bạn có thể rút ngắn thời gian chờ ngay bằng cách hạ WIP. Bắt đầu ít hơn hoàn thành nhiều hơn.

Các chỉ số luồng này cũng nối lên các chỉ số [DORA](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (từ chương trình DevOps Research and Assessment): tần suất triển khai, thời gian chờ cho thay đổi, tỷ lệ thay đổi thất bại, và thời gian khôi phục dịch vụ. Thời gian chờ cho thay đổi là một lát của dòng giá trị của bạn, và việc lập bản đồ cho bạn thấy bước nào để tấn công nhằm cải thiện nó. Hãy coi DORA là bảng điểm kết quả và bản đồ dòng giá trị là chẩn đoán giải thích điểm số, gắn cả hai vào góc nhìn hiệu quả kỹ thuật của chương 1.10.

### Quản lý hàng đợi, kích thước lô và WIP có chủ đích

Các hàng đợi bạn tìm thấy trên bản đồ là nơi thời gian chờ được sinh ra, và chương 11.3 giải thích vì sao chúng bùng nổ khi mức sử dụng leo tới 100 phần trăm. Hai đòn bẩy thuần hóa chúng. Thứ nhất là giới hạn WIP: giới hạn số mục được phép ở mỗi giai đoạn để công việc chỉ được kéo khi có năng lực, trực tiếp rút ngắn thời gian chờ qua Định luật Little và làm lộ nút thắt thay vì giấu nó dưới núi công việc đã bắt đầu nhưng chưa hoàn thành. Thứ hai là kích thước lô: lô lớn (một bản phát hành hằng quý, một pull request khổng lồ, một tài liệu yêu cầu lớn) tạo hàng đợi dài, trì hoãn phản hồi, và nâng chi phí cùng rủi ro của mỗi bàn giao.

Lô nhỏ hơn chảy nhanh hơn và khả đoán hơn, một trong những lý do sâu nhất khiến quy trình phân phối của chương 11.2 ưu tiên thay đổi nhỏ, thường xuyên, đảo ngược được. Giảm kích thước lô và giới hạn WIP là hai can thiệp đáng tin cậy nhất, chi phí thấp nhất bạn làm được, vì chúng tấn công trực tiếp sự chờ đợi thay vì cố làm chính công việc nhanh hơn.

## Đánh đổi: ưu và nhược điểm

| Thực hành | Ưu điểm | Nhược điểm |
|---|---|---|
| Lập bản đồ dòng giá trị | Làm lộ sự chờ ẩn; căn chỉnh các đội vào một bức tranh | Ảnh chụp có thể cũ; công sức lãng phí nếu không có hành động theo sau |
| Chỉ số hiệu quả luồng | Chuyển nỗ lực sang sự chờ, nơi có đòn bẩy | Có thể bị lách bằng định nghĩa lại cái gì tính là công việc tích cực |
| Tập trung lý thuyết ràng buộc | Tập trung nỗ lực nơi nó thực sự dịch chuyển thông lượng | Khó về chính trị khi để yên các đội không phải nút thắt |
| Chi phí trì hoãn | Biến ưu tiên thành kinh tế; xì hơi "tất cả đều khẩn cấp" | Ước tính bất định và có thể bị tranh cãi hay thổi phồng |
| Sắp thứ tự CD3 / WSJF | Tối thiểu hóa tổng trì hoãn kinh tế; ưu tiên chiến thắng nhanh | Cần hai ước tính mỗi mục; rủi ro độ chính xác giả |
| Giới hạn WIP | Rút ngắn thời gian chờ ngay; làm lộ nút thắt | Cảm giác như bị ép rảnh rỗi; bị kháng cự về văn hóa |
| Kích thước lô nhỏ | Phản hồi nhanh hơn, rủi ro thấp hơn mỗi thay đổi | Chi phí chung mỗi mục cao hơn nếu tự động hóa yếu |

Căng thẳng trung tâm là giữa công sức đo lường và sự trung thực mà nó buộc. Một bản đồ dòng giá trị và một mô hình chi phí trì hoãn đều tốn công xây, và cả hai có thể bị lách hoặc để mục rữa nếu tổ chức không nghiêm túc. Kiểu thất bại là một buổi hội thảo lập bản đồ tạo ra một sơ đồ đẹp mà không có thay đổi nào, hay một con số chi phí trì hoãn mà mọi bên liên quan thổi phồng cho đến khi nó lại vô nghĩa. Hãy giải quyết bằng gắn thực hành với hành động và với một tập nhỏ chỉ số luồng được theo dõi. Một bản đồ chỉ đáng làm nếu bạn sẽ tấn công nút thắt nó làm lộ, và một ước tính chi phí trì hoãn chỉ đáng tranh luận nếu nó thực sự sắp xếp lại tồn đọng. Độ chính xác không phải mục tiêu; một quyết định tốt hơn mới là.

## Câu hỏi để thảo luận với đội của bạn

1. **Nếu chúng ta lập bản đồ dòng giá trị thật từ ý tưởng đến sản xuất cho ba tính năng gần nhất, hiệu quả luồng thực của chúng ta sẽ là bao nhiêu, và bể chờ đợi lớn nhất ở đâu?** Hầu hết các đội chưa bao giờ tính điều này và bị sốc bởi câu trả lời, vì các bước làm việc họ thấy cảm giác bận trong khi sự chờ đợi giữa chúng vô hình. Hãy mang dấu thời gian từ công cụ của bạn thay vì trí nhớ, và đi qua một mục gần đây từ đầu đến cuối, viết thời gian xử lý và tổng thời gian chờ cho mỗi bước. Bằng chứng bạn muốn là khoảng trống lớn nhất đơn lẻ giữa khi công việc có thể di chuyển và khi nó thực sự di chuyển. Khoảng trống đó, không phải tốc độ của bất kỳ cá nhân nào, là mục tiêu đầu tiên của bạn, và gọi tên nó to thường đủ để làm đội muốn sửa nó.

2. **Ràng buộc thật duy nhất của chúng ta ở đâu, và chúng ta có đang vô tình tối ưu mọi thứ ngoại trừ nó không?** Lý thuyết ràng buộc nói chỉ nút thắt chi phối thông lượng, vậy mà các đội thường xuyên đổ công sức vào các bước vốn đã nhanh vì đó là các bước họ kiểm soát. Hãy tìm bước có hàng đợi dài nhất, dai dẳng nhất phía trước, và trung thực về việc các cải thiện gần đây có chạm vào nó hay chỉ làm một bước không phải nút thắt nhanh hơn. Kết luận khó chịu nhưng có giá trị thường là một tài nguyên dùng chung, khan hiếm (một người rà soát, một môi trường, một chuyên gia) đặt nhịp cho mọi người, và bảo vệ cùng nâng tài nguyên đó quan trọng hơn bất kỳ tăng tốc cục bộ nào ở nơi khác.

3. **Khi hai bên liên quan đều nói công việc của họ là ưu tiên một, chúng ta quyết định thế nào hôm nay, và chi phí trì hoãn có cho chúng ta thứ tự khác không?** Ngay bây giờ câu trả lời có lẽ là thâm niên, âm lượng, hoặc ai leo thang mạnh nhất, không cái nào phản ánh giá trị kinh tế. Hãy mang hai mục thực sự bị tranh chấp và thử ước tính, dù thô, một tháng trì hoãn tốn mỗi cái bao nhiêu và mỗi cái mất bao lâu, rồi tính chi phí trì hoãn chia cho thời lượng. Điểm không phải là các con số chính xác mà là cuộc trò chuyện chúng buộc: các bên liên quan phải gắn chi phí trì hoãn vào yêu cầu của họ đột nhiên lập luận khác, và mục thắng về kinh tế thường không phải mục đang thắng về âm lượng. Hãy xem điều đó làm gì với căn phòng.

4. **Bàn giao nào trong dòng giá trị của chúng ta có thể bị loại bỏ hay gộp, và ai sẽ phải từ bỏ quyền kiểm soát để điều đó xảy ra?** Mỗi bàn giao là một hàng đợi và một sự mất ngữ cảnh, nên số bàn giao thường dự đoán hiệu quả luồng tốt hơn kỹ năng của bất kỳ đội nào, vậy mà bàn giao vẫn tồn tại vì chúng mã hóa quyền sở hữu, quyền phê duyệt, và cảm giác trách nhiệm của ai đó. Với tổ chức lớn đây là nơi bản đồ trở nên chính trị: gộp một bàn giao thường nghĩa là trao một đội quyền sở hữu đầu-cuối và yêu cầu một chức năng kiểm soát tin một cổng tự động thay vì ký duyệt thủ công. Hãy mang thời gian chờ từng bàn giao, các vòng làm lại mà mỗi bàn giao kích hoạt, và ghi chú trung thực bàn giao nào tồn tại vì lý do rủi ro thật so với thói quen lịch sử. Trong bối cảnh doanh nghiệp và chính phủ, hãy nêu chủ sở hữu kiểm soát cho mỗi bàn giao bị tranh chấp và bằng chứng nào (một kiểm tra tự động đạt, một dấu vết kiểm toán, một thẩm quyền được ủy) sẽ cho họ chấp nhận việc loại bỏ, vì một bàn giao không ai nhượng là khoản thuế vĩnh viễn lên thời gian chờ của bạn.

5. **Chúng ta tự tin đến đâu vào các con số chi phí trì hoãn đang dùng để sắp thứ tự công việc, và cái gì ngăn mọi bên liên quan đơn giản thổi phồng con số của họ?** Chi phí trì hoãn chỉ phá được thế hòa "mọi thứ đều ưu tiên một" nếu các ước tính mang một kỷ luật; khoảnh khắc mỗi bên học rằng con số lớn hơn thắng, tất cả đều tạo ra con số lớn hơn và bạn quay lại cuộc thi âm lượng khoác áo kinh tế. Cân nhắc đối lập là đòi độ chính xác giết thực hành, vì các con số thô được thống nhất bởi những người hiểu giá trị là toàn bộ ý nghĩa, nên bạn cần đủ độ nghiêm ngặt để so sánh các mục mà không giả vờ độ chính xác sai. Hãy mang vài ước tính thật được chia thành thành phần (giá trị, tính cấp bách thời gian, áp lực hạn chót) và tìm những cái tròn hay không có cơ sở một cách đáng ngờ. Với danh mục doanh nghiệp hay chương trình chính phủ tiêu tiền công, hãy quyết định ai phân xử các con số bị tranh chấp và liệu ước tính có được kiểm tra với kết quả thực hiện sau này không, vì một mô hình chi phí trì hoãn không ai hiệu chỉnh theo thực tế là mô hình mọi người cuối cùng sẽ lách.

6. **Chúng ta có thực sự quản lý công việc đang làm và kích thước lô có chủ đích, hay để cả hai trôi lên cho đến khi thời gian chờ lặng lẽ gấp đôi?** Định luật Little làm đòn bẩy cụ thể: thời gian chờ bằng công việc đang làm chia cho thông lượng, nên WIP không kiểm soát kéo dài thời gian chờ của mọi mục ngay cả khi không ai làm chậm hơn, và lô lớn cộng dồn hiệu ứng bằng cách nhồi các hàng đợi bạn đã tìm thấy trên bản đồ. Căng thẳng mang tính văn hóa, vì giới hạn WIP cảm giác như ép rảnh rỗi và lô nhỏ cảm giác như thêm chi phí chung, nên các đội kháng cự cả hai dù chúng là các can thiệp rẻ nhất có. Hãy mang số WIP hiện tại theo từng giai đoạn, kích thước lô điển hình của bạn (bản phát hành, pull request, tài liệu yêu cầu), và xu hướng thời gian chờ đi kèm. Trong tổ chức lớn hay công, hãy gắn điều này với nhịp phát hành và phê duyệt thay đổi mà bạn bị ràng buộc bởi hợp đồng hay quy trình, vì một cửa sổ phát hành hằng quý hay một hội đồng hằng tháng có thể ép lô lớn lên bạn, và gọi tên ràng buộc đó là bước đầu để thương lượng hạ nó xuống.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và ít đường băng, dòng giá trị của bạn ngắn nhưng ràng buộc của bạn thường là một người: một người sáng lập duy nhất phê duyệt mọi thứ, hay kỹ sư duy nhất sở hữu việc triển khai. Đừng chạy bài tập lập bản đồ nặng; hãy dành nửa ngày truy vết vài tính năng gần nhất theo dấu thời gian, tìm nút thắt con người, và ủy quyền hay gom lô quanh nó. Bỏ qua mô hình chi phí trì hoãn chính thức và dùng xếp hạng chi phí-trì-hoãn-chia-thời-lượng thô để kết thúc cuộc tranh luận hằng tuần "chúng ta xây gì tiếp theo," và giữ lô nhỏ xíu để phản hồi nhanh trong khi bạn còn đang học thị trường muốn gì.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia chỉ số luồng và ngân sách eo hẹp, nên hãy dựa vào công cụ bạn đã trả tiền: lấy dấu thời gian từ trình theo dõi vấn đề và quản lý phiên bản của bạn thay vì mua nền tảng dòng giá trị. Lập bản đồ một mục công việc đại diện, tính hiệu quả luồng ước lượng nhanh, và tấn công bể chờ đợi lớn nhất đơn lẻ, thường là một phê duyệt nằm với một chủ bận rộn. Coi chi phí trì hoãn là cuộc trò chuyện, không phải sản phẩm bảng tính để mua, và ưu tiên cắt công việc đang làm và kích thước lô (cả hai miễn phí) hơn bất kỳ công cụ nào hứa trực quan hóa luồng với phí hằng tháng.

**Doanh nghiệp lớn.** Giá trị nằm ở việc nhìn qua nhiều đội, nơi một tính năng đi qua sản phẩm, nền tảng, bảo mật và quản lý phát hành và sự chờ đợi giữa các nhóm lấn át công việc bên trong chúng. Chuẩn hóa lập bản đồ dòng giá trị thành thực hành lặp lại được, biến chi phí trì hoãn chia cho thời lượng thành ngôn ngữ ưu tiên chung để các nhóm thôi tranh luận từ âm lượng, và thực thi giới hạn WIP và lô nhỏ hơn để làm lộ ràng buộc thật thay vì giấu nó dưới công việc đã bắt đầu nhưng chưa hoàn thành. Gắn chỉ số luồng với DORA và Định luật Little để danh mục có một chẩn đoán và một bảng điểm, và đặt quản trị quanh ai sở hữu ràng buộc và ai phân xử các ước tính trì hoãn bị tranh chấp.

**Chính phủ.** Quy tắc mua sắm, nghĩa vụ minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn, và một hạn chót do luật định thường chi phối hồ sơ cấp bách của mọi thứ khác. Hãy lập bản đồ dòng qua chính sách, kỹ thuật, công nhận bảo mật và vận hành, vì ràng buộc cứng thường là một cổng công nhận hay tuân thủ với hàng đợi đo bằng tháng, và nâng nó (thêm người rà soát, chuyển việc thu thập bằng chứng lên thượng nguồn) mua được nhiều hơn bất kỳ tăng tốc hạ nguồn nào. Làm quản lý dòng giá trị thành thực hành thường trực với rà soát đều đặn để cơ quan giám sát có bằng chứng kiểm toán được rằng dòng chảy, không chỉ chi tiêu, đang cải thiện, và định giá chi phí trì hoãn công khai để thứ tự của tiền công có thể được giải thích và bảo vệ.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười lăm người cứ trượt lộ trình của chính mình và đổ lỗi cho kỹ sư. Một buổi lập bản đồ dòng giá trị nửa ngày kể câu chuyện khác: tính năng dành phần lớn đời mình chờ người sáng lập duy nhất phê duyệt mọi thiết kế và mọi bản phát hành. Hiệu quả luồng dưới 10 phần trăm, và người sáng lập là ràng buộc. Họ áp dụng trực tiếp lý thuyết ràng buộc: người sáng lập ủy quyền phê duyệt thiết kế dưới một ngưỡng kích thước, gom bản phát hành vào cửa sổ hằng ngày thay vì ký duyệt tùy nghi, và thôi bị nuôi nhiều quyết định hơn cô quyết định được. Thời gian chờ giảm xấp xỉ một nửa trong một tháng, không tuyển ai. Họ rồi áp dụng xếp hạng chi phí-trì-hoãn-chia-thời-lượng đơn giản cho tồn đọng, lặng lẽ kết thúc cuộc tranh luận hằng tuần về xây gì tiếp theo.

**Doanh nghiệp lớn.** Một ngân hàng lớn lập bản đồ dòng giá trị cho một thay đổi hướng khách hàng và thấy nó đi qua chín đội với thời gian chờ mười một tuần, trong đó khoảng sáu ngày là công việc thật. Phần còn lại là hàng đợi: một rà soát bảo mật chạy hằng tháng, một hội đồng phê duyệt thay đổi họp hằng tuần, và đặt môi trường đo bằng ngày. Thay vì thúc các đội làm nhanh hơn, ngân hàng tấn công sự chờ đợi: nó chuyển rà soát bảo mật sớm hơn và tự động hóa phần lớn (theo chương 11.2), chuyển hội đồng hằng tuần thành phê duyệt thường trực nhẹ cho thay đổi rủi ro thấp, và giới hạn WIP để các đội hoàn thành trước khi bắt đầu thêm. Chi phí trì hoãn trở thành ngôn ngữ ưu tiên của danh mục, xì hơi tồn đọng "mọi thứ đều trọng yếu" triền miên thành một cái đã xếp hạng, và thời gian chờ cho thay đổi (chỉ số DORA) giảm từ mười một tuần xuống dưới hai.

**Chính phủ.** Một cơ quan thuế quốc gia chạy hiện đại hóa nhiều năm dưới hạn chót do luật định. Lãnh đạo không thấy được tiền công đang mua tiến bộ ở đâu, vì chương trình báo cáo hoạt động, không phải dòng chảy. Cơ quan lập bản đồ dòng giá trị qua chính sách, kỹ thuật, công nhận bảo mật và vận hành, và phát hiện công nhận là ràng buộc cứng với hàng đợi đo bằng tháng. Nó coi công nhận là nút thắt cần nâng, thêm nhân sự và chuyển việc thu thập bằng chứng lên thượng nguồn để các mục đến sẵn sàng rà soát. Nó định giá chi phí trì hoãn bằng hồ sơ cấp bách của từng nhiệm vụ: hạn chót lập pháp cố định chi phối thứ tự, trong khi công việc dọn dẹp giá trị phẳng chờ. Quản lý dòng giá trị trở thành thực hành thường trực với rà soát hằng quý, cho cơ quan giám sát bằng chứng kiểm toán được rằng dòng chảy, không chỉ chi tiêu, đang cải thiện.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của các thực hành này đến từ chuyển sự chờ đợi vô hình thành giá trị được giao sớm hơn. Khi hiệu quả luồng là 15 phần trăm, phần lớn thời gian chờ của bạn là lãng phí bạn đã trả tiền dưới dạng phản hồi chậm hơn, doanh thu muộn hơn, và các bên liên quan mất niềm tin vào lộ trình. Loại bỏ sự chờ đợi gần như miễn phí so với tuyển dụng: giới hạn WIP, lô nhỏ hơn, rà soát bảo mật sớm hơn, và một phê duyệt được ủy quyền tốn ít và thường giảm một nửa thời gian chờ. Mỗi tuần thời gian chờ bạn loại bỏ là một tuần giá trị được kéo về phía trước, và chi phí trì hoãn cho phép bạn định lượng lợi ích đó bằng cùng đồng tiền mà lãnh đạo của bạn đã theo dõi.

Ưu tiên theo chi phí trì hoãn có lợi tức riêng biệt: bằng sắp thứ tự với CD3 hay WSJF, bạn tối thiểu hóa một cách chứng minh được tổng trì hoãn kinh tế qua cả tồn đọng, nghĩa là cùng các đội, làm cùng số giờ, giao nhiều giá trị hơn chỉ bằng làm mọi thứ theo thứ tự tốt hơn. Đó là cải thiện rẻ nhất có, vì nó không cần năng lực mới nào. Chi phí áp dụng khiêm tốn và chủ yếu một lần: vài buổi lập bản đồ, một mô hình chi phí trì hoãn nhẹ, và kỷ luật theo dõi một nhúm chỉ số luồng. Chi phí liên tục là sự trung thực để giữ bản đồ hiện hành và chống thổi phồng ước tính trì hoãn.

Chi phí của bỏ bê cộng dồn lặng lẽ. Dòng chưa lập bản đồ tích lũy bàn giao và vòng làm lại mà không ai chịu trách nhiệm, tồn đọng được ưu tiên theo âm lượng trôi khỏi giá trị, và tổ chức hoạch định quanh trung bình trong khi hàng đợi bùng nổ gần mức sử dụng đầy (chương 11.3). Để lập luận với ban lãnh đạo, hãy nối các thực hành này với các chỉ số họ đã theo dõi: thời gian chờ cho thay đổi của DORA, thông lượng, và giá trị được giao mỗi quý. Đóng khung quản lý dòng giá trị là chẩn đoán giải thích các con số đó và chi phí trì hoãn là logic kinh tế cải thiện chúng.

## Phản mẫu và cạm bẫy

- **Lập bản đồ rồi quên:** một sơ đồ dòng giá trị bóng bẩy tạo ra trong hội thảo mà không dẫn đến thay đổi nào cho dòng chảy thực.
- **Tối ưu thứ không phải nút thắt:** tăng tốc các bước vốn đã nhanh, chỉ dồn hàng tồn trước ràng buộc thật.
- **Chỉ số luồng dưa hấu:** bảng điều khiển xanh (thông lượng cao) giấu thực tế đỏ (WIP khổng lồ và thời gian chờ kéo dài).
- **Thổi phồng chi phí trì hoãn:** mọi bên liên quan gán một con số khổng lồ, khôi phục thế hòa "mọi thứ đều ưu tiên một" mà bạn đang cố phá.
- **Mù thời lượng:** xếp hạng thuần theo giá trị và bắt đầu một công việc giá trị sáu tháng trước mười chiến thắng nhanh, bỏ qua CD3.
- **Phớt lờ hồ sơ cấp bách:** coi mục giá trị phai và mục giá trị phẳng như hoán đổi được, và phát hành nhầm cái trước.
- **Sùng bái hiệu quả cục bộ:** giữ mọi đội được sử dụng 100 phần trăm, tối đa hóa hàng đợi và thời gian chờ thay vì dòng chảy.
- **Phát hành lô lớn:** gộp thay đổi vào các đợt hiếm, lớn kéo dài hàng đợi, trì hoãn phản hồi, và nâng rủi ro của mỗi bản phát hành.
- **Hoạch định chỉ theo trung bình:** dùng thời gian chờ trung bình và phớt lờ độ biến thiên, rồi bị bất ngờ bởi cái đuôi dài (chương 11.3).

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Không ai thấy được dòng chảy đầu-cuối. Ưu tiên được đặt theo âm lượng, thâm niên hoặc leo thang, và "mọi thứ đều ưu tiên một" là chuẩn mực. Sự chờ đợi giữa các bước vô hình, và công sức cải thiện đáp xuống nơi một đội cảm thấy bận, thường không phải ràng buộc. Không ai tách thời gian xử lý khỏi thời gian chờ, nên những bể xếp hàng khổng lồ không được chú ý và không được định giá.
- **Mức 2, Phát triển:** Một hai đội đã lập bản đồ ít nhất một dòng giá trị và chỉ ra được các hàng đợi lớn nhất và hiệu quả luồng thô. Một số chỉ số luồng (thời gian chờ, WIP) được theo dõi ở từng điểm, và ưu tiên đôi khi xét giá trị, nhưng thực hành không nhất quán qua các đội: chi phí trì hoãn không chính thức, bản đồ là hiện vật một lần, và mỗi nhóm làm theo cách riêng nếu có.
- **Mức 3, Chuẩn hóa:** Lập bản đồ dòng giá trị là thực hành có tài liệu, lặp lại được dùng toàn tổ chức, ràng buộc được xác định và bảo vệ theo lý thuyết ràng buộc, và giới hạn WIP cùng lô nhỏ hơn là tiêu chuẩn được thực thi thay vì thí nghiệm cục bộ. Chi phí trì hoãn chia cho thời lượng (CD3 hay WSJF) là cách đã thống nhất để sắp thứ tự tồn đọng qua các đội, và chỉ số luồng nối tường minh với DORA bằng định nghĩa chung về thời gian chờ, thời gian chu kỳ, WIP và thông lượng.
- **Mức 4, Quản lý:** Dòng chảy được đo và kiểm soát bằng dữ liệu theo đường cơ sở. Hiệu quả luồng, thời gian chờ, WIP, thông lượng, và thời gian chờ cho thay đổi của DORA được theo dõi liên tục theo mục tiêu đã thống nhất, với giới hạn kiểm soát gắn cờ khi một dòng trôi. Ước tính chi phí trì hoãn được hiệu chỉnh theo kết quả thực hiện để thổi phồng bị bắt, hàng đợi của ràng buộc được giám sát bằng số thật, và quyết định tiếp tục hay dừng với thay đổi quy trình được đưa ra dựa trên bằng chứng thay vì ý kiến.
- **Mức 5, Điều phối:** Quản lý dòng giá trị là liên tục, tích hợp qua tổ chức, và thích ứng. Hồ sơ cấp bách thông tin cho sắp thứ tự, ràng buộc được nâng và xác định lại khi nó dịch chuyển, mô hình chi phí trì hoãn được tinh chỉnh từ kết quả thật, và lập bản đồ, ưu tiên, cùng quản lý hàng đợi nuôi nhau và danh mục rộng hơn. Tổ chức cân bằng lại dòng chảy khi điều kiện dịch chuyển và chứng minh được cải thiện bằng bằng chứng kiểm toán được.

## Ý tưởng để thảo luận

1. Hiệu quả luồng hiện tại của bạn là bao nhiêu, và nếu bạn loại bỏ một nửa sự chờ đợi thay vì tăng tốc công việc, bạn sẽ nhanh hơn bao nhiêu?
2. Ràng buộc thật duy nhất của bạn bây giờ ở đâu, và cần gì để giữ nó không bao giờ nhàn rỗi hay làm việc mà một bước rẻ hơn có thể làm?
3. Với năm mục tồn đọng hàng đầu của bạn, một tháng trì hoãn tốn mỗi mục bao nhiêu, và xếp hạng theo chi phí trì hoãn chia cho thời lượng có đổi thứ tự không?
4. Sáng kiến lớn nào của bạn có hồ sơ cấp bách phai, và bạn có nguy cơ phát hành nó sau khi phần lớn giá trị của nó đã bốc hơi không?
5. Nếu bạn cắt WIP một nửa vào ngày mai, Định luật Little dự đoán gì cho thời gian chờ của bạn, và bạn sẽ phải vượt qua kháng cự văn hóa nào để thử?
6. Lô điển hình của bạn lớn thế nào (bản phát hành, pull request, tài liệu yêu cầu), và giảm một nửa nó sẽ làm gì với tốc độ phản hồi và rủi ro mỗi thay đổi?

## Những điểm cần ghi nhớ

- Lập bản đồ toàn bộ dòng chảy từ ý tưởng đến giá trị và tính hiệu quả luồng; sự chờ đợi giữa các bước, không phải công việc bên trong chúng, là nơi đòn bẩy của bạn sống.
- Tìm ràng buộc duy nhất và tôn trọng lý thuyết ràng buộc: tối ưu bất kỳ bước nào khác không cải thiện gì và chỉ nuôi nút thắt nhanh hơn.
- Làm chi phí trì hoãn tường minh bằng tiền để đánh bại "mọi thứ đều ưu tiên một," và đọc hồ sơ cấp bách của từng mục để biết khi nào chi phí đáp xuống.
- Sắp thứ tự bằng chi phí trì hoãn chia cho thời lượng (CD3 hay WSJF) để tối thiểu hóa tổng trì hoãn kinh tế, để công việc ngắn, có giá trị nhảy hàng.
- Quản lý hàng đợi bằng giới hạn WIP và lô nhỏ, nối chỉ số luồng của bạn với DORA và Định luật Little, và chạy quản lý dòng giá trị như thực hành liên tục.

## Tài liệu tham khảo và đọc thêm

- Donald G. Reinertsen, *The Principles of Product Development Flow: Second Generation Lean Product Development*
- Eliyahu M. Goldratt và Jeff Cox, *The Goal: A Process of Ongoing Improvement*
- Mike Rother và John Shook, *Learning to See: Value Stream Mapping to Add Value and Eliminate Muda*
- Karen Martin và Mike Osterling, *Value Stream Mapping: How to Visualise Work and Align Leadership for Organizational Transformation*
- Mik Kersten, *Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow Framework*
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Dean Leffingwell, *SAFe 5.0 Distilled: Achieving Business Agility with the Scaled Agile Framework*
