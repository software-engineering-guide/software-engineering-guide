# 5.1 Nền tảng UX

## Tổng quan và động lực

[Trải nghiệm người dùng](https://en.wikipedia.org/wiki/User_experience) (UX) là về việc hiểu con người (mục tiêu, bối cảnh, ràng buộc của họ) rồi định hình phần mềm để giúp họ thành công với ít ma sát nhất. Nó không phải đồ trang trí bạn áp dụng vào cuối. Đó là một cách làm việc bắt đầu trước dòng mã đầu tiên và tiếp tục rất lâu sau khi phát hành. Chương này bao quát các thực hành nghiên cứu, mô hình hóa và [tư duy thiết kế](https://en.wikipedia.org/wiki/Design_thinking) cho phép một tổ chức lớn đưa ra quyết định sản phẩm từ bằng chứng thay vì từ phỏng đoán.

Với các đội lớn, UX là một vấn đề điều phối nhiều như là một nghề thủ công. Khi hàng chục nhóm phát hành vào một sản phẩm dùng chung, các mô hình tinh thần không khớp, luồng trùng lặp, và thuật ngữ mâu thuẫn chồng chất thành một tổng thể gây rối mà không đội nào sở hữu. Một nền tảng UX dùng chung, xây từ persona chung, bản đồ hành trình đã thống nhất và một [kiến trúc thông tin](https://en.wikipedia.org/wiki/Information_architecture) có tài liệu, cho mọi đội cùng một bản đồ về người dùng, để các quyết định riêng của họ cộng lại thành một trải nghiệm mạch lạc. Không có nó, mỗi đội tối ưu cục bộ và sản phẩm nói chung chẳng có nghĩa gì.

Doanh nghiệp và chính phủ nâng rủi ro lên. Phần mềm doanh nghiệp thường có người dùng bị giữ chân không thể bỏ đi, nên UX tồi được trả giá bằng đào tạo, phiếu hỗ trợ, lỗi và mất năng suất thay vì bằng việc mọi người rời đi. Các dịch vụ chính phủ thường với tới toàn thể công chúng, bao gồm những người đang khủng hoảng, dùng thiết bị cũ, kém tự tin về số, hoặc không có nhà cung cấp thay thế. Ở đây chất lượng UX là vấn đề công bằng và niềm tin công dân: một đơn xin trợ cấp thiết kế kém có thể từ chối ai đó thức ăn hay nhà ở, không phải vì họ không đủ điều kiện, mà vì họ không thể hoàn thành biểu mẫu.

## Các nguyên tắc chính

- Thiết kế cho con người thật làm nhiệm vụ thật trong điều kiện thật, không phải cho một người dùng lý tưởng hóa trên kết nối nhanh với sự chú ý đầy đủ.
- Nghiên cứu giảm rủi ro. Thời điểm rẻ nhất để phát hiện một giả định sai là trước khi bạn xây chồng lên nó.
- Người dùng không thể nói đáng tin với bạn họ sẽ làm gì; hãy quan sát hành vi, không chỉ sở thích đã nêu.
- Tập trung vào công việc người dùng đang cố hoàn thành, không phải tính năng bạn muốn phát hành.
- Nhất quán là một tính năng: một mô hình tinh thần mạch lạc qua sản phẩm hạ tải nhận thức.
- [Khả năng tiếp cận](https://en.wikipedia.org/wiki/Accessibility) và sự hòa nhập là một phần của UX tốt từ đầu, không phải một lượt tuân thủ sau này.
- Phương pháp định tính và định lượng trả lời các câu hỏi khác nhau; hãy dùng cả hai.
- Nghiên cứu nhỏ, thường xuyên thắng các nghiên cứu nặng nề, hiếm hoi.

## Khuyến nghị

### Thiết lập nghiên cứu liên tục, hỗn hợp phương pháp

Hãy hướng tới một thực hành nghiên cứu nhẹ nhưng liên tục thay vì các nghiên cứu lớn thỉnh thoảng. Phỏng vấn hé lộ động cơ và mô hình tinh thần. [Kiểm thử khả dụng](https://en.wikipedia.org/wiki/Usability_testing) hé lộ nơi các thiết kế đổ vỡ; năm đến tám người tham gia mỗi vòng phơi bày hầu hết các vấn đề nghiêm trọng. Khảo sát đo thái độ ở quy mô lớn nhưng không giải thích được "vì sao." Phân tích và đo đạc cho thấy người ta thực sự làm gì trên toàn quần thể. Hãy ghép một phương pháp định tính (vì sao) với một phương pháp định lượng (bao nhiêu), để các phát hiện vừa được giải thích vừa được định cỡ. Và giữ một kho nghiên cứu, để hiểu biết vẫn tìm kiếm được và tái sử dụng được qua các đội thay vì lạc trong slide của một nhóm.

### Mô hình hóa người dùng bằng persona, bản đồ hành trình và công-việc-cần-làm

Hãy xây một tập nhỏ persona dựa trên bằng chứng nắm bắt mục tiêu, bối cảnh và ràng buộc, không phải biếm họa nhân khẩu học. Đóng khung nhu cầu là công-việc-cần-làm, kết quả nền tảng mà người dùng đang cố đạt thay vì một tính năng ("khi tôi mất việc, tôi muốn hiểu nhanh mình đủ điều kiện nhận hỗ trợ nào, để tôi tiếp tục trả tiền thuê nhà"). Điều này giữ tiêu điểm vào kết quả hơn tính năng. Bản đồ hành trình vẽ toàn bộ trải nghiệm qua các kênh và theo thời gian, phơi bày khoảng trống và điểm bàn giao mà không màn hình đơn lẻ nào cho thấy. Với các dịch vụ có vận hành hậu trường nặng (tổng đài, cán bộ xử lý hồ sơ, hoàn tất đơn hàng), hãy dùng [bản thiết kế dịch vụ](https://en.wikipedia.org/wiki/Service_blueprint) để nối trải nghiệm sân khấu trước với các hệ thống và nhân sự phía sau.

### Thiết kế kiến trúc thông tin có chủ đích

Kiến trúc thông tin (IA) là cách nội dung, tính năng và điều hướng được cấu trúc và gắn nhãn. Hãy dùng [phân loại thẻ](https://en.wikipedia.org/wiki/Card_sorting) và kiểm thử cây để suy ra cấu trúc đó từ mô hình tinh thần của người dùng thay vì từ sơ đồ tổ chức của bạn. Một thất bại phổ biến trong các tổ chức lớn là phơi bày ranh giới phòng ban nội bộ thành điều hướng cấp cao nhất. Hãy thiết lập một từ vựng có kiểm soát để cùng một khái niệm có cùng một tên ở mọi nơi. [Thiết kế tương tác](https://en.wikipedia.org/wiki/Interaction_design) sau đó xác định hành vi từng khoảnh khắc: trạng thái, phản hồi, khôi phục lỗi, và luồng giữa các bước.

### Áp dụng tư duy thiết kế một cách thực dụng

Mô hình kim cương kép (phân kỳ rồi hội tụ để xác định đúng vấn đề, rồi phân kỳ và hội tụ để thiết kế đúng giải pháp) là một khung hữu ích. Tuy nhiên hãy coi nó là một tư duy, không phải một quy trình có cổng cứng nhắc. Trong thực tế, hãy chạy các vòng lặp chặt: đóng khung một giả thuyết, phác thảo, kiểm thử với một nhúm người dùng, và học trong vài ngày. Dành khám phá nặng hơn cho các vấn đề thực sự mới lạ hoặc rủi ro cao. Và đề phòng "sân khấu đổi mới," nơi các buổi hội thảo tạo ra giấy nhớ nhưng không thay đổi nào được phát hành.

### Tích hợp UX vào phân phối

Hãy nhúng nhà thiết kế và nhà nghiên cứu vào các đội phân phối thay vì chạy một "phòng UX" riêng bàn giao đặc tả qua một bức tường. Biến phát hiện nghiên cứu thành đầu vào thường trực cho ưu tiên hóa. Đặt các cổng chất lượng UX, như chuẩn khả dụng và kiểm tra khả năng tiếp cận, vào định nghĩa hoàn thành. Và theo dõi các chỉ số kết quả (thành công nhiệm vụ, thời gian làm nhiệm vụ, tỷ lệ lỗi, mức hài lòng) ngay cạnh chỉ số phân phối của bạn.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Nghiên cứu khám phá liên tục | Bắt vấn đề sớm, xây hiểu biết chung | Chi phí liên tục, cần đường ống tuyển người và nhân sự lành nghề |
| Nghiên cứu nặng ban đầu | Hiểu biết sâu trước khi đầu tư lớn | Chậm, có thể trì hoãn việc học mà chỉ phát hành mới hé lộ |
| Quyết định chỉ dựa trên phân tích | Mở rộng được, khách quan, rẻ khi đã đo đạc | Giải thích cái gì nhưng không vì sao; mù với người không dùng và trường hợp biên |
| Persona và bản đồ hành trình | Căn chỉnh nhiều đội về một mô hình người dùng | Cũ đi, có thể thành hư cấu nếu không được làm mới bằng dữ liệu |
| Nhà thiết kế nhúng | Phản hồi nhanh, quyền sở hữu chung | Khó giữ nghề nhất quán qua nhiều đội |

Mọi tổ chức đều cân bằng đầu tư nghiên cứu với tốc độ phân phối. Sai lầm là coi đây là hoặc-cái-này-hoặc-cái-kia. Lập trường hiệu quả là tương xứng: chi nhiều khám phá hơn cho các quyết định tốn kém để đảo ngược (IA lõi, luồng chính, lựa chọn nền tảng), và ít hơn cho các chi tiết bạn có thể dễ đổi sau. Chi phí nghiên cứu hầu như luôn nhỏ so với chi phí xây sai thứ một cách tốt.

## Câu hỏi để thảo luận với đội của bạn

1. **Ai sở hữu kiến trúc thông tin dùng chung và từ vựng có kiểm soát, và điều gì xảy ra khi một đội muốn đi chệch?** Ở quy mô lớn thất bại phổ biến nhất là để mỗi nhóm phơi bày cấu trúc sơ đồ tổ chức và tên riêng của nó cho cùng một khái niệm, nên sản phẩm kết thúc với ba từ cho một thứ và điều hướng phản chiếu phòng ban thay vì nhiệm vụ của người dùng. Hãy quyết định ngay bây giờ liệu IA và từ vựng có do trung tâm sở hữu, suy ra từ phân loại thẻ và kiểm thử cây thay vì chính trị nội bộ, và một đội yêu cầu thay đổi thế nào. Điều này quan trọng hơn trong doanh nghiệp và chính phủ vì người dùng bị giữ chân không thể bỏ đi, nên sự thiếu mạch lạc được trả giá bằng đào tạo, phiếu hỗ trợ và lỗi thay vì rời bỏ. Hãy mang danh sách hiện tại các thuật ngữ trùng lặp và luồng mâu thuẫn làm bằng chứng. Nếu bạn không nêu được tên chủ sở hữu, đó là mục hành động đầu tiên của bạn.

2. **Đường ống tuyển người tham gia nghiên cứu của chúng ta là gì, và nó có với tới người dùng được hỗ trợ số, kém tự tin và phi số không?** Khám phá liên tục chỉ hoạt động nếu bạn có thể gặp người dùng thật mỗi tuần, và những người khó tuyển nhất thường là những người cần dịch vụ nhất: người đang khủng hoảng, dùng thiết bị cũ, hay thường dựa vào sự giúp đỡ. Chỉ kiểm thử những tình nguyện viên tự tin, có kết nối cho bạn một cái đọc dễ chịu nhưng sai, đặc biệt với dịch vụ công nơi công bằng tiếp cận là toàn bộ mục đích. Hãy thống nhất ai chạy việc tuyển người, ưu đãi nào bạn đưa ra, và bạn quan sát các phiên được hỗ trợ số thế nào mà không thêm gánh nặng cho một người dễ tổn thương. Hãy mang nhân khẩu học người tham gia từ ba nghiên cứu gần nhất của bạn và đối chiếu với cơ sở người dùng thực. Nếu chúng lệch về người dùng dễ tiếp cận, hãy sửa đường ống trước khi bạn tin các phát hiện.

3. **Cổng chất lượng UX nào thuộc về định nghĩa hoàn thành của chúng ta, và làm sao ngăn chúng thành sân khấu?** Nhúng nhà thiết kế và nhà nghiên cứu chỉ hoàn vốn nếu nghiên cứu là đầu vào thường trực cho ưu tiên hóa và nếu kiểm tra khả dụng cùng khả năng tiếp cận thực sự chặn một câu chuyện được phát hành, không phải một bộ slide mọi người gật đầu rồi phớt lờ. Hãy chọn các chỉ số kết quả cụ thể bạn sẽ theo dõi cạnh chỉ số phân phối: thành công nhiệm vụ, thời gian làm nhiệm vụ, tỷ lệ lỗi và mức hài lòng. Rủi ro là nghiên cứu được chạy để biện minh cho quyết định đã đưa ra, nên hãy thống nhất ai có thể phủ quyết một lần ra mắt vì cổng UX và bằng chứng nào ghi đè ý kiến của một giám đốc. Hãy mang một tính năng gần đây và hỏi liệu nghiên cứu của nó đã thay đổi quyết định hay chỉ trang trí nó. Nếu phát hiện không bao giờ dịch chuyển lộ trình, cổng của bạn chỉ là hình thức.

4. **Làm sao chúng ta giữ persona, bản đồ hành trình và IA không thoái hóa thành hư cấu khi nghiên cứu tạo ra chúng đã cũ một năm?** Các mô hình dùng chung là thứ cho phép hàng chục đội thiết kế hướng tới một trải nghiệm mạch lạc, nhưng chúng chỉ hoạt động chừng nào còn mô tả người dùng thật, và khoảnh khắc một persona trở thành hiện vật mọi người trích dẫn để thắng tranh luận thay vì bản tóm tắt bằng chứng, nó gây hại tích cực. Hãy quyết định ai sở hữu việc làm mới từng mô hình, theo nhịp nào, và đối chiếu dữ liệu nào (phỏng vấn mới, phân tích, chủ đề hỗ trợ), và thống nhất một ngày "xác thực lần cuối" hiển thị để các mô hình cũ rõ ràng. Cân nhắc đối lập là chi phí: làm mới mọi thứ liên tục là lãng phí, nên hãy gắn tần suất làm mới với tốc độ thay đổi thực của phần cơ sở người dùng hay hành trình đó. Hãy mang nguồn gốc của các persona hàng đầu hiện tại và hỏi mỗi cái được kiểm tra lần cuối với một người dùng thật khi nào. Trong doanh nghiệp và chính phủ, nơi một cơ sở người dùng bị giữ chân hoặc công cộng dịch chuyển chậm nhưng có hệ quả (dân số già đi, một khoản trợ cấp mới, chuyển đổi thiết bị), một mô hình lặng lẽ lỗi thời có thể lái nhiều năm đầu tư hướng tới những người dùng không còn tồn tại.

5. **Khả năng tiếp cận sống ở đâu trong quy trình của chúng ta, và chúng ta có chứng minh được một bản phát hành đáp ứng nó trước khi phát hành thay vì sau một lời phàn nàn không?** Coi khả năng tiếp cận là lượt tuân thủ muộn vừa là thất bại phổ biến nhất vừa là đắt nhất, vì trang bị ngữ nghĩa, thứ tự tiêu điểm và độ tương phản vào một giao diện đã xây tốn nhiều hơn hẳn thiết kế chúng vào. Hãy quyết định tiêu chuẩn nào bạn giữ mình theo (ví dụ WCAG, Hướng dẫn Khả năng Tiếp cận Nội dung Web), liệu sự phù hợp có là cổng chặn trong định nghĩa hoàn thành, và ai chịu trách nhiệm khi một tính năng không tiếp cận được đến môi trường thực. Căng thẳng là tốc độ so với hòa nhập, và các đội dưới áp lực hạn chót sẽ lặng lẽ bỏ các kiểm tra không được thực thi. Hãy mang cuộc kiểm toán gần nhất của bạn, độ bao phủ tự động và thủ công đằng sau nó, và số vấn đề khả năng tiếp cận tìm thấy sau phát hành thay vì trước. Với chính phủ đặc biệt đây không phải phép lịch sự tùy chọn: nó thường là nghĩa vụ pháp lý và vấn đề công bằng, vì một dịch vụ công loại trừ người khuyết tật hay được hỗ trợ số đã thất bại ở mục đích cốt lõi, không phải mục đích phụ.

6. **Khi phân tích và nghiên cứu định tính của chúng ta bất đồng, chúng ta quyết định tin cái nào thế nào, và ai phân xử?** Các tổ chức lớn tích lũy cả bảng điều khiển cho thấy hàng nghìn người dùng làm gì lẫn các cuộc phỏng vấn giải thích vì sao một nhúm người hành xử như vậy, và hai thứ sẽ thường xuyên chỉ về hướng đối nghịch: một luồng có tỷ lệ hoàn thành cao mà lặng lẽ làm nhục mọi người, hay một tính năng người dùng khen trong các phiên nhưng không bao giờ chạm vào ở quy mô lớn. Hãy thống nhất từ trước cách bạn đối chiếu chéo, phương pháp nào được tin để trả lời câu hỏi nào (phân tích cho độ lớn và tầm với, nghiên cứu cho nguyên nhân và ý nghĩa), và ai có thẩm quyền quyết định khi chúng xung đột. Rủi ro là chọn lọc nguồn nào tâng bốc kế hoạch đã chọn. Hãy mang một bất đồng gần đây cụ thể và đi qua cách nó thực sự được giải quyết. Trong bối cảnh doanh nghiệp và công, rủi ro bị sắc nét hơn vì phân tích đếm thiếu một cách có hệ thống chính những người quan trọng nhất: người không dùng, người bỏ dở, và người dùng công nghệ hỗ trợ hiếm khi hiện ra trong phễu, nên chỉ tin con số có thể khiến những người bị loại trừ vô hình.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Bạn không có nhà nghiên cứu và không có thời gian cho kho lưu trữ, nên hãy biến nghiên cứu thành thói quen của người sáng lập: ngồi cạnh năm người dùng thật trong một buổi chiều trước khi xây thứ kế tiếp. Bỏ qua persona và bản đồ hành trình chính thức; một hiểu biết chung về công việc duy nhất bạn đang giải quyết, được làm mới bằng việc xem người ta hằng tuần, thắng tài liệu không ai duy trì. Lợi thế của bạn là cả đội có thể hấp thụ một hiểu biết ngay ngày nó xuất hiện, vì vậy hãy bảo vệ tốc độ đó và cưỡng lại nghi lễ.

**Doanh nghiệp nhỏ.** Không có chuyên gia UX và ngân sách eo hẹp, hãy dựa vào những quy ước người dùng của bạn đã biết thay vì phát minh riêng, và mua công cụ với mặc định hợp lý thay vì thiết kế luồng từ đầu. Hãy tự làm nghiên cứu rẻ, giá trị cao: một nhúm phiên kiểm thử khả dụng qua cuộc gọi video và đọc các phiếu hỗ trợ của bạn sẽ phơi bày hầu hết vấn đề nghiêm trọng. Hãy coi những điều cơ bản về khả năng tiếp cận (độ tương phản, nhãn, truy cập bàn phím) là điều kiện tối thiểu bạn có được từ một thư viện thành phần tốt hơn là một dự án bạn bố trí nhân sự.

**Doanh nghiệp lớn.** Vấn đề cốt lõi là sự mạch lạc qua nhiều đội, vì vậy hãy đầu tư vào nền tảng dùng chung: persona có chủ sở hữu, bản đồ hành trình được duy trì, một từ vựng có kiểm soát, và một kiến trúc thông tin có tài liệu mà các nhóm thiết kế hướng tới thay vì đi vòng. Hãy nhúng nhà thiết kế và nhà nghiên cứu vào các đội phân phối, nhưng quản trị nghề tập trung để sản phẩm không vỡ thành các phương ngữ không nhất quán. Hãy tài trợ một kho nghiên cứu và cổng chất lượng trong định nghĩa hoàn thành, và theo dõi chỉ số kết quả UX như một danh mục để không đội nào tối ưu cục bộ làm suy giảm tổng thể.

**Chính phủ.** Khả năng tiếp cận và công bằng tiếp cận là nghĩa vụ, không phải sở thích, vì vậy hãy giữ các bản phát hành theo một tiêu chuẩn đã công bố và nghiên cứu với toàn dải công chúng, bao gồm người dùng được hỗ trợ số, kém tự tin và phi số. Mua sắm và minh bạch định hình phân phối: công bố nguyên tắc thiết kế và phương pháp nghiên cứu của bạn, cấu trúc dịch vụ quanh các sự kiện cuộc sống của công dân thay vì phòng ban nội bộ, và giữ bằng chứng kiểm thử cho kiểm toán. Vì người dùng thường không có nhà cung cấp thay thế, một luồng họ không thể hoàn thành là từ chối một dịch vụ, nên hãy coi việc hoàn thành bởi người dùng khó tiếp cận nhất là thước đo thành công thực.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người xây công cụ lập lịch cho phòng khám nhỏ có quan điểm mạnh về điều lễ tân cần, nhưng không có bằng chứng. Trước khi viết thêm tính năng, những người sáng lập ngồi cạnh năm lễ tân mỗi người một buổi chiều và xem họ làm việc. Họ biết rằng nỗi đau thực không phải tốc độ đặt lịch mà là việc đặt trùng do một giao diện lịch gây rối, điều không ai nghĩ đến nhắc trong các cuộc gọi bán hàng trước. Đóng khung lại sản phẩm quanh công việc duy nhất đó, và phác thảo cùng kiểm thử các bản sửa với cùng năm người trong một tuần, biến một bản dùng thử đang chững lại thành những khách hàng trả tiền đầu tiên của họ.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia hợp nhất bảy công cụ khởi tạo khoản vay nội bộ theo khu vực thành một nền tảng. Thay vì gộp các tập tính năng, đội chạy lập bản đồ hành trình và thiết kế bản thiết kế dịch vụ với các thẩm định viên qua các khu vực. Họ thấy rằng "khác biệt khu vực" mà ai cũng giả định phần lớn là thuật ngữ không nhất quán và thứ tự màn hình, không phải khác biệt quy trình thực sự. Một IA thống nhất và từ vựng chung cắt đáng kể thời gian đào tạo thẩm định viên và giảm lỗi xử lý, vì nhân viên giờ chia sẻ một mô hình tinh thần.

**Chính phủ.** Một cơ quan thuế quốc gia thiết kế lại dịch vụ khai thuế trực tuyến chạy kiểm thử khả dụng có điều phối với người nộp thuế trải qua các độ tuổi, thiết bị và mức tự tin về số, cộng quan sát được hỗ trợ số với những người thường dựa vào sự giúp đỡ. Kiểm thử cho thấy tiêu đề mục đầy biệt ngữ khiến người ta bỏ dở hoặc khai sai. Đóng khung lại nội dung quanh công-việc-cần-làm của người nộp thuế, và tái cấu trúc IA quanh các sự kiện cuộc sống thay vì mã thuế nội bộ, tăng tỷ lệ hoàn thành tự phục vụ thành công và giảm lượng cuộc gọi tổng đài, trực tiếp hạ chi phí phục vụ trong khi cải thiện công bằng tiếp cận.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của UX đến từ ba đòn bẩy: thành công nhiều hơn (nhiều người dùng hoàn thành nhiệm vụ có giá trị hơn), chi phí phục vụ thấp hơn (ít liên hệ hỗ trợ, ít đào tạo, ít lỗi hơn), và ít làm lại hơn (bắt hướng sai trước khi chúng được xây). Trong các bối cảnh doanh nghiệp nơi người dùng bị giữ chân, phần thưởng hiện ra dưới dạng năng suất và ít lỗi hơn là chuyển đổi; vài giây tiết kiệm mỗi giao dịch, qua hàng nghìn nhân viên, cộng dồn thành khoản tiết kiệm hằng năm lớn.

Tổng chi phí sở hữu phải cân nhắc chi phí áp dụng so với chi phí không áp dụng. Chi phí áp dụng dễ thấy: nhà nghiên cứu và nhà thiết kế, tuyển người và ưu đãi cho người tham gia, công cụ, và thời gian trong lịch trình. Chi phí của việc không áp dụng lớn hơn nhưng khó nhận ra hơn: giao dịch bị bỏ dở, chi phí chung về hỗ trợ và đào tạo, thiết kế lại muộn tốn kém, ra mắt thất bại, và rủi ro danh tiếng hay pháp lý khi dịch vụ công loại trừ mọi người. Vì những chi phí này trải qua ngân sách hỗ trợ, đào tạo và vận hành thay vì dòng sản phẩm, ban lãnh đạo thường đánh giá thấp chúng.

Để trình bày lập luận với ban lãnh đạo, hãy gắn UX với các chỉ số mà giám đốc đã theo dõi: tỷ lệ hoàn thành và chuyển đổi, chi phí mỗi giao dịch, khối lượng phiếu hỗ trợ, ngày đào tạo, và tỷ lệ lỗi và làm lại. Hãy chạy một thí điểm nhỏ, có đo đạc cho thấy một trước-và-sau đo được, rồi ngoại suy qua danh mục. Đóng khung nghiên cứu là giảm rủi ro trên các quyết định không thể đảo ngược thường gây tiếng vang với tài chính và các bên liên quan quản trị.

## Phản mẫu và cạm bẫy

- **Thiết kế do HiPPO dẫn dắt**: quyết định được đưa ra bởi ý kiến của người được trả lương cao nhất thay vì bằng chứng.
- **Sân khấu nghiên cứu**: các nghiên cứu được chạy để biện minh cho quyết định đã đưa ra, phát hiện bị phớt lờ.
- **Persona như hư cấu**: hồ sơ được bịa ra không bao giờ xác thực với người dùng thật, được dùng để thắng tranh luận.
- **Sơ đồ tổ chức như IA**: điều hướng phản chiếu phòng ban nội bộ thay vì nhiệm vụ của người dùng.
- **Nghiên cứu nổ lớn**: các nghiên cứu hiếm, đắt đến quá muộn để thay đổi bất cứ điều gì.
- **Chỉ kiểm thử đường hạnh phúc**: bỏ qua trạng thái lỗi, trường hợp biên và người dùng dưới căng thẳng.
- **Thiết kế như lớp sơn cuối**: chỉ đưa UX vào để làm một bản dựng đã hoàn tất "trông đẹp."
- **Bỏ qua người dùng được hỗ trợ và phi số**: chỉ thiết kế cho người dùng tự tin, có kết nối.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Không có thực hành UX riêng. Quyết định được đưa ra bằng ý kiến và trực giác của người được trả lương cao nhất. Nghiên cứu, nếu có, là tùy nghi và phản ứng, được kích hoạt bởi một lần ra mắt đã tệ. Luồng và thuật ngữ không nhất quán qua các đội, và không ai sở hữu trải nghiệm tổng thể.

**Mức 2: Phát triển.** Một số đội có nhà thiết kế và chạy kiểm thử khả dụng thỉnh thoảng, và một vài persona hay bản đồ hành trình tồn tại, nhưng thực hành khác nhau nhiều giữa các nhóm và không được duy trì. UX được coi là một giai đoạn thay vì một kỷ luật liên tục, và thường bị bỏ qua dưới áp lực lịch trình. Công việc tốt xảy ra ở từng mảng nhưng không cộng lại qua sản phẩm.

**Mức 3: Chuẩn hóa.** Nghiên cứu hỗn hợp phương pháp liên tục nuôi ưu tiên hóa, và persona dùng chung, bản đồ hành trình, và một IA từ vựng có kiểm soát được lập tài liệu và dùng qua các đội. Cổng chất lượng UX, bao gồm chuẩn khả dụng và kiểm tra khả năng tiếp cận, nằm trong định nghĩa hoàn thành và được thực thi toàn tổ chức. Một kho nghiên cứu tìm kiếm được giữ hiểu biết tái sử dụng được thay vì mắc kẹt trong slide của một nhóm.

**Mức 4: Quản lý.** Thực hành được đo theo đường cơ sở thay vì chỉ được thực hiện. Bạn theo dõi thành công nhiệm vụ, thời gian làm nhiệm vụ, tỷ lệ lỗi, mức hài lòng, và sự phù hợp khả năng tiếp cận như các chỉ số đã thống nhất, đặt mục tiêu, và theo dõi chúng qua các bản phát hành. Mẫu người tham gia nghiên cứu được đối chiếu với cơ sở người dùng thực để phát hiện mang tính đại diện, cổng chất lượng báo cáo tỷ lệ đạt thay vì ý kiến, và chi phí nghiên cứu được cân nhắc so với mức giảm đo được trong liên hệ hỗ trợ, đào tạo và làm lại. Quyết định phát hành hay giữ dựa trên bằng chứng đối chiếu các đường cơ sở đó.

**Mức 5: Điều phối.** Nghiên cứu là liên tục, gắn với kết quả, và tích hợp với hoạch định sản phẩm, kinh doanh và rủi ro trong toàn tổ chức. Các đội chạy thí nghiệm có kiểm soát, khép vòng từ hiểu biết đến thay đổi được phát hành đến hiệu ứng đo được, và loại bỏ hoặc điều chỉnh phạm vi các mô hình người dùng khi quần thể và hành trình của nó dịch chuyển. Nền tảng UX thích ứng liên tục: persona, hành trình, IA và tiêu chuẩn được làm mới dựa trên bằng chứng, và tổ chức cân bằng lại nơi nó đầu tư khám phá khi khả năng đảo ngược và rủi ro thay đổi.

## Ý tưởng để thảo luận

- Bao nhiêu khám phá là "đủ" trước khi cam kết với một hướng, và ai quyết định?
- Làm sao bạn giữ persona và bản đồ hành trình sống thay vì để chúng thành hiện vật cũ?
- Khi phân tích định lượng và nghiên cứu định tính bất đồng, bạn tin cái nào và vì sao?
- Một tổ chức lớn nên cân bằng tiêu chuẩn UX trung tâm với quyền tự chủ của từng đội thế nào?
- Cách đúng để nghiên cứu các dịch vụ được dùng bởi người đang khủng hoảng mà không thêm gánh nặng cho họ là gì?
- Làm sao bạn đo ROI của nghiên cứu ngăn một sai lầm mà vì thế bạn không bao giờ mắc?

## Những điểm cần ghi nhớ

- UX là một cách làm việc từ đầu, không phải trang trí ở cuối.
- Kết hợp phương pháp định tính (vì sao) với phương pháp định lượng (bao nhiêu).
- Mô hình hóa người dùng bằng persona dựa trên bằng chứng, bản đồ hành trình, công-việc-cần-làm và bản thiết kế dịch vụ.
- Cấu trúc thông tin quanh mô hình tinh thần của người dùng, không phải sơ đồ tổ chức.
- Coi tư duy thiết kế là một tư duy thực dụng với các vòng học chặt, không phải một quy trình cứng nhắc.
- Chi phí nghiên cứu nhỏ so với chi phí xây sai thứ.
- Trong doanh nghiệp và chính phủ, chất lượng UX chuyển trực tiếp thành năng suất, chi phí phục vụ và công bằng tiếp cận.

## Tài liệu tham khảo và đọc thêm

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville và Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen và cộng sự, *Competing Against Luck* (công-việc-cần-làm)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* và *Design Principles*
- U.S. General Services Administration, *18F Methods* và hướng dẫn nghiên cứu *U.S. Web Design System*
- Nielsen Norman Group, các bài viết và báo cáo về phương pháp nghiên cứu
