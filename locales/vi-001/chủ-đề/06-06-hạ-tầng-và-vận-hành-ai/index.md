# 6.6 Hạ tầng và vận hành AI

## Tổng quan và động lực

Hạ tầng và vận hành AI là kỷ luật cung cấp, lập lịch và vận hành các hệ thống tính toán, lưu trữ và phục vụ chuyên dụng mà khối lượng công việc AI đòi hỏi, làm điều đó một cách tiết kiệm, đáng tin cậy và quan sát được. AI hiện đại tốn kém để chạy. Huấn luyện và phục vụ các mô hình lớn đòi hỏi các bộ tăng tốc khan hiếm ([GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) và [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), mạng băng thông cao, kho vector quy mô lớn cho truy xuất (lập chỉ mục dữ liệu dưới dạng vector số để tìm nhanh các mục tương tự), và các tầng phục vụ được tinh chỉnh cho độ trễ và thông lượng. Làm đúng hạ tầng này là sự khác biệt giữa AI mở rộng bền vững và AI lặng lẽ tiêu hết ngân sách trong khi giao hàng kém.

Với các đội lớn, vấn đề cốt lõi là quy mô, sự khan hiếm và chi phí. Bộ tăng tốc có hạn và đắt, nên việc lập lịch và tận dụng cực kỳ quan trọng. GPU nhàn rỗi là tiền bị đốt, và suy luận gom lô kém nhân chi phí mỗi yêu cầu. Các ứng dụng nặng truy xuất cần [cơ sở dữ liệu vector](https://en.wikipedia.org/wiki/Vector_database) giữ nhanh khi lớn lên. Các ứng dụng AI sinh tạo cần đánh phiên bản prompt, đường ống đánh giá và khả năng quan sát (đôi khi gọi là LLMOps) để vận hành an toàn và cải thiện theo thời gian. Không có hạ tầng dùng chung và kỷ luật vận hành, mỗi đội chiến đấu cùng những trận đánh và chi phí leo thang.

Các tổ chức chính phủ và chịu quy định thêm yêu cầu về chủ quyền dữ liệu, bảo mật và chi tiêu khả đoán. Họ có thể cần triển khai tại chỗ hoặc đám mây chủ quyền để dữ liệu nhạy cảm và mô hình không bao giờ rời ranh giới được kiểm soát. Họ phải dự báo và biện minh chi tiêu hạ tầng, và đáp ứng tiêu chuẩn bảo mật và sẵn sàng. Các quyết định hạ tầng AI trong những bối cảnh này mang hệ quả nhiều năm, nên hãy đưa ra chúng với mua sắm, bảo mật và lối thoát trong tâm trí.

## Các nguyên tắc chính

- Coi tính toán bộ tăng tốc là nguồn lực khan hiếm, đắt đỏ cần được lập lịch và tận dụng, không tích trữ.
- Tối ưu chi phí mỗi đơn vị công việc hữu ích, không phải năng lực thô.
- Chọn kích thước mô hình và phần cứng vừa với nhiệm vụ; lựa chọn lớn nhất hiếm khi hiệu quả chi phí nhất.
- Thiết kế phục vụ cho độ trễ và thông lượng với gom lô và bộ nhớ đệm như kỹ thuật hạng nhất.
- Làm hệ thống AI quan sát được: theo dõi chi phí, độ trễ, chất lượng và lỗi liên tục.
- Đánh phiên bản và đánh giá prompt cùng mô hình với sự chặt chẽ như mã.
- Lên kế hoạch cho khả năng di chuyển và tránh khóa chặt trong các lựa chọn hạ tầng và phục vụ.

## Khuyến nghị

### Hoạch định và kiểm soát tính toán bộ tăng tốc

Hãy dự báo nhu cầu huấn luyện và suy luận riêng biệt, vì chúng có hình dạng khác nhau. Huấn luyện theo đợt và lập lịch được; suy luận liên tục và nhạy với độ trễ. Hãy dùng bộ lập lịch và hạn ngạch để chia sẻ GPU và TPU khan hiếm qua các đội, ưu tiên khối lượng công việc, và đẩy mức tận dụng lên. Đo mức tận dụng và coi sự nhàn rỗi kinh niên là vấn đề cần sửa. Hãy trộn năng lực đặt trước cho tải nền với năng lực theo yêu cầu hoặc giá điểm (spot) cho các đợt tăng đột biến để kiểm soát chi phí. Cân nhắc liệu bộ tăng tốc rẻ hơn hoặc nhỏ hơn, hay suy luận trên CPU cho các mô hình nhẹ, có đủ không. Chọn giữa đám mây, tại chỗ và lai dựa trên chi phí ở quy mô của bạn, nhu cầu chủ quyền dữ liệu và mẫu tăng đột biến, và giữ một đường thoát.

### Xây hạ tầng truy xuất: embedding và cơ sở dữ liệu vector

Với các ứng dụng tăng cường truy xuất, hãy dựng hạ tầng để tạo [embedding](https://en.wikipedia.org/wiki/Word_embedding) (biểu diễn vector số đặt các mục tương tự gần nhau) và lưu chúng trong một cơ sở dữ liệu vector hỗ trợ [tìm kiếm láng giềng gần nhất xấp xỉ](https://en.wikipedia.org/wiki/Nearest_neighbor_search) nhanh (tìm các vector tương tự nhất mà không so sánh vét cạn từng cái) ở quy mô của bạn. Hãy lên kế hoạch cho ba điều: chi phí và độ trễ của việc tạo embedding, độ mới của chỉ mục khi tài liệu thay đổi, và gánh nặng vận hành của việc giữ chỉ mục nhất quán. Đánh giá xem một cơ sở dữ liệu vector chuyên dụng, một phần mở rộng có khả năng vector của cơ sở dữ liệu hiện có, hay một dịch vụ được quản lý phù hợp nhất với quy mô và mức chịu khóa chặt của bạn. Giám sát độ trễ và độ phủ truy xuất, vì chất lượng truy xuất quyết định trực tiếp chất lượng ứng dụng.

### Tối ưu phục vụ mô hình: gom lô, bộ nhớ đệm và độ trễ

Phục vụ là nơi chi phí suy luận và trải nghiệm người dùng được quyết định. Hãy dùng **gom lô** để xử lý nhiều yêu cầu cùng nhau và nâng thông lượng bộ tăng tốc, cân bằng kích thước lô với độ trễ. Hãy dùng **bộ nhớ đệm** tích cực: lưu đệm các yêu cầu giống hệt hoặc tương tự về ngữ nghĩa, lưu đệm embedding, và tận dụng bộ nhớ đệm prompt hay tiền tố nơi nền tảng hỗ trợ để tránh tính lại ngữ cảnh dùng chung. Hãy đặt mục tiêu độ trễ rõ ràng, và đo độ trễ đuôi, không chỉ trung bình. Định tuyến yêu cầu đến các mô hình vừa kích thước: mô hình nhỏ cho ca dễ, mô hình lớn hơn chỉ khi cần. Tự động co giãn phục vụ theo nhu cầu, và kiểm thử tải trước khi ra mắt để bạn biết năng lực và đường cong chi phí của mình.

### Thực hành LLMOps: đánh phiên bản prompt, đường ống đánh giá và khả năng quan sát

Hãy coi prompt là hiện vật có phiên bản trong quản lý mã nguồn, có rà soát và khả năng hoàn tác. Xây các đường ống đánh giá chạy tự động các bộ kiểm thử ngoại tuyến bất cứ khi nào prompt hay mô hình thay đổi, để bạn bắt hồi quy trước khi phát hành. Gắn công cụ đo toàn diện cho môi trường sản xuất: ghi nhật ký đầu vào, đầu ra, độ trễ, mức dùng token, chi phí và lỗi, với lấy mẫu và biện pháp bảo vệ quyền riêng tư. Theo dõi tín hiệu chất lượng và phản hồi người dùng trực tuyến. Khả năng quan sát này cho phép bạn bắt suy giảm, kiểm soát chi phí, gỡ lỗi thất bại và cải thiện hệ thống an toàn: xương sống vận hành của AI sinh tạo trong môi trường sản xuất.

### Quản lý chi phí không khoan nhượng và quan sát được

Hãy quy chi tiêu AI cho các đội và trường hợp sử dụng để chi phí hiển thị và có chủ. Đặt ngân sách và cảnh báo, giám sát chi phí mỗi yêu cầu và mỗi kết quả, và thường xuyên rà soát các động lực chi phí lớn nhất. Kéo các đòn bẩy bạn có: chọn kích thước mô hình vừa phải, bộ nhớ đệm, gom lô, cắt tỉa prompt và ngữ cảnh, và chọn triển khai rẻ nhất đáp ứng yêu cầu. Chi phí AI có thể tăng theo mức sử dụng theo những cách đáng ngạc nhiên, nên khả năng quan sát chi phí liên tục là thiết yếu để tránh những bất ngờ khó chịu.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Lựa chọn A | Lựa chọn B | Đánh đổi |
|---|---|---|---|
| Vị trí tính toán | Đám mây | Tại chỗ | Tính co giãn và chi phí ban đầu thấp so với kiểm soát, chủ quyền và kinh tế trạng thái ổn định |
| Năng lực | Đặt trước | Theo yêu cầu/giá điểm | Chi phí khả đoán so với linh hoạt và rủi ro bị ngắt |
| Kích thước lô | Lô lớn | Lô nhỏ | Thông lượng và chi phí so với độ trễ |
| Kích thước mô hình | Mô hình lớn | Mô hình nhỏ | Chất lượng so với chi phí và tốc độ |
| Kho vector | Cơ sở dữ liệu chuyên dụng | Phần mở rộng cơ sở dữ liệu hiện có | Hiệu năng ở quy mô so với đơn giản và ít hệ thống hơn |
| Bộ nhớ đệm | Tích cực | Tối thiểu | Chi phí và độ trễ thấp hơn so với độ mới và độ phức tạp |

Đánh đổi chi phối là chi phí so với độ trễ và chất lượng. Gom lô, bộ nhớ đệm và mô hình nhỏ hơn cắt chi phí nhưng có thể thêm độ trễ hoặc giảm chất lượng. Sự cân bằng đúng phụ thuộc vào mức dung nạp của ứng dụng. Tại chỗ so với đám mây đánh đổi kiểm soát và kinh tế trạng thái ổn định lấy tính co giãn và cam kết thấp, một quyết định bị định hình nặng bởi nhu cầu chủ quyền dữ liệu và quy mô.

## Câu hỏi để thảo luận với đội của bạn

1. **Chi phí mỗi kết quả hữu ích của chúng ta hôm nay là bao nhiêu, và đòn bẩy nào sẽ dịch chuyển nó nhiều nhất?** Năng lực thô và trung bình mỗi yêu cầu che giấu con số quan trọng: tốn bao nhiêu để giao một đơn vị giá trị thật, và nó mở rộng thế nào với mức sử dụng. Với một đội lớn, khoảng cách giữa một triển khai được tối ưu và không được tối ưu thường là gấp nhiều lần về chi tiêu, nên câu hỏi này biến một nỗi lo mơ hồ về hóa đơn thành danh sách các bản sửa được xếp hạng. Hãy mang việc quy chi phí hiện tại theo đội và trường hợp sử dụng, xu hướng mỗi yêu cầu và mỗi kết quả, và các động lực chi phí lớn nhất. Hãy thảo luận các đòn bẩy theo thứ tự lợi ích: chọn kích thước mô hình vừa phải, bộ nhớ đệm (gồm bộ nhớ đệm tiền tố và ngữ nghĩa), gom lô, và cắt tỉa prompt hay ngữ cảnh. Trong chính phủ, thêm áp lực dự báo và biện minh chi tiêu nhiều năm. Câu trả lời nên giao cho mỗi động lực chi phí hàng đầu một chủ sở hữu và một đòn bẩy, không phải một cái nhún vai.

2. **Nếu nhà cung cấp suy luận hiện tại của chúng ta tăng gấp đôi giá hoặc ngừng hoạt động ngày mai, chúng ta chuyển nhanh đến đâu?** Khóa chặt thầm lặng dễ xây và đau đớn để thoát, và ngăn xếp phục vụ là nơi nó ẩn sâu nhất. Với doanh nghiệp và đặc biệt là chính phủ, khả năng di chuyển là yêu cầu mua sắm và liên tục, không phải điều dễ chịu. Hãy mang kiến trúc của bạn: liệu mô hình có nằm sau một giao diện nội bộ, liệu prompt và bộ đánh giá có di chuyển được, và bạn phụ thuộc bao nhiêu vào hành vi phục vụ riêng của nhà cung cấp. Tín hiệu cần theo dõi là liệu có ai từng chạy bộ đánh giá của bạn trên nhà cung cấp thứ hai hay mục tiêu triển khai thứ hai chưa. Nếu việc chuyển sẽ mất nhiều tháng và viết lại các đường lõi, hãy coi đó là khiếm khuyết thiết kế cần xử lý ngay, vì các tùy chọn chủ quyền và tại chỗ có thể trở thành bắt buộc với rất ít thông báo.

3. **Mức tận dụng bộ tăng tốc của chúng ta ngay bây giờ là bao nhiêu, và GPU nhàn rỗi cùng suy luận không gom lô đang đốt bao nhiêu?** Bộ tăng tốc khan hiếm và đắt, nên sự nhàn rỗi kinh niên và phục vụ từng yêu cầu lặng lẽ rút ngân sách có thể tài trợ thêm năng lực. Với một tổ chức lớn chia sẻ GPU qua các đội, câu hỏi này phơi bày liệu lập lịch, hạn ngạch và ưu tiên có thực sự giữ mức tận dụng cao hay phần cứng tích trữ, dùng thiếu là chuẩn mực. Hãy mang số liệu tận dụng thực, tư thế gom lô và bộ nhớ đệm, và các phép đo độ trễ đuôi, không chỉ trung bình, vì người dùng cảm nhận cái đuôi chậm. Hãy thảo luận liệu nhu cầu huấn luyện và suy luận có được dự báo riêng, cho hình dạng khác nhau của chúng, và liệu một mô hình nhỏ hơn hay suy luận trên CPU có đủ cho các ca nhẹ. Câu trả lời nên chỉ vào năng lực nhàn rỗi cụ thể để thu hồi và các yêu cầu cụ thể để gom lô hoặc định tuyến đến mô hình vừa kích thước.

4. **Khi một thay đổi prompt hay mô hình được phát hành, cái gì ngăn một hồi quy chất lượng hay chi phí thầm lặng đến người dùng?** Một ngăn xếp phục vụ có thể trông khỏe về độ trễ và thời gian hoạt động trong khi các câu trả lời nó trả về lặng lẽ tệ đi hoặc một prompt mới nhân đôi mức dùng token mỗi yêu cầu. Với một đội lớn nơi nhiều nhóm sửa prompt và đổi mô hình độc lập, một thay đổi không được chặn cổng là sự cố sản xuất đang chờ, và bán kính ảnh hưởng lớn lên với mỗi đội trên nền tảng dùng chung. Hãy mang độ phủ đánh giá của bạn: prompt và mô hình nào có bộ kiểm thử ngoại tuyến, liệu các bộ đó có chạy tự động ở mỗi thay đổi, ngưỡng chất lượng và chi phí nào chặn cổng một bản phát hành, và bạn hoàn tác nhanh đến đâu. Hãy thảo luận liệu prompt sống trong quản lý mã nguồn có rà soát, hay vẫn có ai đó sửa tay được prompt hệ thống đang chạy. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn mỗi thay đổi với dấu vết kiểm toán và một người phê duyệt có tên, vì cơ quan quản lý hỏi "ai đã đổi cái này và bạn đã kiểm thử gì" cần một câu trả lời được ghi lại, không phải được nhớ.

5. **Chúng ta quyết định giữa đám mây, tại chỗ và chủ quyền thế nào, và đã định giá kinh tế trạng thái ổn định thực thay vì bản thí điểm chưa?** Lựa chọn vị trí tính toán đặt đường cong chi phí, tư thế chủ quyền dữ liệu và các lối thoát của bạn trong nhiều năm, vậy mà nó thường được đưa ra dựa trên hóa đơn đám mây của một bản thí điểm trông chẳng giống môi trường sản xuất ở quy mô. Với một tổ chức lớn, năng lực đám mây co giãn rẻ để bắt đầu và có thể thành dòng lớn nhất đơn lẻ khi suy luận chạy liên tục, trong khi tại chỗ đánh đổi cam kết thấp lấy kiểm soát và kinh tế trạng thái ổn định. Hãy mang khối lượng huấn luyện và suy luận dự báo, điểm hòa vốn nơi phần cứng đặt trước hoặc sở hữu thắng theo yêu cầu, ràng buộc cư trú dữ liệu và bảo mật của bạn, và các mẫu tăng đột biến lập luận cho mô hình lai. Trong bối cảnh chính phủ và chịu quy định, hãy cân nhắc các yêu cầu đám mây chủ quyền hoặc tại chỗ có thể trở thành bắt buộc với rất ít thông báo, và xác nhận kiến trúc giữ mô hình sau một giao diện nội bộ để một cuộc chuyển ép buộc không viết lại các đường lõi.

6. **Chúng ta có thực sự sở hữu chi tiêu AI của mình, và mỗi đội có thấy và giải trình được chi phí nó thúc đẩy không?** Chi phí AI tăng theo mức sử dụng theo những cách làm người ta bất ngờ, và không có việc quy chi phí, hóa đơn đáp xuống như một con số mờ đục mà không đội nào thấy có trách nhiệm giảm. Trong một tổ chức lớn, chi phí không ai sở hữu là chi phí không ai tối ưu, nên câu hỏi là liệu chi tiêu có được gắn thẻ cho đội và trường hợp sử dụng với ngân sách, cảnh báo và xu hướng mỗi kết quả, hay chỉ được phát hiện khi tài chính leo thang. Hãy mang mô hình quy chi phí của bạn, các động lực lớn nhất theo đội, và các đòn bẩy mỗi chủ sở hữu kiểm soát: chọn kích thước mô hình vừa phải, bộ nhớ đệm, gom lô, và cắt tỉa ngữ cảnh. Với ngân sách doanh nghiệp và chính phủ, hãy thêm kỷ luật dự báo và biện minh chi tiêu hạ tầng nhiều năm, vì một cơ quan công không giải thích được hóa đơn tính toán từng dòng sẽ khó bảo vệ nó trong rà soát.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Đừng sở hữu hạ tầng nào bạn tránh được. Hãy gọi một API suy luận được lưu trữ, định tuyến yêu cầu dễ đến một mô hình nhỏ rẻ và dành mô hình lớn hơn cho ca khó, và lưu đệm tích cực để các prompt lặp lại không tốn gì. Dùng cơ sở dữ liệu vector được quản lý thay vì tự vận hành, giữ prompt trong git với một tập lệnh đánh giá ngắn trước mỗi thay đổi, và ghi nhật ký chi phí mỗi yêu cầu để một hóa đơn mất kiểm soát hiện ra trước khi gây đau. Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư, nên hãy mua khả năng vận hành và giữ việc chuyển đổi rẻ.

**Doanh nghiệp nhỏ.** Không có đội nền tảng, hãy coi phục vụ, truy xuất và khả năng quan sát là thứ bạn mua bên trong các công cụ đã dùng, không phải hệ thống bạn bố trí nhân sự. Ưu tiên suy luận được quản lý và tìm kiếm vector được quản lý với giá minh bạch, khả đoán, và đặt trần chi tiêu cứng cùng cảnh báo hóa đơn từ ngày đầu. Hãy đóng khung quyết định mua-so-với-xây một cách trung thực: vận hành GPU hay chỉ mục vector hiếm khi đáng ở khối lượng của bạn, và một mô hình nhỏ sau API lưu trữ thường đáp ứng nhu cầu với một phần nhỏ công sức.

**Doanh nghiệp lớn.** Vấn đề là một nền tảng đường lát sẵn dùng chung qua nhiều đội: bộ tăng tốc gộp chung với bộ lập lịch, hạn ngạch và ưu tiên để đẩy mức tận dụng lên, gom lô và bộ nhớ đệm chuẩn, bộ định tuyến chọn kích thước vừa, và chi phí được quy cho từng đội và trường hợp sử dụng. Hãy chặn cổng thay đổi prompt và mô hình bằng các bộ đánh giá tự động, chuẩn hóa tầng giao diện để nhà cung cấp và mục tiêu triển khai thay thế được, và quản lý chi phí mỗi kết quả như một chỉ số hạng nhất thay vì để mỗi nhóm phát minh lại hạ tầng đắt đỏ, dùng thiếu.

**Chính phủ.** Chủ quyền dữ liệu, bảo mật và chi tiêu khả đoán định hình mọi lựa chọn. Hãy ưu tiên triển khai tại chỗ hoặc đám mây chủ quyền để dữ liệu nhạy cảm và mô hình ở trong ranh giới được kiểm soát, lập lịch GPU khan hiếm qua các bộ với hạn ngạch bạn biện minh được trong mua sắm, và dự báo năng lực để bảo vệ chi tiêu nhiều năm từng dòng. Hãy đánh phiên bản và đánh giá prompt cùng mô hình với dấu vết kiểm toán được ghi lại, giữ khả năng quan sát toàn diện về chi phí và chất lượng, và giữ mô hình sau một giao diện nội bộ để một cuộc chuyển ép buộc sang nhà cung cấp mới hay nền tảng chủ quyền không làm bạn mắc kẹt.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp nhỏ chạy tính năng viết bằng AI giữ hóa đơn hợp lý mà không sở hữu GPU nào. Họ gọi một API suy luận được lưu trữ, định tuyến yêu cầu dễ đến một mô hình nhỏ rẻ hơn và dành mô hình lớn hơn cho ca khó, và lưu đệm các câu trả lời cho prompt lặp lại. Họ lưu prompt trong git với một tập lệnh đánh giá ngắn chạy trước mỗi thay đổi, dùng cơ sở dữ liệu vector được quản lý cho truy xuất để không phải vận hành một cái, và ghi nhật ký chi phí mỗi yêu cầu để những người sáng lập thấy chi tiêu leo lên trước khi nó thành bất ngờ.

**Doanh nghiệp lớn.** Một công ty truyền thông chạy tính năng LLM lưu lượng cao đã cắt chi phí suy luận đáng kể. Họ định tuyến yêu cầu dễ đến một mô hình nhỏ và dành mô hình lớn hơn cho yêu cầu khó. Họ lưu đệm phản hồi cho truy vấn lặp lại và bật bộ nhớ đệm tiền tố cho prompt hệ thống dùng chung. Họ chạy GPU qua một bộ lập lịch dùng chung để giữ mức tận dụng cao, đánh phiên bản mọi prompt trong git với một bộ đánh giá tự động chặn cổng thay đổi, và gắn công cụ đo chi phí mỗi yêu cầu để mỗi đội sản phẩm sở hữu chi tiêu của mình.

**Chính phủ.** Một cơ quan quốc gia có quy tắc chủ quyền dữ liệu nghiêm ngặt triển khai các hệ thống AI của mình tại chỗ để dữ liệu nhạy cảm và mô hình không bao giờ rời môi trường được kiểm soát. Họ lập lịch GPU khan hiếm qua các bộ với hạn ngạch và ưu tiên, dự báo năng lực để biện minh mua sắm nhiều năm, và xây một nền tảng tìm kiếm vector cho truy xuất trên tài liệu chính thức. Prompt và mô hình được đánh phiên bản và đánh giá trước khi phát hành. Khả năng quan sát toàn diện theo dõi chi phí và chất lượng, và kiến trúc giữ mô hình sau một giao diện nội bộ để bảo toàn đường thoát và tránh khóa chặt.

## Luận chứng kinh doanh: động lực, ROI và TCO

Động lực cho hạ tầng AI có kỷ luật rất đơn giản. AI ở quy mô lớn tốn kém, và khoảng cách giữa triển khai được tối ưu và không được tối ưu thường là gấp nhiều lần về chi tiêu. ROI đến từ mức tận dụng bộ tăng tốc cao hơn, chi phí mỗi yêu cầu thấp hơn nhờ gom lô và bộ nhớ đệm, mô hình vừa kích thước, và tránh cung cấp thừa. Đường ống đánh giá và khả năng quan sát sinh lời bằng cách ngăn sự cố tốn kém và cho phép lặp lại an toàn.

TCO trải qua tính toán bộ tăng tốc (dòng lớn nhất với nhiều khối lượng công việc), lưu trữ vector, hạ tầng phục vụ, mạng, và nhân sự nền tảng cùng vận hành để chạy nó. Hãy cân nhắc điều đó so với chi phí của việc không đầu tư: hóa đơn suy luận mất kiểm soát, độ trễ kém làm suy yếu việc áp dụng, và không thể mở rộng. Với chính phủ, thêm chi phí của việc thất bại các yêu cầu chủ quyền hay bảo mật. Hãy lập luận với ban lãnh đạo bằng cách cho thấy xu hướng chi phí mỗi kết quả và một nền tảng đường lát sẵn cho phép nhiều đội triển khai AI hiệu quả, thay vì mỗi đội xây hạ tầng đắt đỏ, dùng thiếu.

## Phản mẫu và cạm bẫy

- **Bộ tăng tốc nhàn rỗi.** Dành GPU khan hiếm cho các đội để chúng dùng thiếu.
- **Không gom lô hay bộ nhớ đệm.** Phục vụ từng yêu cầu riêng lẻ và tính lại ngữ cảnh dùng chung.
- **Mô hình lớn nhất theo mặc định.** Dùng mô hình đắt nơi mô hình nhỏ là đủ.
- **Mù chi phí.** Không quy chi phí, ngân sách hay khả năng thấy chi phí mỗi yêu cầu cho đến khi hóa đơn đến.
- **Prompt không đánh phiên bản.** Đổi prompt trong môi trường sản xuất mà không có đánh phiên bản hay cổng đánh giá.
- **Bỏ bê độ trễ đuôi.** Tối ưu độ trễ trung bình trong khi người dùng chịu đựng cái đuôi chậm.
- **Khóa chặt thầm lặng.** Xây sâu trên ngăn xếp phục vụ của một nhà cung cấp mà không có khả năng di chuyển.

## Mô hình trưởng thành

1. **Khởi đầu.** Phân bổ GPU tùy nghi phản ứng với ai đòi to nhất, không gom lô hay bộ nhớ đệm, không thấy chi phí cho đến khi hóa đơn đến, prompt được sửa trực tiếp và không đánh phiên bản, giám sát tối thiểu.
2. **Phát triển.** Một số đội áp dụng lập lịch dùng chung, bộ nhớ đệm và prompt quản lý phiên bản, nhưng thực hành không nhất quán toàn tổ chức: một nhóm gom lô và đánh giá trong khi nhóm khác vẫn phục vụ từng yêu cầu riêng lẻ và đổi prompt bằng tay.
3. **Chuẩn hóa.** Một nền tảng đường lát sẵn có tài liệu được thực thi toàn tổ chức: lập lịch dùng chung với hạn ngạch và ưu tiên, gom lô, bộ nhớ đệm và chọn kích thước vừa chuẩn, hạ tầng vector cho truy xuất, đường ống đánh giá tự động chặn cổng mọi thay đổi prompt hay mô hình, và quy chi phí cho đội và trường hợp sử dụng.
4. **Quản lý.** Nền tảng được đo và kiểm soát theo đường cơ sở: mức tận dụng bộ tăng tốc, chi phí mỗi kết quả hữu ích, độ trễ đuôi, độ phủ truy xuất, và hồi quy chất lượng mỗi thay đổi được theo dõi với cảnh báo và ngưỡng, chi phí do mỗi đội sở hữu, và quyết định tiếp tục hay dừng với một thay đổi dựa trên bằng chứng thay vì trực giác.
5. **Điều phối.** Hạ tầng liên tục cải thiện và thích ứng: định tuyến, gom lô và co giãn tự điều chỉnh theo tín hiệu chi phí và chất lượng trực tiếp, năng lực được cân bằng lại giữa các đội và giữa các mục tiêu đám mây, tại chỗ và chủ quyền khi nhu cầu và ràng buộc dịch chuyển, khả năng di chuyển được diễn tập, và hoạch định hạ tầng được tích hợp với sản phẩm, bảo mật và mua sắm.

## Ý tưởng để thảo luận

- Làm sao bạn đẩy mức tận dụng bộ tăng tốc lên mà không bỏ đói khối lượng công việc ưu tiên?
- Sự cân bằng gom lô và bộ nhớ đệm đúng cho yêu cầu độ trễ của bạn nằm ở đâu?
- Khi nào triển khai tại chỗ hoặc chủ quyền biện minh được chi phí của nó so với đám mây?
- Làm sao bạn quy và kiểm soát chi tiêu AI qua nhiều đội?
- Cái gì nên chặn cổng một thay đổi prompt hay mô hình đến môi trường sản xuất?
- Làm sao bạn giữ hạ tầng phục vụ đủ di chuyển được để đổi nhà cung cấp?

## Những điểm cần ghi nhớ

- Bộ tăng tốc khan hiếm và đắt; hãy lập lịch, chia sẻ và tận dụng chúng có chủ đích.
- Gom lô, bộ nhớ đệm và chọn kích thước mô hình vừa phải là các đòn bẩy chính cho chi phí và độ trễ.
- Ứng dụng truy xuất cần hạ tầng embedding và tìm kiếm vector được vận hành tốt.
- LLMOps (đánh phiên bản prompt, đường ống đánh giá và khả năng quan sát) là xương sống vận hành của AI sinh tạo.
- Quản lý chi phí một cách quan sát được và bảo toàn khả năng di chuyển để tránh khóa chặt.

## Tài liệu tham khảo và đọc thêm

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, biên tập).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
