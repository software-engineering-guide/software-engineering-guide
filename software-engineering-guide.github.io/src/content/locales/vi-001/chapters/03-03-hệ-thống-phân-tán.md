# 3.3 Hệ thống phân tán

## Tổng quan và động lực

Một [hệ thống phân tán](https://en.wikipedia.org/wiki/Distributed_computing) là bất kỳ hệ thống nào có các thành phần chạy trên nhiều hơn một máy và phối hợp qua mạng. Khoảnh khắc bạn vượt qua ranh giới tiến trình qua mạng, bạn thừa hưởng một số sự thật khắc nghiệt vốn không tồn tại trong một tiến trình đơn lẻ. Mạng không đáng tin cậy, và độ trễ của nó thay đổi. Thông điệp có thể bị mất, nhân đôi, trì hoãn hoặc đảo thứ tự. Các thành phần từ xa tự thất bại. Không có đồng hồ chung. "[Những ngụy biện của điện toán phân tán](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)" kinh điển (mạng đáng tin cậy, độ trễ bằng không, băng thông vô hạn, cấu trúc liên kết không bao giờ đổi) gọi tên chính xác những giả định gây ra sự cố ngừng hoạt động. Công việc của bạn là thiết kế cho những thực tế này ngay từ đầu, thay vì phát hiện lại chúng trong một sự cố.

Với một tổ chức lớn, phân tán không phải là tùy chọn. Bất kỳ hệ thống nào phục vụ quy mô quốc gia hay toàn cầu, kết nối nhiều bộ phận, hoặc cần tính sẵn sàng cao sẽ trải rộng trên nhiều máy, trung tâm dữ liệu và thường là nhiều vùng. Doanh nghiệp vận hành các hệ thống giao dịch phân tán, đường ống sự kiện và triển khai đa vùng. Chính phủ vận hành các tích hợp liên cơ quan nơi mỗi cơ quan sở hữu hệ thống riêng và không ai kiểm soát toàn bộ. Ở đây khoảng cách giữa một thiết kế vững chắc và một thiết kế mong manh hiện ra thành các sự cố lên tiêu đề báo, các khoản trợ cấp bị lỡ và hậu quả quy định. Các kỹ thuật trong chương này (suy luận về nhất quán, [tính lũy đẳng](https://en.wikipedia.org/wiki/Idempotence), thử lại với độ lùi, [bộ ngắt mạch](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern), [saga](https://en.wikipedia.org/wiki/Long-running_transaction) và khả năng quan sát phân tán) là các biện pháp phòng thủ tiêu chuẩn của bạn.

Phần khó nhất của hệ thống phân tán là các thất bại mang tính một phần và gián đoạn. Một chương trình trên một máy hoặc chạy hoặc sập. Một hệ thống phân tán có thể hoạt động một nửa: một số yêu cầu thành công, một số hết thời gian chờ, và một số bị mất âm thầm, tất cả cùng lúc. Chương này tập trung vào lập luận và các mẫu cho phép một đội lớn xây dựng các hệ thống suy giảm nhẹ nhàng và vẫn dễ hiểu dưới thất bại một phần.

## Các nguyên tắc chính

- **Mạng không đáng tin cậy.** Hãy thiết kế mọi tương tác từ xa với giả định nó có thể chậm, thất bại, nhân đôi hoặc đảo thứ tự.
- **Bạn không thể có nhất quán hoàn hảo và sẵn sàng hoàn hảo trong một phân vùng mạng.** Hãy chọn có chủ đích cho từng tương tác (CAP/PACELC), và nhớ rằng độ trễ là một chi phí ngay cả khi không có phân vùng.
- **Làm cho các thao tác lũy đẳng.** Nếu một thao tác có thể thử lại an toàn, hầu hết việc xử lý thất bại phân tán trở nên khả thi.
- **Mọi lệnh gọi từ xa cần một thời gian chờ.** Chờ không giới hạn biến một phụ thuộc chậm thành sự cố toàn hệ thống.
- **Ưu tiên nhất quán cuối cùng ở nơi nghiệp vụ cho phép, nhưng hãy làm cho nó tường minh.** Người dùng và kiểm toán viên phải hiểu khi nào họ có thể thấy dữ liệu cũ.
- **Cô lập các thất bại.** Vách ngăn và bộ ngắt mạch ngăn một thành phần đang thất bại lan sang tất cả các thành phần.
- **Bạn không thể gỡ lỗi những gì bạn không thấy.** Các luồng phân tán đòi hỏi truy vết, chỉ số và nhật ký tương quan qua mọi bước nhảy.
- **"Giao nhận đúng-một-lần" là huyền thoại; *xử lý* đúng-một-lần là một thành tựu kỹ thuật.** Hãy thiết kế cho ít-nhất-một-lần cùng khử trùng lặp.

## Khuyến nghị

### Suy luận về nhất quán với CAP và PACELC

[Định lý CAP](https://en.wikipedia.org/wiki/CAP_theorem) nói rằng trong một phân vùng mạng, một hệ thống phải chọn giữa nhất quán (mọi lần đọc thấy lần ghi mới nhất) và tính sẵn sàng (mọi yêu cầu nhận được phản hồi). [PACELC](https://en.wikipedia.org/wiki/PACELC_design_principle) thêm một đánh đổi thứ hai: **E**lse (khi không có phân vùng) bạn vẫn đánh đổi **L**atency (độ trễ) với **C**onsistency (nhất quán). Đừng đóng dấu điều này như một nhãn cho cả hệ thống. Hãy quyết định theo từng thao tác. Một lần chuyển số dư ngân hàng cần nhất quán mạnh và sẽ từ chối thay vì liều chi tiêu kép. Một bảng tin mạng xã hội hay bộ đếm lượt xem sản phẩm có thể chấp nhận dữ liệu cũ để đổi lấy tính sẵn sàng và tốc độ. Hãy ghi lại mô hình nhất quán mà mỗi luồng dữ liệu dùng (mạnh, nhân quả, đọc-ghi-của-chính-mình, hoặc cuối cùng) để không ai giả định một bảo đảm mà hệ thống thực sự không cung cấp.

### Xây dựng tính lũy đẳng, thời gian chờ, thử lại và độ lùi cùng nhau

Hãy coi bốn kỹ thuật này là một gói. Cho mọi thao tác từ xa một **thời gian chờ**, để một phụ thuộc bị treo không thể chặn một luồng mãi mãi. Khi thất bại, **thử lại**, nhưng chỉ với các thao tác an toàn để lặp lại. An toàn để lặp lại nghĩa là **lũy đẳng**: gán cho mỗi yêu cầu một khóa duy nhất và để bên nhận khử trùng lặp, để một lệnh "tính phí thẻ" được thử lại không tính phí hai lần. Giãn cách các lần thử lại bằng **[độ lùi lũy thừa](https://en.wikipedia.org/wiki/Exponential_backoff) và nhiễu (jitter)**, để tránh một cơn bão thử lại đồng bộ biến một gợn sóng ngắn thành một cuộc [từ chối dịch vụ](https://en.wikipedia.org/wiki/Denial-of-service_attack) tự gây ra. Giới hạn số lần thử lại và tổng ngân sách thời gian, vì thử lại mãi mãi chỉ dời thất bại đi chỗ khác. Không có tính lũy đẳng, thử lại là nguy hiểm. Không có độ lùi, thử lại là phá hoại.

### Thêm bộ ngắt mạch và vách ngăn để chặn lan truyền

Một **bộ ngắt mạch** theo dõi các lệnh gọi đến một phụ thuộc và, sau một ngưỡng thất bại, "mở": nó thất bại nhanh trong một khoảng thời gian làm nguội thay vì chất thêm yêu cầu lên một dịch vụ đang vật lộn, rồi "mở một nửa" để thử sự phục hồi. Điều này chặn chuỗi lan truyền trong đó một dịch vụ hạ nguồn chậm làm cạn kiệt các luồng của mọi bên gọi cho đến khi toàn hệ thống đình trệ. **Vách ngăn** phân vùng tài nguyên (nhóm luồng, nhóm kết nối) để sự bão hòa ở một phụ thuộc không thể ăn mất dung lượng mà các phụ thuộc khác cần. Hãy kết hợp cả hai với suy giảm nhẹ nhàng: khi một phụ thuộc không quan trọng không khả dụng, hãy trả về phản hồi được lưu đệm hoặc mặc định thay vì làm hỏng toàn bộ yêu cầu.

### Quản lý giao dịch phân tán bằng saga, không phải cam kết hai pha

Bạn thường không thể giữ một giao dịch [ACID](https://en.wikipedia.org/wiki/ACID) (Tính nguyên tử, Nhất quán, Cô lập, Bền vững) duy nhất qua nhiều dịch vụ hoặc cơ sở dữ liệu. [Cam kết hai pha](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) phân tán thì chậm, khóa tài nguyên và cắt giảm tính sẵn sàng. Hãy dùng **mẫu saga** thay thế. Mô hình hóa một giao dịch kinh doanh như một chuỗi các giao dịch cục bộ, mỗi giao dịch phát một sự kiện kích hoạt giao dịch kế tiếp, với một **hành động bù trừ** cho mỗi bước để hoàn tác nếu một bước sau thất bại. Saga có hai dạng. **Biên đạo** để các dịch vụ phản ứng với sự kiện của nhau, không có bộ điều khiển trung tâm. **Điều phối** để một bộ điều phối trung tâm dẫn dắt các bước, dễ suy luận và giám sát hơn. Saga chấp nhận nhất quán cuối cùng: hệ thống đi qua các trạng thái trung gian rồi hội tụ. Vì vậy hãy thiết kế trải nghiệm người dùng và dấu vết kiểm toán để tính đến các trạng thái "đang tiến hành" và "đã bù trừ".

### Coi đúng-một-lần là ít-nhất-một-lần cộng khử trùng lặp

[Bộ môi giới thông điệp](https://en.wikipedia.org/wiki/Message_broker) không thể thực sự bảo đảm giao nhận đúng-một-lần qua các thất bại. Những gì chúng và bạn *có thể* đạt được là **giao nhận ít-nhất-một-lần với xử lý lũy đẳng**, tạo ra các *hiệu ứng* đúng-một-lần. Hãy thiết kế bên tiêu thụ để xử lý an toàn các thông điệp trùng lặp, dùng khóa lũy đẳng hoặc nhật ký thông điệp đã xử lý. Hãy biết chính xác các bảo đảm thứ tự và giao nhận của bộ môi giới. Với streaming, hãy dùng nhóm người tiêu thụ, phân vùng và quản lý offset một cách có chủ đích, và làm cho việc xử lý lại an toàn, để bạn có thể phát lại một luồng sau khi sửa lỗi mà không làm hỏng trạng thái hạ nguồn.

### Đo đạc các luồng phân tán từ đầu đến cuối

Hãy áp dụng ba trụ cột của khả năng quan sát, được tương quan qua các ranh giới dịch vụ. Lan truyền một **ID truy vết/tương quan** qua mọi bước nhảy, để bạn có thể theo dõi một yêu cầu người dùng duy nhất qua tất cả các dịch vụ nó chạm đến (truy vết phân tán). Phát ra các **chỉ số** có cấu trúc (phân vị độ trễ, tỷ lệ lỗi, độ bão hòa, thông lượng) cho mỗi dịch vụ và mỗi phụ thuộc. Phát ra **nhật ký** có cấu trúc mang ID tương quan. Dùng tất cả để đặt các mục tiêu mức dịch vụ và cảnh báo về các triệu chứng người dùng thực sự cảm nhận, như tỷ lệ lỗi và độ trễ, thay vì chỉ về sức khỏe từng máy. Trong một hệ thống phân tán, khả năng quan sát không phải là công cụ tùy chọn. Đó là cách duy nhất để hiểu hành vi dưới thất bại một phần.

## Đánh đổi: ưu và nhược điểm

| Kỹ thuật | Ưu điểm | Nhược điểm / chi phí |
|---|---|---|
| Nhất quán mạnh | Mô hình tinh thần đơn giản, không đọc dữ liệu cũ | Tính sẵn sàng thấp hơn trong phân vùng, độ trễ cao hơn, chi phí phối hợp |
| Nhất quán cuối cùng | Sẵn sàng cao, độ trễ thấp, mở rộng được | Đọc dữ liệu cũ, suy luận phức tạp, cần giải quyết xung đột |
| Thử lại với độ lùi | Tự động vượt qua thất bại thoáng qua | Khuếch đại tải nếu dùng sai; cần tính lũy đẳng và giới hạn |
| Bộ ngắt mạch / vách ngăn | Ngăn thất bại lan truyền, thất bại nhanh | Thêm độ phức tạp, điều chỉnh ngưỡng, rủi ro ngắt sớm |
| Saga (so với 2PC) | Mở rộng được, sẵn sàng, không khóa phân tán | Nhất quán cuối cùng, logic bù trừ, khó suy luận hơn |

Đánh đổi chủ đạo là giữa phối hợp và độc lập. Mọi bảo đảm bạn muốn qua các máy (nhất quán, thứ tự, đúng-một-lần) tốn độ trễ, tính sẵn sàng hoặc độ phức tạp. Nó đòi hỏi các máy phải đồng thuận, và đồng thuận qua một mạng không đáng tin cậy thì tốn kém. Kỹ năng là chỉ mua những bảo đảm mà nghiệp vụ thực sự cần, từng thao tác một, và thiết kế mọi thứ khác cho suy giảm nhẹ nhàng. Mua dư nhất quán và hệ thống của bạn trở nên chậm và mong manh. Mua thiếu và bạn nhận được sự hỏng dữ liệu âm thầm xuất hiện như một thất bại kiểm toán nhiều tháng sau.

## Câu hỏi để thảo luận với đội của bạn

1. **Các mẫu khả năng phục hồi của bạn được phát hành như mặc định nền tảng dùng chung, hay mỗi đội đang phát minh lại thời gian chờ và thử lại?** Chương này coi tính lũy đẳng, thời gian chờ, thử lại có giới hạn, bộ ngắt mạch và truy vết là rẻ nhất và đáng tin cậy nhất khi được xây một lần vào thư viện dùng chung và mặc định nền tảng. Trong một tổ chức lớn, để mỗi đội tự làm bằng tay bảo đảm sự không nhất quán: một số đường thử lại các thao tác không lũy đẳng, một số không có thời gian chờ, một số không phát ra ID tương quan. Hãy mang bằng chứng bằng cách kiểm toán một mẫu dịch vụ và đếm có bao nhiêu dịch vụ đặt thời gian chờ tường minh trên mọi lệnh gọi từ xa và lan truyền ID truy vết từ đầu đến cuối. Nếu con số đó thấp, cách sửa là đầu tư nền tảng, không phải một bản ghi nhớ đào tạo. Các mặc định chuẩn cũng làm cho khả năng phục hồi kiểm thử được và kiểm toán được, điều mà cơ quan quản lý trong tài chính và chính phủ ngày càng mong bạn chứng minh.

2. **Thời gian chờ và ngân sách thử lại của bạn có kết hợp được qua cả chuỗi gọi không, hay một yêu cầu sâu tự thử lại đến mức gây sự cố?** Một yêu cầu đơn thường vượt qua nhiều bước nhảy, và nếu mỗi tầng độc lập thử lại ba lần với thời gian chờ riêng, thất bại trong cùng nhân lên và bên gọi ngoài cùng chờ vượt xa bất kỳ giới hạn nào con người chịu được. Hãy đặt một tổng ngân sách thời gian cho yêu cầu hướng đến người dùng và chia nó xuống chuỗi, để một dịch vụ bên trong biết còn bao ít thời gian và thất bại nhanh thay vì thử lại vào một cơn bão. Hãy mang đồ thị phụ thuộc và một truy vết thật của bạn, rồi cộng tổ hợp thời gian chờ và thử lại trường hợp xấu nhất và so sánh nó với những gì người dùng thực sự sẽ chờ. Độ lùi lũy thừa với nhiễu và giới hạn tổng số lần thử giữ cho một gợn sóng ngắn không trở thành cuộc từ chối dịch vụ tự gây ra. Các chuỗi đồng bộ sâu, lắm lời là kẻ thù ở đây, nên câu trả lời có thể đẩy bạn về phía các luồng bất đồng bộ hoặc ít bước nhảy hơn.

3. **Lần cuối bạn tiêm các thất bại mà thiết kế của bạn tuyên bố vượt qua được là khi nào, và điều gì đã hỏng mà bạn không ngờ tới?** Các mẫu khả năng phục hồi chỉ là giả thuyết cho đến khi bạn cố ý làm hệ thống thất bại: giết một thể hiện, thêm độ trễ vào một phụ thuộc, bỏ một phần thông điệp, phát lại một lô hai lần. Trong một hệ thống phân tán, các thất bại thú vị là một phần và gián đoạn, nên một bộ ngắt mạch hay bù trừ saga trông đúng trong mã vẫn có thể hành xử sai dưới một thời gian chờ-mà-có-thể-đã-hoàn-thành thực sự. Hãy mang kết quả của một ngày diễn tập hoặc một lần chạy tiêm lỗi thực sự, không phải tài liệu thiết kế, và ghi nhận cảnh báo nào đã kêu, truy vết mất bao lâu để khoanh vùng lỗi, và có cơn bão thử lại nào hình thành không. Trong các lĩnh vực chịu quy định, bằng chứng rằng bạn đã kiểm thử thất bại là một phần của việc chứng minh khả năng phục hồi vận hành với kiểm toán viên. Nếu bạn chưa bao giờ chạy một lần, thí nghiệm đầu tiên thuộc về môi trường kiểm thử với bán kính ảnh hưởng chặt và một công tắc hủy.

4. **Với mỗi luồng dữ liệu chính, đội sở hữu có gọi tên được mô hình nhất quán nó cung cấp không, và lựa chọn đó có khớp với những gì nghiệp vụ thực sự cần không?** CAP và PACELC buộc một lựa chọn có chủ đích cho từng thao tác, nhưng trong một tổ chức lớn mặc định là sự trôi dạt: một luồng khởi đầu nhất quán cuối cùng cho một bộ đếm ít rủi ro được tái sử dụng cho thứ nay phê duyệt thanh toán hoặc cấp quyền truy cập, và không ai xem xét lại bảo đảm. Các cân nhắc đối lập là thật, vì nhất quán mạnh tốn tính sẵn sàng trong phân vùng và độ trễ ngay cả khi không có, trong khi nhất quán cuối cùng mua tốc độ với cái giá là đọc dữ liệu cũ và giải quyết xung đột bạn phải thiết kế. Hãy mang một danh mục các luồng dữ liệu hàng đầu của bạn, mỗi luồng được gắn nhãn với mô hình hiện tại (mạnh, nhân quả, đọc-ghi-của-chính-mình, hoặc cuối cùng) và hậu quả nghiệp vụ của một lần đọc cũ hoặc mất, rồi tìm các điểm lệch nơi bảo đảm mạnh hơn hoặc yếu hơn mức rủi ro đòi hỏi. Trong tài chính doanh nghiệp và các hệ thống trợ cấp hoặc danh tính chính phủ, một lần đọc nhất quán cuối cùng đằng sau một quyết định có thẩm quyền là loại khiếm khuyết âm thầm xuất hiện như một phát hiện kiểm toán hoặc một lần từ chối oan nhiều tháng sau, nên bản thân việc rà soát là bằng chứng kiểm toán viên sẽ yêu cầu xem.

5. **Các giao dịch kinh doanh nhiều dịch vụ của bạn hành xử thế nào ở giữa chừng, và ai chịu trách nhiệm về các bù trừ hoàn tác chúng?** Thay cam kết hai pha bằng saga nghĩa là hệ thống đi qua các trạng thái trung gian hiển thị, và một bước có thể thành công trong khi bước sau thất bại và kích hoạt một hành động bù trừ đảo ngược nó. Với một đội lớn điều này đặt ra các câu hỏi khó về quyền sở hữu: chuỗi cho phép-ghi nợ-ghi có-sổ cái thường vượt qua nhiều đội, và một bù trừ mà một đội quên cài đặt để lại tiền hoặc bản ghi không nhất quán vĩnh viễn. Hãy cân nhắc biên đạo, nơi các dịch vụ phản ứng với sự kiện của nhau không có bộ điều khiển trung tâm và luồng khó thấy, đối chiếu với điều phối, nơi một bộ điều phối dẫn dắt và giám sát các bước với cái giá là một thành phần phải vận hành. Hãy mang sơ đồ trạng thái cho saga quan trọng nhất của bạn, danh sách các hành động bù trừ và chủ sở hữu của chúng, và bằng chứng rằng các trạng thái "đang tiến hành" và "đã bù trừ" được xử lý cả trong trải nghiệm người dùng lẫn dấu vết kiểm toán. Trong ngân hàng và quản lý hồ sơ khu vực công, cơ quan quản lý mong bạn dựng lại chính xác điều gì đã xảy ra với một giao dịch thất bại giữa chừng, nên một trạng thái trung gian không được mô hình hóa là một lỗ hổng tuân thủ, không chỉ là một lỗi.

6. **Bên tiêu thụ thông điệp của bạn có sống sót qua giao nhận trùng lặp và đảo thứ tự không, và bạn có thể chứng minh điều đó trước khi bộ môi giới buộc đặt câu hỏi không?** Giao nhận đúng-một-lần là huyền thoại, nên bảo đảm thực của bạn là ít-nhất-một-lần, và một bên tiêu thụ giả định mỗi thông điệp đến một lần và theo thứ tự sẽ xử lý hai lần vào ngày bộ môi giới giao lại một lô sau một lần chuyển đổi dự phòng. Qua nhiều đội rủi ro cộng dồn, vì một bên tiêu thụ không lũy đẳng trên một luồng dùng chung có thể làm hỏng trạng thái hạ nguồn mà các đội khác phụ thuộc, và thất bại vô hình cho đến khi phát lại hoặc một phân vùng đảo thứ tự sự kiện. Đánh đổi là chi phí kỹ thuật của khóa lũy đẳng, nhật ký thông điệp đã xử lý, và xử lý offset cùng phân vùng tường minh, đặt cạnh chi phí của sự hỏng hóc âm thầm. Hãy mang danh sách các bên tiêu thụ trên các luồng quan trọng của bạn, ghi chú cái nào khử trùng lặp và cái nào chỉ hy vọng, và mang kết quả của một lần kiểm thử giao lại hoặc phát lại thực sự thay vì một lời bảo đảm rằng nó chắc ổn. Với trao đổi dữ liệu liên cơ quan chính phủ và các đường ống sự kiện doanh nghiệp, khả năng phát lại an toàn một luồng sau khi sửa lỗi, mà không tạo hồ sơ hay khoản phí trùng lặp, vừa là điều cần thiết về vận hành vừa là điều kiểm toán viên sẽ muốn thấy được chứng minh.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với hai hoặc ba bộ phận chuyển động và không có đội nền tảng, hãy cưỡng lại việc xây bộ máy phân tán mà bạn không thể bố trí nhân sự. Hãy mua khả năng phục hồi ở nơi nó sống trong SDK mà nhà cung cấp thanh toán hoặc nhắn tin của bạn đã cung cấp, và dành sự chú ý khan hiếm cho hai mẫu ngăn tác hại không thể đảo ngược: một khóa lũy đẳng trên mọi lệnh gọi chuyển tiền hoặc thay đổi tài khoản, và một thời gian chờ với thử lại có giới hạn để một kết nối chập chờn không bao giờ hành động hai lần. Giữ số bước nhảy mạng nhỏ, vì mỗi phụ thuộc đồng bộ bạn thêm là một thứ nữa có thể thất bại trước khi bạn có ai trực ca để nhận ra.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia hệ thống phân tán và ngân sách eo hẹp, vì vậy hãy coi đây là câu hỏi mua-không-xây: ưu tiên hàng đợi được quản lý, cơ sở dữ liệu được quản lý, và các nền tảng xử lý thử lại, thứ tự và khử trùng lặp cho bạn thay vì hạ tầng bạn phải vận hành. Hãy đóng khung rủi ro bằng thuật ngữ đơn giản, biết những thao tác nào sẽ làm hại khách hàng nếu chạy hai lần hoặc trả dữ liệu cũ, và bật các tính năng lũy đẳng và ít-nhất-một-lần mà nhà cung cấp của bạn đã cung cấp. Tránh ghép các dịch vụ lại với nhau qua một cơ sở dữ liệu dùng chung để giả một giao dịch, vì điều đó âm thầm tái tạo vấn đề phân tán khó nhất mà không có công cụ nào để quản lý.

**Doanh nghiệp lớn.** Vấn đề cốt lõi là nhất quán qua nhiều đội, vì vậy hãy phát hành tính lũy đẳng, thời gian chờ, thử lại có giới hạn, bộ ngắt mạch và truy vết tương quan như các mặc định nền tảng dùng chung thay vì để mỗi nhóm tự làm bằng tay. Chuẩn hóa cách khai báo mô hình nhất quán và bảo đảm giao nhận theo từng luồng, chạy tiêm lỗi và ngày diễn tập theo nhịp đều đặn, và làm cho tổng ngân sách thời gian kết hợp được qua các chuỗi gọi sâu để một dịch vụ không thể thử lại cả nền tảng vào một sự cố. Hãy quản lý khả năng phục hồi như một năng lực được đo với các mục tiêu mức dịch vụ trên triệu chứng người dùng thấy, vì ở quy mô của bạn một thời gian chờ bị thiếu có thể lan thành một sự cố lên tiêu đề.

**Chính phủ.** Các hệ thống liên cơ quan nghĩa là không ai sở hữu toàn bộ, vì vậy hãy thiết kế cho các ranh giới bạn không kiểm soát: hàng đợi bền vững với giao nhận ít-nhất-một-lần, khử trùng lặp trên ID thông điệp ổn định, và ID tương quan chảy qua ranh giới cơ quan để cho kiểm toán viên một dấu vết từ đầu đến cuối. Quy tắc mua sắm và minh bạch thúc bạn lập tài liệu mô hình nhất quán và bảo đảm giao nhận của mỗi tích hợp, và giữ các quyết định có thẩm quyền (danh tính, tư cách, trợ cấp) trên các lần đọc nhất quán mạnh thay vì các điểm cuối được lưu đệm. Hãy coi bằng chứng về thất bại đã được kiểm thử và lịch sử giao dịch có thể dựng lại là các sản phẩm bàn giao, vì khả năng phục hồi vận hành và trách nhiệm giải trình trước công chúng là nghĩa vụ hợp đồng và luật định, không phải thứ lịch sự nội bộ.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp fintech nhỏ chỉ có hai bộ phận chuyển động nói chuyện qua mạng: ứng dụng của họ và một nhà cung cấp thanh toán bên thứ ba. Ngay cả ở quy mô này họ làm cho mọi yêu cầu tính phí mang một khóa lũy đẳng và bọc lệnh gọi trong một lần thử lại với độ lùi, để một phản hồi bị rơi trên kết nối chập chờn không bao giờ tính phí hai lần một khách hàng. Bỏ qua điều này có vẻ rẻ vào ngày đầu, nhưng lần tính phí trùng lặp đầu tiên chạm vào một người dùng thật tốn một đám cháy hỗ trợ, một khoản hoàn tiền, và một vết lõm trong niềm tin mà công ty non trẻ không thể phí.

**Doanh nghiệp lớn.** Một nền tảng gọi xe toàn cầu xử lý thanh toán chuyến đi qua một saga: cho phép thẻ, ghi nợ hành khách, ghi có tài xế, ghi bút toán sổ cái, mỗi bước là một giao dịch cục bộ với một đảo ngược bù trừ. Mỗi bước mang một khóa lũy đẳng, nên các lần thử lại sau thời gian chờ mạng không bao giờ tính phí hai lần. Các lệnh gọi đến dịch vụ chấm điểm gian lận nằm sau một bộ ngắt mạch; khi nó suy giảm vào giờ cao điểm, bộ ngắt mở ra và các chuyến đi chuyển sang một điểm số thận trọng thay vì chặn mọi chuyến. Khi một khách hàng khiếu nại một chuyến đi, truy vết phân tán cho phép kỹ sư theo dõi nó qua hàng chục dịch vụ trong vài giây.

**Chính phủ.** Một dịch vụ danh tính quốc gia được nhiều cơ quan dùng để xác minh. Nó cung cấp một lần đọc nhất quán mạnh cho các kiểm tra trạng thái có thẩm quyền (bạn không được phê duyệt một khoản trợ cấp dựa trên dữ liệu danh tính cũ), cộng với một điểm cuối được lưu đệm, nhất quán cuối cùng cho các tra cứu khối lượng cao, không quan trọng. Trao đổi dữ liệu liên cơ quan chạy qua một hàng đợi thông điệp bền vững với giao nhận ít-nhất-một-lần, và bên tiêu thụ của mỗi cơ quan khử trùng lặp trên ID thông điệp, nên một bản ghi được giao lại không tạo ra hồ sơ trùng lặp. ID tương quan chảy qua ranh giới cơ quan, cho kiểm toán viên một dấu vết từ đầu đến cuối về cách dữ liệu của công dân di chuyển giữa các bộ phận.

## Luận chứng kinh doanh: động lực, ROI và TCO

Kỷ luật hệ thống phân tán được mua rẻ và sự vắng mặt của nó phải trả giá thảm khốc. Chi phí áp dụng là thời gian kỹ thuật để xây tính lũy đẳng, thời gian chờ, thử lại, bộ ngắt mạch và truy vết vào thư viện dùng chung và mặc định nền tảng. Đó là một khoản đầu tư khiêm tốn, chủ yếu một lần, sau đó mang lợi cho mọi đội. Chi phí của việc *không* áp dụng được đo bằng các sự cố lớn: một thời gian chờ thiếu lan thành sự cố toàn nền tảng, một đường thanh toán không lũy đẳng tính phí hai lần hàng nghìn khách hàng, hoặc một giao dịch phân tán không saga để lại dữ liệu không nhất quán vĩnh viễn. Mỗi cái là một sự cố lên tiêu đề với chi phí doanh thu, khắc phục và danh tiếng trực tiếp, và trong các lĩnh vực chịu quy định, là tiền phạt.

Hãy đóng khung lập luận với ban lãnh đạo quanh tính sẵn sàng và bán kính ảnh hưởng. Các mẫu khả năng phục hồi trực tiếp giảm cả tần suất lẫn thời lượng của các sự cố nghiêm trọng, những chỉ số mà các giám đốc điều hành đã theo dõi như thời gian hoạt động và thời gian phục hồi trung bình. Khả năng quan sát phân tán là đòn bẩy lớn nhất lên MTTR: các đội có truy vết tương quan giải quyết sự cố liên dịch vụ trong một phần nhỏ thời gian. Vì những năng lực này được cung cấp tốt nhất như các mặc định nền tảng dùng chung, chi phí biên theo từng đội của chúng thấp và lợi ích toàn tổ chức cộng dồn. Lập luận TCO đơn giản: xây khả năng phục hồi vào ngay từ đầu chỉ bằng một phần nhỏ chi phí trang bị bổ sung sau sự cố buộc phải làm.

## Phản mẫu và cạm bẫy

- **Không có thời gian chờ.** Một phụ thuộc bị treo làm cạn mọi luồng và đánh sập cả hệ thống.
- **Thử lại các thao tác không lũy đẳng.** Tác dụng phụ trùng lặp: tính phí hai lần, bản ghi trùng, email nhân đôi.
- **Bão thử lại.** Thử lại đồng bộ không có độ lùi và nhiễu khuếch đại một gợn sóng nhỏ thành sự cố.
- **Giả định giao nhận đúng-một-lần.** Xây bên tiêu thụ hỏng trên các thông điệp trùng lặp mà bộ môi giới cuối cùng sẽ giao.
- **Giao dịch phân tán qua cơ sở dữ liệu dùng chung.** Ghép các dịch vụ qua một cơ sở dữ liệu để giả ACID, tái tạo một khối đơn phân tán.
- **Bỏ qua thất bại một phần.** Mã giả định một lệnh gọi từ xa hoặc hoàn toàn thành công hoặc hoàn toàn thất bại, không xử lý "hết thời gian chờ nhưng có thể đã hoàn thành."
- **Không có ID tương quan.** Gỡ lỗi sự cố liên dịch vụ bằng cách grep các nhật ký không liên quan trên mười máy.
- **Chuỗi gọi đồng bộ lắm lời.** Đồ thị phụ thuộc đồng bộ sâu nơi bất kỳ bước nhảy chậm nào làm đình trệ cả yêu cầu.

## Mô hình trưởng thành

- **Mức 1: Khởi đầu.** Lệnh gọi từ xa được coi như lệnh gọi cục bộ. Thời gian chờ thiếu hoặc ngây thơ, thử lại vắng mặt hoặc liều lĩnh, và thất bại lan khắp hệ thống. Không có cái nhìn chung về nhất quán hay giao nhận, và gỡ lỗi sự cố liên dịch vụ nghĩa là đào bới nhật ký từng máy sau sự việc.
- **Mức 2: Phát triển.** Một số đội thêm thời gian chờ, thử lại cơ bản và chút tính lũy đẳng, nhưng các thực hành không nhất quán giữa các dịch vụ. Nhật ký được tập trung nhưng không tương quan, nên truy vết một yêu cầu qua các bước nhảy là thủ công. Giao dịch phân tán được hy vọng hoạt động thay vì được mô hình hóa, và các bảo đảm nhất quán sống trong đầu từng kỹ sư.
- **Mức 3: Chuẩn hóa.** Tính lũy đẳng, thử lại có giới hạn, độ lùi với nhiễu, bộ ngắt mạch và vách ngăn là tiêu chuẩn trong toàn tổ chức qua các thư viện dùng chung. Saga với các hành động bù trừ xử lý giao dịch nhiều dịch vụ, truy vết phân tán với ID tương quan được triển khai, và mọi luồng dữ liệu chính ghi lại mô hình nhất quán và bảo đảm giao nhận. Các quy tắc được viết ra và thực thi toàn tổ chức thay vì để mỗi đội tự lo.
- **Mức 4: Quản lý.** Khả năng phục hồi được đo theo các đường cơ sở, không chỉ có mặt. Bạn theo dõi tỷ lệ lỗi, phân vị độ trễ, độ bão hòa và thông lượng cho mỗi dịch vụ và phụ thuộc, theo dõi tỷ lệ thử lại và tỷ lệ mở bộ ngắt mạch, và đặt các mục tiêu mức dịch vụ trên triệu chứng người dùng thấy. Tổng ngân sách thời gian được xác minh kết hợp được qua các chuỗi gọi, thời gian phục hồi trung bình cho sự cố liên dịch vụ là chỉ số được giám sát, và kết quả tiêm lỗi cùng ngày diễn tập nuôi các con số kiểm soát mỗi thay đổi.
- **Mức 5: Điều phối.** Khả năng phục hồi là mặc định nền tảng được cải thiện liên tục, tích hợp trong toàn tổ chức và thích ứng với điều kiện. Tiêm lỗi chạy thường xuyên trên môi trường thực với bán kính ảnh hưởng chặt, hệ thống suy giảm nhẹ nhàng theo thiết kế, và các lựa chọn nhất quán và giao nhận được xem xét lại khi tải và mức rủi ro nghiệp vụ dịch chuyển. Các chỉ số từ Mức 4 điều khiển các phản ứng tự động và tiến hóa kiến trúc ổn định, để hệ sinh thái phân tán trở nên vững chắc hơn sau mỗi sự cố thay vì chỉ sống sót qua nó.

## Ý tưởng để thảo luận

1. Những thao tác quan trọng nào của bạn hôm nay thực sự lũy đẳng, và những thao tác nào âm thầm không?
2. Với mỗi luồng dữ liệu chính, đội của bạn có thể nêu mô hình nhất quán và bảo đảm giao nhận từ trí nhớ không?
3. Một bộ ngắt mạch lẽ ra đã ngăn sự cố lan truyền gần nhất của bạn ở đâu?
4. Hiện mất bao lâu để truy vết một yêu cầu thất bại đơn lẻ qua tất cả các dịch vụ nó chạm đến?
5. "Giao dịch phân tán" nào của bạn thực ra dựa vào may rủi, và cái nào là saga thật với bù trừ?
6. Nếu bộ môi giới thông điệp của bạn giao lại mọi thông điệp hai lần trong một giờ, cái gì sẽ hỏng?

## Những điểm cần ghi nhớ

- Giả định mạng không đáng tin cậy và thất bại là một phần; thiết kế mọi tương tác từ xa cho sự chậm trễ, mất mát, nhân đôi và đảo thứ tự.
- Quyết định nhất quán so với sẵn sàng theo từng thao tác bằng CAP/PACELC; ghi lại mô hình mà mỗi luồng cung cấp.
- Tính lũy đẳng, thời gian chờ, thử lại có giới hạn và độ lùi-với-nhiễu là một gói; đừng bao giờ áp dụng thử lại mà thiếu ba thứ còn lại.
- Bộ ngắt mạch và vách ngăn kiềm chế thất bại; saga với bù trừ thay thế các giao dịch phân tán không khả thi.
- Coi giao nhận là ít-nhất-một-lần và làm cho xử lý lũy đẳng để đạt hiệu ứng đúng-một-lần.
- Truy vết, chỉ số và nhật ký tương quan là cách duy nhất để hiểu và vận hành các luồng phân tán.

## Tài liệu tham khảo và đọc thêm

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew Tanenbaum và Maarten van Steen, *Distributed Systems: Principles and Paradigms*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Sam Newman, *Building Microservices*
- Chris Richardson, *Microservices Patterns* (saga, nhắn tin giao dịch)
- Eric Brewer, "CAP Twelve Years Later" và Daniel Abadi về PACELC
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System"
- Cindy Sridharan, *Distributed Systems Observability*
- Khái niệm chống mong manh (antifragility) của Nassim Nicholas Taleb (được áp dụng trong tài liệu kỹ thuật phục hồi)
