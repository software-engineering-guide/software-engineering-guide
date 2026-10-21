# 1.5 Ra quyết định và quản trị

## Tổng quan và động lực

Mọi hệ thống phần mềm là tổng của hàng nghìn quyết định: dùng [cơ sở dữ liệu](https://en.wikipedia.org/wiki/Database) nào, kiến trúc nào, thư viện nào, nên tự xây hay mua, khi nào gánh nợ và khi nào trả nợ. Quản trị là cách bạn đưa ra các quyết định này một cách tốt và nhất quán, đưa đúng người vào cuộc mà không tạo ra nút thắt, và lưu giữ lý do để các đội sau không bị buộc phải học lại từ đầu. Trong một đội nhỏ, các quyết định diễn ra trong trò chuyện và sống trong trí nhớ chung. Ở quy mô lớn, trí nhớ đó bốc hơi. Con người ra đi, các đội tái tổ chức, và "vì sao" đằng sau một lựa chọn then chốt bị mất, để lại những người kế nhiệm hoặc sao chép mù quáng hoặc gỡ bỏ nó một cách mù quáng. Quản trị tốt là bộ máy làm cho các quyết định hiện rõ, có chủ đích và bền vững trong một tổ chức lớn và luôn thay đổi.

Thách thức trung tâm của các đội lớn là cân bằng giữa tự chủ và thống nhất. Đẩy mọi quyết định lên một hội đồng trung tâm, bạn có sự nhất quán, nhưng phải trả giá bằng những nút thắt làm tê liệt và các đội bị tước quyền. Đẩy mọi quyết định xuống dưới, bạn có tốc độ, nhưng phải trả giá bằng hỗn loạn: công nghệ không tương thích, công sức trùng lặp và những sai lầm lặp lại. Câu trả lời trưởng thành không phải là tập trung hóa cũng không phải vô chính phủ. Đó là một mô hình phân tầng. Các đội quyết định hầu hết mọi thứ tại chỗ trong một "con đường trải sẵn" được đánh dấu rõ, trong khi một quy trình nhẹ nhàng, minh bạch chi phối những lựa chọn thực sự xuyên suốt và khó đảo ngược. Mục tiêu là biến các quyết định tốt thành mặc định dễ dàng, và chỉ dành sự chú ý quản trị khan hiếm ở nơi nó thực sự quan trọng.

Doanh nghiệp và chính phủ mang những rủi ro cao hơn. Họ phải thỏa mãn kiểm toán viên, cơ quan quản lý và cơ quan giám sát, những bên đòi hỏi các quyết định có tài liệu, có thể bảo vệ được. Họ làm việc trên những chân trời thời gian dài, nơi một lựa chọn kiến trúc kém hoặc một đống [nợ kỹ thuật](https://en.wikipedia.org/wiki/Technical_debt) không được quản lý có thể đè nặng lên họ cả thập kỷ. Và các nghĩa vụ mua sắm và tuân thủ khiến các quyết định tự xây hay mua đặc biệt hệ trọng và khó đảo ngược. Với các tổ chức này, việc ra quyết định có kỷ luật và được ghi chép tốt không phải là quan liêu vì chính nó. Đó là quản lý rủi ro, trí nhớ tổ chức và nền tảng của trách nhiệm giải trình.

## Các nguyên tắc chính

- Ghi lại các quyết định và lý do của chúng; một quyết định không có lý do là một khoản nợ.
- Đẩy quyết định xuống mức thấp nhất có đủ ngữ cảnh, trong những lan can rõ ràng.
- Cân xứng độ nặng của quy trình với độ nặng và khả năng đảo ngược của quyết định.
- Phân biệt các quyết định có thể đảo ngược ("cửa hai chiều") với không thể đảo ngược ("cửa một chiều") và quản trị chúng khác nhau.
- Ưu tiên các con đường trải sẵn và mặc định hơn việc phê duyệt từng trường hợp.
- Coi nợ kỹ thuật là một danh mục được quản lý, không phải lỗi đạo đức cần che giấu.
- Làm cho quản trị minh bạch; ra quyết định kín đáo nuôi dưỡng sự mất tin cậy và làm lại.

## Khuyến nghị

### Áp dụng Hồ sơ quyết định kiến trúc và quy trình RFC vừa tầm

[Hồ sơ quyết định kiến trúc](https://en.wikipedia.org/wiki/Architectural_decision) (Architecture Decision Record, ADR) là một tài liệu ngắn, bất biến, ghi lại một quyết định quan trọng: bối cảnh, các phương án đã cân nhắc, lựa chọn được đưa ra và các hệ quả. Hãy lưu ADR trong hệ thống quản lý phiên bản cùng với mã nguồn, để lý do đi cùng hệ thống. Với các quyết định cần góp ý trước khi đưa ra, hãy dùng quy trình [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (yêu cầu góp ý) nhẹ nhàng: phát một đề xuất, mời góp ý trong một khoảng thời gian giới hạn, rồi quyết định và ghi lại. Giữ cả hai ở mức nhẹ. Giá trị nằm ở tư duy và bản ghi bền vững, không phải ở các mẫu biểu cầu kỳ. Cùng nhau, ADR và RFC biến lý do ngầm, bị lãng quên thành một trí nhớ tổ chức có thể tìm kiếm.

### Quản trị qua con đường trải sẵn, không qua người gác cổng

Thay vì xem xét từng quyết định một, hãy đầu tư vào một "con đường trải sẵn": một tập hợp các mặc định được chuẩn y, được hỗ trợ tốt, gồm ngôn ngữ, khung phát triển, đường ống triển khai và mẫu thiết kế được phê duyệt, mà các đội có thể áp dụng với ít ma sát và nhiều hỗ trợ. Các đội ở trên con đường trải sẵn cần rất ít quản trị, vì lựa chọn an toàn, tuân thủ cũng là lựa chọn dễ dàng. Các đội có lý do chính đáng để rời khỏi nó thì có thể, nhưng họ nhận thêm trách nhiệm và một cuộc xem xét nhẹ. Mô hình "con đường vàng" này mở rộng tốt hơn nhiều so với một hội đồng trung tâm phê duyệt mọi thứ, vì nó chuyển quản trị từ việc canh cổng từng trường hợp sang các mặc định được thiết kế tốt.

### Dùng hội đồng rà soát kiến trúc một cách tiết chế và minh bạch

Một hội đồng rà soát kiến trúc, hoặc tương đương, có vai trò chính đáng đối với những quyết định lớn nhất, xuyên suốt nhất hoặc khó đảo ngược nhất, và để đặt ra các tiêu chuẩn xác định con đường trải sẵn. Giữ phạm vi của nó hẹp, tiêu chí được công bố, và quy trình nhanh và mang tính tư vấn, không phải nút thắt bắt buộc cho công việc thường ngày. Nhiệm vụ của hội đồng là gìn giữ sự mạch lạc và chia sẻ kiến thức, không phải phê duyệt mọi lựa chọn. Khi một hội đồng trở thành hàng đợi mà mọi dự án phải chờ, nó đã thất bại. Hãy ủy quyền mạnh tay, và chỉ dành việc rà soát trung tâm cho vài quyết định thực sự xứng đáng.

### Biến lựa chọn xây-hay-mua-hay-áp-dụng thành một phân tích có chủ đích

Với bất kỳ năng lực quan trọng nào, hãy cân nhắc ba con đường: tự xây nội bộ, mua một sản phẩm thương mại, hoặc áp dụng một giải pháp [mã nguồn mở](https://en.wikipedia.org/wiki/Open-source_software). Hãy xây khi năng lực đó là yếu tố tạo khác biệt thực sự và cốt lõi với sứ mệnh của bạn. Hãy mua hoặc áp dụng những năng lực không tạo khác biệt mà người khác làm tốt hơn. Hãy tính [tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), không chỉ giá ban đầu. Mua kéo theo chi phí giấy phép, tích hợp và [bị khóa chặt](https://en.wikipedia.org/wiki/Vendor_lock-in). Xây kéo theo chi phí bảo trì và nhân sự vĩnh viễn. Áp dụng mã nguồn mở kéo theo nghĩa vụ hỗ trợ và theo dõi bảo mật. Hãy ghi lại quyết định và các giả định của nó dưới dạng ADR, để bạn có thể xem xét lại khi hoàn cảnh thay đổi.

### Quản lý nợ kỹ thuật như một danh mục

Nợ kỹ thuật không xấu về bản chất. Đôi khi gánh nó để phát hành sớm hơn là lựa chọn đúng. Điều xấu là món nợ không được quản lý, vô hình, bị lãng quên. Hãy giữ một bản kiểm kê tường minh về nợ đáng kể. Với mỗi khoản, ghi lại chi phí nó áp đặt ("lãi" liên tục) và chi phí để sửa. Sau đó quản lý nó như một danh mục tài chính. Trả các khoản nợ lãi cao làm chậm đội mỗi ngày. Chấp nhận các khoản nợ lãi thấp ở những góc ổn định. Đưa ra quyết định về nợ một cách có ý thức thay vì ngẫu nhiên. Dành ra một phần năng lực cố định để trả nợ, để nó không bao giờ cộng dồn thành khủng hoảng.

### Phân biệt quyết định có thể đảo ngược và không thể đảo ngược

Không phải mọi quyết định đều xứng đáng được cân nhắc như nhau. Các quyết định "cửa hai chiều" có thể đảo ngược dễ dàng, nên hãy đưa ra chúng nhanh và tại chỗ, bởi đội, với thiên hướng hành động. Trăn trở về chúng làm lãng phí thời gian và làm chậm việc học. Các quyết định "cửa một chiều" không thể đảo ngược hoặc đảo ngược tốn kém, như một hợp đồng [API](https://en.wikipedia.org/wiki/API) công khai, một mô hình dữ liệu ở quy mô lớn, một cam kết nhà cung cấp nhiều năm, xứng đáng được cân nhắc chậm rãi, cẩn trọng, bởi người cấp cao, cùng một lý do được ghi lại. Phân loại quyết định theo cách này là một trong những thói quen quản trị có đòn bẩy cao nhất bạn có. Nó hướng sự xem xét khan hiếm đến nơi nó sinh lợi, và giải phóng mọi thứ còn lại.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận quản trị | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| Hội đồng rà soát trung tâm cho tất cả | Nhất quán và giám sát tối đa | Nút thắt nghiêm trọng; tước quyền các đội; chậm |
| Con đường trải sẵn với tự chủ tại chỗ | Mở rộng được, nhanh, mặc định an toàn, trao quyền cho các đội | Đòi hỏi đầu tư nền tảng ban đầu; một số đội lệch khỏi đường |
| Hoàn toàn tự chủ, không quản trị | Nhanh, quyền sở hữu cao | Phân mảnh, trùng lặp, sai lầm lặp lại |
| ADR / RFC | Trí nhớ bền vững, quyết định tốt hơn, minh bạch | Chi phí viết; bị bỏ qua nếu không được duy trì |

| Lựa chọn nguồn cung | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| Xây | Kiểm soát đầy đủ, vừa vặn chính xác, có thể tạo khác biệt | Chi phí bảo trì và nhân sự vĩnh viễn |
| Mua | Nhanh, được hỗ trợ, người khác bảo trì | Chi phí giấy phép, bị khóa chặt, không vừa vặn hoàn hảo |
| Áp dụng (mã nguồn mở) | Không phí giấy phép, kiểm tra được, có cộng đồng | Gánh nặng hỗ trợ và bảo mật rơi vào bạn |

Sự đánh đổi thống nhất là kiểm soát so với tốc độ, và nhất quán trung tâm so với tự chủ tại chỗ. Mọi lựa chọn quản trị nằm trên phổ này. Tư thế được khuyến nghị, con đường trải sẵn cộng với ủy quyền dựa trên khả năng đảo ngược, cố ý mua được phần lớn tốc độ của sự tự chủ đồng thời giữ lại sự nhất quán quan trọng. Nó làm điều đó bằng cách biến lựa chọn thống nhất thành lựa chọn dễ dàng, và dành quy trình nặng nề cho những quyết định không thể đảo ngược hiếm hoi.

## Câu hỏi để thảo luận với đội của bạn

1. **Ai quyết định một quyết định có phải là cửa một chiều hay không, và bạn sẽ bắt các phân loại sai theo cả hai hướng như thế nào?** Phân loại quyết định theo khả năng đảo ngược là một trong những thói quen quản trị có đòn bẩy cao nhất, và giá trị của nó sụp đổ nếu bạn gắn nhãn sai: coi một lựa chọn có thể đảo ngược là không thể đảo ngược thì bạn dìm nó trong cân nhắc, coi một lựa chọn không thể đảo ngược là có thể đảo ngược thì bạn phát hành một mô hình dữ liệu hay hợp đồng API công khai mà bạn không thể hoàn tác với giá rẻ. Rủi ro đối lập là người gần công việc nhất có thể thiên về tốc độ, trong khi một hội đồng trung tâm có thể thiên về thận trọng. Hãy mang ví dụ cụ thể vào cuộc thảo luận: việc đảo ngược mỗi quyết định thực sự tốn bao nhiêu, về thời gian và tiền bạc, và ai gánh chi phí đó. Trong bối cảnh doanh nghiệp và chính phủ, các cam kết mua sắm và dữ liệu ở quy mô lớn biến nhiều lựa chọn thành cửa một chiều dù ban đầu trông có thể đảo ngược. Hãy thống nhất ai phân loại, và xây thói quen nhờ một ý kiến thứ hai nhanh đối với bất cứ điều gì gần ranh giới, để sự xem xét khan hiếm rơi vào nơi việc đảo ngược thực sự tốn kém.

2. **Ai sở hữu, tài trợ và bố trí nhân sự cho con đường trải sẵn, và điều gì ngăn nó thoái hóa thành người gác cổng?** Một con đường trải sẵn chỉ hoạt động nếu các mặc định được chuẩn y thực sự được hỗ trợ tốt và dễ hơn các lựa chọn thay thế, và điều đó đòi hỏi sự đầu tư bền bỉ mà dễ bị tài trợ thiếu. Sự đánh đổi rất rõ rệt: một con đường trải sẵn thiếu nguồn lực trở thành một loạt mệnh lệnh không có hỗ trợ, chính là việc canh cổng mà mô hình này được lập ra để thay thế, và các đội khi đó sẽ đi vòng qua nó. Hãy mang bằng chứng về sức khỏe của con đường: tỷ lệ chấp nhận, các công cụ được phê duyệt cập nhật đến mức nào, đội nền tảng phản hồi nhanh ra sao, và các đội thường xuyên đăng ký đi ra ngoài đường đến mức nào. Với các tổ chức lớn và chịu quy định, con đường trải sẵn cũng là cách để lựa chọn tuân thủ trở thành lựa chọn dễ dàng, nên việc tài trợ cho nó là một khoản đầu tư tuân thủ, không chỉ là sự tiện lợi. Hãy quyết định một chủ sở hữu rõ ràng và một ngân sách thường trực, và đo xem các đội có chọn con đường đó vì nó thực sự là con đường dễ nhất hay không.

3. **Các đội đang đi vòng qua quản trị của bạn ở đâu, và "CNTT bóng tối" đó đang nói với bạn điều gì?** Các đội né con đường được cho phép khi nó đau đớn hơn cách lách, vì vậy CNTT bóng tối lan rộng ít phải là vấn đề kỷ luật mà là một phán quyết về thiết kế đối với quản trị của bạn. Những cân nhắc đối lập là có thật: một số hành vi né tránh là liều lĩnh, và nhiều trường hợp là sự né tránh hợp lý một hội đồng rà soát đã trở thành hàng đợi nhiều tuần. Hãy mang bằng chứng: những phê duyệt nào bị bỏ qua, những công cụ không chính thức nào đã âm thầm lan rộng, và con đường chính thức thực sự mất bao lâu. Trong bối cảnh doanh nghiệp và chính phủ, rủi ro cao hơn, vì các công cụ không được cho phép có thể vi phạm các nghĩa vụ kiểm toán, bảo mật và mua sắm mang sức nặng pháp lý. Nếu mô hình cho thấy con người đang đi vòng qua một nút thắt, cách khắc phục là tăng tốc và mở rộng con đường trải sẵn và thu hẹp phạm vi của hội đồng vào vài quyết định xuyên suốt, không thể đảo ngược, chứ không phải thêm nhiều phê duyệt.

4. **Bao nhiêu năng lực phân phối của chúng ta thực sự dành cho việc trả nợ kỹ thuật, và chúng ta có thể gọi tên những hạng mục lãi cao nhất cần nhắm tới trước không?** Nợ kỹ thuật hành xử như lãi kép, một khoản thuế âm thầm lên mọi thay đổi trong tương lai, và một tổ chức lớn có thể mang nó nhiều năm trước khi có ai nhận ra hệ thống đã trở nên chậm và giòn khi sửa đổi. Áp lực đối lập thẳng thừng: mỗi giờ dành cho nợ là một giờ không dành cho các tính năng mà ban lãnh đạo nhìn thấy, vì vậy việc trả nợ là thứ đầu tiên bị cắt khi hạn chót thắt lại. Hãy mang bằng chứng thực vào cuộc thảo luận, một bản kiểm kê bằng văn bản về nợ đáng kể, một ước tính trung thực về chi phí liên tục mỗi hạng mục áp đặt và chi phí để sửa, và tỷ lệ năng lực thực tế gần đây đã dành cho trả nợ so với công việc mới. Với các doanh nghiệp và cơ quan chính phủ có chân trời thập kỷ, nợ không được quản lý cuối cùng buộc phải viết lại tốn kém hoặc nhận một phát hiện kiểm toán, vì vậy hãy coi phân bổ trả nợ thường trực là quản lý rủi ro và quyết định ai bảo vệ nó khi tiến độ trượt.

5. **Khi chúng ta cần lý do đằng sau một quyết định được đưa ra hai năm trước, chúng ta có thực sự tìm thấy nó không, và có ai đang giữ cho bản ghi đó sống không?** Toàn bộ giá trị của Hồ sơ quyết định kiến trúc là lý do tồn tại lâu hơn những người đã đưa ra nó, và giá trị đó sụp đổ nếu ADR được viết một lần, không bao giờ được tìm kiếm, và âm thầm lỗi thời. Căng thẳng nằm giữa kỷ luật viết cần thiết để nắm bắt bối cảnh, phương án và hệ quả vào thời điểm quyết định, và áp lực hằng ngày là cứ phát hành rồi đi tiếp. Hãy mang các phép thử cụ thể vào cuộc thảo luận: chọn ba quyết định quan trọng gần đây và xem có ai tìm được lý do đã ghi chỉ trong vài phút không, và kiểm tra xem các ADR bị thay thế có được đánh dấu như vậy hay âm thầm mâu thuẫn với thực hành hiện tại. Trong bối cảnh doanh nghiệp và chính phủ, bản ghi có thể tìm kiếm đó chính là bằng chứng có thể bảo vệ mà kiểm toán viên và cơ quan giám sát đòi hỏi, vì vậy hãy quyết định ADR nằm ở đâu, ai rà soát chúng, và điều gì khiến một quyết định đủ quan trọng để ghi lại.

6. **Lần cuối cùng chúng ta mở lại một quyết định xây-hay-mua lớn đối chiếu với các giả định ban đầu của nó là khi nào, và chúng ta có nhận ra khi các giả định đó hết hạn không?** Các lựa chọn nguồn cung là một trong những quyết định tốn kém và khó đảo ngược nhất bạn đưa ra, và các giả định đằng sau chúng (giá của nhà cung cấp, nhân sự của chính bạn, mức độ trưởng thành của một lựa chọn mã nguồn mở) âm thầm lỗi thời trong khi quyết định vẫn đông cứng tại chỗ. Những cân nhắc đối lập đặt chi phí chìm và sự xáo trộn của việc chuyển đổi lên cân so với chi phí ngày càng tăng của việc bị khóa chặt, sự không vừa vặn hoàn hảo, hoặc gánh nặng bảo trì mà bạn không còn muốn. Hãy mang ADR gốc và các giả định đã nêu của nó, một ước tính tổng chi phí sở hữu hiện tại cho mỗi con đường bao gồm giấy phép, tích hợp, nhân sự và chi phí thoát ra, cùng mọi tín hiệu, một thay đổi giá hay việc hạ cấp hỗ trợ, cho thấy một tiền đề đã dịch chuyển. Với người mua thuộc chính phủ và chịu quy định, các quy tắc mua sắm và hợp đồng nhiều năm khiến những cánh cửa một chiều này đặc biệt ràng buộc, vì vậy hãy thống nhất trước các ngưỡng kích hoạt và nhịp độ sẽ buộc một quyết định lại có chủ đích thay vì một lần gia hạn mù quáng.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hầu như không quản trị gì và dựa mạnh vào tốc độ: với các lựa chọn cửa hai chiều có thể đảo ngược, hãy quyết định ngay tại bàn và đi tiếp. Dành thói quen quản trị duy nhất của bạn cho một nhúm cửa một chiều, một mô hình dữ liệu cốt lõi hoặc một nhà cung cấp nền tảng, và ghi từng cái vào một đoạn văn để đồng đội tương lai không phải tranh luận lại từ đầu. Bỏ hẳn hội đồng rà soát và con đường trải sẵn, vì ở quy mô của bạn chúng là chi phí bạn không thể gánh và cả đội đã chia sẻ cùng ngữ cảnh.

**Doanh nghiệp nhỏ.** Không có kiến trúc sư trong biên chế, hãy biến xây-hay-mua thành câu hỏi quản trị trung tâm của bạn và trả lời nó dựa trên tổng chi phí sở hữu chứ không phải sở thích. Mặc định mua hoặc áp dụng các công cụ được hỗ trợ tốt cho bất cứ thứ gì không phải yếu tố tạo khác biệt cốt lõi, vì bảo trì vĩnh viễn là chi phí bạn ít có khả năng gánh nhất. Giữ một nhật ký quyết định nhẹ để lý do đằng sau vài lựa chọn quan trọng của bạn tồn tại khi một nhân sự chủ chốt ra đi.

**Doanh nghiệp lớn.** Vấn đề của bạn là cân bằng tự chủ với thống nhất giữa nhiều đội, vì vậy hãy đầu tư vào một con đường trải sẵn được tài trợ và dành một hội đồng rà soát kiến trúc hẹp, nhanh cho các quyết định thực sự xuyên suốt và không thể đảo ngược. Chuẩn hóa ADR để lý do trở thành trí nhớ tổ chức có thể tìm kiếm, và quản lý nợ kỹ thuật cùng các lựa chọn nguồn cung như các danh mục có ngân sách thường trực. Đo xem các đội có chọn con đường đó vì nó dễ nhất không, và thu nhỏ bất kỳ hội đồng nào đã thoái hóa thành hàng đợi.

**Chính phủ.** Các quyết định có tài liệu, có thể bảo vệ được ở đây không phải tùy chọn: kiểm toán viên và cơ quan giám sát mong thấy lý do, các phương án đã cân nhắc và các giả định đằng sau mọi lựa chọn quan trọng. Hãy vận hành xây-hay-mua như một phân tích tổng chi phí sở hữu được ghi lại, tuân thủ các quy tắc mua sắm hạn chế việc bị khóa chặt vào nhà cung cấp duy nhất, và giữ ADR làm dấu vết bằng chứng sẵn sàng kiểm toán. Hãy nghiêm túc với các chân trời thời gian dài, vì một mô hình dữ liệu hay cam kết nhà cung cấp được đưa ra hôm nay có thể ràng buộc tổ chức cả thập kỷ, nên hãy phân loại nó là cửa một chiều và cân nhắc tương ứng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người đưa ra hầu hết quyết định trong vài phút ngay trên chiếc bàn chung, và với các lựa chọn cửa hai chiều có thể đảo ngược, tốc độ đó là lợi thế thực sự, nên họ chống lại mọi chi phí quản trị. Nhưng khi họ chọn một cơ sở dữ liệu và mô hình dữ liệu sẽ khó thay đổi sau này (cửa một chiều), họ dừng lại để viết một ghi chú một đoạn: các phương án, lựa chọn và những giả định đằng sau nó. Một năm sau, khi chạm giới hạn mở rộng, ghi chú duy nhất đó cứu họ khỏi việc tranh luận lại câu hỏi từ đầu. Họ hầu như không quản trị gì, và dành thói quen nhẹ duy nhất của mình cho vài quyết định thực sự tốn kém để đảo ngược.

**Doanh nghiệp lớn.** Các đội nền tảng của một doanh nghiệp lớn bị tê liệt bởi một hội đồng rà soát kiến trúc phải phê duyệt mọi lựa chọn công nghệ, tạo ra những hàng đợi nhiều tuần. Doanh nghiệp đã tái cấu trúc quản trị quanh một con đường trải sẵn: một danh mục được tuyển chọn gồm các ngôn ngữ, kho dữ liệu và đường ống được phê duyệt, hỗ trợ đầy đủ mà các đội có thể áp dụng ngay lập tức. ADR ghi lại mọi quyết định đi chệch, và một cuộc rà soát nhanh, mang tính tư vấn chỉ xử lý các lựa chọn ngoài đường. Phạm vi của hội đồng thu hẹp về việc đặt tiêu chuẩn và một nhúm quyết định thực sự xuyên suốt. Việc phân phối tăng tốc mạnh. Sự nhất quán thực sự cải thiện, vì con đường dễ nay là con đường tuân thủ. Và kho ADR cho tổ chức một bản ghi có thể tìm kiếm về lý do mọi thứ được xây như vậy.

**Chính phủ.** Một bộ của chính phủ đối mặt với quyết định xây-hay-mua lớn cho một nền tảng quản lý hồ sơ vụ việc dưới các quy tắc mua sắm và kiểm toán nghiêm ngặt. Thay vì quyết định theo sở thích, bộ đã thực hiện một phân tích tổng chi phí sở hữu có tài liệu trên ba phương án: xây tùy biến, mua một sản phẩm thương mại và áp dụng một nền tảng mã nguồn mở. Họ cân nhắc giấy phép, tích hợp, bảo trì dài hạn, nhân sự và bị khóa chặt, và ghi lại quyết định cùng các giả định của nó dưới dạng ADR. Nhiều năm sau, khi điều khoản của nhà cung cấp thay đổi, bộ đã xem lại ADR đó, thấy các giả định ban đầu không còn đúng, và quyết định lại với đầy đủ hiểu biết về lý do trước đó, tránh được một cuộc di chuyển mù quáng và tốn kém. Lý do được ghi lại cũng chính là bằng chứng có thể bảo vệ mà kiểm toán viên yêu cầu.

## Luận chứng kinh doanh: động lực, ROI và TCO

Quyết định là chi phí có đòn bẩy cao nhất và ít hiển thị nhất trong phần mềm. Một lựa chọn kiến trúc hoặc nguồn cung kém, không thể đảo ngược có thể áp đặt nhiều năm lực cản hoặc một khoản khắc phục chín chữ số. Quản trị nó tốt, vài giờ cân nhắc và một bản ghi bằng văn bản, gần như không tốn gì so sánh. Lợi tức của ADR và ủy quyền dựa trên khả năng đảo ngược đến từ hai nguồn: tránh những sai lầm đắt giá ở các quyết định cửa một chiều, và tránh lãng phí cân nhắc cũng như làm lại ở mọi thứ còn lại. Lý do được ghi lại cũng cắt giảm mạnh chi phí lặp lại của việc tranh luận lại những câu hỏi đã giải quyết và của việc các đội dịch ngược ý định đằng sau các hệ thống thừa kế.

Nợ kỹ thuật làm cho lập luận TCO trở nên cụ thể. Nợ không được quản lý hành xử đúng như lãi kép: một khoản thuế ngày càng tăng lên mọi thay đổi trong tương lai, cho đến khi hệ thống thực sự không thể bảo trì và đòi hỏi một lần viết lại tốn kém. Quản lý nợ như một danh mục, với phân bổ năng lực thường trực để trả các hạng mục lãi cao, rẻ hơn nhiều so với cuộc khủng hoảng cuối cùng. Quản trị tốt rẻ để áp dụng, chủ yếu là kỷ luật viết các quyết định ra và đầu tư ban đầu vào một con đường trải sẵn. Bỏ qua nó thì đắt: bạn trả bằng những lần viết lại có thể tránh, bất ngờ do bị khóa chặt, thất bại kiểm toán và mất trí nhớ tổ chức. Để thuyết phục ban lãnh đạo, hãy trình bày quản trị bằng ngôn ngữ của họ: giảm rủi ro, tránh làm lại, phân phối nhanh hơn nhờ con đường trải sẵn, và khả năng bảo vệ sẵn sàng kiểm toán. Cho thấy rằng mục tiêu không phải là nhiều quy trình hơn mà là quy trình được nhắm tốt hơn, xem xét nặng chỉ ở nơi việc đảo ngược tốn kém, và tốc độ không ma sát ở mọi nơi khác.

## Phản mẫu và cạm bẫy

- Quyết định không có tài liệu: lý do mất đi ngay khi những người đưa ra nó rời đi.
- Nút thắt hội đồng phê duyệt: một cơ quan trung tâm mà mọi dự án phải xếp hàng chờ.
- Quy trình một cỡ cho tất cả: ép các quyết định nhỏ có thể đảo ngược qua rà soát nặng nề.
- Tê liệt vì phân tích: trăn trở về những quyết định cửa hai chiều dễ đảo ngược.
- [CNTT bóng tối](https://en.wikipedia.org/wiki/Shadow_IT): các đội né hoàn toàn quản trị vì con đường được cho phép quá đau đớn.
- Nợ kỹ thuật vô hình: nợ không bao giờ được kiểm kê, không bao giờ được trả, âm thầm cộng dồn.
- Phản xạ xây-tất-cả hoặc mua-tất-cả: chọn nguồn cung theo thói quen thay vì phân tích TCO.
- Quản trị sân khấu: tài liệu và hội đồng tồn tại cho có vẻ nhưng không định hình quyết định.

## Mô hình trưởng thành

- Mức 1 (Khởi đầu): Quyết định tùy nghi và không được ghi lại; quản trị hoặc vắng mặt hoặc là một nút thắt tràn lan; nợ kỹ thuật vô hình và lý do đằng sau các lựa chọn bốc hơi khi con người rời đi.
- Mức 2 (Phát triển): Một số quyết định được ghi tài liệu và có một số rà soát, nhưng thực hành không nhất quán giữa các đội và quy trình thường không tương xứng với độ nặng và khả năng đảo ngược của quyết định.
- Mức 3 (Chuẩn hóa): ADR, con đường trải sẵn, ủy quyền dựa trên khả năng đảo ngược và bản kiểm kê nợ được lập thành tài liệu và thực thi toàn tổ chức, để lựa chọn tuân thủ là mặc định dễ dàng và lý do có thể tìm kiếm.
- Mức 4 (Quản lý): Quản trị được đo theo các đường cơ sở: mức chấp nhận con đường trải sẵn, độ bao phủ ADR, thời gian chu kỳ quyết định, nợ như một tỷ lệ của năng lực, và tỷ lệ ngoại lệ ngoài đường được theo dõi, và các quyết định trả nợ hoặc xem xét lại nguồn cung được kích hoạt bởi bằng chứng đó thay vì bởi khủng hoảng.
- Mức 5 (Điều phối): Quản trị được tinh chỉnh liên tục và tích hợp với kế hoạch phân phối và rủi ro; sự xem xét được nhắm chính xác vào các quyết định không thể đảo ngược; nợ và các lựa chọn nguồn cung được cân bằng lại tích cực như các danh mục và được quyết định lại dựa trên bằng chứng khi hoàn cảnh dịch chuyển.

## Ý tưởng để thảo luận

- Với những quyết định quan trọng nhất gần đây của chúng ta, chúng ta có tìm được lý do đã ghi đằng sau chúng không?
- Quản trị của chúng ta là nút thắt ở đâu, và vắng mặt ở đâu khi cần nó?
- Quyết định hiện tại nào của chúng ta là cửa một chiều, và chúng ta có đang đối xử với chúng như vậy không?
- Bao nhiêu năng lực của chúng ta dành cho việc trả nợ kỹ thuật, và như vậy có đủ không?
- Các đội của chúng ta đi theo con đường trải sẵn vì nó thực sự là con đường dễ nhất, hay đi vòng qua nó?
- Lần cuối cùng chúng ta xem xét lại một quyết định xây-hay-mua lớn đối chiếu với các giả định ban đầu là khi nào?

## Những điểm cần ghi nhớ

- Ghi lại các quyết định quan trọng và lý do của chúng bằng ADR; làm cho lý do bền vững.
- Quản trị qua các con đường trải sẵn và mặc định, không qua canh cổng từng trường hợp.
- Cân xứng độ nặng của quy trình với độ nặng và khả năng đảo ngược của quyết định; ủy quyền cửa hai chiều, cân nhắc kỹ cửa một chiều.
- Phân tích xây-hay-mua-hay-áp-dụng dựa trên tổng chi phí sở hữu, và ghi lại các giả định.
- Quản lý nợ kỹ thuật như một danh mục tường minh với phân bổ trả nợ thường trực.
- Giữ quản trị minh bạch và nhẹ; nhắm sự xem xét khan hiếm vào nơi việc đảo ngược tốn kém.

## Tài liệu tham khảo và đọc thêm

- Michael Nygard, "Documenting Architecture Decisions" (mẫu ADR gốc)
- Gregor Hohpe, "The Software Architect Elevator" và "37 Things One Architect Knows"
- Thư gửi cổ đông của Amazon về các quyết định Loại 1 so với Loại 2 (cửa một chiều so với hai chiều)
- Ward Cunningham, phép ẩn dụ "nợ kỹ thuật" gốc
- Martin Fowler, các bài viết về nợ kỹ thuật và kiến trúc tiến hóa
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (kiến trúc liên kết lỏng và sự tự chủ)
- ISO/IEC/IEEE 42010 về mô tả kiến trúc
