# 6.8 Đánh giá và kiểm thử AI

## Tổng quan và động lực

Kiểm thử phần mềm thông thường dựa trên một giả định an ủi: với cùng đầu vào, chương trình trả về cùng đầu ra, và bạn có thể khẳng định chính xác đầu ra đó phải là gì. Trí tuệ nhân tạo phá vỡ giả định đó. Một mô hình có thể trả lời cùng một câu hỏi theo hai cách khác nhau, cả hai đều chấp nhận được. Nó có thể được chấm điểm trên một phổ từ sai đến xuất sắc thay vì đạt hay trượt. Và thường không có một câu trả lời đúng duy nhất để khẳng định. Vì vậy kỷ luật đánh giá, đo mô hình hành xử tốt đến đâu qua nhiều ca đại diện thay vì kiểm tra một đầu ra với một giá trị kỳ vọng, trở thành xương sống của mọi hệ thống AI đáng tin cậy. Khi các đội phát hành tính năng AI làm họ xấu hổ, nguyên nhân gốc hầu như luôn là họ không có cách nghiêm túc nào để đo chất lượng trước khi phát hành.

Với các đội lớn, đánh giá là thứ làm thay đổi an toàn. Bạn sẽ đổi mô hình, viết lại prompt, điều chỉnh truy xuất, và thêm công cụ, và mỗi thay đổi đó có thể lặng lẽ làm suy giảm hành vi bạn tưởng vững chắc. Không có cách đo lặp lại được, mỗi thay đổi là một canh bạc và mỗi hồi quy được phát hiện bởi một người dùng. Chương này là người bạn đồng hành đo lường cho các chương xây dựng: AI sinh tạo và ứng dụng LLM (chương 6.3), tác tử AI và hệ thống tác tử (chương 6.7), và kỹ thuật học máy cùng MLOps (chương 6.2). Nó mở rộng chiến lược kiểm thử chung của bạn (chương 2.4) vào thế giới xác suất.

Bối cảnh doanh nghiệp và chính phủ nâng rủi ro thêm. Một doanh nghiệp chạy hàng chục tính năng AI cần một nền tảng đánh giá dùng chung để mỗi đội không phải phát minh lại việc chấm điểm từ đầu. Một cơ quan chính phủ cần đánh giá được lập tài liệu và kiểm toán được, vì "chúng tôi đã kiểm thử nó" phải trở thành "đây là bằng chứng, tập dữ liệu, chỉ số, và chữ ký duyệt." Đánh giá là nơi AI có trách nhiệm và đáng tin cậy (chương 6.5) thôi là một tuyên bố giá trị và trở thành thứ bạn có thể trình cho cơ quan quản lý.

## Các nguyên tắc chính

- Coi đánh giá là sản phẩm hạng nhất, không phải chuyện nghĩ sau bắt vít vào trước khi ra mắt.
- Đo bằng dữ liệu đại diện phản ánh việc sử dụng thực, không phải các ví dụ đồ chơi tâng bốc mô hình.
- Kết hợp đánh giá ngoại tuyến để lặp nhanh với đánh giá trực tuyến để có sự thật nền.
- Dùng phán đoán của con người làm mỏ neo, và hiệu chuẩn mọi bộ chấm điểm tự động với nó.
- Bảo vệ tập đánh giá khỏi ô nhiễm, nếu không các con số sẽ nói dối bạn.
- Nối đánh giá vào tích hợp liên tục như các cổng, để chất lượng không thể hồi quy trong im lặng.
- Tiếp tục đo trong môi trường sản xuất, vì chất lượng trôi ngay cả khi mã của bạn không đổi.

## Khuyến nghị

### Áp dụng phát triển dựa trên đánh giá

Trước khi bạn tinh chỉnh một prompt hay chọn một mô hình, hãy viết đánh giá. Điều này phản chiếu phát triển hướng kiểm thử: bạn xác định "tốt" nghĩa là gì theo thuật ngữ đo được, rồi xây hướng tới nó. Một đánh giá ở đây nghĩa là một tập dữ liệu gồm các đầu vào ghép với một phương pháp chấm điểm trả về một con số hay hạng cho mỗi đầu ra. Hãy bắt đầu nhỏ. Hai mươi ca được chọn cẩn thận phản ánh ý định người dùng thực thắng một nghìn ca ngẫu nhiên. Hãy mở rộng tập khi bạn học được hệ thống thất bại ở đâu, thêm mọi thất bại trong môi trường sản xuất trở lại thành một ca vĩnh viễn để cùng sai lầm không thể quay lại mà không bị chú ý.

Phát triển dựa trên đánh giá thay đổi hành vi của đội. Khi định nghĩa của tốt được viết ra và chạy được, các cuộc tranh cãi về việc một thay đổi có giúp ích không trở nên kiểm tra được thay vì chuyện gu. Hãy biến tập đánh giá thành hiện vật được rà soát trong quản lý phiên bản, ngay cạnh các prompt và mã nó đo.

### Tách đánh giá ngoại tuyến và trực tuyến, và dùng cả hai

Đánh giá ngoại tuyến chạy một tập dữ liệu cố định qua hệ thống của bạn trong môi trường được kiểm soát, nhanh, rẻ và lặp lại được, để bạn so sánh các phiên bản trước khi bất cứ thứ gì được phát hành. Đánh giá trực tuyến đo hệ thống trực tiếp với người dùng thật qua các chỉ số như hoàn thành nhiệm vụ, tỷ lệ leo thang, phản hồi thích và không thích, và kết quả kinh doanh hạ nguồn. Ngoại tuyến cho bạn biết một thay đổi có khả năng an toàn; trực tuyến cho bạn biết nó có thực sự hiệu quả. Bạn cần cả hai, vì tập ngoại tuyến không bao giờ nắm bắt trọn thực tế và tín hiệu trực tuyến đến quá muộn để làm lan can duy nhất.

Hãy nối hai thứ thành một vòng lặp. Khi chỉ số trực tuyến tụt hoặc người dùng gắn cờ một câu trả lời tồi, hãy nắm bắt ca đó, gắn nhãn, và gộp vào tập ngoại tuyến. Hãy đưa các thí nghiệm qua cùng sự so sánh được kiểm soát bạn dùng cho bất kỳ thay đổi sản phẩm nào, là lãnh thổ của phân tích sản phẩm và thí nghiệm (chương 7.4). Một thử nghiệm A/B cho thấy mô hình mới nâng thành công nhiệm vụ đáng giá hơn bất kỳ điểm ngoại tuyến nào, nhưng chính điểm ngoại tuyến là thứ cho bạn dám chạy thử nghiệm.

### Xây tập đánh giá đại diện và bảo vệ chống ô nhiễm

Đánh giá của bạn chỉ trung thực như dữ liệu của nó. Hãy xây các tập dữ liệu vàng, những bộ sưu tập được chọn lọc gồm đầu vào với đầu ra kỳ vọng đã được thẩm định hoặc thang chấm điểm, phản ánh phân phối thực của những gì người dùng hỏi: các ca phổ biến, các ca hiếm nhưng trọng yếu, các ca đối kháng, và những ca hệ thống của bạn hiện làm sai. Hãy phân tầng chúng để bạn đọc chất lượng theo từng phân khúc thay vì giấu một hạng mục thất bại trong một trung bình khá. Hãy để chuyên gia miền thẩm định các câu trả lời kỳ vọng, vì một tập vàng xây trên câu trả lời sai còn tệ hơn không có.

Rồi bảo vệ dữ liệu đó khỏi ô nhiễm. Ô nhiễm tập kiểm thử xảy ra khi các ví dụ đánh giá của bạn rò vào dữ liệu huấn luyện của mô hình hoặc vào chính prompt, nên mô hình có vẻ hoạt động tốt vì nó thực chất đã thấy đáp án. Đó là lý do một mô hình có thể đạt điểm rực rỡ trên một chuẩn công khai và vấp ngã trên lưu lượng thật của bạn. Hãy giữ một phần dữ liệu đánh giá riêng tư và đừng bao giờ gửi nó cho bên thứ ba bạn không tin được. Làm mới tập theo thời gian. Cảnh giác với kiểu rò tinh vi hơn khi lập trình viên chỉnh tay prompt theo tập đánh giá cho đến khi điểm vô nghĩa, một dạng quá khớp với bài kiểm tra thay vì cải thiện thực. Hãy giữ lại một tập mới mà bạn chỉ thỉnh thoảng nhìn.

### Chọn chỉ số phù hợp nhiệm vụ

Hãy khớp phép đo với hình dạng của đầu ra. Với phân loại và trích xuất, nơi có nhãn đúng, các chỉ số cổ điển áp dụng: [độ chính xác và độ phủ](https://en.wikipedia.org/wiki/Precision_and_recall) (trong các mục bạn gắn cờ, bao nhiêu đúng, và trong các mục đúng, bạn tìm thấy bao nhiêu), [điểm F](https://en.wikipedia.org/wiki/F-score) cân bằng chúng, và độ chính xác khớp chính xác. Với bất cứ thứ gì mà một xác suất tự tin quan trọng, hãy đo [hiệu chuẩn](https://en.wikipedia.org/wiki/Calibration_(statistics)), liệu độ tin cậy 80 phần trăm được nêu có đúng khoảng 80 phần trăm số lần, vì một mô hình hiệu chuẩn tốt biết khi nào nó không chắc an toàn hơn nhiều so với mô hình quá tự tin.

Đầu ra sinh tạo khó hơn. Các chỉ số dựa trên tham chiếu như [BLEU](https://en.wikipedia.org/wiki/BLEU) và ROUGE, ban đầu được xây cho dịch máy và tóm tắt, so sánh văn bản được sinh ra với văn bản tham chiếu bằng cách đếm các từ và cụm từ trùng nhau. Chúng rẻ và lặp lại được, và là đại diện yếu cho chất lượng: chúng thưởng cho sự trùng lặp bề mặt và phạt một câu trả lời đúng được diễn đạt khác với tham chiếu. Hãy dùng chúng làm tín hiệu hồi quy thô, không phải định nghĩa của bạn về tốt. Với các nhiệm vụ mở, chấm điểm theo thang hoạt động tốt hơn: xác định tiêu chí tường minh (nó có được neo đất, đầy đủ, an toàn, và đúng định dạng không) và chấm từng cái. Thang chấm làm chất lượng chủ quan trở nên dễ đọc và rà soát được.

### Dùng LLM-làm-giám-khảo, nhưng hiệu chuẩn nó với con người

Chấm đầu ra sinh tạo bằng tay không mở rộng được, nên các đội ngày càng dùng một [mô hình ngôn ngữ lớn](https://en.wikipedia.org/wiki/Large_language_model) mạnh làm giám khảo tự động, prompt nó với đầu vào, đầu ra và thang chấm, và yêu cầu nó cho điểm. Cách tiếp cận LLM-làm-giám-khảo này nhanh và có năng lực đáng ngạc nhiên, và nó mang những thiên kiến thật mà bạn phải quản lý. Giám khảo có xu hướng thích câu trả lời dài hơn, ưu ái lựa chọn đầu tiên được hiển thị trong so sánh cặp (thiên kiến vị trí), thưởng cho phong cách viết của chính nó, và có thể bị lay động bởi suy luận trôi chảy nhưng sai. Không kiểm soát, một giám khảo thiên kiến cho bạn những con số tự tin, chính xác, sai.

Hãy hiệu chuẩn giám khảo với nhãn của con người. Cho người chấm một mẫu, rồi kiểm tra giám khảo mô hình đồng thuận với họ tốt đến đâu, và tiếp tục chỉnh prompt giám khảo cho đến khi sự đồng thuận đủ cao để tin. Giảm các thiên kiến đã biết có chủ đích: ngẫu nhiên hóa thứ tự lựa chọn, kiểm soát độ dài, và yêu cầu điểm neo theo thang cùng lý do thay vì một con số trần. Hãy coi giám khảo là một dụng cụ đo cần hiệu chuẩn lại định kỳ, không phải một tiên tri cố định. Khi xây giám khảo, mặc định dùng mô hình có năng lực nhất có sẵn, vì một giám khảo yếu là một cây thước yếu.

### Giữ con người trong vòng lặp cho sự thật nền

Đánh giá của con người vẫn là mỏ neo mà mọi chỉ số tự động được đo theo, nên hãy đầu tư làm nó tốt. Viết hướng dẫn chú thích rõ ràng, đào tạo người chú thích, và đo độ đồng thuận giữa người chú thích, mức độ mà các người rà soát độc lập cho cùng một ca cùng một hạng. Độ đồng thuận thấp thường nghĩa là thang chấm của bạn mơ hồ, không phải người rà soát cẩu thả, nên hãy sửa thang. Với các miền rủi ro cao, hãy dùng chuyên gia đủ trình độ, không phải nhân công đám đông thiếu ngữ cảnh để đánh giá một câu trả lời pháp lý hay y khoa.

### Đội đỏ cho an toàn và độ bền đối kháng

Các tập đánh giá chuẩn đo liệu hệ thống có làm đúng trên đầu vào hợp lý. [Đội đỏ](https://en.wikipedia.org/wiki/Red_team), cố ý tấn công hệ thống của chính bạn để tìm nơi nó hành xử sai, đo điều xảy ra dưới áp lực. Thăm dò tiêm prompt, bẻ khóa, nội dung không an toàn, rò rỉ quyền riêng tư, và đầu ra thiên kiến. Hãy biến nó thành một bộ lặp lại được, không phải bài tập một lần: biến mọi cuộc tấn công thành công thành một ca hồi quy vĩnh viễn để một lỗ hổng đã sửa vẫn được sửa. Công việc này nối trực tiếp với AI có trách nhiệm và đáng tin cậy (chương 6.5), và trong bối cảnh chịu quy định nó thường là bằng chứng thỏa mãn một cuộc rà soát an toàn.

### Đánh giá tác tử bằng thành công nhiệm vụ đầu-đến-cuối

Tác tử lập kế hoạch và hành động qua nhiều bước không thể được đánh giá từng đầu ra một. Điều quan trọng là toàn bộ nhiệm vụ có thành công không: tác tử có đặt được cuộc họp, giải quyết phiếu, hay hoàn thành quy trình một cách đúng đắn và an toàn không. Hãy xây các đánh giá cấp nhiệm vụ trong môi trường hộp cát nơi tác tử có thể hành động trên các dữ liệu mẫu thực tế nhưng an toàn, và chấm kết quả cuối cùng cộng với quỹ đạo, nghĩa là chuỗi bước và lệnh gọi công cụ nó thực hiện để đến đó. Một câu trả lời đúng đạt được qua đường nguy hiểm hoặc lãng phí vẫn là vấn đề. Điều này thiết yếu với tác tử AI và hệ thống tác tử (chương 6.7), nơi một hành động sai duy nhất có thể gây hệ quả thật.

### Nối đánh giá vào CI và giám sát môi trường sản xuất

Hãy làm đánh giá tự động. Chạy bộ ngoại tuyến của bạn trong [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI) ở mỗi thay đổi prompt, mô hình hay truy xuất, và chặn cổng hợp nhất trên nó như bạn chặn trên kiểm thử đơn vị, một thực hành bắt nguồn từ chiến lược kiểm thử rộng hơn của bạn (chương 2.4). Vì điểm có nhiễu, hãy chặn cổng theo ngưỡng và xu hướng thay vì đòi một lần chạy hoàn hảo, và làm hỏng bản dựng khi một chỉ số then chốt tụt dưới sàn hoặc hồi quy vượt một biên đặt trước. Rồi tiếp tục theo dõi trong môi trường sản xuất: giám sát tín hiệu chất lượng, phân phối đầu ra và độ trôi đầu vào để bắt sự suy giảm chậm mà kiểm thử ngoại tuyến bỏ sót, gắn với các thực hành quan sát của kỹ thuật học máy và MLOps (chương 6.2). Một mô hình chính xác lúc ra mắt có thể mục rữa khi thế giới nó mô tả thay đổi bên dưới.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận đánh giá | Ưu điểm | Nhược điểm | Tốt nhất khi |
|---|---|---|---|
| Đánh giá của con người | Độ trung thực cao nhất, nắm bắt sắc thái | Chậm, tốn kém, khó mở rộng | Sự thật nền, rủi ro cao, hiệu chuẩn giám khảo |
| LLM-làm-giám-khảo | Nhanh, rẻ, mở rộng cho tập lớn | Thiên kiến, cần hiệu chuẩn | Chạy ngoại tuyến thường xuyên trên đầu ra sinh tạo |
| Chỉ số dựa trên tham chiếu (BLEU, ROUGE) | Rẻ, tất định, lặp lại được | Đại diện yếu cho chất lượng thực | Tín hiệu hồi quy thô, không phải phán quyết cuối |
| Chỉ số cổ điển (độ chính xác, độ phủ, điểm F) | Khách quan, được hiểu rõ | Chỉ phù hợp nhiệm vụ có nhãn đúng | Phân loại, trích xuất, truy xuất |
| Chuẩn công khai | So sánh được giữa các mô hình, không cần thiết lập | Ô nhiễm, vừa vặn kém với nhiệm vụ của bạn | Lọc mô hình sớm, không phải cổng phát hành |
| Đánh giá trực tuyến (A/B, phản hồi) | Phản ánh người dùng và kết quả thực | Chậm, đến sau khi đã phơi nhiễm | Xác nhận một thay đổi thực sự giúp ích |

Căng thẳng trung tâm là tốc độ so với độ trung thực. Đánh giá của con người đáng tin nhất và ít mở rộng nhất; chấm điểm tự động thì ngược lại. Cách giải quyết là xếp lớp chúng: dùng phương pháp nhanh, rẻ cho lặp lại liên tục, neo các phương pháp đó vào phán đoán của con người qua hiệu chuẩn đều đặn, và dành rà soát đầy đủ của con người cho các quyết định rủi ro cao nhất và cho việc kiểm tra các chỉ số rẻ của bạn vẫn bám thực tế. Căng thẳng thứ hai là sự tiện lợi ngoại tuyến so với sự thật trực tuyến. Tập ngoại tuyến cho bạn đi nhanh nhưng không bao giờ phản chiếu trọn môi trường sản xuất, nên hãy coi điểm ngoại tuyến mạnh là giấy phép để chạy một thử nghiệm trực tuyến cẩn thận, không phải bằng chứng bạn đã xong.

## Câu hỏi để thảo luận với đội của bạn

1. **Ngưỡng "đủ tốt" của chúng ta là gì, và ai sở hữu tập đánh giá xác định nó?** Mỗi tính năng AI có một ngưỡng chất lượng ngầm, và khi nó vẫn ngầm, mỗi kỹ sư đặt ngưỡng riêng theo cảm tính và tranh cãi được giải quyết bởi người cao cấp nhất trong phòng. Viết ngưỡng thành một tập đánh giá chạy được với điểm mục tiêu theo từng phân khúc biến những tranh cãi đó thành câu hỏi đo được. Hãy mang định nghĩa thành công hiện tại, dữ liệu đằng sau nó, và lời kể trung thực về ai thực sự duy trì nó, vì một tập đánh giá không chủ sở hữu mục rữa nhanh như bất kỳ mã không ai chăm sóc nào. Hãy quyết định liệu ngưỡng có khác theo bậc rủi ro, vì một câu trả lời pháp lý hướng công chúng nên vượt ngưỡng cao hơn một công cụ động não nội bộ. Câu trả lời nên cho bạn biết hiện giờ có ai phát hành được một thay đổi AI mà không có phép đo nào đứng giữa họ và người dùng.

2. **Làm sao chúng ta biết các con số đánh giá của mình trung thực chứ không bị ô nhiễm hay quá khớp?** Một điểm chỉ hữu ích nếu nó dự đoán chất lượng thực, và có nhiều cách để nó thôi làm vậy: dữ liệu chuẩn rò vào huấn luyện, lập trình viên chỉnh prompt theo tập kiểm thử cho đến khi con số vô nghĩa, hoặc một tập dữ liệu vàng xây trên câu trả lời chưa bao giờ được xác minh. Hãy mang bằng chứng về dữ liệu đánh giá của bạn đến từ đâu, bao nhiêu phần được giữ riêng tư, và nó được làm mới bao lâu một lần. Hãy thảo luận liệu bạn có giữ một tập giữ lại mới mà bạn hiếm khi nhìn, để có ít nhất một con số không ai tối ưu theo. Nếu bạn không giải thích được vì sao điểm của mình vẫn đúng trên dữ liệu mô hình chưa bao giờ bị ảnh hưởng, bạn đang đo hình phản chiếu của chính mình.

3. **Con người ở lại trong vòng lặp ở đâu, và làm sao chúng ta giữ các giám khảo tự động được hiệu chuẩn với họ?** LLM-làm-giám-khảo và chỉ số tham chiếu cho phép bạn chấm ở quy mô, và chúng trôi khỏi phán đoán của con người theo những cách vô hình trừ khi bạn kiểm tra. Hãy mang tỷ lệ đồng thuận hiện tại giữa chấm tự động và rà soát của con người, lần đo gần nhất là khi nào, và những thiên kiến nào (độ dài, vị trí, phong cách) bạn đã kiểm thử. Hãy quyết định quyết định nào đòi một người chấm bất kể chi phí, thường là rủi ro cao nhất và những cái dùng để hiệu chuẩn lại giám khảo tự động. Hãy nói cả về chất lượng chú thích, vì một giám khảo hiệu chuẩn theo nhãn của con người không nhất quán thừa hưởng sự không nhất quán đó. Câu trả lời nên tạo ra một lịch hiệu chuẩn lại, không phải một lần ban phước.

4. **Những thay đổi AI nào được chặn cổng theo đánh giá hôm nay, và cái nào vẫn đến người dùng chỉ nhờ sự tự tin của ai đó?** Một cổng chạy trên một số thay đổi nhưng không phải số khác cho bạn ảo giác an toàn trong khi để các hồi quy thật lọt qua đường không cổng: một tinh chỉnh prompt lặng lẽ, một chỉnh truy xuất, một lần nâng phiên bản mô hình mà không ai nghĩ là một thay đổi. Với một đội lớn, mối nguy tăng theo số người có thể chạm vào prompt, vì mỗi đường không cổng là một cách phát hành hồi quy mà không tập dữ liệu nào từng thấy. Hãy mang danh sách các loại thay đổi hiện kích hoạt bộ ngoại tuyến trong tích hợp liên tục, những loại không, và vài sự cố gần đây truy về một thay đổi không cổng. Hãy quyết định ngưỡng và xu hướng nào cổng thực thi, vì một điểm có nhiễu đòi một sàn và biên hồi quy thay vì yêu cầu một lần chạy hoàn hảo. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn cổng với chính bản ghi phát hành, để bằng chứng rằng một thay đổi đã được đo là một phần của dấu vết kiểm toán chứ không phải ảnh chụp màn hình ai đó chụp một lần.

5. **Chúng ta đang chi bao nhiêu cho đánh giá, và khoản chi đó có khớp với rủi ro của từng tính năng không?** Đánh giá không miễn phí: lao động chú thích, tính toán mà giám khảo tự động đốt ở mỗi lần chạy, và công việc thường trực giữ các tập vàng đại diện đều tốn tiền thật, và một đội không bao giờ gọi tên những chi phí đó có xu hướng hoặc đầu tư thiếu cho tính năng rủi ro cao hoặc mạ vàng một tính năng bỏ đi. Lực kéo đối lập là giữa độ trung thực và ngân sách, vì phương pháp đáng tin nhất, rà soát của chuyên gia con người, cũng ít mở rộng nhất, nên bạn không đủ khả năng làm ở khắp nơi và phải quyết định nơi nó xứng đáng với giá. Hãy mang chi phí hiện tại mỗi lần chạy đánh giá, giờ chú thích mỗi tính năng, và bậc rủi ro trung thực cho từng hệ thống để căn phòng thấy tiền đi đâu so với nguy hiểm sống ở đâu. Với một doanh nghiệp, đây là lập luận mạnh nhất cho một nền tảng đánh giá dùng chung phân bổ chú thích và tính toán qua nhiều đội; với một cơ quan chính phủ, bậc rủi ro nên ánh xạ trực tiếp với độ sâu bằng chứng mà một cơ quan giám sát sau này sẽ đòi.

6. **Khi một mô hình tốt hơn xuất hiện, chúng ta chứng minh nó có giúp ích nhanh đến đâu, và ai được phép thực hiện việc chuyển?** Giá trị của một bộ đánh giá được hiện thực sắc nét nhất vào ngày một mô hình mạnh hơn ra mắt, vì một đội có thể chạy các tập vàng và bộ đội đỏ của mình trên mô hình mới trong một buổi chiều có thể áp dụng các cải tiến mà một đội chấm bằng tay sẽ bỏ lỡ nhiều tháng. Căng thẳng là giữa tốc độ và thận trọng: bạn muốn di chuyển ngay ngày một mô hình tốt hơn xuất hiện, và bạn không thể để một lần đổi lặng lẽ làm suy giảm một loại câu trả lời mà điểm trung bình của bạn che giấu. Hãy mang thời gian hiện tại cần để chạy một so sánh ngoại tuyến đầy đủ với một nhà cung cấp mới, liệu các tập đánh giá của bạn có di chuyển được giữa các mô hình, và các phân khúc nơi một hồi quy sẽ quan trọng nhất. Trong bối cảnh chịu quy định và công, hãy nêu ai nắm thẩm quyền phê duyệt một thay đổi mô hình và họ đòi bằng chứng có tài liệu nào, vì một lần đổi không được lập tài liệu mô hình đằng sau một quyết định hướng công dân chính là kiểu thay đổi mà kiểm toán viên sẽ yêu cầu bạn biện minh.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy xây đánh giá trung thực nhỏ nhất bạn có thể và để nó lớn lên cùng sản phẩm. Một bảng tính hai mươi đến bốn mươi ca thật, mỗi ca có câu trả lời kỳ vọng được thẩm định, chạy bằng một tập lệnh trước mỗi lần hợp nhất, thắng bất kỳ chuẩn công khai nào cho ngách của bạn và tốn gần như không gì. Bỏ qua nền tảng dùng chung và LLM-làm-giám-khảo cho đến khi chấm tay thực sự đau, nhưng hãy gộp mọi thất bại do người dùng báo cáo vào tập từ ngày đầu, vì phản xạ đó là thứ ngăn cùng sự xấu hổ hai lần.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia đánh giá và mua AI nhúng trong công cụ, nên việc của bạn là đòi bằng chứng thay vì xây nó. Hãy hỏi mỗi nhà cung cấp họ đã đo chất lượng thế nào, họ có kiểm thử trên dữ liệu giống của bạn không, và bạn sẽ nhận ra một hồi quy thế nào sau một bản cập nhật bạn không chọn. Hãy giữ một tập riêng nhỏ gồm các ca thật của chính bạn để tự kiểm tra công cụ, vì một câu trả lời tự động sai đến tay khách hàng tốn của bạn nhiều hơn hẳn vài phút kiểm tra đó.

**Doanh nghiệp lớn.** Giải thưởng là một nền tảng đánh giá dùng chung để cả chục đội không phát minh lại việc chấm điểm: một kho chung cho tập dữ liệu vàng, bộ ngoại tuyến được chặn cổng trong tích hợp liên tục, prompt giám khảo LLM được đăng ký cùng điểm hiệu chuẩn, và chỉ số trực tuyến mỗi tính năng. Hãy xếp quản trị lên trên với các bậc rủi ro đặt ngưỡng cần thiết và chữ ký duyệt trước phát hành, để một tính năng rủi ro cao vượt cổng cao hơn một công cụ nội bộ. Nền tảng phân bổ chú thích và tính toán qua các đội, là lý do mạnh nhất để xây một cái thay vì để mỗi nhóm ứng biến.

**Chính phủ.** Đánh giá phải kiểm toán được, không chỉ được thực hiện, vì vậy hãy lưu trữ phiên bản tập dữ liệu, các chỉ số, tên người rà soát và chữ ký duyệt làm bằng chứng trách nhiệm giải trình cho mỗi bản phát hành. Một bộ đội đỏ nên chứng minh hệ thống từ chối bịa chính sách hay nêu luật không có trong nguồn của nó, và mua sắm nên yêu cầu nhà cung cấp tiết lộ cách họ đã đánh giá mô hình và trao khả năng di chuyển dữ liệu đánh giá của bạn. Khi một cơ quan giám sát hỏi bạn biết công cụ an toàn thế nào, câu trả lời phải là một bản ghi có ngày tháng, không phải lời trấn an.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty bốn người xây trợ lý rà soát hợp đồng AI bắt đầu với một bảng tính bốn mươi điều khoản thật, mỗi điều khoản được luật sư nội bộ gắn nhãn rủi ro nó nên gắn cờ. Mọi thay đổi prompt chạy trên tập đó trong một tập lệnh trước khi hợp nhất, và điểm được in trong pull request. Khi người dùng gắn cờ một điều khoản bị bỏ sót, nó đi thẳng vào bảng tính, nên tập lớn lên cùng sản phẩm. Khi khối lượng tăng, họ thêm một LLM-làm-giám-khảo để chấm chất lượng giải thích, nhưng chỉ sau khi kiểm tra nó đồng thuận với luật sư trên một mẫu. Rẻ, riêng tư và trung thực thắng bất kỳ chuẩn công khai nào cho ngách của họ.

**Doanh nghiệp lớn.** Một ngân hàng lớn chạy cả chục tính năng AI qua hỗ trợ, tìm kiếm và công cụ nội bộ, và mỗi đội chấm điểm khác nhau. Họ xây một nền tảng đánh giá dùng chung: một nơi chung để lưu tập dữ liệu vàng, chạy bộ ngoại tuyến trong CI, đăng ký prompt giám khảo LLM cùng điểm hiệu chuẩn, và theo dõi chỉ số trực tuyến mỗi tính năng. Quản trị nằm bên trên, với các bậc rủi ro đặt ngưỡng cần thiết và chữ ký duyệt trước phát hành. Một tính năng giải thích gian lận mới không thể phát hành cho đến khi tập đánh giá của nó được rà soát, bộ đội đỏ của nó đạt, và chủ sở hữu chịu trách nhiệm ký các kết quả. Tái sử dụng nền tảng nghĩa là các đội tranh luận về miền của họ, không phải về cách đo.

**Chính phủ.** Một cơ quan y tế công triển khai một trợ lý giúp nhân viên trả lời câu hỏi trợ cấp từ hướng dẫn đã phê duyệt. Vì một câu trả lời sai có thể ảnh hưởng đến tư cách hưởng của ai đó, đánh giá phải kiểm toán được. Mỗi bản phát hành chạy một tập đánh giá có tài liệu bao quát câu hỏi thường gặp, trường hợp biên và prompt đối kháng, và kết quả, phiên bản tập dữ liệu, các chỉ số và tên người rà soát được lưu trữ làm bằng chứng trách nhiệm giải trình. Một bộ đội đỏ kiểm tra rằng hệ thống từ chối bịa chính sách hay nêu luật không có trong nguồn của nó. Khi một cơ quan giám sát hỏi cơ quan biết công cụ an toàn thế nào, câu trả lời là một bản ghi có ngày tháng, không phải lời trấn an.

## Luận chứng kinh doanh: động lực, ROI và TCO

Đánh giá tự trả giá bằng cách làm mọi khoản đầu tư AI khác an toàn và nhanh hơn. Lợi tức đầu tư (ROI) của nó hiện ra là ít sự cố sản xuất hơn, lặp nhanh hơn vì các đội đổi prompt và mô hình tự tin, và khả năng áp dụng mô hình tốt hơn ngay ngày chúng đến vì bạn chứng minh được chúng có giúp ích không. Cách rõ nhất để định giá nó là chi phí khi thiếu nó: một ảo giác công khai, đầu ra thiên kiến hay vụ rò dữ liệu duy nhất có thể tốn nhiều hơn hẳn về khắc phục, mất niềm tin và phơi nhiễm quy định so với nhiều năm hạ tầng đánh giá. Đó là sự khác biệt giữa việc tìm một hồi quy trong CI miễn phí và tìm nó trên báo.

Tổng chi phí sở hữu (TCO) là thật và đáng gọi tên. Bạn trả cho lao động chú thích, cho tính toán mà giám khảo tự động tiêu thụ, và cho công việc liên tục giữ tập đánh giá đại diện khi cách dùng dịch chuyển. Ở quy mô doanh nghiệp, một nền tảng dùng chung phân bổ phần lớn chi phí này qua nhiều đội, là lập luận mạnh nhất để xây một cái thay vì để mỗi nhóm ứng biến. Hãy lập luận với ban lãnh đạo bằng cách ghép một rủi ro cụ thể (chi phí của một câu trả lời công khai tồi trong miền của bạn) với một năng lực cụ thể (tốc độ áp dụng an toàn từng mô hình mới), và bằng cách đóng khung đánh giá là kiểm soát cho phép tổ chức di chuyển nhanh mà không di chuyển liều lĩnh.

## Phản mẫu và cạm bẫy

- **Phát hành theo cảm tính.** Đánh giá thay đổi AI bằng cách thử vài prompt bằng tay, không có tập dữ liệu và không có điểm lặp lại được.
- **Sân khấu chuẩn.** Tin điểm chuẩn công khai mạnh là bằng chứng hệ thống phù hợp nhiệm vụ của bạn, bỏ qua ô nhiễm và lệch phân phối.
- **Quá khớp với tập đánh giá.** Chỉnh prompt theo cùng một tập cố định cho đến khi con số cao và vô nghĩa, không có tập giữ lại mới.
- **Giám khảo không hiệu chuẩn.** Triển khai một LLM-làm-giám-khảo và tin điểm của nó mà không bao giờ kiểm tra sự đồng thuận với người chấm.
- **Sùng bái chỉ số.** Tối ưu BLEU hay ROUGE như thể đó là chất lượng, và phát hành câu trả lời tệ hơn tình cờ trùng với văn bản tham chiếu.
- **Đội đỏ một lần.** Tấn công hệ thống một lần trước khi ra mắt và không bao giờ biến phát hiện thành kiểm thử hồi quy vĩnh viễn.
- **Tự tin chỉ ngoại tuyến.** Tin điểm ngoại tuyến tốt nghĩa là tính năng hoạt động, không đo trực tuyến kết quả thực.
- **Tập đánh giá mồ côi.** Tập dữ liệu không ai sở hữu, không bao giờ hấp thụ thất bại sản xuất và dần thôi phản ánh thực tế.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Thay đổi AI được đánh giá bằng tay trên vài ví dụ, một cách phản ứng, khi ai đó tình cờ lo lắng. Không có tập dữ liệu, không có điểm lặp lại được, và không có cổng. Hồi quy được người dùng tìm ra, và không ai nói được hệ thống tốt hơn hay tệ hơn tháng trước.
- **Mức 2, Phát triển:** Một số đội giữ các tập vàng nhỏ và chạy chúng thủ công trước các thay đổi lớn, và vài điểm cổ điển hoặc dựa trên tham chiếu tồn tại. Rà soát của con người xảy ra cho các tính năng quan trọng, nhưng chấm điểm không nhất quán giữa các đội, đánh giá không tự động hay chặn cổng, và mỗi nhóm làm khác nhau.
- **Mức 3, Chuẩn hóa:** Bộ ngoại tuyến chạy trong tích hợp liên tục ở mỗi thay đổi prompt, mô hình hay truy xuất và chặn cổng hợp nhất, theo một thực hành có tài liệu trong toàn tổ chức. LLM-làm-giám-khảo được hiệu chuẩn với nhãn của con người, đội đỏ là bộ lặp lại được, và tập dữ liệu được sở hữu, đánh phiên bản, và được nuôi bởi thất bại sản xuất, với ô nhiễm được bảo vệ tích cực.
- **Mức 4, Quản lý:** Đánh giá được đo và kiểm soát bằng dữ liệu theo đường cơ sở. Tỷ lệ đồng thuận giám khảo-người, tỷ lệ đạt đội đỏ, điểm theo phân khúc, thành công nhiệm vụ trực tuyến, và độ trôi được theo dõi theo thời gian, và hợp nhất được chặn cổng theo ngưỡng và biên hồi quy thay vì một lần chạy hoàn hảo. Chi phí chú thích và tính toán mỗi lần chạy được lập ngân sách theo từng tính năng, hiệu chuẩn lại diễn ra theo lịch, và mỗi kết quả mang một chủ sở hữu chịu trách nhiệm và chữ ký duyệt.
- **Mức 5, Điều phối:** Một nền tảng đánh giá dùng chung phục vụ toàn tổ chức, và đánh giá ngoại tuyến cùng trực tuyến tạo thành một vòng lặp liên tục gắn với kết quả kinh doanh. Mô hình mới được chứng minh trên các tập đánh giá di chuyển được ngay ngày chúng đến, danh mục thích ứng khi cách dùng và rủi ro dịch chuyển, bằng chứng đánh giá kiểm toán được cho cơ quan quản lý và giám sát, và bài học từ thất bại của một đội chảy vào tập dữ liệu của mọi đội.

## Ý tưởng để thảo luận

1. Làm sao bạn quyết định khi nào một điểm ngoại tuyến đủ mạnh để biện minh cho một thí nghiệm trực tuyến, và khi nào thì không?
2. Tỷ lệ đúng giữa đánh giá của con người và chấm điểm tự động cho hồ sơ rủi ro của bạn là gì, và bạn nên xem xét lại nó bao lâu một lần?
3. Khi một chuẩn công khai và tập đánh giá riêng của bạn bất đồng về mô hình nào tốt hơn, bạn tin cái nào và vì sao?
4. Làm sao bạn giữ một tập đánh giá đại diện khi hành vi người dùng dịch chuyển, mà không để nó phình thành thứ quá chậm để chạy trong CI?
5. Cái gì thuộc về một bộ đội đỏ cho miền của bạn, và ai đủ trình độ để thiết kế các cuộc tấn công?
6. Làm sao bạn đánh giá quỹ đạo của một tác tử, không chỉ câu trả lời cuối, mà không chìm trong chi phí chấm từng bước?

## Những điểm cần ghi nhớ

- Đánh giá AI khác kiểm thử phần mềm vì đầu ra không tất định và hiếm khi có một câu trả lời đúng, nên bạn đo chất lượng qua các ca đại diện thay vì khẳng định giá trị chính xác.
- Thực hành phát triển dựa trên đánh giá: xác định chất lượng đo được trước, rồi xây hướng tới nó, và gộp mọi thất bại sản xuất vào tập.
- Xếp lớp phương pháp theo tốc độ và độ trung thực: chấm tự động rẻ cho lặp lại liên tục, phán đoán của con người làm mỏ neo, và hiệu chuẩn để giữ chúng thẳng hàng.
- Bảo vệ chống ô nhiễm và quá khớp, nếu không các con số sẽ tâng bốc bạn trong khi hệ thống thật làm người dùng thất vọng.
- Nối đánh giá ngoại tuyến vào CI như một cổng và tiếp tục đo chất lượng cùng độ trôi trong môi trường sản xuất, vì một mô hình tốt lúc ra mắt có thể suy giảm.

## Tài liệu tham khảo và đọc thêm

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviours, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
