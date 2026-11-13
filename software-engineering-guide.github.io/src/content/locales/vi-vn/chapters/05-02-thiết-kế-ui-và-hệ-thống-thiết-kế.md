# 5.2 Thiết kế UI và hệ thống thiết kế

## Tổng quan và động lực

[Thiết kế giao diện người dùng (UI)](https://en.wikipedia.org/wiki/User_interface_design) là nghề tạo hình những gì người ta thấy và chạm: bố cục, [kiểu chữ](https://en.wikipedia.org/wiki/Typography), màu sắc, khoảng cách, điều khiển và trạng thái. Một [hệ thống thiết kế](https://en.wikipedia.org/wiki/Design_system) lấy nghề đó và biến nó thành một tài sản dùng chung, tái sử dụng được, được quản trị: một tập nguyên tắc, thành phần, mẫu và token có tài liệu mà mọi đội dựa vào, để toàn bộ sản phẩm trông và hành xử như một. Thiết kế UI quyết định một màn hình nên trông thế nào. Một hệ thống thiết kế quyết định mười nghìn màn hình qua nhiều đội giữ mạch lạc ra sao.

Với một tổ chức lớn, hệ thống thiết kế là khoản đầu tư có đòn bẩy cao nhất vào chất lượng UI và tốc độ phân phối. Không có nó, mọi đội phát minh lại nút, biểu mẫu, hộp thoại và xử lý lỗi, mỗi cái hơi khác nhau, mỗi cái được bảo trì riêng, mỗi cái hỏng riêng. Người dùng trả giá bằng sự bối rối và mất niềm tin; doanh nghiệp trả giá bằng công sức trùng lặp và chất lượng không đều. Một hệ thống thiết kế biến các quyết định thiết kế một lần thành vốn tái sử dụng: giải quyết [khả năng tiếp cận](https://en.wikipedia.org/wiki/Accessibility), [tính đáp ứng](https://en.wikipedia.org/wiki/Responsive_web_design) và thương hiệu một lần trong một thành phần, và mọi đội thừa hưởng kết quả.

Doanh nghiệp và chính phủ thêm hai áp lực cụ thể. Thứ nhất, quy mô: hàng trăm ứng dụng, nhiều cái do nhà cung cấp xây hoặc có được qua sáp nhập, tất cả cần mang cảm giác như một tổ chức. Thứ hai, tuổi thọ và thay đổi: thương hiệu được làm mới, cơ quan được tái tổ chức, và một nền tảng đơn lẻ có thể cần phục vụ nhiều thương hiệu hay cơ quan con từ một cơ sở mã. Một hệ thống thiết kế được kiến trúc tốt, với chủ đề hóa và token hóa đúng cách, khiến những thay đổi sâu rộng này khả thi thay vì thảm họa.

## Các nguyên tắc chính

- Nhất quán hạ [tải nhận thức](https://en.wikipedia.org/wiki/Cognitive_load); một nút nên trông và hành xử giống nhau ở mọi nơi.
- Quyết định thiết kế là tài sản: nắm bắt chúng một lần dưới dạng thành phần và token tái sử dụng.
- Token là nguồn sự thật cho các quyết định thị giác; thành phần tiêu thụ token, không bao giờ giá trị mã hóa cứng.
- Khả năng tiếp cận và tính đáp ứng được xây vào thành phần, không gắn thêm theo từng màn hình.
- Một hệ thống thiết kế là một sản phẩm có người dùng (lập trình viên và nhà thiết kế), không phải sản phẩm bàn giao một lần.
- Phân cấp thị giác dẫn dắt sự chú ý: kiểu chữ, màu sắc và không gian nên làm cho tầm quan trọng hiển nhiên.
- Quản trị giữ một hệ thống mạch lạc; đóng góp giữ nó sống.

## Khuyến nghị

### Cấu trúc hệ thống theo các tầng: token, thành phần, mẫu

Token thiết kế là các giá trị có tên, bất khả tri nền tảng cho màu sắc, khoảng cách, kiểu chữ, bán kính, độ nổi và chuyển động: các quyết định nguyên tử. Hãy xây chúng theo bậc: một bảng màu nguyên thủy (giá trị thô), token ngữ nghĩa (`color-action-primary`, `space-inset-md`) mang ý nghĩa, và token cấp thành phần ở nơi bạn cần. Thành phần tiêu thụ token ngữ nghĩa, nên một thay đổi duy nhất lan truyền ở mọi nơi. Phía trên thành phần là các mẫu: những cách kết hợp đã được chứng minh như bảng dữ liệu, biểu mẫu nhiều bước, hay trạng thái rỗng. Hãy lập tài liệu cả ba tầng ở một nơi, với ví dụ sống và hướng dẫn sử dụng.

### Làm đúng các nền tảng thị giác

Thiết lập một thang kiểu chữ với phân cấp rõ ràng và khoảng cách dòng rộng rãi để dễ đọc, và giữ một tập kích thước và độ đậm hạn chế. Định nghĩa màu sắc như một hệ thống, với độ tương phản đủ cho khả năng tiếp cận (xem chương khả năng tiếp cận) và vai trò ngữ nghĩa, thay vì các sắc thô rải khắp UI. Dùng một thang khoảng cách và lưới bố cục để căn chỉnh và nhịp điệu giữ nhất quán mà không đoán mò theo từng màn hình. Phân cấp thị giác nên làm cho hành động chính và thông tin quan trọng nhất hiển nhiên chỉ trong nháy mắt.

### Thiết kế đáp ứng và ưu tiên di động

Hãy thiết kế cho khung nhìn nhỏ nhất hợp lý trước, rồi nâng cấp cho màn hình lớn hơn. Điều này buộc bạn ưu tiên nội dung và điều khiển thiết yếu. Dùng bố cục linh hoạt và đơn vị tương đối để giao diện thích ứng với bất kỳ màn hình nào, thay vì nhảy giữa vài điểm ngắt cố định. Làm mục tiêu cảm ứng đủ lớn, và bảo đảm tương tác hoạt động với cảm ứng, chuột và bàn phím. Đặc biệt trong chính phủ, hãy giả định một phần đáng kể người dùng của bạn dùng thiết bị nhỏ, cũ, hoặc giá rẻ.

### Biến bàn giao thiết kế-sang-mã và sự tương đương thành mối quan tâm hạng nhất

Một hệ thống thiết kế chỉ hoàn vốn khi UI được phát hành khớp với thiết kế dự định và tiếp tục khớp. Hãy hướng tới một nguồn sự thật duy nhất: token xuất từ công cụ thiết kế nuôi trực tiếp vào mã, để nhà thiết kế và kỹ sư tham chiếu cùng giá trị. Cung cấp một thư viện thành phần đã mã hóa mà kỹ sư sẽ thực sự dùng, với cùng tên và thuộc tính như thành phần thiết kế. Dùng kiểm thử hồi quy thị giác (so sánh tự động UI đã kết xuất với ảnh đường cơ sở được duyệt) và kiểm tra rà soát thiết kế để bắt sự trôi. Và đo "sự tương đương thiết kế-mã" như một chỉ số sức khỏe tường minh: tỷ lệ UI được xây từ thành phần hệ thống so với mã làm một lần.

### Hỗ trợ chủ đề hóa và nhãn trắng ở quy mô doanh nghiệp

Hãy kiến trúc cho nhiều thương hiệu từ đầu nếu có bất kỳ khả năng nào bạn cần chúng. Vì thành phần tiêu thụ token ngữ nghĩa, một chủ đề chỉ là một tập giá trị token khác, nên một lần làm mới thương hiệu hay thương hiệu con mới trở thành một thay đổi dữ liệu, không phải viết lại mã. Hỗ trợ chủ đề sáng và tối, chế độ tương phản cao, và thương hiệu theo từng người thuê qua cùng cơ chế. Giữ logic đặc thù thương hiệu ngoài thành phần, và đẩy nó vào tập token và cấu hình thay thế.

### Quản trị hệ thống như một sản phẩm

Hãy cho hệ thống thiết kế một đội chuyên trách, lộ trình, phiên bản, nhật ký thay đổi và kênh hỗ trợ. Nêu rõ cách các đội đóng góp thành phần mới, và cách chúng được rà soát và thăng cấp. Cân bằng kiểm soát trung tâm (để bảo toàn sự mạch lạc và khả năng tiếp cận) với một mô hình đóng góp (để hệ thống tiến hóa theo nhu cầu thực thay vì trở thành nút thắt). Truyền đạt rõ ràng việc ngừng sử dụng và di chuyển, và cho các đội tiêu thụ đủ thời gian báo trước.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Xây một hệ thống thiết kế | Nhất quán, tốc độ, khả năng tiếp cận một lần, đổi thương hiệu dễ hơn | Chi phí ban đầu và liên tục, cần đội chuyên trách |
| Áp dụng hệ thống có sẵn | Khởi đầu nhanh, mẫu đã được chứng minh | Diện mạo chung chung, khó khớp thương hiệu và nhu cầu riêng |
| Quản trị trung tâm nghiêm ngặt | Mạch lạc, chất lượng, khả năng tiếp cận được bảo đảm | Có thể nghẽn các đội, cảm giác quan liêu |
| Mô hình đóng góp mở | Tiến hóa theo nhu cầu thực, quyền sở hữu chung | Rủi ro trôi và không nhất quán nếu thiếu rà soát |
| Token hóa và chủ đề hóa nặng | Đổi thương hiệu rẻ và hỗ trợ đa thương hiệu | Nhiều trừu tượng hơn, đường cong học dốc hơn |

Hệ thống thiết kế đánh đổi chi phí ban đầu và quản trị lấy sự nhất quán và vận tốc dài hạn. Với một sản phẩm nhỏ có một đội, chi phí chung có thể không hoàn vốn. Với một tổ chức lớn có nhiều đội và sản phẩm sống lâu, câu hỏi không phải có nên có hệ thống không mà là đầu tư bao nhiêu và quản trị thế nào. Sự hối tiếc phổ biến nhất là đầu tư thiếu vào quản trị và công cụ tương đương: hệ thống tồn tại trên giấy, nhưng các đội lặng lẽ trôi khỏi nó.

## Câu hỏi để thảo luận với đội của bạn

1. **Kiến trúc token của chúng ta được phân bậc thế nào, và thành phần có bị cấm dùng giá trị mã hóa cứng không?** Toàn bộ phần thưởng của một hệ thống thiết kế (đổi thương hiệu rẻ, chủ đề hóa đa thương hiệu, khả năng tiếp cận giải quyết một lần) phụ thuộc vào việc thành phần tiêu thụ token ngữ nghĩa như `color-action-primary` thay vì sắc thô và giá trị điểm ảnh rải khắp mã. Hãy quyết định các bậc ngay bây giờ: một bảng màu nguyên thủy, token ngữ nghĩa mang ý nghĩa, và token cấp thành phần chỉ ở nơi bạn thực sự cần. Trừu tượng quá mức là rủi ro thật, nên hãy thống nhất bao nhiêu tầng là quá nhiều và một lập trình viên tìm đúng token nhanh thế nào. Hãy mang một lệnh grep các màu và khoảng cách mã hóa cứng qua cơ sở mã của bạn làm bằng chứng về sự trôi. Nếu logic thương hiệu bị nướng vào thành phần, một lần đổi thương hiệu trở thành viết lại mã thay vì thay đổi cấu hình, đúng là thảm họa mà token hóa tồn tại để ngăn.

2. **Chúng ta đo và bảo vệ sự tương đương thiết kế-mã thế nào, và công cụ nào bắt sự trôi tự động?** Một hệ thống thiết kế chỉ tồn tại dưới dạng tệp thiết kế là một tờ nhãn dán: kỹ sư dù sao cũng xây lại mọi thứ và UI được phát hành từ từ phân kỳ khỏi ý định. Hãy thống nhất một chỉ số tương đương tường minh (tỷ lệ UI được xây từ thành phần hệ thống so với mã làm một lần) và nối kiểm thử hồi quy thị giác vào CI để màn hình đã kết xuất được so sánh với đường cơ sở được duyệt. Điều này quan trọng ở quy mô doanh nghiệp và chính phủ vì hàng trăm ứng dụng, nhiều cái do nhà cung cấp xây hay thừa hưởng qua sáp nhập, tất cả cần mang cảm giác như một tổ chức. Hãy mang con số tương đương hiện tại và danh sách các thành phần theo yêu cầu hàng đầu mà các đội liên tục xây lại. Nếu không ai sở hữu chỉ số hay bộ hồi quy, sự trôi đã đang lặng lẽ thắng.

3. **Chúng ta quản trị đóng góp, ngừng sử dụng và di chuyển thế nào để hệ thống không nghẽn các đội cũng không phân mảnh?** Kiểm soát trung tâm nghiêm ngặt bảo đảm sự mạch lạc và khả năng tiếp cận nhưng có thể biến đội hệ thống thiết kế thành nút thắt mà các đội đi vòng; đóng góp mở giữ hệ thống sống nhưng mạo hiểm các biến thể phân kỳ không có rà soát. Hãy quyết định đường đóng góp: một đội đề xuất thành phần mới thế nào, ai rà soát nó, và nó được thăng cấp ra sao. Tương tự, hãy thống nhất cách bạn truyền đạt các thay đổi phá vỡ, vì ngừng sử dụng mà không hỗ trợ di chuyển và thời gian báo trước khiến các đội tiêu thụ đình trệ hoặc rẽ nhánh. Hãy mang các ví dụ về thành phần các đội xây ngoài hệ thống và hỏi vì sao họ không đóng góp trở lại. Câu trả lời thường hé lộ liệu quản trị của bạn là một dịch vụ hay một chướng ngại.

4. **Làm sao chúng ta bảo đảm khả năng tiếp cận được giải quyết một lần bên trong thành phần, và cái gì ngăn một đội phát hành một thành phần làm một lần không tiếp cận được?** Lập luận mạnh nhất cho một hệ thống thiết kế là độ tương phản màu, trạng thái tiêu điểm, vận hành bàn phím và ngữ nghĩa trình đọc màn hình được giải quyết một lần và thừa hưởng ở mọi nơi, nhưng lời hứa đó sụp đổ ngay khoảnh khắc các đội tự tay làm điều khiển riêng. Với một tổ chức lớn đây là nơi rủi ro pháp lý và danh tiếng lớn nhất nằm, vì một biểu mẫu thanh toán hay bộ chọn ngày không tiếp cận được đơn lẻ có thể chặn người dùng thật và kích hoạt phàn nàn qua mọi sản phẩm đã sao chép nó. Hãy cân nhắc thực thi trung tâm (thành phần tiếp cận được cộng một linter hay cổng rà soát từ chối đánh dấu thô) đối chiếu với quyền tự chủ của đội, và quyết định lằn ranh cứng ở đâu. Hãy mang kết quả của một cuộc kiểm toán khả năng tiếp cận, danh sách thành phần cùng tình trạng phù hợp của chúng, và số điều khiển theo yêu cầu mà các đội xây lại ngoài hệ thống. Trong bối cảnh doanh nghiệp và chính phủ đây không phải điều dễ chịu: các nghĩa vụ như WCAG, Section 508 và EN 301 549 biến sự phù hợp thành yêu cầu mua sắm và kiểm toán, nên một thư viện thành phần có sự phù hợp được lập tài liệu bản thân là một tài sản tuân thủ.

5. **Hệ thống này phải phục vụ bao nhiêu thương hiệu, người thuê và chủ đề, và chúng ta đã kiến trúc tầng token cho điều đó bây giờ thay vì trang bị bổ sung sau chưa?** Chủ đề hóa rẻ nếu bạn thiết kế cho nó và tàn bạo nếu không, vì một thương hiệu hay người thuê chưa từng được lường trước buộc logic thương hiệu quay lại vào thành phần và phá hỏng toàn bộ ý nghĩa của token hóa. Với một đội lớn quyết định này định hình nhiều năm công việc: một nền tảng phải phục vụ nhiều thương hiệu, một chủ đề sáng và tối, chế độ tương phản cao, và thương hiệu theo từng người thuê cần một tầng token ngữ nghĩa đủ sạch để một chủ đề chỉ là một tập giá trị khác. Hãy cân bằng sự linh hoạt đó với trừu tượng quá mức, vì một cây token không ai điều hướng được bản thân là một thất bại. Hãy mang lộ trình các thương hiệu và người thuê bạn có thể thấy trước, số chủ đề đang dùng hôm nay, và bất kỳ thành phần nào đã rò rỉ logic đặc thù thương hiệu. Trong bối cảnh doanh nghiệp và chính phủ, sáp nhập, mua lại và tái tổ chức cơ quan thường xuyên thêm các thương hiệu bạn không hoạch định, nên kiến trúc cho đa thương hiệu từ đầu là sự khác biệt giữa một thay đổi dữ liệu và một cuộc viết lại nhiều năm.

6. **Chúng ta sẽ di chuyển các ứng dụng cũ và do nhà cung cấp xây lên hệ thống thế nào, và đội hệ thống thiết kế được tài trợ ra sao để sống sót chu kỳ ngân sách kế tiếp?** Một hệ thống thiết kế chỉ mang lợi tức khi các sản phẩm thật áp dụng nó, vậy mà các ứng dụng khó chuyển đổi nhất là những cái cũ và thuê ngoài cần nó nhất, và đội duy trì hệ thống thường là đội đầu tiên bị cắt khi ngân sách thắt chặt. Với một tổ chức lớn bạn phải quyết định giữa di chuyển nổ lớn và tăng dần, và làm sao khiến nhà cung cấp xây trên thành phần của bạn thay vì xung quanh chúng. Hãy mang bản kiểm kê các ứng dụng với điểm tương đương hiện tại của chúng, ước tính công sức di chuyển cho mỗi ứng dụng, và các đòn bẩy hợp đồng bạn nắm với nhà cung cấp. Trong bối cảnh doanh nghiệp và chính phủ, hãy viết sự phù hợp hệ thống thiết kế vào điều khoản mua sắm để công việc nhà cung cấp mới đáp xuống hệ thống theo mặc định, và tài trợ đội duy trì như hạ tầng dùng chung bền vững, vì một hệ thống mất người quản lý trong một cuộc tái tổ chức trôi trở lại phân mảnh trong vòng một năm.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với hai hay ba kỹ sư và không có đường băng dư, đừng xây một hệ thống được quản trị. Hãy dành một hai ngày định nghĩa một tập nhỏ token ngữ nghĩa cho màu, khoảng cách và kiểu chữ, cộng một chục thành phần dùng chung, tất cả trong một tệp mà cả đội tham chiếu. Hãy dựa vào một thư viện nguyên thủy có sẵn cho những phần khó, và đừng mã hóa cứng gì để lần đổi thương hiệu thực đầu tiên của bạn là một thay đổi token thay vì viết lại.

**Doanh nghiệp nhỏ.** Không có nhà thiết kế riêng và ngân sách eo hẹp, hãy mua thay vì xây: áp dụng một thư viện thành phần hay bộ UI đã được chứng minh và chủ đề hóa nhẹ theo thương hiệu của bạn. Mục tiêu của bạn là một sản phẩm nhất quán, tiếp cận được mà không bố trí nhân sự cho một đội hệ thống thiết kế, vì vậy hãy ưu tiên một hệ thống đi kèm khả năng tiếp cận và tính đáp ứng ngay từ đầu. Hãy cưỡng lại cám dỗ rẽ nhánh nó, vì một bản sao tùy chỉnh bạn không bảo trì được trở thành khoản nợ ngay khoảnh khắc dự án thượng nguồn di chuyển.

**Doanh nghiệp lớn.** Vấn đề là sự mạch lạc qua nhiều đội và sản phẩm sống lâu, vì vậy hãy coi hệ thống thiết kế là hạ tầng dùng chung được quản trị với đội chuyên trách, phiên bản và lộ trình. Hãy theo dõi sự tương đương thiết kế-mã như một chỉ số thực, nối kiểm thử hồi quy thị giác vào CI, và kiến trúc tầng token cho nhiều thương hiệu và chủ đề từ đầu. Hãy ngân sách tường minh chi phí quản trị và di chuyển, và quản lý việc áp dụng như một danh mục thay vì giả định các đội sẽ tự trôi vào hệ thống.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Sự phù hợp khả năng tiếp cận với các tiêu chuẩn như WCAG, Section 508 và EN 301 549 là yêu cầu pháp lý, không phải sở thích, nên một thư viện thành phần có sự phù hợp được lập tài liệu trở thành tài sản tuân thủ. Hãy ưu tiên hoặc mở rộng một hệ thống thiết kế công dùng chung để công dân gặp cùng mẫu qua các dịch vụ, viết việc sử dụng hệ thống thiết kế vào hợp đồng nhà cung cấp, và công bố công khai thành phần cùng hướng dẫn của bạn để các cơ quan và nhà cung cấp của họ có thể áp dụng chúng và chịu trách nhiệm theo chúng.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp hai kỹ sư liên tục xây lại nút và trường biểu mẫu hơi khác nhau trên mỗi màn hình mới, và sản phẩm bắt đầu trông như chắp vá. Thay vì một hệ thống nặng nề, họ dành hai ngày định nghĩa một tập nhỏ token thiết kế ngữ nghĩa cho màu, khoảng cách và kiểu chữ, cộng khoảng một chục thành phần dùng chung, tất cả trong một tệp mà cả đội tham chiếu. Vì không có gì mã hóa cứng, khi nhà thiết kế đầu tiên họ tuyển đề xuất một bảng màu gọn gàng hơn, lần làm mới là một thay đổi token đáp xuống khắp ứng dụng trong một buổi chiều thay vì một cuộc cày từng màn hình.

**Doanh nghiệp lớn.** Một công ty phần mềm toàn cầu với hàng chục đội sản phẩm xây một hệ thống thiết kế token hóa với thư viện thành phần đã mã hóa dùng chung. Token ngữ nghĩa cho phép họ phát hành một lần làm mới thương hiệu đầy đủ qua mọi sản phẩm trong vài tuần, thay vì một cuộc cày nhiều năm theo từng đội, vì thay đổi là một tập token mới thay vì hàng nghìn chỉnh sửa màu mã hóa cứng. Sự tương đương thiết kế-mã, được theo dõi như một chỉ số bảng điều khiển, tăng khi các đội thay thế thành phần theo yêu cầu, điều cắt giảm việc bảo trì UI trùng lặp.

**Chính phủ.** Một chính phủ quốc gia tạo một hệ thống thiết kế chung cho dịch vụ công (thành phần dùng chung, mẫu, và khả năng tiếp cận tích hợp sẵn) được bắt buộc qua các cơ quan. Một công dân chuyển giữa dịch vụ thuế, dịch vụ y tế và dịch vụ cấp phép gặp cùng đầu trang, điều khiển biểu mẫu và mẫu lỗi, điều xây dựng niềm tin và rút ngắn đường cong học. Các cơ quan và nhà cung cấp của họ phát hành nhanh hơn và tiếp cận được hơn vì các vấn đề khó được giải quyết tập trung, và chính phủ có thể cập nhật hướng dẫn hay bản sửa khả năng tiếp cận một lần và để nó lan truyền ở mọi nơi.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của một hệ thống thiết kế đến từ việc loại bỏ trùng lặp và tăng tốc phân phối. Thay vì mọi đội thiết kế và xây cùng các thành phần, họ ghép từ một thư viện dùng chung, điều tăng tốc phân phối một cách đo được và giải phóng nhà thiết kế cùng kỹ sư cho công việc đặc thù sản phẩm. Khả năng tiếp cận và tính đáp ứng, giải quyết một lần trong thành phần, tiết kiệm cho bạn chi phí khắc phục theo từng dự án. Đổi thương hiệu và chủ đề hóa từng mất nhiều năm nay mất vài tuần.

Về TCO, chi phí áp dụng là một đội chuyên trách, công cụ, và công sức để các sản phẩm hiện có di chuyển lên hệ thống. Chi phí của việc không áp dụng được trả liên tục: xây dựng và bảo trì trùng lặp qua các đội, UI không nhất quán và không tiếp cận được tạo rủi ro hỗ trợ và pháp lý, và đổi thương hiệu chậm, tốn kém. Vì sự trùng lặp rải qua ngân sách của nhiều đội, thật dễ bỏ qua: một hệ thống thiết kế làm chi phí ẩn đó hiển thị và nắm bắt nó ở một nơi.

Để trình bày lập luận với ban lãnh đạo, hãy định lượng công việc thành phần trùng lặp qua các đội, mức tăng thời gian đưa ra thị trường từ việc ghép, và chi phí cùng thời gian của lần đổi thương hiệu gần nhất của bạn so với những gì một hệ thống token hóa cho phép. Đóng khung hệ thống là hạ tầng dùng chung với một chỉ số áp dụng đo được (phần trăm tương đương), để giá trị của nó có thể được theo dõi theo thời gian thay vì chỉ được khẳng định.

## Phản mẫu và cạm bẫy

- **Hệ thống thiết kế như tờ nhãn dán**: một tệp thiết kế tĩnh không có thành phần đã mã hóa, nên kỹ sư dù sao cũng xây lại mọi thứ.
- **Giá trị mã hóa cứng ở khắp nơi**: màu và khoảng cách rải khắp mã, khiến chủ đề hóa và đổi thương hiệu là không thể.
- **Không quản trị**: hệ thống phân mảnh khi các đội thêm biến thể phân kỳ; sự nhất quán xói mòn.
- **Quản trị không có đóng góp**: đội trung tâm trở thành nút thắt và các đội đi vòng nó.
- **Bỏ qua sự tương đương**: UI đã mã hóa trôi khỏi ý định thiết kế và không ai đo khoảng cách.
- **Trừu tượng quá mức**: quá nhiều token và tầng đến mức không ai tìm hay dùng đúng cái.
- **Logic thương hiệu nướng vào thành phần**: khiến đa thương hiệu và chủ đề hóa là viết lại mã thay vì thay đổi cấu hình.
- **Thay đổi phá vỡ không hỗ trợ di chuyển**: các đội tiêu thụ đình trệ hoặc rẽ nhánh hệ thống.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Mỗi đội xây UI của riêng mình tùy nghi và phản ứng. Không thành phần dùng chung, diện mạo và hành vi không nhất quán, màu và khoảng cách mã hóa cứng theo từng màn hình. Mọi lần đổi thương hiệu là một cuộc cày thủ công từng màn hình.

**Mức 2: Phát triển.** Một hướng dẫn phong cách hay thư viện thành phần dùng chung tồn tại nhưng không đầy đủ, tùy chọn, và thường lệch đồng bộ giữa thiết kế và mã. Một số đội dùng nó, số khác không, và các thực hành cơ bản khác nhau nhiều từ đội này sang đội khác.

**Mức 3: Chuẩn hóa.** Một hệ thống thiết kế token hóa với thư viện đã mã hóa được duy trì, tài liệu và quản trị được lập tài liệu và thực thi trên toàn tổ chức. Thành phần tiêu thụ token ngữ nghĩa, chủ đề hóa được hỗ trợ, và khả năng tiếp cận cùng tính đáp ứng được xây vào thay vì gắn thêm theo từng màn hình.

**Mức 4: Quản lý.** Hệ thống được đo và kiểm soát bằng dữ liệu theo các đường cơ sở. Sự tương đương thiết kế-mã được theo dõi như một chỉ số tường minh với mục tiêu theo từng sản phẩm, kiểm thử hồi quy thị giác chạy trong CI để bắt sự trôi, và sự phù hợp khả năng tiếp cận được đo theo tiêu chuẩn thay vì giả định. Bảng điều khiển áp dụng cho thấy độ bao phủ thành phần theo đội, và chi phí cùng thời gian của các lần đổi thương hiệu được ghi lại để cải thiện hiển thị theo thời gian.

**Mức 5: Điều phối.** Hệ thống thiết kế là một sản phẩm cải thiện liên tục, tích hợp trong toàn tổ chức và thích ứng với thay đổi. Nó có phiên bản, lộ trình và một mô hình đóng góp hoạt động, nên tiến hóa theo nhu cầu thực. Đổi thương hiệu và chủ đề mới là các thay đổi token thường lệ, chủ đề hóa đa thương hiệu và đa người thuê là bình thường, và đội loại bỏ, điều chỉnh phạm vi và thăng cấp mẫu dựa trên bằng chứng từ dữ liệu sử dụng, nuôi công cụ thiết kế và đường ống phân phối từ một nguồn sự thật duy nhất.

## Ý tưởng để thảo luận

- Làm sao bạn cân bằng quản trị trung tâm với quyền tự chủ của đội mà không phân mảnh hay gây nút thắt?
- Chỉ số đúng cho "sự tương đương thiết kế-mã" là gì, và làm sao bạn giữ nó trung thực?
- Khi nào một đội nên được phép xây một thành phần làm một lần thay vì dùng hệ thống?
- Làm sao bạn tài trợ và bố trí nhân sự cho một hệ thống thiết kế để nó sống sót qua các chu kỳ ngân sách và tái tổ chức?
- Bao nhiêu sự linh hoạt chủ đề hóa đáng với chi phí trừu tượng thêm vào?
- Làm sao bạn di chuyển ứng dụng cũ và do nhà cung cấp xây lên một hệ thống dùng chung?

## Những điểm cần ghi nhớ

- Một hệ thống thiết kế biến các quyết định thiết kế một lần thành vốn tái sử dụng, được quản trị.
- Cấu trúc nó theo tầng (token, thành phần, mẫu), với thành phần tiêu thụ token ngữ nghĩa.
- Xây khả năng tiếp cận và tính đáp ứng vào thành phần để mọi đội thừa hưởng chúng.
- Coi sự tương đương thiết kế-mã là chỉ số sức khỏe đo được, không phải giả định.
- Token hóa khiến đổi thương hiệu và chủ đề hóa đa thương hiệu là thay đổi dữ liệu, không phải viết lại.
- Quản trị hệ thống như một sản phẩm với lộ trình, phiên bản và mô hình đóng góp.
- Ở quy mô doanh nghiệp và chính phủ, một hệ thống dùng chung là khoản đầu tư UI có đòn bẩy cao nhất có sẵn.

## Tài liệu tham khảo và đọc thêm

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, các bài viết về token thiết kế và quản trị hệ thống thiết kế
- W3C Design Tokens Community Group, đặc tả định dạng
- Các hệ thống thiết kế của chính phủ (ví dụ UK Government Design System, U.S. Web Design System) như cài đặt tham chiếu
