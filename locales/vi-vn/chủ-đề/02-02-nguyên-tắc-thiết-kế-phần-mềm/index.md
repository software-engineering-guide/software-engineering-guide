# 2.2 Nguyên tắc thiết kế phần mềm

## Tổng quan và động lực

Nguyên tắc thiết kế phần mềm là những quy tắc kinh nghiệm để sắp xếp mã sao cho bạn có thể hiểu, thay đổi và mở rộng nó theo thời gian. Chúng bao gồm các từ viết tắt có tên ([SOLID](https://en.wikipedia.org/wiki/SOLID) cho năm nguyên tắc thiết kế [hướng đối tượng](https://en.wikipedia.org/wiki/Object-oriented_programming), [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) cho đừng lặp lại chính mình, [KISS](https://en.wikipedia.org/wiki/KISS_principle) cho giữ cho đơn giản, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) cho bạn sẽ không cần đến nó), các khái niệm cấu trúc ([độ liên kết](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [độ kết dính](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [tách biệt các mối quan tâm](https://en.wikipedia.org/wiki/Separation_of_concerns)), các [mẫu thiết kế](https://en.wikipedia.org/wiki/Software_design_pattern) đã được lập danh mục, các cách tiếp cận mô hình hóa cấp cao hơn như [Thiết kế hướng miền](https://en.wikipedia.org/wiki/Domain-driven_design) (mô hình hóa phần mềm bằng ngôn ngữ của miền nghiệp vụ), và lựa chọn giữa phong cách hướng đối tượng, [hàm](https://en.wikipedia.org/wiki/Functional_programming) và [hướng dữ liệu](https://en.wikipedia.org/wiki/Data-oriented_design). Không điều nào trong số này là điều luật. Chúng là kinh nghiệm được nén lại, và bạn phải áp dụng chúng bằng phán đoán.

Với các đội lớn, giá trị của các nguyên tắc chung là sự điều phối. Khi hàng trăm kỹ sư làm việc trên cùng một hệ thống, họ cần một từ vựng chung cho các cuộc thảo luận thiết kế và một bộ mặc định chung để các mô-đun được viết độc lập khớp với nhau. Thiết kế tốt là thứ cho phép nhiều người thay đổi một hệ thống song song mà không va chạm liên tục. Nó cũng là thứ giữ cho một hệ thống còn thay đổi được sau một thập kỷ, tuổi thọ bình thường của các hệ thống doanh nghiệp và chính phủ, lâu sau nhiệm kỳ của các tác giả ban đầu.

Kỹ năng then chốt không phải là học thuộc các nguyên tắc. Mà là biết khi nào mỗi nguyên tắc đánh lừa bạn. Mỗi nguyên tắc đều có một chế độ thất bại: DRY có thể tạo ra phép trừu tượng sai, SOLID có thể tạo ra sự gián tiếp không cần thiết, YAGNI có thể làm đói khả năng mở rộng mà bạn thực sự cần. Chương này coi các nguyên tắc là những công cụ có phạm vi áp dụng, và nhấn mạnh độ liên kết cùng độ kết dính như những thuộc tính sâu hơn mà các từ viết tắt đang cố phục vụ.

## Các nguyên tắc chính

- Quản lý độ liên kết và độ kết dính trước tiên; hầu hết các nguyên tắc có tên là những cách gián tiếp để cải thiện hai thuộc tính này.
- Tối ưu hóa cho thay đổi: thiết kế tốt giảm thiểu chi phí của những thay đổi bạn thực sự cần thực hiện.
- Ưu tiên thiết kế đơn giản nhất hoạt động được lúc này, nhưng giữ các ranh giới ở nơi thay đổi có khả năng xảy ra.
- Sự trùng lặp rẻ hơn phép trừu tượng sai; hãy chờ cho đến khi mẫu hình rõ ràng.
- Làm cho các phụ thuộc tường minh và hướng chúng về phía những thứ ổn định.
- Mô hình hóa miền nghiệp vụ bằng ngôn ngữ của miền; căn chỉnh ranh giới phần mềm với ranh giới kinh doanh.
- Chọn mô hình lập trình cho phù hợp với vấn đề, không phải theo ý thức hệ; hầu hết các hệ thống lớn là sự pha trộn thực dụng.

## Khuyến nghị

### Dùng SOLID như một lăng kính, không phải một danh sách kiểm tra

Hãy áp dụng trách nhiệm đơn lẻ để giữ các mô-đun kết dính, đảo ngược phụ thuộc để hướng các phụ thuộc vào các phép trừu tượng ở nơi thực sự có một ranh giới, và đóng-mở ở nơi các điểm mở rộng là thật. Đừng chế tạo giao diện, nhà máy và tầng chỉ để thỏa mãn từ viết tắt khi chỉ có một triển khai và không thấy triển khai thứ hai nào. Sự gián tiếp có chi phí, và bạn trả nó trong mỗi lần đọc.

### Áp dụng DRY cho kiến thức, không phải cho văn bản

DRY là về việc không nhân đôi một mẩu *kiến thức* có thẩm quyền duy nhất. Nó không phải là về việc loại bỏ những dòng chỉ trông giống nhau. Hai đoạn mã trông giống nhau nhưng thay đổi vì những lý do khác nhau nên được giữ tách biệt. Hãy ưu tiên một chút trùng lặp hơn là một phép trừu tượng chung quá sớm liên kết những thứ không liên quan. Hãy trích xuất phép trừu tượng khi mẫu hình thực sự đã xuất hiện hai hoặc ba lần.

### Để KISS và YAGNI chống lại sự suy đoán

Xây dựng cho những yêu cầu bạn có, không phải những yêu cầu bạn tưởng tượng. Tránh tính tổng quát mang tính suy đoán, như các khung có thể cấu hình, hệ thống plugin và điểm mở rộng mà không ai yêu cầu. Đối trọng là một số sự linh hoạt thực sự rẻ hơn khi xây vào sớm, như một giao diện ổn định hoặc một đường nối sạch. YAGNI phản đối *việc triển khai* mang tính suy đoán, không phải phản đối các ranh giới được cân nhắc.

### Thiết kế cho độ liên kết thấp và độ kết dính cao một cách tường minh

Làm cho mỗi mô-đun làm một việc được xác định rõ (độ kết dính), và phụ thuộc vào càng ít mô-đun khác càng tốt, thông qua các giao diện hẹp (độ liên kết thấp). Khi bạn đánh giá một thiết kế, hãy hỏi những thay đổi nào lan qua ranh giới mô-đun. Những gợn sóng đó là thước đo thực sự của độ liên kết. Tách biệt các mối quan tâm là cùng một ý tưởng áp dụng cho các tầng và các mối quan tâm xuyên suốt.

### Dùng mẫu thiết kế như từ vựng, áp dụng phản mẫu như cảnh báo

Các mẫu là những cái tên chung hữu ích cho các giải pháp lặp lại. Hãy với tới một mẫu khi vấn đề thực sự khớp với nó. Đừng áp đặt các mẫu để trông tinh vi, vì mã nặng về mẫu thường là dấu hiệu của thiết kế quá mức. Hãy học các [phản mẫu](https://en.wikipedia.org/wiki/Anti-pattern) phổ biến (đối tượng thượng đế, mô hình thiếu máu ở nơi không phù hợp, quả bóng bùn lớn, khối đơn phân tán) như những nhãn chẩn đoán.

### Áp dụng Thiết kế hướng miền ở nơi miền nghiệp vụ phức tạp

Với các hệ thống có quy tắc kinh doanh phong phú, hãy dùng các công cụ chiến thuật và chiến lược của DDD: một ngôn ngữ phổ quát chia sẻ với chuyên gia miền, các ngữ cảnh giới hạn chia hệ thống thành những phần được mô hình hóa độc lập, và các bản đồ ngữ cảnh mô tả cách những phần đó liên hệ với nhau. Ngữ cảnh giới hạn đặc biệt có giá trị ở quy mô doanh nghiệp, vì chúng căn chỉnh quyền sở hữu của đội với ranh giới mô hình. DDD là quá mức cho các hệ thống [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) đơn giản (tạo, đọc, cập nhật, xóa).

### Chọn mô hình lập trình theo sự phù hợp

Dùng hướng đối tượng để đóng gói hành vi có trạng thái và mô hình hóa các miền. Dùng phong cách hàm cho các phép biến đổi, đồng thời và khả năng dự đoán thông qua [tính bất biến](https://en.wikipedia.org/wiki/Immutable_object). Dùng thiết kế hướng dữ liệu ở nơi hiệu năng và hành vi bộ nhớ đệm chi phối. Các hệ thống lớn pha trộn cả ba. Hãy đưa ra lựa chọn cho từng thành phần, và giữ các ranh giới giữa các phong cách sạch sẽ.

## Đánh đổi: ưu và nhược điểm

| Nguyên tắc / cách tiếp cận | Khi áp dụng tốt | Chế độ thất bại |
|---|---|---|
| SOLID | Các đường nối rõ ràng nơi thay đổi xảy ra; các đơn vị kiểm thử được | Giao diện và tầng sinh sôi; sự gián tiếp không có lợi ích |
| DRY | Một nguồn sự thật duy nhất cho kiến thức thực sự | Phép trừu tượng sai liên kết mã không liên quan |
| KISS / YAGNI | Hệ thống gọn gàng, dễ hiểu | Đường nối thiết kế thiếu; hồi tố tốn kém cho sự linh hoạt cần thiết |
| Mẫu thiết kế | Từ vựng chung; cấu trúc đã được chứng minh | Sùng bái mẫu; độ phức tạp ngẫu nhiên |
| Thiết kế hướng miền | Mô hình và đội được căn chỉnh; độ phức tạp được thuần hóa | Nghi thức nặng trên miền đơn giản; ranh giới ngữ cảnh đặt sai |
| Hàm / bất biến | Khả năng dự đoán; đồng thời an toàn hơn | Vụng về với các vấn đề vốn có trạng thái; bất ngờ về hiệu năng |

Căng thẳng lặp lại là giữa thiết kế thiếu và thiết kế thừa. Các hệ thống thiết kế thiếu tích tụ độ liên kết và trở nên cứng nhắc. Các hệ thống thiết kế thừa chìm trong sự trừu tượng mà ai đó phải hiểu và bảo trì. Câu trả lời không phải là một điểm cố định. Đó là một kỷ luật: trì hoãn các quyết định cho đến khi bạn có đủ thông tin, đồng thời giữ những đường nối cho phép bạn đổi ý.

## Câu hỏi để thảo luận với đội của bạn

1. **Ngưỡng cụ thể của bạn để trích xuất một phép trừu tượng dùng chung là gì, và làm thế nào bạn ngăn DRY tạo ra phép trừu tượng sai?** Chương này thẳng thắn rằng sự trùng lặp rẻ hơn phép trừu tượng sai, và rằng bạn nên chờ cho đến khi mẫu hình đã xuất hiện hai hoặc ba lần trước khi trích xuất. Trong một đội lớn, mối nguy là ai đó gộp hai đoạn mã trông giống nhau vào một mô-đun dùng chung qua ranh giới đội, rồi mọi thay đổi trong tương lai đối với một bên gọi lan sang bên kia. Tín hiệu cần mang theo là liệu các bản trùng lặp thay đổi vì cùng một lý do hay chỉ trông giống nhau lúc này. Hãy thống nhất quy tắc ba lần, và yêu cầu một phép trừu tượng ứng viên thực sự đã thay đổi cùng nhau trước khi bạn liên kết các bên gọi. Một thỏa thuận duy nhất đó ngăn một loại liên kết tốn kém để gỡ khi nhiều đội đã phụ thuộc vào nó.

2. **Làm thế nào bạn làm cho độ liên kết và độ kết dính hiển thị trong đánh giá thiết kế thay vì để cho cảm tính?** Các nguyên tắc chính đặt độ liên kết và độ kết dính lên trên mọi từ viết tắt, và định nghĩa độ liên kết là những thay đổi lan qua ranh giới mô-đun. Trực giác không mở rộng được qua hàng trăm kỹ sư mà mỗi người chỉ thấy góc của mình trong hệ thống. Hãy mang bằng chứng mà máy móc có thể tạo ra: đồ thị phụ thuộc, và dữ liệu đồng thay đổi cho thấy những mô-đun nào liên tục được sửa cùng nhau trong cùng các commit. Hãy thêm một câu hỏi đánh giá tường minh hỏi một thay đổi buộc bạn phải vượt qua những ranh giới mô-đun nào. Khi hai mô-đun luôn thay đổi cùng nhau, đó là tín hiệu để bạn hoặc gộp chúng hoặc sửa ranh giới giữa chúng.

3. **Lằn ranh trong các hệ thống của bạn giữa một miền đủ phong phú để biện minh cho Thiết kế hướng miền và một ứng dụng CRUD đơn thuần nơi nó là quá mức nằm ở đâu?** Chương này khuyến nghị các ngữ cảnh giới hạn của DDD chính vì chúng căn chỉnh quyền sở hữu của đội với ranh giới mô hình, và cảnh báo rằng DDD là quá mức cho các hệ thống tạo-đọc-cập nhật-xóa đơn giản và suy thoái thành nghi thức nếu không có mô hình hóa thực sự. Làm sai theo cả hai hướng đều tốn kém: DDD nặng trên một miền mỏng chôn một ứng dụng đơn giản trong nghi thức, trong khi một mô hình chung tràn lan qua nhiều đội buộc phải điều phối liên đội liên tục. Hãy mang những tín hiệu thực sự quyết định: mật độ quy tắc kinh doanh, và bao nhiêu đội cần sở hữu các phần một cách độc lập. Hãy dành bộ máy chiến lược cho lõi phức tạp, và để các rìa đơn giản ở lại đơn giản. Điều đó giữ bạn tránh xa cả sân khấu DDD lẫn quả bóng bùn lớn.

4. **Khi nào một phép trừu tượng, giao diện hay mẫu thiết kế đáng với sự gián tiếp mà nó thêm vào, và ai có thẩm quyền gọi một thiết kế là thiết kế quá mức?** Chương này nói rõ rằng sự gián tiếp có chi phí bạn trả trong mỗi lần đọc, và rằng chế tạo giao diện, nhà máy và tầng để thỏa mãn SOLID hay để trông tinh vi là một chế độ thất bại. Trong một đội lớn, áp lực chạy theo hướng ngược lại: người đánh giá cho qua thêm trừu tượng vì nó trông có kỷ luật, và không ai muốn là người tranh luận cho ít cấu trúc hơn. Cân nhắc đối lập là có thật, vì một số đường nối thực sự xứng đáng với chỗ đứng của chúng và gỡ chúng sau này tốn kém. Hãy mang bằng chứng cụ thể vào cuộc thảo luận: một giao diện hiện thực sự có bao nhiêu triển khai, điểm mở rộng đã bao giờ co giãn chưa, và người đọc phải mở bao nhiêu tệp để theo dõi một đường mã. Hãy thống nhất rằng một triển khai duy nhất không thấy cái thứ hai là lý do mặc định để gộp vào, và nêu tên ai có thể gọi một thiết kế là thiết kế quá mức mà không bị coi là xúc phạm. Trong các hệ thống doanh nghiệp và chính phủ tồn tại lâu hơn tác giả của chúng một thập kỷ, sự gián tiếp vô cớ là cái thuế mà mọi người bảo trì tương lai phải trả, vì vậy hãy coi "phép trừu tượng này mua cho chúng ta điều gì" là một câu hỏi đánh giá thường trực, không phải một thách thức cá nhân.

5. **Làm thế nào bạn quyết định mỗi thành phần dùng mô hình lập trình nào, hướng đối tượng, hàm hay hướng dữ liệu, và làm thế nào bạn giữ các ranh giới giữa chúng sạch sẽ?** Chương này lập luận rằng các hệ thống lớn là sự pha trộn thực dụng và rằng bạn nên chọn cho từng thành phần theo sự phù hợp, dùng hướng đối tượng cho các miền có trạng thái, phong cách hàm cho các phép biến đổi và đồng thời, và thiết kế hướng dữ liệu ở nơi hiệu năng và hành vi bộ nhớ đệm chi phối. Nếu không được quản lý, lựa chọn mô hình trở thành chuyện ai viết mô-đun trước, và trạng thái khả biến rò rỉ vào những gì lẽ ra là các phép biến đổi thuần túy, hoặc sự thuần túy hàm đấu tranh với một vấn đề vốn có trạng thái. Bằng chứng đáng mang là nỗi đau thực sự của bạn nằm ở đâu: thành phần nào khó kiểm thử vì trạng thái ẩn, đường nóng nào bị giới hạn bởi bộ nhớ đệm, và nơi phong cách hiện tại buộc phải có những cách lách vụng về. Hãy quyết định mô hình mặc định cho từng tầng một cách có chủ đích và viết ra nơi các đường nối giữa các phong cách nằm, để lõi hàm và rìa mệnh lệnh không tràn vào nhau. Với một hệ thống chịu quy định hoặc của chính phủ nơi một phép tính phải có thể kiểm toán và tái tạo được cho một giai đoạn nhất định, một lõi hàm, bất biến thường là yêu cầu tuân thủ chứ không phải sở thích, và ràng buộc đó nên dẫn dắt ranh giới chứ không đi theo nó.

6. **Làm thế nào bạn giữ các nguyên tắc này khỏi đông cứng thành giáo điều, và bạn ghi lại lý do đằng sau một quyết định thiết kế ở đâu để một đội tương lai có thể xem xét lại?** Mỗi nguyên tắc trong chương này đều có phạm vi áp dụng và chế độ thất bại, và toàn bộ cách đóng khung coi chúng là những công cụ cần áp dụng bằng phán đoán chứ không phải điều luật cần thực thi. Trong một đội lớn, một nguyên tắc âm thầm trở thành quy tắc: DRY cấm mọi sự trùng lặp, SOLID bắt buộc một giao diện cho mỗi lớp, và các ngoại lệ thực dụng bị chặn trong đánh giá bởi những người trích dẫn từ viết tắt thay vì kết quả. Căng thẳng là một mức nhất quán nào đó thực sự giúp hàng trăm kỹ sư điều phối, nên bạn không thể đơn giản tuyên bố mọi nguyên tắc là tùy chọn. Hãy mang những ví dụ nơi tuân theo một nguyên tắc từng chữ tạo ra một thiết kế tệ hơn, và mang các hồ sơ quyết định, nếu có, giải thích vì sao một ranh giới hay phép trừu tượng nhất định tồn tại. Hãy thống nhất rằng các nguyên tắc là mặc định mà kỹ sư có thể đi chệch với một lý do được ghi lại, và ghi lại các lựa chọn thiết kế hệ trọng trong một hồ sơ quyết định kiến trúc ngắn để đội kế tiếp thừa hưởng lý do chứ không chỉ mã. Trong các hệ thống doanh nghiệp và khu vực công, nơi các tác giả ban đầu đã đi từ lâu và kiểm toán hỏi vì sao hệ thống có hình dạng như vậy, dấu vết bằng văn bản đó là khác biệt giữa một thiết kế mà các đội tương lai có thể thay đổi an toàn và một thiết kế mà họ sợ chạm vào.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy ưu tiên thiết kế đơn giản nhất phát hành được và giữ một mô-đun được phân rã tốt cho đến khi một trường hợp sử dụng thứ hai thực sự buộc phải có đường nối. Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ thuật, vì vậy các giao diện, tầng và khung suy đoán sớm hoàn toàn là chi phí. Hãy theo quy tắc ba lần trước khi trích xuất bất kỳ phép trừu tượng dùng chung nào, và để YAGNI giết những điểm mở rộng mà chưa ai yêu cầu.

**Doanh nghiệp nhỏ.** Không có kiến trúc sư riêng và ít thời gian, hãy dựa vào thiết kế đã được tích hợp sẵn trong các khung và thư viện bạn mua thay vì tự phát minh các mẫu của riêng mình. Hãy dành công sức thiết kế tùy biến cho một nhúm quy tắc thực sự là việc kinh doanh của bạn, và giữ mọi thứ khác theo quy ước để một nhà thầu hay nhân viên mới có thể đọc nó. Một chút trùng lặp mà bạn hiểu tốt hơn một phép trừu tượng thông minh mà chỉ tác giả của nó bảo trì được.

**Doanh nghiệp lớn.** Lợi ích của các nguyên tắc chung là sự điều phối qua nhiều đội: một từ vựng chung cho đánh giá thiết kế, và các ngữ cảnh giới hạn căn chỉnh ranh giới mô hình với quyền sở hữu của đội để các nhóm phát triển độc lập. Hãy quản lý độ liên kết và độ kết dính một cách tường minh bằng dữ liệu phụ thuộc và đồng thay đổi, và ghi lại các quyết định thiết kế hệ trọng để hệ thống còn thay đổi được lâu sau khi tác giả của chúng đi nơi khác. Hãy đề phòng ngang nhau cả phép trừu tượng sai liên kết các đội và thiết kế quá mức đánh thuế mọi người đọc.

**Chính phủ.** Khả năng kiểm toán và tái tạo thường quyết định thiết kế. Một lõi hàm, bất biến cho phép bạn tái tạo chính xác một phép tính lịch sử cho một giai đoạn nhất định, điều mà một đồ thị đối tượng rối rắm với trạng thái khả biến ẩn không thể đảm bảo. Hãy ưu tiên các hợp đồng được công bố tường minh hơn các bảng dùng chung ở ranh giới ngữ cảnh, và giữ thiết kế cùng các hồ sơ quyết định của nó dễ đọc với kiểm toán viên và với bất kỳ đội nào thừa kế hệ thống một thập kỷ sau.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp ba kỹ sư xây dựng sản phẩm đầu tiên cưỡng lại ý muốn chia mỗi tính năng thành các tầng giao diện và nhà máy, giữ một mô-đun được phân rã tốt cho đến khi một trường hợp sử dụng thứ hai thực sự xuất hiện. Khi cùng logic đó xuất hiện lần thứ ba qua các luồng đăng ký và thanh toán, họ trích xuất một hàm dùng chung nhỏ thay vì một khung suy đoán. Điều này giữ cơ sở mã đủ nhỏ để bất kỳ ai trong họ cũng có thể giữ nó trong đầu, và vài đường nối họ vẽ ra rơi vào nơi sản phẩm có nhiều khả năng thay đổi nhất.

**Doanh nghiệp lớn.** Một nền tảng bảo hiểm lớn mô hình hóa hợp đồng, bồi thường và thanh toán thành các ngữ cảnh giới hạn riêng biệt, mỗi cái do một đội chuyên trách sở hữu với mô hình dữ liệu và ranh giới dịch vụ riêng. Ở nơi các ngữ cảnh gặp nhau, như khi một yêu cầu bồi thường tham chiếu một hợp đồng, chúng giao tiếp qua các hợp đồng được công bố tường minh thay vì các bảng cơ sở dữ liệu dùng chung. Điều này cho phép ba đội phát triển độc lập, và ngôn ngữ phổ quát giữ các cuộc trò chuyện với người thẩm định và chuyên viên tính toán chính xác. Một phiên bản trước đó đã chia sẻ một mô hình duy nhất tràn lan, và mọi thay đổi đều đòi hỏi điều phối liên đội.

**Chính phủ.** Một hệ thống xử lý thuế quốc gia cố ý ưu tiên một lõi hướng dữ liệu, hàm cho công cụ tính toán của nó. Các quy tắc thuế được biểu diễn như những phép biến đổi thuần túy trên các bản ghi đầu vào bất biến, giúp chúng có thể kiểm toán, kiểm thử và tái tạo cho một năm thuế nhất định. Các phần mệnh lệnh, có trạng thái (quy trình công việc, thông báo) được giữ ở các rìa. Kiểm toán viên có thể chỉ vào một phiên bản quy tắc cụ thể và tái tạo chính xác bất kỳ phép tính lịch sử nào, đó là yêu cầu pháp lý mà một đồ thị đối tượng rối rắm với trạng thái khả biến ẩn không thể đảm bảo.

## Luận chứng kinh doanh: động lực, ROI và TCO

Chất lượng thiết kế là khoản đầu tư vào *khả năng thay đổi* của một hệ thống, và khả năng thay đổi chi phối tổng chi phí sở hữu. Phần lớn chi phí của một hệ thống rơi vào sau bản phát hành đầu tiên, trong sửa đổi và mở rộng. Các hệ thống được thiết kế tốt giữ chi phí thay đổi gần như phẳng theo thời gian. Các hệ thống được thiết kế tệ thấy chi phí của mỗi thay đổi leo thang cho đến khi hệ thống thực sự không thể sửa đổi và phải được viết lại, kết quả đắt nhất trong tất cả.

Chi phí áp dụng chủ yếu là kỹ năng và kỷ luật đánh giá: dạy các nguyên tắc, và dành thời gian thiết kế ngay từ đầu. Chi phí của việc không áp dụng là sự tích tụ chậm chạp của [nợ kỹ thuật](https://en.wikipedia.org/wiki/Technical_debt), vận tốc phân phối giảm, tỷ lệ lỗi tăng, và những lần viết lại tốn kém cuối cùng. Để thuyết phục ban lãnh đạo, hãy kết nối kỷ luật thiết kế với khả năng dự đoán phân phối và với việc tránh các chương trình viết lại, và theo dõi các chỉ báo dẫn đầu như tỷ lệ thay đổi thất bại và thời gian triển khai các tính năng tương đương theo thời gian. Cũng hãy cảnh giác với thất bại ngược lại: đầu tư quá mức vào thiết kế cho những tương lai không chắc chắn cũng phá hủy giá trị. Vì vậy lập luận là cho thiết kế *phù hợp*, được hiệu chỉnh theo khả năng và chi phí của thay đổi trong tương lai.

## Phản mẫu và cạm bẫy

- **Tính tổng quát suy đoán:** xây dựng khả năng mở rộng cho những yêu cầu tưởng tượng không bao giờ đến.
- **Phép trừu tượng sai:** ép mã không liên quan lại với nhau để thỏa mãn DRY, tạo ra sự liên kết tệ hơn sự trùng lặp.
- **Sùng bái mẫu:** áp dụng mẫu thiết kế vì chính chúng, thêm sự gián tiếp mà không có lợi ích.
- **Đối tượng thiếu máu hoặc thượng đế:** các mô hình không có hành vi, hoặc các đối tượng làm mọi thứ; cả hai đều báo hiệu trách nhiệm đặt sai chỗ.
- **Khối đơn phân tán:** các dịch vụ được tách về mặt vật lý nhưng vẫn liên kết chặt chẽ, kết hợp chi phí của cả hai cách tiếp cận.
- **Quả bóng bùn lớn:** không có cấu trúc nhận ra được; mọi thay đổi đều rủi ro cho tất cả.
- **Sân khấu DDD:** áp dụng từ vựng và cấu trúc thư mục mà không có mô hình hóa miền tạo ra giá trị cho nó.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Thiết kế tùy nghi và phản ứng; độ liên kết tích tụ không bị kiểm soát; các nguyên tắc không được biết đến hoặc được viện dẫn như khẩu hiệu, và các phép trừu tượng xuất hiện hay biến mất theo thói quen cá nhân.
- **Mức 2, Phát triển:** Các đội biết các nguyên tắc và áp dụng chúng, nhưng không nhất quán và thường giáo điều; một số nhóm quản lý độ liên kết và độ kết dính có chủ đích trong khi những nhóm khác thì không, và không có từ vựng chung trong tổ chức.
- **Mức 3, Chuẩn hóa:** Một từ vựng thiết kế chung, quy tắc ba lần để trích xuất các phép trừu tượng, phân tích độ liên kết và độ kết dính, và các ngữ cảnh giới hạn được căn chỉnh với các đội được lập thành tài liệu và kỳ vọng toàn tổ chức, áp dụng nhất quán trong đánh giá thiết kế thay vì để cho sở thích cá nhân.
- **Mức 4, Quản lý:** Sức khỏe thiết kế được đo theo các đường cơ sở: dữ liệu liên kết và đồng thay đổi, tỷ lệ thay đổi thất bại, và thời gian triển khai các tính năng tương đương được theo dõi theo thời gian, để các phép trừu tượng và ranh giới được thêm, giữ hoặc loại bỏ dựa trên bằng chứng, và thiết kế quá mức cùng phép trừu tượng sai được bắt bằng dữ liệu thay vì ý kiến.
- **Mức 5, Điều phối:** Kỷ luật thiết kế được tích hợp với phân phối và hoạch định rủi ro trong toàn tổ chức; các nguyên tắc được áp dụng với sự tinh tế và biết các chế độ thất bại; các lựa chọn mô hình lập trình và ranh giới là có chủ đích và liên tục được xem xét lại, và tổ chức thường xuyên tái cấu trúc, điều chỉnh phạm vi và loại bỏ các phép trừu tượng khi miền nghiệp vụ và bằng chứng dịch chuyển.

## Ý tưởng để thảo luận

- Làm thế nào bạn phân biệt giữa một đường nối cần thiết và tính tổng quát suy đoán trước khi bạn có yêu cầu tương lai?
- Khi nào DRY đã dẫn đội bạn đến phép trừu tượng sai, và làm sao bạn nhận ra điều đó?
- Ranh giới ngữ cảnh giới hạn nên rơi vào đâu, và chúng nên phản chiếu sơ đồ tổ chức sát đến mức nào?
- Bao nhiêu thiết kế nên đi trước mã trong bối cảnh của bạn, và bạn ghi lại các quyết định như thế nào?
- Những phần nào trong hệ thống của bạn sẽ được hưởng lợi từ phong cách hàm hoặc hướng dữ liệu hơn?
- Làm thế nào bạn giữ các nguyên tắc thiết kế khỏi đông cứng thành giáo điều chống lại các ngoại lệ thực dụng?

## Những điểm cần ghi nhớ

- Độ liên kết và độ kết dính là những thuộc tính quan trọng; các từ viết tắt là phương tiện để đạt những mục đích đó.
- Mỗi nguyên tắc đều có chế độ thất bại; hãy biết khi nào mỗi nguyên tắc đánh lừa bạn.
- Ưu tiên một chút trùng lặp hơn một phép trừu tượng quá sớm hoặc sai.
- Dùng DDD và các ngữ cảnh giới hạn để căn chỉnh các miền phức tạp với quyền sở hữu của đội.
- Chọn mô hình lập trình theo sự phù hợp; các hệ thống lớn là sự pha trộn thực dụng.
- Thiết kế cho những thay đổi bạn thực sự cần, tránh cả thiết kế thiếu và thiết kế thừa.

## Tài liệu tham khảo và đọc thêm

- Robert C. Martin, *Clean Architecture* và *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* và *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
