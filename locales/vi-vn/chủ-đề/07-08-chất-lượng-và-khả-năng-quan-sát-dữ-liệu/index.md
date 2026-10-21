# 7.8 Chất lượng và khả năng quan sát dữ liệu

## Tổng quan và động lực

[Chất lượng dữ liệu](https://en.wikipedia.org/wiki/Data_quality) là mức độ phù hợp sử dụng: mức dữ liệu phục vụ các quyết định, sản phẩm và báo cáo phụ thuộc vào nó. Một tập dữ liệu không tốt hay xấu một cách trừu tượng. Nó đủ tốt cho một mục đích, hoặc không. Một địa chỉ khách hàng ổn cho một phép đếm tiếp thị có thể không phù hợp cho một thông báo pháp lý. Cách đóng khung đó quan trọng, vì nó chuyển cuộc trò chuyện từ "dữ liệu của chúng ta có hoàn hảo không" (không bao giờ) sang "dữ liệu của chúng ta có phù hợp với việc chúng ta sắp làm với nó không" (trả lời được, và kiểm thử được). Các chiều kinh điển là độ chính xác, độ đầy đủ, tính nhất quán, tính kịp thời, tính hợp lệ và tính duy nhất, và hầu hết vấn đề thực quy về một trong số chúng.

Đây là sự thật khó chịu với các đội lớn: dữ liệu xấu tệ hơn không có dữ liệu. Khi bạn không có dữ liệu, bạn biết điều đó, và bạn tiến hành với sự thận trọng thích hợp. Khi bạn có dữ liệu sai trông đúng, bạn hành động trên nó với sự tự tin giả. Dữ liệu xấu làm hỏng thầm lặng. Nó chảy vào một bảng điều khiển mà một giám đốc tin, vào một mô hình [học máy](https://en.wikipedia.org/wiki/Machine_learning) huấn luyện trên nó và mã hóa các lỗi của nó, và vào các quyết định không ai nghĩ đến chất vấn vì con số ở ngay đó trên màn hình. Thiệt hại phân tán và bị trì hoãn, đó chính là lý do nó đắt. Đến khi ai đó nhận ra, con số sai đã được trích dẫn trong một bộ slide hội đồng, hồ sơ quy định, hay thống kê công khai.

Khả năng quan sát dữ liệu là kỷ luật bắt điều này trước khi người tiêu dùng của bạn làm. Nó là song song trực tiếp của khả năng quan sát phần mềm và đo từ xa (chương 9.2): cùng bản năng bảo bạn giám sát độ trễ yêu cầu và tỷ lệ lỗi bảo bạn giám sát độ mới, khối lượng, lược đồ và phân phối của dữ liệu. Chương này xây trên chiến lược và quản trị dữ liệu (chương 7.1) và kỹ thuật dữ liệu (chương 7.2), và nó nuôi mô hình hóa dữ liệu và lớp ngữ nghĩa (chương 7.7) cùng AI có trách nhiệm và đáng tin cậy (chương 6.5). Với doanh nghiệp đối chiếu nhiều hệ thống nguồn và chính phủ công bố thống kê theo luật, coi độ tin cậy dữ liệu là bài toán kỹ thuật có chủ sở hữu và mức dịch vụ là sự khác biệt giữa lòng tin và một lần đính chính rất công khai.

## Các nguyên tắc chính

- Chất lượng dữ liệu là mức phù hợp sử dụng, không phải sự hoàn hảo; hãy xác định nó theo mục đích.
- Dữ liệu xấu tệ hơn không có dữ liệu, vì nó làm hỏng quyết định thầm lặng.
- Kiểm thử dữ liệu như bạn kiểm thử mã: khẳng định, kỳ vọng và kiểm tra lược đồ trong đường ống.
- Hợp đồng giữa nhà sản xuất và người tiêu dùng làm kỳ vọng tường minh và thực thi được.
- Quan sát độ mới, khối lượng, lược đồ và phân phối, giống như bạn quan sát dịch vụ.
- Dòng gốc biến "có gì đó sai" thành "đây là cái đã hỏng và nó ảnh hưởng đến gì."
- Coi sự cố dữ liệu như sự cố sản xuất, với quyền sở hữu, mức nghiêm trọng và mức dịch vụ.
- Phát hiện vấn đề nơi chúng đi vào, không phải ba lớp hạ nguồn trong một bảng điều khiển.

## Khuyến nghị

### Xác định chất lượng theo chiều, và đo nó

Mục tiêu chất lượng mơ hồ tạo ra kết quả mơ hồ. Hãy chia chất lượng thành các chiều đo được và gắn kiểm tra cụ thể cho mỗi chiều. Độ chính xác hỏi liệu giá trị có phản ánh thực tế (doanh thu được ghi này có khớp sổ cái nguồn không). Độ đầy đủ hỏi liệu các bản ghi và trường kỳ vọng có hiện diện (có ngày nào bị thiếu không, các cột bắt buộc có null không). Tính nhất quán hỏi liệu cùng một sự kiện có thống nhất qua các hệ thống (số khách hàng ở tài chính có khớp số ở kho dữ liệu không). Tính kịp thời hỏi liệu dữ liệu có đến đủ sớm để hữu ích (dữ liệu hôm qua có sẵn sàng trước báo cáo buổi sáng không). Tính hợp lệ hỏi liệu giá trị có tuân thủ quy tắc và định dạng (mọi mã tiền tệ có thật không, ngày có trong khoảng không). Tính duy nhất hỏi liệu thực thể chỉ xuất hiện một lần (có đơn hàng trùng làm phình tổng không). Hãy chọn các chiều quan trọng cho từng tập dữ liệu, đặt ngưỡng, và theo dõi chúng theo thời gian. Chất lượng bạn không đo là chất lượng bạn đang đoán.

### Kiểm thử đường ống bằng khẳng định và kỳ vọng

Dữ liệu xứng đáng được kiểm thử chặt chẽ như mã ứng dụng. Hãy dùng [xác thực dữ liệu](https://en.wikipedia.org/wiki/Data_validation) ở mọi giai đoạn: kiểm thử dựa trên khẳng định làm đường ống thất bại khi một bất biến bị vi phạm, và kiểm thử dựa trên kỳ vọng khai báo "bình thường" trông thế nào với một bảng và gắn cờ độ lệch. Khẳng định rằng khóa chính là duy nhất và không null, khóa ngoại giải quyết được, cột phân loại chỉ chứa giá trị được chấp nhận, cột số nằm trong khoảng hợp lý, và số hàng rơi vào một dải kỳ vọng. Thêm kiểm tra lược đồ thất bại to khi một cột được thêm, bỏ, đổi tên hay đổi kiểu ở thượng nguồn. Chạy các kiểm tra này trong tích hợp liên tục để một phép biến đổi tồi bị bắt trước khi hợp nhất, và chạy lại trong môi trường sản xuất trên dữ liệu trực tiếp để một nguồn tồi bị bắt trước khi đến người tiêu dùng. Mục tiêu là thất bại sớm và to, vì một đường ống hỏng an toàn hơn một đường ống sai thầm lặng.

### Thiết lập hợp đồng dữ liệu giữa nhà sản xuất và người tiêu dùng

Hầu hết sự cố chất lượng dữ liệu bắt đầu ở thượng nguồn, khi một đội sản xuất đổi lược đồ, ý nghĩa ngữ nghĩa hay quy ước giá trị mà không biết ai phụ thuộc. Một [hợp đồng dữ liệu](https://en.wikipedia.org/wiki/Data_contract) sửa điều này bằng cách làm giao diện tường minh: lược đồ, ngữ nghĩa của từng trường, giá trị được phép, bảo đảm độ mới, và quy trình thực hiện thay đổi. Nhà sản xuất cam kết với hợp đồng, người tiêu dùng xây dựng dựa trên nó, và một thay đổi phá vỡ đòi đánh phiên bản và thông báo thay vì một bất ngờ thầm lặng vào thứ Hai. Hãy thực thi hợp đồng một cách máy móc nơi bạn có thể, bằng cách xác thực dữ liệu đến theo hợp đồng ở ranh giới và từ chối hoặc cách ly vi phạm. Hợp đồng biến một phụ thuộc ngầm, mong manh thành một phụ thuộc tường minh, được thương lượng. Chúng cũng làm quyền sở hữu hiển thị, là một nửa trận chiến ở quy mô.

### Giám sát bốn tín hiệu của khả năng quan sát dữ liệu

Khả năng quan sát dữ liệu theo dõi bốn tín hiệu, song song trực tiếp với cách bạn theo dõi một dịch vụ đang chạy (chương 9.2). Độ mới: dữ liệu có gần đây như nó nên có, hay đường ống đã đình trệ. Khối lượng: số hàng có trong khoảng kỳ vọng, hay một bảng đến rỗng một nửa hoặc tải đôi. Lược đồ: cấu trúc có đổi bất ngờ không. Phân phối: bản thân các giá trị có trôi không, để một cột từng 2 phần trăm null đột nhiên thành 40 phần trăm null, hoặc một trung bình dịch chuyển theo cách báo hiệu lỗi thượng nguồn. Hãy gắn công cụ đo các tín hiệu này trên các bảng quan trọng, học các mẫu bình thường của chúng, và cảnh báo khi vi phạm. Đây là cách bạn thay "một giám đốc nhận ra bảng điều khiển trông sai" bằng "đội sở hữu bị gọi ngay tại điểm thất bại." Bộ phát hiện tệ nhất có thể của một vấn đề dữ liệu là một con người hạ nguồn tin con số.

### Thêm phát hiện bất thường, nhưng điều chỉnh để tránh mệt mỏi vì cảnh báo

Ngưỡng tĩnh bắt các thất bại hiển nhiên. Với trôi tinh vi hơn, hãy thêm vào [phát hiện bất thường](https://en.wikipedia.org/wiki/Anomaly_detection) học mẫu theo mùa bình thường của từng chỉ số và gắn cờ độ lệch bất thường về thống kê, để bạn bắt một rò rỉ chậm trước khi nó thành lũ. Hãy kỷ luật về điều này. Cảnh báo bất thường ồn ào huấn luyện mọi người phớt lờ cảnh báo, còn tệ hơn không có cảnh báo. Hãy bắt đầu với các bảng giá trị cao nhất, chỉ cảnh báo những thứ một con người nên hành động, chuyển mỗi cảnh báo đến một chủ sở hữu có tên, và điều chỉnh không thương tiếc. Một cảnh báo không ai hành động là một lỗi trong giám sát của bạn, không phải một tính năng.

### Theo dõi dòng gốc cho phân tích tác động và nguyên nhân gốc

Khi có gì đó hỏng, hai câu hỏi quan trọng ngay lập tức: cái gì gây ra, và nó ảnh hưởng đến gì. [Dòng gốc dữ liệu](https://en.wikipedia.org/wiki/Data_lineage) trả lời cả hai bằng cách ánh xạ dữ liệu chảy từ nguồn qua mọi phép biến đổi đến mọi bảng, bảng điều khiển và mô hình hạ nguồn. Với nguyên nhân gốc, bạn truy một con số xấu ngược thượng nguồn đến phép biến đổi hay nguồn đã đưa nó vào. Với phân tích tác động, bạn truy xuôi để thấy mọi người tiêu dùng bị ảnh hưởng bởi một lần tải xấu, để bạn thông báo cho họ và cách ly thiệt hại trước khi nó lan. Hãy nắm bắt dòng gốc tự động từ các công cụ biến đổi và điều phối của bạn thay vì duy trì sơ đồ bằng tay, vì một sơ đồ vẽ tay sai ngay ngày sau khi bạn vẽ. Trong các doanh nghiệp có nhiều nguồn, hãy công bố dòng gốc vào danh mục dữ liệu để bất kỳ người tiêu dùng nào cũng thấy một trường đến từ đâu và tin tương ứng.

### Coi sự cố dữ liệu như sự cố sản xuất

Các thực hành giữ dịch vụ đáng tin áp dụng trực tiếp cho dữ liệu. Giao cho mọi tập dữ liệu quan trọng một chủ sở hữu. Xác định các mức nghiêm trọng cho "thời gian chết dữ liệu," những khoảng khi dữ liệu thiếu, sai hay muộn. Đặt mức dịch vụ: mục tiêu độ mới, ngân sách lỗi chấp nhận được, và thời gian mục tiêu để phát hiện và giải quyết. Đặt phiên trực dữ liệu sau các đường ống trọng yếu nhất, viết sổ tay vận hành, và chạy rút kinh nghiệm không đổ lỗi sau sự cố để cùng thất bại không tái diễn. Khi một bảng thanh toán bị muộn hoặc một chỉ số công khai sai, đó là một sự cố, và nó xứng đáng sự nghiêm túc như một lần ngừng hoạt động. Đây là sự chuyển dịch văn hóa làm mọi công cụ sinh lời.

### Lập hồ sơ và đối chiếu liên tục

Lập hồ sơ nghĩa là thường xuyên xem xét hình dạng của dữ liệu: phân phối giá trị, tỷ lệ null, số phần tử khác nhau, nhỏ nhất và lớn nhất, và mẫu định dạng. Nó làm lộ vấn đề bạn chưa nghĩ đến để khẳng định, và cho bạn biết "bình thường" trông thế nào để đặt kỳ vọng tốt. Đối chiếu nghĩa là kiểm tra rằng các nguồn độc lập thống nhất: tổng ở kho dữ liệu có khớp hệ thống nguồn ghi nhận không, tổng các phần có bằng tổng thể không. Hãy tự động hóa đối chiếu giữa các hệ thống trọng yếu và cảnh báo khi phân kỳ, vì một đứt gãy đối chiếu thường là tín hiệu sớm nhất và rõ nhất rằng có gì đó thượng nguồn đã sai.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Kiểm thử khẳng định (thất bại cứng) | Chặn dữ liệu xấu tận gốc, bất biến rõ ràng | Có thể chặn đường ống vì vấn đề nhỏ | Khóa trọng yếu, toàn vẹn tham chiếu |
| Kiểm thử kỳ vọng (gắn cờ mềm) | Bắt trôi, ít giòn hơn | Cần điều chỉnh, có thể bị phớt lờ | Phân phối, dải khối lượng |
| Hợp đồng dữ liệu | Ngăn bất ngờ thượng nguồn, quyền sở hữu rõ ràng | Chi phí phối hợp và quản trị | Ranh giới nhà sản xuất hoặc người tiêu dùng xuyên đội |
| Phát hiện bất thường | Bắt trôi tinh vi, không lường trước | Mệt mỏi cảnh báo, dương tính giả | Bảng giá trị cao, chỉ số theo mùa |
| Kiểm tra tại chỗ thủ công | Rẻ để bắt đầu, không cần công cụ | Không mở rộng, bỏ sót lỗi thầm lặng | Chỉ giai đoạn rất sớm |
| Nền tảng quan sát đầy đủ | Phủ rộng, dòng gốc, cảnh báo | Chi phí, thiết lập, thêm một hệ thống phải chạy | Nhiều nguồn, báo cáo chịu quy định |

Căng thẳng trung tâm là độ phủ so với nhiễu. Không gắn công cụ gì thì vấn đề đến người tiêu dùng của bạn trước, phá hủy lòng tin. Gắn công cụ mọi thứ với cảnh báo nhạy cò thì bạn nhấn chìm đội trong dương tính giả cho đến khi họ tắt tiếng kênh, cũng để vấn đề đến người tiêu dùng. Hãy giải quyết bằng cách xếp hạng dữ liệu theo bán kính ảnh hưởng. Các bảng nuôi chỉ số hội đồng, sản phẩm hướng khách hàng, báo cáo quy định và mô hình học máy nhận đầy đủ sự đối xử: hợp đồng, khẳng định cứng, khả năng quan sát và quyền sở hữu trực. Cái đuôi dài các bảng khám phá nhận lập hồ sơ nhẹ. Hãy tiêu ngân sách độ tin cậy nơi dữ liệu sai gây đau nhất, và tiết kiệm có chủ đích ở mọi nơi khác.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi dữ liệu xấu đến môi trường sản xuất, ai biết đầu tiên, và bằng cách nào?** Đây là câu hỏi tiết lộ nhiều nhất về độ tin cậy dữ liệu của bạn, vì câu trả lời trung thực thường là "một người tiêu dùng, tình cờ." Nếu một nhà phân tích, giám đốc hay khách hàng là hệ thống phát hiện của bạn, thời gian trung bình để phát hiện đo bằng ngày và uy tín của bạn chịu đòn mỗi lần. Lựa chọn thay thế là gắn công cụ đo gọi đội sở hữu tại điểm thất bại, trước khi con số xấu lan ra. Hãy mang con số thật: trong mười sự cố dữ liệu gần nhất, bao nhiêu cái được giám sát bắt so với được một con người hạ nguồn báo cáo, và mỗi cái nằm không bị phát hiện bao lâu. Câu trả lời cho bạn biết bạn có khả năng quan sát hay chỉ có hy vọng, và nó nên trực tiếp thúc đẩy nơi bạn đầu tư vào kiểm tra độ mới, khối lượng, lược đồ và phân phối trước.

2. **Tập dữ liệu nào có chủ sở hữu, hợp đồng và mức dịch vụ, và cái nào là mồ côi?** Ở quy mô lớn, hầu hết thất bại chất lượng dữ liệu truy về một giao diện không chủ sở hữu: một đội sản xuất đổi gì đó mà không biết ai phụ thuộc, vì không hợp đồng nào nói vậy. Quyền sở hữu là nền móng làm hợp đồng, đường chuyển cảnh báo và ứng phó sự cố khả thi, và tập dữ liệu mồ côi là nơi hỏng thầm lặng sống. Hãy đi qua các bảng quan trọng nhất của bạn và hỏi, với mỗi cái, ai chịu trách nhiệm, nhà sản xuất đã cam kết gì, và người tiêu dùng được hứa độ mới cùng độ chính xác nào. Hãy mang dòng gốc của bạn: các bảng có bán kính ảnh hưởng hạ nguồn lớn nhất là những cái cần điều này nhất và thường là những cái thiếu nó. Khoảng cách giữa "quan trọng" và "có chủ sở hữu" là danh sách ưu tiên của bạn cho quý tới.

3. **Chi phí thực của một sự cố chất lượng dữ liệu với chúng ta là bao nhiêu, và chúng ta có đối xử với nó tương ứng không?** Các đội đầu tư thiếu vào chất lượng dữ liệu vì chi phí của dữ liệu xấu phân tán và bị trì hoãn, nên không bao giờ hiện thành dòng khoản mục, trong khi chi phí xây công cụ chất lượng cụ thể và tức thì. Hãy đóng khung lại bằng cách định giá một sự cố thật đầu-đến-cuối: quyết định sai, việc làm lại, giờ kỹ sư tiêu để truy nguyên nhân gốc mà không có dòng gốc, lòng tin bị xói mòn khiến mọi người lặng lẽ xây tập dữ liệu bóng của riêng họ, và, trong bối cảnh chịu quy định hay hướng công chúng, thông báo đính chính và thiệt hại danh tiếng của nó. Hãy mang một ví dụ cụ thể từ năm qua và cộng lại một cách trung thực. Nếu một thất bại thầm lặng duy nhất trong đường ống thanh toán hay thống kê công khai có thể tốn hơn một năm công cụ quan sát, lập luận kinh doanh tự thành, và cuộc trò chuyện chuyển từ có đầu tư không sang đầu tư ở đâu.

4. **Chúng ta đã xếp hạng tập dữ liệu theo bán kính ảnh hưởng chưa, và khoản đầu tư giám sát của chúng ta có thực sự theo thứ hạng đó không?** Kiểu thất bại trung tâm ở quy mô là tiêu công sức độ tin cậy đồng đều, nên bảng khám phá không ai tin nhận cùng sự chú ý như bảng nuôi chỉ số hội đồng, trong khi một cảnh báo nhạy cò trên bảng giá trị thấp huấn luyện mọi người tắt tiếng kênh cũng mang trang gọi trọng yếu. Bạn không thể gắn công cụ mọi thứ mà không chìm trong nhiễu, và không thể gắn công cụ không gì mà không để vấn đề đến người tiêu dùng trước, nên quyết định thực là nơi sự đối xử đầy đủ (hợp đồng, khẳng định cứng, khả năng quan sát và quyền sở hữu trực) đi tới và nơi lập hồ sơ nhẹ là đủ. Hãy mang bản kiểm kê bảng của bạn được gắn thẻ theo cái gì phụ thuộc vào chúng: chỉ số hội đồng, sản phẩm hướng khách hàng, báo cáo quy định và mô hình học máy, rồi so sánh thứ hạng đó với nơi các kiểm tra và cảnh báo của bạn thực sự đặt hôm nay. Với một doanh nghiệp đối chiếu nhiều nguồn hay một chính phủ công bố con số theo luật, các bảng có phơi nhiễm pháp lý hay công khai thuộc về đầu danh sách, và mọi khoảng cách giữa "sẽ đau nhất nếu sai" và "được giám sát nhiều nhất" là lỗi ưu tiên cần sửa ngay.

5. **Mô hình học máy và phân tích nào đang quyết định trên dữ liệu chúng ta chưa bao giờ xác thực, và chúng có thể đang lặng lẽ mã hóa những lỗi nào?** Một bảng điều khiển cho một con người thấy con số sai, người đó có thể chất vấn, nhưng một mô hình huấn luyện trên đặc trưng sai và mã hóa các lỗi đó vào mọi dự đoán nó đưa ra, ở quy mô và sự mờ đục khiến thiệt hại khó phát hiện hay hoàn tác hơn nhiều. Áp lực đối lập là tốc độ: các đội khoa học dữ liệu muốn di chuyển nhanh trên đặc trưng mới, và thêm xác thực, hợp đồng và bảo đảm độ mới cho mọi nguồn cấp cảm thấy như ma sát cho đến khi một mô hình lặng lẽ suy giảm vì một cột thượng nguồn trôi. Hãy mang bản kiểm kê các mô hình và phân tích sản xuất, các tập dữ liệu mỗi cái tiêu thụ, và một dấu trung thực về nguồn cấp nào có kiểm thử, hợp đồng và khả năng quan sát so với nguồn cấp nào không được bảo vệ. Trong bối cảnh doanh nghiệp hoặc chính phủ nơi một mô hình ảnh hưởng đến quyết định tín dụng, trợ cấp hay thực thi, dữ liệu huấn luyện chưa xác thực trở thành khoản nợ kiểm toán và công bằng cộng thêm vào rủi ro chất lượng, nên câu hỏi nguồn cấp nào chặn cổng việc phát hành mô hình nên có chủ sở hữu và câu trả lời có tài liệu (chương 6.5).

6. **Khi một lỗi chất lượng nổi lên nhiều tuần sau đó, chúng ta thực sự xử lý lại và đối chiếu được không, hay đã bỏ những gì chúng ta cần?** Nhiều thất bại chất lượng vô hình lúc tải và chỉ trở nên rõ sau đó, khi một đứt gãy đối chiếu hay một xu hướng đáng ngờ khiến ai đó nhìn vào, và đến lúc đó khả năng sửa gọn gàng phụ thuộc vào các lựa chọn bạn đã đưa ra sớm hơn nhiều: liệu bạn có giữ bản ghi thô bất biến, liệu các nguồn độc lập có đối chiếu được, và liệu dòng gốc có cho phép bạn truy con số xấu về nguồn gốc của nó. Căng thẳng là chi phí và sự đơn giản so với khả năng tái lập, vì giữ dữ liệu thô và chạy đối chiếu liên tục giữa các hệ thống không miễn phí, và dễ bị cám dỗ xóa đầu vào thô khi các bảng đã biến đổi trông đúng. Hãy mang chính sách lưu giữ và bất biến của bạn cho dữ liệu thô, danh sách các cặp hệ thống trọng yếu bạn đối chiếu tự động, và một ví dụ thật về một lỗi bạn đã hoặc không thể xử lý lại để thoát. Với một cơ quan chính phủ chịu nghĩa vụ theo luật truy vết bất kỳ con số được công bố nào về bản ghi nguồn, hay một doanh nghiệp đối mặt điều chỉnh lại theo quy định, dữ liệu thô bất biến và đối chiếu tự động không phải vệ sinh tùy chọn mà là cơ chế làm một lần đính chính bảo vệ được.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ và lòng tin quan trọng hơn độ phủ. Hãy đặt một nhúm kiểm thử nhẹ trong công cụ biến đổi của bạn (tính duy nhất và không null trên khóa, giá trị chấp nhận được trên các cột mang ý nghĩa, một dải số hàng cho mỗi nguồn), và chỉ thêm giám sát độ mới và khối lượng trên vài bảng nuôi chỉ số công ty. Chuyển mọi cảnh báo đến một kênh một kỹ sư sở hữu, và chống lại việc mua nền tảng quan sát trước khi bạn có bảng hay đội để biện minh. Mục tiêu là nhận ra một trường gắn nhãn sai trước khi nó thổi phồng một con số những người sáng lập trích dẫn, không phải gắn công cụ đo mọi thứ.

**Doanh nghiệp nhỏ.** Không có kỹ sư dữ liệu và ngân sách eo hẹp, hãy dựa vào các tính năng chất lượng dựng sẵn trong kho dữ liệu, công cụ BI hay nền tảng SaaS bạn trả tiền thay vì dựng một ngăn xếp riêng. Tập trung công sức vào nhúm con số thực sự thúc đẩy quyết định (doanh thu, đường ống bán hàng, tồn kho), kiểm tra tính hợp lý chúng với một nguồn độc lập theo nhịp đều đặn, và coi cảnh báo độ mới và lược đồ của nhà cung cấp là đủ tốt khi chúng tồn tại. Mua chất lượng nhúng trong công cụ bạn đã chạy thắng xây một đường ống bạn không có ai bảo trì.

**Doanh nghiệp lớn.** Vấn đề là độ tin cậy qua nhiều đội và hàng nghìn bảng, vì vậy hãy chuẩn hóa giao diện: hợp đồng dữ liệu ở mọi ranh giới nhà sản xuất, một nền tảng quan sát theo dõi độ mới, khối lượng, lược đồ và phân phối, và dòng gốc công bố vào danh mục cho phân tích tác động. Xếp hạng tập dữ liệu theo bán kính ảnh hưởng, đặt phát hiện bất thường và quyền sở hữu trực lên các cái giá trị cao, và đưa sự cố dữ liệu qua cùng quy trình mức nghiêm trọng và rút kinh nghiệm như ngừng hoạt động dịch vụ. Mức dịch vụ trên các đường ống nuôi báo cáo quy định và bảng điều khiển điều hành biến độ tin cậy dữ liệu từ khát vọng thành cam kết được đo, được quản trị.

**Chính phủ.** Độ chính xác theo luật và trách nhiệm giải trình công đặt ra thanh chuẩn: hạ cánh bản ghi khảo sát và hành chính thô bất biến, biến đổi chúng trong các giai đoạn phân lớp, đã kiểm thử, và đối chiếu với tổng nguồn ở mỗi bước. Giữ dòng gốc đầy đủ để bất kỳ con số được công bố nào có thể truy vết về bản ghi nguồn để kiểm toán, và chặn cổng mọi bản phát hành sau xác thực về tính hợp lệ, độ đầy đủ và tính nhất quán so với các kỳ trước. Mua sắm công cụ nên đòi sự minh bạch và khả năng di chuyển dữ liệu, và một thống kê công khai sai phải được xử lý như sự cố nghiêm trọng, với sự trang trọng mà lòng tin công chúng vào số liệu chính thức đòi hỏi.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty hai mươi người chạy hoạt động tiếp cận thị trường trên một kho dữ liệu được nuôi bằng sự kiện sản phẩm và một nhà cung cấp thanh toán. Từ sớm, một trường tiền tệ gắn nhãn sai đã lặng lẽ thổi phồng doanh thu báo cáo trong hai tuần trước khi ai nhận ra, làm lung lay lòng tin của đội vào mọi bảng điều khiển. Họ phản ứng bằng một bộ kiểm thử nhẹ trong công cụ biến đổi: tính duy nhất và không null trên khóa, kiểm tra giá trị chấp nhận được trên cột tiền tệ và trạng thái, và một dải số hàng cho mỗi nguồn. Họ thêm giám sát độ mới và khối lượng cơ bản trên vài bảng nuôi chỉ số công ty, chuyển đến một kênh Slack duy nhất một kỹ sư sở hữu. Nó khiêm tốn, nhưng bắt được những thất bại quan trọng, và những người sáng lập lại tin các con số.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia đối chiếu dữ liệu khách hàng và giao dịch qua hàng chục hệ thống nguồn vào một kho dữ liệu được quản trị nuôi báo cáo quy định, mô hình rủi ro và bảng điều khiển điều hành. Nó chạy hợp đồng dữ liệu ở mọi ranh giới nhà sản xuất, nên một thay đổi lược đồ thượng nguồn được đánh phiên bản và thương lượng thay vì bất ngờ áp lên người tiêu dùng. Một nền tảng quan sát giám sát độ mới, khối lượng, lược đồ và phân phối qua hàng nghìn bảng, với phát hiện bất thường trên các bảng giá trị cao và dòng gốc công bố vào danh mục dữ liệu cho phân tích tác động. Sự cố dữ liệu theo cùng quy trình mức nghiêm trọng và trực như ngừng hoạt động dịch vụ, với mức dịch vụ trên các đường ống nuôi hồ sơ quy định. Khi một hệ thống nguồn trôi, đội sở hữu bị gọi và các báo cáo hạ nguồn bị ảnh hưởng được biết trong vài phút, không phải do cơ quan quản lý phát hiện.

**Chính phủ.** Một cơ quan thống kê quốc gia công bố các chỉ số kinh tế mà thị trường, nhà hoạch định chính sách và công chúng coi là có thẩm quyền, nên độ chính xác là nghĩa vụ theo luật và mọi con số được công bố phải kiểm toán được. Đường ống của nó hạ cánh bản ghi khảo sát và hành chính thô bất biến, rồi biến đổi chúng trong các giai đoạn phân lớp, đã kiểm thử với đối chiếu tổng nguồn ở mỗi bước. Dòng gốc đầy đủ cho phép nhà phân tích truy vết bất kỳ con số được công bố nào về bản ghi nguồn, vừa là công cụ chất lượng vừa là yêu cầu pháp lý. Trước khi phát hành, các con số qua cổng xác thực về tính hợp lệ, độ đầy đủ và tính nhất quán so với các kỳ trước, và mọi bất thường được điều tra và lập tài liệu thay vì công bố. Một thống kê công khai sai là sự cố nghiêm trọng, nên cơ quan coi thời gian chết dữ liệu với sự trang trọng mà lòng tin công chúng đòi hỏi.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của chất lượng dữ liệu và khả năng quan sát đến từ lòng tin được giữ, sự cố được rút ngắn, và quyết định tồi được tránh. Dữ liệu đáng tin là nền tảng làm mọi khoản đầu tư hạ nguồn vào phân tích, trí tuệ kinh doanh và AI thực sự sinh lời, vì một mô hình hay bảng điều khiển chỉ tốt như dữ liệu bên dưới. Khi kiểm tra chất lượng bắt một lần tải xấu ở ranh giới, bạn tránh được chi phí lớn hơn nhiều của việc một con số sai đến một quyết định, một khách hàng hay một hồ sơ. Dòng gốc thu gọn điều tra nguyên nhân gốc từ nhiều ngày truy vết thủ công xuống vài phút, là thời gian kỹ thuật thu hồi thuần túy. Khả năng quan sát thu nhỏ thời gian trung bình để phát hiện từ "khi một người tiêu dùng phàn nàn" xuống "khi đường ống thất bại," là nơi phần lớn thiệt hại lòng tin được tránh.

Tổng chi phí sở hữu gồm công cụ cho kiểm thử, khả năng quan sát và lập danh mục, cộng thời gian kỹ thuật để gắn công cụ đo đường ống và công việc tổ chức giao chủ sở hữu và viết hợp đồng. Điều này là thật, nhưng hãy cân nhắc nó so với chi phí của việc không làm: hỏng thầm lặng do giám đốc phát hiện, mô hình học máy huấn luyện trên đặc trưng xấu mã hóa lỗi ở quy mô, nhà phân tích lặng lẽ xây lại tập dữ liệu bóng vì họ không còn tin tập chính thức, và, trong bối cảnh chịu quy định hay công khai, thông báo đính chính làm tổn hại uy tín nhiều năm. Với ban lãnh đạo, hãy đóng khung chất lượng dữ liệu là bảo hiểm cho mọi quyết định dựa trên dữ liệu mà tổ chức đưa ra. Phí bảo hiểm khiêm tốn và khả đoán. Khoản lỗ không được bảo hiểm, một con số sai gây chú ý, thì không.

## Phản mẫu và cạm bẫy

- Coi chất lượng dữ liệu là dự án dọn dẹp một lần thay vì thực hành kỹ thuật liên tục.
- Phát hiện thất bại từ người tiêu dùng hạ nguồn thay vì từ giám sát tại điểm thất bại.
- Không có quyền sở hữu tập dữ liệu, nên không ai chịu trách nhiệm khi có gì hỏng và không ai bị gọi.
- Nhà sản xuất đổi lược đồ hay ngữ nghĩa không có hợp đồng, lặng lẽ làm hỏng mọi người tiêu dùng.
- Cảnh báo bất thường ồn đến mức đội tắt tiếng kênh và bỏ lỡ sự cố thật.
- Đưa dữ liệu chưa xác thực thẳng vào mô hình học máy, mã hóa lỗi ở quy mô (chương 6.5).
- Duy trì dòng gốc như sơ đồ vẽ tay sai ngay ngày sau khi vẽ.
- Đuổi theo dữ liệu hoàn hảo ở mọi nơi thay vì chất lượng phù hợp sử dụng trên các bảng quan trọng.
- Xóa dữ liệu thô, nên không xử lý lại hay đối chiếu được khi một lỗi chất lượng nổi lên sau đó.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Chất lượng không phải việc của ai. Vấn đề được người tiêu dùng tìm thấy, thường sau khi con số sai đến báo cáo. Không kiểm thử, không giám sát, không quyền sở hữu. Sửa chữa là chữa cháy thủ công, và cùng thất bại tái diễn.
- **Mức 2, Phát triển:** Một số đội thêm kiểm thử cơ bản trên bảng trọng yếu (khóa, null, giá trị chấp nhận được) và một ít giám sát độ mới và khối lượng trên tập dữ liệu họ quan tâm nhất. Thực hành hiệu quả nơi chúng tồn tại, nhưng độ phủ và sự chặt chẽ khác nhau theo đội, không gì được chuẩn hóa, và sự cố vẫn được xử lý phản ứng.
- **Mức 3, Chuẩn hóa:** Các chiều chất lượng được xác định với ngưỡng, và cùng kỳ vọng áp dụng qua các đội thay vì phụ thuộc ai xây đường ống. Hợp đồng dữ liệu chi phối các ranh giới nhà sản xuất chính, khả năng quan sát bao quát độ mới, khối lượng, lược đồ và phân phối trên các bảng quan trọng, và dòng gốc hỗ trợ phân tích tác động. Mọi tập dữ liệu quan trọng có chủ sở hữu có tên, và sự cố dữ liệu theo quy trình mức nghiêm trọng và ứng phó có tài liệu toàn tổ chức.
- **Mức 4, Quản lý:** Chất lượng và độ tin cậy được đo và kiểm soát theo đường cơ sở. Thời gian chết dữ liệu được theo dõi bằng chỉ số thật: thời gian trung bình để phát hiện, thời gian trung bình để giải quyết, độ mới và độ chính xác so với mức dịch vụ thống nhất, và ngân sách lỗi mà một tập dữ liệu có thể tiêu trước khi kích hoạt hành động. Tỷ lệ đứt gãy đối chiếu, tỷ lệ đạt kiểm thử và tỷ lệ dương tính giả của phát hiện bất thường được theo xu hướng theo thời gian, cảnh báo được điều chỉnh theo các con số đó thay vì đoán, và quyết định tiếp tục hay dừng cho một bản phát hành dữ liệu dựa trên chất lượng đo được so với đường cơ sở thay vì hy vọng.
- **Mức 5, Điều phối:** Chất lượng và khả năng quan sát lan tỏa, tự động và thích ứng. Phát hiện bất thường bắt trôi tinh vi, hợp đồng được thực thi máy móc, và dòng gốc được nắm bắt tự động và công bố trong danh mục. Dữ liệu có mức dịch vụ và quyền sở hữu trực như dịch vụ sản xuất, đối chiếu chạy liên tục, và rút kinh nghiệm không đổ lỗi nuôi việc giảm đều đặn thời gian chết dữ liệu. Chất lượng được tích hợp với quản trị dữ liệu, học máy và hoạch định kinh doanh, và tổ chức liên tục điều chỉnh ngưỡng, độ phủ và quyền sở hữu khi bối cảnh dữ liệu dịch chuyển.

## Ý tưởng để thảo luận

1. Bảng nào của bạn sẽ gây thiệt hại nhiều nhất nếu sai thầm lặng trong một tuần, và đó có phải những bảng bạn giám sát nhiều nhất không?
2. Một hợp đồng dữ liệu sẽ ngăn sự cố do thượng nguồn gần nhất của bạn ở đâu, và vì sao không có cái nào?
3. Một cuộc điều tra nguyên nhân gốc điển hình hôm nay tốn bao nhiêu thời gian kỹ thuật, và dòng gốc tự động sẽ tiết kiệm bao nhiêu?
4. Có mô hình học máy nào của bạn đang huấn luyện trên dữ liệu bạn không xác thực, và chúng có thể đang mã hóa những lỗi nào?
5. Cảnh báo của bạn được điều chỉnh đủ tốt để mọi người hành động trên mọi cảnh báo, hay có ai đã tắt tiếng kênh?
6. Mức dịch vụ về độ mới và độ chính xác nào mà người tiêu dùng quan trọng nhất của bạn thực sự chịu ký, và bạn có đáp ứng được hôm nay không?

## Những điểm cần ghi nhớ

- Chất lượng dữ liệu là mức phù hợp sử dụng qua độ chính xác, độ đầy đủ, tính nhất quán, tính kịp thời, tính hợp lệ và tính duy nhất.
- Dữ liệu xấu tệ hơn không có dữ liệu, vì nó làm hỏng quyết định và mô hình thầm lặng.
- Kiểm thử dữ liệu như mã: kiểm thử khẳng định và kỳ vọng cộng kiểm tra lược đồ, trong CI và trong môi trường sản xuất.
- Dùng hợp đồng dữ liệu để làm kỳ vọng nhà sản xuất và người tiêu dùng tường minh và thực thi được.
- Quan sát độ mới, khối lượng, lược đồ và phân phối, song song với khả năng quan sát phần mềm (chương 9.2).
- Nắm bắt dòng gốc để tìm nguyên nhân gốc và phân tích tác động nhanh, và công bố nó cho người tiêu dùng.
- Coi sự cố dữ liệu như sự cố sản xuất, với quyền sở hữu, mức nghiêm trọng và mức dịch vụ.
- Gắn công cụ đo nơi dữ liệu sai gây đau nhất; hướng đến chất lượng phù hợp sử dụng, không phải sự hoàn hảo ở mọi nơi.

## Tài liệu tham khảo và đọc thêm

- Barr Moses, Lior Gavish và Molly Vorwerck, "Data Quality Fundamentals."
- Jacek Majchrzak, Sven Balnojan và Marian Siwiak, "Data Contracts."
- Danette McGilvray, "Executing Data Quality Projects."
- Thomas C. Redman, "Data Driven: Profiting from Your Most Important Business Asset."
- Laura Sebastian-Coleman, "Measuring Data Quality for Ongoing Improvement."
- Joe Reis và Matt Housley, "Fundamentals of Data Engineering."
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- ISO/IEC 25012, "Data quality model."
