# 11.1 Quy trình khám phá

## Tổng quan và động lực

Quy trình khám phá là dòng công việc quyết định **xây gì và vì sao**, và xác định **thành công sẽ trông thế nào**, trước và song song với phân phối. Trong khi quy trình phân phối (chương 11.2) biến các ý tưởng đã xác thực thành phần mềm đang chạy, quy trình khám phá biến vấn đề, bằng chứng và chiến lược thành một tập kết quả dự định được ưu tiên, kiểm thử được. Trong thực hành hiện đại, hai quy trình chạy liên tục và song song, thường gọi là phát triển *hai đường*, thay vì các giai đoạn tuần tự. Khám phá liên tục cấp cho phân phối nguồn công việc đã giảm rủi ro, đóng khung tốt, và phân phối liên tục đưa dữ liệu kết quả thực tế ngược lại vào khám phá.

Với các đội lớn, quy trình khám phá yếu là kiểu thất bại đắt nhất trong phần mềm. Một đội phân phối xuất sắc nhưng khám phá kém xây sai thứ một cách hiệu quả: nó phát hành nhanh, đạt mục tiêu vận tốc, và vẫn không dịch chuyển chỉ số kinh doanh nào. Chi phí vô hình trên bảng điều khiển kỹ thuật và khổng lồ trên bảng cân đối. Quy trình khám phá là cách bạn làm chi phí đó hiển thị: nó buộc mục tiêu phải tường minh, đo được và có thể bị bác bỏ trước khi bạn cam kết các khoản đầu tư lớn.

Bối cảnh doanh nghiệp và chính phủ nâng rủi ro. Doanh nghiệp phối hợp hàng chục đội theo một chiến lược chung, nên mục tiêu cục bộ lệch cộng dồn thành danh mục lãng phí. Chương trình chính phủ cam kết tài trợ công nhiều năm cho các nhiệm vụ do luật định, nơi "chúng tôi xây đúng điều hợp đồng nói" không phải lời bào chữa nếu kết quả (công dân được phục vụ, thời gian chờ giảm, gian lận được ngăn) không bao giờ thành hiện thực. Một quy trình khám phá có kỷ luật, được diễn đạt qua mục tiêu, thước đo và yêu cầu chất lượng tường minh, là cách cả hai giữ ý định của mình kiểm toán được.

## Các nguyên tắc chính

- **Kết quả hơn đầu ra.** Đo thay đổi bạn tạo ra cho người dùng và doanh nghiệp, không phải tính năng bạn phát hành.
- **Làm ý định tường minh và đo được.** Một mục tiêu bạn không đo được là một ý kiến bạn không quản lý được.
- **Giảm rủi ro trước khi xây.** Thí nghiệm rẻ nhất thắng ý kiến tự tin nhất.
- **Khám phá và phân phối chạy liên tục song song**, không phải các cổng tuần tự.
- **Thuộc tính chất lượng là yêu cầu, không phải suy nghĩ sau.** Độ tin cậy, bảo mật và khả năng tiếp cận được khám phá và đặc tả, không phải hy vọng.
- **Căn chỉnh thắng tối ưu cục bộ.** Mục tiêu lồng nhau nối công việc của đội với chiến lược.
- **Khép vòng lặp.** Kết quả đã giao là bằng chứng quay lại khám phá.

## Khuyến nghị

### Đóng khung hướng đi bằng OKR

Hãy dùng **[Mục tiêu và Kết quả then chốt](https://en.wikipedia.org/wiki/OKR) (OKR)** để nối chiến lược với thực thi của đội. Một *Mục tiêu* là tuyên bố định tính, truyền cảm hứng về trạng thái cuối mong muốn ("Làm cho việc làm quen lần đầu trở nên dễ dàng"). *Kết quả then chốt* là một số ít (thường 2–4) kết quả đo được chứng minh mục tiêu đang được đáp ứng ("Tăng kích hoạt 7 ngày từ 40% lên 60%"; "Giảm phiếu hỗ trợ làm quen 30%"). Kết quả then chốt diễn đạt **kết quả**, không phải nhiệm vụ: "phát hành trình hướng dẫn mới" là nhiệm vụ cải trang thành kết quả.

Phân tầng OKR bằng *căn chỉnh*, không phải áp đặt: lãnh đạo đặt một số ít mục tiêu công ty; các đội đề xuất kết quả then chốt và mục tiêu riêng nối lên chúng. Đặt chúng theo nhịp đều đặn (thường hằng quý với khung hằng năm), xem xét giữa chu kỳ, và chấm điểm trung thực ở cuối. Giữ chúng tách khỏi đánh giá hiệu suất: OKR được chấm điểm để tính lương nhanh chóng bị đặt thấp. Xem chương 10.1 về cách OKR nối với quản lý danh mục và chương trình.

### Giám sát sức khỏe bằng KPI

Hãy phân biệt **[Chỉ số Hiệu suất Chính](https://en.wikipedia.org/wiki/Performance_indicator) (KPI)** với OKR. OKR mô tả *thay đổi* bạn muốn trong kỳ này; KPI mô tả *sức khỏe liên tục* bạn phải duy trì bất kể bạn đang đổi gì (thời gian hoạt động, tỷ lệ chuyển đổi, chi phí mỗi giao dịch, sự hài lòng của khách hàng). Một chỉ số có thể là cả hai (một KPI bạn đang chủ động cố dịch chuyển trở thành kết quả then chốt), nhưng hầu hết KPI là rào chắn bạn giám sát, không phải mục tiêu bạn chạy nước rút tới.

Hãy phân loại mọi chỉ số quan trọng là **dẫn đầu** (dự đoán và hành động được ngay bây giờ, như đăng ký dùng thử) hay **trễ** (xác nhận và chậm, như doanh thu hằng năm). Khám phá dựa vào chỉ báo dẫn đầu để lái trước khi chỉ báo trễ xác nhận. Coi chừng chỉ số phù phiếm tăng đều đặn nhưng không dự đoán gì (lượt xem trang thô, tổng số người dùng đã đăng ký); ưu tiên chỉ số tỷ lệ và theo nhóm vốn chống lách. Xem chương 7.3 và 7.4 về bộ máy phân tích và thí nghiệm đằng sau các thước đo này.

### Đặc tả thuộc tính chất lượng hệ thống một cách tường minh

Yêu cầu chức năng nói hệ thống làm gì. **Thuộc tính chất lượng hệ thống** (các "-tính": độ tin cậy, hiệu năng, khả năng mở rộng, bảo mật, khả năng tiếp cận, khả năng bảo trì, khả năng vận hành) nói nó phải làm tốt đến đâu. Chúng thường xuyên bị khám phá thiếu: mọi người giả định chúng, không ai đặc tả chúng, và chúng nổi lên thành sự cố sản xuất. Hãy coi chúng là đầu ra khám phá hạng nhất. Xác định **yêu cầu có ý nghĩa kiến trúc** (các đòi hỏi chất lượng định hình đáng kể kiến trúc) cho mỗi sáng kiến. Định lượng chúng ("độ trễ p99 dưới 200 ms ở tải gấp 10 lần hiện tại"; "WCAG (Hướng dẫn Tiếp cận Nội dung Web) 2.2 AA"; "mục tiêu thời gian khôi phục 15 phút"). Và nơi có thể, mã hóa chúng thành **hàm thích nghi** tự động (kiểm tra thực thi được liên tục xác minh một thuộc tính chất lượng) mà đường ống phân phối kiểm tra được. Đây là phần bổ sung phía khám phá cho chương 3.1 (nền tảng kiến trúc) và chương 3.5 (khả năng mở rộng, hiệu năng, khả năng phục hồi).

### Làm mọi mục tiêu thành SMART

Dù viết một kết quả then chốt, một tiêu chí chấp nhận, hay một mục tiêu chất lượng, hãy áp dụng phép thử **[SMART](https://en.wikipedia.org/wiki/SMART_criteria)**:

- **Cụ thể (Specific):** nêu một kết quả rõ ràng, không mơ hồ.
- **Đo được (Measurable):** có chỉ số và nguồn sự thật.
- **Đạt được (Achievable):** thực tế với ràng buộc và bằng chứng.
- **Liên quan (Relevant):** nối lên mục tiêu cao hơn và giá trị người dùng.
- **Có thời hạn (Time-bound):** có hạn chót hoặc ngày xem xét.

"Cải thiện hiệu năng" trượt mọi chữ cái. "Giảm thời gian thanh toán trung vị từ 8 giây xuống 3 giây cho người dùng di động trước cuối Q3, đo bằng giám sát người dùng thật" đạt cả năm. Tiêu chí SMART biến tham vọng mơ hồ thành tuyên bố có thể bị bác bỏ mà khám phá kiểm thử được và phân phối xác minh được.

### Chạy khám phá liên tục, dựa trên bằng chứng

Hãy cấu trúc khám phá thành một quy trình lặp lại được, không phải giai đoạn một lần:

1. **Cảm nhận.** Thu thập tín hiệu: nghiên cứu người dùng, dữ liệu hỗ trợ, phân tích, đầu vào thị trường và tuân thủ.
2. **Đóng khung.** Lập bản đồ cơ hội (một *cây cơ hội-giải pháp* nối kết quả mong muốn với nhu cầu người dùng và giải pháp ứng viên có thể dịch chuyển nó).
3. **Đặt giả thuyết.** Phát biểu giả định thành tuyên bố có thể bị bác bỏ: "Chúng tôi tin [thay đổi] sẽ gây ra [kết quả] cho [phân khúc], và chúng tôi sẽ biết nếu [thước đo] dịch chuyển."
4. **Thí nghiệm.** Xác thực các giả định rủi ro nhất bằng phép thử rẻ nhất: phỏng vấn, nguyên mẫu, phép thử cửa giả (quảng cáo một tính năng chưa xây để đo nhu cầu thật), [thí nghiệm A/B](https://en.wikipedia.org/wiki/A/B_testing) (so sánh ngẫu nhiên hai biến thể, chương 7.4).
5. **Quyết định.** Kiên trì, xoay hướng, hoặc bỏ, và đưa những cái sống sót vào tồn đọng phân phối kèm tiêu chí thành công SMART của chúng.

Đầu ra của quy trình khám phá không phải danh sách tính năng; đó là dòng các *canh bạc đã xác thực, đo được* sẵn sàng cho phân phối.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Mục tiêu dựa trên kết quả (OKR)** | Căn chỉnh các đội với tác động; trao quyền tự chủ về *cách làm* | Khó viết tốt; dễ bị điền bù bằng nhiệm vụ; quy kết nhiễu |
| **Lộ trình đầu ra/tính năng** | Khả đoán, dễ truyền đạt và ký hợp đồng | Thưởng phát hành hơn tác động; giấu rủi ro làm sai thứ |
| **Khám phá nặng từ đầu** | Giảm lãng phí xây dựng; yêu cầu mạnh | Làm chậm khởi đầu; rủi ro tê liệt phân tích; giả định vẫn chưa kiểm thử |
| **Khám phá hai đường liên tục** | Giảm rủi ro liên tục; phản hồi nhanh | Cần năng lực nghiên cứu và kỷ luật; khó lên lịch hơn |
| **Thuộc tính chất lượng tường minh dưới dạng mục tiêu SMART** | Ngăn bất ngờ "-tính"; kiểm toán được | Công sức định lượng; có thể ràng buộc quá mức khám phá sớm |

Căng thẳng trung tâm là **cam kết so với học**. Doanh nghiệp, và đặc biệt chính phủ, thường cần cam kết chắc cho ngân sách và hợp đồng, kéo về lộ trình đầu ra. Kết quả tốt cần chỗ để học, kéo về OKR và thí nghiệm. Hãy giải quyết thế này: cam kết chắc với *vấn đề và kết quả*, và giữ *giải pháp* lỏng.

## Câu hỏi để thảo luận với đội của bạn

1. **Ai trong đội bạn thực sự sở hữu khám phá, và họ có năng lực chạy nó liên tục thay vì trong một sprint một lần không?** Phát triển hai đường chỉ hiệu quả khi ai đó giữ đường khám phá mở mỗi tuần thay vì chỉ ở đầu quý. Trong tổ chức lớn, khám phá thường không có chủ sở hữu chuyên trách, nên nó sụp vào ai có thời gian rảnh, tức là không ai, và đội mặc định xây. Hãy mang bằng chứng: đếm trong mười tính năng gần nhất của bạn có bao nhiêu cái đi qua một giả thuyết có tài liệu và phép thử rẻ trước khi xây, so với đi thẳng vào tồn đọng. Trong bối cảnh doanh nghiệp và chính phủ, nơi một sáng kiến lệch hướng có thể lãng phí nhiều quý-đội, hãy nêu một chủ sở hữu sản phẩm hay một bộ ba (sản phẩm, thiết kế, kỹ thuật) chịu trách nhiệm cho vòng lặp cảm nhận-đóng khung-đặt giả thuyết-thí nghiệm-quyết định. Nếu không ai sở hữu nó, hãy bố trí nhân sự cho nó trước khi tranh luận bất cứ điều gì khác.

2. **Sáng kiến nào hiện tại của bạn có yêu cầu có ý nghĩa kiến trúc mà bạn chưa bao giờ định lượng, và bạn có thể mã hóa cái nào thành hàm thích nghi không?** Các "-tính" (độ tin cậy, hiệu năng, bảo mật, khả năng tiếp cận) bị giả định rồi nổi lên thành sự cố sản xuất. Hãy đi qua từng sáng kiến đang hoạt động, hỏi thuộc tính chất lượng nào định hình đáng kể kiến trúc, và kiểm tra mỗi cái có một con số và nguồn sự thật không: "p99 dưới 200 ms ở tải gấp 10," "WCAG 2.2 AA," "mục tiêu thời gian khôi phục 15 phút." Với doanh nghiệp và chính phủ, yêu cầu tiếp cận hay bảo mật không định lượng tạo phơi nhiễm pháp lý và kiểm toán trực tiếp. Tín hiệu cần mang là ba sự cố gần nhất của bạn: có bao nhiêu truy về một thuộc tính chất lượng không ai đặc tả? Nơi bạn biến được một mục tiêu thành hàm thích nghi tự động mà đường ống phân phối kiểm tra, hãy làm, vì một mục tiêu được đặc tả nhưng không thực thi sẽ trôi.

3. **Lần cuối bạn cam kết một giải pháp, bạn đã kiểm thử giả định rủi ro nhất trước, hay giả định dễ nhất?** Các đội đáng tin cậy xác thực giả định họ thoải mái nhất và bỏ qua cái thực sự sẽ giết ý tưởng. Với mỗi sáng kiến, hãy liệt kê các giả định của nó (tính mong muốn, khả thi kinh doanh, khả thi kỹ thuật) và xếp hạng theo "ý tưởng chết đến đâu nếu chúng ta sai ở đây," rồi nhắm phép thử rẻ nhất vào đầu danh sách đó. Điều này quan trọng ở quy mô vì một đội tự tin, cấp cao có thể cam kết một quý kỹ thuật cho niềm tin chưa kiểm thử, và chi phí vô hình cho đến ra mắt. Hãy mang hiện vật: giả thuyết gần nhất của bạn được phát biểu là "Chúng tôi tin [thay đổi] gây ra [kết quả] cho [phân khúc], đo bằng [chỉ số]," và hỏi bạn đã kiểm thử nó hay chỉ xây nó. Nếu bạn không nêu được giả định rủi ro nhất, bạn chưa sẵn sàng cam kết năng lực xây dựng.

4. **Bao nhiêu kết quả then chốt của bạn là kết quả thật, và bao nhiêu là nhiệm vụ hay ngày phát hành khoác áo kết quả?** Thất bại phổ biến nhất trong hoạch định dựa trên kết quả là điền bù kết quả then chốt bằng công việc bạn đã định làm ("ra mắt trình hướng dẫn mới") thay vì thay đổi công việc đó được cho là gây ra ("nâng kích hoạt 7 ngày từ 40% lên 60%"). Ở quy mô, điều này lặng lẽ đánh bại toàn bộ ý nghĩa: hàng chục đội báo xanh trong khi không chỉ số kinh doanh nào dịch chuyển, vì mọi người tự chấm điểm theo phát hành. Lực kéo đối lập là thật, lộ trình đầu ra dễ truyền đạt, ký hợp đồng và dự báo hơn, chính xác là lý do chúng len lại. Hãy mang bộ OKR hiện tại của bạn và đánh dấu mỗi kết quả then chốt là kết quả hay đầu ra, rồi kiểm tra việc chấm điểm OKR có vướng vào lương thưởng không, vì kết quả gắn với lương nhanh chóng bị đặt thấp. Với danh mục doanh nghiệp và chính phủ, nơi tài trợ được cam kết theo mục tiêu đã nêu, một lộ trình đầu ra không có thước đo kết quả là phát hiện kiểm toán đang chờ; hãy khăng khăng mỗi sáng kiến cam kết chắc với một vấn đề và một kết quả đo được trong khi giữ giải pháp lỏng.

5. **KPI nào của bạn sẽ tiếp tục leo lên ngay cả khi sản phẩm đang tệ đi, và rào chắn nào bảo vệ các chỉ số bạn đang chủ động cố dịch chuyển?** Mọi chỉ số bạn nâng thành mục tiêu mời gọi [Định luật Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law): một khi thước đo trở thành mục tiêu, người ta tối ưu thước đo thay vì thứ nó được cho là đại diện. Chỉ số phù phiếm (lượt xem trang thô, tổng số người dùng đã đăng ký) tăng đều đặn và không dự đoán gì, trong khi một kết quả then chốt đơn lẻ bị đuổi theo không có rào chắn có thể được đáp ứng bằng cách làm suy giảm thứ bạn chưa bao giờ nêu tên. Căng thẳng là chỉ báo dẫn đầu cho phép bạn lái sớm nhưng nhiễu và dễ lách, trong khi chỉ báo trễ đáng tin nhưng xác nhận quá muộn để hành động. Hãy mang bản kiểm kê chỉ số của bạn được phân loại là dẫn đầu hay trễ và là mục tiêu hay rào chắn, và kiểm thử sức chịu đựng từng mục tiêu bằng cách hỏi "một đội thông minh có thể đạt con số này thế nào trong khi làm sản phẩm tệ đi." Trong bối cảnh bị quản lý và công, hãy công bố rào chắn cạnh mục tiêu, vì cơ quan giám sát chỉ thấy chỉ số tiêu đề không phân biệt được giá trị công thật với con số bị lách.

6. **Khi phân phối phát hành một thứ, kết quả thực tế quay lại khám phá thế nào, hay vòng lặp vẫn mở?** Phát triển hai đường chỉ cộng dồn nếu kết quả đã giao chảy ngược làm bằng chứng cho vòng tiếp theo; khi vòng lặp vẫn mở, các đội phát hành, ăn mừng, và không bao giờ biết canh bạc có sinh lời không, nên cùng các giả định chưa kiểm thử tái diễn. Trong tổ chức lớn, đường phản hồi là nơi trách nhiệm dễ rơi qua khe nhất: phân phối sở hữu bản phát hành, phân tích sở hữu bảng điều khiển, và không ai sở hữu việc so sánh kết quả then chốt đã hứa với kết quả quan sát. Hãy mang mười sáng kiến đã phát hành gần nhất và hỏi, với mỗi cái, có ai kiểm tra chỉ số kết quả so với mục tiêu SMART ban đầu không và việc kiểm tra đó có đổi quyết định tiếp theo nào không. Với chương trình doanh nghiệp và chính phủ cam kết tài trợ nhiều năm, hãy nêu nhịp và chủ sở hữu cho việc cho nghỉ hưu hay thu hẹp phạm vi các tính năng không dịch chuyển được chỉ số, vì một tính năng đã phát hành không ai xem lại trở thành chi phí vĩnh viễn không có rà soát chịu trách nhiệm.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với đội nhỏ xíu và ít đường băng, quy trình khám phá của bạn cố ý nhẹ nhưng không bao giờ bị bỏ: một ngày phỏng vấn khách hàng và một phép thử cửa giả gần như không tốn gì so với nhiều tuần một bản xây sai đốt đi. Chọn một chỉ báo dẫn đầu đại diện cho giá trị cốt lõi của bạn, phát biểu mỗi canh bạc thành một giả thuyết có thể bị bác bỏ duy nhất, và khai tử ý tưởng trước khi viết mã thay vì sau. OKR chính thức là quá mức với năm người; một kết quả đo được trung thực mỗi chu kỳ là đủ để giữ tốc độ khỏi thành chuyển động không tiến bộ.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có nhà nghiên cứu hay nhà phân tích sản phẩm riêng, nên hãy coi khám phá là thói quen, không phải vai trò: vài cuộc trò chuyện có cấu trúc với khách hàng thật và một chỉ số đơn giản bạn đã thu thập. Câu hỏi mua-so-với-xây chi phối, vì hầu hết thuộc tính chất lượng (độ tin cậy, bảo mật, khả năng tiếp cận) rẻ hơn để lấy từ nhà cung cấp uy tín so với tự đặc tả và thực thi. Hãy viết một hai mục tiêu SMART để bạn nói được một công cụ đã mua hay bản xây nhỏ có thực sự dịch chuyển kết quả không, và tránh cam kết ngân sách khan hiếm cho tính năng không ai xác thực là được muốn.

**Doanh nghiệp lớn.** Quy mô biến khám phá thành bài toán phối hợp qua hàng chục đội: không có nhịp OKR chung và định nghĩa chung về "kết quả," mục tiêu cục bộ trôi và trùng lặp, và các canh bạc lệch cộng dồn thành danh mục lãng phí. Hãy chuẩn hóa cách yêu cầu có ý nghĩa kiến trúc được định lượng và mã hóa chúng thành hàm thích nghi để thuộc tính chất lượng được quản trị, không phải giả định. Quản lý khám phá như danh mục với tiêu chí khai tử tường minh và vòng lặp đưa chỉ số kết quả đã giao ngược vào chu kỳ tiếp theo, để lãnh đạo lái theo tác động thay vì tồn đọng tính năng.

**Chính phủ.** Mua sắm và tài trợ nhiều năm đòi cam kết chắc, kéo mạnh về hợp đồng đầu ra, vậy mà giá trị công sống trong kết quả: công dân được phục vụ, thời gian chờ cắt giảm, gánh nặng giảm. Hãy đóng khung chương trình quanh kết quả công đo được và thuộc tính chất lượng không thể thương lượng (tiếp cận WCAG, ngôn ngữ đơn giản, bảo mật), và làm bằng chứng khám phá, gồm kiểm thử khả dụng với người dùng công nghệ hỗ trợ, thành một phần hồ sơ mà cơ quan giám sát kiểm toán được. Định nghĩa thành công là kết quả của người đóng thuế hay công dân thay vì mô-đun được giao, để "chúng tôi xây đúng điều hợp đồng nói" không bao giờ thay thế được một kết quả chưa bao giờ thành hiện thực.

## Ví dụ

**Công ty khởi nghiệp.** Một đội giai đoạn hạt giống bốn người xây ứng dụng lập lịch cho tiệm làm tóc bị cám dỗ xây tiện ích đặt lịch trực tuyến vì vài người dùng ồn ào đã hỏi. Thay vào đó họ chạy một tuần khám phá: năm cuộc phỏng vấn chủ tiệm, một nút cửa giả "Đặt lịch trực tuyến" trên trang tiếp thị, và một chỉ báo dẫn đầu duy nhất (phần trăm cuộc hẹn kết thúc bằng vắng mặt). Các cuộc phỏng vấn và dữ liệu nhấp chuột cho thấy vắng mặt, không phải đặt lịch, là nỗi đau thật, nên họ viết một kết quả then chốt SMART (cắt vắng mặt từ 22% xuống dưới 10% cho các tiệm thử nghiệm quý này) và phát hành tính năng đặt cọc-và-nhắc nhở nhỏ trước, khai tử tiện ích đặt lịch trước khi viết một dòng.

**Doanh nghiệp lớn.** Nhóm thanh toán của một ngân hàng bán lẻ thay lộ trình đếm tính năng bằng ba OKR hằng quý, một trong đó là "Làm thanh toán hằng ngày có cảm giác tức thì" với các kết quả then chốt cho thời gian xác nhận chuyển khoản p95, tỷ lệ thành công lần thử đầu, và liên hệ hỗ trợ liên quan thanh toán. Thuộc tính chất lượng hệ thống được đặc tả từ đầu (khả dụng 99,99%, xác nhận dưới một giây, phạm vi PCI-DSS (Tiêu chuẩn Bảo mật Dữ liệu Ngành Thẻ Thanh toán) được tối thiểu hóa) và nối vào phân phối như hàm thích nghi. Khám phá chạy phỏng vấn khách hàng hằng tuần và phép thử cửa giả trước khi cam kết kỹ thuật. Hai tính năng ứng viên bị khai tử trong khám phá vì không dịch chuyển được chỉ báo dẫn đầu (tiết kiệm ước tính hai quý công sức xây), trong khi một bản sửa độ trễ nhỏ hơn, kém hào nhoáng dịch chuyển kết quả then chốt nhiều nhất.

**Chính phủ.** Một cơ quan thuế quốc gia hiện đại hóa khai thuế trực tuyến đặt mục tiêu chương trình "Giảm gánh nặng khai thuế cho người nộp thuế bình thường," với các kết quả then chốt SMART: cắt thời gian khai trung vị từ 45 xuống 20 phút, nâng tỷ lệ hoàn tất tự phục vụ thành công từ 60% lên 85%, và đáp ứng WCAG 2.2 AA và tiêu chuẩn ngôn ngữ đơn giản như thuộc tính chất lượng không thể thương lượng. KPI (thời gian hoạt động trong mùa khai thuế, khối lượng tổng đài) được giám sát làm rào chắn. Khám phá dùng kiểm thử khả dụng có điều phối với người nộp thuế thật, gồm người dùng công nghệ hỗ trợ, trước mỗi bản phát hành. Vì thành công được định nghĩa là kết quả của người nộp thuế thay vì mô-đun được giao, chương trình có thể cho cơ quan giám sát thấy giá trị công đo được, không chỉ chi tiêu.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của một quy trình khám phá bị chi phối bởi **lãng phí tránh được**. Kinh nghiệm ngành, được vọng lại trong các chương trình thí nghiệm có kiểm soát ở các hãng công nghệ lớn, liên tục thấy một phần lớn tính năng được xây, thường được trích dẫn khoảng một nửa hoặc hơn, không tạo cải thiện đo được hoặc chủ động làm hại chỉ số mục tiêu. Giả sử ngay cả một phần tư năng lực xây dựng của một đội dành cho ý tưởng mà khám phá lẽ ra khai tử rẻ. Khi đó quy trình tự hoàn vốn nhiều lần: một tuần nghiên cứu người dùng và phép thử cửa giả gần như không tốn gì so với một quý kỹ thuật, cộng gánh nặng bảo trì liên tục của một tính năng không dùng.

Khung **[tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (TCO) quan trọng vì tính năng chưa xác thực không miễn phí sau ra mắt. Mỗi tính năng đã phát hành mang chi phí vĩnh viễn: bảo trì, kiểm thử, bề mặt bảo mật, hỗ trợ và gánh nặng nhận thức (chương 10.4). Khai tử một ý tưởng tệ trong khám phá tránh được không chỉ chi phí xây mà cả cái đuôi sở hữu. Thuộc tính chất lượng tường minh theo cùng logic: đặc tả độ tin cậy và khả năng tiếp cận thành mục tiêu SMART từ đầu rẻ hơn nhiều so với trang bị sau sự cố, vi phạm hay kiện tụng.

Để lập luận với ban lãnh đạo, hãy đổi cuộc trò chuyện từ "chúng ta phát hành bao nhiêu" sang "chúng ta dịch chuyển các chỉ số quan trọng bao nhiêu," và cho thấy vài ví dụ cụ thể về tính năng đắt tiền không dịch chuyển gì. Chi phí áp dụng khiêm tốn (năng lực nghiên cứu, nhịp OKR, và kỷ luật viết tiêu chí SMART), và rủi ro chính của việc *không* áp dụng là im lặng, không đếm, và cộng dồn.

## Phản mẫu và cạm bẫy

- **Lộ trình tính năng khoác áo chiến lược:** danh sách đầu ra không có kết quả hay thước đo nêu rõ.
- **Kết quả then chốt là nhiệm vụ:** "ra mắt X" thay vì "cải thiện Y thêm Z."
- **Sân khấu OKR:** mục tiêu được viết, cất đi, và không bao giờ được xem xét hay chấm điểm.
- **OKR đặt thấp hoặc anh hùng:** mục tiêu đặt để bảo đảm 100% (không học được gì) hoặc kéo dãn viển vông không có kế hoạch.
- **Thuộc tính chất lượng không đặc tả:** độ tin cậy, bảo mật và khả năng tiếp cận được giả định thay vì định lượng, rồi bị phát hiện trong sản xuất.
- **Chỉ số phù phiếm:** thước đo luôn đi lên và không dự đoán gì.
- **Khám phá như giai đoạn một lần:** một "sprint khám phá" ban đầu, rồi không còn xác thực tiếp.
- **Xây giải pháp trước khi kiểm thử giả định:** bỏ qua thí nghiệm rẻ nhất vì đội tự tin.
- **Ám ảnh chỉ số và [Định luật Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law):** một khi thước đo trở thành mục tiêu, nó thôi là thước đo tốt; cân bằng bằng KPI rào chắn.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Công việc được xác định là tính năng trên lộ trình và thành công là "chúng ta đã phát hành." Không có thước đo kết quả hay mục tiêu chất lượng tường minh; khám phá xảy ra tình cờ, nếu có, và quyết định do ý kiến to nhất thúc đẩy.
- **Mức 2, Phát triển:** OKR và KPI tồn tại ở một số đội mà không phải các đội khác; mục tiêu được nêu nhưng thường mang hình dạng đầu ra; thuộc tính chất lượng được gọi tên nhưng không định lượng. Một đội có thể chạy "sprint khám phá" một lần, rồi thôi xác thực khi xây bắt đầu, nên thực hành thật nhưng không nhất quán trong tổ chức.
- **Mức 3, Chuẩn hóa:** Một nhịp OKR nhất quán căn chỉnh với chiến lược, kết quả then chốt SMART, và thuộc tính chất lượng được đặc tả, kiểm thử được, được lập tài liệu và kỳ vọng toàn tổ chức. Khám phá là hoạt động được công nhận, có nhân sự với giả thuyết và thí nghiệm, và yêu cầu có ý nghĩa kiến trúc được xác định cho mỗi sáng kiến thay vì giả định.
- **Mức 4, Quản lý:** Danh mục được đo theo đường cơ sở. Chỉ báo dẫn đầu và trễ, tỷ lệ trúng của khám phá, và kết quả mỗi canh bạc đã phát hành thực sự dịch chuyển được theo dõi so với mục tiêu SMART của nó; giả thuyết được chấm điểm dựa trên bằng chứng và tiêu chí khai tử được thực thi; hàm thích nghi báo cáo sự tuân thủ thuộc tính chất lượng liên tục, nên độ trôi khỏi mục tiêu độ tin cậy, hiệu năng hay tiếp cận đã đặc tả được bắt bằng dữ liệu thay vì trong sự cố.
- **Mức 5, Điều phối:** Khám phá hai đường liên tục được tích hợp với danh mục, rủi ro và lập ngân sách; các canh bạc đã xác thực chảy đều đến phân phối và chỉ số kết quả tự động quay lại lái vòng tiếp theo. Chỉ báo dẫn đầu lái đầu tư, và tổ chức thường lệ cho nghỉ hưu, thu hẹp phạm vi và cân bằng lại sáng kiến dựa trên bằng chứng, thích ứng chính quy trình khi thị trường và chỉ số dịch chuyển.

## Ý tưởng để thảo luận

1. Nhìn lộ trình hiện tại của bạn: bao nhiêu mục nêu kết quả đo được so với chỉ một tính năng để phát hành?
2. Kết quả then chốt nào của đội bạn thực ra là nhiệm vụ cải trang, và bạn sẽ viết lại chúng thế nào?
3. Sản phẩm của bạn phụ thuộc vào thuộc tính chất lượng hệ thống nào mà chưa bao giờ được định lượng tường minh?
4. Thí nghiệm rẻ nhất có thể đã khai tử tính năng thất bại gần nhất của bạn trước khi bạn xây nó là gì?
5. Làm sao bạn giải quyết căng thẳng giữa cam kết chắc mà ngân sách/mua sắm đòi và việc học mà kết quả tốt cần?
6. KPI nào của bạn sẽ tiếp tục tăng ngay cả khi sản phẩm đang tệ đi?

## Những điểm cần ghi nhớ

- Quy trình khám phá quyết định *cái gì* và *vì sao*, và xác định thành công **trước** khi phân phối cam kết nguồn lực.
- Dùng **OKR** cho thay đổi bạn muốn, **KPI** cho sức khỏe bạn duy trì, và phân loại chỉ số là dẫn đầu hay trễ.
- Coi **thuộc tính chất lượng hệ thống** là yêu cầu tường minh, được định lượng, kiểm thử được, không phải giả định.
- Làm mọi mục tiêu, kết quả then chốt và tiêu chí chấp nhận thành **SMART**.
- Chạy khám phá **liên tục và song song** với phân phối; xác thực giả định rủi ro nhất một cách rẻ.
- ROI chi phối là **lãng phí tránh được**: cả chi phí xây lẫn TCO vĩnh viễn của tính năng không dùng.
- Khép vòng lặp: **chỉ số kết quả** đã giao (chương 11.2) là bằng chứng chính cho vòng khám phá tiếp theo.

## Tài liệu tham khảo và đọc thêm

- *Measure What Matters*, của John Doerr (về OKR).
- *Radical Focus*, của Christina Wodtke (về OKR trong thực hành).
- *Continuous Discovery Habits*, của Teresa Torres (cây cơ hội-giải pháp, khám phá hai đường).
- *Inspired* và *Empowered*, của Marty Cagan (khám phá sản phẩm và đội kết quả).
- *Lean Analytics*, của Alistair Croll và Benjamin Yoskovitz (chỉ báo dẫn đầu, chỉ số phù phiếm).
- *The Lean Startup*, của Eric Ries (xây-đo-học, học có xác thực).
- *Escaping the Build Trap*, của Melissa Perri (kết quả hơn đầu ra).
- *Outcomes Over Output*, của Joshua Seiden.
- *Software Architecture in Practice*, của Bass, Clements, Kazman (thuộc tính chất lượng).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): nguồn gốc của tiêu chí SMART.
