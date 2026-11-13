# 4.7 Quản lý danh tính và truy cập

## Tổng quan và động lực

Mọi yêu cầu chạm vào hệ thống của bạn mang một tuyên bố ngầm: *tôi được phép làm điều này*. Quản lý danh tính và truy cập (IAM) là kỷ luật quyết định liệu tuyên bố đó có đúng không. Nó trả lời hai câu hỏi riêng biệt mà người ta liên tục nhập nhằng. [Xác thực](https://en.wikipedia.org/wiki/Authentication) chứng minh bạn là ai. [Cấp quyền](https://en.wikipedia.org/wiki/Authorization) quyết định bạn được làm gì một khi đã chứng minh. Hãy giữ hai ý tưởng đó tách biệt trong đầu và một nửa sự nhầm lẫn trong lĩnh vực này biến mất.

Với các đội lớn, danh tính đã lặng lẽ trở thành biện pháp kiểm soát quan trọng nhất bạn sở hữu. Chương 4.3 nêu điểm rằng danh tính là chu vi mới, và chương 4.1 xây không tin cậy trên nó: khi bạn ngừng tin mạng, thứ duy nhất còn lại để tin là một danh tính đã xác minh và một chính sách tường minh. Sự dịch chuyển đó nghĩa là một luồng đặt lại mật khẩu yếu hay một tài khoản dịch vụ bị quên không còn là một lỗi nhỏ. Nó là cửa trước. Hầu hết các vụ xâm phạm thực không phải khai thác khéo léo các lỗi an toàn bộ nhớ; chúng là thông tin xác thực bị đánh cắp, quyền hạn quá rộng, và các tài khoản lẽ ra phải tắt từ nhiều tháng trước.

Rủi ro tăng trong bối cảnh doanh nghiệp và chính phủ. Một doanh nghiệp toàn cầu xoay xở hàng chục thư mục chồng lấn, hàng nghìn người gia nhập và rời đi mỗi tháng, và các đối tác cần truy cập có phạm vi vào một lát hệ thống của bạn. Một cơ quan chính phủ chồng thêm thông tin xác thực thẻ thông minh, mức bảo đảm danh tính bắt buộc, và kiểm toán viên sẽ hỏi, bằng văn bản, chính xác ai có thể chạm vào một bản ghi nhất định vào một ngày nhất định. Chương này có chính kiến về cách xây một tầng danh tính trả lời tốt những câu hỏi đó mà không làm mọi người đình trệ.

## Các nguyên tắc chính

- **Xác thực và cấp quyền là các vấn đề khác nhau.** Chứng minh danh tính và cấp quyền cần thiết kế riêng và rà soát riêng.
- **Một danh tính, nhiều hệ thống.** Hợp nhất về một nguồn sự thật duy nhất cho mỗi quần thể danh tính; sự lan tràn thư mục là một lỗi bảo mật.
- **Đặc quyền tối thiểu theo mặc định.** Bắt đầu từ không truy cập và thêm có chủ đích, cho cả con người lẫn máy.
- **Mọi thông tin xác thực đều tạm thời.** Ưu tiên thông tin xác thực sống ngắn, được cấp tự động hơn các bí mật sống lâu.
- **Thu hồi cung cấp quan trọng ngang cung cấp.** Quyền truy cập sống lâu hơn nhu cầu là rủi ro thuần túy.
- **Chống lừa đảo thắng dễ nhớ.** Chuyển xác thực về hướng passkey và các yếu tố có phần cứng hậu thuẫn.
- **Máy cũng là danh tính.** Khối lượng công việc, đường ống và dịch vụ cần danh tính được quản lý, không phải khóa tĩnh dùng chung.
- **Truy cập là một vòng đời, không phải một sự kiện.** Cấp, rà soát và thu hồi theo lịch, và chứng minh bạn đã làm.

## Khuyến nghị

### Tách xác thực khỏi cấp quyền, và tập trung cả hai

Hãy xác thực qua một nhà cung cấp danh tính (IdP) duy nhất, một hệ thống xác minh danh tính và phát hành token mà các hệ thống khác tin cậy. Rồi để mỗi ứng dụng tự đưa ra quyết định cấp quyền từ danh tính và thuộc tính mà token đó mang. Sự tách này cho phép bạn tăng cường xác thực một lần, cho mọi người, trong khi giữ logic quyền mịn gần dữ liệu nó bảo vệ. Hãy áp dụng [đăng nhập một lần](https://en.wikipedia.org/wiki/Single_sign-on) (SSO), nơi một lần xác thực cấp quyền truy cập nhiều ứng dụng, để người của bạn có một đăng nhập mạnh thay vì bốn mươi đăng nhập yếu. Liên kết mở rộng cùng sự tin cậy qua ranh giới tổ chức, cho phép danh tính của một đối tác truy cập hệ thống của bạn mà bạn không phải quản lý mật khẩu của họ.

### Dùng các giao thức hiện đại cho đúng việc của từng cái

Ba tiêu chuẩn làm phần lớn công việc, và mỗi cái có một việc. **OpenID Connect (OIDC)** là một tầng danh tính xây trên [OAuth](https://en.wikipedia.org/wiki/OAuth) 2.0; hãy dùng nó để trả lời *người dùng này là ai* cho đăng nhập web và di động. **OAuth 2.0** là một khung cấp quyền cho truy cập ủy thác; hãy dùng nó để cho một ứng dụng gọi một API thay mặt người dùng mà không bao giờ thấy mật khẩu của họ (chương 2.3). **Security Assertion Markup Language (SAML)** là tiêu chuẩn liên kết dựa trên XML cũ hơn; nó vẫn là con ngựa thồ cho SSO doanh nghiệp vào các ứng dụng kinh doanh đã thiết lập. Một sai lầm phổ biến là với tới OAuth để xác thực trực tiếp. OAuth cấp quyền truy cập tài nguyên; OIDC nằm trên nó để thiết lập danh tính. Hãy chọn OIDC cho đăng nhập hướng người dùng mới, giữ SAML ở nơi danh mục doanh nghiệp của bạn đòi hỏi, và đừng phát minh định dạng token riêng.

### Làm cho xác thực chống lừa đảo

Mật khẩu một mình không thể phòng thủ ở quy mô lớn. Hãy yêu cầu xác thực đa yếu tố (MFA), kết hợp thứ bạn biết, thứ bạn có, và thứ bạn là, cho mọi tài khoản con người không ngoại lệ. Rồi vượt qua các yếu tố yếu: mã dùng một lần qua SMS có thể bị lừa đảo và hoán đổi SIM. Đích đến mạnh là [passkey](https://en.wikipedia.org/wiki/Passkey) và tiêu chuẩn WebAuthn nền tảng (một API trình duyệt cho xác thực khóa công khai), gắn một đăng nhập với khóa riêng do phần cứng nắm giữ và với nguồn gốc của trang thật, nên một trang giả không thể thu thập thứ gì đáng đánh cắp. Passkey cũng không cần mật khẩu, điều người dùng của bạn sẽ cảm ơn. Hãy coi khôi phục tài khoản và đặt lại mật khẩu là một phần của bề mặt xác thực, vì kẻ tấn công không đánh bại được MFA của bạn sẽ đơn giản tấn công luồng đặt lại thay thế.

### Quản lý vòng đời gia nhập-chuyển đổi-rời đi, và thu hồi nhanh

Danh tính là một vòng đời. Một **người gia nhập** cần đúng quyền truy cập từ ngày đầu. Một **người chuyển đổi** thay đổi vai trò cần quyền mới và, quan trọng, cần quyền cũ bị gỡ, nếu không họ từ từ tích lũy chìa khóa cả tòa nhà. Một **người rời đi** phải mất mọi quyền truy cập ngay, lý tưởng trong vài phút sau ngày cuối, qua mọi hệ thống. Hãy điều khiển điều này từ một nguồn có thẩm quyền, thường là hệ thống nhân sự, để một thay đổi trạng thái ở đó tự động cung cấp và thu hồi ở hạ nguồn. Hãy tự động hóa nó. Danh sách kiểm tra thôi việc thủ công luôn bỏ sót thứ gì đó, và tài khoản bị bỏ sót là cái xuất hiện trong báo cáo sự cố.

### Chọn một mô hình cấp quyền và biểu đạt nó dưới dạng chính sách-dưới-dạng-mã

Hãy cấp quyền bằng [kiểm soát truy cập dựa trên vai trò](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC), nơi bạn gán quyền cho các vai trò theo chức năng công việc và gán người vào vai trò, vì nó đơn giản để suy luận và dễ kiểm toán. Hãy với tới [kiểm soát truy cập dựa trên thuộc tính](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) ở nơi bạn cần các quyết định nhận biết ngữ cảnh dựa trên thuộc tính như phòng ban, phân loại dữ liệu, vị trí, hay thời điểm trong ngày. Hầu hết các tổ chức trưởng thành chạy lai: RBAC cho các cấp quyền thô, ABAC cho các điều kiện mịn. Dù bạn chọn gì, hãy biểu đạt cấp quyền dưới dạng **chính sách-dưới-dạng-mã**: các quy tắc được viết ở dạng được quản lý phiên bản, kiểm thử được, rà soát được thay vì bấm vào một bảng điều khiển. Chính sách-dưới-dạng-mã làm các quyết định truy cập kiểm toán được, so sánh được và nhất quán qua các môi trường, và cho phép bạn kiểm thử một thay đổi quyền trước khi nó được phát hành.

### Thực thi đặc quyền tối thiểu bằng truy cập đúng-lúc và PAM

Áp dụng [nguyên tắc đặc quyền tối thiểu](https://en.wikipedia.org/wiki/Principle_of_least_privilege): mọi danh tính nhận quyền truy cập tối thiểu nó cần và không hơn. Đặc quyền thường trực là kẻ thù, vì một quyền được cấp vĩnh viễn là quyền sẵn có cho bất kỳ kẻ tấn công nào đáp xuống tài khoản đó vào bất kỳ lúc nào. Hãy ưu tiên **truy cập đúng-lúc (JIT)**, nơi một người yêu cầu quyền nâng cao trong một cửa sổ có giới hạn, nhận chúng sau khi phê duyệt, và mất chúng tự động khi cửa sổ đóng. Với các tài khoản nguy hiểm nhất của bạn, hãy áp dụng **quản lý truy cập đặc quyền (PAM)**: một hệ thống cất giữ thông tin xác thực quản trị, trung gian và ghi lại các phiên đặc quyền, và cấp nâng quyền theo yêu cầu. Mục tiêu là không có truy cập quản trị thường trực, để ngay cả một laptop bị xâm phạm hoàn toàn cũng không mang lại gì bền vững.

### Cho máy và khối lượng công việc danh tính thực

Con người chỉ là một nửa danh tính của bạn. Dịch vụ, đường ống, container và hàm đều xác thực với thứ gì đó, và quá thường xuyên chúng làm vậy bằng một bí mật sống lâu dán vào tệp cấu hình. Hãy thay khóa tĩnh bằng **danh tính khối lượng công việc** được quản lý: thông tin xác thực sống ngắn được cấp tự động cho một khối lượng công việc dựa trên nơi nó chạy và nó là gì. Dùng TLS tương hỗ (mTLS), nơi cả hai phía của một kết nối xuất trình chứng chỉ, cho xác thực dịch vụ-với-dịch vụ. Giữ mọi bí mật còn lại trong một trình quản lý bí mật chuyên dụng có xoay vòng, không bao giờ trong mã nguồn hay ảnh (chương 4.2). Thông tin xác thực khối lượng công việc sống ngắn, xoay vòng tự động loại bỏ nguyên nhân phổ biến nhất của rò rỉ thông tin xác thực đám mây.

### Biến danh tính thành mặt phẳng điều khiển, và rà soát truy cập liên tục

Trong một kiến trúc không tin cậy (chương 4.1), danh tính là nơi chính sách được quyết định và thực thi, vì vậy hãy đầu tư ở đó tương xứng. Rồi khép vòng với **rà soát truy cập**, còn gọi là chứng nhận lại: theo lịch, chủ sở hữu của mỗi hệ thống xác nhận rằng mọi người và máy có quyền truy cập vẫn cần nó, và thu hồi những gì họ không biện minh được. Hãy nuôi mọi sự kiện xác thực và cấp quyền vào một dấu vết kiểm toán trả lời *ai đã truy cập gì, khi nào, và theo chính sách nào* (chương 4.6). Rà soát truy cập là cách bạn chống lại sự bò lan đặc quyền, sự tích lũy chậm của các quyền mà không cấp quyền đơn lẻ nào trông vô lý nhưng cùng nhau khiến một tài khoản quá mạnh.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| IdP tập trung với SSO | Một đăng nhập mạnh, chính sách nhất quán, kiểm toán dễ | Điểm lỗi đơn; sự cố khóa mọi người ra ngoài |
| RBAC | Đơn giản, kiểm toán được, quen thuộc | Bùng nổ vai trò; thô cho nhu cầu nhạy ngữ cảnh |
| ABAC | Mịn, nhận biết ngữ cảnh, mở rộng theo thuộc tính | Khó thiết kế, kiểm thử và suy luận hơn |
| Passkey / WebAuthn | Chống lừa đảo, không mật khẩu, mạnh | Luồng khôi phục và mất thiết bị cần thiết kế cẩn thận |
| Truy cập đúng-lúc | Đặc quyền thường trực gần bằng không | Ma sát; cần đường phê duyệt nhanh, đáng tin |
| Liên kết với đối tác | Không quản lý mật khẩu bên ngoài; tin cậy có phạm vi | Niềm tin phụ thuộc vào vệ sinh riêng của đối tác |
| Khóa dịch vụ sống lâu | Cực kỳ dễ thiết lập | Dễ rò rỉ; nguyên nhân hàng đầu của xâm phạm thông tin xác thực |

Căng thẳng trung tâm là bảo mật so với ma sát. Mỗi biện pháp kiểm soát thu nhỏ bề mặt tấn công (MFA trên mọi thứ, nâng quyền JIT, thời gian sống thông tin xác thực ngắn) cũng thêm một bước vào ngày của ai đó, và người ta tìm đường vòng quanh các biện pháp kiểm soát gây đau quá nhiều. Hãy giải quyết bằng cách làm cho con đường an toàn là con đường dễ: SSO để xác thực mạnh chỉ là một cú chạm, passkey để không có mật khẩu phải gõ, và cung cấp tự động để quyền truy cập đúng đơn giản xuất hiện. Hãy chi ngân sách ma sát của bạn ở nơi bán kính ảnh hưởng lớn nhất, trên truy cập đặc quyền và sản xuất, và giữ truy cập hằng ngày gần như không ma sát.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn thực sự thu hồi được mọi quyền truy cập của một người rời đi hôm nay nhanh đến đâu, và làm sao bạn biết nó đã hoạt động?** Tốc độ thu hồi là phép đo trực tiếp về độ trưởng thành danh tính của bạn, vì một người rời đi mà quyền truy cập còn tồn tại là một tài khoản không được giám sát với quyền thật. Trong một tổ chức lớn với hàng chục hệ thống rời rạc, câu trả lời trung thực thường là "chúng tôi không chắc," và khoảng trống thường là các ứng dụng chưa bao giờ được nối vào nhà cung cấp danh tính trung tâm. Hãy mang một lần ra đi gần đây thực và truy mọi hệ thống họ có thể chạm vào, kiểm tra dấu thời gian cho khi mỗi quyền truy cập thực sự chấm dứt. Hãy quyết định một mục tiêu, như thu hồi hoàn toàn trong vòng một giờ sau thay đổi trạng thái nhân sự, và đo đạc nó để bạn chứng minh được thay vì hy vọng. Nếu bất kỳ hệ thống nào dựa vào ai đó nhớ một bước thủ công, đó là tài khoản mà một vụ xâm phạm tương lai sẽ dùng.

2. **Bạn vẫn còn đặc quyền thường trực và thông tin xác thực tĩnh sống lâu ở đâu, và cần gì để loại bỏ chúng?** Quyền quản trị thường trực và khóa dịch vụ vĩnh viễn là hai tài sản mà kẻ tấn công muốn nhất, vì chúng bền và mạnh. Hãy kiểm kê mọi con người có truy cập sản xuất hoặc quản trị luôn bật và mọi dịch vụ xác thực bằng khóa tĩnh, rồi hỏi trung thực cái nào có thể chuyển sang nâng quyền đúng-lúc hoặc danh tính khối lượng công việc sống ngắn. Cân nhắc đối lập là nỗi sợ vận hành: các đội giữ truy cập thường trực vì những khoảnh khắc phá kính cảm thấy an toàn hơn với nó, nên bạn phải làm cho nâng quyền khẩn cấp nhanh và đáng tin trước khi bạn gỡ quyền thường trực. Hãy mang danh sách đến cuộc thảo luận và xếp hạng các mục theo bán kính ảnh hưởng, nhắm vào truy cập sản xuất và quản trị trước. Trạng thái cuối cần hướng tới là không có truy cập quản trị thường trực và không có khóa tĩnh nào sống lâu hơn một lần triển khai.

3. **Bạn có một danh tính có thẩm quyền cho mỗi người và mỗi khối lượng công việc, hay nhiều, và sự lan tràn đang tốn bao nhiêu?** Sự lan tràn thư mục, nơi cùng một con người tồn tại thành năm tài khoản qua năm hệ thống với thuộc tính trôi dạt, là nơi sinh ra các khoảng trống thu hồi và quyền truy cập mồ côi. Hợp nhất về một nguồn sự thật duy nhất cho mỗi quần thể danh tính là một trong những khoản đầu tư có đòn bẩy cao nhất mà một đội lớn có thể làm, vì mọi biện pháp kiểm soát hạ nguồn phụ thuộc vào việc biết hai bản ghi là cùng một người. Hãy mang bản kiểm kê các kho danh tính của bạn và ánh xạ cái nào có thẩm quyền so với cái nào là bản sao tiện lợi không ai quản trị. Đánh đổi là hợp nhất là một cuộc di chuyển lớn, kém hào nhoáng cạnh tranh với công việc tính năng về sự chú ý. Hãy quyết định liệu chi phí liên tục của sự lan tràn, trong nỗi đau kiểm toán và rủi ro xâm phạm, có biện minh cho việc tài trợ cuộc di chuyển đó bây giờ thay vì sau sự cố kế tiếp.

4. **Các yếu tố xác thực mạnh nhất của bạn có thực sự chống lừa đảo không, và cái gì ngăn bạn loại bỏ mật khẩu vĩnh viễn?** Yếu tố mà kẻ tấn công không thể lừa đảo là cái chấm dứt đánh cắp thông tin xác thực như con đường xâm phạm thống trị của bạn, và passkey gắn với WebAuthn là lựa chọn có thể triển khai rộng rãi duy nhất vượt qua ngưỡng đó. Trong một tổ chức lớn bức tranh trung thực thường hỗn hợp: passkey cho một số, mã một lần qua SMS cho số khác, và một cái đuôi dài các ứng dụng cũ vẫn chấp nhận chỉ mật khẩu. Cân nhắc đối lập là thật, vì passkey dịch chuyển vấn đề khó sang khôi phục và mất thiết bị, và một luồng khôi phục vụng về trở thành mục tiêu mềm mới mà kẻ tấn công đơn giản xoay sang. Hãy mang số liệu độ bao phủ theo loại yếu tố, danh sách ứng dụng vẫn quay về mật khẩu, và một đường khôi phục tài khoản được thiết kế mà bạn tin trước một nỗ lực kỹ thuật xã hội kiên quyết. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn mục tiêu với bất kỳ mức bảo đảm bắt buộc nào, vì một hệ thống bảo đảm cao vẫn cho phép một yếu tố có thể bị lừa đảo có một khoảng trống tuân thủ cũng như bảo mật.

5. **Bạn quyết định mỗi danh tính nhận quyền truy cập gì thế nào, và bạn có thể so sánh, kiểm thử và chứng minh quyết định đó trước khi nó được phát hành không?** Khoảng cách giữa "ai đó bấm quyền vào một bảng điều khiển" và "một chính sách được rà soát, quản lý phiên bản" là sự khác biệt giữa một mô hình truy cập bạn kiểm toán được và một cái bạn chỉ xin lỗi được. Với một đội lớn áp lực là để mỗi ứng dụng phát triển quy tắc riêng theo yêu cầu, lặng lẽ tạo ra bùng nổ vai trò ở phía RBAC và các điều kiện không kiểm thử được ở phía ABAC, cho đến khi không ai nói được một cấp quyền nhất định thực sự cho phép gì. Cân nhắc đối lập là tốc độ phân phối, vì biểu đạt cấp quyền dưới dạng chính sách-dưới-dạng-mã thêm một bước rà soát mà một cú bấm bảng điều khiển không có, và các đội dưới hạn chót oán ma sát cho đến khi cuộc kiểm toán thất bại đầu tiên hay cấp quyền quá rộng làm lập luận thay họ. Hãy mang một thay đổi quyền thực và truy cách nó sẽ được đề xuất, kiểm thử, rà soát và hoàn tác, cộng số vai trò bạn có và bao nhiêu cái không ai giải thích được. Trong bối cảnh doanh nghiệp và chính phủ, kiểm toán viên sẽ yêu cầu bạn cho thấy chính xác ai có thể truy cập một bản ghi và theo quy tắc nào vào một ngày nhất định, và chỉ một chính sách so sánh được, kiểm thử được mới trả lời điều đó mà không chạy vạy.

6. **Lần cuối một cuộc rà soát truy cập thu hồi thứ gì thật là khi nào, và ai chịu trách nhiệm khi sự bò lan đặc quyền không bị kiểm soát?** Rà soát truy cập là biện pháp kiểm soát chống lại sự tích lũy chậm của các quyền mà không cấp quyền đơn lẻ nào trông vô lý, và một cuộc rà soát không bao giờ thu hồi gì là sân khấu rà soát tạo ra giấy tờ thay vì sự an toàn. Trong một tổ chức lớn chế độ thất bại là con dấu cao su: chủ sở hữu hệ thống chứng nhận lại hàng trăm mục trong một lần ngồi, chấp thuận tất cả vì thực sự đánh giá từng cái thì tẻ nhạt và động cơ giữ quyền truy cập chảy mạnh hơn động cơ cắt nó. Cân nhắc đối lập là các cuộc rà soát có ý nghĩa tốn thời gian của chủ sở hữu và đôi khi làm hỏng quy trình của ai đó khi quyền truy cập họ lặng lẽ dựa vào biến mất, nên bạn phải làm cuộc rà soát có mục tiêu và dẫn dắt bởi rủi ro thay vì một danh sách không phân biệt. Hãy mang tỷ lệ thu hồi từ chu kỳ gần nhất, số quyền trung bình mỗi người, và bằng chứng ai sở hữu việc chứng nhận lại của từng hệ thống. Trong bối cảnh doanh nghiệp và chính phủ, hãy nêu tên viên chức chịu trách nhiệm cho mỗi cuộc rà soát và nhịp họ bị giữ theo, vì sự bò lan đặc quyền mà không ai chịu trách nhiệm bắt được chính là điều kiện mà cả kiểm toán viên lẫn kẻ tấn công đều khai thác.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy mua danh tính, đừng xây. Một nhà cung cấp danh tính được lưu trữ duy nhất với SSO, passkey bắt buộc, và thôi việc một cú nhấp cho một nhúm kỹ sư một tư thế cấp doanh nghiệp với phí theo chỗ ngồi. Dựa vào danh tính khối lượng công việc tích hợp sẵn của nhà cung cấp để không có một khóa đám mây sống lâu nào trong đường ống của bạn, và dùng OIDC cùng OAuth 2.0 có sẵn thay vì phát minh xử lý token mà bạn không gánh nổi việc bảo trì.

**Doanh nghiệp nhỏ.** Không có chuyên gia danh tính trong biên chế, hãy ưu tiên SSO và MFA đã đi kèm trong công cụ bạn trả tiền, và bật chúng thay vì mua sắm một nền tảng riêng. Hãy coi vấn đề gia nhập-chuyển đổi-rời đi là một danh sách kiểm tra bằng văn bản ngắn gắn với ai sở hữu việc tuyển dụng, và ưu tiên passkey vì chúng loại bỏ gánh nặng bàn hỗ trợ đặt lại mật khẩu mà bạn không thể dành ai xử lý. Tránh đăng nhập dùng chung, vì chúng là thói quen rẻ sau này khiến việc quy trách nhiệm và thu hồi là không thể.

**Doanh nghiệp lớn.** Công việc là hợp nhất và quản trị qua nhiều thư mục và đội: một nhà cung cấp danh tính có thẩm quyền được điều khiển bởi hệ thống nhân sự, luồng gia nhập-chuyển đổi-rời đi tự động, RBAC cho chức năng công việc với ABAC cho ngữ cảnh, và quản lý truy cập đặc quyền với ghi phiên. Hãy biểu đạt cấp quyền dưới dạng chính sách-dưới-dạng-mã để thay đổi so sánh được và kiểm thử được, chạy các cuộc rà soát truy cập theo lịch thực sự thu hồi, và chuẩn hóa giao diện để ứng dụng nối vào danh tính trung tâm thay vì mỗi cái tự phát triển đăng nhập riêng.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công thúc đẩy thiết kế. Hãy gắn xác thực với thông tin xác thực phần cứng như thẻ thông minh PIV hay CAC, đặt mức bảo đảm danh tính theo NIST SP 800-63 để các hệ thống rủi ro cao hơn đòi các yếu tố bảo đảm cao hơn, và giữ nhật ký kiểm toán bất biến trả lời chính xác ai đã truy cập gì và khi nào. Hãy công bố cách xử lý bằng ngôn ngữ đơn giản của danh tính hướng đến công dân, giữ ngăn xếp danh tính khách hàng và lực lượng lao động riêng biệt, và bảo đảm mọi hành động đặc quyền trên một hệ thống nhạy cảm được trung gian và ghi lại cho kiểm toán viên sẽ hỏi.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp hai mươi người không thể bố trí đội danh tính, nên mua một cái. Mọi nhân viên đăng nhập qua một nhà cung cấp danh tính được lưu trữ duy nhất với SSO vào email, lưu trữ mã, bảng điều khiển đám mây và ứng dụng nội bộ, và passkey được yêu cầu nên không có mật khẩu để lừa đảo. Thôi việc là một cú nhấp: vô hiệu hóa người đó trong nhà cung cấp danh tính cắt quyền truy cập ở mọi nơi cùng lúc. Cho sản phẩm riêng của họ, họ dùng OIDC cho đăng nhập người dùng và OAuth 2.0 để cho các tích hợp gọi API của họ bằng token có phạm vi. Xác thực dịch vụ-với-đám-mây dùng danh tính khối lượng công việc tích hợp sẵn của nhà cung cấp, nên không có một khóa đám mây sống lâu nào trong đường ống của họ. Điều này tốn phí theo chỗ ngồi khiêm tốn và mua cho họ một tư thế danh tính mạnh hơn nhiều doanh nghiệp đang vận hành.

**Doanh nghiệp lớn.** Một ngân hàng đa quốc gia đã dành một thập kỷ tích lũy bốn thư mục và hàng trăm ứng dụng, một số được liên kết qua SAML, một số có đăng nhập cục bộ riêng. Nó tài trợ một chương trình hợp nhất: một nhà cung cấp danh tính có thẩm quyền, được điều khiển bởi hệ thống nhân sự, với luồng gia nhập-chuyển đổi-rời đi tự động cung cấp khi tuyển và thu hồi trong vài phút sau khi chấm dứt. RBAC bao quát các chức năng công việc chuẩn trong khi ABAC thực thi quy tắc nơi lưu trữ dữ liệu và thẩm tra cho truy cập xuyên biên giới. Quản trị viên không giữ truy cập sản xuất thường trực; họ yêu cầu nâng quyền đúng-lúc qua một hệ thống quản lý truy cập đặc quyền ghi lại mọi phiên. Các cuộc rà soát truy cập hằng quý buộc chủ sở hữu hệ thống chứng nhận lại hoặc thu hồi, và mọi quyết định được biểu đạt dưới dạng chính sách-dưới-dạng-mã để kiểm toán viên có thể so sánh chính xác cái gì đã thay đổi và khi nào.

**Chính phủ.** Một cơ quan liên bang cấp thẻ thông minh xác minh danh tính cá nhân (PIV), và tương đương quân sự, thẻ truy cập chung (CAC), cho lực lượng lao động của mình, nên xác thực được gắn với một thông tin xác thực phần cứng thay vì mật khẩu. Chương trình danh tính của nó theo cách tiếp cận quản lý danh tính, thông tin xác thực và truy cập liên bang (FICAM) và đặt mức bảo đảm danh tính theo hướng dẫn của Viện Tiêu chuẩn và Công nghệ Quốc gia NIST SP 800-63, nên các hệ thống rủi ro cao hơn đòi thông tin xác thực bảo đảm cao hơn. Các dịch vụ hướng đến công dân dùng ngăn xếp danh tính khách hàng riêng ở mức bảo đảm thấp hơn với MFA mạnh. Rà soát truy cập và nhật ký kiểm toán bất biến nuôi trực tiếp bằng chứng cấp phép liên tục của cơ quan (chương 4.6), và mọi hành động đặc quyền trên một hệ thống mật được trung gian và ghi lại.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của đầu tư danh tính đến từ việc đưa vectơ xâm phạm thống trị của bạn ra khỏi vùng nguy hiểm. Thông tin xác thực bị đánh cắp và tài khoản được cấp quá nhiều quyền thúc đẩy một phần lớn các sự cố thực, và mỗi cái mang một cái đuôi nặng: ứng phó sự cố, tiền phạt quy định, thông báo xâm phạm, và thiệt hại danh tiếng lâu dài. Chỉ riêng MFA chống lừa đảo đã loại bỏ con đường xâm nhập phổ biến nhất, và thu hồi tự động đóng khoảng trống tài khoản mồ côi biến một lần ra đi thường lệ thành phơi nhiễm. Đây là những mức giảm rủi ro rẻ nhất có sẵn trên mỗi đô la chi.

Tổng chi phí sở hữu là thật nhưng có giới hạn. Nó bao gồm cấp phép nhà cung cấp danh tính, một nền tảng quản lý truy cập đặc quyền và bí mật, kỹ thuật để nối mọi ứng dụng vào danh tính trung tâm, và công sức liên tục của rà soát truy cập. Chi phí lớn hơn là mang tính tổ chức: hợp nhất thư mục và trang bị SSO vào ứng dụng cũ là công việc chậm, kém hào nhoáng cạnh tranh với tính năng. Hãy cân nhắc nó đối lập với phương án thay thế. Danh tính phân mảnh chi cùng số tiền mãi mãi dưới dạng thôi việc thủ công, chạy vạy kiểm toán, và đặt lại mật khẩu ở bàn hỗ trợ, cộng chi phí cuối cùng của vụ xâm phạm mà sự phân mảnh khiến có khả năng. Khi bạn trình bày lập luận với ban lãnh đạo, hãy đóng khung danh tính là mặt phẳng điều khiển cho không tin cậy: hợp nhất và tự động hóa là khoản đầu tư một lần hạ cả rủi ro xâm phạm lẫn chi phí lặp lại của kiểm toán, thôi việc và hỗ trợ truy cập.

## Phản mẫu và cạm bẫy

- **Tài khoản mồ côi.** Quyền truy cập sống lâu hơn người hay mục đích, đặc biệt là tài khoản dịch vụ không được giám sát và nhà thầu bị quên.
- **Quản trị thường trực ở khắp nơi.** Truy cập đặc quyền luôn bật thay vì nâng quyền đúng-lúc, cho bất kỳ tài khoản quản trị bị xâm phạm nào quyền lực bền vững.
- **Khóa tĩnh sống lâu.** Thông tin xác thực dịch vụ dán vào cấu hình hay CI không bao giờ hết hạn và cuối cùng rò rỉ.
- **Lan tràn thư mục.** Cùng một người là nhiều tài khoản không được quản trị, nên không thay đổi nào lan truyền hoàn toàn.
- **Tài khoản dùng chung.** Thông tin xác thực do nhiều người dùng, phá hủy việc quy trách nhiệm và khiến thu hồi là không thể.
- **SMS như yếu tố mạnh của bạn.** Coi mã một lần có thể bị lừa đảo, hoán đổi SIM là MFA đủ dùng.
- **Bùng nổ vai trò.** Quá nhiều vai trò RBAC hẹp đến mức mô hình không kiểm toán được và không ai biết một vai trò cấp gì.
- **Thu hồi như danh sách kiểm tra thủ công.** Các bước thôi việc của con người chắc chắn bỏ sót tài khoản quan trọng.
- **OAuth dùng cho xác thực.** Coi một token truy cập là bằng chứng danh tính thay vì dùng OIDC.
- **Sân khấu rà soát.** Chứng nhận lại truy cập bị đóng dấu cao su mà không ai thực sự đánh giá nhu cầu.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Mỗi ứng dụng có đăng nhập riêng. Mật khẩu không có MFA nhất quán. Cung cấp và thôi việc là thủ công, phản ứng và chậm; tài khoản mồ côi tích tụ. Thông tin xác thực dịch vụ là khóa tĩnh sống lâu. Không có rà soát truy cập; quyền được cấp và không bao giờ xem lại.
- **Mức 2, Phát triển:** SSO bao quát các ứng dụng chính qua một nhà cung cấp danh tính trung tâm, nhưng độ bao phủ không đồng đều qua các đội. MFA được yêu cầu cho hầu hết truy cập của con người. RBAC cơ bản tồn tại. Gia nhập-chuyển đổi-rời đi được tự động hóa một phần từ hệ thống nhân sự. Một số tài khoản đặc quyền được cất giữ. Rà soát truy cập diễn ra thỉnh thoảng và không nhất quán.
- **Mức 3, Chuẩn hóa:** Một nhà cung cấp danh tính hợp nhất có thẩm quyền cho lực lượng lao động, với cung cấp tự động và thu hồi nhanh được thực thi toàn tổ chức. MFA chống lừa đảo là tiêu chuẩn và được lập tài liệu. RBAC cộng ABAC được biểu đạt dưới dạng chính sách-dưới-dạng-mã. Quản lý truy cập đặc quyền với ghi phiên đã có. Danh tính khối lượng công việc thay thế hầu hết khóa tĩnh. Rà soát truy cập theo lịch được thực thi và kiểm toán theo một chính sách bằng văn bản mà mọi đội theo.
- **Mức 4, Quản lý:** Chương trình danh tính được đo theo đường cơ sở và kiểm soát bằng dữ liệu. Bạn theo dõi thời gian thu hồi từ thay đổi trạng thái nhân sự đến thu hồi hoàn toàn, độ bao phủ MFA và passkey theo quần thể, số tài khoản có đặc quyền thường trực, số khóa tĩnh sống lâu còn dùng, số tài khoản mồ côi, và tỷ lệ thu hồi của rà soát truy cập. Các chỉ số mang mục tiêu, như thu hồi hoàn toàn trong vòng một giờ và không có cấp quản trị thường trực mới ròng, và vi phạm một ngưỡng kích hoạt điều tra thay vì nhún vai. Thay đổi cấp quyền được kiểm thử trong đường ống và mỗi quyết định đi hay không đi cho một cấp quyền được dẫn dắt bởi bằng chứng, không phải thói quen.
- **Mức 5, Điều phối:** Danh tính là mặt phẳng điều khiển được cải thiện liên tục cho không tin cậy, tích hợp với bảo mật, rủi ro và hoạch định gia nhập-chuyển đổi-rời đi trong toàn tổ chức. Passkey là mặc định và mật khẩu đang được loại bỏ. Không có đặc quyền thường trực đạt được qua nâng quyền đúng-lúc, và mọi khối lượng công việc dùng thông tin xác thực sống ngắn, xoay vòng tự động cùng mTLS. Cấp quyền hoàn toàn là chính sách-dưới-dạng-mã. Rà soát truy cập là liên tục và dẫn dắt bởi rủi ro, thu hồi gần như tức thì, và mọi quyết định tạo bằng chứng kiểm toán tự động. Mô hình thích ứng khi tín hiệu rủi ro dịch chuyển, siết hoặc nới truy cập một cách động thay vì theo nhịp cố định.

## Ý tưởng để thảo luận

1. Cần gì để đạt được không có truy cập quản trị thường trực, và đường phá kính nào sẽ làm điều đó an toàn?
2. ABAC đáng với độ phức tạp của nó ở đâu trong môi trường của bạn so với giữ RBAC thuần?
3. Bạn nên loại bỏ mật khẩu để chuyển sang passkey quyết liệt đến mức nào, và luồng khôi phục nào thay thế chúng?
4. Ứng dụng nào vẫn nằm ngoài nhà cung cấp danh tính trung tâm của bạn, và cái gì giữ chúng ở đó?
5. Làm sao bạn cho đối tác và khách hàng truy cập có phạm vi mà không thừa hưởng vệ sinh bảo mật của họ?
6. Chỉ số đơn lẻ nào nắm bắt tốt nhất tốc độ thu hồi của bạn, và bạn có đang đo nó hôm nay không?

## Những điểm cần ghi nhớ

- Xác thực chứng minh bạn là ai; cấp quyền quyết định bạn được làm gì. Hãy thiết kế và rà soát chúng riêng biệt.
- Hợp nhất về một nhà cung cấp danh tính có thẩm quyền với SSO; sự lan tràn thư mục là khiếm khuyết bảo mật, không phải sự tiện lợi.
- Tự động hóa vòng đời gia nhập-chuyển đổi-rời đi và làm cho thu hồi nhanh và chứng minh được.
- Dùng OIDC cho đăng nhập người dùng, OAuth 2.0 cho truy cập API ủy thác, và SAML ở nơi danh mục doanh nghiệp cần; đừng dùng OAuth như xác thực.
- Chuyển xác thực về hướng passkey chống lừa đảo và WebAuthn; yêu cầu MFA ở mọi nơi và coi các yếu tố yếu là biện pháp tạm.
- Thực thi đặc quyền tối thiểu bằng truy cập đúng-lúc và quản lý truy cập đặc quyền; hướng tới không có quyền quản trị thường trực.
- Cho máy danh tính thực bằng thông tin xác thực khối lượng công việc sống ngắn và mTLS; loại bỏ khóa tĩnh sống lâu.
- Biến danh tính thành mặt phẳng điều khiển cho không tin cậy (chương 4.1), và khép vòng bằng rà soát truy cập liên tục cùng bằng chứng kiểm toán (chương 4.6).

## Tài liệu tham khảo và đọc thêm

- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines* (các mức bảo đảm danh tính, xác thực và liên kết)
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations*
- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*, các họ Kiểm soát Truy cập (AC) và Nhận dạng và Xác thực (IA)
- The OAuth 2.0 Authorisation Framework, IETF RFC 6749, và OAuth 2.0 Security Best Current Practice
- Đặc tả OpenID Connect Core 1.0, OpenID Foundation
- Đặc tả Security Assertion Markup Language (SAML) 2.0, OASIS
- Web Authentication (WebAuthn) Level 2, Khuyến nghị của W3C, và các đặc tả passkey của FIDO2 / FIDO Alliance
- Kiến trúc và sổ tay Federal Identity, Credential, and Access Management (FICAM), U.S. General Services Administration
- FIPS 201, *Personal Identity Verification (PIV) of Federal Employees and Contractors*
- Tài liệu Open Policy Agent (OPA), Cloud Native Computing Foundation (chính sách-dưới-dạng-mã cho cấp quyền)
