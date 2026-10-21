# 3.9 Kỹ thuật hệ thống

## Tổng quan và động lực

[Kỹ thuật hệ thống](https://en.wikipedia.org/wiki/Systems_engineering) là kỷ luật kỹ thuật hóa toàn bộ một hệ thống phức tạp từ đầu đến cuối, để mọi bộ phận của nó phối hợp đáp ứng một nhu cầu thực. Các bộ phận bao gồm nhiều thứ hơn phần mềm rất nhiều. Một hệ thống hiện đại thường kết hợp phần mềm, phần cứng, con người, dữ liệu và quy trình, và nó phải vận hành trong một thế giới thực lộn xộn. Kỹ thuật hệ thống giữ cho tất cả những thứ này được căn chỉnh trong suốt vòng đời của hệ thống.

Điều này khác với kiến trúc phần mềm. Kiến trúc phần mềm (chương 3.1) quyết định các thành phần phần mềm được cấu trúc thế nào và giao tiếp với nhau ra sao. Kỹ thuật hệ thống nằm cao hơn một mức. Nó hỏi hệ thống như một tổng thể phải làm gì, phần mềm, phần cứng và người vận hành chia nhau công việc thế nào, và bạn sẽ chứng minh thứ hoàn chỉnh hoạt động bằng cách nào. Mái nhà chuyên môn của nó là [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), Hội đồng Quốc tế về Kỹ thuật Hệ thống, và tiêu chuẩn neo của nó là [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), định nghĩa các quy trình cho vòng đời của một hệ thống.

Điều này quan trọng với các chương trình doanh nghiệp và chính phủ lớn vì hệ thống của họ lớn, sống lâu, và quan trọng về an toàn hoặc sứ mệnh. Một nền tảng quốc phòng, một hệ thống không lưu, hay một chòm vệ tinh pha trộn phần cứng tùy chỉnh, linh kiện bên thứ ba, phần mềm nhúng và đám mây, và người vận hành, và không đội nào có thể giữ toàn bộ trong đầu. Bạn cũng thường xây một [hệ thống của các hệ thống](https://en.wikipedia.org/wiki/System_of_systems): nhiều hệ thống độc lập, mỗi hệ thống hữu ích riêng, phải hợp tác để mang lại một năng lực lớn hơn.

Chương này liên hệ với yêu cầu phần mềm (chương 2.8), nền tảng kiến trúc (chương 3.1), mô hình và phương pháp phần mềm (chương 2.12), khả năng tương tác và tiêu chuẩn mở (chương 3.8), và quản lý dự án (chương 10.6).

## Các nguyên tắc chính

- **Kỹ thuật hóa toàn thể, không phải các bộ phận.** Một hệ thống thành công hay thất bại như một tổng thể, nên tối ưu một hệ thống con riêng lẻ có thể làm tổng thể tệ hơn.
- **Theo vòng đời.** Một hệ thống có cuộc đời từ khái niệm đầu tiên đến ngừng sử dụng cuối cùng. Hãy lên kế hoạch cho tất cả, không chỉ việc xây dựng.
- **Truy vết mọi yêu cầu.** Mọi nhu cầu nên ánh xạ tới một yêu cầu, một phần tử thiết kế và một bài kiểm thử. Nếu bạn không truy vết được, bạn không chứng minh được.
- **Quản lý giao diện có chủ đích.** Hầu hết thất bại xảy ra ở ranh giới giữa các bộ phận, nên giao diện xứng đáng có quyền sở hữu và kiểm soát tường minh.
- **Kiểm chứng và xác nhận riêng biệt.** Xây thứ đó đúng (kiểm chứng) và xây đúng thứ (xác nhận) là những câu hỏi khác nhau, và bạn cần cả hai câu trả lời.
- **Kỳ vọng hành vi nổi lên.** Kết hợp các bộ phận tạo ra hành vi mà không bộ phận đơn lẻ nào thể hiện. Một số là mục đích, và một số là bất ngờ khó chịu.
- **Đồng kỹ thuật phần cứng và phần mềm.** Khi cả hai đều tùy chỉnh, quyết định ở bên này ràng buộc bên kia, nên hãy hoạch định chúng cùng nhau.

## Khuyến nghị

### Quản lý toàn bộ vòng đời hệ thống

Hãy coi hệ thống như có một cuộc đời trọn vẹn, và hoạch định từng giai đoạn. Một vòng đời phổ biến chạy: **khái niệm** (hiểu nhu cầu và khám phá các lựa chọn), **yêu cầu** (nêu chính xác hệ thống phải làm gì), **thiết kế** (quyết định kiến trúc và các bộ phận), **tích hợp** (đưa các bộ phận lại với nhau), **kiểm chứng và xác nhận** (chứng minh nó hoạt động và là hệ thống đúng), **vận hành** (chạy và bảo trì nó), và **ngừng sử dụng** (ngừng hoạt động an toàn, bao gồm dữ liệu và thải bỏ). ISO/IEC/IEEE 15288 cho bạn một khung quy trình cho việc này. Các giai đoạn không nhất thiết là thác nước cứng nhắc; bạn có thể lặp, làm bản mẫu và giao từng phần tăng dần. Điểm chính là bạn có ý thức giải quyết mọi giai đoạn, bao gồm những giai đoạn sau đắt đỏ mà kế hoạch sớm thường bỏ qua.

### Nắm bắt nhu cầu các bên liên quan và phân bổ yêu cầu với khả năng truy vết

Bắt đầu từ những người quan tâm đến hệ thống: người dùng, người vận hành, chủ sở hữu, cơ quan quản lý và công chúng. Thu thập **nhu cầu** của họ bằng ngôn ngữ đơn giản, rồi biến những nhu cầu đó thành các **yêu cầu** được kỹ thuật hóa, cụ thể và kiểm thử được (xem chương 2.8). Tiếp theo là **phân bổ yêu cầu**: gán mỗi yêu cầu cấp hệ thống cho một hệ thống con cụ thể, để bạn biết bộ phận nào chịu trách nhiệm đáp ứng nó. Hãy giữ một **ma trận [truy vết](https://en.wikipedia.org/wiki/Requirements_traceability)**, một bản ghi sống nối mỗi nhu cầu với yêu cầu của nó, với phần tử thiết kế thỏa mãn nó, và với bài kiểm thử kiểm chứng nó. Nó cho phép bạn chứng minh bất cứ lúc nào rằng mọi nhu cầu đều được bao phủ và mọi bộ phận tồn tại có lý do.

### Quản lý giao diện tường minh

Giao diện là nơi các bộ phận gặp nhau, và là nơi các hệ thống hỏng nhiều nhất. Một giao diện có thể là một đầu nối vật lý, một giao thức mạng, một định dạng dữ liệu, hoặc một quy trình của con người. Với mỗi cái, hãy viết một **Tài liệu Kiểm soát Giao diện** (ICD): một đặc tả đã được thống nhất về chính xác cách hai bộ phận kết nối và trao đổi thông tin. Cho mỗi giao diện một chủ sở hữu rõ ràng ở mỗi bên. Dựa vào các đặc tả dùng chung, đã công bố thay vì trình kết nối làm riêng làm cho tích hợp dễ hơn nhiều, đó là lập luận về khả năng tương tác ở chương 3.8. Hãy đóng băng giao diện sớm ở nơi bạn có thể, vì một thay đổi muộn gợn vào mọi bộ phận chạm đến nó.

### Tích hợp rồi kiểm chứng và xác nhận

**Tích hợp hệ thống** kết hợp các hệ thống con thành toàn thể đang hoạt động, thường theo từng giai đoạn thay vì tất cả cùng lúc, để bạn tìm thấy vấn đề khi chúng còn nhỏ. Sau tích hợp là **[kiểm chứng và xác nhận](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), hai kiểm tra riêng biệt. **Kiểm chứng** hỏi: chúng ta có xây hệ thống đúng không, nghĩa là nó có đáp ứng các yêu cầu đã đặc tả không? Bạn kiểm chứng qua kiểm tra, phân tích, trình diễn và kiểm thử. **Xác nhận** hỏi: chúng ta có xây đúng hệ thống không, nghĩa là nó có đáp ứng nhu cầu thực của các bên liên quan trong sử dụng thực không? Một hệ thống có thể qua kiểm chứng (nó đáp ứng đặc tả) mà vẫn thất bại xác nhận (đặc tả sai). Hãy hoạch định cả hai sớm, và viết yêu cầu cùng giao diện sao cho chúng có thể được kiểm chứng ngay từ đầu.

### Áp dụng kỹ thuật hệ thống dựa trên mô hình

Kỹ thuật hệ thống truyền thống tạo ra những núi tài liệu trôi khỏi sự đồng bộ. **[Kỹ thuật hệ thống dựa trên mô hình](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) thay đống đó bằng một mô hình hình thức, dùng chung, duy nhất của hệ thống, từ đó các góc nhìn và báo cáo được sinh ra. Ngôn ngữ mô hình hóa phổ biến là **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Ngôn ngữ Mô hình hóa Hệ thống), một ngôn ngữ đồ họa để mô tả yêu cầu, cấu trúc, hành vi và ràng buộc của hệ thống. Vì mọi thứ sống trong một mô hình liên kết, một thay đổi cập nhật ở mọi nơi, và truy vết trở thành một truy vấn thay vì cuộc rượt đuổi thủ công. MBSE liên hệ với các ý tưởng mô hình hóa trong chương 2.12. Hãy áp dụng dần, bắt đầu với các phần rủi ro cao nhất nơi một mô hình dùng chung hoàn vốn nhanh nhất.

### Áp dụng tư duy hệ thống cho hành vi nổi lên

Hãy thực hành [tư duy hệ thống](https://en.wikipedia.org/wiki/Systems_thinking): suy luận về toàn thể và các mối quan hệ giữa các bộ phận, không chỉ từng bộ phận một. Đây là cách bạn dự đoán **[hành vi nổi lên](https://en.wikipedia.org/wiki/Emergence)**: các thuộc tính chỉ xuất hiện khi các bộ phận kết hợp và không bộ phận đơn lẻ nào thể hiện. Sự nổi lên tốt thường là mục đích của hệ thống (một đàn máy bay không người lái bao phủ một khu vực mà không chiếc nào làm được). Sự nổi lên xấu là thất bại bất ngờ (hai hệ thống con an toàn tương tác tạo ra trạng thái nguy hiểm). Bạn không thể kiểm thử loại bỏ sự nổi lên khỏi một hệ thống bạn chưa bao giờ mô hình hóa, vì vậy hãy dùng mô phỏng và phân tích mối nguy có cấu trúc để tìm nó trước khi vận hành.

### Đồng kỹ thuật phần cứng và phần mềm

Khi một hệ thống bao gồm phần cứng tùy chỉnh, hãy kỹ thuật hóa phần cứng và phần mềm cùng nhau, một thực hành gọi là **[đồng thiết kế phần cứng/phần mềm](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Các quyết định ràng buộc lẫn nhau: phần cứng đặt ra giới hạn thời gian, bộ nhớ và năng lượng mà phần mềm phải sống trong đó, và nhu cầu của phần mềm định hình những gì phần cứng phải cung cấp. Thời gian chờ phần cứng dài cũng chi phối lịch trình. Hãy quyết định sớm chức năng nào ở phần cứng và chức năng nào ở phần mềm, và xem xét lại sự phân chia đó khi các ràng buộc nổi lên.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm / chi phí |
|---|---|---|
| Sự chặt chẽ kỹ thuật hệ thống đầy đủ | Ít bất ngờ muộn, truy vết mạnh, an toàn hơn và kiểm toán được | Chi phí ban đầu cao, khởi đầu chậm hơn, quy trình nặng |
| Cách tiếp cận nhẹ / chỉ phần mềm | Nhanh, rẻ, linh hoạt cho phạm vi nhỏ | Vỡ ra với hệ thống lớn đa ngành, bỏ sót giao diện và sự nổi lên |
| Dựa trên mô hình (MBSE) | Nguồn sự thật duy nhất, truy vết dễ, góc nhìn nhất quán | Chi phí công cụ và đào tạo, thay đổi văn hóa, đường cong học |
| Kỹ thuật hệ thống dựa trên tài liệu | Quen thuộc, chi phí công cụ thấp, dễ chia sẻ | Tài liệu trôi khỏi đồng bộ, truy vết thủ công và dễ sai |

Đánh đổi trung tâm là sự chặt chẽ so với tốc độ. Kỹ thuật hệ thống đầy đủ dồn công sức lên trước vào khái niệm, yêu cầu và công việc giao diện. Công sức đó tự hoàn vốn nhiều lần trên các hệ thống lớn, sống lâu, quan trọng về an toàn, nơi một khiếm khuyết được phát hiện khi vận hành có thể tốn gấp hàng nghìn lần cùng khiếm khuyết đó được phát hiện trong yêu cầu. Trên một sản phẩm nhỏ, ngắn hạn, chỉ phần mềm, sự chặt chẽ đó là quá mức. Hãy khớp trọng lượng quy trình của bạn với quy mô, tuổi thọ và rủi ro của hệ thống. Chế độ thất bại là áp dụng thói quen của dự án dùng một lần cho một hệ thống sẽ chạy ba mươi năm và mang rủi ro thế giới thực.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn đã xây đúng những gì đặc tả đòi hỏi mà vẫn phát hành sai hệ thống ở đâu, và điều gì lẽ ra đã bắt được?** Kiểm chứng (chúng ta có xây đúng không) và xác nhận (chúng ta có xây đúng thứ không) trả lời các câu hỏi khác nhau, và một hệ thống có thể qua mọi kiểm thử kiểm chứng trong khi thất bại xác nhận vì bản thân đặc tả sai. Trong các chương trình lớn, hai thứ bị gộp lại thành "kiểm thử", nên không ai xác nhận đối chiếu với nhu cầu thực của người vận hành cho đến muộn, khi một bản sửa tốn gấp hàng nghìn lần so với thay đổi yêu cầu. Hãy mang một ví dụ trong quá khứ nơi hệ thống được bàn giao đáp ứng yêu cầu nhưng bỏ lỡ nhu cầu thực, và hỏi hoạt động xác nhận nào (một mô phỏng với người vận hành thật, một bản mẫu sớm ngoài hiện trường) lẽ ra đã phơi bày nó sớm hơn. Hãy hoạch định cả hai kiểm tra từ đầu, và viết yêu cầu cùng giao diện sao cho chúng có thể được kiểm chứng. Sự phân biệt này quyết định bạn chi nỗ lực rà soát khan hiếm ở đâu.

2. **Làm thế nào bạn săn tìm hành vi nổi lên xấu trước khi hệ thống vận hành, không phải sau?** Kết hợp các hệ thống con an toàn có thể tạo ra các trạng thái nguy hiểm mà không bộ phận đơn lẻ nào thể hiện, và bạn không thể kiểm thử loại bỏ sự nổi lên khỏi một hệ thống bạn chưa bao giờ mô hình hóa. Với một chương trình quan trọng về an toàn hoặc sứ mệnh, tương tác bất ngờ là cái gây thương tích cho ai đó hoặc làm hỏng sứ mệnh, nên nó phải được tìm thấy trước khi vận hành thực. Hãy mang cách tiếp cận mô hình hóa toàn thể của bạn (mô phỏng, phân tích mối nguy có cấu trúc, một mô hình SysML nắm bắt các tương tác) và hỏi những hành vi xuyên hệ thống con nào bạn thực sự đã khám phá so với đã giả định bỏ qua. Sự nổi lên tốt thường là mục đích của hệ thống và đáng để thiết kế hướng tới; sự nổi lên xấu là thất bại bạn phải kỹ thuật hóa để chống lại. Nếu chiến lược tích hợp duy nhất của bạn là nối các bộ phận lại và xem điều gì xảy ra, bạn đang lên kế hoạch khám phá sự nổi lên trên môi trường thực.

3. **Khi nào các quyết định phần cứng thời gian chờ dài phải được đóng băng, và hạn chót đó chi phối lịch trình phần mềm của bạn thế nào?** Khi một hệ thống bao gồm phần cứng tùy chỉnh, cả hai phải được đồng kỹ thuật: con chip đặt ra trần thời gian, bộ nhớ và năng lượng mà phần mềm sống trong đó, và thời gian chờ phần cứng thường chi phối toàn bộ lịch trình. Các đội coi phần mềm là tách rời được tối ưu cục bộ rồi đụng độ với ràng buộc phần cứng lúc tích hợp, mất nhiều tháng. Hãy mang thời gian chờ phần cứng và ngày mà sự phân chia chức năng phần cứng/phần mềm phải được quyết định, và xem xét lại sự phân chia đó khi các ràng buộc nổi lên thay vì đóng băng mù quáng. Bạn quyết định càng sớm chức năng nào sống trong silicon và chức năng nào trong phần mềm, bạn càng ít đối mặt với các đảo ngược tốn kém. Giao diện giữa hai bên xứng đáng có một Tài liệu Kiểm soát Giao diện và một chủ sở hữu ở mỗi bên, vì một thay đổi muộn ở đó gợn qua mọi thứ chạm đến nó.

4. **Bạn có thể truy vết một nhu cầu bên liên quan duy nhất suốt đến yêu cầu, phần tử thiết kế và bài kiểm thử chứng minh nó không, và ai giữ cho liên kết đó sống?** Khả năng truy vết là thứ cho phép bạn cho thấy bất cứ lúc nào rằng mọi nhu cầu được bao phủ và mọi bộ phận tồn tại có lý do, nhưng trong một chương trình lớn ma trận mục nát ngay khoảnh khắc không ai sở hữu nó. Lực kéo đối lập là thật: kỹ sư trải nghiệm truy vết như chi phí chung quan liêu, và một ma trận duy trì bằng tay trôi khỏi cập nhật nhanh hơn thiết kế thay đổi. Hãy mang một sợi thật từ một chương trình hiện tại và thử đi nó từ đầu đến cuối trong phòng, từ một nhu cầu bên liên quan có tên, đến yêu cầu được phân bổ, đến hệ thống con và phần tử thiết kế thỏa mãn nó, đến bài kiểm thử kiểm chứng, và ghi lại chuỗi đứt ở đâu. Hãy quyết định ai sở hữu ma trận và liệu nó có nên sống trong một mô hình nơi truy vết là truy vấn thay vì cuộc rượt đuổi thủ công không. Với các chương trình doanh nghiệp và chính phủ, ma trận cũng là sản phẩm kiểm toán mà cơ quan quản lý và cơ quan mua sắm đòi hỏi, nên một chuỗi đứt làm nhiều hơn là làm chậm kỹ thuật; nó có thể đình trệ chứng nhận hoặc thanh toán.

5. **Cách tiếp cận dựa trên mô hình có đáng với chi phí công cụ và văn hóa của nó với bạn không, hay nó sẽ thành phần mềm đắt tiền bỏ xó?** Kỹ thuật hệ thống dựa trên tài liệu quen thuộc và rẻ công cụ, nhưng tài liệu của nó trôi khỏi đồng bộ và truy vết của nó thủ công, dễ sai; MBSE thay đống đó bằng một mô hình liên kết, với giá công cụ, đào tạo và một thay đổi văn hóa thực sự. Cả hai thái cực đều đắt: bỏ qua MBSE trên một chương trình lớn đa ngành và bạn trả bằng bất ngờ tích hợp, áp dụng nó mà thiếu kỷ luật giữ mô hình cập nhật và nó mục nát thành phần mềm bỏ xó tệ hơn không có mô hình. Hãy mang một đánh giá trung thực về độ trưởng thành công cụ của bạn, ai trong đội thực sự có thể soạn và duy trì một mô hình SysML, và hệ thống con rủi ro cao nào có thể thí điểm cách tiếp cận nơi một mô hình dùng chung hoàn vốn nhanh nhất. Hãy quyết định dần dần thay vì bắt buộc cả tổ chức cùng lúc. Với một chương trình doanh nghiệp hay chính phủ lớn có nhiều nhà cung cấp, hãy cân nhắc liệu một mô hình dùng chung có phải là cách thực tế duy nhất để giữ yêu cầu, giao diện và kiểm thử nhất quán giữa các nhà thầu vốn trao đổi tài liệu cũ.

6. **Kế hoạch vòng đời của bạn có tài trợ nghiêm túc cho vận hành và ngừng sử dụng không, hay âm thầm dừng ở lúc ra mắt?** Các giai đoạn chi phối tổng chi phí của một hệ thống sống lâu, chạy nó hàng thập kỷ và ngừng hoạt động an toàn, là những giai đoạn mà kế hoạch sớm thường xuyên bỏ qua, vì áp lực luôn là phát hành. Cân nhắc đối lập là tiền và sự chú ý khan hiếm nhất đúng lúc các giai đoạn sau cảm thấy xa xôi nhất, nên vận hành, bảo trì, di chuyển dữ liệu và thải bỏ bị trì hoãn cho đến khi chúng thành một cuộc chạy vạy đắt đỏ, rủi ro. Hãy mang kế hoạch vòng đời hiện tại và kiểm tra xem nó có nêu tên chủ sở hữu, ngân sách và tiêu chí thoát cho vận hành và ngừng sử dụng không, hay nó coi ra mắt là vạch đích. Hãy hỏi điều gì xảy ra với dữ liệu và phần cứng lúc hết vòng đời, và ai trả cho nhiều năm bảo trì ở giữa. Với các hệ thống doanh nghiệp và chính phủ phải chạy hai mươi hay ba mươi năm rồi nghỉ hưu dưới sự soi xét công khai, việc ngừng hoạt động không có kế hoạch có thể vi phạm nghĩa vụ quy định, môi trường hoặc lưu giữ hồ sơ, nên ngừng sử dụng thuộc về kế hoạch và ngân sách ngay từ lần rà soát khái niệm đầu tiên.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Một đội nhỏ xíu không thể chạy một chương trình kỹ thuật hệ thống chính thức và không nên thử, nhưng vẫn có thể coi phần sụn, ứng dụng và đám mây là một hệ thống thay vì ba dự án riêng. Hãy viết một tài liệu giao diện ngắn ghim cách các bộ phận nói chuyện với nhau, giữ một bảng đơn giản nối mỗi nhu cầu khách hàng với bộ phận thỏa mãn nó, và bỏ qua quy trình nặng. Nguồn lực khan hiếm nhất của bạn là sự chú ý kỹ thuật, vì vậy chỉ dành công sức truy vết ở nơi một giả định sai ở ranh giới sẽ âm thầm làm hỏng sản phẩm ngoài hiện trường.

**Doanh nghiệp nhỏ.** Không có kỹ sư hệ thống riêng và ngân sách eo hẹp, hãy dựa vào các tiêu chuẩn đã công bố và hệ thống con mua sẵn thay vì tích hợp theo yêu cầu riêng mà bạn phải tự thiết kế và kiểm chứng. Ưu tiên các nhà cung cấp phơi bày đặc tả giao diện rõ ràng để các bộ phận khớp nhau mà không cần trình kết nối tùy chỉnh bạn phải sở hữu mãi mãi. Hãy đóng khung lựa chọn xây-so-với-mua quanh việc bạn thực tế kiểm soát và kiểm chứng được giao diện nào qua vòng đời sản phẩm, và mua phần còn lại.

**Doanh nghiệp lớn.** Ở quy mô lớn vấn đề là sự nhất quán qua nhiều đội và nhà cung cấp: một quy trình vòng đời dùng chung căn chỉnh theo ISO/IEC/IEEE 15288, một Tài liệu Kiểm soát Giao diện và một chủ sở hữu có tên cho mọi ranh giới nhà cung cấp, và truy vết từ đầu đến cuối để một thay đổi thành phần không kích hoạt một cuộc chạy vạy toàn chương trình. Hãy đầu tư MBSE ở nơi một mô hình dùng chung giữ yêu cầu, giao diện và kiểm thử được căn chỉnh qua các nhà thầu. Quản trị quy trình để kiểm chứng và xác nhận luôn riêng biệt và mọi yêu cầu được phân bổ cho một bộ phận chịu trách nhiệm.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy chỉ rõ quy trình kỹ thuật hệ thống, truy vết và bằng chứng V&V trong hợp đồng, yêu cầu nhà cung cấp giao tài liệu kiểm soát giao diện và sản phẩm vòng đời mà bạn có thể kiểm toán, và dành xác nhận an toàn và sứ mệnh cho rà soát độc lập với người vận hành thật trước bất kỳ lần chuyển đổi sang vận hành thực nào. Hãy hoạch định và tài trợ vận hành cùng ngừng sử dụng tường minh, vì một chương trình công phải chịu trách nhiệm về toàn bộ vòng đời, bao gồm ngừng hoạt động an toàn và lưu giữ hồ sơ.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp phần cứng bốn người xây dựng cảm biến kết nối không thể gánh một chương trình kỹ thuật hệ thống chính thức, nhưng vẫn coi sản phẩm là một hệ thống gồm phần sụn, ứng dụng di động và phần phụ trợ đám mây thay vì ba dự án riêng. Họ viết một tài liệu giao diện ngắn ghim cách thiết bị, ứng dụng và máy chủ nói chuyện (định dạng thông điệp, đơn vị, mã lỗi) và giữ một bảng đơn giản nối mỗi nhu cầu khách hàng với bộ phận thỏa mãn nó. Khi một con chip cảm biến rẻ hơn buộc phải đổi phần sụn, giao diện dùng chung đó cho thấy ngay ứng dụng và phần phụ trợ phải điều chỉnh gì, nên việc đổi linh kiện không âm thầm làm hỏng sản phẩm ngoài hiện trường.

**Doanh nghiệp lớn.** Một nhà sản xuất ô tô toàn cầu xây nền tảng xe điện mới: một hệ thống gồm phần mềm (quản lý pin, hỗ trợ lái, giải trí), phần cứng (động cơ, cảm biến, chip) và yếu tố con người, cộng nhiều nhà cung cấp mỗi bên giao một hệ thống con. Công ty chạy một chương trình kỹ thuật hệ thống. Nhu cầu các bên liên quan nuôi các yêu cầu được phân bổ, mọi giao diện nhà cung cấp có một Tài liệu Kiểm soát Giao diện, và một mô hình SysML nối yêu cầu với thiết kế và kiểm thử. Khi nhà cung cấp cell pin đổi một linh kiện, mô hình truy vết cho thấy chính xác yêu cầu, giao diện và kiểm thử nào bị ảnh hưởng, nên thay đổi được khoanh vùng thay vì kích hoạt cuộc chạy vạy toàn chương trình.

**Chính phủ.** Một cơ quan dẫn đường hàng không quốc gia hiện đại hóa hệ thống quản lý không lưu, một hệ thống của các hệ thống quan trọng về an toàn trải rộng radar, trạm làm việc của kiểm soát viên, thông tin liên lạc và phần mềm, vận hành suốt ngày đêm. Chương trình theo ISO/IEC/IEEE 15288 qua toàn bộ vòng đời. Kiểm chứng chứng minh mỗi hệ thống con đáp ứng đặc tả, và xác nhận qua mô phỏng với kiểm soát viên thật chứng minh hệ thống tích hợp hỗ trợ vận hành an toàn trước khi có bất kỳ lưu lượng bay thực nào phụ thuộc vào nó. V&V chặt chẽ cho phép cơ quan chuyển đổi theo giai đoạn, với phương án dự phòng ở mỗi bước, vì ở đây một thất bại nổi lên chưa được kiểm thử là một sự kiện an toàn công cộng.

## Luận chứng kinh doanh: động lực, ROI và TCO

Động lực là khiếm khuyết trở nên đắt theo cấp số nhân càng phát hiện muộn. Một lỗi yêu cầu bị bắt trong giai đoạn yêu cầu tốn gần như không gì để sửa. Cùng lỗi đó bị bắt khi vận hành có thể tốn gấp hàng nghìn lần, và trên một hệ thống quan trọng về an toàn nó có thể tốn mạng sống, thu hồi sản phẩm hoặc một sứ mệnh thất bại. Kỹ thuật hệ thống dịch việc phát hiện khiếm khuyết vào các giai đoạn sớm, rẻ.

Với **lợi tức đầu tư** (ROI, giá trị thu được so với chi phí bỏ ra), phần thưởng là việc làm lại được tránh, ít thất bại tích hợp hơn, và các chương trình đạt lịch trình cùng ngân sách thay vì vượt. Các nghiên cứu ngành về các chương trình lớn liên tục thấy nỗ lực kỹ thuật hệ thống mạnh tương quan với mức vượt nhỏ hơn. Với **tổng chi phí sở hữu** (TCO, toàn bộ chi phí suốt đời của việc xây dựng, vận hành và ngừng sử dụng một hệ thống), kỹ thuật hệ thống tính đến các giai đoạn vận hành và ngừng sử dụng vốn chi phối chi phí dài hạn nhưng các dự án tùy nghi bỏ qua. Thiết kế cho khả năng bảo trì, giao diện và thải bỏ từ đầu hạ chi phí của hàng thập kỷ hệ thống phục vụ. Xem quản lý dự án (chương 10.6).

## Phản mẫu và cạm bẫy

- **Thiết kế lớn trả trước không lặp.** Coi vòng đời là thác nước một chiều cứng nhắc, nên bạn chỉ biết yêu cầu sai sau khi đã xây mọi thứ.
- **Yêu cầu không có truy vết.** Một đống yêu cầu không ai nối với thiết kế hay kiểm thử, nên bạn không chứng minh được độ bao phủ hay biện minh cho bất kỳ bộ phận nào.
- **Phớt lờ giao diện.** Giả định các hệ thống con sẽ tự khớp nhau, rồi mất nhiều tháng lúc tích hợp vì các sai lệch ranh giới không ai sở hữu.
- **Kiểm chứng không xác nhận.** Chứng minh hệ thống đáp ứng đặc tả mà không bao giờ kiểm tra đặc tả có khớp nhu cầu thực, rồi phát hành sai hệ thống.
- **Coi phần mềm là riêng biệt.** Các đội phần mềm tối ưu cục bộ trong khi bỏ qua ràng buộc phần cứng, thời gian và người vận hành.
- **MBSE như phần mềm bỏ xó.** Xây một mô hình một lần, rồi để nó mục nát khỏi đồng bộ nên nó tệ hơn không có mô hình.
- **Bỏ qua hoạch định ngừng sử dụng.** Không có kế hoạch ngừng hoạt động, di chuyển dữ liệu hay thải bỏ, nên hết vòng đời thành một cuộc chạy vạy đắt đỏ, rủi ro.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Kỹ thuật hệ thống là tùy nghi và phản ứng. Yêu cầu sống trong các tài liệu rải rác, giao diện được khám phá lúc tích hợp, và kiểm chứng là bất cứ kiểm thử nào tình cờ được làm. Các chương trình lớn thường xuyên vượt và làm đội bất ngờ muộn.

**Mức 2: Phát triển.** Các thực hành cơ bản tồn tại trên các chương trình lớn. Yêu cầu được nắm bắt và lập đường cơ sở, các giao diện chính có tài liệu kiểm soát, và có một kế hoạch kiểm chứng. Thực hành không nhất quán giữa các đội và phụ thuộc vào cá nhân thay vì một phương pháp chung.

**Mức 3: Chuẩn hóa.** Kỹ thuật hệ thống là một kỷ luật có tài liệu, toàn tổ chức, căn chỉnh theo ISO/IEC/IEEE 15288 và được thực thi qua các đội. Toàn bộ vòng đời được hoạch định, truy vết được duy trì từ đầu đến cuối, giao diện được kiểm soát chính thức, và kiểm chứng cùng xác nhận là riêng biệt và có kế hoạch. MBSE được dùng trên các chương trình phức tạp.

**Mức 4: Quản lý.** Kỹ thuật hệ thống được đo và kiểm soát bằng dữ liệu. Tổ chức theo dõi các chỉ số theo đường cơ sở: độ biến động yêu cầu và độ bao phủ truy vết, lỗi giao diện được tìm thấy lúc tích hợp, tỷ lệ vượt kiểm chứng và xác nhận, và rò rỉ khiếm khuyết theo giai đoạn vòng đời (bao nhiêu khiếm khuyết thoát khỏi mỗi giai đoạn để bị bắt sau với chi phí cao hơn). Các cuộc rà soát điều hướng chương trình theo những con số này, và ngưỡng kích hoạt hành động khắc phục thay vì chữa cháy sau sự việc.

**Mức 5: Điều phối.** Kỹ thuật hệ thống được cải thiện liên tục và tích hợp trong toàn tổ chức. Một mô hình MBSE sống là nguồn sự thật duy nhất, truy vết được tự động hóa, mô phỏng dự đoán hành vi nổi lên trước khi xây, và các chỉ số từ các chương trình trước nuôi chương trình kế tiếp. Phần cứng và phần mềm được đồng kỹ thuật như lẽ đương nhiên, và quy trình thích ứng khi các chương trình, nhà cung cấp và rủi ro dịch chuyển.

## Ý tưởng để thảo luận

- Ranh giới giữa kỹ thuật hệ thống và kiến trúc phần mềm ở tổ chức của bạn nằm ở đâu, và ai sở hữu khoảng giữa chúng?
- Trên chương trình lớn nhất của bạn, bạn có thể truy vết một nhu cầu bên liên quan duy nhất suốt đến bài kiểm thử kiểm chứng nó không? Nếu không, cần gì để làm được?
- Thất bại gần đây nào của bạn xảy ra ở một giao diện, và ai sở hữu nó?
- MBSE có hoàn vốn với bạn không, hay nó sẽ thành phần mềm đắt tiền bỏ xó với văn hóa và công cụ của bạn?
- Kế hoạch vòng đời của bạn có giải quyết nghiêm túc vận hành và ngừng sử dụng không, hay âm thầm dừng ở lúc ra mắt?

## Những điểm cần ghi nhớ

- Kỹ thuật hệ thống kỹ thuật hóa toàn bộ hệ thống (phần mềm, phần cứng, con người và quy trình) từ đầu đến cuối, và khác với kiến trúc phần mềm.
- Hoạch định toàn bộ vòng đời, từ khái niệm qua yêu cầu, thiết kế, tích hợp, V&V, vận hành và ngừng sử dụng.
- Truy vết mọi nhu cầu tới một yêu cầu, một phần tử thiết kế và một bài kiểm thử, và phân bổ mỗi yêu cầu cho một bộ phận chịu trách nhiệm.
- Quản lý giao diện tường minh với quyền sở hữu rõ ràng và tài liệu kiểm soát, vì ranh giới là nơi các hệ thống hỏng.
- Kiểm chứng (xây đúng) và xác nhận (xây đúng thứ) là các kiểm tra khác nhau, và bạn cần cả hai.
- Dùng MBSE và SysML cho một nguồn sự thật liên kết, và dùng tư duy hệ thống để dự đoán hành vi nổi lên.
- Khớp trọng lượng quy trình của bạn với quy mô, tuổi thọ và rủi ro của hệ thống.

## Tài liệu tham khảo và đọc thêm

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore và Rick Steiner, *A Practical Guide to SysML: The Systems Modelling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage và William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede và William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin và Mark W. Maier, *The Art of Systems Architecting*
- Bộ Quốc phòng Hoa Kỳ, *Defence Acquisition Guidebook* (hướng dẫn kỹ thuật hệ thống)
