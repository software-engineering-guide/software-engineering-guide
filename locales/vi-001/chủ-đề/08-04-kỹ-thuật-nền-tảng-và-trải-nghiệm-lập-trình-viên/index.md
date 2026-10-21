# 8.4 Kỹ thuật nền tảng và trải nghiệm lập trình viên

## Tổng quan và động lực

[Kỹ thuật nền tảng](https://en.wikipedia.org/wiki/Platform_engineering) là kỷ luật xây dựng và vận hành một sản phẩm nội bộ, một nền tảng lập trình viên nội bộ (IDP), mà các kỹ sư khác dùng để xây, phát hành và vận hành phần mềm của họ. Thay vì mỗi đội tự lắp ráp đường ống, hạ tầng và công cụ từ đầu, một đội nền tảng chuyên trách cung cấp các năng lực tự phục vụ được chọn lọc dọc theo các "con đường vàng" được hỗ trợ tốt, là những tuyến có chính kiến, được hỗ trợ với mặc định hợp lý được nướng vào. [Trải nghiệm lập trình viên](https://en.wikipedia.org/wiki/Developer_experience) (DevEx) là mối quan tâm liên quan chặt chẽ về cảm giác làm kỹ sư trong tổ chức: một lập trình viên đi từ ý tưởng đến phần mềm đang chạy dễ và nhanh đến đâu, và bao nhiêu ma sát cản đường.

Với các đội lớn, điều này quan trọng vì [tải nhận thức](https://en.wikipedia.org/wiki/Cognitive_load) và ma sát không mở rộng êm. Khi bạn có nhiều đội, số công cụ, hệ thống và quyết định mỗi kỹ sư phải xoay xở cứ tăng. Chẳng bao lâu, một phần lớn thời gian của họ dành cho hệ thống ống dẫn hạ tầng và phối hợp thay vì tạo giá trị. Không có nền tảng, mỗi đội giải cùng những vấn đề, như cung cấp, triển khai, khả năng quan sát và tuân thủ, một cách không nhất quán và lặp đi lặp lại. Một nền tảng tốt hấp thụ độ phức tạp dùng chung này. Các đội rồi tập trung vào miền của mình trong khi vẫn thừa hưởng tiêu chuẩn của tổ chức về bảo mật, độ tin cậy và chi phí.

Sự liên quan với doanh nghiệp và chính phủ là cao, vì các tổ chức này kết hợp quy mô với quản trị nghiêm ngặt. Một nền tảng là nơi tự nhiên để mã hóa yêu cầu tuân thủ, bảo mật và kiểm toán một lần, như những con đường lát sẵn mà các đội theo theo mặc định. Điều đó thắng việc kỳ vọng mọi đội tự diễn giải và triển khai chính sách đúng. Nó biến quản trị từ nguồn ma sát thành thuộc tính vô hình của quy trình chuẩn, chính xác điều các tổ chức lớn chịu quy định cần để đi nhanh mà không mất kiểm soát.

## Các nguyên tắc chính

- Coi nền tảng là một sản phẩm, với người dùng, lộ trình, và nhiệm vụ giành sự áp dụng thay vì ép buộc nó.
- Cung cấp con đường vàng: các tuyến có chính kiến, được hỗ trợ tốt làm cho cách đúng thành cách dễ.
- Làm năng lực tự phục vụ để các đội không chờ phiếu và bàn giao của con người.
- Lát đường thay vì dựng cổng; xây lan can hướng dẫn mà không chặn công việc chính đáng.
- Không ngừng giảm tải nhận thức cho lập trình viên ứng dụng.
- Đo trải nghiệm và năng suất lập trình viên bằng các tín hiệu cân bằng, đa chiều.
- Giữ con đường vàng là tùy chọn nhưng tốt đến mức các đội chọn chúng.

## Khuyến nghị

### Xây nền tảng như một sản phẩm

Sự chuyển dịch quan trọng nhất đơn lẻ là coi nền tảng là sản phẩm phục vụ khách hàng nội bộ, không phải tiêu chuẩn bắt buộc áp từ trên xuống. Trong thực tế, điều đó nghĩa là hiểu nhu cầu lập trình viên qua nghiên cứu và phản hồi, duy trì lộ trình, đo mức áp dụng và sự hài lòng, và chịu trách nhiệm về trải nghiệm. Một nền tảng mà các đội bị buộc dùng nhưng làm họ chậm sẽ bị oán và bị đi vòng. Một nền tảng thực sự khiến các đội nhanh hơn sẽ lan bằng danh tiếng. Sự áp dụng giành được nhờ chất lượng là thước đo chân thực nhất của thành công nền tảng.

### Cung cấp con đường vàng và đường lát sẵn

Hãy xác định con đường vàng cho các hành trình phổ biến: tạo dịch vụ mới, triển khai nó, thêm cơ sở dữ liệu, nối khả năng quan sát, đáp ứng yêu cầu tuân thủ. Một con đường vàng là tuyến đầu-đến-cuối được hỗ trợ, có chính kiến với mặc định hợp lý được nướng vào. Dọc theo các con đường này, hãy nhúng lan can, nghĩa là quét bảo mật, kiểm tra chính sách và thực hành tốt, để một đội theo con đường tự động tuân thủ và an toàn. Mục tiêu đơn giản: cách dễ nhất để làm một việc cũng phải là cách đúng, an toàn và tuân thủ. Giữ các con đường là tùy chọn, để các đội có nhu cầu thực sự bất thường có thể rẽ. Nhưng hãy làm các con đường đủ hấp dẫn để hầu hết đội không bao giờ muốn rẽ.

### Cung cấp hạ tầng tự phục vụ đích thực

Hãy loại bỏ bàn giao phiếu-và-chờ bằng cách phơi hạ tầng và năng lực qua giao diện tự phục vụ: một cổng, công cụ dòng lệnh, API, hoặc kho mẫu. Một lập trình viên nên có thể cung cấp môi trường tuân thủ, dựng dịch vụ mới từ mẫu, hay yêu cầu cơ sở dữ liệu trong vài phút, mà không nộp yêu cầu và chờ nhiều ngày cho đội khác. Tự phục vụ là thứ biến nền tảng từ nút thắt thành bộ tăng tốc. Và nó chỉ hoạt động vì các lan can bên dưới làm tự phục vụ an toàn.

### Cung cấp cổng lập trình viên, danh mục dịch vụ và bảng điểm

Một cổng lập trình viên cho bạn một ô kính duy nhất: danh mục mọi dịch vụ với chủ sở hữu, tài liệu, phụ thuộc và sức khỏe của chúng. Danh mục dịch vụ làm quyền sở hữu và kiến trúc khám phá được. Điều đó vô giá ở quy mô, nơi không ai giữ được toàn bộ hệ thống trong đầu. Bảng điểm đo mỗi dịch vụ so với tiêu chuẩn như độ phủ kiểm thử, tư thế bảo mật, sẵn sàng trực và tài liệu, và cho các đội bức tranh rõ ràng, khách quan về họ đang ở đâu và cần cải thiện gì. Cùng nhau, các công cụ này cắt thời gian kỹ sư săn thông tin, và chúng làm rõ trách nhiệm giải trình.

### Đo trải nghiệm lập trình viên bằng khung cân bằng

Hãy chống lại chỉ số năng suất một con số. Chúng dễ bị thao túng và gây hiểu lầm. Dùng khung đa chiều như SPACE (sự hài lòng và phúc lợi, hiệu suất, hoạt động, giao tiếp và cộng tác, hiệu quả và dòng chảy) để nắm bắt kết cấu thực của trải nghiệm lập trình viên. Kết hợp dữ liệu cảm nhận từ khảo sát với dữ liệu hệ thống từ công cụ. Theo dõi chỉ số phân phối như thời gian chờ và tần suất triển khai cùng cảm nhận của lập trình viên. Mục tiêu là hiểu và loại bỏ ma sát, không phải xếp hạng cá nhân. Đo lường mang cảm giác giám sát sẽ ăn mòn lòng tin mà nền tảng phụ thuộc.

### Giảm tải nhận thức như mục tiêu hạng nhất

Tải nhận thức, tổng công sức tinh thần một lập trình viên phải bỏ ra để làm việc, là khoản thuế ẩn mà nền tảng tồn tại để giảm. Hãy tối thiểu hóa số công cụ, khái niệm và lần chuyển ngữ cảnh một lập trình viên ứng dụng phải nắm. Cung cấp mặc định hợp lý, để các đội đưa ra ít quyết định giá trị thấp hơn. Cấu trúc quyền sở hữu để mỗi đội sở hữu một lát cắt có giới hạn, dễ hiểu của hệ thống. Khi đánh giá bất kỳ tính năng nền tảng nào, hãy hỏi một câu: nó giảm hay tăng tải lên các đội sẽ dùng nó?

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Nền tảng như sản phẩm (tự nguyện) | Giành được sự áp dụng; giữ được hữu ích | Chậm đạt độ phủ đầy đủ | Hầu hết tổ chức |
| Nền tảng bắt buộc | Chuẩn hóa nhanh | Oán giận; cách lách | Chỉ nhu cầu quản trị mạnh |
| Mua cổng/nền tảng | Nhanh ra giá trị | Ít vừa vặn hơn; chi phí giấy phép | Đội muốn khởi đầu thuận lợi |
| Xây nội bộ | Vừa chính xác nhu cầu | Chi phí xây và bảo trì cao | Tổ chức lớn, đặc thù |
| Chỉ con đường vàng cứng | Nhất quán tối đa | Chặn trường hợp biên chính đáng | Khối lượng công việc rất đồng đều |
| Đường linh hoạt có lối thoát | Cân bằng nhất quán và tự chủ | Một ít phân kỳ phải quản lý | Nhu cầu đội đa dạng |

Căng thẳng cốt lõi là chuẩn hóa so với tự chủ. Quá ít chuẩn hóa thì mỗi đội phát minh lại bánh xe không nhất quán. Quá nhiều thì bạn bóp nghẹt các đội có nhu cầu thực sự khác. Triết lý nền tảng-như-sản-phẩm giải quyết điều này bằng cách làm chuẩn hóa hấp dẫn thay vì bắt buộc. Đánh đổi thật thứ hai là xây so với mua. Xây nền tảng nội bộ vừa chính xác nhu cầu của bạn nhưng mang chi phí liên tục đáng kể. Áp dụng công cụ có sẵn tăng tốc giá trị, với cái giá là một ít tùy biến.

## Câu hỏi để thảo luận với đội của bạn

1. **Làm sao bạn biết nền tảng đang giảm tải nhận thức chứ không thêm một công cụ nữa để học?** Tải nhận thức là tổng công sức tinh thần một kỹ sư bỏ ra để làm việc, và một nền tảng thêm khái niệm và lần chuyển ngữ cảnh có thể làm nó tệ hơn ngay cả khi trông ấn tượng. Hãy áp dụng một phép thử cho mọi tính năng: nó giảm hay tăng tải lên các đội dùng nó? Ở quy mô điều này mang tính quyết định, vì một nền tảng đứng trước hàng trăm kỹ sư và một trừu tượng gây rối đánh thuế tất cả họ hằng ngày. Hãy mang bằng chứng: một lập trình viên chạm bao nhiêu công cụ và cổng để phát hành một thay đổi, thời gian-đến-lần-triển-khai-đầu-tiên của một nhân viên mới, và phản hồi định tính về nơi mọi người mắc kẹt. Nếu nền tảng làm bộ công cụ lớn lên thay vì thu nhỏ, bạn đã xây một khoản thuế, không phải một con đường lát sẵn.

2. **Bảng điểm của bạn thực thi những tiêu chuẩn nào, và điều gì thực sự xảy ra với một dịch vụ điểm kém?** Bảng điểm đo mỗi dịch vụ so với kỳ vọng như độ phủ kiểm thử, tư thế bảo mật, sẵn sàng trực và tài liệu, và giá trị của chúng sụp đổ nếu điểm đỏ không mang hậu quả. Hãy quyết định liệu bảng điểm thuần khuyến cáo, nuôi rà soát, hay chặn cổng một số năng lực, và quyết định ai sở hữu các tiêu chuẩn. Trong các tổ chức chịu quy định, bảng điểm có thể cho các cơ quan giám sát tầm nhìn liên tục về tư thế tuân thủ, thay báo cáo thủ công, nên thanh chuẩn bạn đặt rất quan trọng. Hãy mang bản nháp tiêu chuẩn của bạn và một mẫu dịch vụ thật được chấm điểm theo chúng, và thảo luận nơi các đội sẽ phản đối chính đáng. Một bảng điểm không ai hành động là một bảng điều khiển; một bảng điểm gắn với kỳ vọng rõ ràng thay đổi hành vi.

3. **Bạn đang vận hành nền tảng như một sản phẩm thật, với lộ trình, nghiên cứu người dùng và chỉ số áp dụng, hay như một mệnh lệnh?** Canh bạc trung tâm của chương này là chuẩn hóa nên hấp dẫn thay vì bị ép buộc, và điều đó chỉ đúng nếu bạn coi kỹ sư nội bộ là khách hàng bạn phải giành được. Hãy quyết định ai đóng vai quản lý sản phẩm cho nền tảng, bạn thu thập nhu cầu lập trình viên thế nào, và những con số áp dụng cùng hài lòng nào xác định thành công. Với tổ chức lớn, mệnh lệnh hấp dẫn vì nó chuẩn hóa nhanh, nhưng nó nuôi cách lách và oán giận khi công cụ làm mọi người chậm. Hãy mang tỷ lệ áp dụng tự nguyện hiện tại, tín hiệu hài lòng, và các điểm ma sát hàng đầu mà các đội báo cáo hôm nay. Nếu các đội sẽ bỏ nền tảng ngay khi mệnh lệnh được gỡ, bạn chưa xây một sản phẩm, bạn đã xây một chính sách.

4. **Khi một đội đến rìa của con đường vàng, lối thoát là gì, và ai quyết định mở rộng con đường hay giữ vững lằn ranh?** Một con đường vàng là tuyến có chính kiến, được hỗ trợ với mặc định hợp lý, và giá trị của nó đến từ việc hầu hết đội ở lại trên nó, vậy mà một con đường không lối thoát thành cổng đẩy công việc thực sự bất thường hoàn toàn ra khỏi nền tảng. Hãy thống nhất từ trước một đội yêu cầu một sự lệch thế nào, ai rà soát nó, và bạn phân biệt ngoại lệ một lần với tín hiệu rằng chính con đường nên đổi thế nào. Với một tổ chức lớn đây là sự khác biệt giữa nền tảng hấp thụ sự đa dạng và nền tảng phân mảnh thành công cụ bóng ngay khi một đội cảm thấy bị chặn. Hãy mang số đội hiện đã rời con đường, lý do họ nêu, và một ngoại lệ mất bao lâu để duyệt. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn mỗi lối thoát với các kiểm soát tuân thủ nó bỏ qua, để một sự lệch khỏi con đường lát sẵn không bao giờ lặng lẽ thành sự lệch khỏi đường cơ sở bảo mật hay kiểm định.

5. **Bạn xây nền tảng nội bộ hay mua nó, và bạn đã định giá trung thực chi phí liên tục của cả hai con đường chưa?** Nền tảng tự nó là sản phẩm có vòng đời, và lựa chọn xây-hay-mua đặt cấu trúc chi phí của bạn trong nhiều năm: một cổng nội bộ vừa chính xác nhu cầu nhưng đòi một đội được tài trợ bảo trì, trong khi nền tảng mua đạt giá trị nhanh hơn với giá giấy phép và độ vừa vặn không bao giờ hoàn hảo. Hãy quyết định năng lực nào đủ khác biệt hóa để xây và cái nào là hàng hóa bạn nên mua, và xem xét lại lằn ranh đó khi nhà cung cấp trưởng thành. Với một đội lớn rủi ro là đòn bẩy: một quyết định xây sai nhấn chìm kỹ sư cấp cao khan hiếm vào hệ thống ống dẫn mà một sản phẩm đã xử lý, trong khi quyết định mua sai khóa hàng trăm lập trình viên vào lộ trình của người khác. Hãy mang ước tính tổng chi phí thực tế cho mỗi lựa chọn, gồm bảo trì, nâng cấp và chi phí thoát. Trong mua sắm doanh nghiệp và chính phủ, hãy thêm điều khoản kiểm định và di chuyển dữ liệu, và ưu tiên hợp đồng cho phép bạn rời đi mà không bỏ rơi danh mục dịch vụ và bảng điểm bạn đã xây bên trên.

6. **Đội nền tảng được tài trợ và định cỡ so với số lập trình viên nó phục vụ thế nào, và điều gì xảy ra với nó khi ngân sách thắt chặt?** Một nền tảng kiếm được chỗ đứng nhờ đòn bẩy, vì một đội nhỏ nhân năng suất của một quần thể lập trình viên ứng dụng lớn hơn nhiều, nhưng chính cách đóng khung đó khiến nó là mục tiêu dễ khi tài chính tìm cắt giảm và lợi ích phân tán chứ không quy được cho một dòng sản phẩm. Hãy quyết định mô hình tài trợ, tỷ lệ kỹ sư nền tảng so với lập trình viên họ hỗ trợ, và bạn sẽ bảo vệ khoản đầu tư đó bằng bằng chứng thay vì đức tin thế nào. Với một tổ chức lớn, một nền tảng thiếu tài trợ còn tệ hơn không có: các đội phụ thuộc vào nó, nó mục rữa, và ma sát quay lại kèm một phụ thuộc. Hãy mang số nhân sự của nền tảng, xu hướng áp dụng và hài lòng của nó, và ước tính giờ lập trình viên thu hồi được toàn tổ chức. Trong chính phủ và doanh nghiệp chịu quy định, hãy đóng khung nền tảng là nơi tuân thủ được mã hóa một lần, để cắt nó không tiết kiệm tiền, mà tái rải công việc kiểm toán và bảo mật qua mọi đội giờ phải làm nó bằng tay.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không có đường băng dư, đừng dựng đội nền tảng; hãy xây một kho mẫu con đường vàng mà một dịch vụ mới có thể nhân bản và chạy trong một giờ. Nối sẵn nó với CI, bản dựng container, linting và kiểm tra sức khỏe, và để nó lan vì rõ ràng tiết kiệm thời gian, không phải vì ai bắt buộc. Mua mọi năng lực hàng hóa bạn có thể, giữ bộ công cụ nhỏ, và coi tải nhận thức, không phải độ phủ, là thứ cần bảo vệ.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia nền tảng riêng và ngân sách eo hẹp, vì vậy hãy dựa vào nền tảng được quản lý hoặc dịch vụ đám mây có chính kiến thay vì tự xây nền tảng lập trình viên nội bộ. Đóng khung quyết định như mua-so-với-xây và mặc định mua: một cổng mua và mẫu của nó cho các kỹ sư tổng quát của bạn con đường vàng mà không cần đội bảo trì. Chọn công cụ tự phục vụ và dễ rời, để việc đổi nhà cung cấp không làm mắc kẹt nhúm dịch vụ bạn chạy.

**Doanh nghiệp lớn.** Quy mô và nhiều đội làm nhất quán danh mục là giải thưởng: một đội nền tảng được tài trợ, con đường vàng với lan can, cung cấp tự phục vụ, danh mục dịch vụ, và bảng điểm làm quyền sở hữu và chất lượng hiển thị qua hàng trăm dịch vụ. Hãy vận hành nền tảng như sản phẩm giành sự áp dụng tự nguyện thay vì mệnh lệnh nuôi cách lách, và mã hóa bảo mật cùng tuân thủ một lần như đường lát sẵn để quản trị đi kèm theo mặc định. Đo trải nghiệm lập trình viên bằng khung cân bằng và bảo vệ tài trợ của nền tảng bằng giờ lập trình viên thu hồi.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình nền tảng. Hãy mã hóa các kiểm soát bảo mật bắt buộc và yêu cầu kiểm định thành lan can dọc con đường vàng, để một đội cung cấp hạ tầng qua cổng tự phục vụ thừa hưởng một môi trường đã đáp ứng đường cơ sở kiểm soát, biến nhiều tháng kiểm định thủ công thành bước phần lớn tự động. Dùng bảng điểm để cho các cơ quan giám sát tầm nhìn liên tục, kiểm toán được về tư thế tuân thủ, và trong mua sắm đòi khả năng di chuyển dữ liệu cùng giao diện mở để danh mục và đường lát sẵn bạn xây không bị khóa vào một nhà cung cấp.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười hai người không có đội nền tảng, nên một kỹ sư cấp cao dành vài chiều thứ Sáu xây một kho mẫu "dịch vụ mới" duy nhất được nối sẵn với CI, Dockerfile, linting và kiểm tra sức khỏe. Bất kỳ kỹ sư nào cũng có thể nhân bản nó và có một dịch vụ chạy trên staging trong vòng một giờ, thay vì sao chép cấu hình từ dự án cũ và đoán những chỗ thiếu. Mẫu là con đường vàng, và vì rõ ràng tiết kiệm thời gian của mọi người, cả đội áp dụng nó mà không ai phải nghe bảo.

**Doanh nghiệp lớn.** Một công ty bảo hiểm lớn lập một đội nền tảng phát hành cổng lập trình viên nội bộ. Nó lập danh mục mọi dịch vụ với chủ sở hữu, tài liệu và bảng điểm sức khỏe. Dịch vụ mới được tạo từ mẫu con đường vàng được nối sẵn với CI/CD, quét bảo mật, khả năng quan sát và kiểm tra tuân thủ. Cơ sở dữ liệu và môi trường được cung cấp tự phục vụ qua cổng. Thời gian làm quen của một kỹ sư mới giảm từ nhiều tuần xuống vài ngày, và bằng chứng kiểm toán được tạo tự động vì mọi dịch vụ theo cùng con đường lát sẵn. Việc áp dụng nền tảng là tự nguyện, và nó lan vì các đội dùng nó phát hành nhanh hơn rõ rệt.

**Chính phủ.** Một cơ quan liên bang chạy hàng chục dịch vụ số dựng một nền tảng dùng chung. Nó mã hóa các kiểm soát bảo mật bắt buộc và yêu cầu kiểm định thành lan can dọc con đường vàng. Một đội cung cấp hạ tầng qua cổng tự phục vụ thừa hưởng một môi trường đã thỏa mãn đường cơ sở kiểm soát. Điều đó biến bài tập kiểm định thủ công kéo dài nhiều tháng thành bài tập phần lớn tự động. Bảng điểm theo dõi tư thế tuân thủ của mỗi dịch vụ, cho cơ quan giám sát tầm nhìn liên tục mà không cần báo cáo thủ công, và giải phóng nhân viên chuyên môn khan hiếm khỏi rà soát lặp lại.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của kỹ thuật nền tảng đến từ thời gian lập trình viên thu hồi và tính nhất quán đạt được. Khi kỹ sư tốn ít thời gian hơn chiến đấu với hạ tầng và tìm thông tin, nhiều thời gian đắt giá của họ hơn dành cho giao giá trị sản phẩm. Làm quen nhanh hơn, ít giải pháp trùng lặp hơn, và tuân thủ tự động đều chuyển thành năng lực đo được và rủi ro giảm. Vì nền tảng phục vụ nhiều đội, mọi cải tiến của nó được đòn bẩy qua toàn tổ chức.

Về TCO, chi phí áp dụng là khoản đầu tư thật, liên tục: một đội nền tảng được tài trợ, công cụ (xây hay mua), và kỷ luật vận hành nền tảng như sản phẩm với cải tiến liên tục. Chi phí của việc không áp dụng phân tán nhưng lớn: mọi đội trả cùng một khoản thuế hạ tầng lặp đi lặp lại, bảo mật và tuân thủ không nhất quán, làm quen chậm, và kỹ sư cấp cao kiệt sức vì lao động nhàm chán. Với ban lãnh đạo, lập luận được đưa ra tốt nhất theo đòn bẩy. Một đội nền tảng khiêm tốn, vận hành tốt nhân năng suất của một quần thể lập trình viên ứng dụng lớn hơn nhiều, và nó mã hóa quản trị một lần thay vì dựa vào mọi đội làm đúng.

## Phản mẫu và cạm bẫy

- **Nền tảng bị áp đặt, không được đề nghị.** Bắt buộc một nền tảng lập trình viên không ưa nuôi cách lách và oán giận.
- **Đội nền tảng tháp ngà.** Xây mà không hiểu nhu cầu lập trình viên thực tạo ra công cụ không ai muốn.
- **Cổng thay vì đường lát sẵn.** Lan can chặn công việc chính đáng đẩy các đội bỏ qua hoàn toàn nền tảng.
- **Chỉ số năng suất đơn lẻ.** Rút gọn năng suất thành một con số dễ thao túng bóp méo hành vi và xói mòn lòng tin.
- **Đo lường như giám sát.** Chỉ số DevEx dùng để xếp hạng cá nhân phá hủy sự an toàn tâm lý mà nền tảng cần.
- **Con đường vàng không lối thoát.** Con đường cứng không uốn được cho trường hợp biên đích thực trở thành chướng ngại.
- **Nền tảng thiếu tài trợ.** Coi nền tảng là dự án phụ bỏ đói nó và bảo đảm trải nghiệm kém.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Không có nền tảng. Mỗi đội tự lắp ráp công cụ và hạ tầng một cách phản ứng, với bàn giao theo phiếu nặng nề, giải pháp trùng lặp và tải nhận thức cao. Mọi đội tự giải quyết cung cấp, triển khai và tuân thủ, không nhất quán.

**Mức 2: Phát triển.** Một số công cụ dùng chung, mẫu và kho khởi đầu xuất hiện, thường do một kỹ sư nhiệt tình xây, nhưng chúng phân mảnh và một phần thủ công. Vài đội áp dụng con đường vàng trong khi số khác phớt lờ, tự phục vụ hạn chế, và trải nghiệm lập trình viên không được đo, nên giá trị của nền tảng dựa trên giai thoại.

**Mức 3: Chuẩn hóa.** Một đội nền tảng vận hành các con đường vàng có tài liệu, cung cấp tự phục vụ, cổng lập trình viên với danh mục dịch vụ, và bảng điểm, áp dụng toàn tổ chức. Lan can cho bảo mật, chính sách và tuân thủ được nhúng trong đường lát sẵn, nên quy trình chuẩn là quy trình tuân thủ, và cùng quy ước đúng qua các đội thay vì thay đổi theo nhóm.

**Mức 4: Quản lý.** Nền tảng được đo và kiểm soát bằng dữ liệu theo đường cơ sở. Áp dụng, hài lòng, thời gian-đến-lần-triển-khai-đầu-tiên, thời gian chờ và tần suất triển khai được theo dõi bằng khung cân bằng như SPACE và tín hiệu khảo sát kết hợp hệ thống; kết quả bảng điểm nuôi rà soát, và tải nhận thức, thời gian làm quen và giờ lập trình viên thu hồi được giám sát theo mục tiêu. Quyết định đầu tư vào hay cho nghỉ hưu một năng lực dựa trên bằng chứng, không phải vận động.

**Mức 5: Điều phối.** Nền tảng là sản phẩm trưởng thành với mức áp dụng tự nguyện cao, được cải thiện liên tục từ phản hồi lập trình viên và chỉ số và tích hợp với hoạch định bảo mật, tuân thủ và phân phối toàn tổ chức. Con đường vàng thích ứng khi nhu cầu dịch chuyển, quản trị là thuộc tính vô hình của quy trình chuẩn, và đội nền tảng thường xuyên cho nghỉ hưu, thay thế và thu hẹp phạm vi năng lực khi công nghệ và tổ chức tiến hóa.

## Ý tưởng để thảo luận

- Làm sao bạn giành sự áp dụng cho một nền tảng mà không bắt buộc, và khi nào, nếu có, một mệnh lệnh được biện minh?
- Con đường vàng nào sẽ mang lại nhiều giá trị nhất cho các đội của bạn trước?
- Làm sao bạn đo trải nghiệm lập trình viên mà không để nó cảm giác như giám sát?
- Lối thoát nên tồn tại ở đâu để các đội bất thường không bị buộc rời hoàn toàn nền tảng?
- Kích thước và mô hình tài trợ đúng cho một đội nền tảng so với số lập trình viên nó phục vụ là gì?
- Làm sao bạn quyết định nên xây nội bộ gì so với mua cho cổng lập trình viên và công cụ?

## Những điểm cần ghi nhớ

- Vận hành nền tảng như một sản phẩm giành sự áp dụng bằng cách khiến các đội thực sự nhanh hơn.
- Cung cấp con đường vàng và đường lát sẵn làm cách đúng, an toàn, tuân thủ thành cách dễ.
- Giao tự phục vụ thật để các đội thôi chờ phiếu và bàn giao.
- Dùng cổng, danh mục và bảng điểm để làm quyền sở hữu, kiến trúc và chất lượng hiển thị.
- Đo trải nghiệm lập trình viên bằng khung cân bằng như SPACE, không bao giờ một con số dễ thao túng.
- Coi việc giảm tải nhận thức là mục đích trung tâm của nền tảng.

## Tài liệu tham khảo và đọc thêm

- Matthew Skelton và Manuel Pais, *Team Topologies*.
- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, et al., "The SPACE of Developer Productivity" (bài báo).
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate*.
- Gregor Hohpe, *The Software Architect Elevator*.
- Camille Fournier, *The Manager's Path*.
- Cloud Native Computing Foundation, sách trắng về kỹ thuật nền tảng.
