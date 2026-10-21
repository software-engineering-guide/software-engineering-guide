# 2.20 Xử lý lỗi và mẫu thiết kế chịu lỗi

## Tổng quan và động lực

Mọi chương trình bạn viết rồi sẽ thất bại. Một đĩa đầy, một mạng rớt, một dịch vụ hết thời gian chờ, một bên gọi truyền vào rác, một phụ thuộc trả về thứ mà tài liệu chưa bao giờ nhắc đến. Câu hỏi không bao giờ là liệu thất bại có xảy ra không; mà là liệu mã của bạn đón nhận thất bại đó bằng một kế hoạch hay bằng một bất ngờ. Xử lý lỗi là nghề thủ công quyết định, từng dòng và từng hàm, mã của bạn làm gì khi thế giới không hợp tác. Đó là phần ít hào nhoáng nhất của xây dựng và là phần quyết định, hơn bất kỳ tính năng nào, liệu mọi người có tin hệ thống của bạn hay không.

Chương này nói về khả năng chịu lỗi ở cấp mã và thành phần: những lựa chọn bên trong một hàm, một mô-đun hay một API. Nó bổ sung cho chương 3.5, vốn bao quát khả năng chịu lỗi ở cấp hệ thống (cân bằng tải, nhân bản, chuyển đổi dự phòng qua các dịch vụ). Chương 3.5 giữ cho toàn bộ nền tảng đứng vững khi một khu vực tối đi; chương này giữ cho một yêu cầu đơn lẻ không làm hỏng dữ liệu của bạn hoặc biến mất không để lại dấu vết. Hai chương củng cố lẫn nhau. Một bộ ngắt mạch trong kiến trúc của bạn chẳng có nhiều ý nghĩa nếu mã đằng sau nó nuốt ngoại lệ, và một hàm phòng thủ không thể cứu bạn nếu hệ thống xung quanh không có dự phòng. Chương này cũng xây dựng trên chương 2.9 (xây dựng phần mềm), nơi xử lý lỗi chỉ là một kỷ luật trong nhiều kỷ luật; ở đây nó trở thành toàn bộ chủ đề.

Với các đội lớn, tính nhất quán là phần thưởng. Khi hàng trăm kỹ sư xử lý lỗi theo hàng trăm cách khác nhau, mỗi dịch vụ trở thành một câu đố và mỗi sự cố một cuộc khai quật. Trong bối cảnh doanh nghiệp, sự không nhất quán đó làm tăng chi phí của mọi cuộc kiểm toán và mọi tích hợp. Trong chính phủ và các hệ thống rủi ro cao khác, rủi ro sắc nét hơn: tính đúng đắn, thất bại an toàn và dấu vết kiểm toán rõ ràng không phải là những tính năng bạn thêm sau mà là các thuộc tính hệ thống phải có từ commit đầu tiên. Một hệ thống trợ cấp âm thầm tính sai, hay một hệ thống hồ sơ làm mất một thất bại mà không ghi lại, không chỉ là có lỗi. Nó không đáng tin theo cách xói mòn thể chế đằng sau nó.

## Các nguyên tắc chính

- Phân biệt khiếm khuyết, lỗi và thất bại, và xử lý từng cái ở đúng tầng.
- Chọn thất bại nhanh hay thất bại an toàn một cách có chủ đích, theo từng ngữ cảnh, không bao giờ do tình cờ.
- Làm cho hợp đồng xử lý lỗi của mọi hàm và API tường minh và trung thực.
- Xác thực tại các ranh giới; tin tưởng bên trong chúng; phòng thủ mà không hoang tưởng.
- Không bao giờ nuốt lỗi trong im lặng; hãy phơi bày nó, bọc nó, hoặc xử lý nó có chủ đích.
- Làm cho thử lại an toàn bằng tính lũy đẳng, thời gian chờ, độ lùi và độ nhiễu.
- Dành cho đường lỗi cùng sự chú ý thiết kế như đường suôn sẻ.

## Khuyến nghị

### Phân biệt khiếm khuyết, lỗi và thất bại

Từ vựng cẩu thả tạo ra xử lý cẩu thả, vì vậy hãy bắt đầu với các thuật ngữ rõ ràng. Một khiếm khuyết (fault) là một sai sót trong hệ thống: một lỗi, một cấu hình xấu, một phụ thuộc đang ngừng hoạt động. Một lỗi (error) là trạng thái nội bộ không đúng mà một khiếm khuyết tạo ra: một giá trị rỗng ở nơi lẽ ra phải có giá trị, một số dư không còn khớp. Một thất bại (failure) là thứ người quan sát bên ngoài thấy: yêu cầu trả về sai câu trả lời, hoặc không có câu trả lời. Một khiếm khuyết có thể gây ra nhiều lỗi, và nhiều lỗi có thể bị bắt trước khi bất kỳ lỗi nào trở thành thất bại hiển thị. Toàn bộ ý nghĩa của xử lý lỗi là phá vỡ chuỗi đó, bắt lỗi trước khi nó trở thành thất bại mà người dùng hay kiểm toán viên trải nghiệm.

Từ vựng này cũng cho bạn biết nơi cần hành động. Khiếm khuyết được giải quyết trong đánh giá, kiểm thử và cấu hình. Lỗi được giải quyết lúc chạy bằng các mẫu trong chương này. Thất bại được giải quyết bằng khả năng quan sát (chương 9.2) và bằng khả năng chịu lỗi cấp hệ thống của chương 3.5. Khi đội bạn chia sẻ những từ này, các buổi rà soát sự cố sắc bén hơn: bạn có thể nói chính xác chuỗi lẽ ra phải bị phá vỡ ở đâu và đã không bị phá, thay vì tranh cãi "lỗi" là gì.

### Chọn thất bại nhanh hay thất bại an toàn theo ngữ cảnh

[Thất bại nhanh](https://en.wikipedia.org/wiki/Fail-fast_system) nghĩa là dừng ngay khoảnh khắc có điều gì đó sai, từ chối tiếp tục trên trạng thái xấu để vấn đề nổi lên ồn ào và gần nguyên nhân của nó. Thất bại an toàn nghĩa là suy giảm vào một trạng thái đã biết, vô hại và tiếp tục phục vụ những gì bạn có thể phục vụ an toàn. Không cái nào đúng phổ quát, và kỹ năng là chọn theo ngữ cảnh. Trong phát triển và tại các ranh giới nội bộ, thất bại nhanh là bạn của bạn: một chương trình dừng khi một bất biến bị vi phạm trao cho bạn một dấu vết ngăn xếp ngắn thay vì một bí ẩn dài. Trên môi trường thực, ở rìa của một hệ thống hướng đến người dùng, thất bại an toàn thường thắng: một bảng gợi ý không trả về gì tốt hơn một trang thanh toán không tải được.

Hãy quyết định điều này một cách có chủ đích cho từng ranh giới và viết quyết định ra. Một thành phần điều khiển bay hoặc thiết bị y tế thất bại an toàn vào một trạng thái xác định vì tiếp tục trên dữ liệu hỏng có thể làm hại ai đó. Một lần ghi sổ cái thất bại nhanh vì ghi một bút toán sai tệ hơn không ghi. Sự ghép đôi sai nguy hiểm theo cả hai hướng: thất bại an toàn ở nơi bạn cần thất bại nhanh che giấu sự hỏng hóc, và thất bại nhanh ở nơi bạn cần thất bại an toàn biến một trục trặc mỹ phẩm thành một sự cố ngừng hoạt động.

### Chọn cơ chế báo hiệu lỗi và dùng nó nhất quán

Các ngôn ngữ cho bạn hai cách rộng để báo hiệu có điều gì đó sai. [Xử lý ngoại lệ](https://en.wikipedia.org/wiki/Exception_handling) ném một đối tượng lên ngăn xếp gọi cho đến khi một bộ xử lý bắt được nó, tách đường lỗi khỏi logic chính. Cách thay thế là giá trị lỗi tường minh: hàm trả về cả kết quả và lỗi, và bên gọi phải kiểm tra cả hai. Nhiều ngôn ngữ hiện đại chính thức hóa cách sau bằng một [kiểu Result](https://en.wikipedia.org/wiki/Result_type), thường gọi là Result hoặc Either, buộc bên gọi mở ra hoặc thành công hoặc thất bại trước khi dùng giá trị. Mỗi cách có một cái giá. Ngoại lệ giữ đường suôn sẻ sạch nhưng có thể che giấu luồng điều khiển và cám dỗ lập trình viên vào các khối bắt tất cả xóa thông tin. Kết quả tường minh làm mọi thất bại hiển thị trong chữ ký kiểu nhưng thêm nghi thức và có thể bị bỏ qua nếu ngôn ngữ không buộc kiểm tra.

Câu trả lời đúng ít về cơ chế nào mà nhiều về tính nhất quán và trung thực. Hãy chọn thành ngữ mà ngôn ngữ và hệ sinh thái của bạn ưa chuộng, và áp dụng nó đồng nhất qua các dịch vụ để người đọc luôn biết thất bại di chuyển thế nào. Dành ngoại lệ cho các điều kiện thực sự ngoại lệ, không phải luồng điều khiển thông thường như "không tìm thấy người dùng", vốn được mô hình hóa tốt hơn như một kết quả bình thường. Dù chọn gì, đừng bao giờ để một thất bại trở nên vô hình: một giá trị lỗi không được kiểm tra nguy hiểm như một khối catch rỗng. Trong một cơ sở mã lớn, một quy ước bằng văn bản cộng một linter đánh dấu các lỗi bị bỏ qua thắng sở thích của bất kỳ cá nhân nào.

### Làm cho hợp đồng xử lý lỗi tường minh

Mọi hàm và mọi API đều có một hợp đồng xử lý lỗi, dù có ai viết ra hay không. Nó trả lời: điều gì có thể sai ở đây, bạn sẽ biết về nó thế nào, và điều gì được đảm bảo về trạng thái khi nó xảy ra? Hãy làm hợp đồng đó tường minh. Lập tài liệu những lỗi nào một hàm có thể trả về hoặc ném, phân biệt lỗi phục hồi được (bên gọi có thể thử lại hoặc dự phòng một cách hợp lý) với lỗi không phục hồi được (bên gọi không thể sửa và nên lan truyền hoặc hủy), và nêu hàm có để nguyên trạng thái khi thất bại không. Thuộc tính cuối này, đôi khi gọi là đảm bảo ngoại lệ mạnh, nghĩa là một lệnh gọi thất bại giống như nó chưa từng xảy ra, đúng là điều cho phép bên gọi thử lại an toàn.

Với một API công khai hoặc liên đội, hợp đồng này là một phần của giao diện, thực như các kiểu tham số. Hãy thiết kế một phân loại lỗi nhỏ, ổn định: một tập hữu hạn các loại như lỗi xác thực, không tìm thấy, xung đột, không được ủy quyền, phụ thuộc không khả dụng và lỗi nội bộ. Bên gọi khi đó có thể rẽ nhánh theo loại mà không phải phân tích chuỗi. Một phân loại rõ ràng làm xử lý lỗi kết hợp được qua nhiều dịch vụ, và nó làm thất bại có thể kiểm toán, vì mọi thất bại ánh xạ đến một loại đã biết, có tên.

### Xác thực tại các ranh giới và phòng thủ mà không hoang tưởng

Hãy coi dữ liệu đi qua một ranh giới tin cậy (một yêu cầu mạng, một tệp, đầu vào người dùng, một thông điệp từ dịch vụ khác) là thù địch cho đến khi được xác thực, và xác thực nó tại ranh giới, một lần, kỹ lưỡng. Đây là [lập trình phòng thủ](https://en.wikipedia.org/wiki/Defensive_programming) áp dụng bằng phán đoán. Bên trong một mô-đun mà đầu vào của nó bạn đã xác thực, các kiểm tra dư thừa trên mỗi dòng che giấu logic và triệt tiêu chính những thất bại bạn muốn thấy. Kỷ luật là: phòng thủ mạnh ở rìa, tin tưởng bên trong. Xác thực cấu trúc, phạm vi và bất biến nơi dữ liệu đi vào, chuyển nó thành các kiểu khiến trạng thái bất hợp lệ không thể biểu diễn, và để mã bên trong giả định nó đang làm việc với dữ liệu sạch.

Hoang tưởng có chi phí thực. Mã bị nhấn chìm trong các kiểm tra rỗng và nhánh phòng thủ khó đọc hơn, và tệ hơn, nó thường biến một thất bại rõ ràng thành một cái nhún vai im lặng, trả về một giá trị mặc định ở nơi lẽ ra phải báo động. Sự phòng thủ che giấu lỗi không phải là an toàn; nó là trì hoãn.

### Làm cho thử lại an toàn, có giới hạn và lịch sự

Nhiều khiếm khuyết mang tính tạm thời: một gián đoạn mạng thoáng qua, một dịch vụ khởi động lại, một sự tranh chấp khóa ngắn. Trong bất kỳ hệ thống phân tán nào (chương 3.3), những thất bại một phần này là trường hợp bình thường chứ không phải ngoại lệ. Thử lại là phản ứng tự nhiên, nhưng một vòng thử lại ngây thơ là một khẩu súng đã nạp đạn. Trước tiên, hãy làm thao tác bạn thử lại [lũy đẳng](https://en.wikipedia.org/wiki/Idempotence), nghĩa là thực hiện nó hai lần có cùng tác dụng như thực hiện một lần. Không có tính lũy đẳng, một lần thử lại sau hết thời gian chờ có thể tính phí thẻ hai lần hoặc tạo hai bản ghi, vì bạn không thể biết lần thử đầu thất bại hay chỉ là xác nhận của nó bị mất. Hãy dùng khóa lũy đẳng cho các thao tác ghi để bên nhận có thể nhận ra và loại bỏ trùng lặp một lần lặp lại.

Thứ hai, đặt thời gian chờ trên mọi lệnh gọi từ xa để một phụ thuộc bị treo không thể treo bạn. Thứ ba, giãn cách các lần thử lại bằng [độ lùi lũy thừa](https://en.wikipedia.org/wiki/Exponential_backoff), nhân đôi thời gian chờ sau mỗi lần thử, và thêm độ nhiễu (một độ trễ ngẫu nhiên nhỏ) để một nghìn máy khách phục hồi cùng lúc không đồng bộ thành một cơn giẫm đạp đánh sập lại dịch vụ đang phục hồi. Thứ tư, giới hạn số lần thử lại và tổng thời gian, rồi bỏ cuộc một cách êm ái. Thử lại không có giới hạn, độ lùi, độ nhiễu và tính lũy đẳng là một trong những cách phổ biến nhất để một trục trặc nhỏ trở thành sự cố ngừng hoạt động do chính mình gây ra.

### Thêm bộ ngắt mạch, vách ngăn và suy giảm êm ái trong mã

Khi một phụ thuộc thực sự ngừng hoạt động, thử lại nó chỉ lãng phí công sức và đào sâu cái hố. Một [bộ ngắt mạch](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) theo dõi tỷ lệ thất bại của các lệnh gọi đến một phụ thuộc và, một khi thất bại vượt ngưỡng, "mở" để thất bại ngay lập tức trong một khoảng thời gian làm nguội thay vì chờ các lệnh gọi vô vọng. Sau thời gian làm nguội nó cho một lệnh gọi thử đi qua và đóng lại nếu phụ thuộc đã phục hồi. Điều này bảo vệ cả bên gọi của bạn (thất bại nhanh, dễ đoán thay vì thời gian chờ chồng chất) lẫn phụ thuộc đang chật vật (chỗ thở để phục hồi). Mẫu vách ngăn, đặt theo tên các khoang kín nước của con tàu, cô lập tài nguyên để một phụ thuộc bão hòa không thể tiêu thụ mọi luồng hoặc kết nối và đánh chìm cả tiến trình; bạn cho mỗi phụ thuộc nhóm có giới hạn riêng của nó.

Những mẫu này kết hợp với suy giảm êm ái ở cấp mã: khi một phụ thuộc không thiết yếu không khả dụng, hãy trả về kết quả thu hẹp nhưng hữu ích thay vì một lỗi. Hiển thị dữ liệu được lưu đệm kèm ghi chú về độ cũ, ẩn bảng cá nhân hóa, xếp hàng việc ghi để sau. Đây là phần bổ sung cục bộ cho khả năng chịu lỗi cấp hệ thống của chương 3.5: kiến trúc cung cấp dự phòng qua các máy, và mã của bạn cung cấp hành vi hợp lý khi một mảnh bị thiếu.

### Bọc lỗi với ngữ cảnh và không bao giờ nuốt chúng

Một lỗi có nội dung "connection refused" cách mười tầng so với nơi nó xảy ra gần như vô dụng. Khi một lỗi lan truyền, hãy bọc nó với ngữ cảnh: bạn đang cố làm gì, thực thể hay yêu cầu nào, phụ thuộc nào, trong khi giữ nguyên nguyên nhân gốc để gốc không bị mất. Các ngôn ngữ và thư viện tốt hỗ trợ trực tiếp việc xâu chuỗi lỗi này. Mục tiêu là một dòng nhật ký đơn lẻ cho kỹ sư trực ca biết cái gì đã thất bại, trong thao tác nào, với đầu vào nào. Đây là nguyên liệu thô cho khả năng quan sát của chương 9.2 và gỡ lỗi của chương 2.15.

Tội lỗi lớn nhất là nuốt một lỗi: một khối catch rỗng, một giá trị trả về bị bỏ qua, một `catch` ghi nhật ký ở mức debug rồi tiếp tục như không có gì xảy ra. Một lỗi bị nuốt không biến mất; nó nổi lên sau như dữ liệu hỏng hoặc một khiếm khuyết không giải thích được, giờ đã tách khỏi nguyên nhân của nó. Mọi lỗi phải gặp một trong ba số phận: xử lý nó (phục hồi hoặc suy giảm), bọc và lan truyền nó, hoặc, ở đỉnh ngăn xếp, ghi nhật ký nó với đầy đủ ngữ cảnh và thất bại. Nếu bạn bắt một lỗi và không làm điều nào trong số này, bạn đã chọn giấu một sự cố tương lai khỏi chính bản thân tương lai của mình.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Ngoại lệ | Đường suôn sẻ sạch; khó bỏ qua nếu không được kiểm tra | Luồng điều khiển ẩn; cám dỗ xóa bằng bắt tất cả |
| Giá trị lỗi tường minh / kiểu Result | Thất bại hiển thị trong chữ ký; buộc xử lý | Nhiều nghi thức hơn; có thể bị bỏ qua nếu thiếu thực thi |
| Thất bại nhanh | Phơi bày lỗi ồn ào, gần nguyên nhân | Trải nghiệm người dùng kém nếu dùng ở rìa |
| Thất bại an toàn | Tiếp tục phục vụ; bảo vệ người dùng và dữ liệu | Có thể che giấu sự hỏng hóc nếu dùng ở nơi cần thất bại nhanh |
| Thử lại với độ lùi | Vượt qua khiếm khuyết tạm thời tự động | Khuếch đại tải và ghi trùng nếu thiếu tính lũy đẳng |
| Bộ ngắt mạch | Thất bại nhanh; để phụ thuộc phục hồi | Thêm trạng thái và điều chỉnh; có thể che giấu một vấn đề dai dẳng |
| Xác thực phòng thủ tại ranh giới | Bắt dữ liệu xấu sớm, một lần, ồn ào | Làm quá, nó làm lộn xộn logic và che giấu thất bại thực |

Căng thẳng trung tâm là giữa khả năng hiển thị và nhiễu. Xử lý lỗi quá lặng lẽ và bạn che giấu vấn đề cho đến khi chúng đắt đỏ; xử lý chúng quá ồn ào và khắp nơi, và bạn nhấn chìm tín hiệu trong nghi thức và che các thất bại quan trọng. Hãy giải quyết theo vị trí và ý định. Hãy ồn ào và nghiêm ngặt ở các ranh giới, nơi dữ liệu xấu và thất bại phụ thuộc đi vào. Hãy lặng lẽ và tin tưởng ở bên trong, nơi đầu vào đã sạch. Quyết định thất bại nhanh so với thất bại an toàn theo từng ranh giới và viết nó ra. Mục tiêu là mã nơi mọi thất bại có đúng một chủ sở hữu rõ ràng và một số phận rõ ràng, và không gì rơi lặng lẽ qua các kẽ hở.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta có một phân loại lỗi và quy ước xử lý lỗi chung qua các dịch vụ, hay mỗi đội tự ứng biến?** Trong một đội lớn đây là sự khác biệt giữa các thất bại kết hợp được và các thất bại gây rối. Khi một dịch vụ trả về HTTP 500 cho một vấn đề xác thực, dịch vụ khác ném một ngoại lệ có kiểu, và dịch vụ thứ ba trả về rỗng, mọi tích hợp trở thành một cuộc thương lượng và mọi sự cố một bài tập phiên dịch. Hãy mang các ví dụ về cùng một thất bại logic, chẳng hạn "không tìm thấy bản ghi", như nó xuất hiện qua ba dịch vụ của bạn, và xem chúng báo hiệu khác nhau thế nào. Câu trả lời nên trở thành một tiêu chuẩn bằng văn bản: một tập hữu hạn các loại lỗi, một cách nhất quán để báo hiệu chúng, và một linter hoặc danh sách kiểm tra đánh giá thực thi nó. Sự nhất quán ở đây hoàn vốn trong mọi tích hợp, kiểm toán và ca trực tương lai.

2. **Với mỗi ranh giới quan trọng, chúng ta đã chọn thất bại nhanh hay thất bại an toàn một cách có chủ đích chưa, và mã có khớp với lựa chọn đó không?** Hầu hết các đội chưa bao giờ đưa ra quyết định này một cách tường minh, nghĩa là nó đã được đưa ra thay họ bởi ai viết mã đầu tiên, và không nhất quán. Những cân nhắc đối lập là thật: thất bại an toàn giữ người dùng được phục vụ nhưng có thể để sự hỏng hóc lan ra, trong khi thất bại nhanh bảo vệ dữ liệu nhưng có thể biến một sự cố phụ thuộc nhỏ thành một thất bại hiển thị. Hãy mang lịch sử sự cố của bạn và hỏi, với vài cái tệ nhất, liệu mã có thất bại theo cách bạn sẽ chọn nếu được hỏi trước không. Bằng chứng bạn muốn là một bản đồ các ranh giới của bạn với một nhãn có chủ đích trên mỗi cái, đặc biệt ở bất cứ đâu có tiền, an toàn hoặc hồ sơ công dân. Ở nơi nhãn và mã bất đồng, bạn đã tìm thấy bản sửa tiếp theo của mình.

3. **Lần cuối chúng ta cố ý thực hành một đường lỗi là khi nào, và nó có hành xử như đã thiết kế không?** Đường lỗi thường là mã ít được kiểm thử nhất bạn sở hữu, nhưng đó là nơi niềm tin được giành hay mất, và "chúng ta thất bại an toàn" là một khẳng định bạn không thể chứng minh nếu chưa bao giờ nhìn thấy nó xảy ra. Một vòng thử lại không có tính lũy đẳng, một bộ ngắt mạch có ngưỡng sai, một ngoại lệ bị nuốt trong một nhánh hiếm khi chạm đến: những thứ này ẩn cho đến khi một sự cố thực tìm ra chúng cho bạn. Hãy mang kết quả của việc cố ý tiêm thất bại (một phụ thuộc bị giết, một hết thời gian chờ được gây ra, một tải trọng sai định dạng) vào một môi trường thực tế. Hành động tiếp theo là biến tiêm thất bại thành thường lệ, để hành vi phục hồi, suy giảm và thất bại an toàn được xác minh liên tục thay vì hy vọng. Bất kỳ đường lỗi nào bạn chưa bao giờ kích hoạt là lời hứa bạn chưa kiểm thử.

4. **Thao tác ghi nào của chúng ta lũy đẳng, và nơi nào một lần thử lại sau một xác nhận bị mất sẽ nhân đôi một tác động thế giới thực như một khoản thanh toán hoặc một bản ghi?** Thử lại là phản xạ chịu lỗi phổ biến nhất và, nếu làm cẩu thả, là cách phổ biến nhất để một gián đoạn tạm thời biến thành tiền hoặc dữ liệu bị nhân đôi. Trong một đội lớn, logic thử lại thường sống đồng thời trong máy khách dùng chung, phần mềm trung gian và từng dịch vụ, nên một lần ghi đơn lẻ có thể được thử lại ở nhiều tầng mà không ai sở hữu hành vi tổng thể. Lực kéo đối lập là khóa lũy đẳng, loại bỏ trùng lặp và kết quả yêu cầu được lưu thêm lưu trữ và mã, và các đội chịu áp lực phân phối bỏ qua chúng cho những lần ghi mà họ giả định sai là an toàn. Hãy mang một bản kiểm kê các lần ghi hiển thị bên ngoài của bạn, mỗi cái được đánh dấu liệu nó có mang khóa lũy đẳng không và bên nhận nhận ra cùng loại bỏ trùng lặp một lần lặp lại thế nào. Trong bối cảnh doanh nghiệp và chính phủ, hãy đánh dấu những cái di chuyển tiền hoặc thay đổi hồ sơ công dân trước, vì một khoản thanh toán kép hoặc một khoản trợ cấp trùng lặp là một phát hiện kiểm toán và đôi khi là rủi ro pháp lý, không chỉ là khiếm khuyết.

5. **Thời gian chờ, bộ ngắt mạch và vách ngăn của chúng ta có đến từ một thư viện dùng chung, đã kiểm thử, hay mỗi đội tự cuộn?** Những mẫu này dễ mô tả và dễ làm sai một cách tinh vi: một thời gian chờ bị thiếu, một ngưỡng ngắt mạch không bao giờ kích hoạt, một nhóm kết nối được định cỡ để một phụ thuộc chậm làm đói cả tiến trình. Khi mỗi đội cài đặt lại chúng, bạn tích lũy nhiều bản sao hơi hỏng và không có một nơi duy nhất để sửa một khiếm khuyết một khi tìm ra. Cân nhắc đối lập là một thư viện dùng chung áp đặt một giao diện chung và nhịp nâng cấp, và các đội có môi trường chạy hay nhu cầu độ trễ khác thường có thể khó chịu hoặc đi vòng qua nó. Hãy mang một cuộc khảo sát về có bao nhiêu cài đặt thử-lại-và-ngắt-mạch riêng biệt thực sự chạy trên môi trường thực, và dịch vụ nào vẫn không có thời gian chờ nào trên các lệnh gọi đi của nó. Với một doanh nghiệp hoặc cơ quan lớn, một thư viện dùng chung đã kiểm duyệt cũng cho cơ quan rà soát bảo mật và kiểm toán viên một thành phần để chứng nhận thay vì hàng chục, giảm chi phí của mọi lần rà soát.

6. **Nếu một sự cố xảy ra đêm qua, bất kỳ kỹ sư trực ca nào có thể truy vết nó từ một dòng nhật ký đơn lẻ không, và một kiểm toán viên sau này có thể thấy mọi thất bại mà hệ thống đã ghi lại không?** Một lỗi được bọc, phân loại, ghi nhật ký tốt là sự khác biệt giữa chẩn đoán mười phút và một cuộc khai quật nửa đêm, và một lỗi bị nuốt là một sự cố tương lai bạn đã giấu khỏi chính mình. Trong một đội lớn, thất bại đi qua nhiều bước nhảy dịch vụ, nên giá trị đến từ ngữ cảnh nhất quán và mã định danh tương quan tồn tại qua những bước nhảy đó, không phải từ sự cần mẫn của bất kỳ đội nào. Căng thẳng đối lập là chi phí và nhiễu: ghi mọi thứ và bạn nhấn chìm tín hiệu và trả tiền lưu trữ nó; ghi quá ít và bạn không thể dựng lại điều gì đã xảy ra. Hãy mang một thất bại thực gần đây và đi theo dấu vết của nó từ đầu đến cuối, ghi nhận mọi bước nhảy nơi ngữ cảnh bị bỏ hoặc một lỗi bị bắt và vứt đi. Trong các hệ thống chịu quy định và chính phủ, hãy coi đây là thuộc tính tuân thủ, vì một thất bại không thể kiểm toán, hay một quyết định bạn không thể giải thích nhiều năm sau, là rủi ro pháp lý chứ không chỉ là khoảng trống vận hành.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không còn dư nguồn vốn, hãy dành ngân sách xử lý lỗi ở nơi một thất bại tốn của bạn một khách hàng hoặc dữ liệu: đặt thời gian chờ trên mọi lệnh gọi đi, làm các lần ghi chuyển tiền lũy đẳng, và thêm một quy tắc lint chống các lỗi bị bỏ qua. Bỏ qua khung cầu kỳ; một kiểu Result cho các hàm cốt lõi và suy giảm êm ái trên các phụ thuộc không quan trọng mua phần lớn sự an toàn với vài ngày công việc. Thất bại nhanh trong phát triển để lỗi nổi lên ồn ào, và cưỡng lại việc tự cuộn một bộ ngắt mạch trước khi bạn thực sự có một phụ thuộc xứng đáng với nó.

**Doanh nghiệp nhỏ.** Không có chuyên gia chịu lỗi trong biên chế và ngân sách eo hẹp, hãy dựa vào những gì ngôn ngữ, khung và nhà cung cấp đám mây của bạn đã cho thay vì xây các mẫu từ đầu: hàng đợi được quản lý, thử lại phía nhà cung cấp, và thời gian chờ của thư viện bao phủ nhiều hơn hầu hết các đội mong đợi. Hãy đóng khung quyết định như mua hay xây, và mua ở bất cứ nơi nào một phụ thuộc trưởng thành xử lý thử lại, độ lùi và tính lũy đẳng cho bạn. Hãy tập trung sự chú ý khan hiếm vào một hoặc hai ranh giới nơi một giao dịch sai hoặc mất sẽ thực sự gây hại, và bảo đảm chúng thất bại an toàn và để lại dấu vết.

**Doanh nghiệp lớn.** Qua nhiều đội phần thưởng là nhất quán: một phân loại lỗi dùng chung, một thư viện chung cho thời gian chờ, thử lại, bộ ngắt mạch và vách ngăn, và một linter cùng danh sách kiểm tra đánh giá thực thi chúng trong đường ống. Đưa mọi lỗi vào một nền tảng khả năng quan sát thống nhất với mã định danh tương quan để một thất bại truy vết được qua các bước nhảy dịch vụ, và chuẩn hóa các quyết định thất bại nhanh so với thất bại an toàn theo từng ranh giới để kiểm toán tìm thấy một mẫu có tài liệu, có thể bảo vệ thay vì một đống thói quen cục bộ. Hãy quản trị thư viện dùng chung như một sản phẩm thực, vì một khiếm khuyết được sửa ở đó một lần là một khiếm khuyết được sửa ở mọi nơi.

**Chính phủ.** Tính đúng đắn, thất bại an toàn và dấu vết kiểm toán bền vững là nghĩa vụ, không phải sở thích. Hãy thất bại nhanh trên bất kỳ bất biến bị vi phạm nào chạm đến tiền hoặc tính đủ điều kiện, xác thực mọi đầu vào hướng đến công dân tại ranh giới, và ghi mỗi thất bại vào một nhật ký bất biến với đủ ngữ cảnh để một quyết định có thể được giải thích và xem xét nhiều năm sau. Mua sắm và tuổi thọ hệ thống dài có nghĩa là các hợp đồng lỗi phải được lập tài liệu để công chức có thể bảo trì mã lâu sau khi các tác giả gốc đã đi, và bất kỳ thành phần nhà cung cấp nào phải phơi bày hành vi thất bại của nó thay vì giấu nó sau một giao diện mờ đục.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người phát hành một ứng dụng gọi một nhà cung cấp thanh toán bên thứ ba và một dịch vụ email. Sớm thôi họ thêm một vòng thử lại ngây thơ và lập tức tính phí hai lần một khách hàng khi một hết thời gian chờ che giấu một khoản phí thành công. Bản sửa dạy bài học: họ thêm khóa lũy đẳng vào mọi lần ghi, đặt thời gian chờ trên mọi lệnh gọi đi, và chuyển sang độ lùi lũy thừa với độ nhiễu. Họ áp dụng một kiểu Result cho các hàm dịch vụ cốt lõi để thất bại hiện ra trong chữ ký, và một quy tắc lint đánh dấu bất kỳ lỗi bị bỏ qua nào. Khi gửi email thất bại, thanh toán suy giảm êm ái bằng cách xếp hàng thông điệp thay vì chặn giao dịch. Kỷ luật tốn vài ngày và giúp họ khỏi cả một loại sự cố vốn sẽ tốn nhiều hơn về hoàn tiền và niềm tin.

**Doanh nghiệp lớn.** Một công ty hậu cần toàn cầu vận hành hàng trăm dịch vụ và chuẩn hóa xử lý lỗi qua tất cả. Mỗi dịch vụ ánh xạ thất bại vào một phân loại dùng chung (xác thực, không tìm thấy, xung đột, phụ thuộc không khả dụng, nội bộ), nên bên gọi rẽ nhánh theo loại thay vì phân tích thông điệp. Một thư viện chung cung cấp bộ ngắt mạch, thử lại có giới hạn với độ lùi và độ nhiễu, và các nhóm kết nối có vách ngăn, nên không ai tự cuộn những mẫu này sai. Mọi lỗi được ghi nhật ký kèm ngữ cảnh tương quan nuôi nền tảng khả năng quan sát của chương 9.2, nên một kỹ sư trực ca có thể truy vết một thất bại qua các bước nhảy dịch vụ từ một dòng đơn lẻ. Vì tiêu chuẩn đồng nhất và được thực thi trong đường ống, kỹ sư di chuyển tự tin qua các dịch vụ lạ và kiểm toán viên có thể thấy mọi thất bại được ghi lại, phân loại và truy vết được.

**Chính phủ.** Một cơ quan trợ cấp quốc gia xây một hệ thống đủ điều kiện và thanh toán nơi một câu trả lời sai có thể từ chối tiền thuê nhà của ai đó hoặc trả thừa từ công quỹ. Tính đúng đắn và thất bại an toàn là không thể thương lượng, nên mã thất bại nhanh trên bất kỳ bất biến tài chính bị vi phạm nào: một phép tính không thể đối chiếu từ chối ghi thay vì ghi một con số sai. Mọi đầu vào hướng đến công dân được xác thực tại ranh giới, và các trạng thái bất hợp lệ không thể biểu diễn trong các kiểu miền. Mỗi thất bại được ghi vào một nhật ký kiểm toán bất biến với đầy đủ ngữ cảnh, thỏa mãn yêu cầu pháp lý rằng các quyết định phải giải thích được và xem xét được nhiều năm sau. Ở nơi một phụ thuộc không quan trọng như xem trước tài liệu ngừng hoạt động, hệ thống suy giảm êm ái để nhân viên xử lý hồ sơ vẫn xử lý được yêu cầu. Công chức mới thừa kế mã có hợp đồng lỗi được lập tài liệu, nên họ có thể bảo trì nó an toàn lâu sau khi các tác giả gốc đã đi.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của xử lý lỗi có kỷ luật thể hiện ở ít sự cố hơn, sự cố ngắn hơn và rẻ hơn. Hầu hết các sự cố ngừng hoạt động trên môi trường thực không kỳ lạ; chúng truy về một ngoại lệ bị nuốt, một thời gian chờ bị thiếu, một cơn bão thử lại, hay một ranh giới tin dữ liệu mà lẽ ra phải xác thực. Mỗi cái đều có thể ngăn chặn bằng các mẫu ở đây, và mỗi sự cố được ngăn chặn tiết kiệm không chỉ chi phí trực tiếp của thời gian ngừng hoạt động mà cả chi phí cộng dồn của ứng phó khẩn cấp, khách hàng rời bỏ và điều tra. Vì một lỗi được bọc, ghi nhật ký tốt có thể được chẩn đoán trong vài phút thay vì vài giờ, thời gian phục hồi trung bình giảm, và tỷ lệ thay đổi thất bại giảm theo khi kỹ sư thôi sợ đường lỗi.

Chi phí áp dụng khiêm tốn và chủ yếu một lần. Bạn viết ra một phân loại lỗi, cung cấp một thư viện dùng chung cho thử lại và bộ ngắt mạch để các đội không phát minh lại chúng tệ hại, thêm các quy tắc lint chống lỗi bị bỏ qua, và xây thói quen tiêm thất bại. Chi phí của sự bỏ bê cộng dồn lặng lẽ: các lỗi bị nuốt tích tụ thành dữ liệu hỏng đắt để gỡ, và xử lý không nhất quán nhân lên chi phí của mọi tích hợp và mọi kiểm toán. Trong bối cảnh chịu quy định và chính phủ, một thất bại không thể kiểm toán là rủi ro tuân thủ và pháp lý, không chỉ là vấn đề kỹ thuật. Để thuyết phục ban lãnh đạo, hãy kết nối kỷ luật xử lý lỗi với các chỉ số họ vốn đã theo dõi: tần suất sự cố, thời gian phục hồi trung bình, tỷ lệ thay đổi thất bại và phát hiện kiểm toán.

## Phản mẫu và cạm bẫy

- **Nuốt im lặng:** khối catch rỗng và giá trị trả về bị bỏ qua biến một thất bại thành một bí ẩn bị trì hoãn, tách rời.
- **Xóa bằng bắt tất cả:** một `catch` rộng ghi một thông báo chung chung và vứt bỏ lỗi gốc cùng ngữ cảnh của nó.
- **Thử lại không có tính lũy đẳng:** chạy lại các lần ghi không lũy đẳng sau một hết thời gian chờ, tính phí hai lần hoặc nhân đôi bản ghi.
- **Bão thử lại:** không có độ lùi, không có độ nhiễu, không có giới hạn, nên các máy khách đồng bộ và nện một phụ thuộc đang phục hồi xuống lại.
- **Không có thời gian chờ:** các lệnh gọi từ xa không giới hạn để một phụ thuộc bị treo làm cạn luồng và đóng băng cả tiến trình.
- **Ngoại lệ làm luồng điều khiển:** ném và bắt cho các kết quả thông thường như "không tìm thấy", che giấu logic và làm chậm mã.
- **Hoang tưởng phòng thủ:** kiểm tra trên mọi dòng chôn vùi logic và biến thất bại thực thành giá trị mặc định im lặng.
- **Lỗi kiểu chuỗi:** bên gọi phân tích văn bản thông báo lỗi vì không có phân loại ổn định, được phân loại để rẽ nhánh.
- **Thất bại an toàn ở nơi cần thất bại nhanh:** tiếp tục trên trạng thái hỏng trong một hệ thống nơi một câu trả lời sai tệ hơn không có.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Xử lý lỗi tùy nghi và phản ứng, do từng lập trình viên quyết định. Khối catch rỗng và giá trị trả về bị bỏ qua phổ biến, thử lại ngây thơ, thời gian chờ bị thiếu, và thất bại nổi lên như dữ liệu hỏng hoặc khiếm khuyết bí ẩn không có ghi nhật ký nhất quán.
- **Mức 2, Phát triển:** Các đội áp dụng các thực hành cơ bản, nhưng không nhất quán. Lỗi được ghi nhật ký với chút ngữ cảnh, việc nuốt lỗi hiển nhiên bị nản lòng trong đánh giá, và thời gian chờ cùng thử lại đơn giản tồn tại, nhưng quy ước khác nhau giữa các dịch vụ, tính lũy đẳng chắp vá, và đường lỗi hiếm khi được kiểm thử.
- **Mức 3, Chuẩn hóa:** Một phân loại lỗi dùng chung và quy ước xử lý được lập thành tài liệu và thực thi trong toàn tổ chức. Xác thực ranh giới, thử lại lũy đẳng với độ lùi và độ nhiễu, bộ ngắt mạch, vách ngăn và bọc lỗi là chuẩn, được cung cấp bởi các thư viện chung, và mọi lỗi nuôi một đường ống khả năng quan sát thống nhất.
- **Mức 4, Quản lý:** Hành vi xử lý lỗi được đo theo các đường cơ sở và kiểm soát bằng dữ liệu. Tỷ lệ thử lại, số lần ngắt mạch kích hoạt, số thời gian chờ, các phát hiện lỗi bị nuốt từ phân tích tĩnh, thời gian phục hồi trung bình và tỷ lệ thay đổi thất bại được theo dõi cho từng dịch vụ; ngưỡng bộ ngắt mạch và thời gian chờ được điều chỉnh từ dữ liệu độ trễ và thất bại quan sát được thay vì đoán; tiêm thất bại chạy theo lịch; và các đội xem xét các chỉ số này để bắt hồi quy và giữ mỗi lựa chọn thất bại nhanh hay thất bại an toàn dựa trên bằng chứng.
- **Mức 5, Điều phối:** Khả năng chịu lỗi được tích hợp với phân phối và hoạch định rủi ro và được cải tiến liên tục. Phân loại, thư viện dùng chung và tiêu chuẩn tiến hóa từ mọi sự cố, các thí nghiệm hỗn loạn và tiêm thất bại là thường lệ, và tổ chức điều chỉnh thời gian chờ, ngưỡng ngắt mạch, chiến lược suy giảm và quyết định ranh giới khi lưu lượng, phụ thuộc và bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

1. Ở đâu trong cơ sở mã của bạn một lỗi hiện đang bị nuốt, và làm sao bạn biết nếu bạn sai khi cho rằng nó không?
2. Thao tác ghi nào của bạn lũy đẳng, và cái nào sẽ thực thi hai lần nếu một lần thử lại kích hoạt sau một xác nhận bị mất?
3. "Không tìm thấy người dùng" nên là một ngoại lệ, một giá trị lỗi, hay một kết quả bình thường, và đội bạn có trả lời điều đó nhất quán không?
4. Quy tắc thực tế của bạn về nơi xác thực diễn ra là gì, và bạn có thể chỉ ra một ranh giới tin dữ liệu mà nó không nên không?
5. Làm thế nào bạn quyết định ngưỡng và thời gian làm nguội cho một bộ ngắt mạch, và làm sao bạn biết các thiết lập hiện tại là sai?
6. Nếu một kiểm toán viên yêu cầu xem mọi thất bại mà hệ thống của bạn đã trải qua tháng trước, bạn có thể đưa ra không, được phân loại và kèm ngữ cảnh?

## Những điểm cần ghi nhớ

- Phân biệt khiếm khuyết, lỗi và thất bại, và phá vỡ chuỗi trước khi một lỗi nội bộ trở thành thất bại hiển thị.
- Chọn thất bại nhanh hay thất bại an toàn một cách có chủ đích theo từng ranh giới, và làm hợp đồng xử lý lỗi của mọi hàm tường minh.
- Xác thực mạnh tại các ranh giới tin cậy và tin tưởng bên trong chúng; sự phòng thủ che giấu thất bại là trì hoãn, không phải an toàn.
- Làm thử lại an toàn bằng tính lũy đẳng, thời gian chờ, độ lùi lũy thừa và độ nhiễu, và thêm bộ ngắt mạch cùng suy giảm êm ái trong mã.
- Bọc lỗi với ngữ cảnh, đưa chúng vào khả năng quan sát, và không bao giờ nuốt chúng; mọi lỗi phải được xử lý, lan truyền, hoặc ghi nhật ký và phơi bày.

## Tài liệu tham khảo và đọc thêm

- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
- Andrew Hunt và David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering: How Google Runs Production Systems*
- Marc Brooker, "Timeouts, Retries, and Backoff with Jitter," Amazon Builders' Library
- Martin Fowler, "CircuitBreaker," martinfowler.com
- Nassim Nicholas Taleb, *Antifragile: Things That Gain from Disorder*
