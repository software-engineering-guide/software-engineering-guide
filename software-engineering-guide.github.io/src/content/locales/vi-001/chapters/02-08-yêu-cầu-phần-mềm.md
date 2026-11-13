# 2.8 Yêu cầu phần mềm

## Tổng quan và động lực

Một [yêu cầu phần mềm](https://en.wikipedia.org/wiki/Software_requirements) là một phát biểu về một năng lực hoặc điều kiện mà hệ thống phải cung cấp, thỏa mãn hoặc sở hữu để được các bên liên quan chấp nhận. [Kỹ thuật yêu cầu](https://en.wikipedia.org/wiki/Requirements_engineering), công việc có kỷ luật gồm khơi gợi, phân tích, đặc tả, xác nhận và quản lý các phát biểu đó, nằm ngay ở đầu chuỗi giá trị. Mọi thứ ở hạ nguồn, từ kiến trúc đến mã đến [kiểm thử chấp nhận](https://en.wikipedia.org/wiki/Acceptance_testing), đều là nỗ lực thỏa mãn các yêu cầu. Vì vậy khi yêu cầu sai, không đầy đủ hoặc mơ hồ, mọi công sức bỏ ra để xây dựng đúng cái sai đều là lãng phí thuần túy, và đó là loại lãng phí đắt nhất, bởi bạn phát hiện nó muộn nhất. Lĩnh vực kiến thức Yêu cầu Phần mềm của [Bộ Kiến thức Kỹ thuật Phần mềm](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) coi đây là một kỷ luật kỹ thuật thực sự, không phải khúc dạo đầu văn thư cho công việc thực.

Với các đội lớn, yêu cầu là sự hiểu biết chung cho phép nhiều người xây một hệ thống mạch lạc. Một lập trình viên đơn lẻ có thể giữ ý định trong đầu; hàng trăm người qua nhiều đội thì không. Yêu cầu trở thành hợp đồng giữa những người cần một năng lực và những người xây dựng nó, cơ sở để chia công việc giữa các đội, và thước đo để đánh giá khi nào một thứ là "xong". Chúng kết nối trực tiếp với khám phá (chương 11.1), nơi vấn đề và cơ hội nổi lên; với nền tảng UX (chương 5.1), nơi bạn hiểu nhu cầu người dùng; với API và thiết kế giao diện (chương 2.3), nơi nghĩa vụ giao diện được cố định; với kiến trúc và thuộc tính chất lượng (chương 3.1), nơi yêu cầu phi chức năng định hình cấu trúc; và với quản lý dự án (chương 10.6), nơi phạm vi, chi phí và tiến độ được lên kế hoạch xoay quanh chúng.

Trong bối cảnh doanh nghiệp và chính phủ, yêu cầu mang trọng lượng pháp lý, hợp đồng và an toàn. Một hệ thống chịu quy định phải chứng minh rằng mọi nghĩa vụ bắt buộc (khả năng tiếp cận, riêng tư, bảo mật, lưu giữ hồ sơ, kiểm soát tài chính) được ghi nhận thành yêu cầu, được triển khai và được xác minh bằng bằng chứng. Các cuộc mua sắm của chính phủ thường được xây quanh một bản đặc tả yêu cầu, và thanh toán, kiểm toán cùng chứng nhận đều phụ thuộc vào việc truy vết từng yêu cầu đến bằng chứng rằng nó đã được đáp ứng. Ở đây, yêu cầu hơn cả thực hành tốt: chúng là xương sống của trách nhiệm giải trình.

## Các nguyên tắc chính

- Một yêu cầu diễn đạt một nhu cầu hoặc ràng buộc, không phải một giải pháp; nó nói cái gì và vì sao, không phải thế nào.
- Mọi yêu cầu phải cần thiết, không mơ hồ, kiểm chứng được, khả thi và truy vết được.
- Yêu cầu được khám phá và thương lượng với các bên liên quan, không phải được phát minh một cách cô lập.
- Yêu cầu phi chức năng và ràng buộc định hình kiến trúc nhiều như chức năng.
- Yêu cầu tiến hóa; hãy quản lý thay đổi một cách có chủ đích thay vì đóng băng hoặc phớt lờ nó.
- Khả năng truy vết, từ nhu cầu đến yêu cầu đến thiết kế đến kiểm thử đến bằng chứng, là mô liên kết của trách nhiệm giải trình.
- Mức độ hình thức phù hợp phụ thuộc vào rủi ro, quy mô và bối cảnh quy định, không phải thói quen.

## Khuyến nghị

### Xác định yêu cầu rõ ràng và phân loại chúng

Hãy gọi tên các loại một cách có chủ đích. **[Yêu cầu chức năng](https://en.wikipedia.org/wiki/Functional_requirement)** nêu hệ thống phải làm gì: các hành vi, phép biến đổi và dịch vụ mà nó cung cấp. **[Yêu cầu phi chức năng](https://en.wikipedia.org/wiki/Non-functional_requirement)** (thuộc tính chất lượng) nêu nó phải làm tốt đến đâu: hiệu năng, tính sẵn sàng, bảo mật, tính dùng được, khả năng tiếp cận, khả năng bảo trì và hơn thế; chúng gắn chặt với kiến trúc (chương 3.1). **Ràng buộc** là những ranh giới không thể thương lượng của giải pháp: công nghệ bắt buộc, tiêu chuẩn, ngân sách, quy tắc pháp lý hoặc giao diện với các hệ thống hiện có. Và hãy tách **yêu cầu kinh doanh** (vì sao tổ chức muốn hệ thống) khỏi **yêu cầu người dùng** (người dùng cần hoàn thành gì) khỏi **yêu cầu hệ thống** (phần mềm do đó phải làm gì). Trộn lẫn các cấp này và sự nhầm lẫn về phạm vi sẽ sớm theo sau.

### Khơi gợi từ nguồn thực, không phải giả định

Khơi gợi là khám phá chủ động. Hãy rút yêu cầu từ các bên liên quan thông qua phỏng vấn, hội thảo, quan sát, [bản mẫu](https://en.wikipedia.org/wiki/Software_prototyping), và phân tích các hệ thống cùng tài liệu hiện có. Tìm ra mọi bên liên quan có liên quan, kể cả những người dễ bị bỏ qua: người vận hành, kiểm toán viên, nhân viên hỗ trợ, và những người bị hệ thống ảnh hưởng nhưng không bao giờ dùng trực tiếp. Gắn việc khơi gợi với quy trình khám phá (chương 11.1) và nghiên cứu UX (chương 5.1), để mong muốn đã nêu truy vết về nhu cầu nền tảng. Hãy ghi lại nguồn và lý do của từng yêu cầu, vì biết vì sao một yêu cầu tồn tại chính là điều cho phép bạn thay đổi nó an toàn sau này.

### Phân tích, thương lượng và ưu tiên

Các nhu cầu thô được khơi gợi mâu thuẫn, chồng chéo và cộng lại nhiều hơn mức khả thi. Phân tích là cách bạn dung hòa chúng: phân loại yêu cầu, phát hiện xung đột, cân nhắc tính khả thi và rủi ro, và thương lượng ưu tiên với các bên liên quan. Hãy ưu tiên một cách công khai, chẳng hạn với các phân biệt phải/nên/có thể hoặc xếp hạng giá trị so với chi phí, để khi thời gian cạn, bạn cắt đúng phạm vi. Và hãy mô hình hóa yêu cầu ở bất cứ nơi nào mô hình thêm sự rõ ràng: luồng quy trình, sơ đồ trạng thái, mô hình dữ liệu và định nghĩa giao diện làm lộ những khoảng trống mà văn xuôi che giấu.

### Đặc tả ở mức độ hình thức phù hợp

Hãy viết yêu cầu ở dạng phù hợp với rủi ro và đối tượng. Một hệ thống chính phủ có mức đảm bảo cao có thể đòi hỏi một đặc tả hình thức được cấu trúc theo một tiêu chuẩn như IEEE 29148; một đội sản phẩm di chuyển nhanh có thể ghi yêu cầu thành [câu chuyện người dùng](https://en.wikipedia.org/wiki/User_story) với tiêu chí chấp nhận trong một danh sách tồn đọng. Dù cách nào, mỗi yêu cầu nên nguyên tử, kiểm chứng được và không có những từ trơn trượt như "nhanh", "thân thiện với người dùng" hay "v.v.". Gắn tiêu chí chấp nhận, để bạn xác định cách kiểm chứng một yêu cầu ngay lúc bạn viết nó. Và giữ một nguồn có thẩm quyền duy nhất, thay vì để yêu cầu rải rác trong email, phiếu việc và bản trình chiếu.

### Xác nhận trước khi xây dựng

Xác nhận khẳng định rằng các yêu cầu bạn đã đặc tả là đúng và khớp với nhau. Hãy rà soát chúng với các bên liên quan, đi qua các kịch bản, và nơi có thể, dùng bản mẫu để biến các phát biểu trừu tượng thành cụ thể. Xác nhận rẻ hơn mọi sự sửa chữa sau này: một lỗi bị bắt trong buổi rà soát yêu cầu tốn một phần nhỏ so với cùng lỗi đó bị bắt trên môi trường thực.

### Quản lý yêu cầu và duy trì khả năng truy vết

Yêu cầu thay đổi. Công việc của bạn là kiểm soát sự thay đổi đó, không phải chống lại nó. Thiết lập một quy trình thay đổi: cân nhắc tác động, chi phí và hiệu ứng hạ nguồn của từng thay đổi được đề xuất trước khi bạn chấp nhận. Lập đường cơ sở cho yêu cầu tại các thời điểm đã thống nhất và đánh phiên bản chúng. Giữ **[khả năng truy vết hai chiều](https://en.wikipedia.org/wiki/Requirements_traceability)** nối mỗi yêu cầu tiến về thiết kế, mã và kiểm thử, và lùi về nhu cầu mà nó xuất phát. Khả năng truy vết trả lời hai câu hỏi mà các đội lớn sống nhờ: nếu nhu cầu này thay đổi, nó ảnh hưởng đến cái gì; và với tính năng đã giao này, nhu cầu nào đã biện minh cho nó? Trong các bối cảnh chịu quy định, hãy kéo dài dấu vết đến tận bằng chứng chấp nhận (kết quả kiểm thử, hồ sơ kiểm toán, chữ ký phê duyệt) để bạn có thể chứng minh sự tuân thủ thay vì chỉ khẳng định.

### Thích ứng với bối cảnh agile và theo kế hoạch

Trong các chương trình theo kế hoạch và chịu quy định, bạn đặc tả và lập đường cơ sở cho yêu cầu khá sớm, với kiểm soát thay đổi chính thức. Trong bối cảnh agile, yêu cầu sống như một danh sách tồn đọng được ưu tiên, tiến hóa, được tinh chỉnh ngay trước khi triển khai và được xác nhận liên tục qua phần mềm đang chạy. Các hoạt động nền tảng là như nhau ở cả hai; chỉ thời điểm, mức độ hình thức và hiện vật khác nhau. Các tổ chức lớn thường pha trộn cả hai: họ đặc tả và truy vết chính thức các nghĩa vụ ổn định, có mức đảm bảo cao, trong khi tinh chỉnh hành vi sản phẩm một cách lặp. Hãy chọn sự cân bằng theo rủi ro, không phải ý thức hệ.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Phù hợp nhất cho | Ưu điểm | Nhược điểm |
|---|---|---|---|
| Đặc tả hình thức trả trước | Hợp đồng có mức đảm bảo cao, chịu quy định, phạm vi cố định | Khả năng truy vết mạnh; cơ sở chấp nhận rõ ràng; có thể kiểm toán | Chậm thay đổi; rủi ro đặc tả quá mức trước khi học hỏi |
| Danh sách tồn đọng agile | Sản phẩm tiến hóa với các bên liên quan gắn bó | Phản hồi nhanh; thích ứng với việc học; ít lãng phí cho phạm vi chưa xây | Khả năng truy vết dài hạn yếu hơn; khó kiểm toán và ký hợp đồng hơn |
| Kết hợp (ràng buộc hình thức + hành vi agile) | Doanh nghiệp có nghĩa vụ hỗn hợp | Chặt chẽ ở nơi quan trọng, linh hoạt ở nơi khác | Đòi hỏi phán đoán về phần nào là phần nào |

Căng thẳng trung tâm là giữa ổn định và học hỏi. Cố định yêu cầu sớm mua cho bạn một cơ sở chấp nhận vững chắc và khả năng kiểm toán, nhưng tốn khả năng thích ứng với những gì bạn học được trong khi xây dựng. Trì hoãn chúng mua cho bạn khả năng thích ứng, nhưng tốn khả năng truy vết dài hạn và sự rõ ràng về hợp đồng. Đầu tư nhiều hơn vào kỹ thuật yêu cầu cũng đánh đổi tốc độ ngắn hạn lấy ít làm lại hơn về sau: một sự đánh đổi hoàn vốn khi quy mô, tuổi thọ và hậu quả của thất bại của một hệ thống tăng lên. Các dự án lớn nhất và chịu quy định nhất nằm chắc chắn ở phía đầu tư cao. Một công cụ nội bộ ít rủi ro thì không.

## Câu hỏi để thảo luận với đội của bạn

1. **Ai được coi là bên liên quan cho hệ thống rủi ro cao nhất của chúng ta, và những ai chúng ta cứ bỏ sót cho đến khi chấp nhận?** Trong một chương trình lớn, những người bị bỏ qua hiếm khi là người dùng hiển nhiên: họ là người vận hành chạy hệ thống lúc 3 giờ sáng, kiểm toán viên phải chứng nhận nó, nhân viên hỗ trợ xử lý các thất bại, và những người không dùng nhưng bị ảnh hưởng không bao giờ đăng nhập mà bạn lại giữ dữ liệu của họ. Bỏ sót họ và bạn khám phá yêu cầu của họ vào thời điểm đắt đỏ nhất, trong lúc chấp nhận hoặc sau khi cơ quan quản lý hỏi. Hãy mang một bản đồ bên liên quan cụ thể đến cuộc họp và kiểm tra áp lực nó: với mỗi nghĩa vụ bắt buộc (khả năng tiếp cận, riêng tư, lưu giữ hồ sơ, bảo mật), hãy nêu tên người sở hữu nó và yêu cầu ghi nhận nó. Nếu bạn không thể nêu tên một chủ sở hữu, bạn đã tìm ra một khoảng trống, và cách sửa là thêm bên liên quan đó vào việc khơi gợi ngay bây giờ thay vì lắp nhu cầu của họ vào một kiến trúc đã cố định sau này.

2. **Khi một yêu cầu thay đổi, chúng ta có thể trả lời nó ảnh hưởng đến cái gì trước khi phê duyệt thay đổi không?** Đây là phép thử thực tế cho việc khả năng truy vết hai chiều của bạn là thật hay chỉ để trang trí. Trong một hệ thống lớn hoặc chịu quy định, một thay đổi quy tắc đơn lẻ có thể lan vào thiết kế, mã, kiểm thử và bằng chứng chấp nhận, và phê duyệt nó một cách mù quáng là cách bạn phát hành một hệ thống trông tuân thủ nhưng âm thầm vi phạm một quy tắc mà trước đây nó đã thỏa mãn. Hãy mang một yêu cầu thay đổi gần đây và thử truy vết nó tiến lên ngay trong cuộc họp: nếu mất một buổi chiều khai quật, khả năng truy vết của bạn không làm tròn việc của nó. Câu trả lời nên định hình lại quy trình thay đổi của bạn, để đánh giá tác động là một truy vấn nhanh trên một dấu vết sống thay vì một cuộc lùng sục thủ công, và để các đường cơ sở cùng việc đánh phiên bản cho bạn một điểm ổn định để thay đổi dựa vào.

3. **Nguồn có thẩm quyền duy nhất của các yêu cầu của chúng ta nằm ở đâu, và bao nhiêu sự thật nằm rải rác bên ngoài nó?** Sự tràn lan yêu cầu (bản đặc tả thực sống rải trong email, phiếu việc, bản trình chiếu và trí nhớ của ai đó) là một trong những thất bại phổ biến nhất ở các đội lớn, và nó là chí mạng trong các hệ thống được kiểm toán nơi bạn phải chứng minh điều gì đã được thống nhất. Hãy quyết định, một cách rõ ràng, hệ thống ghi nhận nào là chuẩn, và coi bất cứ điều gì được nêu ở nơi khác là bản nháp cho đến khi nó đáp xuống đó kèm nguồn và lý do. Hãy mang bằng chứng: đếm xem bao nhiêu tranh chấp phạm vi gần đây quy về hai người trích dẫn các phiên bản "cuối cùng" khác nhau. Nếu con số lớn hơn không, hành động là hợp nhất về một nguồn và viết ra lý do cho từng yêu cầu, vì biết vì sao một yêu cầu tồn tại chính là điều cho phép bạn thay đổi hoặc bỏ nó một cách an toàn sau này.

4. **Các yêu cầu phi chức năng của chúng ta có được ghi nhận đủ sớm để dẫn dắt kiến trúc, hay chúng ta cứ khám phá chúng sau khi cấu trúc đã cố định?** Các nghĩa vụ về hiệu năng, tính sẵn sàng, bảo mật và khả năng tiếp cận định hình kiến trúc nhiều hơn hầu hết các tính năng, và trong một chương trình lớn chúng là những yêu cầu thường bị phát hiện quá muộn nhất, khi cấu trúc phải thỏa mãn chúng đã được đổ bê tông. Lực kéo đối lập là có thật: hành vi chức năng là thứ các bên liên quan nói ra thành lời và trình diễn tốt, trong khi một yêu cầu "phản hồi dưới một giây khi tải cao điểm" hay "tuân thủ khả năng tiếp cận WCAG" vô hình cho đến khi bị vi phạm. Hãy mang danh sách các yêu cầu phi chức năng hiện tại của hệ thống rủi ro cao nhất, thời điểm trong dòng thời gian mỗi yêu cầu được viết ra, và liệu kiến trúc (chương 3.1) nhận chúng như các yếu tố dẫn dắt tường minh hay suy ra chúng. Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm các nghĩa vụ chất lượng bắt buộc (mã hóa, lưu giữ hồ sơ, luật khả năng tiếp cận) và kiểm tra mỗi cái là một yêu cầu bằng văn bản, đo được được trao cho thiết kế thay vì một giả định, vì hồi tố một thuộc tính chất lượng sau chấp nhận là nơi ngân sách và tiến độ âm thầm chết.

5. **Mức độ hình thức nào là phù hợp cho từng hệ thống chúng ta sở hữu, và chúng ta chọn nó theo rủi ro hay theo thói quen?** Một tổ chức lớn đơn lẻ thường vận hành một dải hệ thống, từ một công cụ nội bộ dùng một lần đến một nền tảng chịu quy định về an toàn tính mạng, và áp dụng một nghi thức cho tất cả hoặc chôn vùi công việc rủi ro thấp trong giấy tờ hoặc để công việc rủi ro cao được đặc tả thiếu. Căng thẳng là giữa khả năng kiểm toán và cơ sở chấp nhận vững chắc của đặc tả hình thức trả trước với phản hồi nhanh và ít lãng phí của một danh sách tồn đọng tiến hóa, và câu trả lời trung thực với hầu hết doanh nghiệp là một sự pha trộn có chủ đích: chính thức hóa và truy vết các nghĩa vụ ổn định, có mức đảm bảo cao trong khi tinh chỉnh hành vi sản phẩm một cách lặp. Hãy mang một bản kiểm kê ngắn các hệ thống của bạn được xếp hạng theo hậu quả của thất bại, mức độ tiếp xúc quy định và tốc độ thay đổi, và với mỗi hệ thống hãy nêu mức độ hình thức bạn thực sự dùng so với mức độ hình thức mà rủi ro đòi hỏi. Với một chương trình chính phủ neo vào một lời mời thầu và một tiêu chuẩn như IEEE 29148, mức độ hình thức một phần do hợp đồng quy định, nên cuộc thảo luận là nơi bạn có thể chồng sự tinh chỉnh agile lên trên mà không phá vỡ khả năng truy vết mà kiểm toán phụ thuộc vào.

6. **Mọi yêu cầu trong hệ thống rủi ro cao nhất của chúng ta có kiểm chứng được không, và mỗi yêu cầu có mang tiêu chí chấp nhận được viết ngay lúc yêu cầu được viết không?** Một yêu cầu bạn không thể kiểm chứng không phải là một yêu cầu, đó là một điều ước, và những từ trơn trượt như "nhanh", "bảo mật" hay "thân thiện với người dùng" qua được đánh giá chính vì không ai có thể làm chúng thất bại. Với một đội lớn điều này quan trọng gấp đôi: các yêu cầu không kiểm chứng được tạo ra tranh chấp phạm vi lúc chấp nhận, và chúng khiến không thể nói khi nào một tính năng thực sự xong. Cân nhắc đối lập là tốc độ, vì gắn một tiêu chí đo được và phương pháp kiểm chứng cho từng yêu cầu chậm hơn lúc ban đầu so với viết văn xuôi, nhưng đó là sự phòng thủ rẻ nhất chống lại việc làm lại muộn đắt nhất. Hãy mang một mẫu các yêu cầu gần đây và kiểm tra từng cái theo một chuẩn đơn giản: nó có nguyên tử không, đo được không, và có nêu cách nó sẽ được kiểm tra không. Trong bối cảnh chịu quy định và chính phủ, hãy mở rộng phép thử sang bằng chứng: một yêu cầu không có bằng chứng chấp nhận được truy vết, đạt không được coi là đã giao bất kể phần mềm trông làm gì, nên tiêu chí chấp nhận là hạt giống của hồ sơ tuân thủ mà cuối cùng bạn phải tạo ra.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một đội nhỏ và ít nguồn vốn, hãy giữ yêu cầu nhẹ nhất có thể: câu chuyện người dùng với tiêu chí chấp nhận trong một danh sách tồn đọng chung, không phải một tài liệu đặc tả. Kỷ luật hoàn vốn ngay cả ở đây là nói chuyện với người dùng thực trước khi bạn xây dựng và ghi lại nguồn cùng lý do của từng câu chuyện, để tuần bạn lẽ ra phải lãng phí xây sai tính năng là tuần bạn tiết kiệm được. Bỏ qua khả năng truy vết chính thức, nhưng đừng bao giờ bỏ qua cuộc trò chuyện cho bạn biết nhu cầu thực sự là gì.

**Doanh nghiệp nhỏ.** Bạn có thể không có nhà phân tích kinh doanh hay chuyên gia yêu cầu, nên công việc rơi vào ai gần khách hàng nhất, và câu hỏi mua hay xây chi phối. Hãy đóng khung yêu cầu như một danh sách ngắn, được ưu tiên các kết quả bạn cần, rồi dùng nó để đánh giá các công cụ có sẵn thay vì đặc tả một bản dựng riêng. Hãy nghiêm khắc trong việc tách nhu cầu nền tảng khỏi danh sách tính năng của nhà cung cấp, vì một yêu cầu được viết là "chúng tôi cần sản phẩm X" âm thầm đóng cửa các lựa chọn rẻ hơn có thể đã đáp ứng nhu cầu thực.

**Doanh nghiệp lớn.** Quy mô biến yêu cầu thành hợp đồng cho phép nhiều đội xây một hệ thống mạch lạc, nên ưu tiên là một quy trình chuẩn được áp dụng nhất quán: các loại được xác định, khả năng truy vết hai chiều từ nhu cầu đến kiểm thử, một nguồn có thẩm quyền duy nhất, và thay đổi được kiểm soát với các đường cơ sở. Hãy tách rõ ràng yêu cầu kinh doanh, người dùng và hệ thống và trao yêu cầu phi chức năng cho kiến trúc như các yếu tố dẫn dắt, để phạm vi và nghĩa vụ chất lượng không rải rác giữa các đội. Hãy pha trộn đặc tả hình thức cho các nghĩa vụ ổn định, có mức đảm bảo cao với sự tinh chỉnh agile cho hành vi sản phẩm, và quản trị sự cân bằng theo rủi ro thay vì theo sở thích của bất kỳ đội nào.

**Chính phủ.** Quy tắc mua sắm thường xây toàn bộ hợp đồng quanh một bản đặc tả yêu cầu, thường được cấu trúc theo một tiêu chuẩn như IEEE 29148, nên sự chính xác và đầy đủ là thuộc hợp đồng, không phải tùy chọn. Hãy duy trì một ma trận truy vết yêu cầu nối mỗi yêu cầu với thiết kế, ca kiểm thử và bằng chứng chấp nhận, vì thanh toán nhà cung cấp, kiểm toán và quyền cấp phép vận hành đều phụ thuộc vào độ bao phủ đã chứng minh. Tính minh bạch và trách nhiệm giải trình trước công chúng nâng ngưỡng cao hơn nữa: các nghĩa vụ bắt buộc về khả năng tiếp cận, riêng tư và lưu giữ hồ sơ mỗi cái phải xuất hiện như một yêu cầu tường minh, kiểm chứng được, và một yêu cầu không có bằng chứng được truy vết, đạt đơn giản là chưa được giao.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người xây dựng ứng dụng lập lịch ghi yêu cầu thành câu chuyện người dùng với tiêu chí chấp nhận trong một danh sách tồn đọng chung, không phải một đặc tả hình thức. Trước khi viết tính năng đồng bộ lịch, người sáng lập dành một buổi chiều nói chuyện với năm khách hàng tiềm năng và biết được nhu cầu thực là tránh đặt trùng lịch giữa hai công cụ, không phải việc đồng bộ mà họ đã giả định. Cuộc trò chuyện đó đóng khung lại câu chuyện và tiết kiệm một tuần xây dựng sai thứ. Ngay cả ở quy mô này họ vẫn ghi lại nguồn và lý do của từng câu chuyện, để khi ưu tiên thay đổi họ có thể bỏ hoặc làm lại phạm vi mà không phải tranh luận lại vì sao nó tồn tại.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia thay thế nền tảng khởi tạo khoản vay của mình. Đội yêu cầu tách yêu cầu kinh doanh (giảm thời gian phê duyệt, tuân thủ quy định cho vay), yêu cầu người dùng (nhân viên cho vay cần so sánh các đề nghị trong một chế độ xem) và yêu cầu hệ thống (nền tảng phải tích hợp với ba hệ thống lõi). Các yêu cầu phi chức năng (phản hồi dưới một giây cho các truy vấn phổ biến, tính sẵn sàng 99,95%, mã hóa dữ liệu cá nhân) được ghi nhận tường minh và trao cho kiến trúc (chương 3.1) như các yếu tố dẫn dắt. Mọi yêu cầu được truy vết qua danh sách tồn đọng đến các kiểm thử chấp nhận tự động. Vì vậy khi cơ quan quản lý hỏi một quy tắc cho vay cụ thể được thực thi thế nào, đội chỉ cần theo dấu vết từ quy tắc đến kiểm thử xác minh nó.

**Chính phủ.** Một cơ quan quốc gia mua sắm một hệ thống xét điều kiện trợ cấp thông qua một lời mời thầu chính thức. Hợp đồng được neo vào một bản đặc tả yêu cầu cấu trúc theo IEEE 29148, bao gồm các quy tắc đủ điều kiện chức năng, sự tuân thủ khả năng tiếp cận bắt buộc, ràng buộc riêng tư và lưu giữ hồ sơ, và các biện pháp kiểm soát bảo mật. Một ma trận truy vết yêu cầu nối mỗi yêu cầu với các thành phần thiết kế, ca kiểm thử và bằng chứng chấp nhận. Thanh toán nhà cung cấp và quyền cấp phép vận hành (sự phê duyệt chính thức để chạy hệ thống trong môi trường thực) đều phụ thuộc vào độ bao phủ đã chứng minh. Một yêu cầu không có bằng chứng chấp nhận được truy vết, đạt đơn giản là không được coi là đã giao, bất kể phần mềm trông làm gì.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lập luận kinh tế cho kỹ thuật yêu cầu dựa trên chi phí sửa lỗi muộn. Các nghiên cứu ngành luôn thấy rằng lỗi yêu cầu là một trong những nguyên nhân phổ biến và tốn kém nhất của thất bại dự án, và rằng chi phí sửa một lỗi tăng theo bậc độ lớn từ giai đoạn yêu cầu đến môi trường thực. Vì vậy tiền chi để làm rõ và xác nhận yêu cầu thực chất là đòn bẩy: một khoản đầu tư khiêm tốn từ sớm giúp bạn khỏi xây dựng, kiểm thử và vận hành sai thứ.

Tổng chi phí sở hữu của yêu cầu bao gồm công sức liên tục của khơi gợi, đặc tả, công cụ và quản lý thay đổi trong suốt vòng đời hệ thống; nó không phải chi phí một lần. Đối trọng với nó là chi phí của yêu cầu kém: làm lại, tranh chấp phạm vi, vượt tiến độ, chấp nhận thất bại, phạt hợp đồng, và trong bối cảnh chịu quy định, tiền phạt hoặc mất quyền cấp phép. Với ban lãnh đạo, hãy đóng khung độ trưởng thành của yêu cầu như giảm rủi ro và khả năng dự đoán. Theo dõi sự biến động của yêu cầu, nguồn gốc lỗi, và tỷ lệ công việc đã giao truy vết được đến một nhu cầu đã được xác nhận, và kết nối chúng với dự báo quản lý dự án (chương 10.6). Lợi tức không hiện ra như một tính năng. Nó hiện ra như những thất bại và việc làm lại không bao giờ xảy ra.

## Phản mẫu và cạm bẫy

- **Giải pháp ngụy trang thành yêu cầu:** đặc tả một công nghệ hoặc bố cục màn hình đã chọn thay vì nhu cầu nền tảng, đóng cửa các lựa chọn tốt hơn.
- **Ngôn ngữ mơ hồ:** "nhanh", "bảo mật", "trực quan" không có tiêu chí đo được, khiến yêu cầu không kiểm chứng được.
- **[Mạ vàng](https://en.wikipedia.org/wiki/Gold_plating_(software_engineering)):** ghi nhận các yêu cầu mà không bên liên quan nào thực sự cần, thổi phồng phạm vi và chi phí.
- **Thiếu yêu cầu phi chức năng:** chỉ khám phá nghĩa vụ hiệu năng, bảo mật hay khả năng tiếp cận sau khi kiến trúc đã cố định.
- **Yêu cầu tràn lan:** sự thật rải rác trong email, phiếu việc và bản trình chiếu mà không có nguồn có thẩm quyền.
- **Thay đổi bị đóng băng hoặc không kiểm soát:** hoặc từ chối mọi thay đổi hoặc chấp nhận mọi thay đổi mà không đánh giá tác động.
- **Không có khả năng truy vết:** không thể trả lời một thay đổi ảnh hưởng đến cái gì hay vì sao một tính năng tồn tại, chí mạng trong các hệ thống được kiểm toán.
- **Tê liệt vì phân tích:** đặc tả vô tận trì hoãn việc học từ phần mềm đang chạy.
- **Bên liên quan bị phớt lờ:** người vận hành, kiểm toán viên và những người không dùng nhưng bị ảnh hưởng bị bỏ ra ngoài cho đến khi chấp nhận.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu.** Yêu cầu ngầm hiểu hoặc truyền miệng, được ghi nhận không nhất quán và phản ứng. Tranh chấp phạm vi và làm lại phổ biến; không có khả năng truy vết, không có tiêu chí chấp nhận và không có quy trình xác định.
- **Mức 2, Phát triển.** Một số đội viết yêu cầu ra và theo dõi chúng theo từng dự án, với ưu tiên cơ bản và xử lý thay đổi tùy nghi. Các thực hành tồn tại nhưng khác nhau theo đội và theo người, nên các loại, mức độ hình thức và chất lượng không nhất quán trong tổ chức.
- **Mức 3, Chuẩn hóa.** Một quy trình yêu cầu chuẩn được lập thành tài liệu và thực thi toàn tổ chức: các loại được xác định, thực hành khơi gợi và xác nhận, tiêu chí chấp nhận gắn vào lúc soạn thảo, một nguồn có thẩm quyền duy nhất, và khả năng truy vết hai chiều từ nhu cầu đến kiểm thử, được điều chỉnh nhất quán cho bối cảnh agile hoặc theo kế hoạch.
- **Mức 4, Quản lý.** Quy trình được đo lường và kiểm soát bằng dữ liệu. Sự biến động của yêu cầu, nguồn gốc lỗi, độ bao phủ truy vết, và tỷ lệ công việc đã giao truy vết được đến một nhu cầu đã được xác nhận được theo dõi so với đường cơ sở; khả năng truy vết mở rộng đến bằng chứng chấp nhận và tuân thủ; và các chỉ số yêu cầu nuôi dưỡng dự báo dự án (chương 10.6), để các quyết định về thay đổi và chất lượng dựa trên bằng chứng thay vì ý kiến.
- **Mức 5, Điều phối.** Thực hành yêu cầu được cải tiến liên tục và tích hợp trong toàn tổ chức. Mức độ hình thức được tinh chỉnh thích ứng theo rủi ro và kết quả, công cụ khơi gợi và truy vết kết nối với khám phá, kiến trúc và phân phối, và tổ chức dùng lịch sử đo lường của chính mình để ngăn chặn các lỗi yêu cầu tái diễn trước khi chúng đến mã.

## Ý tưởng để thảo luận

- Làm thế nào bạn phân biệt một yêu cầu thực sự với một giải pháp vội vàng khi một bên liên quan cấp cao nêu nó như một giải pháp?
- Mức độ hình thức yêu cầu nào là phù hợp cho hệ thống rủi ro cao nhất của bạn so với hệ thống rủi ro thấp nhất, và ai quyết định?
- Làm thế nào bạn giữ khả năng truy vết hai chiều luôn cập nhật trong một danh sách tồn đọng agile di chuyển nhanh mà không biến nó thành gánh nặng quan liêu?
- Những yêu cầu phi chức năng nào thường bị khám phá quá muộn nhất trong tổ chức của bạn, và vì sao?
- Trong một chương trình chịu quy định, điều gì cấu thành bằng chứng chấp nhận đủ rằng một yêu cầu đã được đáp ứng?
- Các công cụ khơi gợi và đặc tả có AI hỗ trợ nên thay đổi thực hành yêu cầu của bạn thế nào, và chúng đưa vào những rủi ro mới nào?

## Những điểm cần ghi nhớ

- Yêu cầu nêu nhu cầu và ràng buộc, không phải giải pháp; chúng phải cần thiết, không mơ hồ, kiểm chứng được và truy vết được.
- Tách yêu cầu chức năng, phi chức năng và ràng buộc, cùng các cấp kinh doanh, người dùng và hệ thống.
- Khơi gợi từ các bên liên quan thực, phân tích và ưu tiên, đặc tả ở mức độ hình thức phù hợp, xác nhận trước khi xây dựng, và quản lý thay đổi.
- Khả năng truy vết hai chiều từ nhu cầu đến bằng chứng chấp nhận là xương sống của trách nhiệm giải trình, đặc biệt trong các bối cảnh chịu quy định.
- Bối cảnh agile và theo kế hoạch chia sẻ cùng các hoạt động; chúng khác nhau ở thời điểm, mức độ hình thức và hiện vật, vì vậy hãy chọn theo rủi ro.
- Chi phí của yêu cầu kém được trả muộn và nhân lên; đầu tư sớm là đòn bẩy chống lại việc làm lại và chấp nhận thất bại.

## Tài liệu tham khảo và đọc thêm

- IEEE và ISO/IEC, *Guide to the Software Engineering Body of Knowledge (SWEBOK)*, lĩnh vực kiến thức Yêu cầu Phần mềm
- Karl Wiegers và Joy Beatty, *Software Requirements*
- ISO/IEC/IEEE 29148, *Systems and software engineering: Life cycle processes: Requirements engineering*
- Suzanne Robertson và James Robertson, *Mastering the Requirements Process*
- Dean Leffingwell, *Agile Software Requirements*
- Mike Cohn, *User Stories Applied*
- Ian Sommerville, *Software Engineering* (các chương về kỹ thuật yêu cầu)
