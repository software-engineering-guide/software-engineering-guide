# 1.2 Cấu trúc đội nhóm và thiết kế tổ chức

## Tổng quan và động lực

Cách bạn chia con người thành các đội quyết định phần mềm nào bạn có thể xây và bạn xây nhanh đến đâu. Đây không phải là một phép ẩn dụ. Đó là hệ quả gần như cơ học được gọi là [Định luật Conway](https://en.wikipedia.org/wiki/Conway%27s_law): các tổ chức thiết kế ra những hệ thống phản ánh cấu trúc giao tiếp của chính họ. Nếu ba đội xây một [trình biên dịch](https://en.wikipedia.org/wiki/Compiler), bạn sẽ có một trình biên dịch ba lượt. Nếu logic thanh toán của bạn bị chia giữa một đội giao diện, một đội máy chủ và một đội cơ sở dữ liệu, mọi thay đổi về thanh toán đều cần sự phối hợp tay ba. Với một tổ chức nhỏ, điều đó còn xoay xở được. Với một tổ chức lớn, hình dạng của sơ đồ tổ chức trở thành ràng buộc chi phối đối với kỹ thuật, kiến trúc, tốc độ phân phối và chất lượng của bạn. Vì vậy, thiết kế cấu trúc đội nhóm là một hoạt động kỹ thuật hạng nhất, không phải việc nhân sự nghĩ đến sau cùng.

Cấu trúc đội nhóm (team topologies) cung cấp cho bạn một bộ từ vựng có chủ đích cho việc thiết kế này. Thay vì để cấu trúc tích tụ ngẫu nhiên qua các đợt tái tổ chức và tăng biên chế, các tổ chức trưởng thành chọn loại đội và phương thức tương tác một cách có chủ đích, và xem xét lại những lựa chọn đó khi hệ thống và hoạt động kinh doanh phát triển. Mục tiêu là giữ [tải nhận thức](https://en.wikipedia.org/wiki/Cognitive_load) của mỗi đội ở mức thấp, tức tổng lượng mà một đội phải giữ trong đầu để làm việc hiệu quả, để các đội có thể sở hữu miền của mình từ đầu đến cuối và phân phối dòng giá trị ổn định mà không phải liên tục chờ người khác.

Với doanh nghiệp và chính phủ, kỷ luật này mang tính quyết định. Các tổ chức lớn tự nhiên lan rộng thành các tầng bậc sâu, các dịch vụ dùng chung với hàng đợi dài, và các chuỗi bàn giao biến một thay đổi hai ngày thành một dự án hai tháng. Chính phủ còn thêm các ranh giới mua sắm, các đội nhà thầu và [sự phân tách nhiệm vụ](https://en.wikipedia.org/wiki/Separation_of_duties) bắt buộc làm quyền sở hữu càng bị phân mảnh. Thiết kế cấu trúc đội nhóm một cách tường minh là cách các tổ chức này giành lại dòng chảy: căn chỉnh các đội theo dòng giá trị, xây các nền tảng giảm tải nhận thức, và chọn các mẫu tương tác khiến sự phụ thuộc hiện rõ và có chủ đích thay vì ẩn giấu và thường trực.

## Các nguyên tắc chính

- Định luật Conway là không thể tránh; hãy thiết kế các đội để khớp với kỹ thuật phần mềm bạn muốn có ("chiêu thức nghịch đảo").
- Tối ưu hóa tải nhận thức của đội, không phải mức sử dụng tối đa của từng cá nhân.
- Ưu tiên các đội bám theo dòng giá trị, sở hữu một lát cắt giá trị từ đầu đến cuối.
- Nền tảng tồn tại để giảm tải nhận thức cho các đội bám theo dòng giá trị, không phải để canh cổng.
- Làm cho tương tác giữa các đội tường minh và ít: cộng tác, X-như-một-dịch-vụ, hoặc hỗ trợ.
- Giảm thiểu sự phụ thuộc; mỗi lần bàn giao giữa các đội là một hàng đợi và một rủi ro.
- Cấu trúc đội nhóm là một thiết kế sống, phải phát triển khi hệ thống và hoạt động kinh doanh thay đổi.

## Khuyến nghị

### Dùng bốn loại đội cơ bản

Cấu trúc đội nhóm định nghĩa bốn loại đội đáp ứng hầu hết nhu cầu. Đội bám theo dòng giá trị là mặc định: mỗi đội sở hữu một dòng công việc liên tục cho một sản phẩm, dịch vụ hoặc hành trình người dùng cụ thể, từ đầu đến cuối. Đội nền tảng cung cấp các sản phẩm nội bộ (tính toán, triển khai, đường ống dữ liệu, danh tính) mà các đội bám theo dòng giá trị tự phục vụ khi sử dụng, nhờ đó giảm tải nhận thức của họ. Đội hỗ trợ là các chuyên gia (kiểm thử, bảo mật, khả năng quan sát) huấn luyện các đội bám theo dòng giá trị xây dựng một năng lực, rồi lùi lại. Đội hệ thống con phức tạp sở hữu các thành phần cần chuyên môn sâu (một công cụ định giá, một [bộ mã hóa video](https://en.wikipedia.org/wiki/Video_codec), một mô-đun mật mã), nơi việc mọi đội đều nắm kiến thức đó là vô nghĩa. Phần lớn các đội của bạn nên là đội bám theo dòng giá trị; ba loại còn lại tồn tại để hỗ trợ họ.

### Áp dụng chiêu thức Conway nghịch đảo

Vì phần mềm phản ánh cấu trúc tổ chức của bạn, hãy định hình các đội để tạo ra phần mềm bạn muốn. Muốn các dịch vụ liên kết lỏng với ranh giới rõ ràng? Hãy tạo các đội liên kết lỏng với ranh giới sở hữu rõ ràng. Muốn một năng lực thanh toán được phát hành theo lịch riêng? Hãy lập một đội thanh toán sở hữu nó từ đầu đến cuối. Đừng chống lại Định luật Conway bằng sự phối hợp anh hùng. Hãy vẽ lại ranh giới các đội để kiến trúc bạn muốn trở thành con đường ít trở ngại nhất.

### Quản lý tải nhận thức một cách tường minh

Một đội chỉ có thể làm chủ được chừng ấy. Tải nhận thức bao gồm độ phức tạp của miền nghiệp vụ, các công nghệ, gánh nặng vận hành và bề rộng của các bên liên quan. Khi một đội sở hữu quá nhiều dịch vụ không liên quan, cả chất lượng lẫn tốc độ đều sụp đổ. Vì vậy hãy giới hạn trách nhiệm của mỗi đội trong một miền mà họ thực sự làm chủ được, và dùng nền tảng cùng các đội hỗ trợ để gỡ bớt độ phức tạp không tạo khác biệt khỏi đĩa của họ. Giữ các đội ở khoảng năm đến chín người: đủ nhỏ để giao tiếp dễ dàng và, nói vui, để ăn no với vài chiếc pizza.

### Chọn phương thức tương tác một cách có chủ đích

Hãy giới hạn tương tác giữa các đội trong ba phương thức. Cộng tác là công việc gần gũi, băng thông cao giữa hai đội trong một khoảng thời gian nhất định; nó mạnh mẽ cho việc khám phá nhưng tốn kém, nên hãy giữ nó tạm thời. X-như-một-dịch-vụ là quan hệ nhà cung cấp/người dùng rõ ràng với một giao diện được định nghĩa tốt, lý tưởng cho việc sử dụng nền tảng ở quy mô lớn. Hỗ trợ là việc một đội giúp đội khác học hỏi, đó là điều các đội hỗ trợ làm. Hãy gọi tên phương thức cho mỗi mối quan hệ quan trọng giữa các đội, và coi sự cộng tác kéo dài giữa cùng hai đội là tín hiệu cho thấy ranh giới của họ đang đặt sai chỗ.

### Chọn mô hình vận hành cho các chức năng xuyên suốt

Bảo mật, dữ liệu, thiết kế và các lĩnh vực tương tự có thể được tổ chức theo ba cách: tập trung (một đội sở hữu cho tất cả), liên kết (các chuyên gia tham gia bán thời gian, điều phối qua một hội nhóm), hoặc nhúng (một chuyên gia chuyên trách trong mỗi đội bám theo dòng giá trị). Tập trung mang lại tính nhất quán và chiều sâu, nhưng trở thành nút thắt cổ chai. Nhúng mang lại tốc độ và ngữ cảnh, nhưng có nguy cơ thiếu nhất quán và trùng lặp. Liên kết (thường là mô hình trục-và-nan hoặc [cộng đồng thực hành](https://en.wikipedia.org/wiki/Community_of_practice)) nằm giữa hai mô hình kia. Hãy chọn theo từng chức năng và từng quy mô. Hầu hết các tổ chức lớn chọn mô hình liên kết cho các lĩnh vực này, cùng với một lõi trung tâm nhỏ đặt ra các tiêu chuẩn.

### Đầu tư vào inner-source

[Inner-source](https://en.wikipedia.org/wiki/Inner_source) đưa các mẫu cộng tác của [mã nguồn mở](https://en.wikipedia.org/wiki/Open-source_software) vào bên trong tổ chức: các kho mã nội bộ dùng chung, hướng dẫn đóng góp được công bố, [đánh giá mã](https://en.wikipedia.org/wiki/Code_review) xuyên ranh giới giữa các đội, và người bảo trì rõ ràng. Khi một đội cần một thay đổi trong thành phần của đội khác, họ có thể trực tiếp đóng góp thay đổi thay vì tạo phiếu yêu cầu và chờ trong hàng đợi. Điều này giải tỏa các phụ thuộc giữa các đội mà không làm tan biến quyền sở hữu, và nó lan truyền kiến thức cùng tiêu chuẩn một cách tự nhiên trong một cộng đồng kỹ sư lớn.

## Đánh đổi: ưu và nhược điểm

| Mô hình cho các chức năng xuyên suốt | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| Tập trung (một đội cho tất cả) | Nhất quán, chuyên môn sâu, tiêu chuẩn rõ ràng | Nút thắt cổ chai, hàng đợi, mất ngữ cảnh sản phẩm |
| Liên kết (trục-và-nan, hội nhóm) | Cân bằng giữa nhất quán và tốc độ; chia sẻ kiến thức | Đòi hỏi kỷ luật điều phối; trách nhiệm có thể mờ nhạt |
| Nhúng (chuyên gia trong mỗi đội) | Nhanh, giàu ngữ cảnh, quyền sở hữu cao | Trùng lặp, thiếu nhất quán, khó bố trí nhân sự ở quy mô lớn |

| Loại đội | Phù hợp nhất cho | Rủi ro nếu lạm dụng |
| --- | --- | --- |
| Bám theo dòng giá trị | Phần lớn việc phân phối sản phẩm và dịch vụ | Không có; loại này nên chiếm ưu thế |
| Nền tảng | Giảm tải nhận thức dùng chung | Trở thành người gác cổng trong tháp ngà |
| Hỗ trợ | Lan truyền một năng lực một cách tạm thời | Biến thành một phụ thuộc vĩnh viễn |
| Hệ thống con phức tạp | Các miền chuyên môn thực sự sâu | Bị dùng làm cái cớ để tích trữ công việc bình thường |

Sự đánh đổi lặp đi lặp lại là tự chủ so với nhất quán. Các đội hoàn toàn tự chủ di chuyển nhanh, nhưng họ trôi xa nhau về tiêu chuẩn, công cụ và tư thế bảo mật. Kiểm soát hoàn toàn tập trung giữ mọi thứ nhất quán, nhưng bóp nghẹt dòng chảy. Thiết kế cấu trúc đội nhóm tốt tìm ra đường nối: tự chủ cho việc phân phối của các đội bám theo dòng giá trị, cộng với các tiêu chuẩn trung tâm mỏng và các nền tảng "con đường trải sẵn" (công cụ mặc định được hỗ trợ tốt, khiến lựa chọn tuân thủ trở nên dễ dàng) cho những thứ thực sự phải nhất quán.

## Câu hỏi để thảo luận với đội của bạn

1. **Những tín hiệu cụ thể nào cho bạn biết tải nhận thức của một đội quá cao, trước khi chất lượng sụp đổ?** "Giới hạn mỗi đội trong một miền họ làm chủ được" thì dễ nói nhưng khó hành động nếu không có bằng chứng, vì tải nhận thức vô hình cho đến khi việc phân phối và độ tin cậy suy giảm. Hãy tìm các triệu chứng đo được: số dịch vụ hoặc kho mã không liên quan mà một đội sở hữu, thời gian hội nhập kéo dài bao lâu, một kỹ sư phải chuyển đổi ngữ cảnh qua bao nhiêu miền trong một tuần, và tỷ lệ sự cố tăng ở các góc thuộc phạm vi của đội. Với một tổ chức lớn, điều này quan trọng vì các đội quá tải âm thầm trở thành nút thắt cổ chai mà không sơ đồ tái tổ chức nào dự đoán được. Hãy mang những con số này vào cuộc thảo luận, cùng với cảm nhận của chính đội về những gì họ có thể và không thể giữ trong đầu. Nếu tín hiệu cho thấy quá tải, hành động cần làm là chuyển phần việc không tạo khác biệt sang một nền tảng hoặc một đội hỗ trợ, không phải đòi hỏi thêm chủ nghĩa anh hùng.

2. **Việc tái tổ chức ở đây có thực sự đáng với sự xáo trộn, hay bạn đang nghiện tái tổ chức?** Vẽ lại ranh giới để áp dụng chiêu thức Conway nghịch đảo là mạnh mẽ, và mỗi lần tái tổ chức cũng phá hủy sự ổn định mà các đội cần để gắn kết, đồng thời đặt lại kiến thức miền khó khăn mới có được. Những cân nhắc đối lập là cái thuế điều phối liên tục của cấu trúc hiện tại so với chi phí một lần và cú đánh vào tinh thần của việc thay đổi nó. Trong bối cảnh doanh nghiệp và chính phủ, ranh giới mua sắm, các đội nhà thầu và sự phân tách nhiệm vụ bắt buộc làm việc tái tổ chức chậm hơn và đắt hơn, nên ngưỡng phải cao hơn. Hãy mang bằng chứng về sự chậm trễ do phụ thuộc: có bao nhiêu sáng kiến bị chặn chờ một đội khác, và trong bao lâu. Hãy tái tổ chức khi việc chờ đợi đó mang tính cấu trúc và lớn, và hãy cưỡng lại việc xáo trộn khi nỗi đau chỉ là tạm thời hoặc sẽ rẻ hơn nếu giải quyết bằng các đóng góp inner-source và giao diện rõ ràng hơn.

3. **Với bảo mật, dữ liệu và thiết kế, sự kiện nào sẽ kích hoạt việc bạn chuyển giữa mô hình nhúng, liên kết và tập trung?** Khuyến nghị của chương này là chọn theo từng chức năng và từng quy mô, và kỷ luật khó hơn là quyết định trước sự tăng trưởng hay rủi ro nào sẽ khiến bạn xem xét lại lựa chọn đó. Một mô hình phù hợp với năm mươi kỹ sư có thể trở thành nút thắt cổ chai hoặc thảm họa về nhất quán ở năm trăm kỹ sư, và các doanh nghiệp cùng cơ quan chính phủ đặc biệt cần gọi tên những tiêu chuẩn mà một lõi trung tâm nhỏ sẽ luôn nắm giữ. Hãy mang thời gian hàng đợi hiện tại và các khoảng trống về nhất quán của từng chức năng: một đội bảo mật tập trung với hàng đợi rà soát kéo dài nhiều tuần là tín hiệu để liên kết, còn các chuyên gia nhúng tạo ra mô hình dữ liệu không tương thích là tín hiệu để thêm một lõi tiêu chuẩn trung tâm. Hãy quyết định trước ngưỡng kích hoạt, chẳng hạn một ngưỡng độ dài hàng đợi hoặc một phát hiện kiểm toán, để thay đổi trở thành một sự tiến hóa có kế hoạch thay vì phản ứng khủng hoảng. Câu trả lời xác định nơi bạn đầu tư vào các con đường trải sẵn và những người tiên phong so với một trung tâm.

4. **Làm thế nào bạn biết đội nền tảng của mình thực sự đang giảm tải nhận thức hay âm thầm trở thành người gác cổng?** Một nền tảng tồn tại để biến lựa chọn tuân thủ và đáng tin cậy thành lựa chọn dễ dàng thông qua tự phục vụ, và chính đội đó có thể trượt sang việc bắt buộc công cụ, tự tay rà soát mọi yêu cầu và thêm vào chính những ma sát mà nó được lập ra để loại bỏ. Với một tổ chức lớn, sự phân biệt này quyết định việc đầu tư nền tảng có hoàn vốn hay biến thành nút thắt cổ chai trung tâm mà mọi đội bám theo dòng giá trị phải xếp hàng chờ. Những cân nhắc đối lập là nhất quán và kiểm soát ở một bên, so với quyền tự chủ của người dùng và dòng chảy ở bên kia. Hãy mang bằng chứng mà một người dùng sẽ nhận ra: mất bao lâu để một đội bám theo dòng giá trị tự phục vụ một môi trường hoặc đường ống mới mà không phải tạo phiếu yêu cầu, tỷ lệ giữa các hành động tự phục vụ và các hành động có người xử lý, và mức chấp nhận nền tảng đo bằng số đội tự chọn nó thay vì số đội bị ép dùng. Trong bối cảnh doanh nghiệp và chính phủ, hãy khăng khăng rằng nền tảng tự động tạo ra bằng chứng kiểm toán và tuân thủ thay vì qua các cổng thủ công, vì một nền tảng đáp ứng quy tắc phân tách nhiệm vụ bằng cách chèn thêm một người rà soát đã tái tạo chính nút thắt cổ chai mà nó được tài trợ để hóa giải.

5. **Những mối quan hệ nào giữa các đội của bạn đã chuyển thành cộng tác vĩnh viễn, và điều gì sẽ biến từng mối thành một giao diện dịch vụ rõ ràng hoặc một ranh giới được vẽ lại?** Phương thức cộng tác được dự kiến là cường độ cao và tạm thời, và một cặp làm việc chung không bao giờ kết thúc thường là tín hiệu cho thấy quyền sở hữu nằm sai chỗ hoặc giao diện giữa hai đội chưa bao giờ được làm rõ. Điều này quan trọng ở quy mô lớn vì sự cộng tác thường trực, không được gọi tên chính là nơi chi phí điều phối ẩn náu: nó không xuất hiện trên bất kỳ sơ đồ tổ chức nào, nhưng đánh thuế mọi thay đổi mà hai đội đụng đến. Những cân nhắc đối lập là giá trị khám phá của việc ở gần nhau so với dòng chảy bạn thu được khi biến mối quan hệ thành hợp đồng X-như-một-dịch-vụ với giao diện xác định, hoặc khi gộp trách nhiệm vào một đội duy nhất. Hãy mang danh sách các cặp đội đã cộng tác liên tục hơn một quý, những thay đổi đòi hỏi cả hai đội trong vài tháng gần đây, và liệu có thể viết ra một giao diện ổn định giữa họ hay không. Trong bối cảnh doanh nghiệp và chính phủ, nơi ranh giới nhà thầu và các gói thầu có thể đóng băng một điểm bàn giao trong nhiều năm, hãy gọi tên những mối quan hệ nào bạn có thể chuyển đổi bằng giao diện và đóng góp inner-source và những mối nào bị cố định theo hợp đồng và phải được quản lý như các phụ thuộc tường minh.

6. **Khi một đội hỗ trợ giúp đội khác xây dựng một năng lực, làm thế nào bạn biết nó đã thành công và có thể lùi lại thay vì trở thành một phụ thuộc vĩnh viễn?** Các đội hỗ trợ được dự kiến huấn luyện một đội bám theo dòng giá trị làm chủ kiểm thử, bảo mật hay khả năng quan sát rồi đi tiếp, và nếu không có điều kiện thoát rõ ràng, mối quan hệ huấn luyện sẽ cứng lại thành một dịch vụ thường trực mà đội bám theo dòng giá trị không bao giờ thực sự tiếp thu. Với một tổ chức lớn, đây là sự khác biệt giữa việc lan truyền một năng lực qua hàng chục đội và việc tạo ra một nút thắt cổ chai dùng chung mới ngày càng kém mở rộng theo từng năm. Những cân nhắc đối lập là chiều sâu và tính nhất quán mà một đội chuyên gia mang lại so với quyền tự chủ và sở hữu từ đầu đến cuối mà bạn đang cố xây dựng vào các đội bám theo dòng giá trị. Hãy mang bằng chứng về chuyển giao năng lực: liệu đội tiếp nhận hiện có xử lý được công việc mà không cần đội hỗ trợ có mặt hay không, nhóm hỗ trợ cố định cam kết với bao nhiêu đội cùng lúc, và mỗi đợt hỗ trợ đã kéo dài quá thời điểm bàn giao dự kiến bao lâu. Trong bối cảnh doanh nghiệp và chính phủ, nơi một kỹ năng chuyên gia khan hiếm có thể nằm sau một đội trung tâm duy nhất hoặc một hợp đồng duy nhất, hãy quyết định trước cách bạn tài trợ cho việc chuyển giao năng lực và những người tiên phong, để chuyên môn lan vào các đội phân phối thay vì bị khóa sau một hàng đợi mà mọi kiểm toán và bản phát hành đều phải chờ.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và nguồn vốn eo hẹp, cấu trúc đúng là một đội bám theo dòng giá trị duy nhất sở hữu toàn bộ sản phẩm, và kỷ luật là từ chối tạo ra các ô riêng biệt trước khi bạn cần. Hãy cưỡng lại việc thuê một người "DevOps" hay "QA" đơn lẻ trở thành cổng kiểm soát; hãy đưa các kỹ năng đó vào đội duy nhất như một năng lực nhúng. Giữ cho Định luật Conway làm việc có lợi cho bạn bằng cách giữ tổ chức phẳng, để kiến trúc luôn đơn giản và dễ thay đổi như đội.

**Doanh nghiệp nhỏ.** Bạn sẽ không bố trí một đội nền tảng hay đội hỗ trợ chuyên trách, vì vậy hãy mua nền tảng: dùng các dịch vụ đám mây được quản lý, các đường ống được lưu trữ và công cụ bảo mật có sẵn để gỡ tải nhận thức không tạo khác biệt khỏi một hoặc hai đội của bạn. Hãy coi các mối quan tâm xuyên suốt như bảo mật và dữ liệu là thứ bạn cấu hình và sử dụng thay vì một chức năng bạn xây dựng. Chỉ giữ quyền sở hữu riêng cho một hệ thống con phức tạp thực sự tạo khác biệt cho bạn, và để các nhà cung cấp gánh phần còn lại.

**Doanh nghiệp lớn.** Ở quy mô lớn, vấn đề là chi phí điều phối giữa nhiều đội, vì vậy hãy biến cấu trúc đội nhóm thành một thiết kế tường minh, được quản trị: một phân loại chung về bốn loại đội, các phương thức tương tác được đặt tên, một nền tảng con đường trải sẵn và inner-source để giảm hàng đợi giữa các đội. Hãy theo dõi sự chậm trễ do phụ thuộc và tải nhận thức của đội như các chỉ số danh mục, và thực hiện tái tổ chức như những tiến hóa có chủ đích với ngưỡng cao thay vì phản xạ hằng năm. Một lõi trung tâm mỏng nắm giữ các tiêu chuẩn phải nhất quán, trong khi các đội bám theo dòng giá trị giữ quyền tự chủ về phân phối.

**Chính phủ.** Quy tắc mua sắm, ranh giới nhà thầu và sự phân tách nhiệm vụ bắt buộc làm phân mảnh quyền sở hữu, vì vậy hãy thiết kế cấu trúc đội nhóm để đáp ứng các ràng buộc đó thông qua công cụ và giao diện rõ ràng thay vì bàn giao giữa người với người. Ưu tiên các mô hình liên kết với một lõi tiêu chuẩn nhỏ và một nền tảng tự động tạo bằng chứng kiểm toán và tuân thủ, để sự phân tách nhiệm vụ được thực thi bởi các đường ống thay vì hàng đợi rà soát. Hãy ghi lại công khai ranh giới các đội, phương thức tương tác và mô hình vận hành, để cấu trúc minh bạch với kiểm toán viên, cơ quan giám sát và công chúng, những người tài trợ cho nó.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười người có một đội bám theo dòng giá trị duy nhất sở hữu toàn bộ sản phẩm từ đầu đến cuối, điều này hoàn toàn đúng ở quy mô của họ: không bàn giao, không thuế điều phối, mọi người chia sẻ cùng ngữ cảnh. Rắc rối bắt đầu khi họ thuê một "người DevOps" chuyên trách và một "người QA" riêng, vô tình tái tạo các ô chức năng, khiến mỗi bản phát hành giờ phải chờ hai cá nhân. Họ điều chỉnh bằng cách coi những vị trí này là năng lực nền tảng và kiểm thử nhúng trong đội duy nhất, thay vì các cổng mà công việc phải đi qua. Ở quy mô này, cấu trúc rẻ nhất là cấu trúc giữ mọi người trong một dòng chảy duy nhất.

**Doanh nghiệp lớn.** Quy trình thanh toán của một nhà bán lẻ lớn thay đổi chậm vì logic giao diện, máy chủ và hoàn tất đơn hàng bị chia cho ba đội tổ chức theo chức năng, buộc mọi thay đổi đi qua ba danh sách việc tồn đọng. Áp dụng chiêu thức Conway nghịch đảo, họ tái tổ chức thành các đội bám theo dòng giá trị quanh các hành trình khách hàng ("duyệt xem", "giỏ hàng và thanh toán", "sau mua hàng"), mỗi đội sở hữu lát cắt của mình từ đầu đến cuối, được hỗ trợ bởi một đội nền tảng cung cấp triển khai và khả năng quan sát như một dịch vụ. Những thay đổi thanh toán từng mất một quý nay được phát hành trong vài ngày, vì sự điều phối từng trải dài qua nhiều đội nay diễn ra bên trong một đội.

**Chính phủ.** Một cơ quan thuế của chính phủ vận hành một đội bảo mật trung tâm rà soát mọi bản phát hành, tạo ra hàng đợi kéo dài nhiều tuần làm chậm các bản vá quan trọng. Họ chuyển sang mô hình liên kết: một chức năng bảo mật trung tâm nhỏ đặt tiêu chuẩn và cung cấp một "con đường trải sẵn" gồm các đường ống đã được phê duyệt trước và quét tự động, trong khi những người tiên phong về bảo mật tham gia bán thời gian trong mỗi đội phân phối xử lý các quyết định hằng ngày. Nền tảng tự động tạo bằng chứng tuân thủ. Các yêu cầu phân tách nhiệm vụ bắt buộc vẫn được đáp ứng, nhưng thông qua công cụ và giao diện rõ ràng thay vì một nút thắt do con người, giúp rút ngắn đáng kể thời gian dẫn phát hành đồng thời cải thiện mức sẵn sàng kiểm toán.

## Luận chứng kinh doanh: động lực, ROI và TCO

Bạn trả giá cho thiết kế đội nhóm kém bằng chi phí điều phối, và chi phí đó tăng nhanh hơn tuyến tính theo số đội phải đồng bộ cho một thay đổi điển hình. Mỗi lần bàn giao là một hàng đợi với thời gian chờ, một lần chuyển ngữ cảnh làm mất thông tin, và một cơ hội mới để hiểu lầm. Khi một thay đổi thường lệ cần ba đội căn chỉnh lộ trình của họ, chi phí thực sự không phải là tổng công việc của họ; mà là chi phí lớn hơn nhiều của việc lên lịch, chờ đợi và làm lại. Hãy vẽ lại ranh giới để hầu hết thay đổi nằm gọn trong quyền sở hữu của một đội, và chi phí đó đơn giản biến mất.

Chi phí áp dụng là có thật. Tái tổ chức gây xáo trộn, và xây dựng nền tảng cùng thực hành inner-source cần đầu tư ban đầu trước khi lợi ích đến. Nhưng chi phí của việc không áp dụng thì cộng dồn. Các tổ chức để cấu trúc tích tụ ngẫu nhiên sẽ chất đống các chuỗi bàn giao, các đội nút thắt dùng chung với hàng đợi dài cả quý, và các kiến trúc hóa đá bởi sơ đồ tổ chức. Để thuyết phục ban lãnh đạo, hãy đo sự chậm trễ do phụ thuộc: có bao nhiêu sáng kiến đang hoạt động bị chặn chờ một đội khác, và trong bao lâu. Đầu tư vào nền tảng và cấu trúc đội nhóm thường hoàn vốn bằng cách biến thời gian chờ thành dòng chảy, thể hiện ở thời gian dẫn ngắn hơn và thông lượng cao hơn mà không cần thêm biên chế.

## Phản mẫu và cạm bẫy

- Phớt lờ Định luật Conway: thiết kế một kiến trúc mà cấu trúc tổ chức không thể phân phối.
- Các ô chức năng: các đội giao diện, máy chủ, QA và vận hành riêng rẽ phải phối hợp cho mọi thay đổi.
- Nút thắt dịch vụ dùng chung: một đội trung tâm mà mọi dự án phải xếp hàng chờ.
- Nền tảng như người gác cổng: một đội nền tảng áp đặt thay vì phục vụ, thêm ma sát thay vì loại bỏ nó.
- Quá tải nhận thức: các đội sở hữu những hệ thống rộng lớn, không liên quan mà họ không thể làm chủ.
- "Cộng tác" vĩnh viễn: hai đội vướng víu vào nhau mãi mãi, báo hiệu một ranh giới đặt sai chỗ.
- Nghiện tái tổ chức: xáo trộn liên tục, phá hủy sự ổn định mà các đội cần để gắn kết.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu.** Các đội hình thành ngẫu nhiên, theo biên chế hoặc theo hệ thống phân cấp cũ; không ai gọi tên loại đội hay phương thức tương tác; các ô chức năng và nút thắt dịch vụ dùng chung ở khắp nơi và các phụ thuộc bị ẩn cho đến khi chúng chặn một bản phát hành.
- **Mức 2, Phát triển.** Một số đội bám theo dòng giá trị tồn tại và xuất hiện nỗ lực nền tảng hoặc inner-source đầu tiên, nhưng mẫu hình được áp dụng không đồng đều: một vài đội sở hữu lát cắt của mình từ đầu đến cuối trong khi những đội khác vẫn xếp hàng sau các chức năng trung tâm, và tải nhận thức được bàn luận theo giai thoại thay vì được quản lý.
- **Mức 3, Chuẩn hóa.** Bốn loại đội và ba phương thức tương tác được lập thành tài liệu và sử dụng có chủ đích trong toàn tổ chức; nền tảng và inner-source giải tỏa các phụ thuộc giữa các đội; một mô hình vận hành cho bảo mật, dữ liệu và thiết kế được chọn và ghi lại, và các đội mới được hình thành theo các tiêu chuẩn này thay vì ứng biến.
- **Mức 4, Quản lý.** Cấu trúc đội nhóm được đo lường và kiểm soát theo các đường cơ sở: các đội theo dõi tải nhận thức, sự chậm trễ do phụ thuộc (các sáng kiến bị chặn chờ một đội khác, và trong bao lâu), tỷ lệ tự phục vụ và mức chấp nhận nền tảng, thời lượng của phương thức tương tác, và các chỉ số dòng chảy phân phối như thời gian dẫn và tần suất thay đổi. Các ngưỡng kích hoạt hành động, ví dụ một độ dài hàng đợi buộc một chức năng phải liên kết hoặc một sự cộng tác thường trực báo hiệu ranh giới đặt sai, để các quyết định dựa trên bằng chứng thay vì ý kiến.
- **Mức 5, Điều phối.** Thiết kế đội nhóm được cải tiến liên tục và tích hợp với kế hoạch kiến trúc, sản phẩm và rủi ro; tổ chức định hình lại ranh giới khi hệ thống và hoạt động kinh doanh phát triển, kết thúc các đợt hỗ trợ khi năng lực đã được chuyển giao, và cân bằng lại đầu tư nền tảng khi tải nhận thức thay đổi, giữ dòng chảy nhanh như một thuộc tính thích ứng, thường trực thay vì một lần tái tổ chức duy nhất.

## Ý tưởng để thảo luận

- Với một thay đổi điển hình, bao nhiêu đội phải phối hợp, và vì sao?
- Đội nào của chúng ta đang gánh quá nhiều tải nhận thức, và một nền tảng có thể gỡ bớt những gì?
- Chúng ta đang chống lại Định luật Conway ở đâu thay vì vẽ lại ranh giới?
- Các đội nền tảng của chúng ta đang phục vụ hay canh cổng các đội bám theo dòng giá trị?
- Bảo mật, dữ liệu và thiết kế nên tập trung, liên kết hay nhúng đối với chúng ta ngay lúc này?
- Những sự cộng tác "tạm thời" nào đã âm thầm trở thành phụ thuộc vĩnh viễn?

## Những điểm cần ghi nhớ

- Cấu trúc tổ chức quyết định kiến trúc và tốc độ phân phối; hãy thiết kế nó một cách có chủ đích.
- Dùng bốn loại đội, với đội bám theo dòng giá trị là mặc định và các loại còn lại để hỗ trợ.
- Áp dụng chiêu thức Conway nghịch đảo để biến kiến trúc mong muốn thành con đường dễ đi.
- Quản lý tải nhận thức; giới hạn mỗi đội trong một miền họ làm chủ được.
- Giới hạn và đặt tên các phương thức tương tác giữa các đội; coi các phụ thuộc kéo dài là lỗi ranh giới.
- Chọn mô hình tập trung, liên kết hoặc nhúng cho các chức năng xuyên suốt theo quy mô, và dùng InnerSource để giải tỏa hàng đợi.

## Tài liệu tham khảo và đọc thêm

- Matthew Skelton và Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (nguồn gốc của Định luật Conway)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (về việc căn chỉnh dịch vụ theo đội)
- Danese Cooper và Klaas-Jan Stol, "Adopting InnerSource", và các mẫu của InnerSource Commons
- Frederick Brooks, "The Mythical Man-Month" (chi phí giao tiếp)
