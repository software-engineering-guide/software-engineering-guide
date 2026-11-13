# 5.3 Khả năng tiếp cận

## Tổng quan và động lực

[Khả năng tiếp cận](https://en.wikipedia.org/wiki/Accessibility) (thường viết tắt là "a11y") là thực hành xây phần mềm mà người khuyết tật có thể cảm nhận, hiểu, điều hướng và sử dụng. Điều đó bao gồm những người mù hay thị lực kém, người điếc hay nghe kém, người có suy giảm vận động, người có khác biệt về nhận thức hay học tập, và người đối mặt giới hạn tạm thời hay theo tình huống như gãy tay, ánh nắng chói, hay một căn phòng ồn ào. Khoảng một trong năm người có khuyết tật, và mọi người đều hưởng lợi từ thiết kế tiếp cận được vào lúc nào đó. Đây không phải một sự điều chỉnh ngách. Nó là đường cơ sở của chất lượng.

Với các đội lớn, khả năng tiếp cận phải được xây vào hệ thống, không để cho thiện chí cá nhân. Khi nhiều đội phát hành vào một sản phẩm, một thành phần không tiếp cận được đơn lẻ (một trường biểu mẫu không nhãn, một chỉ báo trạng thái chỉ dùng màu, một bẫy bàn phím trong hộp thoại) có thể khóa người dùng khuyết tật ra khỏi cả một hành trình. Xây khả năng tiếp cận vào thành phần dùng chung, token thiết kế, đường ống kiểm thử và định nghĩa hoàn thành là cách duy nhất để làm nó đáng tin ở quy mô lớn. Trang bị bổ sung sau sự việc thì tốn kém và dễ sai. Thiết kế nó vào thì rẻ và bền.

Với chính phủ, khả năng tiếp cận là yêu cầu pháp lý và nghĩa vụ công dân, không phải điều dễ chịu. Dịch vụ công phải phục vụ mọi thành viên của công chúng, và công dân khuyết tật thường không có nhà cung cấp thay thế: nếu trang web chính phủ không tiếp cận được, họ không thể nhận trợ cấp, giấy phép, hay bỏ phiếu theo cách khác. Luật và tiêu chuẩn khắp thế giới biến khả năng tiếp cận thành bắt buộc với các cơ quan công, và ngày càng với cả khu vực tư. Chương này coi khả năng tiếp cận là ba thứ cùng lúc: nghĩa vụ pháp lý, nghĩa vụ đạo đức, và đơn giản là thiết kế tốt.

*Xem thêm:* chương 5.2 (thiết kế UI và hệ thống thiết kế), chương 5.6 (kỹ thuật giao diện người dùng), và chương 5.1 (nền tảng UX).

## Các nguyên tắc chính

- Khả năng tiếp cận là thuộc tính chất lượng cơ sở, như bảo mật và hiệu năng, không phải tính năng tùy chọn.
- Các nguyên tắc POUR: giao diện phải Cảm nhận được, Vận hành được, Hiểu được và Vững chắc.
- [HTML ngữ nghĩa](https://en.wikipedia.org/wiki/Semantic_HTML) trước; chỉ dùng [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) để lấp các khoảng trống thực sự, không bao giờ thay cho phần tử bản địa.
- Mọi thứ dùng được bằng chuột phải dùng được chỉ bằng bàn phím.
- Không truyền đạt thông tin chỉ bằng màu, hình dạng hay vị trí.
- Công cụ tự động chỉ bắt một phần các vấn đề; kiểm thử thủ công và bằng [công nghệ hỗ trợ](https://en.wikipedia.org/wiki/Assistive_technology) là thiết yếu.
- Thiết kế tiếp cận được là thiết kế tốt hơn cho mọi người (["hiệu ứng vỉa hè dốc,"](https://en.wikipedia.org/wiki/Curb_cut) nơi các tính năng xây cho người khuyết tật mang lợi cho mọi người dùng).
- Thiết kế và kiểm thử cùng người khuyết tật, không chỉ cho họ.

## Khuyến nghị

### Thiết kế và xây theo WCAG, nhắm vào tiêu chuẩn hiện hành

[Hướng dẫn Khả năng Tiếp cận Nội dung Web](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) là tham chiếu quốc tế. WCAG 2.1 và 2.2 được tổ chức dưới bốn nguyên tắc POUR, với các tiêu chí thành công kiểm thử được ở các mức phù hợp A, AA và AAA. Hãy nhắm vào Mức AA làm đường cơ sở; đó là mức hầu hết luật tham chiếu. WCAG 2.2 thêm tiêu chí cho khả năng nhìn thấy tiêu điểm, kích thước mục tiêu, và giảm tải nhận thức. WCAG 3.0 là người kế nhiệm đang nổi lên, được cấu trúc khác và vẫn đang phát triển. Hãy theo dõi nó, nhưng hôm nay hãy xây theo 2.2 AA. Hãy coi các hướng dẫn là sàn, không phải trần: đạt mọi tiêu chí không bảo đảm một trải nghiệm thực sự dùng được.

### Dùng HTML ngữ nghĩa và ARIA đúng

Các phần tử HTML bản địa (nút, liên kết, điều khiển biểu mẫu, tiêu đề, danh sách, mốc) đi kèm ngữ nghĩa khả năng tiếp cận tích hợp, hành vi bàn phím và hỗ trợ công nghệ hỗ trợ. Hãy dùng chúng trước. Chỉ với tới vai trò, trạng thái và thuộc tính ARIA (Ứng dụng Internet Phong phú Tiếp cận được) để mô tả các widget tùy chỉnh mà HTML không biểu đạt được, và theo Thực hành Soạn thảo ARIA. Quy tắc đầu tiên của ARIA đơn giản: đừng dùng ARIA nếu một phần tử bản địa làm được. ARIA sai còn tệ hơn không có: nó chủ động đánh lừa [trình đọc màn hình](https://en.wikipedia.org/wiki/Screen_reader). Hãy cho trang một cấu trúc tiêu đề logic, nhãn có ý nghĩa, văn bản thay thế cho hình ảnh, phụ đề và bản chép lời cho phương tiện, và một liên kết lập trình được giữa mỗi nhãn và điều khiển của nó.

### Bảo đảm khả năng vận hành bằng bàn phím và công nghệ hỗ trợ

Mọi phần tử tương tác phải với tới và vận hành được chỉ bằng bàn phím, theo thứ tự logic, với chỉ báo tiêu điểm hiển thị rõ ràng. Tránh bẫy bàn phím. Quản lý tiêu điểm có chủ đích khi nội dung thay đổi: chuyển tiêu điểm đến một hộp thoại khi nó mở, trả lại khi hộp thoại đóng, và thông báo cập nhật động qua vùng sống. Kiểm thử với công nghệ hỗ trợ thật, bao gồm trình đọc màn hình trên máy tính và di động, phóng đại màn hình, điều khiển bằng giọng nói, và truy cập công tắc. Và tôn trọng tùy chọn của người dùng như giảm chuyển động và tăng độ tương phản.

### Kiểm thử bằng công cụ tự động, rà soát thủ công và người dùng thật

Bộ quét khả năng tiếp cận tự động có giá trị, và chúng nên chạy trong đường ống trên mọi thay đổi. Nhưng các nghiên cứu liên tục cho thấy chúng chỉ bắt một thiểu số vấn đề thực, khoảng một phần ba. Phần còn lại cần phán đoán của con người: đi qua bằng bàn phím, kiểm thử bằng trình đọc màn hình, kiểm tra độ tương phản, và hỏi liệu nội dung có thực sự hiểu được. Quan trọng nhất, hãy đưa người khuyết tật vào kiểm thử khả dụng. Xây tiêu chí chấp nhận khả năng tiếp cận vào định nghĩa hoàn thành, để vấn đề bị bắt theo từng câu chuyện thay vì trong một cuộc kiểm toán trước ra mắt.

### Biến khả năng tiếp cận thành tổ chức, không phải anh hùng

Hãy nướng khả năng tiếp cận vào hệ thống thiết kế để thành phần được phát hành tiếp cận được theo mặc định. Cung cấp đào tạo để nhà thiết kế, kỹ sư, tác giả nội dung và quản lý sản phẩm mỗi người biết họ chịu trách nhiệm điều gì. Thiết lập một tiêu chuẩn khả năng tiếp cận, một chủ sở hữu hay trung tâm xuất sắc, và một quy trình khắc phục. Công bố một tuyên bố khả năng tiếp cận và cho người dùng cách báo cáo rào cản. Và mua sắm một cách tiếp cận được: yêu cầu nhà cung cấp và thành phần bên thứ ba phải tuân thủ, và cung cấp bằng chứng (như một báo cáo phù hợp khả năng tiếp cận).

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Xây khả năng tiếp cận vào từ đầu | Rẻ nhất, bền, tốt hơn cho mọi người | Cần đào tạo và kỷ luật ban đầu |
| Trang bị bổ sung / khắc phục sau | Trì hoãn công sức, mở đường cho ra mắt nhanh | Đắt hơn nhiều, mong manh, rủi ro pháp lý trong thời gian chờ |
| Chỉ kiểm thử tự động | Nhanh, rẻ, bắt hồi quy trong CI | Bỏ sót ~hai phần ba vấn đề; tự tin giả |
| Kiểm thử thủ công + công nghệ hỗ trợ | Bắt rào cản khả dụng thực | Chậm hơn, cần người kiểm thử và thiết bị lành nghề |
| Kiểm thử với người dùng khuyết tật | Sự thật nền tảng về trải nghiệm thực | Công sức và chi phí tuyển người, phải làm một cách tôn trọng |

Đánh đổi trung tâm là kỷ luật ban đầu so với chi phí bị trì hoãn. Khả năng tiếp cận được xây vào thì rẻ và cải thiện chất lượng cho mọi người; khả năng tiếp cận trang bị bổ sung dưới áp lực pháp lý thì đắt, không đầy đủ và căng thẳng. Về lâu dài không có đánh đổi thực nào đối với "tốc độ": phần mềm không tiếp cận được đơn giản là không hoạt động với một phần năm người dùng của bạn. Đó là một khiếm khuyết, không phải một khoản tiết kiệm.

## Câu hỏi để thảo luận với đội của bạn

1. **Hồi quy khả năng tiếp cận có làm hỏng bản dựng của chúng ta như một bài kiểm thử hỏng không, và nếu không, vì sao?** Bộ quét tự động chỉ bắt khoảng một phần ba vấn đề, nhưng những cái chúng bắt (thiếu nhãn, lỗi độ tương phản, điều khiển không nhãn) thì rẻ để bắt trong CI và đắt để tìm trong một cuộc kiểm toán trước ra mắt. Coi một hồi quy là thất bại bản dựng là thứ chuyển khả năng tiếp cận từ nỗ lực anh hùng cá nhân sang thuộc tính hệ thống đáng tin cậy, điều duy nhất hiệu quả khi nhiều đội phát hành vào một sản phẩm. Hãy quyết định kiểm tra nào là chặn, cái nào là khuyến nghị, và ai có thể ghi đè một thất bại. Hãy mang kết quả bộ quét hiện tại và định nghĩa hoàn thành của bạn đến cuộc họp. Nếu tiêu chí khả năng tiếp cận không được viết vào định nghĩa hoàn thành theo từng câu chuyện, chúng sẽ bị hạ ưu tiên ngay khoảnh khắc hạn chót siết lại.

2. **Quy tắc của chúng ta cho widget tùy chỉnh là gì, và ai rà soát ARIA trước khi nó được phát hành?** Các phần tử HTML bản địa đi kèm hành vi bàn phím và hỗ trợ công nghệ hỗ trợ miễn phí, và ARIA sai còn tệ hơn không có vì nó chủ động đánh lừa trình đọc màn hình. Hãy thống nhất rằng HTML ngữ nghĩa là mặc định và bất kỳ widget tùy chỉnh nào (một dropdown, bộ chọn ngày, hay hộp thoại riêng) đòi hỏi một lượt đi qua bằng bàn phím và trình đọc màn hình trước khi hợp nhất, theo Thực hành Soạn thảo ARIA. Điều này quan trọng nhất với các thành phần tương tác mà nhiều đội tái sử dụng, vì một hộp thoại hỏng với bẫy bàn phím có thể khóa người dùng khuyết tật ra khỏi cả một hành trình. Hãy mang danh sách widget tùy chỉnh của bạn và hỏi cái nào đã được kiểm thử bằng một trình đọc màn hình thực. Bất kỳ cái nào chưa là khoản nợ ẩn trong mã dùng chung.

3. **Chính sách của chúng ta về lớp phủ khả năng tiếp cận là gì, và có ai tin chúng là bản sửa thực không?** Lớp phủ được quảng cáo là một tập lệnh một dòng làm một trang phù hợp, và chúng hấp dẫn khi áp lực pháp lý đến và hạn chót lù lù. Chúng không mang lại sự phù hợp thực sự, chúng có thể làm tệ trải nghiệm cho người dùng công nghệ hỗ trợ, và với chính phủ chúng để nghĩa vụ pháp lý nền tảng không được đáp ứng. Hãy quyết định tường minh rằng bạn sẽ đầu tư vào đánh dấu ngữ nghĩa, hỗ trợ bàn phím và kiểm thử với người khuyết tật thay vì mua một widget che đậy vấn đề. Hãy mang chi phí của một đăng ký lớp phủ và so sánh với việc xây khả năng tiếp cận vào thành phần và đường ống của bạn một lần. Đóng khung điều này sớm ngăn một quyết định mua sắm hoảng loạn sau này tốn tiền mà không sửa gì.

4. **Người khuyết tật có là một phần của thiết kế và kiểm thử của chúng ta không, hay chúng ta vẫn đang thiết kế cho một người dùng tưởng tượng do mình bịa ra?** Bộ quét tự động và thậm chí các cuộc kiểm toán chuyên gia cho bạn biết đánh dấu có phù hợp không; chúng không cho bạn biết một người dùng mù có thực sự hoàn thành được thanh toán của bạn hay một người có khuyết tật nhận thức có hiểu được thông báo lỗi của bạn không. Đưa người tham gia khuyết tật vào là nguồn sự thật nền tảng duy nhất, và nó thay đổi những gì bạn xây, nhưng nó nêu ra những câu hỏi thật về cách bạn tuyển công bằng, cách bạn đền bù thời gian của họ, và cách bạn tránh coi một người tham gia là người phát ngôn cho mọi khuyết tật. Hãy mang danh sách nghiên cứu hiện tại của bạn, các thực hành tuyển và chi trả, và một con số trung thực về bao nhiêu nghiên cứu trong năm qua có người tham gia khuyết tật. Với một tổ chức lớn, một nhóm thường trực với đền bù công bằng và độ bao phủ qua nhu cầu thị giác, thính giác, vận động và nhận thức là thứ biến điều này từ một cử chỉ một lần thành một đầu vào đáng tin cậy; trong chính phủ, việc đưa công chúng bạn phục vụ vào thường là một phần của nghĩa vụ pháp lý và công dân, không phải điều dễ chịu tùy chọn.

5. **Khi chúng ta mua hoặc nhúng một thành phần bên thứ ba, chúng ta có đòi bằng chứng về khả năng tiếp cận không, và ai kiểm tra?** Phần lớn những gì được phát hành trong một sản phẩm lớn không được viết nội bộ: một bộ chọn ngày từ một thư viện, một widget thanh toán trong iframe, một gói biểu đồ, cả một mô-đun SaaS. Một thành phần nhúng không tiếp cận được đơn lẻ có thể làm hỏng cả một hành trình bất kể mã của bạn sạch đến đâu, và một khi đã nối vào, thay thế nó tốn kém. Hãy quyết định rằng khả năng tiếp cận là yêu cầu mua sắm, rằng nhà cung cấp phải cung cấp một báo cáo phù hợp khả năng tiếp cận (một tài liệu như VPAT nêu một sản phẩm đo với WCAG thế nào), và rằng một người kỹ thuật xác thực tuyên bố thay vì chỉ lưu hồ sơ. Hãy mang bản kiểm kê các thành phần bên thứ ba của bạn và hỏi cái nào có bằng chứng phù hợp hiện hành, đáng tin. Trong mua sắm doanh nghiệp và chính phủ, hãy viết sự phù hợp WCAG 2.2 AA và quyền khắc phục vào hợp đồng, vì một lời hứa đưa ra trước khi ký rẻ hơn nhiều để thực thi so với rào cản phát hiện sau khi đưa vào hoạt động.

6. **Mức phù hợp mục tiêu của chúng ta là gì, ai sở hữu nó, và làm sao chúng ta giữ nó hiện hành khi tiêu chuẩn dịch chuyển?** WCAG 2.2 AA là sàn hôm nay và hầu hết luật tham chiếu nó, nhưng 2.2 đã thêm tiêu chí mà nhiều đội chưa áp dụng, và WCAG 3.0 đang đến với cấu trúc khác. Không có chủ sở hữu có tên, tiêu chuẩn trôi: các đội khác nhau nhắm các phiên bản khác nhau, không ai theo dõi khoảng cách, và sự phù hợp lặng lẽ mục nát giữa các cuộc kiểm toán. Hãy quyết định chính xác phiên bản và mức bạn xây theo, ai có thẩm quyền nâng nó, và tiêu chí mới đến hệ thống thiết kế và định nghĩa hoàn thành thế nào. Hãy mang mục tiêu đã nêu hiện tại của bạn, bằng chứng về nơi các đội thực sự đáp ứng nó, và một lộ trình ngắn để áp dụng các tiêu chí 2.2 bạn đã bỏ qua. Với một tổ chức lớn hoặc công, một chủ sở hữu khả năng tiếp cận hay trung tâm xuất sắc, một tuyên bố khả năng tiếp cận đã công bố, và một kế hoạch có tài liệu cho phiên bản tiêu chuẩn kế tiếp là thứ cho phép bạn trả lời một cơ quan quản lý hay tòa án bằng bằng chứng thay vì thiện chí.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ ủng hộ bạn ở đây, vì khả năng tiếp cận rẻ nhất khi cơ sở mã còn nhỏ. Thêm một bộ quét tự động vào CI và một lượt đi qua bàn phím vào danh sách kiểm tra pull request ngay từ sprint đầu, và dựa vào HTML ngữ nghĩa để bạn có hỗ trợ bàn phím và trình đọc màn hình miễn phí. Bỏ qua lớp phủ và công cụ nặng; phần thưởng là khi đội mua sắm của một khách hàng yêu cầu báo cáo phù hợp giữa thương vụ, bạn trả lời được trong vài ngày thay vì chạy vạy.

**Doanh nghiệp nhỏ.** Không có chuyên gia khả năng tiếp cận và ngân sách eo hẹp, hãy mua khả năng tiếp cận thay vì xây: chọn một nền tảng, chủ đề, hay thư viện thành phần đã phù hợp và nói rõ như vậy, và ưu tiên nhà cung cấp công bố tuyên bố khả năng tiếp cận. Hãy tự bao quát những điều cơ bản giá trị cao bằng công cụ miễn phí, kiểm tra chỉ-bàn-phím, bộ kiểm tra độ tương phản và nhãn rõ ràng trên mọi trường, vì những thứ đó bắt các thất bại thường loại trừ khách hàng nhất. Hãy coi một luồng tự động sai hay không dùng được là một khách hàng mất, vì một doanh nghiệp nhỏ hiếm khi cung cấp kênh hỗ trợ để quay về.

**Doanh nghiệp lớn.** Ở quy mô lớn công việc là biến khả năng tiếp cận thành thuộc tính hệ thống qua nhiều đội. Hãy phát hành thành phần tiếp cận được theo mặc định trong hệ thống thiết kế, chặn hồi quy trong CI, và dựng một chủ sở hữu hay trung tâm xuất sắc với quy trình khắc phục và đào tạo cho nhà thiết kế, kỹ sư và tác giả nội dung. Theo dõi sự phù hợp theo thời gian như một chỉ số, viết sự phù hợp WCAG vào mua sắm, và quản lý thành phần bên thứ ba như một danh mục để một widget nhúng đơn lẻ không thể lặng lẽ làm hỏng một hành trình dùng chung.

**Chính phủ.** Khả năng tiếp cận là yêu cầu pháp lý và nghĩa vụ công dân, vì công dân khuyết tật thường không có nhà cung cấp thay thế cho một khoản trợ cấp, giấy phép, hay lá phiếu. Hãy xây theo tiêu chuẩn mà quyền tài phán của bạn trích dẫn (ví dụ Section 508, EN 301 549, hay Đạo luật Khả năng Tiếp cận Châu Âu ánh xạ sang WCAG 2.2 AA), công bố một tuyên bố khả năng tiếp cận với đường báo cáo rào cản, và kiểm thử với công chúng khuyết tật bạn phục vụ. Hãy từ chối lớp phủ làm vật thay thế cho sự phù hợp thực, và yêu cầu nhà cung cấp cung cấp bằng chứng đáng tin cùng quyền khắc phục trong hợp đồng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp ba người xây công cụ tuyển dụng thêm một bộ quét khả năng tiếp cận vào bản dựng và một lượt đi qua bàn phím nhanh vào danh sách kiểm tra pull request ngay từ sprint đầu tiên, lập luận rằng giữ tiếp cận được rẻ hơn sửa sau. Khi đội mua sắm của một khách hàng cỡ vừa yêu cầu báo cáo phù hợp khả năng tiếp cận trong một chu kỳ bán hàng, công ty khởi nghiệp đã dùng HTML ngữ nghĩa, gắn nhãn mọi trường, và có tiêu điểm hiển thị ở mọi nơi, nên họ trả lời trong vài ngày thay vì chạy vạy. Sự sẵn sàng đó giành được một thương vụ mà đối thủ thua vì cùng yêu cầu.

**Doanh nghiệp lớn.** Một nhà bán lẻ lớn đối mặt vụ kiện tập thể vì khách hàng mù không thể hoàn thành thanh toán bằng trình đọc màn hình. Ngoài thỏa thuận và án phí, công ty phải khắc phục theo mốc thời gian do tòa án giám sát. Sau đó nó xây lại khả năng tiếp cận vào hệ thống thiết kế và đường ống CI, thêm kiểm thử trình đọc màn hình vào định nghĩa hoàn thành, và đào tạo các đội. Quy trình thanh toán tiếp cận được, được xây lại cũng cải thiện chuyển đổi và giảm liên hệ hỗ trợ cho mọi người: các bản sửa giúp người dùng trình đọc màn hình (nhãn rõ ràng, thông báo lỗi, thứ tự logic) giúp mọi người dùng.

**Chính phủ.** Một cơ quan trợ cấp công bị pháp luật yêu cầu đáp ứng WCAG 2.1 AA cho đơn trực tuyến của mình. Kiểm thử sớm với người dùng mù và thị lực kém, người dùng chỉ-bàn-phím, và người dùng có khuyết tật nhận thức cho thấy chỉ báo "trường bắt buộc" chỉ dùng màu, một bộ chọn ngày không tiếp cận được, và lỗi xác thực không được thông báo đang chặn mọi người hoàn thành. Sửa chúng, qua đánh dấu ngữ nghĩa, tiêu điểm hiển thị, thông báo lỗi bằng vùng sống, và trợ giúp [ngôn ngữ đơn giản](https://en.wikipedia.org/wiki/Plain_language), cho phép công dân khuyết tật lần đầu tự nộp đơn. Điều đó giảm sự phụ thuộc vào hỗ trợ trực tiếp và hạ chi phí phục vụ, đồng thời đáp ứng yêu cầu pháp lý.

## Luận chứng kinh doanh: động lực, ROI và TCO

Luận chứng kinh doanh dựa trên tầm với thị trường, rủi ro pháp lý, chi phí phục vụ và chất lượng. Người khuyết tật và gia đình họ kiểm soát sức mua đáng kể; loại trừ họ là từ bỏ nó. Các dịch vụ tiếp cận được giảm nhu cầu về các kênh hỗ trợ đắt đỏ (hỗ trợ qua điện thoại và trực tiếp), là một khoản tiết kiệm vận hành trực tiếp, đặc biệt với chính phủ. Và vì các cải tiến khả năng tiếp cận (nhãn rõ ràng, hỗ trợ bàn phím, nội dung dễ đọc, đánh dấu vững chắc) giúp mọi người, chúng thường nâng tỷ lệ hoàn thành và sự hài lòng tổng thể.

Về TCO, chi phí áp dụng là đào tạo, công cụ, và xây khả năng tiếp cận vào thành phần và đường ống, tất cả khiêm tốn khi bạn làm từ đầu. Chi phí của việc không áp dụng nghiêm trọng và đến từ nhiều hướng: trách nhiệm pháp lý (kiện tụng, thỏa thuận, khắc phục do tòa án ra lệnh, hình phạt quy định), chi phí cao hơn nhiều của việc trang bị bổ sung dưới áp lực hạn chót, thiệt hại danh tiếng, và chi phí liên tục của việc phục vụ người dùng bị loại trừ qua các kênh đắt hơn. Trang bị bổ sung thường tốn gấp nhiều lần so với thiết kế vào.

Để trình bày lập luận với ban lãnh đạo, hãy mở đầu bằng nghĩa vụ pháp lý ở nơi nó áp dụng (nó không thể thương lượng với chính phủ và ngày càng với khu vực tư). Rồi định lượng quần thể có thể tiếp cận bạn đang loại trừ, chi phí kênh hỗ trợ của sự loại trừ đó, và các lợi ích "vỉa hè dốc" cho mọi người dùng. Hãy định vị khả năng tiếp cận là quản lý rủi ro cộng chất lượng, không phải từ thiện.

## Phản mẫu và cạm bẫy

- **Khả năng tiếp cận như ô đánh dấu trước ra mắt**: một cuộc kiểm toán ở cuối thay vì thực hành liên tục, bảo đảm làm lại phút chót tốn kém.
- **"Súp div"**: đánh dấu phi ngữ nghĩa với trình xử lý nhấp trên các phần tử chung, vô hình với công nghệ hỗ trợ.
- **Lạm dụng ARIA**: gắn ARIA lên đánh dấu hỏng, đánh lừa trình đọc màn hình nhiều hơn đánh dấu thuần.
- **Thông tin chỉ bằng màu**: trạng thái chỉ hiển thị bằng màu, vô hình với người mù màu.
- **Tiêu điểm vô hình**: gỡ viền tiêu điểm vì thẩm mỹ, bỏ rơi người dùng bàn phím.
- **Bẫy bàn phím**: hộp thoại và widget bẫy hoặc mất tiêu điểm.
- **Tự mãn vì quét tự động**: qua bộ quét và giả định sản phẩm tiếp cận được.
- **Lớp phủ khả năng tiếp cận**: widget "sửa một dòng" của bên thứ ba không mang lại sự phù hợp thực và có thể làm tệ trải nghiệm.
- **Loại trừ người dùng khuyết tật khỏi nghiên cứu**: thiết kế cho một người khuyết tật tưởng tượng thay vì kiểm thử với người thật.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Không có thực hành khả năng tiếp cận. Vấn đề chỉ được phát hiện khi một người dùng phàn nàn hoặc một vụ kiện đến, và phản ứng là phản ứng. Đánh dấu phi ngữ nghĩa và chưa kiểm thử, và không ai sở hữu vấn đề.

**Mức 2: Phát triển.** Nhận thức tồn tại và một số đội hành động theo: một bộ quét tự động trong một bản dựng ở đây, một lượt đi qua bàn phím ở kia, một cuộc kiểm toán trước ra mắt trước một bản phát hành lớn. Thực hành cơ bản và không nhất quán qua các đội, khả năng tiếp cận vẫn là danh sách kiểm tra giai đoạn muộn, và thường bị hạ ưu tiên dưới áp lực lịch trình.

**Mức 3: Chuẩn hóa.** WCAG 2.2 AA là tiêu chuẩn có tài liệu, được thực thi toàn tổ chức. Khả năng tiếp cận được xây vào hệ thống thiết kế để thành phần được phát hành tiếp cận được theo mặc định, được kiểm thử tự động và thủ công, và được viết vào định nghĩa hoàn thành. Các đội được đào tạo, một chủ sở hữu hay trung tâm xuất sắc tồn tại, và một quy trình khắc phục được xác định.

**Mức 4: Quản lý.** Khả năng tiếp cận được đo và kiểm soát bằng dữ liệu theo các đường cơ sở. Tổ chức theo dõi các chỉ số phù hợp theo thời gian (tỷ lệ qua bộ quét, số rào cản mở theo mức nghiêm trọng, độ bao phủ kiểm thử trình đọc màn hình của các hành trình quan trọng, và thời gian khắc phục), báo cáo chúng theo từng đội trên bảng điều khiển, và coi hồi quy là thất bại bản dựng thay vì cảnh báo khuyến nghị. Mục tiêu được đặt so với một đường cơ sở và tiến trình được rà soát, nên một đội tụt lại hiển thị trước khi một cuộc kiểm toán tìm thấy.

**Mức 5: Điều phối.** Khả năng tiếp cận được cải thiện liên tục và tích hợp trong toàn tổ chức. Người khuyết tật là một phần của nghiên cứu và kiểm thử định kỳ, và khả năng tiếp cận được nhúng trong mua sắm, token thiết kế và CI. Tổ chức thích ứng khi tiêu chuẩn dịch chuyển (áp dụng tiêu chí WCAG mới và chuẩn bị cho WCAG 3.0), và nó gây ảnh hưởng nhà cung cấp cùng đối tác để cả chuỗi cung ứng tuân thủ.

## Ý tưởng để thảo luận

- Làm sao bạn giữ khả năng tiếp cận không bị hạ ưu tiên khi hạn chót siết lại?
- Hỗn hợp đúng của kiểm thử tự động, thủ công và với người dùng cho hồ sơ rủi ro của bạn là gì?
- Sự phù hợp khả năng tiếp cận nên được viết vào hợp đồng nhà cung cấp và mua sắm thế nào?
- Bạn xử lý khoảng cách giữa sự phù hợp WCAG và khả năng dùng thực sự cho người khuyết tật thế nào?
- Các đội nên chuẩn bị cho WCAG 3.0 thế nào trong khi xây theo 2.2 hôm nay?
- Làm sao bạn tuyển và đền bù người tham gia khuyết tật cho nghiên cứu một cách công bằng và tôn trọng?

## Những điểm cần ghi nhớ

- Khả năng tiếp cận là thuộc tính chất lượng cơ sở và, với chính phủ, là yêu cầu pháp lý.
- Thiết kế theo WCAG 2.2 AA làm sàn; dùng các nguyên tắc POUR như mô hình tinh thần.
- HTML ngữ nghĩa trước; ARIA chỉ để lấp khoảng trống thực, làm đúng.
- Công cụ tự động bắt khoảng một phần ba vấn đề; kiểm thử thủ công và bằng công nghệ hỗ trợ là thiết yếu.
- Kiểm thử với người khuyết tật, không chỉ cho họ.
- Xây khả năng tiếp cận vào thì rẻ và bền; trang bị bổ sung thì đắt và mong manh.
- Thiết kế tiếp cận được là thiết kế tốt hơn cho mọi người: hiệu ứng vỉa hè dốc là có thật.

## Tài liệu tham khảo và đọc thêm

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* và các tài liệu Understanding/Techniques hỗ trợ
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), tài liệu giới thiệu và hướng dẫn
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton và Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- Tiêu chuẩn Section 508 của Hoa Kỳ và hướng dẫn trên Section508.gov
- Tiêu chuẩn châu Âu EN 301 549 và Đạo luật Khả năng Tiếp cận Châu Âu
- Hướng dẫn khả năng tiếp cận của chính phủ (ví dụ cẩm nang khả năng tiếp cận của UK GDS)
- WebAIM, nghiên cứu và bài viết bao gồm các phân tích khả năng tiếp cận hằng năm
