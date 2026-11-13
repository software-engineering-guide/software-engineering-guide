# 10.1 Quản lý danh mục và chương trình

## Tổng quan và động lực

Quản lý danh mục và [quản lý chương trình](https://en.wikipedia.org/wiki/Program_management) là kỷ luật quyết định một tổ chức kỹ thuật lớn nên xây gì, tài trợ công việc đó theo thời gian, sắp xếp thứ tự nó qua nhiều đội, và lái nó hướng tới kết quả chiến lược thay vì đầu ra rời rạc. Một đội đơn lẻ có thể xoay xở với căn chỉnh không chính thức và một tồn đọng chung. Một doanh nghiệp hay cơ quan chính phủ chạy hàng chục hay hàng trăm đội thì không. Tất cả công việc đó cạnh tranh cho cùng ngân sách khan hiếm, cùng kỹ năng chuyên gia, cùng nền tảng dùng chung, và cùng sự chú ý của lãnh đạo. Không có tầng danh mục có chủ đích, bạn kết thúc với tối ưu cục bộ: mọi đội bận, mọi lộ trình hợp lý, vậy mà tổng thể giao ít giá trị chiến lược hơn nhiều so với mức nó nên có.

Với các đội lớn, rủi ro cộng dồn. Công sức trùng lặp, ưu tiên lệch và phụ thuộc xuyên đội không được quản lý lặng lẽ đánh thuế mọi sáng kiến. Một tính năng mà một đội có thể phát hành trong một sprint chờ ba quý vì nó phụ thuộc một đội nền tảng chưa bao giờ nghe về nó. Trong chính phủ vấn đề còn sắc hơn. Phân bổ ngân sách hằng năm, tài trợ vốn nhiều năm, luật mua sắm và trách nhiệm giải trình công nghĩa là một chương trình đóng khung kém có thể khóa một cơ quan vào nhiều năm chi tiêu cam kết cho sai thứ. Vì vậy làm đúng [quản lý danh mục](https://en.wikipedia.org/wiki/Project_portfolio_management) không phải chi phí chung quan liêu. Đó là cách một tổ chức lớn biến chiến lược thành phần mềm được phát hành.

Chương này coi quản lý danh mục và chương trình là mối quan tâm lãnh đạo kỹ thuật, không chỉ là chức năng của [văn phòng quản lý dự án (PMO)](https://en.wikipedia.org/wiki/Project_management_office). Mục tiêu là nối chiến lược và mục tiêu với lộ trình, ưu tiên trung thực dưới ràng buộc thật, coi phụ thuộc và nhà cung cấp là rủi ro hạng nhất, và điều hướng các chu kỳ ngân sách và mua sắm, đặc biệt là nhịp tài trợ nhiều năm chi phối công việc khu vực công.

## Các nguyên tắc chính

- **Kết quả hơn đầu ra.** Tài trợ và đo thay đổi trong thế giới (áp dụng, chi phí, độ tin cậy, kết quả sứ mệnh), không phải khối lượng tính năng được phát hành.
- **Chiến lược phải đọc được.** Mọi đội nên truy được công việc của mình về một số ít mục tiêu đã công bố.
- **Ưu tiên là phép trừ.** Một danh mục nói có với mọi thứ không có chiến lược; giá trị nằm ở những gì bạn cố ý không làm.
- **Phụ thuộc là lịch trình thực.** Với các tổ chức lớn, chi phí phối hợp, không phải công sức viết mã, thường là ràng buộc chi phối.
- **Tài trợ đội bền vững, không phải dự án tạm thời.** Các đội ổn định, căn chỉnh theo sản phẩm vượt trội hơn các bể nhân sự được lắp lại cho mỗi dự án.
- **Khớp nhịp tài trợ với nhịp học.** Cam kết tiền theo từng bước cho phép bạn dừng, xoay hoặc tăng cược khi bằng chứng đến.
- **Nhà cung cấp là phần mở rộng của danh mục, không nằm ngoài nó.** Công việc của nhà thầu và [nhà tích hợp hệ thống](https://en.wikipedia.org/wiki/Systems_integrator) phải được quản trị với cùng khả năng nhìn thấy như công việc nội bộ.

## Khuyến nghị

### Căn chỉnh kỹ thuật với chiến lược và OKR

Hãy công bố một tập nhỏ mục tiêu cấp tổ chức (lý tưởng ba đến năm) và phân tầng nhẹ nhàng. Để các đội tự đặt kết quả then chốt phục vụ những mục tiêu chung đó thay vì giao cho họ nhiệm vụ. Giữ phân tầng nông: tối đa hai hoặc ba cấp, nếu không mô liên kết giữa chiến lược và công việc hằng ngày biến thành hư cấu. Xem xét mục tiêu theo nhịp cố định (thường hằng quý cho tiến độ, hằng năm cho chính mục tiêu) và công khai cho nghỉ hưu hoặc viết lại những cái không còn quan trọng. Chống lại việc biến [OKR](https://en.wikipedia.org/wiki/OKR) (mục tiêu và kết quả then chốt) thành vũ khí đánh giá hiệu suất. Ngay khi kết quả then chốt thúc đẩy thưởng cá nhân, các đội đặt mục tiêu thấp và bạn mất tín hiệu.

### Lập lộ trình có ý định và chân trời trung thực

Giữ lộ trình ở nhiều độ cao. Một lộ trình danh mục cho thấy chủ đề và kết quả qua các quý; lộ trình đội cho thấy sản phẩm bàn giao ngắn hạn. Đóng khung chúng quanh vấn đề và kết quả, với độ tin cậy giảm dần theo thời gian. Chân trời "Bây giờ / Tiếp theo / Sau này" truyền đạt độ bất định tốt hơn nhiều so với [biểu đồ Gantt](https://en.wikipedia.org/wiki/Gantt_chart) có ngày ngụ ý độ chính xác giả. Xem xét lại lộ trình theo nhịp đều đặn, và coi chúng là cam kết với một hướng đi, không phải hợp đồng cho những ngày cụ thể xa trong tương lai.

### Ưu tiên bằng khung tường minh và đánh đổi có tên

Chọn một phương pháp ưu tiên nhẹ, nhất quán và áp dụng đồng đều, để bạn so sánh được qua toàn danh mục. Các lựa chọn phổ biến gồm chấm điểm có trọng số (giá trị, chi phí, rủi ro, độ khớp chiến lược), [chi phí trì hoãn](https://en.wikipedia.org/wiki/Cost_of_delay) (giá trị bị bỏ lỡ cho mỗi đơn vị thời gian một sản phẩm bàn giao có giá trị phải chờ) và biến thể Công-việc-ngắn-nhất-có-trọng-số-trước (WSJF) của nó, và RICE (tầm với, tác động, độ tin cậy, công sức). Không công thức nào quyết định thay bạn. Giá trị thực của một khung là nó buộc các giả định ra ánh sáng, nơi lãnh đạo tranh luận về chúng. Luôn ghi lại đánh đổi bạn đang thực hiện (bạn hoãn cái gì, và vì sao) để bạn xem xét lại quyết định khi sự kiện đổi.

### Quản lý phụ thuộc qua nhiều đội

Hãy làm phụ thuộc hiển thị trước khi chúng cắn. Giữ một bản đồ hoặc sổ đăng ký phụ thuộc nêu, cho mỗi sáng kiến đáng kể, nó cần gì từ các đội khác và khi nào. Dùng một sự kiện hoạch định xuyên đội đều đặn (một buổi hoạch định phòng lớn hằng quý là phổ biến trong các khung mở rộng) để làm lộ và thương lượng phụ thuộc ngoài ánh sáng. Tốt hơn, hãy thiết kế chúng đi: đầu tư vào nền tảng tự phục vụ, API được lập tài liệu tốt, và hợp đồng nội bộ rõ ràng để các đội tiến hành mà không chờ nhau. Giao cho mọi phụ thuộc xuyên suốt một chủ sở hữu chịu trách nhiệm duy nhất. Phụ thuộc không chủ là nơi chương trình lặng lẽ trượt.

### Quản trị nhà cung cấp, nhà thầu và nhà tích hợp hệ thống

Hãy coi đối tác phân phối bên ngoài là một phần của danh mục. Yêu cầu cùng khả năng nhìn thấy vào tồn đọng, vận tốc, chất lượng và rủi ro của họ như bạn kỳ vọng nội bộ. Cấu trúc hợp đồng quanh kết quả và phần mềm hoạt động được giao theo từng bước, không phải khối lượng tài liệu hay số người ngồi ghế. Giữ đủ năng lực kỹ thuật nội bộ để đặc tả công việc, đánh giá chất lượng, và tiếp quản nếu nhà cung cấp thất bại. Đừng bao giờ thuê ngoài chức năng người mua thông thái. Đề phòng [khóa chặt](https://en.wikipedia.org/wiki/Vendor_lock-in) bằng cách sở hữu dữ liệu của bạn, đòi giao diện mở, và nhấn mạnh điều khoản thoát và chuyển tiếp từ ngày đầu.

### Điều hướng mua sắm, ngân sách và tài trợ nhiều năm

Hãy hiểu nhịp tài trợ bạn vận hành trong đó, và thiết kế chương trình khớp với nó. Trong chính phủ đặc biệt, phân bổ ngân sách có thể hằng năm trong khi hệ thống mất nhiều năm để xây, tạo áp lực chi tiêu trước cuối năm và mở rộng phạm vi cam kết ban đầu quá mức. Chống lại điều này theo ba cách: cấu trúc chương trình thành các bước độc lập có giá trị (hợp đồng mô-đun), tìm thẩm quyền cho tài trợ gia tăng và agile nơi quy tắc cho phép, và xây ước tính chi phí thực tách xây dựng, vận hành và duy trì. Hãy đưa [mua sắm](https://en.wikipedia.org/wiki/Procurement), tài chính và pháp lý vào sớm (họ định hình điều khả thi nhiều hơn hầu hết kỹ sư nhận ra) và dịch kế hoạch kỹ thuật sang các hạng mục ngân sách và ranh giới năm tài khóa mà các chức năng đó cần.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Kiểm soát danh mục tập trung | Căn chỉnh chiến lược mạnh; ít trùng lặp; đánh đổi tài trợ dễ hơn | Quyết định chậm hơn; có thể đè nén tự chủ đội và đổi mới cục bộ |
| Tự chủ đội phân tán | Đội nhanh, có động lực; chuyên môn cục bộ được tôn trọng | Trùng lặp; mạch lạc chiến lược yếu; rủi ro xuyên đội ẩn |
| Tài trợ theo dự án | Phạm vi và trách nhiệm rõ ràng cho mỗi sáng kiến | Luân chuyển đội; ngắn hạn; quyền sở hữu dài hạn yếu |
| Tài trợ theo sản phẩm/đội | Quyền sở hữu bền vững; chất lượng được duy trì | Khó phân bổ lại hơn; rủi ro tài trợ nỗ lực xác sống |
| Ưu tiên theo công thức | Minh bạch, so sánh được, bảo vệ được | Độ chính xác giả; đầu vào dễ thao túng; có thể chèn ép phán đoán |
| Chương trình cố định nhiều năm | Ổn định tài trợ; đầu tư chân trời dài | Khóa giả định ban đầu; tốn kém để sửa hướng |

Căng thẳng trung tâm là giữa mạch lạc và tốc độ. Quá nhiều kiểm soát trung tâm và tổ chức di chuyển chậm và làm nản người giỏi nhất. Quá ít và nó phân mảnh thành trăm tối ưu cục bộ. Các tổ chức trưởng thành chỉ tập trung hóa vài thứ phải mạch lạc (chiến lược, nền tảng dùng chung, tiêu chuẩn xuyên suốt, và đánh đổi tài trợ) và đẩy quyết định thực thi gần các đội nhất có thể. Căng thẳng giữa ổn định tài trợ và khả năng thích ứng giải quyết theo cùng cách: không phải chọn một, mà cam kết tiền gia tăng với các đội bền vững, để sự ổn định của con người cùng tồn tại với sự linh hoạt của hướng đi.

## Câu hỏi để thảo luận với đội của bạn

1. **Vài thứ nào phải giữ mạch lạc qua cả tổ chức, và quyết định nào nên đẩy xuống các đội?** Căng thẳng trung tâm trong một danh mục là mạch lạc so với tốc độ, và vạch sai ranh giới tốn kém cả hai chiều. Tập trung quá nhiều và quyết định bò chậm trong khi người giỏi nhất của bạn mất tự chủ; tập trung quá ít và bạn phân mảnh thành trăm tối ưu cục bộ với hệ thống trùng lặp và rủi ro xuyên đội ẩn. Các tổ chức trưởng thành chỉ giữ một danh sách ngắn ở trung tâm: chiến lược, nền tảng dùng chung, tiêu chuẩn xuyên suốt, và đánh đổi tài trợ. Hãy mang bằng chứng đến cuộc họp: đếm có bao nhiêu đội đang giải cùng một vấn đề độc lập, và bao nhiêu quyết định gần đây đình trệ chờ ký duyệt trung tâm. Nếu một trong hai con số cao, bạn đã vạch lằn ranh sai chỗ, nên hãy dịch chuyển quyền quyết định cụ thể thay vì tranh luận về tập trung hóa một cách trừu tượng.

2. **Bạn sẽ tài trợ kết quả thay vì đầu ra thế nào mà không mất trách nhiệm giải trình mà tài trợ theo dự án đã cho bạn?** Tài trợ các đội bền vững, căn chỉnh theo sản phẩm thắng tài trợ dự án tạm thời, vì đội ổn định duy trì chất lượng và sở hữu việc vận hành, không chỉ xây. Cái bẫy: tài trợ dự án cho lãnh đạo phạm vi sạch và đường trách nhiệm rõ ràng, và tài trợ đội liên tục có thể trôi vào việc trả tiền cho nỗ lực xác sống rất lâu sau khi tiền đề của chúng thất bại. Giải quyết bằng cách cam kết tiền gia tăng với các đội bền vững, xem xét mỗi chủ đề theo nhịp hằng quý, và phân bổ lại năng lực giữa các chủ đề thay vì giải tán đội. Hãy mang bằng chứng quan trọng: với mỗi đội được tài trợ, kết quả nào (áp dụng, chi phí, độ tin cậy, kết quả sứ mệnh) đã dịch chuyển quý trước, và bạn sẽ ngừng tài trợ cái gì nếu tiền đột nhiên khan hiếm. Nếu bạn không nêu được kết quả, bạn vẫn đang tài trợ đầu ra.

3. **Bạn phải giữ bao nhiêu năng lực kỹ thuật nội bộ để vẫn là người mua thông thái cho công việc của nhà cung cấp và nhà tích hợp hệ thống?** Khi bạn giao phân phối cho nhà thầu hay nhà tích hợp hệ thống, bạn giữ trách nhiệm giải trình, nên bạn cần đủ chiều sâu nội bộ để đặc tả công việc, đánh giá chất lượng, và tiếp quản nếu nhà cung cấp thất bại. Mất năng lực đó và bạn nhận hợp đồng kiểu xưởng thuê người: bạn mua giờ thay vì kết quả và không còn nói được bạn đang được phục vụ hay bị chiếm đoạt. Hãy cân nhắc chi phí giữ kỹ sư cấp cao không viết phần lớn mã với chi phí lớn hơn nhiều của khóa chặt nhà cung cấp và sứ mệnh bị giữ làm con tin. Hãy mang tín hiệu cụ thể: đội của bạn hôm nay có đọc được tồn đọng của nhà cung cấp, tái tạo một bản dựng, và sở hữu dữ liệu cùng giao diện không? Nhấn mạnh điều khoản thoát và chuyển tiếp từ ngày đầu, vì khoảnh khắc thương lượng đòn bẩy là trước khi bạn ký, không phải khi quan hệ xấu đi.

4. **Sáng kiến nào bạn cố ý từ chối tài trợ chu kỳ này, và mọi đội có truy được lời từ chối đó về chiến lược không?** Ưu tiên là phép trừ, và một danh mục lặng lẽ nói có với mọi thứ không có chiến lược; nó chỉ trải năng lực khan hiếm quá mỏng để hoàn thành bất cứ thứ gì tốt. Với một tổ chức lớn thiệt hại phân tán, vì không phê duyệt đơn lẻ nào trông liều lĩnh, vậy mà tổng bỏ đói vài canh bạc thực sự dịch chuyển một mục tiêu. Lực kéo đối lập là thật: mỗi sáng kiến bị từ chối có một người bảo trợ tin nó là thiết yếu, và một khung (chấm điểm có trọng số, chi phí trì hoãn, RICE) sẽ không quyết định thay bạn, nó chỉ buộc giả định ra ánh sáng nơi lãnh đạo tranh luận. Hãy mang danh sách đã xếp hạng, đánh đổi tường minh ghi lại cho mỗi lần hoãn, và số sáng kiến đang tiến hành so với số bạn có năng lực hoàn thành. Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm chi phí chính trị của mỗi lời từ chối và ai nắm thẩm quyền làm nó bám, vì một quyết định ưu tiên mà bất kỳ người bảo trợ nào cũng đảo ngược được bằng cách leo thang không phải quyết định, mà là gợi ý.

5. **Các phụ thuộc xuyên đội của bạn hôm nay ở đâu, và cái nào bạn đang thiết kế đi thay vì chỉ theo dõi?** Với một tổ chức lớn, chi phí phối hợp, không phải công sức viết mã, thường là ràng buộc chi phối, nên một tính năng một đội có thể phát hành trong một sprint có thể chờ ba quý ở một đội nền tảng chưa bao giờ nghe về nó. Theo dõi phụ thuộc trong sổ đăng ký làm chúng hiển thị, nhưng hiển thị không phải giải quyết; nước đi đòn bẩy cao hơn là thiết kế chúng ra ngoài qua nền tảng tự phục vụ, API có tài liệu và hợp đồng nội bộ rõ ràng để các đội thôi chờ nhau. Đánh đổi là đầu tư nền tảng tốn năng lực thật bây giờ so với độ trễ phụ thuộc cộng dồn lặng lẽ về sau, và luôn cám dỗ tài trợ tính năng hiển thị hơn nền tảng vô hình. Hãy mang bản đồ phụ thuộc cho các sáng kiến hàng đầu, số lần giao hàng trượt quý trước vì chờ đội khác, và liệu mỗi phụ thuộc xuyên suốt có một chủ sở hữu chịu trách nhiệm duy nhất. Trong chương trình doanh nghiệp và chính phủ nơi hàng chục đội và nhà tích hợp bên ngoài đan xen, hãy nêu nhịp hoạch định xuyên đội làm lộ chúng sớm, vì một phụ thuộc được phát hiện lúc tích hợp đã là thất bại lịch trình.

6. **Cách bạn cấu trúc tài trợ và hợp đồng có khớp với nhịp bạn thực sự học không?** Cam kết tiền theo từng cục nhiều năm lớn khóa các giả định sớm nhất, ít thông tin nhất của bạn, vậy mà nhiều chế độ tài trợ, đặc biệt phân bổ ngân sách chính phủ hằng năm, đẩy bạn mở rộng quá mức cam kết ban đầu và chi tiêu trước cuối năm. Cân nhắc đối lập là ổn định tài trợ cho phép các đội bền vững đầu tư cho chân trời dài, nên câu trả lời không phải hợp đồng nhỏ xíu mà là các bước độc lập có giá trị được tài trợ theo giai đoạn gắn với kết quả đã chứng minh. Hãy mang hình dạng cam kết hiện tại của bạn: bao nhiêu được cam kết trước khi phần mềm hoạt động đầu tiên được phát hành, ước tính chi phí có tách xây dựng, vận hành và duy trì không, và bạn còn dừng hay chuyển hướng được muộn đến đâu mà không lãng phí phân bổ. Với độc giả doanh nghiệp và chính phủ, mua sắm và pháp lý định hình điều khả thi nhiều hơn hầu hết kỹ sư kỳ vọng, nên hãy đưa họ vào sớm và hỏi tường minh hợp đồng mô-đun và thẩm quyền tài trợ gia tăng nào quy tắc đã cho phép trước khi bạn giả định cần một hợp đồng nguyên khối.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và ít đường băng, những người sáng lập là tầng danh mục, nên hãy giữ nó trên một bảng trắng: hai ba kết quả đã công bố, công việc ghim vào chúng, và mọi thứ khác bị cắt ngay. Tài trợ theo những canh bạc ngắn bạn có thể dừng trong vài tuần thay vì cam kết trước một quý, và bỏ qua khung, sổ đăng ký và sự kiện hoạch định tốn phối hợp hơn chúng tiết kiệm. Rủi ro danh mục thật duy nhất của bạn là nhúm phụ thuộc bên ngoài bạn không tránh được, nên hãy nêu một chủ sở hữu cho mỗi cái.

**Doanh nghiệp nhỏ.** Không có PMO hay quản lý chương trình riêng, quản lý danh mục là cuộc trò chuyện lặp lại giữa những người bạn đã có, không phải vai trò bạn tuyển. Dựa vào mua hơn xây cho bất cứ thứ gì ngoài cốt lõi, và đánh giá nhà cung cấp theo việc bạn rời họ dễ đến đâu, vì khóa chặt đau nhất khi bạn thiếu nhân sự để di chuyển. Giữ một danh sách trung thực duy nhất về những gì bạn đang tài trợ và những gì bạn cố ý không, và xem xét lại nó theo nhịp cố định, nhẹ nhàng để ngân sách khan hiếm theo vài kết quả trả hóa đơn.

**Doanh nghiệp lớn.** Qua hàng chục hay hàng trăm đội, công việc là mạch lạc không tắc nghẽn: chỉ tập trung hóa chiến lược, nền tảng dùng chung, tiêu chuẩn xuyên suốt và đánh đổi tài trợ, và đẩy thực thi cho các đội. Tài trợ liên tục các đội bền vững, căn chỉnh theo sản phẩm, chạy rà soát danh mục hằng quý phân bổ lại năng lực giữa các chủ đề, và quản lý phụ thuộc qua sổ đăng ký chung và hoạch định xuyên đội. Quản trị và kiểm toán là không thể thương lượng ở quy mô này, nên hãy làm công việc nhà cung cấp hiển thị như công việc nội bộ và ghi lại đánh đổi đằng sau mỗi quyết định ưu tiên.

**Chính phủ.** Luật mua sắm, phân bổ ngân sách hằng năm và trách nhiệm giải trình công định hình mọi nước đi. Ưu tiên hợp đồng mô-đun hơn giải thưởng nguyên khối nhiều năm, tài trợ theo giai đoạn gắn với kết quả đã chứng minh, và tách xây dựng, vận hành, duy trì trong ước tính để duy trì không bao giờ là bất ngờ. Giữ đội người mua thông thái nội bộ, sở hữu dữ liệu và giao diện của bạn, và viết điều khoản thoát và chuyển tiếp vào mọi hợp đồng, vì nghĩa vụ minh bạch nghĩa là một chương trình thất bại trở thành sự kiện công khai, được kiểm toán thay vì một khoản xóa sổ lặng lẽ.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp giai đoạn hạt giống mười hai người chạy hai nhóm nhỏ, và những người sáng lập đóng vai toàn bộ tầng danh mục. Mỗi thứ Hai họ ghim công việc vào chỉ hai kết quả đã công bố, kích hoạt và biên lợi nhuận gộp, và công khai cắt bất cứ thứ gì phục vụ cả hai không, nên một yêu cầu tích hợp bóng bẩy bị gác lại để sửa tỷ lệ rời bỏ khi làm quen. Họ tài trợ theo những canh bạc ngắn thay vì cam kết trước một quý, và nêu một chủ sở hữu cho phụ thuộc bên ngoài duy nhất họ không tránh được, nhà cung cấp thanh toán, để nó không bao giờ lặng lẽ làm trượt một lần ra mắt.

**Doanh nghiệp lớn.** Một ngân hàng toàn cầu chạy hơn một trăm đội phân phối qua bán lẻ, thanh toán và rủi ro. Nó tổ chức rà soát danh mục hằng quý nơi một nhóm điều hành nhỏ phân bổ tài trợ cho một chục chủ đề chiến lược, mỗi chủ đề do một cặp chịu trách nhiệm dẫn dắt: một lãnh đạo kinh doanh, một lãnh đạo kỹ thuật. Các đội được tài trợ liên tục, không theo dự án. Rà soát hằng quý phân bổ lại năng lực giữa các chủ đề thay vì giải tán đội. Một sổ đăng ký phụ thuộc chung và sự kiện hoạch định hằng quý làm lộ nhu cầu xuyên đội sớm. Kết quả: ít bất ngờ trượt hơn, và khả năng chuyển hướng đầu tư trong một quý khi điều kiện thị trường dịch chuyển.

**Chính phủ.** Một cơ quan thuế quốc gia hiện đại hóa hệ thống khai thuế hàng thập kỷ từ chối một hợp đồng nguyên khối nhiều năm duy nhất để chọn hợp đồng mô-đun: một chuỗi các bước nhỏ hơn, độc lập có giá trị, mỗi bước giao phần mềm hoạt động mà công dân dùng được. Nó yêu cầu tài trợ theo giai đoạn gắn với kết quả đã chứng minh, giảm rủi ro của một chương trình lớn thất bại. Cơ quan giữ đội kỹ thuật nội bộ làm người mua thông thái, sở hữu mọi dữ liệu và giao diện, và viết điều khoản thoát tường minh vào mọi hợp đồng nhà cung cấp, để không nhà tích hợp nào giữ sứ mệnh làm con tin.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của quản lý danh mục đến từ ba nguồn: lãng phí tránh được, phân phối giá trị nhanh hơn, và ít thất bại chương trình lớn hơn. Lãng phí tránh được là hệ thống trùng lặp bạn không bao giờ xây và sáng kiến giá trị thấp bạn không bao giờ tài trợ vì cái nhìn danh mục làm sự dư thừa hiển thị. Giá trị nhanh hơn đến từ thiết kế phụ thuộc đi để các đội thôi chờ nhau. Lợi tức lớn nhất, dù vậy, là giảm rủi ro. Các chương trình phần mềm lớn thất bại hoặc vượt chi nặng ở tỷ lệ cao, và một thất bại nhiều năm tránh được duy nhất có thể lấn át toàn bộ chi phí của chức năng danh mục.

Chi phí áp dụng là thật: vai trò danh mục và chương trình, nhịp hoạch định, công cụ, và thời gian phối hợp tất cả những thứ này tiêu tốn. Chi phí của việc *không* áp dụng lớn hơn nhưng phân tán, nên dễ bị phớt lờ: chi tiêu không phối hợp, [chi phí chìm](https://en.wikipedia.org/wiki/Sunk_cost) trong công việc lệch hướng, và lực cản cộng dồn của độ trễ phụ thuộc qua mọi sáng kiến. Khi lập luận với ban lãnh đạo, hãy đóng khung quản lý danh mục là cơ chế biến chiến lược của họ thành phân phối và bảo vệ họ khỏi những thất bại chương trình lớn kết thúc sự nghiệp. Hãy cho thấy [tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership) qua xây dựng, vận hành và duy trì nhiều năm, không chỉ bản xây ban đầu, vì lãnh đạo chỉ tài trợ bản xây thường xuyên bị bất ngờ bởi vận hành.

## Phản mẫu và cạm bẫy

- **Ưu tiên kiểu HiPPO.** Quyết định do ý kiến của người lương cao nhất thúc đẩy thay vì bằng chứng hay khung đã thống nhất.
- **Lộ trình như lời hứa về ngày.** Công bố ngày xa trong tương lai như cam kết, rồi quản lý theo lịch thay vì kết quả.
- **Mọi thứ đều ưu tiên một.** Một danh mục không có lời từ chối tường minh, nên năng lực khan hiếm bị trải quá mỏng để hoàn thành bất cứ thứ gì.
- **Mù phụ thuộc.** Phát hiện phụ thuộc xuyên đội lúc tích hợp thay vì lúc hoạch định.
- **Hợp đồng xưởng thuê người.** Mua giờ nhà thầu thay vì kết quả, và mất khả năng nội bộ đánh giá chất lượng.
- **Chi tiêu dùng-hoặc-mất.** Cuộc chạy đua ngân sách cuối năm tài trợ công việc giá trị thấp để tránh trả lại phân bổ.
- **OKR như tháp kiểm soát.** Biến mục tiêu thành nhiệm vụ được giao và chỉ số đánh giá, phá hủy tín hiệu trung thực mà chúng tồn tại để cung cấp.
- **Chương trình xác sống.** Nỗ lực nhiều năm tiếp tục được tài trợ do quán tính rất lâu sau khi tiền đề của chúng thất bại.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Ưu tiên được đặt tùy nghi và đổi theo ai đòi to nhất. Không có cái nhìn danh mục, nên phụ thuộc nổi lên như khủng hoảng lúc tích hợp và hệ thống trùng lặp không bị chú ý. Nhà cung cấp được quản lý theo khối lượng hợp đồng thay vì kết quả, và tài trợ theo các cuộc chạy đua cuối năm.

**Mức 2: Phát triển.** Một bản kiểm kê danh mục tồn tại và được xem xét định kỳ, nhưng thực hành khác nhau theo đội. Mục tiêu được công bố nhưng gắn yếu với công việc hằng ngày; một số đội giữ sổ đăng ký phụ thuộc và quản lý vài nhà cung cấp theo kết quả trong khi số khác không làm cả hai. Ngân sách khả đoán nhưng vẫn theo dự án, nên trách nhiệm giải trình rõ hơn mạch lạc chiến lược.

**Mức 3: Chuẩn hóa.** Chiến lược phân tầng sạch đến các đội qua cấu trúc OKR nông, và một khung ưu tiên được lập tài liệu và áp dụng qua toàn danh mục. Sự kiện hoạch định xuyên đội làm lộ phụ thuộc trước khi chúng cắn, các đội được tài trợ liên tục thay vì theo dự án, và hợp đồng mô-đun với tài trợ gia tăng là chuẩn mực toàn tổ chức thay vì thí nghiệm cục bộ.

**Mức 4: Quản lý.** Danh mục được đo theo đường cơ sở, không chỉ được lập tài liệu. Lãnh đạo theo dõi dịch chuyển kết quả theo từng chủ đề được tài trợ, chi phí trì hoãn cho các sáng kiến hàng đầu, tỷ lệ trượt phụ thuộc, phân phối của nhà cung cấp so với kết quả đã thống nhất, và phần chi tiêu cam kết gắn với kết quả đã chứng minh. Đánh đổi ưu tiên và tiêu chí khai tử được thực thi dựa trên bằng chứng này, và phương sai dự báo-so-với-thực về chi phí và lịch trình thúc đẩy mỗi quyết định tài trợ thay vì vận động.

**Mức 5: Điều phối.** Hoạch định danh mục, chương trình và rủi ro được tích hợp, và danh mục được cân bằng lại liên tục khi bằng chứng đến. Phụ thuộc phần lớn được thiết kế đi qua nền tảng và hợp đồng nội bộ rõ ràng, công việc nhà cung cấp và nội bộ chia sẻ một cái nhìn về giá trị và rủi ro, và nhịp tài trợ khớp nhịp học để tổ chức thường lệ dừng, chuyển hướng hay thu hẹp phạm vi công việc không ồn ào.

## Ý tưởng để thảo luận

- Phân tầng OKR có thể nông đến đâu trước khi nó thôi dẫn dắt công việc, và sâu đến đâu trước khi nó thành hư cấu?
- Khi nào một công thức ưu tiên cải thiện quyết định, và khi nào nó chỉ rửa câu trả lời định sẵn của ai đó?
- Đội nền tảng nên được tài trợ từ ngân sách trung tâm hay tính phí ngược cho các đội tiêu thụ, và điều đó đổi khuyến khích của họ thế nào?
- Trong bối cảnh chính phủ, bạn đẩy tài trợ gia tăng và mô-đun đến đâu trong luật phân bổ ngân sách hiện có trước khi cần thay đổi luật?
- Làm sao bạn giữ công việc nhà cung cấp hiển thị như công việc nội bộ mà không chìm trong chi phí chung báo cáo?
- Phản ứng đúng khi sản phẩm của một đội bền vững mất liên quan chiến lược là gì: bố trí lại con người, hay giải tán và xây lại?

## Những điểm cần ghi nhớ

- Quản lý danh mục biến chiến lược thành phần mềm được giao bằng cách quyết định tài trợ gì, theo thứ tự nào, qua nhiều đội.
- Ưu tiên bằng phép trừ và ghi lại đánh đổi; một danh mục nói có với mọi thứ không có chiến lược.
- Với các tổ chức lớn, phụ thuộc xuyên đội, không phải công sức viết mã, thường là ràng buộc chi phối; hãy làm chúng hiển thị và thiết kế chúng đi.
- Tài trợ các đội bền vững, căn chỉnh theo sản phẩm và cam kết tiền gia tăng để sự ổn định của con người cùng tồn tại với sự linh hoạt của hướng đi.
- Quản trị nhà cung cấp như một phần của danh mục, giữ chức năng người mua thông thái nội bộ, và đề phòng khóa chặt bằng sở hữu dữ liệu và điều khoản thoát.
- Trong chính phủ, cấu trúc chương trình thành các bước độc lập có giá trị để khớp chu kỳ tài trợ nhiều năm và giảm rủi ro thất bại chương trình lớn.

## Tài liệu tham khảo và đọc thêm

- Donald G. Reinertsen, *The Principles of Product Development Flow*
- Marty Cagan, *Inspired* và *Empowered*
- John Doerr, *Measure What Matters*
- Christina Wodtke, *Radical Focus: Achieving Your Most Important Goals with OKRs*
- Mik Kersten, *Project to Product*
- Jez Humble, Joanne Molesky và Barry O'Reilly, *Lean Enterprise*
- Project Management Institute, *The Standard for Portfolio Management*
- Axelos, *Managing Successful Programmes (MSP)*
- U.S. Digital Service, *Digital Services Playbook*
- UK Government Digital Service, *Service Manual* và *Technology Code of Practice*
- U.S. Government Accountability Office, *Agile Assessment Guide*
