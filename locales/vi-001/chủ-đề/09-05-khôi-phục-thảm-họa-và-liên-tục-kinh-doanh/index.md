# 9.5 Khôi phục thảm họa và liên tục kinh doanh

## Tổng quan và động lực

Sớm hay muộn, một điều bạn không lên kế hoạch sẽ làm sập một hệ thống: ngừng hoạt động đám mây toàn khu vực, một lệnh `DROP TABLE` gõ nhầm, một trận lụt ở trung tâm dữ liệu, một vụ ransomware phát nổ, hay một nhà cung cấp biến mất qua đêm. Câu hỏi không bao giờ là gián đoạn có đến không, mà là bạn phục hồi nhanh đến đâu và mất bao nhiêu trong quá trình. Chương này nói về việc sẵn sàng cho ngày tồi tệ trước khi nó đến.

Hai kỷ luật trả lời sự sẵn sàng đó, và chúng không giống nhau. [Hoạch định liên tục kinh doanh](https://en.wikipedia.org/wiki/Business_continuity_planning) (BCP) giữ toàn bộ tổ chức hoạt động qua một gián đoạn: con người, văn phòng, truyền thông, lương, và các quy trình kinh doanh trọng yếu mà khách hàng phụ thuộc. [Khôi phục thảm họa](https://en.wikipedia.org/wiki/Disaster_recovery) (DR) là công việc kỹ thuật hẹp hơn của việc khôi phục hệ thống CNTT và dữ liệu sau khi chúng hỏng. Liên tục là mục tiêu; khôi phục là một trong các phương tiện. Bạn có thể khôi phục mọi máy chủ mà vẫn làm khách hàng thất vọng nếu không ai biết ai được phép tuyên bố thảm họa hay cách liên lạc với họ. Chương này coi DR là thực hành kỹ thuật và BCP là khung kinh doanh nó phục vụ.

Với các đội lớn, rủi ro mở rộng cùng bạn. Một doanh nghiệp mang nghĩa vụ phục hồi theo quy định, dấu chân đa khu vực, và rủi ro tập trung ở một nhúm nhà cung cấp. Chính phủ mang nghĩa vụ pháp lý duy trì các chức năng thiết yếu cho công dân, được mã hóa thành liên tục hoạt động. Cả hai vận hành dưới sự soi xét nơi một kế hoạch chưa kiểm thử là khoản nợ bạn sẽ phát hiện vào lúc tệ nhất có thể. Khôi phục là nơi độ tin cậy (chương 9.1) và ứng phó sự cố (chương 9.3) gặp câu hỏi khó hơn về việc sống sót những thất bại bạn không thiết kế tránh được.

## Các nguyên tắc chính

- **Liên tục rộng hơn khôi phục.** Khôi phục máy chủ không giống với giữ doanh nghiệp chạy.
- **Hai con số điều khiển mọi thứ.** Mục tiêu thời gian phục hồi (RTO) và mục tiêu điểm phục hồi (RPO), đặt từ tác động kinh doanh, định cỡ mọi quyết định.
- **Bản sao lưu chưa kiểm thử không phải bản sao lưu.** Một lần khôi phục bạn chưa bao giờ thực hiện là hy vọng, không phải năng lực.
- **Giả định bản sao lưu là mục tiêu.** Ransomware săn bản sao lưu của bạn trước, nên giữ các bản sao bất biến và ngoại tuyến.
- **Dựng lại từ mã, không phải từ trí nhớ.** Nếu bạn không tạo lại được hạ tầng từ nguồn, bạn không khôi phục nó đáng tin được.
- **Vẽ bản đồ những gì bạn phụ thuộc.** Bạn chỉ khôi phục nhanh bằng phụ thuộc thượng nguồn chậm nhất của mình.
- **Đo khôi phục như bất kỳ hệ thống nào khác.** RTO và RPO thực từ các buổi diễn tập thật, không phải con số bạn viết trên slide.

## Khuyến nghị

### Đặt RTO và RPO từ phân tích tác động kinh doanh

Mọi quyết định khôi phục xuất phát từ hai con số, nên hãy làm đúng chúng trước. **Mục tiêu thời gian phục hồi (RTO)** là một hệ thống có thể ngừng bao lâu trước khi tác hại không chấp nhận được. **Mục tiêu điểm phục hồi (RPO)** là bạn chịu mất bao nhiêu dữ liệu, đo bằng tuổi của bản sao tốt gần nhất bạn khôi phục về được. Một sổ cái thanh toán có thể đòi RTO vài phút và RPO gần bằng không; một bảng điều khiển phân tích nội bộ có thể chịu một ngày mỗi thứ. Bạn không đặt được những thứ này trong kỹ thuật. Hãy suy ra chúng từ một [phân tích tác động kinh doanh](https://en.wikipedia.org/wiki/Business_impact_analysis) (BIA) xếp hạng quy trình kinh doanh theo chi phí gián đoạn của chúng và truy mỗi cái về hệ thống và dữ liệu nó cần. Mục tiêu chặt hơn tốn hơn, nên BIA là thứ ngăn bạn mạ vàng một dịch vụ tầm thường và bảo vệ thiếu một dịch vụ trọng yếu.

### Làm sao lưu đúng: quy tắc 3-2-1, bất biến và kiểm thử

Sao lưu là sàn bên dưới mọi chiến lược khôi phục, và hầu hết tổ chức làm chúng tệ hơn họ nghĩ. Hãy theo kỷ luật [sao lưu](https://en.wikipedia.org/wiki/Backup) gọi là **quy tắc 3-2-1**: giữ ít nhất ba bản sao dữ liệu, trên hai phương tiện hoặc hệ thống khác nhau, với một bản sao ngoài địa điểm. Mối đe dọa hiện đại thêm hai yêu cầu nữa. Giữ ít nhất một bản sao **bất biến** (ghi một lần, không xóa được trong một cửa sổ lưu giữ) và lý tưởng là **ngoại tuyến hoặc cách ly không khí**, vì ransomware nay cố ý mã hóa hoặc xóa các bản sao lưu với tới được trước khi nó tự báo hiệu. Trên hết, hãy kiểm thử khôi phục theo lịch. Một bản sao lưu chưa kiểm thử không phải bản sao lưu, mà là một giả định chưa kiểm thử, và những thất bại bạn tìm thấy trong buổi diễn tập (kho lưu trữ hỏng, thiếu khóa mã hóa, sao lưu nhầm ổ) chính là những cái sẽ kết liễu bạn trong sự kiện thật.

### Chọn chiến lược DR dọc theo phổ chi phí-so-với-tốc-độ

Các chiến lược DR đánh đổi tiền lấy tốc độ khôi phục, và bạn nên chọn theo từng hệ thống dựa trên RTO và RPO của nó thay vì mua một bậc cho mọi thứ. Bốn mẫu neo phổ. **Sao lưu và khôi phục** rẻ nhất và chậm nhất: bạn dựng lại từ bản sao lưu khi thảm họa ập đến, với RTO hàng giờ đến hàng ngày. **Đèn mồi** giữ một lõi tối thiểu (cơ sở dữ liệu sao chép, cấu hình lõi tại chỗ) ấm nhưng thu nhỏ, sẵn sàng mở rộng. **Dự phòng ấm** chạy một bản sao luôn bật nhỏ hơn của toàn bộ ngăn xếp mà bạn mở rộng khi chuyển dự phòng, cắt RTO xuống vài phút. **Đa địa điểm chủ động-chủ động** chạy năng lực đầy đủ ở hai hoặc nhiều địa điểm phục vụ lưu lượng trực tiếp, cho RTO gần bằng không với chi phí và độ phức tạp cao nhất. Hãy khớp bậc với con số doanh nghiệp đã ký duyệt, và đừng trả giá chủ động-chủ động cho một hệ thống chịu được đèn mồi.

### Sao chép dữ liệu với đánh đổi nhất quán trong tâm trí

Tốc độ khôi phục phụ thuộc vào dữ liệu dự phòng của bạn hiện hành đến đâu, và ở đây bạn thừa hưởng các bài toán khó của [hệ phân tán](https://en.wikipedia.org/wiki/Distributed_computing) (chương 3.3). **Sao chép đồng bộ** xác nhận mọi lần ghi ở địa điểm thứ hai trước khi báo nhận, cho RPO gần bằng không với cái giá độ trễ ghi thêm và giới hạn cứng về khoảng cách. **Sao chép bất đồng bộ** báo nhận cục bộ và gửi thay đổi sau, nên nhanh và linh hoạt về địa lý nhưng để lại cửa sổ trễ sao chép mà bạn sẽ mất khi chuyển dự phòng. Không có lựa chọn miễn phí: nhất quán mạnh hơn tốn độ trễ, nhất quán yếu hơn tốn dữ liệu. Hãy quyết định theo từng kho dữ liệu từ RPO của nó, và biết độ trễ sao chép điển hình của bạn, vì độ trễ đó là RPO thực của bạn vào ngày tồi tệ, không phải con số trong tài liệu thiết kế.

### Dựng lại từ mã với hạ tầng dưới dạng mã

Bạn không khôi phục đáng tin được một môi trường bạn cung cấp bằng tay, vì không ai nhớ mọi cú nhấp. Hãy định nghĩa môi trường của bạn như [hạ tầng dưới dạng mã](https://en.wikipedia.org/wiki/Infrastructure_as_code) (chương 8.2) để cả ngăn xếp tạo lại được từ nguồn có quản lý phiên bản ở trạng thái tốt đã biết. Điều này biến khôi phục từ dự án khảo cổ thành một lần chạy đường ống lặp lại được, giữ khu vực dự phòng của bạn trung thực (nó trôi ít hơn khi cả hai được xây từ cùng mã), và cho bạn cách sạch để dựng hạ tầng khôi phục trong một tài khoản hay khu vực mới sau khi bị xâm phạm. Lưu mã, tham chiếu bí mật và sổ tay vận hành ở nơi sống sót qua việc mất môi trường chính.

### Vẽ bản đồ phụ thuộc trước khi bạn cần chúng

Hệ thống hỏng thành mạng lưới, không phải cô lập, và khôi phục đình trệ ở phụ thuộc bạn đã quên. Hãy lập bản đồ mỗi hệ thống trọng yếu cần gì để hoạt động: dịch vụ thượng nguồn, DNS, định danh và xác thực, tổ chức cấp chứng chỉ, hàng đợi thông điệp, và API cùng nhà cung cấp SaaS bên thứ ba. Ghi chú thứ tự khôi phục, vì dựng một ứng dụng lên trước cơ sở dữ liệu hay nhà cung cấp định danh của nó chỉ tạo ra lần ngừng hoạt động thứ hai. Đặc biệt chú ý nhà cung cấp bên ngoài, vì khôi phục của bạn bị chặn trên bởi của họ và bạn có thể không nhìn thấy nó. Việc lập bản đồ này gắn trực tiếp với khả năng phục hồi và suy giảm êm (chương 3.5): càng ít phụ thuộc cứng một hệ thống có, nó trở lại càng nhanh.

### Kiểm thử khôi phục như một thực hành, không phải một sự kiện

Một kế hoạch DR bạn chưa thực hành là hư cấu. Hãy xây một bậc thang kiểm thử. Một **bài tập bàn giấy** dẫn đội qua một kịch bản trên giấy để tìm khoảng trống về vai trò, quyết định và truyền thông. Một **ngày diễn tập** tiêm một thất bại có kiểm soát thật vào môi trường giống thật. Một **buổi diễn tập chuyển dự phòng đầy đủ** thực sự chuyển sang địa điểm khôi phục và chạy trên đó. Hãy chạy chúng theo nhịp, luân phiên kịch bản (gồm mất một người then chốt hoặc nhà cung cấp), và đo kết quả: nắm bắt **RTO và RPO thực** bạn đạt được và so sánh với mục tiêu. Khoảng cách giữa khôi phục đo được và đã hứa là chỉ số độ tin cậy trung thực nhất bạn sở hữu, và đóng nó là toàn bộ ý nghĩa của buổi diễn tập.

### Lên kế hoạch khôi phục mạng như một kịch bản riêng

Ransomware và tấn công mạng phá hủy phá vỡ các giả định của DR thông thường, nên hãy xử lý chúng riêng. Trong thiên tai dữ liệu của bạn còn nguyên ở nơi khác; trong một sự kiện [ransomware](https://en.wikipedia.org/wiki/Ransomware) dữ liệu và thường cả bản sao lưu của bạn là vũ khí, và môi trường khôi phục của bạn có thể tự nó bị xâm phạm. Hãy lên kế hoạch **khôi phục phòng sạch**: một môi trường cô lập, đáng tin nơi bạn khôi phục từ bản sao bất biến, quét tìm xâm nhập, và dựng lại định danh cùng thông tin xác thực trước khi nối lại bất cứ thứ gì. Biết bản sao lưu nào là điểm sạch cuối cùng đã biết của bạn, và kỳ vọng việc tìm nó tốn thời gian pháp y mà RTO thông thường của bạn chưa bao giờ lập ngân sách. Đây là nơi các bản sao bất biến, ngoại tuyến xứng đáng với chi phí, và nó gắn chặt với quản lý sự cố (chương 9.3) và với nghĩa vụ tuân thủ và quản trị cho xử lý vi phạm (chương 4.6).

## Đánh đổi: ưu và nhược điểm

| Chiến lược DR | Ưu điểm | Nhược điểm |
|---|---|---|
| Sao lưu và khôi phục | Rẻ nhất; đơn giản; chi phí liên tục thấp | RTO chậm (hàng giờ đến hàng ngày); RPO lớn hơn |
| Đèn mồi | Chi phí thấp; dữ liệu lõi ấm và sẵn sàng | Mở rộng thủ công; khôi phục vẫn tốn thời gian thực |
| Dự phòng ấm | RTO nhanh (vài phút); ngăn xếp đầy đủ đã chứng minh | Chi phí liên tục của môi trường thứ hai đang chạy |
| Đa địa điểm chủ động-chủ động | RTO gần bằng không; không thất bại một địa điểm | Chi phí và độ phức tạp cao nhất; nhất quán khó |
| Sao chép đồng bộ | RPO gần bằng không | Độ trễ ghi; giới hạn khoảng cách; ghép chặt hơn |
| Sao chép bất đồng bộ | Nhanh, linh hoạt, tự do về địa lý | Cửa sổ mất dữ liệu bằng độ trễ sao chép |

Căng thẳng trung tâm là tốc độ khôi phục và độ mới dữ liệu đều tốn tiền và độ phức tạp, và không cái nào miễn phí ở bất kỳ bậc nào. Hãy giải quyết theo từng hệ thống thay vì theo từng tổ chức: để phân tích tác động kinh doanh giao cho mỗi hệ thống trọng yếu một RTO và RPO, rồi mua chính xác chiến lược đáp ứng nó. Tiêu tiền chủ động-chủ động cho một công cụ báo cáo bỏ đói sổ cái cần nó, và ngược lại là cẩu thả. Kỷ luật là khớp chi tiêu với con số mà doanh nghiệp sở hữu, và xem xét lại sự khớp đó khi tầm quan trọng của hệ thống đổi.

## Câu hỏi để thảo luận với đội của bạn

1. **RTO và RPO cho từng hệ thống trọng yếu của bạn là gì, và ai trong doanh nghiệp đã ký duyệt chúng?** Nếu kỹ thuật tự bịa những con số này, chúng là đoán mò, và đoán mò được tài trợ hoặc quá hào phóng hoặc hoàn toàn không. Mục tiêu thời gian phục hồi và điểm phục hồi nên rơi ra từ một phân tích tác động kinh doanh xếp hạng quy trình theo chi phí gián đoạn của chúng, để sổ cái nhận vài phút và wiki nội bộ nhận một ngày. Hãy mang phân bậc hiện tại của bạn và hỏi liệu người chịu trách nhiệm cho từng quy trình kinh doanh có thực sự chấp nhận mất dữ liệu và thời gian ngừng mà bạn đã thiết kế. Trong một tổ chức lớn cuộc trò chuyện này ngăn sai lầm đắt đỏ của việc bảo vệ mọi thứ như nhau, vốn bảo vệ không gì tốt. Nếu không ai ngoài kỹ thuật nêu được các con số, bạn chưa có mục tiêu, bạn có hy vọng.

2. **Lần cuối bạn thực hiện một lần khôi phục thật là khi nào, và bạn có đo RTO cùng RPO thực mình đạt được không?** Một bản sao lưu bạn chưa bao giờ khôi phục là giả định chưa kiểm thử, và các kiểu thất bại giết bạn (kho lưu trữ hỏng, mất khóa mã hóa, ảnh chụp nhầm ổ, một phụ thuộc không chịu lên) chỉ nổi lên khi bạn thử. Hãy mang ngày và kết quả của buổi diễn tập chuyển dự phòng đầy đủ gần nhất của bạn, không phải bài tập bàn giấy gần nhất, và khoảng cách giữa khôi phục bạn đạt và khôi phục bạn hứa. Với một đội lớn, một lần khôi phục thành công của một hệ thống không chứng minh các hệ thống khác, nên hãy hỏi phần nào của hệ thống trọng yếu đã được khôi phục đầu-đến-cuối trong năm qua. Khoảng cách đo được là con số độ tin cậy trung thực nhất của bạn, và nếu bạn không nêu được, kế hoạch của bạn là hư cấu cho đến khi được chứng minh.

3. **Nếu ransomware mã hóa môi trường sản xuất của bạn và chạm đến bản sao lưu tối nay, bản sao sạch cuối cùng đã biết của bạn là gì và bạn sẽ dựng lại ở đâu?** Khôi phục thảm họa thông thường giả định dữ liệu của bạn an toàn ở nơi khác, và một cuộc tấn công mạng phá hủy phá vỡ chính giả định đó bằng cách biến dữ liệu và bản sao lưu của bạn thành vũ khí. Hãy hỏi liệu ít nhất một bản sao lưu có bất biến và ngoại tuyến, bạn sẽ xác định điểm khôi phục sạch cuối cùng thế nào, và một môi trường phòng sạch đáng tin sẽ đến từ đâu khi chính môi trường sản xuất bị xâm phạm. Kịch bản này cần thời gian pháp y mà RTO bình thường của bạn không lập ngân sách, nên hãy mang ước tính trung thực việc tìm một điểm sạch thực sự mất bao lâu. Với các đội doanh nghiệp và chính phủ đây cũng là sự kiện tuân thủ (chương 4.6) với đồng hồ thông báo vi phạm chạy song song. Nếu câu trả lời là "chúng tôi sẽ khôi phục bản sao lưu mới nhất," bạn hoàn toàn chưa lên kế hoạch cho điều này.

4. **Hệ thống nào của bạn đang trả cho một bậc khôi phục mà phân tích tác động kinh doanh của nó không biện minh, và hệ thống nào được bảo vệ thiếu một cách nguy hiểm?** Tốc độ khôi phục và độ mới dữ liệu đều tốn tiền ở mọi bậc, nên một chính sách đại trà hoặc lãng phí ngân sách chủ động-chủ động cho công cụ báo cáo hoặc bỏ đói sổ cái thực sự cần. Lực kéo đối lập là thật: một bậc tiêu chuẩn đơn giản hơn nhiều cho nhiều đội vận hành, trong khi phân bậc theo từng hệ thống khớp chi tiêu với giá trị nhưng đòi chọn lọc liên tục khi tầm quan trọng của hệ thống dịch chuyển. Hãy mang chiến lược DR hiện tại cho từng hệ thống trọng yếu, RTO và RPO nó nhắm tới, chi phí hằng tháng của dự phòng và sao chép, và ngày phân bậc được xem lại lần cuối so với một phân tích tác động mới. Trong bối cảnh doanh nghiệp hay chính phủ một bậc không khớp nhân lên qua các khu vực và kiểm toán sẽ yêu cầu bạn biện minh cả tiền bạn chi lẫn phơi nhiễm bạn chấp nhận, nên một hóa đơn chủ động-chủ động không giải thích được và một dịch vụ trọng yếu không được bảo vệ đều khó bảo vệ như nhau.

5. **Bạn có thực sự biết thứ tự khôi phục các hệ thống trọng yếu của mình, và khôi phục của bạn phụ thuộc bao nhiêu vào những nhà cung cấp bạn không kiểm thử được?** Hệ thống hỏng thành mạng lưới, không phải cô lập, và khôi phục đình trệ ở phụ thuộc không ai lập bản đồ: dựng một ứng dụng lên trước cơ sở dữ liệu, nhà cung cấp định danh hay DNS của nó và bạn chỉ tạo ra lần ngừng hoạt động thứ hai. Lập bản đồ phụ thuộc tẻ nhạt và bản đồ cũ đi, nhưng lựa chọn thay thế là phát hiện thứ tự khôi phục trực tiếp trong lúc chuyển dự phòng, và rủi ro tập trung ở một nhúm nhà cung cấp SaaS vẫn vô hình cho đến khi họ cùng hỏng và chặn trên khôi phục của bạn bằng của họ. Hãy mang bản đồ phụ thuộc hiện tại, trình tự khôi phục có tài liệu, và danh sách nhà cung cấp bên ngoài với cam kết khôi phục họ nêu và liệu bạn đã bao giờ xác thực cái nào. Với một tổ chức lớn hay công, tính liên tục của nhà cung cấp và rủi ro tập trung ngày càng là mối quan tâm mua sắm và quy định, nên những nghĩa vụ khôi phục đó thuộc về hợp đồng dưới dạng bạn kiểm toán được thay vì trong quảng cáo của nhà bán hàng.

6. **Nếu bạn khôi phục mọi máy chủ tối nay, doanh nghiệp có thực sự tiếp tục chạy không, và ai được ủy quyền tuyên bố thảm họa?** Khôi phục thảm họa khôi phục CNTT, nhưng liên tục kinh doanh giữ tổ chức hoạt động: con người, truyền thông, lương, và các quyết định phụ thuộc vào việc ai đó có thẩm quyền đưa ra. Bạn có thể khôi phục mọi hệ thống và vẫn làm khách hàng thất vọng nếu không ai biết ai có thể tuyên bố thảm họa hay cách liên lạc nhân viên khi các kênh bình thường cũng sập. Kỹ thuật sở hữu khôi phục, nhưng liên tục trải qua cơ sở vật chất, nhân sự, truyền thông và kế nhiệm lãnh đạo, và những đường nối giữa các phòng ban đó chính là nơi một kế hoạch lặng lẽ mục rữa. Hãy mang thẩm quyền tuyên bố và chuỗi leo thang, kế hoạch truyền thông dự phòng, người kế nhiệm có tên và cơ sở vật chất thay thế, và ngày phía kinh doanh (không chỉ CNTT) thực hành kế hoạch lần cuối. Chính phủ mang nghĩa vụ pháp lý liên tục hoạt động với người kế nhiệm có tên và chức năng thiết yếu, và doanh nghiệp đối mặt nghĩa vụ liên tục theo quy định, nên cả hai được đánh giá bằng việc doanh nghiệp có sống sót qua ngày tồi tệ không, không chỉ máy chủ.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một đội nhỏ xíu và ít đường băng, bạn không gánh nổi khu vực thứ hai nóng, nên hãy có chủ đích về những phần rẻ vẫn cứu bạn. Đặt một bậc trung thực, theo quy tắc 3-2-1 với ảnh chụp tự động và ít nhất một bản sao bất biến mà chính quản trị viên của bạn không xóa được, và giữ toàn bộ môi trường là hạ tầng dưới dạng mã để bạn dựng lại từ nguồn. Bỏ kế hoạch cầu kỳ và thay vào đó chạy một lần khôi phục thật vào môi trường nháp mỗi quý, vì một buổi diễn tập có đo thời gian dạy bạn nhiều hơn một tập hồ sơ không ai đọc.

**Doanh nghiệp nhỏ.** Không có chuyên gia liên tục riêng và ngân sách eo hẹp, hãy coi khôi phục là thứ bạn mua hơn xây. Dựa vào sao lưu được quản lý, ảnh chụp và sao chép đa khu vực của nhà cung cấp đám mây thay vì dựng hạ tầng DR đặt riêng, và chọn nhà cung cấp có sao lưu bất biến và quy trình khôi phục bạn tự chạy được. Đóng khung toàn bộ bài tập quanh hai câu hỏi bạn trả lời được không cần chuyên gia: chúng ta mất được bao nhiêu dữ liệu, và ngừng được bao lâu, và chứng minh một lần khôi phục hoạt động trước khi bạn tin nó.

**Doanh nghiệp lớn.** Ở quy mô lớn vấn đề là quản trị danh mục qua nhiều đội: một phân tích tác động kinh doanh giao cho mọi dịch vụ một RTO và RPO, chiến lược khôi phục phân bậc từ sao lưu-và-khôi-phục lên chủ động-chủ động, và một cái nhìn trung tâm về phụ thuộc thượng nguồn và nhà cung cấp gồm rủi ro tập trung. Hãy lập ngân sách tường minh cho dự phòng, sao chép và chi phí bản sao bất biến, chạy các buổi chuyển dự phòng đầy đủ có cơ quan quản lý chứng kiến theo nhịp, và đo khôi phục thực so với mục tiêu như một chỉ số độ tin cậy được theo dõi. Duy trì khôi phục mạng như chương trình riêng với bản sao kho bất biến và sổ tay phòng sạch, kiểm thử độc lập với các buổi diễn tập thiên tai.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn, và liên tục thường là nghĩa vụ pháp lý hơn là sở thích. Hãy xây một chương trình liên tục hoạt động xác định các chức năng thiết yếu, sắp thứ tự khôi phục của chúng, và nêu tên người kế nhiệm cùng cơ sở thay thế để quyết định không bao giờ đình trệ vì thiếu người được ủy quyền, và căn chỉnh nó theo hướng dẫn được công nhận như NIST SP 800-34 hỗ trợ nghĩa vụ FISMA. Giữ bản sao lưu cách ly không khí, định nghĩa hạ tầng dưới dạng mã để dựng lại ở khu vực thay thế, và chạy một bài tập đầy đủ hằng năm cộng các buổi diễn tập bàn giấy ransomware mà bạn báo cáo kết quả đo được cho cơ quan giám sát làm bằng chứng dịch vụ thiết yếu sống sót.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty SaaS mười hai người không gánh nổi khu vực thứ hai nóng, nên có chủ đích về những phần rẻ. Nó đặt một bậc trung thực: RTO bốn giờ, RPO mười lăm phút cho cơ sở dữ liệu khách hàng. Nó theo quy tắc 3-2-1 với ảnh chụp tự động, một bản sao nhân bản sang khu vực đám mây thứ hai và một bản sao bất biến với cửa sổ lưu giữ khóa mà quản trị viên của chính nó không xóa được. Toàn bộ môi trường của nó là hạ tầng dưới dạng mã (chương 8.2), nên nó dựng được ngăn xếp mới từ nguồn. Mỗi quý nó chạy một lần khôi phục thật vào môi trường nháp vào chiều thứ Sáu, bấm giờ, và ghi một ghi chú ngắn. Buổi diễn tập đầu tiên mất chín giờ và tìm ra một bước di chuyển bị thiếu; bản sửa là lý do lần sau chỉ mất ba.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia vận hành dưới yêu cầu khôi phục theo quy định đòi liên tục đã kiểm thử cho dịch vụ trọng yếu. Nó chạy dự phòng ấm ở khu vực thứ hai cho nền tảng ngân hàng lõi, với sao chép đồng bộ trong một cặp đô thị cho RPO gần bằng không và sao chép bất đồng bộ đến khu vực xa để sống sót thảm họa khu vực. Một phân tích tác động kinh doanh giao mọi dịch vụ một RTO và RPO, và một đội trung tâm lập bản đồ phụ thuộc thượng nguồn gồm hai nhà cung cấp SaaS được gắn cờ là rủi ro tập trung. Hai lần một năm nó thực hiện một buổi chuyển dự phòng đầy đủ có cơ quan quản lý chứng kiến, đo thực so với mục tiêu, và đưa khoảng trống vào chu kỳ kế tiếp. Một chương trình khôi phục mạng riêng duy trì bản sao kho bất biến và sổ tay phòng sạch, kiểm thử độc lập với các buổi diễn tập thiên tai.

**Chính phủ.** Một cơ quan quốc gia cung cấp trợ cấp duy trì chương trình liên tục hoạt động (COOP) xây để duy trì các chức năng thiết yếu trong mọi gián đoạn. Theo thực hành [liên tục hoạt động](https://en.wikipedia.org/wiki/Continuity_of_Operations) và hướng dẫn hoạch định dự phòng NIST SP 800-34 hỗ trợ nghĩa vụ FISMA của nó, nó xác định các chức năng thiết yếu, sắp thứ tự khôi phục, và nêu tên người kế nhiệm cùng cơ sở thay thế để quyết định không bao giờ đình trệ vì thiếu người được ủy quyền. Hệ thống hướng công dân mang RTO và RPO có tài liệu, sao lưu theo quy tắc 3-2-1 với bản sao cách ly không khí, và hạ tầng được định nghĩa dưới dạng mã để dựng lại ở khu vực thay thế. Một bài tập đầy đủ hằng năm, cộng các buổi diễn tập bàn giấy cho kịch bản ransomware, kiểm thử kế hoạch theo khôi phục đo được, và kết quả được báo cáo cho cơ quan giám sát làm bằng chứng dịch vụ thiết yếu sống sót qua ngày tồi tệ.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của DR và liên tục là thảm họa tránh được, thực sự khó định giá cho đến khi bạn cần và đau đớn cụ thể khi bạn cần. Hãy đóng khung nó là quản lý rủi ro: chi phí kỳ vọng của một gián đoạn là khả năng xảy ra nhân tác động của nó, và tác động với một tổ chức lớn chạy từ doanh thu mất mỗi giờ ngừng, qua tiền phạt quy định, chi phí thông báo vi phạm, đến thiệt hại danh tiếng kéo dài hơn lần ngừng hoạt động. Một sự kiện ransomware không khôi phục được đã kết liễu các công ty và, trong khu vực công, đã đưa dịch vụ công dân thiết yếu ngoại tuyến nhiều tuần. So với đó, chi phí của một năng lực khôi phục đã kiểm thử là khiêm tốn và biết được.

Tổng chi phí sở hữu (TCO) là thật và liên tục: hạ tầng dự phòng, băng thông sao chép, lưu trữ sao lưu (nhân với bản sao bất biến và ngoại tuyến), và thời gian kỹ thuật để xây tự động hóa và chạy diễn tập. Đây chính là lý do bạn phân bậc theo RTO và RPO thay vì mua chủ động-chủ động ở mọi nơi, để chi tiêu theo giá trị của mỗi hệ thống thay vì một chính sách đại trà. Để lập luận với ban lãnh đạo, hãy dịch kế hoạch sang ngôn ngữ của họ: đây là thời gian ngừng và mất dữ liệu chúng ta sống sót được hôm nay, đây là khoảng cách đến mục tiêu, đây là chi phí đóng nó, và đây là phơi nhiễm nếu chúng ta không. Hiện vật thuyết phục nhất là một buổi diễn tập đo được, vì một khôi phục bạn đã chứng minh là con số lãnh đạo tin được, và một kế hoạch chưa kiểm thử là khoản nợ ngụy trang thành tài sản.

## Phản mẫu và cạm bẫy

- **Sao lưu chưa kiểm thử.** Một lần khôi phục bạn chưa bao giờ thực hiện là hy vọng; buổi diễn tập là nơi bạn tìm thấy hỏng hóc, khóa thiếu và ổ sai.
- **Sao lưu với tới được từ môi trường sản xuất.** Nếu ransomware mã hóa hoặc xóa được bản sao lưu, bạn có một bản sao, không phải ba. Giữ một bản bất biến và ngoại tuyến.
- **Một RTO và RPO cho mọi thứ.** Bậc đại trà bảo vệ thừa cái tầm thường và bảo vệ thiếu cái trọng yếu; hãy phân bậc từ phân tích tác động kinh doanh.
- **Nhầm DR với BCP.** Khôi phục mọi máy chủ trong khi không ai biết ai tuyên bố thảm họa hay liên lạc nhân viên thế nào là hệ thống được khôi phục và doanh nghiệp thất bại.
- **Môi trường khôi phục dựng tay.** Hạ tầng bạn không dựng lại được từ mã trôi, và trôi được phát hiện giữa lúc chuyển dự phòng.
- **Phụ thuộc bị phớt lờ.** Khôi phục một ứng dụng trước cơ sở dữ liệu, nhà cung cấp định danh hay DNS của nó chỉ tạo ra lần ngừng hoạt động thứ hai.
- **Kế hoạch mục rữa.** Một tập hồ sơ viết một lần và không bao giờ thực hành mô tả một hệ thống không còn tồn tại.
- **Điểm mù nhà cung cấp.** Khôi phục của bạn bị chặn trên bởi khôi phục của nhà cung cấp trọng yếu, và rủi ro tập trung vô hình cho đến khi họ cùng hỏng.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Khôi phục tùy nghi và phản ứng. Sao lưu có thể chạy nhưng khôi phục chưa kiểm thử. Không có RTO hay RPO đã thống nhất, không có phân tích tác động kinh doanh, và khôi phục được ứng biến trong sự cố. Một vụ mất dữ liệu nghiêm trọng hay sự kiện ransomware có lẽ không khôi phục được.
- **Mức 2, Phát triển:** Thực hành cơ bản tồn tại nhưng không nhất quán qua các đội. Một số hệ thống trọng yếu có sao lưu theo quy tắc 3-2-1 và RTO cùng RPO có tài liệu cho các dịch vụ quan trọng nhất, và một kế hoạch DR cơ bản tồn tại với khôi phục thỉnh thoảng được kiểm thử. Độ phủ một phần, phụ thuộc chưa được lập bản đồ, diễn tập tùy nghi, và kỷ luật của một đội không hàm ý của đội kế tiếp.
- **Mức 3, Chuẩn hóa:** Thực hành khôi phục được lập tài liệu và thực thi toàn tổ chức. Một phân tích tác động kinh doanh thúc đẩy RTO và RPO phân bậc qua các hệ thống, chiến lược khôi phục được khớp với các bậc đó, môi trường là hạ tầng dưới dạng mã, phụ thuộc và thứ tự khôi phục được lập bản đồ, và các buổi diễn tập theo lịch (bàn giấy, ngày diễn tập và chuyển dự phòng) chạy theo nhịp xác định. Một kế hoạch khôi phục mạng với bản sao bất biến, ngoại tuyến được lập tài liệu và áp dụng nhất quán thay vì để cho từng đội.
- **Mức 4, Quản lý:** Khôi phục được đo và kiểm soát theo đường cơ sở. Mỗi buổi diễn tập nắm bắt RTO và RPO thực đạt được và theo dõi khoảng cách đến mục tiêu, và các chỉ số như tỷ lệ khôi phục thành công, phần hệ thống trọng yếu được khôi phục đầu-đến-cuối trong năm qua, độ phủ và tính bất biến của sao lưu, và độ trễ sao chép được giám sát như RPO thực được báo cáo trên bảng điều khiển. Sai lệch kích hoạt hành động, phân bậc được suy ra lại từ dữ liệu về cách hệ thống thực sự được dùng, và quyết định tiếp tục hay dừng dựa trên bằng chứng thay vì con số viết trên slide.
- **Mức 5, Điều phối:** Khôi phục được cải thiện liên tục, tích hợp trong toàn tổ chức, và thích ứng. Chuyển dự phòng và khôi phục phòng sạch mạng được diễn tập như thường lệ, rủi ro nhà cung cấp và tập trung được quản lý tích cực, và liên tục được tích hợp với độ tin cậy (chương 9.1) và ứng phó sự cố (chương 9.3) để tổ chức khôi phục khả đoán từ những thất bại nó chưa từng thấy và thu hẹp lại tư thế khôi phục khi bối cảnh hệ thống và bức tranh mối đe dọa dịch chuyển.

## Ý tưởng để thảo luận

1. Hệ thống trọng yếu nào của bạn chưa bao giờ được khôi phục đầu-đến-cuối, và cần gì để chứng minh nó làm được?
2. Nếu bạn mất khu vực đám mây chính trong cả một ngày, quy trình kinh doanh nào dừng, và bạn sẽ đưa hệ thống trở lại theo thứ tự nào?
3. Khôi phục của bạn phụ thuộc bao nhiêu vào các nhà cung cấp mà khôi phục của họ bạn không thấy hay kiểm thử được?
4. Bạn đang trả cho một bậc khôi phục mà phân tích tác động kinh doanh không biện minh ở đâu, và bạn đang bảo vệ thiếu ở đâu?
5. Nếu bản sao lưu của bạn với tới được và bị mã hóa tối nay, điểm khôi phục sạch cuối cùng thực sự của bạn là gì?
6. Khoảng cách trung thực giữa RTO và RPO đã hứa và những cái buổi diễn tập gần nhất của bạn thực sự đạt được là bao nhiêu?

## Những điểm cần ghi nhớ

- **Liên tục là mục tiêu; khôi phục là phương tiện.** Hoạch định liên tục kinh doanh giữ tổ chức chạy; khôi phục thảm họa khôi phục hệ thống CNTT nó phụ thuộc.
- **RTO và RPO điều khiển mọi thứ**, và cả hai đến từ phân tích tác động kinh doanh, không phải đoán mò kỹ thuật. Phân bậc hệ thống thay vì bảo vệ tất cả như nhau.
- **Bản sao lưu chưa kiểm thử không phải bản sao lưu.** Theo quy tắc 3-2-1, giữ ít nhất một bản sao bất biến và ngoại tuyến chống ransomware, và kiểm thử khôi phục theo lịch.
- **Khớp chiến lược DR với con số:** sao lưu-và-khôi-phục, đèn mồi, dự phòng ấm, hay chủ động-chủ động, chọn theo RTO và RPO của mỗi hệ thống.
- **Sao chép đánh đổi nhất quán lấy độ mới** (chương 3.3); RPO thực của bạn là độ trễ sao chép, không phải tài liệu thiết kế.
- **Dựng lại từ mã** với hạ tầng dưới dạng mã (chương 8.2), và lập bản đồ phụ thuộc trước khi bạn cần chúng.
- **Kiểm thử bằng bài tập bàn giấy, ngày diễn tập và buổi chuyển dự phòng đầy đủ**, và đo RTO cùng RPO thực so với mục tiêu.
- **Lên kế hoạch khôi phục mạng riêng** với khôi phục phòng sạch, và nối toàn bộ thực hành với độ tin cậy (chương 9.1), ứng phó sự cố (chương 9.3) và tuân thủ (chương 4.6).

## Tài liệu tham khảo và đọc thêm

- ISO 22301, *Security and resilience: Business continuity management systems: Requirements* (tiêu chuẩn quốc tế cho BCP).
- National Institute of Standards and Technology, *SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems* (RTO, RPO và chiến lược khôi phục cho hệ thống chính phủ).
- National Institute of Standards and Technology, *SP 800-61 Rev. 2: Computer Security Incident Handling Guide* (xử lý sự cố và khôi phục mạng).
- U.S. Federal Emergency Management Agency, *Continuity Guidance Circular* và hướng dẫn COOP liên bang (chức năng thiết yếu và liên tục hoạt động).
- Federal Financial Institutions Examination Council (FFIEC), tập *Business Continuity Management* (kỳ vọng khôi phục theo quy định cho tổ chức tài chính).
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, biên tập, *Site Reliability Engineering: How Google Runs Production Systems* (độ tin cậy và kiểm thử thảm họa).
- Kelly Shortridge và Aaron Rinehart, *Security Chaos Engineering* (cố ý thực hành thất bại và khôi phục).
- Cybersecurity and Infrastructure Security Agency (CISA), *#StopRansomware Guide* (phòng ngừa và thực hành khôi phục ransomware).
