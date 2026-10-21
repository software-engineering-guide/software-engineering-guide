# 6.5 AI có trách nhiệm và đáng tin cậy

## Tổng quan và động lực

AI có trách nhiệm và đáng tin cậy là thực hành xây dựng và vận hành các hệ thống AI công bằng, minh bạch, có trách nhiệm giải trình, an toàn và tôn trọng quyền riêng tư. Nó cũng có nghĩa là có thể chứng minh tất cả những điều này với những người bị ảnh hưởng và với cơ quan quản lý. Khi AI đảm nhận các quyết định định hình cuộc sống con người (tuyển dụng, cho vay, đủ điều kiện hưởng trợ cấp), câu hỏi không còn chỉ là "nó có hoạt động không?" mà là "nó có đúng không, và chúng ta có biện minh được không?" Một hệ thống chính xác trung bình vẫn có thể bất công với một nhóm con, không giải thích được cho người bị ảnh hưởng, hoặc không an toàn khi bị lạm dụng. Bạn giành được niềm tin bằng cách xử lý những chiều này một cách có chủ đích, không phải bằng hy vọng chúng tự lo.

Với các đội lớn, AI có trách nhiệm không thể là việc của một người hay một ô đánh dấu ở cuối. Hãy dệt nó vào cách bạn thiết kế, đánh giá, triển khai và quản trị hệ thống, với quyền sở hữu và đường leo thang rõ ràng. Ở quy mô lớn, những thiên kiến nhỏ và khoảng trống nhỏ trong giám sát ảnh hưởng đến nhiều người. Một thất bại gây chú ý duy nhất có thể làm tổn hại danh tiếng và mời gọi quy định. Các khung quản trị tồn tại chính vì thiện chí tùy nghi không mở rộng được.

Các tổ chức chính phủ và chịu quy định đối mặt nghĩa vụ ràng buộc. Luật mới nổi, như [Đạo luật AI của EU](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act), áp đặt yêu cầu phân bậc theo rủi ro. Các tiêu chuẩn như Khung Quản lý Rủi ro AI của NIST và ISO/IEC 42001 cho bạn những cách có cấu trúc để đáp ứng chúng. Các cơ quan công phải tránh phân biệt đối xử trái luật, cung cấp đường để phản đối các quyết định tự động, và minh bạch về cách AI được dùng trong việc thực thi quyền lực công. AI có trách nhiệm trong các bối cảnh này vừa là nghĩa vụ đạo đức vừa là yêu cầu pháp lý.

*Xem thêm:* chương 6.1 (chiến lược và mức độ sẵn sàng AI), chương 10.5 (đạo đức, trách nhiệm giải trình và lợi ích công), và chương 4.5 (quyền riêng tư và bảo vệ dữ liệu).

## Các nguyên tắc chính

- Công bằng là mục tiêu thiết kế cần được đo và quản lý, không được giả định.
- Những người bị ảnh hưởng bởi quyết định của AI xứng đáng được giải thích và có đường để phản đối chúng.
- Trách nhiệm giải trình thuộc về con người và tổ chức, không bao giờ thuộc về mô hình.
- Quyền riêng tư và an toàn phải được thiết kế vào, gồm bảo vệ chống lạm dụng và sử dụng sai.
- Quản trị nên theo các khung đã được công nhận để bảo vệ được và kiểm toán được.
- Giám sát của con người phải có ý nghĩa, với thẩm quyền thực sự để ghi đè và dừng.
- Cân nhắc các chi phí rộng hơn của AI, gồm dấu chân môi trường của nó.

## Khuyến nghị

### Phát hiện và giảm thiểu thiên kiến và bất công

Hãy xác định công bằng nghĩa là gì trong bối cảnh của bạn. Có nhiều định nghĩa toán học, đôi khi xung đột, và định nghĩa đúng phụ thuộc vào quyết định và luật. Hãy kiểm thử mô hình về hiệu năng chênh lệch giữa các nhóm được bảo vệ và dễ tổn thương bằng dữ liệu đại diện. Làm điều này trước khi triển khai và tiếp tục sau đó, vì [thiên kiến](https://en.wikipedia.org/wiki/Algorithmic_bias) có thể nổi lên khi quần thể dịch chuyển. Giảm thiểu qua dữ liệu tốt hơn, đánh trọng số lại, ràng buộc, hoặc đổi cách hệ thống được dùng, và lập tài liệu các đánh đổi bạn đã chấp nhận. Loại bỏ một thuộc tính được bảo vệ không loại bỏ thiên kiến, vì các biến đại diện vẫn còn. Hãy coi công bằng là kỷ luật đo lường và quản lý liên tục, không phải một lần thông qua.

### Cung cấp khả năng giải thích, diễn giải và minh bạch

Hãy khớp mức giải thích với rủi ro và khán giả. Với các quyết định hệ quả, hãy cho người bị ảnh hưởng một lý do rõ ràng, bằng ngôn ngữ đơn giản mà họ hiểu và hành động được. Với quản trị nội bộ, hãy giữ đủ [khả năng diễn giải](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) kỹ thuật để gỡ lỗi và bảo vệ hệ thống. Ưu tiên các mô hình vốn dĩ diễn giải được nơi rủi ro cao và việc diễn giải khả thi. Nơi cần các mô hình phức tạp, hãy dùng kỹ thuật giải thích trong khi trung thực về giới hạn của chúng. Hãy minh bạch về việc khi nào AI được dùng, đặc biệt trong tương tác với công chúng.

### Quản trị bằng các khung đã được công nhận

Hãy áp dụng một cách tiếp cận quản trị có cấu trúc thay vì tự phát minh. **Khung Quản lý Rủi ro AI của NIST** tổ chức công việc quanh việc quản trị, lập bản đồ, đo lường và quản lý rủi ro AI. **Đạo luật AI của EU** phân loại hệ thống theo rủi ro và áp đặt nghĩa vụ tương ứng, với yêu cầu nghiêm ngặt cho các mục đích dùng rủi ro cao. **ISO/IEC 42001** xác định một hệ thống quản lý AI có thể được kiểm toán và chứng nhận. Hãy ánh xạ hệ thống của bạn vào các khung này. Duy trì tài liệu như thẻ mô hình và thẻ dữ liệu (bản tóm tắt chuẩn hóa về mục đích, hiệu năng và hạn chế của mô hình hay tập dữ liệu). Chạy đánh giá rủi ro trước khi triển khai, và giữ bản kiểm kê các hệ thống AI với mức rủi ro và chủ sở hữu của chúng. Quản trị tốt giao vai trò, quyền quyết định và đường leo thang rõ ràng.

### Bảo đảm giám sát của con người, trách nhiệm giải trình và khiếu nại

Hãy giữ một con người kiểm soát có ý nghĩa các quyết định hệ quả, với thẩm quyền thực sự và thông tin cần thiết để ghi đè hệ thống, không phải một con dấu cao su. Giao trách nhiệm rõ ràng: nêu tên một chủ sở hữu chịu trách nhiệm về hành vi của mỗi hệ thống. Cho những người bị ảnh hưởng bởi quyết định tự động quyền được giải thích và một quy trình khả thi để khiếu nại lên một con người có thể thay đổi kết quả. Ghi nhật ký các quyết định và cơ sở của chúng, để bạn xử lý khiếu nại và kiểm toán một cách công bằng và kịp thời.

### Bảo vệ quyền riêng tư, an toàn và chống lạm dụng

Hãy tối thiểu hóa dữ liệu cá nhân bạn thu thập và dùng, thiết lập cơ sở pháp lý, và áp dụng kỹ thuật quyền riêng tư phù hợp với mức độ nhạy cảm liên quan. Hãy [đội đỏ](https://en.wikipedia.org/wiki/Red_team) các hệ thống trước và sau khi triển khai để tìm cách chúng có thể bị thao túng, bẻ khóa, hay bị lạm dụng để gây hại, và sửa những gì bạn tìm thấy. Xây các biện pháp bảo vệ chống tạo ra nội dung có hại, rò rỉ dữ liệu nhạy cảm, hay tạo điều kiện cho lạm dụng. Lập kế hoạch cho sự cố: giám sát, ứng phó và công bố. Cân nhắc [lưỡng dụng](https://en.wikipedia.org/wiki/Dual-use_technology) (cùng một năng lực phục vụ cả mục đích có lợi và có hại) và việc lạm dụng ở hạ nguồn, không chỉ việc dùng theo dự định.

### Tính đến chi phí môi trường

Huấn luyện và phục vụ các mô hình lớn tiêu thụ năng lượng và nước đáng kể. Hãy đo và báo cáo dấu chân của các khối lượng công việc AI lớn. Ưu tiên mô hình và phần cứng hiệu quả nơi chúng đáp ứng nhu cầu. Chọn kích thước mô hình vừa với nhiệm vụ thay vì mặc định dùng cái lớn nhất, và đưa chi phí môi trường vào quyết định kiến trúc và mua sắm.

## Đánh đổi: ưu và nhược điểm

| Căng thẳng | Một phía | Phía kia |
|---|---|---|
| Độ chính xác so với công bằng | Độ chính xác trung bình cao nhất | Kết quả công bằng giữa các nhóm |
| Hiệu năng so với khả năng diễn giải | Mô hình phức tạp, mạnh | Mô hình giải thích được, bảo vệ được |
| Tự động hóa so với giám sát | Hiệu quả và quy mô | Kiểm soát và trách nhiệm giải trình của con người |
| Tiện ích dữ liệu so với quyền riêng tư | Mô hình phong phú hơn từ nhiều dữ liệu hơn | Tối thiểu hóa và bảo vệ dữ liệu |
| Năng lực so với an toàn | Chức năng rộng, mở | Hành vi bị ràng buộc, được bảo vệ |
| Tốc độ so với quản trị | Triển khai nhanh | Rà soát và lập tài liệu kỹ lưỡng |

Hiếm khi có bữa trưa miễn phí. Cải thiện công bằng có thể tốn một ít độ chính xác. Khả năng diễn giải có thể tốn một ít hiệu năng. Quản trị tốn thời gian. Con đường có trách nhiệm là đưa ra các đánh đổi này một cách có ý thức, lập tài liệu chúng, và chọn nghiêng về người bị ảnh hưởng và khả năng bảo vệ khi rủi ro cao. Đóng khung quản trị là cái phanh cho đổi mới là một sự lưỡng phân sai. Rủi ro AI không được quản lý tự nó là mối đe dọa đối với đổi mới bền vững.

## Câu hỏi để thảo luận với đội của bạn

1. **Hệ thống AI nào đã triển khai của chúng ta sẽ bị Đạo luật AI của EU phân loại là rủi ro cao, và hôm nay chúng ta có đang đáp ứng các nghĩa vụ đó không?** Luật phân bậc theo rủi ro nay đã ràng buộc, không còn giả thuyết, và một hệ thống quyết định tuyển dụng, cho vay hay đủ điều kiện hưởng trợ cấp có thể mang yêu cầu nghiêm ngặt mà bạn có thể đang vi phạm. Với một tổ chức lớn, câu hỏi này buộc một bản kiểm kê trung thực thay vì giả định dễ chịu rằng quản trị đã "được xử lý." Hãy mang danh sách hệ thống AI với mức rủi ro và chủ sở hữu, được ánh xạ với Đạo luật AI của EU, Khung Quản lý Rủi ro AI của NIST và ISO/IEC 42001 nơi liên quan. Tín hiệu cần theo dõi là bất kỳ hệ thống hệ quả nào không có phân loại rủi ro, không có đánh giá tác động và không có thẻ mô hình hay thẻ dữ liệu. Với các cơ quan công thực thi quyền lực công, thiếu nghĩa vụ không phải mục tồn đọng mà là phơi nhiễm pháp lý, và câu trả lời nên kích hoạt các đánh giá và tài liệu mà các hệ thống đó yêu cầu.

2. **Khi một trong các mô hình của chúng ta từ chối ai đó, người đó có nhận được lý do bằng ngôn ngữ đơn giản và tiếp cận được một con người thực sự đảo ngược được kết quả không?** Quyền được giải thích và một đường khiếu nại khả thi là thứ phân biệt AI có trách nhiệm giải trình với một hộp đen gây hại cho người ta mà không có cách khắc phục. Công bằng đo theo trung bình vẫn có thể thất bại với một cá nhân, và khả năng diễn giải được chọn sau triển khai thường là sân khấu. Hãy mang một quyết định đã triển khai cụ thể và truy vết nó: lý do người bị ảnh hưởng nhận được, kênh khiếu nại, và liệu con người ở đầu kia có thẩm quyền thực sự và cơ sở đã ghi nhật ký để ghi đè. Trong bối cảnh chính phủ và chịu quy định, đường khiếu nại thường là yêu cầu pháp lý, không phải phép lịch sự. Nếu lý do không hiểu nổi hoặc khiếu nại dẫn đến con dấu cao su, đó là khoảng trống cần sửa trước bản phát hành kế tiếp.

3. **Ai là người có tên duy nhất chịu trách nhiệm khi một mô hình gây hại, và họ có thẩm quyền thực sự để dừng nó không?** Trách nhiệm giải trình thuộc về con người và tổ chức, không bao giờ thuộc về mô hình, nhưng nguyên tắc đó trống rỗng cho đến khi một cái tên được gắn với mỗi hệ thống và người đó thực sự rút được phích cắm. Với một đội lớn, quyền sở hữu phân tán nghĩa là khi một thất bại công bằng hay một vụ bẻ khóa nổi lên, ai cũng giả định người khác đang theo dõi. Hãy mang bản đồ sở hữu, đường leo thang, và bằng chứng rằng giám sát có ý nghĩa: chủ sở hữu có tên có nhận được thông tin và quyền lực để ghi đè hay dừng hệ thống, hay chỉ để gật đầu? Hãy thảo luận cách bạn đội đỏ cho sự lạm dụng và lợi dụng mà bạn chưa tưởng tượng ra, vì chỉ kiểm thử việc dùng theo dự định bỏ sót những thất bại lên báo. Câu trả lời không nên để hệ thống hệ quả nào thiếu một chủ sở hữu chịu trách nhiệm có thể dừng nó.

4. **Với mỗi mô hình hệ quả, chúng ta đã chọn định nghĩa công bằng nào, ai ký duyệt nó, và các chỉ số nhóm con của chúng ta có thực sự đúng trong môi trường sản xuất không?** Công bằng có nhiều định nghĩa toán học xung đột nhau, nên một mô hình thỏa mãn tỷ lệ dương tính giả bằng nhau có thể vi phạm kết quả bằng nhau, và chọn một định nghĩa là phán đoán giá trị không nên để cho bất kỳ ai viết vòng huấn luyện. Với một đội lớn, một mặc định không được xem xét giấu lựa chọn trong mã và khiến mọi nhóm hạ nguồn thừa hưởng một quyết định không ai tranh luận. Hãy mang chỉ số công bằng bạn đã tối ưu, các nhóm được bảo vệ và dễ tổn thương bạn đã kiểm thử, dữ liệu đại diện bạn đã dùng, và độ trôi bạn đã thấy từ khi ra mắt, vì loại bỏ một thuộc tính được bảo vệ để lại các biến đại diện giữ thiên kiến sống. Trong bối cảnh doanh nghiệp và chính phủ, hãy nêu tên người có thẩm quyền chấp nhận một đánh đổi công bằng và ghi lại nó, vì cơ quan quản lý hay thanh tra sẽ hỏi ai đã quyết định rằng định nghĩa công bằng này là đúng cho những người bị từ chối khoản vay, trợ cấp hay việc làm. Nếu không có chỉ số nhóm con nào được giám sát sau triển khai, hãy coi mô hình là chưa được đo chứ không phải công bằng.

5. **Mỗi hệ thống có thể chạy trên ít dữ liệu cá nhân đến mức nào, và chúng ta đã đội đỏ nó cho sự lạm dụng và lưỡng dụng mà chúng ta thà không nghĩ tới chưa?** Quyền riêng tư và an toàn phải được thiết kế vào, và cách rẻ nhất để giảm cả rủi ro vi phạm lẫn bề mặt lạm dụng là thu thập và lưu giữ ít dữ liệu hơn ngay từ đầu, vậy mà các đội thường xuyên tích trữ đầu vào "phòng khi chúng hữu ích sau này." Với một tổ chức lớn, mỗi trường thêm là một câu hỏi cơ sở pháp lý, một nghĩa vụ lưu giữ, và một giải thưởng lớn hơn cho kẻ tấn công hay vụ bẻ khóa. Hãy mang bản kiểm kê dữ liệu và cơ sở pháp lý cho mỗi hệ thống, kết quả đội đỏ về thao túng, rò rỉ và sinh nội dung có hại, và một danh sách trung thực các năng lực lưỡng dụng nơi cùng một tính năng giúp người dùng chính đáng cũng giúp kẻ hành động ác ý. Trong bối cảnh chịu quy định và công, hãy gắn điều này với kế hoạch sự cố: giám sát, ứng phó và công bố, vì một cơ quan công làm rò dữ liệu nhạy cảm hay phát hành hệ thống bẻ khóa được đối mặt nghĩa vụ theo luật, không chỉ sự xấu hổ. Nếu đội đỏ chỉ từng thử đường theo dự định, bạn đã kiểm thử bản demo, không phải hệ thống.

6. **Chúng ta có đo và nhận lấy dấu chân môi trường của các khối lượng công việc AI lớn không, hay "dùng mô hình lớn nhất" là một mặc định không được định giá?** Huấn luyện và phục vụ mô hình lớn tiêu thụ năng lượng và nước thật, và mặc định dùng mô hình lớn nhất cho nhiệm vụ một mô hình nhỏ hơn xử lý được biến một lối tắt kỹ thuật thành chi phí lặp lại mà tổ chức không bao giờ thấy trên bảng điều khiển. Với một đội lớn chạy nhiều khối lượng công việc, những kém hiệu quả nhỏ mỗi lệnh gọi cộng dồn thành dấu chân trở thành gánh nặng mua sắm và báo cáo khi kỳ vọng công bố thắt lại. Hãy mang dấu chân đo được của các khối lượng công việc nặng nhất, một so sánh kích thước mô hình với độ chính xác nhiệm vụ thực sự cần, và các lựa chọn phần cứng cùng phục vụ bạn có thể điều chỉnh cho vừa. Trong bối cảnh doanh nghiệp và chính phủ, hãy nối điều này với cam kết bền vững và tiêu chí mua sắm, vì các cơ quan công ngày càng phải báo cáo tác động môi trường và biện minh chi tiêu, và một dấu chân chưa đo là con số một ngày nào đó bạn sẽ được yêu cầu đưa ra mà không thể. Hãy quyết định liệu chi phí môi trường có là đầu vào chính thức cho lựa chọn mô hình hay không, hoặc thừa nhận rằng hôm nay nó chưa phải.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Bạn không thể bố trí nhân sự cho một hội đồng quản trị, vì vậy hãy làm phiên bản nhẹ vẫn có giá trị. Chọn mô hình diễn giải được nơi quyết định có hệ quả, viết một thẻ mô hình một trang, kiểm thử kết quả chênh lệch giữa các nhóm bạn đo được, và ghi nhật ký quyết định để bạn xem xét lại công bằng khi lớn lên. Hãy cho bất kỳ quyết định bất lợi nào một lý do đơn giản và một đường đến con người. Bỏ qua điều này không phải là tốc độ, mà là một khoản nợ bạn không gánh nổi nếu một quyết định bất công duy nhất đến báo chí hay cơ quan quản lý.

**Doanh nghiệp nhỏ.** Không có chuyên gia riêng, hãy coi AI có trách nhiệm là một câu hỏi mua sắm: ưu tiên nhà cung cấp lập tài liệu kiểm thử công bằng, công khai thẻ mô hình và thẻ dữ liệu, và cho bạn thông báo với khách hàng khi AI đang được dùng. Biết công cụ của bạn thu thập dữ liệu cá nhân nào và bạn có cơ sở pháp lý để dùng nó không. Nơi một câu trả lời tự động sai có thể gây hại cho khách hàng, hãy giữ một người trong vòng lặp thay vì tin một công cụ bạn không kiểm tra hay giải thích được.

**Doanh nghiệp lớn.** Nhiệm vụ là quản trị ở quy mô qua nhiều đội: ánh xạ mọi hệ thống vào Khung Quản lý Rủi ro AI của NIST, Đạo luật AI của EU và ISO/IEC 42001, giữ bản kiểm kê với mức rủi ro và chủ sở hữu có tên, và yêu cầu kiểm thử công bằng, an toàn và quyền riêng tư trước và sau khi ra mắt. Hãy chuẩn hóa thẻ mô hình và thẻ dữ liệu, đội đỏ và quy trình khiếu nại để các nhóm thôi phát minh lại chúng. Lập ngân sách tường minh cho chi phí quản trị, giám sát và khả năng diễn giải, và coi rủi ro AI không được quản lý là mối đe dọa đối với giấy phép hoạt động.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy công bố một thông báo minh bạch bằng ngôn ngữ đơn giản, chạy đánh giá tác động trước khi triển khai, và giữ việc ra quyết định có ý nghĩa của con người cho mọi hành động ảnh hưởng đến công dân, với một đường khiếu nại khả thi. Đòi nhà cung cấp tiết lộ hạn chế mô hình và trao khả năng di chuyển dữ liệu, tránh phân biệt đối xử trái luật, nêu tên một viên chức chịu trách nhiệm cho mỗi hệ thống, và báo cáo dấu chân môi trường của các khối lượng công việc lớn.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp cho vay nhỏ đang xây tính năng chấm điểm tín dụng ban đầu không thể bố trí nhân sự cho hội đồng quản trị, nên đã làm phiên bản nhẹ vẫn quan trọng. Hai người sáng lập cùng ký duyệt mô hình, kiểm thử nó về kết quả chênh lệch giữa các nhóm họ đo được, và viết một thẻ mô hình ngắn một trang bao quát dữ liệu, giới hạn và rủi ro đã biết của nó. Họ chọn một mô hình đơn giản hơn, dễ diễn giải hơn để có thể cho bất kỳ người nộp đơn bị từ chối nào một lý do đơn giản và một đường đến rà soát của con người, và họ ghi nhật ký quyết định để xem xét lại công bằng khi lớn lên.

**Doanh nghiệp lớn.** Một ngân hàng triển khai mô hình tín dụng thành lập một hội đồng quản trị AI, ánh xạ mô hình vào một danh mục rủi ro cao, và yêu cầu kiểm thử công bằng qua các nhóm nhân khẩu trước và sau khi ra mắt. Họ lập tài liệu mô hình trong một thẻ mô hình. Họ cho người nộp đơn bị từ chối một lý do bằng ngôn ngữ đơn giản và quyền khiếu nại lên một nhân viên thẩm định con người, và họ đội đỏ hệ thống về thao túng. Họ chọn một mô hình kém chính xác hơn một chút nhưng dễ diễn giải hơn, vì họ phải giải thích và bảo vệ mọi quyết định trước cơ quan quản lý.

**Chính phủ.** Một cơ quan công dùng AI để giúp phân bổ nguồn lực thanh tra căn chỉnh chương trình của mình theo NIST AI RMF và các điều khoản liên quan của luật AI hiện hành. Họ công bố một thông báo minh bạch mô tả cách hệ thống hoạt động và các biện pháp bảo vệ. Họ tiến hành đánh giá tác động trước khi triển khai, giữ việc ra quyết định có ý nghĩa của con người cho mọi hành động ảnh hưởng đến công dân, và cung cấp một quy trình khiếu nại. Công bằng được giám sát liên tục, chi phí môi trường của khối lượng công việc được báo cáo, và một viên chức chịu trách nhiệm được nêu tên là người giải trình cho hệ thống.

## Luận chứng kinh doanh: động lực, ROI và TCO

AI có trách nhiệm bảo vệ giá trị nhiều như nó tạo ra giá trị. ROI phần lớn là chi phí tránh được: ít khiếu nại phân biệt đối xử, hình phạt quy định và thảm họa danh tiếng hơn; kiểm toán trơn tru hơn; và niềm tin người dùng cùng công chúng cao hơn, thúc đẩy việc áp dụng. Hệ thống đáng tin cũng mạnh mẽ hơn, vì kỷ luật tạo ra công bằng và an toàn cũng tạo ra kỹ thuật tốt hơn.

TCO bao gồm nhân sự quản trị, kiểm thử công bằng và an toàn, tài liệu, đội đỏ, quy trình giám sát, và hiệu năng đôi khi bị đánh đổi vì khả năng diễn giải hay công bằng. Hãy cân nhắc điều đó so với chi phí của việc không đầu tư: trách nhiệm pháp lý, buộc ngừng hoạt động, mất niềm tin công chúng, và chi phí cao hơn nhiều của việc vá quản trị sau một thất bại. Trong bối cảnh chịu quy định, đầu tư vào AI có trách nhiệm ngày càng không thể thương lượng. Hãy lập luận với ban lãnh đạo bằng cách đóng khung nó là quản lý rủi ro và giấy phép hoạt động: điều kiện tiên quyết để triển khai AI ở quy mô lớn.

## Phản mẫu và cạm bẫy

- **Công bằng do bỏ sót.** Giả định một mô hình công bằng vì nó bỏ qua các thuộc tính được bảo vệ.
- **Sân khấu giải thích.** Tạo ra những giải thích không thực sự phản ánh cách quyết định được đưa ra.
- **Giám sát con dấu cao su.** Rà soát của con người trên danh nghĩa mà không có thẩm quyền hay thông tin thực để ghi đè.
- **Quản trị như chuyện nghĩ sau.** Vá tài liệu và rà soát sau khi thiết kế và triển khai.
- **Không có đường khiếu nại.** Để người bị ảnh hưởng không có cách phản đối một quyết định tự động.
- **Phớt lờ lạm dụng.** Chỉ kiểm thử việc dùng theo dự định và bỏ sót bẻ khóa và lợi dụng.
- **Mù dấu chân.** Mặc định dùng mô hình lớn nhất mà không quan tâm chi phí môi trường.

## Mô hình trưởng thành

1. **Khởi đầu.** Không kiểm thử công bằng, giải thích hay quản trị; trách nhiệm không được xác định; thiên kiến, lạm dụng và vấn đề quyền riêng tư chỉ nổi lên sau tác hại, và không có bản kiểm kê các hệ thống AI hay rủi ro của chúng.
2. **Phát triển.** Một số kiểm thử thiên kiến, thẻ mô hình và đội đỏ xảy ra trên từng hệ thống, nhưng thực hành không nhất quán qua các đội; giám sát tùy nghi; các khung như Khung Quản lý Rủi ro AI của NIST và Đạo luật AI của EU được biết đến nhưng chỉ áp dụng một phần.
3. **Chuẩn hóa.** Quản trị được lập tài liệu và thực thi toàn tổ chức: hệ thống được ánh xạ vào các khung đã được công nhận và ISO/IEC 42001, mỗi cái có mức rủi ro và chủ sở hữu có tên, và kiểm thử công bằng, an toàn, quyền riêng tư, thẻ mô hình và thẻ dữ liệu, đường khiếu nại, và đội đỏ cho hệ thống rủi ro cao là bắt buộc thay vì tùy chọn.
4. **Quản lý.** Chương trình được đo và kiểm soát bằng dữ liệu: chỉ số công bằng nhóm con, phát hiện an toàn và bẻ khóa, khối lượng khiếu nại và tỷ lệ đảo ngược, tỷ lệ ghi đè giám sát, và dấu chân khối lượng công việc được theo dõi theo đường cơ sở và ngưỡng; độ trôi và kết quả chênh lệch kích hoạt hành động xác định; các quyết định tiếp tục hay dừng dựa trên bằng chứng thay vì lời cam đoan.
5. **Điều phối.** AI có trách nhiệm được cải thiện liên tục và tích hợp trong toàn tổ chức: giám sát công bằng, an toàn và lạm dụng chạy trong môi trường sản xuất, quản trị được xây vào phân phối, chi phí môi trường là đầu vào chính thức cho lựa chọn mô hình, và tổ chức điều chỉnh các kiểm soát khi luật, rủi ro và năng lực dịch chuyển, với trách nhiệm do mọi người sở hữu thay vì một đội duy nhất.

## Ý tưởng để thảo luận

- Định nghĩa công bằng nào áp dụng cho một quyết định nhất định, và ai quyết định?
- Bao nhiêu độ chính xác hay hiệu năng là chấp nhận được để đánh đổi lấy công bằng hay khả năng diễn giải?
- Điều gì làm giám sát của con người có ý nghĩa thay vì một con dấu cao su?
- Khiếu nại chống lại quyết định tự động nên được thiết kế thế nào để công bằng và kịp thời?
- Làm sao bạn đội đỏ cho sự lạm dụng bạn chưa tưởng tượng ra?
- Chi phí môi trường có nên ảnh hưởng đến lựa chọn mô hình, và bạn sẽ cân nhắc nó thế nào?

## Những điểm cần ghi nhớ

- AI đáng tin cậy là công bằng, giải thích được, có trách nhiệm giải trình, an toàn và tôn trọng quyền riêng tư, ngay từ thiết kế.
- Công bằng và an toàn là kỷ luật đo lường và quản lý liên tục, không phải kiểm tra một lần.
- Căn chỉnh quản trị theo NIST AI RMF, Đạo luật AI của EU và ISO/IEC 42001 để bảo vệ được và kiểm toán được.
- Giữ giám sát có ý nghĩa của con người, trách nhiệm giải trình rõ ràng, và quyền khiếu nại thực sự.
- Thiết kế cho quyền riêng tư và chống lạm dụng, và tính đến chi phí môi trường.

## Tài liệu tham khảo và đọc thêm

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- European Union, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt và Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Maths Destruction*.
- Emma Strubell, Ananya Ganesh và Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
