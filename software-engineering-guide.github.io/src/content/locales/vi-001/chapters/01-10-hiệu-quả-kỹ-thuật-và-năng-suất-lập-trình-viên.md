# 1.10 Hiệu quả kỹ thuật và năng suất lập trình viên

## Tổng quan và động lực

Mọi nhà lãnh đạo của một tổ chức phần mềm lớn cuối cùng đều hỏi một biến thể của cùng một câu hỏi: chúng ta có đang xây dựng phần mềm tốt hơn không, và làm sao chúng ta biết? Chương này nói về việc trả lời điều đó một cách trung thực. **Hiệu quả kỹ thuật** là mức độ tổ chức của bạn biến nỗ lực kỹ thuật thành phần mềm có giá trị, đáng tin cậy. **Năng suất lập trình viên** là phía cá nhân và đội nhóm của điều đó: một lập trình viên có thể tạo ra bao nhiêu đầu ra hữu ích, và môi trường làm việc trả lại cho họ bao nhiêu thời gian và sự chú ý thay vì lấy đi.

Rắc rối bắt đầu ngay khi có ai đó cố gắng rút gọn điều này thành một con số duy nhất. Đếm số dòng mã và mọi người viết nhiều mã hơn. Đếm điểm câu chuyện và ước lượng bị thổi phồng. Đếm commit, pull request hay số giờ ngồi tại bàn, và bạn thưởng cho chuyển động thay vì tiến bộ. Năng suất của một người lao động tri thức không phải là số lượng sản phẩm. Một lập trình viên xóa mười nghìn dòng mã chết, hoặc dành một ngày lập trình theo cặp để đồng đội tránh một sự cố trên môi trường thực, đã làm một công việc xuất sắc mà không chỉ số ngây thơ nào nắm bắt được. Câu trả lời trung thực cho "chúng ta năng suất đến đâu?" là đa chiều, và nó coi trải nghiệm làm việc của lập trình viên là một tín hiệu thực sự chứ không phải mềm.

Điều này quan trọng hơn, không phải ít hơn, khi bạn mở rộng quy mô. Trong một doanh nghiệp có hàng chục đội, những lượng ma sát nhỏ (một bản dựng chậm, một bộ kiểm thử chập chờn, hai ngày chờ một môi trường) nhân lên qua hàng trăm kỹ sư thành năng lực mất đi khổng lồ. Trong chính phủ, nơi không có giá thị trường cho đầu ra, rủi ro là "sân khấu đầu ra": đo số tài liệu được tạo ra hoặc số phiếu việc được đóng trong khi giá trị công không được đo. Mục tiêu của chương này là giúp bạn đo lường và cải thiện hiệu quả của tổ chức kỹ thuật và trải nghiệm hằng ngày của các lập trình viên, mà không bị lách, giám sát hay xếp hạng con người với nhau.

## Các nguyên tắc chính

- **Năng suất là đa chiều.** Không con số đơn lẻ nào nắm bắt được nó. Bất kỳ chỉ số nào được đưa ra như *thước đo duy nhất* đều sai.
- **Đo để loại bỏ ma sát, không phải để xếp hạng con người.** Đối tượng của việc đo là hệ thống, không phải cá nhân.
- **Đối chiếu nhiều nguồn.** Kết hợp cảm nhận của lập trình viên về công việc với điều các hệ thống thực sự ghi lại.
- **Trải nghiệm của lập trình viên là dữ liệu.** Vòng phản hồi, tải nhận thức và dòng chảy đo được và đáng cải thiện.
- **Giả định mọi chỉ số đều sẽ bị lách.** Thiết kế chống lại định luật Goodhart bằng nhiều chiều và ý định trung thực.
- **Kết nối với kết quả, một cách cẩn trọng.** Hiệu quả nên nối lên giá trị kinh doanh mà không trở thành mục tiêu làm hỏng.

## Khuyến nghị

### Từ chối cái bẫy chỉ số đơn lẻ

Kỷ luật đầu tiên là từ chối gọi tên một con số làm năng suất. Số dòng mã, số commit, [vận tốc](https://en.wikipedia.org/wiki/Velocity_(software_development)) theo điểm câu chuyện và số giờ ghi nhận đều chung một khiếm khuyết chí mạng: chúng đo hoạt động, không phải giá trị, và hoạt động thì quá dễ thổi phồng. Đây là [định luật Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law) đang vận hành, nguyên lý rằng khi một thước đo trở thành mục tiêu, nó không còn là thước đo tốt. Vận tốc được phát minh như công cụ dự báo của chính một đội; ngay khi một người quản lý so sánh điểm của đội này với đội khác, các đội âm thầm đổi thang ước lượng của mình và con số trở nên vô nghĩa. Khi ai đó đòi một KPI năng suất duy nhất, hãy coi đó là một yêu cầu cần định hình lại, không phải đáp ứng. Thay vào đó hãy đưa ra một bộ nhỏ cân bằng, và giải thích vì sao một con số sẽ đánh lừa họ.

### Dùng SPACE để cấu trúc điều bạn đo

**Khung SPACE** cho bạn năm chiều đáng giữ cùng nhau: **S**atisfaction và well-being (sự hài lòng và sức khỏe), **P**erformance (hiệu suất), **A**ctivity (hoạt động), **C**ommunication và collaboration (giao tiếp và cộng tác), và **E**fficiency và flow (hiệu quả và dòng chảy). Điểm của SPACE là bạn nên chọn ít nhất vài chiều, không bao giờ chỉ một, và không bao giờ tất cả từ cùng một loại. Các chỉ số hoạt động (commit, triển khai) hấp dẫn vì dễ thu thập, nhưng riêng chúng thì bóp méo. Hãy ghép chúng với một tín hiệu hài lòng và một tín hiệu hiệu suất để không chiều nào có thể bị lách mà các chiều khác không phơi bày. Một đội phát hành nhiều lần triển khai hơn trong khi sự hài lòng sụp đổ và tỷ lệ thay đổi thất bại leo thang không hề năng suất hơn, và một bộ cân bằng cho bạn thấy điều đó ngay lập tức.

### Coi trải nghiệm lập trình viên là vòng phản hồi, tải nhận thức và dòng chảy

**Trải nghiệm lập trình viên (DevEx)** là cảm giác khi làm công việc kỹ thuật ở đây, và nó cụ thể hơn vẻ ngoài. Nó dựa trên ba thứ bạn có thể đo và cải thiện. **Vòng phản hồi** là thời gian một lập trình viên chờ để biết một việc có hiệu quả không: thời gian dựng cục bộ, thời lượng bộ kiểm thử, thời gian xử lý đánh giá mã, thời gian triển khai. Các vòng chậm buộc phải chuyển đổi ngữ cảnh và chờ đợi nhàn rỗi. **[Tải nhận thức](https://en.wikipedia.org/wiki/Cognitive_load)**, tổng nỗ lực tinh thần mà một nhiệm vụ đòi hỏi, tăng lên khi lập trình viên phải xoay xở quá nhiều công cụ, hệ thống không có tài liệu và phụ thuộc rối rắm để thực hiện một thay đổi đơn giản. **[Dòng chảy](https://en.wikipedia.org/wiki/Flow_(psychology))** là trạng thái đắm chìm tập trung, hiệu quả mà lịch bị phân mảnh và sự gián đoạn liên tục phá hủy. Khi bạn rút ngắn một vòng phản hồi, loại bỏ một khái niệm mà lập trình viên phải giữ trong đầu, hoặc bảo vệ một khối thời gian tập trung, bạn đã cải thiện năng suất theo cách không phép đếm hoạt động nào ghi nhận. Đây chính là mối quan tâm DevEx mà kỹ thuật nền tảng phục vụ thông qua các con đường trải sẵn và tự phục vụ (chương 8.4).

### Đối chiếu cảm nhận với các chỉ số hệ thống

Không nguồn dữ liệu đơn lẻ nào đáng tin riêng nó, vì vậy hãy kết hợp hai loại. **Dữ liệu cảm nhận** đến từ chính lập trình viên thông qua một **khảo sát trải nghiệm lập trình viên**: một bảng câu hỏi đều đặn, chủ yếu ẩn danh, hỏi họ cảm thấy tự tin thế nào khi phát hành, họ mất thời gian ở đâu, và điều gì làm họ bực bội. **Dữ liệu hệ thống** đến từ công cụ của bạn: thời gian đường ống, độ trễ đánh giá mã, tần suất sự cố. Mỗi loại sửa cho loại kia. Khảo sát bắt được nỗi đau mà thiết bị bỏ sót, như một lịch trực ca làm nản lòng hay một dịch vụ cũ đáng sợ. Chỉ số hệ thống bắt được những vấn đề mà mọi người đã coi là bình thường và thôi báo cáo. Khi khảo sát nói các bản dựng đau đớn và dữ liệu đường ống của bạn xác nhận thời gian dựng trung vị mười lăm phút, bạn có một khoản đầu tư được ưu tiên, có thể bảo vệ. Hãy chạy khảo sát theo nhịp đều đặn, giữ nó ngắn, và luôn khép vòng bằng cách cho thấy điều gì đã thay đổi nhờ nó.

### Dùng DORA như tín hiệu phân phối, không phải bảng xếp hạng

Bốn chỉ số **[DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (DORA)** (tần suất triển khai, thời gian dẫn của thay đổi, tỷ lệ thay đổi thất bại và thời gian khôi phục dịch vụ) là một cách đọc mạnh, có nghiên cứu hậu thuẫn về năng lực phân phối của bạn, ghép tốc độ với sự ổn định để không cái nào bị hy sinh cho cái kia. Chương 11.5 nắm giữ chiều sâu về các chỉ số này, và chương 11.2 bao quát đường ống phân phối mà chúng đo; hãy dùng chúng ở đó. Ở đây, hướng dẫn là về cách nắm giữ chúng. Hãy coi DORA như một tín hiệu sức khỏe cấp đội cho thấy hệ thống phân phối của bạn có đang cải thiện không, không phải bảng điểm để xếp hạng các đội hay cá nhân. Ngay khi các con số DORA xuất hiện trong đánh giá hiệu suất của ai đó, các đội bắt đầu tách các lần triển khai để độn tần suất và giấu sự cố để bảo vệ tỷ lệ thất bại của mình, và tín hiệu chết.

### Đo hệ thống, không bao giờ giám sát cá nhân

Đây là lằn ranh bạn không được vượt qua. Hãy gộp các chỉ số lên cấp đội và tổ chức, và dùng chúng để tìm và loại bỏ ma sát. Đừng xây các bảng điều khiển xếp hạng lập trình viên theo commit, giờ làm hay "điểm năng suất", và đừng để dữ liệu đo từ xa cá nhân đi vào lương hay thăng tiến. Giám sát phá hủy sự an toàn tâm lý và niềm tin mà kỹ thuật hiệu quả phụ thuộc vào, và nó dạy mọi người tối ưu chỉ số thay vì công việc. Sự phát triển và đánh giá cá nhân thuộc về các cơ chế riêng, mang tính con người của lộ trình nghề nghiệp và các cuộc trò chuyện với người quản lý (chương 1.3). Đo lường hiệu quả hỏi "điều gì đang làm chậm các đội của chúng ta?" Nó không bao giờ hỏi "kỹ sư nào của chúng ta chậm nhất?"

### Tấn công thẳng vào công việc lặp lại và ma sát

Một khi bạn thấy được thời gian rò rỉ ở đâu, hãy chi nó trở lại. Phần lớn những gì giới hạn hiệu quả là **công việc lặp lại (toil)**, công việc thủ công, lặp đi lặp lại, tự động hóa được, tăng theo tăng trưởng và không mang lại giá trị lâu dài (chương 9.1). Các đánh giá chậm cũng là ma sát, nên việc tinh giản đánh giá mã (chương 2.5) bằng các thay đổi nhỏ hơn và kỳ vọng rõ ràng rút ngắn một vòng phản hồi cốt lõi. Các con đường trải sẵn và nền tảng tự phục vụ (chương 8.4) loại bỏ cả những loại chờ đợi và tải nhận thức cùng lúc. Cũng hãy dành ngân sách cho [nợ kỹ thuật](https://en.wikipedia.org/wiki/Technical_debt), chi phí tích lũy của những đường tắt trong quá khứ đánh thuế mọi thay đổi trong tương lai, vì một cơ sở mã mà không ai có thể sửa đổi an toàn là cái hố sâu nhất nuốt năng suất.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| Chỉ số năng suất đơn lẻ (LOC, vận tốc, commit) | Rẻ, dễ, một con số cho lãnh đạo | Bị lách ngay lập tức; đo hoạt động không phải giá trị; ăn mòn niềm tin |
| Bộ cân bằng kiểu SPACE | Chống lách; phản ánh thực tế | Thu thập tốn công hơn; khó tóm tắt thành một con số |
| Khảo sát DevEx (cảm nhận) | Bắt được nỗi đau cảm nhận mà thiết bị bỏ sót | Chủ quan; cần niềm tin và việc theo dõi đến cùng để giữ trung thực |
| Chỉ số hệ thống (DORA, thời gian đường ống) | Khách quan, liên tục, khó làm giả khi gộp | Mù trước tinh thần và ngữ cảnh; nguy hiểm nếu áp dụng cho cá nhân |
| Đối chiếu cả hai | Mỗi nguồn sửa cho nguồn kia; vững chắc | Cần đầu tư vào công cụ và kỷ luật khảo sát |

Căng thẳng trung tâm là sự chặt chẽ so với sự trung thực. Một con số đơn lẻ dễ báo cáo và dễ làm hỏng; một bức tranh phong phú, đa chiều thì trung thực nhưng khó truyền đạt cho một giám đốc điều hành bận rộn. Hãy giải quyết bằng cách chọn một bộ nhỏ cân bằng (vài chiều SPACE cộng một khảo sát cộng DORA như một cách đọc về phân phối), báo cáo xu hướng thay vì ảnh chụp nhanh, và nói rõ rằng các con số tồn tại để cải thiện hệ thống, không phải để chấm điểm con người. Khi ban lãnh đạo muốn "một biểu đồ", hãy đưa cho họ xu hướng của vài tín hiệu bổ sung cho nhau và từ chối sự cám dỗ gộp chúng thành một chỉ số tổng hợp giả.

## Câu hỏi để thảo luận với đội của bạn

1. **Nếu một nhà lãnh đạo đòi một con số năng suất duy nhất vào ngày mai, bạn sẽ đưa cho họ cái gì?** Câu hỏi này phơi bày liệu tổ chức của bạn có hiểu cái bẫy hay không. Câu trả lời trung thực là không con số đơn lẻ nào an toàn, và công việc của bạn là định hình lại yêu cầu thành một bộ nhỏ cân bằng chống được việc lách. Hãy mang các chỉ số bạn đã báo cáo và hỏi, với mỗi cái, "một đội thông minh, hoài nghi sẽ thổi phồng cái này thế nào mà không làm việc tốt hơn?" Nếu câu trả lời dễ, chỉ số đó nguy hiểm ngay khi nó trở thành mục tiêu. Hãy thảo luận bạn sẽ đưa ra gì thay thế, và bạn sẽ giải thích với ban lãnh đạo vì sao một con số sẽ khiến họ tối ưu sai thứ. Chất lượng của cuộc trò chuyện đó dự đoán việc đo lường sẽ giúp bạn hay làm hỏng bạn.

2. **Vòng phản hồi chậm nhất của bạn là gì, và nó tốn của bạn bao nhiêu mỗi ngày?** Vòng phản hồi là nơi năng suất rò rỉ âm thầm: một bản dựng mười lăm phút, hai ngày chờ đánh giá, một bộ kiểm thử chập chờn làm xói mòn niềm tin vào mọi dấu xanh. Hãy mang số liệu thực từ một khảo sát trải nghiệm lập trình viên và từ thiết bị đo đường ống của bạn, và xem nỗi đau cảm nhận và độ trễ đo được có khớp nhau không. Ước tính chi phí hằng ngày bằng cách nhân thời gian chờ với số lập trình viên gặp phải và tần suất, và lập luận đầu tư thường tự nó hiện ra. Hãy quyết định vòng nào cần rút ngắn trước và ai chịu trách nhiệm sửa. Một đội không gọi tên được vòng chậm nhất của mình thì chưa bắt đầu đo thứ quan trọng nhất.

3. **Việc đo lường của bạn có nguy cơ giống như giám sát ở đâu, và bạn sẽ ngăn điều đó như thế nào?** Sự khác biệt giữa đo hệ thống và theo dõi con người là sự khác biệt giữa niềm tin và nỗi sợ, và rất dễ vượt qua mà không nhận ra. Hãy đi qua mọi bảng điều khiển và báo cáo và hỏi liệu cái nào có thể xếp hạng một cá nhân hoặc đưa vào đánh giá hiệu suất. Hãy quyết định tường minh điều gì được giữ ở dạng gộp, điều gì giữ ẩn danh, và điều gì bị cấm, rồi nói công khai điều đó với các đội đang được đo. Trong bối cảnh doanh nghiệp và chính phủ, nơi áp lực giám sát và kiểm toán mạnh, sự cám dỗ đào sâu đến từng cá nhân là liên tục, nên lan can phải là một nguyên tắc đã nêu, không phải một hy vọng. Nếu lập trình viên tin rằng các con số đang bị dùng chống lại họ, họ sẽ tối ưu các con số và sự thật sẽ biến mất.

4. **Lần cuối cùng chúng ta hỏi lập trình viên về cảm giác công việc, điều gì đã thay đổi nhờ đó, và họ có bao giờ biết không?** Một khảo sát không tạo ra hành động hiển thị dạy lập trình viên ngừng trả lời trung thực, nên khảo sát im lặng lần thứ hai thu về ít phản hồi hơn và nhạt hơn lần đầu, và công cụ bạn dựa vào phân rã đúng lúc bạn mở rộng nó. Với một tổ chức lớn, sự lãng phí cộng dồn: hàng trăm người dành thời gian báo cáo ma sát, một báo cáo được lưu hành, và không có gì được phát hành. Hãy mang ba phát hiện hàng đầu của khảo sát gần nhất, công việc cụ thể mỗi phát hiện đã kích hoạt, và cách bạn truyền đạt kết quả lại cho những người đã nêu ra. Hãy cân nhắc lực kéo đối lập giữa hành động theo lời phàn nàn ồn ào nhất và theo lời phàn nàn phổ biến nhất, vì chúng thường là những vấn đề khác nhau. Trong bối cảnh doanh nghiệp và chính phủ, nơi sự mệt mỏi vì khảo sát và quá tải tham vấn đã cao, hãy coi việc khép vòng là một cam kết quản trị: nêu tên ai chịu trách nhiệm phản hồi, công bố điều đã thay đổi, và chấp nhận rằng một khảo sát không được trả lời còn tệ hơn không có khảo sát nào.

5. **Làm thế nào để chúng ta so sánh các đội mà không xây một bảng xếp hạng phạt sự trung thực?** Các nhà lãnh đạo của tổ chức lớn tự nhiên muốn biết đội nào đang phát triển mạnh và đội nào đang kẹt, nhưng xếp hạng các đội theo vận tốc thô, tần suất triển khai hay số DORA bỏ qua rằng một đội thanh toán chịu quy định nặng và một đội làm bản mẫu từ đầu sống trong những thế giới khác nhau. Cân nhắc đối lập là có thật: bạn cần phát hiện các đội gặp khó khăn và lan truyền những gì hiệu quả, nhưng ngay khi so sánh trở thành bảng điểm, các đội đổi thang ước lượng, giấu sự cố và tách các lần triển khai để bảo vệ vị thế của mình. Hãy mang các ví dụ cụ thể về cách ngữ cảnh đội khác nhau trong tổ chức của bạn, cùng một đề xuất so sánh mỗi đội với quỹ đạo của chính nó theo thời gian thay vì với những đội lân cận. Trong bối cảnh doanh nghiệp và chính phủ, nơi áp lực kiểm toán và giám sát đẩy mạnh về phía xếp hạng giữa các đội, hãy thống nhất trước điều gì được phép so sánh, điều gì sẽ chỉ được đọc như xu hướng của từng đội, và ai có quyền từ chối một phép so sánh không công bằng.

6. **Làm thế nào để chúng ta kết nối hiệu quả với kết quả thực mà không biến một chỉ số phân phối thành mục tiêu làm hỏng?** Hiệu quả không bao giờ nối lên giá trị trông như tự ngắm mình với ban lãnh đạo, nhưng ngay khi một tín hiệu phân phối như thời gian dẫn hay tần suất triển khai trở thành mục tiêu trong đánh giá hiệu suất, các đội tối ưu con số và bỏ rơi kết quả mà nó vốn đại diện. Với một tổ chức lớn, căng thẳng này gay gắt, vì các giám đốc điều hành muốn có một đường rõ ràng từ nỗ lực kỹ thuật đến kết quả kinh doanh trong khi đường trung thực thì lộn xộn và có độ trễ. Hãy mang các thước đo kết quả hiện tại của bạn, các tín hiệu phân phối bạn sẽ gắn với chúng, và một bản tường thuật tường minh về cách mỗi cái có thể bị lách nếu nó trở thành mục tiêu. Hãy cân nhắc lực kéo giữa một câu chuyện đơn giản mà ban lãnh đạo có thể kể lại và một bức tranh trung thực chống được sự bóp méo. Trong chính phủ hoặc một nền tảng nội bộ phi thị trường, nơi không có doanh thu để neo giá trị, hãy sẵn sàng định nghĩa kết quả là độ tin cậy dịch vụ, thời gian chu kỳ khi sửa lỗi và lợi ích công thay vì hoạt động thô, và bảo vệ lựa chọn đó trước các cơ quan giám sát vốn có thể thích những hiện vật dễ đếm hơn.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và nguồn vốn eo hẹp, hãy bỏ hẳn các bảng điều khiển và đo hai thứ thay đổi nhanh nhất: một khảo sát trải nghiệm lập trình viên mười câu hỏi và thời gian đường ống cơ bản. Rủi ro năng suất lớn nhất của bạn là một bộ kiểm thử chậm hoặc chập chờn và việc chuyển đổi ngữ cảnh liên tục, vì vậy hãy tìm vòng phản hồi tệ nhất, rút ngắn nó, và đi tiếp. Đừng dựng một chương trình đo lường mà bạn không có ai vận hành, vì một cuộc trò chuyện trung thực duy nhất về việc ngày làm việc rò rỉ ở đâu tốt hơn bất kỳ công cụ nào bạn sau đó phải bảo trì.

**Doanh nghiệp nhỏ.** Không có chuyên gia đo lường và ngân sách eo hẹp, hãy dựa vào những gì công cụ hiện có của bạn đã ghi lại: thời gian dựng, độ trễ đánh giá và số sự cố từ các hệ thống bạn đã trả tiền. Hãy mua một công cụ khảo sát nhẹ thay vì tự xây, và cưỡng lại lời chào hàng của nhà cung cấp về bảng điều khiển năng suất cá nhân, thứ sẽ tốn của bạn niềm tin mà bạn không thể phung phí. Hãy trình bày toàn bộ nỗ lực như việc loại bỏ ma sát cho một đội nhỏ không thể lãng phí ngày làm việc của bất kỳ ai.

**Doanh nghiệp lớn.** Qua hàng chục đội, phần thưởng là năng lực thu hồi ở quy mô lớn, và mối nguy là một bảng điều khiển trung tâm âm thầm trượt thành xếp hạng con người. Hãy chuẩn hóa một chương trình cân bằng (khảo sát DevEx hằng quý, vài chiều SPACE, và DORA được đọc như xu hướng phân phối của từng đội) và quản trị nó để dữ liệu đo từ xa cá nhân không bao giờ được thu thập. Hãy so sánh mỗi đội với quỹ đạo của chính nó, biện minh cho đầu tư nền tảng (chương 8.4) dựa trên ma sát mà dữ liệu phơi bày, và trao cho một chủ sở hữu chịu trách nhiệm thẩm quyền từ chối bất kỳ chỉ số nào sẽ trở thành bảng xếp hạng.

**Chính phủ.** Không có giá thị trường cho đầu ra và áp lực giám sát mạnh, sức hút về phía sân khấu đầu ra (đếm tài liệu và phiếu việc đã đóng) là liên tục, và sức hút về phía giám sát các cá nhân có tên dưới danh nghĩa kiểm toán còn mạnh hơn. Thay vào đó hãy đo kết quả và năng lực phân phối: một dịch vụ phát hành bản sửa nhanh thế nào, nó đáng tin cậy ra sao, và nhân viên cùng nhà thầu trải nghiệm công việc thế nào qua một khảo sát ẩn danh. Hãy đo công chức và nhà thầu trên cùng một cơ sở cấp hệ thống, công bố việc đo lường nhằm mục đích gì, và sẵn sàng lập luận trước cơ quan lập pháp rằng xu hướng phân phối của từng đội là cách đọc trung thực hơn về giá trị công so với bất kỳ điểm số cá nhân nào.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp hai mươi người nhận thấy việc phát hành chậm lại dù mọi người đều bận. Thay vì cài đặt một bảng điều khiển năng suất, trưởng nhóm kỹ thuật chạy một khảo sát DevEx mười câu hỏi và lấy thời gian đường ống cơ bản. Khảo sát và dữ liệu đồng ý: bộ kiểm thử mất hai mươi hai phút và thất bại ngẫu nhiên, nên mọi người gom các thay đổi và chuyển đổi ngữ cảnh trong khi chờ. Đội dành hai tuần sửa các kiểm thử chập chờn và song song hóa bộ kiểm thử, cắt nó còn bốn phút. Tần suất triển khai tự tăng, sự hài lòng nhảy vọt trong khảo sát tiếp theo, và không ai bị xếp hạng hay chấm điểm để điều đó xảy ra.

**Doanh nghiệp lớn.** Một ngân hàng với bốn mươi đội kỹ thuật muốn biện minh cho việc tiếp tục đầu tư vào nền tảng nội bộ. Nhóm nền tảng áp dụng một chương trình đo lường cân bằng: khảo sát DevEx hằng quý trên tất cả các đội, tín hiệu kiểu SPACE, và các chỉ số DORA được đọc ở cấp đội như một xu hướng sức khỏe phân phối (chương 11.5). Quan trọng là, họ đối sánh các đội một cách công bằng bằng cách so sánh mỗi đội với quỹ đạo của chính nó theo thời gian, không phải với nhau, vì ngữ cảnh của các đội khác nhau rất nhiều. Dữ liệu cho thấy các đội trên con đường trải sẵn (chương 8.4) hội nhập kỹ sư mới trong vài ngày thay vì vài tuần và báo cáo tải nhận thức thấp hơn nhiều. Bằng chứng đó, được trình bày như năng lực thu hồi trên hàng trăm lập trình viên, tài trợ cho nền tảng thêm một năm. Dữ liệu đo từ xa cá nhân được cố ý không bao giờ thu thập.

**Chính phủ.** Một cơ quan dịch vụ số liên bang phải chứng minh với cơ quan lập pháp rằng chi tiêu kỹ thuật của họ mang lại giá trị, trong bối cảnh không có giá thị trường cho đầu ra. Cơ quan từ chối sân khấu đầu ra (đếm tài liệu hay phiếu việc đã đóng) và thay vào đó đo kết quả và năng lực phân phối: các dịch vụ có thể phát hành bản sửa nhanh thế nào, chúng đáng tin cậy ra sao, và lực lượng lao động cùng nhà thầu trải nghiệm công việc thế nào qua một khảo sát ẩn danh. Các tín hiệu phân phối kiểu DORA cho thấy việc hiện đại hóa có thực sự cải thiện thông lượng và sự ổn định không, được gắn lại với kết quả công thay vì hoạt động thô (chương 11.5). Vì việc đo lường không bao giờ xếp hạng cá nhân, và vì nhân viên nhà thầu và công chức được đo trên cùng một cơ sở cấp hệ thống, cơ quan tránh được các vấn đề giám sát và tinh thần vốn nhấn chìm những nỗ lực như vậy, và cho các cơ quan giám sát một cách đọc trung thực về giá trị.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của việc đo lường và cải thiện hiệu quả là năng lực thu hồi, và ở quy mô lớn các con số rất lớn. Những ma sát nhỏ nhân lên trong một tổ chức lớn: một bản dựng mười phút mà một trăm kỹ sư gặp phải nhiều lần mỗi ngày là hàng nghìn giờ kỹ sư mỗi năm dành để chờ. Rút ngắn vòng đó và bạn đã thêm năng lực đáng kể mà không cần tuyển ai. ROI chi phối ở đây giống như trong kỹ thuật nền tảng (chương 8.4): thời gian kỹ thuật đắt đỏ được chuyển hướng từ chờ đợi và công việc lặp lại sang công việc có giá trị.

Tổng chi phí sở hữu khiêm tốn nhưng có thật. Bạn trả cho công cụ khảo sát và kỷ luật vận hành nó, cho việc trang bị thiết bị đo đường ống, và cho sự chú ý của ban quản lý để đọc xu hướng và hành động theo chúng. Rủi ro lớn hơn đối với ROI là làm việc đo lường tệ. Một chỉ số đơn lẻ bị lách hoặc một chương trình giám sát có thể tạo ra lợi tức âm: nhiều tháng nỗ lực tối ưu một con số trong khi kết quả thực đình trệ, cộng với sự ăn mòn niềm tin khiến mọi thay đổi trong tương lai khó hơn. Chi phí của việc không đo lường gì cả thì lan tỏa và khổng lồ: ma sát và công việc lặp lại tích tụ vô hình, kỹ sư cấp cao kiệt sức vì lãng phí có thể tránh, và ban lãnh đạo không thể biết các khoản đầu tư có giúp ích không. Hãy trình bày lập luận với ban lãnh đạo như đòn bẩy và sự trung thực: một chương trình đo lường nhỏ, đáng tin, cân bằng tìm ra nơi một lực lượng lao động lớn mất thời gian, và tự hoàn vốn nhiều lần ngay khi bạn hành động theo phát hiện đầu tiên.

## Phản mẫu và cạm bẫy

- **Chỉ số năng suất đơn lẻ.** Bất kỳ con số nào (LOC, vận tốc, commit, giờ) cũng bị lách ngay ngày nó trở thành mục tiêu.
- **Xếp hạng cá nhân.** Bảng xếp hạng và "điểm năng suất" cá nhân phá hủy niềm tin và dạy mọi người tối ưu chỉ số.
- **Đo lường như giám sát.** Dữ liệu đo từ xa cá nhân chi tiết đưa vào đánh giá ăn mòn sự an toàn tâm lý mà công việc hiệu quả cần.
- **Khảo sát không có việc theo dõi.** Hỏi lập trình viên về cảm giác công việc rồi không thay đổi gì dạy họ ngừng trả lời trung thực.
- **So sánh số thô của các đội.** Ngữ cảnh đội khác nhau; so sánh vận tốc hoặc DORA giữa các đội phạt sự trung thực và thưởng cho việc lách.
- **Sân khấu đầu ra.** Đếm hiện vật được tạo ra (tài liệu, phiếu việc, tính năng đã phát hành) trong khi kết quả thực không được đo, phổ biến ở nơi không có giá thị trường.
- **DORA trong đánh giá hiệu suất.** Ngay khi các chỉ số phân phối chấm điểm con người, các đội giấu sự cố và tách các lần triển khai, và tín hiệu chết.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Năng suất được đánh giá bằng cảm tính hoặc một chỉ số đơn lẻ dễ bị lách như số dòng mã, vận tốc hoặc số giờ. Đo lường tùy nghi và phản ứng, ma sát vô hình, phàn nàn mang tính giai thoại, và không ai có thể nói tổ chức có đang tốt hơn không.
- **Mức 2, Phát triển:** Một số đội áp dụng các thực hành cơ bản: vài chỉ số, thường là đếm hoạt động, và thỉnh thoảng có khảo sát trải nghiệm lập trình viên. Các thực hành không nhất quán giữa các đội, dữ liệu được thu thập nhưng hiếm khi được hành động theo, những so sánh thô giữa các đội len vào, và không có nguyên tắc chung nào bảo vệ cá nhân khỏi bị xếp hạng.
- **Mức 3, Chuẩn hóa:** Một chương trình đo lường cân bằng được lập thành tài liệu và áp dụng toàn tổ chức, dùng các chiều kiểu SPACE, khảo sát DevEx đều đặn và DORA như tín hiệu phân phối (chương 11.5). Các chỉ số được gộp lên cấp đội theo chính sách, cá nhân không bao giờ bị xếp hạng, và các phát hiện thúc đẩy công việc cụ thể để rút ngắn vòng phản hồi và cắt công việc lặp lại (chương 9.1).
- **Mức 4, Quản lý:** Chương trình được đo lường và kiểm soát theo các đường cơ sở. Thời gian vòng phản hồi, điểm khảo sát và xu hướng DORA có các mục tiêu đã thống nhất và được theo dõi theo thời gian; mỗi đội được so sánh với quỹ đạo của chính nó thay vì với những đội lân cận; các khoản đầu tư nền tảng và giảm công việc lặp lại được biện minh bằng dữ liệu trước-sau về năng lực thu hồi; và sự suy giảm ở bất kỳ tín hiệu nào kích hoạt việc xem xét thay vì trôi qua không ai để ý.
- **Mức 5, Điều phối:** Đo lường được tin cậy, thường nhật và thích ứng. Dữ liệu cảm nhận và dữ liệu hệ thống được đối chiếu, xu hướng nuôi dưỡng cải tiến liên tục, ma sát và tải nhận thức được chủ động săn tìm và loại bỏ, bộ đo lường tự nó được sửa đổi khi tổ chức thay đổi, và hiệu quả được tích hợp với kết quả kinh doanh và công mà không chỉ số nào được phép trở thành mục tiêu làm hỏng.

## Ý tưởng để thảo luận

1. Chỉ số hiện tại nào của bạn có thể bị một đội hoài nghi thổi phồng mà không làm việc tốt hơn, và bạn sẽ thay chúng bằng gì?
2. Nếu bạn có thể rút ngắn đúng một vòng phản hồi trong toàn tổ chức, vòng nào sẽ mang lại nhiều năng lực thu hồi nhất?
3. Làm thế nào bạn đối sánh nhiều đội một cách công bằng khi ngữ cảnh của họ khác nhau, mà không tạo ra một bảng xếp hạng phạt sự trung thực?
4. Lằn ranh giữa đo hệ thống và giám sát cá nhân nằm ở đâu, và ai trong tổ chức của bạn có thẩm quyền thực thi nó?
5. Trong bối cảnh không có giá thị trường cho đầu ra, như chính phủ hay một nền tảng nội bộ, làm sao bạn đo giá trị thực thay vì hoạt động?
6. Bạn sẽ cho một lập trình viên xem gì để chứng minh rằng khảo sát quý này đã thay đổi điều gì đó?

## Những điểm cần ghi nhớ

- Năng suất của kỹ sư là đa chiều. Hãy từ chối bất kỳ con số đơn lẻ nào (số dòng mã, vận tốc, commit, giờ) là thước đo *duy nhất*, vì định luật Goodhart đảm bảo nó sẽ bị lách.
- Dùng **khung SPACE** (sự hài lòng và sức khỏe, hiệu suất, hoạt động, giao tiếp và cộng tác, hiệu quả và dòng chảy) để giữ nhiều chiều cùng nhau để không chiều nào có thể bị lách riêng lẻ.
- **Trải nghiệm lập trình viên** quy về vòng phản hồi, tải nhận thức và dòng chảy. Rút ngắn vòng và loại bỏ tải là năng suất thực mà phép đếm hoạt động không bao giờ cho thấy.
- **Đối chiếu** dữ liệu cảm nhận từ khảo sát DevEx với dữ liệu hệ thống từ công cụ của bạn; mỗi loại sửa cho loại kia.
- Coi các chỉ số **DORA** là tín hiệu phân phối cấp đội, không phải bảng xếp hạng; chiều sâu của chúng nằm ở chương 11.5 và đường ống ở chương 11.2.
- Đo **hệ thống**, không bao giờ cá nhân. Gộp lên cấp đội, giữ việc đánh giá trong các kênh con người riêng của chương 1.3, và không bao giờ để đo lường trở thành giám sát.
- Chi thời gian thu hồi vào việc cắt công việc lặp lại (chương 9.1), tăng tốc đánh giá mã (chương 2.5) và trải đường (chương 8.4). Kết nối hiệu quả với kết quả kinh doanh mà không để chỉ số nào trở thành mục tiêu làm hỏng.

## Tài liệu tham khảo và đọc thêm

- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck và Jenna Butler, "The SPACE of Developer Productivity" (*ACM Queue*, 2021): khung đa chiều.
- Abi Noda, Margaret-Anne Storey, Nicole Forsgren và Michaela Greiler, "DevEx: What Actually Drives Productivity" (*ACM Queue*, 2023): vòng phản hồi, tải nhận thức và dòng chảy.
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate: The Science of Lean Software and DevOps* (các chỉ số DORA và cơ sở nghiên cứu của chúng).
- DORA, *Accelerate State of DevOps Report* (hằng năm): chương trình nghiên cứu liên tục đằng sau bốn chỉ số.
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy, biên tập, *Site Reliability Engineering* (công việc lặp lại và việc loại bỏ nó).
- Matthew Skelton và Manuel Pais, *Team Topologies* (tải nhận thức như mối quan tâm thiết kế hạng nhất).
- Mihaly Csikszentmihalyi, *Flow: The Psychology of Optimal Experience* (nguồn gốc của trạng thái dòng chảy).
- Tom DeMarco và Timothy Lister, *Peopleware: Productive Projects and Teams* (sự tập trung, gián đoạn và khía cạnh con người của năng suất).
- Goodhart, C. A. E., "Problems of Monetary Management: The UK Experience" (1975): nguồn gốc của định luật Goodhart; xem thêm cách diễn đạt được trích dẫn rộng rãi của Marilyn Strathern.
- Hướng dẫn của Văn phòng Trách nhiệm Giải trình Chính phủ Hoa Kỳ (GAO) về đo lường hiệu suất: đo lường giá trị trong bối cảnh khu vực công phi thị trường.
