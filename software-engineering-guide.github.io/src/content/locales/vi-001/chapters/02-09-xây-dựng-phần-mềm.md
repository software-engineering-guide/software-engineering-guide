# 2.9 Xây dựng phần mềm

## Tổng quan và động lực

[Xây dựng phần mềm](https://en.wikipedia.org/wiki/Software_construction) là nơi thiết kế trở thành mã đang chạy. Đó là công việc chi tiết của lập trình, kiểm chứng, [kiểm thử đơn vị](https://en.wikipedia.org/wiki/Unit_testing), [kiểm thử tích hợp](https://en.wikipedia.org/wiki/Integration_testing) và [gỡ lỗi](https://en.wikipedia.org/wiki/Debugging). Hướng dẫn [Bộ Kiến thức Kỹ thuật Phần mềm](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) coi xây dựng là một lĩnh vực kiến thức riêng, và có lý do chính đáng: đây là nơi phần lớn công việc hằng ngày của bạn diễn ra. Những lựa chọn bạn đưa ra từng dòng một (cách bạn kiềm chế độ phức tạp, cách bạn xử lý lỗi, bạn để mọi thứ dễ đọc đến đâu) quyết định liệu một hệ thống có thể được hiểu, thay đổi và tin cậy trong nhiều năm tới.

Trong một đội lớn, xây dựng là một nỗ lực tập thể, không phải đơn độc. Hàng trăm kỹ sư viết vào một cơ sở mã chung sẽ tồn tại lâu hơn thời gian của bất kỳ ai trong đội. Vì vậy tiêu chuẩn không phải là "nó có chạy trên máy của tôi hôm nay không". Mà là "một người lạ có thể thay đổi nó một cách an toàn sau năm năm không". Xây dựng kết nối lên phía trên với yêu cầu (chương 2.8) và thiết kế (chương 2.2), vốn cho bạn biết cần xây gì và hình dạng của nó. Nó kết nối sang ngang với tiêu chuẩn viết mã (chương 2.1), kiểm thử (chương 2.4) và đánh giá mã (chương 2.5), vốn định hình cách công việc được diễn đạt, xác minh và kiểm tra. Xây dựng tốt biến một thiết kế vững chắc thành một tài sản bảo trì được. Xây dựng kém biến ngay cả một thiết kế tốt thành một khoản nợ.

Trong bối cảnh doanh nghiệp và chính phủ, xây dựng mang thêm trọng lượng. Những hệ thống này sống lâu, chịu quy định chặt chẽ, và thường quan trọng về an toàn hoặc công dân. [Lập trình phòng thủ](https://en.wikipedia.org/wiki/Defensive_programming), xử lý lỗi có kỷ luật và mã hiển nhiên đúng không phải là điều dễ chịu ở đây; chúng là yêu cầu cho sự đảm bảo, kiểm toán và liên tục qua nhiều thập kỷ và sự thay đổi nhân sự. Mục tiêu là mã truyền đạt ý định của nó, chống lại thất bại và có thể được xác minh. Mã chỉ chạy được thôi thì chưa đủ.

## Các nguyên tắc chính

- Giảm thiểu độ phức tạp trên hết; kẻ thù chính của việc xây dựng quy mô lớn là mã mà không ai hiểu hoàn toàn.
- Dự đoán thay đổi; xây dựng sao cho các sửa đổi có khả năng xảy ra trong tương lai được khoanh vùng và rẻ.
- Xây dựng để kiểm chứng; viết mã mà tính đúng đắn của nó dễ kiểm tra bằng kiểm thử, đánh giá và suy luận.
- Tái sử dụng có chủ đích; xây dựng trên các thành phần hiện có đáng tin thay vì phát minh lại, nhưng tránh liên kết với các phép trừu tượng sai.
- Tuân theo tiêu chuẩn; sự nhất quán qua một cơ sở mã giảm chi phí nhận thức của mọi thay đổi trong tương lai.
- Xử lý lỗi và trạng thái không hợp lệ một cách tường minh; làm cho các chế độ thất bại hiển thị thay vì im lặng.
- Giữ mã dễ đọc; xây dựng trước hết là giao tiếp với những người bảo trì tương lai, sau đó mới là với trình biên dịch.

## Khuyến nghị

### Giảm thiểu độ phức tạp như kỷ luật chính

Hãy biến việc giảm độ phức tạp, cả bản chất lẫn ngẫu nhiên, thành mục tiêu trung tâm của bạn. Viết các hàm và mô-đun nhỏ, đơn mục đích. Ưu tiên tên rõ ràng hơn mánh khéo. Giữ độ lồng nông và luồng điều khiển tuyến tính. Khoanh vùng các quyết định để việc hiểu một đoạn mã không buộc bạn phải giữ cả hệ thống trong đầu. Độ phức tạp là thứ khiến các cơ sở mã lớn chậm thay đổi và nguy hiểm khi chạm vào, vì vậy hãy cân nhắc mọi lựa chọn theo việc nó thêm độ phức tạp hay loại bỏ nó. Hãy áp dụng các nguyên tắc thiết kế trong chương 2.2 ở quy mô nhỏ nữa: độ kết dính cao, độ liên kết thấp và [tách biệt các mối quan tâm](https://en.wikipedia.org/wiki/Separation_of_concerns) rõ ràng quan trọng trong một hàm đơn lẻ cũng như trong một kiến trúc.

### Xây dựng cho thay đổi và cho kiểm chứng

Hãy nghĩ trước đến những thay đổi có nhiều khả năng đến nhất (quy tắc kinh doanh mới, tích hợp mới, quy định mới) và cô lập chúng sau các giao diện ổn định để thay đổi ở lại cục bộ. Đồng thời, hãy viết mã dễ kiểm chứng: [hàm thuần](https://en.wikipedia.org/wiki/Pure_function) (cùng đầu vào luôn cho cùng đầu ra, không có tác dụng phụ) ở nơi có thể, trạng thái ẩn tối thiểu, và các phụ thuộc được làm tường minh để các bài kiểm thử có thể thay thế chúng. Mã khó kiểm thử thường là mã khó hiểu và khó thay đổi. Khả năng kiểm thử (chương 2.4) là một tín hiệu thiết kế, không chỉ là mối quan tâm của QA.

### Tái sử dụng có chủ đích và chuẩn hóa

Hãy với tới các thư viện và thành phần nội bộ được bảo trì tốt, đáng tin trước khi viết lại logic nền tảng, và dùng chúng qua các giao diện rõ ràng (chương 2.3). Chỉ xây các thành phần tái sử dụng được khi có một trường hợp sử dụng thứ hai thực sự, vì khái quát hóa quá sớm tự nó là một dạng độ phức tạp. Áp dụng tiêu chuẩn và phong cách viết mã của tổ chức (chương 2.1) một cách đồng nhất, lý tưởng là được thực thi bởi các công cụ định dạng tự động và [linter](https://en.wikipedia.org/wiki/Lint_(software)), để toàn bộ cơ sở mã đọc như thể một tác giả cẩn thận đã viết nó.

### Thực hành lập trình phòng thủ có phán đoán

Xác thực đầu vào tại các ranh giới tin cậy (yêu cầu bên ngoài, I/O tệp và mạng, đầu vào người dùng) và coi bất kỳ dữ liệu nào đi qua các ranh giới đó là thù địch cho đến khi được chứng minh ngược lại. Tuy nhiên, bên trong một mô-đun được kiểm thử tốt, đừng nhấn chìm mỗi dòng trong các kiểm tra dư thừa che giấu logic và triệt tiêu các thất bại thực sự. Quy tắc đơn giản: phòng thủ ở các ranh giới, tin tưởng bên trong chúng. Dùng [khẳng định](https://en.wikipedia.org/wiki/Assertion_(software_development)) để ghi lại và thực thi các bất biến mà không bao giờ được sai trong một chương trình đúng. Dùng [ngoại lệ](https://en.wikipedia.org/wiki/Exception_handling) và xử lý lỗi cho các điều kiện có thể xảy ra một cách chính đáng lúc chạy. Giữ hai thứ này tách biệt: khẳng định bảo vệ các giả định của lập trình viên, xử lý lỗi quản lý thất bại được dự kiến.

### Xử lý lỗi một cách tường minh và thất bại an toàn

Với mỗi lỗi, hãy quyết định có chủ đích phải làm gì: phục hồi, thử lại, lan truyền hay thất bại nhanh. Không bao giờ âm thầm nuốt một ngoại lệ hay bỏ qua một lỗi được trả về; một thất bại bị triệt tiêu quay lại như một khiếm khuyết bí ẩn sau này. Giữ ngữ cảnh trong thông báo lỗi và nhật ký để thất bại có thể được chẩn đoán. Trong các hệ thống quan trọng về an toàn và công dân, hãy thất bại vào một trạng thái an toàn, đã biết thay vì tiếp tục trong một trạng thái bị hỏng. Hãy dành cho đường lỗi sự cân nhắc nhiều như đường suôn sẻ, vì trên môi trường thực đường lỗi là nơi niềm tin được giành hay mất.

### Xây dựng chất lượng vào trong quá trình xây dựng

Chất lượng được xây vào, không phải được kiểm tra vào sau đó. Viết kiểm thử đơn vị cùng với mã, chạy [phân tích tĩnh](https://en.wikipedia.org/wiki/Static_program_analysis) và linter liên tục, và giữ các hàm đủ nhỏ để suy luận. Dùng tên và cấu trúc tự giải thích để bình luận của bạn có thể giải thích vì sao, không phải cái gì. [Tái cấu trúc](https://en.wikipedia.org/wiki/Code_refactoring) trong lúc đi để giữ mã còn ở được. Đánh giá mã (chương 2.5) là chốt chặn của con người, nhưng phần lớn chất lượng cần có mặt trước khi việc đánh giá bắt đầu.

### Chọn và chuẩn hóa công cụ xây dựng

Hãy chuẩn hóa bộ công cụ (trình biên dịch, hệ thống dựng, công cụ định dạng, linter, bộ phân tích tĩnh, trình gỡ lỗi, trình quản lý phụ thuộc và cấu hình IDE) để mọi kỹ sư làm việc trong một môi trường nhất quán, tái tạo được. Nối các công cụ này vào đường ống để các kiểm tra chất lượng không phải tùy chọn. Hãy đưa các công cụ lập trình có AI hỗ trợ vào một cách có chủ đích, và coi đầu ra của chúng là bản nháp phải qua cùng tiêu chuẩn, đánh giá và kiểm thử như bất kỳ mã nào khác.

## Đánh đổi: ưu và nhược điểm

| Thực hành | Ưu điểm | Nhược điểm |
|---|---|---|
| Giảm thiểu độ phức tạp quyết liệt | Dễ đọc, thay đổi được, tỷ lệ lỗi thấp | Có thể có cảm giác chậm; rủi ro trừu tượng quá mức nếu áp dụng sai |
| Kiểm tra phòng thủ rộng rãi | Bắt trạng thái xấu sớm, ranh giới vững chắc | Làm lộn xộn logic; có thể che giấu lỗi thực nếu quá đà |
| Khẳng định cho bất biến | Ghi lại và thực thi các giả định | Bị tắt trong một số bản dựng môi trường thực; không phải xử lý lỗi |
| Tái sử dụng thư viện nhiều | Ít mã phải sở hữu hơn; phân phối nhanh hơn | Rủi ro phụ thuộc, liên kết, phơi nhiễm chuỗi cung ứng |
| Tiêu chuẩn và linter nghiêm ngặt | Cơ sở mã đồng nhất, ít ma sát | Thiết lập ban đầu; có thể có cảm giác cứng nhắc với cá nhân |
| Xây dựng cho khả năng kiểm thử | Mã kiểm chứng được, thay đổi được | Có thể thêm sự gián tiếp mà một số người coi là nghi thức |

Sự đánh đổi trung tâm trong xây dựng là tốc độ ngắn hạn so với khả năng thay đổi dài hạn. Cắt góc (bỏ xử lý lỗi, dung thứ độ phức tạp, phớt lờ tiêu chuẩn) có cảm giác nhanh hơn ngay lúc đó, và hầu như luôn đắt hơn trong suốt vòng đời của hệ thống. Thất bại ngược lại là thiết kế quá mức: quá nhiều phòng thủ, trừu tượng suy đoán, và tính tổng quát không ai cần. Xây dựng điêu luyện nằm ở giữa: đơn giản nhất có thể, phòng thủ đến mức các ranh giới đòi hỏi, và không hơn.

## Câu hỏi để thảo luận với đội của bạn

1. **Định nghĩa chung, cụ thể của chúng ta về "quá phức tạp" là gì, và chúng ta thực thi nó ở đâu trước khi hợp nhất?** "Giảm thiểu độ phức tạp" là kỷ luật trung tâm của xây dựng, nhưng như một khẩu hiệu nó thua mọi cuộc tranh luận với hạn chót. Trong một đội lớn nơi hàng trăm người viết vào một cơ sở mã, độ phức tạp phải đo được, vì vậy hãy thống nhất các tín hiệu mà bạn thực sự sẽ hành động theo: độ dài hàm, độ sâu lồng, độ phức tạp chu trình, và số thứ mà một người đọc phải giữ trong đầu để hiểu một thay đổi. Hãy mang ví dụ tệ nhất của bạn đến cuộc họp và hỏi liệu việc đánh giá hiện tại của bạn có bắt được nó không. Câu trả lời nên biến thành một cổng đường ống hoặc một mục trong danh sách kiểm tra đánh giá, vì một ngưỡng được công cụ thực thi có giá trị hơn một nguyên tắc được thực thi bằng ý chí, và nó giúp người được tuyển tiếp theo của bạn khỏi sự tích tụ chậm chạp của mã mà không ai chạm vào được một cách an toàn.

2. **Trên môi trường thực, các đường lỗi của chúng ta có hành xử như chúng ta đã thiết kế không, và lần cuối cùng chúng ta cố ý thực hành một đường lỗi là khi nào?** Lời khuyên về xây dựng nói hãy dành cho đường lỗi sự cân nhắc nhiều như đường suôn sẻ, nhưng đường lỗi thường là mã ít được kiểm thử nhất mà bạn sở hữu, và trong một hệ thống quan trọng về công dân hoặc an toàn, nó là nơi niềm tin được giành hay mất. Một ngoại lệ bị triệt tiêu hay một mã trả về bị bỏ qua trở thành một khiếm khuyết bí ẩn vài tuần sau, và "thất bại vào trạng thái an toàn" là một lời hứa bạn không thể giữ nếu chưa bao giờ nhìn thấy nó xảy ra. Hãy mang lịch sử sự cố của bạn: bao nhiêu lần ngừng hoạt động trong quá khứ có nguồn gốc từ một lỗi bị nuốt hoặc một đường phục hồi chưa được kiểm thử? Hành động là kiểm thử thất bại một cách có chủ đích (tiêm thẻ bị từ chối, hết thời gian chờ, đầu vào sai định dạng) và yêu cầu mọi lỗi phải được xử lý, ghi nhật ký kèm ngữ cảnh, hoặc lan truyền, không bao giờ bị bỏ rơi trong im lặng.

3. **Những phần nào của cơ sở mã của chúng ta khó kiểm thử, và khó khăn đó đang nói gì với chúng ta về thiết kế?** Mã chống lại kiểm thử hầu như luôn là mã che giấu trạng thái, liên kết với các phụ thuộc sai, hoặc làm quá nhiều việc, nên khả năng kiểm thử là một tín hiệu thiết kế, không phải chuyện QA nghĩ đến sau. Trên một hệ thống doanh nghiệp tồn tại lâu, điều này quan trọng vì các mô-đun đau đớn khi kiểm thử hôm nay là những mô-đun mà một người lạ sẽ sợ thay đổi sau năm năm. Hãy mang lớp hoặc dịch vụ mà đội bạn ngại viết kiểm thử và hỏi vì sao: trạng thái bị ẩn, các phụ thuộc không thể thay thế, hàm đang làm ba việc? Câu trả lời nên dẫn dắt việc tái cấu trúc theo hướng hàm thuần, phụ thuộc tường minh và các đơn vị nhỏ đơn mục đích, vì làm cho mã kiểm chứng được cũng là công việc làm cho nó dễ hiểu và rẻ để thay đổi.

4. **Khi nào chúng ta tái sử dụng một thư viện bên ngoài so với tự xây năng lực đó, và ai sở hữu rủi ro chuỗi cung ứng mà chúng ta gánh?** Với tới một thư viện đáng tin nhanh hơn phát minh lại logic nền tảng, nhưng mỗi phụ thuộc bạn thêm vào là mã bạn không kiểm soát, không dễ kiểm toán, và phải vá vào ngày nó bị xâm phạm. Trong một đội lớn, mối nguy là một trăm kỹ sư mỗi người kéo vào các phụ thuộc bắc cầu riêng của mình cho đến khi không ai có thể nói cơ sở mã thực sự chạy gì. Hãy mang bản kiểm kê phụ thuộc của bạn và hỏi ba điều cụ thể: bao nhiêu thư viện không còn được bảo trì, bao nhiêu mang lỗ hổng đã biết, và bao nhiêu bọc logic đủ đơn giản để tự sở hữu. Cân nhắc đối lập là thật, vì tự viết mật mã hay xử lý ngày tháng gần như luôn tệ hơn một thư viện đã được thử lửa, nên mục tiêu là một chính sách tái sử dụng có chủ đích thay vì tránh né hoàn toàn. Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm góc độ mua sắm và tuân thủ giấy phép, vì một phụ thuộc chưa được kiểm duyệt có thể mang một giấy phép không tương thích với nghĩa vụ của bạn hoặc một nguồn gốc mà không kiểm toán viên nào chấp nhận.

5. **Làm thế nào chúng ta buộc mã do AI sinh ra phải tuân theo cùng tiêu chuẩn xây dựng như mã do con người viết, và chúng ta có thể phân biệt hai loại khi cần không?** Các trợ lý lập trình AI tạo ra các bản nháp hợp lý nhanh chóng, và cám dỗ là coi đầu ra của chúng là hoàn chỉnh vì nó biên dịch được và trông đúng thành ngữ. Quy tắc của chương là mã được sinh ra phải qua cùng đánh giá, kiểm thử và tiêu chuẩn như bất kỳ mã nào khác, và một đội lớn phải biến quy tắc đó thành thực tế vận hành thay vì khát vọng. Hãy mang các ví dụ về những thay đổi có AI hỗ trợ đã phát hành gần đây và hỏi liệu mỗi thay đổi có mang kiểm thử, vượt qua phân tích tĩnh, và được người gửi nó thực sự hiểu hay không, hay nó được cho qua vì tin. Áp lực đối lập là vận tốc, vì các trợ lý này thực sự năng suất và làm chậm mọi gợi ý đến mức bò sẽ vứt bỏ lợi ích. Trong bối cảnh chịu quy định và chính phủ, hãy thêm góc độ nguồn gốc và trách nhiệm giải trình, vì bạn có thể phải chứng thực ai chịu trách nhiệm cho một dòng mã và liệu một đoạn được sinh ra có mang vấn đề giấy phép hoặc bản quyền mà bạn không thể trả lời hay không.

6. **Bộ công cụ xây dựng của chúng ta có thực sự được chuẩn hóa và thực thi trong đường ống, hay cá nhân vẫn làm việc trong các thiết lập không tương thích?** Một bộ công cụ chung gồm công cụ định dạng, linter, bộ phân tích tĩnh, hệ thống dựng và trình quản lý phụ thuộc cho phép một kỹ sư di chuyển tự tin qua các dịch vụ lạ, vì mã đọc như một giọng nói và các kiểm tra giống hệt nhau ở mọi nơi. Khi nó trôi dạt, mỗi đội phát minh lại cấu hình riêng, thời gian đánh giá bị dành cho tranh cãi về phong cách, và các lỗi mà bộ phân tích của một đội lẽ ra đã bắt được lọt qua ở đội khác. Hãy mang danh sách các kho mã không chạy các kiểm tra chuẩn trên mỗi commit và hỏi vì sao mỗi cái chọn không tham gia. Căng thẳng là một thiết lập bắt buộc duy nhất có thể có cảm giác cứng nhắc với các đội có nhu cầu thực sự khác nhau, vì vậy hãy quyết định nơi sự đồng nhất đáng với ma sát và nơi một ngoại lệ có tài liệu là ổn. Với một doanh nghiệp lớn hoặc cơ quan công, hãy gắn điều này với khả năng tái tạo và kiểm toán, vì một bản dựng bạn không thể tái tạo từng byte từ một bộ công cụ được kiểm soát là bản dựng bạn không thể bảo vệ trước một người đánh giá nhiều năm sau.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ thắng, vì vậy hãy đặt một công cụ định dạng và linter chung vào ngay ngày đầu, xác thực đầu vào tại ranh giới bên ngoài duy nhất của bạn, và giữ mã nội bộ sạch sẽ thay vì phòng thủ trên mọi dòng. Bỏ qua trừu tượng suy đoán và quy trình nặng: với hai hoặc ba kỹ sư cả đội giữ cơ sở mã trong đầu, và rủi ro thực sự là độ phức tạp sống lâu hơn trí nhớ chung đó. Hãy dựa vào các thư viện đáng tin cho bất cứ thứ gì nền tảng để bạn viết càng ít mã càng tốt mà vẫn sở hữu tốt.

**Doanh nghiệp nhỏ.** Không có kỹ sư dựng riêng và ngân sách eo hẹp, hãy ưu tiên các quy ước mà công cụ hiện có của bạn thực thi miễn phí: một công cụ định dạng và linter đi kèm ngôn ngữ, mặc định hợp lý, và một bộ quy tắc nhỏ mà ai cũng nhớ được. Mua hoặc áp dụng các thư viện được bảo trì tốt thay vì xây hạ tầng mà bạn không thể bố trí nhân sự bảo trì. Hãy dành kỷ luật hạn chế của bạn cho hai điều đau nhất khi bị bỏ bê: xác thực đầu vào tại ranh giới và không bao giờ nuốt lỗi trong im lặng.

**Doanh nghiệp lớn.** Với hàng trăm kỹ sư viết vào mã dùng chung, ưu tiên là sự đồng nhất và thực thi: một bộ công cụ chuẩn nối vào đường ống, các cổng phân tích tĩnh, và quy tắc xác thực ranh giới được áp dụng ở mọi nơi để mọi người di chuyển tự tin giữa các dịch vụ. Hãy quản lý rủi ro phụ thuộc và chuỗi cung ứng như một quy trình được quản trị thay vì ứng biến theo từng đội, và dùng khẳng định để mã hóa các bất biến miền phải đúng qua mọi đội. Hãy coi tiêu chuẩn xây dựng là nền tảng giữ cho một cơ sở mã còn ở được qua nhiều thập kỷ và sự thay đổi nhân sự.

**Chính phủ.** Các hệ thống tồn tại lâu, quan trọng về công dân khiến xây dựng có kỷ luật trở thành vấn đề đảm bảo và trách nhiệm giải trình. Hãy cô lập các quy tắc biến động như luật pháp sau các giao diện ổn định để thay đổi ở lại cục bộ và truy vết được đến yêu cầu, thất bại vào các trạng thái an toàn, đã biết thay vì tiếp tục trong một trạng thái bị hỏng, và giao mỗi mô-đun kèm các bài kiểm thử đồng thời là bằng chứng kiểm toán. Nghĩa vụ mua sắm và minh bạch có nghĩa là bộ công cụ, phụ thuộc và cách xử lý lỗi của bạn phải được lập tài liệu đủ tốt để một công chức đến nhiều năm sau, hoặc một kiểm toán viên bên ngoài, có thể xác minh mã là đúng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp ba kỹ sư thiết lập một công cụ định dạng và linter chung ngay ngày đầu và chạy chúng trên mỗi commit, để cơ sở mã đọc như một giọng nói ngay cả khi họ thêm nhà thầu. Họ xác thực đầu vào tại ranh giới API và coi mọi thứ từ bên ngoài là thù địch, nhưng giữ logic nội bộ sạch thay vì nhấn chìm nó trong các kiểm tra dư thừa. Khi một webhook thanh toán bắt đầu thất bại, bản sửa nhanh vì không ngoại lệ nào từng bị nuốt trong im lặng và thông báo lỗi mang đủ ngữ cảnh để chỉ thẳng vào nguyên nhân. Toàn bộ thiết lập mất một buổi chiều và giúp họ khỏi sự tích tụ chậm chạp của độ phức tạp vốn sẽ khiến tuần đầu tiên của người được tuyển tiếp theo thật khổ sở.

**Doanh nghiệp lớn.** Một công ty thanh toán toàn cầu thực thi một bộ công cụ chung qua hàng trăm kỹ sư: định dạng và linter tự động trên mỗi commit, các cổng phân tích tĩnh trong đường ống, và quy tắc rằng mọi đầu vào bên ngoài được xác thực tại ranh giới dịch vụ. Logic miền dùng khẳng định để thực thi các bất biến như "một bút toán sổ cái luôn cân", trong khi các điều kiện lúc chạy như thẻ bị từ chối được xử lý như các kết quả tường minh, được ghi nhật ký. Vì tiêu chuẩn đồng nhất và lỗi không bao giờ bị nuốt trong im lặng, kỹ sư di chuyển tự tin qua các dịch vụ lạ, và các sự cố trên môi trường thực có thể được chẩn đoán thẳng từ nhật ký.

**Chính phủ.** Một cơ quan thuế quốc gia xây dựng một hệ thống đánh giá tồn tại lâu dự kiến chạy hàng chục năm dưới luật pháp thay đổi. Việc xây dựng cô lập từng quy tắc thuế sau một giao diện ổn định, nên các thay đổi lập pháp hằng năm ở lại cục bộ và truy vết được đến yêu cầu (chương 2.8). Xác thực phòng thủ bảo vệ mọi đầu vào hướng đến công dân. Các đường lỗi thất bại vào một trạng thái an toàn không bao giờ âm thầm đưa ra một đánh giá sai. Mỗi mô-đun được giao kèm kiểm thử đơn vị làm bằng chứng kiểm toán. Vì việc xây dựng được chuẩn hóa và có tài liệu tốt, công chức mới có thể bảo trì an toàn mã do những người tiền nhiệm đã rời đi từ lâu viết.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của xây dựng có kỷ luật là khả năng lâu dài thay đổi phần mềm một cách rẻ và an toàn, và đó là nơi phần lớn tổng chi phí sở hữu của một hệ thống được quyết định. Các nghiên cứu về kinh tế phần mềm luôn cho thấy phần lớn chi phí vòng đời của một hệ thống là bảo trì, và chi phí bảo trì bị chi phối bởi mức độ dễ hiểu và dễ thay đổi của mã. Giảm thiểu độ phức tạp, xử lý lỗi tường minh và tuân theo tiêu chuẩn trực tiếp giảm chi phí của mọi thay đổi trong tương lai và mọi sự cố trên môi trường thực.

Chi phí áp dụng khiêm tốn và chủ yếu trả trước: đặt tiêu chuẩn, nối linter và bộ phân tích, và xây dựng thói quen viết mã kiểm chứng được, phòng thủ. Mặt khác, chi phí của sự bỏ bê cộng dồn. Độ phức tạp tích tụ thành mã chậm thay đổi và rủi ro khi chạm vào. Lỗi im lặng biến thành các sự cố đắt đỏ trên môi trường thực. Phong cách không nhất quán nhân lên công sức của mọi lần đánh giá và mọi lần hội nhập. Để thuyết phục ban lãnh đạo, hãy kết nối chất lượng xây dựng với tỷ lệ thay đổi thất bại, thời gian phục hồi trung bình, tỷ lệ lỗi thoát ra và thời gian hội nhập, tất cả đều được cải thiện trực tiếp bởi kỷ luật xây dựng.

## Phản mẫu và cạm bẫy

- **Độ phức tạp len lỏi:** tích tụ mã thông minh, lồng sâu hoặc tràn lan cho đến khi không ai hiểu.
- **Nuốt lỗi trong im lặng:** khối catch rỗng và mã trả về bị bỏ qua biến thất bại thành những bí ẩn tương lai.
- **Lập trình phòng thủ quá đà:** kiểm tra dư thừa ở khắp nơi chôn vùi logic và che giấu khiếm khuyết thực.
- **Nhầm lẫn khẳng định với xử lý lỗi:** dùng khẳng định cho điều kiện lúc chạy, hoặc ngoại lệ cho bất biến của lập trình viên.
- **Xây dựng bằng sao chép-dán:** nhân đôi logic thay vì tái sử dụng, nên các bản sửa phải thực hiện ở nhiều nơi.
- **Tính tổng quát suy đoán:** xây dựng trừu tượng và khả năng cấu hình cho những nhu cầu không bao giờ đến.
- **Phớt lờ tiêu chuẩn:** mỗi kỹ sư viết mã theo cách riêng, nhân lên tải nhận thức qua cơ sở mã.
- **Xây dựng không kiểm thử:** viết mã không kèm kiểm thử, trì hoãn việc kiểm chứng sang một giai đoạn không bao giờ đến.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** Xây dựng tùy nghi và phản ứng; độ phức tạp và xử lý lỗi khác nhau theo cá nhân; ít tiêu chuẩn, và thất bại im lặng phổ biến.
- **Mức 2 (Phát triển):** Tiêu chuẩn viết mã, công cụ định dạng và linter tồn tại, và xử lý lỗi cơ bản cùng kiểm thử đơn vị được kỳ vọng, nhưng thực hành không nhất quán và mỗi đội áp dụng khác nhau.
- **Mức 3 (Chuẩn hóa):** Giảm thiểu độ phức tạp, xác thực ranh giới, xử lý lỗi tường minh và khả năng kiểm thử được lập thành tài liệu và thực thi toàn tổ chức, trong đường ống và trong đánh giá, để toàn bộ cơ sở mã đọc như thể một tác giả cẩn thận đã viết nó.
- **Mức 4 (Quản lý):** Chất lượng xây dựng được đo theo các đường cơ sở; đội theo dõi độ phức tạp chu trình, tỷ lệ lỗi thoát ra, tỷ lệ thay đổi thất bại, độ bao phủ kiểm thử đường lỗi và các phát hiện đánh giá mã, và hành động dựa trên xu hướng thay vì ý kiến.
- **Mức 5 (Điều phối):** Xây dựng được cải tiến liên tục và tích hợp trong toàn tổ chức; các mẫu phòng thủ, tiêu chuẩn và chỉ số phản hồi vào tái cấu trúc và công cụ; công cụ có AI hỗ trợ chạy dưới cùng các cổng chất lượng, và thực hành thích ứng khi ngôn ngữ, quy định và rủi ro thay đổi.

## Ý tưởng để thảo luận

- Độ phức tạp ngẫu nhiên tích tụ nhiều nhất ở đâu trong cơ sở mã của bạn, và những thói quen xây dựng nào tạo ra nó?
- Quy tắc thực tế của đội bạn về nơi xác thực đầu vào và nơi tin tưởng là gì?
- Kỹ sư của bạn có phân biệt khẳng định với xử lý lỗi không, và sự phân biệt đó có nhất quán không?
- Bao nhiêu chất lượng của bạn được xây vào trong quá trình xây dựng so với bị bắt sau trong đánh giá hay kiểm thử?
- Làm thế nào bạn quyết định khi nào tái sử dụng thư viện so với tự xây, xét rủi ro chuỗi cung ứng?
- Mã do AI sinh ra nên được giữ theo cùng tiêu chuẩn xây dựng như mã do con người viết như thế nào?

## Những điểm cần ghi nhớ

- Xây dựng là nơi thiết kế trở thành mã bảo trì được; giảm thiểu độ phức tạp là kỷ luật trung tâm của nó.
- Xây dựng cho thay đổi và cho kiểm chứng: mã kiểm thử được, thay đổi được là mã dễ hiểu.
- Phòng thủ tại các ranh giới tin cậy, tin tưởng bên trong chúng, và không bao giờ nuốt lỗi trong im lặng.
- Dùng khẳng định cho bất biến và xử lý lỗi cho các điều kiện lúc chạy được dự kiến; đừng nhầm lẫn chúng.
- Chuẩn hóa công cụ và phong cách, tái sử dụng có chủ đích, và xây chất lượng vào thay vì kiểm tra sau đó.

## Tài liệu tham khảo và đọc thêm

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, lĩnh vực kiến thức Xây dựng Phần mềm
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt và David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
