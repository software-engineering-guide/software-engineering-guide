# 2.19 Tái cấu trúc và nợ kỹ thuật

## Tổng quan và động lực

[Tái cấu trúc](https://en.wikipedia.org/wiki/Code_refactoring) là thay đổi cấu trúc bên trong của mã mà không thay đổi những gì nó làm nhìn từ bên ngoài. Bạn đổi tên một biến, tách một hàm dài, trích xuất một lớp, gộp một mớ điều kiện rối rắm thành thứ người đọc theo dõi được, và chương trình hành xử đúng như trước. Phần cuối cùng đó là toàn bộ kỷ luật. Tái cấu trúc là bảo toàn hành vi theo định nghĩa, và khoảnh khắc bạn cũng thay đổi hành vi bạn không còn tái cấu trúc, bạn đang làm hai việc rủi ro cùng lúc và giấu cái này sau cái kia. Chương này coi chúng là hai hành động riêng biệt một cách có chủ đích, vì sự nhầm lẫn giữa chúng là nơi hầu hết các lần tái cấu trúc đi sai.

Trong một đội lớn, điều này quan trọng hơn nhiều so với một lập trình viên đơn lẻ, vì mã bạn đang dọn dẹp là mã hàng trăm người khác đọc, phụ thuộc và sợ chạm vào. Tái cấu trúc là cách một cơ sở mã dùng chung còn ở được qua nhiều năm và sự thay đổi nhân sự. Nó kết nối trực tiếp với xây dựng phần mềm (chương 2.9), nơi chất lượng lập trình hằng ngày được đặt ra, và với chiến lược kiểm thử (chương 2.4), vốn là lưới an toàn khiến tái cấu trúc an toàn ngay từ đầu. Nó cũng kết nối với câu hỏi khó hơn về [nợ kỹ thuật](https://en.wikipedia.org/wiki/Technical_debt): chi phí tích lũy của những đường tắt, thiết kế cũ và việc dọn dẹp bị trì hoãn khiến mọi thay đổi trong tương lai chậm hơn. Tái cấu trúc là cách chính để bạn trả khoản nợ đó, nên hai chủ đề thuộc về một chương.

Trong bối cảnh doanh nghiệp và chính phủ, rủi ro tăng cao. Những hệ thống này sống lâu, thường đã hàng chục năm tuổi, và thường nằm dưới các chế độ kiểm toán và kiểm soát thay đổi coi bất kỳ thay đổi mã nào là một sự kiện được quản trị. Bạn không thể đơn giản viết lại một hệ thống trợ cấp công dân qua một cuối tuần dài; bạn hiện đại hóa nó theo các bước nhỏ, đảo ngược được, có bằng chứng hậu thuẫn, đúng là điều tái cấu trúc có kỷ luật mang lại cho bạn. Điều phối công việc đó qua nhiều đội và các hệ thống tồn tại lâu (chương 10.4) là một trong những thách thức xác định của kỹ thuật quy mô lớn, và làm sai là cách các tổ chức rơi vào tình trạng đóng băng, không thể thay đổi phần mềm mà họ không còn hiểu.

## Các nguyên tắc chính

- Tái cấu trúc bảo toàn hành vi; nếu bạn đang thay đổi những gì mã làm, đó là một thay đổi riêng, làm riêng.
- Một bộ kiểm thử đáng tin cậy là điều kiện tiên quyết cho tái cấu trúc an toàn, không phải thứ thêm tùy chọn.
- Làm việc theo các bước nhỏ, có tên, đảo ngược được, và giữ cho mã hoạt động sau mỗi bước.
- Làm cho nợ kỹ thuật hiển thị và được theo dõi, rồi tài trợ việc trả nợ như năng lực ổn định thay vì chủ nghĩa anh hùng.
- Tái cấu trúc mã bạn đang thay đổi, nơi việc dọn dẹp xứng đáng với chỗ đứng của nó.
- Không phải nợ nào cũng đáng trả; mã ổn định, hiếm khi chạm đến, hoặc sắp bị loại bỏ có thể để yên.
- Đo chất lượng nội bộ để cung cấp thông tin cho phán đoán, không bao giờ như mục tiêu để bị lách.

## Khuyến nghị

### Giữ tái cấu trúc và thay đổi hành vi tách biệt nghiêm ngặt

Hãy quyết định trước khi bắt đầu bạn đang làm cái nào, và đừng bao giờ trộn lẫn hai thứ trong một commit. Khi bạn tái cấu trúc, các bài kiểm thử đã đạt trước đó phải đạt sau đó, không thay đổi, vì hành vi quan sát được không dịch chuyển. Khi bạn thay đổi hành vi, hãy làm điều đó như một commit riêng với các bài kiểm thử riêng. Lý do là thực tế: nếu một thay đổi hỗn hợp làm hỏng điều gì, bạn không thể biết việc tái cấu trúc của bạn hay thay đổi hành vi của bạn đã đưa lỗi vào, và trong đánh giá mã (chương 2.5) người đánh giá không thể suy luận rõ ràng về nửa nào. Thói quen hiệu quả là quy tắc hai chiếc mũ của Martin Fowler: bạn luôn đội hoặc chiếc mũ tái cấu trúc hoặc chiếc mũ tính năng, bạn biết cái nào, và bạn chuyển đổi có chủ đích. Các commit tách biệt cũng làm lịch sử [quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control) dễ đọc, để một kỹ sư chia đôi một thất bại có thể tự tin bỏ qua các commit tái cấu trúc thuần túy.

### Thiết lập lưới an toàn đáng tin cậy trước khi bạn tái cấu trúc

Tái cấu trúc không có kiểm thử chỉ là chỉnh sửa rồi hy vọng. Trước khi bạn tái cấu trúc bất cứ điều gì hệ trọng, bạn cần một bộ kiểm thử mà bạn tin sẽ bắt được thay đổi hành vi nếu bạn gây ra, đó là lập luận cốt lõi của chiến lược kiểm thử (chương 2.4). Với mã đã có độ bao phủ tốt, hãy chạy các bài kiểm thử, tái cấu trúc theo bước nhỏ, và chạy lại sau mỗi bước. Với mã cũ không có kiểm thử, bước đi trung thực là viết [kiểm thử đặc trưng](https://en.wikipedia.org/wiki/Characterization_test) trước. Một kiểm thử đặc trưng không khẳng định mã nên làm gì; nó nắm bắt những gì mã thực sự làm ngay bây giờ, kể cả các điểm kỳ quặc của nó, để bất kỳ thay đổi hành vi nào hiện ra như một bài kiểm thử thất bại. Michael Feathers phổ biến cách tiếp cận này cho đúng tình huống mà các tổ chức lớn đang sống: mã hoạt động, quan trọng và không có kiểm thử. Một khi hành vi hiện tại được ghim chặt, bạn có thể tái cấu trúc bên dưới nó một cách an toàn, và chỉ khi đó mới thay đổi hành vi bên trên.

### Học cách nhận diện mùi mã và áp dụng các phép tái cấu trúc nhỏ có tên

Một [mùi mã](https://en.wikipedia.org/wiki/Code_smell) là dấu hiệu bề mặt cho thấy có thứ gì bên dưới có thể cần chú ý: một hàm đã dài quá mức, một lớp biết quá nhiều, logic trùng lặp, một danh sách tham số dài, những cái tên nói dối về việc chúng làm. Một mùi là một gợi ý, không phải một phán quyết, nên bạn điều tra thay vì tuân theo nó một cách mù quáng. Phản ứng là một phép tái cấu trúc nhỏ, có tên từ danh mục của Fowler: Trích xuất Hàm, Đổi tên Biến, Di chuyển Phương thức, Thay Điều kiện bằng Đa hình, và hàng chục phép khác. Giá trị của việc dùng các bước đi có tên là mỗi bước nhỏ, được hiểu, an toàn một cách cơ học, và thường được IDE của bạn hỗ trợ trực tiếp. Bạn kết hợp những cải tiến lớn từ nhiều bước nhỏ đáng tin cậy, giữ mã xanh suốt, thay vì thực hiện một bước nhảy lớn mà bạn không kiểm chứng được.

### Ưu tiên tái cấu trúc cơ hội, và dành các chiến dịch cho nhu cầu cấu trúc thực sự

Phần lớn tái cấu trúc nên mang tính cơ hội, được gấp vào công việc bạn đang làm. Quy tắc hướng đạo sinh nắm bắt điều đó: để lại mã sạch hơn một chút so với khi bạn tìm thấy. Khi bạn chạm vào một tệp để thêm tính năng hay sửa lỗi, bạn đã hiểu góc đó, và những lần dọn dẹp nhỏ ở đó cộng dồn theo thời gian mà không cần sự cho phép của ai hay một ngân sách riêng. Các chiến dịch tái cấu trúc có kế hoạch, nơi một đội dừng công việc tính năng để tái cấu trúc một khu vực lớn, đôi khi cần thiết, nhưng chúng tốn kém, khó lên lịch đối chiếu với áp lực sản phẩm, và rủi ro nếu khu vực đó được kiểm thử kém. Hãy dành các chiến dịch cho những vấn đề cấu trúc mà dọn dẹp cơ hội không với tới, và trình bày lập luận bằng bằng chứng về chi phí thay đổi bạn đang trả. Hãy ưu tiên giọt nhỏ đều đặn của các lần dọn dẹp nhỏ; nó bền hơn cuộc viết lại anh hùng thỉnh thoảng.

### Dùng mẫu cây đa bóp nghẹt cho thay đổi cấu trúc lớn

Khi cả một hệ thống con cần thay thế, đừng thử một cuộc viết lại đại bùng nổ chạy một năm và hợp nhất ở cuối; đó là cách các dự án hiện đại hóa chết. Hãy dùng [mẫu cây đa bóp nghẹt](https://en.wikipedia.org/wiki/Strangler_fig_pattern), được Martin Fowler đặt tên theo loài dây leo mọc quanh một cái cây và dần thay thế nó. Bạn đặt một mặt tiền trước hệ thống cũ, định tuyến từng lát chức năng một đến mã mới đằng sau mặt tiền đó, xác minh nó trên môi trường thực, và lặp lại cho đến khi hệ thống cũ bị bao quanh hoàn toàn và có thể loại bỏ. Mỗi lát nhỏ, phát hành được và đảo ngược được, nên rủi ro được giới hạn và giá trị đến liên tục. Một họ hàng gần, phân nhánh bằng trừu tượng, làm điều tương tự bên trong một cơ sở mã đơn lẻ: bạn đưa vào một tầng trừu tượng trên thứ bạn muốn thay thế, xây phần triển khai mới đằng sau nó trong khi cả hai cùng tồn tại, chuyển dần người dùng sang, và xóa phần triển khai cũ khi không còn gì phụ thuộc vào nó. Cả hai cho phép một [hệ thống cũ](https://en.wikipedia.org/wiki/Legacy_system) tiến hóa trong khi vẫn sống, đó là loại hiện đại hóa duy nhất mà hầu hết các tổ chức lớn thực sự gánh được.

### Coi nợ kỹ thuật là một danh mục, và làm cho nó hiển thị

Phép ẩn dụ nợ, do Ward Cunningham đặt ra, tách hai thứ: vốn gốc (mã lộn xộn hoặc đường tắt tự thân) và lãi (công sức thêm mà mọi thay đổi trong tương lai phải trả vì nó). Không phải nợ nào cũng như nhau. Góc phần tư của Fowler phân loại nó theo hai trục: có chủ ý so với vô tình, và thận trọng so với liều lĩnh. Nợ thận trọng-có chủ ý ("chúng ta phát hành bây giờ và dọn dẹp sprint sau, và chúng ta biết chi phí") là một quyết định kinh doanh chính đáng. Nợ liều lĩnh-vô tình ("mẫu thiết kế là gì?") chỉ là thiệt hại. Công việc quản lý, kết nối với ra quyết định và quản trị (chương 1.5) và cách nó coi nợ như một danh mục, là làm cho nợ hiển thị để nó có thể được suy luận: theo dõi các hạng mục quan trọng nơi công việc sống, gắn thẻ mã, và ghi lại lãi bạn đang trả để việc trả nợ cạnh tranh năng lực dựa trên bằng chứng thay vì dựa vào ai phàn nàn lớn nhất. Nợ bạn không thấy, bạn không quản lý được.

### Tài trợ việc trả nợ như năng lực ổn định, không phải chủ nghĩa anh hùng

Chế độ thất bại là coi việc dọn dẹp là thứ bạn sẽ làm "khi mọi thứ lắng xuống", điều không bao giờ xảy ra. Mô hình bền vững là một năng lực cố định, được bảo vệ cho việc trả nợ: một lát tường minh của mỗi chu kỳ, hoặc một thỏa thuận thường trực rằng việc dọn dẹp đi cùng công việc tính năng trong cùng khu vực. Điều không hiệu quả là sprint anh hùng định kỳ nơi ai đó đốt một cuối tuần để sửa mọi thứ, vì nó không bền vững, không được rà soát, và thường tự hoàn tác. Năng lực ổn định giữ các khoản trả lãi ở mức thấp và tránh chu kỳ bùng nổ-sụp đổ nơi nợ tích tụ cho đến khi một cuộc khủng hoảng buộc phải viết lại đắt đỏ. Đây là cam kết quản lý cũng như thực hành kỹ thuật, và nó thuộc về cách bạn lập kế hoạch bảo trì phần mềm (chương 3.7) trong suốt vòng đời của một hệ thống.

### Đo chất lượng nội bộ, nhưng đừng để phép đo trở thành mục tiêu

Bạn có thể đo chất lượng nội bộ bằng các tín hiệu như [độ phức tạp chu trình](https://en.wikipedia.org/wiki/Cyclomatic_complexity) (số đường độc lập qua một hàm), sự trùng lặp, độ bao phủ kiểm thử, tỷ lệ thay đổi thất bại, và các thay đổi mất bao lâu ở những khu vực bạn nghi ngờ. Những con số này hữu ích để phát hiện nơi nợ tập trung và để theo dõi xu hướng theo thời gian. Mối nguy là định luật Goodhart: khi một phép đo trở thành mục tiêu, nó ngừng đo bất cứ thứ gì thực. Bắt buộc một con số độ bao phủ và bạn có các bài kiểm thử không khẳng định gì; thưởng cho điểm độ phức tạp thấp và bạn có logic bị rải ra nhiều hàm hơn để né chỉ số. Hãy dùng chỉ số để khởi đầu các cuộc trò chuyện và xác định các điểm nóng, và đừng bao giờ nối một chỉ số chất lượng với một cổng mà mọi người có động cơ để lách.

### Biết khi nào không tái cấu trúc

Tái cấu trúc là một khoản đầu tư, và một số mã sẽ không bao giờ hoàn vốn. Nếu một mô-đun ổn định, hiếm khi được chạm đến, và được hiểu đủ để thay đổi vào những dịp hiếm hoi bạn phải làm, dọn dẹp nó là công sức bỏ ra cho lãi bạn không phải trả. Nếu mã sắp bị loại bỏ, tái cấu trúc nó là đánh bóng thứ bạn sắp vứt đi. Kỷ luật là chi ngân sách dọn dẹp của bạn ở nơi thay đổi thường xuyên và đau đớn, nơi giảm lãi thực sự cộng dồn, và để yên những góc yên tĩnh.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| Tái cấu trúc cơ hội (quy tắc hướng đạo sinh) | Rẻ, liên tục, không cần ngân sách riêng, cộng dồn theo thời gian | Độ bao phủ không đồng đều; các tệp nóng cải thiện trong khi tệp lạnh mục nát |
| Chiến dịch tái cấu trúc có kế hoạch | Sửa các vấn đề cấu trúc mà dọn dẹp không với tới | Tốn kém; cạnh tranh với tính năng; rủi ro nếu thiếu kiểm thử tốt |
| Cây đa bóp nghẹt / phân nhánh bằng trừu tượng | Tăng dần, đảo ngược được, giữ hệ thống sống, giới hạn rủi ro | Chậm hơn viết lại trên giấy; cần kỷ luật để hoàn thành |
| Viết lại đại bùng nổ | Trang giấy trắng; không ràng buộc cũ | Tỷ lệ thất bại cao; thời gian đến giá trị dài; khoảng trống hành vi |
| Nợ thận trọng có chủ ý | Phát hành giá trị ngay; trả nợ tường minh, có kế hoạch | Trở thành liều lĩnh nếu việc trả không bao giờ được lên lịch |
| Chất lượng được chỉ số đặt cổng | Khách quan, hiển thị, bắt trôi dạt sớm | Mời gọi việc lách; phạt sắc thái; có thể làm suy giảm chất lượng thực |

Căng thẳng trung tâm là tốc độ bây giờ so với khả năng thay đổi sau này, và nó là thật. Phát hành một đường tắt có thể là lựa chọn đúng khi hạn chót là thật và nợ là thận trọng và được theo dõi. Sai lầm là giả vờ nợ miễn phí, hoặc để nó tích tụ vô hình cho đến khi hệ thống quá đắt để thay đổi. Hãy giải quyết bằng cách làm sự đánh đổi tường minh mỗi lần: gọi tên khoản nợ, ước tính lãi, quyết định có chủ đích, và ghi lại quyết định để việc trả nợ có thể được lên lịch thay vì bị lãng quên. Một đội vay có ý thức và trả đều đặn giữ được tốc độ nhiều năm; một đội vay mù quáng chậm dần đến dừng hẳn.

## Câu hỏi để thảo luận với đội của bạn

1. **Làm thế nào chúng ta giữ tái cấu trúc và thay đổi hành vi khỏi tràn vào cùng một commit, và việc đánh giá của chúng ta có thực sự thực thi điều đó không?** Đây là kỷ luật nền tảng của toàn bộ chương, và là kỷ luật bị vi phạm nhiều nhất dưới áp lực hạn chót, vì có cảm giác hiệu quả khi "dọn cái này luôn khi mình đang ở đây" và phát hành tất cả cùng nhau. Chi phí đáp xuống sau: khi một commit hỗn hợp làm hỏng môi trường thực, không ai biết được việc tái cấu trúc hay tính năng gây ra nó, và việc chia đôi qua lịch sử của bạn thôi đáng tin cậy. Hãy mang một nhúm pull request gần đây và kiểm tra trung thực bao nhiêu cái trộn lẫn hai chiếc mũ. Cân nhắc đối lập là ma sát, vì tách công việc thành các commit riêng tốn thêm chút công sức ban đầu. Câu trả lời nên định hình quy ước commit và danh sách kiểm tra đánh giá của bạn.

2. **Nợ kỹ thuật của chúng ta ở đâu, chúng ta đang trả bao nhiêu lãi cho nó, và ai quyết định điều gì được trả?** Hầu hết các đội không thể trả lời điều này, đó chính là vấn đề thực sự, vì nợ bạn không thấy được quản lý bởi ai phàn nàn lớn nhất thay vì bởi nơi chi phí thực sự nằm. Làm nó hiển thị nghĩa là theo dõi các hạng mục quan trọng, gắn thẻ mã, và thu thập bằng chứng về khu vực nào làm thay đổi chậm và dễ thất bại. Lực kéo đối lập là mỗi giờ dành cho trả nợ là một giờ không dành cho tính năng, nên quyết định phải là quyết định danh mục được đưa ra với ban lãnh đạo, kết nối với cách bạn quản trị công việc kỹ thuật (chương 1.5). Hãy mang dữ liệu tỷ lệ thay đổi thất bại và danh sách các tệp mà mọi người ngại chạm vào. Câu trả lời nên biến thành một năng lực trả nợ ổn định, được bảo vệ, không phải ý định mơ hồ để dọn dẹp khi mọi thứ lắng xuống.

3. **Những phần nào của cơ sở mã chúng ta nên cố ý không tái cấu trúc, và làm sao chúng ta biết?** Tái cấu trúc mọi thứ cũng là thất bại ngang với không tái cấu trúc gì, vì công sức bỏ ra dọn mã ổn định, hiếm khi chạm đến, hoặc sắp bị loại bỏ là lãi trả cho một khoản vay bạn không nợ. Phán đoán là thật: một mô-đun có thể trông xấu mà vẫn là nơi sai để đầu tư nếu không ai bao giờ thay đổi nó. Hãy mang dữ liệu tần suất thay đổi của bạn cùng với các tín hiệu độ phức tạp, vì giao điểm của biến động cao và độ phức tạp cao là nơi dọn dẹp cộng dồn, trong khi mã ít biến động thường tốt nhất là để yên. Rủi ro đối lập là "chúng ta sẽ để nó" trở thành cái cớ không bao giờ chạm vào bất cứ thứ gì khó. Câu trả lời nên cho bạn một danh sách rút gọn tường minh các điểm nóng đáng đầu tư và sự cho phép bỏ qua các góc yên tĩnh.

4. **Chúng ta có tin bộ kiểm thử của mình đủ để tái cấu trúc mã chúng ta cần thay đổi nhất không, và chúng ta sẽ phải viết kiểm thử đặc trưng trước ở đâu?** Một lưới an toàn bạn không thể tin biến tái cấu trúc thành chỉnh sửa rồi hy vọng, và trong một đội lớn mã đáng sợ nhất thường là mã ít được kiểm thử nhất, chính là nơi dọn dẹp sẽ hoàn vốn nhiều nhất. Hãy mang dữ liệu độ bao phủ và tỷ lệ thay đổi thất bại cho các điểm nóng của bạn, và thành thật về những mô-đun quan trọng nào sẽ không cho bạn cảnh báo nào nếu một lần tái cấu trúc làm thay đổi hành vi. Cân nhắc đối lập là viết kiểm thử đặc trưng cho mã cũ chậm và không hào nhoáng, không phát hành tính năng nào, nên dễ dàng trì hoãn mãi. Trong các hệ thống doanh nghiệp và chính phủ chịu kiểm toán và kiểm soát thay đổi, những kiểm thử được ghim chặt đó cũng là bằng chứng rằng một thay đổi bảo toàn hành vi, nên tài trợ chúng vừa là biện pháp an toàn vừa là biện pháp tuân thủ; câu trả lời nên nêu tên những khu vực nào nhận được bộ khung kiểm thử trước khi có ai chạm vào.

5. **Khi một hệ thống con thực sự cần thay thế, làm thế nào chúng ta quyết định giữa cách tiếp cận cây đa bóp nghẹt tăng dần và viết lại, và ai có thẩm quyền nói không với việc viết lại?** Viết lại đại bùng nổ là lựa chọn quyến rũ nhất và dễ thất bại nhất trên bàn, vì trang giấy trắng luôn trông rẻ hơn trên giấy so với sống với các ràng buộc cũ. Với một tổ chức lớn, con đường tăng dần (một mặt tiền, từng lát một, xác minh trên môi trường thực) giữ hệ thống sống và giới hạn rủi ro, nhưng chậm hơn, đòi hỏi kỷ luật để hoàn thành, và cạnh tranh với sự thèm muốn một khởi đầu mới. Hãy mang bản đồ tần suất thay đổi của hệ thống con, một ước tính trung thực về việc viết lại sẽ chạy bao lâu trước khi mang lại giá trị, và các khoảng trống hành vi mà một cuộc viết lại song song phải đóng. Trong bối cảnh chính phủ và chịu quy định, một cuộc viết lại nhiều năm hợp nhất ở cuối hiếm khi sống sót qua kiểm toán, nên câu trả lời nên mặc định là cây đa bóp nghẹt hoặc phân nhánh bằng trừu tượng và coi bất kỳ cuộc viết lại nào là ngoại lệ phải được lập luận bằng bằng chứng.

6. **Làm thế nào chúng ta dùng các chỉ số chất lượng nội bộ để tìm nơi nợ tập trung mà không để một con số trở thành mục tiêu mọi người lách?** Các chỉ số như độ phức tạp, sự trùng lặp, độ bao phủ và tỷ lệ thay đổi thất bại là cách duy nhất để một tổ chức lớn nhìn xuyên qua mã mà không ai đọc hết, nhưng khoảnh khắc một cái được nối với một cổng hoặc một đánh giá hiệu suất, định luật Goodhart chiếm lĩnh và con số ngừng đo bất cứ thứ gì thực. Hãy mang các ví dụ về nơi một chỉ số đã thúc đẩy hành vi, và hỏi liệu nó đang khởi đầu các cuộc trò chuyện hay âm thầm thưởng cho các bài kiểm thử không khẳng định gì và logic bị rải qua các hàm để né một ngưỡng. Lực kéo đối lập là lãnh đạo muốn một con số bảng điều khiển đơn giản, và "dùng phán đoán" khó bán hơn một thanh xanh. Trong bối cảnh doanh nghiệp và chính phủ nơi các chỉ số nuôi báo cáo quản trị, hãy nói rõ rằng các tín hiệu chất lượng cung cấp thông tin cho đầu tư và xác định điểm nóng nhưng không bao giờ đặt cổng cho cá nhân; câu trả lời nên vạch một lằn ranh cứng giữa đo để học và đo để phán xét.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không còn dư nguồn vốn, chỉ tái cấu trúc theo cơ hội: đội một chiếc mũ mỗi commit để lịch sử vẫn chia đôi được, và giữ một danh sách ngắn, trung thực các đường tắt bạn đã đi một cách có chủ đích. Đừng khởi động các chiến dịch dọn dẹp hay đánh bóng các mô-đun ổn định; hãy dành sự chú ý khan hiếm cho tệp duy nhất mà ai cũng ngại, và chỉ viết kiểm thử đặc trưng ở nơi một thay đổi thực sự làm bạn sợ. Nợ có chủ ý, hiển thị là ổn ở giai đoạn này; nợ liều lĩnh vô hình là thứ giết bạn.

**Doanh nghiệp nhỏ.** Không có chuyên gia nền tảng hay công cụ riêng và ngân sách eo hẹp, hãy dựa vào những gì IDE và hệ sinh thái ngôn ngữ của bạn cho miễn phí: các phép đổi tên và trích xuất tự động, một linter, và một tín hiệu độ bao phủ cơ bản. Hãy coi phần lớn nợ là thứ bạn quản lý trong quá trình làm việc bình thường thay vì thứ bạn thuê tư vấn để sửa, và ưu tiên mua các thư viện được bảo trì tốt hơn là xây rồi phải tái cấu trúc của chính mình. Hãy dành nỗ lực trả tiền hiếm hoi cho hệ thống duy nhất mà sự chậm chạp của nó đang trực tiếp tốn khách hàng của bạn.

**Doanh nghiệp lớn.** Qua nhiều đội vấn đề là quản trị danh mục: một sổ đăng ký nợ dùng chung, gắn thẻ nhất quán các điểm nóng theo tần suất thay đổi và độ phức tạp, và một lát năng lực được bảo vệ của mỗi đội cho việc trả nợ để dọn dẹp ngừng thua tính năng theo mặc định. Chuẩn hóa kỷ luật hai chiếc mũ và thực hành kiểm thử đặc trưng để bất kỳ kỹ sư nào chuyển giữa các đội đều thấy cùng các quy tắc, và dùng cây đa bóp nghẹt cùng phân nhánh bằng trừu tượng cho thay đổi cấu trúc được điều phối qua các nhóm. Giữ các chỉ số chất lượng mang tính thông tin để chúng xác định nợ mà không bị lách trong các đánh giá hiệu suất.

**Chính phủ.** Các hệ thống tồn tại lâu dưới sự kiểm toán và kiểm soát thay đổi nghiêm ngặt khiến tái cấu trúc có kỷ luật trở thành tài sản tuân thủ, không chỉ là tài sản kỹ thuật: giữ việc tái cấu trúc tách biệt nghiêm ngặt khỏi thay đổi hành vi cho phép kiểm toán viên thấy chính xác những commit nào đã thay đổi hành vi và những commit nào chỉ dọn dẹp. Quy tắc mua sắm và minh bạch ưu ái các bước nhỏ, đảo ngược được, có bằng chứng hậu thuẫn hơn các cuộc viết lại đại bùng nổ, nên hãy mặc định cây đa bóp nghẹt với các kiểm thử đặc trưng ghi lại rằng hành vi được bảo toàn. Hãy biến sổ đăng ký nợ và kế hoạch trả nợ của nó thành một phần của hồ sơ bảo trì hệ thống để các cơ quan giám sát có được khả năng truy vết mà họ yêu cầu.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người phát hành nhanh và biết mình đang gánh nợ, nên họ làm tốt hai việc rẻ. Mỗi pull request đội một chiếc mũ: các commit tái cấu trúc tách khỏi các commit tính năng, giữ lịch sử có thể chia đôi ngay cả ở vận tốc cao. Và họ giữ một danh sách ngắn, trung thực các đường tắt họ đã đi một cách có chủ đích, với một ghi chú một dòng về lãi mỗi cái tốn. Khi một mô-đun thanh toán trở thành tệp mà ai cũng ngại, danh sách đó cộng với lịch sử thay đổi thất bại của họ đưa ra lập luận để dành hai ngày trích xuất một ranh giới sạch hơn. Họ viết kiểm thử đặc trưng để ghim hành vi hiện tại, tái cấu trúc bên dưới bằng các phép đổi tên và trích xuất của IDE, và không bao giờ chạm vào các mô-đun ổn định mà không ai thay đổi. Khoản nợ họ mang là có chủ ý và hiển thị, nên nó không bao giờ biến thành loại liều lĩnh.

**Doanh nghiệp lớn.** Một công ty hậu cần toàn cầu vận hành một hệ thống đơn hàng mười lăm năm tuổi mà nhiều đội thay đổi mỗi tuần. Thay vì viết lại, họ áp dụng mẫu cây đa bóp nghẹt: một mặt tiền đứng trước khối đơn, và từng năng lực có ranh giới một được định tuyến lại đến các dịch vụ mới đằng sau nó, được xác minh trên môi trường thực trước khi lát tiếp theo bắt đầu. Điều phối việc này qua các đội và một hệ thống tồn tại lâu (chương 10.4) là phần khó, nên họ duy trì một sổ đăng ký nợ dùng chung, gắn thẻ các điểm nóng theo tần suất thay đổi và độ phức tạp, và dành một lát cố định năng lực của mỗi đội cho việc trả nợ. Các chỉ số chất lượng nội bộ cho biết nơi cần nhìn nhưng không bao giờ đặt cổng cho đánh giá hiệu suất của ai, giữ các con số trung thực. Trong hai năm khối đơn thu nhỏ đều đặn và không thay đổi đơn lẻ nào từng đe dọa cả hệ thống.

**Chính phủ.** Một cơ quan thuế quốc gia phải hiện đại hóa một nền tảng đánh giá hàng chục năm tuổi dưới các quy tắc kiểm toán và kiểm soát thay đổi nghiêm ngặt, nơi mỗi thay đổi mã là một sự kiện được quản trị, có bằng chứng hậu thuẫn. Một cuộc viết lại đại bùng nổ là bất khả, nên họ dùng phân nhánh bằng trừu tượng: một tầng trừu tượng được đưa vào trên công cụ tính toán cũ, một phần triển khai mới được xây đằng sau nó, và người dùng được di chuyển từng quy tắc thuế một, mỗi lần di chuyển được ghi lại như một thay đổi nhỏ, đảo ngược được với kiểm thử đặc trưng chứng minh hành vi không đổi. Vì tái cấu trúc được giữ tách biệt nghiêm ngặt khỏi bất kỳ thay đổi hành vi lập pháp nào, kiểm toán viên có thể thấy chính xác commit nào đã thay đổi hành vi và commit nào chỉ tái cấu trúc. Sổ đăng ký nợ và kế hoạch trả nợ của nó trở thành một phần của hồ sơ bảo trì hệ thống (chương 3.7), cho các cơ quan giám sát khả năng truy vết mà họ yêu cầu.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của tái cấu trúc và trả nợ là khả năng bền vững để thay đổi phần mềm một cách rẻ, và với hầu hết các hệ thống, phần lớn chi phí vòng đời là bảo trì, nên đây là nơi tổng chi phí sở hữu phần lớn được quyết định. Lãi trên nợ kỹ thuật được trả bằng đơn vị tiền tệ mà ban lãnh đạo vốn đã theo dõi: phân phối chậm hơn, tỷ lệ thay đổi thất bại cao hơn, thời gian phục hồi sự cố dài hơn, và các kỹ sư tránh mã đáng sợ nhất. Khi bạn làm nợ hiển thị và tài trợ việc trả đều đặn, bạn giảm chi phí của mọi thay đổi trong tương lai ở những khu vực quan trọng nhất, và tránh mô hình bùng nổ-sụp đổ nơi nợ bị bỏ bê buộc phải viết lại khẩn cấp đắt đỏ.

Chi phí áp dụng khiêm tốn và chủ yếu mang tính văn hóa: thiết lập kỷ luật hai chiếc mũ, xây lưới an toàn ở nơi bạn cần tái cấu trúc, giữ một sổ đăng ký nợ, và bảo vệ một lát năng lực ổn định cho việc trả nợ. Chi phí của sự bỏ bê cộng dồn lặng lẽ. Lãi tích lũy trên mọi thay đổi cho đến khi vận tốc sụp đổ và tổ chức thấy mình bị đóng băng, không thể sửa đổi an toàn một hệ thống mà nó không còn hiểu, đó là kết quả đắt đỏ nhất trong tất cả. Để thuyết phục ban lãnh đạo, hãy kết nối nợ trực tiếp với các chỉ số phân phối họ đã quan tâm, và đóng khung việc trả nợ như một quyết định danh mục với lợi ích đo được, không phải kỹ sư xin thời gian để dọn dẹp.

## Phản mẫu và cạm bẫy

- **Trộn tái cấu trúc với thay đổi hành vi:** một commit làm cả hai, nên một lỗi hỏng không thể quy cho ai và lịch sử trở nên không đáng tin.
- **Tái cấu trúc không có lưới an toàn:** tái cấu trúc mã chưa kiểm thử rồi hy vọng, là chỉnh sửa bằng niềm tin.
- **Viết lại đại bùng nổ:** thay thế một hệ thống đang hoạt động một lần, một mẫu hình có tỷ lệ thất bại cao và thời gian đến giá trị dài.
- **Tái cấu trúc như một cuối tuần anh hùng:** dọn dẹp không được rà soát, không bền vững, tự hoàn tác thay vì năng lực ổn định.
- **Nợ vô hình:** những đường tắt không ai theo dõi, nên việc trả nợ bị dẫn dắt bởi khối lượng phàn nàn thay vì chi phí thực.
- **Lách chỉ số chất lượng:** đạt mục tiêu độ bao phủ hoặc độ phức tạp trong khi chất lượng thực giảm, vì phép đo đã thành mục tiêu.
- **Tái cấu trúc sai mã:** đánh bóng các mô-đun ổn định hoặc sắp bị loại bỏ trong khi các điểm nóng thực vẫn tốn kém cho bạn.
- **Tái cấu trúc vĩnh viễn:** tái cấu trúc vô tận không bao giờ phát hành giá trị, hình ảnh phản chiếu của việc không bao giờ dọn dẹp.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Tái cấu trúc tùy nghi và phản ứng, thường trộn với thay đổi hành vi trong cùng một commit. Không có lưới an toàn đáng tin, nợ kỹ thuật vô hình và không được theo dõi, và việc dọn dẹp chỉ xảy ra trong những đợt anh hùng thỉnh thoảng hoặc không bao giờ.
- **Mức 2, Phát triển:** Một số đội tách tái cấu trúc khỏi thay đổi hành vi và dựa vào kiểm thử ở nơi có, và các phép tái cấu trúc có tên cùng kiểm thử đặc trưng xuất hiện rải rác. Thực hành không nhất quán giữa các đội, nợ được thảo luận và đôi khi được ghi lại, và việc trả nợ cạnh tranh tùy nghi với tính năng và thường thua.
- **Mức 3, Chuẩn hóa:** Kỷ luật hai chiếc mũ, kiểm thử đặc trưng cho mã cũ và các phép tái cấu trúc nhỏ có tên được lập thành tài liệu và kỳ vọng toàn tổ chức. Nợ được theo dõi trong một sổ đăng ký dùng chung tách vốn gốc khỏi lãi, và một năng lực được bảo vệ cho việc trả nợ được lên kế hoạch mỗi chu kỳ và thực thi trong đánh giá.
- **Mức 4, Quản lý:** Nợ và dọn dẹp được đo và kiểm soát bằng dữ liệu theo các đường cơ sở. Bạn theo dõi tần suất thay đổi và độ phức tạp để xác định điểm nóng, theo dõi tỷ lệ thay đổi thất bại và thời gian dẫn thay đổi trong các khu vực đã tái cấu trúc, và ghi lại lãi mỗi hạng mục quan trọng tốn, để quyết định trả nợ dựa trên bằng chứng và các lời gọi loại bỏ-hay-đầu tư được đưa ra dựa trên xu hướng thay vì khối lượng phàn nàn. Tín hiệu chất lượng cung cấp thông tin cho đầu tư mà không bị nối với các cổng mà mọi người có thể lách.
- **Mức 5, Điều phối:** Nợ được quản lý như một danh mục được cân bằng lại liên tục, tích hợp với hoạch định sản phẩm và bảo trì trong toàn tổ chức. Thay đổi cấu trúc thường xuyên dùng cây đa bóp nghẹt và phân nhánh bằng trừu tượng được điều phối qua các đội, việc trả nợ liên tục và khớp với nơi thay đổi thường xuyên và đau đớn, và thực hành thích ứng khi hệ thống và bức tranh rủi ro dịch chuyển, để mã tồn tại lâu còn thay đổi được qua nhiều thập kỷ.

## Ý tưởng để thảo luận

1. Quy tắc thực tế, được thực thi của đội bạn để giữ tái cấu trúc tách biệt khỏi thay đổi hành vi là gì, và nó vỡ ra ở đâu dưới áp lực hạn chót?
2. Làm thế nào bạn quyết định, bằng bằng chứng, mã nào xứng đáng được dọn dẹp và mã nào tốt nhất để yên?
3. Kiểm thử đặc trưng sẽ cho phép bạn tái cấu trúc an toàn khu vực cũ nào mà hiện nay bạn tránh?
4. Với lần hiện đại hóa lớn tiếp theo của bạn, một cách tiếp cận cây đa bóp nghẹt sẽ trông như thế nào, và mặt tiền hay tầng trừu tượng nào bạn sẽ đưa vào đầu tiên?
5. Ai sở hữu sổ đăng ký nợ kỹ thuật, và việc trả nợ thực sự giành năng lực thắng công việc tính năng bằng cách nào?

## Những điểm cần ghi nhớ

- Tái cấu trúc bảo toàn hành vi; giữ nó tách biệt nghiêm ngặt khỏi thay đổi hành vi, trong các commit riêng.
- Một bộ kiểm thử đáng tin cậy là điều kiện tiên quyết cho tái cấu trúc an toàn, và kiểm thử đặc trưng cho mã cũ một bộ như vậy.
- Làm việc theo các bước nhỏ, có tên, đảo ngược được, ưu tiên dọn dẹp cơ hội, và dùng cây đa bóp nghẹt hoặc phân nhánh bằng trừu tượng cho thay đổi cấu trúc lớn.
- Làm nợ kỹ thuật hiển thị, tách vốn gốc khỏi lãi, và tài trợ việc trả nợ như năng lực ổn định thay vì chủ nghĩa anh hùng.
- Đo chất lượng nội bộ để dẫn dắt phán đoán, không bao giờ như mục tiêu để lách, và đừng tái cấu trúc mã ổn định hoặc sắp bị loại bỏ.

## Tài liệu tham khảo và đọc thêm

- Martin Fowler, *Refactoring: Improving the Design of Existing Code*, ấn bản thứ hai
- Michael Feathers, *Working Effectively with Legacy Code*
- Ward Cunningham, *The WyCash Portfolio Management System* (báo cáo kinh nghiệm OOPSLA 1992, nguồn gốc của phép ẩn dụ nợ)
- Martin Fowler, "TechnicalDebtQuadrant" và "StranglerFigApplication" (martinfowler.com)
- Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
