# 2.5 Đánh giá mã và cộng tác

## Tổng quan và động lực

[Đánh giá mã](https://en.wikipedia.org/wiki/Code_review) là thực hành nhờ một người khác ngoài tác giả xem xét một thay đổi trước khi nó được hợp nhất. Đó là một trong những hoạt động đảm bảo chất lượng và chia sẻ kiến thức có đòn bẩy cao nhất mà một tổ chức phần mềm có, và với các đội lớn nó cũng là cơ chế chính của sự điều phối và văn hóa. Đánh giá bắt lỗi, lan truyền kiến thức về cơ sở mã, thực thi tiêu chuẩn và cố vấn cho kỹ sư, nhưng chỉ khi bạn làm tốt. Làm tệ, nó trở thành nút thắt, nguồn ma sát, hoặc một con dấu đóng cho có, mang lại sự đảm bảo sai.

Với các đội lớn, đánh giá là nơi công việc cá nhân gặp quyền sở hữu tập thể. Nó thường là điểm tiếp xúc chính giữa các kỹ sư vốn làm việc riêng lẻ, nên các chuẩn mực của nó định hình cách cả tổ chức cộng tác. Đánh giá lan truyền kiến thức để không phần nào của hệ thống chỉ do một người hiểu, giảm rủi ro [hệ số xe buýt](https://en.wikipedia.org/wiki/Bus_factor), mối nguy khi kiến thức nằm ở quá ít người, vốn ám ảnh các hệ thống lớn, tồn tại lâu. Nó cũng tạo ra một dấu vết kiểm toán về ai đã thay đổi gì và ai đã phê duyệt.

Trong bối cảnh doanh nghiệp và chính phủ, đánh giá thường mang một chiều kích tuân thủ. [Phân tách nhiệm vụ](https://en.wikipedia.org/wiki/Separation_of_duties) (không một người nào kiểm soát toàn bộ một thay đổi nhạy cảm), các phê duyệt bắt buộc và khả năng truy vết thường là các biện pháp kiểm soát được yêu cầu. Một thay đổi chạm vào các hệ thống nhạy cảm có thể cần được các vai trò cụ thể đánh giá, và bản ghi đánh giá trở thành bằng chứng kiểm toán. Thách thức của bạn là thỏa mãn các biện pháp kiểm soát này trong khi giữ cho việc đánh giá nhanh và mang tính xây dựng, thay vì biến nó thành nghi thức.

## Các nguyên tắc chính

- Đánh giá để cải thiện thay đổi và chia sẻ kiến thức, không phải để phô trương.
- Các thay đổi nhỏ được đánh giá tốt hơn, vì vậy hãy giữ các pull request (PR) tập trung và có kích thước hợp lý.
- Độ trễ đánh giá là chi phí của cả đội. Phản hồi nhanh giữ cho mọi người tiến lên.
- Tự động hóa những thứ cơ học (phong cách, kiểm thử, quét bảo mật) để con người đánh giá thiết kế và tính đúng đắn.
- Tách các vấn đề chặn khỏi các gợi ý và sở thích, và nói rõ cái nào là cái nào.
- Phê bình mã, không phải con người. Chuẩn mực phản hồi quyết định liệu đánh giá xây dựng hay ăn mòn niềm tin.
- Tác giả chịu trách nhiệm làm cho một thay đổi dễ đánh giá.

## Khuyến nghị

### Làm cho pull request nhỏ và được mô tả tốt

Giữ mỗi thay đổi tập trung vào một mối quan tâm logic duy nhất và đủ nhỏ để đánh giá cẩn thận. Các PR lớn nhận được những lần đánh giá hời hợt. Hãy đưa ra mô tả rõ ràng về điều gì đã thay đổi, vì sao, và bạn đã xác minh bằng cách nào, để người đánh giá có ngữ cảnh. Tách các lần tái cấu trúc cơ học và thay đổi hành vi thành các PR riêng, để mỗi cái dễ suy luận. Một mô tả tốt là đóng góp quan trọng nhất của tác giả cho chất lượng đánh giá.

### Thiết lập tiêu chuẩn đánh giá và danh sách kiểm tra

Hãy nêu rõ người đánh giá nên tìm gì: tính đúng đắn, sự phù hợp của thiết kế, mức đủ của kiểm thử, hàm ý bảo mật, khả năng đọc, và tuân thủ tiêu chuẩn. Một danh sách kiểm tra nhẹ giữ cho các lần đánh giá nhất quán và ngăn các khía cạnh quan trọng bị bỏ sót, mà không biến đánh giá thành đánh dấu ô. Xác định điều gì cần đánh giá, ai có thể phê duyệt, và mọi phê duyệt theo vai trò cần thiết cho các khu vực nhạy cảm.

### Đặt và giám sát các chuẩn mực độ trễ đánh giá

Hãy thống nhất một thời gian phản hồi mục tiêu, chẳng hạn trả lời trong vòng một ngày làm việc, và biến đánh giá thành một phần hạng nhất của ngày làm việc thay vì thứ bị nhét vào sau cùng. Hàng đợi đánh giá dài làm đình trệ phân phối và cám dỗ kỹ sư gom thành các thay đổi quá lớn. Giám sát thời gian đến lần đánh giá đầu tiên và thời gian đến khi hợp nhất, và coi độ trễ kéo dài là một vấn đề quy trình cần sửa, không phải lỗi cá nhân.

### Tự động hóa mọi thứ mang tính cơ học

Chạy định dạng, [linter](https://en.wikipedia.org/wiki/Lint_(software)), kiểm thử, quét bảo mật và phụ thuộc trong [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI), để người đánh giá không bao giờ phải dành sự chú ý cho chúng. Hãy dành đánh giá của con người cho những điều máy móc không thể phán đoán: thiết kế có đúng không, cách tiếp cận có phù hợp với hệ thống không, các bài kiểm thử có ý nghĩa không, và mã có còn hợp lý sau này không.

### Dùng lập trình theo cặp và lập trình nhóm ở nơi chúng phù hợp

Dùng [lập trình theo cặp](https://en.wikipedia.org/wiki/Pair_programming), nơi hai kỹ sư cùng viết mã tại một máy, cho công việc phức tạp hoặc rủi ro cao, hội nhập và chuyển giao kiến thức. Đó là đánh giá liên tục, và nó thường loại bỏ nhu cầu một bước đánh giá riêng. Dùng [lập trình nhóm](https://en.wikipedia.org/wiki/Mob_programming), nơi cả đội cùng làm một nhiệm vụ tại một thời điểm, cho các quyết định thiết kế then chốt hoặc để lan truyền kiến thức về một khu vực hóc búa trong đội. Hãy coi những điều này là bổ sung cho đánh giá bất đồng bộ, được chọn theo ngữ cảnh, không phải sự thay thế để bắt buộc ở mọi nơi.

### Áp dụng đánh giá tự động và có AI hỗ trợ một cách cẩn trọng

Dùng các công cụ đánh giá tự động và trợ lý AI để bắt các vấn đề phổ biến, gợi ý cải tiến và giảm bớt tải cho người đánh giá, nhưng hãy coi đầu ra của chúng là đầu vào, không phải thẩm quyền. Đánh giá bằng AI giỏi ở các vấn đề bề mặt và tính nhất quán, và kém ở phán đoán thiết kế sâu và ngữ cảnh hệ thống. Hãy giữ một con người chịu trách nhiệm cho mọi phê duyệt, đặc biệt với các thay đổi nhạy cảm về bảo mật và liên quan đến tuân thủ.

### Đặt các chuẩn mực phản hồi mang tính xây dựng

Đặt các chuẩn mực giữ phản hồi cụ thể, tử tế và tập trung vào mã. Khuyến khích người đánh giá đặt câu hỏi thay vì ra lệnh, giải thích lý do đằng sau một yêu cầu, và khen công việc tốt. Đánh dấu rõ ràng các mối quan ngại chặn và các gợi ý tùy chọn (ví dụ bằng cách thêm tiền tố cho các ghi chú không chặn). Những chuẩn mực này quyết định đánh giá làm mạnh thêm đội hay nuôi dưỡng sự bất bình.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Đánh giá PR bất đồng bộ | Linh hoạt; có tài liệu; mở rộng qua các múi giờ | Độ trễ; mất sắc thái; có thể cảm thấy đối đầu |
| Lập trình theo cặp | Đánh giá liên tục; chuyển giao kiến thức nhanh; chất lượng cao | Hai người trên một nhiệm vụ; mệt mỏi; khó lên lịch hơn |
| Lập trình nhóm | Cả đội thống nhất; lan truyền kiến thức sâu | Tốn kém khi gộp lại; không dành cho công việc thường lệ |
| Bắt buộc nhiều người đánh giá | Đảm bảo mạnh; thân thiện với tuân thủ | Chậm hơn; làm loãng trách nhiệm; áp lực hàng đợi |
| Đánh giá có AI hỗ trợ | Nhanh, không biết mệt với các vấn đề phổ biến; giảm tải | Bỏ sót ngữ cảnh hệ thống; tự tin sai nếu tin quá mức |

Căng thẳng cốt lõi là sự kỹ lưỡng so với tốc độ. Đánh giá sâu hơn bắt được nhiều hơn, nhưng làm chậm phân phối và có thể làm tác giả bực bội. Đánh giá nhanh hơn giữ dòng chảy, nhưng có rủi ro hời hợt. Con đường đi qua là cân xứng độ sâu đánh giá với rủi ro của thay đổi, để thay đổi tầm thường nhận được đánh giá nhẹ và thay đổi rủi ro nhận được đánh giá sâu, và tự động hóa công việc cơ học để công sức của con người tập trung vào nơi nó quan trọng.

## Câu hỏi để thảo luận với đội của bạn

1. **Điều gì được coi là quá lớn cho một pull request, và bạn có tách các lần tái cấu trúc cơ học khỏi các thay đổi hành vi không?** Chương này nêu thẳng rằng các PR lớn nhận được đánh giá hời hợt và rằng tác giả sở hữu khả năng đánh giá được, và nó yêu cầu bạn tách tái cấu trúc khỏi thay đổi hành vi để mỗi cái dễ suy luận. Trong một đội lớn, một PR khổng lồ đảm bảo một con dấu đóng cho có, mang lại sự đảm bảo sai trong khi để lỗi thực sự lọt qua. Hãy mang bằng chứng: phân phối kích thước PR của bạn và độ sâu đánh giá giảm thế nào khi diff lớn lên. Hãy thống nhất một chuẩn mực kích thước thực tế và thói quen đưa các lần tái cấu trúc thuần túy vào riêng khỏi thay đổi logic, để người đánh giá thực sự có thể giữ từng thay đổi trong đầu. Kỷ luật đơn lẻ đó nâng chất lượng của mọi lần đánh giá sau đó.

2. **Làm thế nào bạn phân biệt một phản đối chặn với một gợi ý tùy chọn, và quy ước đó có thực sự được dùng không?** Chương này yêu cầu bạn tách các vấn đề chặn khỏi các sở thích và nói rõ cái nào là cái nào, và nó đánh dấu việc chặn vì sở thích là một phản mẫu ăn mòn. Không có một quy ước chung, ý kiến về phong cách của người đánh giá đọc như một thay đổi bắt buộc, nuôi dưỡng sự bất bình và làm chậm phân phối trong cả đội. Hãy mang các ví dụ từ những lần đánh giá gần đây khi một sở thích làm đình trệ việc hợp nhất làm tín hiệu cụ thể. Hãy áp dụng một dấu hiệu nhẹ, ví dụ một tiền tố gắn nhãn các ghi chú không chặn, để tác giả biết ngay điều gì phải thay đổi so với điều gì là gợi ý. Điều đó giữ cho đánh giá tập trung vào tính đúng đắn và thiết kế thay vì khẩu vị.

3. **Ai phải phê duyệt các thay đổi đối với mã nhạy cảm về bảo mật hoặc liên quan đến tuân thủ, và việc định tuyến đó được thực thi thế nào?** Chương này mô tả phê duyệt theo vai trò, quy tắc sở hữu mã và phân tách nhiệm vụ nơi không một người nào kiểm soát toàn bộ một thay đổi nhạy cảm, với phê duyệt được ghi lại làm bằng chứng kiểm toán. Trong bối cảnh doanh nghiệp và chính phủ, đây là các biện pháp kiểm soát bắt buộc, và rủi ro là chúng hoặc bị bỏ qua hoặc biến thành nút thắt làm đóng băng phân phối. Hãy mang tín hiệu: mô-đun nào nhạy cảm, và các quy tắc sở hữu hiện tại có tự động định tuyến những thay đổi đó đến đúng người phê duyệt không. Hãy mã hóa việc định tuyến trong cấu hình sở hữu mã và ghép nó với các kiểm tra tự động và thay đổi nhỏ, để biện pháp kiểm soát được thỏa mãn mà không có hàng đợi canh cổng của con người. Hãy quyết định điều này một cách có chủ đích thay vì khám phá khoảng trống trong một cuộc kiểm toán.

4. **Mục tiêu độ trễ đánh giá nào bạn thực sự đã thống nhất, và bạn có đo và thực thi nó, hay nó chỉ là khát vọng?** Chương này coi độ trễ đánh giá là chi phí của cả đội và yêu cầu bạn giám sát thời gian đến lần đánh giá đầu tiên và thời gian đến khi hợp nhất, coi sự chậm trễ kéo dài là vấn đề quy trình thay vì lỗi cá nhân. Trong một đội lớn, hàng đợi đánh giá không có chủ sở hữu âm thầm đánh thuế mọi người: tác giả gom các thay đổi lớn hơn để tránh chờ đợi, những thay đổi đó rồi nhận được đánh giá hời hợt hơn, và thời gian dẫn phân phối trôi lên mà không có thủ phạm duy nhất. Cân nhắc đối lập là một mục tiêu độ trễ cứng có thể đẩy người đánh giá đọc lướt, nên tốc độ và độ sâu phải được cân bằng chứ không đánh đổi một cách mù quáng. Hãy mang bằng chứng: phân phối thời gian đến lần đánh giá đầu tiên hiện tại, nó thay đổi thế nào theo đội và theo kích thước thay đổi, và nơi các lần đánh giá nằm lâu nhất. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn mục tiêu với các chỉ số dòng chảy mà ban lãnh đạo đã theo dõi, vì một biện pháp kiểm soát bắt buộc nhiều người đánh giá không có chuẩn mực độ trễ trở thành nút thắt làm đóng băng phân phối và cám dỗ mọi người đi vòng hoàn toàn qua biện pháp kiểm soát.

5. **Với những loại thay đổi nào bạn tin vào đánh giá tự động và có AI hỗ trợ, và ở đâu một con người phải vẫn chịu trách nhiệm?** Chương này nói hãy coi đầu ra đánh giá của AI là đầu vào, không phải thẩm quyền: mạnh về các vấn đề bề mặt và tính nhất quán, yếu về phán đoán thiết kế sâu và ngữ cảnh hệ thống, với một con người chịu trách nhiệm cho mọi phê duyệt. Không có ranh giới tường minh, một đội lớn trôi vào sự tin quá mức, nơi một bình luận xanh của bot đọc như một lần đánh giá đã qua và các rủi ro thiết kế và bảo mật thực sự trượt qua dưới sự tự tin sai. Lực kéo đối lập là đánh giá bằng AI thực sự giảm tải và bắt các lỗi phổ biến không biết mệt, nên cấm nó lãng phí đòn bẩy. Hãy mang bằng chứng: nơi các gợi ý tự động đã bắt được vấn đề thực, nơi chúng tạo ra nhiễu, và loại thay đổi nào (nhạy cảm về bảo mật, liên quan đến tuân thủ, kiến trúc) mà bạn sẽ không bao giờ để máy móc tự ký duyệt. Với công việc doanh nghiệp và chính phủ, hãy nêu tên ai nắm trách nhiệm cho một phê duyệt khi có trợ lý AI trong vòng, vì một cuộc kiểm toán sẽ hỏi ai đã đánh giá một thay đổi, và "công cụ đã làm" không phải là câu trả lời mà cơ quan quản lý chấp nhận.

6. **Lập trình theo cặp hay lập trình nhóm nên thay thế đánh giá bất đồng bộ ở đâu, và làm thế nào bạn dùng đánh giá để giảm rủi ro hệ số xe buýt một cách có chủ đích?** Chương này đóng khung lập trình theo cặp và nhóm là đánh giá liên tục được chọn theo ngữ cảnh, và nó gọi đánh giá là cơ chế lan truyền kiến thức để không phần nào của hệ thống chỉ do một người hiểu. Nếu để ngầm, kiến thức tập trung: cùng một chuyên gia đánh giá mọi thay đổi trên một hệ thống con, đánh giá biến thành con dấu đóng cho có vì không ai khác có thể thách thức họ, và rủi ro hệ số xe buýt tăng chính xác ở nơi hệ thống quan trọng nhất. Cân nhắc đối lập là chi phí, vì lập trình nhóm tốn thời gian của cả đội và lập trình theo cặp ràng buộc hai kỹ sư, nên bạn không thể bắt buộc nó ở mọi nơi. Hãy mang bằng chứng: mô-đun nào chỉ có một người đánh giá đáng tin, nơi hội nhập bị đình trệ, và nơi một khu vực hóc búa sẽ được hưởng lợi từ một buổi làm việc trực tiếp thay vì các chuỗi bình luận. Trong một tổ chức lớn hoặc công, hãy coi việc lan truyền kiến thức có chủ đích là quản lý rủi ro, vì một hệ thống tồn tại lâu mà các phần quan trọng phụ thuộc vào một người là một khoản nợ về vận hành và liên tục, không chỉ là sự bất tiện về nhân sự.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với ba hoặc bốn kỹ sư, hãy giữ đánh giá nhẹ: phê duyệt của một đồng đội trên một pull request nhỏ, kiểm tra cơ học trong CI, và không bắt buộc người đánh giá thứ hai làm đình trệ việc hợp nhất. Mục tiêu thực sự ít là về tuân thủ hơn là bảo đảm có nhiều hơn một người hiểu từng phần của hệ thống, vì vậy hãy lập trình theo cặp trên các phần rủi ro và coi đó là hội nhập. Đừng xây định tuyến sở hữu mã nặng nề mà bạn sẽ sớm vượt qua; một chuẩn mực chung về các thay đổi nhỏ, được mô tả tốt mang lại phần lớn lợi ích với chi phí gần như bằng không.

**Doanh nghiệp nhỏ.** Bạn khó có chuyên gia công cụ đánh giá, vì vậy hãy dựa vào những gì nền tảng lưu trữ của bạn (ví dụ một dịch vụ Git được quản lý) cung cấp sẵn thay vì xây dựng tự động hóa riêng. Hãy mua các tích hợp linter, kiểm thử và quét bảo mật thay vì bảo trì chúng, để vài kỹ sư của bạn dành những phút đánh giá khan hiếm cho thiết kế và tính đúng đắn. Giữ một quy tắc đơn giản, mọi thay đổi có một cặp mắt khác nhìn vào, và cưỡng lại việc thêm quy trình mà bạn không có ai bảo trì.

**Doanh nghiệp lớn.** Thách thức là nhất quán qua nhiều đội: tiêu chuẩn chung, quy tắc sở hữu mã định tuyến các thay đổi nhạy cảm đến đúng người phê duyệt, và phê duyệt theo vai trò được ghi lại làm bằng chứng kiểm toán. Hãy tự động hóa các kiểm tra cơ học trên toàn tổ chức để đánh giá của con người tập trung vào thiết kế, và theo dõi độ trễ đánh giá như một chỉ số dòng chảy để các biện pháp kiểm soát bắt buộc nhiều người đánh giá không âm thầm trở thành nút thắt. Hãy cân xứng độ sâu đánh giá với rủi ro thay đổi bằng một chính sách có tài liệu, để thay đổi tầm thường vẫn nhanh trong khi thay đổi rủi ro cao nhận được phân tách nhiệm vụ và sự soi xét sâu hơn.

**Chính phủ.** Kiểm soát thay đổi thường là bắt buộc: mọi thay đổi trên môi trường thực được đánh giá và phê duyệt bởi người khác ngoài tác giả, với bản ghi được giữ làm bằng chứng kiểm toán để thỏa mãn yêu cầu phân tách nhiệm vụ. Hãy ưu tiên một dấu vết minh bạch, truy vết được về ai là tác giả, ai phê duyệt và các kiểm tra nào đã vượt qua, và đầu tư vào tự động hóa và các thay đổi nhỏ, thường xuyên để biện pháp kiểm soát không làm đóng băng phân phối. Ở nơi công cụ đánh giá được mua sắm, hãy đòi nhật ký kiểm toán có thể xuất và tránh bị khóa chặt, vì bằng chứng phải tồn tại lâu hơn bất kỳ nhà cung cấp đơn lẻ nào và chịu được sự soi xét của công chúng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn kỹ sư giữ mọi pull request nhỏ và yêu cầu phê duyệt của một đồng đội trước khi hợp nhất, ít vì tuân thủ hơn là để bảo đảm không một người nào là người duy nhất hiểu một phần của hệ thống. CI chạy công cụ định dạng và kiểm thử, nên con người dành vài phút đánh giá ít ỏi cho thiết kế và tính đúng đắn thay vì khoảng trắng. Khi đội gặp một phần hóc búa của luồng thanh toán, hai người trong số họ lập trình theo cặp trên đó thay vì trao đổi bình luận bất đồng bộ, cũng đồng thời là hội nhập cho nhân viên mới nhất.

**Doanh nghiệp lớn.** Một công ty phần mềm lớn yêu cầu ít nhất một đánh giá phê duyệt trên mọi thay đổi, cộng với phê duyệt thứ hai cho các thay đổi đối với các mô-đun nhạy cảm về bảo mật được xác định bởi quy tắc sở hữu mã. CI xử lý mọi kiểm tra phong cách và kiểm thử, nên người đánh giá tập trung vào thiết kế và tính đúng đắn. Đội theo dõi thời gian đến lần đánh giá đầu tiên và coi trung vị tăng là tín hiệu để cân bằng lại khối lượng công việc. Kỹ sư mới được hội nhập qua lập trình theo cặp, rút ngắn con đường để họ đóng góp độc lập.

**Chính phủ.** Một cơ quan quốc gia hoạt động dưới các yêu cầu kiểm soát thay đổi nghiêm ngặt bắt buộc mọi thay đổi trên môi trường thực phải được đánh giá và phê duyệt bởi người khác ngoài tác giả, với phê duyệt được ghi lại để kiểm toán. Để biện pháp kiểm soát này không trở thành nút thắt, cơ quan đầu tư vào các kiểm tra tự động và thay đổi nhỏ, thường xuyên, và đặt chuẩn mực phản hồi đánh giá trong ngày. Dấu vết đánh giá, bao gồm ai là tác giả, ai phê duyệt và các kiểm tra nào đã vượt qua, trở thành một phần của bằng chứng tuân thủ cho mỗi bản phát hành, thỏa mãn yêu cầu phân tách nhiệm vụ mà không làm đóng băng phân phối.

## Luận chứng kinh doanh: động lực, ROI và TCO

Đánh giá mã hoàn vốn cho bạn bằng ba loại tiền tệ: lỗi được bắt trước môi trường thực, kiến thức lan truyền trong đội, và các tiêu chuẩn được duy trì tự động theo thời gian. Bắt một lỗi trong đánh giá rẻ hơn rất nhiều so với bắt nó trên môi trường thực, và lợi ích chia sẻ kiến thức giảm rủi ro phụ thuộc vào cá nhân then chốt vốn có thể gây tổn thất lớn cho tổ chức khi có người ra đi. Đánh giá cũng là cơ chế truyền tải văn hóa giữ cho một đội đang lớn mạch lạc.

Chi phí của đánh giá là thời gian kỹ sư và một chút độ trễ, cả hai đều quản lý được bằng thực hành tốt. Chi phí của việc *không* đánh giá, hoặc đánh giá tệ, bao gồm lỗi môi trường thực, kiến thức bị cô lập, mã không nhất quán, và trong bối cảnh chịu quy định, các cuộc kiểm toán thất bại và phát hiện tuân thủ. Đánh giá quá nặng cũng có chi phí thực của riêng nó: hàng đợi dài, các lô quá lớn, kỹ sư nản lòng. Để thuyết phục ban lãnh đạo, hãy kết nối các thực hành đánh giá với tỷ lệ thay đổi thất bại, thời gian dẫn phân phối và tốc độ hội nhập, và theo dõi độ trễ đánh giá như một chỉ số dòng chảy tường minh.

## Phản mẫu và cạm bẫy

- **Con dấu đóng cho có:** phê duyệt không có sự xem xét thực sự, mang lại sự đảm bảo sai và chỉ thỏa mãn câu chữ của một biện pháp kiểm soát.
- **PR khổng lồ:** hàng nghìn dòng chỉ có thể đọc lướt, đảm bảo đánh giá hời hợt.
- **Đánh giá chỉ bắt bẻ:** tập trung vào chuyện vặt trong khi bỏ sót thiết kế và tính đúng đắn, thường vì các kiểm tra cơ học chưa được tự động hóa.
- **Đánh giá như canh cổng:** dùng đánh giá để khẳng định sự thống trị hoặc chặn người khác, đầu độc sự cộng tác.
- **Hàng đợi chậm:** các lần đánh giá nằm nhiều ngày, làm đình trệ phân phối và khuyến khích gom lô.
- **Tin quá mức vào đánh giá bằng AI:** coi các gợi ý tự động là thẩm quyền và bỏ phán đoán của con người trên các thay đổi rủi ro.
- **Chặn vì sở thích:** trình bày ý kiến phong cách cá nhân như các thay đổi bắt buộc mà không phân biệt chúng với lỗi thực sự.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Đánh giá tùy nghi và phản ứng. Nó thường bị bỏ qua hoặc làm không nhất quán, các vấn đề cơ học chi phối bình luận, chuẩn mực phản hồi chưa được đặt ra, và mọi dấu vết phê duyệt là ngẫu nhiên thay vì có chủ đích.
- **Mức 2, Phát triển:** Các thực hành đánh giá cơ bản tồn tại nhưng khác nhau giữa các đội. Đánh giá được yêu cầu ở một số nơi và chậm hoặc tùy chọn ở những nơi khác, tự động hóa chỉ một phần, và kích thước cùng chất lượng pull request dao động rộng mà không có kỳ vọng chung.
- **Mức 3, Chuẩn hóa:** Tiêu chuẩn được lập thành tài liệu và thực thi toàn tổ chức. Các PR nhỏ tập trung, định dạng, linter, kiểm thử và quét bảo mật tự động trong CI, danh sách kiểm tra rõ ràng, một quy ước tường minh giữa chặn và gợi ý, và quy tắc sở hữu mã định tuyến các thay đổi nhạy cảm đến đúng người phê duyệt.
- **Mức 4, Quản lý:** Đánh giá được đo và kiểm soát theo các đường cơ sở. Thời gian đến lần đánh giá đầu tiên, thời gian đến khi hợp nhất, độ sâu đánh giá so với rủi ro thay đổi, tỷ lệ lỗi thoát ra và tỷ lệ thay đổi thất bại được theo dõi; độ trễ kéo dài được coi là vấn đề quy trình; và dữ liệu thúc đẩy nơi cần cân bằng lại tải người đánh giá và nơi các biện pháp kiểm soát đang làm chậm phân phối mà không thêm sự đảm bảo.
- **Mức 5, Điều phối:** Đánh giá được cải tiến liên tục và tích hợp trong toàn tổ chức. Độ sâu thích ứng với rủi ro thay đổi, lập trình theo cặp, lập trình nhóm và hỗ trợ của AI được dùng có chủ đích với một con người chịu trách nhiệm, việc lan truyền kiến thức và rủi ro hệ số xe buýt được quản lý có chủ ý, và đánh giá cải thiện chất lượng, dòng chảy phân phối và hội nhập một cách đo được.

## Ý tưởng để thảo luận

- Mục tiêu độ trễ đánh giá phù hợp cho đội của bạn là gì, và điều gì ngăn bạn đạt được nó?
- Làm thế nào bạn cân xứng độ sâu đánh giá với rủi ro thay đổi mà không thêm quan liêu?
- Lập trình theo cặp hay lập trình nhóm vượt trội hơn đánh giá bất đồng bộ ở đâu trong bối cảnh của bạn?
- Nên tin đánh giá có AI hỗ trợ đến mức nào, và cho loại thay đổi nào?
- Làm thế nào bạn giữ phản hồi đánh giá mang tính xây dựng khi đội lớn lên và đa dạng hơn?
- Làm thế nào bạn thỏa mãn các yêu cầu phê duyệt tuân thủ mà không tạo ra nút thắt?

## Những điểm cần ghi nhớ

- Giữ pull request nhỏ và được mô tả tốt; tác giả sở hữu khả năng đánh giá được.
- Tự động hóa phần cơ học để con người đánh giá thiết kế, tính đúng đắn và kiểm thử.
- Theo dõi và quản lý độ trễ đánh giá như một chi phí dòng chảy của cả đội.
- Cân xứng độ sâu đánh giá với rủi ro thay đổi, và phân biệt các vấn đề chặn với sở thích.
- Dùng lập trình theo cặp, lập trình nhóm và hỗ trợ của AI như những bổ sung phù hợp ngữ cảnh, giữ một con người chịu trách nhiệm.

## Tài liệu tham khảo và đọc thêm

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (như một ví dụ tham chiếu)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (về lập trình theo cặp)
- Woody Zuill, các bài viết về lập trình nhóm
- Michael Lopp, *Managing Humans* (về cộng tác kỹ thuật)
