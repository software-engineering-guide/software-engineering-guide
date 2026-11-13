# 10.6 Quản lý dự án

## Tổng quan và động lực

[Quản lý dự án](https://en.wikipedia.org/wiki/Project_management) là kỷ luật biến ý định thành kết quả được giao dưới các ràng buộc. Bạn phối hợp con người, phạm vi, lịch trình, chi phí, rủi ro và chất lượng để công việc thực sự hoàn tất và mang lại giá trị. Trong phần mềm nó thường bị nhìn với sự nghi ngờ, gắn với những kế hoạch nặng nề và [biểu đồ Gantt](https://en.wikipedia.org/wiki/Gantt_chart) mà thực tế phớt lờ. Nhưng nhu cầu nền tảng không bao giờ biến mất. Ai đó phải bảo đảm đúng công việc diễn ra theo đúng thứ tự, phụ thuộc được quản lý, rủi ro nổi lên sớm, và [các bên liên quan](https://en.wikipedia.org/wiki/Project_stakeholder) biết điều cần kỳ vọng. Câu hỏi không phải *có* nên quản lý dự án hay không, mà là bạn có thể làm điều đó *nhẹ nhàng và thích ứng* đến đâu mà vẫn đáp ứng nghĩa vụ của mình.

Vì sao coi điều này tường minh? Các dự án phần mềm thất bại ở tỷ lệ đáng báo động, và chúng thất bại vì lý do quản lý thường xuyên hơn nhiều so với lý do thuần kỹ thuật: phạm vi không rõ, phụ thuộc không được quản lý, rủi ro không được xử lý, các bên liên quan vắng mặt, và ảo tưởng về ước lượng dài hạn chính xác. Các chương trình lớn đặc biệt dễ bị tổn thương: với nhiều đội, nhà cung cấp và chân trời nhiều quý, những thất bại phối hợp nhỏ cộng dồn. Quản lý dự án tốt phần lớn là thực hành đưa ra cam kết trung thực, chia nhỏ công việc hợp lý, và tạo phản hồi nhanh để vấn đề nổi lên khi còn rẻ để sửa.

Bối cảnh doanh nghiệp và chính phủ nâng rủi ro và đổi ràng buộc. Doanh nghiệp quản lý danh mục các sáng kiến đan xen so với chiến lược và chu kỳ ngân sách (chương 10.1). Chính phủ thêm quy tắc mua sắm, phân bổ ngân sách nhiều năm, quản lý nhà thầu và trách nhiệm giải trình công. Ở đó, mặc định lịch sử (hợp đồng [thác nước](https://en.wikipedia.org/wiki/Waterfall_model) lớn, phạm vi cố định) có thành tích dài về thất bại đắt đỏ, dễ thấy. Chương này bao quát những nền tảng áp dụng qua các cách tiếp cận dự đoán, thích ứng và lai. Chương 10.7 (Agile) đi sâu vào phân phối thích ứng, và chương 10.1 bao quát quản lý danh mục và chương trình ở trên một dự án đơn lẻ.

## Các nguyên tắc chính

- **Quản lý kết quả, không phải hoạt động.** Xong nghĩa là giá trị được giao, không phải nhiệm vụ được đóng.
- **Phân rã và sắp thứ tự.** Công việc nhỏ, có thứ tự, nhận biết phụ thuộc thắng kế hoạch đại bùng nổ.
- **Ước tính là khoảng, không phải lời hứa.** Truyền đạt độ bất định một cách trung thực.
- **Làm lộ rủi ro sớm và liên tục.** Vấn đề rẻ nhất là vấn đề được bắt đầu tiên.
- **Khớp phương pháp với công việc.** Dự đoán, thích ứng hay lai: hãy khớp độ bất định và ràng buộc.
- **Làm trạng thái minh bạch.** Luồng hiển thị thắng báo cáo trấn an.
- **Các bên liên quan là một phần của đội.** Sự vắng mặt của khách hàng là rủi ro dự án.

## Khuyến nghị

### Chọn dự đoán, thích ứng hay lai có chủ đích

Không có mô hình phân phối đúng phổ quát; có sự khớp giữa phương pháp và ngữ cảnh:

- **Dự đoán (dẫn dắt bởi kế hoạch, "thác nước"):** phạm vi cố định từ đầu, rồi lịch trình và chi phí được suy ra. Phù hợp với công việc có yêu cầu thực sự ổn định, được hiểu rõ và ràng buộc bên ngoài cứng (chứng nhận quy định, tích hợp vật lý). Kiểu thất bại của nó là giả vờ yêu cầu phần mềm ổn định khi chúng không phải vậy.
- **Thích ứng ([agile](https://en.wikipedia.org/wiki/Agile_software_development)):** phạm vi co giãn; thời gian và chi phí cố định trong các vòng lặp ngắn giao phần mềm hoạt động và hấp thụ việc học. Phù hợp với hầu hết công việc sản phẩm và dịch vụ số, nơi yêu cầu được khám phá (chương 11.1, 10.7).
- **Lai:** một lõi thích ứng bên trong vỏ quản trị dự đoán, phổ biến và thường đúng trong doanh nghiệp và chính phủ, nơi tài trợ, tuân thủ và hợp đồng đòi cột mốc và kiểm toán trong khi phân phối hưởng lợi từ lặp.

Các khung như [PMBOK](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) (Bộ tri thức Quản lý Dự án, từ [Viện Quản lý Dự án](https://en.wikipedia.org/wiki/Project_Management_Institute)) và [PRINCE2](https://en.wikipedia.org/wiki/PRINCE2) (PRojects IN Controlled Environments) mã hóa thực hành dự đoán và lai. Điểm mấu chốt là mượn kỷ luật của chúng (vai trò, rủi ro, cổng giai đoạn) mà không nhập nghi thức công việc không cần.

### Quản lý phạm vi theo ràng buộc tam giác

Phạm vi, lịch trình và chi phí di chuyển cùng nhau, bị chặn bởi chất lượng: ["tam giác sắt"](https://en.wikipedia.org/wiki/Project_management_triangle) kinh điển. Bạn không thể cố định cả ba và thêm phạm vi miễn phí. Có thứ phải nhường, và giả vờ khác đi là cách [cuộc hành quân tử thần](https://en.wikipedia.org/wiki/Death_march_(project_management)) bắt đầu. Hãy làm các đánh đổi tường minh, và quyết định biến số *nào* co giãn. Phương pháp thích ứng cố định thời gian và chi phí và co giãn phạm vi. Hợp đồng giá cố định cố định phạm vi và chi phí, và thực tế co giãn chất lượng hoặc lịch trình trừ khi bạn quản lý chúng. Kiểm soát [phình phạm vi](https://en.wikipedia.org/wiki/Scope_creep) bằng quy trình thay đổi nhẹ (chương 12.3), và ưu tiên *thu hẹp phạm vi về lõi có giá trị* hơn là trượt mọi thứ.

### Ước lượng trung thực, theo khoảng, và dự báo lại

Ước lượng là nơi các dự án thường nói dối chính mình nhất. Hãy coi ước tính là khoảng xác suất, không phải con số đơn, và mở rộng chúng cho công việc xa, ít được hiểu (["hình nón bất định"](https://en.wikipedia.org/wiki/Cone_of_Uncertainty)). Ưu tiên phương pháp tương đối và thực nghiệm: thông lượng và thời gian chu kỳ lịch sử (chương 11.2, 11.3) dự báo tốt hơn những phỏng đoán từ dưới lên đầy anh hùng. Nơi có thể, hãy thay ước lượng bằng *đo lường*. Một đội đóng 8 mục mỗi tuần sẽ mất khoảng 5 tuần cho 40 mục, bất kể điểm story ([Định luật Little](https://en.wikipedia.org/wiki/Little%27s_law) một lần nữa: thông lượng và công việc đang làm, không phải ước tính, đặt thời gian giao). Dự báo lại liên tục khi thực tế đến. Một kế hoạch không bao giờ đổi không đang được quản lý.

### Quản lý phụ thuộc và đường găng

Ở quy mô, rủi ro chi phối hiếm khi là vận tốc của một đội. Đó là *các phụ thuộc giữa đội và nhà cung cấp*. Hãy lập bản đồ chúng tường minh, xác định [đường găng](https://en.wikipedia.org/wiki/Critical_path_method) (chuỗi quyết định thời điểm kết thúc sớm nhất), và tấn công các phụ thuộc dài nhất và rủi ro nhất trước. Giảm ghép nối nơi có thể (một phụ thuộc bị loại bỏ có giá trị hơn một phụ thuộc được theo dõi) và dùng giao diện và hợp đồng rõ ràng để các đội tiến triển song song (chương 1.2, 2.3). Với chương trình xuyên đội, một buổi đồng bộ phụ thuộc và rủi ro đều đặn thắng báo cáo trạng thái không ai đọc.

### Chạy sổ đăng ký rủi ro sống

Quản lý rủi ro là hoạt động quản lý dự án có đòn bẩy cao nhất, và thường bị bỏ qua nhất. Hãy giữ một **[sổ đăng ký rủi ro](https://en.wikipedia.org/wiki/Risk_register)** đơn giản, sống: mỗi rủi ro với khả năng, tác động, chủ sở hữu, và biện pháp giảm thiểu hay dự phòng (chương 12.3). Xem xét nó đều đặn, cho nghỉ hưu những rủi ro đã qua, và thêm cái mới khi chúng xuất hiện. Phân biệt rủi ro (có thể xảy ra) với vấn đề (đang xảy ra) và quyết định (chương 1.6). Mục tiêu không phải một tài liệu. Đó là thói quen nhìn về phía trước, để bạn dự đoán vấn đề thay vì phát hiện chúng ở hạn chót.

### Tham gia các bên liên quan và truyền đạt minh bạch

Hầu hết thất bại dự án "bất ngờ" đã thấy sớm bởi ai đó không được lắng nghe. Hãy xác định các bên liên quan, hiểu mối quan tâm của họ, và giữ họ thực sự tham gia. Sự vắng mặt của khách hàng tự nó là rủi ro hàng đầu. Truyền đạt trạng thái qua *luồng minh bạch* (bảng hiển thị, biểu đồ burn-up, phần mềm hoạt động được trình diễn) thay vì báo cáo xanh-vàng-đỏ thưởng cho sự lạc quan. Leo thang trung thực và sớm. Một dự án vận hành tốt khiến tin xấu đi nhanh.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Dự đoán / thác nước** | Phạm vi và chi phí khả đoán; thân thiện hợp đồng và kiểm toán | Khớp kém với yêu cầu bất định; phản hồi muộn; rủi ro đại bùng nổ |
| **Thích ứng / agile** | Phản hồi nhanh; hấp thụ thay đổi; giá trị sớm | Khó cố định phạm vi/chi phí từ đầu; cần khách hàng tham gia |
| **Lai** | Lặp bên trong quản trị; khớp doanh nghiệp/chính phủ | Căng thẳng giữa các nhịp; có thể thừa hưởng cả hai bộ chi phí chung |
| **Ước tính chi tiết từ đầu** | Thoải mái cho người hoạch định và nhà tài trợ | Sai một cách chính xác; tốn kém để tạo; phai nhanh |
| **Dự báo thực nghiệm (chỉ số luồng)** | Có cơ sở, tự hiệu chỉnh | Cần lịch sử và kỷ luật; trông kém "chắc chắn" |
| **Nghi thức rủi ro/quy trình nặng** | Kỹ lưỡng; tốt cho chương trình hệ trọng | Làm chậm đội nhỏ; có thể thành đánh dấu ô |

Căng thẳng trung tâm là **khả năng dự đoán so với khả năng thích ứng**. Nhà tài trợ, hợp đồng và kiểm toán muốn cam kết vững chắc. Công việc phần mềm bất định cần chỗ để học. Hãy giải quyết như Agile làm (chương 10.7): cam kết vững chắc với kết quả và hạn chót trong khi để phạm vi co giãn, và dùng quản trị lai để thỏa mãn giám sát mà không đóng băng phân phối.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn sẽ bọc các đội phân phối thích ứng trong vỏ quản trị dự đoán thế nào mà không thừa hưởng chi phí chung của cả hai?** Lai là phổ biến và thường đúng trong doanh nghiệp và chính phủ, nơi chu kỳ tài trợ, tuân thủ và hợp đồng đòi cột mốc và kiểm toán trong khi phân phối hưởng lợi từ lặp. Rủi ro là thật: một mô hình lai thiết kế tệ thừa hưởng tài liệu nặng của thác nước và nghi thức của agile cùng lúc, và các đội cảm nhận ma sát của hai nhịp đánh nhau. Hãy mang bằng chứng: lập bản đồ nơi các cổng tài trợ, điểm kiểm tuân thủ và cột mốc hợp đồng thực sự rơi, và kiểm tra liệu mỗi cái có đòi một tài liệu mà công việc phân phối không tạo ra không. Câu trả lời nên để lặp thỏa mãn giám sát thay vì chống lại nó, bằng cách đưa các phần tăng trưởng hoạt động được trình diễn và sổ đăng ký rủi ro sống vào nhịp quản trị thay vì dừng lại để lắp báo cáo riêng. Hãy mượn kỷ luật của một khung như PRINCE2 mà không nhập nghi thức công việc không cần.

2. **Trạng thái dự án của bạn là luồng minh bạch, hay báo cáo xanh-vàng-đỏ thưởng cho sự lạc quan?** Hầu hết thất bại bất ngờ đã thấy sớm bởi ai đó không được lắng nghe, và trạng thái dưa hấu (xanh bên ngoài, đỏ bên trong) là cách tin xấu trung thực bị chôn đến hạn chót. Hãy thay báo cáo trấn an bằng bảng hiển thị, biểu đồ burn-up và phần mềm hoạt động được trình diễn, và làm leo thang sớm thành hành động an toàn thay vì rủi ro sự nghiệp. Hãy mang bằng chứng: nhìn dự án gặp khó gần nhất của bạn và hỏi dấu hiệu cảnh báo đầu tiên tồn tại khi nào so với khi lãnh đạo nghe thấy. Sự vắng mặt của khách hàng tự nó là rủi ro hàng đầu, nên hãy kiểm tra liệu một bên liên quan tham gia có thực sự trong vòng lặp hay bạn đang xây tự tin về phía sai. Một dự án vận hành tốt khiến tin xấu đi nhanh, và cách sửa là văn hóa nhiều như công cụ.

3. **Bạn có biết lõi giá trị tối thiểu mà bạn sẽ thu hẹp về nếu lịch trình và chi phí ngừng dịch chuyển không?** Phạm vi, lịch trình và chi phí di chuyển cùng nhau bị chặn bởi chất lượng, và khi nhà tài trợ cố định cả ba, chất lượng thành van xả im lặng và các cuộc hành quân tử thần bắt đầu. Phương pháp thích ứng cố định thời gian và chi phí và co giãn phạm vi, điều chỉ hiệu quả nếu bạn đã quyết định lát cắt nào giao giá trị thật và tính năng nào thương lượng được. Hãy mang bằng chứng: với bản phát hành hiện tại, bạn có nêu được lõi phải phát hành và danh sách bạn sẽ cắt đầu tiên, hay mọi tính năng đang lặng lẽ bị coi là bắt buộc? Câu trả lời nên cho phép bạn thu hẹp về lõi có giá trị thay vì trượt mọi thứ, và nó nên được giải quyết trước khi áp lực đến, không phải ứng biến ở hạn chót. Kiểm soát phần còn lại bằng quy trình thay đổi nhẹ để phình phạm vi không ăn mất biên bạn đang tính đến.

4. **Phụ thuộc xuyên đội nào đang nằm trên đường găng của bạn ngay bây giờ, và ai sở hữu việc loại bỏ hay giảm rủi ro cho nó?** Ở quy mô, mối đe dọa chi phối hiếm khi là vận tốc của một đội; đó là chuỗi phụ thuộc giữa đội và nhà cung cấp đặt thời điểm kết thúc sớm nhất có thể. Nếu không ai nêu được phụ thuộc đường găng hiện tại, bạn đang quản lý tiến độ cục bộ trong khi thứ thực sự chi phối ngày của bạn trôi không ai canh. Hãy mang bằng chứng: bản đồ phụ thuộc cho thấy bàn giao nào nuôi bàn giao nào, chuỗi dài nhất chạy ở đâu, và mắt xích nào còn chưa được xây hoặc bị chặn bởi hợp đồng, cộng một chủ sở hữu có tên cho mỗi mắt xích rủi ro. Hãy nhắm tấn công các phụ thuộc dài nhất và rủi ro nhất trước và loại bỏ ghép nối nơi có thể, vì một phụ thuộc bị xóa có giá trị hơn một phụ thuộc được theo dõi. Trong chương trình doanh nghiệp và chính phủ, mắt xích khó nhất thường vượt ranh giới nhà cung cấp hoặc cơ quan, nên hãy nêu chủ sở hữu chịu trách nhiệm ở mỗi bên và xác nhận hợp đồng cho phép họ hành động, nếu không phụ thuộc sẽ nằm không giải quyết cho đến khi thành chậm trễ công khai.

5. **Bạn dự báo lại thế nào khi thực tế đến, và một độ trượt trở nên hiển thị nhanh đến đâu với những người tài trợ công việc?** Một kế hoạch không bao giờ đổi không được quản lý; nó đang được bảo vệ, và một ngày con số đơn được bảo vệ quá bằng chứng là cách dự án trượt trong im lặng đến hạn chót. Hãy thay ước lượng bằng đo lường nơi có thể, dự báo từ thông lượng và thời gian chu kỳ lịch sử thay vì phỏng đoán từ dưới lên đầy anh hùng, và mở rộng khoảng cho công việc xa, ít được hiểu. Hãy mang bằng chứng: tốc độ hoàn thành thực hằng tuần của bạn, kích thước tồn đọng hiện tại, và ngày kết thúc dự phóng rút ra từ chúng, so với ngày lãnh đạo hiện đang tin. Câu trả lời nên trao cho nhà tài trợ một dự phóng trung thực, thu hẹp dần mà họ thấy mỗi chu kỳ thay vì ngày cố định giữ đến khi sụp. Trong chính phủ và các bối cảnh bị ràng buộc bởi phân bổ ngân sách khác, một dự báo làm lộ độ trượt sớm cho phép bạn thu hẹp phạm vi hay đặt lại đường cơ sở trong quy tắc, trong khi một độ trượt bị giấu thành thất bại giám sát và tiêu đề báo.

6. **Quy trình nhẹ nhất mà vẫn đáp ứng nghĩa vụ thật của bạn là gì, và nghi thức đã tách khỏi việc giảm rủi ro ở đâu?** Cả quản lý thiếu lẫn quản lý thừa đều mang chi phí thật: hỗn loạn, làm lại và phụ thuộc bị bỏ sót một bên, và đánh dấu ô làm chậm phân phối mà không giảm rủi ro bên kia. Căng thẳng là kiểm toán, tuân thủ và điều khoản hợp đồng áp đặt yêu cầu thật, vậy mà các đội có xu hướng giữ mọi nghi thức rất lâu sau khi chúng thôi xứng đáng chỗ của mình. Hãy mang bằng chứng: với mỗi báo cáo, cổng và cuộc họp lặp lại, nêu nghĩa vụ hay rủi ro cụ thể nó giải quyết, và gắn cờ những cái không ai truy được về cả hai. Câu trả lời nên cho phép bạn cho nghỉ hưu nghi thức chỉ tạo sự trấn an trong khi bảo tồn các hiện vật thỏa mãn kiểm toán viên hay nhà tài trợ thật. Trong bối cảnh doanh nghiệp và chính phủ, hãy ánh xạ mỗi nghi thức đến quy tắc phân bổ ngân sách, mua sắm hay quản lý có tên mà nó phục vụ, để bạn bảo vệ việc cắt phần còn lại trước giám sát thay vì đoán tuân thủ đòi gì.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy quản lý với gần như không có nghi thức nhưng kỷ luật thật. Chia bản phát hành thành các lát nhỏ có thứ tự, cam kết một ngày ra mắt trong khi để phạm vi co giãn về lõi có giá trị, và báo với những người sáng lập một khoảng thay vì ngày đơn, dự báo lại hằng tuần từ số lát bạn thực sự đóng. Một sổ đăng ký rủi ro mười dòng trong tài liệu chung nêu phụ thuộc duy nhất có thể đánh chìm ngày, với chủ sở hữu và phương án dự phòng, đáng giá hơn bất kỳ công cụ nào, vì nguồn lực khan hiếm nhất của bạn là sự chú ý và một độ trượt bạn phát hiện muộn có thể kết thúc công ty.

**Doanh nghiệp nhỏ.** Bạn không có quản lý dự án và ít dư địa, nên hãy dựa vào công cụ bạn đã chạy thay vì dựng văn phòng quản trị. Theo dõi công việc trên một bảng hiển thị, giữ một danh sách rủi ro sống ngắn, và ưu tiên mua một sản phẩm lập lịch hay phiếu thay vì xây quy trình từ đầu. Hãy quyết định từ trước tính năng duy nhất nào phải phát hành để bản phát hành đáng làm, vì khi lịch trình thắt lại bạn sẽ không có người dư để thương lượng phạm vi ngay lúc đó.

**Doanh nghiệp lớn.** Vấn đề là phối hợp qua nhiều đội, nhà cung cấp và chu kỳ tài trợ. Hãy bọc các đội thích ứng trong vỏ quản trị dự đoán, đưa các phần tăng trưởng được trình diễn và sổ đăng ký rủi ro sống vào nhịp cột mốc thay vì lắp báo cáo riêng, và duy trì bản đồ phụ thuộc xuyên đội để đường găng được quản lý thay vì được khám phá. Chuẩn hóa ước tính theo khoảng, dự báo lại bằng thực nghiệm qua danh mục để lãnh đạo so sánh các dự án trên các dự phóng trung thực, thu hẹp dần thay vì những ngày cố định lạc quan.

**Chính phủ.** Quy tắc mua sắm, phân bổ ngân sách nhiều năm và trách nhiệm giải trình công định hình mọi lựa chọn. Ưu tiên các phần tăng trưởng mô-đun, dựa trên kết quả được giao theo cách thích ứng dưới khung quản trị thỏa mãn phân bổ ngân sách và giám sát, hơn là một hợp đồng thác nước giá cố định, phạm vi cố định với ngày vận hành xa. Sổ đăng ký rủi ro sống và các phần tăng trưởng minh bạch, được trình diễn cho kiểm toán viên và nhà lập pháp khả năng nhìn thấy thật, và co giãn phạm vi về lõi có giá trị trong tài trợ cố định cho phép bạn phát hành năng lực hữu ích sớm thay vì đặt cược mọi thứ vào một ngày.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bảy người chạy đua phát hành sản phẩm trả phí đầu tiên quản lý dự án với gần như không có nghi thức nhưng kỷ luật thật. Nó chia bản phát hành thành các lát nhỏ có thứ tự, cam kết một ngày ra mắt trong khi để phạm vi co giãn về lõi có giá trị thay vì hứa mọi tính năng, và báo với những người sáng lập một khoảng thay vì ngày đơn, dự báo lại hằng tuần từ số lát đội thực sự đóng. Một sổ đăng ký rủi ro mười dòng trong tài liệu chung nêu phụ thuộc duy nhất có thể đánh chìm ngày, một tích hợp thanh toán chưa hoàn tất, với chủ sở hữu và phương án dự phòng, nên mối đe dọa lớn nhất được canh thay vì được phát hiện ở hạn chót.

**Doanh nghiệp lớn.** Một ngân hàng thay nền tảng khởi tạo khoản vay chạy chương trình lai: một vỏ dự đoán với cột mốc tài trợ hằng quý và cổng tuân thủ, bọc các đội thích ứng giao các phần tăng trưởng hoạt động mỗi hai tuần. Một bản đồ phụ thuộc xuyên đội làm lộ rằng một dịch vụ danh tính dùng chung nằm trên đường găng. Vì vậy chương trình xếp nó đầu tiên và giảm rủi ro cho nó, tránh một thác đổ muộn. Ước tính được diễn đạt dưới dạng khoảng và dự báo lại hằng tháng từ thông lượng thực, nên lãnh đạo thấy dự phóng trung thực, thu hẹp dần thay vì ngày cố định lặng lẽ trượt.

**Chính phủ.** Một cơ quan bỏ hợp đồng thác nước giá cố định, phạm vi cố định duy nhất (mô hình đằng sau nhiều thất bại công) để chuyển sang mua sắm mô-đun: các phần tăng trưởng nhỏ hơn, dựa trên kết quả được giao theo cách thích ứng dưới khung quản trị thỏa mãn phân bổ ngân sách và giám sát. Sổ đăng ký rủi ro sống và các phần tăng trưởng minh bạch, được trình diễn cho kiểm toán viên và nhà lập pháp khả năng nhìn thấy thật. Vì phạm vi co giãn về lõi có giá trị trong tài trợ cố định, chương trình có thể phát hành năng lực hữu ích sớm thay vì đặt cược mọi thứ vào một ngày vận hành xa (chương 10.1, 10.3).

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của quản lý dự án tốt bị chi phối bởi **thất bại tránh được**. Các dự án phần mềm lớn dễ trễ, vượt ngân sách hoặc bị hủy hơn là đạt kế hoạch cố định ban đầu, và tổn thất rất lớn: chi phí chìm, cộng giá trị bị bỏ lỡ, cộng, trong chính phủ, thiệt hại công khai và chính trị. Các kỷ luật ở đây (ước lượng trung thực, quản lý phụ thuộc, công việc rủi ro sớm, các bên liên quan tham gia và phạm vi thích ứng) chính xác là những kỷ luật đưa một dự án ra khỏi đường cong thất bại. Ngay cả một mức cắt khiêm tốn xác suất vượt chi lớn hay hủy bỏ cũng lấn át chi phí quản lý dự án tốt.

Về **tổng chi phí sở hữu**, quản lý nhẹ, thích ứng hạ chi phí qua vòng đời công việc. Phản hồi nhanh bắt lỗi đắt tiền sớm. Phân phối gia tăng bắt đầu trả giá trị sớm hơn, cải thiện thời điểm ROI. Luồng minh bạch giảm chi phí chung báo cáo mà quản trị nặng áp đặt. Cả quản lý *thiếu* (hỗn loạn, làm lại, phụ thuộc bị bỏ sót) lẫn quản lý *thừa* (nghi thức làm chậm phân phối) đều mang chi phí thật. Mục tiêu là quy trình nhẹ nhất đáp ứng nghĩa vụ thật của bạn. Hãy lập luận với ban lãnh đạo bằng cách đối chiếu chi phí đầy đủ của một dự án gặp khó gần đây với chi phí gần như bằng không của một sổ đăng ký rủi ro, một bản đồ phụ thuộc và những dự báo theo khoảng trung thực.

## Phản mẫu và cạm bẫy

- **Kế hoạch cố định mọi thứ:** phạm vi, lịch trình và chi phí đều bị khóa, với chất lượng là van xả im lặng.
- **Ước tính như lời hứa:** ngày con số đơn bị coi là cam kết, rồi được bảo vệ quá bằng chứng.
- **Phớt lờ phụ thuộc:** quản lý vận tốc từng đội trong khi đường găng xuyên đội trượt.
- **Sân khấu sổ đăng ký rủi ro:** một tài liệu được tạo một lần và không bao giờ xem lại.
- **Trạng thái dưa hấu:** xanh bên ngoài, đỏ bên trong; sự lạc quan được thưởng hơn sự trung thực.
- **Khách hàng vắng mặt:** không có bên liên quan tham gia, nên thứ sai được xây một cách tự tin.
- **Phân phối đại bùng nổ:** mọi thứ được tích hợp và phát hành ở cuối, tối đa hóa rủi ro (đối chiếu chương 11.2).
- **Quy trình vì chính nó:** nghi thức và báo cáo tiêu tốn công sức mà không giảm rủi ro.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** Dự án chạy bằng anh hùng chủ nghĩa và hy vọng; phạm vi, rủi ro và phụ thuộc được quản lý tùy nghi nếu có; ước tính là con số đơn được bảo vệ quá bằng chứng; bất ngờ đến ở hạn chót.
- **Mức 2 (Phát triển):** Hoạch định cơ bản, báo cáo trạng thái và danh sách rủi ro tồn tại ở một số dự án mà không phải các dự án khác; phương pháp phân phối được chọn theo thói quen thay vì độ khớp; ước lượng và theo dõi phụ thuộc khác nhau theo đội, nên thực hành không nhất quán trong tổ chức.
- **Mức 3 (Chuẩn hóa):** Một cách tiếp cận có tài liệu được thực thi toàn tổ chức: phương pháp phân phối được chọn để khớp công việc, phạm vi được quản lý theo ràng buộc tam giác, sổ đăng ký rủi ro sống và bản đồ phụ thuộc được kỳ vọng ở mọi dự án, và ước tính theo khoảng và được dự báo lại với các bên liên quan tham gia.
- **Mức 4 (Quản lý):** Phân phối được đo và kiểm soát theo đường cơ sở. Thông lượng, thời gian chu kỳ, độ chính xác dự báo, tỷ lệ đóng phụ thuộc và rủi ro, và phương sai lịch trình và chi phí được theo dõi cho từng dự án và gộp lên qua danh mục; dự phóng là thực nghiệm và thu hẹp dần; độ trượt nổi lên sớm và kích hoạt thu hẹp phạm vi hay đặt lại đường cơ sở dựa trên bằng chứng thay vì lạc quan.
- **Mức 5 (Điều phối):** Quản lý dự án được tích hợp với hoạch định danh mục, tài trợ và rủi ro và được cải thiện liên tục. Quản trị lai thỏa mãn giám sát mà không làm chậm phân phối, phụ thuộc xuyên đội và xuyên nhà cung cấp được quản lý chủ động, các buổi nhìn lại đưa thay đổi đã đo ngược vào thực hành, và tổ chức thích ứng phương pháp và cân bằng lại công việc khi ràng buộc và ưu tiên dịch chuyển.

## Ý tưởng để thảo luận

1. Phương pháp phân phối nào (dự đoán, thích ứng, lai) mỗi sáng kiến hiện tại của bạn thực sự cần, và nó có khớp với cái bạn đang dùng không?
2. Lần cuối bạn cam kết một ngày, đó là khoảng hay con số đơn, và điều đó định hình kỳ vọng thế nào?
3. Phụ thuộc đường găng qua các đội của bạn lúc này là gì, và ai sở hữu việc giảm rủi ro cho nó?
4. Sổ đăng ký rủi ro của bạn là thói quen sống hay tài liệu một lần?
5. Chất lượng đang lặng lẽ hấp thụ áp lực ở đâu khi phạm vi, lịch trình và chi phí đều cố định?
6. Dự báo của bạn sẽ đổi thế nào nếu bạn thay ước lượng bằng thông lượng đo được?

## Những điểm cần ghi nhớ

- Quản lý dự án biến ý định thành kết quả được giao dưới ràng buộc phạm vi-lịch trình-chi phí-chất lượng.
- **Khớp phương pháp với công việc:** dự đoán, thích ứng hay lai, và ưu tiên quản trị lai trong doanh nghiệp/chính phủ.
- Coi **ước tính là khoảng**, dự báo lại từ **chỉ số luồng thực nghiệm**, và đừng để ngày con số đơn thành lời nói dối.
- **Phụ thuộc và rủi ro** là kiểu thất bại chi phối ở quy mô: hãy lập bản đồ và quản lý cả hai liên tục.
- Giữ **các bên liên quan tham gia** và trạng thái **minh bạch**; làm tin xấu đi nhanh.
- ROI là thất bại tránh được; quy trình nhẹ nhất đáp ứng nghĩa vụ của bạn thắng. Xem các chương 10.7 (Agile), 10.1 (quản lý danh mục và chương trình), 11.2 (phân phối) và 11.3 (lý thuyết hàng đợi).

## Tài liệu tham khảo và đọc thêm

- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*.
- AXELOS, *Managing Successful Projects with PRINCE2*.
- Frederick Brooks, *The Mythical Man-Month* (vì sao thêm người vào dự án trễ làm nó trễ hơn).
- Tom DeMarco và Timothy Lister, *Peopleware* và *Waltzing with Bears* (quản lý rủi ro).
- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* (dự báo thực nghiệm).
- Standish Group, *CHAOS Report* (kết quả dự án phần mềm, đọc có phê phán).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard* (phân phối khu vực công hiện đại).
- Bent Flyvbjerg và Dan Gardner, *How Big Things Get Done* (phân phối siêu dự án).
