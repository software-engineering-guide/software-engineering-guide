# 5.8 Nghiên cứu thiết kế và kiểm thử khả dụng

## Tổng quan và động lực

[Nghiên cứu người dùng](https://en.wikipedia.org/wiki/User_research) là kỷ luật tìm hiểu về những người bạn xây dựng cho: mục tiêu, bối cảnh, nhiệm vụ của họ, và những chướng ngại khiến họ vấp. Giá trị cốt lõi của nó là giảm rủi ro. Sai lầm tốn kém nhất trong phần mềm không phải là một lỗi hay hạn chót bị lỡ; mà là xây sai thứ một cách tốt, rồi phát hiện sau ra mắt rằng không ai cần nó hoặc không ai dùng được. Nghiên cứu mua giảm rủi ro đó một cách rẻ, trước khi bạn đổ công sức kỹ thuật vào một hướng hóa ra sai. Chương 5.1 đặt nền tảng UX; chương này đi sâu vào hai động cơ giữ những nền tảng ấy trung thực, nghiên cứu sinh tạo cho bạn biết cần xây gì và nghiên cứu đánh giá cho bạn biết cái bạn xây có thực sự hoạt động không.

Với các đội lớn, rủi ro nhân lên. Khi nhiều nhóm phát hành vào một sản phẩm, mỗi nhóm đặt cược về người dùng mỗi sprint, và không có thói quen nghiên cứu chung, những canh bạc đó chỉ là ý kiến khoác bộ đồ của sự tự tin. Một dòng bằng chứng nhỏ, đều đặn cho mọi người cùng một thực tế để tranh luận, nên các cuộc tranh luận kết thúc bằng "hãy đi xem vài người dùng" thay vì bằng ai có thâm niên nhất hoặc giọng to nhất. Nghiên cứu cũng đi xa: một nghiên cứu được chạy tốt có thể sửa các giả định của cả chục đội cùng lúc, nếu bạn nắm bắt và chia sẻ nó tốt.

Doanh nghiệp và chính phủ nâng thanh chuẩn lên nữa. Phần mềm doanh nghiệp thường có người dùng bị giữ chân không thể bỏ, nên các công cụ không dùng được bị trả giá bằng lỗi, đào tạo và giờ mất thay vì sự rời bỏ bạn thấy trên bảng điều khiển. Dịch vụ chính phủ với tới toàn thể công chúng, bao gồm người đang khủng hoảng, dùng điện thoại cũ, kém tự tin về số, hoặc không có lựa chọn nào khác. Nhiều tiêu chuẩn dịch vụ số quốc gia nay biến nghiên cứu người dùng thành bắt buộc chính vì lý do này, vì một biểu mẫu không ai hoàn thành được từ chối mọi người khoản trợ cấp họ được hưởng. Ở đây nghiên cứu không phải điều dễ chịu. Nó là cách bạn giữ một lời hứa công.

## Các nguyên tắc chính

- Nghiên cứu giảm rủi ro xây sai thứ; nó rẻ nhất trước khi bạn xây, không phải sau.
- Nghiên cứu sinh tạo tìm đúng vấn đề; nghiên cứu đánh giá kiểm tra giải pháp. Bạn cần cả hai.
- Xem người ta làm gì, không chỉ nói gì; sở thích đã nêu và hành vi thực phân kỳ.
- Phương pháp định tính giải thích vì sao; phương pháp định lượng định cỡ bao nhiêu. Hãy ghép chúng.
- Nhỏ và liên tục thắng hiếm và nặng nề. Vài người dùng mỗi tuần học nhiều hơn một nghiên cứu lớn mỗi năm.
- Phát hiện của bạn chỉ đại diện như người tham gia của bạn, nên hãy tuyển có chủ đích, bao gồm người dùng khuyết tật và khó tiếp cận.
- Hiểu biết sống trong bộ slide của một đội là hiểu biết mất đi. Hãy nắm bắt nghiên cứu để cả tổ chức tái sử dụng được.
- Thiên kiến len vào qua câu hỏi dẫn dắt và tổng hợp theo ước muốn; hãy thiết kế chống lại nó có chủ đích.

## Khuyến nghị

### Tách nghiên cứu sinh tạo khỏi nghiên cứu đánh giá

Hãy tường minh về câu hỏi bạn đang đặt, vì các phương pháp khác nhau. Nghiên cứu sinh tạo (hay khám phá) là mở đầu và khám phá không gian vấn đề trước khi bạn có giải pháp: Mọi người thực sự đang cố hoàn thành điều gì? Trải nghiệm hiện tại gây đau ở đâu? Họ lách qua cái gì? Nghiên cứu đánh giá kiểm thử một thiết kế cụ thể đối với một nhiệm vụ: Mọi người có hoàn thành được không, và họ vấp ở đâu? Nhầm lẫn hai thứ lãng phí cả hai. Chạy một phiên [kiểm thử khả dụng](https://en.wikipedia.org/wiki/Usability_testing) có kịch bản chặt khi bạn còn chưa hiểu vấn đề cho bạn những câu trả lời bóng bẩy cho sai câu hỏi, trong khi một cuộc trò chuyện không cấu trúc khi bạn cần xác thực một luồng thanh toán để bạn đoán mò. Hãy gọi tên câu hỏi nghiên cứu trước, rồi chọn phương pháp, và đưa phát hiện sinh tạo vào khám phá sản phẩm (chương 10.14) nơi lộ trình thực sự được định hình.

### Khớp phương pháp với câu hỏi

Không có phương pháp đa dụng, chỉ có độ phù hợp. Phỏng vấn người dùng phơi bày động cơ, mô hình tinh thần và lịch sử, và là con ngựa thồ của bạn cho khám phá. [Điều tra theo ngữ cảnh](https://en.wikipedia.org/wiki/Contextual_inquiry), nơi bạn quan sát mọi người làm công việc thực trong môi trường của chính họ, hé lộ những cách lách và gián đoạn mà người ta không bao giờ nhắc trong phòng họp. Khảo sát đo thái độ và tần suất qua một quần thể lớn nhưng không giải thích được lý do đằng sau, và trừng phạt tàn bạo việc thiết kế câu hỏi cẩu thả. [Phân loại thẻ](https://en.wikipedia.org/wiki/Card_sorting) và kiểm thử cây suy ra và xác thực kiến trúc thông tin từ mô hình tinh thần của người dùng: phân loại thẻ yêu cầu mọi người nhóm và gắn nhãn khái niệm, trong khi kiểm thử cây kiểm tra liệu họ có tìm được thứ trong một cấu trúc đề xuất. Nghiên cứu nhật ký nắm bắt hành vi diễn ra qua nhiều ngày hay tuần, như làm quen hay hình thành thói quen, mà không phiên đơn lẻ nào thấy được. Một quy tắc kinh nghiệm đơn giản: dùng phỏng vấn và điều tra theo ngữ cảnh để hiểu con người, phân loại thẻ và kiểm thử cây để cấu trúc thông tin, khảo sát và nghiên cứu nhật ký để thấy qua thời gian và quy mô, và kiểm thử khả dụng để kiểm tra một thiết kế.

### Chạy kiểm thử khả dụng sớm, thường xuyên và nhỏ

Kiểm thử khả dụng là phương pháp đánh giá có đòn bẩy cao nhất đơn lẻ, và bạn có thể bắt đầu nó với bản phác thảo giấy rất lâu trước khi có mã. Quy tắc kinh nghiệm nổi tiếng là khoảng năm người dùng mỗi vòng phơi bày phần lớn các vấn đề khả dụng nghiêm trọng, hiển nhiên, nên bạn tốt hơn nên chạy ba vòng năm người khi thiết kế tiến hóa hơn một nghiên cứu lớn mười lăm người ở cuối. Tuy nhiên hãy hiểu các giới hạn của quy tắc. Năm người dùng chỉ đủ cho một nhóm đồng nhất khám phá các vấn đề lớn; nó không đo tỷ lệ thành công, không bao quát các phân khúc người dùng riêng biệt (mỗi nhóm khác biệt đáng kể cần một nhúm riêng), và không bắt được các vấn đề hiếm nhưng nghiêm trọng. Hãy chọn kiểm thử có điều phối khi bạn muốn dò lập luận, thích ứng tại chỗ, và xử lý nhiệm vụ phức tạp hay nhạy cảm, và kiểm thử không điều phối khi bạn muốn tốc độ, khối lượng, tầm với địa lý và chi phí thấp hơn cho các luồng đơn giản. Hầu hết các đội trưởng thành chạy cả hai: có điều phối để hiểu, không điều phối để xác nhận ở quy mô.

### Viết nhiệm vụ và câu hỏi không dẫn dắt người tham gia

Nghiên cứu của bạn chỉ đáng tin như giao thức của bạn, và cách nhanh nhất để phá hỏng nó là báo trước câu trả lời bạn hy vọng. Hãy cho người tham gia mục tiêu thực tế, không phải chỉ dẫn: nói "bạn vừa chuyển nhà và cần cập nhật địa chỉ" thay vì "nhấp nút Chỉnh sửa Hồ sơ và đổi địa chỉ của bạn." Hỏi về hành vi quá khứ thay vì ý định tương lai, vì "bạn có dùng cái này không?" chắc chắn tạo ra những lời nói dối lịch sự trong khi "hãy kể về lần cuối bạn làm việc này" tạo ra sự thật. Tránh những câu hỏi giả định kết luận của chính chúng, và cảnh giác với [thiên kiến xác nhận](https://en.wikipedia.org/wiki/Confirmation_bias), xu hướng con người chú ý và nhớ bằng chứng ủng hộ điều bạn đã tin. Nhà nghiên cứu viết ra thiết kế không nên lặng lẽ huấn luyện người tham gia hướng tới thành công, và đội theo dõi nên ghi lại điều đã xảy ra trước khi tranh luận nó nghĩa là gì. Khi bạn tách thiết kế và truyền đạt nhiệm vụ khỏi thiết kế sản phẩm (chương 5.4), bạn có tín hiệu sạch hơn.

### Tuyển người tham gia thực sự đại diện cho người dùng của bạn

Phát hiện thừa hưởng thiên kiến của việc tuyển người. Nếu bạn chỉ bao giờ kiểm thử với những tình nguyện viên tự tin, có kết nối, thoải mái với công nghệ, bạn sẽ phát hành thứ hoạt động tuyệt vời cho những người gần như không cần giúp và thất bại với những người cần nhất. Hãy xác định phân khúc của bạn, rồi tuyển đối chiếu với chúng có chủ đích, bao gồm người dùng khuyết tật dựa vào công nghệ hỗ trợ (chương 5.3) và các nhóm khó tiếp cận như người đang khủng hoảng, người kém tự tin về số, người dùng lớn tuổi, và những người trên kết nối chậm hay thiết bị cũ. Tiếp cận những người tham gia này tốn nhiều công sức hơn và thường cần hợp tác với tổ chức cộng đồng, ưu đãi phù hợp, và hậu cần linh hoạt, nhưng bỏ qua nó không làm người dùng biến mất; nó chỉ chuyển khám phá sang môi trường thực, nơi đắt hơn nhiều và gây hại hơn nhiều. Hãy sàng lọc cẩn thận để bạn có thành viên thật của một phân khúc thay vì người kiểm thử chuyên nghiệp lách ưu đãi.

### Tổng hợp phát hiện thành quyết định, không chỉ báo cáo

Quan sát thô không phải hiểu biết. Công việc tổng hợp là biến một đống ghi chép phiên thành một số ít quyết định mà đội có thể hành động. Lập bản đồ ái lực, gom các quan sát riêng lẻ thành chủ đề (thực hành đằng sau [sơ đồ ái lực](https://en.wikipedia.org/wiki/Affinity_diagram)), là bước đi chuẩn để làm các mẫu hiện ra qua các phiên. Với các nghiên cứu nặng phỏng vấn, một [phân tích chủ đề](https://en.wikipedia.org/wiki/Thematic_analysis) nhẹ giữ bạn trung thực về chủ đề nào thực sự được dữ liệu ủng hộ. Hãy gộp các mẫu bền vững vào các mô hình dùng chung từ chương 5.1, persona dựa trên bằng chứng và bản đồ hành trình, để hiểu biết cộng dồn thay vì bay hơi. Phép thử của tổng hợp tốt đơn giản: một quyết định có thay đổi không? Một nghiên cứu tạo ra một bộ slide đẹp mà không mục lộ trình nào đổi là sân khấu. Hãy kết thúc mọi nghiên cứu bằng một danh sách ngắn, được xếp hạng các phát hiện và một hành động đề xuất cho mỗi cái.

### Đối chiếu chéo nghiên cứu định tính với phân tích và thí nghiệm

Nghiên cứu định tính và dữ liệu định lượng trả lời hai nửa khác nhau của cùng một câu hỏi, và mỗi bên bao quát điểm mù của bên kia. Nghiên cứu giải thích vì sao người dùng hành xử như vậy nhưng chỉ thấy một nhúm người trong phòng; phân tích và thí nghiệm (chương 7.4) thấy toàn bộ quần thể nhưng không giải thích được động cơ hay bắt vấn đề của những người chưa bao giờ trở thành người dùng. Hãy dùng chúng như một vòng lặp: phân tích cho thấy một chỗ rơi, nghiên cứu giải thích nó, một thiết kế lại xử lý nó, và một thí nghiệm đo liệu bản sửa có dịch chuyển con số. Khi tín hiệu định tính và định lượng bất đồng, hãy coi mâu thuẫn là một manh mối thay vì phiền toái, vì thường một trong chúng đang đo thứ bạn không nhận ra mình đang đo. Không nguồn nào là sếp của nguồn kia; quyết định đến từ việc đọc chúng cùng nhau.

### Xây vận hành nghiên cứu để nghiên cứu mở rộng được

Ngay khi hơn một vài đội làm nghiên cứu, nút thắt thôi là phương pháp và trở thành hậu cần: tuyển người, lập lịch, đồng ý, ưu đãi, lưu ghi chú, và tìm nghiên cứu quý trước trước khi ai đó chạy lại. Vận hành nghiên cứu (ResearchOps) là thực hành làm bộ máy đó đáng tin. Hãy đầu tư vào một kho hiểu biết tìm kiếm được để phát hiện được gắn thẻ, khám phá được và tái sử dụng được qua các đội; một hệ thống quản lý người tham gia tôn trọng sự đồng ý, quyền riêng tư, và tần suất bạn liên hệ mọi người; và một nhịp nghiên cứu đều đặn để các nghiên cứu là thói quen ổn định thay vì cuộc chạy vạy. Dân chủ hóa nghiên cứu, để người không phải nhà nghiên cứu chạy một số nghiên cứu, đáng làm nhưng chỉ với lan can: mẫu, đào tạo và rà soát, để bạn mở rộng khối lượng học mà không mở rộng khối lượng giao thức tồi và kết luận thiên kiến.

## Đánh đổi: ưu và nhược điểm

| Phương pháp | Tốt nhất cho | Ưu điểm | Nhược điểm |
| --- | --- | --- | --- |
| Phỏng vấn người dùng | Khám phá, động cơ | Vì sao sâu, linh hoạt, rẻ để bắt đầu | N nhỏ, dễ thiên kiến người phỏng vấn |
| Điều tra theo ngữ cảnh | Hành vi thế giới thực | Hé lộ cách lách và ngữ cảnh | Tốn thời gian, khó lập lịch |
| Khảo sát | Thái độ ở quy mô | N lớn, định lượng được | Không giải thích được vì sao, dễ viết tồi |
| Phân loại thẻ và kiểm thử cây | Kiến trúc thông tin | Đặt cấu trúc trên mô hình tinh thần | Phạm vi hẹp, cần phân tích cẩn thận |
| Nghiên cứu nhật ký | Hành vi theo thời gian | Nắm bắt mẫu theo chiều dọc | Bỏ dở cao, công sức người tham gia |
| Kiểm thử khả dụng có điều phối | Hiểu một thiết kế | Dò hỏi, thích ứng, phong phú | Chậm hơn, tốn hơn, nặng lập lịch |
| Kiểm thử khả dụng không điều phối | Xác nhận ở quy mô | Nhanh, rẻ, rộng về địa lý | Không có theo dõi, nông với nhiệm vụ phức tạp |

Căng thẳng trung tâm là chiều sâu so với quy mô, và cách giải quyết là sắp xếp trình tự hơn là chọn. Hãy dùng phương pháp sâu, định tính, N nhỏ để hiểu và sinh giả thuyết, rồi dùng phương pháp rộng, định lượng để định cỡ và xác nhận chúng. Căng thẳng thứ hai là tốc độ so với sự chặt chẽ: nghiên cứu nhẹ liên tục giữ đội học mỗi tuần, nhưng chính tốc độ khiến nó có giá trị cũng khiến dễ cắt góc về tuyển người và giao thức. Hãy giải quyết bằng cách khớp sự chặt chẽ với khả năng đảo ngược. Hãy dành sự cẩn thận phương pháp thực sự cho các quyết định tốn kém để hoàn tác (luồng lõi, kiến trúc thông tin, cược nền tảng) và di chuyển nhanh, lỏng lẻo trên những chi tiết bạn có thể đổi sprint tới.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi chúng ta đặt một cược sản phẩm, phần nghiên cứu nhỏ nhất nào sẽ làm chúng ta đổi ý, và chúng ta có sẵn lòng chạy nó trước khi cam kết không?** Các đội yêu nghiên cứu về nguyên tắc và bỏ qua nó dưới áp lực hạn chót, nên câu hỏi thực là liệu bằng chứng có bất kỳ thẩm quyền nào đối với lộ trình không. Hãy quyết định trước cái gì được tính là bằng chứng bác bỏ, vì một nghiên cứu bạn sẽ phớt lờ bất kể kết quả là lãng phí thời gian của mọi người và là một dạng sân khấu. Điều này quan trọng nhất với các quyết định tốn kém để đảo ngược, nơi một tuần khám phá là tầm thường so với nhiều tháng xây sai thứ. Hãy mang một quyết định hiện tại và nêu tên, thành tiếng, phát hiện nào sẽ làm bạn đổi hướng. Nếu không phát hiện nào có thể đổi nó, bạn không làm nghiên cứu, bạn đang thu thập sự trấn an, và bạn nên hoặc cam kết trung thực hoặc mở lại quyết định.

2. **Những người chúng ta kiểm thử có thực sự giống những người dùng sản phẩm không, đặc biệt là những người vật lộn nhiều nhất?** Tuyển tình nguyện viên tự tin, có kết nối, sẵn sàng thì thoải mái, và sự thoải mái đó tạo ra một cái đọc tâng bốc và sai về độ khả dụng thực của sản phẩm. Những người dùng cần phần mềm hoạt động tốt nhất, người dùng khuyết tật, người đang khủng hoảng, người kém tự tin về số, thường là khó tuyển nhất, nên họ lặng lẽ rơi khỏi mẫu trừ khi bạn chiến đấu vì họ. Hãy lấy nhân khẩu học người tham gia từ ba nghiên cứu gần nhất và đặt chúng cạnh cơ sở người dùng thực hay nghĩa vụ dịch vụ công của bạn. Nếu chúng lệch về người dùng dễ tiếp cận, sự tự tin của bạn bị đặt sai chỗ, và bạn nên sửa đường ống tuyển người, hợp tác với tổ chức cộng đồng, và điều chỉnh ưu đãi trước khi bạn tin thêm một vòng phát hiện.

3. **Phát hiện nghiên cứu của chúng ta sống ở đâu, và một đội khác có thể tìm và tái sử dụng chúng sáu tháng sau không?** Trong một tổ chức lớn cùng một câu hỏi được nghiên cứu hết lần này đến lần khác vì không ai tìm được câu trả lời mà đội đầu đã trả tiền, là sự lãng phí thuần túy khoác áo cần mẫn. Hãy quyết định ai sở hữu kho hiểu biết, các nghiên cứu được gắn thẻ và tóm tắt thế nào, và bản viết tối thiểu khả thi là gì để nắm bắt một phát hiện đủ nhanh để người ta thực sự làm. Hãy cân nhắc điều gì xảy ra với sự đồng ý và quyền riêng tư của người tham gia khi phát hiện được tái sử dụng và chia sẻ, vì tái sử dụng không cẩn thận là vấn đề tuân thủ và niềm tin. Hãy mang một quyết định gần đây và thử truy bằng chứng đằng sau nó. Nếu bạn không tìm được nghiên cứu trong vài phút, nghiên cứu của bạn đang bay hơi nhanh hơn bạn tạo ra nó.

4. **Khi chúng ta trích dẫn quy tắc "khoảng năm người dùng," sản phẩm này thực sự phục vụ bao nhiêu phân khúc riêng biệt, và chúng ta có đang kiểm thử một mẫu thực của từng cái không?** Quy tắc năm-người-dùng trở thành cái bẫy khi một sản phẩm có nhiều nhóm người dùng khác biệt đáng kể, vì năm người tham gia từ một nhóm không cho bạn biết gì về các nhóm khác, vậy mà con số được trích dẫn như thể một vòng đã giải quyết vấn đề cho mọi người. Với một đội lớn phát hành vào một sản phẩm dùng chung, các phân khúc nhân lên nhanh: vai trò, khu vực, thiết bị, nhu cầu tiếp cận và mức chuyên môn khác nhau, và mỗi nhóm khác biệt đáng kể cần một nhúm riêng. Áp lực đối lập là chi phí và lịch trình, vì kiểm thử mọi phân khúc mỗi vòng thì đắt, nên hãy quyết định phân khúc nào mang nhiều rủi ro nhất, bao quát những cái đó mỗi vòng, và luân phiên phần còn lại. Hãy mang bản đồ phân khúc thực của bạn và số người tham gia theo từng phân khúc từ các vòng gần đây, và trung thực về nhóm nào bạn chưa bao giờ xem. Trong bối cảnh doanh nghiệp và chính phủ, nơi người dùng bị giữ chân và nghĩa vụ dịch vụ công nghĩa là phân khúc bị bỏ bê không thể đơn giản rời đi, một phân khúc chưa kiểm thử là một quần thể bạn đang thất bại trong im lặng, và khoảng trống đó thuộc về kế hoạch dưới dạng độ bao phủ tường minh hơn là một thống kê bị trung bình hóa.

5. **Ai được phép chạy một nghiên cứu ở đây, và cái gì ngăn một người nhiệt tình chưa được đào tạo tạo ra những điều vô nghĩa đầy tự tin ở quy mô lớn?** Dân chủ hóa nghiên cứu cho phép nhiều đội học nhanh hơn, nhưng không có mẫu, đào tạo và rà soát, nó cũng mở rộng giao thức thiên kiến, câu hỏi dẫn dắt và tổng hợp theo ước muốn, nên khối lượng học và khối lượng kết luận tồi tăng cùng nhau. Căng thẳng là giữa thông lượng và niềm tin: chặn mọi thứ qua vài nhà nghiên cứu và họ trở thành nút thắt, mở cửa không có lan can và bạn làm ngập tổ chức bằng phát hiện mà không ai nên hành động. Hãy quyết định loại nghiên cứu nào an toàn để ủy thác, như một bài kiểm thử nhiệm vụ không điều phối nhanh, so với loại nào đòi hỏi bàn tay được đào tạo, như chủ đề nhạy cảm, người tham gia dễ tổn thương, hay cược kiến trúc thông tin, và mang các mẫu, bước rà soát, và một cuộc kiểm toán trung thực các nghiên cứu tự phục vụ gần đây để xem bao nhiêu cái sẽ sống sót qua sự soi xét. Với một doanh nghiệp lớn hay cơ quan chính phủ, hãy thêm góc độ mua sắm và quyền riêng tư: công cụ nghiên cứu dùng chung thường được mua, và một nền tảng tự phục vụ cho phép bất kỳ ai liên hệ người tham gia mà không theo dõi sự đồng ý là một sự cố tuân thủ đang chờ, nên lan can liên quan đến xử lý dữ liệu hợp pháp nhiều như chất lượng phương pháp.

6. **Khi phân tích và phỏng vấn của chúng ta kể những câu chuyện đối nghịch về cùng một tính năng, đội này quyết định tin cái nào thế nào?** Tín hiệu định tính và định lượng trả lời hai nửa của một câu hỏi, và coi mâu thuẫn giữa chúng là phiền toái để giải quyết bằng thâm niên vứt đi manh mối hữu ích nhất bạn có, vì thường một nguồn đang đo thứ bạn không nhận ra mình đang đo. Với một tổ chức lớn rủi ro là chủ nghĩa bộ lạc: một đội dữ liệu chỉ tin bảng điều khiển và một đội nghiên cứu chỉ tin các phiên, mỗi bên bác bỏ bên kia thay vì đọc chúng cùng nhau. Hãy mang một bất đồng thực gần đây, chỗ rơi từ phân tích đặt cạnh lý do từ nghiên cứu, và đi qua vòng lặp phân tích cho thấy ở đâu, nghiên cứu giải thích vì sao, và một thí nghiệm đo liệu bản sửa có dịch chuyển con số. Trong bối cảnh doanh nghiệp và chính phủ, nơi một chỉ số đơn lẻ có thể thúc đẩy tài trợ hay một cam kết công, hãy nêu tên trước ai phân xử khi hai bên bất đồng và bằng chứng nào đóng cuộc tranh luận, để quyết định dựa trên một cách đọc được đối chiếu chéo thay vì chức năng nào có người ủng hộ to nhất trong phòng.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm người và không có đường băng để lãng phí, hãy coi nghiên cứu là bảo hiểm rẻ nhất bạn có thể mua, không phải một giai đoạn. Để một người sáng lập chạy năm phiên có điều phối trên bản mẫu giấy trước khi viết nhiều mã, đóng khung nhiệm vụ là mục tiêu thay vì chỉ dẫn, và để những gì bạn xem giết hoặc chuyển hướng ý tưởng khi nó còn là bản phác thảo. Bỏ qua kho lưu trữ và nhóm người tham gia; toàn bộ ý nghĩa là học đủ nhanh để tránh xây sai thứ.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có nhà nghiên cứu riêng và ngân sách eo hẹp, vì vậy hãy dựa vào công cụ kiểm thử không điều phối chi phí thấp và phỏng vấn nhẹ thay vì một chức năng nghiên cứu có nhân sự. Khi bạn mua phần mềm kiểm thử khả dụng, hãy ưu tiên công cụ xử lý tuyển người và sự đồng ý giúp bạn, vì tự xây bộ máy đó hiếm khi đáng ở quy mô của bạn. Hãy kiểm thử vài luồng khiến bạn thắng hoặc mất một khách hàng, và kỷ luật trong việc viết nhiệm vụ không dẫn dắt người tham gia, vì một giao thức tồi lãng phí ít ngân sách bạn có.

**Doanh nghiệp lớn.** Với nhiều nhóm phát hành vào sản phẩm dùng chung, ràng buộc là quản trị: một kho hiểu biết tìm kiếm được, một nhóm người tham gia được quản lý với theo dõi sự đồng ý, và một nhịp nghiên cứu để các nghiên cứu là thói quen thay vì cuộc chạy vạy. Hãy dân chủ hóa nghiên cứu trong lan can của mẫu, đào tạo và rà soát để khối lượng mở rộng mà không mở rộng giao thức tồi, và bảo đảm phát hành được gắn thẻ và kiểm toán được để hai nhóm không bao giờ trả hai lần cho cùng một câu hỏi. Hãy coi dữ liệu người tham gia là chịu quy định: lưu giữ, sự đồng ý và tần suất liên hệ đều cần chính sách.

**Chính phủ.** Nhiều tiêu chuẩn dịch vụ số quốc gia biến nghiên cứu người dùng thành bắt buộc và chịu đánh giá, vì vậy hãy coi nó là một cổng mà một dịch vụ phải vượt qua, với bằng chứng. Quy tắc mua sắm định hình công cụ và nhà cung cấp tuyển người của bạn, minh bạch nghĩa là lập tài liệu bạn đã kiểm thử với ai và tìm thấy gì, và trách nhiệm giải trình công nghĩa là tuyển những người dùng khó tiếp cận nhất, bao gồm người tham gia được hỗ trợ số và khuyết tật, vì một dịch vụ loại trừ họ từ chối mọi người quyền lợi. Hãy giữ hồ sơ rõ ràng về sự đồng ý và phương pháp để một người đánh giá, kiểm toán viên, hay công chúng thấy được nghiên cứu là thật.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người xây phần mềm chi phí cho người làm tự do tin chắc tính năng sát thủ là quét biên lai tự động, và đã xây một bản thô. Trước khi đầu tư thêm, hai người sáng lập chạy năm phiên kiểm thử khả dụng có điều phối với người làm tự do thật dùng bản mẫu giấy, đóng khung nhiệm vụ là mục tiêu ("ghi lại ly cà phê bạn vừa chi") thay vì chỉ dẫn. Bốn trong năm người hoàn toàn bỏ qua quét và gõ số tiền bằng tay, vì nỗi lo thực của họ không phải tốc độ nhập dữ liệu mà là liệu một khoản chi có sống sót qua một cuộc kiểm toán thuế. Đội xoay sản phẩm quanh phân loại sẵn sàng kiểm toán và một dấu vết giấy tờ rõ ràng, chạy thêm hai vòng nhỏ khi họ lặp, và biến một bản dùng thử miễn phí đang chững lại thành những người đăng ký trả tiền, tất cả với chi phí một tuần bản phác thảo và trò chuyện.

**Doanh nghiệp lớn.** Một công ty hậu cần toàn cầu đang chuẩn hóa phần mềm kho trên các địa điểm và dựng một chức năng vận hành nghiên cứu thường trực để giữ hàng chục nhóm sản phẩm trung thực. Họ xây một kho hiểu biết được gắn thẻ, một nhóm nhân viên kho đã đồng ý cho các phiên định kỳ, và một nhịp nghiên cứu hai tuần một lần. Khi hai nhóm độc lập đề xuất thiết kế lại cùng một quy trình quét, một tìm kiếm trong kho đưa ra một điều tra theo ngữ cảnh quý trước cho thấy găng tay và điều kiện kho lạnh, không phải bố cục màn hình, gây ra hầu hết lỗi quét. Phát hiện được tái sử dụng duy nhất đó chuyển hướng cả hai nhóm sang mục tiêu chạm lớn hơn và tương tác thân thiện với găng tay, tránh khám phá trùng lặp, và cắt giảm đo được các lần quét sai sau khi phát hành.

**Chính phủ.** Một cơ quan y tế quốc gia thiết kế lại dịch vụ đặt lịch hẹn coi nghiên cứu người dùng là bắt buộc theo tiêu chuẩn dịch vụ số của mình, không tùy chọn. Cùng với kiểm thử khả dụng có điều phối với một mẫu rộng về nhân khẩu học, đội chạy các phiên được hỗ trợ số với những người thường dựa vào người thân hay nhân viên thư viện, và tuyển người tham gia khuyết tật dùng trình đọc màn hình và truy cập công tắc (chương 5.3) qua hợp tác với các tổ chức từ thiện. Kiểm thử hé lộ rằng biệt ngữ lâm sàng trong tiêu đề mục khiến người dùng lớn tuổi và kém tự tin bỏ dở trước khi đến rào cản thực. Tái cấu trúc nội dung quanh mục tiêu ngôn ngữ đơn giản của bệnh nhân, rồi xác nhận mức tăng bằng một nghiên cứu không điều phối ở quy mô và một so sánh phân tích trực tiếp (chương 7.4), nâng số lần đặt lịch tự phục vụ thành công và giảm tải tổng đài, cải thiện cả chi phí phục vụ lẫn công bằng tiếp cận.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của nghiên cứu đến từ ba đòn bẩy. Thứ nhất, lãng phí được tránh: bắt một hướng sai trong một tuần khám phá thay vì sau một quý kỹ thuật là khoản tiết kiệm lớn nhất và bị đếm thiếu nhiều nhất, chính vì bản dựng lãng phí không bao giờ xảy ra nên không bao giờ xuất hiện trên báo cáo. Thứ hai, thành công cao hơn: nhiều người dùng hoàn thành nhiệm vụ có giá trị hơn, hiện ra là chuyển đổi trong sản phẩm tiêu dùng và là năng suất cùng ít lỗi hơn trong bối cảnh doanh nghiệp nơi người dùng bị giữ chân. Thứ ba, chi phí phục vụ thấp hơn: dịch vụ dùng được tạo ra ít liên hệ hỗ trợ hơn, ít đào tạo hơn, và ít sai lầm hạ nguồn cần sửa hơn.

Tổng chi phí sở hữu phải cân nhắc chi phí làm nghiên cứu so với chi phí bỏ qua nó. Chi phí làm nó hiển thị và khiêm tốn: nhà nghiên cứu, tuyển người và ưu đãi, công cụ, một kho lưu trữ, và thời gian trong lịch trình. Chi phí bỏ qua nó lớn hơn nhưng rải qua các ngân sách khác: giao dịch bị bỏ dở, phiếu hỗ trợ, ngày đào tạo, thiết kế lại muộn tốn kém, ra mắt thất bại, và, trong khu vực công, sự loại trừ công dân cùng rủi ro pháp lý và danh tiếng theo sau. Vì những chi phí này ẩn trong hỗ trợ, đào tạo và vận hành thay vì dòng sản phẩm, ban lãnh đạo thường xuyên đánh giá thấp chúng, chính là lý do nghiên cứu trông như tùy chọn cho đến khi một lần ra mắt thất bại.

Để trình bày lập luận, hãy gắn nghiên cứu với những con số mà giám đốc đã theo dõi: tỷ lệ hoàn thành và chuyển đổi, chi phí mỗi giao dịch, khối lượng hỗ trợ, thời gian đào tạo, và tỷ lệ lỗi cùng làm lại. Hãy chạy một so sánh trước-và-sau nhỏ, có đo đạc trên một luồng thực, cho thấy sự dịch chuyển, và ngoại suy qua danh mục. Đóng khung nghiên cứu là giảm rủi ro trên các quyết định không thể đảo ngược, ngôn ngữ gây tiếng vang với tài chính và các bên liên quan quản trị, những người có thể không bao giờ đọc báo cáo khả dụng nhưng hiểu một canh bạc có thể sai.

## Phản mẫu và cạm bẫy

- **Sân khấu nghiên cứu**: các nghiên cứu chạy để biện minh cho quyết định đã đưa ra, với phát hiện lặng lẽ bị phớt lờ khi bất tiện.
- **Dẫn dắt người tham gia**: nhiệm vụ và câu hỏi báo trước câu trả lời mong muốn, tạo ra dữ liệu tâng bốc vô nghĩa.
- **Tổng hợp thiên kiến xác nhận**: chỉ nghe các quan sát khớp kế hoạch và bỏ phần còn lại.
- **Ngụy biện năm-người-dùng**: coi "khoảng năm người dùng" là quy luật phổ quát, bỏ qua rằng nó giả định một phân khúc và chỉ tìm các vấn đề nghiêm trọng, không phải tỷ lệ thành công.
- **Tuyển người tiện lợi**: kiểm thử ai dễ tiếp cận, nên người dùng khuyết tật và khó tiếp cận biến mất khỏi mẫu.
- **Tin sở thích đã nêu**: tin "vâng, tôi sẽ dùng cái đó" thay vì xem người ta thực sự làm gì.
- **Nghĩa địa hiểu biết**: phát hiện bị chôn trong slide của một đội, nên cùng câu hỏi được nghiên cứu hết lần này đến lần khác.
- **Dân chủ hóa không lan can**: để bất kỳ ai chạy nghiên cứu không có mẫu hay rà soát, mở rộng giao thức thiên kiến và kết luận lung lay.
- **Chủ nghĩa bộ lạc định tính-so-với-định lượng**: chọn nguồn dữ liệu ưa thích và bác bỏ nguồn kia thay vì đối chiếu chéo.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Nghiên cứu là tùy nghi hoặc vắng mặt, và quyết định dựa vào ý kiến và thâm niên. Kiểm thử khả dụng, nếu xảy ra, là một lần phản ứng trước ra mắt với ai tiện, và phát hiện hiếm khi thay đổi gì.
- **Mức 2, Phát triển:** Một số đội chạy kiểm thử khả dụng và phỏng vấn thỉnh thoảng, nhưng việc tuyển người là tiện lợi, giao thức không chính thức, và hiểu biết sống trong các bộ slide rải rác. Thực hành khác nhau nhiều từ nhóm này sang nhóm khác, và nghiên cứu là một giai đoạn bị cắt dưới áp lực lịch trình.
- **Mức 3, Chuẩn hóa:** Nghiên cứu sinh tạo và đánh giá được lập tài liệu và chạy liên tục qua các đội, nuôi ưu tiên hóa qua một quy trình dùng chung. Việc tuyển người nhắm vào các phân khúc thực bao gồm người dùng khuyết tật và khó tiếp cận, một kho hiểu biết tìm kiếm được tồn tại, tổng hợp tạo ra các quyết định được xếp hạng, và vận hành nghiên cứu quản lý nhịp, mẫu và người tham gia toàn tổ chức.
- **Mức 4, Quản lý:** Chương trình nghiên cứu được đo theo đường cơ sở. Các đội theo dõi độ bao phủ phân khúc người dùng, tỷ lệ thành công và hoàn thành nhiệm vụ, thời gian từ hiểu biết đến thay đổi được phát hành, và tác động hạ nguồn lên khối lượng hỗ trợ, thời gian đào tạo, và tỷ lệ lỗi cùng làm lại, và họ đặt ngưỡng kích hoạt hành động khi một chỉ số tụt. Việc tái sử dụng kho lưu trữ và chất lượng nghiên cứu được giám sát, để lãnh đạo thấy được lợi tức nghiên cứu tạo ra thay vì giả định.
- **Mức 5, Điều phối:** Nghiên cứu là một vòng lặp liên tục, được đối chiếu chéo với phân tích và thí nghiệm, khép từ hiểu biết đến thay đổi được phát hành đến hiệu ứng đo được, và nó được tích hợp với chiến lược sản phẩm và hoạch định rủi ro trong toàn tổ chức. Nghiên cứu được dân chủ hóa chạy an toàn trong lan can, phát hiện cộng dồn và thích ứng khi sản phẩm cùng người dùng dịch chuyển, và nghiên cứu định hình chiến lược một cách rõ ràng, không chỉ màn hình.

## Ý tưởng để thảo luận

1. Bao nhiêu khám phá là "đủ" trước khi cam kết xây, và ai có thẩm quyền nói khi nào bạn đã học đủ?
2. Khi phân tích và phỏng vấn kể những câu chuyện đối nghịch về cùng một tính năng, đội nên quyết định hành động theo cái nào thế nào?
3. Lằn ranh giữa dân chủ hóa nghiên cứu có trách nhiệm và để sự nhiệt tình chưa được đào tạo tạo ra các nghiên cứu thiên kiến ở quy mô nằm ở đâu?
4. Làm sao bạn đo lợi tức của một nghiên cứu mà giá trị là một sai lầm bạn vì thế không bao giờ mắc và không bao giờ chỉ ra được?
5. Cách đạo đức để nghiên cứu với người đang khủng hoảng hoặc trong hoàn cảnh dễ tổn thương mà không thêm gánh nặng cho họ là gì?
6. Nghiên cứu người dùng bắt buộc, như trong tiêu chuẩn dịch vụ chính phủ, có nên là một cổng có thể chặn một lần ra mắt không, và ai thực thi nó?

## Những điểm cần ghi nhớ

- Nghiên cứu tồn tại để giảm rủi ro xây sai thứ, và nó rẻ nhất trước khi bạn xây.
- Tách nghiên cứu sinh tạo (tìm đúng vấn đề) khỏi nghiên cứu đánh giá (kiểm tra giải pháp); chọn phương pháp từ câu hỏi.
- "Khoảng năm người dùng" tìm hầu hết vấn đề nghiêm trọng trong một phân khúc mỗi vòng, nhưng không đo thành công hay bao quát các nhóm riêng biệt.
- Viết nhiệm vụ là mục tiêu thực tế, hỏi về hành vi quá khứ, và thiết kế chống lại câu hỏi dẫn dắt và thiên kiến xác nhận.
- Tuyển người tham gia thực sự đại diện cho người dùng của bạn, bao gồm người khuyết tật và khó tiếp cận, nếu không phát hiện của bạn sai một cách lặng lẽ.
- Tổng hợp thành các quyết định được xếp hạng, không phải bộ slide; phép thử là một quyết định có thực sự thay đổi không.
- Đối chiếu chéo nghiên cứu định tính với phân tích và thí nghiệm, và nắm bắt phát hiện trong một kho dùng chung để học cộng dồn.

## Tài liệu tham khảo và đọc thêm

- Erika Hall, *Just Enough Research*
- Steve Krug, *Rocket Surgery Made Easy*
- Jakob Nielsen, *Usability Engineering*
- Mike Kuniavsky, *Observing the User Experience*
- Steve Portigal, *Interviewing Users*
- Tomer Sharon, *Validating Product Ideas: Through Lean User Research*
- Hugh Beyer và Karen Holtzblatt, *Contextual Design*
- Donna Spencer, *Card Sorting: Designing Usable Categories*
- Kathy Baxter, Catherine Courage và Kelly Caine, *Understanding Your Users*
- Kate Towsey, *Research That Scales: The Research Operations Handbook*
- Nielsen Norman Group, các bài viết về kiểm thử khả dụng, cỡ mẫu và phương pháp nghiên cứu
- UK Government Digital Service, *Service Manual*: hướng dẫn nghiên cứu người dùng
