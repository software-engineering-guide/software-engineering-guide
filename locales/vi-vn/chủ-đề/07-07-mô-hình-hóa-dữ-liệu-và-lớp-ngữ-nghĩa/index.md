# 7.7 Mô hình hóa dữ liệu và lớp ngữ nghĩa

## Tổng quan và động lực

Một [mô hình dữ liệu](https://en.wikipedia.org/wiki/Data_model) là một quyết định về dữ liệu của bạn có nghĩa gì, được đưa ra trước khi bạn quyết định dữ liệu sống ở đâu. Nó gọi tên những thứ doanh nghiệp quan tâm, các thuộc tính mô tả chúng, và các quan hệ giữa chúng. Lưu trữ, chỉ mục, định dạng tệp và công cụ truy vấn đều đến sau. Thứ tự này quan trọng vì ý nghĩa của dữ liệu sống lâu hơn mọi công nghệ bạn dùng để giữ nó. Kho dữ liệu bị thay thế, định dạng bảng đổi, công cụ truy vấn đến rồi đi, nhưng "khách hàng," "đơn hàng" và "người dùng hoạt động" phải có cùng nghĩa qua tất cả chúng, trong nhiều năm.

Với một đội nhỏ, mô hình hóa thường ngầm. Một kỹ sư giữ toàn bộ lược đồ trong đầu, và hiểu biết chung về "doanh thu" sống sót vì chỉ có ba người để bất đồng. Ở quy mô của các tổ chức phát triển lớn, doanh nghiệp và cơ quan chính phủ, sự không chính thức đó sụp đổ đúng theo cách mô tả trong chương 7.1 (chiến lược và quản trị dữ liệu). Hàng chục đội xây hàng trăm bảng, mỗi đội có ý tưởng riêng về một "phiên" là gì hay khi nào một người dùng được tính là "hoạt động." Hai bảng điều khiển hiển thị hai con số khác nhau cho cùng một tuần, và một cuộc họp lãnh đạo biến thành tranh cãi về truy vấn của ai đúng thay vì nên làm gì tiếp. Mô hình hóa tồi không tự báo hiệu. Nó nổi lên nhiều tháng sau như công việc đối chiếu, kiểm toán thất bại, và quyết định đưa ra trên những con số không ai bảo vệ được.

Chương này nói về việc làm công việc đó một cách có chủ đích. Nó bao quát mô hình khái niệm, logic và vật lý; mô hình hóa thực thể-quan hệ; khi nào chuẩn hóa và khi nào phi chuẩn hóa; mô hình hóa khác nhau thế nào cho khối lượng công việc giao dịch so với phân tích; mô hình hóa chiều với bảng sự kiện và chiều; và lớp ngữ nghĩa giữ định nghĩa được quản trị duy nhất của mọi chỉ số kinh doanh. Lợi ích không phải sự thanh lịch vì chính nó. Mà là "người dùng hoạt động" và "doanh thu" có một nghĩa ở mọi nơi, để các đội tin được các con số và nhờ đó đi nhanh hơn.

*Xem thêm:* chương 3.4 (kiến trúc dữ liệu và lưu trữ), chương 7.3 (phân tích và trí tuệ kinh doanh), và chương 11.5 (chỉ số hiệu suất chính).

## Các nguyên tắc chính

- Quyết định dữ liệu có nghĩa gì trước khi bạn quyết định nó sống ở đâu.
- Mô hình hóa ở ba cấp: khái niệm (kinh doanh), logic (cấu trúc), vật lý (triển khai).
- Chuẩn hóa để bảo vệ tính đúng trong hệ thống giao dịch; phi chuẩn hóa có chủ đích cho tốc độ phân tích.
- Khớp mô hình với khối lượng công việc: giao dịch và phân tích có nhu cầu đối lập.
- Mỗi chỉ số kinh doanh có đúng một định nghĩa được quản trị, và nó sống trong lớp ngữ nghĩa.
- Chiều đồng nhất cho phép các đội độc lập nối và so sánh dữ liệu an toàn.
- Độ chi tiết (grain) là quyết định thiết kế bạn đưa ra có chủ đích, không phải tai nạn của một truy vấn.
- Mô hình là tài sản sống: đặt tên tốt, lập tài liệu, và giữ chúng tiến hóa được.

## Khuyến nghị

### Mô hình hóa ở ba cấp, theo thứ tự

Hãy làm việc từ ý nghĩa ra ngoài. Bắt đầu với mô hình khái niệm: các thực thể doanh nghiệp quan tâm và quan hệ của chúng, viết bằng ngôn ngữ đơn giản mà một chuyên gia miền kiểm tra được. "Một khách hàng đặt nhiều đơn hàng; một đơn hàng chứa nhiều dòng hàng; mỗi dòng hàng tham chiếu một sản phẩm." Chưa có khóa, kiểu hay bảng. Rồi xây mô hình logic thêm cấu trúc: thuộc tính, khóa chính và khóa ngoại, bản số quan hệ, và ràng buộc, vẫn độc lập với bất kỳ cơ sở dữ liệu cụ thể nào. [Mô hình hóa thực thể-quan hệ](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) là ký hiệu chuẩn ở đây, và sơ đồ thực thể-quan hệ là hiện vật bạn rà soát với cả kỹ sư lẫn các bên liên quan kinh doanh. Chỉ khi đó mới tạo mô hình vật lý: các bảng, cột, kiểu dữ liệu, chỉ mục, phân vùng và bố cục lưu trữ thực cho công cụ bạn chọn. Nhảy đến thiết kế vật lý là sai lầm mô hình hóa phổ biến nhất, vì nó nướng các lựa chọn công nghệ hôm nay vào những quyết định đáng ra phải sống lâu hơn chúng.

### Chuẩn hóa hệ thống giao dịch, phi chuẩn hóa hệ thống phân tích có chủ đích

Với các hệ thống ghi giao dịch, hãy ưu tiên [chuẩn hóa cơ sở dữ liệu](https://en.wikipedia.org/wiki/Database_normalization). Các dạng chuẩn loại bỏ dư thừa để mỗi sự kiện được lưu một lần, ngăn dị thường cập nhật và giữ việc ghi đúng khi nhiều người dùng đồng thời thay đổi dữ liệu. Đây là mặc định đúng cho [xử lý giao dịch trực tuyến](https://en.wikipedia.org/wiki/Online_transaction_processing) (OLTP), nơi tính đúng dưới ghi đồng thời quan trọng hơn tốc độ của bất kỳ truy vấn phân tích đơn lẻ nào. Hệ thống phân tích có ưu tiên đối lập. Chúng nặng đọc, chúng quét và tổng hợp các khoảng khổng lồ, và nối hàng chục bảng chuẩn hóa lúc truy vấn thì chậm và khó suy luận. Ở đó bạn phi chuẩn hóa có chủ đích, gộp các thuộc tính liên quan lại để truy vấn đơn giản và nhanh hơn. Kỷ luật là phi chuẩn hóa một cách có chủ đích, với lý do có tài liệu, thay vì để dư thừa len vào do tai nạn. Chương 3.4 (kiến trúc dữ liệu và lưu trữ) bao quát các công cụ làm mỗi mẫu hoạt động tốt.

### Dùng mô hình hóa chiều cho phân tích

Với khối lượng công việc phân tích, hãy áp dụng [mô hình hóa chiều](https://en.wikipedia.org/wiki/Dimensional_modeling), cách tiếp cận được Ralph Kimball phổ biến. Bạn chia thế giới thành sự kiện và chiều. Bảng sự kiện giữ các phép đo của một quy trình kinh doanh: số tiền của một giao dịch bán, thời lượng của một cuộc gọi, số lượng đã giao. Bảng chiều giữ bối cảnh mô tả bạn lọc và nhóm theo: khách hàng, sản phẩm, cửa hàng, ngày. Sắp xếp một bảng sự kiện được bao quanh bởi các chiều của nó và bạn có một [lược đồ hình sao](https://en.wikipedia.org/wiki/Star_schema), dễ cho nhà phân tích hiểu và nhanh cho công cụ truy vấn. Chuẩn hóa các chiều đó thành bảng con và bạn có lược đồ bông tuyết, tiết kiệm một ít lưu trữ với cái giá nhiều phép nối và phức tạp hơn; hãy ưu tiên hình sao trừ khi bạn có lý do cụ thể. Với các môi trường rất lớn, chịu quy định cao nơi khả năng kiểm toán và theo dõi nguồn chiếm ưu thế, cách tiếp cận data vault mô hình hóa trung tâm, liên kết và vệ tinh để nắm bắt lịch sử và dòng gốc một cách quyết liệt, với cái giá nhiều bảng hơn và đường cong học dốc hơn. Hầu hết đội nên bắt đầu với hình sao kiểu Kimball và chỉ với tới data vault khi yêu cầu kiểm toán biện minh.

### Cố định độ chi tiết và xử lý chiều thay đổi tường minh

Trước khi thêm một cột vào bảng sự kiện, hãy nêu độ chi tiết của nó: chính xác một hàng đại diện cho cái gì. "Một hàng cho mỗi dòng hàng." "Một hàng cho mỗi người dùng mỗi ngày." Độ chi tiết là nền móng của một mô hình đúng, vì mọi số đo và mọi chiều hoặc khớp độ chi tiết đó hoặc không thuộc về bảng. Trộn các độ chi tiết là cách bạn có doanh thu đếm đôi. Rồi quyết định các chiều thay đổi theo thời gian thế nào. Một khách hàng chuyển đến thành phố mới; bạn ghi đè giá trị cũ, giữ toàn bộ lịch sử, hay chỉ theo dõi giá trị hiện tại và trước đó? Đây là các mẫu [chiều thay đổi chậm](https://en.wikipedia.org/wiki/Slowly_changing_dimension) chuẩn, và chọn sai nghĩa là báo cáo lịch sử của bạn lặng lẽ viết lại quá khứ. Hãy quyết định độ chi tiết và chiến lược thay đổi từ trước, viết chúng vào tài liệu mô hình, và giữ vững trong rà soát.

### Xây một lớp ngữ nghĩa làm định nghĩa duy nhất của mọi chỉ số

Đây là khuyến nghị trả giá cho cả chương. Một [lớp ngữ nghĩa](https://en.wikipedia.org/wiki/Semantic_layer) nằm giữa các bảng vật lý và mọi công cụ tiêu thụ chúng, và nó giữ định nghĩa được quản trị duy nhất của mỗi chỉ số kinh doanh. "Người dùng hoạt động" được xác định một lần, dưới dạng mã, với logic chính xác: sự kiện nào tính, trong cửa sổ nào, loại trừ tài khoản nội bộ nào. "Doanh thu" được xác định một lần, gồm cách xử lý hoàn tiền, giảm giá và quy đổi tiền tệ. Mọi bảng điều khiển, sổ tay, báo cáo và công việc reverse-ETL đọc định nghĩa đó thay vì triển khai lại trong một truy vấn đặt riêng. Khi định nghĩa đổi, nó đổi ở một nơi và mọi người tiêu dùng cập nhật cùng nhau. Đây là cơ chế làm định nghĩa chỉ số được quản trị thành hiện thực chứ không phải khát vọng, và nó là sự triển khai trực tiếp điều chương 11.5 (chỉ số hiệu suất chính) yêu cầu. Hãy coi định nghĩa chỉ số như mã có phiên bản với chủ sở hữu, rà soát và kiểm thử, đúng như chương 7.1 yêu cầu bạn coi dữ liệu là sản phẩm.

### Thiết lập quy ước, đặt tên và tài liệu

Nhất quán là một tính năng. Hãy áp dụng quy ước đặt tên và thực thi chúng: một quy ước cho tên bảng, một quy ước cho khóa, một chuẩn cho cột ngày, một quy tắc đánh dấu sự kiện so với chiều. Quyết định một lần có dùng tên thực thể số ít hay số nhiều và đừng bao giờ trộn. Lập tài liệu mỗi mô hình nơi những người dùng nó sẽ tìm: ý nghĩa của mỗi bảng, độ chi tiết của mỗi sự kiện, định nghĩa của mỗi chỉ số, và chủ sở hữu của mỗi cái. Đặt tên và tài liệu tốt là thứ cho một nhà phân tích mới tự phục vụ thay vì làm gián đoạn đội, và là thứ cho kiểm toán viên truy vết một con số từ bộ slide hội đồng về nguồn mà không cần hướng dẫn.

### Giữ mô hình tiến hóa được

Mô hình của bạn sẽ thay đổi, nên hãy thiết kế cho thay đổi. Thêm cột thay vì tái sử dụng cột hiện có. Dùng khóa thay thế để một thay đổi trong khóa tự nhiên của hệ thống nguồn không lan khắp kho dữ liệu. Đánh phiên bản định nghĩa chỉ số và ngừng hỗ trợ chúng có thông báo thay vì lặng lẽ sửa dưới các bảng điều khiển đang chạy. Giữ các phép biến đổi trong quản lý phiên bản, đã kiểm thử, được rà soát, để một thay đổi về "người dùng hoạt động" nghĩa là gì là một pull request có diff và người phê duyệt, không phải một chỉnh sửa lặng lẽ trong công cụ BI. Một mô hình bạn không tiến hóa an toàn được trở thành mô hình người ta đi vòng, và định nghĩa bóng là cách nguồn sự thật duy nhất chết.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Chuẩn hóa (3NF) | Ghi đúng, không dư thừa, linh hoạt | Phép nối phân tích chậm, truy vấn phức tạp | OLTP và hệ thống vận hành |
| Lược đồ hình sao (Kimball) | Nhanh, trực quan, thân thiện nhà phân tích | Một ít dư thừa, ETL phải bảo trì | Hầu hết phân tích và BI |
| Lược đồ bông tuyết | Ít lưu trữ hơn, chiều sạch hơn | Nhiều phép nối hơn, phức tạp hơn | Chiều lớn, được quản trị chặt |
| Data vault | Toàn bộ lịch sử, kiểm toán được, tải linh hoạt | Nhiều bảng, đường cong học dốc | Chịu quy định cao, nặng kiểm toán |
| Lớp ngữ nghĩa trên các mô hình | Một định nghĩa ở mọi nơi, không phụ thuộc công cụ | Xây ban đầu, cần chủ sở hữu | Tổ chức đa đội, đa công cụ |

Căng thẳng trung tâm là tốc độ của một truy vấn đơn lẻ so với tính đúng và linh hoạt trên toàn hệ sinh thái. Chuẩn hóa bảo vệ tính đúng và trả giá bằng độ phức tạp truy vấn; mô hình chiều mua tốc độ truy vấn và sự rõ ràng và trả giá bằng ETL và một ít dư thừa được quản lý. Không có người thắng phổ quát, đó là lý do bạn khớp mô hình với khối lượng công việc thay vì chọn một cái yêu thích. Lớp ngữ nghĩa giải quyết căng thẳng thứ hai, giữa nhiều đội và nhiều công cụ, bằng cách làm định nghĩa chỉ số độc lập với bất kỳ cái nào trong số chúng. Sai lầm là coi những thứ này như phe phái tư tưởng. Một tổ chức khỏe mạnh chạy hệ thống OLTP chuẩn hóa, mô hình phân tích chiều được nuôi từ chúng, và một lớp ngữ nghĩa ở trên, mỗi cái làm việc nó giỏi.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi hai bảng điều khiển hiển thị con số khác nhau cho cùng một chỉ số, định nghĩa của ai thắng, và định nghĩa đó thực sự sống ở đâu?** Câu hỏi này phơi bày liệu bạn thực sự có một nguồn sự thật duy nhất hay chỉ tin là có. Trong hầu hết đội lớn, câu trả lời trung thực là "người dùng hoạt động" được định nghĩa lại trong cả chục truy vấn, và người thắng là ai cãi to nhất trong cuộc họp. Hãy mang bằng chứng thật: chọn một chỉ số, tìm mọi nơi nó được tính, và so sánh logic từng dòng. Bạn gần như chắc chắn sẽ tìm thấy bất đồng thầm lặng về cửa sổ, loại trừ và trường hợp biên. Câu trả lời nên thúc đẩy một quyết định xây lớp ngữ nghĩa nơi mỗi chỉ số được xác định một lần, dưới dạng mã được rà soát, để câu hỏi thôi là về con người và bắt đầu là về một hiện vật có phiên bản. Cho đến khi định nghĩa đó có một ngôi nhà vật lý duy nhất, mọi lần đối chiếu chỉ là tạm thời.

2. **Độ chi tiết của bảng sự kiện quan trọng nhất của bạn là gì, và mọi người trong phòng có phát biểu nó giống nhau không?** Độ chi tiết là nền móng thầm lặng mà hầu hết thất bại mô hình hóa truy về. Nếu một nửa đội nói "một hàng cho mỗi đơn hàng" và nửa kia nói "một hàng cho mỗi dòng hàng," bạn có một lỗi đếm đôi đang chờ nổi lên trong báo cáo doanh thu. Hãy mang bảng thực và yêu cầu mỗi người mô tả một hàng trong một câu. Bất đồng ở đây không phải vấn đề giao tiếp để làm êm; mà là khiếm khuyết thiết kế cần sửa trước khi thêm số đo chồng lên nó. Câu trả lời nên được viết vào tài liệu mô hình và thực thi trong rà soát, vì một khi nhà phân tích xây truy vấn trên độ chi tiết mơ hồ, sự mơ hồ lan nhanh hơn bạn sửa được.

3. **Mô hình này sẽ hấp thụ thay đổi thế nào, và điều gì xảy ra với báo cáo năm ngoái khi một định nghĩa dịch chuyển?** Mọi mô hình đối mặt hệ thống nguồn thay đổi, quy tắc kinh doanh thay đổi và định nghĩa chỉ số thay đổi, nên câu hỏi thực là thay đổi là một pull request được kiểm soát hay một chỉnh sửa lặng lẽ viết lại lịch sử. Hãy mang một ví dụ gần đây: một chỉ số có định nghĩa đã đổi, hoặc một khóa nguồn bị đổi tên, và truy vết điều gì xảy ra với các bảng điều khiển hiện có. Nếu một chiều thay đổi chậm được xử lý bằng ghi đè, báo cáo lịch sử của bạn có thể đã lặng lẽ đổi giá trị quá khứ, là vấn đề nghiêm trọng với bất kỳ ai làm phân tích xu hướng hoặc báo cáo chịu quy định. Câu trả lời nên đẩy bạn về khóa thay thế, định nghĩa chỉ số có phiên bản, chiến lược thay đổi tường minh, và phép biến đổi được giữ trong quản lý phiên bản có rà soát. Một mô hình không ai thay đổi an toàn được trở thành mô hình người ta bỏ rơi.

4. **Những chiều nào phải có cùng nghĩa qua mọi đội, và ai chịu trách nhiệm sở hữu từng cái?** Chiều đồng nhất là thứ cho tiếp thị, tài chính và vận hành nối dữ liệu của họ và nhận câu trả lời so sánh được, nhưng chỉ khi "khách hàng," "sản phẩm," "khu vực" và "ngày" mang một định nghĩa thống nhất thay vì một bản sao riêng cho từng đội. Lực kéo đối lập là tự chủ: mỗi đội muốn mô hình hóa thế giới riêng theo tốc độ riêng, và ép một chiều dùng chung làm họ chậm lại ngắn hạn trong khi sinh lời trên toàn hệ sinh thái. Hãy mang hai ba chiều xuất hiện trong nhiều báo cáo xuyên đội nhất, liệt kê mọi phiên bản của từng cái hiện tồn tại, và xem khóa cùng thuộc tính của chúng thực sự phân kỳ đến đâu. Hãy nêu một chủ sở hữu cho mỗi chiều đồng nhất, vì một chiều dùng chung không chủ sở hữu trôi về bản sao riêng trong vòng một quý. Trong bối cảnh doanh nghiệp và chính phủ, nơi con số của một bộ được so sánh với bộ khác công khai, một chiều chưa đồng nhất là sự khác biệt giữa một phép so sánh trung thực và một điều sai sự thật vô tình, nên hãy quyết định sớm chiều nào được quản trị tập trung và chiều nào ở lại cục bộ.

5. **Ranh giới giữa hệ thống giao dịch chuẩn hóa và mô hình phân tích phi chuẩn hóa của bạn nằm ở đâu, và mọi sự phi chuẩn hóa có phải quyết định có chủ đích không?** Khớp mô hình với khối lượng công việc là kỷ luật cốt lõi, vậy mà ranh giới chính là nơi nó mờ đi: một nhà phân tích phi chuẩn hóa bảng kho dữ liệu cho nhanh, một kỹ sư chuẩn hóa bảng báo cáo theo thói quen, và không ai ghi lại mỗi lựa chọn thuộc phía nào. Căng thẳng là tốc độ của một truy vấn đơn lẻ so với tính đúng và linh hoạt trên mọi thứ, và những người hợp lý đáp xuống khác nhau tùy họ sở hữu ghi hay đọc. Hãy mang truy vấn phân tích chậm nhất và bảng giao dịch tranh chấp nhiều nhất của bạn, và hỏi với mỗi cột dư thừa liệu sự dư thừa đó được chọn với lý do có tài liệu hay len vào do tai nạn. Mục tiêu là một quy tắc bằng văn bản về khi nào phi chuẩn hóa được phép và ai ký duyệt, không phải cuộc thi thuần túy. Với tổ chức lớn hay chịu quy định, ranh giới này cũng quyết định nơi dữ liệu cá nhân bị nhân bản, nên một sự phi chuẩn hóa không tài liệu vừa là câu hỏi hiệu năng vừa là phơi nhiễm quản trị dữ liệu mà ai đó cuối cùng sẽ phải giải thích với kiểm toán viên.

6. **Bạn nên xây hay mua lớp ngữ nghĩa, và ai chịu trách nhiệm giữ mọi định nghĩa chỉ số hiện hành một khi nó tồn tại?** Một lớp ngữ nghĩa chỉ mang lại một nguồn sự thật duy nhất khi nó được sở hữu và bảo trì, nên lựa chọn công cụ ít quan trọng hơn câu trả lời cho ai rà soát một thay đổi về "doanh thu" nghĩa là gì và ai chịu trách nhiệm khi một định nghĩa cũ đi. Các cân nhắc đối lập là thật: xây cho bạn kiểm soát và vừa ngăn xếp của bạn nhưng thêm gánh nặng kỹ thuật, trong khi mua công cụ chỉ số nhanh hơn nhưng rủi ro khóa chặt và ngôn ngữ định nghĩa bạn không kiểm soát hoàn toàn. Hãy mang một nhúm chỉ số rủi ro cao nhất của bạn, các công cụ tiêu thụ chúng hôm nay, và một cái đọc trung thực về liệu có ai hiện sở hữu các định nghĩa đó hay chúng chỉ đơn giản tồn tại. Hãy quyết định từ trước liệu định nghĩa sống như mã có phiên bản với chủ sở hữu có tên và kiểm thử, vì một lớp ngữ nghĩa không ai bảo trì mục rữa thành chính những định nghĩa rải rác mà nó định thay thế. Trong báo cáo doanh nghiệp và chính phủ, nơi một chỉ số trên bảng điều khiển công khai phải truy vết được về một định nghĩa có tài liệu, được rà soát, quyền sở hữu đó và khả năng chứng minh dòng gốc của một con số là thứ biến lớp ngữ nghĩa từ tiện ích thành kiểm soát kiểm toán được.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Mô hình hóa có thể chờ, nhưng định nghĩa thì không. Với hai kỹ sư và không có đường băng để xây kho dữ liệu, hãy đặt một lớp ngữ nghĩa nhỏ trong công cụ biến đổi của bạn và định nghĩa hai ba chỉ số hội đồng thực sự theo dõi, "người dùng hoạt động" và "doanh thu," một lần dưới dạng mã đã kiểm thử. Bỏ qua data vault và lược đồ chiều cầu kỳ; một hình sao mỏng và một nhúm định nghĩa được quản trị mua cho bạn con số nhất quán mà không làm chậm phân phối. Lợi ích là việc chuẩn bị họp hội đồng thôi là tranh cãi về truy vấn của ai đúng.

**Doanh nghiệp nhỏ.** Bạn không có người mô hình hóa dữ liệu và không có ngân sách cho nền tảng chỉ số, vì vậy hãy dựa vào các định nghĩa dựng sẵn trong công cụ bạn đã chạy và viết ra vài cái quan trọng trong một tài liệu chung mọi người đọc. Ưu tiên mua phân tích nhúng trong phần mềm hiện có hơn là dựng một kho dữ liệu bạn không bố trí nhân sự nổi. Nơi bạn mô hình hóa, hãy giữ đơn giản và đặt tên nhất quán, vì người bảo trì năm sau có thể là người không nhớ vì sao "khách hàng" từng có hai nghĩa. Nhất quán rẻ hơn đối chiếu.

**Doanh nghiệp lớn.** Vấn đề là nhiều đội và nhiều công cụ trôi vào định nghĩa riêng, vì vậy hãy đầu tư vào chiều đồng nhất, một lớp ngữ nghĩa được quản trị, và định nghĩa chỉ số giữ dưới dạng mã có phiên bản với chủ sở hữu và rà soát. Chuẩn hóa đặt tên, khai báo độ chi tiết và chiến lược chiều thay đổi chậm khắp hệ sinh thái để một con số trong công cụ này khớp với cùng con số trong công cụ khác. Hãy coi lớp ngữ nghĩa là sản phẩm với lộ trình và một đội sở hữu, và đo nó loại bỏ bao nhiêu thời gian đối chiếu. Lợi tức là con số đáng tin khắp doanh nghiệp và kiểm toán truy vết gọn gàng từ bộ slide hội đồng về nguồn.

**Chính phủ.** Minh bạch và khả năng so sánh xuyên cơ quan định hình công việc: dữ liệu tham chiếu chuẩn cho địa lý và nhân khẩu, định nghĩa được quản trị của các chỉ số cốt lõi, và phương pháp luận được công bố với các bản phát hành có phiên bản để công chúng truy vết bất kỳ con số nào về một định nghĩa có tài liệu. Quy tắc mua sắm có thể yêu cầu mô hình và định nghĩa của bạn vẫn di chuyển được và trung lập nhà cung cấp, nên tránh lớp ngữ nghĩa bị khóa vào một công cụ độc quyền. Hãy để từng cơ quan tự do mô hình hóa dữ liệu vận hành của mình trong khi tuân theo các chiều dùng chung cho bất cứ thứ gì báo cáo ở cấp quốc gia. Một chỉ số được công bố không truy vết được về một định nghĩa có phiên bản là thất bại trách nhiệm giải trình cũng nhiều như thất bại dữ liệu.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty Series A có ba định nghĩa của "người dùng hoạt động" sống ở ba nơi: công cụ phân tích sản phẩm, bảng tính tài chính và bộ slide nhà đầu tư. Các con số không bao giờ khớp, và mỗi lần chuẩn bị họp hội đồng thành một cuộc chạy vạy. Hai kỹ sư giới thiệu một lớp ngữ nghĩa nhỏ trong công cụ biến đổi của họ, xác định "người dùng hoạt động" và "doanh thu định kỳ hằng tháng" một lần dưới dạng mã đã kiểm thử, với các cửa sổ và loại trừ chính xác được viết ra. Mọi bảng điều khiển nay đọc các định nghĩa đó. Cuộc tranh cãi chuẩn bị họp hội đồng biến mất, và việc đưa một nhà phân tích mới vào từ một tuần tri thức truyền miệng thành đọc một mô hình có tài liệu. Điều này nối trực tiếp với kỷ luật mô tả trong chương 7.4 (phân tích sản phẩm và thử nghiệm), nơi một định nghĩa ổn định của "hoạt động" là thứ làm kết quả thử nghiệm so sánh được.

**Doanh nghiệp lớn.** Một nhà bán lẻ toàn cầu chạy năm công cụ trí tuệ kinh doanh qua tiếp thị, tài chính, chuỗi cung ứng, bán hàng hóa và cửa hàng, và mỗi công cụ đã phát minh lại "tỷ suất lợi nhuận gộp" hơi khác nhau. Họ xây một lớp ngữ nghĩa trên một kho dữ liệu kiểu Kimball với các chiều đồng nhất, để "sản phẩm," "cửa hàng" và "ngày" có cùng nghĩa qua mọi bảng sự kiện và mọi công cụ. Mỗi chỉ số được định nghĩa một lần và tiêu thụ ở mọi nơi. Những cuộc họp đối chiếu từng ngốn nhiều ngày mỗi quý phần lớn biến mất, và khi tài chính đổi cách hàng trả lại ảnh hưởng tỷ suất lợi nhuận, thay đổi lan đến cả năm công cụ cùng lúc. Các chiều đồng nhất là thứ cho các đội độc lập nối dữ liệu của họ với sự tự tin thay vì nghi ngờ.

**Chính phủ.** Một chính phủ quốc gia cần báo cáo so sánh được qua các cơ quan y tế, lao động và giáo dục, mỗi cơ quan trước đây định nghĩa "hộ gia đình," "khu vực" và "việc làm" theo cách riêng. Một cơ quan liên ngành thiết lập dữ liệu tham chiếu dùng chung và định nghĩa chuẩn: các bảng chiều chuẩn cho địa lý và nhân khẩu, và định nghĩa được quản trị của các chỉ số cốt lõi, được công bố kèm phương pháp luận và các bản phát hành có phiên bản. Từng cơ quan mô hình hóa dữ liệu vận hành của riêng mình nhưng tuân theo các chiều và định nghĩa dùng chung cho bất cứ thứ gì báo cáo ở cấp quốc gia. Kết quả là con số của một cơ quan có thể được so sánh trung thực với cơ quan khác, và công chúng truy vết được bất kỳ chỉ số được công bố nào về một định nghĩa có tài liệu, hỗ trợ nghĩa vụ minh bạch bao quát trong chương 7.1.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của mô hình hóa tốt và lớp ngữ nghĩa chủ yếu là thời gian thu hồi và lỗi tránh được. Trong nhiều tổ chức, nhà phân tích dành phần lớn thời gian tìm dữ liệu, đối chiếu các con số xung đột, và xây lại định nghĩa mà người khác đã viết. Một định nghĩa được quản trị duy nhất của mỗi chỉ số biến công việc lặp lại đó thành một khoản đầu tư một lần. Nó cũng loại bỏ cả một loại thất bại tốn kém: con số sai trong bộ slide hội đồng, con số báo cáo sai kích hoạt một phát hiện kiểm toán, dự án đối chiếu kéo dài cả quý chỉ tồn tại vì hai đội định nghĩa "doanh thu" khác nhau. Khi định nghĩa sống ở một nơi được rà soát, những thất bại đó phần lớn ngừng xảy ra.

Chi phí là thật và đáng gọi tên. Bạn đầu tư ban đầu vào mô hình hóa khái niệm và logic, vào xây dựng và điền lớp ngữ nghĩa, và vào quyền sở hữu liên tục giữ định nghĩa hiện hành. Tổng chi phí sở hữu (TCO) gồm công cụ, thời gian mô hình hóa và kỹ thuật phân tích, và quản trị để giữ mô hình khỏi trôi. Hãy cân nhắc điều đó so với chi phí của việc không làm, lớn hơn nhưng ẩn: nó hiện ra là đường ống trùng lặp, nhà phân tích như những động cơ đối chiếu bằng người, và giám đốc ra quyết định tự tin trên những con số không ai bảo vệ được. Hãy lập luận với ban lãnh đạo bằng thuật ngữ của họ. Một định nghĩa đáng tin của mọi chỉ số là thứ cho họ so sánh qua doanh nghiệp, tin bảng điều khiển, và trả lời cơ quan quản lý mà không có cuộc báo động. Hãy bắt đầu nơi nỗi đau đối chiếu tệ nhất, định nghĩa vài chỉ số đó một lần, và để thời gian thu hồi tài trợ phần còn lại.

## Phản mẫu và cạm bẫy

- Nhảy thẳng đến bảng vật lý, nướng công nghệ hôm nay vào những quyết định đáng ra sống lâu hơn nó.
- Định nghĩa cùng một chỉ số độc lập trong mọi bảng điều khiển, nên không hai con số nào khớp.
- Để độ chi tiết không được nêu, rồi phát hiện số đo bị đếm đôi trong báo cáo doanh thu.
- Phi chuẩn hóa bảng phân tích do tai nạn thay vì do quyết định có tài liệu.
- Chuẩn hóa một kho phân tích cho đến khi mọi truy vấn là phép nối mười hai bảng không ai hiểu.
- Xử lý chiều thay đổi chậm bằng ghi đè, nên báo cáo lịch sử lặng lẽ viết lại quá khứ.
- Dùng khóa tự nhiên ở mọi nơi, nên một thay đổi khóa hệ thống nguồn lan khắp kho dữ liệu.
- Xây lớp ngữ nghĩa không chủ sở hữu, nên định nghĩa trôi và lòng tin xói mòn.
- Coi mô hình là xong lúc ra mắt thay vì tài sản sống phải giữ tiến hóa được.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Mô hình hóa ngầm và phản ứng. Bảng được thiết kế vật lý-trước bởi ai cần chúng. Chỉ số được định nghĩa lại trong mỗi báo cáo, và con số thường xuyên xung đột. Độ chi tiết không được lập tài liệu, và không ai sở hữu định nghĩa.
- **Mức 2, Phát triển:** Một số bảng phân tích theo mẫu chiều, và vài chỉ số chính có định nghĩa bằng văn bản, nhưng chúng sống trong wiki và không được thực thi. Quy ước đặt tên có trên giấy. Thực hành khác nhau theo từng đội, và đối chiếu vẫn thường xuyên và thủ công.
- **Mức 3, Chuẩn hóa:** Mô hình khái niệm, logic và vật lý tách biệt và được rà soát. Một lớp ngữ nghĩa xác định các chỉ số cốt lõi một lần, dưới dạng mã có phiên bản với chủ sở hữu. Chiều đồng nhất cho phép các đội nối an toàn. Độ chi tiết và chiến lược chiều thay đổi chậm được lập tài liệu và thực thi trong rà soát toàn tổ chức.
- **Mức 4, Quản lý:** Hệ sinh thái mô hình được đo theo đường cơ sở. Bạn theo dõi độ phủ định nghĩa chỉ số (phần các chỉ số được báo cáo do lớp ngữ nghĩa phục vụ), số định nghĩa trùng hoặc bóng vẫn đang dùng, giờ đối chiếu mỗi quý, và tỷ lệ lỗi độ chi tiết và dòng gốc bị bắt trong rà soát so với trong môi trường sản xuất. Thay đổi định nghĩa chảy qua pull request được rà soát với kiểm thử, và độ mới, tỷ lệ đạt kiểm thử và độ trôi được theo dõi trên bảng điều khiển. Khi một chỉ số phân kỳ hoặc một chiều thôi đồng nhất, phép đo làm nó nổi lên trước một cuộc họp hội đồng.
- **Mức 5, Điều phối:** Mọi chỉ số quan trọng có một định nghĩa được quản trị mà mọi công cụ và đội tiêu thụ, và lớp ngữ nghĩa được tích hợp với phân tích, thử nghiệm và báo cáo chịu quy định. Mô hình tiến hóa được theo thiết kế và được tinh chỉnh liên tục; định nghĩa được tin cậy toàn tổ chức; công việc đối chiếu phần lớn đã biến mất. Tổ chức thường xuyên ngừng hỗ trợ, thu hẹp phạm vi, và đồng nhất chiều mới khi doanh nghiệp thay đổi, cân bằng lại hệ sinh thái mô hình như một tài sản thích ứng.

## Ý tưởng để thảo luận

1. Hãy chọn ba chỉ số quan trọng nhất của bạn. Hôm nay có bao nhiêu định nghĩa riêng biệt của mỗi cái qua các công cụ của bạn, và cần gì để thu chúng về một?
2. Một độ chi tiết không được nêu đã gây lỗi báo cáo thật ở đâu, và mất bao lâu để nhận ra?
3. Chiều nào của bạn nên được đồng nhất qua các đội trước, và ai sở hữu chúng?
4. Định nghĩa chỉ số của bạn nằm trong quản lý phiên bản có rà soát, hay sửa được lặng lẽ bên trong công cụ BI?
5. Lần cuối một chiều thay đổi chậm viết lại lịch sử của bạn mà không ai nhận ra là khi nào, và bạn sẽ bắt nó lần sau thế nào?
6. Nếu bạn thay công cụ kho dữ liệu ngày mai, bao nhiêu ý nghĩa của mô hình sẽ sống sót qua đợt chuyển?

## Những điểm cần ghi nhớ

- Mô hình hóa dữ liệu là quyết định dữ liệu có nghĩa gì, và ý nghĩa đó sống lâu hơn mọi công nghệ lưu trữ bạn chọn.
- Mô hình hóa ở ba cấp theo thứ tự: khái niệm, rồi logic, rồi vật lý.
- Chuẩn hóa hệ thống giao dịch cho tính đúng; phi chuẩn hóa hệ thống phân tích có chủ đích cho tốc độ.
- Dùng mô hình hóa chiều với bảng sự kiện, chiều và một độ chi tiết được nêu cho phân tích.
- Xây một lớp ngữ nghĩa để mọi chỉ số kinh doanh có một định nghĩa được quản trị duy nhất ở mọi nơi.
- Chiều đồng nhất cho phép các đội độc lập nối và so sánh dữ liệu của họ tự tin.
- Đặt tên tốt, lập tài liệu, dùng khóa thay thế và đánh phiên bản định nghĩa để mô hình tiến hóa được.

## Tài liệu tham khảo và đọc thêm

- Ralph Kimball và Margy Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling*.
- Bill Inmon, *Building the Data Warehouse*.
- Dan Linstedt và Michael Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Peter Chen, "The Entity-Relationship Model: Toward a Unified View of Data," ACM Transactions on Database Systems.
- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM.
- C. J. Date, *An Introduction to Database Systems*.
- Lars Rönnbäck và các đồng nghiệp, các bài viết về mô hình hóa neo (anchor modelling).
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*.
