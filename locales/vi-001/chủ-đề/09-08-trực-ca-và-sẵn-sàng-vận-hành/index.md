# 9.8 Trực ca và sẵn sàng vận hành

## Tổng quan và động lực

Giờ này có ai đó đang thức vì hệ thống của bạn có thể gọi họ. Trực ca là sự sắp xếp của con người đặt một người đủ năng lực trong tầm với của một vấn đề sản xuất vào bất kỳ giờ nào, và sẵn sàng vận hành là công việc bạn làm trước để người đó có cơ hội chiến đấu. Chương này nói về sự sẵn sàng đó và hệ thống con người đó: cách bạn thiết kế một vòng trực mà mọi người duy trì được nhiều năm, cách bạn quyết định điều gì đáng đánh thức ai đó, và cách bạn bảo đảm một dịch vụ thực sự sẵn sàng để được vận hành trước khi để nó gánh lưu lượng thật.

Hãy giữ nó tách biệt với hai người láng giềng. Chương 9.3 bao quát quản lý sự cố, quy trình ứng phó khi có gì đó đang hỏng thật: vai trò chỉ huy, mức nghiêm trọng, phối hợp và rút kinh nghiệm. Chương 9.1 bao quát [kỹ thuật độ tin cậy hệ thống](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE), kỷ luật rộng hơn về kỹ thuật hóa độ tin cậy bằng mục tiêu mức dịch vụ và ngân sách lỗi. Chương này nằm thượng nguồn của sự cố và bên cạnh kỷ luật đó. Nó hỏi một câu hẹp hơn, cá nhân hơn: dịch vụ đã sẵn sàng để chạy chưa, và người mang máy nhắn được chuẩn bị để thành công thay vì chịu khổ chưa? Một tổ chức có thể có quy trình sự cố xuất sắc mà vẫn làm kỹ sư kiệt sức, vì nỗi đau của trực ca được quyết định rất lâu trước bất kỳ sự cố nào, bởi chất lượng cảnh báo, trạng thái sổ tay vận hành, và tính nhân đạo của lịch trực.

Với các đội lớn, trực ca thôi là một ân huệ không chính thức và trở thành hạ tầng. Một nền tảng với hàng trăm dịch vụ và hàng chục đội không thể dựa vào một người tình cờ biết mọi thứ hoạt động thế nào. Nó cần vòng trực, đường leo thang và tiêu chuẩn sẵn sàng đứng vững khi các tác giả gốc đã chuyển đi. Trong bối cảnh doanh nghiệp và chính phủ rủi ro còn cao hơn. Dịch vụ chịu quy định mang cam kết sẵn sàng và nghĩa vụ chăm sóc với nhân viên vận hành chúng. Một hệ thống trợ cấp hay y tế hướng công dân không thể tắt đèn qua đêm vì người duy nhất hiểu nó đang đi nghỉ. Sẵn sàng vận hành là cách một thể chế giữ lời hứa sau khi bữa tiệc ra mắt kết thúc, và trực ca nhân đạo là cách nó giữ những người giữ những lời hứa đó.

## Các nguyên tắc chính

- Chỉ gọi con người cho vấn đề khẩn cấp, hành động được và có thật.
- Thiết kế vòng trực cho một người có cuộc sống, không phải một cỗ máy luôn sẵn sàng.
- Chứng minh một dịch vụ sẵn sàng vận hành trước khi nó gánh lưu lượng sản xuất.
- Cảnh báo theo triệu chứng người dùng nhìn thấy và SLO, không theo mọi nguyên nhân nội bộ.
- Coi sổ tay vận hành và rà soát sẵn sàng là tài liệu sống được dùng, không phải hồ sơ cất.
- Ai xây một dịch vụ nên giúp chạy nó, trong giới hạn nhân đạo và được hỗ trợ.
- Đo sức khỏe trực ca và cắt lao động nhàm chán để tải có xu hướng giảm, không tăng.

## Khuyến nghị

### Thiết kế vòng trực nhân đạo, bền vững

Hãy bắt đầu với hình dạng của lịch, vì nó quyết định tính bền vững nhiều hơn bất kỳ công cụ nào. Một mẫu phổ biến là vòng trực hằng tuần với một người ứng phó chính nhận cuộc gọi trước và một người phụ làm dự phòng khi người chính không xác nhận hoặc cần giúp. Giữ nhóm đủ lớn để không kỹ sư nào trực quá một tuần trong bốn, và lý tưởng là một trong sáu hoặc hơn. Một vòng trực bốn người hoặc ít hơn là dấu hiệu cảnh báo: bệnh, kỳ nghỉ và nghỉ việc sẽ làm nó sụp thành cùng hai anh hùng kiệt sức.

Nơi bạn vận hành qua các múi giờ, hãy ưu tiên mô hình [theo mặt trời](https://en.wikipedia.org/wiki/Follow-the-sun), trong đó các đội ở các khu vực khác nhau mỗi đội bao phủ giờ ban ngày của mình để không ai thường xuyên bị gọi lúc 3 giờ sáng. Điều này tôn trọng [nhịp sinh học ngày đêm](https://en.wikipedia.org/wiki/Circadian_rhythm), chu kỳ ngủ-thức bên trong của cơ thể, mà sự gián đoạn là chi phí sức khỏe trực tiếp, không phải phiền toái nhỏ. Khi không theo mặt trời được, hãy nén nỗi đau: khối ca đêm ngắn hơn, thời gian hồi phục được bảo đảm sau một đêm tồi, và quy tắc tường minh rằng một kỹ sư bị gọi nặng qua đêm không nợ một ngày công việc tính năng đầy đủ vào sáng hôm sau.

Leo thang là tấm lưới an toàn bên dưới vòng trực. Hãy xác định, bằng văn bản, điều gì xảy ra khi người chính không xác nhận một cuộc gọi trong một cửa sổ đặt trước: nó chuyển sang người phụ, rồi đến trưởng nhóm hoặc quản lý, rồi đến nhóm rộng hơn. Một [chính sách leo thang](https://en.wikipedia.org/wiki/Escalation) tự động và được hiểu rõ nghĩa là không cuộc gọi nào rơi lặng lẽ xuống sàn, và không một người mệt mỏi duy nhất nào là tuyến phòng thủ duy nhất.

### Làm chính sách gọi xoay quanh vấn đề hành động được, khẩn cấp, có thật

Cách nhanh nhất để phá hủy một vòng trực là gọi người vì những thứ họ không thể hoặc không cần hành động. Hãy áp dụng một quy tắc và bảo vệ nó quyết liệt: một cuộc gọi là lời tuyên bố rằng một con người phải làm gì đó ngay bây giờ. Nếu một cảnh báo không đáp ứng cả ba phép thử, khẩn cấp, hành động được, và mô tả vấn đề thật người dùng nhìn thấy, nó không xứng đáng một cuộc gọi. Hãy chuyển nó sang phiếu, bảng điều khiển hoặc bản tóm tắt hằng ngày.

Kẻ thù ở đây là [mệt mỏi cảnh báo](https://en.wikipedia.org/wiki/Alarm_fatigue), hiện tượng được ghi nhận tốt trong đó những người tiếp xúc với báo động thường xuyên trở nên chai lì và bắt đầu phớt lờ chúng, kể cả những cái quan trọng. Đó là khái niệm an toàn bệnh nhân từ bệnh viện, và nó chuyển sang phần mềm đúng nguyên. Khi mỗi ca mang hai mươi cuộc gọi và mười chín là nhiễu, người ứng phó học cách gạt chúng đi trong lúc nửa tỉnh, và cuộc thứ hai mươi, cái thật, nhận cùng sự phớt lờ phản xạ. Mỗi cảnh báo ồn bạn chấp nhận là một khoản thuế nhỏ đánh vào uy tín của mọi cảnh báo khác.

Hãy coi chất lượng cảnh báo là sản phẩm kỹ thuật hạng nhất. Theo dõi tỷ lệ xác nhận-trên-hành động: trong các cuộc gọi đã kích hoạt, bao nhiêu cái dẫn đến việc con người làm điều gì đó quan trọng? Một cảnh báo chưa bao giờ đòi hành động trong cả quý là ứng viên cho xóa hoặc hạ cấp. Hãy rà soát cảnh báo theo nhịp đều đặn, và trao cho bất kỳ kỹ sư nào tư cách thách thức một cái ồn. Mục tiêu là một vòng trực nơi một cuộc gọi đủ hiếm để nó vẫn có nghĩa.

### Cảnh báo theo triệu chứng và SLO, không theo nguyên nhân

Cách hiệu quả nhất để cắt nhiễu là đổi thứ bạn cảnh báo. Cảnh báo theo nguyên nhân, như CPU cao, đĩa đầy, hay một tiến trình khởi động lại, tạo dòng cuộc gọi cho các điều kiện có thể không bao giờ ảnh hưởng người dùng và hệ thống thường tự chữa. Thay vào đó hãy cảnh báo theo triệu chứng: dịch vụ có đang làm điều người dùng cần không? Hãy gắn cảnh báo gọi của bạn với [mục tiêu mức dịch vụ](https://en.wikipedia.org/wiki/Service-level_objective) (SLO), các mục tiêu độ tin cậy bằng số xác định trong chương 9.1, và gọi khi bạn đang đốt qua ngân sách lỗi đủ nhanh để trượt mục tiêu, hoặc khi một chỉ báo hướng người dùng như độ trễ hay tỷ lệ thành công vượt một lằn ranh mà mọi người thực sự cảm nhận.

Cách tiếp cận theo triệu chứng, do SLO dẫn dắt này phụ thuộc vào khả năng quan sát và đo từ xa của chương 9.2, vì cảnh báo tốc độ đốt chỉ hoạt động khi chỉ số, nhật ký và vết của bạn có cấu trúc và đáng tin. Lợi ích rất lớn: một nhúm cảnh báo triệu chứng có ý nghĩa thay hàng trăm cảnh báo nguyên nhân, và một cuộc gọi lại tương quan với vấn đề đáng thức dậy. Nguyên nhân vẫn quan trọng, nhưng chúng thuộc về bảng điều khiển chẩn đoán mà người ứng phó tham khảo sau khi cảnh báo triệu chứng kích hoạt, không phải đường gọi.

### Yêu cầu sẵn sàng vận hành trước khi ra mắt

Một dịch vụ nên giành được chỗ của nó trong môi trường sản xuất. Trước khi nó gánh lưu lượng thật, hãy đưa nó qua một rà soát sẵn sàng sản xuất: một kiểm tra có cấu trúc, lý tưởng bởi người ngoài đội xây, rằng dịch vụ thực sự vận hành được. Hãy mã hóa rà soát thành danh mục kiểm tra trở thành tiêu chuẩn chung qua các đội. Một danh sách mạnh bao quát giám sát và SLO, cảnh báo đáp ứng chính sách gọi, bảng điều khiển, sổ tay vận hành cho các thất bại có khả năng, quyền sở hữu xác định và vòng trực, kỳ vọng năng lực và tải, phân tích phụ thuộc và kiểu thất bại, sao lưu và khôi phục, kiểm soát bảo mật và truy cập, và kế hoạch hoàn tác.

Rà soát là một cuộc trò chuyện, không phải cổng để lách. Giá trị của nó là buộc đội xây đối mặt với khả năng vận hành khi họ còn ngữ cảnh, thay vì phát hiện lúc 2 giờ sáng sáu tháng sau rằng không ai viết sổ tay vận hành hay đặt cảnh báo. Hãy gắn sẵn sàng với kiểm thử khả năng phục hồi của chương 9.6: một dịch vụ chưa bao giờ bị tiêm thất bại phụ thuộc trước khi ra mắt đang đưa ra lời hứa chưa kiểm thử về cách nó thất bại. Với các lần ra mắt doanh nghiệp và chính phủ rủi ro cao, hãy biến rà soát sẵn sàng thành bước bắt buộc, có tài liệu, vì chi phí của một dịch vụ hướng công dân chưa sẵn sàng thất bại trước công chúng được đo bằng lòng tin nhiều như bằng tiền.

### Viết sổ tay vận hành và sổ tay kịch bản thực sự được dùng

Một sổ tay vận hành là tài liệu vận hành từng bước: cách khởi động lại dịch vụ này, xoay vòng thông tin xác thực này, xả hàng đợi này, diễn giải cảnh báo này. Một sổ tay kịch bản là hướng dẫn ứng phó rộng hơn cho một loại tình huống. Cả hai đều vô giá trị nếu không ai đọc, và hầu hết sổ tay vận hành không được đọc vì chúng cũ, mơ hồ, hoặc không tìm được lúc 3 giờ sáng. Hãy sửa trực tiếp các kiểu thất bại. Liên kết sổ tay vận hành từ chính cảnh báo, để người ứng phó đến nó trong một cú nhấp từ cuộc gọi. Giữ sổ tay vận hành trong quản lý phiên bản cạnh mã, như thực hành tài liệu của chương 2.7 khuyến nghị, để chúng được rà soát và cập nhật như bất kỳ hiện vật nào khác. Viết chúng cho một người lạ căng thẳng, buồn ngủ, với lệnh cụ thể và đầu ra kỳ vọng, không phải văn xuôi giả định ngữ cảnh của tác giả.

Phép thử của một sổ tay vận hành là liệu người khác tác giả có làm theo thành công dưới áp lực. Hãy xác thực điều đó trong làm quen và ngày diễn tập, và cập nhật sổ tay vận hành ngay khi một sự cố cho thấy nó sai. Một sổ tay vận hành nói dối còn tệ hơn không có, vì nó đưa một người ứng phó mệt mỏi tự tin đi sai hướng.

### Sở hữu những gì bạn xây, trong giới hạn nhân đạo

Phong trào [DevOps](https://en.wikipedia.org/wiki/DevOps) phổ biến "bạn xây nó, bạn chạy nó": đội viết một dịch vụ cũng mang máy nhắn của nó. Lợi ích là thật và đáng bảo vệ. Khi người xây cảm nhận các cuộc gọi của chính họ, họ đầu tư vào độ tin cậy, sửa cảnh báo ồn, và thiết kế cho khả năng vận hành, vì vòng phản hồi đến họ cá nhân thay vì đáp xuống một đội vận hành riêng không sửa được nguyên nhân gốc.

Mô hình có các giới hạn bạn phải tôn trọng. Nó đòi các đội được trang bị thực sự để chạy dịch vụ của họ: được cung cấp công cụ, nền tảng, đào tạo và thời gian để làm vận hành tốt, như hiệu quả kỹ thuật của chương 1.10 và cách làm việc của chương 1.4 đều đòi hỏi. Quyền sở hữu đầy đủ là tàn nhẫn khi áp đặt lên một đội quá nhỏ để bố trí nhân sự vòng trực, hoặc không có hỗ trợ nền tảng làm trực ca chịu được. Một số tổ chức chạy mô hình lai, nơi một đội SRE hoặc nền tảng trung tâm cùng sở hữu các bậc khó nhất hoặc cung cấp bao phủ ngoài giờ cho dịch vụ đáp ứng thanh độ tin cậy cao, giải phóng đội sản phẩm khỏi cuộc gọi đêm thường lệ. Nguyên tắc cần giữ là vòng phản hồi; hình dạng có thể linh hoạt để vừa kích thước đội, độ trưởng thành, và tính nhân đạo của tải.

### Làm quen kỹ sư trực có chủ đích và chạy ngày diễn tập

Không ai nên nhận máy nhắn lần đầu một mình và chưa chuẩn bị. Hãy xây một đường làm quen: theo dõi một người ứng phó có kinh nghiệm trong một vòng trực, theo dõi ngược nơi người mới dẫn dắt với người cố vấn quan sát, một buổi đi qua bảng điều khiển và sổ tay vận hành, và một bản đồ rõ ràng về ai để leo thang. Hãy biến sự sẵn sàng đi trực thành cột mốc tường minh, không phải giả định.

Ngày diễn tập là buổi tập dượt làm trực ca thật. Trong một ngày diễn tập bạn cố ý thực hành một thất bại, lý tưởng là trong môi trường thực tế, và để kỹ sư trực ứng phó chỉ dùng công cụ và sổ tay vận hành họ có trong sự cố thật. Đây là nơi bạn phát hiện sổ tay vận hành đã cũ, bảng điều khiển thiếu một tín hiệu, hoặc cảnh báo không bao giờ kích hoạt. Ngày diễn tập xây trí nhớ cơ bắp và sự tự tin biến cuộc gọi thật đầu tiên từ hoảng loạn thành quy trình, và chúng kết nối tự nhiên với kỹ thuật hỗn loạn của chương 9.6.

### Chạy bàn giao sạch và đo sức khỏe trực ca

Bàn giao giữa các ca là nơi ngữ cảnh rò rỉ. Hãy thiết lập một bàn giao ngắn, có cấu trúc: cái gì hiện đang suy giảm, cảnh báo nào đã kích hoạt và bị tắt, thay đổi nào đang diễn ra, cần theo dõi gì. Ghép nó với vệ sinh trực ca cơ bản, gồm chính sách rằng người ứng phó rời ca không để lại mớ hỗn độn cho người nhận, và bất cứ thứ gì sửa dở được ghi lại.

Trên hết, hãy đo. Bạn không quản lý được tải bạn không thấy. Theo dõi cuộc gọi mỗi ca, phần cuộc gọi rơi ngoài giờ (buổi tối, đêm, cuối tuần), thời gian xác nhận, và bao lâu một lần bậc phụ và bậc leo thang bị kích hoạt. Theo dõi xu hướng, không chỉ con số: một vòng trực có cuộc gọi ngoài giờ leo lên qua từng quý đang hướng đến kiệt sức bất kể số tuyệt đối hiện tại. Hãy nuôi các chỉ số này vào một rà soát vận hành thường xuyên nơi đội quyết định lao động nhàm chán nào để tự động hóa đi, cảnh báo nào để giết, và sẵn sàng thiếu ở đâu. Giảm lao động nhàm chán, công việc vận hành thủ công lặp lại mở rộng theo lưu lượng thay vì được sửa một lần, là cách bạn giữ tải trực ca phẳng trong khi hệ thống lớn lên.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Bạn xây nó, bạn chạy nó | Vòng phản hồi độ tin cậy chặt; chủ sở hữu sửa nguyên nhân gốc | Tàn nhẫn với đội thiếu nguồn lực hoặc rất nhỏ; tải đêm không đều |
| Trực ca SRE hoặc nền tảng trung tâm | Bảo vệ đội sản phẩm khỏi cuộc gọi đêm thường lệ; kỹ năng vận hành sâu | Làm yếu vòng phản hồi của người xây; có thể thành bãi rác |
| Vòng trực theo mặt trời | Không ai bị gọi qua đêm; nhân đạo và lành mạnh | Cần nhân sự ở nhiều khu vực; chi phí chung bàn giao nặng hơn |
| Vòng trực nhỏ tại chỗ | Đơn giản; mọi người biết hệ thống | Sụp đổ khi bệnh hay nghỉ việc; kiệt sức nhanh |
| Cảnh báo triệu chứng và SLO | Ít cuộc gọi, có ý nghĩa; ít mệt mỏi | Cần đo từ xa trưởng thành; có thể bỏ sót nguyên nhân tích tụ chậm |
| Cảnh báo theo nguyên nhân | Bắt vấn đề sớm và cụ thể | Làm ngập người ứng phó; thúc đẩy mệt mỏi cảnh báo |
| Rà soát sẵn sàng nghiêm ngặt | Ít bất ngờ khó chịu hơn trong môi trường sản xuất | Làm chậm ra mắt; có thể cảm giác quan liêu nếu bị lách |

Căng thẳng trung tâm là giữa phạm vi bao phủ và tính nhân đạo. Đẩy phạm vi tối đa và bạn có vòng trực lớn, cảnh báo hung hăng, và quyền sở hữu đầy đủ ở mọi nơi, bảo vệ hệ thống trong khi nghiền nát con người. Tối ưu thuần túy cho sự thoải mái của người ứng phó và bạn rủi ro khoảng trống nơi một vấn đề thật chờ không ai trông. Giải quyết nó không phải bằng chia đôi mà bằng nâng chất lượng: cảnh báo xuất sắc, sổ tay vận hành hoạt động, và dịch vụ sẵn sàng cho phép một vòng trực nhỏ hơn, bình tĩnh hơn bao phủ nhiều đất hơn an toàn. Các tổ chức vận hành tốt nhất thường là những tổ chức có người ứng phó bị gọi ít nhất, vì họ đầu tư vào sự sẵn sàng thay vì sức chịu đựng. Mỗi giờ dành để loại một cảnh báo ồn hay sửa một sổ tay vận hành mua lại nhiều giờ chú ý của con người và bảo vệ uy tín của cả hệ thống.

## Câu hỏi để thảo luận với đội của bạn

1. **Cá nhân bạn có sẵn lòng mang vòng trực này một năm không, và bạn sẽ đổi gì nếu câu trả lời là không?** Câu hỏi này cắt qua trừu tượng vì nó biến tải thành cá nhân. Hãy mang con số thật vào cuộc trò chuyện: tháng trước bao nhiêu cuộc gọi kích hoạt, bao nhiêu cái rơi sau nửa đêm hay cuối tuần, và thời gian xác nhận trung bình bao lâu. Hỏi từng người trong vòng trực liệu hình dạng hiện tại có phải cái họ duy trì được mà không sợ tuần trực của mình, và lắng nghe câu trả lời lặng lẽ nhiều như ồn ào. Nếu câu trả lời trung thực là vòng trực chỉ sống sót được vì vài anh hùng hấp thụ phần tệ nhất, bạn đã tìm thấy sự mong manh sẽ vỡ lần đầu một trong số họ rời đi. Đầu ra bạn muốn là danh sách thay đổi cụ thể, dù là nhóm lớn hơn, chia theo mặt trời, giảm cuộc gọi đêm, hay dọn cảnh báo, với chủ sở hữu và ngày gắn vào mỗi cái.

2. **Với mỗi cảnh báo có thể gọi một con người, bạn có nêu được hành động người ứng phó được kỳ vọng thực hiện không?** Hầu hết vòng trực chưa bao giờ kiểm toán điều này, và bài tập này tiết lộ nhiều. Kéo toàn bộ danh sách cảnh báo gọi và, với từng cái, hỏi người ứng phó được cho là làm gì khi nó kích hoạt và quý trước nó kích hoạt bao nhiêu lần mà không dẫn đến hành động thật nào. Cảnh báo thất bại phép thử, những cái không ai gắn được hành động hoặc luôn tự giải quyết trước khi ai chạm vào, là nhiễu xói mòn lòng tin vào mọi cảnh báo khác. Hãy mang dữ liệu xác nhận-trên-hành động nếu có, và sẵn sàng xóa hoặc hạ cấp quyết liệt. Mục tiêu là một đường gọi nơi mọi cảnh báo là lời yêu cầu giúp đỡ thật của con người, và cuộc họp nên kết thúc với danh sách cảnh báo ngắn hơn, sắc hơn lúc bắt đầu.

3. **Khi một kỹ sư mới vào vòng trực này, chính xác điều gì chuẩn bị cho họ, và bạn đã kiểm thử nó hiệu quả chưa?** Làm quen trực ca thường được giả định hơn là thiết kế, và khoảng trống hiện ra lần đầu một người mới bị gọi một mình vào một thất bại họ chưa từng thấy. Hãy đi qua đường thật mà người ứng phó mới đi: họ theo dõi gì, họ đọc sổ tay vận hành nào, có ai làm theo những sổ tay đó gần đây để xác nhận chúng còn hoạt động không, và họ leo thang tới ai khi mắc kẹt. Hãy thử chọn một sự cố gần đây thật và hỏi liệu một nhân viên mới, chỉ trang bị sổ tay vận hành và bảng điều khiển hiện tại, có giải quyết được nó không. Câu trả lời trung thực thường làm lộ tài liệu cũ và tín hiệu thiếu, chính xác là điều ngày diễn tập nhằm làm lộ trước khi sự cố thật làm vậy. Hãy rời đi với cột mốc sẵn sàng xác định cho trực ca và lịch cho các ngày diễn tập giữ nó trung thực.

4. **Cuộc gọi ngoài giờ của chúng ta thực sự rơi vào đâu, và chúng ta có sẵn lòng đổi nhân sự hay phạm vi bao phủ để bảo vệ giấc ngủ của mọi người không?** Cuộc gọi đêm và cuối tuần mang chi phí sức khỏe mà số đếm thô giấu, nên một vòng trực trông chịu được trung bình vẫn có thể lặng lẽ phá hoại vài người tình cờ bắt các thất bại 3 giờ sáng. Hãy mang bảng phân tích cuộc gọi theo giờ và ngày trong tuần, chia theo dịch vụ và theo người ứng phó, và tìm sự tập trung hơn là trung bình. Cân nhắc đối lập là thật: bao phủ theo mặt trời cần nhân sự ở nhiều hơn một khu vực và thêm chi phí chung bàn giao, trong khi vòng trực nhỏ tại chỗ đơn giản hơn nhưng để ai đó sở hữu các đêm. Hãy quyết định có chủ đích bản sửa là vòng trực khu vực thứ hai, một đội nền tảng trung tâm nhận các bậc ngoài giờ, khối ca đêm ngắn hơn với thời gian hồi phục được bảo đảm, hay dọn cảnh báo loại nhiễu ban đêm tại nguồn. Với các nhà vận hành doanh nghiệp và chính phủ, hãy coi nghĩa vụ chăm sóc nhân viên trực là nghĩa vụ chính thức có chủ sở hữu và chỉ số báo cáo, không phải khẩu hiệu phúc lợi, vì cơ quan quản lý hay hội đồng lao động có thể cuối cùng yêu cầu bạn chứng minh.

5. **Rà soát sẵn sàng sản xuất của chúng ta là cuộc trò chuyện thực sự về cách dịch vụ thất bại, hay danh mục kiểm tra bị lách để qua cổng?** Một rà soát sẵn sàng chỉ sinh lời nếu nó đổi cái được phát hành, và kiểu thất bại là một biểu mẫu điền buổi chiều trước ra mắt để thỏa mãn một quy trình không ai tin. Hãy mang vài rà soát hoàn tất gần nhất và hỏi mỗi cái thực sự bắt được gì: sổ tay vận hành thiếu, hoàn tác chưa kiểm thử, cảnh báo không bao giờ kích hoạt, hay không gì cả. Căng thẳng là giữa tốc độ ra mắt và độ chặt chẽ vận hành, và một rà soát cảm giác như quan liêu sẽ bị lách trong khi cái làm lộ kiểu thất bại thật sẽ bị oán cho đến lần đầu nó cứu giấc ngủ của ai đó. Hãy quyết định ai chạy rà soát, liệu đó có phải người ngoài đội xây, và bằng chứng nào, như thất bại phụ thuộc được tiêm hay sổ tay vận hành một người lạ làm theo được, được tính là đạt. Trong các lần ra mắt doanh nghiệp và chính phủ, hãy giữ rà soát hoàn tất làm hiện vật kiểm toán và gắn nó với kiểm thử khả năng phục hồi của chương 9.6, vì một dịch vụ hướng công dân chưa sẵn sàng thất bại công khai tốn lòng tin mà không hoàn tác nào khôi phục được.

6. **"Bạn xây nó, bạn chạy nó" thực sự phục vụ chúng ta ở đâu, và nó lặng lẽ tàn nhẫn với đội mà chúng ta chưa cấp nguồn lực để chạy dịch vụ của họ ở đâu?** Quyền sở hữu đầy đủ tạo vòng phản hồi khiến người xây sửa cảnh báo ồn và thiết kế cho khả năng vận hành, nhưng áp đặt lên một đội quá nhỏ để bố trí vòng trực nhân đạo, nó thành động cơ kiệt sức chậm khoác áo trách nhiệm giải trình. Hãy mang bản đồ đội nào sở hữu máy nhắn nào, mỗi vòng trực thực sự lớn bao nhiêu khi bạn loại những người không bao giờ nhận cuộc gọi khó, và nền tảng, công cụ và đào tạo nào mỗi đội có để chạy vận hành tốt. Lực kéo đối lập là giữa nguyên tắc sạch sẽ của quyền sở hữu phổ quát và thực tế lộn xộn rằng một số bậc cần đội SRE hoặc nền tảng trung tâm cùng sở hữu công việc độ tin cậy khó nhất hoặc cung cấp bao phủ ngoài giờ. Đầu ra bạn muốn là phân loại trung thực mỗi dịch vụ thành sở hữu đầy đủ, cùng sở hữu, hoặc được bao phủ tập trung, với khoảng cách nguồn lực được nêu tên cho bất kỳ đội nào bạn đang yêu cầu chạy thứ họ không duy trì được. Với một tổ chức lớn hay công, hãy thêm thời gian chờ mua sắm và tuyển dụng cho hỗ trợ nền tảng và nhân sự mà quyền sở hữu nhân đạo giả định, vì một đội bạn không bố trí nhân sự được trong khung thời gian liên quan là đội bạn đang đặt vào thất bại.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư, mọi người đều trực và không có chỗ để một vòng trực anh hùng ẩn nấp. Hãy dành thời gian khan hiếm cho hai thay đổi sinh lời nhanh nhất: xóa cảnh báo theo nguyên nhân và chỉ gọi trên vài SLO theo dõi luồng cốt lõi của bạn, và liên kết sổ tay vận hành một trang từ mỗi cảnh báo còn lại. Bỏ qua công cụ cầu kỳ và theo mặt trời; một bảng tính chung, leo thang tự động từ chính sang phụ, và quy tắc cứng rằng một đêm tồi mua sáng hôm sau nghỉ sẽ đưa bạn xa hơn bất kỳ lần mua nền tảng nào.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có SRE riêng và không thể bố trí nhân sự vòng trực đêm, vì vậy hãy dựa vào thứ bạn mua hơn thứ bạn xây. Ưu tiên dịch vụ được quản lý và lưu trữ mà nhà cung cấp mang các cuộc gọi hạ tầng sâu, và dùng công cụ gọi lưu trữ thay vì tự lăn leo thang của bạn. Đóng khung sẵn sàng như một danh mục kiểm tra ngắn và một nhúm cảnh báo có ý nghĩa gắn với điều khách hàng sẽ nhận ra, và trung thực rằng một số dịch vụ đơn giản không nên gọi con người qua đêm khi một phiếu buổi sáng là đủ.

**Doanh nghiệp lớn.** Vấn đề là nhất quán qua nhiều đội: một rà soát sẵn sàng sản xuất dùng chung, chính sách gọi chung, và kho sổ tay vận hành trong quản lý phiên bản để một kỹ sư chuyển giữa các đội hiểu ngay hệ thống trực ca. Hãy biến sức khỏe trực ca thành chỉ số được quản trị với ngưỡng cuộc gọi ngoài giờ kích hoạt rà soát, chuẩn hóa leo thang và bàn giao để không cuộc gọi nào rơi lặng lẽ, và để đội nền tảng trung tâm cùng sở hữu các bậc khó nhất. Quản lý danh mục vòng trực như bạn quản lý danh mục dịch vụ, với dữ liệu về lao động nhàm chán, tải cuộc gọi và rủi ro kiệt sức nuôi một rà soát vận hành thường xuyên.

**Chính phủ.** Quy tắc mua sắm, minh bạch và nghĩa vụ chăm sóc định hình sự sắp xếp. Hãy coi sức khỏe của nhân viên trực là yêu cầu chính thức, kiểm toán được, và nơi nhân sự qua đêm hạn chế, hãy ký hợp đồng với đối tác vận hành theo mặt trời để không công chức nào thường xuyên bị gọi lúc 3 giờ sáng. Giữ mỗi rà soát sẵn sàng hoàn tất làm hiện vật kiểm toán, viết sổ tay vận hành để được thực thi bởi người ứng phó không xây hệ thống, vì những người vận hành nó sau năm năm sẽ không phải tác giả của nó, và diễn tập đỉnh theo mùa bằng ngày diễn tập trước khi công dân gặp nó thật.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười hai người ra mắt sản phẩm trả phí đầu tiên và đặt cả sáu kỹ sư vào vòng trực hằng tuần với một chính và một phụ. Tháng đầu máy nhắn kêu hằng đêm, chủ yếu vì cảnh báo CPU và đĩa tự giải quyết, và hai kỹ sư lặng lẽ bắt đầu tìm việc. Đội dừng lại và xây lại: họ xóa mọi cảnh báo theo nguyên nhân, xác định hai SLO cho thanh toán và tìm kiếm, và chỉ gọi khi ngân sách lỗi cháy. Cuộc gọi giảm từ khoảng bốn mươi mỗi tuần xuống ba. Họ thêm danh mục sẵn sàng một trang mà mọi dịch vụ mới phải qua và liên kết mỗi sổ tay vận hành trực tiếp từ cảnh báo của nó. Trực ca đi từ lý do người rời đi thành phần quản lý được của công việc, và họ làm điều đó bằng bảng tính và kỷ luật thay vì công cụ đắt tiền.

**Doanh nghiệp lớn.** Một công ty thanh toán toàn cầu chạy hàng trăm dịch vụ theo mô hình "bạn xây nó, bạn chạy nó", được hậu thuẫn bởi một đội nền tảng trung tâm cung cấp hệ thống gọi, quy trình rà soát sẵn sàng và kho sổ tay vận hành chung trong quản lý phiên bản. Mọi dịch vụ qua một rà soát sẵn sàng sản xuất có tài liệu trước khi ra mắt, bao quát SLO, cảnh báo, sổ tay vận hành, năng lực và hoàn tác. Sức khỏe trực ca là chỉ số được theo dõi: các đội có cuộc gọi ngoài giờ vượt ngưỡng kích hoạt rà soát tự động, và đội nền tảng đề nghị cùng sở hữu công việc độ tin cậy cho đến khi tải hạ xuống. Ngày diễn tập chạy hằng quý với tiêm lỗi thực tế. Vì tiêu chuẩn đồng nhất và công cụ dùng chung, một kỹ sư có thể chuyển giữa các đội và hiểu ngay hệ thống trực ca, và lãnh đạo thấy được, theo từng đội, liệu tải con người có bền vững.

**Chính phủ.** Một cơ quan thuế quốc gia vận hành hệ thống khai thuế với đỉnh theo mùa cứng và nghĩa vụ pháp lý duy trì sẵn sàng với công dân. Vì lực lượng lao động tập trung ở một múi giờ và nhân sự qua đêm hạn chế, cơ quan ký hợp đồng sắp xếp theo mặt trời với một đối tác vận hành để không công chức nào thường xuyên bị gọi giữa đêm, và coi sức khỏe cùng nghĩa vụ chăm sóc của nhân viên trực là yêu cầu chính thức. Mọi thay đổi dịch vụ qua một rà soát sẵn sàng vận hành trước khi triển khai, với danh mục được giữ cho kiểm toán. Sổ tay vận hành được viết để người ứng phó không xây hệ thống thực thi, vì những người chạy nó sau năm năm sẽ không phải những người đã viết nó. Trong mùa khai thuế cơ quan chạy ngày diễn tập theo kịch bản tải đỉnh, để người ứng phó gặp đợt tăng trong buổi tập dượt trước khi gặp nó thật.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của sẵn sàng vận hành và trực ca nhân đạo hiện ra trên hai sổ cái: độ tin cậy của hệ thống và việc giữ chân đội. Về độ tin cậy, các dịch vụ qua rà soát sẵn sàng và mang cảnh báo theo triệu chứng thất bại ít hơn và phục hồi nhanh hơn, vì sổ tay vận hành tồn tại, cảnh báo có ý nghĩa, và người ứng phó đã được tập dượt. Thời gian xác nhận trung bình và thời gian phục hồi trung bình đều giảm khi một cuộc gọi đến một người đã chuẩn bị với sổ tay vận hành được liên kết thay vì một người bối rối đi tìm ngữ cảnh. Về phía con người, trực ca là nguyên nhân hàng đầu của kỹ sư nghỉ việc, và thay thế một kỹ sư cấp cao tốn nhiều lần khoản đầu tư để sửa vòng trực. [Kiệt sức nghề nghiệp](https://en.wikipedia.org/wiki/Occupational_burnout), trạng thái kiệt quệ mạn tính ở nơi làm việc mà Tổ chức Y tế Thế giới công nhận là hiện tượng nghề nghiệp, đắt chính vì nó lấy đi những người giàu kinh nghiệm nhất của bạn, những người hiểu hệ thống, và đẩy họ ra.

Chi phí áp dụng chủ yếu một lần và khiêm tốn. Bạn viết danh mục sẵn sàng, di chuyển cảnh báo từ nguyên nhân sang triệu chứng, đặt sổ tay vận hành vào quản lý phiên bản, và dựng chỉ số sức khỏe trực ca. Chi phí lặp lại là kỷ luật rà soát cảnh báo, chạy ngày diễn tập, và tôn trọng lịch nhân đạo. Chi phí của sự bỏ bê cộng dồn lặng lẽ: cảnh báo ồn sinh mệt mỏi, mệt mỏi sinh sự cố thật bị bỏ lỡ và nghỉ việc, và mỗi lần nghỉ việc mang đi tri thức vận hành, làm tăng tải cho những người còn lại. Để lập luận với ban lãnh đạo, hãy nối sức khỏe trực ca với các chỉ số họ đã theo dõi: tần suất và thời lượng sự cố, thời gian xác nhận, nghỉ việc ngoài kế hoạch, và xu hướng cuộc gọi ngoài giờ. Một vòng trực có cuộc gọi ngoài giờ đang giảm trong khi hệ thống lớn lên là bằng chứng trực tiếp rằng khoản đầu tư độ tin cậy của bạn đang hiệu quả và kỹ sư của bạn vẫn ở đây năm sau.

## Phản mẫu và cạm bẫy

- **Vòng trực anh hùng:** hai ba người lặng lẽ hấp thụ mọi cuộc gọi khó, nên lịch trông ổn trên giấy và sụp đổ ngay khi một trong số họ rời đi.
- **Gọi theo nguyên nhân:** cảnh báo trên CPU, bộ nhớ và đĩa thay vì triệu chứng người dùng nhìn thấy, làm ngập người ứng phó bằng cuộc gọi không bao giờ cần con người.
- **Chấp nhận mệt mỏi cảnh báo:** cảnh báo ồn đã biết nằm trong đường gọi nhiều tháng vì xóa chúng cảm giác rủi ro, cho đến khi người ứng phó phớt lờ mọi thứ.
- **Sổ tay vận hành mục rữa:** tài liệu viết một lần lúc ra mắt, không bao giờ cập nhật, và sai một cách tự tin khi một người ứng phó mệt mỏi làm theo lúc 3 giờ sáng.
- **Quyền sở hữu không có hỗ trợ:** áp đặt "bạn xây nó, bạn chạy nó" lên đội quá nhỏ để bố trí vòng trực hoặc thiếu nền tảng và công cụ để chạy nó nhân đạo.
- **Sân khấu sẵn sàng:** danh mục rà soát được điền để qua cổng thay vì thực sự đối mặt cách dịch vụ thất bại.
- **Ra mắt rồi bỏ:** phát hành một dịch vụ không vòng trực, không cảnh báo, không sổ tay vận hành, rồi phát hiện khoảng trống trong lần ngừng hoạt động đầu tiên.
- **Tải không đo:** không có dữ liệu về cuộc gọi mỗi ca hay cuộc gọi ngoài giờ, nên kiệt sức vô hình cho đến khi mọi người nghỉ việc.
- **Cuộc gọi đầu không tập dượt:** đặt một kỹ sư mới vào trực ca mà không theo dõi và không ngày diễn tập, rồi ngạc nhiên khi họ đứng hình.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Trực ca không chính thức và phản ứng. Vài người được gọi điện khi mọi thứ hỏng, cảnh báo kích hoạt theo nguyên nhân và phần lớn là nhiễu, sổ tay vận hành thiếu hoặc cũ, dịch vụ ra mắt mà không kiểm tra sẵn sàng, và không ai đo tải con người cho đến khi ai đó kiệt sức hoặc nghỉ việc.
- **Mức 2, Phát triển:** Thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Một số vòng trực có chính, phụ và leo thang xác định, một số cảnh báo được điều chỉnh và một số sổ tay vận hành được viết, và danh mục sẵn sàng tồn tại nhưng áp dụng không nhất quán. Cuộc gọi có thể được đếm ở các đội chịu khó, cuộc gọi đêm phổ biến, và làm quen trực ca được ứng biến thay vì thiết kế.
- **Mức 3, Chuẩn hóa:** Rà soát sẵn sàng là bước có tài liệu trước ra mắt, được thực thi qua các đội. Gọi theo triệu chứng và SLO theo chính sách chung, sổ tay vận hành sống trong quản lý phiên bản và liên kết từ cảnh báo, làm quen gồm theo dõi và ngày diễn tập, bàn giao theo định dạng có cấu trúc, và leo thang đồng nhất đủ để một kỹ sư chuyển giữa các đội nhận ra hệ thống ngay.
- **Mức 4, Quản lý:** Trực ca được đo và kiểm soát theo đường cơ sở. Cuộc gọi mỗi ca, tỷ lệ ngoài giờ, thời gian xác nhận, tần suất leo thang, và tỷ lệ xác nhận-trên-hành động được theo dõi theo từng đội và so với mục tiêu, nên một vòng trực trôi về kiệt sức hiện ra trước khi mọi người nghỉ việc thay vì sau. Ngưỡng kích hoạt rà soát, chất lượng cảnh báo được kiểm toán dựa trên bằng chứng cuộc gọi nào dẫn đến hành động thật, và quyết định nhân sự cùng quyền sở hữu được dẫn dắt bởi dữ liệu thay vì giai thoại.
- **Mức 5, Điều phối:** Sức khỏe trực ca là kết quả được cải thiện liên tục và tích hợp trong toàn tổ chức. Xu hướng cuộc gọi và ngoài giờ giảm khi hệ thống lớn lên, lao động nhàm chán được tự động hóa có hệ thống, theo mặt trời hoặc tương đương bảo vệ giấc ngủ, ngày diễn tập và tiêm lỗi là thường lệ, và tổ chức thích ứng quyền sở hữu, phạm vi bao phủ và tiêu chuẩn sẵn sàng khi học từ mỗi ca, cân bằng lại tải qua các đội và khu vực khi bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

1. Tỷ lệ hiện tại của bạn giữa cuộc gọi dẫn đến hành động thật và cuộc gọi tự giải quyết là bao nhiêu, và cần gì để đo nó?
2. Nếu người ứng phó am hiểu nhất của bạn nghỉ việc ngày mai, dịch vụ nào trở nên không an toàn để vận hành, và vì sao?
3. "Bạn xây nó, bạn chạy nó" phục vụ bạn tốt ở đâu, và nó lặng lẽ tàn nhẫn với đội thiếu nguồn lực ở đâu?
4. Lần cuối bạn xem một kỹ sư mới làm theo một trong các sổ tay vận hành của bạn dưới điều kiện thực tế là khi nào, và cái gì hỏng?
5. Cuộc gọi ngoài giờ của bạn đang có xu hướng tăng hay giảm trong bốn quý qua, và có ai sở hữu con số đó không?
6. Mục rà soát sẵn sàng nào, nếu bạn thực thi nghiêm, sẽ ngăn được lần ra mắt tồi gần nhất của bạn?

## Những điểm cần ghi nhớ

- Sự sẵn sàng trực ca được quyết định trước bất kỳ sự cố nào, bởi chất lượng cảnh báo, sổ tay vận hành và vòng trực của bạn, không phải bởi anh hùng chủ nghĩa trong lúc ngừng hoạt động.
- Chỉ gọi con người cho vấn đề khẩn cấp, hành động được và người dùng nhìn thấy; cảnh báo theo triệu chứng và SLO, và chuyển mọi thứ khác sang phiếu và bảng điều khiển.
- Thiết kế vòng trực cho người có cuộc sống: nhóm đủ lớn, theo mặt trời nơi có thể, leo thang tự động, và thời gian hồi phục được tôn trọng.
- Chứng minh dịch vụ sẵn sàng trước ra mắt bằng rà soát sẵn sàng sản xuất, giữ sổ tay vận hành trong quản lý phiên bản và liên kết từ cảnh báo, và tập dượt bằng ngày diễn tập.
- Đo sức khỏe trực ca, đặc biệt cuộc gọi ngoài giờ và thời gian xác nhận, và kéo tải xuống bằng cách cắt lao động nhàm chán và nhiễu thay vì yêu cầu mọi người chịu đựng nhiều hơn.

## Tài liệu tham khảo và đọc thêm

- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara và Stephen Thorne (biên tập), *The Site Reliability Workbook: Practical Ways to Implement SRE*
- Rob Ewaschuk, "My Philosophy on Alerting," trong phụ lục *Site Reliability Engineering*
- John Allspaw và Jesse Robbins (biên tập), *Web Operations: Keeping the Data on Time*
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Gene Kim, Jez Humble, Patrick Debois và John Willis, *The DevOps Handbook*
- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
- World Health Organisation, *ICD-11*, mục về kiệt sức như một hiện tượng nghề nghiệp
