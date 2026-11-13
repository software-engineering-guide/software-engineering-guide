# 10.7 Agile

## Tổng quan và động lực

[Agile](https://en.wikipedia.org/wiki/Agile_software_development) là một tư duy để phân phối phần mềm (và giá trị) theo cách lặp, gia tăng, và cộng tác chặt chẽ với những người sẽ dùng nó. Được hệ thống hóa trong *Tuyên ngôn Phát triển Phần mềm Agile* năm 2001, nó được hiểu tốt nhất không phải như một quy trình mà như một tập **giá trị và nguyên tắc**: ưu tiên cá nhân và tương tác, phần mềm hoạt động, cộng tác với khách hàng, và phản ứng với thay đổi, hơn những mặc định nặng kế hoạch, nặng hợp đồng, nặng tài liệu từng có trước đó. Các khung như [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) và [Lập trình Cực hạn](https://en.wikipedia.org/wiki/Extreme_programming) (XP) là *các triển khai* của tư duy đó. Chúng là điểm khởi đầu hữu ích, nhưng không phải bản thân tư duy. Chương này bổ sung cho chương 1.4 (cách làm việc, khảo sát các phương pháp một cách rộng) bằng cách đi sâu vào riêng Agile.

Agile được thúc đẩy bởi cùng lực tạo sức sống cho các đường ống khám phá và phân phối (chương 11.1–11.2): yêu cầu của phần mềm được *khám phá*, không được biết đầy đủ từ đầu, và thế giới đổi nhanh hơn một kế hoạch dài hấp thụ nổi. Phân phối đại bùng nổ, hoạch định mọi thứ trước, lặp đi lặp lại tạo ra các hệ thống trễ, vượt ngân sách và, tệ nhất, sai, vì toàn bộ việc học đến ở cuối, khi hành động theo nó đắt nhất. Canh bạc cốt lõi của Agile đơn giản: các chu kỳ ngắn xây phần mềm thật, hoạt động và nhận phản hồi thật thắng các chu kỳ dài suy đoán. Làm tốt, nó giảm rủi ro liên tục thay vì hoãn nó.

Với các đội lớn, doanh nghiệp và chính phủ, Agile vừa mạnh vừa thường bị xuyên tạc. Doanh nghiệp áp dụng nó qua hàng trăm đội và thường rút nó thành nghi lễ ("giờ chúng tôi họp đứng") mà không đổi cách đưa ra quyết định hay đo giá trị. Chính phủ đã đón nhận Agile có chủ đích, vì phân phối lặp, lấy người dùng làm trung tâm giảm rủi ro của các chương trình công lớn một cách có thể chứng minh: Dịch vụ Số Hoa Kỳ và *Digital Services Playbook* của nó, Dịch vụ Số Chính phủ Anh và Tiêu chuẩn Dịch vụ, và các cải cách mua sắm agile đều phát sinh một phần để đáp lại các thất bại [thác nước](https://en.wikipedia.org/wiki/Waterfall_model) gây chú ý. Phần thưởng là thật. Kiểu thất bại "agile chỉ trên danh nghĩa" cũng vậy.

## Các nguyên tắc chính

- **Coi trọng bốn giá trị của Tuyên ngôn** (con người, phần mềm hoạt động, cộng tác và khả năng đáp ứng) hơn các hiện vật quy trình.
- **Giao phần mềm hoạt động thường xuyên** theo các phần tăng trưởng nhỏ; phần mềm hoạt động là thước đo chính của tiến độ.
- **Chào đón thay đổi**, kể cả muộn; khả năng thích ứng là tính năng, không phải thất bại.
- **Xây quanh các đội có động lực, được trao quyền, tự tổ chức.**
- **Cộng tác liên tục với người dùng và các bên liên quan.**
- **Nhìn lại và cải thiện** theo nhịp đều đặn.
- **Duy trì nhịp độ nhân đạo** và sự xuất sắc kỹ thuật: tốc độ không có tay nghề sẽ sụp đổ.

## Khuyến nghị

### Neo vào giá trị và nguyên tắc, không phải nghi thức

Khuyến nghị Agile quan trọng nhất là dẫn đầu bằng *vì sao*. Một đội tổ chức họp đứng hằng ngày, buổi trình diễn sprint và buổi nhìn lại, nhưng vẫn cam kết phạm vi cố định vào ngày cố định, giấu tin xấu và không bao giờ đổi kế hoạch, không phải agile. Đó là thác nước có thêm cuộc họp. Hãy dùng mười hai nguyên tắc như danh mục kiểm tra cho sự nhanh nhẹn thật. Bạn có giao phần mềm hoạt động thường xuyên không? Bạn có chào đón được một thay đổi ở vòng lặp tới không? Đội có quyết định *cách* làm công việc không? Khách hàng có thực sự trong vòng lặp không? Nếu các nghi thức không tạo ra những kết quả đó, hãy sửa kết quả, không phải nghi thức.

### Chọn một khung làm điểm khởi đầu, không phải tôn giáo

Hãy chọn khung khớp công việc và điều chỉnh nó:

- **Scrum:** sprint có khung thời gian, một tồn đọng được ưu tiên, và các vai trò xác định (chủ sở hữu sản phẩm, scrum master, nhà phát triển). Tốt cho phân phối tính năng với chủ sở hữu sản phẩm rõ ràng; yếu khi công việc bị ngắt quãng nhiều.
- **Kanban:** luồng liên tục với giới hạn công việc đang làm tường minh và hệ thống kéo. Tốt cho hỗ trợ, vận hành và lượng việc đến khó đoán (và có nền tảng trực tiếp trong lý thuyết luồng và hàng đợi, xem chương 11.2, 11.3). Giới hạn WIP rút ngắn thời gian chờ ([Định luật Little](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Lập trình Cực hạn (XP):** các thực hành kỹ thuật gồm [phát triển hướng kiểm thử](https://en.wikipedia.org/wiki/Test-driven_development), [lập trình cặp](https://en.wikipedia.org/wiki/Pair_programming), [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration), tái cấu trúc, bản phát hành nhỏ. Xương sống kỹ thuật làm bất kỳ khung nào bền vững.
- **Scrumban** và các hỗn hợp: những tổ hợp thực dụng mà nhiều đội trưởng thành hội tụ về.

Khung là giàn giáo. Giữ cái giúp ích, bỏ cái không, và đừng bao giờ để "khung bảo vậy" ghi đè "nguyên tắc nói vì sao."

### Khăng khăng sự xuất sắc kỹ thuật

Agile không có kỷ luật kỹ thuật nhanh chóng thoái hóa thành sản xuất nhanh mã không bảo trì được, "scrum đen tối," nơi các đội chạy nước rút vào hố nhựa đường của lỗi và [nợ kỹ thuật](https://en.wikipedia.org/wiki/Technical_debt). Các thực hành XP không phải phần thêm tùy chọn. Tích hợp liên tục (chương 8.1), kiểm thử tự động (chương 2.4), tái cấu trúc, phát triển trên thân chính (chương 2.6) và thiết kế sạch (chương 2.2) là thứ cho phép một đội tiếp tục thay đổi phần mềm với chi phí rẻ, đó là toàn bộ tiền đề của sự nhanh nhẹn. Nhịp độ bền vững quan trọng vì cùng lý do: các đội kiệt sức không duy trì được chất lượng hay khả năng đáp ứng.

### Mở rộng cẩn thận, và ưu tiên thu nhỏ

Các khung mở rộng, như SAFe (Khung Agile Mở rộng), LeSS, Nexus và Scrum@Scale, phối hợp nhiều đội hướng tới mục tiêu chung. Chúng có thể giúp, nhưng mang một cảnh báo (vọng lại chương 1.4): các khung mở rộng nặng thường đưa trở lại chính chi phí chung chỉ huy-kiểm soát, nặng kế hoạch mà Agile được định ra để loại bỏ. Trước khi bạn áp dụng một khung lớn, hãy thử *thu nhỏ*. Tổ chức quanh các đội độc lập, căn chỉnh theo luồng với quyền sở hữu rõ ràng và phụ thuộc xuyên đội tối thiểu (chương 1.2), để bạn cần ít bộ máy phối hợp hơn ngay từ đầu. Nơi phối hợp thực sự cần, hãy thêm cấu trúc nhẹ nhất có tác dụng, và nối nó với kết quả (OKR, mục tiêu và kết quả then chốt, chương 11.1), không phải đầu ra.

### Làm sự nhanh nhẹn thành thật trong doanh nghiệp và chính phủ

Phân phối thích ứng và ràng buộc thể chế có thể cùng tồn tại, nhưng cần thiết kế có chủ đích:

- **Quản trị lai:** một lõi phân phối thích ứng bên trong vỏ tài trợ/tuân thủ dự đoán (chương 10.6), để lặp thỏa mãn thay vì chống lại giám sát.
- **Mua sắm agile:** hợp đồng mô-đun, dựa trên kết quả và các phần tăng trưởng ngắn hơn thay vì một siêu hợp đồng phạm vi cố định; đây là nơi Agile khu vực công thành hay bại nhiều nhất.
- **Tuân thủ khi đi:** xây kiểm toán, khả năng tiếp cận (chương 5.3) và bảo mật (chương 4.1) vào phần tăng trưởng qua tự động hóa và hàm thích nghi (kiểm tra tự động liên tục xác minh thuộc tính kiến trúc và chất lượng; chương 8.5, 1.6), không phải cổng muộn.
- **Tiếp cận người dùng thật:** khó nhất và quan trọng nhất. Các đội cần tiếp xúc thực sự với công dân hoặc khách hàng, điều mà quy tắc mua sắm và bảo mật thường cản trở.

### Cải thiện liên tục, và thực lòng

Buổi nhìn lại là động cơ cải thiện của Agile, và nó vô giá trị nếu không tạo thay đổi. Hãy chạy các buổi nhìn lại tạo ra một số ít hành động cụ thể, có chủ sở hữu, và thực sự hoàn thành chúng trước buổi tiếp theo. Đo kết quả (thay đổi có dịch chuyển một kết quả then chốt không? xem chương 11.1) và luồng (thời gian chờ có đang rút ngắn không? xem chương 11.2, 11.3). Đừng đo vận tốc: nó là tín hiệu năng lực trở thành lời nói dối ngay khi bạn dùng nó làm mục tiêu năng suất.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| **Agile (thích ứng)** | Phản hồi nhanh; hấp thụ thay đổi; giá trị sớm, liên tục | Khó cố định phạm vi/chi phí từ đầu; đòi khách hàng tham gia và kỷ luật |
| **Thác nước (dự đoán)** | Phạm vi khả đoán; thân thiện hợp đồng/kiểm toán | Phản hồi muộn; rủi ro đại bùng nổ; khớp kém với yêu cầu bất định |
| **Scrum** | Nhịp, vai trò, tập trung; được hiểu rộng rãi | Chi phí chung nghi thức; chật vật với công việc bị ngắt quãng |
| **Kanban** | Luồng, giới hạn WIP, linh hoạt; tuyệt cho vận hành | Ít cấu trúc hơn; cần kỷ luật để giữ giới hạn |
| **Mở rộng nặng (SAFe)** | Phối hợp nhiều đội; quen thuộc với tổ chức lớn | Có thể đưa lại chỉ huy-kiểm soát; nặng nghi thức |
| **Thu nhỏ / tự chủ đội** | Ít chi phí chung phối hợp; đội nhanh hơn | Đòi ghép nối thấp và nền tảng/quyền sở hữu mạnh |

Căng thẳng định nghĩa là **khả năng thích ứng so với khả năng dự đoán**, và hiểu sai kinh điển là Agile nghĩa là "không có kế hoạch." Không phải vậy. Nó nghĩa là hoạch định liên tục và cam kết với *kết quả và nhịp* trong khi để *phạm vi* co giãn. Cái bẫy lặp lại khác là coi Agile là *chỉ* quy trình (nghi thức) hay *chỉ* kỹ thuật (XP). Nó cần cả hai.

## Câu hỏi để thảo luận với đội của bạn

1. **Trong bối cảnh doanh nghiệp hay chính phủ của bạn, hợp đồng của bạn là mô-đun và dựa trên kết quả, hay phân phối bị khóa trong một siêu hợp đồng phạm vi cố định?** Mua sắm agile là nơi sự nhanh nhẹn khu vực công thành hay bại nhiều nhất, vì một hợp đồng giá cố định, phạm vi cố định duy nhất buộc thác nước bất kể các đội phân phối gọi cuộc họp của họ là gì. Hợp đồng mô-đun, dựa trên kết quả với các phần tăng trưởng ngắn hơn cho phép phạm vi co giãn về lõi có giá trị trong tài trợ cố định, chính xác là mô hình đằng sau các thành công khu vực công hiện đại và thuốc giải cho các thất bại đại bùng nổ trước đây. Hãy mang bằng chứng: nhìn các hợp đồng hiện tại của bạn và hỏi nhà cung cấp được trả cho phần mềm hoạt động đã chứng minh hay cho phạm vi cố định được ký duyệt nhiều năm trước. Câu trả lời nên định hình cách bạn cấu trúc lần mua sắm tiếp theo nhiều hơn khung nào các đội của bạn áp dụng nội bộ. Bạn không thể thích ứng trong phân phối khi hợp đồng của bạn bắt buộc một ngày vận hành xa, được ăn cả ngã về không.

2. **Kiểm toán, khả năng tiếp cận và bảo mật được xây vào mỗi phần tăng trưởng qua tự động hóa, hay gắn vào như cổng muộn?** Tuân thủ khi đi là thứ cho phép phân phối thích ứng cùng tồn tại với ràng buộc thể chế: xây các kiểm tra vào phần tăng trưởng qua tự động hóa và hàm thích nghi thay vì để dành cho cuộc chạy đua trước phát hành. Một cổng tuân thủ muộn đưa lại rủi ro đại bùng nổ mà Agile tồn tại để loại bỏ, vì những vấn đề đắt xuất hiện ở cuối khi khó sửa nhất. Hãy mang bằng chứng: với phần tăng trưởng gần nhất của bạn, kiểm tra xem khả năng tiếp cận, bảo mật và bằng chứng kiểm toán được xác minh tự động trong đường ống hay bị hoãn đến rà soát thủ công trước ra mắt. Câu trả lời nên đẩy những thuộc tính này vào các kiểm tra tự động liên tục, để giám sát được thỏa mãn bởi hành động xây dựng thay vì một giai đoạn riêng. Đây cũng là thứ giữ chương trình bị quản lý trung thực giữa các kỳ kiểm toán thay vì chỉ trong những tuần trước một kỳ.

3. **Làm sao bạn biết các đội đang chạy nước rút vào nợ kỹ thuật, và cái gì bảo vệ nhịp độ bền vững dưới áp lực ra mắt?** Agile không có kỷ luật kỹ thuật thoái hóa thành scrum đen tối, nơi các đội chạy nhanh vào hố nhựa đường của lỗi và mã không bảo trì được, và các đội kiệt sức không duy trì được chất lượng hay khả năng đáp ứng. Các thực hành XP (tích hợp liên tục, kiểm thử tự động, tái cấu trúc, phát triển trên thân chính) là thứ cho phép một đội tiếp tục thay đổi phần mềm với chi phí rẻ, đó là toàn bộ tiền đề của sự nhanh nhẹn, nên chúng không phải phần thêm tùy chọn để đánh đổi khi hạn chót lờ mờ. Hãy mang bằng chứng: theo dõi thời gian chờ đang rút ngắn hay kéo dài, tỷ lệ lỗi có tăng không, và đội có lặng lẽ làm việc nhiều giờ hơn để đạt mỗi sprint không. Câu trả lời nên làm sự xuất sắc kỹ thuật và nhịp độ nhân đạo không thể thương lượng, vì tốc độ mua bằng hy sinh tay nghề sụp đổ trong vài vòng lặp. Đo luồng và kết quả, không bao giờ vận tốc như mục tiêu, vì ngay khi bạn biến tín hiệu năng lực thành mục tiêu năng suất nó thành lời nói dối.

4. **Trước khi với tới một khung mở rộng nặng, bạn đã thử giảm các phụ thuộc xuyên đội tạo ra nhu cầu phối hợp ngay từ đầu chưa?** Điều này quan trọng nhất với tổ chức lớn, vì phản xạ khi nhiều đội phải phát hành cùng nhau là mua một khung như SAFe, LeSS hay Scrum@Scale, và bộ máy mở rộng nặng thường lén mang lại chỉ huy-kiểm soát, chi phí chung nặng kế hoạch mà Agile tồn tại để loại bỏ. Cân nhắc đối lập là thật: một số phối hợp thực sự cần, và thu nhỏ thành các đội độc lập, căn chỉnh theo luồng đòi ghép nối thấp, quyền sở hữu rõ ràng và nền tảng đủ trưởng thành để các đội tự phục vụ, điều bạn có thể chưa có. Hãy mang bằng chứng vào cuộc thảo luận: lập bản đồ các phụ thuộc thực buộc các đội chờ nhau, và hỏi bao nhiêu cái sẽ sống sót qua một thiết kế lại có chủ đích ranh giới đội và quyền sở hữu dịch vụ. Trong chương trình doanh nghiệp và chính phủ, nơi sơ đồ tổ chức hàng chục đội là phổ biến, câu hỏi trung thực là liệu bạn đang thêm cấu trúc phối hợp để bù cho kiến trúc và thiết kế đội mà bạn có thể đơn giản hóa thay vào đó, để bạn cần phối hợp ít hơn hẳn.

5. **Các đội của bạn có tiếp xúc thực sự, lặp lại với công dân hay khách hàng mà họ xây cho không, hay phản hồi đến qua trung gian lọc?** Cộng tác với khách hàng là một trong bốn giá trị của Tuyên ngôn, và các vòng lặp thiếu tiếp xúc người dùng thật lặng lẽ tối ưu thứ sai, đó là thất bại đắt nhất mà Agile được cho là ngăn ngừa. Căng thẳng là tiếp cận trực tiếp khó sắp xếp ở quy mô và thường bị cản trở bởi chính quy tắc mua sắm, riêng tư và bảo mật mà tổ chức lớn và công phải tuân theo, nên đường dễ là thay bằng trung gian: một nhà phân tích kinh doanh, một ủy ban các bên liên quan, hay bộ slide nghiên cứu quý trước. Hãy mang bằng chứng: với vài phần tăng trưởng gần nhất, đếm bao nhiêu cái được xác thực với người dùng thật thực sự dùng phần mềm, và bao nhiêu cái dựa trên ý kiến của ai đó về điều người dùng muốn. Với dịch vụ chính phủ, hãy thêm liệu kiểm thử khả dụng của bạn có đến được những người bị ảnh hưởng nhiều nhất không, gồm người dùng công nghệ hỗ trợ và người có sự tự tin kỹ thuật số thấp, vì một dịch vụ công chỉ hoạt động cho đa số tự tin đã thất bại nghĩa vụ giải trình của nó dù mọi nghi thức chạy đúng lịch.

6. **Các đội của bạn được tài trợ và quản trị quanh kết quả và nhịp, hay quanh phạm vi cố định lặng lẽ buộc hành vi thác nước đằng sau các nghi thức?** Đây là sự khác biệt giữa sự nhanh nhẹn thật và agile giả, và nó được quyết định phía trên đội, trong cách tiền được giải ngân và thành công được báo cáo, không phải ở việc họp đứng có diễn ra không. Lực kéo đối lập là các chức năng tài chính, danh mục và giám sát được xây để phê duyệt phạm vi cố định so với ngân sách cố định nhiều năm trước, và yêu cầu họ tài trợ một kết quả với phạm vi linh hoạt cảm giác như mất kiểm soát mà họ sẽ kháng cự. Hãy mang bằng chứng: truy xem một sáng kiến hiện tại được tài trợ thế nào và nó báo cáo về gì, và kiểm tra xem các đội được đo theo kết quả giao và luồng hay theo điểm story và sự tuân thủ phạm vi đã ký duyệt từ lâu. Trong bối cảnh doanh nghiệp và chính phủ, hãy nối điều này trực tiếp với vỏ tài trợ và tuân thủ (chương 10.6): nếu tiền được cam kết cho một ngày vận hành xa, ăn cả ngã về không, các đội không thể thích ứng bất kể họ thực hiện nghi lễ trung thành đến đâu, và cách sửa thuộc về mô hình quản trị chứ không phải các đội phân phối.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy sống với các giá trị và bỏ qua tranh luận về khung. Phát hành một lát hoạt động cho người dùng thật mỗi tuần, ngồi đủ gần những người sáng lập và khách hàng đầu tiên để phản hồi đến hằng ngày, và chào đón thay đổi hướng ngay khi bằng chứng nói canh bạc hiện tại sai. Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư, nên hãy bảo vệ sự xuất sắc kỹ thuật (tích hợp liên tục, kiểm thử tự động, phát triển trên thân chính) ngay cả dưới áp lực ra mắt, vì kỷ luật đó giữ cho bạn có thể xoay chuyển rẻ vào tuần sau.

**Doanh nghiệp nhỏ.** Không có huấn luyện viên agile và ngân sách eo hẹp, hãy coi Agile là một nhúm thói quen thay vì chương trình chuyển đổi bạn phải bố trí nhân sự: chu kỳ hằng tuần ngắn, một bảng hiển thị với giới hạn công việc đang làm, và một cải thiện cụ thể mỗi tuần mà bạn thực sự hoàn thành. Dựa vào Kanban, cần ít nghi thức và khớp công việc bị ngắt quãng, và áp dụng các thực hành nhúng trong công cụ bạn đã mua thay vì dựng quy trình nặng. Đánh giá nỗ lực theo việc bạn có phát hành phần mềm hữu ích cho khách hàng thường xuyên hơn không, không phải theo việc bạn bắt chước Scrum sát đến đâu.

**Doanh nghiệp lớn.** Vấn đề là phối hợp nhiều đội mà không đưa lại chỉ huy-kiểm soát. Ưu tiên thu nhỏ, tức là giảm phụ thuộc xuyên đội qua thiết kế đội căn chỉnh theo luồng và một nền tảng vững, trước khi áp dụng khung mở rộng nặng. Tài trợ và quản trị quanh kết quả (OKR) và nhịp thay vì phạm vi hằng năm cố định và điểm story, làm các thực hành kỹ thuật kiểu XP không thể thương lượng qua các đội, và quản lý phân phối như danh mục với chỉ số luồng và thước đo kết quả để các nhóm cải thiện dựa trên bằng chứng thay vì nghi lễ.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Cấu trúc hợp đồng mô-đun, dựa trên kết quả với các phần tăng trưởng ngắn hơn thay vì một siêu hợp đồng phạm vi cố định, vì mua sắm agile là nơi sự nhanh nhẹn khu vực công thành hay bại nhiều nhất. Xây kiểm toán, khả năng tiếp cận và bảo mật vào mỗi phần tăng trưởng qua tự động hóa để giám sát được thỏa mãn bởi hành động xây dựng, công bố tiến độ và bằng chứng về giá trị công cho các cơ quan giám sát, và đấu tranh để có tiếp cận thực sự đến công dân (gồm người dùng công nghệ hỗ trợ) mỗi vòng lặp, vì đó là ràng buộc thường bị thương lượng bỏ đi nhất.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp năm người bỏ qua tranh luận nghi thức và sống trực tiếp với các giá trị Agile. Nó phát hành một lát hoạt động cho người dùng thật mỗi tuần, ngồi đủ gần những người sáng lập và khách hàng đầu tiên để phản hồi đến hằng ngày, và chào đón thay đổi hướng vào tuần sau khi bằng chứng nói canh bạc hiện tại sai. Đội từ chối đánh đổi sự xuất sắc kỹ thuật lấy tốc độ, nên tích hợp liên tục, kiểm thử tự động và phát triển trên thân chính là không thể thương lượng ngay cả dưới áp lực ra mắt, và mỗi buổi nhìn lại thứ Sáu tạo ra một thay đổi cụ thể mà đội thực sự hoàn thành trước buổi tiếp theo. Nó không bao giờ theo dõi vận tốc như mục tiêu, thay vào đó đo xem công việc đã phát hành có dịch chuyển kích hoạt không và thời gian chờ có đang rút ngắn không.

**Doanh nghiệp lớn.** Chuyển đổi 60 đội của một công ty viễn thông ban đầu "làm Scrum" nhưng không thấy cải thiện. Các đội vẫn nhận phạm vi hằng năm cố định và báo cáo vận tốc. Một lần đặt lại tập trung lại vào nguyên tắc: OKR hằng quý thay thế mệnh lệnh tính năng, các đội được tái tổ chức để giảm phụ thuộc xuyên đội (thu nhỏ), và các thực hành XP (CI, TDD, phát triển trên thân chính) được làm không thể thương lượng. Thời gian chờ giảm, lỗi giảm, và, quan trọng nhất, doanh nghiệp bắt đầu đo kết quả thay vì điểm story, nối phân phối Agile với đường ống khám phá (chương 11.1).

**Chính phủ.** Một đội dịch vụ số xây lại ứng dụng trợ cấp hướng công dân bằng Agile bên trong vỏ quản trị lai: các phần tăng trưởng hai tuần giao phần mềm hoạt động, được kiểm thử với người dùng; khả năng tiếp cận và bảo mật được xây vào mọi phần tăng trưởng; và mua sắm mô-đun thay một hợp đồng giá cố định. Kiểm thử khả dụng thật với công dân (gồm người dùng công nghệ hỗ trợ) mỗi vòng lặp bắt những vấn đề mà quy trình thác nước cũ sẽ phát hành. Chương trình giao một dịch vụ dùng được sớm và cho thấy giá trị công đo được với các cơ quan giám sát. Đây là mô hình đằng sau các thành công khu vực công hiện đại, và là thuốc giải cho các thất bại đại bùng nổ trước đây.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của Agile đến từ **giảm rủi ro và hiện thực hóa giá trị nhanh hơn**. Bằng cách giao phần mềm hoạt động sớm và thường xuyên, các đội liên tục biến độ bất định thành bằng chứng, bắt các thất bại làm-sai-thứ và không-chạy-được khi còn rẻ, thay vì ở một ngày vận hành xa, đắt đỏ. Nghiên cứu đằng sau phân phối hiện đại (các phát hiện DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), trong chương 11.2) cho thấy các thực hành mà Agile thúc đẩy (lô nhỏ, phát hành thường xuyên, phản hồi nhanh, sự xuất sắc kỹ thuật) tương quan với phân phối tốt hơn *và* ổn định *và* hiệu suất tổ chức. Các phần tăng trưởng sớm cũng bắt đầu trả giá trị sớm hơn, cải thiện thời điểm và tổng quy mô của ROI so với một bản phát hành đại bùng nổ không trả gì đến cuối.

Về **[tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, Agile hạ chi phí thay đổi qua vòng đời hệ thống, miễn là kỷ luật kỹ thuật là thật. Rủi ro chi phối của nó là *agile giả*: nghi thức không có nguyên tắc hay tay nghề, thêm chi phí chung họp hành mà không giao lợi ích nào, và có thể tệ hơn một thác nước trung thực. Vì vậy luận chứng kinh doanh có điều kiện. ROI cao khi bạn áp dụng Agile như tư duy cộng kỹ thuật, và xấp xỉ bằng không (hoặc âm) khi bạn áp dụng nó như nghi lễ. Hãy lập luận với ban lãnh đạo bằng cách đóng khung Agile là giảm rủi ro liên tục và đo lường kết quả, không phải "đi nhanh hơn," và khăng khăng rằng khoản đầu tư gồm các thực hành kỹ thuật, không chỉ các cuộc họp mới.

## Phản mẫu và cạm bẫy

- **Agile giả / sùng bái hàng hóa:** nghi thức được thực hiện trong khi quyết định, tài trợ và tư duy vẫn là thác nước.
- **Vận tốc như năng suất:** biến ước tính năng lực thành mục tiêu, làm hỏng nó ([Định luật Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Scrum đen tối:** chạy nước rút không có sự xuất sắc kỹ thuật vào mã không bảo trì được, đầy lỗi.
- **Buổi nhìn lại không đổi gì:** sự phản tư không tạo hành động hoàn thành nào.
- **Phạm vi *và* ngày *và* chi phí cố định:** gọi đó là agile trong khi chất lượng lặng lẽ hấp thụ áp lực.
- **Khách hàng vắng mặt:** không có phản hồi người dùng thật, nên các vòng lặp tối ưu thứ sai.
- **Sùng bái khung:** "SAFe/Scrum bảo vậy" ghi đè nguyên tắc và phán đoán của đội.
- **Mở rộng trước khi thu nhỏ:** thêm khung phối hợp nặng thay vì giảm phụ thuộc.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu.** Phân phối thác nước hoặc tùy nghi; phát hành đại bùng nổ; công việc phản ứng và nặng kế hoạch, không có phản hồi lặp và không có nhận thức chung về vì sao Agile có thể giúp.
- **Mức 2, Phát triển.** Một vài đội áp dụng nghi thức Agile (họp đứng, sprint, buổi nhìn lại), nhưng thực hành không nhất quán trong tổ chức: tư duy và kỷ luật kỹ thuật tụt sau nghi lễ, vận tốc bị coi là đầu ra, và phạm vi vẫn cố định từ đầu.
- **Mức 3, Chuẩn hóa.** Giá trị và nguyên tắc thực sự dẫn dắt công việc toàn tổ chức, được lập tài liệu và kỳ vọng ở mọi đội: sự xuất sắc kỹ thuật kiểu XP (CI, kiểm thử tự động, tái cấu trúc, phát triển trên thân chính) là thực hành tiêu chuẩn, các đội tự tổ chức, khách hàng được tham gia mỗi vòng lặp, và buổi nhìn lại tạo thay đổi cụ thể, đã hoàn thành.
- **Mức 4, Quản lý.** Phân phối được đo và kiểm soát theo đường cơ sở: các đội theo dõi thời gian chờ, tần suất triển khai, tỷ lệ thay đổi thất bại và tỷ lệ lỗi lọt (các chỉ số luồng và ổn định kiểu DORA), cùng các thước đo kết quả gắn với kết quả then chốt, và so sánh mỗi cái với đường cơ sở đã biết. Hành động từ buổi nhìn lại được theo dõi đến khi hoàn thành, tín hiệu nhịp độ bền vững như làm thêm giờ và kiệt sức được giám sát, và vận tốc không bao giờ được dùng làm mục tiêu năng suất. Quyết định tiếp tục hay dừng dựa trên bằng chứng này thay vì ý kiến.
- **Mức 5, Điều phối.** Phân phối thích ứng được tích hợp với hoạch định kinh doanh và rủi ro trong toàn tổ chức: kết quả (OKR) thúc đẩy tài trợ và nhịp, thiết kế đội ít phụ thuộc (thu nhỏ) tối thiểu hóa chi phí chung phối hợp, và quản trị lai thỏa mãn giám sát mà không làm chậm phân phối. Cải thiện liên tục mang tính văn hóa thay vì nghi lễ, và tổ chức thường lệ thu hẹp phạm vi, lập lại đội và cân bằng lại danh mục khi bằng chứng và bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

1. Chấm điểm đội của bạn theo mười hai nguyên tắc Agile: bạn agile về nghi thức nhưng không về bản chất ở đâu?
2. Vận tốc trong đội của bạn được dùng như dự báo hay như mục tiêu, và điều đó đã làm gì với hành vi?
3. Thực hành kỹ thuật XP nào còn thiếu, và sự vắng mặt của chúng đang hiện ra thế nào như lỗi hay thay đổi chậm?
4. Trước khi áp dụng khung mở rộng, bạn có thể giảm phụ thuộc xuyên đội thay vào đó không?
5. Trong bối cảnh của bạn, cái gì cụ thể chặn tiếp cận người dùng thật mỗi vòng lặp, và làm sao bạn gỡ nó?
6. Thay đổi cụ thể cuối cùng mà một buổi nhìn lại thực sự tạo ra là gì?

## Những điểm cần ghi nhớ

- Agile là một **tư duy của giá trị và nguyên tắc**, không phải tập nghi thức; khung là điểm khởi đầu, không phải mục tiêu.
- Giao **phần mềm hoạt động thường xuyên**, chào đón thay đổi, và trao quyền cho **các đội tự tổ chức**.
- **Sự xuất sắc kỹ thuật (thực hành XP) là không thể thương lượng.** Sự nhanh nhẹn không có nó trở thành mục rữa nhanh.
- **Mở rộng cẩn thận; ưu tiên thu nhỏ.** Giảm phụ thuộc trước khi thêm khung phối hợp.
- Trong doanh nghiệp/chính phủ, kết hợp **phân phối thích ứng với quản trị lai và mua sắm agile**, và đấu tranh để có tiếp cận người dùng thật.
- ROI là **giảm rủi ro liên tục và giá trị sớm hơn**, nhưng chỉ khi Agile là thật, không phải nghi lễ. Xem các chương 1.4, 11.1, 11.2, 10.6 và 11.3.

## Tài liệu tham khảo và đọc thêm

- Kent Beck et al., *Manifesto for Agile Software Development* và mười hai nguyên tắc của nó (agilemanifesto.org, 2001).
- Ken Schwaber và Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* và *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton và Manuel Pais, *Team Topologies* (thiết kế đội và thu nhỏ).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (bằng chứng cho thực hành agile/DevOps).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
