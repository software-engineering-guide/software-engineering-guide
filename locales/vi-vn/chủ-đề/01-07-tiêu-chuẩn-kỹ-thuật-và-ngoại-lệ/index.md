# 1.7 Tiêu chuẩn kỹ thuật và ngoại lệ

## Tổng quan và động lực

**Tiêu chuẩn kỹ thuật** là một quy tắc được lập thành tài liệu, được thống nhất về cách thực hiện công việc. Ví dụ: "mọi dịch vụ phải cung cấp một điểm cuối kiểm tra sức khỏe", hoặc "mọi trang web công khai phải đáp ứng **[WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (Hướng dẫn về khả năng tiếp cận nội dung web) 2.2 mức AA**". Một tiêu chuẩn không phải là một gợi ý, cũng không chỉ là một quy ước. Nó là một cam kết mà tổ chức tự ràng buộc mình, lý tưởng là một cam kết bạn có thể kiểm tra. Chương này nói về toàn bộ vòng đời của tiêu chuẩn, cách một tổ chức lớn **soạn thảo, công bố, áp dụng, thực thi và phát triển** chúng, và, cũng quan trọng không kém, cách tổ chức xử lý những trường hợp nằm ngoài chúng một cách chính đáng thông qua một **quy trình ngoại lệ** được quản trị (còn gọi là **quy trình miễn trừ**): một sự cho phép có tài liệu, có thời hạn để đi chệch khỏi một tiêu chuẩn vì một lý do đã nêu.

Động lực là ở quy mô lớn, các chuẩn mực phi chính thức ngừng hoạt động. Khi năm kỹ sư chia sẻ một căn phòng, "cách chúng ta làm ở đây" lan truyền qua trò chuyện và sự thẩm thấu. Khi năm nghìn kỹ sư trải rộng qua hàng chục đội, ba múi giờ và một thập kỷ thay đổi nhân sự, kiến thức ngầm đó vỡ ra thành hàng trăm thói quen cục bộ không tương thích. Tiêu chuẩn là cách bạn viết ra những bài học khó khăn mới có được một lần, để mọi đội thừa hưởng chúng thay vì học lại từng bài qua sự cố ngừng hoạt động của riêng mình. Chúng giảm [tải nhận thức](https://en.wikipedia.org/wiki/Cognitive_load), làm cho [đánh giá mã](https://en.wikipedia.org/wiki/Code_review) xoay quanh nội dung thay vì phong cách, cho phép mọi người di chuyển giữa các đội, và cho kiểm toán viên cùng cơ quan quản lý một thứ cụ thể để đánh giá.

Nhưng tiêu chuẩn mang một chế độ thất bại riêng: sự cứng nhắc. Một tiêu chuẩn không chấp nhận ngoại lệ sớm muộn sẽ chặn công việc chính đáng: một thử nghiệm nhanh, một ràng buộc của nhà cung cấp, một trường hợp thực sự mới mà các tác giả chưa bao giờ hình dung. Các đội khi đó hoặc dừng hẳn lại hoặc, tệ hơn, âm thầm phớt lờ tiêu chuẩn, điều làm ăn mòn uy tín của *mọi* tiêu chuẩn. Phương thuốc là câu châm ngôn cũ "ngoại lệ chứng minh quy tắc". Một quy trình ngoại lệ hiển thị, có nguyên tắc là thứ giữ cho tiêu chuẩn vừa đáng tin vừa nhân văn. Chương này xây dựng trên ra quyết định và quản trị (chương 1.5) cùng hồ sơ quyết định (chương 1.6), và đóng góp trực tiếp vào tiêu chuẩn và phong cách viết mã (chương 2.1), danh sách kiểm tra (chương 12.2) và mẫu biểu (chương 12.3).

## Các nguyên tắc chính

- **Một tiêu chuẩn nêu một kết quả và đưa ra một lý do.** Quy tắc cộng với lý do; không có *vì sao*, mọi người không thể phán đoán khi nào nó thực sự áp dụng.
- **Nếu không kiểm tra được thì chưa phải là tiêu chuẩn.** Ưu tiên các phát biểu kiểm thử được hơn các khát vọng.
- **Tiêu chuẩn là tài liệu sống.** Chúng có phiên bản, có chủ sở hữu, có ngày và được sửa đổi, không phải khắc vào đá rồi bỏ rơi.
- **Tự động hóa việc thực thi ở nơi có thể; dành rà soát của con người cho phán đoán.** Máy kiểm tra phần cơ học; con người kiểm tra phần có ý nghĩa.
- **Sai lệch là điều được mong đợi, không đáng xấu hổ, nhưng chúng phải hiển thị.** Một lần miễn trừ trung thực luôn tốt hơn việc không tuân thủ âm thầm.
- **Đặt thời hạn cho mọi ngoại lệ.** Một ngoại lệ vĩnh viễn là một lỗi của tiêu chuẩn; hãy phát hiện và sửa tiêu chuẩn.
- **Từ ngữ và ví dụ thay vì biệt ngữ và mệnh lệnh.** Mọi người tuân theo các tiêu chuẩn họ hiểu và có thể sao chép.

## Khuyến nghị

### Viết tiêu chuẩn rõ ràng, kiểm thử được và có lý do

Một tiêu chuẩn tốt là một tài liệu ngắn, độc lập với hình dạng dễ đoán để người đọc biết tìm ở đâu. Hãy áp dụng một **mẫu tiêu chuẩn** (chương 12.3) và dùng nó ở mọi nơi. Các phần thiết yếu gồm:

- **Tiêu đề và mã định danh:** một tên ổn định và số tham chiếu để trích dẫn.
- **Trạng thái:** bản nháp, đang hiệu lực, bị thay thế hoặc đã ngừng, kèm ngày.
- **Quy tắc:** được nêu như một kết quả, rõ ràng và không mơ hồ ("phải", "nên", "có thể", dùng có chủ đích, theo quy ước **RFC 2119** cho các từ khóa yêu cầu).
- **Lý do:** *vì sao* quy tắc này tồn tại; chi phí hay rủi ro mà nó ngăn chặn.
- **Ví dụ:** một ví dụ tuân thủ và một ví dụ không tuân thủ; cụ thể tốt hơn trừu tượng.
- **Cách kiểm tra:** bài kiểm thử tự động, quy tắc linter hoặc bước rà soát xác minh nó.
- **Chủ sở hữu và ngày xem xét:** ai bảo trì nó và khi nào nó được xem xét lại tiếp theo.

Các trường lý do và "cách kiểm tra" là thứ phân biệt một tiêu chuẩn thực sự với một điều ước. Nếu bạn không thể nói vì sao một quy tắc tồn tại, hãy đặt câu hỏi liệu nó có nên tồn tại không. Nếu bạn không thể nói cách xác minh sự tuân thủ, quy tắc sẽ được áp dụng không nhất quán và bị phản cảm.

### Ghép mỗi tiêu chuẩn với một danh sách kiểm tra thực hành tốt

Tiêu chuẩn xác định đích đến. Một **danh sách kiểm tra thực hành tốt**, một danh sách ngắn, có thứ tự gồm các bước cụ thể hoặc các mục cần xác nhận, giúp mọi người đến đó và cho phép họ tự xác minh trước khi rà soát. Các sổ tay kỹ thuật khu vực công dùng mẫu này rất nhiều. **[NHS Wales](https://en.wikipedia.org/wiki/NHS_Wales)** và **Digital Health and Care Wales (DHCW)** công bố các tiêu chuẩn kỹ thuật kèm danh sách kiểm tra thực tế, và **[Dịch vụ Kỹ thuật số Chính phủ Anh](https://en.wikipedia.org/wiki/Government_Digital_Service) (GDS)** ghép Tiêu chuẩn Dịch vụ và Quy tắc Thực hành Công nghệ của mình với hướng dẫn có thể hành động của Sổ tay Dịch vụ. Danh sách kiểm tra là tiêu chuẩn được làm cho dùng được: "Bạn đã thêm kiểm toán khả năng tiếp cận chưa? Bạn đã kiểm thử với trình đọc màn hình chưa? Bạn đã bao phủ việc điều hướng chỉ bằng bàn phím chưa?" Xem chương 12.2 để biết mẫu danh sách kiểm tra đầy đủ.

### Công bố tiêu chuẩn ở nơi mọi người đã làm việc và giữ chúng dễ tìm thấy

Lưu tiêu chuẩn trong **[hệ thống quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control)** (một kho mã nguồn) dưới dạng Markdown, hiển thị thành một trang nội bộ có thể tìm kiếm, để chúng có lịch sử, rà soát qua pull request và so sánh khác biệt miễn phí, cùng một lập luận như với hồ sơ quyết định (chương 1.6). Một danh mục, một mẫu, một ô tìm kiếm. Việc hiển thị quan trọng không kém việc lưu trữ. Hãy liên kết tiêu chuẩn liên quan từ mẫu pull request, thông báo lỗi của linter và khung dựng sẵn của dịch vụ, để quy tắc đúng xuất hiện vào lúc làm việc thay vì trong một thư mục không ai ghé thăm.

### Thực thi bằng tự động hóa trước, rà soát của con người sau

Có hai cách để thực thi một tiêu chuẩn, và các tổ chức trưởng thành dùng cả hai một cách có chủ đích:

- **Thực thi tự động:** [linter](https://en.wikipedia.org/wiki/Lint_(software)), công cụ định dạng, [phân tích tĩnh](https://en.wikipedia.org/wiki/Static_program_analysis), chính sách dưới dạng mã (ví dụ **Open Policy Agent (OPA)**), các cổng **[tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI)**, và **hàm thích nghi kiến trúc** (các bài kiểm thử tự động khẳng định một thuộc tính thiết kế vẫn còn đúng). Tự động hóa nhất quán, không biết mệt, tức thì và không thể tranh cãi, khiến nó lý tưởng cho phần lớn tiêu chuẩn mang tính cơ học (định dạng, đặt tên, quy tắc phụ thuộc, siêu dữ liệu bắt buộc).
- **Rà soát của con người:** đánh giá mã, hội đồng rà soát kiến trúc và rà soát bảo mật, dành cho những gì máy không thể phán đoán: một phép trừu tượng có vững không, một sự đánh đổi có khôn ngoan không, *ý định* của một tiêu chuẩn có được đáp ứng không ngay cả khi câu chữ của nó vụng về.

Quy tắc ngón tay cái: **tự động hóa những gì kiểm tra được, và dành sự chú ý khan hiếm của con người cho phán đoán.** Mỗi tiêu chuẩn bạn chuyển được từ rà soát sang CI giải phóng người rà soát để làm việc suy nghĩ mà chỉ họ làm được.

### Quản trị các sai lệch bằng quy trình ngoại lệ/miễn trừ có tài liệu

Không tiêu chuẩn nào phù hợp mọi trường hợp, vì vậy hãy thiết kế lối thoát hiểm một cách có chủ đích. Một quy trình ngoại lệ tốt quy định:

- **Ai có thể cấp miễn trừ:** một thẩm quyền được nêu tên, chịu trách nhiệm, tương xứng với rủi ro (một trưởng nhóm kỹ thuật cho một sai lệch phong cách rủi ro thấp; một hội đồng kiến trúc hoặc bảo mật cho một miễn trừ biện pháp kiểm soát bảo mật). Điều này gắn trực tiếp với mô hình quản trị của chương 1.5.
- **Những gì phải được ghi lại:** tiêu chuẩn bị đi chệch, lý do cụ thể, phạm vi, các biện pháp kiểm soát bù hoặc giảm thiểu, và rủi ro được chấp nhận. Hãy ghi nhận điều này dưới dạng hồ sơ quyết định (chương 1.6) để lý do được lưu giữ.
- **Một thời hạn bắt buộc:** mọi miễn trừ đều **có thời hạn** với ngày kết thúc tường minh. Đây là quy tắc quan trọng nhất: nó ngăn một ngoại lệ tạm thời âm thầm trở thành chính sách vĩnh viễn.
- **Xem xét định kỳ:** một chủ sở hữu xem xét các miễn trừ đang mở theo chu kỳ và hoặc gia hạn chúng với lý do mới, đóng chúng khi công việc đã tuân thủ, hoặc, nếu cùng một ngoại lệ liên tục tái diễn, coi đó là bằng chứng *chính tiêu chuẩn* là sai và sửa đổi nó.

Điểm cuối này là trái tim của "ngoại lệ chứng minh quy tắc". Một dòng miễn trừ đều đặn chống lại một tiêu chuẩn không phải là thất bại của kỷ luật. Nó là dữ liệu. Nó cho bạn biết tiêu chuẩn bị hiệu chỉnh sai, và cách khắc phục là phát triển tiêu chuẩn, không phải tiếp tục cấp ngoại lệ.

### Coi tiêu chuẩn là tài liệu sống với quyền sở hữu rõ ràng

Hãy giao cho mỗi tiêu chuẩn một **chủ sở hữu** (một vai trò, không chỉ một người) chịu trách nhiệm giữ nó cập nhật, và một **chu kỳ xem xét** (ít nhất hằng năm). Cung cấp một con đường nhẹ để bất kỳ ai cũng có thể đề xuất thay đổi thông qua pull request hoặc một **[RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (yêu cầu góp ý)**, một đề xuất bằng văn bản được chuyển để lấy phản hồi trước khi áp dụng. Đánh phiên bản cho tiêu chuẩn, ngừng dùng chúng một cách tường minh, và thông báo các thay đổi. Một danh mục tiêu chuẩn không bao giờ được sửa đổi sẽ mục nát thành truyền thuyết mà mọi người trích dẫn có chọn lọc và ít tin cậy.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| **Nhiều tiêu chuẩn chi tiết** | Nhất quán, hội nhập dễ dàng, sẵn sàng kiểm toán | Cứng nhắc; gánh nặng bảo trì; có thể đi trước thực hành |
| **Ít tiêu chuẩn cấp cao** | Linh hoạt; ít bảo trì | Không nhất quán; tranh luận lại nhiều hơn ở mỗi đội |
| **Thực thi tự động** | Nhất quán, tức thì, không biết mệt, mở rộng được | Chi phí ban đầu; dương tính giả; mù trước ý định |
| **Thực thi bằng rà soát của con người** | Phán đoán ý định và sắc thái | Chậm, không nhất quán, là nút thắt ở quy mô lớn |
| **Nghiêm ngặt, không ngoại lệ** | Thông điệp đơn giản; không có gì để lách | Chặn công việc chính đáng; thúc đẩy việc không tuân thủ âm thầm |
| **Quy trình ngoại lệ được quản trị** | Giữ tiêu chuẩn đáng tin và nhân văn | Đòi hỏi quản trị, hồ sơ và việc theo dõi đến cùng |

Căng thẳng trung tâm là **nhất quán so với linh hoạt**. Một tiêu chuẩn tồn tại để loại bỏ sự biến thiên; một quy trình ngoại lệ tồn tại để chấp nhận sự biến thiên thực sự có lý do. Nghiêng quá xa về phía cứng nhắc và mọi người đi vòng qua các tiêu chuẩn của bạn. Nghiêng quá xa về phía lỏng lẻo và các tiêu chuẩn vô nghĩa. Quy trình ngoại lệ là van xả áp cho phép bạn giữ một lằn ranh vững chắc *và* trung thực với thực tế.

## Câu hỏi để thảo luận với đội của bạn

1. **Bao nhiêu tiêu chuẩn là con số phù hợp với quy mô của bạn, và các tiêu chuẩn của bạn đang trôi về phía cứng nhắc hay về phía thiếu nhất quán?** Bản thân danh mục là một sự đánh đổi: nhiều tiêu chuẩn chi tiết mua được sự nhất quán, hội nhập dễ dàng và sẵn sàng kiểm toán với cái giá là sự cứng nhắc và gánh nặng bảo trì, trong khi ít tiêu chuẩn cấp cao vẫn linh hoạt nhưng để mỗi đội tranh luận lại cùng những câu hỏi. Với một doanh nghiệp lớn hoặc cơ quan chính phủ, kích thước phù hợp phụ thuộc vào mức độ biến thiên bạn thực sự chấp nhận được so với mức độ kiểm toán viên và việc hội nhập cần được ghim chặt. Hãy mang bằng chứng: bạn có bao nhiêu tiêu chuẩn đang hiệu lực, bao nhiêu được xem xét trong năm qua, và các đội tranh luận lại những điều mà một tiêu chuẩn có thể đã giải quyết thường xuyên đến mức nào. Một danh mục đi trước thực hành trở thành truyền thuyết, và một danh mục quá mỏng đẩy chi phí sang mọi đội. Hãy quyết định có chủ đích điều gì xứng đáng có tiêu chuẩn, và cắt bỏ những tiêu chuẩn không còn xứng đáng với chỗ đứng của mình.

2. **Ở đâu câu chữ của một tiêu chuẩn được thông qua tự động trong khi ý định của nó bị vi phạm một cách âm thầm, và bạn sẽ phát hiện điều đó như thế nào?** Tự động hóa nhất quán, không biết mệt và mù trước ý định, nghĩa là một linter hay kiểm tra chính sách có thể báo xanh trong khi mục tiêu thực sự (một phép trừu tượng vững chắc, một sự đánh đổi khôn ngoan, một trang thực sự dễ tiếp cận) bị bỏ lỡ. Quy tắc ngón tay cái là tự động hóa những gì kiểm tra được và dành rà soát khan hiếm của con người cho phán đoán, và phần khó là thống nhất những tiêu chuẩn nào có ý định mà không cổng CI nào khẳng định được. Hãy mang ví dụ: những tiêu chuẩn mà mọi người thỏa mãn đúng câu chữ nhưng đánh bại mục đích, chẳng hạn một điểm cuối kiểm tra sức khỏe báo khỏe mạnh trong khi dịch vụ đã hỏng, hay mã vượt qua công cụ định dạng nhưng che khuất ý nghĩa. Trong bối cảnh chịu quy định, ý định quan trọng nhất đối với các biện pháp kiểm soát an toàn và bảo mật, nơi một ô đánh dấu xanh có thể che giấu rủi ro thực. Hãy quyết định những tiêu chuẩn nào giữ một người rà soát chuyên để phán đoán ý định, và diễn đạt các tiêu chuẩn đó quanh kết quả để cả máy và người rà soát cùng nhắm vào một mục tiêu.

3. **Ai sở hữu vòng phản hồi từ miễn trừ đến tiêu chuẩn, và đến thời điểm nào một ngoại lệ tái diễn buộc bạn phải thay đổi quy tắc?** Một dòng miễn trừ đều đặn chống lại một tiêu chuẩn là dữ liệu, không phải sự vô kỷ luật, và tín hiệu bị lãng phí trừ khi có ai đó chịu trách nhiệm đọc và hành động. Cân nhắc đối lập là sửa đổi một tiêu chuẩn là công việc thực sự, nên việc tiếp tục đóng dấu các miễn trừ vẫn dễ hơn việc sửa quy tắc bị hiệu chỉnh sai bên dưới chúng. Hãy mang các con số: tiêu chuẩn nào tạo ra nhiều ngoại lệ nhất, các miễn trừ có thực sự được đặt thời hạn và xem xét theo chu kỳ không, và bao nhiêu cái đã âm thầm trở thành vĩnh viễn. Với các tiêu chuẩn quan trọng về an toàn và bảo mật trong doanh nghiệp và chính phủ, một miễn trừ phải ghi lại các biện pháp kiểm soát bù, một biện pháp giảm thiểu, rủi ro được chấp nhận và một thời hạn cứng, nếu không một sai lệch tạm thời trở thành chính sách không có tài liệu, nổi lên trong lần kiểm toán tiếp theo. Hãy chỉ định một chủ sở hữu để xem xét các miễn trừ đang mở, đặt một ngưỡng tại đó các ngoại lệ lặp lại kích hoạt việc sửa đổi tiêu chuẩn, và coi một ngoại lệ vĩnh viễn là lỗi của tiêu chuẩn cần được khắc phục.

4. **Tiêu chuẩn đúng có xuất hiện vào lúc làm việc không, hay nó nằm trong một thư mục không ai mở?** Một tiêu chuẩn không ai tìm thấy được thực thi bằng may rủi, và ở quy mô lớn phần lớn việc không tuân thủ không phải là sự thách thức mà là sự thiếu hiểu biết: một kỹ sư chưa bao giờ biết quy tắc tồn tại hoặc không thể tìm thấy nó khi cần. Cân nhắc đối lập là công sức, vì việc hiển thị một tiêu chuẩn trong mẫu pull request, thông báo lỗi của linter và khung dựng sẵn của dịch vụ tốn công sức tích hợp thực sự mà một trang trung tâm duy nhất không cần. Hãy mang bằng chứng về khả năng tìm thấy: các kỹ sư thực sự tìm tiêu chuẩn hiện nay bằng cách nào, một nhân viên mới có thể tìm quy tắc về khả năng tiếp cận hay bảo mật chi phối nhiệm vụ của họ trong chưa đầy một phút không, và người rà soát trích dẫn một tiêu chuẩn mà tác giả đơn giản chưa từng thấy thường xuyên đến mức nào. Với một doanh nghiệp lớn hoặc cơ quan chính phủ, kiểm toán viên ngày càng hỏi không chỉ liệu một tiêu chuẩn có tồn tại mà còn liệu nó có được truyền đạt và tiếp cận được tại thời điểm quyết định, vì vậy hãy coi việc hiển thị là một phần của tiêu chuẩn, không phải nghĩ đến sau, và đo xem mọi người có đến được quy tắc khi họ cần hay không.

5. **Ai sở hữu từng tiêu chuẩn đang hiệu lực, lần xem xét cuối cùng là khi nào, và làm sao bạn phát hiện những tiêu chuẩn đã âm thầm mục nát thành truyền thuyết?** Tiêu chuẩn phân rã một cách âm thầm: một quy tắc viết cách đây ba năm cho một khung bạn không còn dùng vẫn nằm trong danh mục, được trích dẫn có chọn lọc và ít tin cậy, kéo tụt uy tín của những tiêu chuẩn vẫn còn đúng. Với một tổ chức lớn, chi phí của quyền sở hữu chính là chu kỳ xem xét, vốn có cảm giác như chi phí cho đến khi một sự cố hay kiểm toán phơi bày một tiêu chuẩn không còn khớp với thực tế. Hãy mang các con số vào cuộc thảo luận: bao nhiêu tiêu chuẩn có chủ sở hữu được nêu tên (một vai trò, không chỉ một cá nhân đã rời đi), bao nhiêu được xem xét trong năm qua, bao nhiêu được chính thức ngừng dùng so với chỉ lỗi thời, và cái nào được trích dẫn nhiều nhất và ít nhất. Trong bối cảnh doanh nghiệp và chính phủ, kiểm toán viên mong mỗi tiêu chuẩn có phiên bản, có ngày và chứng minh được là hiện hành, vì vậy hãy thống nhất một chu kỳ xem xét tối thiểu, giao mỗi tiêu chuẩn cho một chủ sở hữu chịu trách nhiệm, và loại bỏ những tiêu chuẩn không còn xứng đáng với chỗ đứng trước khi chúng làm suy yếu niềm tin vào phần còn lại.

6. **Thẩm quyền cấp miễn trừ có thực sự tương xứng với rủi ro của tiêu chuẩn đang được miễn trừ không?** Một sai lệch về phong cách và một sai lệch về biện pháp kiểm soát bảo mật không phải là cùng một quyết định, nhưng nhiều tổ chức hoặc đẩy cả hai đến một hội đồng nặng nề (làm công việc chính đáng dừng hẳn lại) hoặc để cả hai trôi qua một trưởng nhóm kỹ thuật duy nhất (cho phép một rủi ro nghiêm trọng được chấp nhận bởi người không có thẩm quyền chấp nhận nó). Căng thẳng là tốc độ so với trách nhiệm giải trình: quá nhiều ma sát phê duyệt thúc đẩy việc không tuân thủ âm thầm, trong khi quá ít nghĩa là các sai lệch hệ trọng bị cho qua trong một luồng trò chuyện. Hãy mang một bản đồ các tiêu chuẩn của bạn với các thẩm quyền phê duyệt, cùng một mẫu các miễn trừ được cấp gần đây, và kiểm tra xem có ai đã miễn trừ một biện pháp kiểm soát quan trọng về an toàn hay bảo mật mà không có hội đồng tương ứng, biện pháp kiểm soát bù, biện pháp giảm thiểu và việc chấp nhận rủi ro được ghi lại hay không. Với doanh nghiệp và chính phủ, đây là câu hỏi về phân tách nhiệm vụ mà các cơ quan quản lý xem xét trực tiếp, vì vậy hãy gắn mỗi loại tiêu chuẩn với một thẩm quyền được nêu tên tương xứng với rủi ro của nó, và bảo đảm người chấp nhận rủi ro thực sự chịu trách nhiệm về hậu quả.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Giữ danh mục thật nhỏ: chỉ viết ra một nhúm quy tắc mà sự vắng mặt của chúng thực sự gây hại cho bạn, như cấu hình công cụ định dạng, yêu cầu kiểm tra sức khỏe và các trang có thể điều hướng bằng bàn phím, và thực thi từng quy tắc bằng một linter hoặc kiểm tra CI thay vì một cuộc họp rà soát. Bỏ hẳn hội đồng miễn trừ; một TODO có ngày trong mã và một ghi chú một dòng trong pull request là một ngoại lệ có thời hạn hoàn toàn tốt ở quy mô này. Nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ thuật, vì vậy hãy cưỡng lại việc soạn tiêu chuẩn cho những vấn đề bạn chưa có.

**Doanh nghiệp nhỏ.** Không có chủ sở hữu tiêu chuẩn riêng và ngân sách eo hẹp, hãy mua tiêu chuẩn thay vì xây dựng: áp dụng các đường cơ sở đã công bố như Tiêu chuẩn Dịch vụ GDS của Anh, hướng dẫn bảo mật OWASP, hoặc các quy tắc lint được khuyến nghị của khung của bạn, và dựa vào các kiểm tra đã tích hợp sẵn trong công cụ và CI lưu trữ của bạn. Giữ một trang ngắn các quy tắc địa phương cho những điều thực sự đặc thù với bạn. Ai lãnh đạo kỹ thuật thì cấp và ghi lại các ngoại lệ trong phiếu việc, kèm ngày hết hạn, để ngay cả một quy trình nhẹ cũng trung thực.

**Doanh nghiệp lớn.** Công việc là quản trị trên nhiều đội: một danh mục, một mẫu, lý do và ví dụ cho mọi tiêu chuẩn, và chính sách dưới dạng mã làm hỏng đường ống cho phần lớn tiêu chuẩn mang tính cơ học. Vận hành một quy trình miễn trừ có thẩm quyền phê duyệt tương xứng với rủi ro, đặt thời hạn cho mọi ngoại lệ, xem xét các miễn trừ đang mở theo chu kỳ, và khai thác các miễn trừ tái diễn như tín hiệu rằng một tiêu chuẩn cần thay đổi. Đo tỷ lệ tiêu chuẩn được thực thi tự động và khối lượng cùng tuổi của các miễn trừ đang mở, và báo cáo cả hai cho chức năng quản trị để các tiêu chuẩn vẫn là một hệ thống được quản lý thay vì một nghĩa địa.

**Chính phủ.** Hãy công bố công khai các tiêu chuẩn kỹ thuật của bạn theo truyền thống DHCW và GDS, và ghép mỗi tiêu chuẩn với một danh sách kiểm tra mà các đội hoàn thành trước một cuộc đánh giá dịch vụ, để sự tuân thủ hiển thị với công chúng và cơ quan giám sát. Giao cho một chủ sở hữu cấp cao có trách nhiệm được nêu tên làm thẩm quyền cho các miễn trừ hệ trọng, và yêu cầu mọi ngoại lệ ghi lại tiêu chí cụ thể, biện pháp kiểm soát bù hoặc biện pháp giảm thiểu tạm thời, kế hoạch khắc phục và một thời hạn cứng. Quy tắc mua sắm và minh bạch có nghĩa là cả tiêu chuẩn lẫn các sai lệch của bạn đều trở thành một phần của hồ sơ công khai, vì vậy hãy coi khả năng kiểm toán và truy vết là yêu cầu thiết kế ngay từ đầu.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bảy người giữ đúng ba tiêu chuẩn bằng văn bản (cấu hình công cụ định dạng chung, yêu cầu điểm cuối kiểm tra sức khỏe, và "mọi trang công khai phải điều hướng được bằng bàn phím"), mỗi tiêu chuẩn được thực thi bằng một linter hoặc kiểm tra CI thay vì một cuộc họp rà soát. Khi một kỹ sư cần phát hành một bản mẫu thử bỏ đi vi phạm quy tắc kiểm tra sức khỏe, không có hội đồng miễn trừ: cô để lại một TODO có ngày trong mã và một ghi chú một dòng trong pull request nói vì sao và khi nào cô sẽ sửa. Đó là một ngoại lệ có thời hạn ở quy mô khởi nghiệp, trung thực và hiển thị mà không tốn chi phí quy trình. Ba kiểm tra này tự hoàn vốn bằng cách giữ cho đánh giá mã xoay quanh nội dung thay vì phong cách.

**Doanh nghiệp lớn.** Một ngân hàng toàn cầu duy trì một sổ tay kỹ thuật nội bộ gồm khoảng bốn mươi tiêu chuẩn đang hiệu lực, mỗi tiêu chuẩn theo một mẫu với lý do, ví dụ và một danh sách kiểm tra thực hành tốt được liên kết. Khoảng 70% được thực thi tự động: định dạng, chính sách phụ thuộc, siêu dữ liệu dịch vụ bắt buộc, và các biện pháp kiểm soát bảo mật được mã hóa thành chính sách dưới dạng mã làm hỏng đường ống CI. Một đội thanh toán cần phát hành trên một cơ sở dữ liệu chưa hỗ trợ một tính năng mã hóa bắt buộc. Thay vì chặn bản phát hành, họ nộp một miễn trừ nêu tên tiêu chuẩn, biện pháp kiểm soát bù ([mã hóa](https://en.wikipedia.org/wiki/Encryption) ở tầng ứng dụng) và thời hạn 90 ngày. Hội đồng bảo mật cấp nó và ghi lại. Chín mươi ngày sau, cuộc xem xét thấy nền tảng nay hỗ trợ tính năng đó nguyên bản, và miễn trừ được đóng. Tiêu chuẩn được giữ vững, công việc được phát hành, và sai lệch hoàn toàn truy vết được cho lần kiểm toán tiếp theo.

**Chính phủ.** Một cơ quan y tế quốc gia theo mô hình cách tiếp cận DHCW và GDS công bố công khai các tiêu chuẩn kỹ thuật của mình, mỗi tiêu chuẩn được ghép với một danh sách kiểm tra mà các đội hoàn thành trước một cuộc đánh giá dịch vụ. Khả năng tiếp cận theo WCAG 2.2 AA là một tiêu chuẩn cứng, được thực thi bằng kiểm toán tự động trong CI cộng với đánh giá thủ công. Một hệ thống lâm sàng cũ không thể ngay lập tức đáp ứng một tiêu chí về khả năng tiếp cận mà không gây rủi ro cho chức năng quan trọng về an toàn bệnh nhân. Đội yêu cầu một ngoại lệ có thời hạn. Một chủ sở hữu cấp cao có trách nhiệm được nêu tên cấp nó, và ghi lại tiêu chí cụ thể, biện pháp giảm thiểu tạm thời (một đường dây điện thoại hỗ trợ tiếp cận), kế hoạch khắc phục và thời hạn sáu tháng, tạo ra đúng bằng chứng truy vết được, rà soát được mà các cơ quan giám sát yêu cầu (chương 4.6, 10.4).

## Luận chứng kinh doanh: động lực, ROI và TCO

Một tiêu chuẩn tốn thời gian để viết, tự động hóa việc kiểm tra và bảo trì nó. Lợi tức được trả mỗi lần kiểm tra chạy, và mỗi lần một kỹ sư không phải dừng lại tranh luận một câu hỏi đã giải quyết. Tiêu chuẩn chuyển chi phí quyết định lặp lại, phân tán thành chi phí soạn thảo một lần, cùng một kinh tế học như hồ sơ quyết định (chương 1.6), được khuếch đại vì một tiêu chuẩn chi phối hàng nghìn trường hợp tương lai, không phải một lựa chọn trong quá khứ.

Về **tổng chi phí sở hữu (TCO)**, tức toàn bộ chi phí vòng đời của việc xây dựng, vận hành và bảo trì một hệ thống, tiêu chuẩn giảm các khoản mục lớn nhất: hội nhập (nhân viên mới thừa hưởng sự nhất quán thay vì dịch ngược nó), bảo trì (mã đồng nhất rẻ hơn để thay đổi), và đảm bảo (kiểm toán rẻ hơn khi sự tuân thủ có thể kiểm tra bằng máy và các sai lệch đã được lập tài liệu). Quy trình ngoại lệ bảo vệ ROI đó khỏi mối đe dọa chính của nó: tiêu chuẩn thoái hóa thành truyền thuyết bị phớt lờ. Một quy trình miễn trừ đáng tin giữ cho tiêu chuẩn được tin cậy, và các tiêu chuẩn được tin cậy là những tiêu chuẩn mọi người thực sự tuân theo. Chi phí của việc bỏ qua tất cả điều này là vô hình trên mọi bảng điều khiển. Nó hiện ra ở việc hội nhập chậm, chất lượng không nhất quán và các phát hiện kiểm toán, và nó cộng dồn với mỗi đội mới và mỗi lần có người ra đi.

## Phản mẫu và cạm bẫy

- **Quy tắc không có lý do:** một tiêu chuẩn không ai hiểu là tiêu chuẩn không ai áp dụng đúng hay thách thức một cách trung thực được.
- **Tiêu chuẩn mang tính khát vọng, không kiểm tra được:** "mã nên dễ bảo trì" là một giá trị, không phải một tiêu chuẩn; nó không thể thực thi hay tranh cãi.
- **Không có quy trình ngoại lệ:** buộc phải chọn sai lầm giữa việc chặn công việc chính đáng và dung thứ việc không tuân thủ âm thầm.
- **Ngoại lệ vĩnh viễn:** các miễn trừ không có hạn đã âm thầm trở thành chính sách thực sự, không có tài liệu.
- **Miễn trừ không có hồ sơ:** sai lệch được cấp ngoài hành lang hoặc trong luồng trò chuyện, vô hình với lần kiểm toán tiếp theo và kỹ sư tiếp theo.
- **Phớt lờ tín hiệu:** cấp cùng một ngoại lệ nhiều lần thay vì đọc nó như bằng chứng tiêu chuẩn cần thay đổi.
- **Thực thi bằng cằn nhằn:** dựa vào người rà soát để bắt những gì một linter nên bắt, lãng phí phán đoán vào phần cơ học.
- **Nghĩa địa tiêu chuẩn:** một danh mục viết một lần, không ai sở hữu, không bao giờ được xem xét, được trích dẫn có chọn lọc, ít người tin.
- **Canh cổng bằng biệt ngữ:** tiêu chuẩn viết cho tác giả của chúng thay vì cho người đọc, không có ví dụ để sao chép.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** Tiêu chuẩn là kiến thức truyền miệng trong đầu các kỹ sư cấp cao, được áp dụng một cách phản ứng. Thực thi là cằn nhằn trong đánh giá mã tùy nghi; sai lệch vô hình; "cách chúng ta làm" khác nhau theo đội và theo người rà soát thay đổi.
- **Mức 2 (Phát triển):** Một số tiêu chuẩn được viết ra, theo định dạng không nhất quán và ở các vị trí rải rác, và mức áp dụng khác nhau nhiều giữa các đội. Thực thi chủ yếu thủ công. Ngoại lệ diễn ra phi chính thức, không có hồ sơ hay ngày hết hạn.
- **Mức 3 (Chuẩn hóa):** Một danh mục duy nhất, một mẫu, lý do và ví dụ cho mỗi tiêu chuẩn, và các danh sách kiểm tra thực hành tốt, được áp dụng nhất quán giữa các đội. Thực thi tự động cho phần lớn mang tính cơ học. Một quy trình ngoại lệ có tài liệu với người phê duyệt được nêu tên, lý do được ghi lại và các miễn trừ có thời hạn.
- **Mức 4 (Quản lý):** Hệ thống tiêu chuẩn được đo theo các đường cơ sở. Bạn theo dõi tỷ lệ tiêu chuẩn được thực thi tự động so với bằng rà soát của con người, khối lượng miễn trừ cho mỗi tiêu chuẩn, thời gian đóng, và bao nhiêu miễn trừ hết hạn khi vẫn còn mở, và bạn báo cáo những điều này cho chức năng quản trị. Thẩm quyền phê duyệt tương xứng với rủi ro và được kiểm toán; chu kỳ xem xét và hạn chót được thực thi dựa trên bằng chứng thay vì thiện chí; một tiêu chuẩn có tỷ lệ miễn trừ vượt ngưỡng đã thống nhất sẽ được đánh dấu để sửa đổi.
- **Mức 5 (Điều phối):** Tiêu chuẩn được hiển thị vào lúc làm việc và được thực thi bởi chính sách dưới dạng mã và hàm thích nghi. Miễn trừ được khai thác như tín hiệu để các ngoại lệ tái diễn liên tục thúc đẩy tiêu chuẩn tiến hóa, và danh mục được cân bằng lại khi thực hành dịch chuyển. Tiêu chuẩn, danh sách kiểm tra và miễn trừ là một hệ thống sống thích ứng duy nhất, tích hợp xuyên suốt hội nhập, phân phối và kiểm toán.

## Ý tưởng để thảo luận

1. Những tiêu chuẩn nào của bạn có thể được nêu bằng một quy tắc kiểm thử được *và* một lý do rõ ràng, và những tiêu chuẩn nào thực chất chỉ là khát vọng?
2. Tỷ lệ tiêu chuẩn của bạn được thực thi tự động so với do người rà soát nhận ra là bao nhiêu? Cần gì để chuyển thêm mười tiêu chuẩn vào CI?
3. Sai lệch diễn ra ở đâu hiện nay, và bạn có biết không? Chúng có được ghi lại và đặt thời hạn, hay âm thầm?
4. Ai được phép cấp miễn trừ cho tiêu chuẩn quan trọng nhất về an toàn hay bảo mật của bạn, và thẩm quyền đó có tương xứng với rủi ro không?
5. Hãy nhìn vào tiêu chuẩn bị miễn trừ nhiều nhất của bạn. Đó là vấn đề kỷ luật, hay tiêu chuẩn đơn giản là sai?
6. Mỗi tiêu chuẩn đang hiệu lực được xem xét lần cuối khi nào, và ai sở hữu nó? Những tiêu chuẩn nào đã âm thầm trở thành truyền thuyết?

## Những điểm cần ghi nhớ

- Một tiêu chuẩn kỹ thuật là **một quy tắc được nêu như một kết quả, với lý do, ví dụ và cách kiểm tra**: nếu không kiểm tra được thì chưa phải là tiêu chuẩn.
- Ghép mỗi tiêu chuẩn với một **danh sách kiểm tra thực hành tốt** để mọi người tự xác minh, theo mẫu sổ tay khu vực công (NHS Wales / DHCW, GDS của Anh).
- Lưu tiêu chuẩn trong **hệ thống quản lý phiên bản**, giữ chúng **sống** với chủ sở hữu được nêu tên và ngày xem xét, và hiển thị chúng vào lúc làm việc.
- **Tự động hóa những gì kiểm tra được** bằng linter, chính sách dưới dạng mã và hàm thích nghi; dành **rà soát của con người** cho phán đoán.
- Quản trị sai lệch bằng một **quy trình ngoại lệ/miễn trừ có tài liệu, có thời hạn**: người phê duyệt được nêu tên, lý do được ghi lại, hạn chót bắt buộc, xem xét định kỳ.
- Một ngoại lệ tái diễn là **tín hiệu để sửa tiêu chuẩn**, không chỉ tiếp tục cấp miễn trừ: "ngoại lệ chứng minh quy tắc". Xem các chương 1.5 (quản trị), 1.6 (hồ sơ quyết định), 2.1 (tiêu chuẩn viết mã), 12.2 (danh sách kiểm tra) và 12.3 (mẫu biểu).

## Tài liệu tham khảo và đọc thêm

- UK Government Digital Service, *Government Service Standard*, *Technology Code of Practice* và *GOV.UK Service Manual*.
- NHS Digital / NHS England, *Service Standard* và hướng dẫn kỹ thuật.
- Digital Health and Care Wales (DHCW) / NHS Wales, các tiêu chuẩn kỹ thuật và danh sách kiểm tra thực hành tốt đã công bố.
- Scott Bradner, *RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels* (IETF, 1997).
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Neal Ford, Rebecca Parsons và Patrick Kua, *Building Evolutionary Architectures* (hàm thích nghi như quản trị tự động).
- Torin Sandall và cộng sự, tài liệu *Open Policy Agent* (chính sách dưới dạng mã).
- GitLab, *The GitLab Handbook*: một ví dụ công khai về các tiêu chuẩn tổ chức sống, được quản lý phiên bản.
- Google, *Software Engineering at Google* (Winters, Manshreck, Wright): tiêu chuẩn, khả năng đọc và thực thi tự động ở quy mô lớn.
- Atul Gawande, *The Checklist Manifesto*: lập luận cho danh sách kiểm tra như thực hành chuyên nghiệp.
