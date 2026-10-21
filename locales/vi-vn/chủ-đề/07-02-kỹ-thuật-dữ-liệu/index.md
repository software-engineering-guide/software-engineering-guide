# 7.2 Kỹ thuật dữ liệu

## Tổng quan và động lực

[Kỹ thuật dữ liệu](https://en.wikipedia.org/wiki/Data_engineering) là kỷ luật xây dựng và vận hành các đường ống và nền tảng đưa dữ liệu từ nơi nó được tạo ra đến nơi nó tạo giá trị. Nó bao quát việc thu nạp từ hệ thống nguồn, biến đổi thành dạng sạch và đã mô hình hóa, lưu trữ trong định dạng tiết kiệm chi phí, điều phối toàn bộ luồng, và các thực hành độ tin cậy giữ mọi thứ đáng tin. Nếu chiến lược dữ liệu quyết định dữ liệu nào nên tồn tại và ai sở hữu nó, thì kỹ thuật dữ liệu là hệ thống ống dẫn và máy móc làm nó chảy.

Với các đội lớn, kỷ luật này là nền tảng. Phân tích, [trí tuệ kinh doanh](https://en.wikipedia.org/wiki/Business_intelligence), thử nghiệm sản phẩm, [học máy](https://en.wikipedia.org/wiki/Machine_learning) và báo cáo quy định đều nằm hạ nguồn của đường ống dữ liệu. Khi các đường ống đó mong manh, chậm hay mờ đục, mọi chức năng phụ thuộc đều chịu thiệt. Bảng điều khiển hiển thị con số cũ. Mô hình huấn luyện trên đặc trưng hỏng. Kiểm toán viên không dựng lại được một con số được tạo ra thế nào. Ở quy mô doanh nghiệp và chính phủ, đường ống xử lý hàng tỷ bản ghi qua nhiều hệ thống nguồn, và một thất bại thầm lặng duy nhất có thể đẩy dữ liệu sai vào quyết định, khoản thanh toán hay thống kê công khai.

Lĩnh vực này đã trưởng thành từ các tập lệnh đặt riêng và các công cụ [ETL (trích xuất, biến đổi, tải)](https://en.wikipedia.org/wiki/Extract,_transform,_load) nguyên khối thành ngăn xếp dữ liệu hiện đại: các thành phần mô-đun, phần lớn dựa trên SQL cho thu nạp, biến đổi, điều phối và lưu trữ, được nối bằng định dạng mở. Tính mô-đun này vừa là món quà vừa là cái bẫy. Nó cho phép bạn lắp ráp công cụ tốt nhất mỗi loại, nhưng không có kỷ luật kỹ thuật nó tạo ra một mớ công việc không tài liệu, không kiểm thử lan tràn. Chương này bao quát các thực hành giữ đường ống lũy đẳng, kiểm thử được, quan sát được và chi trả nổi ở quy mô.

## Các nguyên tắc chính

- Đường ống là phần mềm và xứng đáng có quản lý phiên bản, kiểm thử, rà soát và CI/CD.
- Ưu tiên các phép biến đổi lũy đẳng, tái lập được có thể chạy lại an toàn.
- Làm luồng dữ liệu quan sát được: độ mới, khối lượng, lược đồ và chất lượng được giám sát.
- Mô hình hóa dữ liệu có chủ đích cho người tiêu dùng thay vì đổ bảng thô.
- Chọn theo lô hay luồng dựa trên nhu cầu độ trễ thực, không phải sự mới lạ.
- Tối ưu định dạng lưu trữ, phân vùng và chi phí tính toán như mối quan tâm hạng nhất.
- Tách thu nạp, biến đổi và phục vụ để mỗi thứ tiến hóa độc lập.
- Thất bại to và sớm; một đường ống hỏng an toàn hơn dữ liệu sai thầm lặng.

## Khuyến nghị

### Chọn ETL hay ELT có chủ đích

ETL biến đổi dữ liệu trước khi tải vào đích. [ELT (trích xuất, tải, biến đổi)](https://en.wikipedia.org/wiki/Extract,_load,_transform) tải dữ liệu thô trước và biến đổi nó bên trong một kho hay lakehouse mạnh. Các nền tảng đám mây hiện đại đã biến ELT thành mặc định, vì lưu trữ rẻ và tính toán co giãn, và giữ dữ liệu thô cho phép bạn xử lý lại khi logic thay đổi hoặc lỗi xuất hiện. Hãy ưu tiên ELT cho khối lượng công việc phân tích: hạ cánh dữ liệu thô bất biến, rồi xây các phép biến đổi phân lớp lên trên. Dành biến đổi trước khi tải cho các trường hợp quyền riêng tư, chi phí hay ràng buộc hợp đồng đòi hỏi làm sạch hoặc lọc trước khi dữ liệu hạ cánh.

### Thiết kế đường ống theo lô và luồng cho nhu cầu độ trễ của chúng

Hầu hết nhu cầu phân tích được phục vụ tốt bởi đường ống theo lô theo lịch, đơn giản hơn để suy luận, kiểm thử và chạy bù. Hãy với tới luồng chỉ khi doanh nghiệp thực sự cần dữ liệu độ trễ thấp: phát hiện gian lận, cảnh báo vận hành, cá nhân hóa thời gian thực. Luồng thêm độ phức tạp thật về thứ tự, ngữ nghĩa đúng-một-lần, dữ liệu đến muộn và quản lý trạng thái. Nơi bạn cần cả hai, hãy cân nhắc các kiến trúc thống nhất logic theo lô và luồng thay vì duy trì hai cơ sở mã phân kỳ. Hãy trung thực về yêu cầu độ trễ của bạn. "Thời gian thực" thường là một mong muốn chưa được xem xét làm gấp đôi chi phí của bạn.

### Điều phối với phụ thuộc tường minh

Hãy dùng một bộ điều phối để diễn đạt đường ống như [đồ thị có hướng không chu trình (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) gồm các tác vụ với phụ thuộc, thử lại và lập lịch tường minh. Điều này cho bạn thấy cái gì đã chạy, cái gì thất bại và cái gì bị chặn, cùng khả năng chạy bù và chạy lại tất định. Hãy dựa phụ thuộc vào tính sẵn có của dữ liệu, không chỉ thời gian đồng hồ, để các công việc hạ nguồn chờ dữ liệu thượng nguồn thay vì khởi chạy theo phỏng đoán. Giữ logic điều phối trong quản lý phiên bản, và coi thay đổi DAG như thay đổi mã.

### Mô hình hóa dữ liệu cho tiêu thụ

Bảng thô hiếm khi phù hợp cho nhà phân tích. Hãy áp dụng [mô hình hóa chiều](https://en.wikipedia.org/wiki/Dimensional_modeling), sắp xếp bảng sự kiện và chiều đã đồng nhất trong [lược đồ hình sao](https://en.wikipedia.org/wiki/Star_schema), nơi bạn cần phân tích tự phục vụ được quản trị, tái sử dụng được. Các bảng rộng phi chuẩn hóa ("một bảng lớn") có thể hiệu năng hơn cho các mẫu truy vấn cụ thể và đơn giản hơn với một số người tiêu dùng, với cái giá là trùng lặp và kém linh hoạt. Hãy phân lớp các phép biến đổi: một lớp tập kết thô, một lớp lõi đã làm sạch và đồng nhất, và các kho dữ liệu con hướng người tiêu dùng. Sự tách biệt này cho phép bạn sửa logic ở một nơi, và cho người tiêu dùng dựa vào giao diện ổn định.

### Làm đường ống lũy đẳng và kiểm thử được

Hãy thiết kế các phép biến đổi sao cho chạy lại tạo cùng kết quả, thay vì làm trùng hay hỏng dữ liệu, ví dụ bằng cách dùng upsert tất định khóa theo định danh kinh doanh và mẫu ghi đè phân vùng. Viết kiểm thử ở nhiều cấp: kiểm thử đơn vị cho logic biến đổi, kiểm thử lược đồ, và kiểm thử dữ liệu khẳng định các kỳ vọng như tính duy nhất, khóa không null, toàn vẹn tham chiếu và khoảng giá trị được chấp nhận. Chạy chúng trong CI, để một thay đổi tồi bị bắt trước khi đến dữ liệu sản xuất.

### Gắn công cụ quan sát và độ tin cậy

Hãy giám sát bốn tín hiệu cốt lõi của sức khỏe dữ liệu: độ mới (có cập nhật không), khối lượng (số hàng có trong khoảng kỳ vọng không), lược đồ (cấu trúc có đổi bất ngờ không) và phân phối (giá trị có trôi bất thường không). Cảnh báo khi vi phạm, và chuyển chúng đến đội sở hữu. Giữ sổ tay vận hành, phiên trực và rút kinh nghiệm không đổ lỗi cho sự cố dữ liệu, như bạn làm cho dịch vụ. Theo dõi dòng gốc, để khi có gì hỏng, bạn thấy ngay tác động hạ nguồn.

### Tối ưu lưu trữ và chi phí

Hãy dùng các định dạng cột mở như Parquet, hoặc các định dạng bảng mở hỗ trợ tiến hóa lược đồ, du hành thời gian và cập nhật hiệu quả. Phân vùng dữ liệu theo các cột bạn lọc nhiều nhất, thường là ngày, và tránh sự sinh sôi của các tệp nhỏ bằng cách nén gộp. Tách dữ liệu nóng và lạnh bằng lưu trữ phân tầng và chính sách vòng đời. Giám sát chi tiêu tính toán theo đường ống và theo truy vấn. Chi phí mất kiểm soát thường đến từ quét toàn bộ, thiếu phân vùng và xử lý lại không giới hạn. Hãy coi chi phí là một chỉ số có chủ sở hữu, không phải một bất ngờ trên hóa đơn hằng tháng.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| ELT (biến đổi tại chỗ) | Giữ dữ liệu thô, lưu trữ rẻ, xử lý lại được | Dấu chân lưu trữ lớn, cần quản trị | Phân tích đám mây |
| ETL (biến đổi trước khi tải) | Kiểm soát chi phí, lọc dữ liệu nhạy cảm sớm | Mất dữ liệu thô, khó xử lý lại hơn | Tải chịu quy định hoặc bị ràng buộc |
| Theo lô | Đơn giản, kiểm thử được, chạy bù dễ | Độ trễ cao hơn | Hầu hết phân tích |
| Luồng | Độ trễ thấp, phản ứng thời gian thực | Phức tạp, tốn kém, khó kiểm thử | Gian lận, cảnh báo vận hành |
| Lược đồ hình sao | Được quản trị, tái sử dụng được, thân thiện tự phục vụ | Công sức mô hình hóa ban đầu | BI dùng chung |
| Bảng rộng | Nhanh cho truy vấn đã biết, đơn giản | Trùng lặp, kém linh hoạt | Dùng hiệu năng cao hẹp |

Đánh đổi chi phối là sự đơn giản so với độ trễ và linh hoạt. Theo lô và ELT với lược đồ hình sao phân lớp cho bạn một hệ thống kiểm thử được, chạy bù được, được hiểu rõ phục vụ hầu hết nhu cầu với chi phí chấp nhận được. Luồng, thời gian thực và các thiết kế phi chuẩn hóa cao mua tốc độ và hiệu năng cụ thể, nhưng với cái giá đắt về độ phức tạp vận hành và khó khăn kiểm thử. Hãy chỉ áp dụng độ phức tạp nơi một yêu cầu kinh doanh cụ thể trả giá cho nó, và giữ con đường đơn giản làm mặc định.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn đã chọn có chủ đích ELT hơn ETL, và bạn có giữ dữ liệu thô bất biến để xử lý lại khi logic thay đổi hoặc lỗi nổi lên không?** Mặc định của chương là ELT: hạ cánh dữ liệu thô rẻ, rồi xây các phép biến đổi phân lớp, vì giữ dữ liệu thô cho phép bạn chạy lại mọi thứ khi một quy tắc đổi hoặc lỗi xuất hiện nhiều tuần sau. Xóa dữ liệu thô loại trừ lựa chọn đó và là cạm bẫy phổ biến, đau đớn. Lập luận đối lập cho ETL là có thật trong các tải chịu quy định hoặc bị ràng buộc, nơi quyền riêng tư, chi phí hay điều khoản hợp đồng đòi lọc hoặc che giấu trước khi dữ liệu hạ cánh. Hãy mang bằng chứng: bạn đã cần xử lý lại lịch sử bao nhiêu lần, và nó tốn bao nhiêu khi bạn không thể? Với một đường ống chính phủ hay doanh nghiệp phải truy vết bất kỳ con số nào về nguồn, bản ghi thô bất biến cũng là yêu cầu kiểm toán được, nên câu trả lời định hình cả chính sách lưu trữ lẫn khả năng bảo vệ pháp lý của bạn.

2. **Bạn thực sự giám sát tín hiệu nào trong bốn tín hiệu sức khỏe dữ liệu, và ai bị gọi khi một cái hỏng?** Chương nêu bốn tín hiệu đáng theo dõi: độ mới, khối lượng, lược đồ và phân phối. Nhiều đội không giám sát cái nào và biết về thất bại từ một giám đốc nhìn chằm chằm vào bảng điều khiển cũ, là bộ phát hiện tệ nhất có thể. Ở quy mô doanh nghiệp và chính phủ, một thất bại thầm lặng duy nhất có thể đẩy dữ liệu sai vào khoản thanh toán, báo cáo hay thống kê công khai, nên chi phí phát hiện muộn được đo bằng niềm tin và tiền, không chỉ làm lại. Hãy mang thời gian trung bình để phát hiện thực của bạn và tên người hiện tìm thấy sự cố đầu tiên. Nếu câu trả lời là "một người tiêu dùng," bạn cần cảnh báo chuyển đến đội sở hữu cộng sổ tay vận hành và rút kinh nghiệm không đổ lỗi, coi sự cố dữ liệu đúng như sự cố dịch vụ.

3. **Nhà phân tích của bạn tiêu thụ kho dữ liệu con đã mô hình hóa, kiểm thử, hay bạn đang đổ bảng thô lên họ và gọi đó là tự phục vụ?** Chương nói thẳng: bảng thô hiếm khi phù hợp cho nhà phân tích, và phân lớp các phép biến đổi thành lớp tập kết thô, lõi đồng nhất và kho dữ liệu con hướng người tiêu dùng cho phép bạn sửa logic một lần và cho người tiêu dùng giao diện ổn định. Lực kéo đối lập là tốc độ, vì mô hình hóa bằng lược đồ hình sao hay bảng rộng có chủ đích tốn công sức ban đầu và rất dễ bỏ qua. Nhưng đổ dữ liệu thô đẩy chi phí mô hình hóa lên mọi nhà phân tích lặp đi lặp lại, tạo ra con số phân kỳ và giờ làm lãng phí. Hãy mang một tín hiệu: bao nhiêu phần thời gian nhà phân tích dành cho định hình lại dữ liệu thô, và bao nhiêu đội đã xây lại cùng các phép nối. Nếu con số cao, hãy đầu tư vào một lớp lõi đồng nhất để người tiêu dùng dựa vào giao diện đã kiểm thử, tái sử dụng được thay vì phát minh lại.

4. **"Thời gian thực" thực sự xứng đáng chi phí ở đâu, và ở đâu nó là mong muốn chưa xem xét lặng lẽ nhân đôi gánh nặng vận hành của bạn?** Mặc định của chương là theo lô theo lịch, đơn giản hơn để suy luận, kiểm thử và chạy bù, với luồng dành cho các trường hợp doanh nghiệp thực sự cần độ trễ thấp, như phát hiện gian lận hay cảnh báo vận hành. Lực kéo đối lập là uy tín và các yêu cầu mơ hồ của bên liên quan về dữ liệu "trực tiếp," nghe rẻ trong cuộc họp hoạch định và thành đắt trong môi trường sản xuất, vì luồng kéo theo thứ tự, ngữ nghĩa đúng-một-lần, dữ liệu đến muộn và quản lý trạng thái, cộng một cơ sở mã thứ hai phải đồng bộ với logic theo lô. Hãy mang bằng chứng vào cuộc thảo luận: với mỗi đường ống luồng bạn chạy hay đề xuất, nêu quyết định nó nuôi và độ trễ quyết định đó thực sự chịu được, đo bằng phút hay giờ thay vì tính từ. Với một nền tảng doanh nghiệp hay chính phủ lớn, hãy thêm chi phí trực và kiểm thử của mỗi đường thời gian thực, vì một đường ống luồng không ai kiểm thử được hay bố trí nhân sự suốt ngày đêm là gánh nặng độ tin cậy khoác áo tính năng, và câu trả lời trung thực thường thu một yêu cầu "thời gian thực" về lô theo giờ phục vụ cùng quyết định.

5. **Đường ống nào của bạn không thể chạy lại an toàn hôm nay, và cần gì để mọi phép biến đổi lũy đẳng?** Chương nhấn mạnh các phép biến đổi lũy đẳng, tái lập được, dùng upsert tất định khóa theo định danh kinh doanh và mẫu ghi đè phân vùng, để chạy lại tạo cùng kết quả thay vì làm trùng hay hỏng dữ liệu. Áp lực đối lập là tốc độ phân phối, vì một công việc chỉ-thêm ngây thơ phát hành nhanh hơn công việc được thiết kế để chạy lại được, và chi phí của lối tắt đó ẩn cho đến khi một thất bại buộc chạy lại một phần lúc 2 giờ sáng và ai đó đếm đôi doanh thu. Hãy mang một bản kiểm kê cụ thể: liệt kê các công việc sẽ làm hỏng dữ liệu nếu chạy lại từ điểm thất bại, và ước tính bán kính ảnh hưởng của cái tệ nhất. Ở quy mô doanh nghiệp và chính phủ, nơi một thất bại thầm lặng có thể đẩy dữ liệu sai vào thanh toán, báo cáo hay thống kê công khai, xử lý không lũy đẳng không chỉ bất tiện mà làm suy yếu khả năng kiểm toán cho phép bạn xử lý lại một kỳ sau khi quy tắc đổi mà vẫn truy vết mọi con số về nguồn, nên tài trợ công việc làm lại để chạy lại an toàn là câu hỏi kiểm soát, không chỉ chuyện gọn gàng.

6. **Bạn có biết mỗi đường ống tốn bao nhiêu để chạy, ai sở hữu con số đó, và bao nhiêu hóa đơn đám mây đến từ quét toàn bộ và thiếu phân vùng không?** Chương coi định dạng lưu trữ, phân vùng và chi tiêu tính toán là mối quan tâm hạng nhất có chủ sở hữu, cảnh báo rằng chi phí mất kiểm soát thường truy về quét toàn bộ, thiếu phân vùng và xử lý lại không giới hạn. Cân nhắc đối lập là công việc chi phí cảm thấy ít cấp bách hơn phát hành tính năng, nên bị hoãn cho đến khi hóa đơn hằng tháng thành bất ngờ và tài chính bắt đầu hỏi những câu kỹ thuật không trả lời được. Hãy mang bằng chứng: chi tiêu theo đường ống và theo truy vấn, phần chi phí đến từ quét không phân vùng, và số tệp nhỏ cần được nén gộp. Với một tổ chức lớn chạy hàng tỷ bản ghi qua nhiều hệ thống nguồn, một hóa đơn đám mây không chủ sở hữu tăng lên mà không đội nào cảm thấy có trách nhiệm, và trong bối cảnh chính phủ chi tiêu công phải được biện minh từng dòng, nên quy chi phí tính toán cho một chủ sở hữu có tên với chỉ số được theo dõi biến một khoản chi mờ đục thành được quản lý và thường lộ ra khoản tiết kiệm đủ lớn để tài trợ khoản đầu tư nền tảng kế tiếp.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ thắng kiến trúc. Hãy nối thu nạp với một đầu nối được quản lý, xây một nhúm phép biến đổi được quản lý phiên bản, và chạy chúng trên một bộ điều phối nhẹ tự thử lại và chạy bù, thay vì tự viết cron job hỏng thầm lặng qua đêm. Giữ mọi mô hình lũy đẳng từ commit đầu tiên và thêm vài kiểm thử rẻ cho khóa null và số hàng, để một thay đổi nguồn tồi thất bại trong CI thay vì nổi lên trong bảng điều khiển sáng thứ Hai của người sáng lập. Đừng dựng luồng hay nền tảng đặt riêng: nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư.

**Doanh nghiệp nhỏ.** Không có kỹ sư dữ liệu riêng, hãy ưu tiên mua một ngăn xếp tích hợp hơn là lắp ráp một cái. Một dịch vụ ELT được quản lý cộng một kho đám mây cho bạn đầu nối, lập lịch và lưu trữ mà không cần đội nền tảng bảo trì chúng. Hãy đóng khung lựa chọn như vệ sinh dữ liệu hơn là dự án đường ống: biết hệ thống nguồn nào nuôi báo cáo của bạn, giữ dữ liệu thô để một con số sai có thể được truy vết và xử lý lại, và chọn công cụ có chi phí khả đoán để một lần quét toàn bảng không làm nổ ngân sách tháng.

**Doanh nghiệp lớn.** Vấn đề là nhất quán qua nhiều đội và hàng tỷ bản ghi từ nhiều hệ thống nguồn. Hãy chuẩn hóa mẫu ELT, mô hình phân lớp tập kết-lõi-kho con, và bốn tín hiệu sức khỏe dữ liệu để các nhóm thôi phát minh lại những đường ống mong manh. Thực thi kiểm thử dữ liệu và CI cho mọi mô hình, quy chi phí tính toán cho đội sở hữu, và đưa sự cố dữ liệu qua cùng kỷ luật trực, sổ tay vận hành và rút kinh nghiệm không đổ lỗi bạn dùng cho dịch vụ, để một thất bại thầm lặng không bao giờ đến bảng điều khiển mà không bị chú ý.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình đường ống. Hãy hạ cánh bản ghi thô bất biến cho khả năng kiểm toán, biến đổi chúng trong các giai đoạn phân lớp, đã kiểm thử, và giữ dòng gốc đầy đủ để kiểm toán viên truy vết bất kỳ con số được công bố nào về tài liệu nguồn, thường là yêu cầu pháp lý. Xử lý lũy đẳng cho phép bạn xử lý lại một hồ sơ hay kỳ báo cáo an toàn khi quy tắc đổi, và ưu tiên định dạng mở và mã biến đổi di chuyển được giữ bạn khỏi bị khóa vào một nhà cung cấp duy nhất qua hợp đồng nhiều năm.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp phân tích mười người đã nuôi lớn một mớ cron job hỏng thầm lặng qua đêm và đôi khi đếm đôi hàng khi một kỹ sư chạy lại một cái bằng tay. Đội chuyển sang một đầu nối được quản lý cho thu nạp, một khung biến đổi cho các mô hình được quản lý phiên bản, và một bộ điều phối nhẹ tự thử lại và chạy bù. Họ làm mọi mô hình lũy đẳng và thêm một nhúm kiểm thử cho khóa null và số hàng, nên một thay đổi nguồn tồi nay thất bại trong CI thay vì nổi lên trong bảng điều khiển sáng thứ Hai của người sáng lập.

**Doanh nghiệp lớn.** Một nhà bán lẻ toàn cầu thay hàng trăm tập lệnh trích xuất viết tay bằng một ngăn xếp ELT. Các đầu nối được quản lý hạ cánh dữ liệu nguồn thô, một khung biến đổi xây các mô hình đã kiểm thử, được quản lý phiên bản trong một lakehouse, và một bộ điều phối quản lý phụ thuộc với thử lại và chạy bù. Kiểm thử dữ liệu bắt trôi lược đồ từ hệ thống nguồn trước khi nó đến bảng điều khiển. Lưu trữ cột có phân vùng cắt chi phí truy vấn đáng kể, trong khi cải thiện độ mới từ hằng ngày sang hằng giờ.

**Chính phủ.** Một cơ quan thuế thu nạp hồ sơ khai và dữ liệu bên thứ ba qua một đường ống được quản trị hạ cánh bản ghi thô bất biến cho khả năng kiểm toán, rồi biến đổi chúng trong các giai đoạn phân lớp, đã kiểm thử. Xử lý lũy đẳng cho họ xử lý lại an toàn một kỳ khai thuế khi quy tắc đổi. Dòng gốc đầy đủ cho phép kiểm toán viên truy vết bất kỳ con số tính toán nào về tài liệu nguồn, một yêu cầu pháp lý cho trách nhiệm giải trình công.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của kỹ thuật dữ liệu có kỷ luật đến từ độ tin cậy, tốc độ và kiểm soát chi phí. Đường ống đáng tin nghĩa là quyết định và báo cáo dựa trên dữ liệu đáng tin, nên bạn tránh được việc làm lại tốn kém và thiệt hại danh tiếng của con số sai. Đường ống mô-đun, đã kiểm thử cho phép các đội phát hành sản phẩm dữ liệu mới nhanh hơn, cộng dồn giá trị của mọi khoản đầu tư phân tích và ML hạ nguồn. Tối ưu lưu trữ và tính toán trực tiếp giảm hóa đơn đám mây, thường với biên độ lớn khi phân vùng và mẫu truy vấn được sửa.

Chi phí áp dụng gồm công cụ nền tảng, thời gian kỹ thuật để xây đường ống mô-đun đã kiểm thử, và kỷ luật coi dữ liệu là phần mềm. Hãy cân nhắc điều đó so với chi phí của việc không áp dụng: công việc đặt riêng mong manh chỉ tác giả hiểu, hỏng dữ liệu thầm lặng được giám đốc phát hiện, chi tiêu đám mây phình ra từ quét toàn bảng, và nhà phân tích bị chặn chờ dữ liệu. Với ban lãnh đạo, hãy đóng khung kỹ thuật dữ liệu là nền tảng khiến phân tích, BI và AI đáng tin và chi trả nổi. Đầu tư thiếu ở đây, và bạn đặt trần cho lợi tức của mọi sáng kiến dữ liệu bên trên nó.

## Phản mẫu và cạm bẫy

- Đường ống xây như tập lệnh một lần không có quản lý phiên bản, kiểm thử hay rà soát.
- Công việc không lũy đẳng làm trùng hoặc hỏng dữ liệu khi chạy lại sau thất bại.
- Áp dụng luồng vì uy tín khi theo lô đã đáp ứng yêu cầu độ trễ.
- Đổ bảng thô lên nhà phân tích và gọi đó là tự phục vụ.
- Không có khả năng quan sát, nên thất bại được người tiêu dùng hạ nguồn phát hiện.
- Bỏ qua phân vùng và kích thước tệp cho đến khi hóa đơn đám mây bùng nổ.
- Ghép thu nạp, biến đổi và phục vụ để không gì thay đổi được an toàn.
- Xóa dữ liệu thô, khiến không thể xử lý lại khi logic thay đổi.

## Mô hình trưởng thành

1. Khởi đầu: Tập lệnh tùy nghi và chạy thủ công, không kiểm thử hay giám sát. Thất bại được người tiêu dùng hạ nguồn phát hiện, công việc không chạy lại an toàn được, và chi phí đám mây không được quản lý và không quy chủ.
2. Phát triển: Một số đội đã áp dụng bộ điều phối và đặt các phép biến đổi cơ bản vào quản lý phiên bản, nhưng thực hành không nhất quán toàn tổ chức. Kiểm thử thỉnh thoảng có, tính lũy đẳng chắp vá, và đường ống hỏng vẫn nghĩa là chữa cháy phản ứng.
3. Chuẩn hóa: ELT với mô hình phân lớp tập kết-lõi-kho con, đã kiểm thử và quản lý phiên bản, là tiêu chuẩn có tài liệu áp dụng qua các đội. Phụ thuộc được điều phối với thử lại và chạy bù, kiểm thử dữ liệu chạy trong CI, và quy ước dùng chung cho mô hình hóa lược đồ hình sao và phân vùng được thực thi toàn tổ chức thay vì để mỗi nhóm tự lo.
4. Quản lý: Nền tảng được đo và kiểm soát. Độ mới, khối lượng, lược đồ và phân phối được giám sát với cảnh báo chuyển đến đội sở hữu, và SLA đường ống, thời gian trung bình để phát hiện, tỷ lệ đạt chất lượng dữ liệu, và chi phí tính toán theo đường ống và theo truy vết được theo dõi theo đường cơ sở. Ngưỡng hoàn tác và khai tử được thực thi dựa trên bằng chứng, và chi phí cùng độ tin cậy có chủ sở hữu có tên chịu mục tiêu.
5. Điều phối: Đường ống được coi hoàn toàn là phần mềm với CI/CD, hợp đồng dữ liệu, và phát hiện bất thường tự động bắt trôi trước người tiêu dùng. Logic theo lô và luồng được thống nhất nơi độ trễ thực sự đáng giá, nền tảng được cải thiện liên tục và tự phục vụ, và năng lực, tầng lưu trữ và chi phí được cân bằng lại thích ứng khi khối lượng công việc dịch chuyển để sản phẩm dữ liệu mới phát hành nhanh trên nền tảng ổn định.

## Ý tưởng để thảo luận

- "Thời gian thực" thực sự xứng đáng chi phí ở đâu trong ngăn xếp của bạn, và ở đâu nó là mong ước?
- Đường ống nào không thể chạy lại an toàn hôm nay, và cần gì để sửa điều đó?
- Bao nhiêu hóa đơn dữ liệu đám mây của bạn đến từ quét toàn bộ và thiếu phân vùng?
- Nhà phân tích của bạn tiêu thụ kho dữ liệu con đã mô hình hóa hay bảng thô, và điều đó tốn họ gì?
- Thời gian trung bình để phát hiện sự cố dữ liệu của bạn là bao nhiêu, và ai tìm thấy đầu tiên?
- Thống nhất logic theo lô và luồng sẽ giảm gánh nặng bảo trì hay thêm rủi ro?

## Những điểm cần ghi nhớ

- Coi đường ống là phần mềm: quản lý phiên bản, kiểm thử, rà soát, CI/CD và khả năng quan sát.
- Ưu tiên ELT với các mô hình phân lớp, đã kiểm thử; giữ dữ liệu thô để xử lý lại.
- Chọn theo lô theo mặc định và luồng chỉ nơi độ trễ thực sự đáng giá.
- Làm các phép biến đổi lũy đẳng để chạy lại an toàn.
- Mô hình hóa dữ liệu cho người tiêu dùng bằng lược đồ hình sao hoặc bảng rộng có chủ đích.
- Giám sát độ mới, khối lượng, lược đồ và phân phối, và coi sự cố dữ liệu như ngừng hoạt động.
- Tối ưu định dạng lưu trữ, phân vùng và chi phí tính toán như mối quan tâm hạng nhất.

## Tài liệu tham khảo và đọc thêm

- Joe Reis và Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball và Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz và James Warren, "Big Data" (kiến trúc Lambda).
- Barr Moses và các đồng nghiệp, "Data Quality Fundamentals" (khả năng quan sát dữ liệu).
