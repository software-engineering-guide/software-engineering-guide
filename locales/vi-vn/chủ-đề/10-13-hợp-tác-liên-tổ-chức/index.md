# 10.13 Hợp tác liên tổ chức

## Tổng quan và động lực

Hợp tác liên tổ chức là công việc chung về phần mềm và công nghệ của hai hay nhiều tổ chức độc lập không có chủ sở hữu, ngân sách hay chuỗi chỉ huy chung. Nó khác với làm việc nhóm trong một công ty (chương 1.2). Trong một công ty, một nhà lãnh đạo cuối cùng có thể chỉ đạo con người, phân xử tranh chấp và phân bổ lại nguồn lực. Qua ranh giới tổ chức, không ai làm được. Mỗi bên giữ danh tính pháp lý, khuyến khích và quyền thoát của riêng mình, nên sự hợp tác phải được *giành lấy và duy trì* qua quản trị, hợp đồng và lòng tin thay vì được *ra lệnh*. Chương này nằm trong phần quản lý vì công việc liên tổ chức về bản chất là vấn đề chiến lược, quản trị và quan hệ có hệ quả kỹ thuật, không phải ngược lại.

Động lực là không tổ chức đơn lẻ nào xây hay kiểm soát được mọi thứ đáng có. Phần mềm nền tảng, như hệ điều hành, thư viện mật mã, giao thức web và công cụ đám mây, nay được xây dựng cộng tác, vì chi phí nhân bản nó khổng lồ và giá trị của một nền tảng chung, tương tác được lớn hơn bất kỳ lợi thế riêng nào từ việc tích trữ. **[Cạnh tranh hợp tác](https://en.wikipedia.org/wiki/Coopetition)** (sự pha trộn giữa *hợp tác* và *cạnh tranh*, nơi các đối thủ hợp tác trên nền tảng chung trong khi vẫn cạnh tranh trên sản phẩm phía trên) đã trở nên bình thường. Các công ty cạnh tranh cùng phát triển một runtime mã nguồn mở, rồi tạo khác biệt ở các dịch vụ họ xây phía trên. Về quy mô và hiệu ứng mạng, một tiêu chuẩn chung mà mọi người dùng được thắng một tiêu chuẩn độc quyền chỉ bạn dùng được.

Với doanh nghiệp và chính phủ, rủi ro là trực tiếp và cụ thể. Doanh nghiệp tham gia **[liên minh](https://en.wikipedia.org/wiki/Consortium)** (nhóm do thành viên tài trợ, lập vì mục đích chung) và quỹ mã nguồn mở để định hình các nền tảng họ phụ thuộc và tránh khóa chặt vào một nhà cung cấp (chương 10.3, 10.11). Chính phủ gặp vấn đề này liên tục. Các cơ quan phải chia sẻ dữ liệu để giao một dịch vụ mà công dân trải nghiệm như một tương tác. Các thẩm quyền phải tương tác qua biên giới. Khu vực công ngày càng xây **nền tảng dùng chung**: các dịch vụ chung như danh tính, thanh toán hay thông báo, xây một lần và nhiều cơ quan tái sử dụng. Một **hệ sinh thái GovTech** thịnh vượng (mạng lưới công ty khởi nghiệp, nhà cung cấp và cơ quan công xây công nghệ cho chính phủ) phụ thuộc vào các tổ chức tách biệt về pháp lý cộng tác trên thực tế.

## Các nguyên tắc chính

- **Không ai chịu trách nhiệm chung.** Qua ranh giới bạn có ảnh hưởng, không có thẩm quyền; hãy thiết kế cho sự đồng thuận, không phải mệnh lệnh.
- **Trung lập cho phép tham gia.** Một mái nhà trung lập cho phép đối thủ đóng góp mà không trao lợi thế cho đối thủ cạnh tranh.
- **Căn chỉnh khuyến khích trước kiến trúc.** Hợp tác thất bại vì lợi ích lệch thường xuyên hơn nhiều so với vì không tương thích kỹ thuật.
- **[Khả năng tương tác](https://en.wikipedia.org/wiki/Interoperability) là nền tảng kỹ thuật.** [Tiêu chuẩn mở](https://en.wikipedia.org/wiki/Open_standard) và giao diện (chương 3.8) là thứ cho phép các hệ thống độc lập thực sự kết nối.
- **Làm đóng góp và SHTT tường minh.** Ai sở hữu gì, và ai được dùng nó, phải được viết xuống trước khi công việc bắt đầu, không phải sau.
- **Lòng tin được xây theo những bước nhỏ, xác minh được.** Bắt đầu hẹp, giao hàng, và mở rộng phạm vi khi thành tích tích lũy.
- **Thiết kế cho lối thoát.** Bất kỳ bên nào cũng có thể rời đi; sự hợp tác phải sống sót qua sự ra đi mà không sụp đổ hay bị chiếm đoạt.

## Khuyến nghị

### Chọn hình thức hợp tác khớp mục tiêu

Không có mô hình duy nhất, nên hãy chọn có chủ đích. **Liên minh ngành và hiệp hội** đặt hướng và gộp tài trợ cho một lĩnh vực. **Quỹ mã nguồn mở** (tổ chức phi lợi nhuận trung lập như [Linux Foundation](https://en.wikipedia.org/wiki/Linux_Foundation) hay [Apache Software Foundation](https://en.wikipedia.org/wiki/Apache_Software_Foundation) nắm giữ và quản trị mã dùng chung) lưu trữ phần mềm mà nhiều tổ chức xây dựng và phụ thuộc. **[Cơ quan tiêu chuẩn](https://en.wikipedia.org/wiki/Standards_organization)** (tổ chức như ISO, IETF hay W3C công bố các đặc tả kỹ thuật đã thống nhất) tạo ra quy tắc tương tác mà mọi người lập trình theo. **[Liên doanh](https://en.wikipedia.org/wiki/Joint_venture)** tạo một thực thể mới cùng sở hữu cho mục đích thương mại chung. **[Quan hệ đối tác công-tư (PPP)](https://en.wikipedia.org/wiki/Public%E2%80%93private_partnership)**, các sắp xếp dài hạn trong đó chính phủ và doanh nghiệp tư cùng chia sẻ việc phân phối, tài trợ và rủi ro của một dịch vụ công, kết hợp nhiệm vụ công với năng lực tư. **Hợp tác liên cơ quan và xuyên chính phủ** nối trực tiếp các cơ quan công. **Nền tảng và dịch vụ dùng chung**, **thỏa thuận chia sẻ dữ liệu**, và **cạnh tranh hợp tác** hoàn thiện bộ công cụ. Khớp hình thức với mục tiêu: căn chỉnh nhẹ cần một hiệp hội; mã dùng chung cần một quỹ; một phương tiện thương mại bền vững cần một liên doanh.

### Thiết lập quản trị trung lập qua ranh giới

Vì không người tham gia nào có thể ra lệnh cho người khác, quản trị phải tường minh và, lý tưởng, trung lập. Hãy trao tài sản dùng chung (mã, nhãn hiệu, lộ trình) cho một **quỹ trung lập** thay vì cho bất kỳ thành viên nào, để không người tham gia nào đơn phương chiếm hay lái chúng. Xác định rõ **quyền quyết định**: ai quyết định hướng kỹ thuật (thường là ủy ban chỉ đạo kỹ thuật), ai kiểm soát ngân sách, và tranh chấp được giải quyết thế nào. Công bố một **lộ trình chung** để các bên hoạch định theo một hướng chung. Áp dụng một mô hình quản trị bằng văn bản, để thẩm quyền chảy từ quy tắc đã thống nhất thay vì từ ai ồn ào hay lớn nhất. "Chế độ tài năng" của Apache (ảnh hưởng giành được qua đóng góp) và cấu trúc hội đồng quỹ là các khuôn mẫu đã được chứng minh.

### Làm tường minh điều khoản đóng góp và sở hữu trí tuệ ngay từ đầu

[Sở hữu trí tuệ](https://en.wikipedia.org/wiki/Intellectual_property) (**SHTT**, các sáng tạo được pháp luật bảo vệ như mã, bằng sáng chế và nhãn hiệu) là nơi các cộng tác thiện chí thường vỡ nhất. Hãy giải quyết nó trước khi viết mã. Dùng một **[giấy phép mã nguồn mở](https://en.wikipedia.org/wiki/Open-source_license)** rõ ràng (chương 10.3) để mọi người biết quyền sử dụng và phân phối lại của mình. Yêu cầu **[Thỏa thuận Cấp phép Người đóng góp](https://en.wikipedia.org/wiki/Contributor_License_Agreement) (CLA)** hoặc **Chứng nhận Nguồn gốc Nhà phát triển (DCO)**, cơ chế để người đóng góp xác nhận họ có quyền đóng góp mã và cấp giấy phép cần thiết, để tài sản chung có nguồn gốc sạch. Giải quyết bằng sáng chế một cách tường minh, thường qua điều khoản không khẳng định hoặc cam kết bằng sáng chế, để người đóng góp không thể sau này kiện người dùng tác phẩm chung. Điều khoản SHTT bằng văn bản biến thiện chí mơ hồ thành sự rõ ràng bền vững, thực thi được.

### Ký hợp đồng cẩn thận về dữ liệu, riêng tư và chống độc quyền

Hợp tác giữa các tổ chức độc lập mang rủi ro pháp lý mà công việc trong công ty không có. **Thỏa thuận chia sẻ dữ liệu** phải nêu mục đích, mục đích sử dụng được phép, kiểm soát bảo mật, lưu giữ và trách nhiệm, và phải tôn trọng luật riêng tư và bảo vệ dữ liệu (chương 4.5), gồm cơ sở pháp lý để chia sẻ dữ liệu cá nhân và, nơi cần, thỏa thuận xử lý dữ liệu. **[Chống độc quyền](https://en.wikipedia.org/wiki/Competition_law)** (luật cạnh tranh cấm các thỏa thuận hạn chế thị trường không công bằng) là ràng buộc sống động mỗi khi đối thủ cạnh tranh hợp tác. Hãy giữ hợp tác ở nền tảng tiền cạnh tranh. Tránh trao đổi thông tin nhạy cảm về thương mại như giá. Lập tài liệu rằng mục đích là khả năng tương tác và hạ tầng dùng chung, không phải thông đồng. Đưa cố vấn pháp lý vào sớm. Một bước hụt về dữ liệu hay chống độc quyền có thể phá hỏng sự hợp tác và phơi nhiễm thành viên trước hình phạt.

### Xây trên khả năng tương tác và tiêu chuẩn mở

Khả năng tương tác, khả năng của các hệ thống độc lập trao đổi và dùng thông tin (chương 3.8), là nền tảng kỹ thuật làm mọi thứ khác khả thi. Ưu tiên **tiêu chuẩn mở** (đặc tả công khai mà ai cũng triển khai được mà không cần phép hay phí) và giao diện ổn định, có tài liệu (**API**, [giao diện lập trình ứng dụng](https://en.wikipedia.org/wiki/API)), để các bên kết nối mà không phụ thuộc vào cấu trúc bên trong độc quyền của một nhà cung cấp. Trong chính phủ, tiêu chuẩn dữ liệu chung và API dùng chung là thứ cho phép các cơ quan lắp ráp dịch vụ qua ranh giới (chương 7.1). Không có khả năng tương tác, hợp tác thoái hóa thành các tích hợp điểm-nối-điểm giòn vỡ làm cố hóa sự phụ thuộc thay vì mở ra giá trị chung.

### Vun đắp khuyến khích và lòng tin có chủ đích

Vì tham gia là tự nguyện, mỗi tổ chức phải thấy lợi ích tiếp tục, và mỗi bên phải tin các bên khác đủ để đầu tư. Hãy làm giá trị chung hiển thị và tương xứng đại thể với đóng góp, để không người đóng góp lớn nào cảm thấy bị bóc lột và không kẻ ăn theo nào thống trị. Bắt đầu với phạm vi hẹp, rủi ro thấp, giao một thứ thật, và chỉ mở rộng khi thành tích lớn lên. Đây là cùng logic xây dựng lòng tin như quan hệ hợp tác đổi mới (chương 10.9) và InnerSource (chương 1.2), mở rộng qua ranh giới công ty. Minh bạch (quyết định mở, lộ trình mở, chỉ số mở) là thứ duy trì lòng tin nơi thẩm quyền không làm được.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Quỹ mã nguồn mở** | Mái nhà trung lập; chia sẻ chi phí; áp dụng rộng; không có chủ đơn lẻ | Quyết định chậm hơn; phải tài trợ và bố trí nhân sự; chi phí chung quản trị |
| **Liên minh / hiệp hội ngành** | Định hình hướng; gộp tài trợ; trọng lượng ngành | Có thể đình trệ trong chính trị; rủi ro bị thành viên lớn chiếm đoạt |
| **Cơ quan tiêu chuẩn** | Khả năng tương tác bền vững; tính chính danh rộng | Rất chậm; đặc tả có thể tụt sau thực hành; quy trình nặng |
| **Liên doanh** | Quyền sở hữu và phương tiện thương mại rõ ràng; nguồn lực cam kết | Phức tạp để lập và giải thể; tranh chấp thoát và SHTT |
| **Quan hệ đối tác công-tư** | Kết hợp nhiệm vụ công với năng lực tư | Rủi ro trách nhiệm giải trình và khóa chặt; hợp đồng dài, cứng nhắc |
| **Cạnh tranh hợp tác** | Nền tảng chung, khác biệt cạnh tranh phía trên | Phơi nhiễm chống độc quyền; ranh giới giữa chia sẻ và cạnh tranh mong manh |

Căng thẳng định nghĩa là **giá trị chung so với kiểm soát riêng**. Một bên gộp càng nhiều vào một kho chung trung lập, lợi ích tập thể càng lớn, và bên đó càng ít đơn phương kiểm soát kết quả. Cách giải quyết là vạch ranh có chủ đích. Hãy hợp tác ở nền tảng tiền cạnh tranh, nơi mọi người hưởng lợi từ nền chung. Giữ kiểm soát nơi lợi thế cạnh tranh hay chủ quyền thực sự nằm (chương 10.11, 3.8).

## Câu hỏi để thảo luận với đội của bạn

1. **Tài sản dùng chung của chúng ta được trao cho một mái nhà trung lập, hay do một người tham gia nắm giữ mà sau này có thể rẽ nhánh, cấp phép lại, hoặc rút chúng?** Qua ranh giới tổ chức không ai chịu trách nhiệm chung, nên ai nắm mã, nhãn hiệu và lộ trình cuối cùng có thể lái hoặc chiếm chúng. Một quỹ trung lập cho phép đối thủ đóng góp mà không trao lợi thế cho đối thủ cạnh tranh, chính xác là lý do các mô hình Linux Foundation và Apache Software Foundation tồn tại. Nếu một thành viên đơn lẻ sở hữu kho chung, mọi thành viên khác chỉ cách bị chiếm đoạt một quyết định cấp phép lại. Hãy mang từng tài sản dùng chung bạn đóng góp và hỏi nó nằm hợp pháp ở đâu và ai kiểm soát hướng đi của nó. Nếu câu trả lời là "đối tác lớn nhất của chúng ta," bạn có rủi ro bị chiếm đoạt cần sửa trước khi đầu tư thêm công sức kỹ thuật.

2. **Chúng ta đã chọn hình thức hợp tác có chủ đích để khớp mục tiêu, hay mặc định cái quen thuộc?** Căn chỉnh nhẹ cần một hiệp hội; mã dùng chung cần một quỹ; quy tắc tương tác bền vững cần một cơ quan tiêu chuẩn; một phương tiện thương mại cam kết cần một liên doanh; một dịch vụ công cần quan hệ đối tác công-tư. Mỗi cái mang tốc độ, chi phí và hệ quả thoát khác nhau, và chọn sai là cách các cộng tác đình trệ trong chính trị hoặc hóa đá trong hợp đồng dài hạn cứng nhắc. Hãy khớp hình thức với cái bạn thực sự cần, và ưu tiên cấu trúc nhẹ nhất đạt được nó. Hãy mang kết quả cụ thể bạn muốn từ một cộng tác và kiểm thử nó với các phương án. Nếu bạn đang gia nhập một liên minh nặng ký để làm điều mà một kho dùng chung và một ghi chú quản trị bằng văn bản sẽ xử lý được, hãy thu nhỏ.

3. **Làm sao chúng ta ngăn ăn theo và giữ đóng góp tương xứng đại thể với lợi ích?** Một kho chung mục rữa khi các bên tiêu thụ công việc chung mà không bao giờ đóng góp, và nó vỡ khi một người đóng góp lớn cảm thấy bị những kẻ ăn theo bóc lột. Hãy làm giá trị chung hiển thị, giữ đóng góp tương xứng đại thể với lợi ích, và bắt đầu với phạm vi hẹp, rủi ro thấp để lòng tin và thành tích tích lũy trước khi bạn mở rộng cái bạn chia sẻ. Minh bạch (quyết định, lộ trình và chỉ số mở) là thứ duy trì hợp tác nơi không ai có thẩm quyền ép buộc. Hãy mang bản trình bày trung thực về tổ chức của bạn lấy gì từ mỗi dự án chung so với đưa lại gì. Nếu bạn là người nhận ròng trên thứ bạn phụ thuộc, bạn đang lặng lẽ làm yếu thứ bảo vệ bạn khỏi khóa chặt nhà cung cấp đơn lẻ.

4. **Ranh giới giữa cái chúng ta hợp tác và cái chúng ta cạnh tranh nằm ở đâu, và ai đủ tư cách giám sát nó?** Cạnh tranh hợp tác chỉ hiệu quả nếu mọi người đồng ý sự hợp tác dừng ở nền tảng tiền cạnh tranh, vì khoảnh khắc đối thủ trao đổi giá, lộ trình lộ chiến lược thị trường, hoặc dữ liệu khách hàng, hợp tác thành thông đồng và phơi nhiễm mọi thành viên trước hình phạt luật cạnh tranh. Với đội lớn, nguy hiểm là kỹ sư ngập sâu trong kho dùng chung trôi vào việc chia sẻ những thứ cố vấn pháp lý sẽ không bao giờ cho phép, đơn giản vì lằn ranh chưa bao giờ được vạch. Hãy mang tuyên bố bằng văn bản về những gì cộng tác bao phủ và những gì nó loại trừ tường minh, cùng các rào chắn chống độc quyền cố vấn của bạn đã rà soát, và nêu tên người rà soát các nhóm làm việc mới trước khi chúng hình thành. Trong bối cảnh doanh nghiệp và chính phủ, nơi cơ quan quản lý soi kỹ liên doanh và liên minh, hãy coi ranh giới có tài liệu, được cố vấn phê duyệt là điều kiện tiên quyết để tham gia, không phải giấy tờ để bổ sung sau khi một cuộc điều tra bắt đầu.

5. **Kế hoạch thoát của chúng ta là gì nếu sự hợp tác này bị chiếm đoạt, đình trệ hoặc sụp đổ, và quản trị có thực sự bảo vệ chúng ta không?** Bất kỳ bên nào cũng có thể rời đi, một thành viên thống trị có thể lái kho chung theo mục đích riêng, và một liên minh có thể họp nhiều năm mà không giao gì, nên bạn phải biết trước bạn sẽ ra đi thế nào và giữ lại gì. Cân nhắc đối lập là thiết kế cho lối thoát (dữ liệu di chuyển được, mã rẽ nhánh được theo giấy phép mở, không phụ thuộc nhà cung cấp đơn lẻ) tốn công sức cảm giác lãng phí khi mối quan hệ lành mạnh. Hãy mang điều khoản giấy phép, nơi nhãn hiệu và lộ trình nằm hợp pháp, và câu trả lời cụ thể cho việc tổ chức của bạn sẽ làm gì trong tuần một đối tác then chốt rút lui. Với cơ quan công mang nghĩa vụ nhiều năm với công dân, một nền tảng không rẽ nhánh được do một thành viên nắm là rủi ro liên tục với dịch vụ mà người dân phụ thuộc, nên hãy yêu cầu quyền giữ trung lập và quyền thoát bằng văn bản trước khi tiếp nhận.

6. **Chúng ta sẽ đo thế nào liệu sự hợp tác này có thực sự mang lại giá trị không, và bằng chứng nào sẽ khiến chúng ta rời đi?** Công việc liên tổ chức tích lũy tư cách thành viên xác sống: liên minh bạn vẫn tài trợ và bố trí nhân sự rất lâu sau khi lợi ích phai, vì rời đi cảm giác như tuyên bố chính trị và không ai theo dõi lợi tức. Hãy thống nhất từ trước thành công trông thế nào (chi phí tránh được so với xây riêng, tính năng phát hành trên nền chung, khóa chặt giảm) và đặt ngưỡng kích hoạt rà soát việc tham gia của bạn. Hãy mang chi phí hằng năm cho ghế của bạn, giờ nhân viên bạn đóng góp, và đánh giá thẳng thắn về những gì bạn đã nhận lại trong năm qua. Trong danh mục doanh nghiệp và chính phủ, nơi tư cách thành viên nhân lên qua các phòng ban và hiếm khi bị hủy, hãy nêu ai sở hữu từng mối quan hệ, xem xét nó theo nhịp cố định, và giữ thẩm quyền rút lui, vì một sự hợp tác không ai chịu trách nhiệm rà soát là sự hợp tác không ai thoát ra được.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư, nên chỉ hợp tác để thôi phát minh lại một phụ thuộc hàng hóa, không bao giờ để theo đuổi uy tín trong ủy ban tiêu chuẩn. Cùng bảo trì thư viện dùng chung duy nhất bạn không đủ sức sở hữu một mình, dùng ghi chú quản trị nhẹ và Chứng nhận Nguồn gốc Nhà phát triển để nguồn gốc luôn sạch, và giữ phạm vi đủ hẹp để rời đi không tốn gì ngoài một bản rẽ nhánh. Tốc độ quan trọng hơn một ghế ở bàn: bỏ qua liên minh nặng ký cho đến khi một nền chung trực tiếp đe dọa sự sống còn của bạn.

**Doanh nghiệp nhỏ.** Không có chuyên gia pháp lý hay tiêu chuẩn trong nhân sự, hãy coi công việc liên tổ chức là thứ bạn tham gia chứ không xây, và dựa vào điều khoản giấy phép và đóng góp có sẵn của quỹ trung lập thay vì tự soạn. Trước khi ký bất kỳ thỏa thuận chia sẻ dữ liệu nào, hãy có câu trả lời bằng ngôn ngữ đơn giản về những gì bạn được làm với dữ liệu chung và trách nhiệm đáp xuống đâu, vì một bước hụt riêng tư hay chống độc quyền có thể tốn hơn giá trị của sự hợp tác. Ưu tiên các quỹ mã nguồn mở đã thiết lập và tiêu chuẩn đã công bố bạn áp dụng được ngay hơn các thỏa thuận song phương riêng phải thương lượng và giám sát.

**Doanh nghiệp lớn.** Hãy quản lý hợp tác như một danh mục qua nhiều đội: sổ đăng ký mọi liên minh, quỹ và liên doanh bạn thuộc về, chi phí và thời gian nhân viên mỗi cái tiêu tốn, và giá trị nó trả lại. Khăng khăng quyền giữ trung lập tài sản dùng chung, ranh giới chống độc quyền được cố vấn rà soát, và mô hình quản trị bằng văn bản để một đối tác thống trị không chiếm được nền tảng bạn phụ thuộc. Lập ngân sách tường minh cho công sức tham gia và đóng góp, và dành đầu tư riêng cho lợi thế cạnh tranh thực sự trong khi gộp chi phí vào nền tảng hàng hóa mà mọi người chia sẻ.

**Chính phủ.** Quy tắc mua sắm, nghĩa vụ minh bạch và trách nhiệm giải trình công định hình mọi sắp xếp, nên hãy ưu tiên tiêu chuẩn mở và quản trị trung lập mà không nhà cung cấp đơn lẻ nào chiếm được, và đòi khả năng di chuyển dữ liệu và quyền thoát trong mọi hợp đồng. Công bố quản trị, lộ trình và điều khoản chia sẻ dữ liệu của nền tảng dùng chung để công dân và cơ quan giám sát thấy dịch vụ được vận hành thế nào, và đặt chia sẻ dữ liệu liên cơ quan trên cơ sở pháp lý tường minh và biện pháp bảo vệ riêng tư. Tiếp nhận các dịch vụ ít nhạy cảm trước để chứng minh mô hình, và giữ trách nhiệm cho các quyết định có hệ quả với một viên chức công có tên thay vì phân tán nó qua một liên minh.

## Ví dụ

**Công ty khởi nghiệp.** Ba công ty khởi nghiệp giai đoạn đầu cùng phụ thuộc vào cùng một thư viện phân tích dữ liệu mã nguồn mở, do một tình nguyện viên làm việc quá sức duy nhất bảo trì mà sự kiệt sức của họ đe dọa cả ba. Thay vì mỗi bên lặng lẽ rẽ nhánh nó, họ đồng ý cùng bảo trì trong một kho dùng chung trung lập, với ghi chú quản trị bằng văn bản nhẹ và Chứng nhận Nguồn gốc Nhà phát triển để đóng góp có nguồn gốc sạch. Họ chỉ cộng tác trên bộ phân tích hàng hóa, giữ sản phẩm của mình hoàn toàn tách biệt, và bắt đầu với phạm vi hẹp (chỉ bản vá bảo mật) để xây lòng tin trước khi mở rộng cái họ chia sẻ.

**Doanh nghiệp lớn.** Nhiều nhà cung cấp đám mây và phần mềm cạnh tranh phụ thuộc vào cùng một nền tảng điều phối container. Thay vì mỗi bên duy trì một bản rẽ nhánh riêng, họ đóng góp nó cho một quỹ trung lập với ủy ban chỉ đạo kỹ thuật, mô hình quản trị bằng văn bản và Thỏa thuận Cấp phép Người đóng góp. Mỗi công ty vẫn cạnh tranh quyết liệt ở các dịch vụ được quản lý họ xây phía trên nền tảng (cạnh tranh hợp tác), nhưng họ chia sẻ chi phí và hướng đi của lõi chung. Điều này tránh khóa chặt nhà cung cấp đơn lẻ và giữ nền tảng mà tất cả cùng dựa vào lành mạnh. Cố vấn chống độc quyền xác nhận hợp tác chỉ giới hạn ở hạ tầng dùng chung, không phải thị trường hay giá.

**Chính phủ.** Một chính phủ quốc gia dựng nền tảng danh tính dùng chung để công dân đăng nhập một lần để tới dịch vụ của nhiều cơ quan. Nền tảng được quản trị bởi một cơ quan trung ương trung lập với lộ trình công bố và quyền quyết định rõ ràng, trong khi mỗi cơ quan vẫn độc lập và tích hợp qua API mở và tiêu chuẩn dữ liệu chung (chương 3.8, 7.1). **Thỏa thuận chia sẻ dữ liệu** liên cơ quan quy định chính xác cái gì được chia sẻ, vì mục đích gì, dưới biện pháp bảo vệ riêng tư nào (chương 4.5), để dữ liệu của công dân chỉ chảy như luật và sự đồng ý cho phép. Các cơ quan ít nhạy cảm hơn tiếp nhận trước để xây lòng tin và chứng minh mô hình trước khi các dịch vụ rủi ro cao hơn tham gia.

## Luận chứng kinh doanh: động lực, ROI và TCO

Kinh tế của hợp tác liên tổ chức xoay quanh chi phí chung và hiệu ứng mạng. Động lực cốt lõi là công nghệ nền tảng đắt để xây và bảo trì nhưng giá trị hơn nhiều khi chia sẻ. Gộp đầu tư vào một nền tảng hay tiêu chuẩn chung trải tổng chi phí sở hữu (**TCO**) qua nhiều tổ chức, nên mỗi bên trả một phần nhỏ của chi phí xây riêng trong khi có được nền tảng tương tác với của mọi người khác. Lợi tức đầu tư (**ROI**) đến từ trùng lặp tránh được, thời gian ra thị trường nhanh hơn trên nền tảng sẵn có, khóa chặt giảm và vị thế thương lượng mạnh hơn với nhà cung cấp, và tiếp cận nhân tài cùng ý tưởng vượt ra ngoài bức tường của một tổ chức (chương 10.9).

Chi phí là thật và thường bị đánh giá thấp: chi phí chung quản trị và pháp lý, thời gian nhân viên để tham gia có ý nghĩa, đóng góp ngược lại cho kho chung, và quyết định chậm hơn một chủ sở hữu đơn lẻ có thể đưa ra. Với chính phủ, luận chứng kinh doanh thêm giá trị công, vì nền tảng dùng chung giảm phân mảnh, cắt tổng chi tiêu qua các cơ quan và cải thiện trải nghiệm công dân, nhưng nó phải được cân nhắc với trách nhiệm giải trình và rủi ro quán tính tập thể. Cái bẫy ở cả hai phía là hiệu chỉnh sai. Hợp tác ở những gì là lợi thế cạnh tranh hay chủ quyền thực sự lãng phí sự khác biệt. Từ chối hợp tác trên nền tảng hàng hóa nghĩa là trả giá đầy đủ một mình cho thứ cả ngành đã xây. Luận chứng mạnh nhất gộp chi phí vào nền chung và dành đầu tư riêng cho nơi kiểm soát thực sự quan trọng.

## Phản mẫu và cạm bẫy

- **Ăn theo:** các bên tiêu thụ công việc chung mà không bao giờ đóng góp, bỏ đói kho chung cho đến khi nó mục rữa (vấn đề [hành động tập thể](https://en.wikipedia.org/wiki/Collective_action_problem) kinh điển mà Ostrom nghiên cứu).
- **Chiếm đoạt quản trị:** một thành viên lớn hay nhiều nguồn lực lặng lẽ lái sự hợp tác theo lợi ích riêng, làm rỗng tính trung lập.
- **Khuyến khích lệch:** các bên tham gia với mục tiêu không tương thích chỉ nổi lên sau khi cam kết đã được đưa ra, làm đình trệ nỗ lực.
- **Không có mái nhà trung lập:** tài sản dùng chung do một người tham gia nắm giữ, người này sau đó có thể rẽ nhánh, cấp phép lại hoặc rút chúng.
- **Điều khoản SHTT mơ hồ:** bắt đầu xây trước khi quyền sở hữu, giấy phép và bằng sáng chế được giải quyết, bảo đảm một tranh chấp về sau.
- **Mù chống độc quyền:** đối thủ chia sẻ thông tin nhạy cảm về thương mại dưới vỏ "hợp tác."
- **Sân khấu hợp tác:** một liên minh họp và công bố mà không bao giờ giao, tiêu tốn ngân sách và thiện chí.
- **Nhầm lẫn ranh giới:** coi công việc xuyên công ty như công việc nội bộ, giả định một thẩm quyền chỉ đạo không tồn tại.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu.** Hợp tác cơ hội và phụ thuộc cá nhân, được chi phối bằng cái bắt tay, không có điều khoản SHTT, dữ liệu hay quản trị bằng văn bản. Đối thủ hợp tác trên một phụ thuộc chung chỉ bằng thiện chí không chính thức. Nó hiệu quả cho đến khi một người then chốt rời đi hoặc nảy sinh tranh chấp, rồi sụp đổ.
- **Mức 2, Phát triển.** Một số cộng tác được hậu thuẫn bởi thỏa thuận tường minh (giấy phép, CLA hoặc DCO, thỏa thuận chia sẻ dữ liệu) với phạm vi và quyền quyết định xác định, nhưng thực hành không nhất quán giữa các đội. Một nhóm trao tài sản dùng chung cho mái nhà trung lập trong khi nhóm khác vẫn dựa vào cái bắt tay, và quản trị, nơi tồn tại, là song phương và nặng.
- **Mức 3, Chuẩn hóa.** Một mô hình có tài liệu, toàn tổ chức chi phối cách bạn hợp tác: tài sản dùng chung nằm trong mái nhà trung lập (quỹ hay cơ quan trung ương) với quản trị, lộ trình và quyền quyết định dựa trên năng lực được công bố; một danh mục kiểm tra chuẩn về điều khoản giấy phép, SHTT, chia sẻ dữ liệu và chống độc quyền được yêu cầu trước khi bất kỳ công việc chung nào bắt đầu; khả năng tương tác dựa trên tiêu chuẩn mở (chương 3.8). Các quy tắc được thực thi nhất quán, không để tùy ý từng đội.
- **Mức 4, Quản lý.** Danh mục hợp tác được đo và kiểm soát theo đường cơ sở. Bạn theo dõi chi phí và giờ nhân viên của từng tư cách thành viên, đóng góp so với lợi ích cho mọi dự án chung, chi phí tránh được so với xây riêng, và khóa chặt giảm, và bạn theo dõi các chỉ báo dẫn đầu của việc chiếm đoạt quản trị như tỷ lệ commit, ghế hội đồng hay vai trò người bảo trì của một thành viên. Ngưỡng khai tử hay gia hạn được đặt trước, nên một liên minh đình trệ hay mối quan hệ người-nhận-ròng bị bắt dựa trên bằng chứng thay vì được bảo vệ bằng cảm tình.
- **Mức 5, Điều phối.** Hợp tác là năng lực chiến lược được cải thiện liên tục, tích hợp trong toàn tổ chức. Bạn định hình tiêu chuẩn và quỹ thay vì chỉ tiêu thụ chúng, duy trì kho chung lành mạnh, cân bằng lại cạnh tranh hợp tác và lối thoát khi thị trường và bức tranh rủi ro dịch chuyển, và thích ứng quản trị theo các chỉ số bạn theo dõi. Công việc liên tổ chức là năng lực cốt lõi: một hệ sinh thái GovTech hay ngành thịnh vượng thay vì một tập dự án rời rạc.

## Ý tưởng để thảo luận

- Phần nào của công nghệ bạn là lợi thế cạnh tranh hay chủ quyền thực sự, và phần nào là nền tảng hàng hóa mà bạn nên chia sẻ chi phí xây?
- Làm sao bạn phát hiện sớm việc chiếm đoạt quản trị, trước khi một thành viên thống trị lặng lẽ lái cộng tác theo mục đích riêng?
- Thỏa thuận bằng văn bản tối thiểu (SHTT, dữ liệu, quyền quyết định) bạn sẽ yêu cầu là gì trước khi đóng góp công sức kỹ thuật cho một dự án chung?
- Với sáng kiến chia sẻ dữ liệu liên cơ quan, làm sao bạn thỏa mãn cả mục tiêu phân phối lẫn luật riêng tư và bảo vệ dữ liệu (chương 4.5) mà không đình trệ?
- Khi một người đóng góp lớn dọa rời nền tảng dùng chung, quản trị của bạn giữ sự hợp tác sống thế nào thay vì sụp đổ hay bị chiếm đoạt?
- Lằn ranh giữa cạnh tranh hợp tác lành mạnh và rủi ro chống độc quyền nằm ở đâu, và ai trong tổ chức của bạn đủ tư cách phán đoán nó?

## Những điểm cần ghi nhớ

- Hợp tác liên tổ chức là công việc chung của các tổ chức độc lập không có thẩm quyền chung; nó được giành lấy qua quản trị, hợp đồng và lòng tin, không phải được ra lệnh.
- Chọn hình thức có chủ đích, dù là liên minh, quỹ, cơ quan tiêu chuẩn, liên doanh, PPP, nền tảng dùng chung, thỏa thuận chia sẻ dữ liệu hay cạnh tranh hợp tác, để khớp mục tiêu.
- Quản trị trung lập, quyền quyết định rõ ràng, và điều khoản đóng góp cùng SHTT tường minh là thứ cho phép các bên độc lập, gồm cả đối thủ, hợp tác an toàn.
- Khả năng tương tác và tiêu chuẩn mở (chương 3.8) là nền tảng kỹ thuật; không có chúng, hợp tác thoái hóa thành các tích hợp giòn vỡ, dễ khóa chặt.
- Ký hợp đồng cẩn thận về chia sẻ dữ liệu, riêng tư (chương 4.5) và chống độc quyền, đặc biệt khi đối thủ hợp tác.
- Coi chừng các kiểu thất bại (ăn theo, chiếm đoạt quản trị và khuyến khích lệch) và thiết kế quản trị và quyền thoát để chịu đựng chúng.
- Với cả doanh nghiệp lẫn chính phủ, hãy chia sẻ chi phí trên nền tảng chung và giữ kiểm soát nơi lợi thế và chủ quyền thực sự nằm (chương 10.11).

## Tài liệu tham khảo và đọc thêm

- Elinor Ostrom, *Governing the Commons: The Evolution of Institutions for Collective Action* (1990): nghiên cứu nền tảng về cách tài nguyên chung được duy trì mà không có thẩm quyền trung ương.
- Henry Chesbrough, *Open Innovation: The New Imperative for Creating and Profiting from Technology* (2003): hợp tác qua ranh giới tổ chức như nguồn đổi mới.
- The Apache Software Foundation: mô hình quản trị, "The Apache Way," và ra quyết định dựa trên năng lực (apache.org).
- The Linux Foundation: lưu trữ và quản trị trung lập cho hợp tác mã nguồn mở quy mô lớn (linuxfoundation.org).
- Karim Lakhani và những người khác, các bài viết về đổi mới mã nguồn mở và dựa trên cộng đồng; và Adam Brandenburger và Barry Nalebuff, *Co-opetition* (1996): chiến lược hợp tác và cạnh tranh cùng lúc.
- OpenSSF (Open Source Security Foundation) và tiêu chuẩn OpenChain (ISO/IEC 5230): các cách tiếp cận liên tổ chức cho chuỗi cung ứng và tuân thủ giấy phép.
- Tài liệu dịch vụ số chính phủ và GovTech về nền tảng dùng chung và chia sẻ dữ liệu liên cơ quan (ví dụ, hướng dẫn dịch vụ số quốc gia và tiêu chuẩn mở).
