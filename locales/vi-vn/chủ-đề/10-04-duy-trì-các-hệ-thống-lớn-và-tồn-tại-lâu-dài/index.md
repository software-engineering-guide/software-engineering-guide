# 10.4 Duy trì các hệ thống lớn và tồn tại lâu dài

## Tổng quan và động lực

Hầu hết các bài viết về kỹ thuật phần mềm nói về xây thứ mới. Nhưng hầu hết phần mềm quan trọng của thế giới là cũ, lớn, và vẫn đang chạy: hệ thống thuế, chi trả trợ cấp, kiểm soát không lưu, ngân hàng lõi, điều khiển công nghiệp, và hạ tầng của đời sống hằng ngày. Những hệ thống này thường xuyên chạy mười, hai mươi, hay ba mươi năm. Đó là lâu hơn nhiều so với nhiệm kỳ của bất kỳ ai đã xây chúng, và thường lâu hơn các công ty và ngôn ngữ đã tạo ra chúng. Duy trì những hệ thống như vậy nghĩa là giữ chúng đáng tin cậy, an toàn, được hiểu, và có khả năng thay đổi, qua nhiều thập kỷ và nhiều thế hệ nhân viên. Đó là một trong những kỷ luật khó nhất và ít hào nhoáng nhất của lĩnh vực, và là nơi các doanh nghiệp lớn và chính phủ gánh gánh nặng nhất.

Vì sao điều này quan trọng hơn với các tổ chức lớn? Tính liên tục của nghĩa vụ. Một công ty khởi nghiệp có thể viết lại hoặc bỏ phần mềm của mình. Một chính phủ quốc gia không thể ngừng trả lương hưu trong khi tái cấu trúc. Doanh nghiệp và cơ quan sở hữu những hệ thống mà thất bại có hậu quả đo bằng sinh kế, an toàn, hay lòng tin công chúng. Và họ sở hữu nhiều hệ thống cùng lúc, do những người vào và rời đi qua nhiều thập kỷ vận hành. Các mối đe dọa trung tâm không hề kỳ lạ. Đó là sự xói mòn chậm của những người hiểu hệ thống ([hệ số xe buýt](https://en.wikipedia.org/wiki/Bus_factor), bao nhiêu ít người phải rời đi trước khi tri thức về một hệ thống bị mất), sự chồng chất tri thức không có tài liệu trong vài cái đầu, sự mục rữa của ngăn xếp công nghệ về phía [hết vòng đời](https://en.wikipedia.org/wiki/End-of-life_(product)), và sự tê liệt xuất hiện khi một hệ thống trở nên quá trọng yếu để chạm vào và quá ít được hiểu để thay đổi an toàn.

Chương này nói về quản gia: công việc có chủ đích, kém hào nhoáng giúp một hệ thống sống lâu hơn tác giả của nó một cách êm đẹp. Nó bao quát tính liên tục quyền sở hữu và giảm thiểu hệ số xe buýt, [ngừng hỗ trợ](https://en.wikipedia.org/wiki/Deprecation) có kế hoạch và khai tử, chuyển giao tri thức, những thách thức đặc thù của hệ thống hàng thập kỷ, và hành động cân bằng liên tục giữa đổi mới và giữ sự ổn định mà công dân và khách hàng phụ thuộc.

## Các nguyên tắc chính

- **Mọi hệ thống trọng yếu cần một chủ sở hữu, luôn luôn.** Quyền sở hữu là sự phân công liên tục, không phải ký ức về ai đã viết nó.
- **Tri thức nằm trong một cái đầu là rủi ro, không phải tài sản.** Thể chế hóa sự hiểu biết trước khi người đó rời đi.
- **Nhàm chán là một tính năng.** Với hệ thống trọng yếu tồn tại lâu dài, sự ổn định và khả đoán thường vượt trên sự mới lạ.
- **Lên kế hoạch cho kết thúc ngay từ đầu.** Mọi hệ thống sẽ bị loại bỏ hoặc thay thế; hãy thiết kế và lập tài liệu cho ngày đó.
- **Thay đổi là cách bạn giữ an toàn.** Một hệ thống quá đáng sợ để chạm vào đã đang thất bại; khả năng thay đổi là đặc tính sống còn.
- **Tính liên tục sống lâu hơn cá nhân.** Thiết kế đội, tài liệu và quy trình sao cho không sự ra đi đơn lẻ nào là khủng hoảng.
- **Lòng tin là sản phẩm thật.** Với hệ thống hướng công dân và khách hàng, độ tin cậy và sự công bằng được duy trì theo thời gian là sứ mệnh.

## Khuyến nghị

### Thiết lập quản gia và tính liên tục quyền sở hữu

Hãy giao quyền sở hữu tường minh, hiện hành cho mọi hệ thống quan trọng. Sở hữu ở cấp đội, không phải cấp cá nhân, để quyền sở hữu sống sót qua sự ra đi. Duy trì [danh mục dịch vụ](https://en.wikipedia.org/wiki/Service_catalog) ghi lại, với mỗi hệ thống, ai sở hữu nó, nó làm gì, nó phụ thuộc vào gì, và nó trọng yếu đến mức nào. Xem xét quyền sở hữu đều đặn, và đừng bao giờ để một hệ thống thành mồ côi. Một hệ thống trọng yếu không chủ là tình huống khẩn cấp đang chờ xảy ra. Khi các đội tái tổ chức, hãy chuyển giao quyền sở hữu có chủ đích, bằng bàn giao, không phải bằng giả định. Với các hệ thống tồn tại lâu dài trọng yếu nhất, hãy bảo đảm quyền sở hữu gồm không chỉ vận hành mà cả khả năng hiểu và thay đổi hệ thống, để quản gia không suy thoái thành trông nom đơn thuần.

### Giảm thiểu hệ số xe buýt và rủi ro người then chốt

Hãy chủ động đo và giảm sự tập trung tri thức. Nếu chỉ một người triển khai, gỡ lỗi hay thay đổi được một hệ thống, đó là [điểm đơn thất bại](https://en.wikipedia.org/wiki/Single_point_of_failure) thật như bất kỳ phần cứng nào. Giảm nó qua lập trình cặp và luân phiên, rà soát mã bắt buộc, trực ca chung, và quy tắc có chủ đích rằng không tác vụ trọng yếu nào có đúng một người đủ năng lực. Đào tạo chéo để ít nhất hai (tốt hơn ba) người thực hiện được mỗi chức năng thiết yếu. Coi sự ra đi của người then chốt là sự kiện có thể thấy trước mà bạn chuẩn bị liên tục, không phải cú sốc bạn hấp thụ. Tài liệu có giúp. Nhưng tri thức làm việc lan rộng khắp đội qua thực hành thực sự bền vững hơn nhiều so với tài liệu không ai thực hành.

### Thể chế hóa chuyển giao tri thức

Hãy nắm bắt tri thức mà nếu không sẽ ra đi cùng con người. Tập trung trước vào tri thức khó dựng lại: vì sao các quyết định được đưa ra, phương án nào bị loại và vì sao, các cạnh sắc và các mẹo trọng yếu mà phần còn lại của hệ thống lặng lẽ dựa vào ở đâu, và hệ thống hành xử thế nào dưới căng thẳng. Dùng hồ sơ quyết định kiến trúc để bảo tồn lập luận đằng sau các lựa chọn, không chỉ chính các lựa chọn. Giữ [sổ tay vận hành](https://en.wikipedia.org/wiki/Runbook) và tài liệu vận hành gần hệ thống, và thực hành chúng đều đặn để chúng luôn đúng. Xây đường làm quen đưa người quản gia mới đến năng lực thực sự. Coi sự ra đi là sự kiện chuyển giao tri thức với thời gian bàn giao thật. Hãy nhớ rằng [tri thức ngầm](https://en.wikipedia.org/wiki/Tacit_knowledge), cảm giác về một hệ thống, chuyển giao chủ yếu qua làm cùng với người có nó, nên hãy cho người quản gia ra đi và đến chồng lấn nhau nơi có thể.

### Quản lý ngừng hỗ trợ, khai tử và hết vòng đời

Hãy lên kế hoạch kết thúc có chủ đích. Khi bạn quyết định loại bỏ hoặc thay thế một hệ thống, hãy coi việc khai tử là một dự án riêng: xác định mọi bên tiêu thụ và phụ thuộc, cung cấp đường di chuyển và lịch trình thực tế, truyền đạt rõ ràng và lặp lại, và hỗ trợ các bên tiêu thụ qua quá trình chuyển đổi. Tránh cái bẫy chạy hệ thống cũ và mới song song mãi mãi vì không ai làm công việc khó là tắt cái cũ. Giao trách nhiệm tường minh cho việc hoàn tất tháo dỡ. Bảo tồn dữ liệu, hồ sơ, và khả năng trả lời câu hỏi về hệ thống đã loại bỏ rất lâu sau khi nó ngừng chạy, đặc biệt nơi áp dụng quy tắc lưu giữ pháp lý. Một cuộc khai tử làm tệ để lại các hệ thống xác sống không được bảo trì nhưng vẫn được dựa vào: điều tệ nhất trong mọi thế giới.

### Duy trì hệ thống qua nhiều thập kỷ

Với hệ thống phải chạy hai mươi hay ba mươi năm, hãy lên kế hoạch sống lâu hơn mọi thứ: đội ban đầu, nhà cung cấp, hệ sinh thái ngôn ngữ và phần cứng. Ưu tiên [tiêu chuẩn mở](https://en.wikipedia.org/wiki/Open_standard) và giao diện có tài liệu hơn hộp đen độc quyền, để người bảo trì tương lai có cơ hội. Mô-đun hóa, để các phần được thay từng cái một thay vì qua [viết lại](https://en.wikipedia.org/wiki/Rewrite_(programming)) được ăn cả ngã về không quá rủi ro để từng thử. Giữ hệ thống được bảo trì liên tục. Một hệ thống được giữ cập nhật theo bước nhỏ vẫn bền vững. Một hệ thống bị đóng băng "vì nó chạy được" lặng lẽ trở nên không bảo trì được khi ngăn xếp của nó hết hỗ trợ. Cũng giữ kỹ năng vận hành nó: với công nghệ thực sự cũ, hãy cố ý đào tạo người kế nhiệm thay vì hy vọng chuyên gia cuối cùng không bao giờ nghỉ hưu.

### Cân bằng đổi mới với ổn định và lòng tin

Hãy phân biệt những phần của tài sản nơi sự mới lạ tạo giá trị với những phần nơi sự ổn định là giá trị. Hệ thống lõi mà công dân và khách hàng phụ thuộc hằng ngày thường thưởng cho độ tin cậy, tương thích ngược và thay đổi thận trọng hơn là viết lại thú vị. Đầu tư đổi mới ở rìa (kênh mới, tính năng mới, giao diện mới) trong khi giữ lõi bền vững ổn định và được hiểu rõ. Hãy thay đổi lõi, đúng, nhưng theo những bước nhỏ, đảo ngược được, kiểm thử tốt thay vì những bước nhảy anh hùng. Mục tiêu là một hệ thống vừa đáng tin cậy vừa có khả năng tiến hóa: không bao giờ đông cứng đến mức [mục rữa](https://en.wikipedia.org/wiki/Software_rot), không bao giờ khuấy động đến mức trở nên không đáng tin.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Giữ và bảo trì hệ thống cũ | Bảo tồn tri thức thể chế; ít gián đoạn; độ tin cậy đã chứng minh | Ngăn xếp già; kỹ năng khan hiếm; rủi ro tăng nếu không bảo trì |
| Viết lại đại bùng nổ | Ngăn xếp mới; rũ bỏ cặn tích lũy | Tỷ lệ thất bại rất cao; mất tri thức trường hợp biên khó giành được |
| Hiện đại hóa gia tăng | Giảm rủi ro liên tục; tiếp tục chạy | Chậm; đòi tài trợ và kỷ luật bền vững |
| Chuyển giao nặng tài liệu | Bản ghi tường minh, tìm kiếm được | Mục rữa nếu không bảo trì; bỏ sót tri thức ngầm |
| Chuyển giao dựa vào con người (lập trình cặp/luân phiên) | Tri thức làm việc bền vững; đội có khả năng phục hồi | Tốn năng suất hiện tại; cần lên lịch có chủ đích |
| Đóng băng lõi trọng yếu | Ổn định tối đa ngắn hạn | Ngăn xếp già thành không bảo trì được; ngày càng quá đáng sợ để chạm vào |

Đánh đổi định nghĩa là ổn định so với tiến hóa, và cả hai cách giải quyết ngây thơ đều thất bại. Đóng băng một hệ thống trọng yếu để bảo vệ nó, và bạn bảo đảm cuối cùng nó trở nên không bảo trì được và không an toàn. Viết lại toàn bộ để hiện đại hóa, và bạn mời gọi tỷ lệ thất bại cao nổi tiếng của các cuộc thay thế đại bùng nổ, và bạn vứt bỏ hàng thập kỷ tri thức trường hợp biên được mã hóa mà không ai nhớ là có đó. Con đường bền vững là thay đổi liên tục, gia tăng: giữ hệ thống sống và di chuyển theo bước nhỏ, để nó không bao giờ hết hỗ trợ và không bao giờ cần một bước nhảy đáng sợ. Chuyển giao tri thức là đánh đổi tương tự, giữa sự dễ dàng của tài liệu và độ bền của trải nghiệm sống. Câu trả lời là cả hai: tri thức sống, do đội nắm giữ làm xương sống, và tài liệu làm tham chiếu.

## Câu hỏi để thảo luận với đội của bạn

1. **Hệ thống trọng yếu nào của bạn hiện không có đội chủ sở hữu hiện hành, được nêu tên?** Quyền sở hữu là sự phân công liên tục, không phải ký ức về ai viết mã, và một hệ thống trọng yếu không chủ là tình huống khẩn cấp đang chờ xảy ra, chỉ được chú ý khi nó hỏng. Hãy đi qua danh mục dịch vụ của bạn (hoặc xây một cái) và kiểm tra mỗi hệ thống ghi ai sở hữu nó, nó phụ thuộc vào gì, và nó trọng yếu đến đâu. Hãy mang bằng chứng: chọn ba hệ thống quan trọng và thử nêu tên đội chịu trách nhiệm và lần cuối quyền sở hữu được xem xét. Nơi một hệ thống mồ côi, hoặc nơi một đợt tái tổ chức lặng lẽ bỏ rơi nó, hãy giao quyền sở hữu có chủ đích với bàn giao thật thay vì giả định. Bảo đảm quyền sở hữu gồm khả năng hiểu và thay đổi hệ thống, để quản gia không suy thoái thành trông nom đơn thuần.

2. **Khi bạn thay thế một hệ thống, ai chịu trách nhiệm thực sự tắt cái cũ?** Chạy song song vĩnh cửu là thất bại phổ biến và tốn kém: hệ thống cũ và mới chạy cạnh nhau vô hạn vì không ai sở hữu việc tắt, để bạn bảo trì hai hệ thống mà không nhận được sự an toàn của cái nào. Hãy coi mỗi cuộc khai tử là dự án được quản lý với trách nhiệm có tên cho việc hoàn tất tháo dỡ, danh sách bên tiêu thụ đã lập bản đồ, đường di chuyển, và lịch trình thực tế. Hãy mang bằng chứng: hôm nay trong tài sản của bạn còn bao nhiêu lần chạy song song "tạm thời" hay hệ thống loại bỏ dở vẫn hút bảo trì? Bảo tồn dữ liệu và hồ sơ để đáp ứng quy tắc lưu giữ pháp lý rất lâu sau khi hệ thống ngừng chạy, nhưng đừng để lưu giữ thành cái cớ không bao giờ hoàn tất. Một cuộc khai tử làm tệ để lại hệ thống xác sống không được bảo trì nhưng vẫn được dựa vào, điều tệ nhất trong mọi thế giới.

3. **Kỹ năng nào cho hệ thống tồn tại lâu dài của bạn mà thị trường lao động sẽ thôi cung cấp, và kế hoạch kế nhiệm của bạn là gì?** Hệ thống chạy hai mươi hay ba mươi năm sống lâu hơn hệ sinh thái ngôn ngữ, nhà cung cấp, và sự nghiệp của những người hiểu ngăn xếp cũ, và thị trường sẽ không đáng tin cậy trao cho bạn người thay thế. Hãy giảm hệ số xe buýt có chủ đích để không chức năng trọng yếu nào có đúng một người đủ năng lực, và đào tạo chéo để ít nhất hai, tốt hơn ba, người thực hiện được mỗi tác vụ thiết yếu. Hãy mang bằng chứng: với mỗi hệ thống trọng yếu già, đếm bao nhiêu người thay đổi nó an toàn được và những người am hiểu nhất sắp nghỉ hưu đến đâu. Câu trả lời nên thúc đẩy đào tạo người kế nhiệm có chủ đích và sự chồng lấn thực giữa người quản gia ra đi và đến, vì tri thức ngầm (cảm giác về một hệ thống) chuyển giao chủ yếu bằng làm cùng người có nó. Tài liệu là tham chiếu; tri thức sống, do đội nắm giữ là xương sống.

4. **Lần cuối bạn thay đổi hệ thống tồn tại lâu dài trọng yếu nhất của mình là khi nào, và còn ai dám làm không?** Một hệ thống không ai chạm vào một năm không ổn định, nó đang trôi vào cái bẫy "quá đáng sợ để chạm vào", nơi mọi thay đổi bị sợ nên ngăn xếp lặng lẽ hết hỗ trợ. Với tổ chức lớn điều này quan trọng vì tê liệt cộng dồn: đóng băng càng lâu, tri thức càng phai và thay đổi không thể tránh cuối cùng càng rủi ro. Hãy mang bằng chứng: với mỗi hệ thống trọng yếu, ngày thay đổi có chủ đích gần nhất, kích thước của thay đổi nhỏ nhất mà ai đó sẽ thử hôm nay, và liệu một bản vá phụ thuộc hay bảo mật thường lệ có phát hành được tuần này mà không cần anh hùng. Cân nhắc đối lập là thật, vì thay đổi cũng đưa vào rủi ro, nên mục tiêu không phải khuấy động mà là nhịp đều đặn các bước nhỏ, đảo ngược được, kiểm thử tốt. Trong tài sản doanh nghiệp và chính phủ, nơi một lõi bị đóng băng có thể nằm dưới dịch vụ công dân cả thập kỷ, hãy coi "chúng tôi không bao giờ đổi nó" là cờ đỏ thay vì sự trấn an, và tài trợ bảo trì liên tục giữ cho lựa chọn thay đổi còn sống.

5. **Bao nhiêu tài sản của bạn đang chạy trên công nghệ đã hoặc sắp hết vòng đời, và ai theo dõi chiếc đồng hồ đó?** Runtime già, cơ sở dữ liệu không được hỗ trợ và khung không còn bảo trì là kiểu thất bại chậm biến thành khủng hoảng đột ngột vào ngày bản vá bảo mật thôi đến. Với đội lớn, nguy hiểm là không ai sở hữu chân trời: từng đội vá cái hỏng, nhưng không ai duy trì cái nhìn danh mục về ngăn xếp nào mất hỗ trợ nhà cung cấp và khi nào. Hãy mang bằng chứng: bản kiểm kê các công nghệ cốt lõi của từng hệ thống trọng yếu, ngày hết vòng đời hay hết hỗ trợ đã công bố của chúng, và khoảng cách hiện tại giữa cái bạn chạy và cái vẫn còn được hỗ trợ. Căng thẳng là giữa chi phí nâng cấp liên tục và rủi ro trì hoãn, và trì hoãn thường thắng cho đến khi nó thua thảm khốc. Trong bối cảnh doanh nghiệp và chính phủ, nơi chu kỳ mua sắm và công nhận có thể mất một năm hoặc hơn, một ngày hết vòng đời trông xa thường đã nằm trong thời gian chờ của bạn, nên công việc kế nhiệm và nâng cấp phải bắt đầu rất lâu trước khi đồng hồ chạy hết.

6. **Ở đâu trong tài sản của bạn sự ổn định là giá trị và sự mới lạ là gánh nặng, và làm sao bạn giữ ranh giới đó trung thực?** Không phải hệ thống nào cũng thưởng cùng một cách đối xử: hệ thống lõi mà công dân và khách hàng phụ thuộc hằng ngày thường thưởng độ tin cậy và thay đổi thận trọng, trong khi rìa thưởng thí nghiệm, và nhầm hai thứ phí tiền hoặc mời gọi sự cố. Với tổ chức lớn, rủi ro là tham vọng và khuyến khích sự nghiệp đẩy các bản viết lại thú vị vào đúng phần lõi bền vững nên giữ nhàm chán. Hãy mang bằng chứng: bản đồ tài sản của bạn đánh dấu nơi độ tin cậy là sứ mệnh và nơi sự mới lạ tạo giá trị, cùng các thay đổi gần đây vượt lằn ranh đó theo cả hai hướng và chúng tốn bao nhiêu. Cân nhắc đối lập là ngay cả một lõi ổn định vẫn phải tiến hóa, nên "ổn định" không thể thành cái cớ để đóng băng. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn ranh giới này với các bậc trọng yếu tường minh và một thẩm quyền có tên có thể phủ quyết bản viết lại rủi ro của hệ thống mà công chúng không chịu nổi khi thấy nó thất bại, để phán đoán không trôi theo ai ồn ào nhất quý này.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và ít đường băng, rủi ro duy trì của bạn tập trung vào một hai người đã viết các hệ thống bạn không thể mất, như thanh toán hay xác thực. Hãy tiêu gần như không gì cho quy trình, nhưng làm ngay những việc rẻ, giá trị cao: ghép người thứ hai qua mỗi hệ thống trọng yếu, viết hồ sơ quyết định kiến trúc một trang cho các phần gây ngạc nhiên, và giữ một sổ tay vận hành bạn thực sự dùng. Chống lại thôi thúc viết lại thứ gì đó chỉ vì nó cũ, vì ở quy mô của bạn một bản viết lại thất bại của hệ thống lõi có thể kết thúc công ty.

**Doanh nghiệp nhỏ.** Bạn không có đội bảo trì riêng và ngân sách eo hẹp, nên hãy ưu tiên mua và lưu trữ hơn xây bất cứ thứ gì bạn phải tự duy trì. Ưu tiên nhà cung cấp và tiêu chuẩn mở cho phép bạn rời đi, và giữ bản ghi đơn giản về hệ thống bên ngoài nào chạy chức năng trọng yếu nào và gọi ai khi nó hỏng. Nơi bạn sở hữu mã tùy biến, hãy bảo đảm ít nhất hai người (hoặc một nhà thầu đáng tin cộng một nhân viên) hiểu nó, để một sự ra đi hay hợp đồng hỗ trợ hết hạn không bỏ rơi bạn.

**Doanh nghiệp lớn.** Thách thức của bạn là quy mô danh mục: nhiều hệ thống tồn tại lâu dài, nhiều đội, và nhân viên luân chuyển qua nhiều thập kỷ. Chuẩn hóa quyền sở hữu cấp đội trong danh mục dịch vụ, đo hệ số xe buýt qua tài sản, và tài trợ hiện đại hóa gia tăng liên tục thay vì đặt cược vào viết lại đại bùng nổ. Quản trị chân trời hết vòng đời tập trung để không ngăn xếp trọng yếu nào lặng lẽ hết hỗ trợ, và chạy mỗi cuộc khai tử như dự án được kiểm toán với trách nhiệm có tên cho việc hoàn tất tháo dỡ.

**Chính phủ.** Tính liên tục của nghĩa vụ là tuyệt đối: bạn không thể ngừng trả trợ cấp hay chạy kiểm soát không lưu trong khi tái cấu trúc, và thất bại là công khai và có hậu quả. Quy tắc mua sắm đẩy bạn về tiêu chuẩn mở, khả năng di chuyển dữ liệu, và giao diện có tài liệu để người bảo trì và nhà cung cấp tương lai có cơ hội. Hãy tài trợ đào tạo kế nhiệm có chủ đích cho các công nghệ cũ mà thị trường lao động không còn cung cấp, bảo tồn hồ sơ của hệ thống đã loại bỏ để đáp ứng lưu giữ theo luật định, và coi độ tin cậy bền vững của dịch vụ công dân là sứ mệnh chịu trách nhiệm thay vì chi phí chung.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp năm người đã có một hệ thống nó không thể mất: dịch vụ thanh toán một người sáng lập viết trong tháng đầu và nay chạy mọi khoản tính phí khách hàng. Chỉ người sáng lập đó hiểu nó, nên đội coi hệ số xe buýt là rủi ro thật thay vì lời khen. Họ ghép một kỹ sư thứ hai qua một chu kỳ thanh toán đầy đủ, viết một hồ sơ quyết định kiến trúc ngắn giải thích vì sao logic thử lại kỳ lạ tồn tại, và giữ sổ tay vận hành cạnh mã mà họ thực sự thực hành trong sự cố. Họ chống lại việc viết lại nó chỉ vì nó cũ và không hào nhoáng, và thay vào đó cải thiện nó bằng bước nhỏ đảo ngược được, để dịch vụ giữ công ty sống được hiểu bởi hơn một cái đầu.

**Doanh nghiệp lớn.** Một công ty bảo hiểm lớn chạy hệ thống quản trị hợp đồng được viết lần đầu cách đây hàng thập kỷ và vẫn trung tâm với hoạt động kinh doanh. Thay vì thử viết lại toàn bộ rủi ro, nó mô-đun hóa hệ thống sau các giao diện được xác định rõ và nay thay từng thành phần một, mỗi thay đổi nhỏ và đảo ngược được. Mọi chức năng trọng yếu có ít nhất ba người thực hiện được. Trực ca được chia sẻ. Hồ sơ quyết định kiến trúc ghi lại vì sao hệ thống hoạt động như vậy. Một khóa học nội bộ được tuyển chọn đưa kỹ sư mới đến năng lực trên ngăn xếp [kế thừa](https://en.wikipedia.org/wiki/Legacy_system), và các chuyên gia ra đi chồng lấn với người kế nhiệm để tri thức ngầm chuyển giao bằng làm.

**Chính phủ.** Một cơ quan an sinh xã hội quốc gia vận hành hệ thống chi trả trợ cấp đã chạy hơn ba mươi năm và không thể dừng. Nó ghi quyền sở hữu đội tường minh trong danh mục dịch vụ. Nó tài trợ bảo trì liên tục thay vì đóng băng hệ thống. Nó đào tạo người kế nhiệm có chủ đích trong các công nghệ cũ, vì thị trường lao động sẽ không cung cấp họ. Khi loại bỏ một hệ thống con lỗi thời, nó chạy khai tử như dự án được quản lý: lập bản đồ mọi bên tiêu thụ, cung cấp hỗ trợ di chuyển, bảo tồn hồ sơ để đáp ứng quy tắc lưu giữ pháp lý, và giao trách nhiệm cho việc thực sự hoàn tất tháo dỡ, để không hệ thống xác sống nào nấn ná.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của việc duy trì hệ thống tồn tại lâu dài đến từ việc tránh hai kiểu thất bại thảm khốc chi phối [tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership) của chúng. Thứ nhất là khủng hoảng đột ngột: một người then chốt ra đi, một thành phần không được hỗ trợ bị xâm phạm, hoặc một hệ thống mồ côi thất bại mà không ai hiểu nó. Thứ hai là mega-dự án thất bại: một bản viết lại toàn bộ vội vàng vượt chi, giao thiếu, hoặc sụp đổ. Cả hai đều cực kỳ đắt, và cả hai phần lớn có thể ngăn ngừa bằng quản gia đều đặn. Chi phí của một thất bại viết lại tránh được, hoặc một sự cố kéo dài tránh được của dịch vụ công dân trọng yếu, thường vượt nhiều năm đầu tư bảo trì bền vững.

Chi phí áp dụng là liên tục và kém hào nhoáng: tài trợ bảo trì không sinh tính năng mới, trả cho thời gian đào tạo chéo và tài liệu làm giảm đầu ra ngắn hạn, và đầu tư vào hiện đại hóa gia tăng không bao giờ lên tiêu đề. Chi phí của việc *không* áp dụng bị hoãn và lớn hơn: rủi ro tăng khi ngăn xếp già, mức phơi nhiễm người then chốt phình ra, và cuối cùng là một cuộc thay thế bị ép, rủi ro cao, chi phí cao trong điều kiện khẩn cấp. Khi lập luận với ban lãnh đạo, hãy đóng khung lại bảo trì từ "trung tâm chi phí" thành "quản lý rủi ro cho các hệ thống tổ chức không thể mất." Trình bày tổng chi phí sở hữu qua toàn bộ vòng đời nhiều thập kỷ (gồm duy trì và tháo dỡ cuối cùng) thay vì chỉ bản xây. Và nhấn mạnh điều này: với hệ thống hướng công dân và khách hàng, độ tin cậy bền vững không phải chi phí chung. Nó là lòng tin, sản phẩm thật sự.

## Phản mẫu và cạm bẫy

- **Người bảo trì anh hùng.** Một người không thể thay thế hiểu hệ thống; sự ra đi của họ là sự kiện sinh tử.
- **Đóng băng và quên.** Tuyên bố hệ thống trọng yếu là "xong," dừng bảo trì, và nhìn ngăn xếp của nó già đi thành không bảo trì được.
- **Bản viết lại định mệnh.** Đặt cược tổ chức vào một cuộc thay thế toàn bộ vứt bỏ tri thức được mã hóa và thường vượt chi hoặc thất bại.
- **Hệ thống mồ côi.** Phần mềm trọng yếu không có chủ hiện hành, chỉ được chú ý khi nó hỏng.
- **Sân khấu tài liệu.** Hàng khối tài liệu lỗi thời, không được thực hành, và không ai tin.
- **Chạy song song vĩnh cửu.** Hệ thống cũ và mới chạy cạnh nhau vô hạn vì không ai chịu trách nhiệm cho việc tắt.
- **Mất tri thức ngầm.** Để chuyên gia ra đi mà không chồng lấn, nên cảm giác về hệ thống bốc hơi.
- **Quá đáng sợ để chạm vào.** Một hệ thống ít được hiểu đến mức mọi thay đổi bị sợ, điều bảo đảm nó mục rữa.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Duy trì là tùy nghi và phản ứng. Hệ thống phụ thuộc vào cá nhân anh hùng, quyền sở hữu được nhớ thay vì được giao, và tri thức sống không tài liệu trong vài cái đầu. Hệ thống cũ bị đóng băng cho đến khi hỏng, ngăn xếp già trôi về hết vòng đời mà không ai để ý, và việc loại bỏ được thông báo nhưng không bao giờ hoàn tất.

**Mức 2: Phát triển.** Thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Quyền sở hữu được viết xuống cho các hệ thống lớn rõ ràng nhất, một số sổ tay vận hành và tài liệu tồn tại, và vài chức năng trọng yếu có người thứ hai đủ năng lực. Bảo trì được tài trợ nhưng phản ứng, đào tạo chéo xảy ra khi ai đó nhớ, và không có cách làm chung nào trong tổ chức.

**Mức 3: Chuẩn hóa.** Thực hành quản gia được lập tài liệu và thực thi toàn tổ chức. Quyền sở hữu cấp đội được ghi trong danh mục dịch vụ và sống sót qua tái tổ chức. Giảm thiểu hệ số xe buýt qua luân phiên và đào tạo chéo là quy tắc thường trực, hồ sơ quyết định kiến trúc và sổ tay vận hành được thực hành là kỳ vọng, hiện đại hóa gia tăng theo chính sách, và mỗi cuộc khai tử chạy như dự án được quản lý với trách nhiệm có tên cho việc hoàn tất tháo dỡ.

**Mức 4: Quản lý.** Duy trì được đo và kiểm soát bằng dữ liệu theo đường cơ sở. Bạn theo dõi hệ số xe buýt cho mỗi hệ thống trọng yếu, số người thay đổi an toàn được từng hệ thống, tuổi của mọi công nghệ cốt lõi so với ngày hết vòng đời của nó, tỷ lệ tài sản được bảo trì liên tục so với bị hoãn, và số lần chạy song song bị đình trệ và tháo dỡ dở dang. Các chỉ số này mang ngưỡng kích hoạt hành động: một hệ thống rơi dưới sàn hệ số xe buýt hay vượt chân trời hết hỗ trợ nhận khắc phục được tài trợ, và sức khỏe quản gia được báo cáo cho lãnh đạo cùng phân phối.

**Mức 5: Điều phối.** Quản gia được cải thiện liên tục và tích hợp trong toàn tổ chức. Không hệ thống trọng yếu nào là điểm đơn thất bại của con người, chuyển giao tri thức gồm tri thức ngầm qua chồng lấn là thường lệ, và hệ thống tiến hóa theo bước nhỏ đảo ngược được nên không cái nào hết hỗ trợ. Quyền sở hữu, theo dõi hết vòng đời, kế nhiệm và hoạch định khai tử được đan vào hoạch định danh mục và rủi ro, tài sản được cân bằng lại khi công nghệ và nghĩa vụ dịch chuyển, và hệ thống nhiều thập kỷ được duy trì trong khi bảo tồn lòng tin của những người phụ thuộc vào chúng.

## Ý tưởng để thảo luận

- Làm sao bạn đo hệ số xe buýt có ý nghĩa, và mục tiêu nào là đúng cho các mức trọng yếu khác nhau?
- Khi nào hiện đại hóa gia tăng thực sự bất khả thi, khiến viết lại là rủi ro nhỏ hơn?
- Làm sao bạn tài trợ và thưởng công việc bảo trì để quản gia là con đường nghề nghiệp được tôn trọng, không phải ngõ cụt?
- Cách đúng để bảo tồn tri thức ngầm khi chuyên gia cuối cùng sắp nghỉ hưu và không thể chồng lấn là gì?
- Bạn nên giữ khả năng trả lời câu hỏi về một hệ thống đã loại bỏ trong bao lâu, và ai trả tiền cho việc đó?
- Ở đâu trong tài sản của bạn sự ổn định là giá trị và sự mới lạ là gánh nặng, và làm sao bạn giữ phán đoán đó trung thực theo thời gian?

## Những điểm cần ghi nhớ

- Hầu hết phần mềm quan trọng là cũ và tồn tại lâu dài; duy trì nó qua nhiều thập kỷ và nhiều thế hệ nhân viên là kỷ luật hạng nhất.
- Mọi hệ thống trọng yếu cần quyền sở hữu hiện hành, cấp đội; hệ thống trọng yếu mồ côi là tình huống khẩn cấp tiềm ẩn.
- Giảm hệ số xe buýt có chủ đích (không tác vụ trọng yếu nào nên có đúng một người đủ năng lực) và chuyển giao tri thức ngầm qua chồng lấn, không chỉ qua tài liệu.
- Giữ hệ thống tồn tại lâu dài được bảo trì liên tục và gia tăng; đóng băng chúng và đặt cược vào viết lại toàn bộ đều là kiểu thất bại.
- Lên kế hoạch kết thúc như dự án được quản lý với việc hoàn tất có trách nhiệm, bảo tồn dữ liệu và hồ sơ để đáp ứng nghĩa vụ.
- Với hệ thống hướng công dân và khách hàng, độ tin cậy và sự công bằng bền vững là sứ mệnh, và bảo trì là quản lý rủi ro cho những gì bạn không thể mất.

## Tài liệu tham khảo và đọc thêm

- Michael Feathers, *Working Effectively with Legacy Code*
- Titus Winters, Tom Manshreck và Hyrum Wright, *Software Engineering at Google*
- Frederick P. Brooks Jr., *The Mythical Man-Month*
- Nat Pryce và Steve Freeman, *Growing Object-Oriented Software, Guided by Tests*
- Sam Newman, *Monolith to Microservices*
- Martin Fowler, *Refactoring* và các bài viết về mẫu Strangler Fig
- Betsy Beyer et al., *Site Reliability Engineering* và *The Site Reliability Workbook* (Google)
- Diomidis Spinellis, *Code Reading: The Open Source Perspective*
- U.S. Government Accountability Office, các báo cáo về hiện đại hóa CNTT kế thừa liên bang
