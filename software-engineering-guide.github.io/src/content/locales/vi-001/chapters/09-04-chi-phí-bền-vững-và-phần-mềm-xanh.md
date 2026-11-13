# 9.4 Chi phí, bền vững và phần mềm xanh

## Tổng quan và động lực

Phần mềm chạy trên hạ tầng vật lý tiêu thụ tiền, điện, nước và vật liệu. Trong phần lớn lịch sử tính toán, những chi phí này là vấn đề của người khác: ngân sách vốn giấu phần cứng, và năng lượng vô hình với kỹ sư. [Điện toán đám mây](https://en.wikipedia.org/wiki/Cloud_computing) đã thay đổi điều đó. Nó làm tiêu thụ chi tiết, theo yêu cầu, và quy được trực tiếp, biến chi phí, và ngày càng cả carbon, thành mối quan tâm kỹ thuật. Chương này bao quát hai kỷ luật đan xen: **FinOps**, thực hành mang trách nhiệm giải trình tài chính vào chi tiêu đám mây biến đổi, và **[phần mềm xanh](https://en.wikipedia.org/wiki/Green_computing)**, thực hành xây hệ thống làm cùng công việc với ít năng lượng hơn và phát thải carbon thấp hơn. Chúng chồng lấn mạnh, vì phần mềm hiệu quả thường vừa rẻ hơn vừa sạch hơn.

Với các đội lớn, con số rất khổng lồ. Hóa đơn đám mây của một doanh nghiệp lớn có thể đạt hàng chục hay hàng trăm triệu mỗi năm, và vài điểm lãng phí đại diện cho tiền thật có thể tài trợ nhân sự hay sản phẩm. [Dấu chân carbon](https://en.wikipedia.org/wiki/Carbon_footprint) của hệ sinh thái số lớn cũng đáng kể, và các tổ chức đối mặt áp lực ngày càng tăng từ cơ quan quản lý, nhà đầu tư, khách hàng và chính nhân viên để đo và giảm nó. Khi hàng trăm đội mỗi đội đưa ra quyết định độc lập về kích thước thể hiện, lưu giữ dữ liệu và kiến trúc, những kém hiệu quả nhỏ cộng dồn thành chi phí và phát thải lớn. Quản trị làm chi phí và carbon hiển thị và chịu trách nhiệm là thiết yếu để giữ cả hai trong tầm kiểm soát.

Sự liên quan với doanh nghiệp và chính phủ là trực tiếp. Các tổ chức khu vực công chi tiền thuế và ngày càng bị ràng buộc bởi yêu cầu bền vững và cam kết phát thải ròng bằng không, nên chứng minh vận hành hiệu quả, carbon thấp vừa là nghĩa vụ tài khóa vừa là nghĩa vụ chính sách. Doanh nghiệp đối mặt sự soi xét của nhà đầu tư về hiệu quả môi trường và áp lực cạnh tranh lên biên lợi nhuận. Trong cả hai bối cảnh, chi phí và bền vững đã chuyển từ chuyện nghĩ sau thành mối quan tâm cấp hội đồng quản trị. Lựa chọn kỹ thuật là nơi những mối quan tâm đó cuối cùng được hiện thực hóa hoặc bỏ lỡ.

## Các nguyên tắc chính

- **Làm tiêu thụ hiển thị.** Bạn không tối ưu được thứ bạn không thấy; chi phí và carbon phải được quy cho các đội và dịch vụ gây ra chúng.
- **Trách nhiệm giải trình thuộc về chủ sở hữu.** Những kỹ sư cung cấp tài nguyên nên thấy và sở hữu tác động chi phí và carbon của họ.
- **Hiệu quả phục vụ chi phí và carbon cùng nhau.** Làm cùng công việc với ít tài nguyên hơn thường tiết kiệm tiền và phát thải đồng thời.
- **Chọn kích thước vừa liên tục.** Nhu cầu thay đổi, nên việc cung cấp phải được xem xét lại, không đặt một lần rồi quên.
- **Carbon có thời gian và địa điểm.** Cùng một phép tính phát thải nhiều hay ít tùy khi nào và nơi nào điện được sản xuất.
- **Cân bằng bộ ba.** Chi phí, hiệu năng và độ tin cậy đánh đổi lẫn nhau; hãy tối ưu có chủ đích, không mù quáng.
- **Thiết kế cho hiệu quả sớm.** Lựa chọn kiến trúc chi phối chi phí và carbon dài hạn nhiều hơn hẳn việc tinh chỉnh giai đoạn muộn.

## Khuyến nghị

### Thiết lập khả năng nhìn thấy, tối ưu và trách nhiệm giải trình FinOps

FinOps tiến hành qua ba giai đoạn lặp. **Thông tin**: xây khả năng nhìn thấy qua gắn thẻ, phân bổ và bảng điều khiển, để mọi chi phí được quy cho một đội, dịch vụ và mục đích kinh doanh, và chi phí chung được chia công bằng. **Tối ưu**: loại bỏ lãng phí (tài nguyên nhàn rỗi và mồ côi), chọn kích thước vừa cho dịch vụ cung cấp thừa, áp dụng chiết khấu dựa trên cam kết như đặt trước hay gói tiết kiệm cho tải nền ổn định, và dùng năng lực spot hay có thể bị chiếm cho công việc ngắt được. **Vận hành**: nhúng chi phí vào thực hành kỹ thuật bình thường với ngân sách, cảnh báo bất thường, dự báo và rà soát thường xuyên. Trên hết, hãy đặt dữ liệu chi phí trước mặt các kỹ sư tạo ra nó. Làm hiệu quả thành mục tiêu chung của kỹ thuật, tài chính và sản phẩm, không chỉ là mối quan tâm của tài chính.

### Xây phần mềm nhận biết carbon và tiết kiệm năng lượng

Giảm carbon có ba đòn bẩy. **Hiệu quả năng lượng**: viết và cấu hình phần mềm để làm cùng công việc với ít chu kỳ CPU, ít bộ nhớ và ít di chuyển dữ liệu hơn, qua thuật toán tốt hơn, bộ nhớ đệm, và tránh tính toán không cần thiết. **Hiệu quả phần cứng**: dùng tài nguyên đầy đủ qua mức sử dụng cao hơn, hợp nhất, và phần cứng hiện đại hiệu quả, vì năng lực nhàn rỗi vẫn tiêu điện và hàm chứa carbon sản xuất. **Nhận biết carbon**: dịch chuyển khối lượng công việc linh hoạt theo thời gian và không gian đến khi và nơi lưới điện sạch hơn, ví dụ chạy công việc lô khi sản xuất tái tạo cao, hoặc ở khu vực có điện carbon thấp. Hãy đo bằng các cách tiếp cận được công nhận như đặc tả Cường độ Carbon Phần mềm. Ưu tiên nhà cung cấp và khu vực có cam kết tái tạo mạnh và báo cáo minh bạch.

### Thiết kế kiến trúc bền vững và chọn kích thước vừa

Kiến trúc quyết định sàn cho chi phí và carbon. Ưu tiên thiết kế đàn hồi co giãn theo nhu cầu thực và co về không khi nhàn rỗi, để bạn không bao giờ trả tiền giữ năng lực không dùng chạy. [Serverless](https://en.wikipedia.org/wiki/Serverless_computing) và [co giãn tự động](https://en.wikipedia.org/wiki/Autoscaling) giảm lãng phí cho khối lượng công việc đột biến, và dịch vụ được quản lý có thể cải thiện mức sử dụng qua [đa người thuê](https://en.wikipedia.org/wiki/Multitenancy). Chọn kích thước vừa cho tính toán, lưu trữ và cơ sở dữ liệu theo mức dùng thực thay vì cung cấp thừa vì sợ hãi. Đặt chính sách vòng đời dữ liệu để dữ liệu lạnh chuyển sang bậc rẻ hơn, tiêu ít năng lượng hơn hoặc bị xóa. Giảm khối lượng dữ liệu và truyền mạng cắt cả chi phí lưu trữ lẫn năng lượng di chuyển bit. Coi hiệu quả là yêu cầu thiết kế, được rà soát cạnh hiệu năng và độ tin cậy.

### Cân bằng chi phí, hiệu năng và độ tin cậy có chủ đích

Chi phí, hiệu năng và độ tin cậy tạo thành một bộ ba. Đẩy mạnh một cái, bạn thường đánh thuế các cái kia: nhiều dư thừa hơn và độ trễ thấp hơn tốn hơn, và thường tiêu nhiều năng lượng hơn. Hãy làm các đánh đổi này tường minh và gắn chúng với giá trị kinh doanh. Dùng SLO ([mục tiêu mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_objective)) để xác định dịch vụ thực sự cần bao nhiêu độ tin cậy và hiệu năng, rồi cung cấp theo mục tiêu đó thay vì mạ vàng mọi thứ đồng đều. Khối lượng công việc không trọng yếu và nội bộ có thể chấp nhận cấu hình rẻ hơn, ít dư thừa hơn, linh hoạt carbon hơn. Dành cung cấp cao cấp cho cái thực sự đáng.

### Quản trị mà không ngột ngạt

Hãy cung cấp lan can, không phải cổng. Các đội nền tảng trung tâm có thể đưa ra mặc định hiệu quả, thực thi gắn thẻ, cảnh báo ngân sách và bảng điều khiển tự phục vụ, trong khi để quyết định hằng ngày cho các đội sở hữu khối lượng công việc. Đặt mục tiêu toàn tổ chức cho hiệu quả chi phí và giảm carbon, báo cáo tiến độ minh bạch, và ăn mừng khoản tiết kiệm. Tránh quan liêu phê duyệt nặng làm chậm phân phối. Mục tiêu là làm lựa chọn hiệu quả thành mặc định dễ.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Chiết khấu cam kết | Tiết kiệm lớn trên tải nền | Khóa chặt, rủi ro nếu nhu cầu dịch chuyển |
| Năng lực spot/có thể bị chiếm | Tính toán rẻ nhất, dùng năng lực dư của lưới | Gián đoạn, thêm độ phức tạp |
| Chọn kích thước vừa quyết liệt | Chi phí và carbon thấp hơn | Rủi ro cung cấp thiếu khi đột biến |
| Lập lịch nhận biết carbon | Phát thải thấp hơn | Công việc bị trễ, công sức kỹ thuật |
| Dư thừa đa khu vực | Độ tin cậy cao hơn | Chi phí, năng lượng và carbon nhiều hơn |

Đánh đổi thống nhất là độ tin cậy và hiệu năng tối đa hiếm khi trùng với chi phí và carbon tối thiểu. Hệ thống dư thừa, luôn bật, độ trễ thấp thì đắt và ngốn năng lượng, nên mạ vàng đồng đều lãng phí cả tiền lẫn phát thải trên khối lượng công việc không cần. Kỷ luật là chọn kích thước tham vọng khớp với giá trị kinh doanh bằng SLO, chỉ tiêu tài nguyên cao cấp nơi chúng quan trọng. Chiết khấu cam kết và năng lực spot mang lại tiết kiệm thật, nhưng chúng đưa vào khóa chặt và rủi ro gián đoạn mà bạn phải quản lý. Lập lịch nhận biết carbon tiết kiệm phát thải, nhưng chỉ phù hợp với khối lượng công việc chịu được trễ hay di dời.

## Câu hỏi để thảo luận với đội của bạn

1. **Hôm nay phần nào trong chi tiêu đám mây của bạn thực sự được gắn thẻ và quy cho một đội?** Giai đoạn thông tin của FinOps là nền móng: bạn không tối ưu được thứ bạn không thấy, và chi tiêu không gắn thẻ, không phân bổ nghĩa là không ai sở hữu lãng phí. Hãy mang con số độ phủ thực vào cuộc thảo luận, không phải khát vọng, và danh sách các mục chi lớn nhất chưa gắn thẻ. Với một tổ chức lớn nơi hàng trăm đội mỗi đội cung cấp độc lập, tỷ lệ quy thấp nghĩa là kém hiệu quả chung cộng dồn vô hình thành hàng triệu. Trong bối cảnh chính phủ và doanh nghiệp, việc quy cũng là cách bạn bảo vệ chi tiêu tiền thuế hay cổ đông và cách bạn phân bổ chi phí công bằng của nền tảng dùng chung. Câu trả lời đặt nước đi đầu tiên của bạn: nếu độ phủ thấp, thực thi gắn thẻ và phân bổ đến trước mọi việc chọn kích thước vừa, vì tối ưu không có khả năng nhìn thấy là đoán mò.

2. **Phần nào trong tải nền của bạn được chiết khấu cam kết bao phủ, và điều gì xảy ra với những cam kết đó nếu nhu cầu dịch chuyển?** Đặt trước và gói tiết kiệm mang lại tiết kiệm lớn trên tải nền ổn định, nhưng chúng đưa vào khóa chặt, nên mua quá hăng biến chiết khấu thành khoản nợ khi một sản phẩm bị khai tử hay di chuyển. Hãy mang các con số: phần trăm độ phủ cam kết của bạn, xu hướng tải nền, và khối lượng công việc có khả năng đổi hình dạng nhất trong năm tới. Kỷ luật là chỉ cam kết sàn bạn tự tin tồn tại, bao phủ lớp biến đổi bằng theo yêu cầu hoặc spot, và xem xét lại khi nhu cầu tiến hóa. Với một doanh nghiệp lớn đây là quyết định kiểu ngân quỹ với phơi nhiễm tài chính thật, nên tài chính và kỹ thuật nên cùng sở hữu thay vì một bên một mình. Câu trả lời nên tách tải nền bền vững của bạn khỏi nhu cầu không chắc chắn và định cỡ cam kết theo cái trước.

3. **Bao nhiêu đội máy của bạn nhàn rỗi, và bạn đang đếm carbon sản xuất hàm chứa hay chỉ năng lượng nó đốt khi chạy?** Năng lực nhàn rỗi vẫn tiêu điện và mang carbon sản xuất đã tiêu để xây phần cứng, nên chỉ tập trung vào năng lượng chạy trong khi cung cấp thừa bỏ sót một phần thật của dấu chân. Hãy mang dữ liệu sử dụng: trung bình và đỉnh, khoảng cách giữa cung cấp và dùng, và nơi co về không hay hợp nhất khả thi. Mức sử dụng cao hơn phục vụ chi phí và carbon cùng lúc, là mạch xuyên suốt của chương này, nên lãng phí nhàn rỗi là chiến thắng sạch nhất bạn có. Với các tổ chức dưới yêu cầu phát thải ròng bằng không, một thước đo carbon trung thực gồm phát thải hàm chứa là thứ phân biệt tiến bộ thật với tẩy xanh mời phản ứng quy định và danh tiếng. Câu trả lời nên nhắm các khối lượng công việc mức sử dụng thấp nhất để hợp nhất, co giãn tự động, hoặc co về không, và đặt một cách đo không lặng lẽ bỏ qua carbon sản xuất.

4. **Kỹ sư của bạn có thấy chi phí và carbon của dịch vụ của chính họ không, và có ai hành động theo những gì họ thấy không?** Khả năng nhìn thấy chỉ sinh lời khi nó đến những người cung cấp tài nguyên và thay đổi hành vi của họ, nên bảng điều khiển mà tài chính xem hằng tháng nhưng kỹ sư không bao giờ mở là đồ trang trí, không phải trách nhiệm giải trình. Lực kéo đối lập là thật: đội nền tảng muốn kiểm soát trung tâm và báo cáo sạch, trong khi đội phân phối bực với bất cứ thứ gì cảm giác như giám sát hay thêm một cổng cho việc phát hành. Hãy mang bằng chứng ai thực sự xem dữ liệu chi phí và carbon, bao lâu một lần, và liệu có việc chọn kích thước vừa hay dọn dẹp nào theo sau trong quý vừa rồi không. Với một tổ chức lớn nơi hàng trăm đội cung cấp độc lập, sự khác biệt giữa tín hiệu kỹ sư sở hữu và báo cáo họ phớt lờ là sự khác biệt giữa tiết kiệm cộng dồn và lãng phí cộng dồn. Trong bối cảnh doanh nghiệp và chính phủ, hãy đặt kinh tế đơn vị (chi phí và carbon mỗi yêu cầu, mỗi khách hàng, hay mỗi hồ sơ) trước mặt đội sở hữu, vì một con số tổng hợp bảo vệ ngân sách nhưng một con số mỗi đơn vị đổi một quyết định thiết kế.

5. **Khối lượng công việc nào thực sự linh hoạt về thời gian hay khu vực, và cần gì để lập lịch chúng nơi lưới sạch hơn?** Lập lịch nhận biết carbon dịch chuyển công việc linh hoạt đến khi và nơi điện carbon thấp, nhưng nó chỉ phù hợp với công việc chịu được trễ hay di dời, nên việc đầu tiên là tách công việc lô thực sự hoãn được khỏi bất cứ thứ gì hướng người dùng hay ràng buộc độ trễ. Đánh đổi là di chuyển công việc qua khu vực hay cửa sổ ngoài giờ cao điểm thêm công sức kỹ thuật, chi phí truyền dữ liệu, và đôi khi rủi ro cư trú dữ liệu có thể lấn át phát thải tiết kiệm. Hãy mang danh sách ứng viên các công việc lô và phân tích, độ chịu trễ của chúng, ràng buộc cư trú dữ liệu, và cường độ carbon của các khu vực bạn chạy chúng được hợp pháp. Với doanh nghiệp đây là tối ưu khiêm tốn bên trên chọn kích thước vừa, nên hãy xếp nó sau các nền tảng chi phí thay vì trước. Trong chính phủ, quy tắc cư trú dữ liệu và chủ quyền có thể cấm di chuyển dữ liệu công dân qua biên giới bất kể độ sạch của lưới, nên chọn khu vực là câu hỏi pháp lý trước khi là câu hỏi carbon.

6. **Bạn đã đặt mục tiêu hiệu quả và bền vững nào, và chúng có được viết để đạt chúng không thể lặng lẽ làm hỏng độ tin cậy không?** Mục tiêu tập trung công sức, nhưng một mục tiêu chi phí hay carbon thô mời hành vi sai: các đội cung cấp thiếu, lột dư thừa, hoặc hoãn công việc theo cách đổi khoản tiết kiệm nhỏ lấy sự cố lớn. Căng thẳng là giữa con số tham vọng từ trên xuống mà lãnh đạo báo cáo được và mục tiêu từ dưới lên đặt trên SLO thực của từng dịch vụ, nên hai thứ phải được dung hòa thay vì áp đặt. Hãy mang mục tiêu hiện tại của bạn, đường cơ sở chúng được đo theo, và các lan can độ tin cậy ngăn tối ưu cắt vào cái một dịch vụ thực sự cần. Với một tổ chức lớn, mục tiêu tổng hợp phải phân rã công bằng cho các đội có khối lượng công việc khác nhau, nên một dịch vụ thanh toán hướng khách hàng và một công việc báo cáo nội bộ không nên mang cùng kỳ vọng hiệu quả. Trong bối cảnh doanh nghiệp và chính phủ nơi con số bền vững xuất hiện trong công bố công khai, hãy gắn mọi con số báo cáo với một phương pháp đo kiểm toán được, vì một mục tiêu bạn không bảo vệ được dưới soi xét là khoản nợ, không phải thành tựu.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Chi phí là đường băng, nên một buổi chiều gắn thẻ và một cảnh báo ngân sách có thể mua cho bạn thêm một tháng trước khi gọi vốn lại. Bỏ qua hoàn toàn quy trình FinOps và kế toán carbon; chỉ cần theo dõi hóa đơn, giết tài nguyên nhàn rỗi, và chọn nền tảng được quản lý co về không để bạn trả theo tải thay vì cho năng lực nằm sẵn sàng. Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư, nên hãy tự động hóa lãng phí hiển nhiên và đi tiếp.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia FinOps và ngân sách eo hẹp, vì vậy hãy dựa vào công cụ chi phí mà nhà cung cấp đám mây đã cho thay vì mua nền tảng chuyên dụng. Đặt cảnh báo ngân sách hằng tháng, bật đề xuất chọn kích thước vừa của nhà cung cấp, và ưu tiên dịch vụ được quản lý và serverless gộp hiệu quả vận hành vào giá. Coi bền vững là chọn một khu vực carbon thấp và một mặc định hiệu quả, không phải chương trình báo cáo bạn phải bố trí nhân sự.

**Doanh nghiệp lớn.** Vấn đề là quản trị qua nhiều đội: gắn thẻ nhất quán, phân bổ công bằng chi phí nền tảng dùng chung, chiến lược chiết khấu cam kết do tài chính và kỹ thuật cùng sở hữu, và chi phí cùng carbon được hiển thị như tín hiệu mọi đội thấy. Chuẩn hóa mặc định hiệu quả và một phương pháp đo để hàng trăm quyết định cung cấp độc lập không cộng dồn thành lãng phí, và quản lý chi tiêu đám mây cùng phát thải như một danh mục với mục tiêu, cảnh báo bất thường và báo cáo minh bạch thay vì một mớ tối ưu cục bộ.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Bạn đang chi tiền thuế và thường bị ràng buộc bởi yêu cầu phát thải ròng bằng không, nên bạn phải cho thấy cả sự thận trọng tài khóa lẫn tiến bộ phát thải được kiểm toán, nghĩa là một thước đo carbon trung thực gồm phần cứng hàm chứa thay vì tẩy xanh. Quy tắc cư trú dữ liệu và chủ quyền có thể ràng buộc khu vực bạn dùng được bất kể độ sạch của lưới, và chỉ số hiệu quả và phát thải có thể cần công bố để công chúng soi xét, nên hãy chọn phương pháp đo bạn bảo vệ được dưới kiểm toán.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp giai đoạn hạt giống thấy hóa đơn đám mây tăng gấp đôi trong hai tháng và không nói được vì sao. Một người sáng lập dành một buổi chiều gắn thẻ mọi tài nguyên theo tính năng và bật cảnh báo ngân sách đơn giản. Các thẻ làm lộ một cụm staging bị quên và một cơ sở dữ liệu quá khổ chạy suốt ngày đêm cho một công việc hằng đêm. Tắt cụm đó và chuyển công việc sang chạy ngoài giờ cao điểm theo lịch trên thể hiện nhỏ hơn cắt hóa đơn một phần ba, mua cho đội thêm một tháng đường băng.

**Doanh nghiệp lớn.** Một nhà bán lẻ đa quốc gia với hệ sinh thái đám mây lớn, lan rộng dựng một thực hành FinOps. Nó thực thi gắn thẻ, phân bổ mọi chi phí cho một đội sản phẩm, và hiển thị chi tiêu trên bảng điều khiển mà kỹ sư thấy hằng ngày. Trong một năm nó loại bỏ tài nguyên nhàn rỗi, chọn kích thước vừa cho dịch vụ cung cấp thừa, và mua gói tiết kiệm cho tải nền ổn định, cắt chi tiêu đám mây khoảng một phần tư. Rồi nó lập lịch các công việc lô phân tích hằng đêm chạy ở khu vực carbon thấp hơn và ngoài giờ cao điểm, giảm cả chi phí lẫn phát thải, và báo cáo khoản tiết kiệm carbon trong công bố bền vững hằng năm.

**Chính phủ.** Một cơ quan chính phủ vận hành dịch vụ công dân dưới yêu cầu phát thải ròng bằng không quốc gia phải cho thấy cả sự thận trọng tài khóa với tiền thuế lẫn tiến bộ hướng tới mục tiêu phát thải. Nó chọn kích thước vừa và hợp nhất khối lượng công việc, đặt chính sách lưu giữ dữ liệu chuyển bản ghi hiếm truy cập sang lưu trữ lạnh, tiết kiệm năng lượng, và chọn khu vực đám mây chạy bằng điện tái tạo chiếm tỷ lệ cao. Nó đo cường độ carbon của các dịch vụ chính và công bố chỉ số hiệu quả và phát thải cho trách nhiệm giải trình công. Mặc định hiệu quả và bảng điều khiển tự phục vụ cho hàng chục đội phân phối đưa ra lựa chọn bền vững mà không có nút thắt trung tâm.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức ở đây trực tiếp một cách bất thường. Tối ưu FinOps thường giảm chi tiêu đám mây từ một phần năm đến một phần ba với nỗ lực có kỷ luật, khoản tiết kiệm chảy thẳng xuống lợi nhuận, hoặc tài trợ công việc mới. Giảm carbon cũng ngày càng mang giá trị tài chính, qua việc tránh định giá carbon, đủ điều kiện cho hợp đồng có yêu cầu bền vững, và giảm rủi ro quy định và danh tiếng. Vì hiệu quả hạ cả chi phí lẫn carbon cùng lúc, một khoản đầu tư duy nhất vào khả năng nhìn thấy và chọn kích thước vừa hoàn vốn ở cả hai chiều.

Tổng chi phí sở hữu phải tính chi phí áp dụng: công cụ cho khả năng nhìn thấy chi phí và carbon, nhân sự FinOps hoặc nền tảng để chạy thực hành, và thời gian kỹ thuật để chọn kích thước vừa và thiết kế lại. Những chi phí này khiêm tốn so với khoản tiết kiệm, và chúng co lại khi mặc định hiệu quả được nhúng. Chi phí của việc không áp dụng cộng dồn lặng lẽ: hóa đơn đám mây mất kiểm soát lớn nhanh hơn doanh nghiệp, lãng phí không bao giờ nổi lên vì không ai sở hữu, và phơi nhiễm quy định, nhà đầu tư và danh tiếng về bền vững chồng chất. Để lập luận với ban lãnh đạo, hãy trình bày chi tiêu hiện tại và quỹ đạo tăng, lãng phí ước tính, và khoản tiết kiệm chuẩn từ áp dụng FinOps. Rồi ghép nó với giá trị giảm phát thải và tuân thủ. Đóng khung chi phí và bền vững là cùng một sáng kiến hiệu quả nhìn qua hai thấu kính, để doanh nghiệp không phải chọn giữa tiết kiệm tiền và cắt carbon.

## Phản mẫu và cạm bẫy

- **Không quy chi phí.** Chi tiêu không gắn thẻ, không phân bổ nghĩa là không ai sở hữu lãng phí và không ai tối ưu được nó.
- **Cung cấp đặt rồi quên.** Định cỡ tài nguyên một lần và không bao giờ xem xét lại bảo đảm trôi vào cung cấp thừa.
- **FinOps chỉ của tài chính.** Coi chi phí là mối quan tâm hậu trường thay vì tín hiệu kỹ thuật thất bại, vì kỹ sư đưa ra các quyết định thúc đẩy chi tiêu.
- **[Tẩy xanh](https://en.wikipedia.org/wiki/Greenwashing).** Tuyên bố bền vững mà không đo mời phản ứng quy định và danh tiếng.
- **Hiệu quả đổi lấy độ tin cậy.** Cắt quá quyết liệt đến mức dịch vụ thất bại dưới tải đổi khoản tiết kiệm nhỏ lấy sự cố lớn.
- **Phớt lờ carbon hàm chứa.** Chỉ tập trung vào năng lượng chạy trong khi cung cấp thừa phần cứng nhàn rỗi bỏ sót dấu chân sản xuất.
- **Cổng quan liêu.** Quy trình phê duyệt nặng cho chi tiêu làm chậm phân phối và đẩy các đội đi vòng quản trị.

## Mô hình trưởng thành

**Mức 1, Khởi đầu.** Chi phí đám mây là bất ngờ trên hóa đơn hằng tháng. Không có gắn thẻ, phân bổ hay nhận thức carbon, và việc cung cấp hào phóng và hiếm khi được xem xét lại. Lãng phí vô hình vì không ai sở hữu nó, và bất kỳ dọn dẹp nào xảy ra là phản ứng với cú sốc hóa đơn thay vì thực hành.

**Mức 2, Phát triển.** Khả năng nhìn thấy chi phí cơ bản và gắn thẻ tồn tại, và một số chọn kích thước vừa cùng dọn tài nguyên nhàn rỗi diễn ra, nhưng độ phủ và sự chặt chẽ khác nhau nhiều giữa các đội. Vài nhóm theo dõi chi tiêu và thử khu vực carbon thấp; số khác thì không. Bền vững được thừa nhận nhưng không đo, và thói quen tốt phụ thuộc vào sáng kiến cá nhân thay vì kỳ vọng chung.

**Mức 3, Chuẩn hóa.** Một thực hành FinOps được lập tài liệu và áp dụng toàn tổ chức: gắn thẻ được thực thi, chi phí chung được phân bổ theo phương pháp đã thống nhất, và ngân sách, dự báo và cảnh báo bất thường là chuẩn. Chiết khấu cam kết và chọn kích thước vừa theo một sổ tay xác định, và carbon được đo cho các dịch vụ chính bằng phương pháp được công nhận như đặc tả Cường độ Carbon Phần mềm, với lựa chọn khu vực và lập lịch được cân nhắc nhất quán thay vì từng trường hợp.

**Mức 4, Quản lý.** Chi phí và carbon được đo và kiểm soát theo đường cơ sở. Các đội theo dõi kinh tế đơn vị (chi phí và carbon mỗi yêu cầu, mỗi khách hàng, hay mỗi hồ sơ), mức sử dụng gồm ước tính nhàn rỗi và carbon hàm chứa, độ phủ cam kết so với tải nền, và độ chính xác dự báo, tất cả được báo cáo theo mục tiêu của tổ chức. Bất thường kích hoạt điều tra, hiệu quả và tuân thủ SLO được rà soát cùng nhau để tối ưu không bao giờ lặng lẽ xói mòn độ tin cậy, và quyết định tiếp tục hay dừng về cung cấp được đưa ra dựa trên dữ liệu này thay vì trực giác.

**Mức 5, Điều phối.** Chi phí và carbon là tín hiệu kỹ thuật liên tục, có chủ được nối vào thực hành hằng ngày. Mặc định hiệu quả, chọn kích thước vừa tự động và lập lịch nhận biết carbon là chuẩn mực, và tổ chức liên tục cân bằng lại hệ sinh thái khi nhu cầu, giá và cường độ lưới dịch chuyển. Chi phí, hiệu năng và độ tin cậy được đánh đổi có chủ đích qua SLO, chỉ số bền vững nuôi báo cáo công khai và nhà đầu tư bằng phương pháp kiểm toán được, và thực hành thích ứng khi doanh nghiệp, thị trường và quy định tiến hóa.

## Ý tưởng để thảo luận

- Ai nên sở hữu chi phí đám mây trong tổ chức của bạn: tài chính, một đội FinOps trung tâm, hay các đội kỹ thuật cung cấp tài nguyên?
- Làm sao bạn phân bổ công bằng chi phí nền tảng dùng chung qua nhiều đội tiêu thụ?
- Cân bằng đúng giữa tiết kiệm chi phí và độ tin cậy hay hiệu năng bạn có thể hy sinh để có chúng nằm ở đâu?
- Bạn sẽ đo dấu chân carbon của dịch vụ thế nào, và bạn tin dữ liệu sẵn có đến đâu?
- Khối lượng công việc nào của bạn đủ linh hoạt cho lập lịch nhận biết carbon theo thời gian hay khu vực?
- Làm sao bạn đặt mục tiêu hiệu quả và bền vững khuyến khích các đội mà không mời gọi cung cấp thiếu rủi ro?

## Những điểm cần ghi nhớ

- Đám mây biến chi phí và carbon thành mối quan tâm kỹ thuật; khả năng nhìn thấy và quyền sở hữu là nền móng để kiểm soát cả hai.
- FinOps hoạt động trong ba giai đoạn: thông tin (nhìn thấy), tối ưu (chọn kích thước vừa và chiết khấu), và vận hành (nhúng vào thực hành).
- Phần mềm hiệu quả thường tiết kiệm tiền và carbon cùng nhau, nên hãy coi chúng là một sáng kiến với hai thấu kính.
- Giảm carbon qua hiệu quả năng lượng, mức sử dụng phần cứng cao hơn, và lập lịch nhận biết carbon theo thời gian và địa điểm.
- Kiến trúc và chọn kích thước vừa chi phối chi phí và carbon dài hạn; hãy thiết kế cho tính đàn hồi và co về không.
- Cân bằng chi phí, hiệu năng và độ tin cậy có chủ đích bằng SLO, và quản trị bằng lan can thay vì cổng.

## Tài liệu tham khảo và đọc thêm

- J.R. Storment, Mike Fuller, *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*
- FinOps Foundation, tài liệu *FinOps Framework*
- Green Software Foundation, *Principles of Green Software Engineering* và *Software Carbon Intensity (SCI) Specification*
- Anne Currie, Sarah Hsu, Sara Bergman, *Building Green Software*
- Adrian Cockcroft, các bài viết về hiệu quả và bền vững đám mây
- The Shift Project, *Lean ICT: Towards Digital Sobriety*
