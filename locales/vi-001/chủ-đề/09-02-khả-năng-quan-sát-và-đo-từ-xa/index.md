# 9.2 Khả năng quan sát và đo từ xa

## Tổng quan và động lực

[Đo từ xa](https://en.wikipedia.org/wiki/Telemetry) là dữ liệu một hệ thống phát ra về hành vi của chính nó: các chỉ số, nhật ký, vết và sự kiện được thu thập từ phần mềm đang chạy. Giám sát trả lời những câu hỏi bạn đã biết cần hỏi từ đo từ xa đó. Đĩa có đầy không? Tỷ lệ lỗi có vượt ngưỡng không? Dịch vụ có đang chạy không? [Khả năng quan sát](https://en.wikipedia.org/wiki/Observability_(software)) rộng hơn. Đó là khả năng đặt câu hỏi mới về trạng thái bên trong của hệ thống từ bên ngoài, không cần phát hành mã mới, để bạn hiểu hành vi bạn chưa bao giờ lường trước. Khi hệ thống lớn lên thành các kiến trúc phân tán, [vi dịch vụ](https://en.wikipedia.org/wiki/Microservices) và [hướng sự kiện](https://en.wikipedia.org/wiki/Event-driven_architecture), những thất bại đau nhất là những cái không ai thấy trước, và khả năng quan sát là thứ cho phép bạn gỡ lỗi chúng. Giám sát cho bạn biết có gì đó sai. Khả năng quan sát giúp bạn tìm ra vì sao.

Với các đội lớn, sự phân biệt này mang tính quyết định. Bạn có thể hiểu một khối nguyên bằng cách đọc nhật ký trên một máy. Một nền tảng hiện đại trải qua hàng trăm dịch vụ, nhiều đội, nhiều khu vực và phụ thuộc bên thứ ba, nơi một yêu cầu người dùng duy nhất có thể chạm hàng chục thành phần. Không một người nào giữ toàn bộ hệ thống trong đầu. Đo từ xa chất lượng cao, dùng chung trở thành mô liên kết cho phép bất kỳ kỹ sư nào theo một yêu cầu qua các ranh giới, xếp các triệu chứng qua dịch vụ, và suy luận về một hệ thống không ai sở hữu trọn vẹn. Không có nó, sự cố kéo dài, đổ lỗi bay giữa các đội, và nguyên nhân gốc vẫn ẩn.

Hệ thống doanh nghiệp và chính phủ nâng rủi ro với tuân thủ, khả năng kiểm toán và trách nhiệm giải trình công. Cơ quan quản lý có thể yêu cầu bằng chứng về ai đã truy cập gì và khi nào. Đội bảo mật cần đo từ xa để phát hiện xâm nhập. Dịch vụ hướng công dân phải cho thấy chúng đáp ứng cam kết hiệu năng đã công bố. Khả năng quan sát tốt phục vụ tất cả những điều này cùng lúc: nó là công cụ kỹ thuật, kiểm soát bảo mật và cơ chế trách nhiệm giải trình trong một. Chuẩn hóa trên công cụ đo mở tránh khóa chặt vào tác tử độc quyền của một nhà cung cấp, điều quan trọng vô cùng khi hệ thống phải bền hàng thập kỷ và sống sót qua các chu kỳ mua sắm.

*Xem thêm:* chương 9.1 (kỹ thuật độ tin cậy hệ thống và SLO), chương 9.3 (quản lý sự cố), và chương 3.3 (hệ phân tán).

## Các nguyên tắc chính

- **Gắn công cụ đo cho những câu hỏi chưa biết.** Thiết kế đo từ xa để bạn điều tra được các thất bại mới lạ, ngoài những cái bạn đã dự đoán.
- **Ba trụ cột, một câu chuyện.** Chỉ số, nhật ký và vết là các góc nhìn bổ sung; giá trị của chúng nhân lên khi được tương quan, không bị cô lập.
- **Cấu trúc hóa mọi thứ.** Đo từ xa có cấu trúc, phân tích được bằng máy với trường nhất quán thắng văn bản tự do chỉ con người đọc được.
- **Tương quan bằng định danh chung.** ID vết và yêu cầu được lan truyền khắp nơi cho phép bạn khâu một sự kiện duy nhất qua các dịch vụ.
- **Cảnh báo theo triệu chứng, không theo nguyên nhân.** Gọi con người cho vấn đề người dùng nhìn thấy; để bảng điều khiển và điều tra làm lộ nguyên nhân bên dưới.
- **Mỗi cuộc gọi phải hành động được.** Một cảnh báo không đòi hành động của con người là nhiễu xói mòn lòng tin và gây mệt mỏi.
- **Số phần tử cao là một tính năng.** Khả năng cắt theo người dùng, yêu cầu, khu vực và phiên bản là thứ làm gỡ lỗi trong môi trường sản xuất khả thi.
- **Sở hữu công cụ đo của bạn.** Chuẩn hóa trên đo từ xa mở, trung lập nhà cung cấp để bạn kiểm soát dữ liệu và đổi được backend.

## Khuyến nghị

### Xây trên ba trụ cột và hơn thế

**Chỉ số** là chuỗi thời gian số, rẻ để lưu và lý tưởng cho bảng điều khiển, xu hướng và ngưỡng cảnh báo. **Nhật ký** là bản ghi rời rạc, có dấu thời gian về sự kiện, giàu chi tiết và thiết yếu cho điều tra pháp y. **[Vết](https://en.wikipedia.org/wiki/Tracing_(software))** theo một yêu cầu đơn khi nó đi qua các dịch vụ, cho thấy độ trễ và phụ thuộc qua đồ thị gọi phân tán. Ngoài những cái này, hãy cân nhắc **sự kiện** (thay đổi trạng thái có ý nghĩa như triển khai), **hồ sơ hiệu năng** (nơi mã tiêu CPU và bộ nhớ), và **[giám sát người dùng thực](https://en.wikipedia.org/wiki/Real_user_monitoring)** về trải nghiệm phía máy khách thật. Không trụ cột nào đủ một mình. Mục tiêu là di chuyển trôi chảy giữa chúng trong khi điều tra.

### Chuẩn hóa trên OpenTelemetry và ghi nhật ký có cấu trúc

Hãy áp dụng [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) làm tiêu chuẩn trung lập nhà cung cấp để tạo và thu thập chỉ số, nhật ký và vết. Nó tách công cụ đo khỏi backend phân tích, để bạn đổi nhà cung cấp mà không gắn lại công cụ đo cho hàng trăm dịch vụ. Thuộc tính đó là then chốt cho các hệ thống doanh nghiệp và chính phủ sống lâu. Phát nhật ký dưới dạng bản ghi có cấu trúc (ví dụ JSON) với tên trường nhất quán cho dấu thời gian, mức nghiêm trọng, dịch vụ và định danh. Lan truyền một ID vết hoặc tương quan từ rìa qua mọi lệnh gọi hạ nguồn, và đưa nó vào mọi dòng nhật ký và exemplar chỉ số, để ba trụ cột tự động nối với nhau.

### Thiết kế cảnh báo cho khả năng hành động và nhiễu thấp

Triết lý cảnh báo của bạn quyết định trực ca có bền vững không. Hãy cảnh báo chủ yếu trên các triệu chứng người dùng cảm nhận, được diễn đạt dưới dạng tốc độ đốt SLO ([mục tiêu mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_objective)). Gọi khi bạn đang đốt qua ngân sách lỗi (mức thiếu hụt cho phép khỏi mục tiêu đó) đủ nhanh để vi phạm nó, dùng cảnh báo tốc độ đốt đa cửa sổ để cân bằng phát hiện nhanh với báo động giả. Dành việc gọi cho các vấn đề cần hành động tức thì của con người, và chuyển mọi thứ khác sang phiếu hoặc bảng điều khiển. Hãy tỉa không thương xót những cảnh báo kích hoạt mà không đòi hành động, vì mệt mỏi cảnh báo là nguyên nhân hàng đầu của sự cố thật bị bỏ lỡ và kiệt sức trực ca. Mỗi cảnh báo nên liên kết đến một sổ tay vận hành.

### Mô hình hóa sức khỏe bằng bảng điều khiển và giám sát SLO

Hãy xây bảng điều khiển quanh một mô hình sức khỏe rõ ràng, không phải bức tường mọi chỉ số bạn có. Một khung khởi đầu tốt là "bốn tín hiệu vàng": độ trễ, lưu lượng, lỗi và độ bão hòa. Tạo bảng điều khiển cấp dịch vụ cho thấy trạng thái SLO và ngân sách lỗi còn lại trong nháy mắt, cộng bảng điều khiển cấp cao hơn mô hình hóa sức khỏe toàn hệ thống và hành trình người dùng. Chọn lọc chúng có chủ đích, vì bảng điều khiển cho thấy mọi thứ truyền đạt không gì. Giữ chúng gần cảnh báo và sổ tay vận hành, để người ứng phó di chuyển nhanh từ tín hiệu đến ngữ cảnh đến hành động.

### Cho phép gỡ lỗi trong môi trường sản xuất với số phần tử cao

Những vấn đề sản xuất khó nhất đánh vào một lát hẹp: một khách hàng, một khu vực, một phiên bản API, một loại thiết bị. Để điều tra chúng bạn cần đo từ xa **số phần tử cao**, khả năng nhóm và lọc theo các trường có nhiều giá trị khác nhau như ID người dùng hay ID yêu cầu. Các sự kiện rộng, được gán thuộc tính phong phú mang nhiều chiều mỗi bản ghi cho phép bạn đặt câu hỏi tùy ý sau sự việc. Giữ đủ số phần tử và độ trung thực lấy mẫu để cô lập ngoại lệ, và ưu tiên vết liên kết exemplar để một đỉnh trên chỉ số dẫn bạn thẳng đến các yêu cầu chậm đại diện.

### Quản lý chi phí, lưu giữ và lấy mẫu

Khối lượng đo từ xa lớn lên cùng hệ thống và có thể thành một khoản chi lớn. Hãy đặt chính sách lưu giữ theo lớp dữ liệu: giữ dữ liệu độ phân giải cao ngắn và tổng hợp lâu hơn. Áp dụng lấy mẫu thông minh cho vết, nghiêng về giữ lỗi và yêu cầu chậm, để bạn giữ cái đuôi thú vị mà không trả cho mọi thành công thường lệ. Hãy xem xét chi tiêu đo từ xa thường xuyên, vì chi phí quan sát không được quản lý có thể sánh với hạ tầng chúng quan sát.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Sự kiện số phần tử cao | Gỡ lỗi mạnh, hỏi được mọi thứ | Chi phí lưu trữ và truy vấn cao hơn |
| Lấy mẫu quyết liệt | Chi phí thấp hơn, ít nhiễu hơn | Có thể bỏ sót sự kiện hiếm |
| Cảnh báo theo triệu chứng | Ít cuộc gọi hơn, hành động được | Cần SLO tốt để hoạt động tốt |
| Tiêu chuẩn OpenTelemetry | Trung lập nhà cung cấp, di động | Công sức di chuyển, công cụ đang trưởng thành |
| Lưu giữ nhật ký dài | Pháp y và kiểm toán tốt hơn | Chi phí lưu trữ, phơi nhiễm quyền riêng tư |

Quyết định quan sát quy về căng thẳng giữa độ trung thực và chi phí. Nắm bắt mọi thứ ở độ phân giải đầy đủ cho bạn khả năng nhìn lại hoàn hảo, nhưng ở quy mô thì đắt đến mức cấm đoán. Cắt quyết liệt thì tiết kiệm tiền, nhưng bạn có thể vứt bản ghi duy nhất sẽ giải thích một lần ngừng hoạt động. Lấy mẫu và các bậc lưu giữ là cách các đội trưởng thành đi trên lằn ranh này, giữ lỗi và ngoại lệ trong khi làm mỏng dữ liệu thường lệ. Đánh đổi cảnh báo là giữa độ nhạy và nhiễu: quá nhiều cảnh báo gây mệt mỏi và bỏ lỡ sự cố, quá ít để vấn đề mưng mủ. Cảnh báo theo triệu chứng, do SLO dẫn dắt giải quyết nhiều phần của điều này, nhưng chỉ nếu bạn có SLO có ý nghĩa.

## Câu hỏi để thảo luận với đội của bạn

1. **Kế hoạch của bạn để chuyển các dịch vụ cũ sang OpenTelemetry là gì, và bạn tránh trả cho hai ngăn xếp công cụ đo trong thời gian chuyển tiếp thế nào?** Công cụ đo trung lập nhà cung cấp là thuộc tính cho phép bạn đổi backend mà không gắn lại công cụ đo cho hàng trăm dịch vụ, và nó quan trọng nhất với các hệ thống doanh nghiệp và chính phủ sống lâu hơn bất kỳ hợp đồng nhà cung cấp đơn lẻ nào. Việc di chuyển là nơi thiện chí đình trệ: hệ sinh thái được gắn công cụ một nửa để lại khoảng trống đúng nơi một yêu cầu chuyển từ dịch vụ mới sang cũ, làm đứt vết đầu-đến-cuối. Hãy mang một bản kiểm kê vào cuộc thảo luận: dịch vụ nào phát dữ liệu tác tử độc quyền, cái nào phát OpenTelemetry, và nơi ngữ cảnh vết bị rơi ở ranh giới. Hãy quyết định trình tự đi theo đường yêu cầu thật thay vì sơ đồ tổ chức, và lập ngân sách cho khoảng thời gian bạn chạy cả hai bộ thu thập. Câu trả lời quyết định bạn có thực sự sở hữu đo từ xa của mình hay vẫn bị khóa vào tác tử của một nhà cung cấp.

2. **Lần cuối bạn kiểm toán mọi cảnh báo về khả năng hành động là khi nào, và bao nhiêu cuộc gọi tháng trước không đòi hành động của con người?** Mệt mỏi cảnh báo là nguyên nhân hàng đầu của sự cố thật bị bỏ lỡ và kiệt sức trực ca, nên một cuộc gọi không cần hành động không phải nhiễu vô hại, nó chủ động xói mòn sự ứng phó bạn phụ thuộc. Hãy mang biên nhận: kéo các cuộc gọi tháng trước, đánh dấu từng cái là được hành động hay bị phớt lờ, và đếm bao nhiêu cái ánh xạ đến một sổ tay vận hành. Với một đội lớn trải qua nhiều dịch vụ, cảnh báo ồn từ một đội làm giảm nhạy cảm của phiên trực chung cho mọi người. Hãy đặt tiêu chuẩn rằng mọi cuộc gọi liên kết đến một sổ tay vận hành và gắn với một tốc độ đốt SLO, rồi xóa phần còn lại không thương xót. Kết quả của cuộc kiểm toán này nên trực tiếp cắt khối lượng gọi của bạn và cho bạn biết dịch vụ nào không có SLO có ý nghĩa đằng sau cảnh báo của chúng.

3. **Chiến lược lấy mẫu vết của bạn là gì, và bạn tự tin đến đâu rằng nó giữ lại lỗi và cái đuôi chậm?** Khối lượng đo từ xa lớn lên cùng hệ thống và chi phí quan sát không được quản lý có thể sánh với hạ tầng nó quan sát, nên bạn sẽ lấy mẫu, và câu hỏi là liệu bạn lấy mẫu thông minh không. Lột số phần tử hoặc lấy mẫu mù loại bỏ chính các bản ghi cần để gỡ lỗi những vấn đề hẹp đánh vào một khách hàng, một khu vực, hay một phiên bản API. Hãy mang các bậc lưu giữ và quy tắc lấy mẫu hiện tại: bạn có nghiêng về giữ lỗi và yêu cầu chậm không, dùng vết liên kết exemplar để một đỉnh chỉ số dẫn đến một yêu cầu chậm đại diện? Với hệ thống được kiểm toán và bị ràng buộc quyền riêng tư, hãy dung hòa lưu giữ với quy tắc tối thiểu hóa dữ liệu để bạn không tích trữ dữ liệu cá nhân để gỡ lỗi. Câu trả lời đặt nơi bạn tiêu ngân sách đo từ xa và liệu lần ngừng hoạt động khó kế tiếp của bạn giải thích được hay là bí ẩn.

4. **SLO nào của bạn là cam kết hành trình người dùng thật, và cái nào là chỉ số đại diện không ai ngoài đội sở hữu tin?** Cảnh báo theo triệu chứng chỉ hoạt động khi các triệu chứng ánh xạ đến những điều người dùng thực sự cảm nhận, nên một cảnh báo nối với ngưỡng CPU hay mục tiêu sẵn sàng bịa gọi người vì vấn đề có thể không quan trọng trong khi im lặng với những vấn đề quan trọng. Với một tổ chức lớn, SLO cũng là hợp đồng cho phép các đội độc lập chia sẻ một vòng trực mà không tranh cãi lại mức nghiêm trọng ở mỗi sự cố. Hãy mang danh mục SLO hiện tại, hành trình người dùng mỗi mục tiêu định bảo vệ, và các vi phạm quý trước cùng liệu khách hàng có thực sự phàn nàn. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn các SLO dễ thấy nhất với cam kết hiệu năng đã công bố mà dịch vụ chịu trách nhiệm, để cùng tín hiệu tốc độ đốt gọi một kỹ sư cũng là bằng chứng bạn trình cho cơ quan quản lý hoặc cơ quan giám sát. Cuộc thảo luận nên cho nghỉ hưu các chỉ số đại diện và để lại một danh sách ngắn các mục tiêu mà người không phải kỹ sư nhận ra là lời hứa với người dùng.

5. **Ai sở hữu quản trị dữ liệu đo từ xa, và bạn có chứng minh được dữ liệu cá nhân được che trước khi hạ cánh vào backend quan sát của bạn không?** Sự kiện số phần tử cao và lưu giữ nhật ký dài chính là những tính năng làm gỡ lỗi khả thi, và chính là những cái biến kho quan sát thành bản sao không được quản lý của dữ liệu cá nhân người dùng. Lực kéo đối lập là thật: kỹ sư muốn thuộc tính phong phú hơn và lưu giữ lâu hơn, trong khi quyền riêng tư và pháp lý muốn tối thiểu hóa dữ liệu và tuổi thọ ngắn. Hãy mang bản đồ luồng dữ liệu cho thấy trường nào mang dữ liệu cá nhân hay nhạy cảm, nơi che hay mã thông báo hóa xảy ra trong đường ống, và các bậc lưu giữ của bạn theo lớp dữ liệu. Với hệ thống chịu quy định và công, hãy nêu chủ sở hữu chịu trách nhiệm, ánh xạ lưu giữ với cơ sở pháp lý và quy tắc tối thiểu hóa dữ liệu bạn vận hành dưới đó, và sẵn sàng cho kiểm toán viên thấy rằng truy cập vào chính đo từ xa được ghi nhật ký và kiểm soát. Câu trả lời quyết định nền tảng quan sát của bạn là tài sản hay vụ vi phạm thường trực đang chờ được phát hiện.

6. **Khi một sự cố xuyên qua dịch vụ của nhiều đội, đo từ xa của bạn có cho một người ứng phó theo yêu cầu đầu-đến-cuối, hay dấu vết đứt ở mỗi ranh giới quyền sở hữu?** Toàn bộ lời hứa của đo từ xa có tương quan, lan truyền ID là một kỹ sư duy nhất có thể suy luận về hệ thống không ai sở hữu trọn vẹn, và lời hứa đó sụp đổ đúng ở ranh giới nơi ngữ cảnh vết bị rơi hoặc nơi hai đội dùng định danh và công cụ không tương thích. Hãy cân nhắc lực kéo về tự chủ từng đội trong việc chọn công cụ quan sát với chi phí chung của một hệ sinh thái phân mảnh nơi mỗi lần bàn giao là ngõ cụt trong lúc ngừng hoạt động. Hãy mang dòng thời gian một sự cố xuyên đội gần đây và đánh dấu nơi người ứng phó mất sợi dây, cộng bản kiểm kê dịch vụ nào lan truyền một ID tương quan chung và cái nào không. Với một doanh nghiệp lớn hay nền tảng chính phủ lắp ráp từ nhiều nhà cung cấp và hệ thống sống lâu, hãy quyết định bạn ra lệnh tập trung bao nhiêu, một tiêu chuẩn ngữ cảnh vết chung và sơ đồ ID chung, so với những gì bạn để cho các đội, vì các thành phần bạn mua lại qua nhiều thập kỷ vẫn phải tương tác trên cùng một yêu cầu. Câu trả lời cho bạn biết sự cố đa đội kế tiếp là một cuộc điều tra phối hợp hay một vòng đổ lỗi.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm dịch vụ và không có tay dư, hãy gắn công cụ đo bằng OpenTelemetry từ ngày đầu và phát nhật ký JSON có cấu trúc mang một ID yêu cầu đầu-đến-cuối. Khoản đầu tư nhỏ đó biến "ứng dụng chậm" thành một vết bạn đọc được, và giữ bạn tự do chuyển từ gói miễn phí sang backend trả phí sau này mà không gắn lại công cụ đo. Bỏ qua bảng điều khiển cầu kỳ và bộ máy SLO cho đến khi bạn có người dùng mà trải nghiệm của họ bạn đo được thực sự.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia quan sát và ngân sách eo hẹp, vì vậy hãy dựa vào backend được quản lý nơi công cụ đo, lưu trữ và bảng điều khiển đi kèm thay vì lắp ráp ngăn xếp của riêng bạn. Lựa chọn mua-so-với-xây nghiêng về mua hầu như lúc nào ở đây; sự chú ý khan hiếm của bạn nên dành cho hai ba cảnh báo tín hiệu vàng cho bạn biết dịch vụ hỏng hơn là chạy một đường ống đo từ xa. Đặt giới hạn lưu giữ cứng để chi phí đo từ xa không lặng lẽ vượt hạ tầng nó theo dõi.

**Doanh nghiệp lớn.** Công việc là quản trị qua nhiều đội: một tiêu chuẩn OpenTelemetry dùng chung, một sơ đồ ID tương quan chung, và bảng điều khiển SLO được chọn lọc để một người ứng phó duy nhất theo được một yêu cầu qua hàng chục dịch vụ. Quản lý đo từ xa như trung tâm chi phí với các bậc lưu giữ và chính sách lấy mẫu, chuẩn hóa cảnh báo trên tốc độ đốt SLO để giữ phiên trực chung bền vững, và tỉa cảnh báo ồn tập trung để mệt mỏi của một đội không làm giảm nhạy cảm của mọi người. Coi tầng công cụ đo là hạ tầng trung lập nhà cung cấp sống lâu hơn bất kỳ hợp đồng backend đơn lẻ nào.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình thiết kế. Hãy chuẩn hóa trên công cụ đo mở để một hệ thống dự kiến chạy hàng thập kỷ sống sót qua mua lại bởi các nhà cung cấp khác nhau mà không bị giữ làm con tin bởi tác tử độc quyền, và yêu cầu khả năng di chuyển đó trong hợp đồng. Dùng nhật ký kiểm toán có cấu trúc để cho thấy ai đã truy cập bản ghi nào và khi nào, che hoặc mã thông báo hóa dữ liệu cá nhân trước khi nó đến kho đo từ xa, và dung hòa lưu giữ với luật tối thiểu hóa dữ liệu. Công bố bảng điều khiển SLO cho dịch vụ hướng công dân để cùng tín hiệu các kỹ sư của bạn theo dõi là bằng chứng hiển thị về cam kết bạn chịu trách nhiệm.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người phát hành backend di động và liên tục nhận phàn nàn mơ hồ "ứng dụng chậm" mà họ không tái hiện được. Đội thêm OpenTelemetry vào nhúm dịch vụ của mình và chuyển sang nhật ký JSON có cấu trúc với ID yêu cầu mang từ ứng dụng qua mọi bước. Báo cáo chậm kế tiếp được giải quyết trong vài phút: một vết cho thấy thiếu chỉ mục cơ sở dữ liệu trên bảng đơn hàng dưới một truy vấn cụ thể. Vì họ chọn công cụ đo mở từ sớm, họ sau đó chuyển từ gói miễn phí sang backend trả phí mà không gắn lại bất cứ thứ gì.

**Doanh nghiệp lớn.** Một nền tảng thương mại điện tử lớn gắn công cụ đo mọi dịch vụ bằng OpenTelemetry, lan truyền một ID vết từ trình duyệt của khách hàng qua thanh toán, chi trả, tồn kho và vận chuyển. Khi chuyển đổi tụt, một kỹ sư trực bắt đầu từ cảnh báo tốc độ đốt SLO, mở các tín hiệu vàng của bảng điều khiển thanh toán, phát hiện độ trễ tăng ở một khu vực, và theo một vết exemplar đến một lệnh gọi cơ sở dữ liệu chậm trong một dịch vụ duy nhất. Thuộc tính số phần tử cao cho thấy vấn đề giới hạn ở một danh mục sản phẩm, hướng dẫn một bản sửa có mục tiêu trong vài phút thay vì hàng giờ.

**Chính phủ.** Một cơ quan y tế quốc gia chạy nền tảng hồ sơ bệnh nhân dưới quy tắc kiểm toán và quyền riêng tư nghiêm ngặt. Nhật ký có cấu trúc nắm bắt ai đã truy cập bản ghi nào và khi nào, nuôi cả giám sát bảo mật lẫn báo cáo tuân thủ, trong khi các trường nhận dạng cá nhân được che hoặc mã thông báo hóa trong đo từ xa. Bảng điều khiển SLO công khai cho thấy tính sẵn sàng và độ trễ của đặt lịch hướng công dân. Bằng cách chuẩn hóa trên công cụ đo mở, cơ quan tránh khóa chặt độc quyền qua một hệ thống dự kiến chạy hàng thập kỷ và được các nhà cung cấp khác nhau mua lại trong vòng đời của nó.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức chính của khả năng quan sát là mức giảm mạnh thời gian để phát hiện và giải quyết sự cố. Với một dịch vụ nơi ngừng hoạt động tốn kém, cắt thời gian giải quyết trung bình từ hàng giờ xuống vài phút trả giá công cụ nhiều lần chỉ trong một sự cố lớn. Khả năng quan sát cũng tiết kiệm thời gian kỹ thuật bạn sẽ tốn để đoán, tái hiện lỗi, và tranh cãi đội nào có lỗi, và nó rút ngắn vòng phản hồi cho phép các đội phát hành tự tin. Giá trị bảo mật và tuân thủ cũng thật: cùng đo từ xa hỗ trợ phát hiện xâm nhập và bằng chứng kiểm toán.

Tổng chi phí sở hữu gồm công sức gắn công cụ đo, chi phí lưu trữ và truy vấn đo từ xa, và kỷ luật chọn lọc tín hiệu từ nhiễu. Những chi phí này hiển thị và lặp lại, cám dỗ lãnh đạo đầu tư thiếu. Chi phí của việc không áp dụng lớn hơn nhưng khó thấy hơn: ngừng hoạt động kéo dài, vấn đề hiệu năng không chẩn đoán được, sự cố bảo mật phát hiện muộn hoặc không bao giờ, và kỹ sư kiệt sức vì cảnh báo họ không làm gì được. Hãy lập luận bằng dữ liệu sự cố cụ thể. Cho thấy thời gian giải quyết và tác động kinh doanh của các lần ngừng hoạt động gần đây, và dự phóng mức giảm mà đo từ xa tốt hơn sẽ mang lại. Đóng khung khả năng quan sát là bảo hiểm cũng tăng tốc phân phối, thay vì trung tâm chi phí thuần túy, sẽ thắng lập luận.

## Phản mẫu và cạm bẫy

- **Cảnh báo mọi thứ.** Gọi vì mọi bất thường dạy người ứng phó phớt lờ cảnh báo, nên sự cố thật lọt qua.
- **Gọi theo nguyên nhân.** Cảnh báo theo nguyên nhân nội bộ thay vì triệu chứng người dùng làm ngập trực ca bằng nhiễu và bỏ lỡ thất bại mới lạ.
- **Nhật ký không cấu trúc.** Nhật ký văn bản tự do không truy vấn hay tương quan được buộc phải grep thủ công, chậm trong sự cố.
- **Ba trụ cột cô lập.** Chỉ số, nhật ký và vết trong công cụ rời rạc không có ID chung ngăn theo một sự kiện đầu-đến-cuối.
- **Sinh sôi bảng điều khiển.** Hàng trăm bảng điều khiển không được chọn lọc nghĩa là không ai biết cái nào cho thấy hệ thống có khỏe không.
- **Sụp đổ số phần tử.** Lột các trường số phần tử cao để tiết kiệm chi phí loại bỏ chính dữ liệu cần để gỡ lỗi vấn đề hẹp.
- **Khóa chặt nhà cung cấp.** Tác tử độc quyền khắp nơi khiến chuyển backend đắt đến cấm đoán và giữ dữ liệu của bạn làm con tin.

## Mô hình trưởng thành

**Mức 1, Khởi đầu.** Khả năng quan sát tùy nghi và phản ứng. Kiểm tra thời gian hoạt động cơ bản và nhật ký không cấu trúc sống trên từng máy, gỡ lỗi nghĩa là đăng nhập vào máy chủ để grep, và không có đo từ xa dùng chung. Cảnh báo ồn, theo nguyên nhân, và thường bị phớt lờ, nên sự cố thật nổi lên qua phàn nàn của người dùng thay vì tín hiệu.

**Mức 2, Phát triển.** Thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Một số dịch vụ đẩy chỉ số và nhật ký lên một nơi trung tâm, vài bảng điều khiển và cảnh báo ngưỡng tồn tại, nhưng nhật ký chỉ bán cấu trúc và vết vắng mặt hoặc một phần. Tương quan qua dịch vụ là thủ công, và liệu một kỹ sư theo được một yêu cầu đầu-đến-cuối hay không phụ thuộc vào đội nào tình cờ liên quan.

**Mức 3, Chuẩn hóa.** Công cụ đo được lập tài liệu và thực thi toàn tổ chức. OpenTelemetry qua các dịch vụ với một ID vết hoặc tương quan được lan truyền, ghi nhật ký có cấu trúc với tên trường nhất quán, truy vết phân tán, bảng điều khiển tín hiệu vàng được chọn lọc, và cảnh báo theo triệu chứng dựa trên SLO là tiêu chuẩn mọi đội theo. Mọi cuộc gọi liên kết đến một sổ tay vận hành và gắn với một SLO, và trực ca bền vững thay vì nguồn kiệt sức.

**Mức 4, Quản lý.** Chính hệ sinh thái quan sát được đo và kiểm soát theo đường cơ sở. Bạn theo dõi độ phủ công cụ đo và tỷ lệ lan truyền ngữ cảnh vết qua các dịch vụ, phần cuộc gọi được hành động so với bị phớt lờ, thời gian trung bình để phát hiện và giải quyết, mức đạt SLO và tốc độ đốt ngân sách lỗi, và chi phí đo từ xa theo dịch vụ so với ngân sách. Khoảng trống và nhiễu cảnh báo được kéo xuống bằng dữ liệu hướng tới mục tiêu tường minh, độ trung thực lấy mẫu được xác minh để các bản ghi lỗi và đuôi chậm sống sót, và quyết định tiếp tục hay dừng về độ phủ và lưu giữ được đưa ra dựa trên bằng chứng thay vì ý kiến.

**Mức 5, Điều phối.** Khả năng quan sát được cải thiện liên tục và tích hợp trong toàn tổ chức. Đo từ xa số phần tử cao, giàu sự kiện cho phép điều tra tùy ý bất kỳ lát nào, cảnh báo do tốc độ đốt SLO dẫn dắt với nhiễu tối thiểu, và lấy mẫu cùng lưu giữ thích ứng với chi phí và rủi ro thay đổi. Đo từ xa nuôi hoạch định năng lực, phát hiện bảo mật và quyết định sản phẩm một cách thường lệ, và nền tảng tự điều chỉnh tín hiệu, ngân sách và độ phủ khi hệ thống, bức tranh mối đe dọa và nghĩa vụ quy định dịch chuyển.

## Ý tưởng để thảo luận

- Cân bằng đúng giữa độ trung thực đo từ xa và chi phí cho các dịch vụ trọng yếu nhất của bạn nằm ở đâu?
- Làm sao bạn quyết định cái gì xứng đáng một cuộc gọi so với một phiếu so với chỉ một mục bảng điều khiển?
- Chiến lược của bạn để lan truyền ID tương quan qua các đội không chia sẻ cơ sở mã hay chu kỳ phát hành là gì?
- Làm sao bạn bảo toàn sức mạnh gỡ lỗi số phần tử cao trong khi đáp ứng yêu cầu quyền riêng tư và tối thiểu hóa dữ liệu?
- Công cụ quan sát nên được ra lệnh tập trung hay chọn theo từng đội, và hệ quả của cả hai là gì?
- Bạn sẽ chứng minh với kiểm toán viên rằng đo từ xa của bạn đầy đủ và chống giả mạo thế nào?

## Những điểm cần ghi nhớ

- Giám sát phát hiện vấn đề đã biết; khả năng quan sát cho bạn điều tra vấn đề chưa biết mà không phát hành mã mới.
- Chỉ số, nhật ký và vết có giá trị nhất khi được tương quan qua định danh chung, không bị cô lập.
- Chuẩn hóa trên OpenTelemetry và ghi nhật ký có cấu trúc để giữ trung lập nhà cung cấp và di động qua vòng đời hệ thống dài.
- Cảnh báo theo triệu chứng người dùng nhìn thấy qua tốc độ đốt SLO, làm mọi cuộc gọi hành động được, và tỉa nhiễu không ngừng.
- Chọn lọc bảng điều khiển quanh một mô hình sức khỏe rõ ràng như các tín hiệu vàng thay vì hiển thị mọi chỉ số.
- Đo từ xa số phần tử cao, giàu sự kiện là thứ làm gỡ lỗi vấn đề sản xuất hẹp khả thi.

## Tài liệu tham khảo và đọc thêm

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (các chương về giám sát và cảnh báo)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- Dự án OpenTelemetry, đặc tả và tài liệu (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, chương giám sát)
