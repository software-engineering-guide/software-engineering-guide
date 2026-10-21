# 2.12 Mô hình và phương pháp phần mềm

## Tổng quan và động lực

Một mô hình phần mềm là sự đơn giản hóa có chủ đích của một hệ thống, được xây dựng để trả lời một câu hỏi cụ thể. Một phương pháp là cách thức có kỷ luật để tạo ra phần mềm, bao gồm các mô hình mà nó sử dụng dọc đường. Cùng nhau chúng tạo thành một lĩnh vực kiến thức của Bộ Kiến thức Kỹ thuật Phần mềm (SWEBOK), vì chúng là những công cụ tư duy bạn dùng để suy luận về một hệ thống trước, trong và sau khi bạn xây dựng nó. Một sơ đồ lớp UML ([Ngôn ngữ Mô hình hóa Thống nhất](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), một [sơ đồ thực thể-quan hệ](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), một [máy trạng thái](https://en.wikipedia.org/wiki/Finite-state_machine), một [đặc tả hình thức](https://en.wikipedia.org/wiki/Formal_specification) và một bản mẫu dùng một lần đều là mô hình. [Thác nước](https://en.wikipedia.org/wiki/Waterfall_model), [tạo bản mẫu](https://en.wikipedia.org/wiki/Software_prototyping), phát triển hình thức và [agile](https://en.wikipedia.org/wiki/Agile_software_development) đều là phương pháp.

Vì sao phải bận tâm đến mô hình? Vì bộ nhớ làm việc của con người nhỏ còn các hệ thống phần mềm thì lớn. Không ai có thể giữ một hệ thống trăm nghìn dòng trong đầu, nên chúng ta vẽ hình và viết các phép trừu tượng cho thấy từng khía cạnh một: dữ liệu, luồng điều khiển, các trạng thái, các tương tác. Một mô hình không bao giờ nhằm trung thành với mã; nó nhằm phù hợp cho một quyết định. Một mô hình tốt cho thấy chính xác những gì bạn cần để quyết định một điều, và che giấu mọi thứ còn lại.

Với các đội lớn, rủi ro thực sự là điều phối và giao tiếp. Khi hàng trăm kỹ sư, kiến trúc sư, nhà phân tích và kiểm toán viên làm việc trên một hệ thống, các mô hình chung là nền tảng chung nơi họ thương lượng về thiết kế, yêu cầu và rủi ro. Vì vậy hãy coi mô hình hóa là một công cụ có việc phải làm. Nó hoàn vốn khi một mô hình rẻ hơn sai lầm mà nó ngăn chặn. Nó trở thành lãng phí khi bạn vẽ nó vì chính nó, giữ nó rất lâu sau khi nó đã lỗi thời, hoặc tinh chỉnh nó vượt quá quyết định mà nó phục vụ. Mô hình hóa kết nối chặt với yêu cầu phần mềm (chương 2.8), nguyên tắc thiết kế phần mềm (chương 2.2), kiến trúc và các ký hiệu của nó như C4 và arc42 (chương 3.1), và cách thức làm việc agile (chương 10.7).

## Các nguyên tắc chính

- Mỗi mô hình có một mục đích; nếu bạn không thể nêu tên quyết định mà một mô hình cung cấp thông tin, đừng vẽ nó.
- Trừu tượng hóa là hành động cốt lõi của mô hình hóa: bao gồm những gì quan trọng cho mục đích, bỏ phần còn lại.
- Tính nhất quán quan trọng trong và giữa các mô hình; các mô hình mâu thuẫn còn tệ hơn không có.
- Mô hình trước hết là hiện vật giao tiếp; đối tượng của chúng quyết định ký hiệu và mức chi tiết.
- Ưu tiên mô hình nhẹ nhất trả lời được câu hỏi; sự tinh chỉnh có chi phí duy trì.
- Một mô hình chỉ tốt bằng phân tích của nó; một mô hình chưa kiểm tra là một giả định chưa được kiểm thử.
- Chọn phương pháp phù hợp với mức độ không chắc chắn, rủi ro và hậu quả thất bại của vấn đề.

## Khuyến nghị

### Mô hình hóa với trừu tượng, mục đích và tính nhất quán

Hãy bắt đầu mọi mô hình bằng việc gọi tên mục đích và đối tượng của nó. Sau đó trừu tượng hóa quyết liệt hướng về mục đích đó: một sơ đồ tuần tự nhằm giải quyết một điều kiện chạy đua nên cho thấy thời điểm và thông điệp, không phải mọi trường. Giữ các mô hình của bạn nhất quán với nhau, để các thực thể trong ERD, các lớp trong sơ đồ lớp, và các danh từ trong yêu cầu đều khớp nhau, và nhất quán với thực tế, nghĩa là bạn cập nhật hoặc xóa một mô hình khi hệ thống đã đi tiếp. Một mô hình lỗi thời mà mọi người tin là một mối nguy. Một mô hình lỗi thời mà mọi người phớt lờ là lãng phí vẫn tốn sự chú ý.

### Chọn mô hình cấu trúc hoặc hành vi phù hợp với câu hỏi

Dùng các mô hình cấu trúc để cho thấy một hệ thống được tạo thành từ gì và các phần liên hệ thế nào: sơ đồ lớp, sơ đồ thành phần và sơ đồ thực thể-quan hệ cho cấu trúc dữ liệu. Dùng các mô hình hành vi để cho thấy một hệ thống làm gì theo thời gian: máy trạng thái cho các đối tượng có vòng đời có ý nghĩa, sơ đồ tuần tự cho các tương tác giữa các thành phần, và sơ đồ hoạt động cho quy trình công việc và quy trình kinh doanh. Chọn một ký hiệu làm lộ quyết định trước mặt bạn. Hầu hết các hệ thống chỉ cần một nhúm loại sơ đồ, được vẽ có chọn lọc, không phải toàn bộ danh mục UML áp dụng cho mọi thứ.

### Phân tích các mô hình, đừng chỉ vẽ chúng

Một mô hình xứng đáng nhờ phân tích, không chỉ nhờ vẽ. Kiểm tra một máy trạng thái xem có trạng thái không thể đạt tới, thiếu chuyển tiếp và bế tắc không. Kiểm tra một ERD xem có vấn đề chuẩn hóa và quan hệ mồ côi không. Đi qua một sơ đồ tuần tự đối chiếu với yêu cầu để tìm các đường lỗi bị thiếu. Rà soát các mô hình của bạn với các chuyên gia miền có thể phát hiện điều sai. Và ở nơi chi phí thất bại cao, hãy với tới phân tích có công cụ hỗ trợ (bộ kiểm tra mô hình, bộ kiểm tra tính nhất quán, mô phỏng) thay vì nhìn bằng mắt.

### Áp dụng các phương pháp kinh nghiệm làm mặc định

Hầu hết phần mềm được xây bằng các phương pháp kinh nghiệm: các cách tiếp cận lặp, dựa trên kinh nghiệm dùng mô hình một cách không chính thức và đánh giá kết quả theo kỳ vọng thay vì chứng minh. Với hầu hết các hệ thống kinh doanh và chính phủ, đó là điều hoàn toàn đúng: yêu cầu tiến hóa, và một lỗi thường phục hồi được. Các phương pháp kinh nghiệm kết hợp tự nhiên với agile (chương 10.7): mô hình hóa vừa đủ để thống nhất đội, rồi xây dựng và học hỏi.

### Dành phương pháp hình thức cho các lõi có hậu quả cao

[Phương pháp hình thức](https://en.wikipedia.org/wiki/Formal_methods) diễn đạt đặc tả bằng toán học và dùng kiểm chứng, dù là chứng minh hay [kiểm tra mô hình](https://en.wikipedia.org/wiki/Model_checking) vét cạn, để thiết lập các thuộc tính. Chúng tốn kỹ năng và thời gian thực sự, và chúng hoàn vốn chính xác ở nơi thất bại là thảm khốc hoặc không thể đảo ngược: điều khiển quan trọng về an toàn, giao thức mật mã, lõi thanh toán bù trừ tài chính và tương tự. Hãy áp dụng chúng cho lõi quan trọng nhỏ, không phải toàn bộ hệ thống. Và lưu ý rằng chỉ riêng đặc tả hình thức, ngay cả khi không có chứng minh đầy đủ, thường mang lại giá trị đơn giản vì buộc bạn phải chính xác.

### Dùng tạo bản mẫu để loại bỏ sự không chắc chắn

Khi yêu cầu hoặc tính khả thi chưa rõ, hãy xây một bản mẫu để học hỏi, rồi quyết định, có chủ đích, xem nên phát triển nó hay loại bỏ nó. Bản mẫu dùng một lần khám phá một câu hỏi với chi phí rẻ và sau đó bị xóa. Bản mẫu tiến hóa trở thành sản phẩm và phải được xây theo tiêu chuẩn môi trường thực. Thất bại kinh điển là để một bản mẫu dùng một lần trượt vào môi trường thực một cách vô tình. Vì vậy hãy gọi tên loại của bản mẫu trước khi bạn xây nó.

### Khớp phương pháp với rủi ro, không phải mốt

Chọn phương pháp theo mức độ không chắc chắn của vấn đề và hậu quả của thất bại. Sự không chắc chắn cao ưu ái tạo bản mẫu và lặp agile. Hậu quả cao ưu ái phân tích hình thức và kiểm chứng nghiêm ngặt. Một hệ thống có cả hai cần một lõi hình thức quan trọng bên trong một lớp vỏ agile. Dù làm gì, đừng áp dụng một phương pháp chỉ vì nó danh giá hoặc vì một nhà cung cấp đang bán nó.

## Đánh đổi: ưu và nhược điểm

| Mô hình hoặc phương pháp | Khi áp dụng tốt | Chế độ thất bại |
|---|---|---|
| Mô hình cấu trúc (UML, ERD) | Bức tranh chung về các phần và dữ liệu | Sơ đồ tràn lan; trôi khỏi mã |
| Mô hình hành vi (trạng thái, tuần tự, hoạt động) | Phơi bày thời điểm, trạng thái và trường hợp biên | Sơ đồ quá chi tiết không ai đọc |
| Phương pháp kinh nghiệm | Nhanh, linh hoạt, phù hợp hầu hết hệ thống | Thiếu kỷ luật; giả định ẩn |
| Phương pháp hình thức | Thuộc tính chứng minh được cho lõi quan trọng | Chi phí cao; áp dụng sai cho toàn hệ thống |
| Tạo bản mẫu | Học rẻ; loại bỏ rủi ro sớm | Mã dùng một lần được thăng lên môi trường thực |
| Phương pháp agile | Thích ứng với yêu cầu thay đổi | Bỏ qua mô hình hóa cần cho các vấn đề khó |

Căng thẳng lặp lại là giữa sự chặt chẽ và tốc độ. Mô hình hóa quá ít đưa các giả định ẩn vào môi trường thực. Mô hình hóa quá nhiều đốt công sức vào các sơ đồ không bao giờ cung cấp thông tin cho quyết định và mục nát ngay khi mã thay đổi. Không có liều cố định nào sửa được điều này, chỉ có quy tắc tỷ lệ: đầu tư vào một mô hình hay phương pháp tương xứng với sự không chắc chắn nó giải quyết và chi phí của việc quyết định sai. Một công cụ thanh toán và một trang vi mô tiếp thị xứng đáng được đối xử khác nhau.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta có phân tích các mô hình của mình, hay chỉ vẽ chúng rồi đi tiếp?** Một mô hình xứng đáng nhờ phân tích, không phải nhờ tồn tại: một máy trạng thái mà bạn không bao giờ kiểm tra xem có trạng thái không thể đạt tới hay thiếu chuyển tiếp là một giả định chưa được kiểm thử khoác áo sơ đồ. Trong một đội lớn đây là nơi các lỗi thực sự ẩn náu, vì một bức tranh trông hợp lý được tin chính vào lúc không ai đem nó đối chiếu với yêu cầu để tìm đường lỗi bị thiếu hay quan hệ mồ côi. Hãy mang mô hình hành vi quan trọng nhất của bạn đến cuộc họp và thử phá nó: chuyển tiếp nào chưa được xác định, trạng thái nào không có lối ra, tuần tự nào không có thời gian chờ? Ở nơi chi phí thất bại cao, câu trả lời nên đẩy bạn về phía phân tích có công cụ hỗ trợ (bộ kiểm tra mô hình, bộ kiểm tra tính nhất quán, mô phỏng) thay vì nhìn bằng mắt, vì toàn bộ lý do để mô hình hóa một lõi quan trọng là tìm ra lỗi trên bảng trắng thay vì trên môi trường thực.

2. **Khi hai mô hình của chúng ta mâu thuẫn nhau, mô hình nào thắng, và ai nhận ra sự mâu thuẫn?** Tính nhất quán quan trọng trong và giữa các mô hình, và các mô hình mâu thuẫn còn tệ hơn không có vì mọi người hành động theo cả hai. Trong một hệ thống lớn, các thực thể trong mô hình dữ liệu, các lớp trong thiết kế và các danh từ trong yêu cầu âm thầm trôi xa nhau khi các đội khác nhau cập nhật các hiện vật khác nhau, và dấu hiệu đầu tiên thường là một lỗi môi trường thực khi hai thành phần bất đồng về một thứ là gì. Hãy mang một ví dụ: chọn một khái niệm cốt lõi và kiểm tra xem ERD, mã và yêu cầu có thực sự đồng ý về hình dạng và vòng đời của nó không. Nếu không, hãy quyết định hiện vật nào có thẩm quyền và ai chịu trách nhiệm giữ các hiện vật khác theo kịp, và sẵn sàng xóa một mô hình thay vì để một mô hình lỗi thời tiếp tục nói dối đội.

3. **Lõi nào trong hệ thống của chúng ta, nếu sai, làm mất tiền thật hoặc gây hại cho ai đó, và nó có nhận được sự chặt chẽ mà nó xứng đáng không?** Bước đi trung tâm của chương này là khớp phương pháp với rủi ro: phương pháp kinh nghiệm và agile cho phần lớn có thể phục hồi, đặc tả và kiểm chứng hình thức cho lõi nhỏ có hậu quả cao, và tạo bản mẫu rẻ cho phần thực sự không chắc chắn. Các chế độ thất bại là đối xứng và đều tốn kém: áp dụng phương pháp hình thức cho một trang vi mô tiếp thị đốt tiền, và coi một công cụ thanh toán bù trừ hay bộ quy tắc đủ điều kiện là công việc agile thông thường mời gọi khiếm khuyết thảm khốc, không thể đảo ngược. Hãy mang một bản đồ hệ thống của bạn và đánh dấu nơi một lỗi là thảm khốc so với phục hồi được, và nơi yêu cầu chắc chắn so với chưa biết. Câu trả lời nên tập trung khoản đầu tư mô hình hóa của bạn vào nơi có tiền và sự mơ hồ, và tường minh giữ lại nó ở mọi nơi khác, để một lõi hình thức quan trọng có thể nằm bên trong một lớp vỏ agile mà không phương pháp nào tràn sang lãnh thổ của phương pháp kia.

4. **Chúng ta mô hình hóa bao nhiêu trước khi viết mã, và liều lượng đó có thay đổi theo sự không chắc chắn trước mặt không?** Thiết kế lớn trả trước và không thiết kế gì đều là chế độ thất bại, và liều lượng đúng nằm giữa chúng, được chi phối bởi mức độ không chắc chắn mà một mô hình thực sự loại bỏ. Trong một đội lớn, áp lực chạy cả hai hướng: một quy trình quản trị có thể đòi một bộ sơ đồ đầy đủ trước khi có mã, khóa chặt các quyết định được đưa ra với ít thông tin nhất, trong khi áp lực phân phối có thể đẩy một đội bỏ qua máy trạng thái duy nhất lẽ ra đã bắt được một trường hợp biên đắt giá. Hãy mang hai dự án gần nhất của bạn và sắp xếp các mô hình bạn tạo ra thành những cái đã cung cấp thông tin cho một quyết định thực và những cái chỉ được vẽ vì một biểu mẫu đòi hỏi. Trong các chương trình doanh nghiệp và chính phủ, nơi một cổng giai đoạn hoặc hội đồng phê duyệt thường bắt buộc tài liệu trả trước, hãy chuẩn bị lập luận cho việc mô hình hóa bám theo rủi ro thay vì một danh sách sản phẩm bàn giao cố định, để lõi thanh toán nhận được sự chặt chẽ của nó còn công cụ báo cáo nội bộ không chìm trong những sơ đồ không ai đọc.

5. **Chúng ta đã thống nhất một ký hiệu chung và một nơi duy nhất cho các mô hình của mình chưa, hay mỗi đội tự phát minh?** Mô hình trước hết là hiện vật giao tiếp, và giá trị của chúng sụp đổ khi một máy trạng thái vẽ trong công cụ của một đội không thể được đọc, tìm thấy hay tin cậy bởi đội thừa kế nó. Với hàng trăm kỹ sư, những cân nhắc đối lập là thật: một ký hiệu và kho lưu trữ bắt buộc mua sự nhất quán và khả năng tìm thấy, nhưng chúng cũng áp đặt chi phí học tập và có thể đẩy mọi người về phía các công cụ nặng nề khi một bức ảnh chụp bảng trắng đã đủ phục vụ. Hãy mang các ví dụ về nơi một mô hình thực sự sống (một wiki, một công cụ sơ đồ, một bản trình chiếu, laptop của ai đó) và hỏi ai có thể tìm thấy và hiểu nó sáu tháng sau. Trong bối cảnh doanh nghiệp và chịu quy định, góc độ kiểm toán làm điều này sắc nét hơn: một kiểm toán viên không thể xác định vị trí mô hình dữ liệu hiện hành hoặc truy vết một quyết định về một máy trạng thái có tài liệu sẽ coi hệ thống là không có tài liệu, vì vậy hãy thống nhất một ký hiệu chung nhỏ và một vị trí bền vững, và chấp nhận việc nắm bắt nhẹ nhàng thay vì nghi thức ở nơi hậu quả thấp.

6. **Trước khi xây một bản mẫu, chúng ta có quyết định có chủ đích nó là dùng một lần hay tiến hóa không, và chúng ta có giữ mình với lựa chọn đó không?** Thất bại kinh điển, tốn kém là một bản mẫu dùng một lần âm thầm trượt vào môi trường thực vì nó trình diễn tốt và không ai gọi tên loại của nó từ đầu. Căng thẳng là thật: bản mẫu dùng một lần mua việc học rẻ nhất có thể và nên bị xóa, trong khi bản mẫu tiến hóa trở thành sản phẩm và phải được xây theo tiêu chuẩn môi trường thực từ dòng đầu tiên, và nhầm lẫn hai loại hoặc lãng phí việc làm lại hoặc phát hành mã mong manh vào một vai trò mà nó chưa bao giờ được thiết kế. Hãy mang một bản mẫu gần đây và hỏi điều gì đã được quyết định trước khi nó được xây, ai nắm thẩm quyền để thăng cấp hay loại bỏ nó, và quyết định đó có sống sót qua áp lực phân phối không. Trong chính phủ và các bối cảnh có trách nhiệm giải trình khác, nơi một hệ thống hướng đến công dân mang nghĩa vụ minh bạch và độ tin cậy, hãy coi việc thăng cấp vô tình là thất bại kiểm soát: cố định số phận của bản mẫu từ trước, và biến việc loại bỏ một bản mẫu dùng một lần thành công thành một kết quả được ăn mừng thay vì một lãng phí cần tránh.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy mô hình hóa trên bảng trắng, chụp ảnh nó, và đi tiếp. Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ thuật, vì vậy chỉ với tới một mô hình khi nó rẻ hơn sai lầm mà nó ngăn chặn: một máy trạng thái đăng ký trước khi bạn lập trình các trường hợp biên thanh toán, không phải toàn bộ danh mục UML cho một sản phẩm có thể đổi hướng tháng sau. Hãy ở lại với kinh nghiệm và agile, loại phương pháp hình thức khỏi bàn hoàn toàn, và coi mọi bản mẫu là dùng một lần trừ khi bạn chủ động quyết định khác.

**Doanh nghiệp nhỏ.** Bạn có thể không có ai có công việc là mô hình hóa hình thức, vì vậy hãy dựa vào các mô hình đã được nhúng trong công cụ và khung bạn mua thay vì dựng một thực hành mô hình hóa của riêng mình. Hãy đóng khung vài mô hình bạn vẽ quanh các quyết định cụ thể: một bản phác thảo mô hình dữ liệu đơn giản để thống nhất dữ liệu khách hàng nào bạn giữ, một sơ đồ trạng thái cho quy trình duy nhất làm bạn mất khách khi nó hỏng. Hãy ưu tiên một sản phẩm mua về với mô hình dữ liệu đã được chứng minh hơn là tự xây và lập tài liệu, và giữ mọi thứ bạn vẽ đủ nhẹ để một người có thể bảo trì.

**Doanh nghiệp lớn.** Vấn đề cốt lõi là điều phối qua nhiều đội, vì vậy các mô hình chung trở thành nền tảng chung: một mô hình dữ liệu đã thống nhất, một ký hiệu nhất quán, và một nơi mà ERD, sơ đồ C4 và máy trạng thái có thể được tìm thấy và tin cậy. Hãy chuẩn hóa một ký hiệu nhỏ và thực thi tính nhất quán để các thực thể trong yêu cầu, thiết kế và cơ sở dữ liệu không trôi xa nhau giữa các đội. Hãy dành đặc tả hình thức và kiểm tra mô hình cho các lõi có hậu quả cao (thanh toán bù trừ, đối chiếu, kiểm soát truy cập), tài trợ kỹ năng chuyên gia mà điều đó đòi hỏi, và giữ một dấu vết kiểm toán từ từng mô hình có tài liệu về quyết định mà nó biện minh.

**Chính phủ.** Các quy tắc được đặt ra trong luật phải truy vết được về đạo luật, đó là nơi đặc tả hình thức xứng đáng với chi phí của nó: đặc tả logic đủ điều kiện hoặc đánh giá một cách chính xác, kiểm chứng các thuộc tính then chốt, và để kiểm toán viên truy vết mọi kết quả về quy tắc đã tạo ra nó. Mua sắm thêm trọng lượng riêng, vì tài liệu và mô hình thường là sản phẩm bàn giao theo hợp đồng, nên hãy thống nhất mô hình nào thực sự mang tính quyết định thay vì chỉ được tạo ra để thỏa mãn một danh sách kiểm tra. Hãy công bố các mô tả bằng ngôn ngữ giản dị về cách các hệ thống hệ trọng hoạt động, và dùng tạo bản mẫu dùng một lần để kiểm thử việc tiếp nhận hướng đến công dân với người dùng thực trước khi cam kết một bản dựng môi trường thực.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp nhỏ xây dựng sản phẩm thanh toán đăng ký phác thảo vòng đời đăng ký (dùng thử, hoạt động, quá hạn, đã hủy, kích hoạt lại) thành một máy trạng thái trên bảng trắng trước khi viết mã. Khi đi qua sơ đồ, họ nhận thấy mình chưa bao giờ xác định điều gì xảy ra khi khoản thanh toán của một tài khoản quá hạn cuối cùng cũng được xử lý, một trường hợp biên lẽ ra đã khiến khách hàng thực rơi vào tình trạng lấp lửng. Mô hình năm phút đó tiết kiệm một rắc rối trên môi trường thực, và họ chụp ảnh nó thay vì duy trì một công cụ sơ đồ nặng nề. Ở mọi nơi khác họ ở lại agile và mô hình hóa vừa đủ để thống nhất, vì ở quy mô của họ một lỗi phục hồi được và phương pháp hình thức sẽ chỉ là chi phí thuần túy.

**Doanh nghiệp lớn.** Một ngân hàng toàn cầu xây một nền tảng thanh toán mới. Đội dùng một sơ đồ thực thể-quan hệ để thống nhất mô hình dữ liệu chung giữa các đội tài khoản, sổ cái và nhắn tin, và các sơ đồ C4 (chương 3.1) để cho thấy các dịch vụ khớp với nhau thế nào. Họ mô hình hóa vòng đời giao dịch (đang chờ, đã bù trừ, đã quyết toán, đã đảo ngược, đang tranh chấp) thành một máy trạng thái tường minh, và phân tích cho thấy nó thiếu một chuyển tiếp cho các lần đảo ngược một phần. Khoảng trống được sửa trên bảng trắng thay vì trên môi trường thực. Các sơ đồ tuần tự đi qua luồng quyết toán đối chiếu với yêu cầu (chương 2.8) để làm lộ các đường hết thời gian chờ và thử lại bị thiếu. Việc phân phối hằng ngày là agile, nhưng thuật toán đối chiếu lõi, nơi một lỗi nghĩa là mất tiền thật, nhận được một đặc tả hình thức và được kiểm tra mô hình trước khi triển khai. Mô hình hóa tập trung ở nơi có tiền và sự mơ hồ, và giữ nhẹ ở mọi nơi khác.

**Chính phủ.** Một cơ quan thuế quốc gia hiện đại hóa việc đánh giá trợ cấp. Vì các quy tắc đủ điều kiện được đặt ra trong luật và được kiểm toán, đội viết một đặc tả hình thức của các quy tắc như những phép biến đổi thuần túy và kiểm chứng các thuộc tính then chốt, chẳng hạn không có người nộp đơn nào vừa đủ điều kiện vừa không đủ điều kiện và mọi hồ sơ đều đi đến một quyết định, để kiểm toán viên có thể truy vết kết quả về đạo luật. Bên cạnh lõi hình thức, đội xây một bản mẫu dùng một lần của biểu mẫu tiếp nhận hướng đến công dân để kiểm thử với người dùng thực. Họ học được rằng một trình hướng dẫn nhiều bước giảm lỗi, rồi loại bỏ bản mẫu và xây lại phần tiếp nhận theo tiêu chuẩn môi trường thực. Các sơ đồ hoạt động ghi lại quy trình đầu-cuối của nhân viên xử lý hồ sơ cho đào tạo và kiểm toán. Các quy tắc có hậu quả cao nhận sự chặt chẽ hình thức; trải nghiệm người dùng không chắc chắn nhận tạo bản mẫu rẻ; không phương pháp nào được áp dụng ở nơi phương pháp kia thuộc về.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của mô hình hóa đến từ việc tìm lỗi sớm hơn, nơi chúng rẻ hơn nhiều để sửa. Một mâu thuẫn tìm thấy trên bảng trắng tốn vài phút. Cùng mâu thuẫn đó tìm thấy trên môi trường thực có thể tốn một sự cố ngừng hoạt động, một chương trình làm lại, hoặc, trong các lĩnh vực chịu quy định, một trách nhiệm pháp lý. Mô hình cũng giảm tổng chi phí sở hữu bằng cách phục vụ như giao tiếp bền vững. Một hệ thống tồn tại lâu hơn tác giả của nó, trường hợp bình thường trong doanh nghiệp và chính phủ, rẻ hơn nhiều để bảo trì khi mô hình dữ liệu, máy trạng thái và các luồng chính của nó được lập tài liệu chính xác.

Chi phí là thật, và bạn phải cân nhắc chúng. Mô hình tốn thời gian để xây, kỹ năng để xây tốt, và công sức liên tục để giữ cập nhật; phương pháp hình thức thêm lao động chuyên gia. Điểm hòa vốn bị chi phối bởi sự không chắc chắn và hậu quả. Ở nơi cả hai thấp, mô hình hóa nặng phá hủy giá trị và các phương pháp kinh nghiệm agile thắng. Ở nơi một trong hai cao, mô hình hóa có mục tiêu, và, với lõi quan trọng, kiểm chứng hình thức, hoàn vốn nhiều lần bằng cách ngăn chặn loại thất bại đắt đỏ. Để thuyết phục ban lãnh đạo, hãy gắn khoản đầu tư mô hình hóa với các rủi ro cụ thể được loại bỏ và với khả năng bảo trì của các hệ thống tồn tại lâu. Và theo dõi xem các mô hình có thực sự được tham khảo không, vì một mô hình không dùng là chi phí thuần túy.

## Phản mẫu và cạm bẫy

- **Mô hình hóa vì chính nó:** tạo ra sơ đồ vì một quy trình đòi hỏi, không phải vì chúng cung cấp thông tin cho một quyết định.
- **Mô hình lỗi thời được tin như sự thật:** các sơ đồ không còn khớp với mã nhưng vẫn được dựa vào.
- **Thiết kế lớn trả trước:** các mô hình vét cạn được tạo ra trước khi có bất kỳ mã nào, khóa chặt các quyết định được đưa ra với ít thông tin nhất.
- **Sơ đồ tràn lan:** mọi loại UML được áp dụng đồng đều, nhấn chìm vài góc nhìn hữu ích trong nhiễu.
- **Phương pháp hình thức ở khắp nơi:** áp dụng kiểm chứng đắt đỏ cho mã mà hậu quả thất bại không biện minh.
- **Thăng cấp bản mẫu vô tình:** một bản mẫu dùng một lần âm thầm được phát hành làm sản phẩm.
- **Ký hiệu hơn thực chất:** tranh cãi về tính đúng đắn của UML thay vì liệu mô hình có trả lời câu hỏi không.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** Mô hình hóa tùy nghi hoặc vắng mặt và hoàn toàn phản ứng; không có phương pháp nào được nêu tên; các mô hình, khi có vẽ, không nhất quán, không được phân tích, và bị bỏ ngay khi cuộc họp kết thúc.
- **Mức 2 (Phát triển):** Một số đội vẽ các sơ đồ phổ biến và theo một phương pháp có tên, nhưng thực hành không đồng đều trong tổ chức: các mô hình thường được tạo ra theo nghi thức, trôi khỏi mã, và hiếm khi được phân tích để tìm lỗi.
- **Mức 3 (Chuẩn hóa):** Một ký hiệu chung, một hướng dẫn chọn phương pháp có tài liệu, và các quy tắc nhất quán được xác định và thực thi toàn tổ chức; các mô hình được chọn theo mục đích, giữ đồng bộ với hệ thống, được rà soát để tìm lỗi, và phương pháp được khớp với rủi ro của từng vấn đề.
- **Mức 4 (Quản lý):** Mô hình hóa được đo và kiểm soát theo các đường cơ sở; các đội theo dõi phân tích bắt được bao nhiêu lỗi trước khi triển khai, các mô hình trôi khỏi mã bao xa, liệu mỗi mô hình có thực sự được tham khảo cho một quyết định thực không, và việc làm lại cùng thời gian chu kỳ tiết kiệm được so với một đường cơ sở xác định; lựa chọn phương pháp được hiệu chỉnh theo sự không chắc chắn và hậu quả đo được, và các lõi quan trọng được kiểm chứng hình thức theo các mục tiêu độ bao phủ đã thống nhất.
- **Mức 5 (Điều phối):** Mô hình hóa và lựa chọn phương pháp được cải tiến liên tục và tích hợp với phân phối và hoạch định rủi ro trong toàn tổ chức; đầu tư thích ứng khi sự không chắc chắn và hậu quả dịch chuyển, các mô hình thường xuyên được giữ cập nhật, loại bỏ hoặc đào sâu dựa trên bằng chứng, và các phương pháp hình thức, kinh nghiệm và tạo bản mẫu được kết hợp để mỗi cái nằm đúng nơi nó hoàn vốn.

## Ý tưởng để thảo luận

- Với dự án gần nhất của bạn, những mô hình nào đã cung cấp thông tin cho một quyết định thực, và những mô hình nào chỉ được vẽ vì một quy trình đòi hỏi?
- Ở đâu trong hệ thống của bạn một đặc tả hình thức sẽ tự hoàn vốn, và ở đâu nó sẽ là lãng phí?
- Làm thế nào bạn quyết định một bản mẫu là dùng một lần hay tiến hóa, và bạn có thực thi quyết định đó không?
- Làm thế nào bạn giữ các mô hình khỏi trôi lệch khỏi mã, hay bạn chấp nhận rằng một số nên bị xóa?
- Lượng mô hình hóa phù hợp trước khi viết mã trong bối cảnh của bạn là bao nhiêu, và nó thay đổi thế nào theo sự không chắc chắn?
- Mô hình hành vi nào (trạng thái, tuần tự hay hoạt động) sẽ đã bắt được sự cố môi trường thực gần nhất của bạn?

## Những điểm cần ghi nhớ

- Một mô hình là một phép trừu tượng có mục đích; nếu bạn không thể nêu tên quyết định nó cung cấp thông tin, đừng vẽ nó.
- Khớp mô hình cấu trúc và hành vi với câu hỏi cụ thể, và giữ chúng nhất quán và hiện hành.
- Phân tích các mô hình; một mô hình chưa kiểm tra là một giả định chưa được kiểm thử.
- Phương pháp kinh nghiệm và agile phù hợp hầu hết hệ thống; dành phương pháp hình thức cho các lõi có hậu quả cao.
- Dùng bản mẫu để loại bỏ sự không chắc chắn, và quyết định từ trước chúng là dùng một lần hay tiến hóa.
- Đầu tư vào mô hình hóa tương xứng với sự không chắc chắn nó giải quyết và chi phí của việc quyết định sai.

## Tài liệu tham khảo và đọc thêm

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, lĩnh vực kiến thức Mô hình và Phương pháp Kỹ thuật Phần mềm
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* và *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (ngôn ngữ mô hình hóa Alloy)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (mô hình C4)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
