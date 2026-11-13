# 6.1 Chiến lược và mức độ sẵn sàng AI

## Tổng quan và động lực

[Trí tuệ nhân tạo](https://en.wikipedia.org/wiki/Artificial_intelligence) đã đi từ một điều mới lạ trong nghiên cứu thành năng lực cốt lõi mà các tổ chức lớn nay được kỳ vọng triển khai có trách nhiệm và ở quy mô lớn. Với doanh nghiệp và cơ quan chính phủ, câu hỏi thực không còn là liệu AI có làm được điều gì ấn tượng trong một bản demo hay không. Mà là liệu một khoản đầu tư cụ thể có giải quyết một vấn đề thật tốt hơn các lựa chọn thay thế, có thể được vận hành an toàn trong nhiều năm, và có sống sót được qua kiểm toán, mua sắm và sự soi xét của công chúng. Chiến lược AI là kỷ luật quyết định nơi áp dụng AI, nơi tránh nó, và những nền tảng bạn cần trước khi mô hình đầu tiên đến môi trường sản xuất.

Với các đội lớn, quy mô và quán tính nâng rủi ro lên. Một sáng kiến được đặt khung tồi có thể đốt ngân sách, làm phân tâm các kỹ sư tài năng, và làm xói mòn niềm tin với cơ quan quản lý và công dân khi thất bại trước công chúng. Một sáng kiến được chọn tốt có thể tự động hóa việc nhàm chán, làm lộ hiểu biết từ dữ liệu mà trước đây bạn không thể với tới, và giải phóng những người có kỹ năng cho công việc giá trị cao hơn. Sự khác biệt hiếm khi nằm ở chính mô hình. Nó quy về việc bạn đặt khung vấn đề tốt đến đâu, dữ liệu và nhân tài của bạn sẵn sàng đến đâu, và luận chứng kinh doanh của bạn trung thực đến đâu.

Bối cảnh chính phủ và chịu quy định thêm nhiều ràng buộc hơn. Các cơ quan công phải biện minh chi tiêu, bảo đảm minh bạch, tránh phân biệt đối xử trái luật, và chịu trách nhiệm trước các quan chức dân cử và công chúng. Quy tắc mua sắm có thể cấm khóa chặt nhà cung cấp duy nhất, đòi khả năng giải thích, và yêu cầu nhà cung cấp phơi bày hành vi mô hình. Ở đây, hãy coi tuân thủ, khả năng kiểm toán và lối thoát là yêu cầu hạng nhất, không phải chuyện nghĩ sau.

## Các nguyên tắc chính

- Bắt đầu từ một vấn đề đáng giải quyết, không phải từ một công nghệ đi tìm công dụng.
- Ưu tiên cách tiếp cận đơn giản nhất đáp ứng nhu cầu; AI là một lựa chọn trong nhiều lựa chọn, và thường không phải tốt nhất.
- Coi mức độ sẵn sàng của dữ liệu, nhân tài và nền tảng là điều kiện tiên quyết, không phải các luồng công việc song song để sắp xếp sau.
- Đưa ra quyết định xây-hay-mua một cách tường minh và xem xét lại khi thị trường và năng lực của bạn thay đổi.
- Định lượng tổng chi phí sở hữu, gồm vận hành, giám sát và thay thế cuối cùng, không chỉ giấy phép hay bản thí điểm.
- Thiết kế cho lối thoát từ ngày đầu: tránh các kiến trúc khiến việc đổi nhà cung cấp hay mô hình đắt đến mức cấm đoán.
- Trong bối cảnh chịu quy định và công, hãy coi minh bạch, tuân thủ mua sắm và trách nhiệm giải trình là ràng buộc thiết kế.
- Đo chi phí của việc *không* hành động bên cạnh chi phí của việc hành động.

## Khuyến nghị

### Đặt khung vấn đề trước khi chọn công nghệ

Hãy viết một bản phát biểu vấn đề một trang. Nêu quyết định hay nhiệm vụ bạn muốn cải thiện, đường cơ sở hiện tại, kết quả đo được bạn muốn, và điều gì xảy ra khi hệ thống làm sai. Rồi hỏi liệu vấn đề có hợp với AI không. Có đủ dữ liệu liên quan không? Nhiệm vụ dựa trên mẫu hình hơn là dựa trên quy tắc không? Bạn có chấp nhận được câu trả lời xác suất không? Một con người có kiểm tra được đầu ra không? Nhiều vấn đề được giải tốt hơn bằng phần mềm tất định, thiết kế quy trình tốt hơn, hoặc đơn giản là vệ sinh dữ liệu tốt hơn. Hãy viết ra tường minh nơi AI *không* phù hợp: ví dụ, các quyết định phải giải thích được hoàn hảo theo luật, hoặc nơi chi phí của một lỗi hiếm là thảm khốc và không thể bắt được.

### Dùng cây quyết định xây-so-với-mua-so-với-tinh-chỉnh-so-với-prompt

Đi từ rẻ nhất và nhanh nhất đến đắt nhất và kiểm soát nhiều nhất:

1. **Prompt một mô hình được lưu trữ sẵn.** Nếu một mô hình đa dụng (như Claude của Anthropic, hay các sản phẩm tương đương của nhà cung cấp khác) giải được vấn đề bằng prompt cẩn thận và truy xuất, hãy làm điều đó trước. Chi phí thấp nhất, lặp nhanh nhất, không cần hạ tầng huấn luyện.
2. **Tăng cường bằng truy xuất hoặc công cụ.** Nếu khoảng trống là kiến thức hay hành động, hãy thêm [sinh tạo tăng cường truy xuất](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), lấy các tài liệu liên quan lúc truy vấn và cung cấp cho mô hình làm ngữ cảnh, và dùng công cụ trước khi chạm đến trọng số mô hình.
3. **Tinh chỉnh hoặc điều chỉnh.** Nếu prompt không thể đạt độ chính xác, giọng điệu hay định dạng cần thiết một cách nhất quán, hãy [tinh chỉnh](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) một mô hình nhỏ hơn trên dữ liệu của bạn: tức là huấn luyện thêm một mô hình đã được tiền huấn luyện trên các ví dụ của bạn để chuyên môn hóa nó. Điều này mua sự kiểm soát với cái giá là một đường ống [MLOps](https://en.wikipedia.org/wiki/MLOps) (vận hành học máy).
4. **Mua một sản phẩm chuyên biệt.** Với các lĩnh vực được xác định rõ (xử lý tài liệu, chấm điểm gian lận), một sản phẩm nhà cung cấp trưởng thành có thể thắng bất cứ thứ gì bạn xây.
5. **Xây từ đầu.** Hãy dành việc huấn luyện [mô hình nền tảng](https://en.wikipedia.org/wiki/Foundation_model) (mô hình lớn được tiền huấn luyện trên dữ liệu rộng và thích ứng được cho nhiều nhiệm vụ) cho các tổ chức có dữ liệu độc đáo, nhân tài sâu và lý do chiến lược. Với gần như mọi doanh nghiệp và cơ quan, đây là lựa chọn sai.

### Thiết lập điều kiện tiên quyết về dữ liệu, nhân tài và nền tảng

Hãy kiểm toán dữ liệu của bạn về tính sẵn có, chất lượng, gắn nhãn, dòng gốc và cơ sở pháp lý để sử dụng. Xác nhận bạn thực sự có quyền dùng nó cho AI, gồm mọi dữ liệu cá nhân hay của bên thứ ba. Hãy đánh giá nhân tài trung thực: bạn cần các nhà khoa học dữ liệu, và cả kỹ sư ML, kỹ sư dữ liệu, quản lý sản phẩm hiểu hệ thống xác suất, và người rà soát có thể đánh giá đầu ra. Trước khi mở rộng, hãy dựng một đường cơ sở nền tảng: theo dõi thí nghiệm, một sổ đăng ký mô hình (hệ thống ghi nhận các phiên bản mô hình đã huấn luyện và trạng thái phê duyệt của chúng), giám sát, và phục vụ an toàn, để mỗi trường hợp sử dụng mới không phát minh lại vận hành.

### Xử lý có chủ đích các bối cảnh chịu quy định và chính phủ

Hãy đưa các đội mua sắm, pháp lý và rủi ro vào sớm. Yêu cầu nhà cung cấp tiết lộ nguồn gốc mô hình, thực hành dữ liệu huấn luyện, kết quả đánh giá và các hạn chế đã biết. Ưu tiên các hợp đồng trao khả năng di chuyển dữ liệu và prompt của bạn, và tránh các định dạng độc quyền bẫy bạn. Khi thích hợp, hãy công bố mục đích và các biện pháp bảo vệ của hệ thống AI hướng công chúng, và cho mọi người một kênh để phản đối các quyết định tự động. Hãy căn chỉnh theo các khung đã được công nhận (xem chương 6.5) để các cuộc kiểm toán thấy một quy trình có tài liệu, bảo vệ được.

### Tính tổng chi phí sở hữu và đề phòng khóa chặt

Hãy mô hình hóa chi phí toàn vòng đời: suy luận hay cấp phép, đường ống dữ liệu, rà soát bởi con người, giám sát, huấn luyện lại, ứng phó sự cố, và ngừng hoạt động. So sánh nó với chi phí của hiện trạng và của các lựa chọn thay thế. Giảm khóa chặt bằng cách đặt mô hình sau một giao diện nội bộ, giữ prompt và tập dữ liệu đánh giá di chuyển được, và thỉnh thoảng thử một nhà cung cấp thứ hai.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm | Tốt nhất khi |
|---|---|---|---|
| Prompt mô hình được lưu trữ | Nhanh, rẻ, không cần hạ tầng, dễ chuyển | Ít kiểm soát hơn, chi phí mỗi lệnh gọi, câu hỏi chia sẻ dữ liệu | Nguyên mẫu, nhiệm vụ rộng, yêu cầu chưa chắc chắn |
| Tăng cường truy xuất | Neo câu trả lời vào dữ liệu của bạn, cập nhật được | Chất lượng truy xuất khó, thêm hạ tầng | Nhiệm vụ nặng kiến thức |
| Tinh chỉnh mô hình nhỏ hơn | Kiểm soát, chi phí mỗi lệnh gọi thấp hơn ở quy mô, tùy chọn tại chỗ | Cần MLOps, dữ liệu và bảo trì | Nhiệm vụ ổn định, khối lượng cao, chuyên biệt |
| Mua một sản phẩm | Đã kiểm chứng, được hỗ trợ, nhanh ra giá trị | Chi phí giấy phép, khóa chặt, độ vừa vặn hạn chế | Vấn đề hàng hóa được xác định rõ |
| Xây mô hình nền tảng | Kiểm soát và khác biệt hóa tối đa | Chi phí khổng lồ, nhân tài hiếm, rủi ro cao | Gần như không bao giờ, ngoài các phòng thí nghiệm biên giới |

Đánh đổi chi phối là kiểm soát so với chi phí và tốc độ. Prompt cho bạn tốc độ và linh hoạt nhiều nhất nhưng ít kiểm soát nhất; xây cho bạn kiểm soát nhiều nhất nhưng đòi nguồn lực mà ít tổ chức nên chi. Hầu hết các đội lớn nên sống ở giữa: prompt và truy xuất trước, tinh chỉnh có chọn lọc, và mua cho nhu cầu hàng hóa. Khóa chặt đánh đổi sự tiện lợi ngắn hạn lấy rủi ro dài hạn, và điều đó đặc biệt quan trọng trong chính phủ, nơi nghĩa vụ thoát nhiều năm là phổ biến.

## Câu hỏi để thảo luận với đội của bạn

1. **Mỗi trường hợp sử dụng trong ba ứng viên hàng đầu của chúng ta nằm ở đâu trên bậc thang prompt-rồi-truy-xuất-rồi-tinh-chỉnh-rồi-mua-rồi-xây, và bằng chứng nào sẽ đẩy nó lên một bậc?** Điều này quan trọng vì hầu hết chi tiêu AI lãng phí đến từ việc bắt đầu cao hơn một bậc: huấn luyện một mô hình khi prompt cẩn thận đã đủ. Với một đội lớn, thống nhất bậc thang như một mặc định chung ngăn mỗi nhóm phát minh lại một đường ống đắt tiền. Hãy mang bản phát biểu vấn đề một trang cho mỗi ứng viên, đường cơ sở hiện tại, và một cái đọc trung thực về việc khoảng trống là kiến thức (truy xuất), tính nhất quán (tinh chỉnh), hay một hàng hóa đã giải (mua). Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm chi phí mua sắm và kiểm toán của mỗi bậc, vì một mô hình tinh chỉnh kéo theo gánh nặng MLOps mà một lệnh gọi được lưu trữ không có. Câu trả lời nên cho phép bạn loại bỏ hoặc hạ cấp ít nhất một dự án quá tầm ngay trong phòng.

2. **Kế hoạch thoát cụ thể của chúng ta cho nhà cung cấp hay mô hình chúng ta phụ thuộc nhiều nhất là gì, và chúng ta đã thực sự kiểm thử nó chưa?** Khóa chặt rẻ để chấp nhận và đắt để gỡ, và trong chính phủ bạn có thể mang nghĩa vụ thoát nhiều năm mà bạn không đáp ứng được nếu chưa bao giờ diễn tập. Hãy mang danh sách các tính năng độc quyền bạn dựa vào, liệu prompt và tập dữ liệu đánh giá có di chuyển được không, và mô hình nằm sau một giao diện nội bộ thế nào (hay không). Tín hiệu cần theo dõi là liệu có ai từng chạy bộ đánh giá của bạn trên một nhà cung cấp thứ hai chưa; nếu chưa, kế hoạch thoát của bạn là một hy vọng, không phải một kế hoạch. Nếu câu trả lời trung thực là việc chuyển sẽ mất nhiều tháng và viết lại mã lõi, hãy coi đó là khiếm khuyết thiết kế cần sửa ngay, không phải cây cầu để qua sau.

3. **Một bảng điểm sẵn sàng trung thực nói gì về quyền dữ liệu của chúng ta, và hôm nay nó loại những trường hợp sử dụng nào?** Bỏ qua mức độ sẵn sàng của dữ liệu là thất bại lặng lẽ nhấn chìm các bản thí điểm: mô hình hoạt động, nhưng bạn chưa bao giờ có cơ sở pháp lý để dùng dữ liệu, hoặc nó chưa gắn nhãn và chưa có dòng gốc. Với một tổ chức lớn, dữ liệu cá nhân và của bên thứ ba đặt ra các giới hạn đồng ý và hợp đồng khác nhau theo khu vực pháp lý và theo tập dữ liệu. Hãy mang một cuộc kiểm toán về tính sẵn có, chất lượng, gắn nhãn, dòng gốc và cơ sở pháp lý cho mỗi ứng viên, và sẵn sàng đánh dấu một số trường hợp sử dụng là bị chặn cho đến khi nền tảng dữ liệu tồn tại. Trong bối cảnh chịu quy định và công, một cơ sở pháp lý không dùng được không phải một sự chậm trễ, mà là điểm dừng cứng, và việc tài trợ công việc sẵn sàng nên là một dòng tường minh trong kế hoạch thay vì chuyện nghĩ sau.

4. **Làm sao chúng ta biết một trường hợp sử dụng AI đang chạy thực sự hiệu quả, và bằng chứng nào sẽ khiến chúng ta khai tử nó?** Hầu hết danh mục AI tích lũy những xác sống: các bản thí điểm đã phát hành, gây ấn tượng với ai đó, và nay chạy mãi mà không ai kiểm tra liệu chúng còn xứng đáng chi phí. Hãy thống nhất đường cơ sở và chỉ số thành công trước khi ra mắt, rồi đặt một ngưỡng khai tử tường minh, để quyết định dừng được đưa ra trước thay vì phải biện hộ ngay lúc đó. Hãy mang chỉ số hiện tại, chi phí giám sát của con người cho mỗi kết quả, và độ trôi bạn đã thấy kể từ khi ra mắt. Với danh mục doanh nghiệp và chính phủ, hãy nêu ai rà soát từng hệ thống theo nhịp cố định và ai nắm thẩm quyền cho nó nghỉ hưu; một trường hợp sử dụng không ai chịu trách nhiệm rà soát là cái không ai bao giờ tắt.

5. **Con người ở lại trong vòng lặp ở đâu, sự giám sát đó tốn bao nhiêu, và chúng ta đã thực sự lập ngân sách cho nó chưa?** Những trường hợp sử dụng AI trông rẻ nhất là những cái lặng lẽ giả định tự động hóa hoàn toàn, rồi rò chi phí qua việc rà soát, sửa chữa và leo thang mà thực tế buộc quay lại. Hãy quyết định có chủ đích quyết định nào một người phải xác nhận, cái nào mô hình có thể tự đưa ra, và cái nào nó không bao giờ được đưa ra, rồi định giá thời gian con người mà điều đó hàm ý. Hãy mang khối lượng các ca độ tin cậy thấp, chi phí của một câu trả lời sai, và đường leo thang hiện tại. Trong bối cảnh chịu quy định và công, hãy gắn mỗi quyết định tự động với một viên chức chịu trách nhiệm và một đường khiếu nại, vì sự giám sát bạn không mô tả được là sự giám sát bạn không có.

6. **Chúng ta có nhân tài và nền tảng để vận hành điều chúng ta đề xuất không, hay đang lặng lẽ giả định năng lực mà mình thiếu?** Các kế hoạch AI tham vọng thất bại ít ở mô hình hơn ở những nền móng không hào nhoáng: không ai bảo trì đường ống, không ai đánh giá được đầu ra, không có nền tảng để triển khai. Hãy khớp mỗi trường hợp sử dụng ứng viên với kỹ năng và hạ tầng nó thực sự cần, và trung thực nơi khoảng trống là một lần tuyển dụng, một đối tác, hay một lý do để không xây. Hãy mang bản kiểm kê ai có thể sở hữu từng hệ thống trong môi trường sản xuất, nó sẽ chạy trên nền tảng nào, và những năng lực nào bạn phải mua. Với một tổ chức lớn hay công, hãy thêm thời gian chờ mua sắm và tuyển dụng, vì một kế hoạch phụ thuộc nhân tài bạn không tuyển được trong khung thời gian liên quan là kế hoạch giao hàng thiếu.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ và sự sống còn chi phối. Hãy chọn một trường hợp sử dụng hẹp chạm đến giá trị cốt lõi của bạn, phát hành nó trên một mô hình được lưu trữ sau một giao diện mỏng, và giới hạn chi tiêu chặt. Tránh xây hạ tầng hay huấn luyện mô hình: nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư, và một đường ống tinh chỉnh bạn không bảo trì nổi là gánh nặng, không phải hào bảo vệ. Giữ việc chuyển đổi rẻ để bạn theo kịp một thị trường biến động nhanh.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có nhà khoa học dữ liệu và ngân sách eo hẹp, vì vậy hãy coi AI là thứ bạn mua tích hợp trong các công cụ đã dùng, không phải một chương trình bạn bố trí nhân sự. Hãy đóng khung mức độ sẵn sàng như câu hỏi về vệ sinh dữ liệu và quyền riêng tư hơn là một dự án học máy: biết bạn giữ dữ liệu khách hàng nào, bạn được phép làm gì với nó, và nơi một câu trả lời tự động sai sẽ làm bạn mất một khách hàng. Ưu tiên nhà cung cấp biến AI thành tùy chọn, minh bạch và dễ tắt.

**Doanh nghiệp lớn.** Vấn đề là quản trị danh mục qua nhiều đội: một bậc thang xây-so-với-mua dùng chung, đánh giá sẵn sàng nhất quán, và phân tích khóa chặt cùng tổng chi phí để các nhóm thôi phát minh lại những đường ống đắt tiền. Hãy lập ngân sách tường minh cho gánh nặng MLOps và giám sát của con người, chuẩn hóa tầng giao diện để nhà cung cấp thay thế được, và quản lý các trường hợp sử dụng AI như một danh mục với chỉ số rõ ràng và tiêu chí khai tử thay vì một mớ bản thí điểm rải rác.

**Chính phủ.** Minh bạch, quy tắc mua sắm và trách nhiệm giải trình định hình mọi lựa chọn. Hãy ưu tiên các hệ thống trích dẫn nguồn chính thức thay vì sinh ra chính sách, giữ một con người chịu trách nhiệm cho các quyết định hệ quả, và đòi khả năng di chuyển dữ liệu cùng việc tiết lộ hạn chế mô hình trong hợp đồng. Hãy công bố mô tả bằng ngôn ngữ đơn giản và một đường khiếu nại, tôn trọng mọi nghĩa vụ thoát nhiều năm bạn ký, và giữ AI ngoài các quyết định đánh giá cuối cùng vốn phải thuộc về một viên chức chịu trách nhiệm.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp lập lịch năm người muốn thêm tính năng ngôn ngữ tự nhiên "đặt cho tôi một cuộc họp" mà không kéo hai kỹ sư khỏi sản phẩm lõi. Họ chọn vấn đề nhỏ nhất vẫn quan trọng, phân tích một yêu cầu thành một thời điểm đề xuất, và phát hành nó với một mô hình được lưu trữ sau một API nội bộ mỏng để có thể đổi nhà cung cấp về sau. Đội đặt trần chi tiêu hằng tháng cứng, theo dõi liệu người dùng có chấp nhận các thời điểm gợi ý, và thống nhất chỉ xem xét lại một mô hình tinh chỉnh nếu khối lượng bao giờ biện minh cho công sức thêm.

**Doanh nghiệp lớn.** Một công ty bảo hiểm đa quốc gia muốn tăng tốc phân loại yêu cầu bồi thường. Thay vì huấn luyện một mô hình đặt riêng, họ đóng khung vấn đề hẹp (định tuyến và tóm tắt các yêu cầu đến), làm nguyên mẫu với một mô hình được lưu trữ cộng truy xuất trên tài liệu chính sách của mình, và đo so với thời gian xử lý và độ chính xác của con người. Chỉ sau khi chứng minh giá trị, họ mới tinh chỉnh một mô hình nhỏ hơn cho loại yêu cầu khối lượng cao nhất để cắt chi phí mỗi lệnh gọi. Họ giữ mô hình sau một API nội bộ để có thể đổi nhà cung cấp, và mô hình hóa một TCO ba năm gồm rà soát bởi con người các ca độ tin cậy thấp.

**Chính phủ.** Một cơ quan thuế quốc gia cân nhắc một trợ lý AI giúp nhân viên trả lời thắc mắc của công dân. Vì các câu trả lời đó chạm đến nghĩa vụ pháp lý, cơ quan nhất quyết đòi minh bạch: hệ thống chỉ được đưa ra hướng dẫn chính thức kèm trích dẫn, không bao giờ bịa chính sách, và một con người rà soát mọi gợi ý tự động trước khi gửi đi. Mua sắm yêu cầu nhà cung cấp tiết lộ hạn chế mô hình và trao khả năng di chuyển dữ liệu, và cơ quan công bố một mô tả bằng ngôn ngữ đơn giản về hệ thống cùng một đường khiếu nại. Họ giữ AI hoàn toàn ngoài các quyết định đánh giá cuối cùng, dành chúng cho các viên chức chịu trách nhiệm.

## Luận chứng kinh doanh: động lực, ROI và TCO

Chiến lược AI tồn tại để giúp bạn tránh hai thất bại đối xứng: đầu tư quá mức vào AI không bao giờ sinh lời, và đầu tư thiếu trong khi đối thủ hay cơ quan đồng cấp vượt lên. ROI đến từ lao động tiết kiệm, thời gian chu kỳ giảm, tỷ lệ lỗi hạ thấp, và năng lực mới được mở ra. Hãy đo những điều này so với một đường cơ sở chân thực, và chiết khấu cho chi phí thực của giám sát bởi con người, thứ hiếm khi biến mất.

TCO phải bao gồm các dòng chi phí không hào nhoáng: đường ống dữ liệu, giám sát, huấn luyện lại khi thế giới trôi, rà soát bảo mật, và ngừng hoạt động cuối cùng. Một bản thí điểm trông rẻ có thể thành đắt khi chạy ở quy mô trong nhiều năm. Hãy trình bày cả chi phí của việc *không* áp dụng: dịch vụ chậm hơn, chi phí thủ công cao hơn, và trôi chiến lược. Hãy lập luận với ban lãnh đạo bằng góc nhìn danh mục: vài canh bạc tin cậy cao, chỉ số thành công rõ ràng, tiêu chí khai tử cho thất bại, và một đánh giá sẵn sàng cho thấy nền tảng dữ liệu và nhân tài tồn tại. Hãy yêu cầu lãnh đạo tài trợ mức độ sẵn sàng một cách tường minh; bỏ qua nó và bạn bảo đảm làm lại tốn kém.

## Phản mẫu và cạm bẫy

- **Giải pháp đi tìm vấn đề.** Mua AI vì đối thủ làm vậy, rồi đi săn một trường hợp sử dụng.
- **Bỏ qua mức độ sẵn sàng của dữ liệu.** Ra mắt mô hình trên dữ liệu không có sẵn, chưa gắn nhãn, hoặc không dùng được về mặt pháp lý.
- **Quyết định theo demo.** Cam kết dựa trên một bản demo bóng bẩy mà không có đánh giá chất lượng môi trường sản xuất.
- **Phớt lờ vòng lặp con người.** Giả định tự động hóa hoàn toàn và lập ngân sách thiếu cho việc rà soát, là nơi phần lớn chi phí ẩn nấp.
- **Khóa chặt thầm lặng.** Xây sâu trên các tính năng độc quyền của một nhà cung cấp mà không có kế hoạch thoát.
- **Đánh giá thấp vận hành.** Coi triển khai là vạch đích thay vì khởi đầu của nghĩa vụ bảo trì.
- **Tuân thủ như chuyện nghĩ sau.** Vá minh bạch và khả năng kiểm toán sau khi thiết kế, với chi phí gấp nhiều lần.

## Mô hình trưởng thành

1. **Khởi đầu.** Thí nghiệm tùy nghi, không có chiến lược chung, quyết định do cường điệu và sự nhiệt tình cá nhân thúc đẩy.
2. **Phát triển.** Việc đặt khung vấn đề tồn tại cho một số dự án; đường cơ sở nền tảng đầu tiên xuất hiện; xây-so-với-mua được thảo luận nhưng không nhất quán.
3. **Chuẩn hóa.** Một danh mục các trường hợp sử dụng AI với chỉ số rõ ràng, một cây quyết định có tài liệu, đánh giá sẵn sàng, và phân tích khóa chặt cùng TCO, được áp dụng nhất quán qua các đội.
4. **Quản lý.** Danh mục được đo: mức độ sẵn sàng, ROI, TCO và chi phí giám sát của con người được theo dõi theo đường cơ sở; tiêu chí khai tử được thực thi dựa trên bằng chứng; tác động đến phân phối và chất lượng thúc đẩy mỗi quyết định tiếp tục hay dừng.
5. **Điều phối.** Chiến lược AI được tích hợp với hoạch định kinh doanh và rủi ro; mức độ sẵn sàng được duy trì liên tục; tổ chức thường xuyên cho nghỉ hưu, thay thế và thu hẹp phạm vi các hệ thống AI dựa trên bằng chứng, cân bằng lại danh mục khi thị trường và bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

- Làm sao bạn quyết định khi nào một vấn đề thực sự không phù hợp với AI, và ai có thẩm quyền nói không?
- Ngưỡng sẵn sàng nào nên chặn cổng một dự án từ thí điểm sang môi trường sản xuất?
- Bao nhiêu khóa chặt là chấp nhận được để đổi lấy thời gian ra giá trị nhanh hơn?
- Trong chính phủ, nghĩa vụ minh bạch nên định hình lựa chọn xây-hay-mua thế nào?
- Làm sao bạn giữ các ước tính TCO trung thực khi nhà cung cấp và người nhiệt tình có động cơ đánh giá thấp chúng?
- Ai sở hữu danh mục AI, và các quyết định khai tử được đưa ra thế nào?

## Những điểm cần ghi nhớ

- Chiến lược bắt đầu với một vấn đề thật và một đường cơ sở trung thực, không phải với một công nghệ.
- Ưu tiên lựa chọn đơn giản nhất: prompt, rồi truy xuất, rồi tinh chỉnh, rồi mua, và hiếm khi xây từ đầu.
- Mức độ sẵn sàng của dữ liệu, nhân tài và nền tảng là điều kiện tiên quyết; tài trợ chúng là một phần của kế hoạch.
- Bối cảnh chịu quy định và chính phủ đòi hỏi minh bạch, tuân thủ mua sắm và lối thoát ngay từ thiết kế.
- Mô hình hóa tổng TCO và chi phí của việc không hành động, và đề phòng khóa chặt nhà cung cấp từ quyết định kiến trúc đầu tiên.

## Tài liệu tham khảo và đọc thêm

- Ajay Agrawal, Joshua Gans và Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
