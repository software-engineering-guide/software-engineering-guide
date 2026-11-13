# 10.8 Mô hình trưởng thành

## Tổng quan và động lực

Một [mô hình trưởng thành](https://en.wikipedia.org/wiki/Maturity_model) là cách có cấu trúc để đánh giá thực hành của bạn có năng lực và nhất quán đến đâu trong một lĩnh vực nào đó, và để mô tả con đường cải thiện nó. Nó xác định một bậc thang nhỏ các mức. Ở đáy, công việc là tùy nghi và phản ứng. Ở đỉnh, nó được đo, được quản lý và liên tục tối ưu. Mỗi nấc có những đặc điểm quan sát được để bạn đối chiếu.

Mô hình trưởng thành biến một câu hỏi mơ hồ ("chúng ta có giỏi việc này không?") thành một câu trả lời lặp lại được ("chúng ta ở mức 2 ở đây, mức 4 ở kia, và đây là điều mức 3 đòi hỏi"). Cuốn sách này dùng mô hình năm mức trong mọi chương và hợp nhất chúng ở chương 12.4. Chương này nói về chính kỷ luật đó: các mô hình hoạt động thế nào, khi nào chúng giúp, và chúng đánh lạc hướng ra sao.

Lý do chúng quan trọng thì đơn giản. Các tổ chức lớn không cải thiện được cái họ không thấy. Qua hàng chục đội, năng lực khác nhau rất nhiều và vô hình. Một số đội có kiểm thử xuất sắc và bảo mật yếu; số khác ngược lại. Một mô hình trưởng thành cho bạn từ vựng chung và thước đo chung, để các khoảng trống có thể so sánh, đầu tư có thể được ưu tiên, và tiến độ có thể được theo dõi theo thời gian thay vì chỉ được tuyên bố. Các ví dụ nổi tiếng gồm CMMI ([Mô hình Trưởng thành Năng lực Tích hợp](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), cho quy trình), mô hình DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (hiệu suất phân phối phần mềm), OWASP SAMM (Mô hình Trưởng thành Đảm bảo Phần mềm) và BSIMM (Mô hình Trưởng thành Xây dựng Bảo mật Vào) cho bảo mật phần mềm, TMMi (Test Maturity Model integration, cho kiểm thử), mô hình Agile Fluency, và các mô hình trưởng thành quản lý dữ liệu, cộng vô số bảng điểm nội bộ.

Với doanh nghiệp và đặc biệt là chính phủ, mô hình trưởng thành mang trọng lượng riêng. Hợp đồng chính phủ từ lâu dùng mức thẩm định CMMI làm tiêu chí đủ điều kiện nhà cung cấp, và các khung như CMMC của Hoa Kỳ ([Chứng nhận Mô hình Trưởng thành An ninh mạng](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) gắn trực tiếp mức trưởng thành an ninh mạng với tư cách đủ điều kiện cho công việc quốc phòng. Điều đó cho mô hình trưởng thành răng thật. Nó cũng tạo ra rủi ro trung tâm của chương này: khi một mức trở thành cổng hay mục tiêu, người ta tối ưu cho cuộc thẩm định thay vì năng lực nền tảng. Dùng tốt, mô hình trưởng thành là một tấm gương. Dùng tệ, chúng là sân khấu.

## Các nguyên tắc chính

- **Trưởng thành là phương tiện, không phải đích.** Mục tiêu là năng lực và kết quả, không phải một con số mức.
- **Đánh giá để học, không phải để chấm điểm.** Tự đánh giá trung thực thắng một thẩm định tâng bốc.
- **Cao hơn không phải lúc nào cũng tốt hơn.** Mục tiêu đúng phụ thuộc rủi ro, ngữ cảnh và chi phí.
- **Đo theo từng lĩnh vực, không phải một điểm toàn cục.** Năng lực không đồng đều; một con số đơn giấu điều đó.
- **Ưu tiên các khoảng trống trưởng thành thấp nhất, rủi ro cao nhất trước.**
- **Coi chừng [Định luật Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Một khi một mức là mục tiêu, nó thôi đo năng lực.
- **Đánh giá lại định kỳ.** Độ trưởng thành trôi khi con người, hệ thống và mối đe dọa thay đổi.

## Khuyến nghị

### Chọn mô hình đúng cho lĩnh vực

Hãy khớp mô hình với năng lực bạn muốn cải thiện, và ưu tiên các mô hình đã được thiết lập, dựa trên bằng chứng hơn những mô hình tự bịa nơi chúng tồn tại:

- **Quy trình và phân phối:** CMMI (độ trưởng thành quy trình rộng), mô hình năng lực DORA (hiệu suất phân phối, có cơ sở nghiên cứu, chương 11.2).
- **Bảo mật:** OWASP SAMM và BSIMM (thực hành bảo mật phần mềm), CMMC (an ninh mạng quốc phòng).
- **Kiểm thử và chất lượng:** TMMi.
- **Agile và cách làm việc:** mô hình Agile Fluency (chương 10.7).
- **Dữ liệu:** các mô hình trưởng thành quản lý dữ liệu (DMM, DCAM).

Cho sử dụng nội bộ, một thang bốn hoặc năm mức đơn giản áp dụng theo từng năng lực (như cuốn sách này làm) thường hành động được hơn một khung bên ngoài nặng nề. Hãy để dành các mô hình chính thức, được thẩm định cho nơi chúng bị yêu cầu theo hợp đồng.

### Đánh giá trung thực và theo từng năng lực

Hãy chạy các đánh giá tạo ra sự thật, không phải sự thoải mái. Đưa những người làm công việc vào cuộc. Thu thập bằng chứng thay vì ý kiến. Chấm điểm từng năng lực riêng, để bức tranh phản ánh thực tế: mạnh ở đây, yếu ở kia. Một tự đánh giá dùng để dẫn dắt cải thiện đáng giá hơn một thẩm định bên ngoài dùng để giành huy hiệu, vì cái đầu thưởng cho sự thẳng thắn còn cái sau thưởng cho cách trình bày. Chương 12.4 cung cấp một tự đánh giá hợp nhất qua mọi lĩnh vực trong cuốn sách này; hãy dùng nó như công cụ khởi đầu.

### Dùng độ trưởng thành để ưu tiên, không phải để trừng phạt

Đầu ra của một đánh giá là một tồn đọng cải thiện được ưu tiên, không phải phiếu điểm để đổ lỗi. Hãy kết hợp độ trưởng thành với rủi ro. Một năng lực mức 1 ở khu vực rủi ro thấp có thể ổn. Một năng lực mức 2 ở khu vực trọng yếu về an toàn hay tuân thủ là khẩn cấp. Hướng đầu tư vào các khoảng trống nơi độ trưởng thành thấp gặp rủi ro cao, và nối công việc với kết quả (chương 11.1) để cải thiện được đo bằng kết quả, không phải bằng việc leo bậc thang vì chính nó.

### Đặt mức mục tiêu có chủ đích: cao hơn không miễn phí

Mỗi mức lên tốn công sức và thường thêm trọng lượng quy trình. Mục tiêu đúng hiếm khi là "mức 5 ở mọi nơi." Đó là mức mà năng lực thêm vẫn biện minh được chi phí thêm cho rủi ro của lĩnh vực đó. Các năng lực bị quản lý và trọng yếu về an toàn có thể thực sự cần các nấc cao nhất, và kiểm toán thường đòi ít nhất mức 3 "được xác định." Nhiều cái khác được phục vụ tốt ở mức 3 và chỉ tích lũy quan liêu nếu đẩy xa hơn. Hãy quyết định mục tiêu theo từng năng lực, và dừng leo khi lợi tức điều chỉnh theo rủi ro dừng.

### Đề phòng sân khấu trưởng thành

Kiểu thất bại duy nhất phá hủy giá trị của mô hình trưởng thành là tối ưu cho điểm số. Hãy coi chừng những đánh giá chấm rộng rãi, bằng chứng chỉ được lắp cho cuộc thẩm định, hay tuyên bố "mức 5" mà sự cố sản xuất mâu thuẫn. Giữ đánh giá gắn với hành vi quan sát được và kết quả thật. Luân phiên hoặc kiểm tra tỉnh táo bên ngoài những người đánh giá. Coi tự chấm điểm cao đáng ngờ là mùi cần điều tra. Khoảnh khắc mức trở thành mục tiêu, mô hình thôi nói sự thật cho bạn.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| **Mô hình thẩm định chính thức (CMMI, CMMC)** | So sánh được, được hợp đồng công nhận, nghiêm ngặt | Tốn kém; mời gọi lách; có thể làm quy trình hóa đá |
| **Bảng điểm nội bộ nhẹ** | Nhanh, hành động được, chi phí chung thấp | Kém so sánh được với bên ngoài; dễ thiên kiến |
| **Mô hình năng lực dựa trên bằng chứng (DORA)** | Gắn với kết quả thật; có nghiên cứu hậu thuẫn | Phạm vi hẹp hơn; cần chỉ số thật |
| **Một điểm trưởng thành tổng thể** | Đơn giản để truyền đạt | Giấu năng lực không đồng đều; gây hiểu lầm |
| **Đánh giá theo từng năng lực** | Ưu tiên chính xác, hành động được | Nhiều công sức hơn; không có con số tiêu đề đơn |

Căng thẳng trung tâm là **đánh giá như tấm gương so với đánh giá như mục tiêu**. Cùng một mô hình giúp một đội nhìn rõ chính mình trở nên phản tác dụng ngay khi một mức được gắn với phần thưởng, tư cách đủ điều kiện hay địa vị. Một mức càng quan trọng, càng nhiều năng lượng chảy vào vẻ ngoài của độ trưởng thành thay vì bản chất.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta có nên giữ một tự đánh giá nội bộ thẳng thắn tách khỏi bất kỳ mức nào được thẩm định theo hợp đồng không, và ai sở hữu từng cái?** Khi một mức CMMC hay CMMI chặn doanh thu, thẩm định và sự thật trôi xa nhau, vì năng lượng chảy về hướng đạt thay vì cải thiện. Với doanh nghiệp lớn hay nhà cung cấp chính phủ, khoảng cách đó là nơi rủi ro ẩn: bạn qua kiểm toán và vẫn bị phơi nhiễm. Hãy chạy hai cuốn sổ có chủ đích. Giữ thẩm định chính thức cho tư cách đủ điều kiện, và giữ một bảng điểm nội bộ thẳng thừng mà không ai được thưởng vì thổi phồng. Nêu tên chủ sở hữu cho mỗi cái, và coi bất kỳ khoảng cách nào giữa chúng là tín hiệu để điều tra, không phải để che đậy. Hãy mang các sự cố gần đây, suýt xảy ra, và sự suy giảm sau thẩm định đến cuộc họp như bằng chứng cuốn sổ nào đang nói sự thật.

2. **Với mỗi lĩnh vực, chúng ta đang áp dụng một mô hình đã thiết lập dựa trên bằng chứng hay tự bịa bảng điểm của riêng mình, và đó có phải lựa chọn đúng không?** Các mô hình đã thiết lập (DORA cho phân phối, SAMM hoặc BSIMM cho bảo mật, TMMi cho kiểm thử) mang nghiên cứu và khả năng so sánh bên ngoài mà một lưới tự chế không sánh được. Một thang bốn mức nội bộ nhẹ nhanh hơn và hành động được hơn, và thường là lựa chọn tốt hơn cho chỉ đạo nội bộ. Cái bẫy là bịa ra một khung riêng nặng nề có mọi nghi thức của mô hình chính thức mà không có cơ sở bằng chứng nào. Hãy quyết định theo từng lĩnh vực: để dành mô hình thẩm định chính thức cho nơi hợp đồng đòi, dùng mô hình dựa trên bằng chứng nơi chúng tồn tại và phù hợp, và giữ một thang đơn giản theo từng năng lực cho mọi thứ còn lại. Hãy mang danh sách các lĩnh vực, đánh dấu mỗi cái hôm nay dùng mô hình nào, và thách thức mọi bảng điểm tự bịa.

3. **Ai chạy các đánh giá của chúng ta, làm sao chúng ta bắt được chấm rộng rãi, và bao lâu chúng ta đánh giá lại?** Một đánh giá tự chấm tự tâng bốc, và độ trưởng thành trôi khi con người, hệ thống và mối đe dọa thay đổi, nên một thẩm định hai năm tuổi thường là hư cấu. Hãy luân phiên người đánh giá hoặc đưa vào một kiểm tra tỉnh táo bên ngoài, và coi tự chấm điểm cao đáng ngờ là mùi cần đuổi theo, không phải chiến thắng để ăn mừng. Đặt nhịp đánh giá lại gắn với tốc độ mỗi lĩnh vực thay đổi: bảo mật thường xuyên hơn, chẳng hạn, tài liệu. Hãy thu thập bằng chứng và đưa những người làm công việc vào cuộc thay vì thu ý kiến từ quản lý. Nếu câu trả lời của bạn là một đội tự chấm điểm một lần một năm không có kiểm tra chéo, bạn đang đo sự thoải mái, không phải năng lực.

4. **Mỗi năng lực thực sự cần mức trưởng thành mục tiêu nào, và đẩy cao hơn ở đâu chỉ mua cho chúng ta trọng lượng quy trình?** Cao hơn không miễn phí: mỗi mức lên tốn công sức và thường thêm nghi thức, nên mục tiêu mức 5 ở mọi nơi rút ngân sách cải thiện hữu hạn vào quan liêu mà một số lĩnh vực sẽ không bao giờ hoàn vốn. Với tổ chức lớn mục tiêu đúng thay đổi theo năng lực, vì một khu vực rủi ro thấp ở mức 2 có thể hoàn toàn an toàn trong khi một khu vực trọng yếu về an toàn hay tuân thủ ở cùng mức là tình huống khẩn cấp. Hãy mang xếp hạng rủi ro theo từng năng lực, ước tính trung thực nấc kế tiếp tốn bao nhiêu công sức và quy trình, và bất kỳ ngưỡng sàn kiểm toán hay hợp đồng nào, vì nhiều kiểm toán đòi ít nhất mức 3 được xác định. Trong bối cảnh doanh nghiệp và chính phủ, một số năng lực bị quản lý thực sự cần các nấc cao nhất trong khi hầu hết được phục vụ tốt ở mức 3, nên hãy quyết định mục tiêu có chủ đích, từng năng lực một, và dừng leo khi lợi tức điều chỉnh theo rủi ro dừng.

5. **Lần cuối chúng ta nâng một mức trưởng thành, kết quả nó nhằm bảo vệ có thực sự cải thiện, hay chỉ điểm số dịch chuyển?** Một mức leo lên trong khi sự cố, thời gian chờ hay tỷ lệ lỗi đứng yên là Định luật Goodhart đang vận hành: một khi con số trở thành mục tiêu, nó thôi đo năng lực. Với đội lớn điều này dễ trượt qua, vì một thẩm định thành công cảm giác như tiến bộ ngay cả khi môi trường sản xuất kể chuyện khác. Hãy gắn mức của từng năng lực với một chỉ số kết quả thật trước khi bạn đầu tư, rồi mang bằng chứng trước-và-sau đến cuộc thảo luận: sự cố mỗi quý, tỷ lệ thay đổi thất bại, thời gian khôi phục, bất cứ thứ gì năng lực đó tồn tại để cải thiện. Trong danh mục doanh nghiệp và chính phủ nơi một mức được thẩm định chặn tư cách đủ điều kiện, khoảng cách là nguy hiểm, vì mức có thể tăng nhờ bằng chứng được lắp ráp trong khi thực hành nền tảng lặng lẽ suy tàn, và bằng chứng đầu tiên của điều đó là một vụ vi phạm, sự cố hay kiểm toán thất bại.

6. **Chúng ta truyền đạt một điểm trưởng thành tiêu đề duy nhất hay một bức tranh theo từng năng lực, và các mức có bao giờ bị gắn với phần thưởng, xếp hạng hay vị thế của đội không?** Một con số tổng thể duy nhất dễ trình bày cho lãnh đạo và giấu đúng sự không đồng đều quan trọng, vì phân phối mạnh có thể che một năng lực bảo mật mức 1; một bản đồ nhiệt theo từng năng lực tốn công hơn nhưng cho thấy nơi độ trưởng thành thấp gặp rủi ro cao. Câu hỏi khó hơn là điểm số được dùng thế nào, vì khoảnh khắc một mức gắn với phần thưởng hay xếp hạng của đội, báo cáo trung thực chết và năng lượng chảy vào vẻ ngoài của độ trưởng thành thay vì bản chất. Hãy mang bản đồ nhiệt, và một lời kể thẳng thắn về mọi nơi một mức hiện đang nuôi đánh giá hiệu suất, quyết định ngân sách hay bảng điểm nhà cung cấp. Với doanh nghiệp và nhà cung cấp chính phủ, nơi các mức được thẩm định có thể chặn doanh thu và tư cách đủ điều kiện, hãy tường minh điểm nào mang hệ quả và điểm nào chỉ để chỉ đạo, vì một bức tranh trưởng thành mà người ta được thưởng khi thổi phồng thôi mô tả thực tế.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Một mô hình thẩm định nặng nề là chi phí chung bạn không đủ sức gánh trên đường băng ngắn. Hãy chạy một tự đánh giá một giờ trên thang đơn giản qua một nhúm năng lực, chỉ sửa khoảng trống trưởng thành thấp nhất chặn một thứ cụ thể (chẳng hạn, bảng câu hỏi bảo mật từ khách hàng doanh nghiệp đầu tiên của bạn), và để yên phần còn lại. Đánh giá nên tốn một buổi chiều, không phải một nhà tư vấn, và đầu ra của nó là một hành động tiếp theo duy nhất thay vì một điểm cao đồng đều mà bạn không cần và không tài trợ nổi.

**Doanh nghiệp nhỏ.** Không có người đánh giá riêng và ngân sách eo hẹp, hãy mượn một mô hình công khai nhẹ thay vì đặt hàng một khung riêng: một danh mục kiểm tra phân phối hoặc bảo mật ngắn bạn tự chấm điểm được. Coi nó như cuộc trò chuyện hằng năm về nơi một điểm yếu sẽ khiến bạn mất khách hàng, không phải chương trình thường trực. Giữ nó rẻ và thẳng thừng, vì một điểm tâng bốc bạn trả tiền cho nhà cung cấp tạo ra có giá trị thấp hơn một điểm thẳng thắn bạn tự làm trong một buổi chiều.

**Doanh nghiệp lớn.** Giá trị là một bảng điểm theo từng năng lực dùng chung, áp dụng nhất quán qua nhiều đội, để khoảng trống so sánh được và ngân sách cải thiện chảy tới nơi độ trưởng thành thấp gặp rủi ro cao. Hãy đề phòng mạnh sân khấu trưởng thành một khi các mức nuôi ngân sách hay vị thế: luân phiên hoặc kiểm tra tỉnh táo bên ngoài những người đánh giá, và quản lý kết quả như bản đồ nhiệt hướng đầu tư đường lát sẵn (chương 4.2) thay vì bảng xếp hạng xếp hạng các đội và giết báo cáo trung thực.

**Chính phủ.** Một mức trưởng thành thường là cổng theo nghĩa đen ở đây: CMMC cho công việc quốc phòng, thẩm định CMMI làm tiêu chí nhà cung cấp. Hãy đạt mức yêu cầu bằng năng lực thật, và giữ tự đánh giá nội bộ thẳng thắn tách khỏi thẩm định chính thức để ngưỡng sàn kiểm toán không bao giờ lặng lẽ thành trần. Lập tài liệu bằng chứng minh bạch cho người thẩm định, và coi bất kỳ khoảng cách nào giữa mức được chứng nhận và thực hành thật là rủi ro chịu trách nhiệm cần đóng, không phải giấy tờ để nộp.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp SaaS mười người chạy tự đánh giá một giờ theo thang bốn mức đơn giản bao quát phân phối, kiểm thử, bảo mật và trực ca. Nó thấy phân phối và kiểm thử ở mức 3 nhưng bảo mật kẹt ở mức 1, điều quan trọng vì nó sắp ký khách hàng doanh nghiệp đầu tiên kèm bảng câu hỏi bảo mật. Vì vậy những người sáng lập dành tháng tới chỉ nâng bảo mật lên mức 2 bảo vệ được và để yên phần còn lại, thay vì đuổi theo điểm cao đồng đều mà họ chưa cần và chưa đủ sức chi trả.

**Doanh nghiệp lớn.** Một công ty dịch vụ tài chính đánh giá 40 đội của mình bằng bảng điểm theo từng năng lực nhẹ (phân phối, kiểm thử, bảo mật, khả năng quan sát, trực ca). Bản đồ nhiệt cho thấy độ trưởng thành bảo mật tụt sau nhiều nhất ở nơi phơi nhiễm quy định cao nhất, nên đội nền tảng tài trợ công cụ bảo mật đường lát sẵn (chương 4.2) cho các đội đó trước. Vì đánh giá được dùng để ưu tiên đầu tư thay vì xếp hạng các đội, quản lý báo cáo trung thực. Đánh giá lại một năm sau cho thấy dịch chuyển thật, và, quan trọng nhất, ít sự cố bảo mật hơn, không chỉ điểm cao hơn.

**Chính phủ.** Một nhà thầu quốc phòng phải đạt một mức CMMC yêu cầu để đấu thầu, và một nhà tích hợp hệ thống giữ thẩm định CMMI làm tiêu chí hợp đồng. Ở đây mức trưởng thành là cổng theo nghĩa đen đến doanh thu. Phiên bản chạy tốt coi mức yêu cầu là ngưỡng sàn cho năng lực thật và giữ tự đánh giá nội bộ thẳng thắn tách khỏi thẩm định chính thức. Phiên bản chạy tệ lắp bằng chứng cho thẩm định và để thực hành thật suy tàn ngay ngày hôm sau, qua kiểm toán mà vẫn bị phơi nhiễm.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của đánh giá độ trưởng thành đến từ **đầu tư có định hướng**. Ngân sách cải thiện là hữu hạn. Chi tiêu mù quáng, chúng tài trợ bất cứ thứ gì ồn ào nhất. Một đánh giá độ trưởng thành cho bạn thấy năng lực yếu nhất ở đâu so với rủi ro, nên cùng khoản chi mua được nhiều giảm rủi ro và cải thiện kết quả hơn. Bản thân đánh giá rẻ, chỉ vài ngày rà soát có cấu trúc, dựa trên bằng chứng, đặt cạnh chi phí của các chương trình cải thiện phân bổ sai hoặc, tệ hơn, một khoảng trống năng lực không bị phát hiện nổi lên như vụ vi phạm, sự cố hay kiểm toán thất bại.

Về **tổng chi phí sở hữu**, kỷ luật này tốn ít khi bạn giữ nó nhẹ và tốn nhiều khi nó cứng thành quan liêu thẩm định. Chi phí ẩn chi phối là *sân khấu trưởng thành*: công sức bỏ ra tạo vẻ ngoài của độ trưởng thành không trả lại gì và có thể che rủi ro thật, tức ROI âm. Để lập luận với ban lãnh đạo, hãy trình bày độ trưởng thành như lăng kính rủi ro-và-đầu tư, một bản đồ nhiệt biến "cải thiện mọi thứ" thành "cải thiện ba thứ này trước," và lập ngân sách tường minh chống lại cám dỗ đuổi theo các mức vì chính chúng. Nơi một mức được yêu cầu theo hợp đồng (CMMC, CMMI), ROI là trực tiếp: đó là giá của tư cách đủ điều kiện, và mục tiêu là đáp ứng nó bằng năng lực thật thay vì giả vờ tốn kém.

## Phản mẫu và cạm bẫy

- **Mức như mục tiêu:** đuổi theo một con số thay vì năng lực nó được cho là đại diện.
- **Sân khấu trưởng thành:** lắp bằng chứng cho thẩm định trong khi thực hành thật suy tàn.
- **Một điểm toàn cục:** một điểm trưởng thành đơn giấu sự không đồng đều nguy hiểm.
- **Cao hơn luôn tốt hơn:** đẩy mọi năng lực lên mức 5 bất kể rủi ro hay chi phí.
- **Đánh giá một lần, không bao giờ nữa:** một thẩm định một lần bị coi là sự thật vĩnh viễn.
- **Xếp hạng đội để đổ lỗi:** dùng độ trưởng thành để trừng phạt, điều giết báo cáo trung thực.
- **Sùng bái mô hình:** theo nghi thức của một khung nặng nề quá điểm hữu ích.
- **Phớt lờ kết quả:** leo bậc thang trong khi phân phối, độ tin cậy hay bảo mật không cải thiện.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu.** Không có khái niệm chung về độ trưởng thành; năng lực được giả định, không đồng đều và không được đo; bất kỳ đánh giá nào cũng phản ứng, được kích hoạt bởi sự cố hay yêu cầu kiểm toán thay vì được lên kế hoạch.
- **Mức 2, Phát triển.** Một vài đội chạy đánh giá tùy nghi theo một thang nào đó, nhưng mô hình, nhịp và độ nghiêm ngặt khác nhau theo đội; kết quả được dùng không nhất quán và bằng chứng mỏng, nên chấm điểm cho vẻ ngoài là rủi ro luôn hiện diện.
- **Mức 3, Chuẩn hóa.** Một mô hình theo từng năng lực duy nhất và nhịp đánh giá được lập tài liệu và áp dụng toàn tổ chức; các đánh giá dựa trên bằng chứng, đưa những người làm công việc vào cuộc, và nuôi một tồn đọng cải thiện được ưu tiên thay vì phiếu điểm.
- **Mức 4, Quản lý.** Độ trưởng thành được đo và kiểm soát bằng dữ liệu: mức của từng năng lực được theo dõi theo đường cơ sở, gắn với một chỉ số kết quả (sự cố, thời gian chờ, tỷ lệ thay đổi thất bại), và đánh giá lại theo nhịp đã định, nên trôi dạt và chấm rộng rãi hiện ra thành con số thay vì ý kiến, và mục tiêu được đặt có chủ đích theo từng lĩnh vực so với rủi ro và chi phí.
- **Mức 5, Điều phối.** Đánh giá được tích hợp trong toàn tổ chức và cải thiện liên tục: độ trưởng thành, rủi ro và kết quả thông tin đầu tư như một bức tranh thích ứng duy nhất, mục tiêu được cân bằng lại khi mối đe dọa và ngữ cảnh dịch chuyển, người đánh giá được luân phiên hoặc kiểm tra bên ngoài như lẽ thường, và thực hành chủ động cho nghỉ hưu nghi thức không còn xứng chi phí của nó.

## Ý tưởng để thảo luận

1. Năng lực nào của bạn đang được giả định là trưởng thành mà không có bằng chứng?
2. Độ trưởng thành thấp nhất của bạn trùng với rủi ro cao nhất ở đâu, và đó có phải nơi ngân sách cải thiện của bạn đang đi không?
3. Có mức trưởng thành nào trong tổ chức của bạn là mục tiêu hay cổng không? Hành vi nào nó đã tạo ra?
4. Mức mục tiêu đúng cho từng năng lực là gì, và leo cao hơn ở đâu chỉ thêm quan liêu?
5. Các đội của bạn sẽ báo cáo độ trưởng thành của họ trung thực, hay cách bạn dùng điểm số trừng phạt sự thẳng thắn?
6. Lần cuối bạn "cải thiện độ trưởng thành," kết quả có thực sự thay đổi không?

## Những điểm cần ghi nhớ

- Một mô hình trưởng thành đánh giá năng lực theo bậc thang các mức và mô tả con đường cải thiện: một tấm gương, không phải cúp.
- Chọn mô hình đã thiết lập, dựa trên bằng chứng theo từng lĩnh vực (CMMI, DORA, SAMM/BSIMM, CMMC); một thang theo từng năng lực nhẹ thường hành động được nhất.
- **Đánh giá trung thực, theo từng năng lực**, và dùng kết quả để **ưu tiên theo rủi ro**, không phải để xếp hạng hay đổ lỗi.
- **Cao hơn không phải lúc nào cũng tốt hơn:** đặt mức mục tiêu có chủ đích so với rủi ro và chi phí.
- Coi chừng **sân khấu trưởng thành** và **Định luật Goodhart**: một mức trở thành mục tiêu thôi đo năng lực.
- Xem chương 12.4 cho tự đánh giá trưởng thành hợp nhất của cuốn sách này, và phần trưởng thành riêng của mỗi chương.

## Tài liệu tham khảo và đọc thêm

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (nguồn gốc của độ trưởng thành quy trình phần mềm).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (tư duy năng lực, không phải mức trưởng thành, cho phân phối).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore và Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), về cách dùng và lạm dụng của chúng.
