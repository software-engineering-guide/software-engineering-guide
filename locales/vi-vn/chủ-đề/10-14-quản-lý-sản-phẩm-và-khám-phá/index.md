# 10.14 Quản lý sản phẩm và khám phá

## Tổng quan và động lực

[Quản lý sản phẩm](https://en.wikipedia.org/wiki/Product_management) là kỷ luật quyết định *xây gì* và *vì sao*, và chịu trách nhiệm về việc nó có hiệu quả không. Một quản lý sản phẩm sở hữu vấn đề, khách hàng và kết quả. Họ không sở hữu lịch trình, hàng đợi phiếu, hay danh mục tính năng được một bên liên quan giao xuống. Sự phân biệt đó là cả chương trong một câu. Khi quản lý sản phẩm sụp đổ thành điều phối dự án hay nhận đơn hàng, một đội trở thành nhà máy tính năng: nó phát hành liên tục, đạt số vận tốc, và không dịch chuyển chỉ số kinh doanh nào. Vai trò này tồn tại để ngăn chính điều đó.

Với các đội lớn, quản lý sản phẩm yếu lặng lẽ là kiểu thất bại đắt nhất có. Kỹ thuật có thể xuất sắc, phân phối có thể nhanh, và cả bộ máy vẫn có thể dành một năm xây sai thứ với hiệu quả lớn. Chi phí không bao giờ hiện trên bảng điều khiển kỹ thuật. Nó hiện ra là doanh thu phẳng, khách hàng rời bỏ, và một tồn đọng các tính năng không ai dùng nhưng mọi người giờ phải bảo trì. Quản lý sản phẩm tốt làm rủi ro đó hiển thị trước khi bạn cam kết tiền, bằng cách khăng khăng rằng mục tiêu phải tường minh, đo được, và gắn với vấn đề thật của khách hàng.

Bối cảnh doanh nghiệp và chính phủ nâng rủi ro và đổi hình dạng công việc. Doanh nghiệp ngày càng chuyển từ mô hình vận hành dự án (tài trợ một dự án, phát hành nó, giải tán đội) sang mô hình vận hành sản phẩm (tài trợ các đội bền vững sở hữu kết quả qua nhiều năm), và coi nền tảng nội bộ là sản phẩm có khách hàng thật. Chính phủ đang học cùng bài học dưới ngọn cờ thiết kế lấy người dùng làm trung tâm: tài trợ dịch vụ, không phải dự án, và đo xem công dân có thực sự được phục vụ không. Chương này nói về tư duy và cơ chế làm sự chuyển đổi đó thành thật. Nó ghép chặt với chương 11.1 (đường ống khám phá), chi tiết hóa bộ máy đường ống; ở đây chúng ta tập trung vào vai trò, chiến lược và thói quen khám phá hằng ngày.

## Các nguyên tắc chính

- **Sở hữu cái gì và vì sao.** Quản lý sản phẩm chịu trách nhiệm về kết quả, không phải về điều phối nhiệm vụ.
- **Kết quả hơn đầu ra.** Phát hành là chi phí, không phải kết quả. Kết quả là một khách hàng hay chỉ số kinh doanh đã thay đổi.
- **Hiểu khách hàng và vấn đề hơn bất kỳ ai.** Chiến lược không có tiếp xúc khách hàng là phỏng đoán.
- **Khám phá là liên tục, không phải một giai đoạn.** Bạn nói chuyện với khách hàng mỗi tuần, song song với phân phối.
- **Khung ưu tiên là công cụ hỗ trợ phán đoán, không phải thần dụ.** Con số thông tin cho quyết định; chúng không đưa ra nó.
- **Lộ trình là tuyên bố ý định, không phải lời hứa có ngày.** Cam kết chắc với vấn đề và lỏng với giải pháp.
- **Trao quyền cho bộ ba.** Sản phẩm, thiết kế và kỹ thuật cùng quyết định; một quản lý sản phẩm một mình quyết định tệ.

## Khuyến nghị

### Sở hữu cái gì và vì sao, và để đội sở hữu như thế nào

Phép thử rõ nhất cho việc quản lý sản phẩm có lành mạnh không là ai sở hữu câu hỏi nào. Quản lý sản phẩm sở hữu *vấn đề chúng ta đang giải là gì* và *vì sao nó quan trọng ngay bây giờ*. Thiết kế sở hữu *nó nên có cảm giác thế nào* với người dùng. Kỹ thuật sở hữu *chúng ta xây nó thế nào*. Khi một quản lý sản phẩm bắt đầu áp đặt giải pháp, hạn chót và triển khai, họ đã trở thành quản lý dự án mang chức danh sản phẩm, và đã lấy đi chính quyền tự chủ làm một đội được trao quyền hiệu quả (chương 5.1 bao quát quan hệ đối tác thiết kế, chương 10.7 bao quát mô hình phân phối agile).

Một đội sản phẩm được trao quyền, đôi khi gọi là bộ ba sản phẩm, làm việc như sản phẩm, thiết kế và kỹ thuật cùng nhau, được giao một vấn đề để giải thay vì một tính năng để xây. Đây là sự khác biệt giữa "tăng tỷ lệ giữ chân 30 ngày cho người dùng mới" và "xây trung tâm thông báo trước tháng Ba." Cái đầu trao quyền cho đội tìm giải pháp tốt nhất và buộc họ chịu trách nhiệm về kết quả. Cái sau rút họ thành cánh tay phân phối và lặng lẽ chuyển rủi ro sai sang người viết yêu cầu. Nếu bạn muốn trách nhiệm về kết quả, bạn phải trao đi quyền kiểm soát đầu ra.

### Đặt tầm nhìn và chiến lược sản phẩm đặt nền trên khách hàng

[Chiến lược sản phẩm](https://en.wikipedia.org/wiki/Product_strategy) là một tập nhỏ các lựa chọn khó về khách hàng nào bạn phục vụ, vấn đề nào bạn giải cho họ, và, quan trọng không kém, vấn đề nào bạn từ chối. Tầm nhìn là bức tranh bền vững về thế giới bạn đang cố tạo ra, thường hai đến năm năm nữa. Chiến lược là chuỗi các nước đi đưa bạn đến đó. Không có cả hai, ưu tiên thoái hóa thành ai tranh luận to nhất, và lộ trình trở thành danh sách các tính năng yêu thích của mọi người được ghim lại với nhau.

Chiến lược là bất khả thi nếu không có hiểu biết trực tiếp, sâu sắc về khách hàng và vấn đề. Một quản lý sản phẩm không mô tả được, chi tiết cụ thể, khách hàng là ai, họ đang cố hoàn thành việc gì, và họ đang chật vật ở đâu, chưa sẵn sàng ưu tiên bất cứ thứ gì. Đây không phải khảo sát bạn đặt hàng một lần. Đó là thói quen tiếp xúc thường trực. Các lãnh đạo sản phẩm giỏi nhất kể lại được cuộc trò chuyện khách hàng tuần trước từ trí nhớ, không phải bộ slide nghiên cứu quý trước. Khi bạn biết vấn đề thấu đáo, hầu hết tranh luận ưu tiên tan biến, vì đội có thể lập luận từ bằng chứng thay vì ý kiến.

### Quản lý theo kết quả và thoát khỏi nhà máy tính năng

Nhà máy tính năng là thứ bạn nhận được khi thành công được định nghĩa là "chúng ta đã phát hành nó." Các đội đo vận tốc, đếm bản phát hành, và ăn mừng các lần ra mắt, trong khi các chỉ số trả hóa đơn nằm yên. Thuốc giải là định nghĩa thành công là một kết quả (thay đổi trong hành vi khách hàng hay kinh doanh) và gắn một thước đo vào nó trước khi bạn xây. Đây là nơi quản lý sản phẩm gặp mục tiêu và kết quả then chốt (chương 11.4): mục tiêu mô tả thay đổi bạn muốn, kết quả then chốt đo nó, và một kết quả then chốt phát biểu là "ra mắt tính năng X" là một nhiệm vụ cải trang.

Hãy coi chừng các dấu hiệu. Nếu lộ trình của bạn là danh sách tính năng không nêu kết quả, nếu không ai nói được chỉ số nào một tính năng đã phát hành dịch chuyển, nếu buổi nhìn lại không bao giờ hỏi "nó có hiệu quả không" mà chỉ hỏi "chúng ta đã phát hành chưa," bạn đang ở trong nhà máy tính năng. Thoát khỏi nó phần lớn là vấn đề kỷ luật: từ chối nhận công việc đóng khung như giải pháp cho đến khi ai đó nêu vấn đề và thước đo. Phân tích sản phẩm và thí nghiệm có kiểm soát (chương 7.4) cho bạn bảng đồng hồ để phân biệt kết quả thật với câu chuyện dễ chịu.

### Chạy khám phá liên tục song song với phân phối

Khám phá sản phẩm liên tục nghĩa là mỗi tuần, song song với phân phối, đội học từ khách hàng và kiểm thử các giả định đằng sau điều nó định xây. Mô hình là hai đường: đường khám phá giảm rủi ro cho ý tưởng trong khi đường phân phối xây những cái đã xác thực, và cả hai chạy liên tục thay vì các giai đoạn tuần tự (chương 11.1 chi tiết hóa đường ống). Cam kết thực tế đằng sau là nhỏ và không ngừng: nói chuyện với khách hàng mỗi tuần, ngay cả khi bạn bận, nhất là khi bạn bận.

Một xương sống hữu ích cho việc này là cây cơ hội-giải pháp: bạn bắt đầu từ một kết quả mong muốn, rẽ nhánh sang các cơ hội của khách hàng (nhu cầu, điểm đau, mong muốn) có thể dịch chuyển nó, rẽ nhánh lần nữa sang các giải pháp ứng viên cho từng cơ hội, rồi sang các phép thử giả định cho bạn biết một giải pháp có hiệu quả không. Cây giữ đội trung thực về *vì sao* một tính năng đang nằm trên bàn và buộc bạn so sánh các cơ hội thay vì phải lòng giải pháp đầu tiên. Trước khi cam kết kỹ thuật, bạn kiểm thử giả định rủi ro nhất bằng thí nghiệm rẻ nhất: một cuộc phỏng vấn, một nguyên mẫu, một phép thử cửa giả, một phép thử A/B. Đầu ra của khám phá không phải danh sách tính năng. Đó là dòng các canh bạc đã xác thực, đo được sẵn sàng cho phân phối.

### Dùng khung ưu tiên như công cụ hỗ trợ phán đoán, không phải thần dụ

Khung ưu tiên mang cấu trúc hữu ích cho quyết định lộn xộn, và mỗi cái đều sai nếu bạn coi con số của nó là sự thật. **RICE** chấm mỗi ý tưởng theo Tầm với (bao nhiêu người dùng), Tác động, Độ tin cậy và Công sức, rồi xếp hạng theo (Tầm với x Tác động x Độ tin cậy) / Công sức. **Chấm điểm có trọng số** đánh giá các phương án theo nhiều tiêu chí có trọng số. **Chi phí trì hoãn** hỏi mỗi tuần chờ tốn bạn bao nhiêu, thường là lăng kính sắc nhất để sắp thứ tự. [Mô hình Kano](https://en.wikipedia.org/wiki/Kano_model) phân loại tính năng thành kỳ vọng cơ bản, nhu cầu hiệu suất và điều làm vui lòng, nhắc bạn rằng không phải mọi sự hài lòng đều tuyến tính.

Hãy dùng chúng để làm lộ giả định và để các đánh đổi có thể thảo luận, không phải để từ bỏ quyết định. Số hạng Độ tin cậy trong RICE và các ước tính trong chấm điểm có trọng số là phán đoán khoác áo số học, và độ chính xác giả có thể rửa một canh bạc tệ thành danh sách xếp hạng trông khách quan. Chạy các con số, rồi hỏi liệu thứ hạng có khớp chiến lược và hiểu biết khách hàng của bạn không. Nếu không, hãy tin phán đoán và chất vấn đầu vào. Khung là công cụ suy nghĩ; bạn vẫn là người phải đúng.

### Coi lộ trình là tuyên bố ý định

Một lộ trình có ngày hứa các tính năng cụ thể vào các quý cụ thể là hư cấu mà mọi người ký và không ai giữ được, vì nó cố định đúng thứ (giải pháp) mà khám phá được cho là tiếp tục học. Hãy ưu tiên lộ trình **bây giờ / tiếp theo / sau này**: cái chúng ta đang làm bây giờ, cái có khả năng tiếp theo, và cái chúng ta đang cân nhắc sau này, diễn đạt dưới dạng vấn đề và kết quả thay vì tính năng cam kết kèm ngày. Điều này truyền đạt hướng đi một cách trung thực trong khi bảo toàn tự do đổi giải pháp khi bằng chứng đến.

Nước đi nền tảng là cam kết chắc với vấn đề và kết quả, và lỏng với giải pháp. Các bên liên quan đòi cam kết tính năng chắc ngày thường đang xin khả năng dự đoán, điều hợp lý; hãy trao nó ở cấp kết quả và khung thời gian ("chúng ta sẽ giảm đáng kể tỷ lệ rời bỏ khi làm quen nửa năm này") thay vì ở cấp tính năng cụ thể bạn chưa xác thực. Khi bạn phải đưa ngày cứng, hãy gắn nó với kết quả có giá trị và để phạm vi giải pháp co giãn, chính xác như chương 10.6 khuyến nghị cho phân phối dự án.

### Xác thực tính mong muốn, khả thi về kinh doanh, khả thi về kỹ thuật và khả dụng

Trước khi bạn cam kết đầu tư thật, một ý tưởng sản phẩm phải vượt bốn rủi ro. **Tính mong muốn**: khách hàng có thực sự muốn nó không? **Khả thi kinh doanh**: nó có hiệu quả cho doanh nghiệp không (pháp lý, tài chính, thương hiệu, bán hàng)? **Khả thi kỹ thuật**: kỹ thuật có xây được với thời gian và công nghệ sẵn có không? **Khả dụng**: người ta có thực sự dùng được nó không? Bộ ba được xây để bao quát chúng: sản phẩm dẫn dắt khả thi kinh doanh, thiết kế dẫn dắt khả dụng, kỹ thuật dẫn dắt khả thi kỹ thuật, và tính mong muốn là vấn đề của mọi người. Bỏ qua một cái và nó quay lại là một lần ra mắt khách hàng phớt lờ, pháp lý chặn, kỹ thuật không phát hành được, hoặc người dùng không hiểu nổi.

Đây cũng là khung cho quyết định xây, mua hay hợp tác. Nếu một năng lực là cốt lõi cho sự khác biệt của bạn, hãy xây nó. Nếu nó cần thiết nhưng không tạo khác biệt (thanh toán, xác thực, gửi email), hãy mạnh mẽ ưu tiên mua hoặc hợp tác, vì mọi tính năng bạn xây mang cái đuôi vĩnh viễn của bảo trì, bề mặt bảo mật và gánh nặng nhận thức. [Sản phẩm khả thi tối thiểu](https://en.wikipedia.org/wiki/Minimum_viable_product) (MVP) là thứ rẻ nhất kiểm thử giả định rủi ro nhất của bạn, không phải phiên bản 1.0 rút gọn bạn phát hành rồi quên; hãy giữ nó trung thực bằng cách hỏi bạn sẽ học được gì, không chỉ bạn sẽ ra mắt gì.

### Biết sự khớp sản phẩm-thị trường và đầu tư vào vận hành sản phẩm

[Sự khớp sản phẩm-thị trường](https://en.wikipedia.org/wiki/Product/market_fit) là khoảnh khắc một sản phẩm thỏa mãn nhu cầu thị trường mạnh, và bạn thường cảm thấy nó trước khi chứng minh được: đường cong giữ chân phẳng ra thay vì suy giảm về không, mức dùng tăng nhờ truyền miệng, khách hàng sẽ thực sự buồn nếu mất sản phẩm, và bạn chật vật theo kịp nhu cầu thay vì tạo ra nó. Trước khi khớp, việc của bạn là tìm ra nó, và gần như không gì khác quan trọng. Sau khi khớp, việc của bạn đổi sang mở rộng và bảo vệ nó. Nhầm lẫn hai giai đoạn (mở rộng trước khi có sự khớp, hoặc vẫn tìm kiếm sau khi đã có) là sai lầm kinh điển và đắt.

Khi số đội sản phẩm tăng, hãy đầu tư vào **vận hành sản phẩm**: nghiên cứu, dữ liệu, công cụ và thực hành dùng chung cho phép nhiều đội làm khám phá tốt mà không mỗi đội phát minh lại. Vận hành sản phẩm giữ nhịp phỏng vấn khách hàng được bố trí nhân sự, phân tích đáng tin, định dạng lộ trình nhất quán, và nhịp OKR chạy. Trong doanh nghiệp chuyển sang mô hình vận hành sản phẩm, và trong tổ chức nền tảng-như-sản-phẩm nơi nền tảng nội bộ có khách hàng nội bộ thật, vận hành sản phẩm là thứ giữ mô hình mạch lạc qua hàng chục đội thay vì để nó phân mảnh thành thói quen cục bộ.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Đội sản phẩm được trao quyền (kết quả)** | Sở hữu kết quả; tìm giải pháp tốt hơn; có động lực | Cần nhân tài cấp cao và lòng tin thật; khó chỉ đạo từ trên xuống |
| **Mô hình đội tính năng / nhận đơn hàng** | Đầu ra khả đoán; dễ quản lý và ký hợp đồng | Phát hành sai thứ một cách hiệu quả; không ai sở hữu kết quả |
| **Khám phá liên tục** | Giảm rủi ro canh bạc hằng tuần; học nhanh; ít lãng phí | Cần năng lực nghiên cứu và kỷ luật; khó lên lịch hơn |
| **Yêu cầu chi tiết nặng từ đầu** | Thoải mái cho nhà tài trợ; phạm vi rõ ràng | Giả định chưa kiểm thử; phản hồi muộn; rủi ro đại bùng nổ |
| **Lộ trình bây giờ/tiếp theo/sau này** | Trung thực về bất định; bảo toàn việc học | Làm bực bội các bên liên quan muốn cam kết tính năng có ngày |
| **Lộ trình tính năng có ngày** | Cảm giác khả đoán; dễ truyền đạt | Hứa điều bạn không thể biết; thưởng đầu ra hơn kết quả |
| **Ưu tiên theo điểm khung** | Có cấu trúc, thảo luận được, giảm chính trị | Độ chính xác giả; có thể rửa một canh bạc tệ thành khách quan |

Căng thẳng trung tâm là **cam kết so với học**. Ngân sách, hợp đồng và lãnh đạo muốn cam kết chắc, kéo về lộ trình tính năng có ngày và yêu cầu từ đầu. Sản phẩm tốt cần chỗ để khám phá, kéo về kết quả và thí nghiệm liên tục. Hãy giải quyết nó như xuyên suốt cẩm nang này: cam kết chắc với vấn đề, kết quả và khung thời gian, và giữ giải pháp cụ thể lỏng. Điều đó cho lãnh đạo khả năng dự đoán họ thực sự cần (tiến bộ đo được trên những thứ quan trọng) mà không buộc đội hứa các tính năng nó chưa xác thực.

## Câu hỏi để thảo luận với đội của bạn

1. **Quản lý sản phẩm của bạn sở hữu một kết quả, hay một tồn đọng?** Đây là câu hỏi tiết lộ nhiều nhất về cách đội bạn thực sự vận hành. Nếu quản lý sản phẩm được đo theo việc phát hành lộ trình, chạy theo yêu cầu của bên liên quan và giữ sprint đầy, bạn có một điều phối viên dự án mang chức danh sản phẩm, và không ai thực sự chịu trách nhiệm về việc công việc có dịch chuyển chỉ số không. Hãy mang bằng chứng: nhìn ba sản phẩm bàn giao gần nhất của quản lý sản phẩm và hỏi mỗi cái được cho là đổi kết quả khách hàng hay kinh doanh nào, và có ai kiểm tra không. Trong tổ chức lớn rủi ro cộng dồn, vì một đội đơn lẻ hướng vào đầu ra có thể đốt nhiều quý xây các tính năng thử nghiệm tốt trong bản trình diễn và không đổi gì trong môi trường sản xuất. Câu trả lời nên định hình lại cả việc bạn đo quản lý sản phẩm theo gì lẫn bao nhiêu quyền kiểm soát giải pháp bạn sẵn lòng trao cho đội. Nếu không ai sở hữu kết quả, hãy sửa điều đó trước khi tranh luận về lộ trình.

2. **Lần cuối ai đó trong đội này nói chuyện với khách hàng là khi nào, và có phải tuần này không?** Khám phá liên tục sống hay chết nhờ thói quen này, và nó là thứ đầu tiên bị cắt khi áp lực phân phối tăng, chính là lúc bạn cần nó nhất. Các đội thôi nói chuyện với khách hàng không nhận ra mình đã mù; họ đơn giản bắt đầu lập luận từ ý kiến nội bộ và nghiên cứu cũ, ngày càng tự tin hơn và kém đúng hơn. Hãy mang nhật ký thật: đếm trong mười tính năng gần nhất của bạn có bao nhiêu cái đi qua một giả định có tài liệu và phép thử rẻ trước khi xây, so với đi thẳng từ miệng bên liên quan vào tồn đọng. Với đội doanh nghiệp và chính phủ, nơi một sáng kiến lệch hướng có thể lãng phí nhiều quý-đội và, trong khu vực công, lòng tin công thật, hãy nêu ai chịu trách nhiệm giữ tiếp xúc khách hàng hằng tuần sống. Nếu câu trả lời trung thực là "không phải tuần này" hay "không chắc," bạn đang bay trên giả định và gọi đó là chiến lược.

3. **Cần gì để chuyển từ mô hình vận hành dự án sang mô hình vận hành sản phẩm, và cái gì đang cản bạn?** Nhiều doanh nghiệp vẫn tài trợ dự án tạm thời, bố trí nhân sự, phát hành, và giải tán đội, điều phá hủy quyền sở hữu bền vững và tri thức khách hàng mà công việc sản phẩm tốt phụ thuộc. Chuyển sang các đội bền vững sở hữu kết quả qua nhiều năm, gồm coi nền tảng nội bộ là sản phẩm có khách hàng thật, là thay đổi về tài trợ, thiết kế tổ chức và quản trị, không chỉ đổi chức danh. Hãy mang bằng chứng: truy xem một sáng kiến hiện tại được tài trợ và bố trí nhân sự thế nào, và hỏi chuyện gì xảy ra với việc học tích lũy khi dự án kết thúc và đội tản đi. Cân nhắc đối lập là thật, vì ngân sách dự án hằng năm và quy tắc mua sắm tồn tại vì lý do trách nhiệm giải trình chính đáng, và bạn phải thỏa mãn chúng, không phải phớt lờ. Câu trả lời nên xác định bước cụ thể nhỏ nhất (một đội bền vững sở hữu một kết quả với ngân sách ổn định) chứng minh mô hình trước khi bạn thử chuyển cả danh mục (chương 10.1).

4. **Khi chúng ta chạy khung ưu tiên, nó đang thông tin cho quyết định hay chỉ phê chuẩn một quyết định đã đưa ra?** RICE, chấm điểm có trọng số và chi phí trì hoãn hữu ích chính xác vì chúng buộc giả định ra ánh sáng, và chúng trở nên ăn mòn ngay khi một con số thành cái cớ để thôi suy nghĩ. Cân nhắc đối lập là thật: khung giảm chính trị và cho dấu vết giấy tờ bảo vệ được, điều tổ chức lớn thực sự cần, vậy mà số hạng Độ tin cậy và Tác động là phán đoán khoác áo số học và có thể rửa một canh bạc tệ thành thứ hạng trông khách quan. Hãy mang vài quyết định ưu tiên gần nhất và kiểm tra hai điều: có ai bao giờ ghi đè điểm khi chiến lược hay hiểu biết khách hàng bất đồng không, và liệu sở thích của người lương cao nhất có lặng lẽ đặt các đầu vào tạo ra thứ hạng không. Trong bối cảnh doanh nghiệp và chính phủ, nơi tồn đọng có điểm thường thành hiện vật được trình ủy ban chỉ đạo và kiểm toán viên, hãy nêu ai được phép ghi đè con số và trên cơ sở nào, vì một khung không ai bác được đã thôi là công cụ suy nghĩ và thành con dấu cao su.

5. **Chúng ta đã hứa với các bên liên quan những tính năng có ngày nào, và chúng ta có thể phát biểu lại các cam kết đó thành kết quả mà không mất lòng tin của họ không?** Lộ trình tính năng có ngày cảm giác như khả năng dự đoán và thường là hư cấu, vì chúng cố định giải pháp mà khám phá được cho là tiếp tục học, và trong tổ chức lớn mỗi lời hứa như vậy lan sang các đội phụ thuộc, kế hoạch tiếp thị và kỳ vọng điều hành. Căng thẳng là chính đáng: nhà tài trợ và các bên liên quan muốn sự chắc chắn vì lý do ngân sách và trách nhiệm giải trình, nên bạn không thể đơn giản từ chối cam kết; bạn phải trao khả năng dự đoán ở cấp kết quả và khung thời gian thay vì tính năng chưa xác thực. Hãy mang lộ trình hiện tại và đánh dấu mỗi mục là kết quả bạn cam kết được hay giải pháp cụ thể bạn đang đoán, rồi soạn cách bạn sẽ phát biểu lại các phỏng đoán thành vấn đề bây giờ/tiếp theo/sau này. Với đội doanh nghiệp và khu vực công bị ràng buộc bởi ngân sách hằng năm và cột mốc mua sắm, hãy xác định cam kết nào thực sự là hợp đồng so với chỉ là thói quen, vì những cái thói quen là nơi bạn đổi độ chính xác giả lấy hướng đi trung thực, và những cái hợp đồng là nơi bạn phải thương lượng cam kết với một kết quả thay vì một tính năng.

6. **Chúng ta đang xây năng lực không tạo khác biệt ở đâu mà có thể mua hoặc hợp tác, và ai quyết định?** Mọi tính năng bạn xây mang cái đuôi vĩnh viễn của bảo trì, bề mặt bảo mật và tải hỗ trợ, nên tự tay làm thanh toán, xác thực hay gửi email tiêu năng lực khan hiếm nhất của bạn cho công việc không tạo khác biệt (chương 10.4). Cân nhắc đối lập là "mua" đổi kiểm soát và độ khớp lấy tốc độ và chi phí sở hữu thấp hơn, và đôi khi một năng lực bạn giả định là hàng hóa thực ra là cốt lõi cho lợi thế của bạn, nên lăng kính mong muốn-khả thi kinh doanh-khả thi kỹ thuật-khả dụng phải được áp dụng trung thực thay vì làm cái cớ cho sở thích. Hãy mang bản kiểm kê những gì các đội bạn đang xây nội bộ, đánh dấu mỗi cái là yếu tố tạo khác biệt cốt lõi hay đường ống không tạo khác biệt, và ước tính chi phí sở hữu liên tục của đường ống so với phương án nhà cung cấp. Trong bối cảnh doanh nghiệp và chính phủ, hãy tính cả quy tắc mua sắm, yêu cầu cư trú dữ liệu và bảo mật, và điều khoản khóa chặt nhà cung cấp và thoát, vì quyết định xây-mua-hợp tác ở đó không chỉ là đánh đổi kỹ thuật mà còn là đánh đổi tuân thủ và trách nhiệm giải trình, và người sở hữu nó phải bảo vệ được lựa chọn trước kiểm toán viên.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với ít đường băng, khám phá là sinh tồn, không phải quy trình. Một người sáng lập đội mũ sản phẩm, nói chuyện với khách hàng mỗi tuần không nghi thức, và chạy các phép thử rẻ nhất có thể (một nút cửa giả, năm cuộc phỏng vấn) trước khi cam kết một kỹ sư nào vào một bản xây. Bỏ qua khung nặng và lộ trình có ngày; cả công ty có thể giữ chiến lược trong đầu, nên hãy dành kỷ luật cho việc từ chối xây yêu cầu ồn ào cho đến khi ai đó nêu vấn đề và chỉ số.

**Doanh nghiệp nhỏ.** Bạn không có quản lý sản phẩm riêng, nên tư duy sản phẩm là thói quen mà chủ hay một kỹ sư trưởng mang bên cạnh các nhiệm vụ khác. Hãy đóng khung hầu hết quyết định mua-so-với-xây nghiêng về mua: năng lực không tạo khác biệt như đặt chỗ, thanh toán hay email thuộc về nhà cung cấp, và sự chú ý khan hiếm của bạn dành cho một hai thứ thực sự giành khách hàng. Giữ danh sách bây giờ/tiếp theo/sau này nhẹ thay vì lộ trình chính thức, và coi một chỉ số dẫn đầu duy nhất (mua lặp lại, vắng mặt) là kết quả của bạn thay vì cả bộ máy OKR.

**Doanh nghiệp lớn.** Công việc là phối hợp nhiều đội sản phẩm mà không để mô hình phân mảnh: các bộ ba bền vững sở hữu kết quả, định dạng lộ trình nhất quán, và vận hành sản phẩm giữ nhịp phỏng vấn, phân tích và nhịp OKR mạch lạc qua hàng chục đội. Quản trị và kiểm toán muốn truy vết, nên hãy làm kết quả, lý do ưu tiên và quyết định khai tử đọc được thay vì quay về lời hứa tính năng có ngày thỏa mãn ủy ban nhưng thưởng đầu ra hơn tác động. Quản lý sự chuyển từ tài trợ dự án sang mô hình vận hành sản phẩm có chủ đích, vì thiết kế tổ chức và ngân sách đổi chậm hơn chức danh.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy tài trợ các đội dịch vụ bền vững thay vì dự án phạm vi cố định, định nghĩa thành công là kết quả công dân (thời gian nộp đơn, hoàn tất tự phục vụ) mà cơ quan giám sát xác minh được, và coi thiết kế lấy người dùng làm trung tâm và tiêu chuẩn tiếp cận là yêu cầu cứng được kiểm thử với người nộp đơn thật, gồm người dùng công nghệ hỗ trợ. Công bố kết quả và tiến độ rõ ràng để sự soi xét thấy giá trị công, và cấu trúc quyết định xây-mua và hợp đồng nhà cung cấp quanh khả năng di chuyển dữ liệu và thoát để lựa chọn nhà cung cấp hôm nay không thành một thập kỷ khóa chặt.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người xây công cụ lập lịch cho các phòng khám độc lập cưỡng lại cám dỗ xây tính năng "đặt lịch trực tuyến" lớn mà ba khách hàng ồn ào cứ đòi. Người sáng lập kiêm quản lý sản phẩm chạy một tuần khám phá thay vào đó: năm cuộc phỏng vấn chủ phòng khám, một nút cửa giả trên trang tiếp thị, và một chỉ số dẫn đầu (phần trăm cuộc hẹn kết thúc bằng vắng mặt). Bằng chứng nói vắng mặt, không phải đặt lịch, là nỗi đau thật, nên đội đóng khung một kết quả duy nhất (cắt vắng mặt xuống dưới 10% cho các phòng khám thử nghiệm quý này), phát hành MVP đặt cọc-và-nhắc nhở nhỏ để kiểm thử giả định rủi ro nhất, và khai tử tính năng đặt lịch trước khi viết một dòng. Lộ trình là danh sách bây giờ/tiếp theo/sau này, không phải kế hoạch có ngày, và cả đội kể lại được cuộc gọi khách hàng tuần trước từ trí nhớ.

**Doanh nghiệp lớn.** Một ngân hàng bán lẻ chuyển nhóm thanh toán từ mô hình dự án sang mô hình sản phẩm: một bộ ba bền vững (sản phẩm, thiết kế, kỹ thuật) sở hữu "thanh toán hằng ngày có cảm giác tức thì" như kết quả thường trực với ngân sách hằng năm ổn định, thay vì một chuỗi dự án có điều lệ. Đội chạy phỏng vấn khách hàng hằng tuần và duy trì cây cơ hội-giải pháp, dùng RICE để sắp thứ tự các giải pháp ứng viên nhưng ghi đè thứ hạng khi phân tích chi phí trì hoãn cho thấy một bản sửa độ trễ quan trọng hơn, và công bố lộ trình bây giờ/tiếp theo/sau này cho các bên liên quan thay vì lời hứa tính năng có ngày. Hai tính năng đề xuất chết trong khám phá vì không dịch chuyển được các chỉ báo dẫn đầu, tiết kiệm ước tính hai quý công sức xây, và vận hành sản phẩm giữ nhịp phỏng vấn và phân tích đáng tin qua mười lăm đội sản phẩm của ngân hàng.

**Chính phủ.** Một cơ quan quốc gia hiện đại hóa các đơn xin trợ cấp áp dụng tư duy sản phẩm khu vực công mà các đội dịch vụ số ủng hộ: nó tài trợ một đội dịch vụ bền vững, không phải dự án phạm vi cố định, và định nghĩa thành công là kết quả công dân (cắt thời gian nộp đơn trung vị từ 40 xuống 15 phút và nâng tỷ lệ hoàn tất tự phục vụ thành công từ 55% lên 85%) thay vì các mô-đun được giao. Thiết kế lấy người dùng làm trung tâm là không thể thương lượng: đội chạy kiểm thử khả dụng có điều phối với người nộp đơn thật, gồm người dùng công nghệ hỗ trợ, trước mỗi bản phát hành, và coi tiêu chuẩn tiếp cận là yêu cầu cứng. Vì lộ trình được đóng khung dưới dạng kết quả và đội sở hữu dịch vụ qua nhiều năm, cơ quan giám sát thấy giá trị công đo được thay vì báo cáo chi tiêu, và cơ quan có thể phát hành năng lực hữu ích sớm thay vì đặt cược mọi thứ vào một ngày vận hành xa (chương 11.1, 5.1).

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của quản lý sản phẩm thật bị chi phối bởi **lãng phí tránh được**. Các chương trình thí nghiệm có kiểm soát ở các hãng công nghệ lớn liên tục thấy một phần lớn tính năng được xây, thường được trích dẫn khoảng một nửa, không tạo cải thiện đo được hoặc chủ động làm hại chỉ số mục tiêu. Nếu ngay cả một phần tư năng lực của đội dành cho ý tưởng mà khám phá liên tục lẽ ra khai tử rẻ, kỷ luật hoàn vốn nhiều lần: một tuần phỏng vấn khách hàng và phép thử cửa giả gần như không tốn gì so với một quý kỹ thuật, cộng việc bảo trì vĩnh viễn một tính năng không ai dùng. Chi phí chính của nhà máy tính năng không phải các tính năng nó phát hành. Đó là chi phí cơ hội của những kết quả nó không bao giờ dịch chuyển.

Về **tổng chi phí sở hữu**, mọi tính năng đã phát hành là một khoản nợ thường trực: bảo trì, kiểm thử, bề mặt bảo mật, tải hỗ trợ, và gánh nặng nhận thức lên mọi người phải điều hướng sản phẩm (chương 10.4). Quản lý sản phẩm hạ chi phí đó theo hai cách. Nó khai tử ý tưởng tệ trong khám phá, tránh không chỉ bản xây mà cả cái đuôi sở hữu. Và nó lái quyết định xây-mua-hợp tác về phía mua năng lực không tạo khác biệt, để năng lực hữu hạn của đội bạn dành cho thứ thực sự tạo khác biệt. Sự chuyển từ mô hình vận hành dự án sang mô hình vận hành sản phẩm thêm một lợi tức nữa, tinh tế hơn: các đội bền vững giữ lại tri thức khách hàng và ngữ cảnh cơ sở mã mà các đội dự án vứt bỏ mỗi lần giải tán và lập lại.

Để lập luận với ban lãnh đạo, hãy đổi cuộc trò chuyện từ "chúng ta phát hành bao nhiêu" sang "chúng ta dịch chuyển các chỉ số quan trọng bao nhiêu," và cho thấy hai ba ví dụ cụ thể về các tính năng đắt tiền không dịch chuyển gì. Chi phí áp dụng khiêm tốn: năng lực nghiên cứu, nhịp khám phá, lộ trình dựa trên kết quả, và kỷ luật định nghĩa thành công trước khi xây. Rủi ro của việc *không* đầu tư là im lặng, không đếm, và cộng dồn, vì nhà máy tính năng trông năng suất cho đến lúc bạn nhận ra doanh nghiệp chưa dịch chuyển.

## Phản mẫu và cạm bẫy

- **Nhà máy tính năng:** thành công được định nghĩa là "chúng ta đã phát hành nó," với vận tốc được ăn mừng trong khi chỉ số kinh doanh nằm yên.
- **Quản lý sản phẩm như quản lý dự án:** sở hữu lịch trình và hàng đợi phiếu thay vì vấn đề và kết quả.
- **Quản lý sản phẩm như thư ký tính năng:** chép yêu cầu của bên liên quan vào tồn đọng mà không gắn vấn đề hay thước đo.
- **Lộ trình như lời hứa tính năng có ngày:** cam kết các giải pháp cụ thể vào các quý cụ thể mà bạn chưa xác thực được.
- **Khám phá như giai đoạn một lần:** một sprint khám phá ban đầu, rồi nhiều tháng xây không còn tiếp xúc khách hàng.
- **Ưu tiên do HiPPO dẫn dắt:** ý kiến của người lương cao nhất ghi đè bằng chứng, và khung thành sân khấu để phê chuẩn nó.
- **Sùng bái khung:** coi điểm RICE hay có trọng số là sự thật, để độ chính xác giả rửa một canh bạc tệ.
- **Xây hạ tầng không tạo khác biệt:** tự tay làm thanh toán hay xác thực mà nhà cung cấp sẽ cung cấp tốt hơn và rẻ hơn.
- **Mở rộng trước khi khớp sản phẩm-thị trường:** đổ tiền vào tăng trưởng cho sản phẩm mà thị trường chưa muốn mạnh.
- **Nền tảng nội bộ không có chủ sở hữu sản phẩm:** đội nền tảng xây thứ nó thấy thú vị thay vì thứ khách hàng nội bộ cần.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Quản lý sản phẩm là nhận đơn hàng và phản ứng. Một lộ trình tính năng có ngày được giao xuống; thành công là phát hành nó. Không có kết quả nêu rõ, không tiếp xúc khách hàng đều đặn, và không ai chịu trách nhiệm về việc công việc có dịch chuyển chỉ số không.
- **Mức 2, Phát triển:** Thực hành sản phẩm cơ bản xuất hiện nhưng không nhất quán giữa các đội. Kết quả và OKR tồn tại ở một số đội, nhưng mục tiêu thường mang hình dạng đầu ra và lộ trình vẫn là danh sách tính năng. Khám phá xảy ra thỉnh thoảng, thường như giai đoạn ban đầu, và ưu tiên dùng khung, đôi khi làm cái cớ cho giọng nói to nhất.
- **Mức 3, Chuẩn hóa:** Các bộ ba được trao quyền sở hữu kết quả, và thực hành được lập tài liệu và kỳ vọng toàn tổ chức. Lộ trình là tuyên bố ý định bây giờ/tiếp theo/sau này; khám phá liên tục là thói quen hằng tuần được bố trí nhân sự với phép thử giả định có tài liệu; khung ưu tiên thông tin cho phán đoán thay vì thay thế nó; và sự khớp sản phẩm-thị trường được hiểu và theo dõi như tiêu chuẩn chung thay vì thói quen cục bộ.
- **Mức 4, Quản lý:** Thực hành được đo và kiểm soát theo đường cơ sở. Mỗi đội theo dõi các chỉ số kết quả dẫn đầu và trễ so với đường cơ sở đã nêu, và sau ra mắt mỗi tính năng được kiểm tra so với chỉ số thành công đăng ký trước với ngưỡng khai tử được thực thi dựa trên bằng chứng, không phải ý kiến. Sức khỏe khám phá cũng được gắn công cụ đo (nhịp phỏng vấn được đáp ứng, giả định được kiểm thử trước khi xây, ý tưởng bị khai tử trong khám phá so với được phát hành), tín hiệu khớp sản phẩm-thị trường như đường cong giữ chân và điểm sẽ-thất-vọng được định lượng, và đầu vào khung như Độ tin cậy RICE được hiệu chỉnh theo kết quả thực của các canh bạc.
- **Mức 5, Điều phối:** Một mô hình vận hành sản phẩm chạy qua danh mục và được cải thiện liên tục và tích hợp với tài trợ và chiến lược. Các đội bền vững sở hữu kết quả qua nhiều năm và nền tảng nội bộ được quản lý như sản phẩm; khám phá và phân phối lặp liên tục; dữ liệu kết quả lái đầu tư và cân bằng lại danh mục một cách thích ứng; vận hành sản phẩm giữ thực hành mạch lạc ở quy mô; và lãnh đạo quản lý một danh mục kết quả, thường lệ cho nghỉ hưu, thu hẹp phạm vi và ưu tiên lại các canh bạc khi bằng chứng và thị trường dịch chuyển.

## Ý tưởng để thảo luận

1. Nhìn lộ trình hiện tại của bạn: bao nhiêu mục nêu kết quả đo được so với chỉ một tính năng và một ngày?
2. Ai trong đội bạn sở hữu quan hệ khách hàng đủ tốt để kể lại cuộc trò chuyện tuần trước từ trí nhớ?
3. Tính năng gần đây nào của bạn sẽ bị bạn khai tử nếu bạn đã chạy một thí nghiệm rẻ cho giả định rủi ro nhất trước?
4. Bạn đang xây năng lực không tạo khác biệt ở đâu mà có thể mua hoặc hợp tác, và nó tốn bạn bao nhiêu?
5. Bạn có sự khớp sản phẩm-thị trường không, và làm sao bạn thực sự biết, thay vì giả định?
6. Bước nhỏ nhất bạn có thể làm hướng tới mô hình vận hành sản phẩm là gì, và rào cản quản trị nào cản đường?

## Những điểm cần ghi nhớ

- Quản lý sản phẩm sở hữu **cái gì** và **vì sao**, và chịu trách nhiệm về **kết quả**, không phải điều phối nhiệm vụ hay chép yêu cầu.
- Thoát khỏi **nhà máy tính năng** bằng cách định nghĩa thành công là thay đổi đo được trong hành vi khách hàng hay kinh doanh trước khi bạn xây.
- Chạy **khám phá liên tục** song song với phân phối: nói chuyện với khách hàng mỗi tuần và kiểm thử giả định rủi ro nhất bằng thí nghiệm rẻ nhất (chương 11.1).
- Dùng **khung ưu tiên** (RICE, chấm điểm có trọng số, chi phí trì hoãn, Kano) như công cụ hỗ trợ phán đoán, không bao giờ như thần dụ.
- Coi **lộ trình là tuyên bố ý định** (bây giờ/tiếp theo/sau này): cam kết chắc với vấn đề và kết quả, lỏng với giải pháp.
- Trao quyền cho **bộ ba** và xác thực **tính mong muốn, khả thi kinh doanh, khả thi kỹ thuật và khả dụng** trước khi bạn đầu tư (chương 5.1).
- Trong doanh nghiệp và chính phủ, chuyển từ **mô hình vận hành dự án** sang **mô hình vận hành sản phẩm**, tài trợ dịch vụ không phải dự án, và đầu tư vào **vận hành sản phẩm** (chương 10.1, 11.4).

## Tài liệu tham khảo và đọc thêm

- Marty Cagan, *Inspired* và *Empowered* (đội sản phẩm được trao quyền, mô hình vận hành sản phẩm).
- Marty Cagan và Chris Jones, *Transformed* (chuyển sang mô hình vận hành sản phẩm).
- Teresa Torres, *Continuous Discovery Habits* (cây cơ hội-giải pháp, tiếp xúc khách hàng hằng tuần).
- Melissa Perri, *Escaping the Build Trap* (kết quả hơn đầu ra, vận hành sản phẩm).
- Roman Pichler, *Strategise* (tầm nhìn, chiến lược và lộ trình sản phẩm).
- C. Todd Lombardo, Bruce McCarthy, Evan Ryan và Michael Connors, *Product Roadmaps Relaunched* (lộ trình bây giờ/tiếp theo/sau này).
- Dan Olsen, *The Lean Product Playbook* (sự khớp sản phẩm-thị trường).
- Eric Ries, *The Lean Startup* (sản phẩm khả thi tối thiểu, xây-đo-học).
- Noriaki Kano et al., "Attractive Quality and Must-Be Quality" (*Journal of the Japanese Society for Quality Control*, 1984): nguồn gốc của mô hình Kano.
- Melissa Perri và Denise Tilles, *Product Operations* (mở rộng thực hành sản phẩm).
- U.S. Digital Service, *Digital Services Playbook*; UK Government Digital Service, *Government Design Principles* và *Service Standard* (phân phối sản phẩm khu vực công, lấy người dùng làm trung tâm).
