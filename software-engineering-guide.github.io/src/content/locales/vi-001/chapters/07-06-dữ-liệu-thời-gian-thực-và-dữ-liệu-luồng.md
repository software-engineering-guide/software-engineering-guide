# 7.6 Dữ liệu thời gian thực và dữ liệu luồng

## Tổng quan và động lực

Hầu hết những gì bạn biết về đường ống dữ liệu đều giả định dữ liệu đứng yên. Bạn thu thập một ngày bản ghi, chạy một công việc qua đêm, và đọc kết quả vào buổi sáng. Dữ liệu thời gian thực và dữ liệu luồng lật ngược giả định đó. Thay vì xử lý một đống dữ liệu đã hoàn tất, bạn xử lý một dòng sự kiện vô tận khi chúng đến, và bạn tạo ra câu trả lời liên tục. Đây là sự khác biệt giữa [xử lý theo lô](https://en.wikipedia.org/wiki/Batch_processing), hoạt động trên một tập dữ liệu có giới hạn, đầy đủ, và [xử lý luồng](https://en.wikipedia.org/wiki/Stream_processing), hoạt động trên một dòng không giới hạn, không bao giờ kết thúc.

Với các đội lớn, luồng xuất hiện ngay khi độ trễ bắt đầu quan trọng với doanh nghiệp. Một quyết định gian lận đến muộn một giờ là vô giá trị. Một tín hiệu cá nhân hóa đến ngày mai thì chẳng cá nhân hóa được gì. Một bảng điều khiển vận hành chậm hơn thực tế cả một ca làm lệch hướng những người xem nó. Chương 7.2 (kỹ thuật dữ liệu) lập luận rằng bạn nên chọn theo lô theo mặc định và chỉ với tới luồng nơi độ trễ thực sự sinh lời, và chương này đưa bạn đi nốt quãng còn lại: khi nào thời gian thực xứng đáng chi phí, và cách xây nó mà không đốt cháy ngân sách vận hành. Luồng nằm gần các mẫu nhắn tin hướng sự kiện trong chương 3.12 (kiến trúc hướng sự kiện và nhắn tin), các lựa chọn lưu trữ trong chương 3.4 (kiến trúc dữ liệu và lưu trữ), và các thực hành đo từ xa trong chương 9.2 (khả năng quan sát và đo từ xa).

Bối cảnh doanh nghiệp và chính phủ nâng rủi ro lên. Một ngân hàng chấm điểm giao dịch tìm gian lận trong thời gian một máy đọc thẻ chớp mắt. Một cơ quan giao thông theo dõi phương tiện và dự đoán giờ đến cho hàng triệu hành khách. Một cơ quan trợ cấp theo dõi bất thường trong các yêu cầu trong khi giữ một bản ghi kiểm toán được về mọi quyết định. Trong tất cả, giá trị đến từ việc hành động trên dữ liệu khi nó còn tươi, và rủi ro đến từ việc hành động trên dữ liệu sai, không đầy đủ, hoặc không thể dựng lại sau này. Chương này có chính kiến rõ về cả hai.

## Các nguyên tắc chính

- Chỉ với tới luồng khi độ trễ có giá trị kinh doanh rõ ràng; theo lô rẻ hơn và đơn giản hơn.
- Phân biệt dữ liệu có giới hạn (hữu hạn) với dữ liệu không giới hạn (vô tận), và thiết kế tương ứng.
- Coi thời gian sự kiện, không phải thời gian đến, là nguồn sự thật, và lên kế hoạch cho dữ liệu đến muộn và sai thứ tự.
- Cửa sổ và dấu mốc là cách bạn có câu trả lời hữu hạn từ luồng vô hạn.
- Ưu tiên kết quả hiệu quả-một-lần qua đích ghi lũy đẳng hơn các lời hứa đúng-một-lần mong manh.
- Xử lý có trạng thái cần điểm kiểm tra để phục hồi mà không mất hay đếm đôi.
- Thiết kế cho áp lực ngược và xử lý lại từ ngày đầu, không phải chuyện nghĩ sau.
- Giữ logic luồng quan sát được và kiểm toán được; một luồng im lặng còn tệ hơn một lô thất bại.

## Khuyến nghị

### Biện minh thời gian thực trước khi xây nó

Quyết định luồng quan trọng nhất là có truyền luồng hay không. Thời gian thực gần như nhân đôi độ phức tạp và chi phí vận hành của bạn, vì bạn đổi một công việc chạy rồi dừng lấy một hệ thống phải khỏe mạnh từng giây. Trước khi cam kết, hãy nêu quyết định mà dữ liệu tươi cho phép và chi phí khi quyết định đó đến muộn. Chấm điểm gian lận, cảnh báo vận hành và cá nhân hóa trực tiếp thường vượt qua ngưỡng. Một bảng điều khiển mà con người nhìn hai lần một ngày hầu như không bao giờ, dù "thời gian thực" nghe thỏa mãn thế nào trong cuộc họp hoạch định. Hãy viết yêu cầu độ trễ thành con số, bằng giây hay phút, và kiểm tra nó với thực tế. Phần lớn những gì người ta gọi là thời gian thực được phục vụ tốt bởi các lô nhỏ chạy mỗi vài phút với một phần nhỏ chi phí.

### Thiết kế quanh thời gian sự kiện, không phải thời gian xử lý

Ý tưởng khó nhất đơn lẻ của luồng là sự kiện xảy ra ở một thời điểm và được xử lý ở thời điểm khác. Thời gian sự kiện là khi việc đó thực sự xảy ra, ví dụ khi một hành khách chạm thẻ. Thời gian xử lý là khi hệ thống của bạn xử lý nó. Chúng liên tục lệch nhau: một chiếc điện thoại mất sóng trong đường hầm và tải lên ba phút lượt chạm cùng lúc, một trục trặc mạng sắp xếp lại thông điệp, một phân vùng chậm. Nếu bạn tính theo thời gian xử lý, con số của bạn dao động theo hạ tầng thay vì phản ánh thế giới. Vấn đề đến muộn và sai thứ tự này là trái tim của kỷ luật, và nó nối trực tiếp với mô hình hóa sự kiện trong [kiến trúc hướng sự kiện](https://en.wikipedia.org/wiki/Event-driven_architecture). Hãy đóng dấu mỗi sự kiện bằng thời gian sự kiện tại nguồn, mang dấu thời gian đó qua toàn bộ đường ống, và tính kết quả theo nó.

### Dùng cửa sổ và dấu mốc để có câu trả lời hữu hạn

Một luồng không giới hạn không bao giờ kết thúc, nên "đếm các sự kiện" không có câu trả lời cho đến khi bạn giới hạn nó. Cửa sổ làm việc giới hạn đó. Cửa sổ lăn chặt thời gian thành các thùng cố định, không chồng lấn, ví dụ mỗi phút. Cửa sổ trượt chồng lấn, nên một cửa sổ năm phút tiến mỗi phút cho bạn con số di động mượt. Cửa sổ phiên gom các đợt hoạt động ngăn cách bởi khoảng nghỉ không hoạt động, phù hợp với phiên người dùng. Khi đã có cửa sổ, bạn cần quyết định khi nào một cửa sổ xong, vì dữ liệu muộn vẫn có thể đến. Một dấu mốc là ước lượng của hệ thống rằng nó có lẽ đã thấy mọi sự kiện đến một thời gian sự kiện nhất định. Khi dấu mốc vượt qua cuối cửa sổ, bạn phát kết quả. Hãy điều chỉnh bạn chờ bao lâu: giữ cửa sổ mở lâu hơn thì chịu được nhiều độ muộn hơn với cái giá độ trễ và bộ nhớ, đóng nhanh hơn thì rủi ro bỏ rơi các sự kiện đến muộn. Hãy quyết định tường minh điều gì xảy ra với dữ liệu đến sau khi cửa sổ đóng, bạn bỏ nó, ghi nhật ký nó, hay phát một bản hiệu chỉnh.

### Làm đích ghi lũy đẳng và ưu tiên hiệu quả-một-lần

Bảo đảm phân phối nghe đơn giản và không phải vậy. Phân phối ít-nhất-một-lần nghĩa là mọi sự kiện được xử lý, nhưng một số có thể được xử lý nhiều hơn một lần sau khi thử lại, nên số đếm có thể phình. Đúng-một-lần nghe lý tưởng nhưng đắt và, hiểu theo nghĩa đen qua các hệ thống bên ngoài tùy ý, thường bất khả. Mục tiêu thực tế là hiệu quả-một-lần: kết quả quan sát được như thể mỗi sự kiện được xử lý một lần, dù bộ máy bên dưới đã thử lại. Bạn đạt được điều đó bằng cách làm các đích ghi [lũy đẳng](https://en.wikipedia.org/wiki/Idempotence) an toàn để ghi lặp lại, dùng khóa tất định và upsert để một sự kiện phát lại ghi đè thay vì trùng lặp. Kết hợp phân phối ít-nhất-một-lần với ghi lũy đẳng và bạn có kết quả đúng mà không phải trả giá cho điều phối giao dịch nặng nề khắp nơi. Hãy dành bộ máy đúng-một-lần thực sự cho những chỗ hẹp thực sự cần nó.

### Đặt điểm kiểm tra cho xử lý có trạng thái để nó phục hồi được

Nhiều phép tính luồng hữu ích có trạng thái: số đếm chạy, phép nối giữa các luồng, loại trùng, mô hình gian lận nhớ hành vi gần đây. Trạng thái đó sống trong bộ nhớ và sẽ biến mất khi một tiến trình khởi động lại. Điểm kiểm tra định kỳ chụp ảnh nhanh trạng thái và vị trí luồng cùng nhau, để sau một sự cố hệ thống tiếp tục từ một điểm nhất quán thay vì phát lại mọi thứ hay mất trí nhớ. Hãy định cỡ trạng thái của bạn có chủ đích, vì trạng thái không giới hạn là cách phổ biến làm cạn bộ nhớ của một công việc luồng trong môi trường sản xuất. Dùng hết hạn và thời gian sống trên trạng thái bạn không còn cần, và giám sát kích thước trạng thái như một chỉ số hạng nhất. Thời gian phục hồi sau thất bại là mối quan tâm mức dịch vụ thực, nên hãy kiểm thử nó trước khi người dùng làm.

### Truyền luồng từ cơ sở dữ liệu vận hành bằng thu thập thay đổi dữ liệu

Bạn thường muốn phản ứng với thay đổi trong một cơ sở dữ liệu chưa bao giờ được thiết kế để phát sự kiện. [Thu thập thay đổi dữ liệu](https://en.wikipedia.org/wiki/Change_data_capture) (CDC) giải quyết điều này bằng cách đọc nhật ký giao dịch của cơ sở dữ liệu và biến mỗi lệnh chèn, cập nhật và xóa thành một luồng sự kiện thay đổi. Điều này tốt hơn nhiều so với thăm dò bảng theo bộ hẹn giờ, vốn chậm, bỏ sót trạng thái trung gian và đập vào nguồn. CDC cho phép bạn giữ một chỉ mục tìm kiếm, bộ nhớ đệm, kho phân tích hay dịch vụ hạ nguồn liên tục đồng bộ với hệ thống ghi nhận, và làm vậy mà không cần thay đổi xâm lấn ứng dụng. Hãy coi luồng thay đổi là sản phẩm dữ liệu hạng nhất: đánh phiên bản lược đồ, lập tài liệu ý nghĩa, và theo dõi độ trễ của nó, vì mọi thứ hạ nguồn thừa hưởng độ trễ đó.

### Ưu tiên kiến trúc luồng-trước hơn duy trì hai cơ sở mã

[Kiến trúc Lambda](https://en.wikipedia.org/wiki/Lambda_architecture) kinh điển chạy một tầng lô cho lịch sử chính xác, đầy đủ cùng một tầng tốc độ cho kết quả tươi, xấp xỉ, rồi gộp chúng. Nó hoạt động, nhưng buộc bạn viết và bảo trì cùng một logic kinh doanh hai lần, trong hai hệ thống, và đối chiếu sự khác biệt mãi mãi. Kiến trúc Kappa thu gọn điều này: giữ một nhật ký sự kiện bền, phát lại được và chạy mọi xử lý như xử lý luồng, xử lý lại lịch sử bằng cách phát lại nhật ký khi logic thay đổi. Ngành đã trôi về hình dạng luồng-trước này vì một cơ sở mã duy nhất rẻ hơn nhiều để bảo trì và suy luận. Nếu bạn diễn đạt được nhu cầu lô của mình như các lần phát lại trên một nhật ký sự kiện được giữ lại, bạn tránh hoàn toàn thuế hai cơ sở mã. Hãy dùng các bộ môi giới dựa trên nhật ký giữ lại lịch sử để xử lý lại là chuyện tua lại, không phải xây lại.

### Phơi luồng dưới dạng SQL, khung nhìn cụ thể hóa và OLAP thời gian thực

Không phải ai cần luồng cũng nên phải viết mã xử lý luồng cấp thấp. SQL luồng cho phép nhà phân tích và kỹ sư diễn đạt cửa sổ, phép nối và tổng hợp bằng ngôn ngữ họ đã biết, và giữ kết quả liên tục cập nhật như các khung nhìn cụ thể hóa. Với truy vấn phân tích độ trễ thấp trên dữ liệu tươi, một kho [xử lý phân tích trực tuyến](https://en.wikipedia.org/wiki/Online_analytical_processing) (OLAP) thời gian thực thu nạp luồng và trả lời truy vấn cắt lát trong mili giây, là thứ chạy một bảng điều khiển vận hành thực sự trực tiếp. Hãy ghép những thứ này với các thực hành phân tích sản phẩm trong chương 7.4 (phân tích sản phẩm và thử nghiệm) khi mục tiêu là phản hồi nhanh về tính năng và thử nghiệm. Hãy chọn các công cụ cấp cao hơn này nơi chúng phù hợp, và dành bộ xử lý luồng viết tay cho logic chúng không diễn đạt được.

### Lên kế hoạch cho áp lực ngược và xử lý lại từ đầu

Một luồng có thể đến nhanh hơn bạn xử lý được. Áp lực ngược là cơ chế cho phép một người tiêu dùng chậm báo ngược thượng nguồn giảm tốc thay vì sụp đổ hay lặng lẽ bỏ dữ liệu. Hãy bảo đảm mọi giai đoạn trong đường ống của bạn tôn trọng nó, và giám sát độ trễ người tiêu dùng như chỉ số tiêu đề, vì độ trễ tăng là cảnh báo sớm nhất rằng bạn đang thua cuộc đua. Xử lý lại là khả năng khác mà người ta ước họ đã xây vào. Khi bạn tìm thấy lỗi hoặc đổi một quy tắc, bạn muốn phát lại lịch sử qua logic đã sửa. Điều đó chỉ khả thi nếu nhật ký sự kiện của bạn giữ đủ lịch sử và đích ghi của bạn đủ lũy đẳng để hấp thụ việc phát lại. Hãy thiết kế cả hai vào từ ngày đầu; vá chúng dưới áp lực sự cố thật khốn khổ.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
| --- | --- | --- | --- |
| Theo lô | Đơn giản, rẻ, dễ kiểm thử và chạy bù | Độ trễ cao, cũ giữa các lần chạy | Báo cáo, hầu hết phân tích |
| Lô nhỏ (phút) | Gần thời gian thực, đơn giản hơn nhiều so với luồng | Không thực sự tức thì | Bảng điều khiển "thời gian thực" |
| Luồng thực sự (dưới một giây) | Phản ứng tức thì, kết quả liên tục | Phức tạp, tốn kém, khó kiểm thử | Gian lận, cảnh báo, cá nhân hóa trực tiếp |
| Ít-nhất-một-lần + đích ghi lũy đẳng | Kết quả đúng, chi trả nổi, bền | Đòi thiết kế khóa kỷ luật | Hầu hết đường ống luồng |
| Bộ máy đúng-một-lần | Bảo đảm mạnh đầu-đến-cuối | Đắt, hạn chế qua các hệ thống | Đường rủi ro cao hẹp |
| Lambda (lô + tốc độ) | Lịch sử chính xác cộng cái nhìn tươi | Hai cơ sở mã phải bảo trì | Di chuyển hệ thống cũ |
| Kappa (luồng-trước) | Một cơ sở mã, phát lại được | Cần nhật ký bền, được giữ lại | Nền tảng luồng mới |

Căng thẳng trung tâm là độ trễ so với độ phức tạp. Mỗi bước hướng đến thời gian thực tốn bạn về gánh nặng vận hành, khó khăn kiểm thử và tiền, và lợi tức không tuyến tính: đi từ hằng ngày đến vài phút một lần thì rẻ và thường là đủ, trong khi đi từ phút đến dưới một giây là nơi chi phí tập trung. Hãy giải quyết căng thẳng bằng cách định giá quyết định, không phải công nghệ. Hỏi hành động nào mà độ tươi cho phép và độ muộn tốn gì, rồi chỉ mua giảm độ trễ vừa bằng mức hành động đó biện minh. Khi bạn thực sự cần luồng, hãy dựa vào phân phối ít-nhất-một-lần với đích ghi lũy đẳng và một nhật ký luồng-trước, vì tổ hợp đó cho bạn tính đúng và khả năng phát lại mà không có các bảo đảm nặng nhất.

## Câu hỏi để thảo luận với đội của bạn

1. **Dữ liệu thời gian thực thực sự cho phép chúng ta quyết định gì, và nó tốn gì khi dữ liệu đó đến muộn một phút thay vì tức thì?** Đây là câu hỏi nên chặn cổng mọi dự án luồng, vì luồng gần như nhân đôi chi phí và độ phức tạp vận hành so với theo lô. Một đội lớn có thể đốt nhiều quý để xây một nền tảng thời gian thực phục vụ bảng điều khiển mà con người kiểm tra hai lần một ngày, là tiền bị đốt. Hãy mang hành động cụ thể mà dữ liệu thúc đẩy, dù là chặn một giao dịch gian lận, gọi một nhân viên vận hành, hay thay đổi điều người dùng thấy, và đặt một con số cho chi phí độ trễ của mỗi cái. Nếu câu trả lời trung thực là một lô nhỏ năm phút sẽ phục vụ nhu cầu, đó là phát hiện đáng ăn mừng, không phải giấu. Câu trả lời nên thay đổi trực tiếp việc bạn xây luồng thực sự, chấp nhận lô nhỏ, hay ở lại theo lô.

2. **Chúng ta xử lý sự kiện đến muộn và sai thứ tự thế nào, và điều gì xảy ra với dữ liệu đến sau khi cửa sổ đóng?** Dữ liệu đến muộn và sai thứ tự là phần khó của luồng, và các đội bỏ qua câu hỏi này phát hiện ra nó trong môi trường sản xuất khi con số của họ không chịu đối chiếu. Áp lực đối lập là độ trễ và tính đúng: giữ cửa sổ mở lâu hơn để bắt các sự kiện đến muộn thì làm chậm mọi kết quả và tốn thêm bộ nhớ, đóng nhanh hơn thì lặng lẽ bỏ dữ liệu thật. Hãy mang bằng chứng về dữ liệu của bạn thực sự đến muộn thế nào, đo bằng khoảng cách giữa thời gian sự kiện và thời gian xử lý qua các nguồn, vì một nguồn di động trong đường hầm hành xử rất khác một sự kiện phía máy chủ. Hãy quyết định tường minh liệu dữ liệu muộn bị bỏ, ghi nhật ký, hay kích hoạt một bản hiệu chỉnh, và bảo đảm mọi người hạ nguồn biết là cái nào. Trong bối cảnh chính phủ nơi các con số phải bảo vệ được, lặng lẽ bỏ sự kiện muộn có thể là vấn đề tuân thủ, nên chính sách cần có chủ đích và được lập tài liệu.

3. **Đích ghi của chúng ta có đủ lũy đẳng để phát lại lịch sử an toàn không, và nhật ký sự kiện của chúng ta có giữ đủ để việc phát lại khả thi không?** Xử lý lại là khả năng các đội thường ước mình đã xây vào nhất và thường không xây, và nó phụ thuộc vào hai thứ hoạt động cùng nhau: đích ghi lũy đẳng hấp thụ sự kiện phát lại mà không trùng lặp, và một nhật ký bền giữ đủ lịch sử để phát lại. Không có cả hai, sửa một lỗi logic nghĩa là bạn không tính lại sạch sẽ kỳ bị ảnh hưởng, và bạn mắc kẹt vá con số bằng tay dưới áp lực. Hãy mang cửa sổ lưu giữ hiện tại và một bài kiểm tra cụ thể: chọn một lỗi thật quý trước và hỏi liệu bạn có thể đã phát lại logic đã sửa trên dữ liệu bị ảnh hưởng. Lực kéo ngược là chi phí, vì giữ lịch sử và thiết kế ghi lũy đẳng tốn lưu trữ và kỷ luật ban đầu. Nhưng lựa chọn thay thế nổi lên vào lúc tệ nhất có thể, giữa một sự cố, nên câu trả lời định hình bạn đầu tư bao nhiêu vào khả năng phát lại trước khi cần.

4. **Khi một công việc luồng sập, nó phải phục hồi nhanh đến đâu, được phép giữ bao nhiêu trạng thái, và chúng ta đã thực sự đo thời gian một lần phục hồi dưới tải sản xuất chưa?** Một công việc lô chết có thể chạy lại vào ngày mai, nhưng một luồng luôn bật chết là một sự cố đang diễn ra, và các công việc có trạng thái giữ số đếm chạy, phép nối hay mô hình gian lận có thể mất vài phút bộ nhớ hoặc mất lâu để nạp lại trạng thái sau khởi động lại. Với một đội lớn, đây là nơi một chi tiết không hào nhoáng lặng lẽ đặt ra tính sẵn sàng thực của bạn: trạng thái không giới hạn lớn lên cho đến khi một công việc cạn bộ nhớ, và một lần khôi phục điểm kiểm tra chậm biến một trục trặc mười giây thành mười phút. Áp lực đối lập là độ tươi so với an toàn, vì điểm kiểm tra thường xuyên hơn rút ngắn phục hồi nhưng thêm chi phí chung, và lưu giữ trạng thái rộng rãi cải thiện độ chính xác nhưng rủi ro cạn bộ nhớ. Hãy mang một mục tiêu thời gian phục hồi cụ thể, kích thước trạng thái hiện tại và đường cong tăng của nó, khoảng điểm kiểm tra, và kết quả của một buổi diễn tập chuyển đổi dự phòng thật thay vì ước lượng đầy hy vọng. Trong bối cảnh doanh nghiệp và chính phủ nơi luồng hậu thuẫn chấm điểm gian lận hay nguồn cấp an toàn công cộng, một đường phục hồi chưa kiểm thử là rủi ro vận hành bạn đã chấp nhận mà chưa đo, nên hãy coi buổi diễn tập là yêu cầu, không phải điều tốt nếu có.

5. **Chúng ta chạy một cơ sở mã luồng-trước hay một tầng lô và tầng tốc độ riêng, và việc giữ hai bên đối chiếu thực sự tốn bao nhiêu?** Mẫu Lambda gồm tầng lô cho lịch sử chính xác cộng tầng tốc độ cho kết quả tươi buộc bạn viết cùng logic kinh doanh hai lần, trong hai hệ thống, và đối chiếu câu trả lời của chúng mãi mãi, trong khi hình dạng luồng-trước (Kappa) giữ một nhật ký bền, phát lại được và chạy mọi xử lý như xử lý luồng. Với một tổ chức lớn, logic trùng lặp là nơi trôi dạt và con số tranh cãi sinh sôi, vì một quy tắc đổi ở một tầng và không ở tầng kia, và kỹ sư dành thời gian thật để giải thích vì sao hai bên bất đồng. Lực kéo về giữ cả hai là quán tính và sự thoải mái của một tầng lô đã kiểm chứng, nên hãy cân nhắc điều đó với thuế bảo trì một cách trung thực. Hãy mang danh sách các phép tính bạn hiện chạy ở cả hai nơi, các sự cố do hai tầng bất đồng gây ra, và đánh giá liệu nhật ký sự kiện của bạn có giữ đủ lịch sử để diễn đạt nhu cầu lô như các lần phát lại. Trong bối cảnh chính phủ và doanh nghiệp được kiểm toán, hai tầng có thể báo cáo con số khác nhau cho cùng một kỳ tự nó là khoản nợ tuân thủ, vì bạn phải nói được con số nào có thẩm quyền và vì sao.

6. **Ai vận hành hệ thống luôn bật này khi nó hỏng lúc ba giờ sáng, và chúng ta đã lập ngân sách cho tải trực và kỹ năng chuyên môn nó đòi hỏi, hay đang giả định nhân sự kiểu lô?** Luồng chuyển chi phí từ xây sang chạy: hệ thống phải khỏe mạnh từng giây, nghĩa là phủ trực thật, các kỹ sư thông thạo thời gian sự kiện, dấu mốc, trạng thái và ngữ nghĩa phân phối, và kiểm thử khó hơn một công việc chạy rồi dừng. Các đội thường xuyên phê duyệt một nền tảng luồng dựa trên năng lực của nó và không bao giờ tài trợ những người giữ nó sống, nên nền tảng suy giảm và lòng tin xói mòn. Đánh đổi là phạm vi so với tính bền vững: mỗi đường ống thời gian thực thêm là một thứ nữa có thể gọi ai đó, nên câu hỏi là liệu độ trễ nó mua có biện minh cho một cam kết vận hành vĩnh viễn. Hãy mang một bản kiểm kê trung thực về ai sở hữu từng luồng trong môi trường sản xuất, vòng trực hiện tại của bạn và dư địa của nó, và chuyên môn thời gian sự kiện thực sự nằm ở đâu, dù là một lần tuyển dụng, một đối tác, hay một dịch vụ được quản lý. Với một cơ quan công hay doanh nghiệp lớn, hãy thêm thời gian chờ mua sắm và tuyển dụng cùng bất kỳ lựa chọn dịch vụ được quản lý nào, vì một nền tảng thời gian thực phụ thuộc nhân tài khan hiếm bạn không tuyển hay giữ được là kế hoạch vận hành một hệ thống dễ ngừng hoạt động thiếu người.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Luồng hiếm khi là nước đi đầu tiên của bạn, và dựng một nền tảng nặng có thể nhấn chìm một đội nhỏ xíu. Hãy chọn tín hiệu duy nhất chạm đến giá trị cốt lõi của bạn, đặt sự kiện lên một bộ môi giới dựa trên nhật ký được giữ lại duy nhất, và chạy một bộ xử lý nhẹ với đích ghi có khóa, lũy đẳng để một lần thử lại ít-nhất-một-lần không bao giờ đếm đôi. Giữ vài ngày lịch sử để bạn phát lại qua logic đã sửa, và ưu tiên một dịch vụ luồng được quản lý hơn là vận hành cụm của riêng bạn, vì nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia luồng và không muốn chạy hạ tầng luôn bật, vì vậy hãy coi thời gian thực là thứ bạn mua bên trong các công cụ đã dùng thay vì hệ thống bạn bố trí nhân sự. Hãy đóng khung nhu cầu như câu hỏi độ trễ có con số đi kèm, và trong hầu hết trường hợp một lô nhỏ làm mới mỗi vài phút sẽ đáp ứng nó với một phần nhỏ chi phí và rủi ro. Chọn nhà cung cấp có tính năng thời gian thực minh bạch về độ trễ và dễ quay lui, và dành luồng đặt riêng cho trường hợp hiếm nơi dữ liệu tươi trực tiếp thúc đẩy doanh thu hay an toàn.

**Doanh nghiệp lớn.** Vấn đề là nhất quán và chi phí qua nhiều đội: một nền tảng dựa trên nhật ký dùng chung, một chính sách thời gian sự kiện và dữ liệu muộn chuẩn, và đích ghi lũy đẳng để các nhóm thôi phát minh lại những đường ống mong manh. Hãy lập ngân sách tường minh cho vận hành luôn bật và gánh nặng trực, chuẩn hóa trên một nhật ký luồng-trước để bạn tránh một cơ sở mã lô trùng lặp, và quản lý luồng như sản phẩm dữ liệu được quản trị với chủ sở hữu, phiên bản lược đồ và độ trễ được giám sát thay vì một mớ công việc đặt riêng. Theo dõi độ trễ, thời gian phục hồi và chi phí mỗi luồng như chỉ số danh mục.

**Chính phủ.** Khả năng kiểm toán và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy giữ mọi sự kiện đã xử lý trong một nhật ký bền để các con số báo cáo cho cơ quan giám sát, lượng hành khách, bất thường trợ cấp, quyết định gian lận, có thể được dựng lại chính xác, và làm chính sách dữ liệu muộn tường minh và có tài liệu thay vì lặng lẽ bỏ sự kiện. Mua sắm nên đòi khả năng di chuyển dữ liệu và công bố bảo đảm phân phối và lưu giữ của một dịch vụ được quản lý, và mọi điều chỉnh lại sau một thay đổi quy tắc nên là một lần phát lại bảo vệ được qua logic đã sửa, không phải một bản vá thủ công không ai truy vết được.

## Ví dụ

**Công ty khởi nghiệp.** Một ứng dụng tiêu dùng muốn cho người dùng thấy nguồn cấp hoạt động trực tiếp và gắn cờ các đăng nhập đáng ngờ khi chúng xảy ra. Đội chống lại việc dựng một nền tảng luồng nặng. Họ đặt sự kiện lên một bộ môi giới dựa trên nhật ký được giữ lại duy nhất, chạy một bộ xử lý luồng nhẹ cho logic rủi ro đăng nhập, và nuôi một kho OLAP thời gian thực chạy nguồn cấp hoạt động. Mọi đích ghi đều có khóa và lũy đẳng, nên một lần thử lại ít-nhất-một-lần không bao giờ đếm đôi. Khi sau đó tìm thấy lỗi trong quy tắc rủi ro, họ đơn giản phát lại nhật ký qua logic đã sửa qua đêm, vì họ giữ một tuần lịch sử và không bao giờ cần cơ sở mã lô thứ hai.

**Doanh nghiệp lớn.** Một ngân hàng bán lẻ chấm điểm mọi giao dịch thẻ tìm gian lận trong cửa sổ ủy quyền, nối luồng giao dịch trực tiếp với một mô hình có trạng thái về hành vi tài khoản gần đây. Điểm kiểm tra cho phép dịch vụ chấm điểm phục hồi sau sự cố nút trong vài giây mà không mất trí nhớ về vài phút cuối. Riêng biệt, thu thập thay đổi dữ liệu truyền các cập nhật từ cơ sở dữ liệu ngân hàng lõi vào một chỉ mục tìm kiếm và một dịch vụ cá nhân hóa, giữ cả hai tươi mà không cần thăm dò. Bảng điều khiển vận hành đọc từ một kho OLAP thời gian thực để các đội rủi ro và vận hành theo dõi doanh nghiệp khi nó chuyển động, và toàn bộ đường ống phát ra đo từ xa về độ trễ và thông lượng mô tả trong chương 9.2.

**Chính phủ.** Một cơ quan giao thông đô thị thu nạp vị trí phương tiện và lượt chạm thẻ vé để dự đoán giờ đến và giám sát mật độ thời gian thực, nuôi cả ứng dụng công cộng và một trung tâm vận hành. Vì hành khách trong đường hầm tải lên lượt chạm thành các đợt bị trễ, đội tính lượng hành khách theo thời gian sự kiện với dấu mốc điều chỉnh theo độ muộn quan sát được, và ghi nhật ký mọi sự kiện đến sau khi cửa sổ đóng thay vì lặng lẽ bỏ. Mọi sự kiện đã xử lý được giữ trong một nhật ký kiểm toán được để số liệu lượng hành khách báo cáo cho cơ quan giám sát có thể dựng lại chính xác. Khi một quy tắc giá vé đổi, họ phát lại kỳ bị ảnh hưởng qua logic đã sửa và tạo một bản điều chỉnh lại bảo vệ được.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của dữ liệu thời gian thực đến từ việc hành động khi hành động còn quan trọng. Gian lận bị bắt trong lúc ủy quyền ngăn một khoản lỗ mà một lô qua đêm chỉ báo cáo lại. Cá nhân hóa phản hồi trong một phiên nâng chuyển đổi theo cách mà đề xuất của ngày mai không làm được. Giám sát vận hành phản ánh hiện tại cho phép bạn can thiệp trước khi một vấn đề nhỏ thành ngừng hoạt động hay sự cố công khai. Trong mỗi trường hợp, giá trị là chênh lệch giữa hành động bây giờ và hành động sau, và đó là điều bạn nên định lượng khi lập luận.

Tổng chi phí sở hữu cao hơn theo lô, và trung thực về điều đó bảo vệ uy tín của bạn. Bạn trả cho hạ tầng luôn bật, cho kỹ sư hiểu thời gian sự kiện, dấu mốc, trạng thái và ngữ nghĩa phân phối, và cho gánh nặng kiểm thử cùng trực khó hơn của một hệ thống phải khỏe mạnh liên tục thay vì chạy rồi dừng. Kiến trúc luồng-trước trên nhật ký được giữ lại giảm chi phí liên tục bằng cách tha cho bạn một cơ sở mã lô trùng lặp, và chọn ít-nhất-một-lần với đích ghi lũy đẳng tránh chi phí của bộ máy đúng-một-lần đầu-đến-cuối. Sai lầm đắt nhất là xây thời gian thực nơi lô nhỏ hay lô là đủ, nên lập luận chi phí mạnh nhất thường là quyết định không truyền luồng. Hãy đóng khung lời chào với ban lãnh đạo quanh các quyết định nhạy với độ trễ cụ thể và lợi ích đo được của chúng, và rõ ràng như nhau về nơi ở lại theo lô tiết kiệm tiền mà không mất giá trị.

## Phản mẫu và cạm bẫy

- Xây luồng vì uy tín khi một lô nhỏ mỗi vài phút đã đáp ứng nhu cầu.
- Tính theo thời gian xử lý, nên con số dao động theo hạ tầng thay vì thế giới.
- Phớt lờ dữ liệu đến muộn và sai thứ tự cho đến khi đối chiếu thất bại trong môi trường sản xuất.
- Đuổi theo đúng-một-lần theo nghĩa đen ở mọi nơi thay vì ít-nhất-một-lần với đích ghi lũy đẳng.
- Trạng thái không giới hạn không hết hạn, lặng lẽ lớn lên cho đến khi một công việc cạn bộ nhớ.
- Không có điểm kiểm tra, nên khởi động lại mất trạng thái hoặc buộc phát lại toàn bộ.
- Thăm dò cơ sở dữ liệu vận hành theo bộ hẹn giờ thay vì dùng thu thập thay đổi dữ liệu.
- Duy trì tầng lô Lambda và tầng tốc độ với logic trùng lặp, trôi dạt.
- Cửa sổ lưu giữ quá ngắn để phát lại lịch sử khi bạn tìm thấy lỗi.
- Luồng không có chỉ số độ trễ, thông lượng hay độ mới, thất bại thầm lặng.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Mọi thứ là theo lô, hoặc vài công việc luồng làm tay chạy phản ứng không giám sát. Con số được tính theo thời gian xử lý, dữ liệu muộn bị phớt lờ, và khởi động lại mất trạng thái. Không ai phát lại được lịch sử để sửa lỗi, và vấn đề được phát hiện khi các con số hạ nguồn không chịu đối chiếu.
- **Mức 2, Phát triển:** Một số đội chạy đường ống luồng cốt lõi trên bộ môi giới dựa trên nhật ký với điểm kiểm tra, và họ phân biệt thời gian sự kiện với thời gian xử lý và dùng cửa sổ cơ bản. Thực hành không nhất quán giữa các đội: phân phối là ít-nhất-một-lần nhưng không phải đích ghi nào cũng lũy đẳng, xử lý dữ liệu muộn là ứng biến, và độ trễ được theo dõi không chính thức thay vì cảnh báo.
- **Mức 3, Chuẩn hóa:** Thời gian sự kiện, dấu mốc và chính sách dữ liệu muộn tường minh được lập tài liệu và áp dụng toàn tổ chức. Đích ghi lũy đẳng cho kết quả hiệu quả-một-lần, trạng thái có hết hạn, và thu thập thay đổi dữ liệu nuôi các hệ thống hạ nguồn theo quy ước. Một nhật ký được giữ lại hỗ trợ phát lại, và độ trễ, thông lượng và độ mới được giám sát với cảnh báo như tiêu chuẩn toàn tổ chức thay vì thói quen của từng đội.
- **Mức 4, Quản lý:** Hệ sinh thái luồng được đo và kiểm soát theo đường cơ sở. Mỗi đường ống mang mục tiêu mức dịch vụ về độ trễ đầu-đến-cuối, độ trễ người tiêu dùng, thời gian phục hồi, độ lệch thời gian sự kiện, tỷ lệ sự kiện muộn, kích thước trạng thái và chi phí mỗi triệu sự kiện, tất cả được theo dõi theo mục tiêu thống nhất và cảnh báo khi hồi quy. Phục hồi được diễn tập và đo thời gian thay vì giả định, dư địa áp lực ngược và tăng trưởng trạng thái được theo dõi như tín hiệu năng lực, và một luồng mới phải vượt các chỉ số này trước khi lên môi trường sản xuất.
- **Mức 5, Điều phối:** Một kiến trúc luồng-trước phục vụ cả nhu cầu tươi lẫn lịch sử từ một nhật ký phát lại được, và SQL luồng, khung nhìn cụ thể hóa và OLAP thời gian thực làm dữ liệu tươi được tiếp cận rộng. Xử lý lại là thường lệ và được kiểm thử, nền tảng tự co giãn và cân bằng lại theo tải và chi phí đo được, và luồng được cho nghỉ hưu, thu hẹp phạm vi hay thay thế dựa trên bằng chứng. Luồng được tích hợp với hoạch định kinh doanh và rủi ro, và mọi luồng quan sát được và kiểm toán được đầu-đến-cuối khi bức tranh tải và chi phí dịch chuyển.

## Ý tưởng để thảo luận

1. "Thời gian thực" thực sự xứng đáng chi phí ở đâu trong ngăn xếp của bạn, và ở đâu nó là một mong ước chưa được xem xét?
2. Khoảng cách giữa thời gian sự kiện và thời gian xử lý qua các nguồn của bạn lớn đến đâu, và bạn có đo nó không?
3. Bạn có thể thu gọn một thiết lập Lambda lô-và-tốc-độ thành một cơ sở mã luồng-trước duy nhất không, và điều gì sẽ cản trở?
4. Đích ghi nào của bạn thực sự lũy đẳng, và bạn có thể phát lại an toàn dữ liệu quý trước qua logic đã sửa hôm nay không?
5. Chính sách của bạn cho dữ liệu đến sau khi cửa sổ đóng là gì, và mọi người hạ nguồn có biết không?
6. Thu thập thay đổi dữ liệu sẽ đổi cách bạn giữ tìm kiếm, bộ nhớ đệm và phân tích đồng bộ thế nào?

## Những điểm cần ghi nhớ

- Chỉ với tới luồng khi một quyết định nhạy với độ trễ trả giá cho nó; theo lô và lô nhỏ là mặc định rẻ hơn.
- Tính theo thời gian sự kiện, và coi dữ liệu đến muộn và sai thứ tự là vấn đề cốt lõi, xử lý bằng cửa sổ và dấu mốc.
- Ưu tiên phân phối ít-nhất-một-lần với đích ghi lũy đẳng cho kết quả hiệu quả-một-lần hơn đúng-một-lần theo nghĩa đen ở mọi nơi.
- Đặt điểm kiểm tra cho xử lý có trạng thái, giới hạn trạng thái của bạn, và giám sát độ trễ người tiêu dùng như chỉ số tiêu đề.
- Dùng thu thập thay đổi dữ liệu để truyền luồng từ cơ sở dữ liệu vận hành thay vì thăm dò.
- Ưu tiên kiến trúc luồng-trước trên nhật ký được giữ lại, phát lại được hơn duy trì hai cơ sở mã.
- Phơi luồng qua SQL luồng, khung nhìn cụ thể hóa và OLAP thời gian thực, và giữ mọi luồng quan sát được và kiểm toán được.

## Tài liệu tham khảo và đọc thêm

- Tyler Akidau, Slava Chernyak và Reuven Lax, "Streaming Systems."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Nathan Marz và James Warren, "Big Data" (kiến trúc Lambda).
- Jay Kreps, "Questioning the Lambda Architecture" (O'Reilly Radar).
- Fabian Hueske và Vasiliki Kalavri, "Stream Processing with Apache Flink."
- Ben Stopford, "Designing Event-Driven Systems."
- Tyler Akidau và các đồng nghiệp, "The Dataflow Model" (bài báo VLDB về cửa sổ và dấu mốc).
