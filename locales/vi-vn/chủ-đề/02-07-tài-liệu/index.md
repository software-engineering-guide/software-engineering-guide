# 2.7 Tài liệu

## Tổng quan và động lực

[Tài liệu](https://en.wikipedia.org/wiki/Software_documentation) là kiến thức bằng văn bản cho phép mọi người sử dụng, vận hành và thay đổi phần mềm mà không phải ghép nối sự hiểu biết từ riêng mã nguồn. Nó có nhiều thể loại: cách bắt đầu, cách hoàn thành một nhiệm vụ, hệ thống được cấu trúc ra sao, cách ứng phó với một sự cố, một [API](https://en.wikipedia.org/wiki/API) chấp nhận và trả về những gì. Mỗi thể loại phục vụ một người đọc khác nhau với nhu cầu khác nhau. Tài liệu tốt không phải là tùy chọn. Đó là sự khác biệt giữa kiến thức mở rộng được trong một tổ chức lớn và kiến thức chỉ sống trong đầu của vài người.

Với các đội lớn, tài liệu là tuyến phòng thủ tốt nhất của bạn chống lại rủi ro phụ thuộc vào cá nhân then chốt (mối nguy khi kiến thức quan trọng chỉ nằm ở một hoặc vài người) và là cách nhanh nhất để hội nhập người mới. Khi hàng trăm kỹ sư phụ thuộc vào các hệ thống họ không xây dựng, và con người liên tục gia nhập, chuyển đi và rời bỏ, tổ chức chỉ có thể vận hành nếu kiến thức được viết ra và dễ tìm. Các hệ thống không có tài liệu trở nên mong manh: chỉ tác giả của chúng mới có thể thay đổi chúng một cách an toàn, và khi những tác giả đó rời đi, tổ chức mất khả năng bảo trì phần mềm của chính mình. Đó là một trong những thất bại phổ biến và tốn kém nhất ở quy mô lớn.

Bối cảnh doanh nghiệp và chính phủ nâng cao rủi ro hơn nữa. Các hệ thống sống rất lâu, nên tài liệu của bạn phải phục vụ người bảo trì nhiều năm, thậm chí hàng chục năm, sau khi đội ban đầu đã đi. Các chế độ quy định và kiểm toán thường bắt buộc các tài liệu cụ thể làm bằng chứng của sự kiểm soát: hồ sơ kiến trúc, [sổ tay vận hành](https://en.wikipedia.org/wiki/Runbook) (các quy trình vận hành và ứng phó sự cố từng bước) và nhật ký quyết định. Các hệ thống khu vực công được bàn giao giữa các nhà cung cấp hoàn toàn dựa vào tài liệu để mang kiến thức qua ranh giới hợp đồng. Và tài liệu nổi tiếng là dễ mục nát, nên thách thức thực sự là giữ cho nó chính xác khi phần mềm thay đổi.

## Các nguyên tắc chính

- Viết cho một người đọc cụ thể với nhu cầu cụ thể; các loại tài liệu khác nhau phục vụ các mục đích khác nhau.
- Giữ tài liệu gần mã và coi nó như mã (tài liệu như mã).
- Chính xác thắng đầy đủ; một lượng nhỏ tài liệu đáng tin cậy tốt hơn một lượng lớn sai.
- Sinh ra những gì có thể sinh ra; đừng bảo trì thủ công những gì một công cụ có thể tạo ra từ nguồn sự thật.
- Chống lại sự mục nát của tài liệu một cách chủ động; tài liệu lỗi thời tệ hơn không có vì chúng gây hiểu lầm.
- Làm cho tài liệu dễ tìm thấy; kiến thức không tìm được thì thực tế là vắng mặt.
- Ghi lại các quyết định và lý do của chúng, không chỉ trạng thái hiện tại.

## Khuyến nghị

### Áp dụng tài liệu như mã

Giữ tài liệu trong [hệ thống quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control) ngay bên cạnh mã mà nó mô tả, viết bằng ngôn ngữ đánh dấu văn bản thuần, và rà soát nó qua cùng quy trình pull request. Điều đó giữ cho nó có phiên bản, rà soát được và gần mã, để bạn có thể cập nhật cả hai cùng lúc. Hãy công bố nó thông qua một đường ống tự động để phiên bản mới nhất luôn có sẵn. Coi tài liệu như mã mang lại cùng kỷ luật giữ cho mã đáng tin: đánh giá, lịch sử và tự động hóa.

### Cấu trúc nội dung bằng khung Diátaxis

Tổ chức tài liệu thành bốn loại riêng biệt, vì trộn lẫn chúng không phục vụ người đọc nào tốt: hướng dẫn học (hướng đến việc học, cho người mới), hướng dẫn thực hiện (hướng đến nhiệm vụ, cho một mục tiêu cụ thể), tham chiếu (hướng đến thông tin, chính xác và đầy đủ), và giải thích (hướng đến sự hiểu biết, là vì sao và ngữ cảnh). Giữ chúng tách biệt và mọi thứ trở nên dễ viết, dễ điều hướng và dễ bảo trì hơn, vì mỗi trang có một nhiệm vụ rõ ràng và một đối tượng rõ ràng.

### Duy trì các tài liệu vận hành thiết yếu

Cho mỗi kho mã một [README](https://en.wikipedia.org/wiki/README) rõ ràng làm cửa trước của nó: nó là gì, cách dựng và chạy nó, và đi đâu tiếp theo. Viết sổ tay vận hành cho các nhiệm vụ vận hành và ứng phó sự cố, để bất kỳ ai trực ca cũng có thể hành động, không chỉ các chuyên gia. Giữ tài liệu kiến trúc giải thích cấu trúc và các thành phần chính của hệ thống. Và cung cấp tài liệu hội nhập giúp một kỹ sư mới nhanh chóng làm việc hiệu quả. Đây là những tài liệu bạn nhớ nhất khi chúng vắng mặt.

### Sinh tài liệu API và nhật ký thay đổi từ nguồn sự thật

Sinh tài liệu tham chiếu API của bạn từ hợp đồng đọc được bằng máy hoặc chú thích trong mã, để nó không thể trôi khỏi giao diện thực. Giữ một [nhật ký thay đổi](https://en.wikipedia.org/wiki/Changelog), lý tưởng là được sinh từ các commit có cấu trúc hoặc ghi chú phát hành, để người dùng có thể thấy điều gì đã thay đổi giữa các phiên bản. Tự động hóa những thứ này gỡ bỏ khỏi đĩa của bạn loại tài liệu bảo trì thủ công dễ mục nát nhất và giữ cho nó đáng tin cậy.

### Ghi lại các quyết định kiến trúc

Ghi lại các quyết định kiến trúc và thiết kế quan trọng dưới dạng các hồ sơ nhẹ, có ngày nêu bối cảnh, quyết định và hệ quả của nó. Những hồ sơ quyết định này bảo tồn lý do vốn sẽ bị mất, để những người bảo trì tương lai thấy được vì sao hệ thống như vậy thay vì nghi ngờ nó hoặc lặp lại những sai lầm cũ. Chúng đặc biệt có lợi suốt vòng đời dài của các hệ thống doanh nghiệp và chính phủ.

### Chống lại sự mục nát của tài liệu một cách có chủ đích

Coi tài liệu lỗi thời là một khiếm khuyết. Cập nhật tài liệu như một phần của chính thay đổi làm đổi hành vi, và biến đó thành kỳ vọng trong đánh giá. Giao quyền sở hữu để mọi tài liệu quan trọng có người chịu trách nhiệm. Thỉnh thoảng rà soát tài liệu giá trị cao về độ chính xác, cắt tỉa những gì đã lỗi thời, và gỡ bỏ hoặc đánh dấu rõ ràng bất cứ thứ gì bạn không còn tin. Tài liệu mục nát ít nhất là tài liệu sống: được sinh ra hoặc kiểm thử đối chiếu với chính hệ thống.

### Đầu tư vào quản lý kiến thức và khả năng tìm thấy

Làm cho tài liệu dễ tìm thông qua tìm kiếm tốt, điều hướng rõ ràng và một nơi chứa đã biết, để mọi người có thể tìm thứ họ cần mà không phải hỏi ai đó. Đừng để nó phân mảnh qua quá nhiều wiki và công cụ rời rạc. Và hãy thu nhận [kiến thức ngầm](https://en.wikipedia.org/wiki/Tacit_knowledge), sự hiểu biết phi chính thức sống trong các luồng trò chuyện và trong đầu mọi người, vào một dạng bền vững, dễ tìm trước khi nó biến mất.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Tài liệu như mã | Có phiên bản, rà soát được, gần mã; ít mục nát | Đòi hỏi kỷ luật của kỹ sư; kém thân thiện với tác giả không chuyên kỹ thuật |
| Wiki / cơ sở tri thức | Dễ chỉnh sửa; mọi người đều tiếp cận được | Trôi khỏi mã; phân mảnh; mục nát một cách lặng lẽ |
| Tài liệu sinh tự động (API, nhật ký thay đổi) | Luôn chính xác; ít bảo trì | Giới hạn trong những gì nguồn biểu đạt; cần công cụ |
| Giải thích viết tay | Ngữ cảnh và lý do phong phú mà máy không tạo ra được | Tốn nhiều công sức; dễ lỗi thời |
| Cấu trúc Diátaxis | Mục đích rõ ràng cho mỗi trang; dễ điều hướng và bảo trì hơn | Công sức cấu trúc ban đầu; đòi hỏi kỷ luật của tác giả |

Sự đánh đổi trung tâm là công sức so với độ chính xác và độ bền. Tài liệu rẻ nhất để viết, một trang wiki nhanh, cũng là tài liệu dễ mục nát và phân mảnh nhất. Tài liệu bền nhất, được sinh từ nguồn hoặc được rà soát như mã, tốn nhiều kỷ luật hơn ngay từ đầu nhưng vẫn đáng tin. Một quy tắc ngón tay cái tốt: sinh những gì bạn có thể, giữ phần còn lại gần mã và rà soát như mã, và dành phần giải thích viết tay tốn nhiều công sức cho lý do mà chỉ con người mới cung cấp được.

## Câu hỏi để thảo luận với đội của bạn

1. **Các tài liệu của bạn có được tách theo nhu cầu người đọc không, hay hướng dẫn học, tham chiếu và giải thích bị trộn lẫn trên một trang?** Chương này khuyến nghị sự tách của Diátaxis thành hướng dẫn học, hướng dẫn thực hiện, tham chiếu và giải thích, và liệt kê việc trộn lẫn các loại là một phản mẫu không phục vụ người đọc nào tốt. Ở quy mô lớn, một người mới đang học hệ thống và một kỹ sư trực ca đang tìm một sự kiện chính xác cần những trang khác nhau, và một trang trộn lẫn duy nhất làm chậm cả hai. Hãy mang tín hiệu: chọn những tài liệu được xem nhiều nhất của bạn và kiểm tra xem mỗi tài liệu có một nhiệm vụ rõ ràng và một đối tượng rõ ràng không. Tái cấu trúc những trường hợp tệ nhất thành các loại riêng biệt, để mỗi trang dễ viết, dễ điều hướng và dễ giữ cập nhật hơn. Cấu trúc đó là thứ khiến tài liệu bảo trì được khi tổ chức lớn lên.

2. **Bạn có ghi lại các quyết định kiến trúc quan trọng cùng lý do của chúng, hay chỉ trạng thái hiện tại?** Chương này khuyến nghị các hồ sơ quyết định nhẹ, có ngày nêu bối cảnh, quyết định và hệ quả, và lưu ý rằng chúng có lợi nhất suốt vòng đời dài của các hệ thống doanh nghiệp và chính phủ. Không có chúng, một người bảo trì nhiều năm sau không thể thấy vì sao hệ thống như vậy, nên họ nghi ngờ những lựa chọn đúng đắn hoặc lặp lại những sai lầm cũ. Hãy mang một quyết định khó gần đây mà lý do của nó hiện chỉ nằm trong một luồng trò chuyện hoặc trí nhớ của ai đó làm tín hiệu cụ thể. Hãy áp dụng một định dạng hồ sơ quyết định ngắn và biến việc viết một hồ sơ thành một phần của bất kỳ thay đổi thiết kế quan trọng nào. Lý do chính là kiến thức mà chỉ con người mới cung cấp được và mục nát nhanh nhất khi không được viết ra.

3. **Bất kỳ kỹ sư trực ca nào cũng có thể ứng phó với một sự cố chỉ từ sổ tay vận hành của bạn không, mà không phải gọi người đã xây dựng hệ thống?** Chương này gọi sổ tay vận hành là tài liệu vận hành thiết yếu để bất kỳ ai trực ca cũng có thể hành động, không chỉ các chuyên gia, và mô tả một đội chính phủ chỉ có thể thừa kế một hệ thống vì sổ tay vận hành đã mang kiến thức qua ranh giới hợp đồng. Rủi ro phụ thuộc vào cá nhân then chốt là thất bại mà điều này phòng ngừa: khi chuyên gia duy nhất không liên lạc được hoặc đã đi, một quy trình khôi phục không có tài liệu biến một sự cố thường lệ thành một vụ ngừng hoạt động. Hãy mang bằng chứng: lấy một sự cố gần đây và kiểm tra xem riêng sổ tay vận hành có giải quyết được nó không. Viết và kiểm thử sổ tay vận hành cho các quy trình mà mọi người e ngại, và coi một sổ tay vận hành không thể tự đứng vững là một khiếm khuyết. Đó là sự khác biệt giữa một lần khôi phục lúc 2 giờ sáng và một lần leo thang lúc 2 giờ sáng.

4. **Những tài liệu tham chiếu API và nhật ký thay đổi nào của bạn được sinh từ nguồn sự thật, và những cái nào vẫn được bảo trì thủ công và âm thầm trôi dạt?** Chương này bảo bạn sinh tài liệu tham chiếu từ hợp đồng đọc được bằng máy hoặc chú thích trong mã để nó không thể lệch khỏi giao diện thực, và liệt kê việc bảo trì thủ công nội dung có thể sinh ra là một phản mẫu. Với một đội lớn, một tài liệu API viết tay chậm hơn giao diện thực còn tệ hơn không có: mọi người dùng tin vào nó đều viết một tích hợp hỏng, và thất bại hiện ra xa trang lỗi thời đã gây ra nó. Hãy mang tín hiệu cụ thể: lấy mẫu một nhúm giao diện được dùng nhiều nhất của bạn và đối chiếu tài liệu tham chiếu đã công bố với hợp đồng thực để xem mỗi cái đã trôi bao xa. Ở nơi bạn thấy sự trôi dạt, hãy nối tài liệu tham chiếu vào bản dựng để nó tái sinh trên mỗi thay đổi, và loại bỏ bản giữ tay. Trong bối cảnh doanh nghiệp và chính phủ, nơi các giao diện được sử dụng qua các đội, nhà cung cấp và ranh giới hợp đồng mà bạn không bao giờ thấy, một tham chiếu được sinh tự động có thẩm quyền thường là thứ duy nhất ngăn người tích hợp xây dựng dựa trên hư cấu.

5. **Ai sở hữu từng tài liệu giá trị cao, và hôm nay bạn sẽ nhận ra thế nào nếu một tài liệu đã lỗi thời?** Chương này coi tài liệu lỗi thời là một khiếm khuyết và cảnh báo rằng các tài liệu không có chủ sở hữu mục nát vì việc cập nhật chúng không phải việc của ai, trong khi tài liệu lỗi thời được trình bày như hiện hành phá hủy niềm tin vào mọi tài liệu của bạn. Ở quy mô lớn, mối nguy không phải một trang sai đơn lẻ mà là sự xói mòn chậm rãi của niềm tin: một khi người đọc bị bỏng bởi hướng dẫn lỗi thời, họ ngừng tin cả kho tài liệu và quay lại làm phiền mọi người. Hãy mang một bản đồ quyền sở hữu của các tài liệu quan trọng nhất và một câu trả lời trung thực về cách sự mục nát được phát hiện, bằng chu kỳ rà soát, sinh tự động, kiểm thử đối chiếu với hệ thống, hay thuần túy may rủi. Hãy giao một chủ sở hữu được nêu tên cho mọi tài liệu quan trọng, và ưu tiên tài liệu sống được sinh ra hoặc kiểm thử để sự lỗi thời hiện ra một cách cơ học thay vì qua một người đọc ngượng ngùng. Với các hệ thống doanh nghiệp và chính phủ tồn tại lâu hơn đội ban đầu, tài liệu không có chủ sở hữu là một khoản nợ mà kiểm toán viên hoặc nhà cung cấp kế thừa cuối cùng sẽ tính cho bạn.

6. **Tài liệu của bạn dễ tìm đến mức nào, và bao nhiêu kiến thức quan trọng vẫn chỉ sống trong các luồng trò chuyện và trong đầu mọi người?** Chương này nói kiến thức không tìm được thì thực tế là vắng mặt, cảnh báo không phân mảnh tài liệu qua quá nhiều wiki và công cụ rời rạc, và thúc giục bạn thu nhận kiến thức ngầm vào dạng bền vững, dễ tìm trước khi nó biến mất. Trong một tổ chức lớn, cùng một sự kiện thường bị khám phá lại, hỏi lại và trả lời lại cả trăm lần vì không ai tìm được nơi nó đã được viết, và mỗi lần có người ra đi mang theo ngữ cảnh không thể thay thế. Hãy mang bằng chứng: đếm xem bạn duy trì bao nhiêu nơi chứa tài liệu riêng biệt, thử tìm ba sự kiện quan trọng chỉ bằng tìm kiếm, và ghi nhận nơi các câu trả lời thực sự hóa ra nằm trong trí nhớ của ai đó hoặc một tin nhắn bị chôn vùi. Hãy hợp nhất về một nơi chứa đã biết với tìm kiếm thực sự và điều hướng rõ ràng, và biến việc thu nhận kiến thức ngầm thành một phần thường lệ của công việc thay vì một cuộc giải cứu anh hùng. Trong bối cảnh khu vực công và thuê ngoài nhiều, nơi các hệ thống truyền giữa các nhà cung cấp và đội theo hợp đồng, kiến thức bằng văn bản dễ tìm là thứ duy nhất sống sót qua việc bàn giao.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không còn nguồn vốn dư, hãy chỉ lập tài liệu những gì một sự cố lúc 2 giờ sáng hoặc một nhân viên mới thực sự cần: một README thực sự cho mỗi dịch vụ, một sổ tay vận hành đã kiểm thử cho quy trình triển khai-và-khôi phục mà ai cũng sợ, và vài ghi chú có ngày về các quyết định mà bạn sẽ quên. Hãy sinh tài liệu API từ hợp đồng để bạn không bao giờ phải bảo trì thủ công. Cưỡng lại việc xây dựng một nền tảng tài liệu; một thư mục có phiên bản các ngôn ngữ đánh dấu bên cạnh mã là đủ cho đến khi bạn cảm thấy nỗi đau thực sự.

**Doanh nghiệp nhỏ.** Không có người viết kỹ thuật và ngân sách eo hẹp, hãy dựa vào tài liệu mà công cụ của bạn đã sinh ra và vào tài liệu như mã nhẹ nhàng thay vì một chương trình có nhân sự. Đóng khung lựa chọn như mua hay xây: ưu tiên các nền tảng tự tạo tài liệu tham chiếu hiện hành và cơ sở tri thức có thể tìm kiếm hơn một wiki mà bạn phải chăm sóc bằng tay. Hãy dành công sức khan hiếm cho hai hoặc ba tài liệu mà sự vắng mặt của chúng sẽ dừng doanh nghiệp, và để một trang sai hoặc thiếu là cú hích để sửa quyền sở hữu.

**Doanh nghiệp lớn.** Qua nhiều đội, vấn đề là nhất quán và khả năng tìm thấy: một đường ống tài liệu như mã dùng chung, một cấu trúc chung như Diátaxis, tham chiếu API và nhật ký thay đổi được sinh tự động, và hồ sơ quyết định được áp dụng như nhau ở mọi nơi để kiến thức không phân mảnh qua hàng chục wiki. Giao quyền sở hữu cho mọi tài liệu giá trị cao và đo độ chính xác, không chỉ sự hiện diện. Hãy coi hồ sơ kiến trúc, sổ tay vận hành và nhật ký quyết định là bằng chứng kiểm toán, và chuẩn hóa cách chúng được tạo ra để một cuộc rà soát kiểm soát tìm thấy một dấu vết có tài liệu, có thể bảo vệ thay vì một cuộc xoay xở.

**Chính phủ.** Quy tắc mua sắm và trách nhiệm giải trình trước công chúng khiến tài liệu trở thành sản phẩm bàn giao, không phải phép lịch sự. Hãy viết tài liệu kiến trúc, sổ tay vận hành và hồ sơ quyết định vào hợp đồng như các hiện vật bắt buộc, được rà soát độ chính xác để kiến thức sống sót qua một lần chuyển nhà cung cấp và một hệ thống có thể được vận hành bởi bất kỳ ai thừa kế nó. Yêu cầu bất kỳ người vận hành được ủy quyền nào cũng có thể ứng phó với sự cố chỉ từ sổ tay vận hành, và giữ nhật ký quyết định như một hồ sơ công khai minh bạch về lý do các lựa chọn được đưa ra. Tài liệu mỏng ở đây không phải là sự bất tiện riêng tư; nó trở thành việc dịch ngược tốn kém do người đóng thuế tài trợ.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp năm người viết một README thực sự cho mỗi dịch vụ và một sổ tay vận hành ngắn cho quy trình triển khai-và-khôi phục mà ai cũng sợ, để một sự cố lúc 2 giờ sáng không phụ thuộc vào việc đánh thức người sáng lập duy nhất biết hệ thống. Họ sinh tài liệu API từ hợp đồng thay vì viết tay, và ghi vài ghi chú có ngày giải thích vì sao họ chọn cơ sở dữ liệu và cách tiếp cận xác thực. Nó vẫn nhẹ, nhưng có nghĩa là những người được tuyển thứ sáu và thứ bảy hội nhập từ tài liệu thay vì làm phiền mọi người.

**Doanh nghiệp lớn.** Một công ty phần mềm lớn giữ toàn bộ tài liệu của mình trong cùng các kho mã với mã, viết bằng ngôn ngữ đánh dấu và được rà soát trong pull request ngay cạnh các thay đổi chúng mô tả. Tài liệu tham chiếu API được sinh từ hợp đồng dịch vụ, nên chúng không bao giờ trôi dạt. Nhật ký thay đổi được sinh từ các commit có cấu trúc, và hồ sơ quyết định kiến trúc bảo tồn lý do đằng sau các lựa chọn lớn. Một trang tài liệu được công bố tự động dựng trên mỗi lần hợp nhất. Kỹ sư mới nhanh chóng làm việc hiệu quả vì hướng dẫn hội nhập và sổ tay vận hành luôn hiện hành và dễ tìm, và kỹ sư trực ca dựa vào sổ tay vận hành thay vì gọi các tác giả gốc.

**Chính phủ.** Một cơ quan quốc gia thừa kế một hệ thống từ một nhà thầu sắp rời đi, hoàn toàn phụ thuộc vào tài liệu để mang kiến thức qua ranh giới hợp đồng. Vì nhà cung cấp trước đã duy trì tài liệu kiến trúc, sổ tay vận hành và hồ sơ quyết định như các sản phẩm bàn giao bắt buộc, đội mới có thể vận hành và sửa đổi hệ thống mà không cần các tác giả gốc. Ở nơi tài liệu mỏng, cơ quan đối mặt với việc dịch ngược tốn kém. Trải nghiệm đó thúc đẩy một chính sách mới: tài liệu là sản phẩm bàn giao theo hợp đồng, được rà soát độ chính xác thay vì bị coi là chuyện nghĩ đến sau, và sổ tay vận hành phải cho phép bất kỳ người vận hành được ủy quyền nào ứng phó với sự cố.

## Luận chứng kinh doanh: động lực, ROI và TCO

Tài liệu hoàn vốn cho bạn bằng thời gian hội nhập ngắn hơn, ít rủi ro phụ thuộc vào cá nhân then chốt hơn, ứng phó sự cố nhanh hơn, và chi phí thay đổi thấp hơn trong suốt vòng đời của một hệ thống. Kỹ sư mới đạt năng suất trong vài ngày thay vì vài tuần, nhân viên trực ca giải quyết sự cố từ sổ tay vận hành thay vì leo thang, người bảo trì thay đổi một hệ thống một cách tự tin nhiều năm sau khi nó được xây dựng: đây là những khoản tiết kiệm lớn, lặp lại, cộng dồn qua một tổ chức lớn và vòng đời hệ thống dài.

Tài liệu tốn gì? Công sức soạn thảo và bảo trì. Việc *không* lập tài liệu tốn gì? Bạn trả liên tục: trong hội nhập chậm, câu hỏi lặp lại, nút thắt cá nhân then chốt, phục hồi sự cố chậm hơn, và, ở thái cực, các hệ thống không ai có thể thay đổi an toàn, buộc phải viết lại đắt đỏ hoặc dịch ngược. Trong các tình huống chuyển nhà cung cấp và kiểm toán, tài liệu thiếu có thể mang chi phí hợp đồng và tuân thủ trực tiếp. Để thuyết phục ban lãnh đạo, hãy đặt con số lên thời gian hội nhập, thời gian ứng phó sự cố, và bao nhiêu kiến thức quan trọng nằm trong đầu từng cá nhân. Rồi đóng khung tài liệu như mã và việc sinh tự động như cách để có tài liệu bền vững mà không có gánh nặng bảo trì tương ứng. Và nhấn mạnh rằng tài liệu không chính xác là một khoản nợ, nên khoản đầu tư phải bao gồm việc giữ nó cập nhật.

## Phản mẫu và cạm bẫy

- **Tài liệu lỗi thời được trình bày như hiện hành:** gây hiểu lầm cho người đọc và phá hủy niềm tin vào mọi tài liệu.
- **Wiki viết một lần:** các trang được tạo ra và không bao giờ được cập nhật, lặng lẽ trôi khỏi thực tế.
- **Phân mảnh tài liệu:** kiến thức rải rác qua nhiều công cụ và wiki nên không thể tìm thấy gì.
- **Trộn các loại tài liệu:** hướng dẫn học, tham chiếu và giải thích lẫn lộn trên một trang, không phục vụ người đọc nào tốt.
- **Bảo trì thủ công nội dung có thể sinh ra:** tài liệu API viết tay chắc chắn sẽ lệch khỏi giao diện thực.
- **Kiến thức truyền miệng:** sự hiểu biết quan trọng chỉ được giữ trong đầu người và lịch sử trò chuyện, mất đi khi họ rời đi.
- **Tài liệu như chuyện nghĩ đến sau:** viết ở cuối, nếu có, thay vì cùng với thay đổi.
- **Không có chủ sở hữu:** các tài liệu không có chủ sở hữu chịu trách nhiệm mục nát vì việc cập nhật chúng không phải việc của ai.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu.** Tài liệu thưa thớt, rải rác và lỗi thời, và kiến thức nằm trong đầu mọi người. Những gì tồn tại được viết một lần và không bao giờ được chạm lại, nên một sự cố ngừng hoạt động hoặc một lần ra đi đồng nghĩa với việc dịch ngược hệ thống.
- **Mức 2, Phát triển.** Các tài liệu chính tồn tại, như README và một vài sổ tay vận hành, nhưng được bảo trì không nhất quán và khó tìm. Một số đội lập tài liệu tốt và những đội khác hầu như không, và không có kỳ vọng chung về một kho mã nên mang gì hoặc nên nằm ở đâu.
- **Mức 3, Chuẩn hóa.** Tài liệu như mã là chuẩn mực trong tổ chức: một cấu trúc chung như Diátaxis, tham chiếu API và nhật ký thay đổi được sinh tự động, hồ sơ quyết định, và kỳ vọng trong đánh giá rằng tài liệu thay đổi cùng với mã mà chúng mô tả. Mọi tài liệu giá trị cao có một chủ sở hữu được nêu tên, và có một nơi chứa đã biết với tìm kiếm thực sự.
- **Mức 4, Quản lý.** Tài liệu được đo lường, không chỉ hiện diện. Bạn theo dõi độ bao phủ của các tài liệu thiết yếu, tỷ lệ thay đổi tài liệu so với tỷ lệ thay đổi mã, thời gian hội nhập, việc giải quyết sự cố chỉ từ sổ tay vận hành, và độ mới so với một ngưỡng lỗi thời xác định, và bạn xem xét các chỉ số đó so với đường cơ sở. Sự mục nát được bắt một cách cơ học thông qua sinh tự động, kiểm thử đối chiếu với hệ thống, và kiểm tra liên kết cùng độ chính xác, và các trang lỗi thời được đánh dấu hoặc cắt tỉa dựa trên bằng chứng thay vì ngẫu nhiên.
- **Mức 5, Điều phối.** Tài liệu được cải tiến liên tục và tích hợp trong toàn tổ chức: sống, phần lớn được sinh ra hoặc kiểm thử đối chiếu với hệ thống, có chủ sở hữu, dễ tìm và thích ứng. Các chỉ số phản hồi lại nơi bạn đầu tư, kiến thức ngầm được thu nhận như một phần thường lệ của công việc, và kho tài liệu được cân bằng lại và cắt tỉa chủ động khi hệ thống, đội và người đọc thay đổi.

## Ý tưởng để thảo luận

- Tài liệu nào, nếu biến mất vào ngày mai, sẽ gây hại nhất cho tổ chức của bạn, và hiện nó có tồn tại và được giữ cập nhật không?
- Làm thế nào bạn biến việc cập nhật tài liệu thành một phần tự nhiên của việc thay đổi mã thay vì một việc vặt riêng?
- Bạn có thể thay tài liệu viết tay bằng tài liệu sinh tự động gắn với nguồn sự thật ở đâu?
- Làm thế nào bạn đo xem tài liệu của mình có chính xác và được dùng, không chỉ hiện diện?
- Các trợ lý AI nên thay đổi cách bạn viết, bảo trì và tìm kiếm tài liệu như thế nào, và chúng có thể đưa vào nội dung hợp lý nhưng sai ở đâu?
- Làm thế nào bạn thu nhận kiến thức ngầm trước khi những người nắm giữ nó rời đi?

## Những điểm cần ghi nhớ

- Coi tài liệu như mã: có phiên bản, được rà soát, gần nguồn và được công bố tự động.
- Cấu trúc nội dung theo nhu cầu người đọc bằng hướng dẫn học, hướng dẫn thực hiện, tham chiếu và giải thích.
- Duy trì những thiết yếu giá trị cao: README, sổ tay vận hành, tài liệu kiến trúc, hội nhập và hồ sơ quyết định.
- Sinh tài liệu API và nhật ký thay đổi để chúng không thể trôi khỏi nguồn sự thật.
- Chống lại sự mục nát bằng quyền sở hữu, kỳ vọng đánh giá và cắt tỉa; tài liệu không chính xác tệ hơn không có.

## Tài liệu tham khảo và đọc thêm

- Daniele Procida, khung tài liệu *Diátaxis*
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* và hướng dẫn Season of Docs (như các ví dụ tham chiếu)
- Michael Nygard, *Documenting Architecture Decisions* (hồ sơ quyết định kiến trúc)
- Andrew Hunt và David Thomas, *The Pragmatic Programmer* (về kiến thức và tài liệu)
- *Keep a Changelog* (như một quy ước tham chiếu)
