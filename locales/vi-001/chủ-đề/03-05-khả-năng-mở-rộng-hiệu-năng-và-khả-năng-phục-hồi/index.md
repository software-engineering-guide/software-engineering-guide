# 3.5 Khả năng mở rộng, hiệu năng và khả năng phục hồi

## Tổng quan và động lực

[Khả năng mở rộng](https://en.wikipedia.org/wiki/Scalability), hiệu năng và khả năng phục hồi là ba chất lượng riêng biệt, và người ta thường nhầm lẫn chúng với nhau. **Hiệu năng** là hệ thống phản hồi nhanh đến đâu và làm được bao nhiêu việc trên mỗi đơn vị tài nguyên. **Khả năng mở rộng** là hệ thống duy trì hiệu năng tốt đến đâu khi tải tăng. **Khả năng phục hồi** là hệ thống tiếp tục hoạt động, hoặc suy giảm nhẹ nhàng, tốt đến đâu khi có thứ thất bại. Một hệ thống có thể nhanh nhưng không mở rộng được (tuyệt vời ở tải thấp, sụp đổ ở tải cao), mở rộng được nhưng mong manh (xử lý được khối lượng nhưng đổ khi một thành phần thất bại), hoặc phục hồi tốt nhưng chậm. Một tổ chức lớn cần cả ba, được thiết kế vào ngay từ đầu, vì trang bị bổ sung bất kỳ cái nào sau khi ra mắt đều tốn kém và gây xáo trộn.

Với các hệ thống doanh nghiệp và chính phủ, hậu quả của việc làm sai những điều này là công khai và nghiêm trọng. Hãy nghĩ đến một cổng thông tin trợ cấp quỵ ngay ngày đầu của một chương trình mới, một hệ thống khai thuế hết thời gian chờ vào hạn chót, hay một nền tảng thanh toán sập vào mùa mua sắm cao điểm. Đó là những thất bại lên tiêu đề báo, kích hoạt các cuộc điều tra và làm xói mòn niềm tin công chúng. Các hệ thống này cũng đối mặt với tải có đỉnh rất cao, thường định thời theo luật (hạn nộp hồ sơ, cửa sổ ghi danh, ngày trả lương) và các nghĩa vụ nghiêm ngặt về tính sẵn sàng và khôi phục. Bạn phải hoạch định năng lực cho các đợt tăng đột biến có thể dự đoán, suy giảm nhẹ nhàng trước những đợt không thể dự đoán, và khôi phục trong giới hạn thời gian và mất dữ liệu đã định sau thảm họa. Đây là kỹ thuật mang chiều kích trách nhiệm giải trình công khai.

Chương này bao quát mở rộng theo chiều ngang so với chiều dọc, tính phi trạng thái và [phân mảnh](https://en.wikipedia.org/wiki/Shard_(database_architecture)) như những yếu tố cho phép quy mô, [cân bằng tải](https://en.wikipedia.org/wiki/Load_balancing_(computing)), [tự động mở rộng](https://en.wikipedia.org/wiki/Autoscaling) và hoạch định năng lực, kỹ thuật hiệu năng với ngân sách tường minh, các mẫu khả năng phục hồi và [kỹ thuật hỗn loạn](https://en.wikipedia.org/wiki/Chaos_engineering), và [khôi phục thảm họa](https://en.wikipedia.org/wiki/Disaster_recovery) đa vùng được đóng khung bởi RTO, RPO và tính liên tục kinh doanh. Thông điệp thống nhất là những chất lượng này là sản phẩm của thiết kế có chủ đích và kiểm thử liên tục, không phải của hy vọng.

*Xem thêm:* chương 3.3 (hệ thống phân tán), chương 9.1 (kỹ thuật độ tin cậy hệ thống) và chương 9.2 (khả năng quan sát và giám sát).

## Các nguyên tắc chính

- **Thiết kế để mở rộng ra, không phải nâng lên.** Mở rộng dọc có trần và là một [điểm lỗi đơn](https://en.wikipedia.org/wiki/Single_point_of_failure); mở rộng ngang là cách bạn đạt quy mô lớn và phục hồi tốt.
- **Tính phi trạng thái là yếu tố cho phép mở rộng ngang.** Nếu bất kỳ yêu cầu nào cũng có thể đến bất kỳ thể hiện nào, bạn có thể thêm và bớt năng lực tự do.
- **Bạn không thể cải thiện những gì bạn không đo.** Công việc hiệu năng được dẫn dắt bởi phân tích hồ sơ và kiểm thử tải theo ngân sách tường minh, không bao giờ bằng phỏng đoán.
- **Mọi thứ đều thất bại; hãy thiết kế cho điều đó.** Giả định các thành phần sẽ thất bại và xây dựng để hệ thống sống sót qua thất bại của chúng.
- **Suy giảm nhẹ nhàng tốt hơn thất bại cứng.** Một hệ thống hoạt động một phần, bỏ bớt các tính năng không thiết yếu, tốt hơn một sự cố toàn phần.
- **Năng lực được hoạch định, các đợt tăng đột biến được hấp thụ.** Dự báo tải có thể dự đoán; dùng tự động mở rộng và khoảng dư cho phần còn lại.
- **Mục tiêu khôi phục là các quyết định kinh doanh.** RTO và RPO được doanh nghiệp chọn đối chiếu với chi phí, rồi được kỹ thuật hóa để đạt được.
- **Kiểm thử khả năng phục hồi có chủ đích.** Bạn không biết một hệ thống có phục hồi tốt cho đến khi bạn cố ý làm nó thất bại.

## Khuyến nghị

### Ưu tiên mở rộng ngang và thiết kế các dịch vụ phi trạng thái

Mở rộng dọc (máy lớn hơn) đơn giản và đôi khi là bước đầu đúng, nhưng nó chạm trần cứng, trở nên đắt không cân xứng ở đầu cao, và để lại một điểm lỗi đơn. **Mở rộng ngang** (nhiều máy hơn đằng sau một bộ cân bằng tải) mở rộng xa hơn nhiều và cải thiện tính sẵn sàng, vì mất một thể hiện là sống sót được. Điều kiện tiên quyết là **tính phi trạng thái**. Đừng giữ phiên máy khách hay trạng thái yêu cầu trên thể hiện; đẩy nó sang một kho dùng chung (cơ sở dữ liệu, bộ đệm, token). Các dịch vụ phi trạng thái có thể được thêm, bớt, thay thế và cân bằng tải tự do, đó là điều làm cho cả tự động mở rộng lẫn triển khai cuốn chiếu khả thi. Ở nơi trạng thái phải được phân vùng, hãy **phân mảnh** theo một khóa phân bố tải đều và giữ dữ liệu liên quan trên cùng một mảnh.

### Cân bằng tải, tự động mở rộng và hoạch định năng lực

Đặt một **bộ cân bằng tải** phía trước mọi tầng được mở rộng để phân phối lưu lượng và định tuyến vòng qua các thể hiện không khỏe qua kiểm tra sức khỏe. Cấu hình **tự động mở rộng** để thêm năng lực khi một chỉ báo dẫn đầu (CPU, độ sâu hàng đợi yêu cầu, độ trễ) vượt ngưỡng và bớt khi tải giảm. Điều chỉnh tốc độ mở rộng và thời gian làm nguội để bạn không bị chậm sau một đợt tăng đột biến cũng không dao động liên tục. Tự động mở rộng không thay thế cho **hoạch định năng lực**. Với các đợt tăng đột biến có thể dự đoán, quan trọng với kinh doanh (hạn nộp thuế, kỳ ghi danh, sự kiện bán hàng), hãy dự báo tải, cung cấp trước hoặc làm nóng trước năng lực, và kiểm thử tải đến mục tiêu đó từ trước. Riêng tự động mở rộng không thể phản ứng tức thì với một bước thay đổi đột ngột, và khởi động lạnh thêm độ trễ đúng lúc bạn ít có thể chịu nhất. Luôn giữ khoảng dư. Chạy ở 100% không để chỗ hấp thụ các đợt tăng đột biến hay thất bại.

### Kỹ thuật hóa hiệu năng theo ngân sách tường minh

Hãy đặt **ngân sách hiệu năng** (các mục tiêu cụ thể như độ trễ API p95 dưới 200 ms, trang tương tác được dưới 2 giây, hoặc chi phí mỗi giao dịch dưới một ngưỡng) và thực thi chúng trong kiểm thử và giám sát để các hồi quy làm hỏng đường ống thay vì tới tay người dùng. Dẫn dắt tối ưu hóa bằng **đo lường**. Phân tích hồ sơ để tìm nút thắt thực, hiếm khi ở chỗ bạn đoán, và kiểm thử tải để tìm nơi hệ thống vỡ và nó hành xử thế nào gần giới hạn đó. Tập trung vào đường tới hạn và phần đuôi (p95/p99), vì ở quy mô lớn độ trễ đuôi chi phối trải nghiệm người dùng. Tối ưu nút thắt lớn nhất trước, đo lại, và dừng khi bạn đạt ngân sách. Tối ưu quá mức mã vốn đã đủ tốt là công sức lãng phí.

### Xây dựng các mẫu khả năng phục hồi và xác thực bằng kỹ thuật hỗn loạn

Áp dụng các mẫu khả năng phục hồi từ hệ thống phân tán: thời gian chờ, thử lại có giới hạn với độ lùi, [bộ ngắt mạch](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (thất bại nhanh khi một phụ thuộc không khỏe) và vách ngăn (cô lập các nhóm tài nguyên để một thất bại không thể làm cạn phần còn lại), cộng với **suy giảm nhẹ nhàng** (bỏ hoặc đơn giản hóa các tính năng không thiết yếu dưới áp lực: tắt gợi ý, phục vụ nội dung lưu đệm, xếp hàng công việc không khẩn cấp) và **loại bỏ tải** (từ chối hoặc điều tiết các yêu cầu dư thừa để bảo vệ lõi thay vì sụp đổ hoàn toàn). Loại bỏ các điểm lỗi đơn qua dự phòng ở mọi tầng. Sau đó **xác thực** khả năng phục hồi bằng kỹ thuật hỗn loạn. Cố ý tiêm thất bại (giết thể hiện, thêm độ trễ, cắt một phụ thuộc, làm hỏng một vùng sẵn sàng) trong các thí nghiệm có kiểm soát, bắt đầu từ kiểm thử và trưởng thành lên các ngày diễn tập trên môi trường thực, để chứng minh hệ thống hành xử như đã thiết kế. Khả năng phục hồi chưa bao giờ được kiểm thử chỉ là một giả thuyết.

### Hoạch định đa vùng, khôi phục thảm họa và tính liên tục kinh doanh

Hãy quyết định tường minh các mục tiêu khôi phục: **RTO** (Mục tiêu Thời gian Khôi phục, bạn có thể ngừng hoạt động bao lâu) và **RPO** (Mục tiêu Điểm Khôi phục, bạn có thể chấp nhận mất bao nhiêu dữ liệu). Đây là các quyết định kinh doanh với hàm ý chi phí trực tiếp, và chúng dẫn dắt kiến trúc. Các lựa chọn trải rộng về chi phí và tốc độ: sao lưu-và-khôi phục (rẻ nhất, chậm nhất), đèn mồi, dự phòng ấm, và đa vùng chủ động-chủ động (đắt nhất, RTO/RPO gần bằng không). Chọn bậc mà mức độ quan trọng của từng hệ thống biện minh được. Không phải thứ gì cũng cần chủ động-chủ động. Sao chép dữ liệu qua các vùng phù hợp với RPO đã chọn, tự động hóa chuyển đổi dự phòng, và trên hết, **kiểm thử chuyển đổi dự phòng thường xuyên**. Khôi phục thảm họa chưa được kiểm thử chắc chắn thất bại khi cuối cùng cần đến. Bọc tất cả trong một **kế hoạch liên tục kinh doanh** bao gồm con người, truyền thông và các phương án thủ công dự phòng, không chỉ công nghệ.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Mở rộng dọc | Đơn giản, không đổi mã, công sức ban đầu thấp | Trần cứng, đắt ở đầu cao, điểm lỗi đơn |
| Mở rộng ngang | Quy mô gần như không giới hạn, cải thiện tính sẵn sàng | Cần phi trạng thái, cân bằng tải, vận hành nhiều hơn |
| Tự động mở rộng | Khớp chi phí với nhu cầu, xử lý tải biến thiên | Phản ứng có độ trễ; khởi động lạnh; có thể dao động nếu chỉnh sai |
| Đa vùng chủ động-chủ động | RTO/RPO gần bằng không, sống sót khi mất cả vùng | Chi phí và độ phức tạp cao nhất, nhất quán dữ liệu khó |
| Khôi phục thảm họa kiểu sao lưu-và-khôi phục | Rẻ nhất, đơn giản nhất | RTO dài, cửa sổ mất dữ liệu lớn hơn |

Đánh đổi trung tâm là chi phí so với sự bảo đảm. Mỗi mức tăng thêm của khoảng dư mở rộng, hiệu năng và năng lực khôi phục tốn tiền và độ phức tạp, và lợi tức không tuyến tính. Đi từ tính sẵn sàng 99,9% lên 99,99%, hay từ RTO một giờ xuống vài giây, có thể nhân chi phí lên nhiều lần. Kỷ luật là định cỡ mỗi khoản đầu tư theo mức độ quan trọng thực tế của hệ thống và mức chịu đựng của doanh nghiệp với thời gian ngừng và mất dữ liệu, thay vì phản xạ kỹ thuật hóa mọi thứ lên bậc cao nhất. Một hệ thống thanh toán hướng đến công dân xứng đáng với dự phòng chủ động-chủ động; một công cụ báo cáo nội bộ thì không.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi sự cố nghiêm trọng gần nhất xảy ra, cái nào trong ba (hiệu năng, khả năng mở rộng, khả năng phục hồi) thực sự thất bại, và bạn có sửa đúng cái không?** Chương này tách chúng một cách có chủ đích: một hệ thống có thể nhanh nhưng sụp đổ dưới tải, mở rộng được nhưng đổ khi một thành phần chết, hoặc sống sót qua thất bại nhưng chậm. Các đội thường chẩn đoán sai, thêm năng lực cho một vấn đề phục hồi hoặc gia cố một hệ thống chỉ đơn giản là cấp thiếu cho một đợt tăng đột biến. Hãy duyệt hai sự cố nghiêm trọng gần nhất và gọi tên chất lượng nào đã vỡ và phản ứng thực sự cải thiện điều gì. Sự phân biệt này đổi cách sửa: phi trạng thái và phân mảnh cho khả năng mở rộng, dự phòng và bộ ngắt mạch cho khả năng phục hồi, phân tích hồ sơ và ngân sách cho hiệu năng. Chọn đúng loại là sự khác biệt giữa chi tiền cho thuốc chữa và chi tiền cho một triệu chứng.

2. **Các hồi quy hiệu năng có làm hỏng đường ống của bạn không, hay chúng tới tay người dùng trước khi ai đó nhận ra?** Một ngân sách hiệu năng (độ trễ p95, thời gian tương tác của trang, chi phí mỗi giao dịch) chỉ bảo vệ người dùng nếu được thực thi tự động, để một thay đổi vượt qua nó làm hỏng bản dựng thay vì được phát hành. Trong một đội lớn có nhiều người đóng góp, độ trễ len vào qua hàng nghìn commit nhỏ, và không có cổng chặn thì phần đuôi mục dần cho đến khi một lần ra mắt phơi bày nó. Hãy mang các ngân sách hiện tại của bạn và kiểm tra liệu chúng có được nối vào CI và giám sát không, và liệu chúng nhắm vào p95 và p99 thay vì trung bình không, vì phần đuôi là thứ người dùng cảm nhận ở quy mô lớn. Nơi chưa có ngân sách, đặt một cái là bước đầu tiên. Thực thi là thứ biến thiện ý thành thuộc tính sống sót qua sự lớn lên của đội.

3. **Dưới áp lực, cái gì bị bỏ trước, và bạn đã thiết kế thứ tự đó hay sẽ khám phá nó trong sự cố?** Suy giảm nhẹ nhàng và loại bỏ tải nghĩa là hệ thống từ bỏ công việc không thiết yếu để bảo vệ lõi, nhưng chỉ khi bạn đã quyết định trước cái gì là thiết yếu. Với một dịch vụ hướng đến công dân, thứ hạng đó thường là một quyết định chính sách: nộp tờ khai thuế phải sống sót ngay cả khi bảng điều khiển trạng thái và tra cứu lịch sử tắt. Nếu không ai chọn, hệ thống bỏ bất cứ thứ gì thất bại trước, có thể đúng là thứ người dùng cần nhất. Hãy liệt kê các tính năng của bạn theo thứ tự ưu tiên và xác nhận kiến trúc có thể bỏ các tính năng ưu tiên thấp (phản hồi lưu đệm, gợi ý bị tắt, công việc không khẩn cấp được xếp hàng) mà không kéo theo đường tới hạn. Sau đó kiểm thử nó dưới tải thật, vì suy giảm chưa được kiểm thử chỉ là hy vọng.

4. **Với hệ thống quan trọng nhất của bạn, RTO và RPO là bao nhiêu, ai thực sự chọn những con số đó, và lần cuối bạn chứng minh mình đáp ứng được chúng là khi nào?** Mục tiêu Thời gian Khôi phục (bạn có thể ngừng bao lâu) và Mục tiêu Điểm Khôi phục (bạn có thể chấp nhận mất bao nhiêu dữ liệu) là các quyết định kinh doanh với hàm ý chi phí trực tiếp, nhưng trong một đội lớn chúng thường do ai viết sổ tay vận hành tự nghĩ ra thay vì do những người chịu trách nhiệm về dịch vụ sở hữu. Lực kéo đối lập là chi phí so với sự bảo đảm: thu hẹp RTO từ một giờ xuống vài giây hoặc RPO từ vài phút xuống không có thể nhân hóa đơn hạ tầng lên nhiều lần, nên con số đúng là con số mà doanh nghiệp thực sự sẽ trả, không phải con số ấn tượng nhất. Hãy mang các mục tiêu đã lập tài liệu, ngày của lần kiểm thử chuyển đổi dự phòng thực cuối cùng, và thời gian cùng dữ liệu mất đo được mà lần kiểm thử đó tạo ra, vì một mục tiêu chưa kiểm thử là một điều ước. Trong bối cảnh doanh nghiệp và chính phủ, những con số này có thể do luật, hợp đồng hoặc SLA đặt, nên hãy nêu tên ai ký duyệt chúng và liệu buổi diễn tập gần nhất có đáp ứng nghĩa vụ hay âm thầm bỏ lỡ.

5. **Với đợt tăng đột biến có thể dự đoán lớn nhất của bạn, bạn đang tin vào tự động mở rộng phản ứng tại chỗ, hay đã dự báo tải, cung cấp trước và kiểm thử tải đến mục tiêu đó?** Tự động mở rộng phản ứng với độ trễ và khởi động lạnh thêm độ trễ đúng lúc bạn ít có thể chịu nhất, nên một bước thay đổi đột ngột đã biết (hạn nộp hồ sơ, cửa sổ ghi danh, sự kiện bán hàng) chính xác là trường hợp mở rộng phản ứng thất bại và hoạch định năng lực có chủ đích thắng. Căng thẳng là chi phí: làm nóng trước năng lực cho một đỉnh nghĩa là trả tiền cho khoảng dư nằm không phần lớn thời gian trong năm, và cám dỗ là hy vọng tự động mở rộng lo miễn phí. Hãy mang số liệu đỉnh năm ngoái, dự báo năm nay có tăng trưởng, và kết quả của một bài kiểm thử tải chạy đến bội số của dự báo đó thay vì đến lưu lượng trung bình hôm nay. Với dịch vụ chính phủ hoặc doanh nghiệp đối mặt một đợt tăng đột biến định thời theo luật, hãy thêm hậu quả của việc làm sai, vì một cổng thông tin trợ cấp hay hệ thống thuế quỵ vào ngày đầu trở thành một cuộc điều tra công khai, không chỉ là một buổi chiều chậm chạp.

6. **Bạn đã bao giờ cố ý làm hỏng một thành phần trên môi trường thực chưa, và bậc dự phòng của từng hệ thống có thực sự khớp với mức độ quan trọng và chi phí của nó không?** Khả năng phục hồi chưa bao giờ được kiểm thử là một giả thuyết, và các bậc bạn có thể mua trải từ sao lưu-và-khôi phục rẻ qua dự phòng ấm đến đa vùng chủ động-chủ động đắt, nên kỷ luật là chi sự bảo đảm ở nơi được biện minh thay vì mạ vàng mọi thứ hay không bảo vệ gì. Các cân nhắc đối lập là bán kính ảnh hưởng và ngân sách: thí nghiệm hỗn loạn phải có lan can và công tắc hủy, và chủ động-chủ động cho công cụ báo cáo nội bộ là lãng phí trong khi chỉ sao lưu cho nền tảng thanh toán là sơ suất. Hãy mang bản kiểm kê các điểm lỗi đơn của bạn, bậc dự phòng của từng hệ thống quan trọng, và bằng chứng về lần tiêm lỗi có kiểm soát gần nhất cùng điều nó đã phơi bày. Trong các danh mục doanh nghiệp và chính phủ, hãy ánh xạ mỗi bậc với một xếp hạng mức độ quan trọng có tài liệu để kiểm toán viên thấy tiền đi theo rủi ro, và để không ai phải bảo vệ khoản chi lần đầu tiên trong chính sự cố.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Bạn không thể dự đoán một lần ra mắt mang đến năm mươi lượt đăng ký hay năm mươi nghìn, vì vậy hãy mua quy mô thay vì xây: chạy các dịch vụ phi trạng thái đằng sau một bộ cân bằng tải được quản lý và để nền tảng tự động mở rộng theo tốc độ yêu cầu. Đặt một ngân sách hiệu năng khiêm tốn và chọn các kho dữ liệu được quản lý để một đợt tăng đột biến không buộc phải tái kiến trúc lúc 2 giờ sáng. Hiện tại hãy bỏ qua khôi phục thảm họa đa vùng và các chương trình hỗn loạn; giữ các bản sao lưu đã kiểm thử và dành sự chú ý kỹ thuật khan hiếm cho sản phẩm, không phải cho sự dự phòng mà lưu lượng của bạn chưa biện minh.

**Doanh nghiệp nhỏ.** Không có chuyên gia độ tin cậy và ngân sách eo hẹp, lựa chọn mua-so-với-xây nghiêng mạnh về mua: một nền tảng được quản lý hoặc bộ công nghệ serverless biến mở rộng và chuyển đổi dự phòng thành việc của nhà cung cấp, và một vùng được vận hành tốt thường là đủ. Hãy đóng khung khả năng phục hồi thành một số ít lời hứa cụ thể bạn giữ được, như một bản sao lưu hằng đêm bạn đã thực sự khôi phục từ nó một lần và một cửa sổ khôi phục thực tế bạn đã thông báo cho khách hàng. Tránh trả tiền cho chủ động-chủ động hay kiểm thử tải liên tục mà bạn không có lưu lượng lẫn nhân sự để biện minh.

**Doanh nghiệp lớn.** Vấn đề là sự nhất quán qua nhiều đội: chuẩn hóa ngân sách hiệu năng được thực thi trong CI, một thư viện dùng chung các mẫu khả năng phục hồi (thời gian chờ, bộ ngắt mạch, vách ngăn), và một bậc dự phòng có tài liệu cho mỗi hệ thống gắn với mức độ quan trọng của nó. Dành đa vùng chủ động-chủ động cho các dịch vụ bậc một, chạy chương trình kỹ thuật hỗn loạn có lan can và các ngày diễn tập trên môi trường thực, và coi hoạch định năng lực cho các đợt tăng đột biến đã biết là kỷ luật theo lịch trình thay vì chuyện nghĩ sau. Quản trị RTO và RPO tập trung để mọi hệ thống quan trọng có các mục tiêu được sở hữu, đã kiểm thử mà kiểm toán viên xác minh được.

**Chính phủ.** Tải thường định thời theo luật và nghĩa vụ sẵn sàng là luật định, nên hoạch định năng lực không thể dựa vào tự động mở rộng phản ứng tại chỗ: hãy dự báo đợt tăng đột biến hạn chót, cung cấp trước, và kiểm thử tải cao hơn nhiều so với dự báo. Mua sắm nên quy định RTO, RPO và một lịch chuyển đổi dự phòng đã diễn tập như yêu cầu hợp đồng, không phải lời hứa của nhà cung cấp, và nên tránh bị khóa một vùng duy nhất cho các dịch vụ quan trọng. Hãy quyết định trước đường nào là thiết yếu về pháp lý (nộp tờ khai, yêu cầu trợ cấp) để suy giảm bỏ bảng điều khiển trạng thái và tra cứu trước, và minh bạch với công chúng về sự cố và khôi phục thay vì hy vọng không ai để ý.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp nhỏ ra mắt trên Product Hunt không thể dự đoán mình sẽ nhận năm mươi lượt đăng ký hay năm mươi nghìn, nên giữ các dịch vụ phi trạng thái đằng sau một bộ cân bằng tải được quản lý và để nền tảng tự động mở rộng theo tốc độ yêu cầu. Họ đặt một ngân sách hiệu năng khiêm tốn (trang phản hồi dưới 300ms ở phân vị 95) và chọn một cơ sở dữ liệu được quản lý để một đợt tăng lưu lượng không buộc phải tái kiến trúc lúc 2 giờ sáng. Khi đợt tăng đột biến ngày ra mắt thực sự đến, trang web chậm đi một chút thay vì đổ, và đội dành cả ngày nói chuyện với người dùng mới thay vì chiến đấu với một sự cố.

**Doanh nghiệp lớn.** Một công ty truyền thông phát trực tuyến chạy các dịch vụ phi trạng thái qua nhiều vùng đằng sau cân bằng tải toàn cầu, tự động mở rộng theo tốc độ yêu cầu để theo làn sóng giờ vàng hằng ngày. Ngân sách hiệu năng kiểm soát mọi bản phát hành theo độ trễ khởi động p99. Khi một vùng thất bại, lưu lượng tự động chuyển sang các vùng khỏe, và các tính năng không thiết yếu (ảnh bìa cá nhân hóa, làm mới gợi ý) suy giảm trước để bảo vệ việc phát. Công ty chạy các thí nghiệm hỗn loạn liên tục trên môi trường thực, thường xuyên chấm dứt thể hiện và tiêm độ trễ, để các thất bại thật không thể phân biệt với diễn tập và không gây sự cố nào khách hàng nhìn thấy.

**Chính phủ.** Một cơ quan thuế biết hệ thống khai thuế của mình đối mặt với một đợt tăng đột biến khổng lồ, ấn định theo luật mỗi năm. Thay vì dựa vào tự động mở rộng phản ứng tại chỗ, họ dự báo tải đỉnh từ các năm trước, cung cấp trước năng lực nhiều tuần, và kiểm thử tải đến 150% dự báo. Kiến trúc là phi trạng thái đằng sau các bộ cân bằng tải với một vùng thứ hai dự phòng ấm. RTO và RPO được đặt bằng chính sách (không quá 15 phút ngừng hoạt động và gần như không mất dữ liệu cho các tờ khai đã nộp), và chuyển đổi dự phòng được diễn tập hằng quý. Dưới tải cực đoan, các tính năng không quan trọng (bảng điều khiển trạng thái, tra cứu lịch sử) bị bỏ trước để việc nộp tờ khai, đường thiết yếu về pháp lý, vẫn khả dụng.

## Luận chứng kinh doanh: động lực, ROI và TCO

Khả năng mở rộng, hiệu năng và khả năng phục hồi là những trường hợp điển hình mà chi phí thất bại vượt xa chi phí phòng ngừa. Nhưng phòng ngừa hiện rõ trên ngân sách còn thất bại chỉ là tiềm năng, đó là lý do chúng bị tài trợ thiếu kinh niên cho đến thảm họa đầu tiên. Chi phí áp dụng là thật: hạ tầng dự phòng, năng lực đa vùng, công cụ kiểm thử tải và hỗn loạn, và thời gian kỹ thuật để xây tính phi trạng thái và các mẫu khả năng phục hồi. Chi phí của việc *không* đầu tư là một sự cố nổi bật vào lúc nhu cầu cao điểm: doanh thu mất từng phút với thương mại, nghĩa vụ luật định bị lỡ và điều tra công khai với chính phủ, tiền phạt [thỏa thuận mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA), và thiệt hại danh tiếng lâu dài.

Hãy đóng khung lập luận với ban lãnh đạo bằng những con số mà doanh nghiệp đã hiểu. Ước tính chi phí của một giờ ngừng hoạt động lúc cao điểm (giao dịch mất, tiền phạt, khắc phục, danh tiếng), rồi so sánh với chi phí hằng năm của sự dự phòng và kiểm thử ngăn nó. Với các hệ thống quan trọng, phòng ngừa hầu như luôn chỉ là một phần nhỏ của một sự cố lớn đơn lẻ. Gắn RTO và RPO với tiền cụ thể: bao nhiêu doanh thu hoặc bao nhiêu giao dịch mỗi giờ ngừng hoạt động, và mất bao nhiêu dữ liệu là chấp nhận được về pháp lý hay thương mại. Hãy trình bày hiệu năng như một đòn bẩy doanh thu và sự hài lòng, vì các hệ thống nhanh hơn chuyển đổi tốt hơn và tốn ít hơn mỗi giao dịch, và trình bày khả năng phục hồi như bảo hiểm có phí nhỏ so với tổn thất được bảo vệ. Lập luận mạnh nhất là những chất lượng này rẻ để thiết kế vào và tai hại để trang bị bổ sung sau sự cố buộc phải làm.

## Phản mẫu và cạm bẫy

- **Phiên dính và trạng thái trong thể hiện.** Lưu trạng thái phiên trên máy chủ, ngăn mở rộng ngang tự do và thay thế thể hiện an toàn.
- **Tự động mở rộng như hoạch định năng lực.** Giả định tự động mở rộng sẽ hấp thụ một đợt tăng đột biến đã biết mà nó quá chậm để phản ứng.
- **Chạy nóng không có khoảng dư.** Vận hành ở mức sử dụng gần 100%, không để lại gì để hấp thụ các đợt tăng đột biến hay thất bại.
- **Tối ưu không phân tích hồ sơ.** Tinh chỉnh mã không phải nút thắt trong khi nút thắt thực không được đụng đến.
- **Bỏ qua phần đuôi.** Báo cáo độ trễ trung bình trong khi người dùng p99 chịu khổ; trung bình che giấu nỗi đau ở quy mô lớn.
- **Khôi phục thảm họa chưa kiểm thử.** Một kế hoạch DR và bản sao lưu chưa bao giờ được thực hành và sẽ thất bại khi cần.
- **Điểm lỗi đơn.** Một bộ cân bằng tải, một cơ sở dữ liệu chính, một vùng: một thành phần không dự phòng kéo sập mọi thứ.
- **Kỹ thuật hỗn loạn không có lan can.** Tiêm thất bại mà không kiểm soát bán kính ảnh hưởng hay công tắc hủy, gây ra chính sự cố bạn định ngăn.

## Mô hình trưởng thành

- **Mức 1: Khởi đầu.** Tùy nghi và phản ứng. Một thể hiện hoặc mở rộng dọc, trạng thái giữ trên máy chủ. Không kiểm thử tải, không ngân sách hiệu năng, và không khôi phục thảm họa ngoài những bản sao lưu thỉnh thoảng không ai khôi phục thử. Mọi thất bại thành phần gây sự cố toàn phần, và vấn đề quy mô được phát hiện trên môi trường thực.
- **Mức 2: Phát triển.** Các thực hành cơ bản xuất hiện nhưng khác nhau giữa các đội. Một số dịch vụ mở rộng ngang và phi trạng thái đằng sau bộ cân bằng tải, với tự động mở rộng cơ bản trên một vài cái. Kiểm thử tải diễn ra trước các lần ra mắt lớn nhưng không thường xuyên, và bản sao lưu tồn tại trong khi khôi phục thảm họa được lập tài liệu nhưng hiếm khi thực hành. Điều một đội làm tốt thì đội khác chưa bắt đầu.
- **Mức 3: Chuẩn hóa.** Các thực hành được lập tài liệu và thực thi toàn tổ chức. Năng lực được hoạch định cho các đợt tăng đột biến đã biết với khoảng dư, ngân sách hiệu năng được thực thi trong CI để hồi quy làm hỏng bản dựng, và các mẫu khả năng phục hồi (thời gian chờ, thử lại có giới hạn, bộ ngắt mạch, vách ngăn) cùng suy giảm nhẹ nhàng là mặc định. RTO và RPO được xác định cho từng hệ thống, bậc dự phòng được gán theo mức độ quan trọng, và chuyển đổi dự phòng khôi phục thảm họa được kiểm thử theo lịch đều đặn qua các đội.
- **Mức 4: Quản lý.** Các chất lượng được đo và kiểm soát theo đường cơ sở. Các đội theo dõi độ trễ p95 và p99, ngân sách lỗi, mức sử dụng và khoảng dư so với dự báo, và cảnh báo khi vi phạm thay vì phát hiện lúc ra mắt. Thời gian chuyển đổi dự phòng đã kiểm thử được so với RTO và RPO mục tiêu, ngưỡng suy giảm và loại bỏ tải được xác thực bằng chỉ số, và các quyết định phát hành và năng lực đi hay không đi được dẫn dắt bởi dữ liệu. Khi các con số trôi khỏi đường cơ sở, khoảng cách hiện rõ và có người sở hữu thay vì bị che sau trung bình.
- **Mức 5: Điều phối.** Khả năng mở rộng, hiệu năng và khả năng phục hồi được cải thiện liên tục và tích hợp trong toàn tổ chức. Đa vùng chủ động-chủ động được dùng ở bất cứ nơi nào mức độ quan trọng biện minh, kỹ thuật hỗn loạn chạy liên tục bao gồm các ngày diễn tập trên môi trường thực, và dự báo năng lực nuôi trực tiếp vào hoạch định và mua sắm. Khả năng phục hồi được xác thực liên tục, mục tiêu khôi phục được đáp ứng nhất quán và được chứng minh, và kiến trúc thích ứng khi mẫu tải và bức tranh rủi ro dịch chuyển, gắn với hoạch định liên tục kinh doanh và rủi ro.

## Ý tưởng để thảo luận

1. Dịch vụ nào của bạn vẫn giữ trạng thái trên thể hiện, và điều gì ngăn bạn làm chúng phi trạng thái?
2. Với hệ thống quan trọng nhất của bạn, RTO và RPO là bao nhiêu, ai đặt chúng, và lần cuối bạn chứng minh đáp ứng được chúng là khi nào?
3. Tự động mở rộng có thực sự bảo vệ bạn trước đợt tăng đột biến đã biết lớn nhất không, hay bạn đang dựa vào nó làm điều nó không thể?
4. Điểm lỗi đơn còn lại của bạn ở đâu, và kế hoạch loại bỏ nó là gì?
5. Bạn có đang đo và lập ngân sách cho độ trễ p99, hay ẩn sau các con số trung bình?
6. Bạn đã bao giờ cố ý làm hỏng một thành phần trên môi trường thực chưa? Nếu chưa, làm sao bạn biết khả năng phục hồi của mình hoạt động?

## Những điểm cần ghi nhớ

- Phân biệt hiệu năng, khả năng mở rộng và khả năng phục hồi; một hệ thống lớn cần cả ba, được thiết kế vào ngay từ đầu.
- Mở rộng ngang và dịch vụ phi trạng thái là nền tảng của quy mô, tính sẵn sàng và triển khai an toàn.
- Kết hợp tự động mở rộng với hoạch định năng lực thực sự và khoảng dư cho các đợt tăng đột biến có thể dự đoán, quan trọng với kinh doanh.
- Dẫn dắt hiệu năng bằng phân tích hồ sơ và kiểm thử tải theo ngân sách tường minh, tập trung vào đường tới hạn và phần đuôi.
- Xây dựng khả năng phục hồi bằng thời gian chờ, bộ ngắt mạch, vách ngăn, suy giảm nhẹ nhàng và dự phòng, rồi xác thực nó bằng kỹ thuật hỗn loạn.
- Đặt RTO và RPO như các quyết định kinh doanh, kỹ thuật hóa DR khớp với mức độ quan trọng của từng hệ thống, và kiểm thử chuyển đổi dự phòng thường xuyên.

## Tài liệu tham khảo và đọc thêm

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Betsy Beyer và cộng sự (Google), *Site Reliability Engineering* và *The Site Reliability Workbook*
- Casey Rosenthal và Nora Jones, *Chaos Engineering*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- John Allspaw, *The Art of Capacity Planning*
- Ilya Grigorik, *High Performance Browser Networking*
- Nassim Nicholas Taleb, *Antifragile*
