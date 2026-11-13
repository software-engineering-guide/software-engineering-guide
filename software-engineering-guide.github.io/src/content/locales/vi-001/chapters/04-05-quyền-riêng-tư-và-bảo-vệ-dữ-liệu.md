# 4.5 Quyền riêng tư và bảo vệ dữ liệu

## Tổng quan và động lực

Bảo mật bảo vệ dữ liệu khỏi truy cập trái phép. Quyền riêng tư đặt một câu hỏi khác: bạn có nên thu thập, sử dụng và giữ dữ liệu đó không, và những người mà nó mô tả có được nói gì không? Hai thứ chồng lấn, nhưng không giống nhau. Bạn có thể hoàn toàn an toàn mà vẫn vi phạm quyền riêng tư. Bạn làm vậy bằng cách tích trữ dữ liệu mà bạn không có quyền gì giữ, dùng nó cho những mục đích mà người ta chưa từng đồng ý, hoặc chuyển nó qua biên giới theo cách luật pháp cấm. Với các đội lớn, quyền riêng tư là một ràng buộc thiết kế. Nó chạm vào mọi dịch vụ xử lý thông tin cá nhân, mà ngày nay nghĩa là gần như tất cả.

Rủi ro cao và đang tăng. Quy định về quyền riêng tư đã lan khắp thế giới. Nó mang các khoản phạt tăng theo doanh thu, và nó trao cho cá nhân các quyền có thể thực thi đối với dữ liệu của họ. Với doanh nghiệp, xử lý sai dữ liệu cá nhân mời gọi hành động quy định, kiện tập thể, và mất niềm tin khách hàng tốn kém để xây lại. Với chính phủ, nghĩa vụ còn nặng hơn. Công dân không thể chọn nhà cung cấp khác cho dữ liệu thuế, y tế hay trợ cấp của họ, nên nhà nước nợ họ một nghĩa vụ chăm sóc đặc biệt. Và thất bại về quyền riêng tư ăn mòn niềm tin công chúng mà chính phủ dựa vào.

Chương này coi quyền riêng tư là một kỷ luật kỹ thuật. Chúng tôi bao quát thiết kế cho quyền riêng tư từ đầu, tối thiểu hóa và lưu giữ dữ liệu có trách nhiệm, phân loại và bảo vệ các loại nhạy cảm như [PII](https://en.wikipedia.org/wiki/Personally_identifiable_information) và [PHI](https://en.wikipedia.org/wiki/Protected_health_information), xử lý sự đồng ý và cơ sở pháp lý, và quản lý các yêu cầu về chuyển giao xuyên biên giới và nơi lưu trữ ngày càng định hình kiến trúc.

*Xem thêm:* chương 4.6 (tuân thủ và quản trị), chương 7.1 (chiến lược và quản trị dữ liệu), và chương 4.1 (nền tảng và văn hóa bảo mật).

## Các nguyên tắc chính

- **[Quyền riêng tư theo thiết kế](https://en.wikipedia.org/wiki/Privacy_by_design) và theo mặc định.** Xây quyền riêng tư vào từ đầu, và biến thiết lập bảo vệ quyền riêng tư nhất thành mặc định.
- **[Tối thiểu hóa dữ liệu](https://en.wikipedia.org/wiki/Data_minimization).** Chỉ thu thập những gì bạn thực sự cần, giữ nó chỉ chừng nào bạn cần, và chia sẻ nó chỉ khi cần thiết.
- **Giới hạn mục đích.** Chỉ dùng dữ liệu cho những mục đích cụ thể đã công bố khi nó được thu thập.
- **Cơ sở pháp lý.** Có một biện minh pháp lý hợp lệ cho mọi hoạt động xử lý.
- **Quyền của cá nhân.** Tôn trọng quyền của mọi người được truy cập, chỉnh sửa, xóa và chuyển dữ liệu của họ.
- **Minh bạch.** Nói rõ cho mọi người biết bạn thu thập gì, vì sao, và chia sẻ với ai.
- **Trách nhiệm giải trình.** Có thể chứng minh sự tuân thủ, không chỉ tuyên bố nó.

## Khuyến nghị

### Thiết kế cho quyền riêng tư từ đầu

Quyền riêng tư gắn thêm vào một hệ thống đã hoàn chỉnh thì đắt và không đầy đủ. Hãy nướng nó vào từ đầu.

- Thực hiện **[Đánh giá Tác động Bảo vệ Dữ liệu](https://en.wikipedia.org/wiki/Data_protection_impact_assessment) (DPIA)** cho các hệ thống và tính năng mới xử lý dữ liệu cá nhân ở quy mô lớn hoặc mang rủi ro cao hơn, xác định và giảm thiểu rủi ro quyền riêng tư trước khi xây.
- Làm cho các mặc định bảo vệ quyền riêng tư: chọn tham gia thay vì chọn không tham gia cho xử lý không thiết yếu, trường dữ liệu tối thiểu, và lưu giữ ngắn nhất hợp lý.
- Đưa chuyên môn quyền riêng tư vào sớm trong thiết kế, cùng với mô hình hóa mối đe dọa bảo mật, để cả hai được cân nhắc ở giai đoạn ranh giới tin cậy.
- Duy trì một **bản đồ hay bản kiểm kê dữ liệu**: bạn giữ dữ liệu cá nhân nào, nó sống ở đâu, vì sao, và nó chảy đi đâu. Bạn không thể bảo vệ hay giải trình dữ liệu mà bạn không thấy.

### Tối thiểu hóa, lưu giữ và xóa có trách nhiệm

Mỗi mẩu dữ liệu cá nhân bạn giữ là một khoản nợ cũng như một tài sản.

- **Tối thiểu hóa thu thập:** chất vấn mọi trường. Nếu bạn không cần nó cho một mục đích đã nêu, đừng thu thập.
- **Đặt lịch lưu giữ** theo loại dữ liệu và mục đích, và thực thi chúng bằng xóa tự động. Dữ liệu giữ "phòng khi" là dữ liệu đang chờ bị xâm phạm hoặc bị trát đòi.
- **Hỗ trợ quyền được xóa:** xây năng lực tìm và xóa dữ liệu của một cá nhân qua mọi hệ thống, bao gồm bản sao lưu và bản sao hạ nguồn, trong thời hạn pháp lý. Điều này dễ hơn nhiều khi được thiết kế vào hơn là gắn thêm.
- **[Ẩn danh](https://en.wikipedia.org/wiki/Data_anonymization) hoặc tổng hợp** dữ liệu cho phân tích và kiểm thử để dữ liệu có thể nhận dạng không lan vào các môi trường thứ cấp.

### Phân loại và bảo vệ dữ liệu nhạy cảm

Không phải dữ liệu cá nhân nào cũng mang cùng rủi ro, và một số loại mang sức nặng pháp lý đặc biệt.

- Phân loại dữ liệu thành các bậc, phân biệt **PII** (thông tin nhận dạng cá nhân), **PHI** (thông tin y tế được bảo vệ), dữ liệu tài chính, và các loại đặc biệt (như chủng tộc, tôn giáo, sức khỏe, sinh trắc học, hay xu hướng tính dục) mang bảo vệ pháp lý cao hơn.
- Áp dụng bảo vệ tương xứng với độ nhạy cảm: kiểm soát truy cập, mã hóa và giám sát mạnh hơn cho các bậc nhạy cảm nhất.
- Dùng **[mã thông báo hóa](https://en.wikipedia.org/wiki/Tokenization_(data_security))** để thay các giá trị nhạy cảm (như số thẻ hay định danh quốc gia) bằng token không nhạy cảm, thu nhỏ các hệ thống từng chạm vào dữ liệu thô và qua đó thu nhỏ phạm vi tuân thủ.
- Dùng **[bút danh hóa](https://en.wikipedia.org/wiki/Pseudonymization)** để tách định danh khỏi phần còn lại của một bản ghi để dữ liệu ít quy được trực tiếp, giảm rủi ro trong khi giữ tính hữu dụng.
- Che dữ liệu nhạy cảm trong nhật ký, thông báo lỗi, phân tích và các môi trường phi sản xuất.

### Xử lý sự đồng ý và cơ sở pháp lý đúng cách

Xử lý dữ liệu cá nhân đòi hỏi một nền tảng pháp lý hợp lệ, và sự đồng ý chỉ là một trong nhiều.

- Xác định và lập tài liệu **cơ sở pháp lý** cho mỗi hoạt động xử lý: sự đồng ý, hợp đồng, nghĩa vụ pháp lý, lợi ích sống còn, nhiệm vụ công, hay lợi ích hợp pháp, tùy chế độ áp dụng.
- Ở nơi sự đồng ý là cơ sở, làm cho nó **được cho tự do, cụ thể, có hiểu biết và không mơ hồ**, với cách rút lại dễ dàng ngang nhau. Ô đánh dấu sẵn và đồng ý gộp không hợp lệ.
- Ghi lại sự đồng ý: người đó đã đồng ý với gì, khi nào, và theo điều khoản nào, để bạn có thể chứng minh nó.
- Tôn trọng **giới hạn mục đích**: đừng tái sử dụng dữ liệu cho điều không tương thích với lý do nó được thu thập mà không có cơ sở mới.
- Tôn trọng các tín hiệu như [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) và yêu cầu từ chối ở nơi luật yêu cầu.

### Quản lý chuyển giao xuyên biên giới và nơi lưu trữ dữ liệu

Nơi dữ liệu vật lý sống và di chuyển nay là mối quan tâm kiến trúc hạng nhất.

- Hiểu các yêu cầu về **nơi lưu trữ dữ liệu**: một số quyền tài phán yêu cầu một số dữ liệu ở lại trong biên giới quốc gia, và một số dữ liệu chính phủ phải ở trong các môi trường có chủ quyền hoặc được công nhận cụ thể.
- Với **chuyển giao xuyên biên giới**, bảo đảm có một cơ chế pháp lý hợp lệ (quyết định tương xứng, điều khoản hợp đồng tiêu chuẩn, hoặc tương đương) và được lập tài liệu.
- Kiến trúc cho nơi lưu trữ từ đầu: lưu trữ ghim theo vùng, bản địa hóa dữ liệu, và kiểm soát cẩn thận nơi bản sao lưu, nhật ký và dữ liệu phân tích chảy đến, vì chúng thường rò rỉ dữ liệu qua biên giới mà không ai để ý.
- Theo dõi bên xử lý phụ và bên thứ ba; một nhà cung cấp chuyển dữ liệu ra nước ngoài có thể vi phạm nghĩa vụ nơi lưu trữ thay mặt bạn.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Tối thiểu hóa dữ liệu quyết liệt | Ít rủi ro hơn, tác động xâm phạm nhỏ hơn, tuân thủ đơn giản hơn | Có thể hạn chế phân tích và các lựa chọn sản phẩm tương lai |
| Lưu giữ dài | Lịch sử phong phú cho phân tích, ML, tranh chấp | Nợ lớn hơn, phơi nhiễm xâm phạm, độ phức tạp xóa |
| Mã thông báo hóa | Thu nhỏ phạm vi tuân thủ, bảo vệ dữ liệu thô | Thêm độ phức tạp hệ thống, kho token phải bảo mật |
| Mặc định chọn tham gia | Niềm tin mạnh hơn, tuân thủ rõ ràng | Khối lượng dữ liệu thấp hơn, chỉ số tăng trưởng khó hơn |
| Nơi lưu trữ dữ liệu theo vùng | Đáp ứng yêu cầu pháp lý, xây niềm tin chủ quyền | Độ phức tạp kiến trúc, chi phí cao hơn, hạ tầng trùng lặp |
| Hồ dữ liệu tập trung | Sức mạnh phân tích, nguồn duy nhất | Rủi ro tập trung, giới hạn mục đích khó hơn |

Căng thẳng trung tâm là giữa sự thèm khát dữ liệu của doanh nghiệp và khoản nợ mà dữ liệu đại diện. Các đội sản phẩm và phân tích tự nhiên muốn thu thập nhiều hơn và giữ lâu hơn. Kỷ luật quyền riêng tư kéo ngược lại. Cách giải quyết trưởng thành đóng khung lại dữ liệu là một khoản nợ cần được biện minh, không phải một tài sản để tích trữ. Mỗi quyết định thu thập và lưu giữ phải xứng đáng với rủi ro nó tạo ra. Nơi lưu trữ dữ liệu thêm một chiều chi phí-so-với-tuân thủ. Đáp ứng yêu cầu chủ quyền có thể nhân lên hạ tầng, nhưng nó đơn giản là không thể thương lượng ở một số thị trường và bối cảnh chính phủ.

## Câu hỏi để thảo luận với đội của bạn

1. **Lịch lưu giữ của bạn cho mỗi lớp dữ liệu cá nhân là gì, và cái gì thực thi việc xóa?** Dữ liệu giữ "phòng khi" là dữ liệu đang chờ bị xâm phạm hoặc bị trát đòi, nên mỗi trường và mỗi bản ghi cần một thời gian sống xác định gắn với mục đích của nó. Hãy quyết định lịch theo loại dữ liệu, rồi thực thi nó bằng xóa tự động thay vì tin ai đó nhớ. Với doanh nghiệp điều này thu nhỏ cả phơi nhiễm xâm phạm lẫn chi phí lưu trữ cùng lúc, và với chính phủ nó khớp với nghĩa vụ luật định giữ dữ liệu công dân không lâu hơn luật cho phép. Hãy mang một mẫu các bản ghi cũ nhất của bạn và hỏi ai còn cần chúng và theo cơ sở nào, vì câu trả lời trung thực thường là không ai. Nếu việc xóa là thủ công hoặc không tồn tại, dữ liệu tích tụ mãi mãi và khoản nợ của bạn lớn lên lặng lẽ trên bảng cân đối.

2. **Trường nhạy cảm nào bạn có thể mã thông báo hóa hoặc bút danh hóa để thu nhỏ cả rủi ro và phạm vi tuân thủ?** Thay số thẻ hoặc định danh quốc gia bằng token giới hạn các giá trị thô vào một kho nhỏ, được kiểm soát chặt, cắt mạnh các hệ thống thuộc phạm vi cho các cuộc kiểm toán như PCI-DSS. Bút danh hóa tách định danh khỏi phần còn lại của một bản ghi, hạ rủi ro trong khi giữ dữ liệu hữu dụng cho phân tích và kiểm thử. Hãy quyết định giá trị độ nhạy cảm cao nào biện minh cho một kho token (thêm độ phức tạp, một kho phải bảo mật) và cái nào chỉ cần che trong nhật ký và phi sản xuất. Hãy mang bản đồ về nơi các giá trị nhạy cảm thô chảy hôm nay, vì mọi hệ thống chạm vào chúng là một hệ thống bạn phải bảo vệ và kiểm toán. Với dữ liệu chịu quy định và chính phủ, việc giảm phạm vi này là một trong số ít nước đi hạ cả chi phí lẫn rủi ro cùng lúc, nên hãy nhắm vào các trường nhạy cảm nhất của bạn trước.

3. **Trước khi tính năng kế tiếp của bạn được phát hành, cái gì kích hoạt một Đánh giá Tác động Bảo vệ Dữ liệu và ai thực hiện nó?** Quyền riêng tư gắn thêm vào một hệ thống đã hoàn chỉnh thì đắt và không đầy đủ, nên một DPIA phải chạy sớm, cùng với mô hình hóa mối đe dọa bảo mật, khi bạn vẫn có thể thay đổi thiết kế một cách rẻ. Hãy quyết định tác nhân kích hoạt (xử lý mới ở quy mô lớn, dữ liệu loại đặc biệt, một mục đích mới) và nêu tên ai sở hữu đánh giá để nó không rơi qua khe hở dưới áp lực phân phối. Một DPIA thực có thể bắt việc thu thập thừa trước khi ra mắt, ví dụ chuyển vị trí chính xác sang dữ liệu vùng thô mà không mất gì về sản phẩm. Hãy mang một tính năng sắp tới và đi qua nó: nó thu thập dữ liệu cá nhân nào, vì sao, và liệu một thiết kế ít xâm lấn hơn có đạt cùng mục tiêu không. Với các dịch vụ chính phủ mà công dân không thể chọn không tham gia, kiểm tra sớm này là một phần của nghĩa vụ chăm sóc, nên hãy biến nó thành một cổng, không phải chuyện nghĩ sau.

4. **Khi dữ liệu cá nhân băng qua một biên giới, bao gồm qua bản sao lưu, nhật ký và bên xử lý phụ, cơ chế pháp lý nào bao quát mỗi lần băng qua, và bạn có thể chứng minh không?** Quy tắc nơi lưu trữ và chuyển giao nay định hình kiến trúc nhiều như bất kỳ yêu cầu hiệu năng nào, và những lần băng qua làm các đội bất ngờ hiếm khi là những cái hiển nhiên: một nhật ký gửi đến công cụ quan sát ở nước ngoài, một bản sao lưu nhân bản sang vùng rẻ hơn, hay một bên xử lý phụ lặng lẽ chuyển dữ liệu ra nước ngoài. Với một tổ chức lớn các áp lực cạnh tranh là thật, vì hạ tầng ghim theo vùng tốn hơn và nhân đôi vận hành, nhưng một lần chuyển giao bất hợp pháp đơn lẻ có thể vô hiệu hóa việc vào một thị trường hoặc kích hoạt lệnh cưỡng chế. Hãy mang bản đồ luồng dữ liệu hiện tại gọi tên mọi nơi dữ liệu cá nhân vật lý nằm hay đi qua, cơ chế pháp lý cho mỗi biên giới nó băng qua (quyết định tương xứng, điều khoản hợp đồng tiêu chuẩn, hoặc tương đương), và danh sách bên xử lý phụ cùng vị trí của họ. Trong bối cảnh chính phủ và dữ liệu có chủ quyền, hãy coi nơi lưu trữ là ràng buộc kiến trúc cứng thay vì điều khoản hợp đồng, vì một số hồ sơ không bao giờ được rời khỏi các môi trường quốc gia được công nhận, và cơ quan chịu trách nhiệm không thể ủy thác nghĩa vụ đó cho nhà cung cấp.

5. **Cơ sở pháp lý nào hậu thuẫn mỗi hoạt động xử lý, và bạn có thể bảo vệ lựa chọn đó trước cơ quan quản lý vào ngày mai không?** Sự đồng ý chỉ là một trong nhiều nền tảng pháp lý, và các đội thường mặc định chọn nó khi hợp đồng, nghĩa vụ pháp lý, nhiệm vụ công, hay lợi ích hợp pháp sẽ vừa trung thực hơn vừa bền vững hơn. Điều này quan trọng ở quy mô lớn vì một cơ sở yếu hay chọn sai có thể vô hiệu hóa cả một đường ống, và gỡ rối xử lý bạn không có quyền thực hiện tốn kém hơn nhiều so với chọn cơ sở đúng ngay từ đầu. Hãy cân nhắc công khai các cân nhắc cạnh tranh: sự đồng ý cho cá nhân sự kiểm soát nhưng có thể bị rút lại và phải được cho tự do, cụ thể, không gộp, trong khi một cơ sở như lợi ích hợp pháp tránh mệt mỏi vì đồng ý nhưng đòi hỏi một phép thử cân bằng có tài liệu. Hãy mang một sổ đăng ký ánh xạ mỗi hoạt động xử lý với cơ sở được tuyên bố, bằng chứng hậu thuẫn nó, và cách bạn sẽ rút lại hay chuyển đổi nếu bị thách thức. Trong chính phủ, hầu hết xử lý cốt lõi dựa trên nhiệm vụ công thay vì sự đồng ý, nên hãy chính xác về nơi sự đồng ý tùy chọn, rút lại được bắt đầu, vì làm mờ hai thứ ăn mòn niềm tin mà công dân không có lựa chọn nào ngoài việc dành cho.

6. **Nếu một người thực hiện quyền truy cập, xóa hay chuyển dữ liệu hôm nay, bạn có thể thỏa mãn nó qua mọi hệ thống trong thời hạn pháp lý không?** Quyền của cá nhân dễ hứa trong chính sách quyền riêng tư và khó thực hiện trong một kiến trúc đã rải các bản sao dữ liệu cá nhân vào bản sao lưu, bộ đệm, kho phân tích và dịch vụ hạ nguồn. Với một đội lớn đây là khoảnh khắc tuân thủ trừu tượng trở thành một bài kiểm tra kỹ thuật cụ thể, và một hạn chót luật định bị lỡ vừa là một thất bại phải báo cáo vừa là tín hiệu rằng bạn thực sự không thấy được dữ liệu của chính mình. Cân nhắc đối lập là chi phí và độ phức tạp, vì xây việc xóa và xuất xuyên hệ thống thực sự là công việc thật, nhưng phương án thay thế là thực hiện thủ công, chậm, dễ sai không mở rộng được và lặng lẽ vi phạm luật. Hãy mang một buổi đi qua trung thực của một yêu cầu thật từ tiếp nhận đến hoàn thành, bao gồm cách bản sao lưu và bên thứ ba được với tới, và tính giờ so với hạn chót pháp lý. Với các dịch vụ chính phủ mà người ta không thể rời đi, hãy coi việc thực hiện quyền tự phục vụ, đầy đủ và kiểm toán được là một phần của nghĩa vụ chăm sóc, không phải tính năng lập lịch cho sau này.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với đội nhỏ xíu và đường băng ít ỏi, hãy coi quyền riêng tư là bảo hiểm rẻ hơn là một chương trình bạn không thể bố trí nhân sự. Chỉ thu thập các trường mà tính năng cốt lõi của bạn cần, giữ một bản đồ dữ liệu bảng tính nhẹ để bạn thực sự trả lời được một yêu cầu xóa, và giữ email cùng token ngoài nhật ký của bạn. Một luồng đồng ý rõ ràng và xóa thật tốn một buổi chiều bây giờ; trang bị chúng sau khi khách hàng doanh nghiệp đầu tiên hay cơ quan quản lý hỏi tốn nhiều hơn hẳn, và dữ liệu thu thập thừa là khoản nợ bạn không được gì khi giữ.

**Doanh nghiệp nhỏ.** Không có chuyên gia quyền riêng tư riêng và ngân sách eo hẹp, hãy dựa vào các biện pháp kiểm soát quyền riêng tư đã tích hợp trong công cụ bạn mua, và ưu tiên nhà cung cấp làm cho việc xử lý dữ liệu minh bạch và nơi lưu trữ rõ ràng. Hãy đóng khung quyết định là mua-so-với-xây: bạn hầu như không bao giờ tự xây mã thông báo hóa hay thực hiện quyền, vì vậy hãy chọn các nền tảng cung cấp quy tắc lưu giữ, xuất và xóa ngay từ đầu. Biết bạn giữ dữ liệu cá nhân nào và nơi một bản ghi sai hay mất sẽ khiến bạn mất khách hàng, và viết ra một cơ sở pháp lý cho mỗi mục đích dùng ngay cả khi tài liệu ngắn.

**Doanh nghiệp lớn.** Ở quy mô lớn vấn đề là sự nhất quán qua nhiều đội: một bản đồ dữ liệu dùng chung, các bậc phân loại được chuẩn hóa, và lưu giữ được thực thi để không nhóm đơn lẻ nào là mắt xích yếu. Hãy ngân sách tường minh kỹ thuật cho xóa xuyên hệ thống, kho mã thông báo, và kiến trúc nhận biết nơi lưu trữ, và quản trị bên xử lý phụ tập trung để một nhà cung cấp không thể vi phạm nghĩa vụ chuyển giao thay mặt bạn. Biến DPIA thành một cổng trong quy trình phân phối và đo tư thế quyền riêng tư, vì kiểm toán viên và cơ quan quản lý sẽ yêu cầu bạn chứng minh tuân thủ, không chỉ khẳng định.

**Chính phủ.** Quy tắc mua sắm, nghĩa vụ minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn, và công dân không thể mang dữ liệu thuế, y tế hay trợ cấp của họ đi nơi khác, nên nghĩa vụ chăm sóc được nâng cao. Hãy ghim các hồ sơ nhạy cảm vào các môi trường quốc gia được công nhận bao gồm cả bản sao lưu và phân tích, ràng buộc mọi nhà cung cấp bằng hợp đồng với cùng nghĩa vụ về nơi lưu trữ và xóa, và lập tài liệu một cơ sở pháp lý (thường là nhiệm vụ công) cho xử lý cốt lõi trong khi giữ các mục đích dùng tùy chọn trong sự đồng ý riêng, rút lại được. Hãy công bố mô tả bằng ngôn ngữ đơn giản về những gì bạn thu thập và vì sao, và làm cho việc thực hiện quyền đáng tin cậy trong mốc thời gian luật định, vì một thất bại quyền riêng tư ở đây ăn mòn niềm tin công chúng mà dịch vụ dựa vào.

## Ví dụ

**Công ty khởi nghiệp.** Một ứng dụng tiêu dùng giai đoạn đầu chỉ thu thập dữ liệu nó thực sự cần, vì mỗi trường thừa là một khoản nợ nó thà không phải bảo vệ sau này. Nó giữ một bản đồ dữ liệu bảng tính đơn giản về nơi dữ liệu cá nhân sống để thực sự trả lời được một yêu cầu xóa, giữ email và token ngoài nhật ký, và đặt một quy tắc lưu giữ cơ bản để thanh trừ dữ liệu từ các tài khoản đã chết từ lâu. Xây một luồng đồng ý rõ ràng và xóa thật bây giờ tốn một buổi chiều; trang bị chúng sau khi khách hàng doanh nghiệp đầu tiên hay cơ quan quản lý hỏi tốn nhiều hơn hẳn.

**Doanh nghiệp lớn.** Một ứng dụng tiêu dùng toàn cầu thực hiện một DPIA trước khi ra mắt tính năng gợi ý mới và phát hiện nó sẽ thu thập vị trí chính xác một cách không cần thiết; đội chuyển sang dữ liệu vùng thô, giảm rủi ro mà không mất gì về sản phẩm. Số thẻ được mã thông báo hóa để chỉ một kho nhỏ, được kiểm soát chặt mới giữ giá trị thô, cắt mạnh phạm vi [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (ngành thẻ thanh toán) của công ty. Các quy tắc lưu giữ tự động thanh trừ dữ liệu tài khoản không hoạt động theo lịch, và một luồng tự phục vụ cho phép người dùng xuất và xóa dữ liệu của họ trong thời hạn pháp lý qua mọi hệ thống bao gồm bản sao lưu.

**Chính phủ.** Một cơ quan y tế quốc gia phân loại mọi hồ sơ bệnh nhân là PHI và dữ liệu loại đặc biệt, thực thi kiểm soát truy cập, mã hóa và ghi nhật ký kiểm toán nghiêm ngặt. Chính sách nơi lưu trữ dữ liệu giữ mọi hồ sơ trong biên giới quốc gia, bao gồm bản sao lưu và phân tích, và mọi nhà cung cấp bị ràng buộc bằng hợp đồng với điều tương tự. Công dân có một cơ sở pháp lý có tài liệu (nhiệm vụ công) cho xử lý cốt lõi, trong khi các mục đích dùng nghiên cứu tùy chọn đòi hỏi sự đồng ý riêng, rút lại được, được ghi lại và tôn trọng. Một bản đồ dữ liệu làm nền cho khả năng đáp ứng yêu cầu truy cập và xóa trong mốc thời gian luật định.

## Luận chứng kinh doanh: động lực, ROI và TCO

Đầu tư vào quyền riêng tư thường được đóng khung như chi phí tuân thủ thuần túy, nhưng điều đó đánh giá thấp nó. Tổng chi phí sở hữu bao gồm quy trình DPIA, công cụ lập bản đồ và kiểm kê dữ liệu, hạ tầng mã thông báo hóa và lưu giữ, và kỹ thuật hỗ trợ quyền cá nhân cùng nơi lưu trữ. Hãy cân nhắc điều đó đối chiếu với chi phí của việc không đầu tư, vốn nghiêm trọng và ngày càng có khả năng. Tiền phạt về quyền riêng tư nay lên đến phần trăm của doanh thu toàn cầu, kiện tập thể theo sau các vụ xâm phạm lớn, và cơ quan quản lý đã chứng tỏ họ sẽ hành động. Ngoài tiền phạt, quyền riêng tư bị xử lý sai phá hủy niềm tin khách hàng làm nền cho doanh thu. Và khắc phục một thất bại quyền riêng tư sau sự việc (trang bị bổ sung việc xóa, gỡ rối các luồng dữ liệu bất hợp pháp) tốn nhiều hơn hẳn xây nó vào.

ROI cũng có mặt lợi thật. Quyền riêng tư mạnh là yếu tố khác biệt cạnh tranh, và ở các thị trường chịu quy định và chính phủ nó là điều kiện tiên quyết để giành kinh doanh. Tối thiểu hóa dữ liệu trực tiếp giảm phơi nhiễm xâm phạm và chi phí lưu trữ, và mã thông báo hóa thu nhỏ phạm vi tốn kém của các cuộc kiểm toán như PCI-DSS. Khi bạn trình bày lập luận với ban lãnh đạo, hãy trình bày quyền riêng tư theo hai cách: như quản lý nợ có điều chỉnh rủi ro với mức phơi nhiễm quy định thực, và như một tài sản niềm tin mở ra thị trường. Hãy nhấn mạnh rằng quyền riêng tư-theo-thiết-kế rẻ so với quyền riêng tư-theo-kiện-tụng, và rằng dữ liệu tích trữ không có mục đích là khoản nợ nằm trên bảng cân đối, chờ được hiện thực hóa.

## Phản mẫu và cạm bẫy

- **Thu thập mọi thứ, quyết định sau.** Tích trữ dữ liệu không có mục đích, tối đa hóa nợ mà không có lợi ích.
- **Lưu giữ do bỏ bê.** Không bao giờ xóa gì vì không có lịch, nên dữ liệu tích tụ mãi mãi.
- **Sân khấu đồng ý.** Ô đánh dấu sẵn, đồng ý gộp, hoặc mẫu tối vừa bất hợp pháp vừa ăn mòn niềm tin.
- **Xóa bỏ sót bản sao lưu.** Xóa khỏi kho chính nhưng để lại bản sao trong bản sao lưu, nhật ký và phân tích.
- **PII trong nhật ký và dữ liệu kiểm thử.** Rải dữ liệu nhạy cảm vào các môi trường ít kiểm soát nơi nó dễ bị phơi bày.
- **Bỏ qua luồng dữ liệu.** Bỏ sót rằng nhật ký, bản sao lưu, phân tích và bên xử lý phụ di chuyển dữ liệu qua biên giới.
- **Quyền riêng tư chỉ là mối quan tâm pháp lý.** Coi nó là giấy tờ hơn là một ràng buộc thiết kế kỹ thuật.
- **Không có bản đồ dữ liệu.** Không trả lời được dữ liệu cá nhân sống ở đâu, khiến yêu cầu quyền và phản ứng xâm phạm là không thể.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Quyền riêng tư được xử lý phản ứng, nếu có. Dữ liệu cá nhân được thu thập tự do không có kiểm kê, tối thiểu hóa hay giới hạn lưu giữ. Sự đồng ý là chuyện nghĩ sau, không có quy trình cho yêu cầu truy cập hay xóa, và nơi dữ liệu vật lý sống không được cân nhắc.

**Mức 2: Phát triển.** Các thực hành cơ bản xuất hiện nhưng khác nhau theo đội. Một chính sách quyền riêng tư tồn tại và sự đồng ý cơ bản được ghi nhận, với chút nhận thức về lưu giữ. Yêu cầu quyền được xử lý thủ công và chậm, phân loại dữ liệu không chính thức, và một đội có thể lập bản đồ dữ liệu của mình trong khi đội khác thu thập tự do. Không gì được thực thi nhất quán trong tổ chức.

**Mức 3: Chuẩn hóa.** Quyền riêng tư theo thiết kế được lập tài liệu và thực thi toàn tổ chức. DPIA chạy cho các dự án rủi ro cao hơn, dữ liệu được lập bản đồ và phân loại thành các bậc, và lịch lưu giữ được thực thi bằng xóa tự động. Một cơ sở pháp lý được lập tài liệu cho mỗi hoạt động xử lý, cơ chế đồng ý hợp lệ có mặt, yêu cầu quyền được thực hiện trong thời hạn, và nơi lưu trữ được giải quyết cho dữ liệu chịu quy định.

**Mức 4: Quản lý.** Chương trình quyền riêng tư được đo và kiểm soát theo các đường cơ sở. Bạn theo dõi thời gian thực hiện yêu cầu quyền so với hạn chót luật định, độ bao phủ chính sách lưu giữ và tuổi của các bản ghi cũ nhất, số trường dữ liệu cá nhân thuộc phạm vi và bao nhiêu được mã thông báo hóa hay bút danh hóa, tỷ lệ hoàn thành DPIA cho các tính năng đủ điều kiện, và số luồng xuyên biên giới không được quản lý tìm thấy trong kiểm toán. Các chỉ số nuôi các ngưỡng xác định, nên việc vượt một mục tiêu (một yêu cầu quyền gần hạn chót, một chuyển giao bất ngờ, sự trôi lưu giữ) kích hoạt một phản ứng có tài liệu thay vì không được để ý.

**Mức 5: Điều phối.** Quyền riêng tư là ràng buộc kỹ thuật mặc định, liên tục cải thiện và tích hợp trong toàn tổ chức. Tối thiểu hóa, mã thông báo hóa và lưu giữ tự động là tiêu chuẩn, yêu cầu quyền là tự phục vụ và đầy đủ qua mọi hệ thống bao gồm bản sao lưu, và luồng dữ liệu cùng nơi lưu trữ được theo dõi và thực thi liên tục. Tư thế quyền riêng tư thích ứng khi quy định, thị trường và kiến trúc dịch chuyển, đưa bài học trở lại thiết kế để đường cơ sở tiếp tục nâng lên thay vì chỉ giữ nguyên.

## Ý tưởng để thảo luận

1. Làm sao bạn giải quyết căng thẳng giữa các đội phân tích muốn nhiều dữ liệu hơn và quyền riêng tư muốn ít hơn?
2. Một kiến trúc thực tế để tôn trọng việc xóa qua kho chính, bản sao lưu và bản sao hạ nguồn là gì?
3. Cơ sở pháp lý nào phù hợp với từng hoạt động xử lý của bạn, và bạn có bảo vệ được lựa chọn đó không?
4. Làm sao bạn giữ dữ liệu cá nhân ngoài nhật ký và môi trường phi sản xuất mà không cản trở gỡ lỗi?
5. Yêu cầu nơi lưu trữ dữ liệu nào áp dụng cho các thị trường của bạn, và bản sao lưu cùng phân tích làm chúng phức tạp ra sao?
6. Mô hình hóa mối đe dọa quyền riêng tư và bảo mật nên được kết hợp thành một hoạt động thiết kế duy nhất thế nào?

## Những điểm cần ghi nhớ

- Quyền riêng tư điều chỉnh liệu và cách bạn dùng dữ liệu cá nhân; nó khác với và bổ sung cho bảo mật.
- Thiết kế quyền riêng tư vào từ đầu với DPIA và mặc định bảo vệ quyền riêng tư.
- Tối thiểu hóa thu thập, thực thi lịch lưu giữ, và xây năng lực xóa thực sự.
- Phân loại PII, PHI và các loại đặc biệt, và bảo vệ chúng tương xứng bằng mã thông báo hóa và che.
- Thiết lập và lập tài liệu một cơ sở pháp lý; làm cho sự đồng ý được cho tự do, cụ thể và rút lại được.
- Coi nơi lưu trữ dữ liệu và chuyển giao xuyên biên giới là ràng buộc kiến trúc hạng nhất.
- Dữ liệu là một khoản nợ cũng như một tài sản; tích trữ nó không có mục đích là rủi ro đang chờ được hiện thực hóa.

## Tài liệu tham khảo và đọc thêm

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- Liên minh Châu Âu, văn bản và hướng dẫn *General Data Protection Regulation (GDPR)*
- National Institute of Standards and Technology, *Privacy Framework* và *SP 800-122* (Guide to Protecting PII)
- ISO/IEC 27701, *Privacy Information Management*
- Daniel Solove, *Understanding Privacy*
- OECD, *Privacy Guidelines* và *Fair Information Practice Principles (FIPPs)*
- Văn bản luật California Consumer Privacy Act (CCPA/CPRA) và hướng dẫn của cơ quan quản lý
