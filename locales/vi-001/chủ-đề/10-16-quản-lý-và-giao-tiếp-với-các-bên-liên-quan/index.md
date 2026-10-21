# 10.16 Quản lý và giao tiếp với các bên liên quan

## Tổng quan và động lực

Mọi công việc phần mềm nghiêm túc đều có những người có thể ảnh hưởng đến nó hoặc bị nó ảnh hưởng: lãnh đạo tài trợ cho nó, đội xây nó, nhóm vận hành chạy nó, khách hàng dùng nó, kiểm toán viên thanh tra nó. Đó là [các bên liên quan](https://en.wikipedia.org/wiki/Project_stakeholder) của bạn, và quản lý mối quan hệ với họ là một trong những kỹ năng cốt lõi của lãnh đạo kỹ thuật. Nhiều kỹ sư coi công việc này là chính trị, thứ khó chịu kéo họ khỏi công việc "thật" là xây dựng. Cách đóng khung đó là sai lầm, và đắt đỏ. Quản lý các bên liên quan là thực hành giữ những người xung quanh công việc của bạn được thông tin, căn chỉnh và tự tin, để công việc kỹ thuật tốt thực sự được phát hành và sống sót khi tiếp xúc với tổ chức. Mã xuất sắc mà không ai tin, tài trợ hay hiểu không mang lại giá trị.

Vì sao coi điều này tường minh? Vì ở quy mô, thông tin không tự chảy. Một đội nhỏ có thể giữ mọi người căn chỉnh bằng việc nói chuyện qua bàn; một đội lớn, một chương trình gồm nhiều đội, hay một cơ quan chính phủ thì không. Bị bỏ mặc, các bên liên quan tự hình thành bức tranh từ tin đồn, bảng điều khiển lỗi thời, và điều cuối cùng họ tình cờ nghe. Hầu hết thất bại "bất ngờ" không phải bất ngờ với tất cả mọi người; chúng đã thấy sớm bởi ai đó không được lắng nghe. Giao tiếp có chủ đích là cách bạn thay sự trôi dạt đó bằng một hiểu biết chung, hiện hành, trung thực về vị trí mọi thứ đang đứng và điều cần kỳ vọng tiếp theo.

Bối cảnh doanh nghiệp và chính phủ nâng rủi ro mạnh. Một sáng kiến doanh nghiệp có thể có hàng chục bên liên quan qua sản phẩm, tài chính, pháp lý, bảo mật và nhiều đơn vị kinh doanh, mỗi bên có khuyến khích và mức chịu đựng chi tiết khác nhau. Công việc chính phủ thêm các chủ thể chính trị, cơ quan giám sát và kiểm toán, báo chí và công chúng, cùng nghĩa vụ minh bạch theo luật mà doanh nghiệp tư không bao giờ đối mặt. Ở cả hai thế giới, khả năng hòa giải các lợi ích mâu thuẫn, truyền đạt rủi ro sớm, và giữ một bản tường thuật đáng tin duy nhất về sự thật thường phân biệt các chương trình bền vững với các chương trình bị hủy lặng lẽ. Chương này nói về việc làm tốt công việc đó, và làm nó như kỹ thuật, không phải sân khấu.

## Các nguyên tắc chính

- **Quản lý các bên liên quan là kỹ năng lãnh đạo, không phải chính trị.** Đó là cách công việc tốt được tài trợ, tin cậy và phát hành.
- **Biết các bên liên quan là ai trước khi bạn cần họ.** Lập bản đồ quyền lực và quan tâm có chủ đích, và xem xét lại.
- **Điều chỉnh thông điệp cho khán giả.** Lãnh đạo muốn kết quả và rủi ro; kỹ sư muốn chi tiết; công chúng muốn sự trung thực.
- **Giữ một nguồn sự thật duy nhất.** Con số mâu thuẫn phá hủy lòng tin nhanh hơn tin xấu.
- **Quản lý kỳ vọng, và nói không cho khéo.** Một lời từ chối rõ ràng, có lý do thắng một lời đồng ý vui vẻ bạn không giữ được.
- **Truyền đạt tin xấu sớm.** Vấn đề rẻ nhất, và uy tín của bạn cao nhất, khi bạn nêu chúng trước.
- **Ghi lại quyết định và gắn chúng với mục tiêu.** Các lựa chọn truy vết được sống sót qua thay đổi nhân sự, kiểm toán và tranh chấp.

## Khuyến nghị

### Lập bản đồ các bên liên quan trước khi bạn cần họ

Hãy bắt đầu bằng việc viết xuống các bên liên quan của bạn thực sự là ai. Đó là nhiều người hơn bạn nghĩ: người bảo trợ và người dùng, cộng các đội bạn phụ thuộc, các đội phụ thuộc vào bạn, các chức năng có thể chặn bạn (bảo mật, pháp lý, mua sắm), và các bên sẽ đánh giá kết quả về sau. Hãy làm một [phân tích các bên liên quan](https://en.wikipedia.org/wiki/Stakeholder_analysis) đơn giản và xếp họ theo hai trục, họ có bao nhiêu quyền lực đối với công việc và quan tâm đến nó bao nhiêu. Lưới quyền lực-quan tâm kết quả cho bạn biết nơi dành sự chú ý: quản lý chặt chẽ những người quyền lực cao, quan tâm cao; giữ người quyền lực cao, quan tâm thấp hài lòng và không bị bất ngờ; giữ người quyền lực thấp, quan tâm cao được thông tin; và theo dõi phần còn lại mà không nhấn chìm họ. Đây là bức tranh sống, không phải bài tập một lần. Ưu tiên dịch chuyển, và một bên liên quan quan tâm thấp có thể trở thành người quan trọng nhất trong phòng ngay khi ngân sách của họ bị chạm tới.

Hãy ghép bản đồ với sự rõ ràng về ai làm gì. Một [ma trận phân công trách nhiệm](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix), phổ biến nhất ở dạng RACI (Thực hiện, Chịu trách nhiệm, Được tham vấn, Được thông báo), làm tường minh ai làm việc, ai chịu trách nhiệm giải trình, ai phải được hỏi, và ai phải được báo. Kỷ luật ít nằm ở lưới mà nhiều ở việc buộc cuộc trò chuyện: đúng một người chịu trách nhiệm cho mỗi quyết định, một danh sách ngắn những người thực sự được tham vấn, và danh sách "được thông báo" trung thực để không ai cảm thấy bị phục kích. Khi vai trò mờ, giao tiếp thất bại trong im lặng, vì mọi người giả định ai đó khác đang xử lý bên liên quan quan trọng.

### Quản lý lên, xuống, ngang và ra ngoài

Bốn hướng giao tiếp mỗi hướng cần kỷ luật riêng. **Quản lý lên** nghĩa là trao cho lãnh đạo cái nhìn rõ ràng, trung thực, sẵn sàng cho quyết định: cái gì đúng tiến độ, cái gì có rủi ro, bạn cần gì từ họ, và bạn đã quyết định gì trong thẩm quyền của mình để họ không bị bất ngờ. **Quản lý xuống** nghĩa là trao cho đội ngữ cảnh và sự che chở: vì sao công việc quan trọng, nó nối với mục tiêu thế nào, và lãnh đạo đang lo gì, để họ không bay mù. **Quản lý ngang** nghĩa là các mối quan hệ ngang hàng với các đội và chức năng khác mà bạn cần sự hợp tác nhưng không ra lệnh được. **Quản lý ra ngoài** nghĩa là khách hàng, đối tác, nhà cung cấp, và, trong khu vực công, cơ quan giám sát, báo chí và công dân. Thất bại phổ biến là đầu tư quá mức hướng lên, đánh bóng bộ slide cho lãnh đạo, trong khi bỏ đói các mối quan hệ ngang thực sự gỡ nút cho công việc.

### Điều chỉnh thông điệp cho khán giả

Cùng một trạng thái phải được kể theo nhiều cách, và kỹ năng là chuyển dịch không bóp méo. Lãnh đạo muốn kết quả, rủi ro và quyết định: chúng ta có đạt mục tiêu không, cái gì đe dọa nó, và bạn cần gì ở tôi? Chôn rủi ro duy nhất quan trọng dưới mười đoạn tiến độ kỹ thuật là thất bại giao tiếp, không phải sự thể hiện nghiêm ngặt. Ngược lại, kỹ sư cần chi tiết: phụ thuộc cụ thể, ràng buộc thực, đánh đổi thật. Một hội đồng quản trị hay ủy ban lập pháp cần ngôn ngữ đơn giản, trung thực về bất định, và không biệt ngữ. Điều chỉnh là chính đáng và cần thiết; điều không bao giờ chính đáng là kể cho các khán giả khác nhau những câu chuyện mâu thuẫn. Cùng sự kiện, độ cao và từ vựng khác. Nếu bạn sẽ thấy khó chịu khi bản tóm tắt điều hành và chi tiết kỹ thuật của mình được đọc cạnh nhau, bạn không đang điều chỉnh, bạn đang tô vẽ.

### Báo cáo trạng thái trung thực từ một nguồn sự thật duy nhất

Báo cáo trạng thái giành được hay phá hủy lòng tin, và cách nhanh nhất để phá hủy nó là để các con số phân kỳ. Hãy giữ một [nguồn sự thật duy nhất](https://en.wikipedia.org/wiki/Single_source_of_truth): một nơi trạng thái hiện tại của công việc sống, mà mọi người thấy được, và từ đó mọi báo cáo được rút ra. Khi bảng điều khiển điều hành, bảng của đội và email cập nhật bất đồng, các bên liên quan thôi tin bất kỳ cái nào và bắt đầu quản lý bằng tin đồn. Ưu tiên tín hiệu minh bạch, tự cập nhật (phần mềm hoạt động được trình diễn, biểu đồ burn-up, chỉ số thật) hơn các bản tóm tắt xanh-vàng-đỏ lắp thủ công thưởng cho sự lạc quan. Coi chừng trạng thái "dưa hấu," xanh bên ngoài và đỏ bên trong, là cách tin xấu trung thực bị chôn đến hạn chót. Báo cáo trạng thái tốt nhàm chán có chủ đích: hiện hành, nhất quán, và không sợ màu vàng. Xem chương 10.6 về cách luồng minh bạch làm nền cho quản lý dự án.

### Quản lý kỳ vọng và nói không cho khéo

Phần lớn quản lý các bên liên quan là quản lý kỳ vọng: định hình điều mọi người tin sẽ xảy ra để thực tế, khi nó đáp xuống, gần với điều họ được hứa. Kỷ luật là cam kết ít hơn bạn nghĩ mình làm được và truyền đạt tiến độ so với đó, thay vì hứa mọi thứ rồi giải thích thiếu hụt về sau. Nói không là một phần của điều này, và làm tốt là kỹ năng đáng luyện. Một lời không tốt không phải sự từ chối phẳng; đó là một đánh đổi có lý do: "Vâng, chúng tôi làm được, và đây là cái gì dịch chuyển hoặc nó tốn gì." Hãy cho thấy [thương lượng](https://en.wikipedia.org/wiki/Negotiation) một cách trung thực, gắn nó với mục tiêu chung, và để bên liên quan chọn trong ràng buộc thật. Một lời đồng ý vui vẻ bạn không giữ được tốn lòng tin nhiều hơn nhiều so với một lời không rõ ràng có lý do, vì lời đồng ý thất bại trong im lặng và muộn.

### Hòa giải các bên liên quan mâu thuẫn và thương lượng ưu tiên

Các bên liên quan sẽ muốn những thứ không tương thích: bán hàng muốn tính năng ngay, bảo mật muốn rà soát trước, tài chính muốn hạ chi phí, và tất cả đều đúng một phần. Công việc của bạn không phải làm mọi người hài lòng, điều bất khả, mà là làm lộ mâu thuẫn, đóng khung đánh đổi theo mục tiêu chung, và đẩy nó đến một quyết định tường minh bởi người chịu trách nhiệm. Hãy làm điều này công khai thay vì lặng lẽ thiên vị giọng nói to nhất. Đặt cuộc trò chuyện trên mục tiêu và kết quả then chốt (chương 11.4) để tranh luận là về mục tiêu nào thắng, không phải cảm xúc của ai. Khi một quyết định không thể đưa ra ở cấp của bạn, hãy leo thang nó thay vì để nó thối rữa. Mâu thuẫn bên liên quan chưa giải quyết không biến mất; nó tái xuất hiện dưới dạng vật vã, làm lại và đổ lỗi.

### Xây ảnh hưởng không cần thẩm quyền, và leo thang mang tính xây dựng

Ở quy mô bạn liên tục cần hợp tác từ những người không báo cáo cho bạn. Ảnh hưởng không cần thẩm quyền đến từ uy tín (bạn giao điều bạn nói), có đi có lại (bạn giúp người khác), và đóng khung yêu cầu theo mục tiêu của bên kia thay vì của bạn. Hãy đầu tư vào các mối quan hệ này trước khi bạn cần; thời điểm để xây lòng tin với đội bảo mật không phải buổi chiều bạn cần một ngoại lệ khẩn cấp. Khi ảnh hưởng không đủ, hãy leo thang, và làm điều đó mang tính xây dựng. Leo thang mang tính xây dựng không phải mách lẻo; đó là đưa một bất đồng thật, đóng khung tốt đến người có thẩm quyền giải quyết, kèm các phương án và một khuyến nghị, để một quyết định được đưa ra. Hãy leo thang vấn đề, không phải con người; leo thang sớm, khi các phương án còn đó; và nói với bên kia rằng bạn đang làm vậy. Các đội coi leo thang là thất bại kết thúc với những quyết định không bao giờ được đưa ra.

### Truyền đạt tin xấu, rủi ro và bất định sớm

Thói quen đòn bẩy cao nhất trong chương này là nêu vấn đề sớm. Tin xấu không tốt lên theo tuổi; một ngày trượt, một phụ thuộc hỏng, hay một mối lo bảo mật rẻ nhất để xử lý khi nó mới xuất hiện và gây hại nhất khi nó nổ ở hạn chót. Hãy làm cho tin xấu đi nhanh một cách an toàn, và làm gương bằng cách là người đầu tiên nêu rủi ro của chính mình. Cũng truyền đạt bất định một cách trung thực: đưa khoảng thay vì ngày đơn độ chính xác giả, nói bạn chưa biết gì, và cập nhật khi học. Thừa nhận bất định sớm xây uy tín nhiều hơn độ chính xác tự tin sau này hóa ra sai. Bên liên quan nghe "đây là một rủi ro, đây là điều chúng tôi đang làm về nó" tin bạn hơn người không nghe gì rồi nghe "nó trượt rồi."

### Ghi lại quyết định và gắn chúng với mục tiêu

Giao tiếp cũng là để lại dấu vết truy vết được, không chỉ phục vụ hiện tại. Hãy ghi lại các quyết định đáng kể, cùng ngữ cảnh và lý do, bằng hồ sơ quyết định nhẹ (chương 1.6) để sáu tháng sau, khi mọi người đã chuyển đi, bất kỳ ai cũng dựng lại được vì sao một lựa chọn được đưa ra. Gắn các quyết định đó và trạng thái của bạn trở lại các mục tiêu chúng phục vụ (chương 11.4), và đưa các quyết định có trọng lượng qua nhóm chỉ đạo hay diễn đàn quản trị thích hợp (chương 1.5) để chúng mang tính chính danh. Trong môi trường được kiểm toán và khu vực công, khả năng truy vết này không tùy chọn; cơ quan giám sát sẽ hỏi vì sao, và "chúng tôi từng thảo luận" không phải câu trả lời. Hồ sơ tốt biến giao tiếp với các bên liên quan từ dòng các cuộc trò chuyện bị quên thành một thể chế sống sót qua thay đổi nhân sự.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Cập nhật chủ động thường xuyên** | Xây lòng tin; làm lộ vấn đề sớm; không bất ngờ | Tốn thời gian; rủi ro nhiễu nhấn chìm tín hiệu |
| **Điều chỉnh thông điệp theo khán giả** | Rõ ràng, liên quan, sẵn sàng cho quyết định với từng nhóm | Công sức chuyển dịch; trượt sang tô vẽ nếu sự kiện phân kỳ |
| **Nguồn sự thật duy nhất** | Nhất quán, được tin; giết quản lý theo tin đồn | Cần kỷ luật và công cụ để giữ hiện hành |
| **Nói đồng ý để mọi người vui** | Thiện chí ngắn hạn dễ dàng | Cam kết bị phá; lòng tin sụp muộn và đắt |
| **Leo thang mang tính xây dựng** | Quyết định được đưa ra; mâu thuẫn giải quyết công khai | Cảm giác đối đầu; bị hiểu là thất bại nếu văn hóa chưa trưởng thành |
| **Nghi thức bên liên quan nặng** | Bao phủ kỹ lưỡng; tốt cho chương trình hệ trọng | Quá tải họp; ăn thời gian khỏi công việc |

Căng thẳng trung tâm là **minh bạch so với thoải mái**. Giao tiếp trung thực, sớm, nhất quán đôi khi nghĩa là đưa tin xấu, thừa nhận bất định, hay nói không, tất cả đều khó chịu ngay lúc đó. Phương án trấn an, trạng thái lạc quan và những lời đồng ý vui vẻ, mua sự bình lặng ngắn hạn bằng cái giá của một cuộc thanh toán lớn hơn nhiều về sau. Hãy giải quyết bằng chọn lòng tin bền vững hơn sự thoải mái nhất thời: hãy là người nêu điều khó trước. Danh tiếng đó, một khi giành được, là tài sản quý nhất bạn có khi khủng hoảng thật đáp xuống, vì mọi người tin bạn.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn có thực sự biết mọi bên liên quan của mình là ai, và quyền lực cùng sự quan tâm thực sự nằm ở đâu không?** Hầu hết các đội nêu được người bảo trợ và người dùng rõ ràng nhưng bỏ sót những người có thể lặng lẽ chặn họ: một chức năng bảo mật, một cổng mua sắm, một đội ngang hàng có lộ trình va chạm với bạn, một kiểm toán viên chỉ xuất hiện ở cuối. Khi quyền lực và quan tâm chưa được lập bản đồ, bạn giao tiếp thừa với người thân thiện và thiếu với người nguy hiểm, và bạn bị bất ngờ bởi một bên liên quan bạn không biết mình có. Hãy mang bằng chứng: thử phác lưới quyền lực-quan tâm cho công việc hiện tại từ trí nhớ và xem bao nhiêu cái tên bạn không chắc. Câu trả lời nên đổi ai nhận sự chú ý của bạn quý này, và nó nên được xem xét lại mỗi khi lãnh đạo hoặc ưu tiên dịch chuyển, vì bản đồ cũ đi nhanh.

2. **Khi tin xấu tồn tại, mất bao lâu để nó đến những người cần nó, và làm vậy có an toàn không?** Khoảng cách giữa khi dấu hiệu cảnh báo đầu tiên tồn tại và khi người ra quyết định nghe thấy là một trong những yếu tố dự báo tốt nhất việc một dự án có thất bại trong im lặng không. Nếu văn hóa của bạn trừng phạt người đưa tin, khoảng cách đó lớn lên, vì mọi người chờ, hy vọng và né tránh thay vì nêu rủi ro khi nó còn rẻ. Hãy nhìn nỗ lực gặp khó gần nhất của bạn và truy dòng thời gian một cách trung thực: ai đó biết đầu tiên khi nào, và lãnh đạo phát hiện khi nào? Cân nhắc liệu báo cáo trạng thái của bạn thưởng sự trung thực hay lạc quan, và liệu một kỹ sư báo cờ độ trượt sớm được cảm ơn hay bị đổ lỗi. Mục tiêu là một đội nơi tin xấu đi nhanh và người nêu nó được đối xử như đã làm tốt việc của mình.

3. **Khi hai bên liên quan muốn những thứ không tương thích, mâu thuẫn đó thực sự được giải quyết thế nào hôm nay?** Ưu tiên mâu thuẫn là không tránh khỏi ở quy mô, và kiểu thất bại không phải bản thân mâu thuẫn mà là cách nó được dàn xếp: bởi ai ồn ào nhất, cấp cao nhất, hay dai dẳng nhất, thay vì một đánh đổi tường minh theo mục tiêu chung. Điều đó tạo vật vã, làm lại lặng lẽ và oán giận, và giấu quyết định thật khỏi những người chịu trách nhiệm cho nó. Hãy mang một ví dụ cụ thể gần đây nơi bán hàng, bảo mật, tài chính hay hai đội sản phẩm kéo ngược hướng, và truy nó được quyết định thế nào và có bao giờ được viết xuống không. Câu trả lời nên cho bạn biết bạn có cơ chế thật, đặt nền trên mục tiêu (chương 11.4) và leo thang mang tính xây dựng (chương 1.5), hay bạn đang giải quyết mâu thuẫn bằng hao mòn và hy vọng nó trụ được.

4. **Có thực sự một nguồn sự thật duy nhất cho trạng thái của công việc này không, hay bảng điều khiển, bảng và email trạng thái của bạn lặng lẽ bất đồng?** Khi các con số phân kỳ, các bên liên quan thôi tin tất cả và bắt đầu quản lý bằng tin đồn, và sự phân kỳ thường giấu chính tin xấu cụ thể mà ai đó không muốn làm lộ. Với đội lớn rủi ro cộng dồn, vì mỗi bề mặt báo cáo thêm là một nơi khác một chỉnh sửa lạc quan hay con số cũ có thể bén rễ, và trạng thái "dưa hấu" (xanh bên trên, đỏ bên dưới) sống lâu nhất nơi không hiện vật đơn lẻ nào có thẩm quyền. Hãy mang các báo cáo thật các bên liên quan đã thấy tháng trước và trải chúng cạnh nhau để xem tóm tắt điều hành, bảng phân phối và các chỉ số nền có kể cùng một câu chuyện không. Trong bối cảnh doanh nghiệp và chính phủ, nơi cơ quan kiểm toán hay ủy ban giám sát có thể đòi số liệu thô, một nguồn duy nhất đã đối soát không chỉ là công cụ lòng tin; nó là sự phòng vệ, vì hồ sơ mâu thuẫn mời gọi phát hiện tai hại rằng bạn không biết trạng thái của chính mình.

5. **Mối quan hệ nào nằm ngang chứ không phải hướng lên, và cái nào bạn đang bỏ đói cho đến ngày bạn cần?** Hầu hết các đội đầu tư quá mức vào quản lý lên, đánh bóng slide cho lãnh đạo, trong khi những người ngang hàng và chức năng thực sự gỡ nút cho công việc (bảo mật, mua sắm, một đội láng giềng có lộ trình va chạm với bạn) chỉ nhận sự chú ý trong khủng hoảng. Ảnh hưởng không cần thẩm quyền được xây chậm qua uy tín và có đi có lại, và không thể triệu hồi vào buổi chiều bạn cần một ngoại lệ khẩn cấp, nên mạng lưới ngang mỏng hiện ra là chậm trễ lặng lẽ thay vì thất bại hiển thị. Hãy mang danh sách trung thực các mối quan hệ ngang hàng công việc này phụ thuộc vào và chấm xem bạn đã gửi gắm bao nhiêu lòng tin với từng bên trước khi phải rút ra. Với doanh nghiệp lớn hay chương trình chính phủ trải qua nhiều đội và nhà thầu, hãy thêm nơi một mối quan hệ thiếu sẽ buộc một leo thang chính thức chậm thay cho một ân huệ nhanh, vì ở quy mô chi phí của quan hệ ngang yếu được đo bằng hàng tuần quy trình có thể tránh.

6. **Sáu tháng nữa, sau khi mọi người đã chuyển đi, ai đó có dựng lại được vì sao quyết định hệ trọng gần nhất của bạn được đưa ra không?** Giao tiếp phục vụ nhiều hơn khoảnh khắc hiện tại, vì các quyết định bạn dàn xếp hôm nay thành tranh chấp, kiểm toán và đảo ngược của năm sau, và ký ức về lý do bốc hơi nhanh hơn bất kỳ ai tưởng. Lực kéo đối lập là tốc độ: ghi lại ngữ cảnh và lý do cảm giác như chi phí chung khi mọi người trong phòng đã đồng ý, vậy mà sự hiểu biết chung đó chính xác là thứ thay đổi nhân sự phá hủy. Hãy mang ba quyết định đáng kể gần nhất và kiểm tra mỗi cái có hồ sơ viết với ngữ cảnh, các phương án đã cân nhắc, và ai chịu trách nhiệm không, hay dấu vết là một sợi chỉ rải rác không ai tìm được. Trong môi trường kiểm toán và khu vực công điều này không tùy ý, vì cơ quan giám sát sẽ hỏi vì sao một lựa chọn được đưa ra và "chúng tôi từng thảo luận" không phải câu trả lời sống sót qua soi xét; hồ sơ là thứ biến dòng các cuộc trò chuyện bị quên thành bản tường thuật bạn đứng sau được.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm người và đường băng ngắn, hãy giữ nó nhẹ nhưng không bao giờ vắng. Các bên liên quan của bạn ít (một người sáng lập, vài khách hàng đầu tiên, các nhà đầu tư), nên một cập nhật hằng tuần trung thực trong kênh chung và một buổi trình diễn thứ Sáu về phần mềm hoạt động thường đủ bao phủ bản đồ. Cái bẫy là câu chuyện thứ hai, màu hồng hơn kể cho nhà đầu tư; hãy cưỡng lại, vì bản tường thuật duy nhất bạn giữ bây giờ là thứ mua cho bạn quyền tự chủ khi một quyết định thực sự khó đến.

**Doanh nghiệp nhỏ.** Bạn không có văn phòng chương trình riêng và ít dư địa, nên hãy dựa vào thói quen rẻ hơn nghi thức: một danh sách bên liên quan một trang, một bảng tính hay bảng duy nhất mọi người đọc, và quy tắc thường trực rằng tin xấu đi ra ngay ngày nó được biết. Thay vì mua công cụ giao tiếp, hãy dùng thứ đội bạn đã sống trong đó và để dành báo cáo chính thức cho vài quyết định (khoản chi lớn, cam kết khách hàng) nơi dấu vết bằng văn bản thực sự bảo vệ bạn.

**Doanh nghiệp lớn.** Vấn đề là quy mô: hàng chục bên liên quan qua sản phẩm, tài chính, pháp lý, bảo mật và nhiều đơn vị kinh doanh, mỗi bên có khuyến khích khác nhau. Hãy chuẩn hóa bộ máy để các nhóm thôi phát minh lại nó: một bản đồ quyền lực-quan tâm được duy trì, một RACI với đúng một chủ sở hữu chịu trách nhiệm cho mỗi quyết định, một bảng điều khiển duy nhất nuôi mọi báo cáo, và một nhóm chỉ đạo đều đặn nơi các đánh đổi xuyên đơn vị được đưa ra công khai theo mục tiêu đã thống nhất thay vì được dàn xếp bằng vận động hành lang.

**Chính phủ.** Quy tắc mua sắm, minh bạch theo luật và trách nhiệm giải trình công mở rộng tập bên liên quan tới các bộ trưởng, ủy ban giám sát, cơ quan kiểm toán, báo chí và công dân. Hãy công bố tiến độ bằng ngôn ngữ đơn giản, giữ mọi quyết định đáng kể trong hồ sơ viết kèm lý do để kiểm toán viên dựng lại được vì sao, và báo cáo cơ quan giám sát về rủi ro nổi lên sớm thay vì chờ được hỏi. Hợp đồng và nghĩa vụ tiết lộ nghĩa là giao tiếp của bạn là một phần của hồ sơ công, nên giữ điều bạn nói với bộ trưởng nhất quán với điều bạn nói với ủy ban là nghĩa vụ pháp lý cũng như danh tiếng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười hai người giữ quản lý bên liên quan nhẹ nhưng có chủ đích. Người sáng lập kiêm CEO là bên liên quan chính, cùng hai khách hàng doanh nghiệp đầu tiên và các nhà đầu tư hạt giống. Trưởng kỹ thuật gửi một cập nhật hằng tuần ngắn trong một kênh, cùng các con số mọi người thấy, bao quát cái đã phát hành, cái có rủi ro, và quyết định nào cần, và trình diễn phần mềm hoạt động mỗi thứ Sáu. Khi một tích hợp then chốt trượt, trưởng nhóm nói vào thứ Hai nó trở nên rõ ràng, kèm khoảng sửa đổi và phương án dự phòng, thay vì hy vọng phục hồi trước thứ Sáu. Vì có một bản tường thuật trung thực và không có câu chuyện thứ hai bóng bẩy cho nhà đầu tư, hội đồng tin phán đoán của đội khi một quyết định thực sự khó đến, và để họ đưa ra nó.

**Doanh nghiệp lớn.** Một ngân hàng hiện đại hóa nền tảng thanh toán có hàng chục bên liên quan qua bán lẻ, tuân thủ, bảo mật, tài chính và ba đơn vị kinh doanh, cộng một nhà cung cấp. Lãnh đạo chương trình duy trì bản đồ bên liên quan và RACI để mọi quyết định lớn có đúng một chủ sở hữu chịu trách nhiệm, và chạy nhóm chỉ đạo hằng tháng (chương 1.5) nơi các đánh đổi giữa các đơn vị kinh doanh được đưa ra công khai theo mục tiêu đã thống nhất thay vì được dàn xếp bằng vận động hành lang. Trạng thái chảy từ một bảng điều khiển duy nhất do các đội phân phối nuôi, nên tóm tắt điều hành và chi tiết kỹ thuật không bao giờ mâu thuẫn nhau. Khi một rà soát bảo mật đe dọa ngày ra mắt, lãnh đạo leo thang sớm với hai phương án và một khuyến nghị, và nhóm chỉ đạo quyết định trong một ngày thay vì vấn đề thối rữa cả tháng.

**Chính phủ.** Một cơ quan công cung cấp dịch vụ trợ cấp hướng công dân chịu trách nhiệm trước tập bên liên quan rộng hơn nhiều: bộ trưởng và văn phòng của họ, một ủy ban giám sát của quốc hội, cơ quan kiểm toán quốc gia, các nhóm vận động, báo chí và công chúng, cùng với các đội phân phối và nhà thầu. Chương trình công bố tiến độ minh bạch, giữ mọi quyết định đáng kể trong hồ sơ viết kèm lý do (chương 1.6) để kiểm toán viên dựng lại được vì sao các lựa chọn được đưa ra, và điều chỉnh giao tiếp: kết quả và rủi ro cho bộ trưởng, hiệu suất dịch vụ bằng ngôn ngữ đơn giản cho công chúng, và chi tiết đầy đủ cho cơ quan kiểm toán. Khi một rủi ro di chuyển dữ liệu nổi lên, đội báo cáo ủy ban giám sát sớm và trung thực thay vì chờ được hỏi, điều bảo toàn lòng tin chính trị mà chương trình cần để sống sót qua tiêu đề khó khăn kế tiếp.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của quản lý các bên liên quan bị chi phối bởi **thảm họa tránh được và lòng tin được bảo toàn**. Các dự án hiếm khi chết vì một lỗi kỹ thuật đơn lẻ; chúng chết khi những người tài trợ và quản trị chúng mất niềm tin, rút hỗ trợ, và hủy công việc, thường sau chi phí chìm khổng lồ. Giao tiếp bên liên quan tốt ngăn vòng xoáy đó: nó giữ người bảo trợ gắn bó, làm lộ vấn đề khi còn rẻ, và hòa giải các mâu thuẫn mà nếu không sẽ di căn thành vật vã và làm lại. Khoản đầu tư nhỏ, chủ yếu là sự chú ý và vài thói quen có kỷ luật, và bị chi phí toàn phần của một sáng kiến lớn bị hủy vì lãnh đạo thôi tin vào nó lấn át.

Về **tổng chi phí sở hữu**, chi phí liên tục là thật nhưng khiêm tốn: thời gian lập bản đồ bên liên quan, điều chỉnh cập nhật, chạy diễn đàn chỉ đạo, và giữ nguồn sự thật duy nhất hiện hành. Đầu tư thiếu thì đắt ở làm lại, phụ thuộc bị bỏ sót và leo thang bất ngờ tiêu thời gian lãnh đạo ở chế độ khủng hoảng. Đầu tư thừa cũng đắt: các cuộc họp trạng thái bất tận và nghi thức báo cáo ăn thời gian khỏi công việc và dạy các bên liên quan tắt tai. Mục tiêu là kỷ luật giao tiếp nhẹ nhất giữ các bên liên quan thực sự của bạn căn chỉnh và không bị bất ngờ. Hãy lập luận với ban lãnh đạo bằng cách đối chiếu chi phí của một dự án gần đây bị hại bởi thất bại giao tiếp (rủi ro bị bỏ sót, cam kết bị phá, người bảo trợ bị mất) với chi phí gần bằng không của bản đồ bên liên quan, một bảng điều khiển duy nhất và văn hóa nơi tin xấu đi nhanh.

## Phản mẫu và cạm bẫy

- **Coi nó là dưới tầm mình:** gạt công việc bên liên quan là chính trị, nên nó không được làm cho đến khi một mối quan hệ thất bại.
- **Chỉ quản lý lên:** đánh bóng slide điều hành trong khi bỏ đói các mối quan hệ ngang hàng thực sự gỡ nút cho công việc.
- **Câu chuyện mâu thuẫn:** kể cho các khán giả khác nhau các phiên bản không tương thích, làm sụp lòng tin ngay khi họ so ghi chú.
- **Trạng thái dưa hấu:** xanh bên ngoài, đỏ bên trong, nên tin xấu trung thực bị chôn đến hạn chót.
- **Nhiều nguồn sự thật:** bảng điều khiển, bảng và email bất đồng, để các bên liên quan quản lý bằng tin đồn.
- **Đồng ý vui vẻ:** đồng ý mọi thứ để tránh xung đột, rồi phá cam kết muộn và đắt.
- **Leo thang như thất bại:** văn hóa nơi nêu bất đồng bị trừng phạt, nên quyết định không bao giờ được đưa ra.
- **Tích trữ tin xấu:** hy vọng phục hồi lặng lẽ trước khi ai để ý, biến vấn đề nhỏ thành khủng hoảng.
- **Quá tải họp:** nhiều nghi thức trạng thái đến mức bản thân giao tiếp thành công việc.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Giao tiếp với bên liên quan là tùy nghi và phản ứng. Không ai lập bản đồ các bên liên quan là ai. Tin xấu đi chậm, trạng thái lạc quan, và bất ngờ thường xuyên. Mâu thuẫn được dàn xếp bởi ai ồn ào nhất.
- **Mức 2, Phát triển:** Thực hành cơ bản xuất hiện nhưng không nhất quán giữa các đội. Cập nhật trạng thái đều đặn tồn tại và các bên liên quan chính được xác định ở một số nhóm, nhưng thông điệp một-kích-cỡ-cho-tất-cả, các con số đôi khi phân kỳ giữa các báo cáo, và leo thang bị coi là phương sách cuối hoặc dấu hiệu thất bại.
- **Mức 3, Chuẩn hóa:** Các bên liên quan được lập bản đồ theo quyền lực và quan tâm và vai trò rõ ràng qua RACI, áp dụng cùng cách qua các đội. Giao tiếp được điều chỉnh theo khán giả từ một nguồn sự thật duy nhất có tài liệu, quyết định được ghi lại và gắn với mục tiêu, và nêu tin xấu sớm được thực thi như chuẩn mực toàn tổ chức thay vì thói quen của một đội.
- **Mức 4, Quản lý:** Thực hành giao tiếp được đo và kiểm soát bằng dữ liệu theo đường cơ sở. Tổ chức theo dõi độ trễ giữa khi một rủi ro xuất hiện lần đầu và khi người ra quyết định nghe thấy, độ tin cậy của cam kết (đã hứa so với đã giao), tính nhất quán của báo cáo rút ra từ nguồn duy nhất, và sự tự tin của bên liên quan được lấy mẫu trực tiếp thay vì giả định. Thời gian chu kỳ leo thang và tỷ lệ leo thang bất ngờ được theo xu hướng, và khi một chỉ số trôi khỏi đường cơ sở quy trình được điều chỉnh có chủ đích thay vì theo giai thoại.
- **Mức 5, Điều phối:** Quản lý các bên liên quan là sức mạnh tổ chức được cải thiện liên tục, tích hợp với quản trị, hoạch định và phân phối trong toàn tổ chức. Lòng tin đủ cao để lãnh đạo trao quyền tự chủ thật, mâu thuẫn được giải quyết công khai theo mục tiêu chung, leo thang là thường lệ và mang tính xây dựng, và đội luôn là bên đầu tiên nêu rủi ro của chính mình. Thực hành thích ứng khi các bên liên quan, cấu trúc và nghĩa vụ dịch chuyển, đưa bài học từ mỗi chương trình ngược vào cách chương trình tiếp theo giao tiếp.

## Ý tưởng để thảo luận

1. Các bên liên quan hiện tại của bạn nằm ở đâu trên lưới quyền lực-quan tâm, và bạn đang giao tiếp thừa hay thiếu với ai?
2. Nếu lãnh đạo đọc tóm tắt điều hành và chi tiết kỹ thuật của bạn cạnh nhau, chúng có kể cùng một câu chuyện không?
3. Nguồn sự thật duy nhất của bạn hôm nay là gì, và các con số của bạn hiện phân kỳ giữa các báo cáo ở đâu?
4. Lần cuối bạn nói không với một bên liên quan là khi nào, và bạn đóng khung nó như một đánh đổi có lý do hay một sự từ chối phẳng?
5. Đội bạn đối xử thế nào với người leo thang một bất đồng hay nêu một rủi ro: như đang làm việc của họ, hay như một vấn đề?
6. Với ba quyết định đáng kể gần nhất của bạn, một người mới có dựng lại được vì sao chúng được đưa ra không?

## Những điểm cần ghi nhớ

- Quản lý các bên liên quan là kỹ năng lãnh đạo kỹ thuật cốt lõi, không phải chính trị; công việc tốt vẫn cần được tài trợ, tin cậy và phát hành.
- **Lập bản đồ các bên liên quan** theo quyền lực và quan tâm, làm rõ vai trò bằng RACI, và xem xét lại cả hai khi mọi thứ thay đổi.
- **Điều chỉnh thông điệp** cho từng khán giả (kết quả và rủi ro cho lãnh đạo, chi tiết cho kỹ sư) mà không bao giờ kể những câu chuyện mâu thuẫn.
- Báo cáo từ **một nguồn sự thật duy nhất**, và làm **tin xấu đi nhanh**; giao tiếp sớm, trung thực, nhất quán thắng sự lạc quan trấn an.
- **Nói không cho khéo**, hòa giải mâu thuẫn công khai theo mục tiêu chung, leo thang mang tính xây dựng, và xây ảnh hưởng trước khi bạn cần.
- **Ghi lại quyết định** và gắn chúng với mục tiêu để truy vết (chương 1.6, 11.4), và đưa các quyết định có trọng lượng qua diễn đàn quản trị (chương 1.5). Xem thêm các chương 10.6 và 10.1.

## Tài liệu tham khảo và đọc thêm

- Allan R. Cohen và David L. Bradford, *Influence Without Authority*.
- Roger Fisher và William Ury, *Getting to Yes: Negotiating Agreement Without Giving In*.
- Camille Fournier, *The Manager's Path*.
- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* (quản lý sự tham gia của bên liên quan và giao tiếp).
- AXELOS, *Managing Successful Projects with PRINCE2* (vai trò bên liên quan và quản trị).
- Aaron Dignan, *Brave New Work* (ra quyết định và lòng tin tổ chức).
- Kim Scott, *Radical Candour* (giao tiếp trung thực xây dựng lòng tin).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard* (minh bạch và thực hành bên liên quan trong phân phối khu vực công).
