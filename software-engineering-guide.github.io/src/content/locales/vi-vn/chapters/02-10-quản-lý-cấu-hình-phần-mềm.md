# 2.10 Quản lý cấu hình phần mềm

## Tổng quan và động lực

[Quản lý cấu hình phần mềm](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) là kỷ luật xác định các thành phần của một hệ thống phần mềm, kiểm soát cách chúng thay đổi, ghi lại trạng thái của mọi thay đổi, và xác minh rằng những gì bạn đã dựng và giao khớp với những gì bạn dự định. Nó trả lời một câu hỏi nghe có vẻ đơn giản nhưng trở nên khó ở quy mô lớn: chính xác thì bản phát hành này chứa gì, nó đến đó bằng cách nào, và ai đã phê duyệt? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) coi SCM là một lĩnh vực kiến thức nền tảng vì một lý do rõ ràng: mọi hoạt động kỹ thuật khác đều cần một cấu hình ổn định, đã biết để làm việc dựa trên.

Trong một đội lớn, SCM là mô liên kết giữ cho hàng nghìn bộ phận chuyển động nhất quán. Mã nguồn, thư viện, ảnh container, định nghĩa hạ tầng, dữ liệu cấu hình, tài liệu và hiện vật kiểm thử đều thay đổi theo đồng hồ riêng của chúng, và một hệ thống được giao là một tổ hợp cụ thể của các phiên bản cụ thể của tất cả những thứ đó. Không có quản lý cấu hình có chủ đích, tổ hợp đó không được biết và không thể tái tạo. Bạn không thể tạo lại một bản phát hành trong quá khứ, truy vết một lỗi về thay đổi gây ra nó, hay nói một cách tự tin điều gì đang chạy trên môi trường thực.

Bối cảnh doanh nghiệp và chính phủ nâng cao rủi ro. Các chương trình chịu quy định và khu vực công phải chứng minh rằng các thay đổi được ủy quyền, rà soát và ghi lại; rằng một bản dựng được giao truy vết về các yêu cầu và mã nguồn đã được phê duyệt; và rằng không có gì vào hệ thống mà không được kiểm soát. Ở đây SCM vừa là một hệ thống bằng chứng vừa là một hệ thống kỹ thuật. [Quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control) (chương 2.6) quản lý lịch sử mã nguồn; SCM quản trị toàn bộ cấu hình và quy trình được kiểm soát qua đó nó thay đổi. Nó gắn chặt với [hạ tầng dưới dạng mã](https://en.wikipedia.org/wiki/Infrastructure_as_code) (chương 8.2), các đường ống phân phối (chương 8.1), và kiểm toán cùng đảm bảo (chương 10.2).

## Các nguyên tắc chính

- Mọi thứ quyết định hành vi hệ thống là một [hạng mục cấu hình](https://en.wikipedia.org/wiki/Configuration_item) nằm dưới sự kiểm soát, không chỉ mã nguồn.
- Một [đường cơ sở](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) là một điểm tham chiếu đã biết, đã thống nhất; các thay đổi được thực hiện đối chiếu với đường cơ sở một cách có chủ đích, không tùy tiện.
- Thay đổi được kiểm soát và ghi lại, không bị ngăn chặn; mục tiêu là thay đổi được ủy quyền, truy vết được.
- Kế toán trạng thái nghĩa là bạn luôn có thể trả lời cái gì nằm trong một cấu hình và lịch sử thay đổi của nó là gì.
- Kiểm toán xác minh rằng hệ thống được dựng và giao khớp với cấu hình đã ghi lại và các yêu cầu đã được phê duyệt.
- Khả năng tái tạo là không thể thương lượng: bất kỳ phiên bản đã phát hành nào cũng phải dựng lại được từ các đầu vào được kiểm soát.
- Tự động hóa việc xác định, ghi lại và xác minh; ghi sổ thủ công không mở rộng được và không sống sót qua kiểm toán.

## Khuyến nghị

### Xác định quy trình SCM và giao quyền sở hữu

Hãy viết ra một kế hoạch SCM nêu cái gì nằm dưới kiểm soát cấu hình, các hạng mục được xác định thế nào, các thay đổi được đề xuất và phê duyệt ra sao, và trạng thái được ghi lại cùng kiểm toán thế nào. Giao quyền sở hữu rõ ràng, như một người quản lý cấu hình hoặc một đội chịu trách nhiệm, để SCM không phải là việc của mọi người và do đó không phải của ai. Điều chỉnh quy trình theo rủi ro: một công cụ nội bộ nhỏ cần kiểm soát nhẹ, trong khi một hệ thống quan trọng về an toàn hoặc chịu quy định cần các hội đồng và hồ sơ chính thức. Neo kế hoạch vào một tiêu chuẩn được công nhận như IEEE 828 để kiểm toán viên và đối tác có thể theo dõi.

### Xác định hạng mục cấu hình và thiết lập đường cơ sở

Liệt kê các hạng mục cấu hình quyết định cách hệ thống hành xử: mã nguồn, phụ thuộc, tập lệnh dựng, ảnh container, định nghĩa hạ tầng, dữ liệu cấu hình, lược đồ và các tài liệu then chốt. Cho mỗi hạng mục một mã định danh ổn định và một lược đồ đánh phiên bản. Đặt đường cơ sở tại các điểm có ý nghĩa (một phiên bản đã phát hành, một tập yêu cầu đã phê duyệt, một bản dựng đã chứng nhận) để bạn có một tham chiếu đã thống nhất để thay đổi dựa vào và quay lại. Một đường cơ sở là bất biến: khi đã tuyên bố, bạn không chỉnh sửa nó. Bạn chỉ thay thế nó bằng một đường cơ sở mới được tạo qua quy trình thay đổi.

### Kiểm soát thay đổi qua một quy trình xác định và các hội đồng phù hợp

Định tuyến các thay đổi đến các hạng mục được kiểm soát qua một con đường xác định: đề xuất, đánh giá tác động, phê duyệt, triển khai và xác minh. Với các hạng mục rủi ro cao hơn, hãy dùng một [hội đồng kiểm soát thay đổi](https://en.wikipedia.org/wiki/Change_control_board) (CCB) cân nhắc chi phí, rủi ro và tiến độ trước khi ủy quyền một thay đổi. Điều chỉnh kích thước hội đồng cho phù hợp: một cổng tự động nhẹ cho các thay đổi mã thường lệ, và một CCB liên chức năng chính thức cho các thay đổi chạm vào đường cơ sở, giao diện hoặc hành vi chịu quy định. Ghi lại từng quyết định và lý do đằng sau, và kết nối các quyết định cấu hình quan trọng với hồ sơ quyết định (chương 1.6) để lý do tồn tại.

### Duy trì kế toán trạng thái cấu hình

Giữ một bản ghi chính xác, truy vấn được về mọi hạng mục cấu hình: phiên bản hiện tại, nó thuộc đường cơ sở nào, và các yêu cầu thay đổi đã áp dụng cho nó. Kế toán trạng thái này là thứ cho phép bạn trả lời, vào bất kỳ lúc nào, một bản phát hành chứa gì và nó đến đó bằng cách nào. Hãy sinh bản ghi tự động từ các công cụ ghi nhận của bạn (quản lý phiên bản, đường ống, kho hiện vật) thay vì duy trì một bảng tính song song trôi khỏi thực tế. Bản ghi này là xương sống của khả năng truy vết từ yêu cầu đến thay đổi đến bản dựng đến triển khai.

### Tiến hành kiểm toán cấu hình

Xác minh hai điều theo lịch đều đặn. Một cuộc kiểm toán cấu hình chức năng xác nhận rằng cấu hình hoạt động đúng như các yêu cầu của nó quy định. Một cuộc kiểm toán cấu hình vật lý xác nhận rằng các hiện vật được giao khớp với cấu hình đã ghi lại: rằng bản dựng đến từ mã nguồn và phụ thuộc đã ghi lại và không chứa gì không được tính đến. Hãy tự động hóa càng nhiều càng tốt: [bản dựng tái tạo được](https://en.wikipedia.org/wiki/Reproducible_builds), tổng kiểm hiện vật, bảng kê vật liệu phần mềm (SBOM) và chứng thực nguồn gốc biến kiểm toán từ kiểm tra thủ công thành kiểm tra liên tục.

### Quản lý phát hành và phân phối như các sự kiện được kiểm soát

Hãy coi một bản phát hành là một đường cơ sở cụ thể, được xác định, được giao qua một quy trình lặp lại được. Đánh phiên bản các bản phát hành một cách tường minh, tạo ra một bản kê khai hoặc bảng kê vật liệu mô tả chính xác những gì được bao gồm, và ghi lại ánh xạ từ bản phát hành đến bản sửa đổi mã nguồn đến hiện vật đã triển khai. Ký và tính tổng kiểm các hiện vật đã phát hành để bất kỳ ai ở hạ nguồn cũng có thể xác minh tính toàn vẹn của chúng. Gắn quản lý phát hành vào đường ống phân phối (chương 8.1) để việc thăng cấp qua các môi trường tự nó được kiểm soát, ghi lại và đảo ngược được.

### Chọn và tích hợp công cụ SCM

Hãy dựa vào các công cụ tự động hóa việc xác định, kiểm soát, kế toán và kiểm toán thay vì chỉ dựa vào kỷ luật: quản lý phiên bản cho mã nguồn, kho hiện vật và ảnh cho nhị phân, một đường ống bất biến cho bản dựng, hạ tầng dưới dạng mã cho môi trường, và công cụ phụ thuộc cùng SBOM cho nguồn gốc. Kết nối chúng để một thay đổi đơn lẻ chảy truy vết được từ commit đến bản phát hành đã triển khai. Điều bạn nhắm đến là một bộ công cụ nơi bản ghi cấu hình là sản phẩm phụ của việc làm, không phải một việc văn thư riêng.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Hội đồng kiểm soát thay đổi chính thức | Ủy quyền mạnh và dấu vết kiểm toán; rủi ro được cân nhắc trước thay đổi | Thông lượng chậm hơn; chi phí nếu áp dụng cho thay đổi thường lệ |
| Cổng tự động nhẹ | Dòng chảy nhanh; chi phí thấp; mở rộng được cho nhiều thay đổi | Yếu hơn cho đường cơ sở rủi ro cao; ít cân nhắc hơn |
| Đường cơ sở bất biến nghiêm ngặt | Điểm tham chiếu tái tạo được, kiểm toán được | Cần kỷ luật và công cụ; ma sát nếu dùng quá mức |
| Kế toán trạng thái tự động | Bản ghi chính xác, luôn hiện hành; sẵn sàng kiểm toán | Đầu tư công cụ và tích hợp ban đầu |
| Bản ghi cấu hình thủ công | Dễ bắt đầu; không cần công cụ | Trôi khỏi thực tế; thất bại ở quy mô lớn và dưới kiểm toán |

Sự đánh đổi trung tâm là kiểm soát so với dòng chảy. Kiểm soát thay đổi nặng cho sự đảm bảo mạnh nhưng làm chậm phân phối. Kiểm soát nhẹ chảy nhanh nhưng làm yếu khả năng truy vết. Câu trả lời không phải là chọn một cách toàn cục; mà là phân tầng kiểm soát theo rủi ro: tự động hóa các thay đổi thường lệ qua các cổng nhanh, và dành các hội đồng chính thức cùng đường cơ sở bất biến cho các hạng mục nơi sự ủy quyền và khả năng kiểm toán thực sự quan trọng. Sự đánh đổi thứ hai là đầu tư công cụ ban đầu so với chi phí văn thư liên tục và rủi ro kiểm toán. Kế toán tự động tốn hơn để thiết lập và tốn ít hơn nhiều để sống cùng.

## Câu hỏi để thảo luận với đội của bạn

1. **Chính xác thì cái gì thuộc về danh sách hạng mục cấu hình của chúng ta, và ai sở hữu quyết định khi có thứ gì mới xuất hiện?** SCM chỉ hoạt động nếu danh sách các hạng mục được kiểm soát khớp với tập hợp những thứ thực sự quyết định hành vi, và trong một hệ thống lớn tập hợp đó lớn hơn hầu hết các đội nghĩ: mã nguồn, phụ thuộc, tập lệnh dựng, ảnh container, định nghĩa hạ tầng, lược đồ, cờ tính năng, và dữ liệu cấu hình âm thầm thay đổi những gì phần mềm làm. Nếu không ai sở hữu danh sách, nó lỗi thời, và hạng mục đã đánh sập bạn trên môi trường thực hóa ra là thứ duy nhất không ai nghĩ đến việc kiểm soát. Hãy mang bản kiểm kê hiện tại của bạn đến cuộc họp và tìm các hạng mục quyết định hành vi bị thiếu trong đó. Giao một chủ sở hữu chịu trách nhiệm (một người quản lý cấu hình hoặc một đội được nêu tên) để thêm một hạng mục mới là một quyết định có chủ đích, không phải tình cờ, vì SCM là việc của mọi người thì không phải việc của ai.

2. **Chúng ta có thể chứng minh một hiện vật đã triển khai đến từ mã nguồn và đường ống mà chúng ta nghĩ không, và bằng chứng đó có sống sót qua sự giả mạo không?** Khả năng tái tạo và truy vết là toàn bộ ý nghĩa của SCM, và phiên bản sắc bén của câu hỏi là liệu bạn có thể nối tệp nhị phân đang chạy về một commit và lần chạy dựng cụ thể bằng bằng chứng, không phải khẳng định. Trong một hệ thống chịu quy định hoặc giá trị cao, đây cũng là sự phòng thủ chuỗi cung ứng của bạn: chứng thực nguồn gốc có chữ ký, tổng kiểm hiện vật và bảng kê vật liệu phần mềm biến "chúng tôi khá chắc" thành thứ mà kiểm toán viên hay người ứng phó sự cố có thể xác minh. Hãy mang bản phát hành gần nhất của bạn và thử đi ngược từ hiện vật đã triển khai về thay đổi đã được phê duyệt. Nếu bất kỳ bước nào là một khẳng định thủ công thay vì một liên kết được ghi lại, xác minh được, đó là nơi kẻ tấn công hoặc một sai lầm trung thực có thể lọt thứ gì đó vào mà không bị chú ý, và đóng nó nghĩa là nối ký và nguồn gốc vào đường ống để bản ghi là sản phẩm phụ của việc phân phối.

3. **Hiện nay có ai có thể chỉnh sửa một bản phát hành tại chỗ không, và điều đó sẽ làm gì với khả năng tin cậy nó của chúng ta?** Một đường cơ sở chỉ hữu ích nếu nó bất biến: khoảnh khắc "bản phát hành" có thể bị chỉnh sửa sau sự việc, bạn không còn có thể tái tạo nó hay dựa vào nó như một tham chiếu, và mọi cuộc kiểm toán hạ nguồn trở thành khảo cổ. Thất bại kinh điển là cấu hình bị sửa trực tiếp trên môi trường thực hoặc một thẻ bị âm thầm di chuyển, chính là đường tắt có vẻ vô hại và khiến một bản phát hành không thể dựng lại sau này. Hãy mang câu trả lời trung thực đến cuộc họp: ai có quyền truy cập để thay đổi một đường cơ sở đã triển khai mà không qua quy trình thay đổi, và điều đó đã xảy ra chưa? Cách sửa là làm cho đường cơ sở thực sự bất biến và định tuyến mọi thay đổi qua đề xuất, đánh giá tác động, phê duyệt và xác minh, phân tầng độ nghiêm ngặt để các thay đổi thường lệ chảy qua các cổng tự động nhanh trong khi các thay đổi đường cơ sở và chịu quy định đến một hội đồng.

4. **Kế toán trạng thái cấu hình của chúng ta được sinh tự động từ các công cụ ghi nhận hay duy trì bằng tay, và nó đã trôi khỏi những gì thực sự được triển khai đến đâu?** Kế toán trạng thái là bản ghi cho phép bạn trả lời, vào bất kỳ lúc nào, một bản phát hành chứa gì và nó đến đó bằng cách nào, và trong một hệ thống lớn bản ghi đó chỉ đáng tin nếu nó rơi ra từ công việc thay vì được gõ vào một bảng tính song song. Lực kéo đối lập là một sổ đăng ký giữ tay có cảm giác rẻ để bắt đầu và linh hoạt, trong khi tự động hóa nó nghĩa là tích hợp quản lý phiên bản, đường ống và kho hiện vật để bản ghi trở thành sản phẩm phụ của phân phối. Hãy mang sổ đăng ký bạn dựa vào hôm nay, chọn ngẫu nhiên ba bản phát hành gần đây, và kiểm tra xem các phiên bản, đường cơ sở và yêu cầu thay đổi đã áp dụng được ghi lại có khớp với những gì công cụ nói đã phát hành không. Với một chương trình doanh nghiệp hoặc chính phủ, một bản ghi trạng thái lệch khỏi thực tế không phải là vấn đề gọn gàng, mà là một phát hiện kiểm toán đang chờ xảy ra, vì một kiểm toán viên bắt được một khoảng trống sẽ ngừng tin cả bản tường thuật và yêu cầu bạn dựng lại bằng tay.

5. **Kiểm soát thay đổi của chúng ta có được phân tầng theo rủi ro không, hay cùng một mức nghi thức chi phối mọi thay đổi bất kể nó chạm vào gì?** Kiểm soát và dòng chảy kéo ngược nhau: một hội đồng kiểm soát thay đổi chính thức cân nhắc chi phí, rủi ro và tiến độ trước khi ủy quyền một thay đổi, nhưng áp dụng nghi thức đó cho một chỉnh sửa mã thường lệ chỉ thêm độ trễ, trong khi đẩy một đường cơ sở dùng chung hoặc một luồng thanh toán chịu quy định qua một cổng tự động nhanh loại bỏ sự cân nhắc đúng ở nơi bạn cần. Các chế độ thất bại là đối xứng, sự nặng nề đồng loạt mà mọi người học cách đi vòng, hoặc sự lỏng lẻo đồng loạt để một thay đổi rủi ro cao lọt qua không được xem xét. Hãy mang một mẫu các thay đổi quý trước được sắp xếp theo thứ mỗi thay đổi chạm vào, và kiểm tra xem sự nghiêm ngặt nó nhận được có thực sự khớp với rủi ro của nó không. Trong bối cảnh chịu quy định hoặc khu vực công, hãy nêu tên những lớp hạng mục nào phải đến một hội đồng liên chức năng và những lớp nào có thể chảy qua các cổng tự động, và ghi lại sự phân tầng đó một cách tường minh, vì "chúng tôi dùng phán đoán" không phải là biện pháp kiểm soát mà một kiểm toán viên hay cơ quan giám sát có thể xác minh.

6. **Lần cuối cùng chúng ta chạy một cuộc kiểm toán cấu hình chức năng và vật lý là khi nào, và bao nhiêu bằng chứng sẽ là một bản ghi sống thay vì một sự dựng lại?** Một cuộc kiểm toán cấu hình chức năng xác nhận hệ thống hoạt động đúng như các yêu cầu của nó quy định, và một cuộc kiểm toán cấu hình vật lý xác nhận các hiện vật được giao khớp với cấu hình đã ghi lại và không chứa gì không được tính đến; bỏ qua chúng và bạn đang tin rằng các đường cơ sở và kế toán trạng thái của mình là trung thực mà không bao giờ kiểm tra. Căng thẳng là chi phí: kiểm toán thủ công chậm và đau đớn, đó chính là lý do các đội trì hoãn chúng, và lối thoát là tự động hóa các kiểm tra bằng bản dựng tái tạo được, tổng kiểm hiện vật, bảng kê vật liệu phần mềm và chứng thực nguồn gốc để việc xác minh trở thành liên tục. Hãy mang bản phát hành gần nhất của bạn và thử tạo ra ngay tại chỗ dấu vết từ yêu cầu đến thay đổi đến bản dựng đến triển khai và bằng chứng từ hiện vật về mã nguồn. Với các chương trình doanh nghiệp và chính phủ, dấu vết bằng chứng này là thứ mà chứng nhận và giám sát đòi hỏi, vì vậy câu hỏi trung thực là liệu cuộc kiểm toán ngày mai sẽ được trả lời từ các bản ghi bạn đã có hay từ một bài tập khảo cổ mà bạn không thể gánh.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy giữ SCM nhẹ nhưng có thật. Đặt mã nguồn, định nghĩa hạ tầng và dữ liệu cấu hình vào hệ thống quản lý phiên bản, và biến mỗi bản phát hành thành một bản dựng được gắn thẻ do một đường ống duy nhất tạo ra thay vì một hiện vật lắp ráp bằng tay. Bỏ qua hội đồng kiểm soát thay đổi và đường cơ sở chính thức, vốn là quá mức ở quy mô của bạn, nhưng đừng bao giờ để ai chỉnh sửa cấu hình trực tiếp trên môi trường thực, vì đường tắt đơn lẻ đó là thứ khiến một bản phát hành không thể tái tạo khi một khách hàng gặp lỗi vào thứ Ba tới.

**Doanh nghiệp nhỏ.** Không có người quản lý cấu hình và ngân sách eo hẹp, hãy dựa vào các công cụ cho bạn SCM gần như miễn phí: một nền tảng quản lý phiên bản lưu trữ, đường ống tích hợp sẵn của nó, và một kho hiện vật, để bản ghi cấu hình là sản phẩm phụ chứ không phải một công việc bạn phải bố trí nhân sự. Hãy mua năng lực này được nhúng trong các công cụ bạn đã trả tiền thay vì xây một quy trình riêng. Dành sự chú ý khan hiếm của bạn cho hai thói quen quan trọng nhất, các bản phát hành được gắn thẻ, tái tạo được và giữ cấu hình thay đổi hành vi tránh xa các chỉnh sửa thủ công trên môi trường thực.

**Doanh nghiệp lớn.** Vấn đề là nhất quán qua nhiều đội: một kế hoạch SCM dùng chung, một phân loại hạng mục cấu hình chung, kiểm soát thay đổi phân tầng, và kế toán trạng thái được sinh tự động từ quản lý phiên bản, kho hiện vật và đường ống. Hãy dành các hội đồng kiểm soát thay đổi chính thức và đường cơ sở bất biến cho nền tảng dùng chung và các luồng chịu quy định, để các thay đổi thường lệ chảy qua các cổng tự động, và chuẩn hóa nguồn gốc có chữ ký cùng SBOM để bản phát hành của bất kỳ đội nào cũng có thể được truy vết và bất kỳ kiểm toán viên nào cũng có thể truy vấn một bản ghi sống thay vì ủy quyền một cuộc dựng lại.

**Chính phủ.** Quy tắc mua sắm, tính minh bạch và trách nhiệm giải trình trước công chúng định hình quy trình. Hãy theo một kế hoạch SCM chính thức phù hợp với một tiêu chuẩn được công nhận như IEEE 828, lập đường cơ sở cho các hạng mục cấu hình tại các mốc hợp đồng, và định tuyến mọi thay đổi đối với một đường cơ sở được kiểm soát qua một hội đồng ghi lại tác động, quyết định và lý do. Yêu cầu các hiện vật được giao tái tạo được từ các đầu vào được kiểm soát, có tổng kiểm, và truy vết được từ đầu đến cuối từ yêu cầu đã phê duyệt đến bản dựng được giao, vì dấu vết bằng chứng có tài liệu đó chính là thứ mà chứng nhận, kiểm toán và giám sát công chúng đòi hỏi.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người giữ SCM nhẹ nhưng có thật: mã nguồn, định nghĩa hạ tầng và dữ liệu cấu hình đều nằm trong hệ thống quản lý phiên bản, và mỗi bản phát hành là một bản dựng được gắn thẻ, đánh phiên bản do cùng một đường ống tạo ra thay vì lắp ráp bằng tay. Khi một khách hàng báo một lỗi xuất hiện từ thứ Ba tuần trước, họ truy vết hiện vật đã triển khai về đúng commit trong vài phút thay vì đoán. Họ bỏ qua hội đồng kiểm soát thay đổi và đường cơ sở chính thức, vốn là quá mức ở quy mô của họ, nhưng họ từ chối để ai chỉnh sửa cấu hình trực tiếp trên môi trường thực, vì đường tắt đó là thứ khiến một bản phát hành không thể tái tạo sau này.

**Doanh nghiệp lớn.** Một công ty dịch vụ tài chính lớn đặt mọi hiện vật triển khai được, định nghĩa hạ tầng và dữ liệu cấu hình dưới kiểm soát cấu hình. Mỗi bản phát hành là một đường cơ sở bất biến, có phiên bản kèm một bảng kê vật liệu phần mềm được sinh ra, và mỗi hiện vật đã triển khai mang một chứng thực nguồn gốc có chữ ký nối nó với một bản sửa đổi mã nguồn và lần chạy đường ống cụ thể. Các thay đổi ứng dụng thường lệ chảy qua các cổng đường ống tự động, trong khi các thay đổi đối với đường cơ sở nền tảng dùng chung hoặc các luồng thanh toán chịu quy định đến một hội đồng kiểm soát thay đổi. Kế toán trạng thái được sinh tự động từ quản lý phiên bản, kho hiện vật và đường ống, nên kiểm toán viên truy vấn một bản ghi sống thay vì yêu cầu một sự dựng lại.

**Chính phủ.** Một chương trình quốc phòng theo một kế hoạch SCM chính thức phù hợp với IEEE 828. Các hạng mục cấu hình được liệt kê và lập đường cơ sở tại các mốc hợp đồng, và một hội đồng kiểm soát thay đổi ủy quyền mọi thay đổi đối với một đường cơ sở được kiểm soát, ghi lại tác động, quyết định và lý do. Các cuộc kiểm toán cấu hình chức năng xác nhận hệ thống được giao đáp ứng các yêu cầu đã chỉ định, và các cuộc kiểm toán cấu hình vật lý xác nhận các hiện vật được giao khớp chính xác với cấu hình đã ghi lại. Các bản phát hành tái tạo được từ các đầu vào được kiểm soát, có tổng kiểm, và truy vết được từ đầu đến cuối, từ yêu cầu đã phê duyệt qua yêu cầu thay đổi đến bản dựng được giao, đúng là dấu vết bằng chứng mà chứng nhận và giám sát đòi hỏi.

## Luận chứng kinh doanh: động lực, ROI và TCO

SCM tồn tại để kiểm soát rủi ro và chi phí suốt vòng đời của một hệ thống. Lợi tức đến từ khả năng tái tạo và truy vết: bạn có thể tạo lại bất kỳ bản phát hành nào, truy vết các lỗi về thay đổi gây ra chúng, và trả lời câu hỏi kiểm toán từ các bản ghi thay vì khảo cổ. Điều đó rút ngắn thời gian chẩn đoán sự cố, giảm chi phí và độ dài của kiểm toán, và ngăn loại thất bại đắt đỏ nơi không ai có thể nói điều gì đang chạy hay cách dựng lại nó.

Tổng chi phí sở hữu ưu ái tự động hóa. Bản ghi cấu hình thủ công rẻ để bắt đầu và đều đặn đắt để bảo trì, và chúng thất bại đúng lúc bạn cần chúng nhất, trong một sự cố hoặc một cuộc kiểm toán, vì chúng đã trôi khỏi thực tế. Việc xác định, kế toán và kiểm toán tự động tốn nhiều hơn lúc ban đầu nhưng biến bản ghi cấu hình thành một sản phẩm phụ gần như miễn phí của đường ống phân phối. Để thuyết phục ban lãnh đạo, hãy đóng khung SCM như biện pháp kiểm soát khiến các bản phát hành tái tạo được và các thay đổi kiểm toán được, và cân nhắc nó đối với chi phí của các bản phát hành không tái tạo được, kiểm toán kéo dài, và rủi ro tuân thủ của thay đổi không được kiểm soát.

## Phản mẫu và cạm bẫy

- **Cấu hình bằng kiến thức truyền miệng:** nội dung thực sự của một bản phát hành chỉ sống trong đầu một kỹ sư, không có trong bản ghi nào.
- **Đường cơ sở khả biến:** "bản phát hành" bị chỉnh sửa tại chỗ, nên nó không còn có thể tái tạo hay tin cậy như một tham chiếu.
- **Dữ liệu cấu hình không được kiểm soát:** mã được quản lý phiên bản nhưng cấu hình thay đổi hành vi của nó bị chỉnh sửa tùy tiện trên môi trường thực.
- **Sân khấu kiểm soát thay đổi:** một hội đồng đóng dấu mọi thứ, thêm độ trễ mà không thêm sự xem xét thực sự.
- **Kế toán trạng thái thủ công:** một bảng tính các phiên bản âm thầm lệch khỏi những gì thực sự được triển khai.
- **Bản dựng không tái tạo được:** các bản phát hành không thể dựng lại từ các đầu vào được kiểm soát, nên kiểm toán và dựng lại trở thành đoán mò.
- **Bản phát hành không truy vết được:** không có ánh xạ từ hiện vật đã triển khai về bản sửa đổi mã nguồn, yêu cầu thay đổi và phê duyệt.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** SCM tùy nghi và phản ứng. Chỉ mã nguồn được kiểm soát; các bản phát hành được lắp ráp bằng tay; không có đường cơ sở, không có bản ghi đáng tin về những gì được triển khai, và không có cách tái tạo một bản dựng trong quá khứ.
- **Mức 2 (Phát triển):** Các thực hành cơ bản tồn tại nhưng khác nhau theo đội. Một số hệ thống xác định hạng mục cấu hình và một quy trình thay đổi và đánh phiên bản bản phát hành của chúng, đường cơ sở có ở chỗ này chỗ kia, nhưng bản ghi một phần là thủ công và độ nghiêm ngặt của kiểm soát không nhất quán trong tổ chức.
- **Mức 3 (Chuẩn hóa):** Các thực hành được lập thành tài liệu và thực thi toàn tổ chức. Một phân loại hạng mục cấu hình chung, đường cơ sở bất biến, kiểm soát thay đổi phân tầng và kế toán trạng thái được thiết lập và phần lớn tự động; các bản phát hành tái tạo được và truy vết được, và kiểm toán được hỗ trợ bằng công cụ thay vì trí nhớ.
- **Mức 4 (Quản lý):** SCM được đo lường và kiểm soát bằng dữ liệu. Tỷ lệ tái tạo, độ bao phủ truy vết từ yêu cầu đến hiện vật đã triển khai, thời gian dẫn thay đổi qua từng tầng kiểm soát, các sự cố trôi dạt cấu hình và phát hiện kiểm toán được theo dõi so với đường cơ sở và mục tiêu. Sai lệch kích hoạt việc khắc phục, và mỗi quyết định đi hay không đi dựa trên bằng chứng này thay vì khẳng định.
- **Mức 5 (Điều phối):** SCM được cải tiến liên tục và tích hợp trong toàn tổ chức. Hoàn toàn tự động và được xác minh liên tục với bản dựng tái tạo được, SBOM, chứng thực nguồn gốc và kế toán trạng thái sống, quy trình được đan vào phân phối, bảo mật và kiểm toán, và nó thích ứng khi rủi ro và kết quả phân phối dịch chuyển, loại bỏ và điều chỉnh phạm vi các biện pháp kiểm soát dựa trên bằng chứng.

## Ý tưởng để thảo luận

- Hôm nay bạn có thể tái tạo chính xác bản phát hành cuối cùng của mình từ các đầu vào được kiểm soát không, và mất bao lâu?
- Hạng mục cấu hình nào quyết định hành vi nhưng thực sự không nằm dưới kiểm soát, đặc biệt là dữ liệu cấu hình và hạ tầng?
- Kiểm soát thay đổi của bạn được phân tầng theo rủi ro, hay nó thêm chi phí đồng loạt hoặc sự lỏng lẻo đồng loạt ở mọi nơi?
- Bản ghi cấu hình của bạn nằm ở đâu, và nó đã trôi khỏi những gì thực sự được triển khai đến đâu?
- Bạn có thể tạo ra bằng chứng nào trong một cuộc kiểm toán ngày mai, và bao nhiêu phần trong đó sẽ là dựng lại thay vì bản ghi?
- Bản dựng tái tạo được, SBOM và chứng thực nguồn gốc thay đổi những gì kiểm toán của bạn có thể xác minh tự động như thế nào?

## Những điểm cần ghi nhớ

- SCM kiểm soát toàn bộ cấu hình (mã, phụ thuộc, hạ tầng và dữ liệu cấu hình), không chỉ mã nguồn.
- Đường cơ sở là các điểm tham chiếu bất biến; thay đổi được ủy quyền và ghi lại đối chiếu với chúng, không bị ngăn chặn.
- Kế toán trạng thái phải cho phép bạn trả lời, vào bất kỳ lúc nào, một bản phát hành chứa gì và nó đến đó bằng cách nào.
- Kiểm toán xác minh rằng những gì được dựng và giao khớp với cấu hình đã ghi lại và các yêu cầu đã phê duyệt.
- Phân tầng kiểm soát theo rủi ro và tự động hóa xác định, kế toán và kiểm toán để bản ghi là sản phẩm phụ của phân phối.

## Tài liệu tham khảo và đọc thêm

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, lĩnh vực kiến thức Quản lý Cấu hình Phần mềm
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quy trình quản lý cấu hình)
- Jez Humble và David Farley, *Continuous Delivery*
- Bob Aiello và Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- Hướng dẫn của NIST về bảo mật chuỗi cung ứng phần mềm, bảng kê vật liệu phần mềm (SBOM) và nguồn gốc hiện vật
- CNCF và các tiêu chuẩn mở về nguồn gốc bản dựng và chứng thực (như các khung tham chiếu)
