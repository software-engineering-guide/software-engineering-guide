# 6.7 Tác tử AI và hệ thống tác tử

## Tổng quan và động lực

Một **tác tử AI** là một [mô hình ngôn ngữ lớn](https://en.wikipedia.org/wiki/Large_language_model) (LLM) được bọc trong một vòng lặp: nó được giao một mục tiêu, nó có thể gọi công cụ, nó giữ một ít bộ nhớ về những gì đã làm, và nó tự quyết định bước kế tiếp cho đến khi đạt mục tiêu hoặc bỏ cuộc. Vòng lặp đó là toàn bộ sự khác biệt giữa một tác tử và các lệnh gọi prompt-phản hồi thuần túy của chương 6.3. Một lệnh gọi đơn trả lời một câu hỏi. Một tác tử đọc email của nó, tìm trong cơ sở dữ liệu, mở một phiếu, kiểm tra kết quả, và thử lại. Mô hình không còn chỉ tạo văn bản; nó đang chọn hành động trong hệ thống của bạn.

Sự dịch chuyển đó thay đổi bài toán kỹ thuật. Khi một mô hình chỉ viết lời, một đầu ra tồi là một câu tồi. Khi một mô hình điều khiển công cụ, một đầu ra tồi có thể gửi nhầm thông điệp, xóa một bản ghi, hoặc chuyển tiền. Vì vậy một [tác tử thông minh](https://en.wikipedia.org/wiki/Intelligent_agent) được hiểu tốt nhất là một bộ lập kế hoạch không đáng tin ngồi bên trong một hệ thống đáng tin, và phần lớn công việc của bạn dành cho việc ràng buộc những gì bộ lập kế hoạch đó được phép làm. Chương này xây trực tiếp trên nền tảng LLM của chương 6.3, các mối quan tâm về lòng tin và trách nhiệm giải trình của chương 6.5, và các thực hành nền tảng của chương 6.6.

Với các đội lớn, rủi ro mang tính tổ chức nhiều như kỹ thuật. Doanh nghiệp muốn tác tử được nối vào các hệ thống nội bộ thật (phiếu hỗ trợ, tài chính, hồ sơ khách hàng), nghĩa là tác tử thừa hưởng các kiểm soát truy cập thật và nghĩa vụ quản lý thay đổi thật. Chính phủ thêm trách nhiệm giải trình công: một hành động tự chủ ảnh hưởng đến một công dân phải giải thích được, giám sát được và kiểm toán được sau sự việc. Mẫu này mạnh. Triển khai không có kỷ luật, nó là cách nhanh để tự động hóa sai lầm.

## Các nguyên tắc chính

- Một tác tử là một mô hình cộng một vòng lặp, công cụ, bộ nhớ và một mục tiêu. Rủi ro sống trong vòng lặp, không phải trong văn xuôi.
- Ràng buộc quyền tự chủ theo nhiệm vụ. Hãy cho lượng tự do nhỏ nhất hoàn thành được công việc.
- Ưu tiên một quy trình cố định khi các bước đã biết. Chỉ với tới quyền tự chủ mở khi chúng chưa biết.
- Coi mọi công cụ là bề mặt tấn công và cấp cho nó quyền tối thiểu nó hoạt động được.
- Đặt một con người trong vòng lặp cho các hành động hệ quả hay không đảo ngược được, và làm cho việc đảo ngược rẻ.
- Đánh giá theo thành công nhiệm vụ, không theo việc bản ghi đọc nghe thế nào.
- Truy vết mọi lần chạy. Một hành động bạn không dựng lại được là hành động bạn không quản trị được.
- Thiết kế đơn giản nhất chạy được thường là đúng. Thường nó hoàn toàn không phải là một tác tử.

## Khuyến nghị

### Bắt đầu bằng một quy trình, chỉ thêm quyền tự chủ nơi bạn buộc phải

Sai lầm phổ biến nhất là với tới một tác tử tự chủ khi một đường ống cố định là đủ. Nếu bạn đã biết các bước (trích xuất trường, xác thực chúng, tra một bản ghi, soạn một phản hồi), hãy viết nó thành một quy trình được điều phối với mô hình lấp các chỗ cụ thể. Quyền tự chủ chỉ xứng đáng khi con đường thực sự không thể định trước, ví dụ nghiên cứu mở hay phân loại qua nhiều công cụ có thể. Hãy ràng buộc quyền tự chủ theo nhiệm vụ: giới hạn số bước, hạn chế bộ công cụ theo những gì mục tiêu này cần, và đặt điều kiện dừng rõ ràng. Một quy tắc tốt là cho mô hình đúng bằng lượng tự do mà bài toán đòi hỏi và không hơn một độ.

### Biến việc dùng công cụ thành năng lực cốt lõi, và làm cho nó an toàn

Dùng công cụ (còn gọi là gọi hàm) là thứ biến một mô hình thành một tác tử. Hãy định nghĩa mỗi công cụ với một lược đồ chính xác, xác thực mọi đối số mô hình cung cấp, và áp dụng [nguyên tắc quyền tối thiểu](https://en.wikipedia.org/wiki/Principle_of_least_privilege): một tác tử báo cáo chỉ-đọc nhận thông tin xác thực chỉ-đọc, không bao giờ quyền ghi mà nó có thể lạm dụng. Chạy công cụ trong một [hộp cát](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) để một lệnh gọi tồi không vươn quá bán kính ảnh hưởng của nó. Ưu tiên nhiều công cụ hẹp, đơn mục đích hơn vài công cụ rộng, vì một công cụ hẹp dễ suy luận, cấp quyền và kiểm toán hơn. Đây là cùng sự kiềm chế mà chương 6.3 thúc giục cho việc dùng công cụ của LLM, được đưa lên trung tâm.

### Dùng các mẫu suy luận và lập kế hoạch tường minh

Tác tử làm việc tốt hơn khi tư duy của chúng có cấu trúc. Trong mẫu suy luận-và-hành động (được phổ biến bởi nghiên cứu ReAct), mô hình luân phiên giữa suy luận về tình huống và thực hiện một hành động, rồi quan sát kết quả trước khi suy luận lại. Với các mục tiêu khó hơn, hãy để mô hình lập kế hoạch trước (phân rã thành nhiệm vụ con) rồi mới thực thi, để bạn kiểm tra và thậm chí phê duyệt kế hoạch trước khi bất kỳ công cụ nào chạy. Giữ các vòng lặp này quan sát được và ngắt được. Một kế hoạch bạn đọc được là một kế hoạch bạn dừng được.

### Giữ con người trong vòng lặp cho các hành động hệ quả

Hãy quyết định, theo từng công cụ và từng hành động, liệu mô hình có thể tự hành động hay phải hỏi trước. Các hành động đảo ngược được, rủi ro thấp (tìm kiếm, soạn thảo) có thể chạy không giám sát. Các hành động hệ quả hay không đảo ngược (gửi thông tin liên lạc bên ngoài, chuyển tiền, đổi dữ liệu sản xuất, quyết định hồ sơ của một công dân) cần một cổng [con người trong vòng lặp](https://en.wikipedia.org/wiki/Human-in-the-loop) với thẩm quyền thực sự để nói không. Hãy thiết kế cho khả năng đảo ngược bất cứ đâu bạn có thể: ưu tiên dàn dựng một thay đổi hơn là cam kết nó, và làm hoàn tác thành tính năng hạng nhất để một hành động nhầm tốn vài phút, không phải một sự cố.

### Coi mô hình bảo mật là đối kháng

Tác tử mở rộng bề mặt tấn công được mô tả trong chương 4.2. Mối đe dọa hàng đầu là [tiêm prompt](https://en.wikipedia.org/wiki/Prompt_injection): các chỉ dẫn độc hại ẩn trong một trang web, tài liệu hay email mà tác tử đọc và tuân theo. Liên quan chặt chẽ là [vấn đề phó thác bị nhầm lẫn](https://en.wikipedia.org/wiki/Confused_deputy_problem), nơi kẻ tấn công lừa một tác tử có đặc quyền lạm dụng quyền truy cập hợp pháp của chính nó, ví dụ rút dữ liệu qua một công cụ tác tử được phép gọi. Hãy giả định bất kỳ nội dung nào tác tử tiếp nhận có thể là thù địch. Tách chỉ dẫn đáng tin khỏi dữ liệu không đáng tin, ràng buộc công cụ để một tác tử bị chiếm quyền không với tới được hệ thống nhạy cảm, và đừng bao giờ để đầu ra thô của mô hình kích hoạt một hành động không đảo ngược được mà không xác thực.

### Đánh giá theo thành công nhiệm vụ và kiểm thử hồi quy tính không tất định

Hãy đánh giá tác tử bằng việc chúng có hoàn thành nhiệm vụ không, không phải bằng việc bản ghi nghe có thông minh không. Xây một tập đánh giá các mục tiêu đại diện với tiêu chí thành công kiểm tra được (phiếu có nhận đúng mức ưu tiên không, khoản hoàn tiền có khớp chính sách không) và chạy nó ở mỗi thay đổi prompt, mô hình hay công cụ. Vì tác tử không tất định, một lần chạy đơn chứng minh rất ít: hãy chạy mỗi ca nhiều lần và theo dõi tỷ lệ thành công, không phải đạt hay trượt. Điều này mở rộng kỷ luật đánh giá ngoại tuyến và trực tuyến của chương 6.3 và 6.2 (kỹ thuật học máy và MLOps) sang các hệ thống có đầu ra là một chuỗi hành động.

### Gắn công cụ đo cho các lần chạy để quan sát, kiểm soát chi phí và xử lý thất bại

Bạn không quản trị được thứ bạn không thấy. Hãy truy vết mọi lần chạy tác tử đầu-đến-cuối (chương 6.6): mục tiêu, từng bước suy luận, mọi lệnh gọi công cụ cùng đối số và kết quả, số token đã tiêu, và kết quả cuối. Việc truy vết này đồng thời là trình gỡ lỗi, dấu vết kiểm toán và đồng hồ đo chi phí của bạn. Hãy đặt ngân sách cứng cho số bước, thời gian và chi tiêu, vì một tác tử lặp có thể đốt độ trễ và tiền rất nhanh. Xử lý thất bại tường minh: thử lại các lỗi công cụ tạm thời với lùi bước, nhưng phát hiện vòng lặp nơi mô hình lặp lại một hành động đang thất bại, và thất bại an toàn thay vì quẫy đạp.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Tốt nhất khi |
|---|---|---|---|
| Quy trình cố định (mô hình lấp chỗ) | Khả đoán, rẻ, dễ kiểm thử và kiểm toán | Cứng nhắc; hỏng ở các đường không lường trước | Các bước đã biết từ trước |
| Tác tử tự chủ đơn | Linh hoạt; xử lý mục tiêu mở | Khó kiểm soát, đánh giá và ràng buộc hơn | Con đường không thể định trước |
| Điều phối đa tác tử | Song song; vai trò chuyên biệt | Chi phí phối hợp, lỗi cộng dồn, chi tiêu cao hơn | Một nhiệm vụ thực sự phân rã thành các phần độc lập |
| Hành động không giám sát | Nhanh, ít ma sát | Sai lầm được thực thi mà không kiểm tra | Hành động đảo ngược được và rủi ro thấp |
| Cổng con người trong vòng lặp | An toàn, trách nhiệm giải trình, đảo ngược được | Chậm hơn; cần năng lực người rà soát | Hành động hệ quả hoặc không đảo ngược được |

Căng thẳng trung tâm là quyền tự chủ so với kiểm soát. Nhiều quyền tự chủ hơn xử lý nhiều tình huống hơn nhưng đòi nhiều lan can hơn, nhiều đánh giá hơn, và nhiều tiền hơn, và nó thất bại theo những cách khó dự đoán hơn. Thiết kế đa tác tử cám dỗ các đội bằng sự thanh lịch, nhưng mỗi tác tử thêm vào làm tăng chi phí phối hợp và một chỗ nữa để lỗi nhỏ cộng dồn thành kết quả sai. Hãy giải quyết căng thẳng bằng cách bắt đầu với quyền tự chủ ít nhất giải quyết được bài toán và chỉ thêm tự do khi một nhiệm vụ cụ thể buộc bạn, luôn ghép với một lan can tương ứng.

## Câu hỏi để thảo luận với đội của bạn

1. **Tính năng này có thực sự cần một tác tử không, hay một quy trình cố định sẽ an toàn và rẻ hơn?** Quyền tự chủ quyến rũ, nhưng hầu hết công việc có các bước biết được mà một đường ống được điều phối xử lý với rủi ro thấp hơn nhiều. Với một đội lớn, mặc định dùng tác tử nghĩa là mọi nhóm gánh các gánh nặng đánh giá, truy vết và bảo mật mà một thiết kế đơn giản hơn tránh được. Hãy mang nhiệm vụ cụ thể và hỏi liệu các bước của nó có định trước được không; nếu được, một tác tử có lẽ là thiết kế quá mức. Hãy dành quyền tự chủ mở cho các mục tiêu mà con đường thực sự khác nhau theo từng ca. Câu trả lời nên đẩy hầu hết tính năng về một quy trình và để lại một tập nhỏ, có chủ đích là tác tử thật sự.

2. **Với mỗi công cụ tác tử của chúng ta có thể gọi, điều tệ nhất một tác tử bị chiếm quyền có thể làm với nó là gì, và cái gì ngăn điều đó?** Tiêm prompt và tấn công phó thác bị nhầm lẫn biến chính quyền truy cập hợp pháp của tác tử thành vũ khí chống lại bạn, nên lăng kính đúng là đối kháng (chương 4.2). Hãy kiểm kê từng công cụ, phạm vi quyền của nó, và liệu một chỉ dẫn độc hại được lén qua nội dung tiếp nhận có thể với tới nó không. Với các doanh nghiệp nối tác tử vào hệ thống nội bộ, đây là nơi quyền tối thiểu, hộp cát và cổng con người cho hành động không đảo ngược trở nên thực. Hãy mang danh sách công cụ và thông tin xác thực mỗi cái nắm giữ. Nếu bất kỳ hành động hệ quả nào với tới được mà không có xác thực hay kiểm tra của con người, đó là điều đầu tiên cần sửa.

3. **Làm sao chúng ta biết tỷ lệ thành công của một tác tử đã giảm, khi mọi lần chạy đều trông hợp lý?** Tác tử không tất định, nên một bản ghi đọc hay vẫn có thể đã thực hiện sai hành động, và một lần chạy xanh không chứng minh gì. Hãy hỏi liệu bạn có một tập đánh giá các mục tiêu với kết quả kiểm tra được, chạy nhiều lần mỗi ca để tạo ra tỷ lệ thành công thay vì một lần đạt. Với các triển khai rủi ro cao hay công khai, hãy thảo luận cách vết chạy cho phép bạn dựng lại chính xác điều đã xảy ra khi có sự cố (chương 6.5 và 6.6). Nếu tín hiệu duy nhất của bạn là phàn nàn của người dùng, bạn đã quá muộn. Câu trả lời nên tài trợ một khung đánh giá trước khi mở rộng, không phải sau một sự cố.

4. **Những hành động nào của tác tử này thực sự không đảo ngược được, ai nắm thẩm quyền phê duyệt chúng, và chúng ta có đủ năng lực người rà soát để bố trí nhân sự cho cổng đó không?** Cám dỗ là để mô hình hành động không giám sát khắp nơi, nhưng một cổng con người chỉ thật nếu có một người có tên với thẩm quyền nói không sẵn sàng khi tác tử hỏi. Với một đội lớn, một hàng đợi phê duyệt không ai sở hữu lặng lẽ thành con dấu cao su, và sự an toàn bạn đã thiết kế bốc hơi dưới khối lượng. Hãy mang danh sách đầy đủ các hành động tác tử có thể thực hiện, đánh dấu từng cái đảo ngược được hay không, và ước tính khối lượng hằng ngày của các ca độ tin cậy thấp sẽ đổ lên một người rà soát. Cân nhắc ma sát và chi phí nhân sự của một cổng so với bán kính ảnh hưởng của một sai lầm không giám sát, và ưu tiên thiết kế lại một hành động không đảo ngược thành một hành động được dàn dựng, hoàn tác được hơn là thêm một người rà soát nữa. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn mỗi hành động hệ quả với một viên chức chịu trách nhiệm và một bản ghi quản lý thay đổi, vì một hành động tự chủ ảnh hưởng đến công dân hay khách hàng mà không con người nào phê duyệt chính là thất bại một cuộc kiểm toán sẽ tìm ra.

5. **Chúng ta với tới thiết kế đa tác tử vì nhiệm vụ thực sự phân rã, hay vì nó trông thanh lịch?** Chia công việc qua các tác tử chuyên biệt quyến rũ, nhưng mỗi tác tử thêm vào làm tăng chi phí phối hợp và một chỗ nữa để lỗi nhỏ cộng dồn thành kết quả sai. Với một tổ chức lớn, chi phí không chỉ là chi tiêu và độ trễ: một hệ thống đa tác tử khó truy vết, đánh giá và suy luận hơn nhiều khi nó thất bại, nên gánh nặng quản trị nhân lên với mỗi vai trò bạn thêm. Hãy mang nhiệm vụ và chỉ ra cụ thể phần nào chạy độc lập và song song, rồi so sánh tỷ lệ thành công và chi phí đo được của phiên bản đa tác tử với một tác tử đơn trên cùng tập đánh giá. Nếu tác tử đơn thắng hoặc hòa, thiết kế thanh lịch là thiết kế quá mức. Với các triển khai chịu quy định hay công, hãy nhớ rằng mỗi tác tử trong chuỗi là một thành phần nữa mà cơ quan giám sát phải kiểm tra được, nên cấu trúc thêm bạn không biện minh được là trách nhiệm thêm.

6. **Ngân sách cứng cho số bước, thời gian và chi tiêu của một tác tử là gì, và một tác tử lặp sẽ bị bắt thế nào trước khi nó đẩy chi phí hay độ trễ lên?** Một tác tử lặp lại một hành động đang thất bại có thể đốt tiền và thời gian không báo trước, nên quyền tự chủ không giới hạn là rủi ro tài chính cũng như an toàn. Với một đội lớn chạy nhiều tác tử, một vòng lặp hành xử sai duy nhất có thể đẩy vọt hóa đơn đám mây hoặc làm cạn một giới hạn tốc độ bỏ đói mọi khối lượng công việc khác, khiến giới hạn mỗi lần chạy thành mối quan tâm vận hành chung chứ không phải vấn đề của một đội. Hãy mang ngân sách bước, thời gian và token hiện tại cho từng tác tử, cảnh báo kích hoạt khi một lần chạy vượt chúng, và việc phát hiện vòng lặp thất bại an toàn thay vì quẫy đạp. Cân nhắc ngân sách chặt, có thể cắt một nhiệm vụ khó chính đáng, so với ngân sách lỏng để chi phí chạy mất kiểm soát. Trong bối cảnh doanh nghiệp và chính phủ nơi chi tiêu phải được dự báo và biện minh, một tác tử có chi phí không giới hạn là một dòng bạn không bảo vệ được trong rà soát ngân sách hay kiểm toán.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy phát hành một tác tử hẹp chạm đến giá trị cốt lõi của bạn, trên một mô hình lưu trữ sẵn, với bộ công cụ nhỏ nhất làm được việc và trần cứng về bước và chi tiêu. Chống lại bản demo đa tác tử: sự chú ý kỹ thuật khan hiếm của bạn nên dùng để ràng buộc quyền tự chủ của một tác tử đơn và truy vết các lần chạy hơn là phối hợp các vai trò bạn không bảo trì nổi. Giữ mọi hành động hệ quả sau một cổng "soạn, không bao giờ gửi" để một sai lầm tốn một cú nhấp để hoàn tác, không phải một sự cố.

**Doanh nghiệp nhỏ.** Bạn không có ai chạy khung đánh giá hay hộp cát, vì vậy hãy ưu tiên tác tử nhúng trong các công cụ bạn đã tin, và chỉ bật quyền tự chủ bạn giám sát được bằng mắt. Coi bất kỳ tác tử nào có thể gửi, trả tiền hay xóa thay bạn là thứ giữ tắt cho đến khi một người xác nhận từng hành động, vì một thông điệp tự động sai gửi khách hàng tốn của bạn mối quan hệ. Ưu tiên nhà cung cấp cho bạn thấy tác tử đã làm gì và cho bạn tắt tự động hóa.

**Doanh nghiệp lớn.** Vấn đề là quản trị tác tử qua nhiều đội: các mẫu dùng chung để ràng buộc quyền tự chủ, thông tin xác thực công cụ quyền tối thiểu, hộp cát, cổng con người trong vòng lặp, và truy vết đầu-đến-cuối để không nhóm nào phát minh lại lan can. Hãy nối tác tử vào hệ thống nội bộ dưới cùng các kiểm soát truy cập một con người sẽ nắm, chặn cổng hành động không đảo ngược sau các người phê duyệt có tên và quản lý thay đổi, và quản lý danh mục bằng chỉ số tỷ lệ thành công, ngân sách mỗi lần chạy, và kiểm thử tiêm đối kháng. Chuẩn hóa tầng truy vết và đánh giá để hành vi của bất kỳ tác tử nào cũng dựng lại và kiểm toán được.

**Chính phủ.** Mua sắm, minh bạch và trách nhiệm giải trình công ràng buộc mọi lựa chọn. Hãy giữ tác tử ở việc thu thập sự kiện và soạn thảo, và dành mọi quyết định ảnh hưởng đến công dân cho một con người chịu trách nhiệm, vì trách nhiệm cho một quyết định khu vực công không thể ủy thác cho một mô hình. Ghi nhật ký mọi lần chạy để cơ quan giám sát thấy nguồn nào đã được tham khảo và đã làm gì, đòi nhà cung cấp tiết lộ công cụ và hạn chế của tác tử, và chứng minh bằng một tập đánh giá đối kháng rằng tác tử từ chối hành động vượt quá phạm vi có giới hạn của nó.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp phân tích năm người xây một tác tử phân loại hỗ trợ. Nó đọc một phiếu đến, tìm trong tài liệu, và hoặc soạn một phản hồi hoặc chuyển phiếu cho con người, và đó là toàn bộ bộ công cụ. Thông tin xác thực là chỉ-đọc cộng một hành động "tạo bản nháp" duy nhất không bao giờ gửi nếu không có người nhấp gửi. Mọi lần chạy được truy vết để những người sáng lập thấy vì sao một phiếu được chuyển đến nơi nó được chuyển, và một tập đánh giá hằng đêm gồm năm mươi phiếu thật chạy tác tử năm lần mỗi phiếu để theo dõi tỷ lệ chính xác định tuyến. Khi bản demo đa tác tử khéo léo của đối thủ cám dỗ họ, họ vẫn ở một tác tử vì nhiệm vụ của họ không phân rã.

**Doanh nghiệp lớn.** Một ngân hàng xây một tác tử giúp nhân viên vận hành đối soát các khoản thanh toán thất bại. Nó tích hợp với hệ thống nội bộ dưới cùng các kiểm soát truy cập mà một nhân viên văn thư con người có, được cấp qua thông tin xác thực dịch vụ quyền tối thiểu chỉ trong phạm vi đối soát. Tác tử có thể điều tra tự do (đọc sổ cái, tìm lịch sử giao dịch) nhưng bất kỳ hành động nào chuyển tiền hay sửa một bản ghi đều được dàn dựng và cần một người phê duyệt có tên, thỏa mãn quản lý thay đổi. Tài liệu tiếp nhận được coi là không đáng tin để làm cùn tiêm prompt, công cụ chạy trong hộp cát, và mọi lần chạy được truy vết đầu-đến-cuối để kiểm toán. Một tập đánh giá ngoại tuyến chặn cổng mỗi thay đổi mô hình hay prompt, và ngân sách mỗi lần chạy giới hạn bước và chi tiêu để một tác tử lặp không đẩy chi phí hay độ trễ lên.

**Chính phủ.** Một cơ quan trợ cấp thí điểm một tác tử giúp nhân viên xử lý hồ sơ tập hợp sự kiện cho một yêu cầu: lấy hồ sơ, kiểm tra quy tắc đủ điều kiện, và soạn bản tóm tắt. Cơ quan vạch một lằn ranh cứng: tác tử thu thập và soạn thảo, nhưng một nhân viên xử lý hồ sơ con người đưa ra và chịu trách nhiệm mọi quyết định ảnh hưởng đến công dân, vì trách nhiệm cho các quyết định khu vực công không thể ủy thác cho một mô hình (chương 6.5). Mỗi lần chạy được ghi nhật ký đầy đủ, cho thấy nguồn nào đã được tham khảo và cái gì đã được soạn, để cơ quan giám sát kiểm toán được bất kỳ hồ sơ nào. Quyền tự chủ được ràng buộc có chủ đích ở đọc-và-soạn, công cụ là quyền tối thiểu và trong hộp cát, và một tập đánh giá đối kháng xác nhận tác tử từ chối hành động vượt quá việc thu thập sự kiện.

## Luận chứng kinh doanh: động lực, ROI và TCO

Tác tử mang lại lợi tức bằng cách tự động hóa công việc nhiều bước vốn cần một người nhấp giữa các hệ thống: phân loại, đối soát, nghiên cứu và vận hành thường lệ. Giá trị hiện ra là công việc hoàn thành mà không cần con người ở mỗi bước, thời gian chu kỳ nhanh hơn, và nhân viên được giải phóng cho các nhiệm vụ nặng phán đoán. Vì tác tử xây trên LLM và công cụ sẵn có, thời gian đến nguyên mẫu hoạt động ngắn, chính là lý do các đội xây quá mức.

Tổng chi phí sở hữu là nơi tác tử khác với các tính năng LLM thuần túy. Ngoài chi phí suy luận, bạn trả cho các tích hợp công cụ, hạ tầng hộp cát và cấp quyền, khung đánh giá, ngăn xếp truy vết và quan sát (chương 6.6), và những người rà soát con người bố trí nhân sự cho các cổng phê duyệt. Một tác tử lặp hoặc ràng buộc kém thêm một chi phí biến đổi có thể vọt lên không báo trước, nên ngân sách về bước và chi tiêu là một phần của thiết kế, không phải chuyện nghĩ sau. Chi phí của việc không áp dụng là vận hành chậm hơn và công việc thủ công đối thủ của bạn tự động hóa. Chi phí của việc áp dụng cẩu thả là một hành động tự chủ gửi nhầm thông điệp, làm rò dữ liệu, hoặc đưa ra một quyết định không ai chịu trách nhiệm. Hãy lập luận với ban lãnh đạo bằng cách ghép một mục tiêu tự động hóa cụ thể với một kế hoạch cụ thể về lan can, đánh giá và giám sát của con người, và trung thực rằng lan can là phần lớn chi phí.

## Phản mẫu và cạm bẫy

- **Tác tử khi một quy trình là đủ.** Gánh toàn bộ rủi ro của quyền tự chủ cho một nhiệm vụ có các bước biết được.
- **Công cụ và thông tin xác thực quá rộng.** Một công cụ "làm mọi thứ" thay vì các công cụ hẹp, quyền tối thiểu.
- **Mù trước tiêm prompt.** Đưa nội dung không đáng tin cho một tác tử nắm đặc quyền thật.
- **Không có cổng con người cho hành động không đảo ngược.** Để mô hình gửi, trả tiền hay xóa mà không kiểm tra.
- **Sân khấu đa tác tử.** Chia một nhiệm vụ đơn giản qua các tác tử, trả chi phí phối hợp mà không được gì.
- **Đánh giá theo cảm tính.** Đánh giá theo việc bản ghi đọc thế nào thay vì tỷ lệ thành công nhiệm vụ.
- **Vòng lặp không giới hạn.** Không giới hạn bước, thời gian hay chi tiêu, nên một tác tử mắc kẹt đốt tiền và độ trễ.
- **Lần chạy không truy vết.** Không có bản ghi tác tử đã làm gì, khiến bạn không gỡ lỗi, kiểm toán hay giải trình được.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Tác tử được làm nguyên mẫu tùy nghi với quyền truy cập công cụ rộng và không giới hạn. Thành công được đánh giá qua demo, một cách phản ứng, sau khi có gì đó hỏng. Không có tập đánh giá, không truy vết, và không có cổng con người cho hành động hệ quả.
- **Mức 2, Phát triển:** Một số tác tử có vòng lặp giới hạn và công cụ quyền tối thiểu, và truy vết cơ bản tồn tại, nhưng thực hành khác nhau theo từng đội. Một tập đánh giá thủ công bắt các hồi quy thô ở vài dự án trong khi dự án khác không có. Phê duyệt của con người bảo vệ các hành động không đảo ngược rõ ràng nhất, nhưng độ phủ không đều và không có tài liệu.
- **Mức 3, Chuẩn hóa:** Các mẫu dùng chung chi phối quyền tự chủ, quyền công cụ, hộp cát và cổng con người trong vòng lặp, được lập tài liệu và thực thi qua mọi đội. Mọi hành động hệ quả được chặn cổng hoặc xác thực, tác tử được truy vết đầu-đến-cuối, và một tập đánh giá tự động có chấm điểm tỷ lệ thành công chạy ở mỗi thay đổi. Tiêm prompt được coi là mối đe dọa thường trực với phản ứng xác định.
- **Mức 4, Quản lý:** Danh mục tác tử được đo và kiểm soát theo đường cơ sở. Tỷ lệ thành công mỗi nhiệm vụ, tỷ lệ vượt phòng thủ tiêm prompt, chi phí và số bước mỗi lần chạy, độ trễ phê duyệt của con người, và sự cố vòng lặp hay thất bại được theo dõi như chỉ số; ngưỡng hoàn tác và khai tử được thực thi dựa trên bằng chứng đó thay vì phàn nàn. Ngân sách mỗi lần chạy về bước, thời gian và chi tiêu được giám sát, và một hồi quy ở bất kỳ chỉ số nào kích hoạt hành động trước khi mở rộng, không phải sau một sự cố.
- **Mức 5, Điều phối:** Quyền tự chủ được khớp với rủi ro nhiệm vụ bằng chính sách và được điều chỉnh liên tục khi có kết quả. Đánh giá ngoại tuyến và trực tuyến liên tục gắn hành vi tác tử với kết quả kinh doanh, và tổ chức thường xuyên cho nghỉ hưu, thu hẹp phạm vi hay cấp quyền lại cho tác tử khi bức tranh rủi ro dịch chuyển. Truy vết, ngân sách chi phí và dấu vết kiểm toán đồng nhất trên toàn danh mục; phòng thủ tiêm và phó thác bị nhầm lẫn được kiểm thử đối kháng; trách nhiệm cho hành động tự chủ rõ ràng và kiểm toán được.

## Ý tưởng để thảo luận

1. Tính năng LLM nào hiện tại của bạn đã lặng lẽ thành tác tử, và quyền tự chủ của từng cái có được ràng buộc có chủ đích không?
2. Với mỗi công cụ tác tử, cách rẻ nhất để kẻ tấn công lạm dụng nó qua nội dung được tiêm là gì, và cái gì ngăn điều đó?
3. Bạn đã chọn thiết kế đa tác tử ở đâu, và bạn có chứng minh được chi phí phối hợp đã sinh lời so với một tác tử đơn không?
4. Hành động nào của tác tử thực sự không đảo ngược được, và mọi cái có thể được thiết kế lại thành đảo ngược được hay dàn dựng được không?
5. Nếu một tác tử thực hiện một hành động có hại vào ngày mai, bạn có dựng lại chính xác nó đã làm gì và ai chịu trách nhiệm không?

## Những điểm cần ghi nhớ

- Một tác tử là một LLM trong một vòng lặp với công cụ, bộ nhớ và một mục tiêu. Rủi ro sống trong vòng lặp và công cụ, không phải văn bản.
- Ưu tiên một quy trình cố định khi các bước đã biết; dành quyền tự chủ cho các mục tiêu thực sự mở và ràng buộc nó chặt.
- Dùng công cụ là năng lực cốt lõi. Cho mỗi công cụ quyền tối thiểu, một lược đồ được xác thực và một hộp cát.
- Chặn cổng các hành động hệ quả và không đảo ngược sau một con người có thẩm quyền thực sự, và thiết kế để đảo ngược rẻ.
- Coi tác tử là đối kháng: phòng thủ chống tiêm prompt và lạm dụng phó thác bị nhầm lẫn (chương 4.2).
- Đánh giá theo tỷ lệ thành công nhiệm vụ qua nhiều lần chạy, và truy vết mọi lần chạy để gỡ lỗi, kiểm soát chi phí và kiểm toán (chương 6.5 và 6.6).
- Thường câu trả lời đúng là hoàn toàn không xây một tác tử.

## Tài liệu tham khảo và đọc thêm

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (hướng dẫn kỹ thuật về quy trình so với tác tử).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (gồm tiêm prompt và quyền tác tử quá mức).
- Simon Willison, các bài viết về tiêm prompt và "bộ ba chết người" cho tác tử AI.
- Norman Hardy, *The Confused Deputy* (phát biểu kinh điển về vấn đề phó thác bị nhầm lẫn).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell và Peter Norvig, *Artificial Intelligence: A Modern Approach* (tác tử thông minh và hành động hợp lý).
