# 1.6 Hồ sơ quyết định

## Tổng quan và động lực

**Hồ sơ quyết định** là một tài liệu ghi lại một quyết định quan trọng cùng với bối cảnh và hệ quả của nó. Hình thức nổi tiếng nhất là **[hồ sơ quyết định kiến trúc](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, một ghi chú ngắn, ưu tiên bất biến, ghi lại một lựa chọn có ý nghĩa kiến trúc, lý do nó được đưa ra và những gì theo sau. Toàn bộ tập hồ sơ của một dự án là **nhật ký quyết định (ADL)** của nó, và kỷ luật duy trì chúng là một phần của **quản lý tri thức kiến trúc (AKM)**. Chương này xây dựng trên các thực hành ra quyết định và quản trị của chương 1.5, tập trung vào cách bạn viết, lưu trữ và duy trì hồ sơ quyết định ở quy mô lớn.

Động lực rất đơn giản, và đau đớn nếu phải học bằng con đường khó. Với bất kỳ hệ thống tồn tại lâu dài nào, câu hỏi tốn kém nhất là "tại sao nó lại được xây như thế này?", được hỏi nhiều tháng hoặc nhiều năm sau bởi những người không có mặt trong phòng. Mã nguồn cho thấy hệ thống *làm gì*. Kiểm thử cho thấy nó *hoạt động*. Nhưng không cái nào nắm bắt *lý do* bạn chọn con đường này thay vì các phương án bạn đã cân nhắc và loại bỏ. Không có hồ sơ quyết định, lý do đó bốc hơi theo sự thay đổi nhân sự. Các đội tranh luận lại những câu hỏi đã giải quyết, đảo ngược những quyết định tốt vì lý do tồi, hoặc giữ lại những quyết định tồi vì sợ hãi. Một hồ sơ quyết định là một bức thư rẻ tiền gửi cho tương lai, lưu giữ lý do.

Với các đội lớn, đây vừa là công cụ điều phối vừa là trợ giúp trí nhớ. Các doanh nghiệp vận hành hàng chục đội đưa ra những lựa chọn chồng chéo. Một nhật ký quyết định chung biến lý do khó khăn mới có được của một đội thành tài sản tái sử dụng được, và ngăn các quyết định lệch hướng, không tương thích. Trong bối cảnh chính phủ và chịu quy định, hồ sơ quyết định gần như bắt buộc. Kiểm toán viên, cơ quan giám sát và nhà thầu kế nhiệm đều cần một lý do có thể truy vết nối các yêu cầu có ý nghĩa kiến trúc với những lựa chọn được đưa ra để đáp ứng chúng. Một nhật ký quyết định được giữ tốt thường là sự khác biệt giữa một hệ thống bạn có thể đảm bảo và kiểm toán và một hệ thống bạn không thể.

## Các nguyên tắc chính

- **Ghi lại *lý do*, không chỉ *nội dung*.** Bối cảnh và các phương án bị loại bỏ chính là điểm mấu chốt.
- **Một quyết định mỗi hồ sơ.** Giữ mỗi hồ sơ cụ thể và độc lập.
- **Nhỏ và nhẹ tốt hơn toàn diện nhưng không dùng.** Một hồ sơ một trang tồn tại tốt hơn một báo cáo không bao giờ được viết.
- **Đánh dấu thời gian cho mọi thứ.** Chi phí, ràng buộc và nhà cung cấp thay đổi; hãy ghi ngày cho từng khẳng định.
- **Ưu tiên một nhật ký sống, một cách thực dụng.** Bất biến là lý tưởng; trên thực tế, hãy bổ sung bằng các ghi chú có ngày.
- **Từ ngữ thay vì viết tắt.** "Quyết định" mời gọi nhiều đóng góp hơn "ADR".
- **Làm cho quyết định dễ tìm thấy và, khi có thể, kiểm thử được.** Hiển thị đúng hồ sơ vào đúng lúc; đảm bảo nó bằng các hàm thích nghi.

## Khuyến nghị

### Nắm bắt cấu trúc thiết yếu

Một hồ sơ quyết định tốt có một vài phần thiết yếu. Hãy điều chỉnh một mẫu đã biết thay vì phát minh ra mẫu mới:

- **Tiêu đề:** một cụm mệnh lệnh ngắn, ở thì hiện tại ("Dùng [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) cho sổ cái").
- **Trạng thái:** đề xuất, chấp nhận, bị thay thế, không còn dùng.
- **Bối cảnh:** tình huống, các lực tác động, ưu tiên kinh doanh và ràng buộc khiến quyết định này cần thiết; bao gồm yêu cầu có ý nghĩa kiến trúc mà nó giải quyết.
- **Quyết định:** lựa chọn được đưa ra, nêu một cách rõ ràng.
- **Hệ quả:** điều gì trở nên dễ hơn và điều gì trở nên khó hơn, các quyết định tiếp theo được kích hoạt, và rủi ro được chấp nhận.

Các mẫu phổ biến gồm mẫu của Michael Nygard (đơn giản và được áp dụng rộng rãi), mẫu của Tyree và Akerman (cầu kỳ hơn, với các phương án có trọng số), MADR (Markdown Any Decision Records, mạnh về các lựa chọn và ưu/nhược điểm của chúng) và Y-statement (một dạng có cấu trúc một câu). Hãy chuẩn hóa theo một mẫu cho mỗi tổ chức, để các hồ sơ có thể so sánh được. Xem chương 12.3 để có một mẫu sao chép dán.

### Viết hồ sơ cụ thể, có ngày và gần như bất biến

Giữ mỗi hồ sơ về đúng một quyết định. Đánh dấu thời gian cho từng khẳng định, đặc biệt là bất cứ thứ gì trôi dạt: giá cả, con số mở rộng, năng lực nhà cung cấp, điều khoản giấy phép. Về lý thuyết, một hồ sơ nên bất biến. Khi một quyết định thay đổi, bạn viết một hồ sơ *mới* thay thế hồ sơ cũ, giữ lại lịch sử. Trên thực tế, nhiều đội thấy cách tiếp cận **tài liệu sống** hiệu quả hơn: chèn thông tin mới vào hồ sơ hiện có với dấu thời gian và một ghi chú rằng nó đến sau quyết định. Cả hai đều chính đáng. Kiểu bất biến mạnh hơn cho dấu vết kiểm toán; kiểu sống tốt hơn cho tri thức hằng ngày của đội. Hãy chọn có chủ đích, và nhất quán.

### Lưu hồ sơ ở nơi công việc diễn ra

Đặt hồ sơ quyết định trong [hệ thống quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control) cùng với mã nguồn: một thư mục `decisions/` (hoặc `adr/`) gồm các tệp [Markdown](https://en.wikipedia.org/wiki/Markdown), mỗi quyết định một tệp, được đặt tên bằng một cụm động từ mệnh lệnh viết thường, ngăn cách bằng dấu gạch ngang (`choose-database.md`, `format-timestamps.md`). Điều này cho bạn lịch sử, rà soát và so sánh khác biệt miễn phí, và giữ lý do bên cạnh thứ nó giải thích. Nếu đội của bạn thích [wiki](https://en.wikipedia.org/wiki/Wiki), Google Docs hay công cụ theo dõi kiểu Jira, hãy dùng chúng. Công cụ quan trọng ít hơn nhiều so với thói quen. Một công cụ dòng lệnh nhẹ (như `adr-tools`) có thể dựng khung và lập chỉ mục các hồ sơ.

### Gọi chúng là "quyết định" và mở rộng ra ngoài kiến trúc

Một thấu hiểu thực tế từ nhiều đội: nhãn quan trọng. Một số lập trình viên và người quản lý dị ứng với từ "kiến trúc", và "hồ sơ" có thể gợi cảm giác giấy tờ làm sau. Đổi tên thư mục đơn giản thành "decisions" thường bật một công tắc. Các đội bắt đầu ghi lại các lựa chọn nhà cung cấp, quyết định lập kế hoạch, quyết định lịch trình, quyết định về dữ liệu và tuân thủ, tất cả bằng cùng một mẫu. Con người học nhanh hơn từ từ ngữ so với từ viết tắt, và họ đóng góp nhiều hơn khi khung nhìn là "giúp đồng đội tương lai của bạn suy nghĩ" thay vì "nộp biểu mẫu bắt buộc".

### Xác định vòng đời và quản trị

Để hồ sơ quyết định mở rộng được, hãy thống nhất quy trình xung quanh (đây là nơi quản trị của chương 1.5 gặp thực hành):

- **Ai có thể khởi tạo một hồ sơ, và điều gì biện minh cho nó:** thường là bất kỳ người đóng góp có hiểu biết nào; hãy khởi tạo hồ sơ khi các lập trình viên tương lai sẽ cần *lý do*, và bỏ qua với các lựa chọn rủi ro thấp, độc lập hoặc đã có tài liệu.
- **Vòng đời:** một luồng đơn giản như *Khởi xướng → Nghiên cứu → Đánh giá → Triển khai → Duy trì → Ngừng dùng*, với tiêu chí chấp nhận để chuyển giữa các giai đoạn (vấn đề được trình bày rõ, các phương án đã cân nhắc, các đánh đổi đã ghi lại, các bên liên quan đã được tham vấn).
- **Vai trò:** người đề xuất, người nghiên cứu, người rà soát, người phê duyệt, và một người bảo trì chịu trách nhiệm định kỳ xem xét hồ sơ (ít nhất hằng năm) và thúc đẩy việc ngừng dùng cuối cùng.
- **Quản trị:** cách đồng thuận, xung đột, leo thang và quyền phủ quyết vận hành, cùng mọi ràng buộc tuân thủ. Dựa vào các nguyên tắc như *thiên hướng hành động* và *[bất đồng nhưng cam kết](https://en.wikipedia.org/wiki/Disagree_and_commit)*, và dành quy trình nặng hơn cho các quyết định không thể đảo ngược, có bán kính ảnh hưởng lớn ("cửa một chiều").

### Làm cho quyết định kiểm thử được và dễ tìm thấy

Một hồ sơ quyết định *ghi lại* một quyết định; một **hàm thích nghi** *đảm bảo* nó: một kiểm tra tự động, chạy trong [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI), xác minh quyết định vẫn còn đúng ("mọi thay đổi trạng thái phải phát ra sự kiện", "không mô-đun nào được nhập chéo qua các ranh giới này", dùng các công cụ như ArchUnit). Điều này biến quản trị từ việc rà soát thủ công định kỳ thành thực thi liên tục, mở rộng được, đặc biệt có giá trị cho các mục tiêu quy định và kiểm toán (chương 3.1, 4.6, 8.5). Sau đó hãy hiển thị hồ sơ *đúng* vào thời điểm *đúng*. Công cụ gắn các quyết định liên quan vào một pull request, khi một lập trình viên chạm vào mã mà chúng chi phối, tốt hơn việc hy vọng mọi người đọc một thư mục tài liệu.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| **ADR nhẹ (Nygard/MADR)** | Viết nhanh, thực sự được viết ra; ít nghi thức | Ít chặt chẽ hơn cho các quyết định rủi ro cao, gây tranh cãi |
| **Mẫu nặng (Tyree-Akerman)** | Phương án có trọng số; mạnh cho các lựa chọn lớn, tốn kém | Chậm hơn; có thể ngăn cản việc ghi chép thường ngày |
| **Bất biến + thay thế** | Dấu vết kiểm toán sạch; giữ lại lịch sử | Nhiều hồ sơ hơn; người đọc phải lần theo chuỗi |
| **Tài liệu sống (bổ sung có ngày)** | Một nguồn sự thật hiện hành duy nhất; dễ duy trì | Câu chuyện kiểm toán yếu hơn; rủi ro chỉnh sửa âm thầm |
| **Markdown trong kho mã** | Có phiên bản, rà soát được, nằm cạnh mã | Kém thân thiện với người không phải lập trình viên |
| **Wiki / công cụ tài liệu** | Mọi vai trò đều tiếp cận được | Lịch sử và rà soát yếu hơn; trôi khỏi mã |

Căng thẳng cốt lõi là **độ chặt chẽ so với mức chấp nhận**. Hệ thống chặt chẽ nhất mà không ai dùng thì không ghi lại gì. Hệ thống nhẹ nhất mà mọi người dùng thì cộng dồn giá trị. Hãy mặc định chọn nhẹ, và dành quy trình nặng hơn cho vài quyết định tốn kém và khó đảo ngược.

## Câu hỏi để thảo luận với đội của bạn

1. **Làm thế nào để hồ sơ quyết định đúng đến được tay lập trình viên vào đúng lúc họ chạm vào mã mà nó chi phối, thay vì nằm trong một thư mục không ai mở?** Một nhật ký chỉ ghi mà không ai đọc ghi lại lý do không bao giờ thay đổi hành vi, đó là cách phổ biến nhất khiến hồ sơ quyết định thất bại: chúng tồn tại, và không ai đọc chúng khi cần. Cân nhắc đối lập là công sức, vì việc hiển thị hồ sơ tự động (gắn chúng vào một pull request khi có người sửa mã được chi phối) cần đầu tư công cụ mà một wiki hay thư mục tài liệu không cần. Hãy mang bằng chứng vào cuộc thảo luận: khi gần đây có người đảo ngược hoặc tranh luận lại một câu hỏi đã giải quyết, hồ sơ liên quan có tìm thấy được vào lúc đó, hay bị chôn vùi? Với một tổ chức lớn vận hành hàng chục đội, khả năng tìm thấy là thứ biến lý do khó khăn mới có được của một đội thành tài sản tái sử dụng thay vì một kho lưu trữ riêng. Hãy quyết định có lưu hồ sơ trong hệ thống quản lý phiên bản cạnh mã và nối chúng vào luồng pull request hay không, để hồ sơ xuất hiện ở nơi công việc diễn ra.

2. **Ai là người bảo trì chịu trách nhiệm cho mỗi hồ sơ, và điều gì ngăn nhật ký của bạn thoái hóa thành thông tin sai lệch đầy tự tin?** Chế độ thất bại nguy hiểm của một nhật ký quyết định không phải là thư mục trống, mà là thư mục đầy những hồ sơ có chi phí, năng lực nhà cung cấp và ràng buộc đã âm thầm lỗi thời từ nhiều năm trước. Mỗi hồ sơ cần một chủ sở hữu chịu trách nhiệm xem xét nó theo chu kỳ (ít nhất hằng năm) và thúc đẩy việc thay thế hoặc ngừng dùng, nếu không nhật ký mục nát thành truyền thuyết mà mọi người trích dẫn có chọn lọc và ít tin cậy. Hãy mang bằng chứng: bao nhiêu hồ sơ của bạn không có ngày, bao nhiêu hồ sơ mô tả một nhà cung cấp hay mức giá đã thay đổi, và lần xem xét cuối của từng hồ sơ là khi nào. Trong bối cảnh chính phủ và chịu quy định, điều này càng sắc nét, vì một chuỗi bất biến, bị thay thế chính là thứ kiểm toán viên và nhà thầu kế nhiệm dựa vào để có lý do truy vết được. Hãy quyết định vòng đời một cách tường minh, đánh dấu thời gian cho từng khẳng định trôi dạt, và chỉ định người bảo trì, để nhật ký vẫn là tài sản sống thay vì nghĩa địa.

3. **Bạn có nên chuẩn hóa theo một mẫu cho mọi đội không, và các quyết định rủi ro cao nhất của bạn thực sự cần bao nhiêu độ chặt chẽ?** Khả năng so sánh là lợi ích thực sự: khi mọi đội dùng cùng một hình dạng (Nygard, MADR hay tương tự), một đội mới có thể tìm ba hồ sơ trước đó và áp dụng lý do trong một buổi chiều thay vì một tháng tranh luận. Căng thẳng cốt lõi là độ chặt chẽ so với mức chấp nhận, vì mẫu nặng nhất mà không ai dùng thì không ghi lại gì, trong khi mẫu nhẹ nhất mà mọi người dùng thì cộng dồn giá trị. Hãy mang bằng chứng: các hồ sơ có thực sự được viết ra không, và riêng biệt, có quyết định lớn, gây tranh cãi, tốn kém nào bị phân tích thiếu vì dạng nhẹ bỏ qua việc cân nhắc các phương án không? Với các doanh nghiệp điều phối các lựa chọn chồng chéo giữa các đội, một mẫu chung cộng với một chỉ mục có thể tìm kiếm ngăn các quyết định lệch hướng, không tương thích. Hãy mặc định nhẹ cho trường hợp phổ biến, và thống nhất trước những quyết định cửa một chiều nào xứng đáng với dạng nặng hơn có phương án có trọng số.

4. **Điều gì thực sự biện minh cho việc khởi tạo một hồ sơ quyết định, và ai có thẩm quyền nói rằng một lựa chọn không cần một hồ sơ?** Đặt ngưỡng quá cao thì lý do đằng sau các lựa chọn hệ trọng bốc hơi; đặt quá thấp thì nhật ký đầy những chuyện vặt chôn vùi các hồ sơ mà mọi người thực sự cần. Với một tổ chức lớn, một ngưỡng không rõ ràng nghĩa là mỗi đội tự ứng biến ngưỡng riêng, nên độ bao phủ không đồng đều và không ai tin được rằng một hồ sơ vắng mặt báo hiệu một quyết định không quan trọng. Hãy mang bằng chứng vào cuộc thảo luận: một nhúm quyết định gần đây đã được ghi lại mà không cần thiết, và những quyết định đau đớn không được ghi lại mà sau đó khiến bạn tốn công khám phá lại. Hãy thống nhất một phép thử đơn giản, chẳng hạn ghi lại bất cứ khi nào lập trình viên tương lai sẽ cần *lý do* và bỏ qua các lựa chọn rủi ro thấp, độc lập hoặc đã có tài liệu. Trong bối cảnh chịu quy định và chính phủ, phép tính thay đổi, vì một yêu cầu kiểm toán có thể đòi hỏi một hồ sơ cho mọi yêu cầu có ý nghĩa kiến trúc dù đội có thấy đáng viết hay không, vì vậy hãy gọi tên trước những quyết định nào là không thể thương lượng.

5. **Các hồ sơ của bạn là lý do thực sự được nắm bắt vào thời điểm quyết định, hay giấy tờ được viết sau đó để thỏa mãn một yêu cầu bắt buộc?** Một hồ sơ được tạo ra sau sự việc để đóng một phiếu việc có xu hướng "tẩy trắng" phương án được chọn và âm thầm bỏ qua các phương án đã thực sự được cân nhắc, đúng là thông tin mà người đọc tương lai cần nhất. Áp lực đối lập là có thật: viết *lý do* trước hoặc trong khi quyết định có cảm giác chậm hơn việc phát hành, và việc thừa nhận bằng văn bản các con đường bị loại bỏ đòi hỏi sự an toàn tâm lý mà một số đội thiếu. Hãy mang một mẫu các hồ sơ gần đây ra bàn và trung thực hỏi liệu bối cảnh và các phương án bị loại bỏ đọc lên như sự cân nhắc thực sự hay như sự biện minh chắp vá sau. Với một đội lớn, các hồ sơ rỗng tuếch còn tệ hơn không có, vì chúng dạy mọi người rằng nhật ký không thể tin cậy. Trong kiểm toán doanh nghiệp và chính phủ, sự phân biệt này rất sắc: các cơ quan giám sát và nhà thầu kế nhiệm phụ thuộc vào một lý do phản ánh điều thực sự đã được cân nhắc, và một hồ sơ đọc như một màn trình diễn làm suy yếu sự đảm bảo mà nhật ký tồn tại để cung cấp.

6. **Những quyết định rủi ro cao nhất nào của bạn có thể được đảm bảo bằng một hàm thích nghi tự động, thay vì tin rằng việc rà soát thủ công định kỳ sẽ bắt được vi phạm?** Một hồ sơ quyết định ghi lại một lựa chọn, nhưng chỉ một kiểm tra tự động chạy trong tích hợp liên tục mới giữ cho lựa chọn đó không bị xói mòn âm thầm khi hàng chục lập trình viên chạm vào mã qua nhiều năm. Sự đánh đổi là đầu tư, vì viết và duy trì các hàm thích nghi (với các công cụ như ArchUnit) tốn thời gian kỹ thuật, và nhiều quyết định, đặc biệt là lựa chọn về quy trình hoặc nhà cung cấp, hoàn toàn không thể kiểm thử bằng máy. Hãy mang bằng chứng: những quyết định về ranh giới nào (phụ thuộc mô-đun, phát sự kiện, quy tắc truy cập dữ liệu) đã bị vi phạm âm thầm và chỉ bị bắt muộn trong rà soát hoặc trên môi trường thực. Với một doanh nghiệp vận hành nhiều đội, các hàm thích nghi biến quản trị từ nút thắt trung tâm thành thực thi liên tục mở rộng được mà không làm chậm mọi người. Trong bối cảnh chịu quy định và chính phủ, một kiểm tra tự động, luôn bật là bằng chứng kiểm toán mạnh hơn nhiều so với một chữ ký trên bản rà soát, vì nó chứng minh quyết định vẫn còn đúng hôm nay chứ không chỉ rằng ai đó đã từng phê duyệt nó.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy giữ nó ở mức thói quen và không gì khác: một thư mục `decisions/` trong kho chính, và một ghi chú hai phần (bối cảnh và lựa chọn) mỗi khi bạn đưa ra một quyết định mà bản thân tương lai sẽ thắc mắc. Bỏ hẳn vòng đời, vai trò và người phê duyệt, vì quy trình bạn không thể duy trì là quy trình bạn sẽ bỏ. Một hồ sơ duy nhất giúp nhân viên đầu tiên của bạn khỏi phải hỏi tại sao hệ thống được xây như vậy đã bù đắp cho toàn bộ thực hành.

**Doanh nghiệp nhỏ.** Không có kiến trúc sư riêng và ít thời gian, hãy đặt hồ sơ ở bất cứ nơi nào đội của bạn đã làm việc, dù là wiki, tài liệu chung hay kho mã, thay vì mua một công cụ chuyên dụng. Thói quen quan trọng hơn nhiều so với công cụ, vì vậy hãy hạ rào cản: đặt tên thư mục là `decisions` thay vì `adr`, và ghi lại các lựa chọn nhà cung cấp và xây-hay-mua cùng lúc với các lựa chọn kỹ thuật. Khi bạn dựa vào nhà thầu bên ngoài, một hồ sơ ngắn có ngày về lý do bạn chọn một nhà cung cấp hay nền tảng là bảo hiểm rẻ tiền chống lại việc bị khóa chặt vào một lựa chọn mà sau này không ai giải thích được.

**Doanh nghiệp lớn.** Công việc là điều phối giữa nhiều đội: chuẩn hóa theo một mẫu, công bố một chỉ mục liên đội có thể tìm kiếm, và hỗ trợ các quyết định ranh giới then chốt bằng các hàm thích nghi để vi phạm làm hỏng bản dựng thay vì chờ rà soát. Chỉ định một người bảo trì chịu trách nhiệm cho mỗi hồ sơ với chu kỳ xem xét, để nhật ký vẫn là tài sản sống thay vì thoái hóa thành truyền thuyết. Làm tốt, lý do của một đội về một lựa chọn khó trở thành tài sản mà đội kế tiếp áp dụng trong một buổi chiều thay vì tranh luận lại.

**Chính phủ.** Quy tắc mua sắm, tính minh bạch và trách nhiệm giải trình trước công chúng khiến hồ sơ quyết định gần như bắt buộc. Hãy yêu cầu một hồ sơ bất biến, bị thay thế cho mọi yêu cầu có ý nghĩa kiến trúc, mỗi hồ sơ liên kết lựa chọn với nhiệm vụ hay biện pháp kiểm soát tuân thủ mà nó thỏa mãn, để các cơ quan giám sát tìm thấy một lý do truy vết được thay vì một sự dựng lại. Vì các hệ thống công có vòng đời nhiều năm, nhiều nhà cung cấp, một nhật ký được giữ tốt thường là thứ cho phép nhà thầu kế nhiệm hiểu vì sao hệ thống có hình dạng như vậy và tiếp tục công việc mà không phải tranh luận lại những vấn đề đã giải quyết.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp năm người thêm một thư mục `decisions/` đơn giản vào kho chính, với một ghi chú hai phần (bối cảnh và lựa chọn) mỗi khi có ai đưa ra một quyết định mà bản thân tương lai sẽ thắc mắc. Không có vòng đời, không có vai trò, không có người phê duyệt: chỉ là thói quen viết *lý do* cạnh mã. Khi nhân viên đầu tiên của họ gia nhập sáu tháng sau, cô đọc toàn bộ thư mục trong một giờ và thôi hỏi "tại sao nó được xây như vậy?". Nhật ký nhẹ tốn vài phút cho mỗi mục và giúp họ khỏi cái thuế khám phá lại vốn cắn từ rất lâu trước khi một đội lớn lên.

**Doanh nghiệp lớn.** Một nhà bán lẻ với 30 đội kỹ thuật chuẩn hóa các hồ sơ định dạng MADR trong mỗi kho, cộng với một chỉ mục trung tâm có thể tìm kiếm. Khi một đội mới đối mặt với "[monorepo](https://en.wikipedia.org/wiki/Monorepo) hay multirepo", họ tìm thấy ba hồ sơ trước đó với bối cảnh và hệ quả, và áp dụng lý do trong một buổi chiều thay vì một tháng tranh luận. Các quyết định ranh giới then chốt (quyền sở hữu dịch vụ, quy tắc truy cập dữ liệu) được hỗ trợ bởi các hàm thích nghi ArchUnit, nên vi phạm làm hỏng bản dựng thay vì bị bắt trong rà soát. Đó là quản trị mở rộng được mà không có nút thắt trung tâm.

**Chính phủ.** Một cơ quan hiện đại hóa hệ thống trợ cấp yêu cầu một ADR cho mọi yêu cầu có ý nghĩa kiến trúc, mỗi ADR liên kết quyết định với nhiệm vụ hay biện pháp kiểm soát tuân thủ mà nó thỏa mãn (khả năng tiếp cận, nơi lưu trữ dữ liệu, khả năng kiểm toán). Các hồ sơ là bất biến và bị thay thế, tạo ra một nhật ký truy vết được đáp ứng việc rà soát giám sát. Quan trọng là, nó cũng cho phép nhà thầu kế nhiệm hiểu *vì sao* hệ thống có hình dạng như vậy, giữ tính liên tục qua vòng đời nhiều năm, nhiều nhà cung cấp điển hình của các chương trình công (chương 4.6, 10.4).

## Luận chứng kinh doanh: động lực, ROI và TCO

Một hồ sơ quyết định tốn vài phút để viết và thêm vài phút để rà soát. Lợi tức là chi phí *quyết định lại* được tránh và chi phí *đảo ngược sai* được tránh, cả hai đều lớn và lặp lại trên các hệ thống tồn tại lâu. Mỗi lần một đội tranh luận lại một câu hỏi đã giải quyết, hoặc đảo ngược một lựa chọn đúng đắn vì không ai nhớ ràng buộc đằng sau nó, họ trả bằng thời gian của kỹ sư cấp cao và thường là một sự cố. Một nhật ký quyết định chuyển cái thuế lặp lại đó thành một lần viết duy nhất.

Về **tổng chi phí sở hữu**, hồ sơ quyết định là một trong những tài liệu có đòn bẩy cao nhất bạn có thể giữ, vì chúng nhắm vào tài sản nhạy cảm nhất với sự thay đổi nhân sự: lý do. Hội nhập nhanh hơn (nhân viên mới đọc *lý do*, không chỉ mã). Hiện đại hóa an toàn hơn (chương 3.6: bạn có thể phân biệt các quyết định thiết yếu với những quyết định ngẫu nhiên). Kiểm toán rẻ hơn (bằng chứng đã tồn tại). Chi phí của việc *không* giữ chúng là vô hình trên mọi bảng điều khiển, và nó cộng dồn âm thầm sau mỗi lần có người ra đi. Để thuyết phục ban lãnh đạo, hãy chỉ ra một lần khám phá lại tốn kém gần đây, hoặc một quyết định bị đảo ngược gây ra sự cố, và lưu ý rằng cách khắc phục gần như không tốn gì để thiết lập.

## Phản mẫu và cạm bẫy

- **Ghi lại *nội dung* mà không có *lý do*:** bỏ qua bối cảnh và các phương án bị loại bỏ, tức toàn bộ điểm mấu chốt.
- **Giấy tờ làm sau:** hồ sơ được viết để thỏa mãn yêu cầu bắt buộc, không phải để suy nghĩ; chúng đọc lên rỗng tuếch và không ai tin.
- **Tài liệu khổng lồ nhiều quyết định:** một trang khổng lồ không ai điều hướng hay thay thế gọn gàng được.
- **Khẳng định không có ngày:** chi phí và ràng buộc từng đúng một lúc, được trình bày như vĩnh cửu.
- **Chỉnh sửa âm thầm:** thay đổi lịch sử của một quyết định mà không có ghi chú ngày, phá hủy dấu vết kiểm toán.
- **Nhật ký chỉ ghi:** hồ sơ được tạo ra và không bao giờ được hiển thị vào lúc chúng liên quan, nên chúng không ảnh hưởng đến hành vi.
- **Canh cổng bằng từ viết tắt:** khăng khăng dùng "ADR" và "kiến trúc" và do đó ngăn cản đóng góp.
- **Không có vòng đời:** hồ sơ không bao giờ được rà soát, thay thế hay ngừng dùng, thoái hóa thành thông tin sai lệch.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** Quyết định nằm trong đầu mọi người, các luồng trò chuyện và thông điệp commit; việc ghi lại là phản ứng và tùy nghi, và lý do thường xuyên mất đi cùng với sự thay đổi nhân sự.
- **Mức 2 (Phát triển):** Một số đội giữ hồ sơ, theo nhiều định dạng và mẫu khác nhau, bất cứ khi nào một cá nhân nhớ ra; thực hành không nhất quán giữa các đội, không có nhật ký chung, cách đặt tên hay quy trình.
- **Mức 3 (Chuẩn hóa):** Một mẫu duy nhất, lưu trữ trong kho mã, và một vòng đời cùng quản trị xác định (tiêu chí khởi tạo/bỏ qua, vai trò, chu kỳ xem xét) được lập thành tài liệu và áp dụng nhất quán toàn tổ chức; hồ sơ được rà soát và thay thế thay vì chỉnh sửa âm thầm.
- **Mức 4 (Quản lý):** Nhật ký quyết định được đo theo các đường cơ sở: độ bao phủ (tỷ lệ các quyết định có ý nghĩa kiến trúc mang một hồ sơ), độ mới (tỷ lệ hồ sơ được xem xét trong chu kỳ của chúng, cộng số lượng khẳng định không có ngày hoặc lỗi thời), và khả năng tìm thấy (mức độ thường xuyên một hồ sơ liên quan thực sự đến được tay lập trình viên đã thay đổi mã được chi phối). Những người bảo trì chịu trách nhiệm hành động dựa trên các chỉ số này, thay thế hồ sơ lỗi thời và lấp các khoảng trống bao phủ dựa trên bằng chứng thay vì giai thoại.
- **Mức 5 (Điều phối):** Một nhật ký quyết định liên đội có thể tìm kiếm được tích hợp vào công việc hằng ngày: các hồ sơ liên quan tự động hiển thị trên các thay đổi mà chúng chi phối, các quyết định then chốt được đảm bảo bằng hàm thích nghi trong tích hợp liên tục, và nhật ký nuôi dưỡng việc hội nhập, hiện đại hóa và kiểm toán như một tài sản sống. Tổ chức liên tục cải thiện chính thực hành, loại bỏ, thay thế và điều chỉnh lại phạm vi hồ sơ khi hệ thống và các ràng buộc của nó dịch chuyển, và cân bằng lại nơi đầu tư sự chặt chẽ khi danh mục quyết định lớn lên.

## Ý tưởng để thảo luận

1. Quyết định cuối cùng mà đội bạn đảo ngược hoặc tranh luận lại vì không ai nhớ lý do ban đầu là gì?
2. Đổi tên thư mục `adr/` của bạn thành `decisions/` có thay đổi ai đóng góp và điều gì được ghi lại không?
3. Những quyết định quan trọng nào của bạn có thể được đảm bảo bằng một hàm thích nghi tự động ngay hôm nay?
4. Bất biến-và-thay-thế hay tài liệu sống: cái nào phù hợp với nghĩa vụ kiểm toán và văn hóa của bạn, và vì sao?
5. Một nhân viên mới (hoặc một nhà thầu kế nhiệm) hiện đang khám phá *vì sao* hệ thống của bạn có hình dạng như vậy bằng cách nào?
6. Điều gì biện minh cho việc khởi tạo một hồ sơ quyết định trong đội của bạn, và điều gì biện minh cho việc *không* khởi tạo?

## Những điểm cần ghi nhớ

- Một hồ sơ quyết định ghi lại một quyết định quan trọng cùng **bối cảnh và hệ quả** của nó: *lý do*, không chỉ *nội dung*.
- Giữ hồ sơ **cụ thể, có dấu thời gian và nhẹ**; chuẩn hóa theo một mẫu (Nygard, MADR hoặc tương tự).
- Lưu chúng **trong hệ thống quản lý phiên bản cạnh mã**; cân nhắc gọi chúng là "decisions" để mở rộng đóng góp.
- Xác định **vòng đời và quản trị** (tiêu chí khởi tạo/bỏ qua, vai trò, chu kỳ xem xét); dành quy trình nặng cho các quyết định cửa một chiều.
- Làm cho quyết định **dễ tìm thấy** vào lúc thay đổi và, khi có thể, **kiểm thử được** qua các hàm thích nghi.
- ROI là chi phí khám phá lại và đảo ngược sai được tránh; lập luận TCO mạnh nhất ở nơi sự thay đổi nhân sự, hiện đại hóa và kiểm toán quan trọng nhất. Xem chương 1.5 (ra quyết định và quản trị) và chương 3.1 (nền tảng kiến trúc).

## Tài liệu tham khảo và đọc thêm

- Michael Nygard, "Documenting Architecture Decisions" (2011): ADR nhẹ nền tảng.
- MADR: dự án Markdown Any Decision Records (adr.github.io/madr).
- Jeff Tyree và Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" và "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: mẫu, ví dụ và hướng dẫn làm việc nhóm (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (các hàm thích nghi).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" và "Architecturally significant requirements."
