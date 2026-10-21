# 3.1 Nền tảng kiến trúc

## Tổng quan và động lực

[Kiến trúc phần mềm](https://en.wikipedia.org/wiki/Software_architecture) là tập hợp các quyết định thiết kế quan trọng tốn kém để thay đổi: cấu trúc của các thành phần chính, các mối quan hệ giữa chúng, và các thuộc tính mà toàn bộ hệ thống phải thể hiện. Hãy coi nó là mô hình tinh thần chung cho phép nhiều người xây dựng một sản phẩm mạch lạc. Với một đội nhỏ, kiến trúc có thể sống trong vài cái đầu và tiến hóa dần theo thời gian. Trong một tổ chức lớn (hàng trăm kỹ sư, hàng chục đội, nhiều sản phẩm, nhiều năm lộ trình), kiến trúc trở thành thứ giữ cho mọi người được điều phối. Khi nó rõ ràng, các đội di chuyển độc lập mà không va chạm. Khi nó mơ hồ, mỗi phụ thuộc liên đội biến thành một cuộc thương lượng, và mỗi sự cố biến thành một dự án khảo cổ.

Với doanh nghiệp và chính phủ, những nguyên lý cơ bản còn quan trọng hơn, vì các hệ thống sống lâu, chịu quy định chặt chẽ và được chia sẻ giữa các bộ phận. Một hệ thống thuế, một nền tảng trợ cấp, một hồ sơ sức khỏe quốc gia, hay sổ cái lõi của một ngân hàng sẽ tồn tại lâu hơn sự nghiệp của những người xây dựng nó. Những quyết định bạn đưa ra hôm nay về độ liên kết, quyền sở hữu dữ liệu và [thuộc tính chất lượng](https://en.wikipedia.org/wiki/List_of_system_quality_attributes) ràng buộc những gì khả thi trong một thập kỷ hoặc hơn. Cơ quan quản lý và kiểm toán viên ngày càng mong đợi kiến trúc có tài liệu, có thể bảo vệ: bằng chứng rằng độ tin cậy, bảo mật, riêng tư và khả năng tiếp cận được thiết kế vào, không phải gắn thêm. Làm đúng các nguyên lý cơ bản không phải chuyện học thuật. Đó là sự khác biệt giữa một nền tảng thích ứng với các yêu cầu mới và một nền tảng phải xây lại từ đầu.

Chương này bao quát các nguyên lý cơ bản bền vững tồn tại lâu hơn mốt công nghệ: thuộc tính chất lượng (các "-ility"), yêu cầu có ý nghĩa kiến trúc, hàm thích nghi và kiến trúc tiến hóa, tài liệu nhẹ với [C4](https://en.wikipedia.org/wiki/C4_model) và arc42, và phân tích đánh đổi có cấu trúc. Đây là những công cụ cho phép một đội lớn suy luận về kiến trúc một cách có chủ đích thay vì tình cờ.

## Các nguyên tắc chính

- **Kiến trúc là về đánh đổi, không phải câu trả lời đúng.** Mọi quyết định quan trọng đánh đổi chất lượng này lấy chất lượng khác; công việc là thực hiện những đánh đổi đó một cách có chủ đích và minh bạch.
- **Thuộc tính chất lượng là yêu cầu.** Hiệu năng, tính sẵn sàng, bảo mật và khả năng bảo trì phải được đặc tả với cùng sự chặt chẽ như tính năng, nếu không chúng sẽ bị hy sinh dưới áp lực hạn chót.
- **Không phải yêu cầu nào cũng có ý nghĩa kiến trúc.** Tập trung sự chú ý thiết kế khan hiếm vào những yêu cầu định hình cấu trúc, khó thay đổi, hoặc mang rủi ro cao.
- **Kiến trúc phải có khả năng tiến hóa.** Thiết kế lớn trả trước thất bại vì kiến thức thấp nhất ở lúc bắt đầu; hãy thiết kế tăng dần và bảo vệ các thuộc tính then chốt bằng kiểm tra tự động.
- **Ghi lại quyết định, không chỉ sơ đồ.** Lý do đằng sau một lựa chọn (và các phương án bị loại) có giá trị hơn một bức tranh của kết quả.
- **Làm cho kiến trúc dễ đọc với những người không tạo ra nó.** Người mới vào, kiểm toán viên và người bảo trì tương lai phải có thể dựng lại ý định.
- **Trì hoãn những quyết định bạn có thể, quyết định những cái bạn phải.** Giữ các lựa chọn mở ở nơi thay đổi rẻ; chỉ cam kết sớm ở nơi cam kết muộn tốn kém.

## Khuyến nghị

### Đặc tả thuộc tính chất lượng dưới dạng kịch bản đo được

Những mục tiêu mơ hồ như "hệ thống nên nhanh" hay "sẵn sàng cao" không thể kiểm thử hay thực thi. Thay vào đó, hãy viết mỗi thuộc tính chất lượng thành một kịch bản cụ thể với tác nhân kích thích, bối cảnh và phản hồi đo được: "Khi số người dùng đồng thời đỉnh đạt 50.000, 95% yêu cầu tìm kiếm hoàn thành trong 300 ms." Bao quát các thuộc tính quan trọng cho miền của bạn: tính sẵn sàng, hiệu năng, khả năng mở rộng, bảo mật, khả năng bảo trì, khả năng quan sát, khả năng tiếp cận, tính khả chuyển và hiệu quả chi phí. Hãy xếp hạng chúng thành tiếng, vì bạn không thể tối đa hóa tất cả cùng lúc. Một hệ thống được điều chỉnh cho nhất quán tối đa sẽ không đồng thời sẵn sàng tối đa.

### Xác định các yêu cầu có ý nghĩa kiến trúc (ASR)

Hãy dành thời gian để tách ASR khỏi các yêu cầu thông thường. Một yêu cầu có ý nghĩa kiến trúc nếu nó chạm vào nhiều thành phần, tốn kém để đáp ứng, áp đặt một ràng buộc nghiêm ngặt, hoặc rủi ro về mặt kỹ thuật. Các yêu cầu quy định (nơi lưu trữ dữ liệu, lưu giữ, khả năng kiểm toán), các kịch bản tải cao, tích hợp với hệ thống ghi nhận cũ, và các ranh giới bảo mật cứng thường là ASR. Giữ một danh sách ngắn, sống của chúng, và truy vết các quyết định thiết kế lớn về danh sách đó, để người rà soát thấy vì sao kiến trúc trông như vậy.

### Áp dụng kiến trúc tiến hóa và hàm thích nghi

Hãy coi kiến trúc là thứ thay đổi từng bước theo các hướng được dẫn dắt, không phải một bản thiết kế cố định. Một **hàm thích nghi** là một bài kiểm thử tự động, khách quan rằng một đặc tính kiến trúc cụ thể vẫn đứng vững: một kiểm tra lúc dựng rằng không mô-đun nào nhập từ một tầng bị cấm, một kiểm thử hiệu năng làm hỏng đường ống nếu độ trễ p99 hồi quy, một lần quét bảo mật chặn các phụ thuộc có lỗ hổng đã biết, một bài kiểm thử xác nhận không dịch vụ nào giữ kết nối trực tiếp với cơ sở dữ liệu của dịch vụ khác. Hàm thích nghi biến ý định kiến trúc thành các lan can được thực thi liên tục: cách duy nhất để giữ ý định đó sống qua một đội lớn, luôn thay đổi.

### Lập tài liệu bằng C4 và arc42

Hãy dùng **mô hình C4** để mô tả cấu trúc ở bốn mức phóng to (Ngữ cảnh Hệ thống, Vật chứa, Thành phần và Mã) để mỗi đối tượng đọc mức phù hợp với họ và không sơ đồ đơn lẻ nào phải nói hết mọi thứ. Dùng **arc42** làm biểu mẫu cho phần tường thuật xung quanh: mục tiêu, ràng buộc, ngữ cảnh, chiến lược giải pháp, khối xây dựng, kịch bản lúc chạy, triển khai, mối quan tâm xuyên suốt, quyết định và rủi ro. Ghi lại từng quyết định riêng lẻ dưới dạng các **[Hồ sơ Quyết định Kiến trúc (ADR)](https://en.wikipedia.org/wiki/Architectural_decision)** ngắn: bối cảnh, quyết định, trạng thái và hệ quả, một tệp cho mỗi quyết định, được đánh phiên bản cùng với mã. Nếu bạn chỉ áp dụng một thói quen tài liệu, hãy làm nó là ADR: chúng hoàn vốn hơn bất cứ thứ gì khác cho các đội lớn.

### Tiến hành phân tích đánh đổi có cấu trúc và dẫn dắt thiết kế theo rủi ro

Với các hệ thống rủi ro cao, hãy dùng một phương pháp như **[Phương pháp Phân tích Đánh đổi Kiến trúc (ATAM)](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method)** để cân nhắc các kiến trúc ứng viên đối chiếu với các kịch bản thuộc tính chất lượng đã được ưu tiên. Nó làm lộ các điểm nhạy cảm (nơi một quyết định ảnh hưởng mạnh đến một thuộc tính) và các điểm đánh đổi (nơi nó ảnh hưởng đến nhiều thuộc tính). Với cách tiếp cận nhẹ hơn, hãy áp dụng **thiết kế dẫn dắt bởi rủi ro**: dành công sức thiết kế tương xứng với rủi ro. Các phần ít rủi ro, được hiểu rõ cần ít nghi thức. Các quyết định mới lạ, tác động lớn, hoặc không thể đảo ngược xứng đáng có bản mẫu, thử nghiệm và rà soát chính thức.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Kiến trúc nặng trả trước | Sự rõ ràng về điều phối; ít bất ngờ muộn trong các chương trình phạm vi cố định | Quyết định được đưa ra khi kiến thức thấp nhất; chậm; giòn trước thay đổi |
| Kiến trúc nổi lên / tiến hóa | Thích ứng với việc học; ít lãng phí hơn; hỗ trợ phân phối nhanh | Rủi ro trôi dạt nếu thiếu hàm thích nghi; cần kỷ luật kỹ thuật mạnh |
| Đánh giá chính thức kiểu ATAM | Chặt chẽ, có thể kiểm toán, làm lộ các xung đột ẩn | Tốn thời gian và chuyên môn; quá mức cho thay đổi nhỏ |
| ADR nhẹ + C4 | Rẻ, dễ đọc, tăng dần, mở rộng được cho nhiều đội | Chỉ tốt bằng kỷ luật giữ chúng cập nhật |

Căng thẳng trung tâm là giữa sự chắc chắn và khả năng thích ứng. Các chương trình chính phủ giá cố định và các hệ thống quan trọng về an toàn nghiêng về sự chặt chẽ trả trước và đánh giá chính thức nhiều hơn, vì chi phí của thay đổi muộn hay thất bại là khổng lồ. Các tổ chức sản phẩm di chuyển nhanh nghiêng về cách tiếp cận tiến hóa được bảo vệ bởi tự động hóa. Hầu hết các tổ chức lớn cần cả hai: quản trị nặng hơn cho các quyết định không thể đảo ngược, tác động cao và các mối quan tâm xuyên suốt, và thiết kế nhẹ hơn, nổi lên ở mọi nơi khác. Cả hai thái cực đều thất bại theo cách riêng: kiến trúc quá mức lãng phí nhiều năm và không giao gì, trong khi kiến trúc thiếu tạo ra một mớ rối không mở rộng hay kiểm toán được.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi hai thuộc tính chất lượng của bạn va chạm dưới tải, cái nào thắng, và bạn đã viết thứ tự ưu tiên đó ra chưa?** Mọi kiến trúc đều buộc phải đánh đổi: nhất quán tối đa làm suy yếu tính sẵn sàng, bảo mật chặt thêm độ trễ, lưu đệm quyết liệt chống lại khả năng kiểm toán. Trong một đội lớn, mối nguy là các nhóm khác nhau âm thầm giả định các ưu tiên khác nhau, nên một nhóm tối ưu thông lượng trong khi nhóm khác bảo vệ nhất quán nghiêm ngặt, và xung đột chỉ nổi lên trong một sự cố. Trong bối cảnh doanh nghiệp và chính phủ, cơ quan quản lý sẽ hỏi bạn bảo vệ thuộc tính nào và vì sao, nên thứ hạng phải tường minh và có thể bảo vệ thay vì truyền miệng. Hãy mang các kịch bản thuộc tính chất lượng của bạn và xếp hạng chúng thành tiếng với nhau, từng cặp một, cho đến khi thứ tự không còn mơ hồ. Sau đó mã hóa người thắng thành một hàm thích nghi để ưu tiên đứng vững dưới áp lực hạn chót thay vì xói mòn.

2. **Những quyết định gần đây nào của bạn là cửa một chiều, và chúng có nhận được sự xem xét nhiều hơn cửa hai chiều không?** Thiết kế dẫn dắt bởi rủi ro nói hãy dành công sức thiết kế tương xứng với mức độ khó đảo ngược của một quyết định, nhưng hầu hết các đội xem xét mọi thay đổi với nghi thức gần như nhau. Điều đó lãng phí sự chú ý vào các lựa chọn rẻ, đảo ngược được trong khi những lựa chọn không thể đảo ngược (một mô hình dữ liệu cố định vào một hồ sơ pháp lý, một hợp đồng API công khai, một kho dữ liệu cốt lõi) trượt qua với quá ít thách thức. Hãy lấy các quyết định quan trọng quý trước và phân loại theo khả năng đảo ngược, rồi hỏi liệu những cái không thể đảo ngược có nhận được bản mẫu, thử nghiệm hay rà soát chính thức không. Trong các hệ thống doanh nghiệp và chính phủ tồn tại lâu, chi phí của một cửa một chiều sai cộng dồn trong một thập kỷ, nên sự chặt chẽ thêm hoàn vốn nhiều lần. Hãy khớp trọng lượng quy trình của bạn với khả năng đảo ngược của quyết định, không phải kích thước của diff.

3. **Với quyết định rủi ro cao, khó đảo ngược tiếp theo của bạn, ai cần có mặt trong phòng, và bạn sẽ chấm điểm các phương án theo kịch bản nào?** Một cuộc rà soát đánh đổi có cấu trúc kiểu ATAM xứng đáng với chi phí của nó khi một quyết định không thể đảo ngược và chạm đến nhiều thuộc tính chất lượng cùng lúc, và sức mạnh của nó đến từ những người có mặt: phân phối, bảo mật, vận hành, và các chủ sở hữu chính sách hoặc kinh doanh cảm nhận hậu quả. Bỏ sót một tiếng nói như vậy và bạn khám phá ra xung đột sau khi xây dựng, như cách một lựa chọn lưu đệm có thể âm thầm phá vỡ một yêu cầu kiểm toán. Hãy mang các kịch bản thuộc tính chất lượng đã được ưu tiên làm thang chấm, và tìm các điểm nhạy cảm nơi một phương án làm một thuộc tính dao động mạnh và các điểm đánh đổi nơi nó di chuyển nhiều thuộc tính. Đầu ra bạn muốn là một ADR ngắn ghi lại các phương án bạn đã loại và vì sao, để lý do tồn tại lâu hơn những người đã đưa ra nó. Nếu dường như không quyết định sắp tới nào biện minh cho điều này, bản thân điều đó đáng kiểm tra, vì một chương trình lớn không có quyết định không thể đảo ngược nào ở chân trời thường là chưa nhìn đủ xa.

4. **Nếu một người mới vào hoặc một kiểm toán viên bên ngoài chỉ có kiến trúc bằng văn bản của bạn, họ có thể dựng lại vì sao hệ thống có hình dạng như vậy không, và lần cuối bạn kiểm tra điều đó là khi nào?** Kiến trúc sống trong vài cái đầu cấp cao là điểm lỗi duy nhất: khi những người đó chuyển đi, lý do đằng sau mọi quyết định khó đảo ngược đi cùng họ, và đội kế tiếp học lại qua các sự cố. Với một tổ chức lớn, khả năng đọc của kiến trúc (sơ đồ C4 khớp thực tế, một bản tường thuật arc42, ADR ghi lại các phương án bị loại) là thứ cho phép hàng chục đội suy luận về cùng một hệ thống mà không cần họp. Hãy mang một ADR gần đây và một sơ đồ hiện tại, trao cho ai đó không xây dựng thành phần, và xem họ đi được bao xa trước khi phải hỏi một người. Trong bối cảnh doanh nghiệp và chính phủ, kiểm toán viên sẽ làm đúng bài tập này, và tài liệu mô tả hệ thống năm ngoái còn tệ hơn không có vì nó đánh lừa chính những người phải chứng nhận. Hãy coi độ mới của bản ghi bằng văn bản là một thuộc tính đo được, và đặt một hàm thích nghi hoặc nhịp rà soát đằng sau việc giữ nó đúng.

5. **Những đặc tính kiến trúc nào của bạn hôm nay được bảo vệ bởi một hàm thích nghi tự động, và những đặc tính nào vẫn dựa vào việc mọi người nhớ quy tắc?** Ý định chỉ sống trong một trang wiki hay trí nhớ của người rà soát xói mòn ngay khoảnh khắc hạn chót đến, vì quy tắc phân tầng, ranh giới không-dùng-chung-cơ-sở-dữ-liệu và ngân sách độ trễ chính là những gì các đội cắt khi chịu áp lực. Trên một cơ sở mã lớn, thay đổi nhanh, ý định duy nhất sống sót là ý định mà một bản dựng thực thi, nên khoảng cách giữa các đặc tính bạn tuyên bố và những đặc tính bạn thực sự kiểm tra là rủi ro kiến trúc thực của bạn. Hãy liệt kê các đặc tính quan trọng, đánh dấu mỗi cái là được thực thi, rà soát thủ công, hoặc không được bảo vệ, và mang ba lần gần nhất một cuộc rà soát bắt được sự trôi dạt mà một hàm thích nghi lẽ ra đã bắt sớm hơn. Trong các hệ thống chịu quy định và công điều này quan trọng gấp đôi, vì cơ quan quản lý sẽ hỏi không phải bạn có định bảo vệ nơi lưu trữ dữ liệu hay khả năng kiểm toán không mà bạn chứng minh nó đứng vững liên tục thế nào, và một đường ống xanh là câu trả lời mạnh hơn nhiều so với một tài liệu chính sách. Hãy ưu tiên tự động hóa những đặc tính mà thất bại vừa có khả năng vừa tốn kém, và chấp nhận rằng một số sẽ ở lại thủ công.

6. **Khi bạn quyết định một yêu cầu có ý nghĩa kiến trúc hay không, ai đưa ra quyết định đó, và làm thế nào bạn giữ danh sách ASR khỏi trở thành tất cả hay không gì?** Giá trị của việc gọi tên các yêu cầu có ý nghĩa kiến trúc đến từ tính chọn lọc: coi mọi yêu cầu là quan trọng và thiết kế dừng lại, coi không yêu cầu nào là quan trọng và những yêu cầu cấu trúc, rủi ro, khó thay đổi trượt qua mà không được bảo vệ. Trong một đội lớn, cám dỗ là để từng nhóm tự quyết định cục bộ, điều tạo ra các ngưỡng không nhất quán và bất ngờ liên đội khi lựa chọn "nhỏ" của một nhóm ràng buộc cấu trúc của nhóm khác. Hãy mang danh sách ASR hiện tại của bạn, các tiêu chí bạn đã dùng (chạm vào nhiều thành phần, tốn kém để đáp ứng, ràng buộc nghiêm ngặt, rủi ro về mặt kỹ thuật), và vài yêu cầu ở ranh giới để kiểm tra ranh giới thành tiếng. Với doanh nghiệp và chính phủ, các yêu cầu quy định như nơi lưu trữ dữ liệu, lưu giữ và khả năng kiểm toán hầu như luôn quan trọng và không thể thương lượng, vì vậy hãy nêu tên ai sở hữu danh sách, nó được rà soát thế nào, và một quyết định thêm hoặc bỏ một ASR được ghi lại ra sao, vì một ASR không ai quản trị là một yêu cầu không ai bảo vệ dưới sự soi xét.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Giữ nghi thức gần bằng không và bản ghi gần đầy đủ. Bỏ qua các buổi hội thảo ATAM chính thức và biểu mẫu nặng nề, nhưng vẫn viết khoảng một chục ADR ngắn cho những lựa chọn sẽ đau đớn để gỡ (kho dữ liệu, khối đơn so với dịch vụ, nhà cung cấp xác thực) và ghim hai hoặc ba kịch bản thuộc tính chất lượng mà những khách hàng đầu tiên của bạn thực sự cảm nhận. Nguồn lực khan hiếm của bạn là sự chú ý của kỹ thuật, vì vậy chỉ bảo vệ những đặc tính mà thất bại sẽ đánh chìm bạn, như cô lập người thuê, và để mọi thứ khác nổi lên và rẻ để thay đổi.

**Doanh nghiệp nhỏ.** Không có kiến trúc sư riêng và ngân sách eo hẹp, hãy dựa vào những nguyên lý cơ bản gần như không tốn gì: gọi tên một nhúm thuộc tính chất lượng của bạn bằng các con số cụ thể, viết ADR cho bất cứ thứ gì bạn khó đảo ngược, và để nền tảng hay nhà cung cấp bạn chọn gánh các quyết định cấu trúc nặng. Ưu tiên mua một bộ công nghệ được hỗ trợ tốt hơn xây hạ tầng riêng, và coi kiến trúc có tài liệu của nhà cung cấp là một ràng buộc bạn thừa hưởng thay vì một ràng buộc bạn phải soạn từ đầu.

**Doanh nghiệp lớn.** Thách thức là sự mạch lạc qua nhiều đội và nhiều năm lộ trình, vì vậy hãy đầu tư vào bộ máy chung: một hội nhóm kiến trúc, một tập kịch bản thuộc tính chất lượng chung, ADR lưu cạnh mã, và hàm thích nghi trong CI thực thi các ranh giới mà không người rà soát đơn lẻ nào có thể canh gác ở quy mô lớn. Dùng phân tích đánh đổi có cấu trúc cho các quyết định không thể đảo ngược, xuyên suốt, giữ sơ đồ C4 làm bản đồ chung trong các buổi rà soát thiết kế, và quản trị danh sách ASR tập trung để các nhóm thôi đưa ra những lựa chọn hợp lý cục bộ mà va chạm toàn cục.

**Chính phủ.** Các hệ thống sống lâu, chịu quy định khiến kiến trúc có tài liệu, có thể bảo vệ trở thành yêu cầu mua sắm và trách nhiệm giải trình, không phải điều dễ chịu. Hãy coi nơi lưu trữ dữ liệu, lưu giữ, khả năng kiểm toán và khả năng tiếp cận là các yêu cầu có ý nghĩa kiến trúc được viết vào một mô tả arc42 mà kiểm toán viên có thể đọc trực tiếp, và tổ chức các buổi hội thảo đánh đổi nhẹ bao gồm các viên chức chính sách và bảo mật để các xung đột (như lưu đệm so với khả năng kiểm toán) nổi lên trên giấy trước khi có mã. Hãy giữ dấu vết lý do đủ đầy để một viên chức chịu trách nhiệm có thể cho thấy sự thẩm định thích đáng, và ưu tiên các kiến trúc có lối thoát rõ ràng hơn những kiến trúc khóa một cơ quan công vào một nhà cung cấp duy nhất trong một thập kỷ.

## Ví dụ

**Công ty khởi nghiệp.** Một đội SaaS giai đoạn hạt giống sáu người giữ kiến trúc của mình trong một tài liệu chung thay vì một quy trình chính thức, nhưng vẫn ghi lại các quyết định sẽ đau đớn để đảo ngược. Họ ghi khoảng một chục ADR (vì sao Postgres thay vì kho tài liệu, vì sao khối đơn mô-đun thay vì dịch vụ, vì sao họ chọn nhà cung cấp xác thực) và ghim hai kịch bản thuộc tính chất lượng thực sự quan trọng với khách hàng đầu tiên: "một lần đăng ký hoàn thành dưới hai giây" và "không khách hàng nào có thể đọc dữ liệu của người thuê khác." Khi họ tuyển kỹ sư thứ bảy và thứ tám, những ghi chú đó cho phép người mới phát hành ngay tuần đầu thay vì làm phiền mọi người để hỏi vì sao mọi thứ như vậy.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia hợp nhất mười hai hệ thống thanh toán khu vực nên lập một hội nhóm kiến trúc nhỏ. Hội nhóm xác định tám kịch bản thuộc tính chất lượng (bao gồm "xử lý 10.000 giao dịch mỗi giây không mất giao dịch nào" và "khôi phục một khu vực trong 15 phút"), nắm bắt khoảng bốn mươi ADR, và thực thi các hàm thích nghi trong CI ([tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration)): không dịch vụ nào được ghi vào cơ sở dữ liệu của miền khác, mọi lệnh gọi giữa các dịch vụ phải được truy vết, và bất kỳ phụ thuộc nào có [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (Lỗ hổng và Phơi nhiễm Thông dụng) nghiêm trọng làm hỏng bản dựng. Các sơ đồ ngữ cảnh và vật chứa C4 trở thành bản đồ chung trong mọi buổi rà soát thiết kế, và tranh chấp tích hợp liên đội giảm mạnh.

**Chính phủ.** Một cơ quan quốc gia hiện đại hóa nền tảng trợ cấp, và luật yêu cầu nó phải đảm bảo nơi lưu trữ dữ liệu, khả năng kiểm toán bảy năm và tuân thủ khả năng tiếp cận. Các kiến trúc sư của họ coi những điều này là ASR và viết chúng vào một mô tả arc42 mà kiểm toán viên rà soát trực tiếp. Họ tổ chức một buổi hội thảo ATAM nhẹ với các đội phân phối, bảo mật và viên chức chính sách để so sánh hai kiến trúc ứng viên, và phát hiện rằng chiến lược lưu đệm của thiết kế được ưa thích xung đột với yêu cầu kiểm toán. Bắt được sự đánh đổi đó trên giấy, trước một dòng mã, tiết kiệm nhiều tháng làm lại và cho bộ trưởng chịu trách nhiệm bằng chứng có tài liệu về sự thẩm định thích đáng.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của các nguyên lý cơ bản kiến trúc chủ yếu là chi phí được tránh, khiến nó dễ bị tài trợ thiếu và tốn kém nếu bỏ qua. Chi phí áp dụng khiêm tốn: thời gian của một nhúm kiến trúc sư có kinh nghiệm, vài buổi hội thảo, một biểu mẫu tài liệu, và một chút đầu tư CI vào các hàm thích nghi, thường là một phần trăm nhỏ một chữ số của ngân sách chương trình. Chi phí của việc *không* áp dụng đến sau, và với mức giá cao: làm lại khi một thuộc tính chất lượng không được đặc tả thất bại trên môi trường thực, tái nền tảng khẩn cấp khi một liên kết không có tài liệu chặn một thay đổi bắt buộc, các sự cố kéo dài vì không ai hiểu hệ thống, và các cuộc kiểm toán thất bại làm đình trệ phân phối hoặc kích hoạt tiền phạt.

Với ban lãnh đạo, hãy đóng khung lập luận quanh tính tùy chọn và rủi ro. Nền tảng kiến trúc tốt hạ thấp chi phí của thay đổi trong tương lai (một đòn bẩy trực tiếp lên tốc độ phân phối và tổng chi phí sở hữu qua vòng đời hệ thống cả thập kỷ), giảm tần suất và thời gian của các sự cố nghiêm trọng, và tạo ra dấu vết tài liệu mà cơ quan quản lý và kiểm toán viên nay đòi hỏi. Riêng thói quen ADR đã tự hoàn vốn lần đầu tiên một ban lãnh đạo mới hỏi "vì sao chúng ta xây nó như thế này?" và nhận được câu trả lời trong vài phút thay vì một cuộc điều tra pháp y. Hãy đặt con số lên nó khi có thể: cân nhắc chi phí của một lần tái kiến trúc lớn được tránh, hoặc một cuộc kiểm toán thất bại được tránh, đối chiếu với chi phí liên tục nhỏ của các thực hành.

## Phản mẫu và cạm bẫy

- **Kiến trúc tháp ngà.** Các kiến trúc sư tạo ra sơ đồ nhưng không bao giờ chạm vào mã hoặc nói chuyện với các đội phân phối; thiết kế của họ bị phớt lờ hoặc không xây được.
- **Thuộc tính chất lượng như tính từ.** "Mở rộng được, bảo mật, đáng tin cậy" không có con số, không có kịch bản, và do đó không có cách kiểm chứng hay đánh đổi.
- **Thiết kế lớn trả trước.** Cam kết mọi chi tiết trước dòng mã đầu tiên, khóa chặt các quyết định khi hiểu biết yếu nhất.
- **Tài liệu nói dối.** Sơ đồ mô tả hệ thống năm ngoái; tệ hơn không có vì chúng gây hiểu lầm.
- **Thiết kế theo lý lịch.** Chọn công nghệ để xây dựng sự nghiệp thay vì đáp ứng ASR.
- **Mạ vàng.** Thiết kế cho quy mô, linh hoạt hay tính tổng quát mà yêu cầu chưa bao giờ đòi hỏi, thêm chi phí và độ phức tạp vĩnh viễn.
- **Không có lan can kiến trúc.** Dựa vào thiện chí thay vì hàm thích nghi để bảo toàn cấu trúc qua một đội lớn.

## Mô hình trưởng thành

- **Mức 1: Khởi đầu.** Kiến trúc ngầm hiểu và sống trong đầu cá nhân. Không có thuộc tính chất lượng được lập thành tài liệu, không ADR, không sơ đồ chung. Cấu trúc được khám phá trong các sự cố, và mọi phụ thuộc liên đội được thương lượng lại từ đầu.
- **Mức 2: Phát triển.** Một số đội ghi lại các quyết định sẽ đau để đảo ngược và phác thảo các sơ đồ chính, nhưng thực hành không nhất quán: một nhóm giữ ADR trong khi nhóm khác không giữ gì, thuộc tính chất lượng được gọi tên như tính từ thay vì kịch bản đo được, và tài liệu trôi khỏi thực tế giữa các dự án.
- **Mức 3: Chuẩn hóa.** Kịch bản thuộc tính chất lượng và yêu cầu có ý nghĩa kiến trúc được đặc tả và ưu tiên theo một tiêu chuẩn toàn tổ chức có tài liệu. ADR là thường lệ và lưu cạnh mã, tài liệu C4 và arc42 được duy trì theo một biểu mẫu chung, và các cuộc rà soát đánh đổi có cấu trúc được yêu cầu cho các quyết định quan trọng ở mọi đội.
- **Mức 4: Quản lý.** Kiến trúc được đo theo các đường cơ sở thay vì khẳng định. Các hàm thích nghi trong CI báo cáo về các đặc tính như độ trễ p99, vi phạm phân tầng, lệnh gọi không được truy vết và phụ thuộc có lỗ hổng; độ bao phủ ADR và độ mới của tài liệu được theo dõi như các chỉ số; các cuộc rà soát đánh đổi chấm điểm các phương án theo các kịch bản đã ưu tiên; và sự trôi dạt so với các đường cơ sở đã thống nhất kích hoạt một phản ứng xác định thay vì một bất ngờ. Kiểm toán viên có thể dựa vào bằng chứng đo được thay vì chỉ tường thuật.
- **Mức 5: Điều phối.** Kiến trúc tiến hóa liên tục và thích ứng trong toàn tổ chức. Dữ liệu hàm thích nghi và sự cố phản hồi vào đặc tính nào quan trọng và công sức thiết kế đi đâu; danh sách ASR, ưu tiên thuộc tính chất lượng và lan can được điều chỉnh phạm vi khi các yêu cầu bắt buộc và rủi ro dịch chuyển; và thực hành được tích hợp với phân phối, bảo mật và hoạch định rủi ro để nền tảng thích ứng với yêu cầu mới thay vì bị xây lại từ đầu.

## Ý tưởng để thảo luận

1. Ba thuộc tính chất lượng nào thực sự không thể thương lượng cho hệ thống quan trọng nhất của bạn, và bạn có thể nêu mỗi cái thành một kịch bản đo được hôm nay không?
2. Làm thế nào bạn quyết định khi nào một quyết định có ý nghĩa kiến trúc đủ để cần một ADR so với cứ thế làm?
3. Hàm thích nghi sẽ bắt sự trôi dạt ở đâu mà việc đánh giá mã hiện tại của bạn bỏ sót?
4. Tổ chức của bạn đang kiến trúc quá mức hay kiến trúc thiếu, và bằng chứng nào cho bạn biết?
5. Ai chịu trách nhiệm về kiến trúc trong cấu trúc đội của các đội, và làm sao bạn tránh được cả tháp ngà lẫn vô chính phủ hoàn toàn?
6. Một kiểm toán viên bên ngoài sẽ dựng lại ý định của kiến trúc bạn từ những gì được viết ra hôm nay như thế nào?

## Những điểm cần ghi nhớ

- Kiến trúc là tập hợp các quyết định đắt để đảo ngược; hãy thực hiện những đánh đổi đó một cách có chủ đích và ghi lại chúng.
- Đặc tả thuộc tính chất lượng dưới dạng kịch bản đo được và xác định các yêu cầu có ý nghĩa kiến trúc định hình cấu trúc.
- Thiết kế tăng dần và bảo vệ các đặc tính kiến trúc then chốt bằng hàm thích nghi tự động.
- Lập tài liệu nhẹ nhưng trung thực bằng sơ đồ C4, bản tường thuật arc42 và ADR cho từng quyết định lưu cạnh mã.
- Khớp sự chặt chẽ với rủi ro: phân tích nặng cho các quyết định không thể đảo ngược, tác động cao; quy trình nhẹ ở mọi nơi khác.
- Luận chứng kinh doanh là việc làm lại được tránh, sự cố ngắn hơn, thay đổi tương lai nhanh hơn, và bằng chứng sẵn sàng kiểm toán.

## Tài liệu tham khảo và đọc thêm

- Len Bass, Paul Clements và Rick Kazman, *Software Architecture in Practice*
- Neal Ford, Rebecca Parsons và Patrick Kua, *Building Evolutionary Architectures*
- Simon Brown, *Software Architecture for Developers* (và mô hình C4)
- Mark Richards và Neal Ford, *Fundamentals of Software Architecture*
- George Fairbanks, *Just Enough Software Architecture: A Risk-Driven Approach*
- Michael Nygard, "Documenting Architecture Decisions" (mẫu ADR)
- Gernot Starke và Peter Hruschka, biểu mẫu tài liệu *arc42*
- Paul Clements và cộng sự, *Evaluating Software Architectures: Methods and Case Studies* (ATAM)
- ISO/IEC 25010, *Systems and software quality models*
