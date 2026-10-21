# 7.5 Khoa học quyết định và văn hóa dựa trên dữ liệu

## Tổng quan và động lực

Khoa học quyết định là thực hành nối dữ liệu với các quyết định thực, dựa trên thống kê, khoa học hành vi và phán đoán để giúp mọi người chọn tốt trong điều kiện bất định. Một văn hóa dựa trên dữ liệu là điều kiện tổ chức trong đó điều này xảy ra theo mặc định: mọi người với tới bằng chứng, suy luận cẩn thận về nhân quả, truyền đạt độ bất định trung thực, và cập nhật niềm tin khi dữ liệu bảo đảm. Chương này cố ý là đỉnh chóp của chuỗi dữ liệu, vì mọi chiến lược, kỹ thuật, phân tích và thử nghiệm đến trước nó đều vô giá trị nếu chúng không thay đổi quyết định theo hướng tốt hơn.

Với các đội lớn, đây là nơi các khoản đầu tư dữ liệu thất bại nhiều nhất, không phải ở đường ống mà ở dặm cuối từ hiểu biết đến hành động. Doanh nghiệp chi nặng cho nền tảng và bảng điều khiển mà vẫn đưa ra các quyết định lớn theo thứ bậc, thói quen, hoặc người thuyết trình tự tin nhất. Một kiểu thất bại phổ biến là sân khấu dữ liệu: bảng điều khiển và phân tích tỉ mỉ được tạo ra để trông chặt chẽ trong khi quyết định thực đã được đưa ra từ trước và dữ liệu bị chọn lọc để biện minh cho nó. Chính phủ thêm rủi ro cao và sự soi xét. Các quyết định chính sách được biện minh bởi những tuyên bố nhân quả yếu có thể phân bổ sai tiền công và hại công dân, và đòi hỏi trách nhiệm giải trình khiến suy luận trung thực về bằng chứng là nghĩa vụ công dân, không chỉ là thực hành tốt.

Những vấn đề khó ở đây mang tính nhận thức và văn hóa, không phải kỹ thuật. Người ta nhầm lẫn [tương quan với nhân quả](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation), bỏ qua [yếu tố gây nhiễu](https://en.wikipedia.org/wiki/Confounding) (các biến ẩn thúc đẩy cả nguyên nhân giả định lẫn hệ quả), neo vào con số đầu tiên họ thấy, và đọc ước lượng điểm như sự chắc chắn. Và trong nỗ lực trở thành dựa trên dữ liệu, các tổ chức có thể trôi vào giám sát: đo cá nhân xâm phạm đến mức phá hủy lòng tin và kích động thao túng. Xây một văn hóa đo lường đích thực nghĩa là suy luận đúng, truyền đạt độ bất định trung thực, và đo hệ thống cùng kết quả mà không biến dữ liệu thành công cụ kiểm soát con người.

## Các nguyên tắc chính

- Mục đích của dữ liệu là quyết định tốt hơn, không phải sản xuất báo cáo.
- Hãy quyết định điều gì sẽ làm bạn đổi ý trước khi nhìn dữ liệu.
- Tương quan không phải nhân quả; chất vấn yếu tố gây nhiễu trước khi hành động.
- Truyền đạt độ bất định trung thực; một ước lượng điểm không có khoảng gây hiểu lầm.
- Hãy dựa trên dữ liệu, không bị dữ liệu nô lệ hóa; phán đoán và ngữ cảnh vẫn quan trọng.
- Đo để học và cải thiện hệ thống, không phải để giám sát và trừng phạt cá nhân.
- Cập nhật niềm tin khi bằng chứng bảo đảm; đổi ý là một điểm mạnh.
- [An toàn tâm lý](https://en.wikipedia.org/wiki/Psychological_safety) là điều kiện tiên quyết cho phân tích trung thực và bất đồng chính kiến.

## Khuyến nghị

### Nối dữ liệu với quyết định và tránh sân khấu dữ liệu

Hãy gắn phân tích với một quyết định cụ thể ngay từ đầu: chúng ta sẽ làm khác đi gì tùy theo những gì chúng ta tìm thấy? Trước khi thu thập dữ liệu, hãy nêu quyết định, các lựa chọn, và bằng chứng nào sẽ ủng hộ từng cái, lý tưởng là kết quả nào sẽ làm bạn đổi ý. Điều này bảo vệ chống sân khấu dữ liệu, nơi phân tích chỉ trang trí một quyết định đã đưa ra. Nếu không phát hiện thực tế nào sẽ thay đổi lựa chọn, đừng chi cho phân tích. Hãy đưa ra phán đoán một cách trung thực và nói rõ như vậy. Nhấn mạnh rằng các bài thuyết trình dẫn đầu bằng quyết định và khuyến nghị, không phải một chuyến tham quan biểu đồ.

### Suy luận cẩn thận về nhân quả

Hầu hết câu hỏi kinh doanh và chính sách là nhân quả (hành động này có tạo ra kết quả này không), nhưng hầu hết dữ liệu sẵn có là quan sát và đầy yếu tố gây nhiễu. Hãy dạy các đội sự khác biệt giữa tương quan và nhân quả, và các cái bẫy: biến gây nhiễu, [thiên kiến chọn mẫu](https://en.wikipedia.org/wiki/Selection_bias), nhân quả ngược và tương quan giả. Ưu tiên thử nghiệm ngẫu nhiên cho các tuyên bố nhân quả khi khả thi. Nơi thử nghiệm bất khả, hãy dùng các kỹ thuật [suy luận nhân quả](https://en.wikipedia.org/wiki/Causal_inference) cẩn thận và nêu giả định tường minh thay vì trượt từ "liên quan đến" sang "gây ra." Đặc biệt hoài nghi một câu chuyện hấp dẫn được dựng trên một tương quan duy nhất.

### Truyền đạt độ bất định cho các bên liên quan

Các con số được trình bày như ước lượng điểm chính xác mời gọi sự tự tin giả. Hãy truyền đạt khoảng, khoảng tin cậy hoặc khoảng khả tín, và các giả định chính đằng sau mọi con số. Dùng ngôn ngữ đơn giản và hình ảnh trung thực (thanh sai số, khoảng, dải kịch bản) để người ra quyết định nắm được điều đã biết và chưa biết. Phân biệt điều dữ liệu cho thấy, điều bạn suy ra, và điều bạn giả định. Hiệu chuẩn sự tự tin theo bằng chứng: trình bày một dự báo từ dữ liệu mỏng đúng như vậy. Độ bất định được truyền đạt trung thực xây dựng nhiều lòng tin hơn độ chính xác giả, vì nó sống sót khi chạm vào thực tế.

### Xây văn hóa đo lường không giám sát

Hãy tạo một môi trường nơi các đội thường xuyên xác định chỉ số thành công, đo kết quả và học từ chúng, nhưng hướng đo lường vào hệ thống, quy trình và kết quả thay vì giám sát cá nhân. Các chỉ số dùng để giám sát và xếp hạng con người bị thao túng, nuôi sợ hãi, và phá hủy sự trung thực mà quyết định tốt đòi hỏi (một động lực được [định luật Goodhart](https://en.wikipedia.org/wiki/Goodhart's_law) nắm bắt: một thước đo trở thành mục tiêu thì thôi là thước đo tốt). Ưu tiên chỉ số tổng hợp, định hướng kết quả. Để các đội tham gia chọn thước đo của chính mình, và tách chỉ số học tập khỏi đánh giá hiệu suất. Bảo vệ an toàn tâm lý để mọi người nêu tin xấu và bất đồng sớm.

### Nuôi dưỡng thói quen dữ liệu lành mạnh và hiểu biết dữ liệu

Hãy nâng hiểu biết dữ liệu rộng rãi để mọi người đọc biểu đồ một cách phê phán, chất vấn định nghĩa của một chỉ số, và phát hiện một tuyên bố gây hiểu lầm. Bình thường hóa việc hỏi "làm sao chúng ta biết điều đó?" và "điều gì sẽ làm chúng ta đổi ý?" Thưởng cho người cập nhật quan điểm theo bằng chứng và chạy thử nghiệm thất bại một cách có thông tin. Làm cho việc nói "dữ liệu không cho chúng ta biết" an toàn thay vì chế ra sự chắc chắn. Lãnh đạo đặt giọng điệu: khi họ đổi quyết định dựa trên bằng chứng và thừa nhận độ bất định, văn hóa theo sau.

### Bảo vệ chống thiên kiến và lạm dụng

Hãy để ý các thiên kiến dự đoán được: [thiên kiến xác nhận](https://en.wikipedia.org/wiki/Confirmation_bias) trong chọn dữ liệu ủng hộ, [thiên kiến người sống sót](https://en.wikipedia.org/wiki/Survivorship_bias) trong bỏ qua điều bị thiếu, neo vào con số ban đầu, và thiên kiến nhận thức muộn trong rà soát sau sự cố. Hãy xây vào đó rà soát phản biện (người đóng vai luật sư quỷ), đăng ký trước điều bạn kỳ vọng tìm thấy, và các góc nhìn đa dạng cho các phân tích quan trọng. Hãy coi trọng đạo đức dữ liệu (công bằng, minh bạch và tránh gây hại), đặc biệt khi quyết định ảnh hưởng đến sinh kế, trợ cấp hay quyền của mọi người.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Dựa vào dữ liệu (dữ liệu quyết định) | Giảm thiên kiến, nhất quán | Bỏ qua ngữ cảnh, bị thao túng, giòn | Các miền được hiểu rõ |
| Dựa trên dữ liệu (dữ liệu cộng phán đoán) | Cân bằng bằng chứng và ngữ cảnh | Chậm hơn, cần phán đoán | Quyết định phức tạp hoặc mới |
| Thử nghiệm cho nhân quả | Bằng chứng nhân quả mạnh | Tốn kém, chậm, không phải lúc nào cũng khả thi | Lựa chọn rủi ro cao, đảo ngược được |
| Suy luận quan sát | Dùng dữ liệu sẵn có | Rủi ro gây nhiễu, tuyên bố yếu hơn | Khi thử nghiệm bất khả |
| Chỉ số kết quả/hệ thống | Thúc đẩy cải thiện, ít thao túng | Ít trách nhiệm giải trình cá nhân hơn | Văn hóa học tập |
| Giám sát cá nhân | Khả năng nhìn chi tiết | Thao túng, sợ hãi, lòng tin bị xói mòn | Hiếm khi biện minh được |

Căng thẳng xác định là sự chặt chẽ so với tốc độ và tính khả thi. Thử nghiệm ngẫu nhiên cho bằng chứng nhân quả mạnh nhất, nhưng chúng tốn thời gian và thường bất khả cho các lựa chọn chiến lược hay chính sách một lần, nơi phán đoán cẩn thận về yếu tố gây nhiễu và giả định tường minh phải là đủ. Căng thẳng thứ hai là giữa đo lường và lòng tin: bạn đo cá nhân càng chi tiết, bạn thấy càng nhiều và nhận được càng ít hành vi trung thực. Một văn hóa trưởng thành nghiêng về phán đoán dựa trên dữ liệu và đo lường tổng hợp, định hướng kết quả. Nó chấp nhận độ chính xác bề ngoài kém hơn một chút để đổi lấy các quyết định đứng vững và một lực lượng lao động nói thật.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn có nêu điều gì sẽ làm bạn đổi ý trước khi nhìn dữ liệu không, và câu hỏi đó có được viết vào tài liệu quyết định của bạn không?** Biện pháp bảo vệ mạnh nhất của chương chống sân khấu dữ liệu là nêu quyết định, các lựa chọn, và bằng chứng nào ủng hộ từng cái, lý tưởng là kết quả sẽ lật lựa chọn của bạn, trước khi thu thập dữ liệu. Nếu không phát hiện thực tế nào sẽ thay đổi quyết định, nước đi trung thực là bỏ qua phân tích và đưa ra phán đoán công khai. Với doanh nghiệp và cơ quan nơi một lựa chọn chiến lược hay chính sách duy nhất có thể lãng phí hơn cả chi phí của một chương trình phân tích, kỷ luật này có đòn bẩy cao. Hãy mang một quyết định gần đây và hỏi liệu có phát hiện nào có thể thay đổi nó, hay các biểu đồ chỉ trang trí một kết luận đã đạt được. Nếu "điều gì sẽ làm chúng ta đổi ý?" không phải câu nhắc chuẩn trong tài liệu quyết định của bạn, hãy biến nó thành thế, và nhấn mạnh các bài thuyết trình dẫn đầu bằng khuyến nghị, không phải một chuyến tham quan biểu đồ.

2. **Khi một tương quan hấp dẫn xuất hiện, bạn chất vấn yếu tố gây nhiễu thế nào trước khi hành động, và bạn có ưu tiên thử nghiệm nơi khả thi không?** Chương cảnh báo hầu hết câu hỏi kinh doanh và chính sách là nhân quả trong khi hầu hết dữ liệu sẵn có là quan sát và đầy yếu tố gây nhiễu, thiên kiến chọn mẫu và nhân quả ngược. Các ví dụ của chính nó lặp lại một cái bẫy: khách hàng gắn bó tự chọn vào một tính năng hay chương trình, nên tương quan thô với rời bỏ thấp hơn hay tìm được việc cao hơn biến mất dưới một so sánh có đối chứng. Hành động theo tương quan đó nghĩa là một chiến dịch hay chính sách tốn kém, đi sai hướng. Hãy mang một quyết định gần đây dựa trên một tương quan duy nhất và hỏi biến ẩn nào có thể thúc đẩy cả hai phía. Nơi một thử nghiệm khả thi, hãy ưu tiên nó; nơi không, hãy dùng phương pháp suy luận nhân quả cẩn thận và nêu giả định tường minh thay vì trượt từ "liên quan đến" sang "gây ra."

3. **Chỉ số của bạn nhắm vào cải thiện hệ thống và kết quả, hay giám sát cá nhân, và bạn đã tách chỉ số học tập khỏi đánh giá hiệu suất chưa?** Chương vạch một lằn ranh rõ ràng: đo lường chĩa vào con người bị thao túng, nuôi sợ hãi, và phá hủy sự trung thực mà quyết định tốt đòi hỏi, một động lực định luật Goodhart dự đoán khi một thước đo thành mục tiêu. Nó ưu tiên chỉ số tổng hợp, định hướng kết quả, để các đội tham gia chọn thước đo của mình, và bảo vệ an toàn tâm lý để mọi người nêu tin xấu sớm. Trong bối cảnh chính phủ và doanh nghiệp, giám sát nhân viên tuyến đầu làm xói mòn lòng tin vốn làm cho dữ liệu chính xác khả thi ngay từ đầu. Hãy mang câu hỏi cụ thể: chỉ số nào của bạn có thể bị dùng để xếp hạng hay trừng phạt cá nhân, và mọi người có thao túng chúng dưới áp lực không? Nếu chỉ số học tập và đánh giá hiệu suất bị vướng vào nhau, hãy tách chúng, để đo lường thúc đẩy cải thiện thay vì hành vi phòng thủ.

4. **Khi một con số đến người ra quyết định, nó đến như một khoảng kèm giả định, hay như ước lượng điểm mời gọi sự tự tin giả?** Chương lập luận rằng độ bất định được truyền đạt trung thực xây dựng nhiều lòng tin hơn độ chính xác giả, vì nó sống sót khi chạm vào thực tế, vậy mà lực kéo về một con số tự tin duy nhất rất mạnh khi một nhà lãnh đạo muốn một câu trả lời gọn. Với một đội lớn, áp lực đối lập là có thật: khoảng và thanh sai số có thể đọc như né tránh với các giám đốc thưởng cho sự quyết đoán, nên nhà phân tích học cách lột bỏ các lưu ý để được nghe. Hãy mang một báo cáo gần đây và kiểm tra liệu nó có phân biệt điều dữ liệu cho thấy, điều bạn suy ra và điều bạn giả định, và liệu một dự báo dựa trên dữ liệu mỏng có được gắn nhãn đúng như vậy. Trong bối cảnh doanh nghiệp và chính phủ, nơi một con số có thể kết thúc trong hồ sơ hội đồng, hồ sơ ngân sách hay lời khai công khai, một ước lượng điểm trình bày như sự chắc chắn là khoản nợ, nên hãy thống nhất một tiêu chuẩn nội bộ rằng các con số hệ quả mang một khoảng, các giả định chính và một tuyên bố đơn giản về độ tin cậy.

5. **Ở đây thực sự an toàn để nói "dữ liệu không cho chúng ta biết" không, và ai được phép chất vấn cách một chỉ số được định nghĩa?** Chương coi hiểu biết dữ liệu và an toàn tâm lý là điều kiện tiên quyết: mọi người cần đọc biểu đồ phê phán, hỏi "làm sao chúng ta biết điều đó?", và thừa nhận độ bất định mà không bị phạt, nếu không văn hóa chế ra sự chắc chắn giả theo mặc định. Căng thẳng với một tổ chức lớn là hiểu biết rộng cần thời gian và ngân sách đào tạo thực, và chất vấn chỉ số được ưa thích của một người cấp cao có thể cảm thấy hại sự nghiệp, nên các con số chưa được xem xét đi lên mà không bị thách thức. Hãy mang bằng chứng về ai trong phòng thực sự chất vấn được định nghĩa và nguồn gốc của một chỉ số, và nhớ lại lần cuối ai đó được thưởng thay vì bị phạt vì cập nhật quan điểm hay báo cáo một thất bại có thông tin. Với các cơ quan doanh nghiệp và chính phủ, nơi một thước đo định nghĩa kém có thể thúc đẩy tài trợ hay báo cáo công khai, hãy nêu tường minh ai có tư cách chất vấn một chỉ số và bảo vệ họ khi họ dùng nó.

6. **Bạn bảo vệ các phân tích quan trọng chống thiên kiến dự đoán được thế nào, và bạn có xây bất đồng vào trước một quyết định thay vì sau nó không?** Chương liệt kê các cái bẫy lặng lẽ làm hỏng bằng chứng: thiên kiến xác nhận khi chọn dữ liệu ủng hộ, thiên kiến người sống sót khi bỏ qua điều bị thiếu, neo vào con số ban đầu, và thiên kiến nhận thức muộn trong rà soát sau sự cố. Cân nhắc đối lập là tốc độ, vì rà soát phản biện, đăng ký trước điều bạn kỳ vọng tìm thấy, và các góc nhìn đa dạng đều làm chậm quyết định và là những thứ đầu tiên bị cắt dưới áp lực hạn chót. Hãy mang một phân tích rủi ro cao gần đây và hỏi điều gì sẽ nổi lên nếu ai đó được giao tranh luận trường hợp ngược lại, và liệu đội có ghi lại kỳ vọng của mình trước khi thấy kết quả. Trong bối cảnh doanh nghiệp và đặc biệt chính phủ, nơi quyết định ảnh hưởng đến sinh kế, trợ cấp hay quyền của mọi người, hãy coi đạo đức dữ liệu và bất đồng có cấu trúc là yêu cầu thường trực với các phân tích hệ quả, không phải đồ phụ mà một quý bận rộn có thể lặng lẽ bỏ.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Không có nhà phân tích và chỉ vài tuần đường băng mỗi canh bạc, khoa học quyết định của bạn là một thói quen hơn là một chức năng: trước một cam kết lớn, hãy hỏi kết quả nào sẽ làm bạn đổi ý và liệu một thử nghiệm rẻ có trả lời nó nhanh hơn một cuộc họp. Đề phòng chặt việc đặt cược cả quý vào một tương quan hào nhoáng duy nhất, vì một đội nhỏ xíu không phục hồi nổi sau một lộ trình đi sai hướng. Giữ nó nhẹ, một dòng viết trong tài liệu quyết định nêu tín hiệu sẽ làm bạn dừng, không phải một cuộc rà soát chính thức bạn sẽ không bao giờ chạy.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia dữ liệu và mua phân tích bên trong các công cụ đã dùng, nên rủi ro là tin bảng điều khiển của nhà cung cấp mà không chất vấn một chỉ số được định nghĩa thế nào hay phép so sánh của nó có công bằng không. Hãy dành sự chú ý khan hiếm cho việc suy luận hơn là công cụ: tách tương quan khỏi nhân quả trong một hai quyết định thực sự dịch chuyển doanh nghiệp, và nêu khoảng trung thực cho chính mình trước khi cam kết tiền mặt bạn không lấy lại được. Khi một công cụ đề nghị tự động hóa một quyết định, hãy giữ một người trong vòng lặp bất cứ nơi nào một lựa chọn sai tốn của bạn một khách hàng.

**Doanh nghiệp lớn.** Qua nhiều đội, vấn đề là nhất quán và quản trị: một kỳ vọng dùng chung rằng các phân tích nêu quyết định và tiêu chí khai tử từ trước, các tuyên bố nhân quả nêu giả định, và các con số hệ quả mang khoảng vào hồ sơ hội đồng và kiểm toán. Hãy tách chỉ số học tập khỏi đánh giá hiệu suất toàn tổ chức để đo lường không biến chất thành giám sát và thao túng. Đầu tư vào hiểu biết dữ liệu rộng và vào các thực hành rà soát như phản biện và đăng ký trước, để một người thuyết trình tự tin không thay thế được bằng chứng ở quy mô.

**Chính phủ.** Mua sắm, minh bạch và trách nhiệm giải trình công nâng rủi ro của mọi tuyên bố nhân quả, vì một chính sách được biện minh bằng tương quan giả phân bổ sai tiền công và có thể hại công dân. Hãy ưu tiên thiết kế so sánh chặt chẽ cho đánh giá chương trình, truyền đạt hiệu ứng dưới dạng khoảng với giả định được nêu cho cơ quan giám sát, và lập tài liệu lập luận để kiểm toán theo dõi được. Hướng đo lường vào kết quả chương trình hơn là giám sát nhân viên xử lý hồ sơ, và trao cho công chúng một lời kể rõ ràng về cách bằng chứng định hình quyết định.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp trước Series A nhận thấy người dùng tham gia diễn đàn cộng đồng của mình rời bỏ ít hơn nhiều, và những người sáng lập sẵn sàng hướng toàn bộ lộ trình vào các tính năng diễn đàn. Trước khi cam kết, một người hỏi điều gì sẽ làm họ đổi ý, và một cái nhìn nhanh cho thấy khách hàng đã gắn bó chỉ đơn giản là những người chịu khó tham gia diễn đàn. Họ chạy một thử nghiệm nhỏ thay vì đặt cược cả quý vào một tương quan, và biến "điều gì sẽ làm chúng ta đổi ý?" thành câu hỏi chuẩn trong tài liệu quyết định.

**Doanh nghiệp lớn.** Một công ty dịch vụ tài chính nhận thấy khách hàng dùng một tính năng cụ thể có tỷ lệ rời bỏ thấp hơn nhiều và suýt ra mắt một chiến dịch tốn kém để đẩy mọi người vào nó. Một cuộc rà soát khoa học quyết định gắn cờ yếu tố gây nhiễu hiển nhiên: khách hàng đã gắn bó tự chọn vào tính năng. Một thử nghiệm có đối chứng sau đó cho thấy chính tính năng ít tác động nhân quả lên rời bỏ. Công ty tránh một khoản đầu tư lớn đi sai hướng, và ban lãnh đạo áp dụng "điều gì sẽ làm chúng ta đổi ý?" như câu hỏi chuẩn trước các khoản chi lớn.

**Chính phủ.** Một cơ quan công đánh giá một chương trình việc làm đã chống lại việc tuyên bố thành công từ thống kê thô rằng người tham gia tìm được việc với tỷ lệ cao, nhận ra rằng những người có động lực tự chọn vào các chương trình như vậy. Họ dùng thiết kế so sánh chặt chẽ và truyền đạt hiệu ứng ước lượng như một khoảng với giả định được nêu cho cơ quan giám sát. Đo lường tập trung vào kết quả chương trình thay vì giám sát nhân viên xử lý hồ sơ, giữ được lòng tin tuyến đầu mà vẫn thúc đẩy trách nhiệm giải trình và cải thiện.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của khoa học quyết định là chi phí tránh được của các quyết định sai tự tin và chất lượng được cải thiện của những quyết định một tổ chức đưa ra hàng nghìn lần. Một lựa chọn chiến lược hay chính sách lớn duy nhất được biện minh bằng tương quan giả có thể lãng phí hơn nhiều toàn bộ chi phí xây dựng thực hành quyết định tốt. Hiệu chuẩn tốt hơn (biết điều bạn biết và không biết) cho bạn định cỡ cược đúng và tránh cả cam kết liều lĩnh lẫn tê liệt. Gộp lại, một văn hóa dựa trên dữ liệu cộng dồn: mọi đội đưa ra quyết định tốt hơn một chút, được suy luận tốt hơn là đòn bẩy khổng lồ.

Chi phí áp dụng chủ yếu là văn hóa và giáo dục: đào tạo hiểu biết dữ liệu, thời gian cho phân tích và rà soát cẩn thận, và sự sẵn lòng của lãnh đạo thay đổi quyết định và thừa nhận độ bất định. Nó rẻ hơn về đô la so với các nền tảng của các chương trước nhưng khó cài đặt hơn, vì nó đòi những người có quyền lực bị bằng chứng chi phối. Hãy cân nhắc nó so với chi phí của việc không áp dụng: sân khấu dữ liệu lãng phí công sức phân tích, quyết định do giọng tự tin nhất thúc đẩy, tuyên bố nhân quả sụp đổ khi chạm thực tế, và, nơi giám sát bén rễ, một lực lượng lao động thao túng chỉ số và giấu tin xấu. Với ban lãnh đạo, lập luận đơn giản. Mọi khoản đầu tư dữ liệu trước đó chỉ sinh lời nếu dặm cuối từ hiểu biết đến quyết định vững chắc, và khoa học quyết định chính là dặm cuối đó.

## Phản mẫu và cạm bẫy

- Sân khấu dữ liệu: phân tích tạo ra để biện minh cho một quyết định đã đưa ra.
- Trượt từ "tương quan với" sang "gây ra" mà không chất vấn yếu tố gây nhiễu.
- Trình bày ước lượng điểm như sự chắc chắn, giấu khoảng bất định.
- Thiên kiến xác nhận: chỉ tìm dữ liệu ủng hộ một kết luận ưa thích.
- Quyết định kiểu HiPPO nơi ý kiến của người lương cao nhất đè lên bằng chứng.
- Biến chỉ số thành giám sát cá nhân, kích động thao túng và sợ hãi.
- Định luật Goodhart đang vận hành: một chỉ số mục tiêu thôi đo điều quan trọng.
- Phạt người vì thất bại có thông tin, giết chết sự trung thực và thử nghiệm.

## Mô hình trưởng thành

1. **Khởi đầu.** Quyết định chạy theo thứ bậc và trực giác, và giọng to nhất hoặc cấp cao nhất thắng. Tương quan được tự do coi là nhân quả, độ bất định bị phớt lờ, và vài chỉ số đang dùng giám sát cá nhân và bị thao túng.
2. **Phát triển.** Một số đội tham khảo dữ liệu và cho thấy nhận thức về các cái bẫy nhân quả, nhưng phân tích thường chọn lọc, tạo ra để biện minh cho quyết định đã đưa ra. Độ bất định hiếm khi được truyền đạt, và thực hành đo lường không nhất quán giữa các đội.
3. **Chuẩn hóa.** Tổ chức lập tài liệu và thực thi thực hành dùng chung: phân tích gắn với một quyết định có tên với tiêu chí xác định trước, các đội phân biệt tương quan với nhân quả và ưu tiên thử nghiệm cho tuyên bố nhân quả, các con số mang khoảng và giả định được nêu, và đo lường nhắm vào kết quả hơn là cá nhân, với an toàn tâm lý được bảo vệ.
4. **Quản lý.** Chất lượng quyết định được đo và kiểm soát theo đường cơ sở. Tổ chức theo dõi bao lần phân tích nêu một tín hiệu khai tử trước khi dữ liệu đến, tỷ lệ các con số hệ quả được phát hành kèm khoảng được truyền đạt, bao nhiêu tuyên bố nhân quả dựa trên thử nghiệm so với tương quan trần, và liệu quyết định có đảo ngược theo bằng chứng. Thực hành bảo vệ chống thiên kiến như đăng ký trước và rà soát phản biện được kiểm toán, và các chỉ số bắt đầu bị thao túng được bắt và cho nghỉ hưu.
5. **Điều phối.** Suy luận vững chắc được cải thiện liên tục và tích hợp trong toàn tổ chức. "Điều gì sẽ làm chúng ta đổi ý?" là thường lệ trước bất kỳ quyết định lớn nào, sự chặt chẽ nhân quả và độ bất định trung thực là chuẩn mực văn hóa, và lãnh đạo cập nhật rõ ràng theo bằng chứng và thừa nhận điều chưa biết. Đo lường thúc đẩy học tập mà không giám sát, thực hành quyết định thích ứng khi tổ chức và rủi ro của nó dịch chuyển, và mọi cấp quyết định tốt hơn nhờ đó.

## Ý tưởng để thảo luận

- Dữ liệu được dùng để trang trí các quyết định đã đưa ra ở đâu trong tổ chức của bạn?
- Quyết định gần đây nào dựa trên một tương quan có thể không phải nhân quả?
- Báo cáo của bạn truyền đạt độ bất định trung thực đến đâu, và ai chống lại khoảng?
- Chỉ số của bạn nhắm vào cải thiện hệ thống hay giám sát cá nhân?
- Lần cuối một nhà lãnh đạo rõ ràng đổi quyết định vì dữ liệu là khi nào?
- Làm sao bạn giữ cho việc theo đuổi đo lường không nghiêng sang giám sát?

## Những điểm cần ghi nhớ

- Mục đích của dữ liệu là quyết định tốt hơn; đề phòng sân khấu dữ liệu.
- Hãy nêu điều sẽ làm bạn đổi ý trước khi nhìn dữ liệu.
- Đừng bao giờ nhầm tương quan với nhân quả; chất vấn yếu tố gây nhiễu và ưu tiên thử nghiệm.
- Truyền đạt độ bất định trung thực; độ chính xác giả phá hủy lòng tin khi nó thất bại.
- Hãy dựa trên dữ liệu, không bị dữ liệu nô lệ hóa; phán đoán và ngữ cảnh vẫn quan trọng.
- Đo hệ thống và kết quả để học, không đo cá nhân để giám sát.
- Bảo vệ an toàn tâm lý để mọi người cập nhật niềm tin và nêu tin xấu.

## Tài liệu tham khảo và đọc thêm

- Daniel Kahneman, "Thinking, Fast and Slow."
- Judea Pearl và Dana Mackenzie, "The Book of Why."
- Douglas W. Hubbard, "How to Measure Anything."
- Nate Silver, "The Signal and the Noise."
- Cathy O'Neil, "Weapons of Maths Destruction."
- Darrell Huff, "How to Lie with Statistics."
- Philip Tetlock và Dan Gardner, "Superforecasting."
- Charles Wheelan, "Naked Statistics."
