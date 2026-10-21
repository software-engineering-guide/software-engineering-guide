# 10.2 Rủi ro, kiểm toán và đảm bảo

## Tổng quan và động lực

Rủi ro, kiểm toán và đảm bảo là thực hành hiểu điều gì có thể sai: với phần mềm của bạn và với tổ chức xây dựng và vận hành nó. Bạn quyết định làm gì với nó. Rồi bạn chứng minh rằng các kiểm soát bạn tuyên bố có thực sự hoạt động. Bạn chứng minh điều đó với lãnh đạo, cơ quan quản lý, kiểm toán viên và công chúng. Ở một đội nhỏ, [quản lý rủi ro](https://en.wikipedia.org/wiki/Risk_management) phần lớn ngầm định. Vài người giữ toàn bộ bức tranh trong đầu. Ở một doanh nghiệp lớn hay cơ quan chính phủ, bạn phải làm rủi ro tường minh và có hệ thống. Không một người nào thấy được toàn bộ bề mặt. Hậu quả của thất bại lớn và thường bị quy định. Lòng tin phải được chứng minh, không phải giả định.

Điều này quan trọng hơn với các tổ chức lớn, vì ba lý do. Thứ nhất, quy mô nhân lên mức phơi nhiễm. Nhiều hệ thống, nhà cung cấp, dữ liệu, con người và kết nối hơn nghĩa là nhiều cách thất bại hơn và bán kính ảnh hưởng lớn hơn khi thất bại đến. Thứ hai, các tổ chức lớn chịu trách nhiệm trước người ngoài (cơ quan quản lý, kiểm toán viên, hội đồng quản trị, tòa án và công dân) muốn bằng chứng, không phải lời đảm bảo. Thứ ba, sự tập trung len lỏi lặng lẽ. Nền tảng dùng chung, nhà cung cấp chung và thành phần tái sử dụng tạo ra [điểm đơn thất bại](https://en.wikipedia.org/wiki/Single_point_of_failure) mà không đội nào để ý, nhưng có thể hạ cả doanh nghiệp cùng lúc.

Chương này nhằm mang kỷ luật quản lý rủi ro doanh nghiệp vào phần mềm mà không bóp nghẹt phân phối bằng quan liêu. Làm tốt, rủi ro và đảm bảo không phải thuế đánh vào kỹ thuật. Chúng là cách một tổ chức lớn giành quyền vận hành ở quy mô. Chúng biến "hãy tin chúng tôi" thành "đây là bằng chứng."

## Các nguyên tắc chính

- **Rủi ro được quản lý, không bị loại bỏ.** Công việc là nhận diện, đánh giá, xử lý và theo dõi rủi ro tới mức chấp nhận được, không phải giả vờ nó giảm được về không.
- **Sở hữu rủi ro nơi nó được tạo ra.** Đội xây và vận hành một hệ thống sở hữu rủi ro của nó; các chức năng trung tâm đặt tiêu chuẩn và kiểm tra, chúng không hấp thụ trách nhiệm giải trình.
- **Bằng chứng hơn tuyên bố.** Một kiểm soát bạn không chứng minh được là kiểm soát bạn không có.
- **Liên tục hơn tại một thời điểm.** [Kiểm toán](https://en.wikipedia.org/wiki/Audit) hằng năm bắt sự trôi dạt quá muộn; kiểm soát nên được theo dõi liên tục và tự động nơi có thể.
- **Bên thứ ba thừa hưởng rủi ro của bạn.** Điểm yếu của nhà cung cấp thành điểm yếu của bạn; rủi ro chuỗi cung ứng là rủi ro của bạn.
- **Tập trung là rủi ro hạng nhất.** Hiệu quả nhờ hợp nhất lặng lẽ tạo ra điểm đơn thất bại phải được nêu tên và quản lý.
- **Tương xứng.** Khớp độ sâu kiểm soát với hậu quả; coi mọi hệ thống là mức trọng yếu tối đa phí công sức và sinh ra né tránh.

## Khuyến nghị

### Áp dụng quản lý rủi ro doanh nghiệp vào phần mềm

Hãy áp dụng một khung và từ vựng rủi ro chung toàn tổ chức, để bạn so sánh và cộng dồn được rủi ro. Giữ một [sổ đăng ký rủi ro](https://en.wikipedia.org/wiki/Risk_register) cho mỗi hệ thống đáng kể, và gộp các sổ riêng lên một cái nhìn danh mục. Với mỗi rủi ro, ghi khả năng xảy ra, tác động, chủ sở hữu, kiểm soát hiện có, và quyết định xử lý (chấp nhận, giảm thiểu, chuyển giao hoặc tránh). Dùng mô hình ["ba tuyến"](https://en.wikipedia.org/wiki/Three_lines_of_defence) để tách nhiệm vụ: các đội sở hữu và quản lý rủi ro của mình (tuyến thứ nhất), các chức năng rủi ro và tuân thủ đặt chính sách và phản biện (tuyến thứ hai), và kiểm toán nội bộ đảm bảo độc lập (tuyến thứ ba). Đặt [khẩu vị rủi ro](https://en.wikipedia.org/wiki/Risk_appetite) tường minh ở cấp cao nhất, để các đội biết tổ chức sẵn lòng mang bao nhiêu rủi ro thay vì mỗi đội tự đoán.

### Đảm bảo rủi ro bên thứ ba và chuỗi cung ứng

Hãy kiểm kê nhà cung cấp và, quan trọng không kém, các phụ thuộc phần mềm của bạn, gồm cả thành phần mã nguồn mở bắc cầu. Đánh giá từng nhà cung cấp tương xứng với quyền truy cập và mức trọng yếu họ mang. Dựa vào các chứng thực được công nhận (như SOC 2, một báo cáo kiểm toán độc lập về kiểm soát bảo mật của nhà cung cấp, hay báo cáo [ISO 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)) thay vì phát minh lại bảng câu hỏi nơi bằng chứng tốt đã tồn tại. Yêu cầu danh mục vật liệu phần mềm (SBOM) cho các thành phần bạn tiêu thụ, để bạn trả lời được "chúng ta có bị ảnh hưởng không?" ngay khoảnh khắc một lỗ hổng nổ ra. Xây tính toàn vẹn chuỗi cung ứng vào đường ống: xác minh nguồn gốc, ghim và ký hiện vật, và kiểm soát cái gì vào bản dựng của bạn. Viết điều khoản bảo mật, thông báo vi phạm, quyền kiểm toán và thoát vào hợp đồng. Đánh giá lại nhà cung cấp theo nhịp đều đặn, thay vì chỉ lúc tiếp nhận.

### Xây dấu vết kiểm toán, bằng chứng và giám sát kiểm soát liên tục

Hãy thiết kế hệ thống để tạo bằng chứng như sản phẩm phụ của việc chạy. Ghi nhận nhật ký kiểm toán bất biến, có dấu thời gian, lộ dấu can thiệp về các hành động đáng kể: ai làm gì, với cái gì, khi nào, và với sự ủy quyền nào. Bảo vệ các nhật ký đó khỏi bị sửa bởi chính những người chúng ghi lại. Ưu tiên kiểm soát được tự động hóa và giám sát liên tục: chính sách dưới dạng mã chặn thay đổi không tuân thủ, cổng đường ống thực thi rà soát bắt buộc, và bảng điều khiển cho thấy trạng thái kiểm soát theo thời gian thực. Giám sát kiểm soát liên tục biến kiểm toán từ cuộc chạy đua định kỳ để dựng lại bằng chứng thành dòng đảm bảo đều đặn. Nó bắt sự trôi dạt trong vài giờ thay vì ở lần rà soát hằng năm kế tiếp.

### Quản trị liên tục kinh doanh và khôi phục thảm họa

Hãy biết tổ chức của bạn phải tiếp tục làm gì, và nhanh đến đâu, nếu hệ thống thất bại. Chạy phân tích tác động kinh doanh để đặt mục tiêu thời gian khôi phục và điểm khôi phục (RTO/RPO) cho mỗi dịch vụ dựa trên nhu cầu kinh doanh, không phải sự tiện lợi của kỹ thuật. Rồi duy trì các kế hoạch [liên tục kinh doanh](https://en.wikipedia.org/wiki/Business_continuity_planning) và [khôi phục thảm họa](https://en.wikipedia.org/wiki/Disaster_recovery) (DR) và (đây là phần các tổ chức bỏ qua) thực sự kiểm thử chúng. Chạy diễn tập đều đặn gồm chuyển dự phòng đầy đủ và diễn tập khôi phục từ sao lưu. Sao lưu chưa kiểm thử và chuyển dự phòng chưa kiểm thử là giả định, không phải năng lực. Quản trị điều này ở cấp doanh nghiệp, để bạn hiểu phụ thuộc xuyên hệ thống trước một thảm họa thật, không phải trong lúc đó.

### Quản lý rủi ro tập trung và điểm đơn thất bại

Hãy chủ động đi tìm những nơi nhiều dịch vụ phụ thuộc vào một thứ: một vùng đám mây duy nhất, một nhà cung cấp xác thực, một nhà cung cấp then chốt, một cơ sở dữ liệu, một con người. Lập bản đồ các tập trung này ở cấp danh mục, vì từng đội không thấy được chúng. Với những cái trọng yếu nhất, giảm tập trung qua dự phòng, chiến lược đa vùng hoặc đa nhà cung cấp, và suy giảm êm, đồng thời cân nhắc trung thực chi phí và độ phức tạp tăng thêm. Nơi bạn chấp nhận tập trung vì hiệu quả, hãy biến nó thành quyết định có ý thức, có tài liệu, có chủ sở hữu với kế hoạch dự phòng đã kiểm thử. Đừng để nó là tai nạn không ai để ý cho đến khi nó thất bại.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Kiểm soát chính thức nặng | Đảm bảo mạnh; sẵn sàng cho kiểm toán và cơ quan quản lý | Làm chậm phân phối; mời gọi tuân thủ đánh dấu ô và né tránh |
| Kiểm soát nhẹ dựa trên rủi ro | Nhanh; công sức tập trung vào phơi nhiễm thật | Đòi phán đoán trưởng thành; có khoảng trống nếu đánh giá rủi ro kém |
| Kiểm toán tại một thời điểm | Quen thuộc; khoảnh khắc đạt/trượt rõ ràng | Bắt trôi dạt muộn; khuyến khích chỉ chuẩn bị cho ngày kiểm toán |
| Giám sát kiểm soát liên tục | Phát hiện trôi dạt sớm; ít chạy đua kiểm toán | Đầu tư tự động hóa ban đầu; chi phí công cụ và đo đạc |
| Hợp nhất / một nhà cung cấp | Chi phí thấp hơn; đơn giản hơn; đòn bẩy khối lượng | Rủi ro tập trung; điểm đơn thất bại; khóa chặt |
| Dự phòng / đa nhà cung cấp | Khả năng phục hồi; không điểm đơn thất bại | Chi phí và độ phức tạp cao hơn; nhiều thứ hơn để bảo trì và bảo mật |

Đánh đổi lặp lại là đảm bảo so với vận tốc. Cách giải quyết là tương xứng cộng tự động hóa. Kiểm soát nặng đồng loạt làm chậm mọi người và, tệ hơn, dạy các đội coi tuân thủ là sân khấu để lách. Kiểm soát thuần nhẹ phụ thuộc vào phán đoán mà không phải đội nào cũng có. Lối đi: khớp độ sâu kiểm soát với hậu quả, và tự động hóa kiểm soát vào đường ống phân phối để đảm bảo đến từ hành động xây dựng thay vì gắn vào sau. Đánh đổi tập trung (hiệu quả so với khả năng phục hồi) không có câu trả lời phổ quát. Hãy quyết định có ý thức cho từng phụ thuộc trọng yếu, với rủi ro chấp nhận được ghi lại và kế hoạch dự phòng đã kiểm thử.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn sẽ phân loại hệ thống theo mức trọng yếu thế nào để độ sâu kiểm soát khớp với hậu quả?** Tương xứng là cách giải quyết căng thẳng đảm bảo-so-với-vận-tốc: coi mọi hệ thống là mức trọng yếu tối đa và bạn phí công sức và dạy các đội lách tuân thủ, coi không gì là trọng yếu và bạn bị bắt gặp phơi nhiễm. Bạn cần một phân bậc tường minh gắn mỗi hệ thống với khẩu vị rủi ro đặt ở cấp cao nhất, để một công cụ nội bộ rủi ro thấp và một hệ thống trợ cấp hướng công dân không mang cùng kiểm soát. Hãy mang bằng chứng vào cuộc thảo luận: liệt kê hệ thống, dữ liệu và bán kính ảnh hưởng mỗi cái mang, và các kiểm soát đang áp dụng, rồi tìm sự không khớp theo cả hai hướng. Câu trả lời nên đổi cái bạn tự động hóa vào đường ống so với cái để cho phán đoán con người, và nên cho các đội cơ sở rõ ràng cho đánh đổi hằng ngày thay vì đoán. Không có các bậc đã thống nhất, tương xứng chỉ là một từ.

2. **Bạn có trả lời được "chúng ta có bị ảnh hưởng không?" trong vài phút lần tới khi một phụ thuộc trọng yếu công bố lỗ hổng không?** Khi một thành phần được dùng rộng rãi hỏng, các tổ chức phản ứng nhanh đã có bản kiểm kê SBOM ánh xạ mọi nơi một thành phần được dùng, gồm cả phụ thuộc mã nguồn mở bắc cầu. Nếu câu trả lời trung thực của bạn là nhiều ngày, hoặc "chúng ta sẽ phải đi tìm," khoảng trống đó là sự khác biệt giữa ứng phó được kiềm chế và cuộc chạy đua. Hãy mang bằng chứng: chọn một thư viện thật bạn phụ thuộc và đo bao lâu để liệt kê mọi dịch vụ phát hành nó. Câu trả lời nên thúc đẩy đầu tư vào tạo SBOM trong đường ống, ghim và ký hiện vật, và xác minh nguồn gốc, để phơi nhiễm là một truy vấn thay vì một cuộc điều tra. Đây là rủi ro chuỗi cung ứng, và điểm yếu của nhà cung cấp đã là điểm yếu của bạn.

3. **Dịch vụ nào được diễn tập chuyển dự phòng đầy đủ và khôi phục từ sao lưu, bao lâu một lần, và ai ký xác nhận chúng đạt?** Sao lưu chưa kiểm thử và chuyển dự phòng chưa kiểm thử là giả định, không phải năng lực, và các tổ chức phát hiện điều này trong một thảm họa thật thay vì trước nó. Chạy phân tích tác động kinh doanh để đặt mục tiêu thời gian khôi phục và điểm khôi phục cho mỗi dịch vụ từ nhu cầu kinh doanh, rồi gắn tần suất diễn tập với các bậc đó. Hãy mang bằng chứng: với dịch vụ trọng yếu nhất của bạn, lần cuối một khôi phục đầy đủ thực sự được thực hành từ đầu đến cuối là khi nào, và nó có đạt RTO đã nêu không? Câu trả lời nên tạo ra lịch diễn tập DR thường lệ, xuyên hệ thống mà kết quả được báo cáo cho lãnh đạo, vì quản trị ở cấp doanh nghiệp là thứ làm lộ phụ thuộc xuyên hệ thống mà một đội đơn lẻ không thấy. Nơi bạn chấp nhận tập trung một vùng hay một nhà cung cấp vì hiệu quả, hãy biến nó thành quyết định có ý thức, có tài liệu, có chủ sở hữu với kế hoạch dự phòng đã kiểm thử.

4. **Kiểm soát nào của bạn tạo bằng chứng tự động như sản phẩm phụ của việc chạy, và cái nào vẫn phụ thuộc vào ai đó gom bằng chứng lúc kiểm toán?** Một kiểm soát bạn không chứng minh được là kiểm soát bạn không có, và các tổ chức qua kiểm toán bình tĩnh là những tổ chức có đường ống phát ra bản ghi bất biến, có dấu thời gian về các hành động đáng kể mà không ai phải nhớ thu thập. Lực kéo đối lập là thật: tự động hóa kiểm soát thành chính sách dưới dạng mã và giám sát liên tục tốn công sức kỹ thuật ban đầu, trong khi thu thập bằng chứng tại một thời điểm cảm giác rẻ hơn cho đến khi cuộc chạy đua hằng năm đến và sự trôi dạt đã tích lũy nhiều tháng. Hãy mang bằng chứng vào cuộc thảo luận: với vài kiểm soát hàng đầu của bạn, hỏi bằng chứng có tồn tại trong kho lộ dấu can thiệp ngay bây giờ không, những người mà nhật ký ghi lại có sửa được chúng không, và mất bao nhiêu giờ để dựng lại một quý hoạt động. Câu trả lời nên lái đầu tư về giám sát kiểm soát liên tục và cổng đường ống hơn chứng thực thủ công. Trong bối cảnh doanh nghiệp và chính phủ, vị thế mạnh nhất là cho kiểm toán viên quyền đọc vào bảng điều khiển kiểm soát trực tiếp, biến kiểm toán từ dựng lại định kỳ thành lấy mẫu liên tục một dòng bằng chứng đều đặn.

5. **Ba tuyến phòng thủ có thực sự vận hành như nhiệm vụ tách biệt, hay quyền sở hữu đã nhòe đến mức những người xây một hệ thống cũng đảm bảo nó?** Độc lập là toàn bộ ý nghĩa của mô hình: các đội sở hữu và quản lý rủi ro của mình ở tuyến thứ nhất, rủi ro và tuân thủ đặt chính sách và phản biện ở tuyến thứ hai, và kiểm toán nội bộ đảm bảo độc lập ở tuyến thứ ba, và khi các vai trò đó sụp vào nhau, đảm bảo thành bài tập về nhà tự chấm. Căng thẳng là đẩy quyền sở hữu rủi ro ra các đội phân phối có thể cảm giác chậm và gây tranh cãi hơn việc để một chức năng trung tâm hấp thụ, vậy mà hấp thụ trung tâm lặng lẽ gỡ trách nhiệm giải trình khỏi nơi rủi ro thực sự được tạo ra. Hãy mang bằng chứng: lập bản đồ một quyết định rủi ro đáng kể gần đây và nêu tên ai sở hữu nó, ai phản biện nó, và ai đảm bảo độc lập, rồi kiểm tra có nhóm đơn lẻ nào đóng hai trong các vai đó không. Cuộc thảo luận cũng nên làm lộ liệu khẩu vị rủi ro có được đặt tường minh ở cấp cao nhất không, vì không có nó mỗi đội tự đoán mang bao nhiêu rủi ro. Với doanh nghiệp bị quản lý hay cơ quan chính phủ, một quan chức chịu trách nhiệm chính thức chấp nhận rủi ro dư, khác với đội đã xây hệ thống, thường là yêu cầu cứng thay vì điều tốt đẹp.

6. **Nhiều dịch vụ của bạn lặng lẽ phụ thuộc vào một thứ ở đâu, và ai ở cấp danh mục sở hữu sự tập trung đó?** Hợp nhất vào một vùng đám mây duy nhất, một nhà cung cấp xác thực, một nhà cung cấp then chốt, một cơ sở dữ liệu, hay một con người mang lại hiệu quả thật và đòn bẩy khối lượng, và nó cũng đáng tin cậy tạo ra điểm đơn thất bại mà không đội nào thấy được vì mỗi đội chỉ thấy lát cắt của mình. Đánh đổi trung thực là hiệu quả so với khả năng phục hồi, và nó không có câu trả lời phổ quát: dự phòng và chiến lược đa vùng hoặc đa nhà cung cấp mua khả năng phục hồi bằng tiền, độ phức tạp và thêm bề mặt phải bảo mật. Hãy mang bằng chứng: thử lập bản đồ cấp danh mục các phụ thuộc dùng chung và tìm những điểm nghẽn nơi một sự cố đơn lẻ lan qua nhiều dịch vụ, rồi kiểm tra có ai thực sự sở hữu các tập trung đó không. Câu trả lời nên biến tập trung tình cờ thành quyết định có ý thức, có tài liệu, được kiểm thử dự phòng cho các phụ thuộc trọng yếu nhất. Trong danh mục doanh nghiệp và chính phủ, một sự cố vùng làm lộ dịch vụ hướng công dân một vùng chính xác là thất bại mà cơ quan quản lý và công chúng sẽ soi xét sau đó, nên hãy lập bản đồ nó trước thảm họa thay vì trong lúc đó.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm người và không có đường băng cho phòng rủi ro, hãy biến đảm bảo thành sản phẩm phụ của việc xây thay vì một chức năng riêng. Giữ một sổ đăng ký rủi ro ngắn với chủ sở hữu và quyết định xử lý cho mỗi mục, dựa vào báo cáo SOC 2 của nhà cung cấp đám mây thay vì viết kiểm soát từ đầu, và tạo SBOM trong đường ống để "chúng ta có phơi nhiễm không?" là một truy vấn vào ngày một lỗ hổng phụ thuộc đáp xuống. Hãy nói to sự tập trung nổi bật nhất của bạn, thường là một người duy nhất triển khai được, và ghép một người với họ để tri thức không bị kẹt trong một cái đầu.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia rủi ro hay kiểm toán riêng và ngân sách eo hẹp, vì vậy hãy mua đảm bảo thay vì xây: ưu tiên nhà cung cấp có chứng thực SOC 2 hoặc ISO 27001 đã mang bằng chứng bạn lẽ ra phải tự tạo. Dành công sức hạn hẹp nơi hậu quả cao nhất, một sổ đăng ký rủi ro duy nhất và diễn tập khôi phục từ sao lưu hằng tháng thắng một khung cầu kỳ không ai bảo trì. Coi hợp đồng là một kiểm soát, viết điều khoản thông báo vi phạm và thoát vào thỏa thuận nhà cung cấp để bạn thừa hưởng ít rủi ro của họ một cách mù quáng hơn.

**Doanh nghiệp lớn.** Vấn đề định nghĩa là quy mô qua nhiều đội: chạy mô hình ba tuyến, giữ sổ đăng ký rủi ro theo dịch vụ gộp lên cái nhìn danh mục cấp hội đồng quản trị, và đặt khẩu vị rủi ro tường minh ở cấp cao nhất để các đội thôi đoán. Mã hóa kiểm soát then chốt thành chính sách dưới dạng mã thực thi trong đường ống, cho kiểm toán viên quyền đọc vào bảng điều khiển kiểm soát trực tiếp thay vì chuẩn bị cho kiểm toán hằng năm, và lập bản đồ rủi ro tập trung ở cấp danh mục vì không đội đơn lẻ nào thấy được các điểm nghẽn dùng chung. Khớp độ sâu kiểm soát với hậu quả qua các bậc trọng yếu tường minh để tương xứng là thật thay vì khẩu hiệu.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Theo quy trình ủy quyền chính thức trong đó một quan chức chịu trách nhiệm chấp nhận rủi ro dư, duy trì giám sát liên tục để ủy quyền là trạng thái đang diễn ra thay vì chứng chỉ một lần, và viết điều khoản quyền kiểm toán và khả năng di chuyển dữ liệu vào hợp đồng nhà cung cấp. Vì một sự cố vùng làm lộ dịch vụ hướng công dân một vùng trở thành vấn đề công, hãy bắt buộc chuyển dự phòng đa vùng và khôi phục đã kiểm thử cho các dịch vụ trọng yếu nhất, và báo cáo kết quả diễn tập khôi phục thảm họa cho lãnh đạo theo nhịp cố định.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp công nghệ y tế sáu người xử lý dữ liệu bệnh nhân không đủ sức có phòng rủi ro, nên nó biến đảm bảo thành sản phẩm phụ của việc xây. Nó giữ một sổ đăng ký rủi ro ngắn trong tài liệu chung, với chủ sở hữu và quyết định xử lý cho mỗi mục, và xem xét nó ở buổi họp đứng thứ Sáu. Nó dựa vào báo cáo SOC 2 của nhà cung cấp đám mây thay vì viết kiểm soát riêng từ đầu, tạo SBOM trong đường ống để trả lời "chúng ta có phơi nhiễm không?" vào ngày một lỗ hổng phụ thuộc đáp xuống, và chạy diễn tập khôi phục từ sao lưu mỗi tháng vì một bản sao lưu chưa kiểm thử chỉ là hy vọng. Nó cũng nói to rủi ro tập trung nổi bật duy nhất: người sáng lập duy nhất triển khai được, và ghép một kỹ sư thứ hai với anh ấy để tri thức đó không bị kẹt trong một cái đầu.

**Doanh nghiệp lớn.** Một công ty thanh toán hoạt động dưới sự soi xét quản lý liên tục. Nó chạy mô hình ba tuyến. Nó duy trì sổ đăng ký rủi ro theo dịch vụ gộp lên bảng điều khiển cấp hội đồng quản trị. Nó mã hóa kiểm soát then chốt thành chính sách dưới dạng mã, thực thi trong đường ống triển khai. Phê duyệt thay đổi, cấp quyền truy cập và thay đổi cấu hình phát ra sự kiện kiểm toán bất biến vào kho lộ dấu can thiệp. Thay vì chuẩn bị cho kiểm toán hằng năm, công ty cho kiểm toán viên quyền đọc vào bảng điều khiển kiểm soát trực tiếp, biến kiểm toán thành lấy mẫu bằng chứng liên tục. Khi một thư viện mã nguồn mở được dùng rộng rãi công bố lỗ hổng nghiêm trọng, bản kiểm kê SBOM của công ty trả lời "chúng ta phơi nhiễm ở đâu?" trong vài phút.

**Chính phủ.** Một cơ quan chính phủ quốc gia theo quy trình ủy quyền chính thức trước khi bất kỳ hệ thống nào được vận hành. Nó yêu cầu kiểm soát có tài liệu, đánh giá độc lập, và một quan chức chịu trách nhiệm chấp nhận rủi ro dư. Nó duy trì giám sát liên tục, nên ủy quyền là trạng thái đang diễn ra thay vì chứng chỉ một lần. Một sự cố đám mây vùng từng làm lộ phụ thuộc một vùng trong hệ thống trợ cấp hướng công dân. Đáp lại, cơ quan lập bản đồ [rủi ro tập trung](https://en.wikipedia.org/wiki/Concentration_risk) qua danh mục của mình, bắt buộc chuyển dự phòng đa vùng và khôi phục đã kiểm thử cho các dịch vụ trọng yếu nhất, và nay chạy diễn tập khôi phục thảm họa định kỳ mà kết quả được báo cáo cho lãnh đạo.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của rủi ro và đảm bảo bị chi phối bởi tổn thất thảm khốc tránh được: một vi phạm lớn, một khoản phạt quản lý, một sự cố kéo dài của dịch vụ trọng yếu, hay một vụ xâm phạm chuỗi cung ứng. Những sự kiện này riêng lẻ hiếm nhưng riêng lẻ khổng lồ. Một sự cố tránh được đơn lẻ có thể vượt chi phí nhiều năm của cả chương trình đảm bảo. Ngoài tránh tổn thất, đảm bảo trưởng thành hạ chi phí tuân thủ liên tục, vì bằng chứng được tạo tự động thay vì gom trong hoảng loạn. Nó giúp dễ thắng kinh doanh bị quản lý và qua thẩm định của khách hàng hơn. Và nó đẩy nhanh ứng phó sự cố, vì bạn đã biết phơi nhiễm của mình.

Chi phí áp dụng gồm nhân sự rủi ro và kiểm toán, công cụ giám sát và bằng chứng, và công sức kỹ thuật để tự động hóa kiểm soát vào đường ống. Chi phí của việc *không* áp dụng là giá trị kỳ vọng của những thảm họa bạn đã không ngăn được, cộng thuế chậm của chuẩn bị kiểm toán thủ công và thiệt hại danh tiếng cộng dồn sau bất kỳ thất bại công khai nào. Khi lập luận với ban lãnh đạo, hãy định lượng một số ít kịch bản xấu nhất hợp lý và khả năng của chúng. Đóng khung giám sát kiểm soát liên tục là đổi một tổn thất lớn, khó đoán, thỉnh thoảng lấy một chi phí nhỏ, đều, khả đoán. Nhấn mạnh tổng chi phí sở hữu: một kiểm soát tự động hóa một lần trả bớt chi phí kiểm toán mỗi năm sau đó.

## Phản mẫu và cạm bẫy

- **Tuân thủ đánh dấu ô.** Tạo tài liệu thỏa mãn kiểm toán viên trong khi kiểm soát thật không hoạt động.
- **Sân khấu ngày kiểm toán.** Hệ thống chỉ tuân thủ trong những tuần trước kiểm toán hằng năm và trôi dạt suốt phần còn lại của năm.
- **Sổ đăng ký rủi ro như nghĩa địa.** Một sổ đăng ký được điền một lần và không bao giờ xem lại, tách rời quyết định thực tế.
- **DR chưa kiểm thử.** Kế hoạch sao lưu và chuyển dự phòng chưa từng được thực hành nên không hoạt động khi cần.
- **Tin nhà cung cấp theo logo.** Giả định một nhà cung cấp nổi tiếng là an toàn mà không có bằng chứng, và hoàn toàn phớt lờ phụ thuộc bắc cầu.
- **Tập trung vô hình.** Hợp nhất vào một vùng, nhà cung cấp hay con người vì hiệu quả mà không ai sở hữu điểm đơn thất bại kết quả.
- **Đảm bảo như rào cản phân phối.** Kiểm soát trung tâm nặng không tương xứng, mà các đội đi vòng, tạo hệ thống bóng không có đảm bảo nào cả.
- **Nhật ký mà tác nhân sửa được.** Dấu vết kiểm toán mà người bị kiểm toán thay đổi được, không chứng minh được gì.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Rủi ro được xử lý phản ứng sau sự cố. Không có khung hay sổ đăng ký chung. Kiểm soát không có tài liệu và không được xác minh, và kiểm toán là những cuộc chạy đua thủ công đau đớn. Rủi ro tập trung và nhà cung cấp không được xem xét, và điểm đơn thất bại chỉ lộ ra khi chúng thất bại.

**Mức 2: Phát triển.** Thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Một số sổ đăng ký rủi ro tồn tại cho hệ thống lớn, và một khung kiểm soát được áp dụng để kiểm toán đạt, nhưng chuẩn bị thủ công và tại một thời điểm. Nhà cung cấp chính được đánh giá lúc tiếp nhận mà không sau đó. Sao lưu tồn tại nhưng hiếm khi được kiểm thử, và chỉ một số điểm đơn thất bại được biết.

**Mức 3: Chuẩn hóa.** Mô hình ba tuyến và một khung chung được lập tài liệu và thực thi toàn tổ chức, cho một từ vựng rủi ro cho phép so sánh và gộp phơi nhiễm. Nhiều kiểm soát được tự động hóa vào đường ống, và giám sát liên tục bao phủ kiểm soát then chốt. Kiểm kê nhà cung cấp và phụ thuộc, gồm SBOM, được duy trì; DR được kiểm thử theo lịch; và rủi ro tập trung được lập bản đồ ở cấp danh mục thay vì để cho từng đội.

**Mức 4: Quản lý.** Đảm bảo được đo và kiểm soát theo đường cơ sở thay vì chỉ được lập tài liệu. Độ phủ kiểm soát, thời gian phát hiện trôi dạt, tỷ lệ đạt diễn tập DR so với RTO và RPO đã nêu, thời gian trung bình để trả lời "chúng ta có bị ảnh hưởng không?" sau một công bố, và rủi ro dư so với khẩu vị rủi ro đã nêu đều được theo dõi như chỉ số và báo cáo cho lãnh đạo. Độ lệch khỏi đường cơ sở kích hoạt hành động, tiêu chí khai tử và hạn khắc phục được thực thi dựa trên bằng chứng, và mỗi quyết định tiếp tục hay dừng đáng kể được đưa ra theo con số thay vì tuyên bố.

**Mức 5: Điều phối.** Đảm bảo được cải thiện liên tục và tích hợp trong toàn tổ chức. Kiểm toán viên lấy mẫu bằng chứng trực tiếp, khẩu vị rủi ro thúc đẩy kiểm soát tương xứng thích ứng khi hồ sơ rủi ro dịch chuyển, và tính toàn vẹn chuỗi cung ứng được xác minh trong đường ống. Diễn tập DR là thường lệ và xuyên hệ thống, quyết định tập trung là có ý thức, có chủ sở hữu và được kiểm thử dự phòng, và rủi ro cùng đảm bảo được đan vào hoạch định danh mục và chiến lược để tổ chức cân bằng lại kiểm soát khi phơi nhiễm đổi.

## Ý tưởng để thảo luận

- Làm sao bạn đặt khẩu vị rủi ro có ý nghĩa mà các đội thực sự dùng được để đánh đổi hằng ngày?
- Ranh giới đúng giữa kiểm soát tự động hóa trong đường ống và kiểm soát đòi phán đoán con người là gì?
- Khi nào chấp nhận rủi ro tập trung vì hiệu quả là quyết định đúng, và làm sao bạn giữ quyết định đó trung thực theo thời gian?
- Bao nhiêu đảm bảo chuỗi cung ứng là tương xứng cho một phụ thuộc bắc cầu nhỏ so với một nhà cung cấp trọng yếu có quyền truy cập sâu?
- Giám sát kiểm soát liên tục có bao giờ thay thế hoàn toàn kiểm toán độc lập không, hay độc lập đòi một người ngoài là con người?
- Làm sao bạn ngăn các chức năng rủi ro và đảm bảo thành nút thắt phân phối mà các đội đi vòng?

## Những điểm cần ghi nhớ

- Rủi ro được quản lý tới mức chấp nhận được, được sở hữu nơi nó được tạo ra, và được chứng minh bằng bằng chứng thay vì tuyên bố.
- Ưu tiên giám sát kiểm soát liên tục, tự động hơn kiểm toán tại một thời điểm để trôi dạt được bắt sớm và bằng chứng được tạo như sản phẩm phụ của vận hành.
- Rủi ro bên thứ ba và chuỗi cung ứng (gồm phụ thuộc mã nguồn mở bắc cầu) là rủi ro của bạn; hãy kiểm kê nó, đòi SBOM, và xác minh nguồn gốc.
- Liên tục kinh doanh và DR chỉ là năng lực nếu được kiểm thử; sao lưu và chuyển dự phòng chưa kiểm thử là giả định.
- Rủi ro tập trung và điểm đơn thất bại là mối quan tâm cấp danh mục vô hình với từng đội; hãy lập bản đồ chúng và biến hợp nhất thành quyết định có ý thức, được kiểm thử dự phòng.
- Luận chứng kinh doanh bị chi phối bởi thảm họa tránh được; hãy đổi một tổn thất lớn khó đoán thỉnh thoảng lấy một chi phí nhỏ đều khả đoán.

## Tài liệu tham khảo và đọc thêm

- ISO 31000, *Risk Management: Guidelines*
- ISO/IEC 27001 và 27005, *Information Security Management* và *Information Security Risk Management*
- NIST, *Risk Management Framework (SP 800-37)* và *Security and Privacy Controls (SP 800-53)*
- NIST, *Secure Software Development Framework (SP 800-218)* và *Cybersecurity Framework*
- Committee of Sponsoring Organisations of the Treadway Commission (COSO), *Enterprise Risk Management: Integrating with Strategy and Performance*
- AICPA, *SOC 2 Trust Services Criteria*
- The Open Group, *FAIR (Factor Analysis of Information Risk)*
- Betsy Beyer et al., *Site Reliability Engineering* (Google)
- Institute of Internal Auditors, *The Three Lines Model*
