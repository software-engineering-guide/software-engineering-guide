# 6.3 AI sinh tạo và ứng dụng LLM

## Tổng quan và động lực

[AI sinh tạo](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), và đặc biệt là [mô hình ngôn ngữ lớn](https://en.wikipedia.org/wiki/Large_language_model) (LLM), có thể tạo ra văn bản trôi chảy, mã, bản tóm tắt và dữ liệu có cấu trúc từ các chỉ dẫn bằng ngôn ngữ tự nhiên. Điều đó khiến chúng thành những khối xây dựng mạnh cho trợ lý, tìm kiếm, xử lý tài liệu và tự động hóa. Nhưng những điểm mạnh đó đi kèm một hồ sơ rủi ro đặc thù. LLM mang tính xác suất. Chúng có thể tạo ra những điều sai tự tin ([ảo giác](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Chúng nhạy với cách bạn viết prompt. Và chúng mở ra các bề mặt tấn công mới như [tiêm prompt](https://en.wikipedia.org/wiki/Prompt_injection) (các chỉ dẫn độc hại được lén vào đầu vào để chiếm quyền hành vi của mô hình). Vì vậy xây dựng ứng dụng LLM đáng tin cậy ít nói về mô hình mà nhiều hơn về kỹ thuật bao quanh nó: cách bạn cung cấp ngữ cảnh, neo câu trả lời vào kiến thức đáng tin, ràng buộc đầu ra, và đánh giá chất lượng.

Với các đội lớn, ứng dụng LLM đòi hỏi các mẫu mới khác với cả phần mềm truyền thống lẫn học máy cổ điển. Thường không có bước huấn luyện. Thay vào đó, hành vi được định hình bởi prompt, ngữ cảnh truy xuất, định nghĩa công cụ và lan can (kiểm tra lúc chạy ràng buộc đầu vào và đầu ra của mô hình). Điều đó chuyển công sức kỹ thuật sang quản lý ngữ cảnh, chất lượng truy xuất, điều phối và đánh giá. Các doanh nghiệp áp dụng LLM ở quy mô lớn cần các mẫu dùng chung để mỗi đội không phải tự khám phá lại cùng các kiểu thất bại bằng con đường khó.

Các tổ chức chính phủ và chịu quy định đối mặt thêm đòi hỏi. Một LLM bịa ra một trích dẫn chính sách hoặc làm rò dữ liệu nhạy cảm không chỉ là một lỗi; nó có thể là một sự cố pháp lý hay an toàn. Những bối cảnh này cần neo vào các nguồn có thẩm quyền, xác thực đầu ra nghiêm ngặt, giám sát bởi con người cho đầu ra hệ quả, và hồ sơ rõ ràng về những gì hệ thống được hỏi và những gì nó tạo ra. Các kỹ thuật trong chương này (sinh tạo tăng cường truy xuất, lan can và đánh giá nghiêm ngặt) là thứ làm LLM đủ an toàn để triển khai trong các bối cảnh rủi ro cao. Các mô hình Claude của Anthropic là một lựa chọn hàng đầu trong số nhiều nhà cung cấp có năng lực; các thực hành ở đây áp dụng bất kể bạn chọn mô hình nào.

## Các nguyên tắc chính

- Neo mô hình vào kiến thức đáng tin thay vì dựa vào những gì nó đã ghi nhớ.
- Coi prompt và ngữ cảnh là các hiện vật được thiết kế, đánh phiên bản, không phải những chuỗi vứt đi.
- Giả định mô hình có thể sai hoặc bị thao túng; xác thực đầu ra và ràng buộc hành động.
- Chỉ cho mô hình ngữ cảnh và công cụ nó cần, không hơn, để giảm lỗi và bề mặt tấn công.
- Đánh giá liên tục bằng tập kiểm thử ngoại tuyến, chỉ số trực tuyến và phán đoán của con người.
- Giữ con người trong vòng lặp cho đầu ra hệ quả.
- Thiết kế coi mô hình là một thành phần không đáng tin trong một hệ thống đáng tin.

## Khuyến nghị

### Thiết kế prompt và quản lý ngữ cảnh có chủ đích

Hãy coi prompt như mã: lưu chúng trong quản lý phiên bản, rà soát thay đổi, và kiểm thử chúng với một bộ ví dụ. Cấu trúc mỗi prompt rõ ràng: vai trò và nhiệm vụ, ràng buộc, yêu cầu định dạng, và ví dụ nơi chúng giúp ích. Hãy coi cửa sổ ngữ cảnh (đoạn văn bản cố định mà mô hình có thể xét cùng lúc) là một nguồn lực khan hiếm. Đưa vào thông tin liên quan nhất, sắp xếp nó cẩn thận, và loại bỏ nhiễu, vì ngữ cảnh không liên quan hoặc quá mức làm giảm chất lượng và tăng chi phí. Với ứng dụng nhiều lượt, hãy quản lý trạng thái hội thoại tường minh, tóm tắt hoặc cắt bớt lịch sử để giữ trong giới hạn trong khi giữ lại điều quan trọng. Ưu tiên chỉ dẫn rõ ràng và ví dụ few-shot (một nhúm minh họa đã làm sẵn được đưa vào prompt) hơn các mánh khóe cầu kỳ vỡ ngay khi mô hình đổi.

### Neo câu trả lời bằng sinh tạo tăng cường truy xuất (RAG)

Với các nhiệm vụ nặng kiến thức, hãy truy xuất các tài liệu liên quan từ một kho đáng tin và cung cấp cho mô hình làm ngữ cảnh, bảo nó chỉ trả lời từ tài liệu đó và trích dẫn nguồn. RAG giữ kiến thức cập nhật mà không cần huấn luyện lại, giới hạn câu trả lời trong nội dung được phê duyệt, và cho phép trích dẫn cùng xác minh. Hãy đầu tư vào chất lượng truy xuất: chia tài liệu thành đoạn hợp lý, chọn [embedding](https://en.wikipedia.org/wiki/Word_embedding) (biểu diễn vector số đặt các nghĩa tương tự gần nhau) phù hợp với miền của bạn, và kiểm tra xem các đoạn được truy xuất có thực sự chứa câu trả lời không, vì một câu trả lời trôi chảy dựng trên đoạn sai còn tệ hơn không có câu trả lời. Và khi không có gì liên quan xuất hiện, hãy để hệ thống nói như vậy thay vì bịa nội dung.

### Xây tác tử và dùng công cụ có kiềm chế

LLM có thể gọi công cụ (tìm kiếm, cơ sở dữ liệu, máy tính, API nội bộ) và có thể được ghép thành tác tử lập kế hoạch và hành động qua nhiều bước. Điều này thêm năng lực thật, nhưng cũng nhân rủi ro: mỗi công cụ là một cách nữa để một mô hình sai hay bị thao túng gây hại. Hãy định nghĩa công cụ với lược đồ chính xác, xác thực mọi đối số, áp dụng quyền tối thiểu, và yêu cầu xác nhận hoặc phê duyệt của con người cho các hành động hệ quả như gửi thông tin liên lạc hay chuyển tiền. Giữ các vòng lặp tác tử có giới hạn, quan sát được và ngắt được. Hãy bắt đầu với các công cụ phạm vi hẹp, đơn mục đích trước khi với tới quyền tự chủ mở.

### Thêm lan can và xác thực đầu ra

Hãy bọc mô hình trong các lớp phòng thủ. Ở đầu vào, lọc và phát hiện tiêm prompt, đặc biệt khi nội dung không đáng tin (trang web, tài liệu người dùng) đi vào ngữ cảnh. Ở đầu ra, xác thực cấu trúc theo lược đồ, kiểm tra các khẳng định với nguồn, lọc nội dung không an toàn hay không tuân thủ, và từ chối hoặc thử lại khi xác thực thất bại. Với đầu ra có cấu trúc, hãy phân tích và xác minh thay vì tin định dạng của mô hình. Đừng bao giờ để đầu ra thô của mô hình kích hoạt hành động không đảo ngược được mà không xác thực. Hãy coi giảm thiểu ảo giác là một thuộc tính của hệ thống bạn đạt được qua neo đất, trích dẫn, xác thực và rà soát của con người, không phải thứ mô hình tự quản lý.

### Đánh giá ngoại tuyến, trực tuyến và với con người

Hãy xây một bộ đánh giá gồm các đầu vào đại diện với đầu ra đã biết là tốt hoặc được chấm điểm theo thang, và chạy nó với mọi thay đổi prompt hay mô hình (đánh giá ngoại tuyến). Đo hành vi thực trong môi trường sản xuất bằng các chỉ số như thành công nhiệm vụ, tỷ lệ leo thang và phản hồi người dùng (đánh giá trực tuyến). Với chất lượng chủ quan, hãy dùng người rà soát và, một cách cẩn thận, chấm điểm dựa trên mô hình. Đánh giá là tấm lưới an toàn cho phép bạn đổi prompt và mô hình tự tin. Không có nó, bạn bay mù.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Tốt nhất khi |
|---|---|---|---|
| Chỉ prompt | Đơn giản, nhanh, rẻ để đổi | Neo đất hạn chế, có thể ảo giác | Nhiệm vụ rộng, rủi ro thấp |
| RAG | Cập nhật, được neo, trích dẫn được | Truy xuất khó làm đúng | Nhiệm vụ nặng kiến thức, thực tế |
| Tác tử có công cụ | Mạnh, có thể hành động | Bề mặt tấn công lớn hơn, khó kiểm soát hơn | Tự động hóa phạm vi rõ có lan can |
| Mô hình lớn hơn, mạnh hơn | Chất lượng và suy luận tốt hơn | Chi phí và độ trễ cao hơn | Nhiệm vụ phức tạp hoặc rủi ro cao |
| Mô hình nhỏ hơn, rẻ hơn | Nhanh và không đắt | Yếu hơn với nhiệm vụ khó | Khối lượng cao, nhiệm vụ đơn giản |

Căng thẳng cốt lõi là năng lực so với kiểm soát và chi phí. Nhiều quyền tự chủ hơn và mô hình lớn hơn mang lại nhiều giá trị hơn, nhưng đòi nhiều lan can hơn, nhiều đánh giá hơn, và nhiều tiền hơn. Neo đất qua RAG cải thiện độ đáng tin với cái giá là kỹ thuật truy xuất. Sự cân bằng đúng phụ thuộc vào rủi ro: các ứng dụng rủi ro cao nghiêng về neo đất, xác thực và giám sát của con người, ngay cả khi điều đó tốn hơn.

## Câu hỏi để thảo luận với đội của bạn

1. **Một tính năng LLM phải vượt mức chính xác và neo đất nào trước khi gặp công chúng, và ai ký duyệt?** Một câu trả lời trôi chảy trích dẫn sai nguồn hoặc bịa chính sách còn tệ hơn không có câu trả lời, và trong chính phủ một trích dẫn bịa đặt là sự cố pháp lý, không phải lỗi. Với một đội lớn, một mức chuẩn tường minh ngăn mỗi nhóm đặt ngưỡng riêng theo cảm tính. Hãy mang định nghĩa của bạn về "đủ neo đất": liệu mọi khẳng định có phải truy vết được đến một nguồn đã truy xuất, đã xác minh, liệu hệ thống có phải từ chối khi truy xuất trống, và tập đánh giá đối kháng của bạn thực sự bao quát gì. Tín hiệu cần theo dõi là liệu hiện giờ có ai có thể phát hành một thay đổi prompt thẳng đến người dùng mà không chạy hồi quy. Nếu rủi ro liên quan đến pháp lý hay an toàn, câu trả lời nên chuyển các đầu ra rủi ro cao nhất qua một người rà soát có thẩm quyền thật trước khi phát hành.

2. **Tính năng LLM nào của chúng ta thực ra là tác tử trá hình, và mỗi công cụ đã được cấp quyền tối thiểu và một cổng con người cho hành động không đảo ngược chưa?** Bất kỳ tính năng nào cho mô hình gọi công cụ hoặc hành động qua nhiều bước đã bước vào lãnh thổ tác tử, và mỗi công cụ là một cách nữa để mô hình sai hay bị thao túng gây hại. Với các doanh nghiệp nối LLM vào API nội bộ, câu hỏi này làm lộ rủi ro mà nhãn "trợ lý đơn giản" che giấu. Hãy mang bản kiểm kê mọi công cụ mô hình có thể gọi, xác thực đối số của nó, phạm vi quyền, và hành động nào (gửi thông tin liên lạc, chuyển tiền, đổi hồ sơ) đòi xác nhận. Hãy thảo luận liệu các vòng lặp tác tử có giới hạn, quan sát được và ngắt được. Câu trả lời nên thắt chặt phạm vi và thêm cổng phê duyệt của con người ở bất cứ đâu một hành động hệ quả hay không đảo ngược hiện với tới được mà không có.

3. **Làm sao chúng ta biết trong vòng một ngày rằng chất lượng truy xuất đã tụt, khi một câu trả lời tự tin dựng trên đoạn sai trông vẫn ổn?** RAG làm câu trả lời đáng tin chỉ khi truy xuất thực sự đưa ra đoạn chứa câu trả lời, và truy xuất mục rữa lặng lẽ khi tài liệu thay đổi, các đoạn cũ đi, hoặc embedding trôi khỏi miền của bạn. Vì mô hình vẫn viết trôi chảy trên ngữ cảnh tồi, người dùng có thể không phàn nàn cho đến khi niềm tin đã mất. Hãy mang các thước đo hiện tại về độ trễ và độ phủ truy xuất, cách bạn kiểm tra liệu các đoạn truy xuất có thực sự chứa câu trả lời, và độ mới của chỉ mục theo kịp thay đổi tài liệu thế nào. Với các triển khai rủi ro cao hay công khai, hãy thảo luận ghi nhật ký nguồn được truy xuất để kiểm toán nhằm truy một câu trả lời tồi về đoạn tồi của nó. Nếu bạn không có đánh giá truy xuất nào, bạn đang neo đất bằng đức tin.

4. **Chúng ta coi prompt, ngữ cảnh và tập đánh giá là các hiện vật được đánh phiên bản, rà soát, hay là những chuỗi rải rác trong sổ tay và nhật ký trò chuyện?** Khi prompt lan tràn qua các đội không đánh phiên bản và trùng lặp, một bản sửa ở một nơi không bao giờ đến các nơi khác, và không ai tái lập được hệ thống đã được yêu cầu làm gì quý trước. Với một đội lớn, một sổ đăng ký prompt dùng chung và một bộ hồi quy chạy ở mỗi thay đổi là thứ cho phép bạn đổi mô hình hay sửa chỉ dẫn mà không lặng lẽ làm hỏng một tính năng cách hai đội. Lực kéo đối lập là tốc độ: kỹ sư lặp nhanh nhất khi dán một prompt rồi phát hành, nên hãy thống nhất ranh giới giữa thí nghiệm nhanh và bất cứ thứ gì chạm đến người dùng. Hãy mang nơi prompt của bạn thực sự sống hôm nay, liệu một tập đánh giá có chặn cổng thay đổi, và bạn đánh phiên bản kho truy xuất cùng với prompt thế nào. Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm yêu cầu kiểm toán: bạn có thể phải chỉ ra chính xác prompt và nguồn nào tạo ra một đầu ra nhất định nhiều tháng sau, và một prompt bạn không dựng lại được là một hồ sơ bạn không bảo vệ được.

5. **Khi khối lượng tăng, chúng ta kiểm soát chi phí suy luận thế nào mà không lặng lẽ hạ chất lượng, và ai sở hữu quyết định chọn mô hình?** TCO cho tính năng LLM bị chi phối bởi suy luận mỗi lệnh gọi, và chi phí trông tầm thường trong bản thí điểm cộng dồn nhanh ở quy mô sản xuất, cám dỗ các đội lặng lẽ hạ xuống mô hình yếu hơn và hy vọng không ai nhận ra chất lượng trượt. Với một tổ chức lớn, để mỗi đội chọn mô hình và giới hạn chi phí theo cảm tính tạo ra cả hóa đơn bất ngờ lẫn chất lượng không nhất quán. Đánh đổi thật là năng lực so với chi phí và độ trễ: mô hình lớn hơn suy luận tốt hơn ở nhiệm vụ khó, mô hình nhỏ hơn rẻ và nhanh hơn ở nhiệm vụ đơn giản, và bộ nhớ đệm, định tuyến, và phạm vi truy xuất đều dịch chuyển con số. Hãy mang chi phí mỗi nhiệm vụ đã giải quyết, chất lượng theo bậc mô hình trên tập đánh giá của bạn, và nơi prompt hoặc ngữ cảnh phình to đang đẩy chi tiêu token. Trong ngân sách doanh nghiệp và chính phủ, hãy nêu ai phê duyệt lựa chọn mô hình và trần chi tiêu, vì một dòng chi phí không ai sở hữu là cái không ai kiểm soát khi lưu lượng tăng gấp ba.

6. **Dữ liệu nhạy cảm nào có thể đến mô hình, dữ liệu đó đi đâu, và chúng ta có chứng minh được nó ở trong giới hạn không?** Mỗi prompt, tài liệu truy xuất và kết quả công cụ có thể mang dữ liệu cá nhân hay bí mật vào mô hình và, với nhà cung cấp lưu trữ, ra khỏi vành đai của bạn, và một vụ rò ở đây là sự cố pháp lý hay an toàn, không phải phiếu lỗi. Với một đội lớn nối LLM vào hệ thống nội bộ, rủi ro ẩn trong đường ống: một kho truy xuất gồm các bản ghi mà một người dùng nhất định không bao giờ nên thấy, hoặc nhật ký ghi đầu vào thô. Căng thẳng là năng lực so với phơi nhiễm, vì che giấu và giới hạn phạm vi chặt có thể làm cùn tính năng bạn đang xây. Hãy mang bản đồ luồng dữ liệu những gì đi vào ngữ cảnh, điều khoản lưu giữ và huấn luyện của nhà cung cấp, và cách bạn che giấu, giới hạn phạm vi và ghi nhật ký các trường nhạy cảm. Trong bối cảnh chịu quy định và công, hãy gắn điều này với quy tắc cư trú dữ liệu, nghĩa vụ lưu giữ hồ sơ, và giới hạn hợp đồng về cách nhà cung cấp được dùng dữ liệu của bạn, vì sự giám sát bạn không chứng minh được là sự giám sát bạn không có.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy phát hành một tính năng LLM hẹp chạm đến giá trị cốt lõi của bạn, xây trên một mô hình lưu trữ sẵn với truy xuất trên nội dung của chính bạn, và giữ prompt trong git sau một giao diện mỏng để đổi được nhà cung cấp. Chạy một tệp đánh giá nhỏ gồm câu hỏi thật trước mỗi thay đổi, lọc văn bản người dùng dán vào để làm cùn tiêm prompt, và giới hạn chi tiêu hằng tháng chặt. Chống lại tác tử và tự lưu trữ: một vòng lặp gọi công cụ không giới hạn mà bạn không giám sát được là gánh nặng, không phải bản demo.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia ML, vì vậy hãy mua các tính năng LLM nhúng trong công cụ bạn đã dùng thay vì bố trí nhân sự để xây. Hãy đóng khung rủi ro như một câu hỏi đơn giản: nơi nào một câu trả lời sai tự tin sẽ làm bạn mất một khách hàng, và ai kiểm tra đầu ra trước khi nó gửi đi. Ưu tiên nhà cung cấp cho thấy nguồn, cho bạn giữ con người trong vòng lặp, và làm AI dễ tắt khi nó hành xử sai.

**Doanh nghiệp lớn.** Vấn đề là quy mô qua nhiều đội: hãy công bố các mẫu dùng chung cho RAG, lan can và lược đồ công cụ, cùng một bộ khung đánh giá và sổ đăng ký prompt chung để mỗi nhóm thôi tự khám phá lại cùng các kiểu thất bại. Hãy lập ngân sách tường minh cho chi phí suy luận và rà soát của con người, chuẩn hóa tầng giao diện để mô hình thay thế được, và quản trị tác tử tập trung với quyền tối thiểu, vòng lặp có giới hạn và ghi nhật ký kiểm toán. Hãy quản lý tính năng LLM như một danh mục có chỉ số và tiêu chí khai tử, không phải một mớ bản thí điểm rải rác.

**Chính phủ.** Minh bạch, quy tắc mua sắm và trách nhiệm giải trình định hình mọi lựa chọn. Hãy neo chặt vào các nguồn được phê duyệt kèm trích dẫn, từ chối khi truy xuất trống, và cấm mô hình nêu luật mà nó không trích dẫn được. Giữ một viên chức chịu trách nhiệm rà soát đầu ra hệ quả, ghi nhật ký đầu vào và nguồn truy xuất để kiểm toán, chạy một tập đánh giá đối kháng trước mỗi bản phát hành, và đòi tiết lộ hạn chế mô hình cùng điều khoản xử lý dữ liệu trong hợp đồng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp công cụ dành cho lập trình viên ba người thêm một trợ lý trò chuyện trên chính tài liệu của mình để người dùng thôi gửi email hỏi những câu cơ bản. Họ dùng RAG để mỗi câu trả lời trích dẫn một trang tài liệu cụ thể, chỉ dẫn mô hình nói "Tôi không chắc, đây là người để hỏi" khi truy xuất trống, và giữ prompt trong git. Trước mỗi thay đổi, họ chạy các prompt trên một tệp nhỏ các câu hỏi thật của người dùng để bắt hồi quy, và lọc văn bản người dùng dán vào để làm cùn tiêm prompt. Trợ lý xử lý các câu hỏi thường gặp và lặng lẽ chuyển phần còn lại vào hộp thư chung của những người sáng lập.

**Doanh nghiệp lớn.** Một công ty phần mềm xây một trợ lý hỗ trợ nội bộ trên tài liệu sản phẩm của mình. Họ dùng [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) để câu trả lời trích dẫn các trang tài liệu cụ thể, bảo mô hình nói "Tôi không biết" khi truy xuất thất bại, và xác minh rằng mọi nguồn được trích dẫn thực sự tồn tại. Prompt được quản lý phiên bản và kiểm thử với một bộ câu hỏi hỗ trợ thật ở mỗi thay đổi. Trợ lý làm chệch hướng các phiếu thường lệ và leo thang mọi thứ có độ tin cậy thấp lên nhân viên con người, trong khi các chỉ số trực tuyến theo dõi tỷ lệ giải quyết và chỉnh sửa.

**Chính phủ.** Một cơ quan công triển khai một trợ lý LLM giúp nhân viên soạn phản hồi cho thắc mắc của công dân. Việc neo đất rất nghiêm ngặt: mô hình chỉ được soạn phản hồi từ hướng dẫn đã phê duyệt kèm trích dẫn, và bị cấm nêu chính sách không có trong nguồn đã truy xuất. Một viên chức chịu trách nhiệm rà soát mọi bản nháp trước khi gửi đi. Lọc đầu vào bảo vệ chống tiêm prompt từ tài liệu công dân nộp, đầu ra được ghi nhật ký để kiểm toán, và một tập đánh giá các truy vấn đối kháng và trường hợp biên chạy trước mỗi bản phát hành để xác nhận hệ thống từ chối suy đoán về các vấn đề pháp luật.

## Luận chứng kinh doanh: động lực, ROI và TCO

Ứng dụng LLM mang lại ROI bằng cách tự động hóa công việc nặng ngôn ngữ: trả lời câu hỏi, tóm tắt tài liệu, soạn nội dung, và trích xuất cấu trúc từ văn bản phi cấu trúc. Giá trị hiện ra là phiếu được làm chệch hướng, soạn thảo nhanh hơn, ít rà soát thủ công hơn, và năng lực tự phục vụ mới. Vì thường không có bước huấn luyện, thời gian đến giá trị đầu tiên ngắn, một sức hút lớn.

Tuy nhiên, TCO bị chi phối bởi chi phí suy luận liên tục, hạ tầng truy xuất, đường ống đánh giá, hệ thống lan can, và rà soát của con người. Chi phí mỗi lệnh gọi cộng dồn nhanh ở quy mô, và một ứng dụng không được giám sát có thể trôi vào hành vi không an toàn hoặc đắt đỏ. Chi phí của việc không áp dụng là tụt lại về chất lượng dịch vụ và năng suất nhân viên. Chi phí của việc áp dụng cẩu thả là một sự cố ảo giác công khai hoặc một vụ rò dữ liệu. Hãy lập luận với ban lãnh đạo bằng cách ghép một mục tiêu năng suất cụ thể với một kế hoạch an toàn và đánh giá cụ thể, và bằng cách lập ngân sách cho lan can và giám sát của con người giúp giá trị bền vững.

## Phản mẫu và cạm bẫy

- **Tin đầu ra trôi chảy.** Nhầm văn bản tự tin, viết hay với văn bản đúng.
- **RAG không đánh giá truy xuất.** Giả định truy xuất hoạt động và không bao giờ kiểm tra liệu nó có đưa ra đúng đoạn.
- **Mù trước tiêm prompt.** Đưa nội dung không đáng tin vào prompt mà không có phòng thủ.
- **Tác tử không giới hạn.** Để tác tử thực hiện hành động hệ quả không có giới hạn hay phê duyệt của con người.
- **Không có khung đánh giá.** Đổi prompt và mô hình theo cảm tính, không kiểm thử hồi quy.
- **Prompt lan tràn.** Prompt rải rác, không đánh phiên bản và trùng lặp qua các đội.
- **Tự động hóa quá mức.** Loại con người khỏi các quyết định mang trọng lượng pháp lý hay an toàn.

## Mô hình trưởng thành

1. **Khởi đầu.** Viết prompt tùy nghi trong các dự án cô lập; không neo đất, lan can hay đánh giá; prompt sống ở bất cứ đâu ai đó dán chúng, và ảo giác được phát hiện trong môi trường sản xuất.
2. **Phát triển.** Một số đội thêm RAG và đánh phiên bản prompt, xác thực đầu ra cơ bản, và một tập đánh giá thủ công nhỏ, nhưng thực hành khác nhau theo đội và dựa vào những người ủng hộ cá nhân thay vì kỳ vọng chung.
3. **Chuẩn hóa.** Các mẫu có tài liệu cho RAG, lan can, lược đồ công cụ và đánh phiên bản prompt được thực thi toàn tổ chức; đánh giá ngoại tuyến tự động chạy ở mỗi thay đổi prompt hay mô hình; các luồng rủi ro cao mang chỉ số trực tuyến và rà soát của con người.
4. **Quản lý.** Danh mục được đo theo đường cơ sở: độ phủ truy xuất, tỷ lệ ảo giác và từ chối, độ phủ phòng thủ tiêm prompt, chi phí và độ trễ mỗi lệnh gọi, tỷ lệ leo thang và chỉnh sửa được theo dõi trên bảng điều khiển; cổng phát hành và tiêu chí khai tử kích hoạt dựa trên bằng chứng thay vì ý kiến, và một lần chạy hồi quy chặn bất kỳ thay đổi nào làm một chỉ số đi sai hướng.
5. **Điều phối.** Đánh giá ngoại tuyến và trực tuyến liên tục gắn với kết quả kinh doanh; phòng thủ tiêm prompt, tác tử và neo đất được quản trị và quan sát được; tổ chức thường xuyên cho nghỉ hưu, điều chỉnh lại và thu hẹp phạm vi các tính năng LLM, và đổi mô hình khi chất lượng, chi phí và rủi ro dịch chuyển.

## Ý tưởng để thảo luận

- Làm sao bạn quyết định đầu ra nào cần con người rà soát trước khi dùng?
- Tiêu chuẩn của bạn cho "đủ neo đất" trước khi một câu trả lời được hiển thị cho người dùng là gì?
- Làm sao bạn phòng thủ chống tiêm prompt khi nội dung không đáng tin phải đi vào ngữ cảnh?
- Khi nào một tác tử đáng với rủi ro thêm của nó so với thiết kế một lệnh gọi đơn giản hơn?
- Làm sao bạn đánh giá chất lượng chủ quan ở quy mô mà không quá phụ thuộc vào chấm điểm dựa trên mô hình?
- Làm sao bạn giữ prompt dễ bảo trì và nhất quán qua nhiều đội?

## Những điểm cần ghi nhớ

- Độ tin cậy đến từ kỹ thuật bao quanh mô hình: ngữ cảnh, neo đất, lan can và đánh giá.
- RAG neo câu trả lời vào nguồn đáng tin và cho phép trích dẫn cùng xác minh.
- Coi mô hình là một thành phần không đáng tin; xác thực đầu ra và ràng buộc việc dùng công cụ.
- Cho tác tử quyền tối thiểu, vòng lặp có giới hạn và phê duyệt của con người cho hành động hệ quả.
- Đánh giá liên tục ngoại tuyến, trực tuyến và với con người; đó là thứ làm thay đổi an toàn.

## Tài liệu tham khảo và đọc thêm

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (hướng dẫn kỹ thuật).
- Louis-François Bouchard và Louie Peters, *Building LLMs for Production*.
