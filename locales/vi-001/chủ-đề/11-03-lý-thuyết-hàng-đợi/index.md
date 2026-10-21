# 11.3 Lý thuyết hàng đợi

## Tổng quan và động lực

[Lý thuyết hàng đợi](https://en.wikipedia.org/wiki/Queueing_theory) là nghiên cứu toán học về hàng chờ. Trong kỹ thuật phần mềm, đó là lý thuyết thầm lặng đằng sau một lượng lớn thực hành. Khả năng đáp ứng dịch vụ khách hàng, hoạch định [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) (phương pháp kéo giới hạn [công việc đang làm](https://en.wikipedia.org/wiki/Work_in_process) để cải thiện luồng), hàng đợi thông điệp giữa các tiến trình, quy trình triển khai liên tục: tất cả đều là hàng đợi, và tất cả đều tuân theo cùng các định luật. Hiểu những định luật đó cho phép một đội lập luận về [thời gian chờ](https://en.wikipedia.org/wiki/Lead_time), [thông lượng](https://en.wikipedia.org/wiki/Throughput), năng lực, và chi phí thật của việc chạy hệ thống gần giới hạn của chúng, thay vì bị chúng làm bất ngờ trong môi trường sản xuất. Chương này nằm trong phần Dòng chảy vì lý thuyết hàng đợi là nền tảng hình thức của dòng chảy: nó giải thích *vì sao* công việc chờ, và cái gì thực sự giảm việc chờ.

Đây là động lực: trực giác về hàng đợi luôn sai, và sai theo những cách đắt đỏ. Mọi người giả định một máy chủ chạy ở mức sử dụng 90% "cách rắc rối 10%," trong khi thực ra thời gian chờ bùng nổ phi tuyến khi mức sử dụng tiến tới 100%. Họ giả định thêm công việc đang làm (WIP) đẩy nhanh phân phối, trong khi nó kéo dài thời gian chờ. Họ hoạch định năng lực quanh các giá trị trung bình, rồi bị độ biến thiên nghiền nát. Một chút lý thuyết hàng đợi thay các trực giác đắt đỏ này bằng một số ít quan hệ vững chắc, quan trọng nhất là **[Định luật Little](https://en.wikipedia.org/wiki/Little%27s_law)**, đúng qua hàng đợi khách hàng, bảng tác vụ và quy trình CI/CD như nhau.

Với các đội lớn, doanh nghiệp và chính phủ, lý thuyết hàng đợi là ngôn ngữ chung cho năng lực và dòng chảy, thứ nối các vai trò vốn nói chuyện lệch nhau. Quản lý sản phẩm quan tâm thời gian chờ từ ý tưởng đến khách hàng. SRE quan tâm mức sử dụng máy chủ và độ trễ. Đội DevOps quan tâm tần suất triển khai. Lãnh đạo hỗ trợ quan tâm thời gian phản hồi. Tất cả đều là chỉ số hàng đợi, và diễn đạt chúng trong một khung (tốc độ đến, tốc độ phục vụ, mức sử dụng, thời gian chờ) cho phép một tổ chức hoạch định năng lực, đặt SLO (mục tiêu mức dịch vụ) thực tế, và biện minh đầu tư bằng toán học thay vì giai thoại.

## Các nguyên tắc chính

- **Mọi thứ có chờ đều là hàng đợi:** gồm phiếu, tác vụ, thông điệp và lần triển khai.
- **Định luật Little là điểm neo:** số mục trong hệ thống = tốc độ đến × thời gian trong hệ thống (κ = λτ).
- **Mức sử dụng và thời gian chờ là phi tuyến:** 15% năng lực cuối là đắt nhất.
- **Độ biến thiên là kẻ thù của dòng chảy:** trung bình giấu nỗi đau; phương sai tạo ra hàng đợi.
- **Giảm công việc đang làm giảm thời gian chờ:** dòng chảy, không phải sự bận rộn, là mục tiêu.
- **Đo toàn bộ dòng chảy:** đến, phục vụ, thành công, thất bại, bỏ qua và chờ.
- **Một quy trình là hàng đợi của các hàng đợi:** mô hình hóa các giai đoạn, rồi tối ưu cái ràng buộc.

## Khuyến nghị

### Học ký hiệu cốt lõi và dùng nhất quán

Một nhúm đại lượng mô tả bất kỳ hàng đợi nào. Chuẩn hóa theo chúng (chữ cái Hy Lạp là quy ước) loại bỏ sự mơ hồ qua các đội:

- **λ (lambda), tốc độ đến:** các mục mới vào nhanh thế nào.
- **μ (mu), tốc độ phục vụ:** các mục được xử lý nhanh thế nào. Vì "tốc độ phục vụ" bị dùng mơ hồ, thường đáng tách thông lượng tường minh thành **tốc độ tổng (χ)**, **tốc độ thành công (α)**, **tốc độ thất bại (β)** và **tốc độ bỏ qua (σ)**, trong đó χ = α + β + σ.
- **ρ (rho), mức sử dụng / cường độ lưu lượng = λ / μ:** bản tóm tắt quan trọng nhất đơn lẻ. ρ < 1 nghĩa là hàng đợi cạn; ρ ≥ 1 nghĩa là nó lớn vô hạn.
- **Thời gian:** thời gian chờ (τ, từ đầu đến cuối), thời gian làm việc (φ, xử lý thực), thời gian chờ đợi (ω, đang chờ), và thời gian bước (θ, giữa các lần hoàn thành).
- **ε (epsilon), tỷ lệ lỗi:** thất bại ÷ tổng.

Gọi tên tường minh thất bại và *bỏ qua* quan trọng trong phần mềm: một mục bị bỏ (khách hàng bỏ cuộc, giỏ hàng bị bỏ lại, phiếu công việc bị từ chối) rời hàng đợi mà không được phục vụ, và giả vờ nó đã được "phục vụ" làm hỏng chỉ số của bạn. Hãy theo dõi **ngập ngừng** (quyết định không tham gia), **bỏ cuộc** (từ bỏ sau khi chờ) và **chuyển hàng** (đổi hàng đợi) như kết quả hạng nhất.

### Neo hoạch định vào Định luật Little

Định luật Little nói số mục trung bình dài hạn trong một hệ thống ổn định bằng tốc độ đến trung bình nhân thời gian trung bình mỗi mục ở trong hệ thống: **κ = λ τ** (kinh điển là L = λW). Nó tổng quát đáng kinh ngạc (không cần giả định nào về phân phối đến hay thứ tự phục vụ), làm nó thành con ngựa thồ của hoạch định dòng chảy. Sắp xếp lại, nó cho bạn biết **thời gian chờ = công việc đang làm ÷ thông lượng**. Đó là cơ sở toán học của kanban và tinh gọn: nếu bạn muốn thời gian chờ ngắn hơn và không nâng được thông lượng, bạn phải hạ WIP. Nó cũng cho các kiểm tra tỉnh táo nhanh. Nếu 40 phiếu đang mở và bạn đóng 8 mỗi ngày, phiếu trung bình mất khoảng 5 ngày, bất kể ai cảm thấy bận đến đâu. Yêu cầu duy nhất của nó là *tính ổn định*: tốc độ đến không được liên tục vượt tốc độ đi (ρ < 1), nếu không hàng đợi, và các giả định của định luật, sụp đổ.

### Tôn trọng tính phi tuyến của mức sử dụng

Bài học vận hành quan trọng nhất của lý thuyết hàng đợi là thời gian phản hồi tăng vọt, không dần dần, khi mức sử dụng tiến tới 100%. *Bảy hiểu biết về lý thuyết hàng đợi* của Bob Wescott nắm bắt các hệ quả thực tế một cách sinh động:

1. Trung tâm phục vụ càng chậm, mức sử dụng đỉnh bạn nên hoạch định càng thấp.
2. Rất khó dùng 15% cuối của bất cứ thứ gì.
3. Bạn chạy càng gần bờ vực, giá của việc sai càng cao.
4. Tăng trưởng thời gian phản hồi bị giới hạn bởi bao nhiêu mục có thể chờ.
5. Đây là giá trị trung bình, không phải tối đa: hãy hoạch định cho cái đuôi.
6. Coi chừng hiệu ứng chối bỏ của con người qua nhiều trung tâm phục vụ.
7. Cho thấy những cải thiện nhỏ trong ánh sáng tốt nhất của chúng.

Hàm ý thiết kế: **cung cấp dư địa có chủ đích.** Nhắm mức sử dụng 70–80% cho hệ thống nhạy với độ trễ không phải lãng phí; đó là mua thời gian phản hồi khả đoán. Điều này trực tiếp thông tin cho hoạch định năng lực và SLO (chương 3.5 và 9.1).

### Mô hình hóa quy trình như hàng đợi của các hàng đợi

Công việc thật chảy qua các giai đoạn, và một quy trình nhiều giai đoạn đơn giản là một hàng đợi có các mục tự được xếp hàng ở mỗi bước. Hãy mô hình hóa theo cách đó: tốc độ đến của quy trình là tốc độ đến của giai đoạn 1; tốc độ thành công của quy trình là tốc độ thành công của giai đoạn cuối; số lỗi và bỏ qua của quy trình là tổng qua các giai đoạn. Hai hình dạng phổ biến lặp lại:

- **Phễu**, nơi số mục co lại qua từng giai đoạn (tuyển dụng: tiếp cận → phỏng vấn → đề nghị; mua hàng: duyệt → giỏ → trả tiền; phân phối: tích hợp → UAT → sản xuất). Tối ưu giai đoạn quan trọng nhất: tối đa hóa lượng đến ở đầu phễu, tối thiểu hóa bỏ qua giữa phễu (bỏ giỏ hàng), hoặc tối thiểu hóa lỗi giai đoạn cuối (triển khai sản xuất tệ).
- **Kim cương đôi** các dòng chảy khám phá-và-phân phối (khám phá → xác định → phát triển → giao), mà phần Dòng chảy của cuốn sách này xử lý trực tiếp (chương 11.1).

Tìm và giải tỏa **giai đoạn ràng buộc** (nút thắt) là nơi cải thiện dòng chảy sinh lời; tối ưu giai đoạn không ràng buộc chỉ dời hàng đợi.

### Nối chỉ số hàng đợi với KPI mà các đội đã dùng

Các đại lượng hàng đợi ánh xạ gọn vào chỉ số phân phối và độ tin cậy ở nơi khác trong cuốn sách này, làm lý thuyết thực tế thay vì hàn lâm:

- **Thời gian chờ phân phối (Dτ)**, "từ khái niệm đến khách hàng," là thước đo thời gian chờ (τ) và là chỉ số DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (chương 11.2).
- **Tần suất triển khai (Dμ)** là thước đo tốc độ phục vụ.
- **Tỷ lệ thay đổi thất bại (Dε)** là tỷ lệ lỗi.
- **Thời gian khôi phục (Rτ)** là thời gian chờ khôi phục, tức MTTR (chương 9.3).

Hãy phân biệt các **MTTR** (thời gian trung bình để *phản hồi*, *sửa chữa*, *khôi phục* và *giải quyết*) vì chúng đo các đoạn khác nhau của hàng đợi sự cố và thường bị gộp nhầm. Đặt nền SLI/SLO/SLA (chương 9.1) trong thuật ngữ hàng đợi giữ mục tiêu trung thực và so sánh được.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| **Chạy hệ thống ở mức sử dụng cao** | Chi phí phần cứng/đơn vị thấp hơn | Độ trễ bùng nổ phi tuyến; dễ vỡ trước đột biến |
| **Cung cấp dư địa hào phóng** | Độ trễ khả đoán; chịu được phương sai | Chi phí trạng thái ổn định cao hơn; trông "dùng thiếu" |
| **Giới hạn WIP (kanban)** | Thời gian chờ ngắn hơn; ít chuyển ngữ cảnh | Cảm giác chậm hơn; cần kỷ luật để giữ giới hạn |
| **Mô hình hóa hàng đợi chính thức** | Quyết định năng lực được định lượng; ít bất ngờ | Đường cong học; mô hình đơn giản hóa thực tế lộn xộn |
| **Chỉ dùng quy tắc kinh nghiệm** | Nhanh, không toán | Sai chính xác nơi đắt nhất (gần năng lực) |

Đánh đổi lặp lại là **hiệu quả so với khả năng dự đoán**: đẩy mức sử dụng lên tiết kiệm tiền cho đến khi đột nhiên không, lúc đó chi phí độ trễ, thất bại và chữa cháy lấn át khoản tiết kiệm. Đóng góp của lý thuyết hàng đợi là cho bạn biết vách đá đó *ở đâu* để đánh đổi là một lựa chọn, không phải tai nạn.

## Câu hỏi để thảo luận với đội của bạn

1. **Mục tiêu mức sử dụng tường minh của bạn cho từng hệ thống nhạy với độ trễ là gì, và ai đã ký duyệt nó?** Dư địa là sự mua có chủ đích độ trễ khả đoán, nên nó phải là chính sách được nêu, không phải tai nạn của tải tình cờ đến. Vì thời gian phản hồi tăng phi tuyến, chạy ở 85% đã có thể nghĩa là độ trễ đuôi tăng cao, vậy mà tài chính thấy dư địa là lãng phí và đẩy mức sử dụng lên. Hãy mang các con số: mức sử dụng hiện tại, đường cong độ trễ đo được, và chi phí của sự cố độ trễ gần nhất, rồi cho thấy vách đá nằm ở đâu cho từng dịch vụ. Với hệ thống doanh nghiệp và chính phủ có đỉnh theo mùa (mùa khai thuế, cửa sổ ghi danh), hãy đặt mục tiêu lệch khỏi vách đá cho đỉnh, không phải trung bình. Nếu không ai sở hữu mục tiêu mức sử dụng, sự cố độ trễ sẽ tiếp tục xuất hiện "từ hư không."

2. **Ở đâu trong hệ thống của bạn có hàng đợi không giới hạn, không có áp lực ngược để xả tải khi quá tải?** Một hàng đợi không giới hạn không thất bại êm; nó suy giảm thành sụp đổ, vì tốc độ đến liên tục vượt tốc độ đi (rho >= 1) nghĩa là hàng đợi lớn không giới hạn. Hãy kiểm kê hàng đợi thông điệp, bể luồng và bộ đệm yêu cầu của bạn, và hỏi điều gì xảy ra ở từng cái khi tốc độ đến vượt tốc độ phục vụ: nó xả tải, áp dụng áp lực ngược, hay đổ? Điều này đặc biệt gấp ở quy mô doanh nghiệp, nơi một hạ nguồn bão hòa duy nhất có thể lan qua các dịch vụ. Hãy mang kết quả kiểm thử tải hoặc một sự cố quá khứ nơi hàng đợi bị tồn, và kiểm tra hệ thống có từ chối công việc thừa hay cố giữ tất cả. Cách sửa là hàng đợi có giới hạn với áp lực ngược tường minh và thời gian chờ suy ra từ Định luật Little, để quá tải được xả thay vì lật đổ.

3. **Bạn có đang mô hình hóa dòng chảy từ ý tưởng đến sản xuất như hàng đợi của các hàng đợi, và các cải thiện của bạn có nhắm vào ràng buộc thật không?** Một quy trình nhiều giai đoạn là hàng đợi có các mục được xếp hàng ở mỗi giai đoạn, và tối ưu bất cứ thứ gì ngoài giai đoạn ràng buộc chỉ dời hàng đợi. Hãy lập bản đồ phễu phân phối của bạn (tích hợp đến UAT đến sản xuất, hoặc khám phá đến xác định đến phát triển đến giao) và đo tốc độ đến, phục vụ, chờ và bỏ qua ở mỗi giai đoạn để tìm nơi công việc thực sự dồn lại. Các đội thường xuyên tối ưu giai đoạn họ hiểu nhất thay vì nút thắt, tiêu công sức mà không dịch chuyển gì. Hãy mang dữ liệu thời gian chờ theo từng giai đoạn, không phải cảm giác, vì nút thắt thường là trạng thái chờ (rà soát, phê duyệt, sẵn có môi trường) hơn là trạng thái làm việc. Một khi bạn biết ràng buộc, hãy nhắm vào đó và để yên những cái không ràng buộc.

4. **Bạn có dùng Định luật Little để đặt giới hạn WIP, hay đang thêm năng lực để chữa thời gian chờ mà chỉ thêm kỷ luật mới sửa được?** Định luật Little nói thời gian chờ bằng công việc đang làm chia cho thông lượng, nên nếu bạn không nâng được thông lượng, đòn bẩy duy nhất còn lại cho thời gian chờ ngắn hơn là hạ WIP, thứ không tốn gì ngoài sự tiết chế. Lực kéo đối lập là thật: giới hạn công việc đang làm cảm giác chậm hơn và rảnh rỗi, và quản lý dưới áp lực thà tuyển người hay mua phần cứng hơn bảo các đội bắt đầu ít đi và hoàn thành nhiều hơn. Hãy mang các con số cứng, số mục đang mở hiện tại và tốc độ hoàn thành theo từng giai đoạn, và tính thời gian chờ trung bình ngụ ý, rồi so với cái mọi người tin; khoảng cách thường lớn và đáng xấu hổ. Trong một doanh nghiệp hay cơ quan lớn, một yêu cầu tuyển dụng hay mua sắm được biện minh là bản sửa thời gian chờ nên được kiểm thử với phép số học này trước, vì tăng nhân sự làm tăng WIP có thể kéo dài chính thời gian chờ mà nó được định rút ngắn.

5. **Bạn hoạch định năng lực quanh giá trị trung bình, hay đã định lượng độ biến thiên thực sự tạo ra hàng đợi của bạn?** Hàng đợi hình thành từ phương sai, không phải từ trung bình, nên hai hệ thống có cùng tải trung bình có thể hành xử hoàn toàn khác nếu một cái có lượng đến bùng phát hay thời gian phục vụ đuôi dài. Căng thẳng là trung bình dễ thu thập và trấn an khi báo cáo, trong khi phương sai và cái đuôi khó đo hơn và không được chào đón trong bản cập nhật trạng thái. Hãy mang phân phối, không phải trung bình: độ bùng phát của lượng đến, thời gian phục vụ và chờ ở phân vị 95 và 99, và kích thước lô dồn công việc thành đột biến. Với hệ thống doanh nghiệp và chính phủ có đợt tăng dự đoán được (mùa khai thuế, kỳ trả lương, cửa sổ ghi danh, tải cuối quý), hãy hoạch định bộ đệm và mục tiêu mức sử dụng theo phương sai kỳ đỉnh, vì một thiết kế định cỡ theo trung bình hằng năm sẽ thất bại chính xác khi công chúng đang nhìn.

6. **Hàng đợi nào của bạn lặng lẽ đếm việc bỏ cuộc và từ chối như thể công việc đã được phục vụ, và nhu cầu chưa đáp ứng nào bị giấu?** Một mục ngập ngừng, bỏ cuộc hoặc bị từ chối rời hàng đợi mà không được xử lý, và ghi nó là "đã phục vụ" làm hỏng thông lượng, tỷ lệ lỗi và kế hoạch năng lực của bạn cùng lúc. Cân nhắc đối lập là "cuộc gọi đã trả lời" hay "phiếu đã đóng" trông tốt hơn trên bảng điều khiển so với "người gọi đã bỏ cuộc," nên con số trung thực là cái không ai tình nguyện làm lộ. Hãy mang tốc độ bỏ qua (σ), số lần ngập ngừng và bỏ cuộc, và chênh lệch giữa tải được đề nghị và tải được phục vụ, để nhu cầu thật hiển thị. Điều này đặc biệt quan trọng trong cung cấp dịch vụ chính phủ, nơi công dân bỏ hàng đợi điện thoại hay đơn xin trợ cấp là nghĩa vụ chưa đáp ứng thay vì hồ sơ đã giải quyết, và báo cáo họ là đã xử lý vừa nói sai hiệu suất vừa đánh giá thấp năng lực mà công chúng được nợ.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Bạn không có thời gian cho mô hình hóa hàng đợi chính thức và không cần nó. Hãy với tới hai chiến thắng rẻ nhất trước: áp dụng Định luật Little cho tồn đọng của bạn để thấy thời gian chờ thật mà WIP ngụ ý, và theo dõi bảng kanban để tìm giai đoạn công việc dồn lại trước khi bạn tuyển người chống nút thắt có thể không tồn tại. Giữ mức sử dụng xa vách đá trên bất kỳ đường nhạy với độ trễ nào bằng cách để dư địa thay vì chỉnh nó, vì một sự cố trong đợt tăng trưởng tốn hơn nhiều so với chút năng lực nhàn rỗi.

**Doanh nghiệp nhỏ.** Không có chuyên gia hàng đợi trong nhân sự, hãy mua chỉ số thay vì xây mô hình. Chọn bàn hỗ trợ, môi giới thông điệp hay nền tảng lưu trữ đã báo cáo tốc độ đến, thời gian chờ và bỏ cuộc, và đọc những con số đó thay vì tự suy ra. Đóng khung quyết định là theo dõi hai triệu chứng: thời gian chờ leo phi tuyến khi bạn bận hơn, và khách hàng bỏ cuộc trước khi được phục vụ, vì một khách hàng mất là chi phí hàng đợi đau nhất với doanh nghiệp nhỏ.

**Doanh nghiệp lớn.** Công việc là biến tư duy hàng đợi thành kỷ luật chung qua nhiều đội: một ký hiệu thống nhất (λ, μ, ρ, thời gian chờ), chính sách WIP và dư địa mức sử dụng nhất quán, và tiêu chuẩn áp lực ngược để một hạ nguồn bão hòa không lan qua các dịch vụ. Đặt SLO và năng lực từ phân tích hàng đợi thay vì phỏng đoán, và quản lý hàng đợi của bạn như danh mục với đường cơ sở và rà soát để không đội đơn lẻ nào chạy nóng cô lập. Nướng phân tích vào quản trị năng lực và kiểm toán, để mục tiêu dư địa là quyết định có tài liệu mà ai đó sở hữu.

**Chính phủ.** Mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn năng lực. Hãy định cỡ tổng đài và hệ thống hướng công dân theo phương sai kỳ đỉnh (mùa khai thuế, cửa sổ ghi danh), không phải trung bình hằng năm, và bố trí nhân sự để giữ mức sử dụng xa vách đá khi nhu cầu tăng. Theo dõi ngập ngừng và bỏ cuộc như nhu cầu công chưa đáp ứng thay vì giấu chúng trong "cuộc gọi đã trả lời," và biện minh chi tiêu năng lực bằng ước tính thời gian chờ theo Định luật Little, cho kiểm toán viên và quan chức dân cử một lập luận bảo vệ được, dựa trên toán thay vì giai thoại.

## Ví dụ

**Công ty khởi nghiệp.** Một đội SaaS năm người chìm trong tồn đọng hỗ trợ giả định họ cần tuyển thêm một nhân viên. Trước khi tiêu tiền, họ áp dụng Định luật Little: 60 phiếu đang mở và 12 phiếu đóng mỗi ngày nghĩa là phiếu trung bình chờ khoảng 5 ngày, khớp với các email giận dữ. Theo dõi bảng kanban, họ nhận ra phiếu dồn lại chờ kỹ thuật, không phải hỗ trợ, nên họ giới hạn công việc đang làm và định tuyến báo cáo lỗi thẳng vào sprint thay vì để chúng xếp hàng. Thời gian chờ giảm xuống dưới hai ngày mà không tuyển thêm ai, và họ dùng ngân sách giải phóng cho nút thắt thật.

**Doanh nghiệp lớn.** Một nền tảng thanh toán định cỡ dịch vụ ủy quyền của mình đo được λ ≈ 850 yêu cầu/giây và μ mỗi nút ≈ 200/giây. Ngây thơ thì đó là ~5 nút (ρ = 0,85), nhưng biết ρ = 0,85 đã nghĩa là độ trễ đuôi tăng mạnh, đội cung cấp ở ρ ≈ 0,65 và dùng Định luật Little để dự đoán số yêu cầu đang bay và đặt độ sâu hàng đợi và thời gian chờ. Các sự cố mùa cao điểm từng xuất hiện "từ hư không" biến mất, vì đội không còn vận hành trên phần dốc của đường cong.

**Chính phủ.** Tổng đài của một cơ quan thuế mô hình hóa hỗ trợ mùa khai thuế như hàng đợi: đột biến lượng đến (λ), năng lực nhân viên (μ), và, quan trọng, **tốc độ bỏ qua (σ)** của công dân bỏ cuộc sau khi giữ máy lâu. Bằng cách theo dõi ngập ngừng và bỏ cuộc thay vì chỉ "cuộc gọi đã trả lời," lãnh đạo thấy nhu cầu chưa đáp ứng thật, bố trí nhân sự để giữ mức sử dụng xa vách đá trong kỳ đỉnh, và biện minh năng lực thêm bằng ước tính thời gian chờ theo Định luật Little, một lập luận bảo vệ được, dựa trên toán cho chi tiêu công thay vì giai thoại.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lý thuyết hàng đợi sinh lời bằng cách ngăn hai sai lầm đắt đỏ: **cung cấp thừa** (trả tiền cho năng lực nhàn rỗi bạn không cần) và, gây hại hơn nhiều, **cung cấp thiếu gần vách đá** (nơi tăng tải nhỏ gây độ trễ lớn, vi phạm SLA, khách hàng bỏ cuộc và chi tiêu khẩn cấp). Vì chi phí chạy gần 100% mức sử dụng là phi tuyến, khoản tiết kiệm từ "chỉ thêm chút tải" nhỏ và mặt trái là thảm khốc, chính xác là sự bất đối xứng mà một chút toán biến thành quyết định có chủ đích. Lợi tức được đo bằng sự cố tránh được, SLA đạt, khách hàng được giữ lại vốn sẽ ngập ngừng, và vòng trực ca bình lặng hơn.

Về **tổng chi phí sở hữu**, khung này rẻ để áp dụng (đó là tri thức, không phải công cụ) và nó cải thiện gần như mọi quyết định về năng lực, độ trễ và dòng chảy mà một tổ chức lớn đưa ra qua vòng đời hệ thống. Định luật Little và giới hạn WIP giảm thời gian chờ mà không mua gì (chiến thắng quy trình thuần túy), trong khi kỷ luật mức sử dụng đổi một chi phí trạng thái ổn định khiêm tốn, khả đoán lấy việc loại bỏ các thất bại đắt đỏ, khó đoán. Để lập luận với ban lãnh đạo, hãy chuyển một sự cố độ trễ gần đây thành đường cong mức sử dụng và cho thấy mục tiêu dư địa lẽ ra đã ngăn nó thế nào, và dùng Định luật Little để nối giảm WIP trực tiếp với phân phối nhanh hơn.

## Phản mẫu và cạm bẫy

- **Hoạch định năng lực quanh trung bình:** phớt lờ phương sai, thứ thực sự tạo ra hàng đợi.
- **Chạy nóng:** nhắm mức sử dụng 90%+ trên hệ thống nhạy với độ trễ và bị sốc bởi độ trễ đuôi.
- **Đếm bỏ qua là phục vụ:** coi khách hàng bỏ cuộc hay phiếu bị từ chối là đã xử lý, làm hỏng chỉ số.
- **Chất đống WIP:** nhầm bận rộn với thông lượng và kéo dài thời gian chờ.
- **Tối ưu thứ không phải nút thắt:** cải thiện các giai đoạn không phải ràng buộc và dời hàng đợi sang nơi khác.
- **Nhầm lẫn các MTTR:** báo cáo "khôi phục" trong khi đo "sửa chữa," hoặc ngược lại.
- **Hàng đợi không giới hạn:** không có áp lực ngược, nên hệ thống quá tải suy giảm thành sụp đổ thay vì xả tải.
- **Trung bình như tối đa:** thiết kế theo trung bình và bị gọi bởi cái đuôi.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Hàng đợi (phiếu, tác vụ, thông điệp, triển khai) không được quản lý và phản ứng; năng lực được đoán; mức sử dụng chạy ở nơi tải đáp xuống; vấn đề độ trễ làm đội bất ngờ và bị chữa cháy sau sự việc.
- **Mức 2, Phát triển:** Một vài đội thu thập chỉ số cơ bản (thông lượng, thời gian chờ trung bình) nhưng đọc chúng như trung bình và áp dụng không nhất quán; một số nhóm giới hạn WIP hay để dư địa trong khi số khác chạy nóng; không có ký hiệu chung, nên thực hành không truyền qua các đội.
- **Mức 3, Chuẩn hóa:** Một ký hiệu chung (λ, μ, ρ, thời gian chờ) được lập tài liệu và thực thi toàn tổ chức; giới hạn WIP và mục tiêu dư địa mức sử dụng được đặt có chủ đích cho mọi hệ thống nhạy với độ trễ; các MTTR khác nhau được phân biệt; hàng đợi có giới hạn với áp lực ngược là mặc định qua các dịch vụ.
- **Mức 4, Quản lý:** Hàng đợi được đo và kiểm soát theo đường cơ sở: tốc độ đến, tốc độ phục vụ, mức sử dụng, độ trễ đuôi (p95/p99), và thời gian chờ được theo dõi theo mục tiêu và SLO xác định; độ sâu hàng đợi, thời gian chờ và dư địa được suy ra từ Định luật Little thay vì đoán; ngập ngừng, bỏ cuộc và tốc độ bỏ qua được đếm để tải được đề nghị phân biệt với tải được phục vụ; quyết định năng lực được rà soát dựa trên bằng chứng này, không phải cảm giác.
- **Mức 5, Điều phối:** Dòng chảy được mô hình hóa liên tục như hàng đợi của các hàng đợi; nút thắt được xác định và giải tỏa như thực hành liên tục; năng lực, SLO và áp lực ngược thích ứng với nhu cầu và phương sai dịch chuyển; chỉ số hàng đợi nối trực tiếp với DORA và KPI kinh doanh, và tổ chức cân bằng lại năng lực qua toàn bộ dòng chảy khi bức tranh tải và rủi ro thay đổi.

## Ý tưởng để thảo luận

1. Hệ thống nhạy với độ trễ của bạn thực sự chạy ở mức sử dụng nào, và vách đá của chúng ở đâu?
2. Áp dụng Định luật Little cho tồn đọng hiện tại của bạn: WIP ÷ thông lượng ngụ ý thời gian chờ nào, và nó có khớp thực tế không?
3. Hàng đợi nào của bạn lặng lẽ đếm "bỏ qua" (bỏ cuộc, từ chối) như thể chúng đã được phục vụ?
4. Hạ WIP sẽ rút ngắn thời gian chờ rẻ hơn thêm năng lực ở đâu?
5. Giai đoạn nào trong dòng chảy từ ý tưởng đến sản xuất của bạn là nút thắt thật, và các cải thiện của bạn có nhắm vào đó không?
6. Bảng điều khiển của bạn có cho thấy trung bình ở nơi cái đuôi mới là thứ thực sự làm bạn đau không?

## Những điểm cần ghi nhớ

- Hàng đợi khách hàng, bảng kanban, hàng đợi thông điệp và quy trình triển khai đều là hàng đợi bị chi phối bởi cùng các định luật.
- **Định luật Little (κ = λτ)** neo hoạch định dòng chảy: thời gian chờ = WIP ÷ thông lượng.
- Mức sử dụng và thời gian chờ là **phi tuyến**: hãy cung cấp dư địa; 15% cuối là đắt nhất.
- Theo dõi bức tranh đầy đủ: đến, phục vụ, thành công, **thất bại và bỏ qua**, và chờ; đừng để việc bỏ cuộc ẩn đi.
- Mô hình hóa quy trình như **hàng đợi của các hàng đợi** và sửa **nút thắt**, không phải sự bận rộn.
- Chỉ số hàng đợi ánh xạ trực tiếp vào thước đo **DORA/luồng** và **SLI/SLO** (chương 11.1, 11.2, 9.1), cho cả tổ chức một ngôn ngữ chung cho năng lực và dòng chảy.

## Tài liệu tham khảo và đọc thêm

- Bob Wescott, *Seven Insights into Queueing Theory* (và *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): Định luật Little.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: các chỉ số DORA dựa trên luồng khớp với KPI hàng đợi.
- Donald Reinertsen, *The Principles of Product Development Flow*: hàng đợi, kích thước lô và kinh tế WIP.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: Định luật Little áp dụng cho kanban.
- Joel Parker Henderson, *Queueing Theory*: ký hiệu, KPI và hàng đợi của các hàng đợi (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory," "M/M/1 queue," "Little's law," "Markov chain."
