# 2.18 Quản lý phụ thuộc và chuỗi cung ứng

## Tổng quan và động lực

Hãy mở tệp khóa của dự án và đếm các gói. Nếu bạn giống hầu hết các đội, mã bạn tự viết chỉ là một lớp mỏng trên hàng trăm hay hàng nghìn [phụ thuộc](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) mà bạn không viết, không hiểu hết, và không dễ kiểm toán. Một dịch vụ web hiện đại kéo vào một khung phát triển, một trình điều khiển cơ sở dữ liệu, một thư viện ghi nhật ký và một định dạng tuần tự hóa, và mỗi thứ đó lại kéo vào nhiều thứ nữa. Kết quả là phần lớn phần mềm đang chạy của bạn, thường là đa số, đến từ những người lạ trên internet. Đó không phải là thất bại. Đó là thỏa thuận cho phép một đội nhỏ phát hành trong vài tuần thứ từng mất nhiều năm. Điểm mấu chốt là chấp nhận thỏa thuận đó với đôi mắt mở to.

Quản lý mã vay mượn đó tốt là một kỷ luật kỹ thuật tự thân, và chương này nói về nghề thủ công của nó: cách bạn chọn phụ thuộc, ghim chúng, cập nhật chúng, tái tạo bản dựng, và giữ cho toàn bộ đồ thị dễ đọc khi nó lớn lên. Phía mối đe dọa bảo mật, nơi kẻ tấn công cố ý đầu độc đồ thị đó, được xử lý đầy đủ trong chương 4.2 về bảo mật ứng dụng. Ở đây mối quan tâm là kỹ thuật hằng ngày: ràng buộc phiên bản, tệp khóa, xung đột bắc cầu, nhịp cập nhật, và biết những gì có trong phần mềm của bạn. Làm đúng điều này và bảo mật trở nên dễ hơn nhiều, vì bạn không thể bảo vệ một chuỗi cung ứng mà bạn không nhìn thấy.

Với các đội lớn, và đặc biệt là doanh nghiệp và chính phủ, rủi ro tăng theo quy mô. Khi năm trăm kho mã mỗi kho tự chọn thư viện của mình, bạn có năm trăm phiên bản hơi khác nhau của cùng một khung ghi nhật ký, một giấy phép không ai phê duyệt, và không cách nào trả lời "chúng ta có bị ảnh hưởng không?" khi một lỗ hổng nghiêm trọng đáp xuống. Các doanh nghiệp trả lời điều này bằng các thư viện được phê duyệt và kho đăng ký dùng chung. Các chính phủ ngày càng trả lời bằng các sắc lệnh: Sắc lệnh Hành pháp 14028 của Hoa Kỳ đã đẩy [bảng kê vật liệu phần mềm](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM) và nguồn gốc bản dựng vào đường cơ sở cho phần mềm họ mua. Những tổ chức giữ được bình tĩnh trong cuộc khủng hoảng phụ thuộc tiếp theo là những tổ chức đã làm công việc này trước khi cần đến nó.

## Các nguyên tắc chính

- Phần lớn phần mềm của bạn là mã bạn không viết; hãy nhận trách nhiệm dù bạn không viết nó.
- Mỗi phụ thuộc là một khoản nợ vĩnh viễn cũng như một tài sản; hãy thêm chúng một cách có chủ đích, không phản xạ.
- Ghim phiên bản bằng tệp khóa để bản dựng tái tạo được và xác định, không phải "bất cứ thứ gì mới nhất vào ngày hôm đó."
- Cập nhật theo nhịp đều đặn, ở các gia số nhỏ tự động, thay vì những bước nhảy hiếm hoi đáng sợ.
- Biết chính xác những gì có trong phần mềm của bạn; bạn không thể bảo mật hay cấp phép những gì bạn không liệt kê được.
- Ưu tiên ít phụ thuộc, được bảo trì tốt hơn nhiều phụ thuộc tiện lợi.
- Kiểm soát các gói đến từ đâu; một kho đăng ký chưa được xác minh là một cánh cửa mở.

## Khuyến nghị

### Hiểu việc đánh phiên bản và ràng buộc nó một cách có chủ đích

Hãy học cách hệ sinh thái của bạn biểu diễn phiên bản, vì hành vi cập nhật của bạn hoàn toàn dựa vào đó. Hầu hết trình quản lý gói dùng một dạng nào đó của [đánh phiên bản ngữ nghĩa](https://en.wikipedia.org/wiki/Software_versioning) (SemVer), trong đó một phiên bản được đọc là MAJOR.MINOR.PATCH: tăng patch hứa chỉ sửa lỗi, tăng minor thêm các tính năng tương thích ngược, và tăng major báo hiệu các thay đổi phá vỡ. Các khai báo phụ thuộc của bạn sau đó đặt một ràng buộc, như "tương thích với 4.x" hoặc "ít nhất 2.3.0," cho bộ phân giải biết nó được phép đi xa đến đâu khi chọn phiên bản.

Hãy có chủ đích về mức lỏng hay chặt của những ràng buộc đó. Khoảng rộng tự động nhận bản sửa, với cái giá là để một bản phát hành minor bạn chưa bao giờ rà soát lọt vào môi trường thực; ghim chặt cho kiểm soát với cái giá là công sức thủ công. Câu trả lời thực dụng cho hầu hết các đội là khai báo các khoảng khá dễ dãi trong tệp kê khai, rồi đóng băng các phiên bản đã phân giải chính xác trong một tệp khóa để khoảng đó chỉ được đánh giá lại khi bạn cố ý cập nhật. Hãy coi SemVer là lời hứa mà người bảo trì cố giữ, không phải bảo đảm họ luôn giữ; một bản phát hành "patch" vẫn có thể làm hỏng bạn, đó chính là lý do bạn kiểm thử các bản cập nhật thay vì tin chúng.

### Commit tệp khóa và đòi hỏi bản dựng tái tạo được

Một tệp khóa ghi lại phiên bản chính xác và mã băm mật mã của mọi gói trong đồ thị phụ thuộc của bạn, cả trực tiếp lẫn bắc cầu. Hãy commit nó vào hệ thống quản lý phiên bản (chương 2.6) và coi nó là một phần hạng nhất của mã nguồn. Nhiệm vụ của nó là biến bản dựng của bạn thành một hàm: cùng đầu vào tạo ra cùng đầu ra mọi lần, trên mọi máy, năm nay và năm sau. Không có nó, hai kỹ sư chạy "install" cách nhau một tuần có thể nhận mã khác nhau, và một lỗi xuất hiện trên môi trường thực có thể không thể tái hiện trên chiếc laptop đã dựng nó.

Hãy hướng đến [bản dựng tái tạo được](https://en.wikipedia.org/wiki/Reproducible_builds) thực sự, nơi một commit nhất định luôn cho ra một hiện vật có hành vi giống hệt. Trong tích hợp liên tục (chương 8.1), hãy cài đặt nghiêm ngặt từ tệp khóa và làm hỏng bản dựng nếu tệp khóa và tệp kê khai bất đồng, thay vì âm thầm phân giải các phiên bản mới. Các mã băm trong tệp khóa làm hai việc: chúng ghim hành vi và phát hiện sự giả mạo, vì một gói có nội dung không còn khớp mã băm đã ghi sẽ không cài được. Khả năng tái tạo là nền tảng mà mọi thứ khác trong chương này đứng trên đó.

### Quản lý phụ thuộc bắc cầu và xung đột hình thoi một cách có chủ đích

Các phụ thuộc trực tiếp của bạn chỉ là những cái bạn đã gọi tên. Bên dưới chúng là một đồ thị lớn hơn nhiều gồm các phụ thuộc bắc cầu, các gói mà gói của bạn phụ thuộc vào, và đó là nơi phần lớn rủi ro và bất ngờ của bạn sống. Một thất bại kinh điển là phụ thuộc hình thoi: thư viện A cần phiên bản 1 của một tiện ích dùng chung, thư viện B cần phiên bản 2, và bây giờ bộ phân giải phải dung hòa một yêu cầu bất khả. Một số hệ sinh thái cho phép nhiều phiên bản cùng tồn tại, đổi đĩa và bộ nhớ lấy sự bình yên; những hệ khác ép một phiên bản duy nhất và để bạn môi giới xung đột.

Hãy làm cho những xung đột này hiển thị thay vì để chúng mưng mủ. Dùng công cụ của bạn để in toàn bộ cây phụ thuộc và giải thích vì sao một gói nhất định có mặt và ai đã kéo nó vào. Khi một xung đột xuất hiện, hãy giải quyết nó một cách có chủ đích: nâng cấp bên tụt hậu, ghim một ghi đè, hoặc bỏ một phụ thuộc mà đòi hỏi của nó bạn không thể đáp ứng. Theo dõi sự tăng trưởng của đồ thị theo thời gian, vì sự tràn lan không kiểm soát trong các phụ thuộc bắc cầu là sự tích lũy chậm của [nợ kỹ thuật](https://en.wikipedia.org/wiki/Technical_debt) cuối cùng hiện ra như một lần nâng cấp không giải được hoặc một lỗ hổng bạn không thể vá nếu không viết lại.

### Cập nhật theo nhịp đều đặn với pull request tự động

Chiến lược cập nhật rủi ro nhất là chiến lược mà hầu hết các đội vô tình trôi vào: không bao giờ cập nhật, rồi cập nhật mọi thứ cùng lúc dưới áp lực khẩn cấp khi một lỗ hổng nghiêm trọng buộc tay bạn. Đến lúc đó bạn đã tụt hậu nhiều năm, nhật ký thay đổi là một bức tường, và việc nâng cấp là một dự án nhiều tuần thay vì một việc vặt thường lệ. Cách chữa là nhịp điệu. Hãy áp dụng một trình cập nhật phụ thuộc tự động (các công cụ Dependabot và Renovate là ví dụ phổ biến) mở một pull request mỗi khi một phụ thuộc có phiên bản mới, kèm nhật ký thay đổi và kết quả kiểm thử của bạn.

Rồi điều chỉnh luồng để nó giúp bạn thay vì nhấn chìm bạn. Một vòi nước pull request riêng lẻ mỗi sáng huấn luyện mọi người phớt lờ chúng, còn tệ hơn không có tự động hóa. Hãy gom các bản cập nhật rủi ro thấp như bản phát hành patch, để chúng tự hợp nhất khi kiểm thử đạt, và dành sự chú ý của con người cho các bản tăng phiên bản major và bất cứ thứ gì chạm vào một thư viện nhạy cảm. Đặt một nhịp mà đội có thể duy trì, có lẽ là một buổi rà soát hằng tuần, để việc cập nhật vẫn là một khoản thuế nhỏ đều đặn thay vì một hóa đơn hiếm hoi đau đớn. Đây chính xác là nơi một chiến lược kiểm thử mạnh (chương 2.4) hoàn vốn, vì các bản cập nhật tự động chỉ an toàn nếu kiểm thử của bạn bắt được những gì chúng làm hỏng.

### Giảm thiểu dấu chân và đánh giá trước khi áp dụng

Mỗi phụ thuộc bạn thêm là một cam kết thường trực: với lỗi của nó, lỗ hổng của nó, giấy phép của nó, sự quan tâm liên tục của người bảo trì nó, và đồ thị phụ thuộc phụ ngày càng lớn của chính nó. Phụ thuộc rẻ nhất để quản lý là phụ thuộc bạn không thêm. Trước khi với tới một gói, hãy hỏi liệu vài chục dòng mã của chính bạn có đủ không, đặc biệt với chức năng tầm thường. Lịch sử các hệ sinh thái gói đầy những câu chuyện cảnh báo nơi một gói nhỏ xíu, được phụ thuộc rộng rãi bị gỡ hoặc bị chiếm đoạt và làm hỏng nửa internet.

Khi bạn thực sự áp dụng, hãy đánh giá ứng viên như mối quan hệ dài hạn mà nó là. Kiểm tra sức khỏe bảo trì: commit gần đây, người bảo trì phản hồi, lịch sử phát hành thực, và hơn một người nắm chìa khóa. Kiểm tra giấy phép và xác nhận nó nằm trong danh sách được phê duyệt của bạn (chương 10.3). Kiểm tra hồ sơ bảo mật, kích thước, và dấu chân bắc cầu của chính nó, vì một tính năng nhỏ không đáng để kéo theo một trăm gói. Hãy viết các tiêu chí này ra để "chúng ta có nên thêm cái này không?" là một danh sách kiểm tra mà cả đội áp dụng nhất quán, không phải một tâm trạng.

### Tạo SBOM và nắm bắt nguồn gốc bản dựng

Bạn không thể nhanh chóng trả lời "chúng ta có bị ảnh hưởng bởi lỗ hổng này không?" trừ khi bạn đã biết những gì có trong phần mềm của mình. SBOM là câu trả lời: một bản kiểm kê đọc được bằng máy của mọi thành phần trong một bản dựng, kèm phiên bản và giấy phép, theo một định dạng chuẩn như SPDX hoặc CycloneDX. Hãy sinh một cái tự động như một phần của đường ống dựng, lưu nó cạnh hiện vật, và giữ nó chừng nào hiện vật đó còn chạy ở bất cứ đâu. Khi lỗ hổng tiêu đề tiếp theo xuất hiện, một truy vấn đối chiếu với các SBOM của bạn biến một tuần grep hoảng loạn thành một báo cáo năm phút.

Hãy đi thêm một bước và nắm bắt nguồn gốc: một bản ghi có chữ ký, chống giả mạo về cách một hiện vật được dựng, từ commit nguồn nào, bởi đường ống nào. Cộng đồng [phần mềm nguồn mở](https://en.wikipedia.org/wiki/Open-source_software) đã hội tụ về khung SLSA (Các Cấp độ Chuỗi cung ứng cho Hiện vật Phần mềm) như một mô hình phân bậc chính cho việc này, đi từ "chúng tôi có thể mô tả bản dựng của mình" lên "chúng tôi có thể chứng minh nó, và bằng chứng đó chống lại một hệ thống dựng bị xâm phạm." Chứng thực cho phép người dùng xác minh rằng một hiện vật thực sự đến từ đường ống của bạn. Với công việc chính phủ điều này ngày càng không còn tùy chọn; nguồn gốc và SBOM nằm trong các sắc lệnh mua sắm, nên xây dựng năng lực sớm giữ bạn đủ điều kiện để dự thầu.

### Kiểm soát nguồn của bạn bằng kho đăng ký, gương và đóng gói trực tiếp

Các gói của bạn đến từ đâu cũng quan trọng như bạn chọn những gói nào. Kéo trực tiếp từ internet công khai ở mỗi bản dựng và bạn thừa hưởng những lần ngừng hoạt động của nó, các phiên bản bị rút lại, và những kẻ tấn công của nó. Hãy dựng một kho đăng ký gói nội bộ hoặc một gương đệm làm proxy cho hệ sinh thái công khai, để bản dựng nhanh, lặp lại được, và được cách ly khỏi việc thượng nguồn biến mất. Kho đăng ký cũng trở thành nơi tự nhiên để thực thi chính sách: chặn các phiên bản xấu đã biết, cách ly các bản phát hành mới trong một thời gian ngắn, và từ chối các gói không đạt cổng giấy phép hay bảo mật của bạn.

Hãy cấu hình kho đăng ký đó cẩn thận để tránh hai cái bẫy cụ thể. Nhầm lẫn phụ thuộc xảy ra khi một công cụ dựng, được cung cấp cả gói nội bộ riêng và một gói công khai cùng tên, lấy cái công khai của kẻ tấn công; bạn phòng thủ bằng cách giới hạn phạm vi tên nội bộ và ghim các gói nội bộ vào nguồn nội bộ một cách tường minh. [Typosquatting](https://en.wikipedia.org/wiki/Typosquatting) xảy ra khi một gói độc hại dùng một cái tên lệch một phím so với một gói phổ biến và chờ ngón tay gõ nhầm; một kho đăng ký được tuyển chọn với danh sách cho phép chặn nó ngay cửa. Với một tập nhỏ các phụ thuộc quan trọng hoặc thay đổi chậm, hãy cân nhắc đóng gói trực tiếp, commit mã nguồn phụ thuộc thực sự vào kho của chính bạn, để bản dựng của bạn không có phụ thuộc bên ngoài nào. Nó đánh đổi sự tiện lợi cập nhật lấy kiểm soát hoàn toàn, đôi khi chính xác là điều đúng.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| Khoảng phiên bản rộng | Bản sửa tự động; ít công sức thủ công | Mã chưa rà soát đến môi trường thực; không xác định nếu thiếu tệp khóa |
| Ghim chặt cộng tệp khóa | Bản dựng tái tạo được, kiểm toán được | Đòi hỏi công việc cập nhật có chủ đích; có thể chậm bản sửa |
| Nhịp cập nhật quyết liệt | Bước nhỏ, an toàn; luôn gần hiện tại | Xáo trộn liên tục; cần sự chú ý đều đặn của người rà soát |
| Nâng cấp lớn hiếm, theo lô | Ít gián đoạn hằng ngày | Đáng sợ, rủi ro, đắt khi bị ép buộc |
| Nhiều phụ thuộc tiện lợi | Xây tính năng nhanh | Bề mặt tấn công lớn; gánh nặng bảo trì nặng |
| Dấu chân tối thiểu cộng đóng gói trực tiếp | Kiểm soát, bề mặt nhỏ, không rủi ro thượng nguồn | Nhiều mã hơn bạn sở hữu; bạn tự gánh cập nhật |
| Kho đăng ký công khai trực tiếp | Không cần thiết lập | Ngừng hoạt động, rút lại, nhầm lẫn và phơi nhiễm typosquatting |
| Kho đăng ký nội bộ và gương | Tốc độ, thực thi chính sách, cách ly | Hạ tầng phải vận hành và bảo trì |

Căng thẳng trung tâm chạy giữa vận tốc và kiểm soát. Mỗi lựa chọn ở trên là cùng một núm xoay nhìn từ một góc khác: bạn sẽ chủ động quản trị bao nhiêu phần mã vay mượn của mình, và để bao nhiêu phần chảy vào bằng niềm tin? Nghiêng quá xa về kiểm soát và bạn chìm trong rà soát thủ công, tụt hậu về bản sửa bảo mật, và làm chậm chính đội mà các phụ thuộc đáng lẽ phải tăng tốc. Nghiêng quá xa về vận tốc và một ngày bạn thức dậy với một đồ thị không thể kiểm toán, không thể nâng cấp và một vi phạm giấy phép mà bạn không thể giải thích với luật sư. Lời giải là một tư thế, không phải một điểm cố định: khóa và tái tạo mọi thứ, cập nhật liên tục theo bước nhỏ, giảm thiểu những gì bạn gánh vào, và thực thi chính sách tại một điểm nghẽn mà bạn kiểm soát. Sự kết hợp đó mua cho bạn cả tốc độ lẫn an toàn, đó là sự đánh đổi đáng làm ở quy mô lớn.

## Câu hỏi để thảo luận với đội của bạn

1. **Nhịp cập nhật thực sự của bạn là gì, và một lần nâng cấp khẩn cấp bắt buộc sẽ mất vài giờ hay vài tuần?** Hầu hết các đội không thể trả lời điều này trung thực cho đến khi một lỗ hổng nghiêm trọng buộc vấn đề. Chương này coi việc cập nhật đều đặn, tự động, theo bước nhỏ là con đường an toàn và nâng cấp lớn hiếm hoi là nguy hiểm, vì khoảng cách bạn để mở là khoảng cách bạn phải chạy nước rút qua dưới áp lực sau này. Hãy mang bằng chứng: bao nhiêu phụ thuộc của bạn tụt hậu hơn một phiên bản major, và lần nâng cấp đáng kể gần nhất của bạn thực sự mất bao lâu. Hãy thảo luận liệu bạn có thể áp dụng một trình cập nhật tự động không, bạn sẽ gom các thay đổi rủi ro thấp thế nào để mọi người không bỏ ngoài tai, và bạn cần kiểm thử gì để tự hợp nhất an toàn. Câu trả lời nên thay đổi cách bạn lập ngân sách thời gian kỹ thuật, biến một cuộc khủng hoảng hiếm hoi thành một khoản thuế hằng tuần thường lệ. Nếu câu trả lời trung thực là "vài tuần", đó là một rủi ro cần gọi tên bây giờ, không phải khám phá giữa sự cố.

2. **Nếu một lỗ hổng nghiêm trọng được công bố trong một thư viện phổ biến ngay bây giờ, bạn có thể liệt kê nhanh đến đâu mọi hiện vật bị ảnh hưởng mà bạn đang chạy?** Đây là câu hỏi mà SBOM tồn tại để trả lời, và tốc độ câu trả lời của bạn là thước đo trực tiếp độ trưởng thành chuỗi cung ứng của bạn. Không có bản kiểm kê bạn bị rút gọn thành grep các kho mã và phỏng vấn các đội, mất nhiều ngày bạn có thể không có trong khi đồng hồ chạy. Hãy mang tín hiệu cụ thể: bạn có sinh một SBOM cho mỗi bản dựng không, nó được lưu ở đâu, và bạn có thể thực sự truy vấn qua tất cả chúng hôm nay không? Hãy thảo luận liệu bạn biết không chỉ các phụ thuộc trực tiếp mà cả đồ thị bắc cầu, vì gói dễ bị tổn thương thường là gói bạn chưa bao giờ gọi tên. Câu trả lời quyết định sự cố tiếp theo của bạn là một truy vấn hay một cuộc diễn tập cháy, và đáng xây năng lực trước khi bạn cần nó. Các chính phủ nay bắt buộc điều này chính vì lý do đó.

3. **Làm thế nào bạn quyết định một phụ thuộc mới có đáng áp dụng không, và mọi người có áp dụng cùng một tiêu chuẩn không?** Chương này lập luận rằng mỗi phụ thuộc là một khoản nợ vĩnh viễn cũng như một sự tiện lợi, và rằng thứ rẻ nhất để quản lý là thứ bạn không bao giờ thêm. Tuy vậy ở hầu hết các đội quyết định đó vô hình: một kỹ sư cần một tính năng, tìm thấy một gói, và nó nằm trong tệp khóa trước bữa trưa mà không có sự xem xét nào về bảo trì, giấy phép, lịch sử bảo mật hay dấu chân của nó. Hãy mang các ví dụ từ đồ thị của chính bạn về những gói không ai nhớ đã áp dụng và hôm nay không thể bảo vệ. Hãy thảo luận liệu một danh sách kiểm tra đánh giá bằng văn bản và danh sách thư viện được phê duyệt (chương 10.3) sẽ giúp hay chỉ thêm ma sát, và lằn ranh nằm ở đâu giữa các tiện ích tầm thường bạn nên tự viết và hạ tầng thực đáng để phụ thuộc. Câu trả lời định hình trọng lượng dài hạn mà đội bạn gánh, từng quyết định nhỏ một.

4. **Bạn có thực sự quản trị các phụ thuộc bắc cầu của mình, hay chỉ những cái bạn đã gọi tên?** Phần lớn rủi ro của bạn sống ở một tầng bên dưới, trong các gói mà gói của bạn kéo vào, và một xung đột hình thoi nơi hai thư viện đòi các phiên bản không tương thích của một tiện ích dùng chung có thể chặn một lần nâng cấp vào thời điểm tệ nhất có thể. Điều này quan trọng ở quy mô lớn vì một gói bắc cầu không thể vá đơn lẻ có thể đóng băng một bản sửa bảo mật qua hàng trăm kho mã, và lực kéo đối lập là thật: phơi bày và ghim toàn bộ đồ thị tốn công sức liên tục, trong khi phớt lờ nó đổi công sức đó lấy sự tích lũy chậm của nợ nổi lên như một lần nâng cấp không giải được. Hãy mang bằng chứng: công cụ của bạn có thể in toàn bộ cây và giải thích vì sao bất kỳ gói nào có mặt và ai đã kéo nó vào không, và có bao nhiêu phiên bản riêng biệt của các thư viện phổ biến nhất của bạn cùng tồn tại hôm nay? Với doanh nghiệp và chính phủ, hãy thêm liệu bản kiểm kê và chính sách của bạn có với tới các thành phần bắc cầu không, vì một sắc lệnh phải biết những gì có trong phần mềm của bạn là vô nghĩa nếu một nửa đồ thị vô hình với bạn. Câu trả lời cho bạn biết lần nâng cấp bắt buộc tiếp theo là một lần hợp nhất thường lệ hay một cuộc khai quật nhiều đội.

5. **Các gói của bạn thực sự đến từ đâu, và điều gì ngăn kẻ tấn công lọt một gói vào?** Mỗi bản dựng kéo trực tiếp từ internet công khai thừa hưởng những lần ngừng hoạt động của nó, các phiên bản bị rút lại, và hai cuộc tấn công cụ thể: nhầm lẫn phụ thuộc, nơi một công cụ dựng lấy một gói công khai che bóng gói riêng của bạn, và typosquatting, nơi một gói độc hại nằm lệch một phím so với một cái tên phổ biến. Điều này quan trọng với một đội lớn vì một lần lấy gói bị đầu độc đơn lẻ có thể lan qua cả hệ thống của bạn trước khi ai đó nhận ra, và sự đánh đổi là thật: một kho đăng ký nội bộ hoặc gương đệm cho bạn một điểm nghẽn chính sách và sự cách ly khỏi thượng nguồn, nhưng đó là hạ tầng mà ai đó phải vận hành và giữ cập nhật. Hãy mang tín hiệu cụ thể: tên gói nội bộ có được giới hạn phạm vi và ghim vào nguồn nội bộ một cách tường minh không, có danh sách cho phép không, và bất kỳ bản phát hành mới nào có được cách ly ngắn trước khi dùng không? Với người mua thuộc chính phủ và chịu quy định, hãy gắn điều này với danh sách phần mềm được phê duyệt và tư thế không truy cập internet trực tiếp mà mua sắm ngày càng đòi hỏi, và thành thật liệu thiết lập hiện tại của bạn có vượt qua ngưỡng đó hôm nay không.

6. **Bạn có thể thực sự tái tạo và chứng minh cách các hiện vật của bạn được dựng không?** Một tệp khóa được commit với các mã băm mật mã nên biến bản dựng của bạn thành một hàm, cùng đầu vào cho cùng đầu ra trên mọi máy năm nay và năm sau, và nguồn gốc nên cho phép bất kỳ ai xác minh rằng một hiện vật thực sự đến từ đường ống và commit nguồn của bạn. Điều này quan trọng vì một bản dựng không tái tạo được biến một lỗi môi trường thực thành một bí ẩn không giải được và khiến bạn không thể chứng minh sự giả mạo đã không xảy ra, và cân nhắc đối lập là công sức so với sự đảm bảo: cài đặt nghiêm ngặt từ tệp khóa, chứng thực có chữ ký và nguồn gốc phù hợp SLSA tốn thiết lập và kỷ luật mà luồng "cứ cài bản mới nhất" tránh được. Hãy mang bằng chứng: tích hợp liên tục của bạn có làm hỏng khi tệp khóa và tệp kê khai bất đồng không, bạn có sinh và lưu một SBOM cùng một bản ghi nguồn gốc có chữ ký cho mỗi bản dựng không, và đã từng có ai xác minh một cái chưa? Với công việc doanh nghiệp và đặc biệt là chính phủ, nguồn gốc và SBOM ngày càng nằm trong các sắc lệnh mua sắm, nên câu trả lời trung thực ở đây quyết định bạn còn đủ điều kiện dự thầu hay bị loại ra.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một đội nhỏ và không có nhóm nền tảng, hãy dựa vào mặc định và tự động hóa thay vì quy trình. Commit tệp khóa ngay từ ngày đầu, bật một trình cập nhật tự động gom các bản phát hành patch và tự hợp nhất khi kiểm thử xanh, và giữ một quy tắc nhẹ để thêm gói: ưu tiên các thư viện nhàm chán, được bảo trì tốt và suy nghĩ kỹ về những cái nhỏ xíu. Bạn chưa dựng kho đăng ký nội bộ, và điều đó ổn, nhưng riêng các mã băm được commit đã bảo vệ bạn: một phiên bản bị đầu độc đơn giản là sẽ không cài được.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia phụ thuộc và ngân sách eo hẹp, vì vậy hãy mua kỷ luật thay vì xây dựng. Hãy dựa vào tự động hóa cập nhật mà nền tảng lưu trữ và mã của bạn đã cung cấp, ưu tiên một tập nhỏ thư viện trưởng thành để nâng cấp vẫn rẻ, và dùng một trình sinh SBOM miễn phí trong đường ống để bạn có thể trả lời "chúng ta có bị ảnh hưởng không?" mà không phải bố trí nhân sự. Hãy dành sự chú ý khan hiếm cho kiểm tra giấy phép và cho việc không áp dụng các gói tầm thường mà bạn có thể viết trong một chục dòng.

**Doanh nghiệp lớn.** Vấn đề là nhất quán qua nhiều đội: một kho đăng ký nội bộ dùng chung nhân bản hệ sinh thái công khai và thực thi chính sách giấy phép, nguồn và phiên bản tại một điểm nghẽn, cộng với một tập thư viện vàng được tuyển chọn làm mặc định và một con đường ngoại lệ có tài liệu cho bất cứ thứ gì khác. Phát ra một SBOM cho mỗi bản dựng vào một kho trung tâm để một truy vấn trả lời mức phơi nhiễm của bạn qua toàn hệ thống, triển khai các lần nâng cấp phối hợp qua pull request tự động, và coi sức khỏe phụ thuộc là một danh mục được đo, được quản trị thay vì tai nạn của từng kho.

**Chính phủ.** Quy tắc mua sắm và trách nhiệm giải trình trước công chúng định hình mọi thứ. Yêu cầu nhà cung cấp giao một SBOM đọc được bằng máy và nguồn gốc bản dựng phù hợp SLSA với mỗi bản phát hành, chỉ cài đặt nội bộ từ danh sách phần mềm được phê duyệt do một gương phục vụ không có đường trực tiếp đến internet công khai, và ưu tiên các phụ thuộc có bảo trì ổn định và giấy phép rõ ràng vì một hệ thống có thể chạy mười lăm năm và phải vá được trong cả khoảng thời gian đó. Hãy lên kế hoạch di chuyển hết vòng đời một cách có chủ đích thay vì như các sự cố khẩn cấp, và giữ các hồ sơ cho phép kiểm toán viên truy vết bất kỳ hiện vật nào đã phát hành về nguồn của nó.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người phát hành một ứng dụng web xây trên một khung, một thư viện thanh toán, và khoảng chín trăm gói bắc cầu mà họ chưa bao giờ kiểm tra. Họ không thể gánh một đội nền tảng, nên họ dựa vào tự động hóa: tệp khóa được commit từ ngày đầu, một trình cập nhật tự động gom các bản phát hành patch và hợp nhất chúng khi kiểm thử xanh, và một giờ mỗi tháng để rà soát các bản tăng phiên bản major đã chồng chất. Quy tắc một đoạn của họ để thêm phụ thuộc chủ yếu là "ưu tiên các thư viện nhàm chán, được bảo trì tốt và suy nghĩ kỹ về những cái nhỏ xíu". Khi một gói phổ biến bị xâm phạm, các mã băm tệp khóa được commit của họ có nghĩa là phiên bản bị đầu độc đơn giản là không cài được, và họ đọc về sự cố thay vì sống qua nó.

**Doanh nghiệp lớn.** Một ngân hàng với bốn trăm kho mã vận hành một kho đăng ký gói nội bộ nhân bản hệ sinh thái công khai và thực thi chính sách tại điểm nghẽn đó. Một tập thư viện vàng được tuyển chọn, một khung ghi nhật ký được phê duyệt, một ứng dụng HTTP khách, một bộ phân tích JSON, là mặc định, và bất cứ thứ gì khác đòi hỏi một ngoại lệ có tài liệu. Một mô hình nguồn nội bộ cho phép bất kỳ đội nào đóng góp vào các thư viện dùng chung đó trong khi một nhóm nền tảng nhỏ sở hữu sức khỏe của chúng. Các lần nâng cấp phối hợp triển khai một bản vá bảo mật qua cả bốn trăm kho mã bằng pull request tự động trong vài ngày, và mỗi bản dựng phát ra một SBOM vào một kho trung tâm. Khi một lỗ hổng nghiêm trọng được công bố, họ chạy một truy vấn và biết mức phơi nhiễm của mình trước khi chu kỳ tin tức kết thúc.

**Chính phủ.** Một cơ quan liên bang mua sắm phần mềm theo các yêu cầu nguồn gốc và SBOM truy vết về Sắc lệnh Hành pháp 14028. Nhà cung cấp phải giao một SBOM đọc được bằng máy với mỗi bản phát hành và chứng minh nguồn gốc bản dựng phù hợp khung SLSA, để cơ quan có thể xác minh mỗi hiện vật đến từ nguồn được tuyên bố. Nội bộ, lập trình viên chỉ có thể cài đặt từ một danh sách phần mềm được phê duyệt do một gương nội bộ phục vụ không có đường trực tiếp đến internet công khai. Khả năng hỗ trợ dài hạn dẫn dắt các lựa chọn: họ ưu tiên các phụ thuộc có bảo trì ổn định và giấy phép rõ ràng, vì một hệ thống có thể chạy mười lăm năm và phải vá được trong cả khoảng thời gian đó. Khi một thành phần hết vòng đời, một cuộc di chuyển có kế hoạch thay thế nó thay vì một sự cố khẩn cấp.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của kỷ luật phụ thuộc chủ yếu được đo bằng những thảm họa không bao giờ xảy ra. Một tệp khóa được commit và bản dựng tái tạo được gần như không tốn gì để áp dụng và loại bỏ cả một lớp lỗi "chạy trên máy của tôi" và lỗi môi trường thực không tái hiện được, mỗi cái có thể đốt nhiều ngày thời gian kỹ sư cấp cao. Nhịp cập nhật tự động chuyển đổi lần nâng cấp khẩn cấp nhiều tuần thỉnh thoảng, loại làm đình trệ lộ trình và kiệt sức một đội, thành một tiếng ù đều đặn thấp của các thay đổi nhỏ được hợp nhất. Qua một danh mục nhiều kho mã, sự chuyển từ hiếm-và-khổng-lồ sang thường-xuyên-và-nhỏ-xíu là một trong những thay đổi quy trình có đòn bẩy cao nhất sẵn có cho một tổ chức kỹ thuật.

Lập luận tổng chi phí sở hữu là về những gì bạn mang qua nhiều năm, không phải những gì bạn chi trong sprint này. Các phụ thuộc không được quản lý tích tụ lặng lẽ: các phiên bản lỗi thời không thể nâng cấp nếu không viết lại, giấy phép tạo rủi ro pháp lý mà không ai tính giá, và một đồ thị rối rắm đến mức một bản vá bắt buộc đơn lẻ kích hoạt một chuỗi thay đổi phá vỡ. Chi phí của việc không làm điều này đến cùng một lúc và vào thời điểm tệ nhất, trong một sự cố bảo mật hay một cuộc kiểm toán hay một cuộc di chuyển bắt buộc, khi hóa đơn cho nhiều năm bảo trì bị trì hoãn đến hạn kèm lãi. Để thuyết phục ban lãnh đạo, hãy đóng khung bằng ngôn ngữ của họ: bản dựng tái tạo được giảm chi phí sự cố, SBOM cắt thời gian phản ứng lỗ hổng từ vài ngày xuống vài phút, và thư viện được phê duyệt cộng nguồn gốc giữ bạn đủ điều kiện cho các hợp đồng chịu quy định và chính phủ mà nếu không bạn sẽ bị loại.

## Phản mẫu và cạm bẫy

- **Không có tệp khóa, hoặc tệp khóa không được commit:** bản dựng phân giải mới mỗi lần, nên không ai có thể tái tạo đáng tin những gì đã phát hành hay đã hỏng.
- **"latest" trôi nổi trong môi trường thực:** bất cứ gì kho đăng ký phục vụ vào phút đó trở thành bản phát hành của bạn, chưa rà soát và không truy vết được.
- **Không bao giờ cập nhật cho đến khi bị ép:** nhiều năm trôi dạt sụp thành một lần nâng cấp khẩn cấp đáng sợ, rủi ro cao dưới áp lực lỗ hổng.
- **Mệt mỏi vì bot cập nhật:** một vòi nước pull request không gom huấn luyện đội phớt lờ tất cả, kể cả những cái khẩn cấp.
- **Phụ thuộc tràn lan:** thêm gói theo phản xạ cho tính năng tầm thường, nuôi một đồ thị không bảo trì nổi và bề mặt tấn công rộng.
- **Không có bản kiểm kê:** không có SBOM, trả lời "chúng ta có bị ảnh hưởng không?" nghĩa là nhiều ngày khảo cổ thủ công qua các kho mã.
- **Tin kho đăng ký công khai một cách mù quáng:** kéo trực tiếp phơi bày bạn trước ngừng hoạt động, phiên bản bị rút, nhầm lẫn phụ thuộc và typosquatting.
- **Phớt lờ phụ thuộc bắc cầu:** chỉ quản trị những gì bạn gọi tên trong khi phần lớn rủi ro ẩn ở một tầng bên dưới.
- **Giấy phép chưa kiểm duyệt:** kéo mã có giấy phép xung đột với cách bạn phát hành, chỉ phát hiện trong kiểm toán hoặc thâu tóm.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Phụ thuộc được thêm tự do không đánh giá. Không có tệp khóa được commit, bản dựng không tái tạo được, cập nhật chỉ xảy ra trong các tình huống khẩn cấp bắt buộc, và không ai liệt kê được phần mềm chứa gì.
- **Mức 2, Phát triển:** Một số đội commit tệp khóa và có bản dựng phần lớn tái tạo được, và một chút tự động hóa mở các pull request cập nhật, nhưng thực hành không nhất quán từ kho mã này sang kho khác. Nhận thức về giấy phép và rủi ro bắc cầu không chính thức, không có chính sách, bản kiểm kê hay kiểm soát chung đối với nơi các gói đến từ đâu.
- **Mức 3, Chuẩn hóa:** Các thực hành được lập thành tài liệu và thực thi toàn tổ chức. Một trình cập nhật tự động chạy theo nhịp đều đặn với việc gom hợp lý, bản dựng cài đặt nghiêm ngặt từ tệp khóa và hỏng khi tệp khóa và tệp kê khai bất đồng, một SBOM được sinh cho mỗi bản dựng, một kho đăng ký nội bộ thực thi chính sách nguồn và giấy phép, và các phụ thuộc mới được đánh giá theo một danh sách kiểm tra bằng văn bản mà mọi đội áp dụng.
- **Mức 4, Quản lý:** Hệ phụ thuộc được đo và kiểm soát bằng dữ liệu theo các đường cơ sở. Bạn theo dõi độ trễ phiên bản (bao nhiêu phụ thuộc tụt hậu hơn một phiên bản major), thời gian trung bình để vá một lỗ hổng nghiêm trọng qua mọi hiện vật, tỷ lệ hợp nhất cập nhật tự động, độ bao phủ SBOM tính theo phần trăm các bản dựng đã phát hành, và số lượng xung đột hình thoi chưa giải quyết cùng ngoại lệ chính sách. Những chỉ số này chặn bản phát hành và dẫn dắt nơi bạn dành công sức, để nâng cấp và khắc phục được quản lý bằng bằng chứng thay vì bởi ai la to nhất.
- **Mức 5, Điều phối:** Quản lý phụ thuộc được cải tiến liên tục và tích hợp trong toàn tổ chức. Nguồn gốc bản dựng và chứng thực được nắm bắt và xác minh, SBOM truy vấn được qua cả danh mục để phản ứng lỗ hổng tức thì, các lần nâng cấp phối hợp triển khai qua nhiều kho mã một cách tự động, thư viện vàng được tuyển chọn và nguồn nội bộ hóa, và toàn bộ hệ thống thích ứng khi hệ sinh thái, mối đe dọa và sắc lệnh mua sắm dịch chuyển.

## Ý tưởng để thảo luận

1. Lằn ranh phù hợp cho đội bạn nằm ở đâu giữa việc tự viết một tiện ích nhỏ và gánh một phụ thuộc cho nó?
2. Ràng buộc phiên bản của bạn nên lỏng hay chặt đến mức nào, và câu trả lời có khác nhau giữa ứng dụng với thư viện được công bố không?
3. Các bản cập nhật patch rủi ro thấp có nên tự hợp nhất khi kiểm thử xanh không, và bộ kiểm thử của bạn cần gì để làm điều đó an toàn?
4. Một kho đăng ký hoặc gương nội bộ có đáng chi phí vận hành cho quy mô và hồ sơ rủi ro của tổ chức bạn không?
5. Bạn sẽ ưu tiên phụ thuộc nào để đóng gói trực tiếp nhằm kiểm soát tối đa, và phụ thuộc nào để lại trên kho đăng ký công khai?
6. Cần gì để sinh và thực sự dùng một SBOM cho mọi hiện vật bạn phát hành, bắt đầu từ quý này?

## Những điểm cần ghi nhớ

- Phần lớn phần mềm của bạn là mã vay mượn; quản lý nó tốt là một kỷ luật kỹ thuật cốt lõi, không phải chuyện nghĩ đến sau.
- Commit tệp khóa và đòi hỏi bản dựng tái tạo được, xác định để cùng đầu vào luôn cho cùng đầu ra.
- Cập nhật liên tục theo các bước nhỏ tự động thay vì những bước nhảy hiếm hoi, bị ép buộc, đáng sợ.
- Thêm phụ thuộc một cách có chủ đích theo một ngưỡng bằng văn bản; phụ thuộc rẻ nhất để quản lý là phụ thuộc bạn không bao giờ gánh.
- Sinh một SBOM và nắm bắt nguồn gốc để bạn luôn biết những gì có trong phần mềm của mình và nó đến từ đâu.
- Kiểm soát nguồn của bạn bằng một kho đăng ký nội bộ để phòng thủ trước nhầm lẫn phụ thuộc, typosquatting và sự cố thượng nguồn.

## Tài liệu tham khảo và đọc thêm

- Sắc lệnh Hành pháp Hoa Kỳ 14028, *Improving the Nation's Cybersecurity* (2021)
- National Institute of Standards and Technology (NIST), *Secure Software Development Framework* (SP 800-218)
- Đặc tả khung SLSA (Supply-chain Levels for Software Artifacts), Open Source Security Foundation
- Đặc tả OWASP CycloneDX và đặc tả SPDX, cho các định dạng SBOM
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
- Tài liệu dự án Reproducible Builds
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
