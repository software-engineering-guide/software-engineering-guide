# 2.6 Quản lý phiên bản và mã nguồn

## Tổng quan và động lực

Hãy coi [quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control) là hệ thống ghi nhận của cơ sở mã của bạn. Nó ghi lại mọi thay đổi, bao gồm ai đã thực hiện, khi nào và vì sao, và cho phép nhiều người làm việc trên cùng một phần mềm mà không ghi đè lên nhau. Với một tổ chức lớn, nó hơn nhiều so với một bản sao lưu. Nó là nền tảng mà cộng tác, [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI), kiểm toán và quản lý phát hành đều dựa vào. Những lựa chọn bạn đưa ra về phân nhánh, cấu trúc kho mã và kỷ luật commit định hình đội của bạn có thể di chuyển nhanh đến đâu, và an toàn ra sao.

Với các đội lớn, quản lý mã nguồn thực chất là một bài toán điều phối ở quy mô lớn. Khi hàng trăm kỹ sư đẩy thay đổi vào mã dùng chung, họ cần một chiến lược giữ cho các lần hợp nhất nhỏ, giữ cho nhánh chính luôn sẵn sàng phát hành, và giữ cho lịch sử dễ đọc. Một đội tích hợp liên tục thì dòng chảy trôi chảy. Một đội để các nhánh phân kỳ hàng tuần thì loạng choạng từ khủng hoảng tích hợp này sang khủng hoảng khác. Cấu trúc kho mã của bạn, một kho lớn hay nhiều kho, cũng định hình cách các đội chia sẻ mã và điều phối.

Các bối cảnh doanh nghiệp và chính phủ thêm một số yêu cầu: khả năng truy vết, kiểm soát truy cập và lưu giữ. Một thay đổi có thể cần liên kết với một hạng mục công việc đã được phê duyệt để kiểm toán. Bí mật không bao giờ được vào lịch sử. Quyền truy cập kho mã phải tôn trọng các ranh giới bảo mật. Ở đây, các thực hành quản lý phiên bản của bạn trở thành một phần của khung kiểm soát của tổ chức, và một sai lầm như lộ bí mật hoặc một lịch sử không thể kiểm toán có thể có hậu quả nghiêm trọng.

## Các nguyên tắc chính

- Tích hợp các thay đổi nhỏ thường xuyên; sự phân kỳ kéo dài là gốc rễ của nỗi đau hợp nhất.
- Giữ nhánh chính luôn sẵn sàng phát hành.
- Lịch sử là tài liệu; hãy viết commit cho người đọc tương lai cần hiểu vì sao.
- Không bao giờ commit bí mật; coi bất kỳ bí mật nào đã lọt vào lịch sử là đã bị xâm phạm.
- Tự động hóa việc thực thi vệ sinh (hook, kiểm tra CI) thay vì chỉ dựa vào kỷ luật.
- Chọn cấu trúc kho mã (một kho so với nhiều kho) theo cách các đội thực sự chia sẻ mã và điều phối, không phải theo mốt.
- Liên kết các thay đổi với lý do của chúng (hạng mục công việc, phiếu việc hoặc quyết định) để truy vết.

## Khuyến nghị

### Ưu tiên phát triển dựa trên thân chính với các nhánh sống ngắn

Nghiêng về [phát triển dựa trên thân chính](https://en.wikipedia.org/wiki/Trunk-based_development): tích hợp vào một nhánh chính dùng chung thường xuyên, dùng các nhánh tính năng sống ngắn đo bằng giờ hoặc ngày, không phải tuần. Các nhánh ngắn giữ cho việc hợp nhất nhỏ và tích hợp liên tục, và thói quen đó gắn bó chặt chẽ với hiệu suất phân phối cao. Khi công việc chưa xong, đừng để nó trên một nhánh sống lâu. Hãy dùng [cờ tính năng](https://en.wikipedia.org/wiki/Feature_toggle), các công tắc lúc chạy che giấu công việc chưa hoàn thành, để bạn có thể hợp nhất nó một cách an toàn. Hãy dành các nhánh phát hành sống lâu cho việc hỗ trợ nhiều phiên bản thực sự, và đi vào với sự hiểu biết về chi phí bảo trì mà chúng mang theo.

### Chọn mô hình phân nhánh phù hợp với nhịp phát hành

Hãy khớp [mô hình phân nhánh](https://en.wikipedia.org/wiki/Branching_(version_control)) của bạn với cách bạn thực sự phát hành. Nếu bạn triển khai liên tục, phát triển dựa trên thân chính với phân nhánh tối thiểu phục vụ bạn tốt. Nếu bạn phát hành các phiên bản có đánh số cho khách hàng, hoặc hỗ trợ nhiều phiên bản đang sống cùng lúc, bạn có thể cần các nhánh phát hành và chuyển ngược bản vá. Hãy tránh xa các mô hình nặng với nhiều nhánh sống lâu trừ khi mô hình phát hành của bạn thực sự đòi hỏi, vì chúng nhân lên chi phí hợp nhất và bảo trì.

### Quyết định một cách có chủ đích giữa monorepo và polyrepo

Hãy chọn [monorepo](https://en.wikipedia.org/wiki/Monorepo), một kho duy nhất chứa nhiều dự án, khi các đội chia sẻ mã nhiều, cần các thay đổi nguyên tử xuyên dự án, và muốn công cụ cùng khả năng hiển thị thống nhất. Đổi lại, bạn chấp nhận nhu cầu về công cụ dựng và kiểm soát truy cập có quy mô. Hãy chọn polyrepo, các kho riêng cho mỗi dự án hoặc dịch vụ, khi các đội và dịch vụ thực sự độc lập, muốn truy cập và chu kỳ phát hành cô lập, và không cần các thay đổi nguyên tử xuyên kho. Đổi lại, bạn chấp nhận chi phí điều phối các thay đổi trải qua nhiều kho. Cả hai đều hoạt động ở quy mô lớn. Chính lựa chọn sai với mô hình liên kết của bạn mới tạo ra ma sát liên tục.

### Thực thi vệ sinh commit và commit theo quy ước

Hãy yêu cầu thông điệp commit giải thích vì sao một thay đổi được thực hiện, không chỉ là gì. Áp dụng một quy ước như commit theo quy ước để thông điệp có cấu trúc và máy phân tích được, cho phép bạn tự động hóa nhật ký thay đổi và đánh phiên bản. Giữ các commit nguyên tử, mỗi cái một thay đổi logic, để lịch sử có thể tìm kiếm nhị phân và dễ hoàn tác. Để hook và kiểm tra CI thực thi định dạng thông điệp và vệ sinh cơ bản, thay vì dựa vào trí nhớ.

### Giữ các tệp nhị phân lớn và mã sinh ra khỏi lịch sử thông thường

Đừng commit trực tiếp các tài sản nhị phân lớn vào lịch sử chính, vì chúng làm phình mọi bản sao mãi mãi. Hãy dùng cơ chế lưu trữ tệp lớn hoặc một kho hiện vật thay thế. Theo nguyên tắc, cũng tránh commit mã sinh ra; hãy sinh nó trong quá trình dựng. Khi bạn thực sự phải commit một hiện vật sinh ra, hãy cô lập và đánh dấu rõ ràng để nó không làm ô nhiễm các đánh giá và diff.

### Ngăn bí mật không bao giờ vào kho mã

Đặt việc quét bí mật tự động vào hook trước commit và CI để thông tin xác thực bị chặn trước khi chúng đáp xuống. Cung cấp cho kỹ sư một hệ thống quản lý bí mật đàng hoàng, để họ không bao giờ cần mã hóa cứng thông tin xác thực ngay từ đầu. Và coi bất kỳ bí mật nào đã lọt vào lịch sử là bị xâm phạm: hãy xoay vòng nó ngay lập tức. Một khi bí mật đã được đẩy lên và sao chép, việc gỡ nó khỏi lịch sử là khó và không đáng tin cậy.

### Thiết lập kiểm soát truy cập và khả năng truy vết

Thiết lập quyền truy cập kho mã để tôn trọng các ranh giới bảo mật và [đặc quyền tối thiểu](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Liên kết commit hoặc pull request với các hạng mục công việc, để mọi thay đổi truy vết về lý do của nó, giúp ích cho cả ngữ cảnh kỹ thuật hằng ngày lẫn kiểm toán. Bảo vệ các nhánh then chốt của bạn bằng các kiểm tra và đánh giá bắt buộc, để không gì được hợp nhất mà không qua các cổng bạn đã thống nhất.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Phát triển dựa trên thân chính | Tích hợp liên tục; hợp nhất nhỏ; dòng chảy cao | Cần cờ tính năng và kỷ luật; ít cô lập hơn |
| Nhánh tính năng sống lâu | Cô lập mạnh công việc đang tiến hành | Hợp nhất đau đớn; tích hợp bị trì hoãn; trôi dạt |
| Monorepo | Thay đổi nguyên tử xuyên dự án; công cụ dùng chung; khả năng hiển thị | Cần công cụ dựng có quy mô; kiểm soát truy cập thô theo mặc định |
| Polyrepo | Phát hành độc lập; truy cập cô lập; công cụ đơn giản cho từng kho | Khó thay đổi xuyên kho; chi phí điều phối phiên bản |
| Commit theo quy ước | Nhật ký thay đổi và phiên bản tự động; lịch sử nhất quán | Quy ước ban đầu; cần thực thi |

Sự đánh đổi lớn ở đây là tần suất tích hợp so với sự cô lập. Các nhánh sống lâu có cảm giác an toàn hơn vì công việc của bạn nằm riêng một mình, nhưng chính sự cô lập đó gây ra các lần hợp nhất đắt đỏ và bất ngờ tích hợp sau này. Phát triển dựa trên thân chính từ bỏ cảm giác cô lập đó để đổi lấy tích hợp liên tục, rẻ, và yêu cầu bạn mang theo cờ tính năng và kỷ luật. Quyết định monorepo/polyrepo đánh đổi sự dễ dàng xuyên dự án lấy sự độc lập của đội. Hãy chọn cái khớp với mức độ liên kết thực sự của mã của bạn.

## Câu hỏi để thảo luận với đội của bạn

1. **Những kiểm tra nào phải qua trước khi bất cứ thứ gì được hợp nhất vào nhánh chính được bảo vệ của bạn, và nhánh chính đó có thực sự luôn sẵn sàng phát hành không?** Chương này coi nhánh chính sẵn sàng phát hành là nguyên tắc cốt lõi và gọi một nhánh chính không được bảo vệ, nơi mã hỏng hoặc chưa được đánh giá đến được nhánh mà mọi người phụ thuộc, là một phản mẫu. Trong một đội lớn, một nhánh chính đỏ chặn mọi người cùng lúc, nên cổng bạn yêu cầu là một thuộc tính an toàn chung, không phải cá nhân. Hãy mang bằng chứng: bảo vệ nhánh của bạn thực sự thực thi gì hiện nay, và nhánh chính hiện đang hỏng thường xuyên đến mức nào. Hãy quyết định tập hợp bắt buộc, kiểm thử đạt, quét bảo mật và đánh giá, và làm cho nhánh chính sẵn sàng phát hành bằng chính sách thay vì bằng hy vọng. Cổng đó là thứ cho phép nhiều người tích hợp liên tục mà không sợ hãi.

2. **Áp dụng commit theo quy ước có đáng với chi phí quy ước cho đội của bạn, xét những gì nó tự động hóa không?** Chương này khuyến nghị thông điệp commit có cấu trúc, máy phân tích được chính vì chúng cho phép bạn tự động hóa nhật ký thay đổi và đánh phiên bản, và yêu cầu các commit nguyên tử để lịch sử có thể tìm kiếm nhị phân và hoàn tác. Sự đánh đổi là thật: bạn trả một quy ước ban đầu và cần thực thi, đổi lấy ghi chú phát hành được sinh tự động và lịch sử đáng tin cậy. Hãy mang tín hiệu về những gì bạn làm thủ công hiện nay, như viết tay nhật ký thay đổi hoặc tìm xem commit nào đã đưa vào một hồi quy. Nếu bạn phát hành thường xuyên hoặc bảo trì nhiều phiên bản, tự động hóa thường tự hoàn vốn; nếu bạn hiếm khi cắt bản phát hành, một quy ước nhẹ hơn có thể là đủ. Hãy để hook và CI thực thi định dạng để nó không dựa vào trí nhớ.

3. **Bạn đã chấp nhận chi phí vận hành mà cấu trúc kho mã của bạn đòi hỏi chưa, dù là công cụ monorepo hay điều phối xuyên kho?** Chương này nói cả monorepo và polyrepo đều hoạt động ở quy mô lớn, và rằng lựa chọn sai với mô hình liên kết của bạn mới tạo ra ma sát liên tục. Một monorepo cần công cụ dựng có quy mô và kiểm soát truy cập chi tiết hơn, trong khi polyrepo biến mọi thay đổi trải qua nhiều kho thành một dự án điều phối với rủi ro lệch phiên bản. Hãy mang tín hiệu cụ thể: các thay đổi của bạn vượt qua ranh giới dự án thường xuyên đến mức nào, và công cụ dựng cùng truy cập của bạn có thể gánh được cấu trúc bạn có không. Nếu các thay đổi nguyên tử xuyên dự án là phổ biến, hãy đầu tư vào công cụ monorepo; nếu các đội và dịch vụ thực sự độc lập, hãy chấp nhận chi phí điều phối xuyên kho một cách có chủ đích. Điểm mấu chốt là khớp cấu trúc với mức độ liên kết thực sự của mã của bạn, rồi tài trợ công cụ mà cấu trúc đó đòi hỏi.

4. **Nếu một thông tin xác thực đang sống được commit vào một kho bận rộn ngay bây giờ, bạn sẽ phát hiện nó nhanh đến đâu, và việc xoay vòng có thực sự tự động hay chỉ là hy vọng?** Chương này coi bất kỳ bí mật nào lọt vào lịch sử là bị xâm phạm và cảnh báo rằng gỡ nó sau này là khó và không đáng tin cậy, nên phòng ngừa và xoay vòng nhanh là những biện pháp bảo vệ thực sự duy nhất. Với một đội lớn, rủi ro cộng dồn: một bí mật được đẩy lên kho dùng chung được sao chép vào hàng chục máy và nhân bản vào bộ nhớ đệm CI trong vài phút, nên một phản ứng chậm của con người đảm bảo một vụ vi phạm. Cân nhắc đối lập là ma sát: quét trước commit quyết liệt và xoay vòng bắt buộc làm chậm mọi người và tạo ra dương tính giả, nên bạn phải tinh chỉnh các biện pháp kiểm soát thay vì tắt chúng. Hãy mang bằng chứng: việc quét bí mật có chạy cả trong hook trước commit lẫn CI không, thời gian trung bình để phát hiện và xoay vòng một vụ lộ đã biết của bạn, và kỹ sư có hệ thống quản lý bí mật loại bỏ cám dỗ mã hóa cứng hay không. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn điều này với quy trình sự cố và quy tắc lưu giữ của bạn, vì một thông tin xác thực bị lộ trong một lịch sử có thể kiểm toán vừa là sự kiện bảo mật vừa là sự kiện tuân thủ, và cơ quan quản lý sẽ hỏi ai đã biết và hành động nhanh thế nào.

5. **Các nhánh của bạn có thực sự sống ngắn không, và ở nơi chúng không, vì sao công việc chưa xong lại được đỗ trên một nhánh thay vì ẩn sau một cờ tính năng?** Chương này nghiêng mạnh về phát triển dựa trên thân chính vì sự phân kỳ kéo dài là gốc rễ của nỗi đau hợp nhất, và đưa cờ tính năng ra như cơ chế cho phép bạn hợp nhất công việc chưa hoàn thành một cách an toàn thay vì cô lập nó hàng tuần. Trong một đội lớn đây là thuộc tính điều phối, không phải sở thích cá nhân: mỗi nhánh sống hàng tuần trở thành một bản rẽ nhánh riêng của thực tế mà ai đó cuối cùng phải dung hòa, và chi phí của việc dung hòa đó tăng theo quy mô nhân sự. Cân nhắc đối lập là cờ tính năng có chi phí riêng, bao gồm độ phức tạp lúc chạy, kiểm thử các tổ hợp, và những cờ lỗi thời phải bị loại bỏ. Hãy mang dữ liệu: phân phối thực tế về tuổi thọ nhánh của bạn, tích hợp tạo ra xung đột hoặc bất ngờ thường xuyên đến mức nào, và hiện có bao nhiêu nhánh sống lâu và vì sao. Với một tổ chức lớn hoặc chịu quy định, hãy thêm bức tranh phát hành, vì việc hỗ trợ nhiều phiên bản thực sự có thể biện minh cho các nhánh phát hành sống lâu với việc chuyển ngược bản vá có kỷ luật, và đó là một quyết định khác với việc đỗ công việc tính năng hằng ngày ra ngoài nhánh chính.

6. **Mọi thay đổi trong lịch sử của bạn có thể truy vết về tác giả và lý do của nó trong các ranh giới bảo mật phù hợp không, và điều đó có chịu được một cuộc kiểm toán không?** Chương này coi kiểm soát truy cập, đặc quyền tối thiểu và liên kết thay đổi với hạng mục công việc là một phần của khung kiểm soát của tổ chức, không phải sự đánh bóng tùy chọn. Với một đội lớn, khả năng truy vết là thứ biến một dòng commit mờ đục thành thứ bạn có thể suy luận trong một sự cố hoặc một cuộc rà soát tuân thủ, và ranh giới truy cập là thứ ngăn một tài khoản bị xâm phạm đơn lẻ chạm đến mã mà nó không bao giờ nên chạm. Cân nhắc đối lập là vận tốc của lập trình viên: liên kết hạng mục công việc bắt buộc, quyền hạn chi tiết và đánh giá bắt buộc thêm nghi thức mà một đội nhỏ, di chuyển nhanh có thể hợp lý bỏ qua. Hãy mang bằng chứng: các nhánh được bảo vệ có thực sự yêu cầu các kiểm tra và đánh giá bạn tuyên bố không, các commit có thực sự tham chiếu đến các hạng mục công việc đã được phê duyệt không, và quyền truy cập ánh xạ vào các ranh giới bảo mật thực của bạn hiện nay ra sao. Trong bối cảnh doanh nghiệp và chính phủ, hãy kết nối điều này với các nghĩa vụ phân loại, lưu giữ và kiểm toán, vì một lịch sử không thể kiểm toán hoặc một quyền truy cập quá rộng trở thành một phát hiện có thể dừng một chương trình hoặc làm hỏng một cuộc công nhận.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ và sự sống còn thắng. Dùng một kho duy nhất, làm việc dựa trên thân chính, hợp nhất các nhánh sống ngắn nhiều lần mỗi ngày, và ẩn công việc chưa hoàn thành sau các cờ tính năng đơn giản thay vì các nhánh dài. Bật quét bí mật ngay từ commit đầu tiên, vì một khóa bị lộ trong kho công khai có thể đánh chìm một công ty không có đội bảo mật để kiềm chế. Bỏ qua các mô hình phân nhánh cầu kỳ và quy trình nặng nề; một nhánh chính được bảo vệ và thông điệp commit có ý nghĩa là đủ kỷ luật để di chuyển nhanh.

**Doanh nghiệp nhỏ.** Không có chuyên gia nền tảng hay DevOps riêng và ngân sách eo hẹp, hãy mua các mặc định được quản lý thay vì xây dựng chúng. Một nhà cung cấp Git lưu trữ cho bạn bảo vệ nhánh, đánh giá bắt buộc và quét bí mật ngay từ đầu, vì vậy hãy dựa vào chúng thay vì tự lưu trữ một máy chủ mà bạn không thể bảo trì. Hãy đóng khung quyết định như vệ sinh dữ liệu: biết kho nào chứa cấu hình nhạy cảm, giữ thông tin xác thực trong trình quản lý bí mật của nhà cung cấp, và để nền tảng thực thi vài quy tắc bạn thực sự cần.

**Doanh nghiệp lớn.** Bài toán khó là nhất quán qua nhiều đội. Hãy chuẩn hóa bảo vệ nhánh, quy ước commit và quét bí mật như chính sách toàn tổ chức để các nhóm thôi phát minh lại chúng, và đưa ra lựa chọn monorepo hay polyrepo một cách có chủ đích theo từng mô hình liên kết, tài trợ công cụ dựng có quy mô hoặc điều phối xuyên kho mà nó đòi hỏi. Định tuyến các thay đổi đến đúng người đánh giá bằng quy tắc sở hữu mã, liên kết commit với hạng mục công việc để truy vết, và coi vệ sinh quản lý phiên bản như một biện pháp kiểm soát được quản trị với chủ sở hữu và chỉ số thay vì vấn đề thói quen cá nhân.

**Chính phủ.** Quy tắc mua sắm, tính minh bạch và trách nhiệm giải trình trước công chúng định hình toàn bộ cách thiết lập. Yêu cầu mọi commit tham chiếu một hạng mục công việc đã được phê duyệt, kiểm soát truy cập theo từng ranh giới phân loại, và biến quét bí mật cùng xoay vòng tức thì thành bắt buộc dưới một quy trình sự cố có tài liệu. Hỗ trợ nhiều phiên bản đã triển khai bằng các nhánh phát hành sống lâu và chuyển ngược bản vá có kỷ luật ở nơi các địa điểm không thể nâng cấp cùng lúc, và giữ lịch sử có thể kiểm toán và được lưu giữ để các yêu cầu công nhận, tự do thông tin và giám sát có thể được trả lời mà không phải xoay xở.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp ba người làm việc dựa trên thân chính vừa do thói quen vừa do cần thiết, hợp nhất các nhánh sống ngắn vào nhánh chính nhiều lần mỗi ngày và ẩn các tính năng làm dở sau các cờ đơn giản. Họ bật quét bí mật trong CI từ commit đầu tiên, vì một khóa API bị lộ trong kho công khai có thể đánh chìm một công ty không có đội bảo mật để kiềm chế hậu quả. Một kho duy nhất, một nhánh chính được bảo vệ và thông điệp commit có ý nghĩa cho họ đủ kỷ luật để di chuyển nhanh mà không vấp vào lịch sử của chính mình.

**Doanh nghiệp lớn.** Một công ty công nghệ lớn vận hành một monorepo với hàng trăm dịch vụ và thư viện dùng chung. Công cụ dựng có quy mô và quy tắc sở hữu mã định tuyến mỗi thay đổi đến đúng người đánh giá. Một commit đơn lẻ có thể cập nhật nguyên tử một thư viện dùng chung và mọi bên dùng cùng lúc, tránh các vấn đề lệch phiên bản ám ảnh các kho phân tán. Phát triển dựa trên thân chính với cờ tính năng giữ nhánh chính sẵn sàng phát hành, và quét bí mật chặn thông tin xác thực ngay lúc commit trên toàn kho.

**Chính phủ.** Một nhà thầu quốc phòng quốc gia giữ vững khả năng truy vết nghiêm ngặt. Mọi commit phải tham chiếu một hạng mục công việc đã được phê duyệt. Bảo vệ nhánh yêu cầu quét bảo mật đạt và đánh giá độc lập, và truy cập được kiểm soát chặt chẽ theo từng ranh giới phân loại. Quét bí mật là bắt buộc, và bất kỳ thông tin xác thực nào bị lộ đều kích hoạt xoay vòng tức thì dưới một quy trình sự cố. Các nhánh phát hành sống lâu hỗ trợ nhiều phiên bản đã triển khai qua các địa điểm không thể nâng cấp cùng lúc, với việc chuyển ngược các bản vá bảo mật có kỷ luật.

## Luận chứng kinh doanh: động lực, ROI và TCO

Quản lý mã nguồn tốt gần như miễn phí để áp dụng và đắt đỏ khi thiếu. Phát triển dựa trên thân chính và tích hợp liên tục là một trong những thực hành gắn bó chặt chẽ nhất với hiệu suất phân phối phần mềm cao, vốn lại tương quan với kết quả tổ chức tốt hơn. Lịch sử sạch, truy vết được cắt giảm thời gian chẩn đoán sự cố và đáp ứng kiểm toán, và phân nhánh có kỷ luật giúp bạn tránh chi phí lặp lại, không có trong ngân sách của các cuộc khủng hoảng tích hợp và những cuộc marathon hợp nhất.

Rủi ro lệch lớn nhất là bí mật trong hệ thống quản lý phiên bản. Một thông tin xác thực bị lộ đơn lẻ có thể gây ra một vụ vi phạm mà chi phí vượt xa mọi khoản đầu tư công cụ, và lịch sử khiến những vụ lộ như vậy tồn tại dai dẳng. Phòng ngừa chúng thì rẻ; dọn dẹp sau đó thì không. Các lựa chọn cấu trúc kém thể hiện ở ma sát kinh niên: mỗi thay đổi xuyên kho trở thành một dự án điều phối, hoặc mỗi bản dựng monorepo trở thành nút thắt. Để thuyết phục ban lãnh đạo, hãy gắn chiến lược phân nhánh của bạn với các chỉ số phân phối và thời gian chẩn đoán sự cố, và trình bày quét bí mật cùng kiểm soát truy cập như những biện pháp kiểm soát chi phí thấp chống lại rủi ro vi phạm và kiểm toán chi phí cao.

## Phản mẫu và cạm bẫy

- **Nhánh phân kỳ sống lâu:** nhiều tuần công việc cô lập hợp nhất thành những sự kiện tích hợp đau đớn, rủi ro.
- **Bí mật trong lịch sử:** thông tin xác thực mã hóa cứng tồn tại mãi trong các bản sao và đòi hỏi xoay vòng một khi bị lộ.
- **Commit tệp nhị phân lớn vào lịch sử chính:** làm phình vĩnh viễn mọi bản sao và làm chậm mọi thao tác.
- **Thông điệp commit vô nghĩa:** "fix", "wip", "changes" phá hủy giá trị của lịch sử như tài liệu.
- **Commit mã sinh ra như thể viết tay:** diff nhiễu, xung đột hợp nhất và nhầm lẫn về nguồn sự thật.
- **Cấu trúc kho sai với mức liên kết:** polyrepo cho mã liên kết chặt, hoặc monorepo không có công cụ có quy mô.
- **Nhánh chính không được bảo vệ:** không có kiểm tra bắt buộc, nên mã hỏng hoặc chưa được đánh giá đến được nhánh mà mọi người phụ thuộc.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Tùy nghi và phản ứng. Phân nhánh được ứng biến, các nhánh sống nhiều tuần, thông điệp commit nói "fix" hay "wip", không có quét bí mật, và tích hợp loạng choạng từ khủng hoảng hợp nhất này sang khủng hoảng khác.
- **Mức 2, Phát triển:** Các thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Một mô hình phân nhánh và quy ước thông điệp tồn tại ở một số nơi, nhưng các nhánh vẫn sống quá lâu, việc thực thi chỉ một phần, quét bí mật chắp vá, và cấu trúc kho được thừa kế thay vì được chọn.
- **Mức 3, Chuẩn hóa:** Các thực hành được lập thành tài liệu và thực thi toàn tổ chức: phát triển dựa trên thân chính với nhánh ngắn, nhánh chính được bảo vệ và luôn sẵn sàng phát hành, quy ước commit được thực thi, quét bí mật cả trong hook lẫn CI, truy cập đặc quyền tối thiểu, và lựa chọn monorepo hay polyrepo có chủ đích.
- **Mức 4, Quản lý:** Các thực hành mã nguồn được đo lường và kiểm soát bằng dữ liệu. Bạn theo dõi tuổi thọ nhánh, tần suất tích hợp, tỷ lệ nhánh chính hỏng, thời gian trung bình để phát hiện và xoay vòng một bí mật bị lộ, và khả năng truy vết từ thay đổi đến hạng mục công việc so với các đường cơ sở đã thống nhất, và bạn hành động khi các con số trôi dạt thay vì chờ sự cố tiếp theo.
- **Mức 5, Điều phối:** Các thực hành được cải tiến liên tục và tích hợp trong toàn tổ chức. Phân nhánh, cấu trúc kho và công cụ thích ứng khi các đội và độ liên kết của mã thay đổi, tự động hóa thực thi vệ sinh từ đầu đến cuối, và dữ liệu quản lý phiên bản nuôi dưỡng các quyết định phân phối, bảo mật và rủi ro trên toàn tổ chức.

## Ý tưởng để thảo luận

- Tuổi thọ nhánh của đội bạn có thực sự ngắn không, và nếu không, điều gì đang ngăn cản tích hợp liên tục?
- Lựa chọn monorepo hay polyrepo của bạn có khớp với mức độ liên kết thực sự của mã không?
- Hiện nay bạn xử lý các tệp nhị phân lớn và hiện vật sinh ra thế nào, và nó tốn của bạn gì?
- Điều gì sẽ xảy ra nếu một thông tin xác thực đang sống bị commit ngay bây giờ, và bạn sẽ phát hiện cùng xoay vòng nó nhanh đến đâu?
- Bao nhiêu kỷ luật về thông điệp commit và khả năng truy vết đáng để thực thi trong bối cảnh của bạn?
- Cờ tính năng thay đổi chiến lược phân nhánh của bạn thế nào, và chúng đưa vào những rủi ro mới nào?

## Những điểm cần ghi nhớ

- Tích hợp thường xuyên với các nhánh sống ngắn; sự phân kỳ kéo dài gây ra chính nỗi đau mà nó có vẻ tránh.
- Giữ nhánh chính sẵn sàng phát hành và được bảo vệ bằng các kiểm tra bắt buộc.
- Không bao giờ để bí mật vào lịch sử; quét tự động và xoay vòng ngay nếu chúng lọt vào.
- Chọn monorepo hay polyrepo theo nhu cầu liên kết và điều phối thực của bạn.
- Coi lịch sử commit là tài liệu, với các commit có ý nghĩa, theo quy ước, nguyên tử.

## Tài liệu tham khảo và đọc thêm

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble và David Farley, *Continuous Delivery*
- Scott Chacon và Ben Straub, *Pro Git*
- Paul Hammant và những người khác, các bài viết về phát triển dựa trên thân chính
- Đặc tả Conventional Commits (như một tiêu chuẩn tham chiếu)
- Martin Fowler, các bài viết về các mẫu phân nhánh và tích hợp liên tục
