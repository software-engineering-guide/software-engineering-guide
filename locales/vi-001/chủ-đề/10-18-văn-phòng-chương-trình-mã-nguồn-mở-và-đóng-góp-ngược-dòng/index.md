# 10.18 Văn phòng chương trình mã nguồn mở (OSPO) và đóng góp ngược dòng

## Tổng quan và động lực

Tổ chức của bạn đã chạy trên [phần mềm nguồn mở](https://en.wikipedia.org/wiki/Open-source_software): hệ điều hành, ngôn ngữ, cơ sở dữ liệu và thư viện mang sản phẩm của bạn phần lớn do những người không làm việc cho bạn viết. Chương 10.3 bao quát mua sắm và tuân thủ giấy phép, và chương 10.12 bao quát quyết định mở-so-với-đóng. Chương này nói về chức năng làm tất cả những điều đó mạch lạc: một [văn phòng chương trình mã nguồn mở](https://en.wikipedia.org/wiki/Open_Source_Program_Office) (OSPO), đội sở hữu cách công ty tiêu thụ, đóng góp cho và phát hành mã nguồn mở. Một OSPO là trọng tâm cho một mối quan hệ vốn rải qua mọi kỹ sư gõ `import`.

Hầu hết tổ chức bước vào mã nguồn mở từng phụ thuộc một, rồi phát hiện phơi nhiễm tích lũy cùng một lúc: một câu hỏi giấy phép trong thẩm định mua lại, một thư viện trọng yếu với một người bảo trì kiệt sức, một khuyến cáo bảo mật trong mã mà không ai biết mình đang phát hành. Một OSPO biến cuộc chạy đua đó thành năng lực được quản lý. Nó đặt chính sách tiêu thụ cho phép thay vì chặn, quyết định khi nào đóng góp ngược dòng phục vụ doanh nghiệp, quản gia các dự án bạn phát hành, và áp dụng cộng tác mở bên trong công ty qua [InnerSource](https://en.wikipedia.org/wiki/Inner_source). Đây là chức năng chiến lược, nối với các giá trị kỹ thuật phần mềm của bạn (chương 1.1), không phải ô đánh dấu tuân thủ.

Với doanh nghiệp, động lực là quy mô: hàng nghìn phụ thuộc, nghĩa vụ xuất khẩu và giấy phép qua các thẩm quyền, và hàng trăm kỹ sư mỗi người đưa ra những quyết định mã nguồn mở nhỏ hằng ngày. Một văn phòng duy nhất cho sự lan rộng đó một cột sống. Với chính phủ, động lực là chính sách và lòng tin công. "Mã nguồn mở theo mặc định" và "tiền công, mã công" ngày càng là luật, nên các cơ quan công cần ai đó có thể công bố mã an toàn, tái sử dụng qua các cơ quan, và buộc nhà cung cấp theo tiêu chuẩn mở. Ở cả hai bối cảnh, OSPO tự hoàn vốn bằng cách chuyển rủi ro vô hình, không định giá thành công việc có chủ đích, có ngân sách.

## Các nguyên tắc chính

- **Mã nguồn mở là mối quan hệ hai chiều, không phải kho miễn phí.** Bạn tiêu thụ, bạn đóng góp, và bạn phát hành, và một OSPO sở hữu cả ba.
- **Đóng góp là chiến lược, không phải từ thiện.** Đóng góp ngược dòng giảm chi phí mang bản vá riêng và mua cho bạn ảnh hưởng.
- **Cho phép đường nhanh, đừng canh cổng.** Một chính sách chậm hơn sao chép mã sẽ bị phớt lờ, nên hãy làm đường tuân thủ thành đường nhanh nhất.
- **Tài trợ những người bảo trì bạn phụ thuộc.** Kho chung không tự duy trì, và thư viện trọng yếu nhất của bạn có thể có một tác giả không lương.
- **Quản gia cái bạn phát hành, hoặc đừng phát hành.** Một dự án bị bỏ rơi hại danh tiếng của bạn hơn là không có dự án nào.
- **Đo mức tham gia để bạn cải thiện nó.** Đếm đóng góp, sức khỏe phụ thuộc và thời gian-đến-phê-duyệt, không phải thông cáo báo chí.
- **Trong chính phủ, mặc định là mở và công bố theo mặc định.** Cởi mở là chuẩn mực; đóng là ngoại lệ có tài liệu.

## Khuyến nghị

### Dựng một OSPO có quy mô khớp thực tế của bạn

Bạn không cần đội lớn để bắt đầu. Ở một công ty khởi nghiệp, OSPO có thể là một kỹ sư với nhiệm vụ bằng văn bản và vài giờ mỗi tuần. Ở một doanh nghiệp, đó là một nhóm trung tâm nhỏ cộng một mạng lưới liên kết các nhà vô địch nhúng trong đội sản phẩm. Dù quy mô nào, hãy trao cho nó một điều lệ rõ ràng bao quát bốn trách nhiệm: chính sách tiêu thụ và tuân thủ, đóng góp ngược dòng, phát hành và quản gia các dự án của chính bạn, và quan hệ cộng đồng và tài trợ. Đặt nó ở nơi nó thấy được cả kỹ thuật lẫn pháp lý, thường báo cáo cho CTO hoặc phó chủ tịch kỹ thuật với đường chấm tới pháp lý và bảo mật. Kiểu thất bại là một OSPO sống hoàn toàn trong pháp lý và trở thành cái phanh; cách sửa là bố trí nhân sự bằng kỹ sư thật sự phát hành, để hướng dẫn của nó mang uy tín với các đội nó phục vụ.

### Tiêu thụ có trách nhiệm, và làm đường an toàn thành đường dễ

Tiêu thụ là nơi hầu hết rủi ro vào, nên hãy làm hành vi tốt trở nên dễ dàng. Cung cấp một danh mục nội bộ được tuyển chọn gồm các thành phần đã thẩm định trước, quét giấy phép và lỗ hổng tự động trong đường ống, và mặc định rõ ràng mà nhà phát triển làm theo được mà không cần nộp phiếu. Dựa vào kỷ luật giấy phép ở chương 10.3 và các thực hành chuỗi cung ứng và sức khỏe phụ thuộc ở chương 2.18: ghim phiên bản, tạo danh mục vật liệu phần mềm, theo dõi [chuỗi cung ứng phần mềm](https://en.wikipedia.org/wiki/Software_supply_chain) tìm gói bị xâm phạm hoặc bị bỏ rơi, và theo dõi hết vòng đời trước khi nó buộc một cuộc di chuyển. Việc của OSPO không phải duyệt tay mọi phụ thuộc. Mà là xây rào chắn để chín mươi lăm phần trăm lựa chọn tự động an toàn và chỉ những trường hợp thực sự bất thường mới đến tay con người.

### Đóng góp ngược dòng vì nó sinh lời, không phải vì nó tử tế

Hãy coi đóng góp ngược dòng là quyết định kinh tế. Mỗi bản vá riêng bạn mang chống lại một phụ thuộc là một khoản thuế bạn trả ở mỗi lần nâng cấp, mãi mãi, cho đến khi thay đổi đáp xuống ngược dòng hoặc bản rẽ nhánh phân kỳ xa đến mức bạn sở hữu hoàn toàn. Đóng góp bản sửa ngược lại xóa khoản thuế đó. Đóng góp ngược dòng cũng mua ảnh hưởng lên hướng đi, để lộ trình của thành phần bạn dựa vào uốn về phía nhu cầu của bạn, và báo hiệu năng lực với các kỹ sư bạn muốn tuyển. Hãy trao cho nhà phát triển một con đường nhanh, có tài liệu: một thỏa thuận cấp phép người đóng góp hoặc chứng nhận nguồn gốc nhà phát triển đã được duyệt trước, một phê duyệt nhẹ xác nhận thay đổi an toàn để chia sẻ, và thời gian quản lý được lập ngân sách cho công việc. Khi phương án thay thế là duy trì một [bản rẽ nhánh](https://en.wikipedia.org/wiki/Fork_(software_development)) vĩnh viễn của dự án bạn không kiểm soát, đóng góp ngược lại hầu như luôn rẻ hơn.

### Phát hành dự án của chính bạn với quản trị thật

Khi bạn mở mã nguồn phần mềm bạn đã xây, hãy làm có chủ đích hoặc không làm. Trước tiên quyết định mã là hàng hóa đáng chia sẻ hay yếu tố tạo khác biệt đáng giữ đóng, dùng lập luận ở chương 10.12. Nếu phát hành, hãy chọn giấy phép khớp ý định của bạn (cho phép rộng rãi để tối đa hóa áp dụng, copyleft để giữ hệ sinh thái có đi có lại), lập tài liệu ai quyết định gì qua mô hình quản trị bằng văn bản, và đăng ký [nhãn hiệu](https://en.wikipedia.org/wiki/Trademark) cho tên dự án để bạn bảo vệ nó khỏi bị lạm dụng trong khi giữ mã tự do. Cam kết quản gia thật: một trình theo dõi vấn đề công khai, hướng dẫn đóng góp, bộ quy tắc ứng xử, và chính sách bảo mật với tiết lộ phối hợp để người báo cáo biết cách liên hệ bạn (chương 4.2). Nêu tên một người bảo trì và lập ngân sách thời gian của họ. Một dự án bạn ra mắt rầm rộ rồi bỏ rơi trong một năm hại danh tiếng của bạn hơn một dự án bạn chưa bao giờ phát hành.

### Áp dụng InnerSource để cộng tác bên trong công ty

Những thói quen làm mã nguồn mở hiệu quả (kho công khai, hướng dẫn đóng góp rõ ràng, rà soát theo năng lực, rào cản thấp cho bản vá đầu tiên) hiệu quả y như vậy sau bức tường lửa. InnerSource nghĩa là bất kỳ kỹ sư nào cũng tìm, dùng và cải thiện được bất kỳ dự án nội bộ nào, gửi pull request qua ranh giới đội thay vì nộp phiếu và chờ. Điều này phá vỡ silo, lan truyền tái sử dụng mã, và huấn luyện người của bạn đúng quy trình họ sẽ dùng khi đóng góp ra bên ngoài. OSPO là nơi tự nhiên cho InnerSource vì nó đã sở hữu công cụ và sổ tay văn hóa. Hãy bắt đầu với vài thư viện dùng chung giá trị cao, công bố hướng dẫn đóng góp của chúng nội bộ, và thưởng cho các đội chấp nhận bản vá từ bên ngoài một cách lịch thiệp.

### Tài trợ và duy trì những người bảo trì bạn phụ thuộc

Hệ thống sản xuất của bạn có thể dựa vào một thư viện do một người bảo trì trong thời gian rảnh. Đó là rủi ro chuỗi cung ứng, và phản ứng trung thực là giúp gánh phần tải. Hãy xác định các phụ thuộc trọng yếu nhất từ danh mục vật liệu của bạn, tìm những cái có cơ sở người bảo trì mỏng, và chọn phản ứng cho từng cái: tài trợ trực tiếp người bảo trì, đóng góp thời gian kỹ thuật, tham gia một quỹ tài trợ dự án, hoặc, như phương sách cuối, chuẩn bị rẽ nhánh hay thay thế. Tài trợ kho chung rẻ hơn sự cố khẩn cấp theo sau sự sụp đổ của nó, và nó giữ các thành phần bạn dựa vào lành mạnh và di chuyển theo hướng bạn có thể ảnh hưởng.

### Đặt chính sách đóng góp phê duyệt nhanh

Một chính sách đóng góp tồn tại để nói có nhanh, không phải nói không chậm. Hãy nêu rõ kỹ sư được đóng góp gì mà không cần hỏi (sửa lỗi, tài liệu, tính năng nhỏ cho dự án bạn đã dùng), cái gì cần kiểm tra nhẹ (bất cứ thứ gì chạm vào yếu tố tạo khác biệt hay bằng sáng chế), và sở hữu trí tuệ cùng thỏa thuận người đóng góp được xử lý một lần, tập trung, thay vì cho từng đóng góp. Tự động hóa phần nhàm chán: kiểm tra giấy phép, thỏa thuận người đóng góp doanh nghiệp ký sẵn, và một bot gắn cờ đóng góp hiếm gặp cần mắt người. Đo thời gian-đến-phê-duyệt và coi hàng đợi chậm là lỗi của chính sách.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| OSPO trung tâm | Chính sách nhất quán, chuyên môn sâu, quyền sở hữu rõ ràng | Có thể thành nút thắt nếu chỉ canh cổng mà không cho phép |
| OSPO liên kết (nhà vô địch trong các đội) | Mở rộng được, giữ quyết định gần kỹ sư | Cần phối hợp mạnh nếu không chính sách trôi rời nhau |
| Đóng góp ngược dòng | Xóa thuế bản vá riêng, mua ảnh hưởng, hỗ trợ tuyển dụng | Công sức liên tục, rà soát SHTT, làm việc theo lịch của người khác |
| Mang bản rẽ nhánh riêng | Kiểm soát đầy đủ, phát hành theo lịch của bạn | Thuế bảo trì vĩnh viễn, trôi khỏi bản sửa bảo mật ngược dòng |
| Phát hành dự án của chính bạn | Hệ sinh thái, danh tiếng, bảo trì chung | Chi phí quản gia thật; bị bỏ rơi hại danh tiếng |
| Tài trợ người bảo trì | Bảo vệ phụ thuộc trọng yếu, mua thiện chí | Chi phí trực tiếp, và chọn ai để tài trợ mang tính chính trị |
| Không có OSPO (tùy nghi) | Chi phí thiết lập bằng không | Nợ pháp lý, bảo mật và bền vững vô hình |

Căng thẳng trung tâm là giữa kiểm soát và cho phép. Một OSPO duyệt tay mọi phụ thuộc và mọi đóng góp cảm giác an toàn, nhưng nó trở thành thứ kỹ sư đi vòng, tạo ra các phụ thuộc bóng vô hình mà bạn muốn ngăn. Một OSPO chỉ công bố hướng dẫn vui vẻ mà không có thực thi tự động nào bị phớt lờ ngay khi hạn chót lờ mờ. Cách giải quyết là cùng cách chạy xuyên chương 10.3: tự động hóa trường hợp phổ biến để đường tuân thủ là đường nhanh nhất, và dành phán đoán của con người cho cái thực sự mới. Cân bằng đúng và văn phòng là bội số lực; cân bằng sai theo bất kỳ hướng nào và nó hoặc là cái phanh hoặc là đồ trang trí.

## Câu hỏi để thảo luận với đội của bạn

1. **Ai sở hữu mối quan hệ của bạn với mã nguồn mở hôm nay, và họ có thể trả lời một câu hỏi khó vào ngày mai không?** Nếu luật sư của một bên mua lại tiềm năng đòi bản kiểm kê giấy phép của bạn, hoặc một phóng viên hỏi thư viện không được bảo trì nào nằm trong đường thanh toán của bạn, có cái tên nào gắn với câu trả lời không? Với hầu hết tổ chức câu trả lời trung thực là "không ai," nghĩa là mọi kỹ sư đang lặng lẽ đặt chính sách và không ai chịu trách nhiệm về tổng. Hãy mang bằng chứng đến cuộc họp: thử tạo danh sách giấy phép được phê duyệt, danh mục vật liệu phần mềm, và người sẽ tiếp câu hỏi copyleft trong thẩm định. Nếu các hiện vật đó không tồn tại hoặc chỉ về không ai, bạn đã tìm thấy nhiệm vụ OSPO đầu tiên. Quyết định cần đưa ra không phải có chức năng hay không mà là ai sở hữu nó và họ mang nhiệm vụ gì, dù văn phòng là một người một ngày một tuần.

2. **Bạn có đang mang bản vá riêng mà bạn có thể đóng góp ngược dòng, và điều đó tốn bạn bao nhiêu?** Nhiều đội duy trì một đống lặng lẽ các sửa đổi cục bộ chống lại phụ thuộc, áp lại bằng tay mỗi lần nâng cấp và hấp thụ nỗi đau hợp nhất như thể đó là quy luật tự nhiên. Mỗi bản vá đó là một khoản thuế lặp lại, và mỗi cái là ứng viên để đóng góp ngược để thuế biến mất. Hãy mang chi tiết: liệt kê các bản rẽ nhánh và bản vá cục bộ mà bản dựng của bạn thực sự mang, ước tính giờ kỹ thuật mỗi cái tốn mỗi năm, và ghi dự án ngược dòng nào có khả năng chấp nhận thay đổi. Cân nhắc đối lập là thật, vì đóng góp ngược dòng tốn công sức bây giờ và chạy theo lịch của người bảo trì, nhưng phép so sánh là với việc trả thuế bản vá mãi mãi. Câu trả lời nên biến "chúng ta luôn chỉ áp lại nó" thành lựa chọn có chủ đích, với con đường đóng góp đủ nhanh để kỹ sư dùng nó.

3. **Phụ thuộc nào sẽ gây đau nhất nếu người bảo trì của nó bỏ đi, và bạn sẽ làm gì về nó?** Đâu đó trong ngăn xếp của bạn là một thành phần sẽ dừng một dịch vụ doanh thu hay sứ mệnh trọng yếu nếu nó hỏng, do một người hay một nhúm người bạn chưa bao giờ tài trợ hay cảm ơn bảo trì. Kho chung cảm giác miễn phí cho đến đúng khoảnh khắc nó không còn, và phiên bản đắt đỏ của bài học đó là cuộc chạy đua sau khi bị bỏ rơi hoặc một lỗ hổng chưa vá. Hãy mang danh mục vật liệu của bạn và xếp hạng phụ thuộc theo bán kính ảnh hưởng, rồi ghi số người bảo trì và tình trạng tài trợ của vài cái hàng đầu. Với mỗi cái trọng yếu, thiếu nhân sự, hãy quyết định từ trước bạn sẽ tài trợ, đóng góp thời gian, tham gia một quỹ, hay chuẩn bị thay thế. Điều đó biến một điểm đơn thất bại tiềm ẩn thành một mối quan hệ được quản lý, theo cùng tiêu chuẩn như bất kỳ rủi ro vận hành nào khác (chương 2.18).

4. **Trước khi mở mã nguồn công cụ nội bộ tiếp theo, bạn đã sẵn sàng quản gia nó nhiều năm, hay đang phát hành một lần ra mắt và một lời xin lỗi cuối cùng?** Một bản phát hành công khai là cam kết thường trực: một trình theo dõi vấn đề ai đó phải phân loại, một hộp thư bảo mật ai đó phải canh, và một cái tên ai đó phải bảo vệ. Các đội với tới mở mã nguồn để hỗ trợ tuyển dụng hay thiện chí, rồi phát hiện rằng một dự án bị bỏ rơi với vấn đề cũ hại danh tiếng họ hy vọng xây, nhiều hơn việc không phát hành gì. Hãy mang bằng chứng: liệt kê các dự án bạn đã phát hành, và với mỗi cái cho thấy tuổi của vấn đề mở, liệu người bảo trì có tên có giờ được lập ngân sách không, nó có mô hình quản trị, nhãn hiệu đã đăng ký và chính sách tiết lộ phối hợp không, và mã là hàng hóa đáng chia sẻ hay yếu tố tạo khác biệt bạn nên giữ đóng (chương 10.12). Cân nhắc đối lập là quản gia thật tốn thời gian kỹ thuật bạn có thể dùng cho sản phẩm, nên lựa chọn trung thực thường là phát hành ít thứ hơn và quản gia chúng đúng cách. Với doanh nghiệp, điều này nghĩa là rà soát pháp lý và thương hiệu trước ra mắt; với chính phủ, nó nghĩa là nhãn hiệu, kênh tiết lộ, và quy trình ngoại lệ công bố-theo-mặc định được giải quyết trước khi kho trở nên công khai.

5. **Một kỹ sư thực sự mất bao lâu để được duyệt một phụ thuộc hay được thông qua một đóng góp, và nó có chậm hơn việc đi vòng bạn không?** Một chính sách mã nguồn mở cạnh tranh trực tiếp với cách đi vòng nhanh nhất mà kỹ sư tìm được, và bất kỳ quy trình nào chậm hơn sao chép mã đều bị vượt qua, tạo ra các phụ thuộc bóng vô hình mà văn phòng được lập ra để ngăn. Căng thẳng là kiểm soát so với cho phép: mỗi rà soát thủ công thêm dấu vết kiểm toán và bắt được vấn đề thật hiếm gặp, nhưng cũng thêm độ trễ đẩy trường hợp trung vị khỏi đường tuân thủ. Hãy mang các con số đến cuộc họp: thời gian-đến-phê-duyệt đo được cho một phụ thuộc chuẩn và một đóng góp chuẩn, tỷ lệ quyết định được xử lý tự động so với bởi con người, và số ngoại lệ thực sự cần phán đoán quý trước. Trong doanh nghiệp với hàng trăm kỹ sư mỗi người đưa ra những quyết định nhỏ hằng ngày, một hàng đợi hai ngày lặng lẽ thành hàng nghìn rà soát bị đi vòng; trong chính phủ, cùng độ trễ va chạm nghĩa vụ mua sắm và kiểm toán đòi dấu vết giấy tờ mà cách đi vòng bỏ qua, nên cách sửa là tự động hóa trường hợp phổ biến thay vì bố trí nhân sự cho một cổng lớn hơn.

6. **Dự án nội bộ nào hưởng lợi nhiều nhất từ InnerSource, và cái gì cản đội khác gửi bạn một pull request hôm nay?** Những thực hành làm mã nguồn mở hiệu quả (kho công khai, hướng dẫn đóng góp, rà soát theo năng lực, rào cản thấp cho bản vá đầu tiên) sinh lời sau bức tường lửa bằng cách phá vỡ silo, lan truyền tái sử dụng, và huấn luyện mọi người đúng quy trình họ sẽ dùng để đóng góp ra bên ngoài. Cân nhắc đối lập là mở một dự án nội bộ đòi hướng dẫn đóng góp, năng lực rà soát dư, và quyết định mã nào phải giữ hạn chế vì lý do bảo mật hay quy định. Hãy mang chi tiết: nêu tên các thư viện dùng chung giá trị cao, ghi cái nào đã công bố hướng dẫn đóng góp nội bộ, và mô tả một pull request xuyên đội được xử lý thế nào hôm nay, được chào đón hay lạc trong hàng đợi. Với doanh nghiệp, lợi tức đo bằng các bản xây nội bộ trùng lặp được tránh qua nhiều đội; với chính phủ, cùng thói quen mở rộng qua ranh giới cơ quan thành tái sử dụng liên cơ quan, để công bố-theo-mặc định và thành phần dùng chung giảm chi tiêu công trùng lặp thay vì nhân lên nó.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy giao văn phòng cho một kỹ sư có tên vài giờ mỗi tuần với điều lệ một trang, không phải ủy ban. Mặc định giấy phép cho phép rộng rãi với máy quét trong đường ống, chỉ đóng góp ngược dòng số ít bản vá riêng thực sự gây đau ở mỗi lần nâng cấp, và thiết lập khoản tài trợ hằng tháng nhỏ cho thư viện do một người bảo trì mà bạn thực sự không thể sống thiếu. Tốc độ quan trọng hơn độ phủ ở đây: một đường tuân thủ nhanh hơn sao chép mã thắng một chính sách kỹ lưỡng không ai theo.

**Doanh nghiệp nhỏ.** Bạn sẽ không bố trí OSPO riêng, nên hãy mua năng lực nhúng trong công cụ bạn đã chạy: một máy quét gắn cờ vấn đề giấy phép và lỗ hổng, và một danh mục được tuyển chọn gồm các thành phần đã thẩm định trước. Đóng khung công việc là vệ sinh tuân thủ giấy phép và sức khỏe phụ thuộc hơn là một chương trình: biết có gì trong danh mục vật liệu phần mềm của bạn, biết mỗi giấy phép buộc gì, và biết phụ thuộc một người bảo trì nào sẽ gây đau nếu nó biến mất. Ưu tiên mua việc quét và lập danh mục hơn tự xây.

**Doanh nghiệp lớn.** Hãy chạy một văn phòng trung tâm nhỏ cộng một mạng liên kết các nhà vô địch nhúng trong đội sản phẩm, để chính sách nhất quán trong khi quyết định ở gần kỹ sư. Tự động hóa quét giấy phép, lỗ hổng và xuất khẩu, bao phủ mọi kỹ sư bằng thỏa thuận người đóng góp ký sẵn, và theo dõi thời gian-đến-phê-duyệt như chỉ số được báo cáo. Tài trợ các quỹ đứng sau phụ thuộc trọng yếu của bạn, chạy InnerSource qua nhiều kho, và quản lý toàn bộ tài sản như danh mục với chỉ số sức khỏe và mức tham gia thay vì một nhúm quyết định riêng lẻ.

**Chính phủ.** Hãy vận hành dưới mã-nguồn-mở-theo-mặc-định và tiền-công-mã-công: công bố dịch vụ mới trong kho công khai trừ khi áp dụng ngoại lệ có tài liệu về bảo mật hay riêng tư. Chạy danh mục liên cơ quan để các đội tái sử dụng trước khi xây, viết yêu cầu mã nguồn mở và tiêu chuẩn mở vào mua sắm để nhà cung cấp giao mã tái sử dụng được với quyền được giữ lại, và xử lý tiết lộ phối hợp cho cái bạn công bố. Tài trợ bảo trì các thư viện dùng chung mà nhiều cơ quan phụ thuộc, để không đội đơn lẻ nào lặng lẽ sở hữu hạ tầng mà cả chính phủ dựa vào.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp hai mươi người biến kỹ sư nền tảng trưởng thành chủ sở hữu OSPO bán thời gian với điều lệ một trang. Cô đặt chính sách tiêu thụ đơn giản (giấy phép cho phép rộng rãi được duyệt trước, copyleft được rà soát, máy quét trong đường ống), và cô nhận ra đội mang ba bản vá riêng chống lại một thư viện hàng đợi mã nguồn mở, áp lại đau đớn ở mỗi lần nâng cấp. Cô đóng góp ngược dòng cả ba; hai cái được chấp nhận trong một tháng, xóa vĩnh viễn thuế nâng cấp. Cô mở mã nguồn một công cụ nội bộ nhỏ với README thật, giấy phép và đầu mối bảo mật, chủ yếu để thu hút kỹ sư, và cô thiết lập khoản tài trợ hằng tháng cho bộ phân tích do một người bảo trì mà sản phẩm phụ thuộc vào. Không cái nào cần thêm nhân sự, chỉ một chủ sở hữu có tên và nhiệm vụ rõ ràng.

**Doanh nghiệp lớn.** Một ngân hàng toàn cầu chạy OSPO trung tâm sáu người cộng một mạng liên kết các nhà vô địch mã nguồn mở nhúng trong mỗi nhóm sản phẩm. Đội trung tâm sở hữu chính sách, việc quét tuân thủ giấy phép và xuất khẩu tự động, và thỏa thuận cấp phép người đóng góp mà mọi kỹ sư được bao phủ từ ngày đầu. Các nhà vô địch xử lý rà soát cục bộ và huấn luyện đội của họ về đóng góp. Ngân hàng tài trợ nhiều quỹ có dự án nâng đỡ hệ thống giao dịch của nó, đóng góp bản sửa ngược dòng cho một khung dữ liệu được dùng rộng rãi để thôi duy trì một bản rẽ nhánh, và chạy InnerSource qua hai trăm kho nội bộ để bất kỳ đội nào cũng gửi được pull request cho bất kỳ đội nào khác. Thời gian-đến-phê-duyệt cho một đóng góp chuẩn dưới hai ngày, được theo dõi như chỉ số OSPO báo cáo hằng quý.

**Chính phủ.** Một cơ quan số quốc gia vận hành dưới nhiệm vụ "mã nguồn mở theo mặc định" và tiền công, mã công. OSPO của nó công bố dịch vụ mới trong kho công khai trừ khi áp dụng ngoại lệ có tài liệu về bảo mật hay riêng tư, chạy danh mục xuyên chính phủ để các cơ quan tái sử dụng mã trước khi xây, và viết yêu cầu mã nguồn mở và tiêu chuẩn mở vào mua sắm để nhà cung cấp giao mã tái sử dụng được, có tài liệu tốt với chính phủ giữ quyền. Văn phòng cũng xử lý tiết lộ bảo mật phối hợp cho mã nó công bố và tài trợ bảo trì thư viện danh tính dùng chung mà nhiều cơ quan nay phụ thuộc, để không đội đơn lẻ nào lặng lẽ sở hữu thành phần mà cả chính phủ dựa vào.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức rõ ràng nhất là loại bỏ những bất ngờ tránh được, đắt đỏ. Mã nguồn mở không được quản lý tạo ra khủng hoảng đến theo lịch của chúng: vi phạm copyleft nổi lên trong thẩm định mua lại, di chuyển khẩn cấp khỏi thành phần đã chết, một vụ vi phạm truy về phụ thuộc không bản kiểm kê nào liệt kê. Một OSPO biến những sự kiện xác suất thấp, chi phí cao đó thành công việc đều đặn, có ngân sách. Cộng thêm khoản tiết kiệm lặp lại từ đóng góp ngược dòng: mỗi bản vá riêng bạn cho nghỉ hưu thôi đánh thuế mọi lần nâng cấp tương lai, và qua một tài sản lớn điều đó cộng dồn thành năng lực kỹ thuật thật được trả về cho công việc sản phẩm.

Trên sổ cái [tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership), văn phòng rẻ so với những gì nó bảo vệ. Chi phí của nó là một đội nhỏ, một ít công cụ quét và danh mục, và tài trợ người bảo trì khiêm tốn. Hãy đặt đó cạnh chi phí của việc không có nó: trách nhiệm pháp lý, thẩm định thất bại hay bị trì hoãn, sự cố bảo mật, các bản xây nội bộ trùng lặp của thứ đã tồn tại như mã nguồn mở, và sự chảy máu chậm của các bản rẽ nhánh không ai chọn giữ. Cũng có những lợi tức mặt trên khó định giá hơn nhưng thật: ảnh hưởng lên hướng đi của các thành phần bạn phụ thuộc, lợi thế tuyển dụng và danh tiếng từ sự hiện diện mã nguồn mở đáng tin, và phân phối nhanh hơn vì kỹ sư tái sử dụng thay vì xây lại. Khi lập luận với ban lãnh đạo, hãy đóng khung OSPO là quản lý chuỗi cung ứng cho phần lớn cơ sở mã của bạn, với một khoản cổ tức chiến lược thêm lên trên. Trong chính phủ, hãy thêm chiều tuân thủ, vì sự cởi mở thường bị bắt buộc và làm tốt tránh được cả không tuân thủ lẫn chi tiêu công trùng lặp.

## Phản mẫu và cạm bẫy

- **OSPO như một cái cổng.** Một văn phòng chỉ rà soát và chặn, không bao giờ cho phép, bị đi vòng, tạo ra những phụ thuộc bóng mà nó được lập ra để ngăn.
- **Sân khấu đóng góp.** Tuyên bố chiến lược mã nguồn mở trong khi làm quy trình phê duyệt chậm đến mức không ai thực sự đóng góp.
- **Bản phát hành bị bỏ rơi.** Công bố một dự án với bài blog ra mắt, rồi không bao giờ phân loại một vấn đề nào, hại danh tiếng hơn sự im lặng.
- **Rẽ nhánh rồi quên.** Rẽ nhánh một phụ thuộc cho một bản sửa rồi mang nó mãi mãi, trôi khỏi các bản vá bảo mật ngược dòng.
- **Ăn theo người bảo trì mong manh.** Phụ thuộc vào một thư viện trọng yếu một người bảo trì mà không bao giờ tài trợ, cảm ơn hay giúp người đứng sau nó.
- **Bỏ bê nhãn hiệu.** Phát hành dự án mà không bảo vệ tên của nó, rồi nhìn một bản rẽ nhánh hay nhà cung cấp lợi dụng danh tiếng của bạn.
- **Sở hữu chỉ ở pháp lý.** Đặt OSPO hoàn toàn trong pháp lý nên hướng dẫn của nó không mang uy tín kỹ thuật và các đội tắt tai.
- **Chỉ số phù phiếm.** Đếm sao và nhắc đến trên báo chí thay vì sức khỏe phụ thuộc, thời gian-đến-phê-duyệt và bản vá riêng đã cho nghỉ hưu.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Kỹ sư thêm, vá và thỉnh thoảng công bố mã nguồn mở mà không có chính sách và không có chủ sở hữu. Tiêu thụ, đóng góp và phát hành là phản ứng và tùy nghi, do sáng kiến cá nhân thúc đẩy. Bản rẽ nhánh riêng tích lũy không ai để ý, không ai tài trợ dự án ngược dòng nào, và không ai trả lời được câu hỏi giấy phép trong thẩm định.
- **Mức 2, Phát triển:** Thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Một chính sách tiêu thụ thô và danh sách giấy phép được phê duyệt tồn tại, và ai đó chịu trách nhiệm lỏng lẻo, nhưng đóng góp chậm và từng trường hợp và một số nhóm làm nhiều hơn hẳn nhóm khác. Một vài phụ thuộc trọng yếu được biết, nhưng tính bền vững, phát hành và quản gia vẫn không nhất quán.
- **Mức 3, Chuẩn hóa:** Một OSPO có điều lệ sở hữu tiêu thụ, đóng góp, phát hành và cộng đồng, và thực hành được lập tài liệu và thực thi toàn tổ chức. Quét và danh mục vật liệu phần mềm được tự động hóa, thỏa thuận người đóng góp duyệt trước và con đường phê duyệt nhanh tồn tại, dự án đã phát hành mang quản trị thật, nhãn hiệu và chính sách bảo mật, và InnerSource đang lan. Các đội chính phủ công bố theo mặc định.
- **Mức 4, Quản lý:** Chức năng mã nguồn mở được đo và kiểm soát theo đường cơ sở. Thời gian-đến-phê-duyệt được theo dõi so với mục tiêu, khối lượng đóng góp và tỷ lệ chấp nhận ngược dòng được báo cáo, bảng điều khiển sức khỏe phụ thuộc và số người bảo trì gắn cờ điểm đơn thất bại, độ phủ người bảo trì được tài trợ của các phụ thuộc rủi ro cao nhất được giám sát, và bản kiểm kê bản vá riêng và bản rẽ nhánh giảm theo xu hướng quý này qua quý khác. Dự án đã phát hành có thời gian phản hồi vấn đề đo được, ngoại lệ được rà soát theo nhịp, và chỉ số phù phiếm như sao bị bỏ để dùng những chỉ số này.
- **Mức 5, Điều phối:** Mã nguồn mở là năng lực chiến lược được quản lý, tích hợp với hoạch định kỹ thuật, pháp lý, bảo mật và mua sắm và thích ứng liên tục. Đóng góp là thường lệ, người bảo trì trọng yếu và các quỹ được tài trợ, tổ chức quản gia các dự án chạy tốt và lái các hệ sinh thái nó phụ thuộc, và InnerSource là chuẩn mực. Chỉ số mức tham gia và sức khỏe nuôi cải thiện liên tục, và danh mục được cân bằng lại khi phụ thuộc, rủi ro và nhiệm vụ dịch chuyển.

## Ý tưởng để thảo luận

1. Lằn ranh giữa OSPO cho phép và OSPO canh cổng nằm ở đâu, và làm sao bạn biết từ bên ngoài bạn đã xây cái nào?
2. Bản vá riêng hay bản rẽ nhánh nào của bạn đang được mang vì thói quen hơn là cần thiết, và cần gì để đóng góp ngược dòng ba cái hàng đầu?
3. Bạn nên quyết định tài trợ người bảo trì và quỹ nào khi danh sách phụ thuộc trọng yếu dài hơn ngân sách?
4. Điều gì sẽ thực sự đổi trong bản phát hành tiếp theo của bạn nếu bạn phải công bố nó với quản trị thật, nhãn hiệu và chính sách tiết lộ phối hợp ngay từ ngày đầu?
5. Với độc giả khu vực công, quy trình bảo vệ được để miễn mã khỏi công bố-theo-mặc định mà không lặng lẽ xói mòn nguyên tắc là gì?
6. Thư viện nội bộ nào hưởng lợi nhiều nhất từ InnerSource, và cái gì cản đội khác gửi bạn một pull request hôm nay?

## Những điểm cần ghi nhớ

- Một OSPO sở hữu toàn bộ mối quan hệ với mã nguồn mở: tiêu thụ có trách nhiệm, đóng góp ngược dòng, phát hành dự án của chính bạn, và duy trì những người bảo trì bạn phụ thuộc.
- Đóng góp ngược dòng là chiến lược, không phải từ thiện; nó xóa khoản thuế lặp lại của bản vá riêng, mua ảnh hưởng lên hướng đi, và giúp bạn tuyển dụng.
- Làm đường tuân thủ thành đường nhanh nhất qua tự động hóa và tuyển chọn, để văn phòng cho phép kỹ sư thay vì canh cổng họ.
- Chỉ phát hành dự án của chính bạn với quản trị thật, giấy phép đã chọn, nhãn hiệu được bảo vệ và tiết lộ bảo mật phối hợp, hoặc đừng phát hành chúng.
- Tài trợ và giúp những người bảo trì trọng yếu mà hệ thống sản xuất của bạn dựa vào, vì kho chung không tự duy trì.
- Áp dụng InnerSource để mang cộng tác mã nguồn mở vào bên trong công ty, và trong chính phủ, mặc định là mở, công bố theo mặc định, và tái sử dụng trước khi xây.

## Tài liệu tham khảo và đọc thêm

- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Nadia Eghbal, *Roads and Bridges: The Unseen Labour Behind Our Digital Infrastructure*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Danese Cooper và Klaas-Jan Stol (biên tập), *Adopting InnerSource: Principles and Case Studies*
- The Linux Foundation và TODO Group, *OSPO guides và Open Source Program Office resources*
- The Linux Foundation và TODO Group, *State of OSPOs and Open Source Management* (chuỗi khảo sát hằng năm)
- Heather Meeker, *Open (Source) for Business*
- Open Source Initiative, *The Open Source Definition* và danh sách giấy phép được phê duyệt
- Free Software Foundation Europe, tài liệu chiến dịch *Public Money, Public Code*
- U.S. Federal Source Code Policy và hướng dẫn Code.gov
