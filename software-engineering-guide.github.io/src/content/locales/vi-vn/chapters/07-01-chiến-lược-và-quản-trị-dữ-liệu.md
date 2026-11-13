# 7.1 Chiến lược và quản trị dữ liệu

## Tổng quan và động lực

Chiến lược dữ liệu là kế hoạch có chủ đích của bạn để coi dữ liệu là tài sản: nó được tạo ra, mô tả, sở hữu, bảo vệ, chia sẻ và tiêu thụ thế nào để tạo giá trị. [Quản trị dữ liệu](https://en.wikipedia.org/wiki/Data_governance) là hệ điều hành làm chiến lược thành hiện thực: các vai trò, chính sách, tiêu chuẩn và kiểm soát giữ dữ liệu đáng tin và tuân thủ theo thời gian. Trong các đội nhỏ, những mối quan tâm này thường ngầm, nằm trong đầu của vài kỹ sư. Ở quy mô của các tổ chức phát triển lớn, doanh nghiệp và cơ quan chính phủ, sự không chính thức đó sụp đổ. Hàng trăm đội tạo ra hàng nghìn bảng. Hàng chục hệ thống tuyên bố giữ bản ghi khách hàng "thật." Và không ai có thể nói chắc con số nào đúng trong một bộ slide hội đồng quản trị hay một báo cáo công khai.

Với các đội lớn, chi phí của quản trị dữ liệu kém không trừu tượng. Cơ quan quản lý kỳ vọng dòng gốc và kiểm soát chứng minh được đối với dữ liệu cá nhân, tài chính và y tế theo các chế độ như [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (Quy định Bảo vệ Dữ liệu Chung của EU), [HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) (Đạo luật Trách nhiệm giải trình và Khả năng chuyển đổi Bảo hiểm Y tế của Hoa Kỳ), và các quy tắc theo ngành. Doanh nghiệp đối mặt phơi nhiễm tài chính trực tiếp từ các chỉ số báo cáo sai, kiểm toán thất bại và nền tảng dữ liệu trùng lặp. Các cơ quan chính phủ gánh thêm nghĩa vụ về lưu giữ hồ sơ, quyền tiếp cận thông tin, trách nhiệm giải trình công và đối xử công bằng với công dân. Trong mọi bối cảnh này, dữ liệu bạn không tin được còn tệ hơn không có dữ liệu, vì nó thúc đẩy các quyết định tự tin nhưng sai.

Ý tưởng thúc đẩy tiến bộ ở quy mô lớn rất đơn giản: coi dữ liệu là một sản phẩm. Thay vì dữ liệu là sản phẩm phụ thải ra của ứng dụng, mỗi tập dữ liệu quan trọng có một chủ sở hữu, một giao diện có tài liệu, bảo đảm chất lượng, và những người tiêu dùng được đối xử như khách hàng. Chương này bao quát tư duy sản phẩm đó cùng các kỷ luật quản trị cổ điển: quản lý viên, lập danh mục, [quản lý dữ liệu chủ](https://en.wikipedia.org/wiki/Master_data_management) và chất lượng. Nó cũng bao quát các lựa chọn tổ chức quyết định mô hình nào phù hợp với đội bạn: một [lưới dữ liệu](https://en.wikipedia.org/wiki/Data_mesh) (dữ liệu phi tập trung, do miền sở hữu, được xuất bản như sản phẩm), một kho dữ liệu kiểu lakehouse (quản lý và quản trị kiểu kho đặt lên một [hồ dữ liệu](https://en.wikipedia.org/wiki/Data_lake) linh hoạt), và một [kho dữ liệu](https://en.wikipedia.org/wiki/Data_warehouse) (một kho trung tâm được quản trị gồm dữ liệu đã mô hình hóa, sẵn sàng truy vấn).

*Xem thêm:* chương 4.5 (quyền riêng tư và bảo vệ dữ liệu), chương 7.2 (kỹ thuật dữ liệu), và chương 4.6 (tuân thủ và quản trị).

## Các nguyên tắc chính

- Dữ liệu là tài sản bền vững có chủ sở hữu, không phải sản phẩm phụ dùng một lần của ứng dụng.
- Mỗi tập dữ liệu quan trọng có một chủ sở hữu chịu trách nhiệm có tên và một hợp đồng có tài liệu.
- Quản trị cho phép sử dụng đáng tin; nó không phải một cổng quan liêu chỉ biết nói không.
- Nên có một nguồn có thẩm quyền duy nhất cho mỗi thực thể kinh doanh trọng yếu.
- Chất lượng, quyền riêng tư và dòng gốc được thiết kế vào, không phải kiểm tra vào sau.
- Người tiêu dùng dữ liệu là khách hàng có nhu cầu định hình sản phẩm.
- Chính sách được mã hóa và thực thi tự động bất cứ nơi nào có thể, không để lại cho thiện chí.
- Quyền sở hữu liên bang mở rộng tốt hơn một đội trung tâm duy nhất khi tổ chức lớn lên.

## Khuyến nghị

### Coi dữ liệu là sản phẩm

Hãy giao cho mỗi tập dữ liệu quan trọng một chủ sản phẩm chịu trách nhiệm về mức độ phù hợp sử dụng của nó. Một sản phẩm dữ liệu có tên, lược đồ có tài liệu, mô tả ý nghĩa và nguồn gốc, nhịp làm mới xác định, và kỳ vọng chất lượng được công bố. Người tiêu dùng của bạn nên khám phá, hiểu và dựa vào nó mà không phải hỏi đội tạo ra nó một câu nào. Hãy áp dụng cùng kỷ luật bạn áp dụng cho API phần mềm: đánh phiên bản, thông báo ngừng hỗ trợ, nhật ký thay đổi và tương thích ngược.

### Thiết lập hợp đồng dữ liệu và SLA

Một hợp đồng dữ liệu là một thỏa thuận tường minh, kiểm tra được bằng máy giữa nhà sản xuất và người tiêu dùng. Nó bao quát lược đồ, ngữ nghĩa, độ mới, khối lượng và các thay đổi được phép. Hãy thực thi hợp đồng trong đường ống để một thay đổi phá vỡ thượng nguồn thất bại nhanh tại nguồn, thay vì lặng lẽ làm hỏng các báo cáo hạ nguồn nhiều tuần sau. Ghép hợp đồng với thỏa thuận và mục tiêu mức dịch vụ. Ví dụ, "chiều khách hàng được làm mới trước 06:00 hằng ngày, 99,5% số ngày, với dưới 0,1% khóa kinh doanh null." Hãy công bố những điều này, và cảnh báo khi vi phạm.

### Xây dựng quản lý viên và mô hình vận hành quản trị

Hãy giữ trách nhiệm giải trình tách khỏi thực thi. Chủ sở hữu dữ liệu (thường là lãnh đạo kinh doanh) chịu trách nhiệm về một miền. Quản lý viên dữ liệu (chuyên gia chủ đề) duy trì định nghĩa, giải quyết vấn đề chất lượng và phê duyệt truy cập. Một hội đồng quản trị dữ liệu nhẹ đặt tiêu chuẩn xuyên suốt và giải quyết tranh chấp. Giữ mô hình liên bang: một đội hỗ trợ trung tâm cung cấp công cụ, tiêu chuẩn và huấn luyện, trong khi các đội miền sở hữu dữ liệu của mình. Điều này tránh cả nút thắt của tập trung hoàn toàn lẫn hỗn loạn của không có quản trị.

### Đầu tư vào danh mục dữ liệu và dòng gốc

Một danh mục tìm kiếm được là cửa trước đến hệ sinh thái dữ liệu của bạn. Nó nên chứa bảng thuật ngữ kinh doanh, lược đồ kỹ thuật, quyền sở hữu, phân loại độ nhạy cảm, điểm chất lượng, và dòng gốc đầu-đến-cuối từ hệ thống nguồn qua các phép biến đổi đến bảng điều khiển. Hãy tự động hóa việc thu hoạch siêu dữ liệu thay vì dựa vào tài liệu thủ công, vốn mục rữa nhanh. Dòng gốc là thiết yếu cho phân tích tác động, ứng phó sự cố, kiểm toán và các yêu cầu quy định như truy cập và xóa của chủ thể dữ liệu.

### Quản lý dữ liệu chủ và một nguồn sự thật duy nhất

Với các thực thể cốt lõi (khách hàng, công dân, sản phẩm, nhà cung cấp, nhân viên), hãy dùng quản lý dữ liệu chủ để đối chiếu các bản ghi trùng và xung đột thành một bản ghi vàng. Hãy chọn một kiến trúc (sổ đăng ký, hợp nhất, cùng tồn tại, hay tập trung) dựa trên mức độ có thẩm quyền mà trung tâm cần có. Xác định tường minh các quy tắc đối sánh và quyền sống sót, và làm chúng kiểm toán được. Một [nguồn sự thật duy nhất](https://en.wikipedia.org/wiki/Single_source_of_truth) ngăn thất bại kinh điển khi tài chính, bán hàng và vận hành mỗi bên báo cáo doanh thu khác nhau.

### Đo chất lượng dữ liệu qua các chiều

Hãy quản lý chất lượng theo các chiều có tên: độ chính xác, độ đầy đủ, tính nhất quán, tính kịp thời, tính hợp lệ và tính duy nhất. Gắn công cụ đo cho đường ống bằng kiểm thử tự động và khả năng quan sát dữ liệu liên tục (kiểm tra độ mới, khối lượng, trôi lược đồ và phân phối), để bạn bắt các bất thường trước khi người tiêu dùng bị ảnh hưởng. Hãy coi sự cố dữ liệu như sự cố sản xuất, với phát hiện, phân loại, phân tích nguyên nhân gốc và rút kinh nghiệm.

### Phân loại, bảo vệ và kiểm soát truy cập

Hãy phân loại dữ liệu theo độ nhạy cảm, và áp dụng kiểm soát tương xứng: mã hóa, che giấu, mã thông báo hóa, bảo mật cấp hàng và cột, và truy cập quyền tối thiểu được rà soát thường xuyên. Giữ một lịch lưu giữ và xóa thỏa mãn cả yêu cầu tối thiểu hóa lẫn luật lưu giữ hồ sơ. Trong bối cảnh chính phủ, hãy dung hòa có chủ đích nghĩa vụ minh bạch với bảo vệ quyền riêng tư, thay vì từng trường hợp một.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Đội quản trị tập trung | Tiêu chuẩn nhất quán, trách nhiệm rõ | Nút thắt, tách rời khỏi các miền | Tổ chức nhỏ hoặc chịu quy định chặt |
| Quản trị liên bang | Mở rộng được, chuyên môn miền, quyền sở hữu | Cần công cụ và văn hóa mạnh | Doanh nghiệp lớn đa miền |
| Kho dữ liệu | Trưởng thành, được quản trị, SQL hiệu năng | Cứng nhắc, tốn kém cho dữ liệu phi cấu trúc | Khối lượng công việc nặng BI ổn định |
| Lakehouse | Linh hoạt, thống nhất, xử lý mọi kiểu dữ liệu | Công cụ còn non, công sức quản trị | Phân tích hỗn hợp và ML |
| Lưới dữ liệu | Quyền sở hữu miền, mở rộng theo tổ chức | Ngưỡng trưởng thành cao, chi phí phối hợp | Tổ chức rất lớn, phi tập trung |

Quản trị luôn đánh đổi tốc độ lấy niềm tin. Quản trị nhẹ cho các đội đi nhanh, cho đến khi một cuộc kiểm toán, vụ vi phạm hay báo cáo sai gây xấu hổ buộc một cuộc thanh toán tốn kém. Quản trị nặng bảo vệ niềm tin nhưng có thể bóp nghẹt thí nghiệm và đẩy các đội về hệ thống bóng. Câu trả lời bền vững là mã hóa quản trị thành lan can tự phục vụ, tự động, để con đường tuân thủ cũng là con đường dễ. Về kiến trúc, kho ưu tiên sự đơn giản được quản trị, lưới ưu tiên quy mô tổ chức, và lakehouse chia đôi. Lựa chọn đúng theo cấu trúc tổ chức của bạn nhiều hơn bất kỳ chuẩn kỹ thuật nào.

## Câu hỏi để thảo luận với đội của bạn

1. **Kiến trúc dữ liệu nào (kho, lakehouse hay lưới) thực sự khớp với cách tổ chức của bạn được cấu trúc, và bạn có trung thực về ngưỡng trưởng thành mỗi cái đòi hỏi không?** Bảng đánh đổi nêu rõ lựa chọn này theo cấu trúc tổ chức, không theo chuẩn kỹ thuật: kho thưởng cho khối lượng công việc nặng BI ổn định, lakehouse xử lý phân tích và ML hỗn hợp, và lưới mở rộng qua nhiều miền tự chủ nhưng đòi hỏi trưởng thành cao và công cụ mạnh. Với một doanh nghiệp lớn hay cơ quan chính phủ có hàng chục miền, nhảy sang lưới trước khi có nền tảng tự phục vụ và văn hóa quản trị tạo ra hỗn loạn khoác áo phi tập trung. Hãy mang tín hiệu cụ thể: bao nhiêu miền tạo dữ liệu, liệu các đội trung tâm đã là nút thắt, và liệu các đội miền có kỹ năng và động lực để sở hữu sản phẩm. Nếu hôm nay bạn thiếu công cụ liên bang, câu trả lời trung thực có thể là một kho hay lakehouse được quản trị bây giờ và một lưới về sau. Hãy chọn mô hình người của bạn thực sự vận hành được, rồi đầu tư vào mức trưởng thành mô hình kế tiếp cần.

2. **Hôm nay bạn có thể đáp ứng một yêu cầu xóa đầu-đến-cuối không, và dòng gốc của bạn có chứng minh mọi bản sao của một bản ghi cá nhân đã đi đâu không?** Theo GDPR và các chế độ tương tự, một yêu cầu xóa hay truy cập của chủ thể dữ liệu là nghĩa vụ pháp lý với thời hạn cứng, và sao chép dữ liệu rộng rãi mà không có dòng gốc khiến không thể đáp ứng. Các đội lớn thường xuyên rải dữ liệu vào các kho dữ liệu con, trích xuất, bộ nhớ đệm và bảng tính, nên câu hỏi thực là bạn có truy vết và với tới mọi bản sao không, không phải bạn có xóa được bản gốc không. Hãy mang bằng chứng: chọn một khách hàng hay công dân thật và thử liệt kê mọi nơi dữ liệu của họ sống. Nếu không được, khoảng trống đó vừa là rủi ro tuân thủ vừa là vấn đề bán kính ảnh hưởng của vi phạm. Câu trả lời nên thúc đẩy đầu tư vào dòng gốc tự động và kiểm soát chặt hơn đối với sao chép không kiểm soát, vì con đường tuân thủ phải được xây trước khi yêu cầu đến.

3. **Quản trị của bạn là con đường dễ hay một cổng người ta đi vòng, và các hệ thống bóng chứng minh điều đó ở đâu?** Câu trả lời bền vững của chương là mã hóa quản trị thành lan can tự phục vụ, tự động để con đường tuân thủ cũng là con đường nhanh nhất, vì quản trị thủ công nặng đẩy các đội về bảng tính bóng và bản sao không được quản trị. Với doanh nghiệp và cơ quan, hệ thống bóng là nơi vi phạm, con số sai và kiểm toán thất bại sinh ra, chính vì không ai theo dõi chúng. Hãy mang một bản kiểm kê cụ thể: đội nào giữ bản sao riêng, báo cáo nào bỏ qua danh mục, và nơi người ta nói quy trình chính thức quá chậm. Mỗi hệ thống bóng là một tín hiệu rằng con đường được quản trị tốn hơn cách lách. Hãy sửa ma sát thay vì ban hành thêm một chính sách, để dùng dữ liệu và hợp đồng đã được chứng nhận thực sự dễ hơn đi vòng.

4. **Thực thể kinh doanh trọng yếu nào cần nhất một nguồn có thẩm quyền duy nhất, và ai có tên chịu trách nhiệm cho bản ghi vàng của nó hôm nay?** Quản lý dữ liệu chủ tồn tại để ngăn tài chính, bán hàng và vận hành mỗi bên báo cáo một khách hàng hay một con số doanh thu khác nhau, và ở quy mô lớn việc thiếu một nguồn có thẩm quyền duy nhất biến mọi con số xuyên miền thành một cuộc tranh cãi. Các cân nhắc đối lập là trung tâm cần có thẩm quyền đến mức nào (sổ đăng ký, hợp nhất, cùng tồn tại, hay hoàn toàn tập trung) và bạn sẵn sàng xây và kiểm toán bao nhiêu logic đối sánh cùng quyền sống sót, vì một trung tâm nặng hơn tốn hơn nhưng giải quyết nhiều xung đột hơn. Hãy mang các thực thể xuất hiện trong nhiều báo cáo nhất (khách hàng, công dân, sản phẩm, nhà cung cấp, nhân viên), số hệ thống tuyên bố giữ bản ghi thật cho mỗi thực thể, và các quy tắc đối sánh bạn dùng hôm nay, nếu có. Với một ngân hàng hay cơ quan quốc gia, hãy nêu tên chủ sở hữu chịu trách nhiệm và các quy tắc quyền sống sót một cách tường minh, vì một cơ quan quản lý truy một con số từ báo cáo công khai về nguồn sẽ hỏi ai quyết định bản trùng nào thắng, và "không ai" không phải câu trả lời qua nổi kiểm toán.

5. **Làm sao bạn biết một tập dữ liệu trọng yếu phù hợp sử dụng trước khi một người tiêu dùng phát hiện nó hỏng?** Trong các hệ sinh thái chưa trưởng thành, chất lượng được tìm ra bởi nhà phân tích có bảng điều khiển hỏng hoặc giám đốc có con số hội đồng sai, là điểm phát hiện đắt nhất có thể. Căng thẳng là giữa chi phí gắn công cụ đo chất lượng (kiểm thử, kiểm tra độ mới và khối lượng, giám sát trôi phân phối và lược đồ qua các chiều có tên như độ chính xác, độ đầy đủ và tính hợp lệ) và chi phí của các sự cố bạn ngăn được, và các đội thường xuyên đầu tư thiếu vì các thất bại vô hình cho đến khi thành thảm họa. Hãy mang ba sự cố dữ liệu gần nhất, chúng được phát hiện thế nào, và chạy bao lâu trước khi ai nhận ra, cùng với SLA chất lượng bạn thực sự công bố và cảnh báo hôm nay. Với báo cáo doanh nghiệp và chính phủ, hãy gắn mỗi sản phẩm dữ liệu trọng yếu với ngưỡng chất lượng tường minh và coi một vi phạm như sự cố sản xuất với phân loại và rút kinh nghiệm, vì một con số sai trong hồ sơ quy định hay thống kê công khai mang chi phí pháp lý và danh tiếng lấn át hóa đơn giám sát.

6. **Quản trị của bạn có thực sự liên bang với quyền sở hữu miền, hay là một đội trung tâm bị buộc chịu trách nhiệm về dữ liệu mà nó không hiểu?** Chương lập luận rằng quyền sở hữu liên bang với hỗ trợ trung tâm mở rộng được nơi tập trung thuần túy thành nút thắt và phi tập trung thuần túy rơi vào hỗn loạn, vậy mà nhiều tổ chức tuyên bố liên bang trong khi một đội trung tâm nhỏ vẫn trên danh nghĩa chịu trách nhiệm về hàng nghìn bảng mà nó không có kiến thức miền. Lực kéo đối lập là có thật: đội trung tâm cho tính nhất quán và một đầu mối duy nhất, trong khi quyền sở hữu miền cho chuyên môn và trách nhiệm giải trình nhưng đòi các chủ sở hữu kinh doanh nhận trách nhiệm mà họ có thể không muốn. Hãy mang một bản đồ trung thực về ai chịu trách nhiệm so với ai thực sự duy trì định nghĩa và giải quyết vấn đề chất lượng cho các miền hàng đầu của bạn, và liệu quản lý viên có thẩm quyền và thời gian mà vai trò đòi hỏi. Trong một doanh nghiệp hay cơ quan lớn, hãy kiểm tra rằng quyền sở hữu thuộc về những người nắm cả kiến thức miền lẫn thẩm quyền nói không, vì quản trị giao cho một đội trung tâm không có thẩm quyền tạo ra chính sách không ai theo và một hội đồng không giải quyết được gì.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ và sự sống còn thắng quy trình. Hãy chọn một chủ sở hữu cho mỗi tập dữ liệu cốt lõi và biến một kho thành nguồn sự thật duy nhất cho các thực thể như "khách hàng hoạt động," và bỏ qua danh mục, hội đồng và lưới hoàn toàn. Một hợp đồng một trang cho vài bảng trọng yếu của bạn (lược đồ, thời điểm làm mới, một kỳ vọng chất lượng) kết thúc cuộc tranh cãi "con số ai đúng" trong một buổi chiều. Hãy dựa vào quản trị đã có sẵn trong kho của bạn thay vì bố trí nhân sự cho một chức năng bạn không gánh nổi.

**Doanh nghiệp nhỏ.** Không có chuyên gia dữ liệu riêng và ngân sách eo hẹp, hãy coi quản trị là vệ sinh dữ liệu hơn là dự án nền tảng: biết bạn giữ dữ liệu cá nhân nào, nó sống ở đâu, và ai được phép chạm vào. Ưu tiên một kho được quản lý hoặc công cụ BI cung cấp sẵn dòng gốc, kiểm soát truy cập và lưu giữ, để bạn mua quản trị nhúng trong công cụ đã chạy thay vì xây nó. Dành đường ống tùy chỉnh cho tập dữ liệu duy nhất thực sự thúc đẩy doanh nghiệp.

**Doanh nghiệp lớn.** Ở quy mô lớn qua nhiều đội, công việc là quyền sở hữu liên bang với hỗ trợ trung tâm: một danh mục dùng chung có dòng gốc tự động, hợp đồng dữ liệu được thực thi, dữ liệu chủ cho các thực thể cốt lõi, và SLA chất lượng được đo theo đường cơ sở. Hãy mã hóa quản trị thành lan can tự phục vụ để con đường tuân thủ cũng là con đường nhanh, và quản lý dữ liệu như một danh mục sản phẩm có chủ sở hữu có tên. Như vậy kiểm toán viên có thể truy vết bất kỳ con số nào từ báo cáo về nguồn, và các nhóm thôi phát minh lại cùng đường ống và định nghĩa.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy coi các chỉ số được công bố là sản phẩm dữ liệu với phương pháp luận có tài liệu, các bản phát hành có phiên bản và cổng chất lượng, và dung hòa có chủ đích nghĩa vụ tự do thông tin và dữ liệu mở với quyền riêng tư và tối thiểu hóa thay vì từng trường hợp. Đòi khả năng di chuyển dữ liệu và công bố dòng gốc trong hợp đồng nhà cung cấp để tránh khóa chặt, giữ một lịch lưu giữ và xóa bảo vệ được, và để một hội đồng quản lý viên giữ các định nghĩa dùng chung để "hộ gia đình" hay "thất nghiệp" có cùng nghĩa ở mọi bộ.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty SaaS giai đoạn hạt giống phát hiện bảng tính thanh toán, công cụ bán hàng và cơ sở dữ liệu sản phẩm của mình mỗi cái báo cáo số khách hàng khác nhau, và không ai nói được cái nào đúng cho bản cập nhật gửi nhà đầu tư. Đội bốn người chọn một chủ sở hữu cho mỗi tập dữ liệu cốt lõi, biến kho thành nguồn duy nhất cho "khách hàng hoạt động," và viết một hợp đồng một trang mô tả lược đồ và thời điểm làm mới hằng ngày. Việc đó tốn một buổi chiều, và nó chấm dứt cuộc tranh cãi hằng tuần về nên tin con số nào.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia hợp nhất hàng chục bản ghi khách hàng xung đột qua các bộ phận bán lẻ, cho vay và quản lý tài sản vào một trung tâm quản lý dữ liệu chủ với quy tắc quyền sống sót và một bản ghi vàng. Mỗi miền xuất bản sản phẩm dữ liệu với hợp đồng và SLA độ mới, hiển thị trong một danh mục trung tâm có dòng gốc. Thời gian báo cáo quy định giảm mạnh, vì kiểm toán viên giờ có thể truy vết bất kỳ con số nào từ báo cáo về nguồn. Ngân hàng cũng cho nghỉ hưu nhiều nền tảng báo cáo dư thừa.

**Chính phủ.** Một cơ quan thống kê quốc gia coi các chỉ số được công bố của mình là sản phẩm dữ liệu, với phương pháp luận có tài liệu, các bản phát hành có phiên bản, và cổng chất lượng nghiêm ngặt. Một hội đồng quản lý viên đối chiếu định nghĩa giữa các bộ, để "thất nghiệp" hay "hộ gia đình" có cùng nghĩa ở mọi nơi. Phân loại và truy cập có kiểm soát bảo vệ tính bảo mật của người trả lời, trong khi một danh mục công khai hỗ trợ minh bạch và nghĩa vụ tự do thông tin.

## Luận chứng kinh doanh: động lực, ROI và TCO

Động lực của quản trị dữ liệu là giảm rủi ro và tạo giá trị với tỷ lệ gần ngang nhau. Về rủi ro, chi phí tránh được gồm tiền phạt quy định, trách nhiệm vi phạm, kiểm toán thất bại, và thiệt hại danh tiếng khi công bố con số sai. Về giá trị, dữ liệu đáng tin, khám phá được tăng tốc mọi nỗ lực phân tích và học máy hạ nguồn, giảm đường ống trùng lặp, và rút ngắn thời gian từ câu hỏi đến câu trả lời.

Chi phí áp dụng là có thật: công cụ danh mục và chất lượng, thời gian của quản lý viên và chủ sở hữu, và thay đổi tổ chức để quyền sở hữu bền vững. Hãy cân nhắc TCO (tổng chi phí sở hữu) so với chi phí của việc không áp dụng, thường lớn hơn, chỉ là ẩn. Khi không được đo, chi phí đó hiện ra là nhà phân tích dành phần lớn thời gian tìm và làm sạch dữ liệu, các đội xây lại cùng đường ống, và giám đốc ra quyết định trên các con số không ai bảo vệ được. Hãy lập luận với ban lãnh đạo bằng ngôn ngữ của họ: quản trị biến dữ liệu từ một khoản nợ có rủi ro không giới hạn thành một tài sản có lợi tức cộng dồn, và nó là điều kiện tiên quyết cho AI đáng tin. Hãy bắt đầu nơi nỗi đau và phơi nhiễm quy định cao nhất, để bạn cho thấy giá trị nhanh.

## Phản mẫu và cạm bẫy

- Quản trị theo ủy ban không có tự động hóa, tạo ra chính sách không ai theo.
- Lập danh mục mọi thứ cùng lúc thay vì các tập dữ liệu thực sự quan trọng.
- Dự án dữ liệu chủ cố đun sôi đại dương và không bao giờ phát hành được bản ghi vàng.
- Coi [chất lượng dữ liệu](https://en.wikipedia.org/wiki/Data_quality) là dọn dẹp một lần thay vì khả năng quan sát liên tục.
- Quyền sở hữu giao cho một đội trung tâm thiếu kiến thức miền hoặc thẩm quyền.
- Hợp đồng được ghi trong wiki nhưng không được thực thi trong đường ống.
- Sao chép dữ liệu rộng rãi không có dòng gốc, khiến yêu cầu xóa không thể đáp ứng.
- Mua một công cụ và gọi đó là chiến lược; công cụ không có mô hình vận hành thì thất bại.

## Mô hình trưởng thành

1. Khởi đầu: Dữ liệu không có tài liệu và không có chủ sở hữu, được xử lý tùy nghi và phản ứng. Định nghĩa xung đột giữa các đội. Chất lượng được người tiêu dùng phát hiện khi báo cáo hỏng. Không có danh mục hay dòng gốc.
2. Phát triển: Thực hành cơ bản xuất hiện nhưng không nhất quán giữa các đội. Một số tập dữ liệu có chủ sở hữu và tài liệu, và một danh mục một phần tồn tại. Kiểm tra chất lượng thủ công và phản ứng. Một chính sách quản trị được viết nhưng thực thi yếu và không đồng đều.
3. Chuẩn hóa: Quyền sở hữu, hợp đồng và SLA được lập tài liệu và thực thi toàn tổ chức. Sản phẩm dữ liệu trọng yếu có chủ sở hữu có tên; một danh mục có dòng gốc tự động bao quát các miền chính; dữ liệu chủ tồn tại cho các thực thể cốt lõi; quản trị liên bang với hỗ trợ trung tâm và được áp dụng nhất quán thay vì từng đội một.
4. Quản lý: Hệ sinh thái được đo và kiểm soát theo đường cơ sở. Các chiều chất lượng (độ chính xác, độ đầy đủ, tính kịp thời, tính hợp lệ, tính duy nhất) được theo dõi theo mục tiêu SLA đã công bố; tỷ lệ vi phạm hợp đồng, độ phủ dòng gốc và danh mục, độ mới, và thời gian đáp ứng yêu cầu xóa được báo cáo trên bảng điều khiển; khả năng quan sát cảnh báo về trôi lược đồ và bất thường khối lượng; sự cố được phân loại, phân tích nguyên nhân gốc và rút kinh nghiệm; các quyết định truy cập và tiếp tục hay dừng dựa trên chỉ số so với đường cơ sở, không phải ý kiến.
5. Điều phối: Quản trị được cải thiện liên tục và tích hợp trong toàn tổ chức. Dữ liệu-như-sản-phẩm là chuẩn mực qua các miền; hợp đồng được thực thi tự động và thay đổi phá vỡ thất bại nhanh; lan can tự phục vụ mã hóa chính sách; chất lượng và dòng gốc nuôi quản lý rủi ro chủ động; định nghĩa được tin cậy toàn doanh nghiệp và hỗ trợ báo cáo chịu quy định và AI. Tổ chức thường xuyên cân bằng lại quyền sở hữu, cho nghỉ hưu nền tảng dư thừa, và điều chỉnh quản trị khi doanh nghiệp và quy định dịch chuyển.

## Ý tưởng để thảo luận

- Thực thể kinh doanh nào của bạn cấp bách nhất cần một nguồn sự thật duy nhất, và vì sao hôm nay nó bị phân mảnh?
- Hợp đồng dữ liệu được thực thi sẽ ngăn một sự cố gần đây ở đâu?
- Tổ chức của bạn được cấu trúc cho quyền sở hữu liên bang, hay tập trung sẽ phù hợp hơn ngay bây giờ?
- Làm sao bạn dung hòa nghĩa vụ minh bạch của chính phủ với quyền riêng tư và tối thiểu hóa?
- Bao nhiêu phần trăm thời gian của nhà phân tích dành cho tìm và làm sạch dữ liệu, và giảm một nửa nó đáng giá bao nhiêu?
- Ai chịu trách nhiệm, theo tên, cho tập dữ liệu quan trọng nhất của bạn, và họ có biết không?

## Những điểm cần ghi nhớ

- Coi dữ liệu là sản phẩm có chủ sở hữu, hợp đồng và SLA, không phải khí thải ứng dụng.
- Quản trị liên bang với hỗ trợ trung tâm mở rộng tốt hơn tập trung thuần túy.
- Một danh mục có dòng gốc tự động là cửa trước đến một hệ sinh thái dữ liệu đáng tin.
- Thiết lập một nguồn sự thật duy nhất cho các thực thể cốt lõi qua quản lý dữ liệu chủ.
- Quản lý chất lượng liên tục qua các chiều có tên bằng khả năng quan sát và ứng phó sự cố.
- Mã hóa quản trị thành lan can tự động để con đường tuân thủ là con đường dễ.
- Chọn kho, lakehouse hay lưới để khớp tổ chức của bạn, không phải sự cường điệu.

## Tài liệu tham khảo và đọc thêm

- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- Zhamak Dehghani, "Data Mesh: Delivering Data-Driven Value at Scale."
- Ralph Kimball và Margy Ross, "The Data Warehouse Toolkit."
- Piethein Strengholt, "Data Management at Scale."
- David Loshin, "Master Data Management."
- Chad Sanderson và các đồng nghiệp, các bài viết về hợp đồng dữ liệu.
- ISO/IEC 38505, "Governance of data."
- Loạt tiêu chuẩn ISO 8000, "Data quality."
