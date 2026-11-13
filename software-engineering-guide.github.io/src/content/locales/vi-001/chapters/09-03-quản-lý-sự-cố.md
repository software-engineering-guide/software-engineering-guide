# 9.3 Quản lý sự cố

## Tổng quan và động lực

[Quản lý sự cố](https://en.wikipedia.org/wiki/Incident_management) là kỷ luật phát hiện, ứng phó, giải quyết và học từ các gián đoạn dịch vụ ngoài kế hoạch. Mọi hệ thống không tầm thường rốt cuộc đều thất bại, nên câu hỏi không phải sự cố có xảy ra không mà là bạn xử lý chúng tốt đến đâu. Quản lý sự cố tốt giữ tác động và thời lượng của gián đoạn nhỏ, phối hợp con người dưới áp lực, truyền thông trung thực với những người bị ảnh hưởng, và biến mỗi thất bại thành cải thiện bền vững. Nó kết hợp sẵn sàng vận hành, vai trò rõ ràng, truyền thông bình tĩnh và văn hóa học tập.

Với các đội lớn, quản lý sự cố là nơi độ phức tạp của tổ chức thực sự cắn. Một sự cố nghiêm trọng có thể liên quan nhiều dịch vụ, vài đội, lãnh đạo, khách hàng, cơ quan quản lý và công chúng, tất cả cùng lúc, dưới áp lực thời gian và với thông tin không đầy đủ. Không có cấu trúc chung, ứng phó rơi vào hỗn loạn: công sức trùng lặp, quyết định xung đột, im lặng với các bên liên quan, và anh hùng chủ nghĩa làm người kiệt sức. Một quy trình sự cố được xác định tốt cho mọi người một cách đã biết để cắm vào, một nguồn sự thật duy nhất, và thẩm quyền quyết định rõ ràng, để một nhóm lớn hành động mạch lạc trong khủng hoảng.

Rủi ro doanh nghiệp và chính phủ cao. Dịch vụ tài chính đối mặt hạn báo cáo quy định cho các lần ngừng hoạt động lớn. Sự cố y tế có thể ảnh hưởng an toàn bệnh nhân. Thất bại dịch vụ chính phủ có thể ngăn công dân tiếp cận trợ cấp, khai thuế, hay liên lạc dịch vụ khẩn cấp. Trách nhiệm giải trình công nghĩa là ngừng hoạt động hiển thị và bị soi xét. Thực hành trực ca bền vững cũng là nghĩa vụ chăm sóc: vòng trực thiếu người, quản lý kém gây [kiệt sức](https://en.wikipedia.org/wiki/Occupational_burnout) và nghỉ việc cuối cùng làm độ tin cậy tệ hơn. Quản lý sự cố do đó nằm nơi sự xuất sắc vận hành, phúc lợi con người và lòng tin thể chế gặp nhau.

*Xem thêm:* chương 9.1 (kỹ thuật độ tin cậy hệ thống), chương 9.2 (khả năng quan sát và giám sát), và chương 1.1 (văn hóa kỹ thuật: văn hóa sự cố không đổ lỗi, hướng học tập).

## Các nguyên tắc chính

- **Cấu trúc thắng anh hùng chủ nghĩa.** Một cấu trúc chỉ huy xác định cho phép nhiều người phối hợp; dựa vào vài anh hùng không mở rộng được và làm họ kiệt sức.
- **Vai trò, không phải chức danh.** Trong một sự cố, vai trò rõ ràng như chỉ huy sự cố và trưởng truyền thông quan trọng hơn cấp bậc tổ chức.
- **Truyền thông sớm và thường xuyên.** Cập nhật thường xuyên, trung thực cho các bên liên quan xây lòng tin ngay cả khi tin xấu; im lặng phá hủy nó.
- **Tách phối hợp khỏi điều tra.** Người chạy sự cố không nên đồng thời cắm đầu gỡ lỗi.
- **Trực ca phải bền vững.** Vòng trực, đền bù và giới hạn tải bảo vệ những người bảo vệ hệ thống.
- **Không đổ lỗi theo mặc định.** Con người hành động hợp lý theo những gì họ biết; đổ lỗi giấu nguyên nhân thật, mang tính hệ thống.
- **Học là mục đích.** Một sự cố không tạo cải thiện bền vững là đau khổ bị lãng phí.
- **Bảo tồn trí nhớ tổ chức.** [Rút kinh nghiệm](https://en.wikipedia.org/wiki/Postmortem_documentation) và hành động của chúng phải tìm được và tái sử dụng, không mất sau một tuần.

## Khuyến nghị

### Chạy vòng trực ca bền vững

Hãy thiết kế trực ca nhân đạo và hiệu quả. Giữ vòng trực đủ lớn để không ai trực quá thường, cung cấp bậc chính và phụ (leo thang), và đặt kỳ vọng rõ ràng về thời gian xác nhận và phản hồi. Đền bù trực ca công bằng, dù bằng lương hay nghỉ bù, và coi nó là công việc thật. Theo dõi tải cảnh báo mỗi ca, và coi vòng trực ồn, phá giấc ngủ là lỗi cần sửa bằng cách cắt các cuộc gọi giả, không phải bình thường. Theo mặt trời qua các múi giờ nơi có thể, để mọi người trực trong giờ thức. Bảo đảm mọi kỹ sư trực có [sổ tay vận hành](https://en.wikipedia.org/wiki/Runbook), quyền truy cập và thẩm quyền hành động, và các lần bàn giao ca chuyển ngữ cảnh có chủ đích.

### Thiết lập chỉ huy sự cố và mức nghiêm trọng

Hãy áp dụng một [hệ thống chỉ huy sự cố](https://en.wikipedia.org/wiki/Incident_Command_System) lấy cảm hứng từ ứng phó khẩn cấp. **Chỉ huy sự cố** sở hữu phối hợp và quyết định, không phải bản sửa kỹ thuật. Họ ủy thác, theo dõi hành động và giữ ứng phó chuyển động. Các vai trò hỗ trợ gồm một **trưởng vận hành hoặc kỹ thuật** chỉ đạo điều tra thực hành, một **trưởng truyền thông** xử lý cập nhật nội bộ và bên ngoài, và một **thư ký** ghi dòng thời gian. Xác định **mức nghiêm trọng** (ví dụ SEV1 cho ngừng hoạt động nghiêm trọng, lan rộng hay ảnh hưởng an toàn xuống SEV3 cho vấn đề nhỏ) với tiêu chí rõ ràng, vì mức nghiêm trọng quyết định ai được gọi, nhanh đến đâu, và bao nhiêu tổ chức huy động. Bất kỳ ai cũng nên có thể tuyên bố một sự cố, và bạn nên nghiêng về tuyên bố.

### Truyền thông trong sự cố, nội bộ và công khai

Hãy lập một kênh phối hợp duy nhất làm nguồn sự thật, và đăng cập nhật theo nhịp cố định, ngay cả khi cập nhật chỉ là "vẫn đang điều tra." Nội bộ, giữ lãnh đạo và các đội bị ảnh hưởng được thông tin qua trưởng truyền thông, để người ứng phó không bị gián đoạn. Bên ngoài, dùng trang trạng thái và, cho sự cố đáng kể, thông báo cho khách hàng hoặc công chúng trung thực về tác động và thời gian giải quyết dự kiến mà không hứa quá. Với dịch vụ chịu quy định và chính phủ, hãy biết trước nghĩa vụ và hạn báo cáo bắt buộc, và có sẵn mẫu. Mục tiêu là các bên liên quan luôn nghe nhiều hơn từ bạn so với từ tin đồn.

### Tổ chức rút kinh nghiệm không đổ lỗi và thúc đẩy hành động khắc phục

Sau bất kỳ sự cố đáng kể nào, hãy viết một **bản rút kinh nghiệm không đổ lỗi**: một dòng thời gian thực tế, tác động, các yếu tố góp phần, cái gì tốt, cái gì tệ, và nơi bạn gặp may. Không đổ lỗi nghĩa là nó tập trung vào hệ thống và quy trình đã cho phép thất bại thế nào, không phải ai để trừng phạt, vì [an toàn tâm lý](https://en.wikipedia.org/wiki/Psychological_safety) là thứ tạo ra lời kể trung thực và học tập thật. Mỗi bản rút kinh nghiệm cho ra **hành động khắc phục** với chủ sở hữu và hạn, ưu tiên theo tác động lên rủi ro tương lai. Theo dõi chúng đến khi hoàn tất trong tồn đọng kỹ thuật bình thường. Một bản rút kinh nghiệm có hành động không bao giờ xong chỉ là sân khấu.

### Học từ sự cố và xây trí nhớ tổ chức

Các bản rút kinh nghiệm riêng lẻ là cần thiết, nhưng một mình chúng chưa đủ. Hãy rà soát sự cố tổng hợp để tìm chủ đề lặp lại, điểm yếu hệ thống, và loại thất bại đáng một bản sửa cấu trúc. Làm bản rút kinh nghiệm tìm kiếm được và chia sẻ rộng, để bài học vượt ranh giới đội. Nuôi những gì bạn học vào sổ tay vận hành, đào tạo, rà soát kiến trúc và thanh sẵn sàng sản xuất. Cân nhắc rà soát độ tin cậy định kỳ và ngày diễn tập hay [bài tập hỗn loạn](https://en.wikipedia.org/wiki/Chaos_engineering) diễn tập ứng phó và làm lộ khoảng trống trước khi sự cố thật làm vậy. Coi kho sự cố của bạn là tài sản chiến lược nắm bắt tri thức vận hành khó giành.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Chỉ huy sự cố chính thức | Ứng phó phối hợp, mở rộng được | Chi phí chung cho sự cố nhỏ |
| Ngưỡng tuyên bố thấp | Bắt vấn đề sớm | Thỉnh thoảng báo động giả |
| Minh bạch trạng thái công khai | Xây lòng tin, giảm tin đồn | Phơi bày thất bại, mời gọi soi xét |
| Rút kinh nghiệm không đổ lỗi | Học trung thực, an toàn | Có thể cảm giác không có trách nhiệm giải trình nếu bị lạm dụng |
| Vòng trực ca lớn | Bền vững, ít kiệt sức hơn | Cần nhiều nhân sự được đào tạo hơn, loãng ngữ cảnh |

Đánh đổi trung tâm là giữa chi phí chung quy trình và lợi ích phối hợp. Một cấu trúc sự cố nặng vô giá trong SEV1 trải qua nhiều đội nhưng thừa cho một trục trặc nhỏ, nên hãy điều chỉnh quy trình theo mức nghiêm trọng. Minh bạch đánh đổi sự xấu hổ ngắn hạn lấy lòng tin dài hạn. Các tổ chức truyền thông cởi mở trong ngừng hoạt động thường giữ được nhiều thiện chí hơn những tổ chức im lặng. Không đổ lỗi đôi khi bị hiểu nhầm là thiếu trách nhiệm giải trình, nhưng trách nhiệm giải trình nó đòi hỏi là tập thể và hệ thống: đội sở hữu việc sửa các điều kiện đã cho phép thất bại, hiệu quả hơn nhiều so với đổ tội cho một cá nhân.

## Câu hỏi để thảo luận với đội của bạn

1. **Bao nhiêu người có thể chạy một sự cố với tư cách chỉ huy, và bạn có nêu tên được ba người không phải quản lý cấp cao?** Phụ thuộc một hai anh hùng để cứu mọi sự cố là mong manh và bảo đảm sự kiệt sức của họ, và vai trò chỉ huy sự cố là về phối hợp, không phải cấp bậc kỹ thuật, nên không nên mặc định lúc nào cũng là cùng những người cấp cao. Hãy mang danh sách vào cuộc thảo luận: liệt kê mọi người được đào tạo giữ vai trò chỉ huy và lần cuối họ thực sự chạy một cái là khi nào. Với một tổ chức lớn, một sự cố nghiêm trọng có thể trải qua nhiều đội lúc 3 giờ sáng, và bạn cần một chỉ huy được đào tạo sẵn sàng ở mọi múi giờ, không phải một chuyên gia đang ngủ. Hãy luân phiên vai trò và cho chỉ huy mới qua ngày diễn tập để kỹ năng lan ra. Câu trả lời cho bạn biết ứng phó của bạn mở rộng cùng tổ chức hay vỡ ngay khi người giỏi nhất của bạn không có mặt.

2. **Bạn có biết hạn báo cáo ngừng hoạt động bắt buộc của mình không, và mẫu cùng chủ sở hữu đã sẵn sàng trước SEV1 kế tiếp chưa?** Dịch vụ tài chính đối mặt hạn báo cáo quy định cho các lần ngừng hoạt động lớn, sự cố y tế chạm an toàn bệnh nhân, và thất bại chính phủ chặn công dân khỏi trợ cấp hay dịch vụ khẩn cấp, nên một cửa sổ báo cáo bị lỡ biến sự cố kỹ thuật thành vấn đề pháp lý. Giữa một SEV1 là lúc tệ nhất để phát hiện bạn có bốn giờ để thông báo cho cơ quan quản lý và không có mẫu. Hãy mang các nghĩa vụ thật: cơ quan quản lý nào, ngưỡng nào kích hoạt báo cáo, hạn là bao giờ, và ai được ủy quyền nộp. Giao việc này cho vai trò trưởng truyền thông từ trước để người ứng phó không bao giờ bị kéo khỏi bản sửa để soạn hồ sơ. Câu trả lời nên tạo ra mẫu sẵn sàng, một chủ sở hữu có tên, và một mức nghiêm trọng tự động kích hoạt đồng hồ báo cáo.

3. **Lần cuối bạn diễn tập một sự cố lớn bằng ngày diễn tập là khi nào, và nó làm lộ khoảng trống nào?** Ngày diễn tập và bài tập hỗn loạn diễn tập ứng phó và làm lộ khoảng trống trước khi sự cố thật làm vậy, và trạng thái trưởng thành trong chương này là ứng phó trơn tru, được diễn tập kỹ, không phải ứng phó bịa dưới áp lực. Một kế hoạch chưa bao giờ được thực hành giấu các giả định hỏng: sổ tay vận hành cũ, truy cập thiếu, đường leo thang đi vào ngõ cụt, trang trạng thái không ai cập nhật được. Hãy mang phát hiện của bài tập gần nhất, hoặc nếu không có, coi đó là phát hiện. Với hệ thống doanh nghiệp và chính phủ nơi ngừng hoạt động bị soi xét công khai, diễn tập là cách bạn cho thấy năng lực thay vì ứng biến trước mặt công dân và cơ quan quản lý. Câu trả lời nên đặt nhịp cho ngày diễn tập và nuôi mọi khoảng trống bị lộ vào sổ tay vận hành, rà soát truy cập và thanh sẵn sàng sản xuất.

4. **Tải cảnh báo thực trên vòng trực bận nhất của bạn là bao nhiêu, và bạn có sẵn lòng tự mang chiếc máy nhắn đó không?** Một vòng trực ồn, phá giấc ngủ là lỗi, không phải huy chương, và mệt mỏi cảnh báo là nơi người ứng phó bỏ lỡ hoặc xác nhận chậm tình huống khẩn cấp thật, nên câu hỏi nhân đạo và câu hỏi độ tin cậy là cùng một câu hỏi. Áp lực đối lập là cắt cuộc gọi cảm giác như hạ cảnh giác, trong khi thực tế một dòng cuộc gọi giả hạ nó nhiều hơn hẳn. Hãy mang các con số: số cuộc gọi mỗi ca, bao nhiêu cái xảy ra ngoài giờ làm, bao nhiêu cái hành động được, và thời gian xác nhận cho những cái quan trọng. Đặt trần tường minh về cuộc gọi mỗi ca và coi bất kỳ vòng trực nào vượt nó là công việc cần sửa bằng cách điều chỉnh hay xóa cảnh báo. Với một tổ chức lớn hay chính phủ, trực ca bền vững là nghĩa vụ chăm sóc và đòn bẩy giữ chân, vì những kỹ sư có kinh nghiệm mang tri thức hệ thống không thay thế được chính là những người một vòng trực tàn nhẫn đẩy đi, và xây lại tri thức đó tốn hơn nhiều so với bố trí nhân sự vòng trực nhân đạo.

5. **Phần nào trong các hành động khắc phục quý trước thực sự đã xong, và ai chịu trách nhiệm khi chúng chưa?** Một bản rút kinh nghiệm có hành động không bao giờ hoàn tất tạo ra cùng sự cố lần nữa, nên kỷ luật phân biệt học thật với sân khấu là liệu bản sửa có được phát hành không, không phải bản viết có đọc hay không. Căng thẳng là hành động khắc phục cạnh tranh với công việc tính năng trong cùng tồn đọng, và không có chủ sở hữu có tên, hạn và nhịp rà soát chúng lặng lẽ thua mọi cuộc chiến ưu tiên. Hãy mang sổ cái: mọi hành động từ các bản rút kinh nghiệm gần đây, chủ sở hữu, hạn và trạng thái của nó, cộng số sự cố tái diễn vì một bản sửa đình trệ. Theo dõi chúng trong tồn đọng kỹ thuật bình thường và rà soát mức hoàn thành như một chỉ số so với đường cơ sở, để hành động già đi hay bị bỏ nổi lên thay vì biến mất. Trong bối cảnh doanh nghiệp và chính phủ, một hành động khắc phục chưa xong sau một lần ngừng hoạt động đã báo cáo là kiểu phát hiện mà kiểm toán viên hay cơ quan giám sát bám lấy, nên hoàn thành vừa là biện pháp bảo vệ kỹ thuật vừa là vấn đề trách nhiệm giải trình chứng minh được.

6. **Mọi người có cảm thấy an toàn khi tuyên bố sự cố sớm và nói trung thực trong buổi rút kinh nghiệm, hay nỗi sợ bị đổ lỗi làm họ chậm lại?** Văn hóa không đổ lỗi là thứ tạo ra lời kể trung thực làm lộ nguyên nhân hệ thống, và ngưỡng tuyên bố thấp là thứ bắt vấn đề khi chúng còn nhỏ, nên cả hai phụ thuộc vào việc mọi người không sợ giơ tay sẽ bị dùng chống lại họ. Mối lo đối lập là không đổ lỗi đọc như thiếu trách nhiệm giải trình, nhưng trách nhiệm giải trình nó đòi hỏi là tập thể: đội sở hữu việc sửa các điều kiện đã cho phép thất bại thay vì đổ tội cho ai chạm vào sau cùng. Hãy mang bằng chứng bạn quan sát được thực sự: sự cố được tuyên bố nhanh đến đâu so với vấn đề âm ỉ bao lâu trước đó, kỹ sư mới có bao giờ tuyên bố không, và các bản rút kinh nghiệm nêu điều kiện góp phần hay lặng lẽ nêu một người. Với một tổ chức lớn hay công, an toàn tâm lý mong manh và dễ bị phá bởi một buổi rà soát dẫn dắt bởi đổ lỗi hay một lãnh đạo trừng phạt người đưa tin, nên hãy để ý tín hiệu rằng mọi người đang đi vòng quy trình, và coi việc tuyên bố sớm trung thực là hành vi cần bảo vệ hơn là rủi ro cần quản lý.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không có đường băng dư, hãy giữ quy trình trong một trang: ai nhận ra thì tuyên bố, một người phối hợp, một người điều tra, một người nói với khách hàng, và không ai khác chạm vào môi trường sản xuất. Bỏ qua các bậc nghiêm trọng chính thức và vai trò chuyên trách bạn không bố trí nhân sự nổi, nhưng hãy viết bản ghi một trang không đổ lỗi, vì ở kích thước của bạn một thất bại lặp lại duy nhất có thể nhấn chìm bạn. Dựa vào trang trạng thái lưu trữ và công cụ gọi thay vì xây công cụ phối hợp.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia độ tin cậy riêng và ngân sách eo hẹp, vì vậy hãy mua công cụ sự cố nhúng trong dịch vụ giám sát và gọi bạn đã trả tiền thay vì xây của riêng bạn. Coi trực ca là nhiệm vụ chung với giới hạn rõ ràng, nhân đạo để nó không làm kiệt sức một hai người hiểu hệ thống. Viết bản rút kinh nghiệm ngắn và thực sự hoàn tất các bản sửa, vì với đội nhỏ một lần ngừng hoạt động lặp lại tốn của bạn khách hàng khó thay thế.

**Doanh nghiệp lớn.** Thách thức là phối hợp nhiều đội dưới áp lực, vì vậy hãy chuẩn hóa một hệ thống chỉ huy sự cố, tiêu chí nghiêm trọng chung, và một nguồn sự thật duy nhất để một SEV1 trải qua nhiều dịch vụ không bị phân mảnh. Đầu tư vào chỉ huy được đào tạo ở mọi múi giờ, tổng hợp bản rút kinh nghiệm thành trí nhớ tổ chức tìm kiếm được, và quản trị hành động khắc phục đến khi hoàn tất với chủ sở hữu và dấu vết kiểm toán. Quản lý tải trực ca như chỉ số toàn đội để không vòng trực nào lặng lẽ trở nên vô nhân đạo.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình ứng phó. Hãy biết trước hạn và ngưỡng báo cáo ngừng hoạt động bắt buộc, giữ mẫu nộp hồ sơ và một chủ sở hữu được ủy quyền có tên sẵn sàng, và công bố cập nhật trạng thái trung thực cùng kịch bản tổng đài để công dân không bao giờ bị bỏ đoán. Chia sẻ bản rút kinh nghiệm khắp cơ quan, nuôi chúng vào hoạch định khả năng phục hồi cho các giai đoạn đỉnh, và coi hồ sơ các sự cố quá khứ là bằng chứng bạn cho cơ quan giám sát thấy thất bại đã tạo ra bản sửa bền vững.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người thức dậy thấy API trả lỗi và mọi người cùng dồn vào cùng một chuỗi trò chuyện. Bị cháy bởi hỗn loạn, họ viết một trang kiến thức sự cố cơ bản: ai nhận ra tuyên bố sự cố và thành người phối hợp, một người điều tra, một người đăng cập nhật đơn giản cho khách hàng, và không ai khác chạm vào môi trường sản xuất. Lần ngừng hoạt động kế tiếp chạy bình tĩnh và giải quyết trong bốn mươi phút. Một bản ghi ngắn không đổ lỗi tìm thấy một di chuyển chạy mà không có bước sao lưu, và họ thêm kiểm tra đó vào tập lệnh triển khai ngay trong ngày.

**Doanh nghiệp lớn.** Một nhà cung cấp phần mềm dịch vụ lớn gặp ngừng hoạt động một phần trong giờ làm việc. Kỹ sư trực tuyên bố một SEV1, và một chỉ huy sự cố tiếp quản phối hợp trong khi trưởng kỹ thuật điều tra và trưởng truyền thông đăng cập nhật lên trang trạng thái công khai mỗi hai mươi phút. Ban điều hành theo dõi một kênh lãnh đạo thay vì gián đoạn người ứng phó. Dịch vụ trở lại trong chín mươi phút. Một bản rút kinh nghiệm không đổ lỗi tuần sau tìm thấy biện pháp bảo vệ bị thiếu trong đường ống triển khai và tạo ba hành động khắc phục có chủ sở hữu. Rà soát tổng hợp sau đó cho thấy đây là sự cố liên quan triển khai thứ ba trong quý, kích hoạt khoản đầu tư cấu trúc vào tung ra an toàn hơn.

**Chính phủ.** Hệ thống chi trả của một cơ quan trợ cấp thất bại vào ngày khối lượng cao, chặn công dân nhận hỗ trợ. Quy trình sự cố của cơ quan huy động một chỉ huy, người ứng phó kỹ thuật, và một trưởng truyền thông phối hợp thông điệp công khai và đáp ứng yêu cầu quy định báo cáo ngừng hoạt động lớn trong một cửa sổ cố định. Một trang trạng thái và kịch bản tổng đài giữ công dân và nhân viên được thông tin. Bản rút kinh nghiệm không đổ lỗi, được chia sẻ khắp cơ quan, nuôi bài học vào sổ tay vận hành và rà soát sẵn sàng sản xuất, và kho sự cố quá khứ cung cấp thông tin cho hoạch định năng lực và khả năng phục hồi của năm sau cho các giai đoạn đỉnh.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của quản lý sự cố trưởng thành hiện ra là tác động mỗi sự cố giảm và ít sự cố lặp lại hơn. Ứng phó nhanh hơn, phối hợp tốt hơn rút ngắn ngừng hoạt động, trực tiếp tiết kiệm doanh thu, tiền phạt và chi phí khắc phục. Rút kinh nghiệm và hành động khắc phục có kỷ luật đều đặn loại bỏ cả loại thất bại, nên tỷ lệ sự cố giảm theo thời gian. Trực ca bền vững giảm chi phí khổng lồ, thường ẩn của kiệt sức và nghỉ việc trong các kỹ sư có kinh nghiệm, những người đắt để thay thế và mang tri thức hệ thống không thể thay.

Chi phí áp dụng khiêm tốn so với lợi ích: đào tạo chỉ huy sự cố, công cụ phối hợp và truyền thông trạng thái, thời gian dành cho rút kinh nghiệm, và nhân sự cần cho vòng trực nhân đạo. Chi phí của việc không áp dụng nghiêm trọng và lặp lại: ứng phó hỗn loạn kéo dài ngừng hoạt động, im lặng xói mòn lòng tin khách hàng và công chúng, phạt quy định cho báo cáo bị lỡ, sự cố lặp lại từ hành động không ai hoàn tất, và đội trực nản chí. Để lập luận với ban lãnh đạo, hãy định lượng các sự cố gần đây theo thời lượng và tác động, cho thấy phối hợp và hành động khắc phục đã hoàn tất sẽ rút ngắn hay ngăn tái diễn chúng thế nào, và đóng khung trực ca bền vững là giữ chân và quản lý rủi ro, không phải nuông chiều.

## Phản mẫu và cạm bẫy

- **Văn hóa anh hùng.** Phụ thuộc một hai người để cứu mọi sự cố là mong manh và bảo đảm sự kiệt sức của họ.
- **Không có chỉ huy rõ ràng.** Không ai sở hữu phối hợp, người ứng phó trùng lặp công việc, xung đột, và mất dòng thời gian.
- **Im lặng.** Giữ lại cập nhật trong ngừng hoạt động nuôi tin đồn, hoảng loạn và bất tín nhiệm lâu dài.
- **Trò đổ lỗi.** Trừng phạt cá nhân đẩy sự trung thực xuống ngầm và giấu nguyên nhân hệ thống bạn cần sửa.
- **Sân khấu rút kinh nghiệm.** Viết bản rút kinh nghiệm có hành động khắc phục không bao giờ hoàn tất tạo ra cùng sự cố lần nữa.
- **Trực ca mệt mỏi cảnh báo.** Vòng trực ồn làm kiệt sức người ứng phó nên họ bỏ lỡ hoặc xác nhận chậm tình huống khẩn cấp thật.
- **Nhầm lẫn mức nghiêm trọng.** Mức nghiêm trọng không xác định hoặc áp dụng không nhất quán gây ứng phó thiếu với sự cố nghiêm trọng và ứng phó thừa với cái tầm thường.

## Mô hình trưởng thành

**Mức 1, Khởi đầu.** Sự cố được xử lý tùy nghi bởi ai nhận ra, và ứng phó phản ứng và ứng biến. Không có vai trò, mức nghiêm trọng hay rút kinh nghiệm xác định. Trực ca, nếu có, không chính thức và căng thẳng, và cùng thất bại tái diễn vì không có gì bền vững được học.

**Mức 2, Phát triển.** Vòng trực ca cơ bản và định nghĩa nghiêm trọng tồn tại, và một số sự cố có rút kinh nghiệm, nhưng thực hành không nhất quán qua các đội. Vai trò không rõ trong ứng phó, một đội có thể chạy sự cố có kỷ luật trong khi đội kế tiếp rơi vào hỗn loạn, và hành động khắc phục được theo dõi tùy tiện nếu có.

**Mức 3, Chuẩn hóa.** Một hệ thống chỉ huy sự cố chính thức với vai trò rõ ràng và tiêu chí nghiêm trọng được lập tài liệu và dùng nhất quán toàn tổ chức. Rút kinh nghiệm không đổ lỗi là tiêu chuẩn cho sự cố đáng kể, hành động khắc phục được ghi với chủ sở hữu và hạn, trực ca được đền bù, và một kênh phối hợp duy nhất cùng thực hành trang trạng thái được thực thi toàn tổ chức thay vì để mỗi đội tự lo.

**Mức 4, Quản lý.** Chương trình sự cố được đo và kiểm soát theo đường cơ sở. Bạn theo dõi thời gian phát hiện, thời gian xác nhận, thời gian giải quyết, cuộc gọi mỗi ca, tỷ lệ hoàn thành hành động khắc phục, và tỷ lệ sự cố lặp lại, và bạn rà soát các chỉ số này theo nhịp để bắt hồi quy. Mức nghiêm trọng được áp dụng đủ nhất quán để dữ liệu đáng tin, tải cảnh báo được giữ dưới trần tường minh, và quyết định tiếp tục hay dừng trong và sau sự cố được dẫn dắt bởi bằng chứng thay vì bản năng.

**Mức 5, Điều phối.** Quản lý sự cố được cải thiện liên tục và tích hợp trong toàn tổ chức. Ứng phó trơn tru và được diễn tập kỹ qua ngày diễn tập thường xuyên, phân tích tổng hợp thúc đẩy đầu tư cấu trúc loại bỏ cả loại thất bại, và rút kinh nghiệm tạo thành trí nhớ tổ chức tìm kiếm được nuôi sổ tay vận hành, đào tạo, rà soát kiến trúc và hoạch định năng lực. Hệ thống thích ứng khi nó lớn, và tỷ lệ cùng tác động sự cố xu hướng giảm theo thời gian.

## Ý tưởng để thảo luận

- Tiêu chí nào phân biệt các mức nghiêm trọng của bạn, và mọi người có áp dụng chúng nhất quán không?
- Làm sao bạn giữ trực ca bền vững khi hệ thống lớn lên mà không thêm người vô tận?
- Ai có thẩm quyền đưa ra quyết định tốn kém, như chuyển dự phòng hay hoàn tác, trong một sự cố trực tiếp?
- Bạn nên minh bạch với khách hàng và công chúng đến mức nào trong ngừng hoạt động, và giới hạn ở đâu?
- Làm sao bạn bảo đảm hành động khắc phục thực sự được hoàn tất thay vì nằm trong tồn đọng?
- Cần gì để biến bộ sưu tập rút kinh nghiệm của bạn thành trí nhớ tổ chức thực sự tái sử dụng được?

## Những điểm cần ghi nhớ

- Mọi hệ thống đều thất bại; độ trưởng thành được đo bằng bạn ứng phó và học tốt đến đâu, không phải bằng việc tránh mọi sự cố.
- Một cấu trúc chỉ huy sự cố rõ ràng với vai trò và mức nghiêm trọng xác định cho phép nhóm lớn phối hợp dưới áp lực.
- Truyền thông sớm, thường xuyên và trung thực với các bên liên quan nội bộ và bên ngoài; im lặng phá hủy lòng tin.
- Giữ trực ca bền vững qua vòng trực công bằng, đền bù, và giảm không ngừng cảnh báo ồn.
- Tổ chức rút kinh nghiệm không đổ lỗi tạo hành động khắc phục có chủ sở hữu, được theo dõi, và hoàn tất chúng.
- Học tổng hợp và trí nhớ tổ chức tìm kiếm được biến sự cố riêng lẻ thành cải thiện bền vững.

## Tài liệu tham khảo và đọc thêm

- Betsy Beyer et al., *Site Reliability Engineering* (các chương về quản lý sự cố và rút kinh nghiệm)
- Betsy Beyer et al., *The Site Reliability Workbook* (thực hành trực ca và ứng phó sự cố)
- John Allspaw, *Blameless PostMortems and a Just Culture* (Etsy engineering)
- Sidney Dekker, *The Field Guide to Understanding Human Error*
- Charles Perrow, *Normal Accidents: Living with High-Risk Technologies*
- U.S. Federal Emergency Management Agency, tài liệu tham khảo *Incident Command System (ICS)*
- PagerDuty, *Incident Response Documentation* (thực hành mã nguồn mở)
