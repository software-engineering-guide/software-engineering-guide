# 2.1 Tiêu chuẩn và phong cách viết mã

## Tổng quan và động lực

Tiêu chuẩn viết mã là những quy ước chung cho phép nhiều người viết mã như thể một tác giả cẩn thận đã viết nó. Chúng bao quát đặt tên, định dạng, bố cục tệp, thành ngữ, xử lý lỗi và các mô hình lập trình mà một đội ưa chuộng. Với một đội nhỏ, sở thích cá nhân có thể quyết định mọi thứ. Với một đội lớn (hàng trăm hoặc hàng nghìn kỹ sư, nhiều nhà thầu, tỷ lệ luân chuyển cao), sự thiếu nhất quán trở thành một khoản thuế bạn trả trong mỗi lần đọc, mỗi lần đánh giá và mỗi lần hội nhập. Tiêu chuẩn biến vô số cuộc tranh cãi nhỏ về phong cách thành một quyết định một lần mà sau đó máy móc thực thi giúp bạn.

Với các tổ chức lớn, rủi ro là cụ thể. Mã được đọc nhiều hơn rất nhiều lần so với được viết. Trong bối cảnh doanh nghiệp và chính phủ, một dòng mã có thể được kiểm toán viên, người rà soát bảo mật và người bảo trì đọc nhiều năm sau khi tác giả của nó đã rời đi. Phong cách nhất quán giảm chi phí tinh thần của việc đọc đó, thu hẹp bề mặt cho lỗi, và làm cho phân tích tự động đáng tin cậy trên các [linter](https://en.wikipedia.org/wiki/Lint_(software)) (công cụ tự động đánh dấu các lỗi có khả năng xảy ra và vi phạm phong cách), trình quét bảo mật và công cụ [tái cấu trúc](https://en.wikipedia.org/wiki/Code_refactoring). Nơi có quy định áp dụng, như trong dịch vụ tài chính, chăm sóc sức khỏe, quốc phòng và hệ thống khu vực công, tiêu chuẩn cũng là một phần của bằng chứng rằng một cơ sở mã bảo trì được và được kiểm soát.

Cách tiếp cận hiện đại là coi phong cách như một mối quan tâm đã được giải quyết, tự động hóa thay vì vấn đề phán đoán liên tục của con người. Các công cụ định dạng và linter chạy trong trình soạn thảo, trong các hook trước commit và trong [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI), quy trình dựng-và-kiểm-thử tự động chạy trên mọi thay đổi. Máy móc thực thi phong cách, để bạn có thể dành sự chú ý đánh giá cho thiết kế và tính đúng đắn. Mục tiêu không phải sự đồng nhất vì chính nó. Đó là loại bỏ ma sát: bạn nên có thể di chuyển giữa các dịch vụ và đội mà không phải học lại những điều cơ bản.

## Các nguyên tắc chính

- Nhất quán thắng sở thích cá nhân; một phong cách thống nhất duy nhất, áp dụng ở mọi nơi, có giá trị hơn phong cách "tốt nhất" áp dụng không đồng đều.
- Tự động hóa việc thực thi. Công cụ định dạng và linter là nguồn sự thật, không phải các bình luận đánh giá mã về khoảng trắng.
- Tối ưu hóa cho người đọc và người bảo trì, không phải tác giả ban đầu.
- Ưu tiên các quy ước mà cộng đồng ngôn ngữ rộng hơn đã dùng thay vì các quy tắc riêng của công ty.
- Làm cho tiêu chuẩn dễ áp dụng: cung cấp cấu hình dùng chung, biểu mẫu và công cụ thay vì một tệp PDF không ai đọc.
- Các quy tắc phong cách nên ít, có thể bảo vệ và không mơ hồ; mỗi quy tắc có một cơ chế thực thi hoặc nó chỉ là một gợi ý.
- Đặt tên là quyết định về khả năng đọc có đòn bẩy cao nhất và xứng đáng có hướng dẫn tường minh.

## Khuyến nghị

### Áp dụng một hướng dẫn phong cách chuẩn cho mỗi ngôn ngữ

Với mỗi ngôn ngữ bạn dùng, hãy áp dụng một hướng dẫn phong cách được công nhận rộng rãi làm đường cơ sở (ví dụ, hướng dẫn của cộng đồng hoặc nhà cung cấp cho ngôn ngữ đó) và chỉ lập tài liệu cho những khác biệt mà tổ chức của bạn cần. Đừng phát minh một phong cách riêng từ đầu. Hãy công bố lựa chọn của bạn ở một nơi trung tâm, dễ tìm, và đánh phiên bản nó như mã.

### Biến công cụ định dạng thành mặc định không thể thương lượng

Dùng một công cụ định dạng tự động có chính kiến cho mọi ngôn ngữ có nó, với một cấu hình chung duy nhất được commit vào kho mã. Định dạng không bao giờ nên xuất hiện trong đánh giá, vì nó được áp dụng tự động khi lưu và được xác minh trong CI. Ở nơi một ngôn ngữ thiếu công cụ định dạng mạnh, hãy chọn một cấu hình linter và đối xử với nó theo cách tương tự.

### Chạy linter như các cổng bắt buộc, không phải lời khuyên

Cấu hình linter với một bộ quy tắc đã thống nhất, làm hỏng bản dựng khi có vi phạm, và giữ bộ quy tắc trong [hệ thống quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control) để các thay đổi đi qua đánh giá. Tách các quy tắc có thể tự sửa (áp dụng chúng tự động) khỏi các quy tắc cần phán đoán của con người (đánh dấu và chặn). Đưa các quy tắc mới vào ở chế độ "cảnh báo", dọn dẹp phần tồn đọng, rồi nâng chúng lên "lỗi".

### Thực thi ở nhiều tầng

Cung cấp tích hợp trình soạn thảo để có phản hồi tức thì, hook trước commit để thực thi cục bộ, và kiểm tra CI làm cổng có thẩm quyền. Bạn bắt một vi phạm càng sớm thì chi phí càng rẻ. CI phải là chốt chặn cuối cùng, vì các hook cục bộ có thể bị bỏ qua.

### Đặt quy tắc tường minh cho việc đặt tên

Chuẩn hóa quy ước viết hoa theo từng ngôn ngữ, yêu cầu các tên tiết lộ ý định, cấm các từ viết tắt gây hiểu lầm, và xác định quy ước cho giá trị luận lý, tập hợp, đơn vị và các thao tác bất đồng bộ. Hãy viết từ vựng miền nghiệp vụ của bạn vào một bảng thuật ngữ chung để cùng một khái niệm có cùng một tên ở mọi nơi.

### Quản lý tính nhất quán đa ngôn ngữ một cách có chủ đích

Trong một cơ sở mã trải qua nhiều ngôn ngữ, hãy hướng đến các khái niệm nhất quán (mẫu xử lý lỗi, cấu trúc ghi nhật ký, bố cục dự án) ngay cả khi cú pháp khác nhau. Cung cấp cấu hình theo từng ngôn ngữ từ một kho trung tâm để một dịch vụ mới tự thừa hưởng các tiêu chuẩn thông qua biểu mẫu hoặc khung dựng sẵn.

### Hệ thống hóa thành ngữ và mô hình lập trình

Đi xa hơn định dạng. Hãy viết ra các thành ngữ ưa thích của bạn, chẳng hạn cách xử lý lỗi, cách cấu trúc mô-đun, và khi nào dùng ngoại lệ so với kiểu kết quả, cùng với các mô hình lập trình mà đội của bạn ưa chuộng. Đây là nơi khả năng đọc và khả năng bảo trì thực sự nằm.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Công cụ định dạng tự động nghiêm ngặt, không cấu hình | Chấm dứt mọi tranh cãi về định dạng; nhất quán tức thì; hội nhập đơn giản | Một số lựa chọn không thích là không thể thương lượng; diff ban đầu lớn khi áp dụng lần đầu |
| Linter có thể cấu hình với quy tắc riêng | Phù hợp nhu cầu tổ chức; có thể mã hóa các quy tắc ngăn lỗi thực sự | Cấu hình trôi dạt; tranh cãi vặt về quy tắc; gánh nặng bảo trì |
| Áp dụng nguyên tiêu chuẩn cộng đồng | Quen thuộc với nhân viên mới; hệ sinh thái công cụ mạnh; ít bảo trì | Có thể không phù hợp ràng buộc đặc thù của tổ chức; thỉnh thoảng có quy tắc vụng về |
| Tiêu chuẩn nội bộ riêng | Phù hợp chính xác với tổ chức | Tốn kém để viết và bảo trì; lạ với nhân viên mới; công cụ yếu |
| Tự chủ theo từng đội | Tinh thần địa phương cao; phù hợp ngữ cảnh | Phân mảnh; di chuyển giữa các đội đau đớn; công cụ không nhất quán |

Các mặc định được thực thi đánh đổi một chút tự chủ cá nhân lấy lợi ích tập thể lớn: ít ma sát đánh giá hơn, hội nhập nhanh hơn và tự động hóa đáng tin cậy. Rủi ro chính là thiết kế quá mức tiêu chuẩn thành hàng trăm quy tắc làm chậm mọi người mà không ngăn được lỗi thực sự. Hãy giữ bộ quy tắc nhỏ và dựa trên bằng chứng, và nghiêng về việc áp dụng một tiêu chuẩn có sẵn để việc bảo trì luôn rẻ.

## Câu hỏi để thảo luận với đội của bạn

1. **Quy tắc linter nào nên làm hỏng bản dựng, và làm thế nào bạn nâng một quy tắc từ cảnh báo lên lỗi mà không làm mọi người dừng lại?** Chương này lập luận rằng mọi quy tắc cần một cơ chế thực thi, và rằng các quy tắc mới nên vào ở chế độ cảnh báo, dọn xong phần tồn đọng, rồi chuyển sang lỗi. Với một đội lớn, chuyển một quy tắc sang lỗi trên một cơ sở mã bẩn sẽ chặn hàng trăm thay đổi không liên quan qua một đêm. Hãy mang bằng chứng cứng đến cuộc họp: số lượng vi phạm hiện tại cho mỗi quy tắc ứng viên, và liệu nó có thể tự sửa hay cần phán đoán của con người. Trong bối cảnh doanh nghiệp và chính phủ, ranh giới đạt/trượt cũng nuôi các cổng kiểm toán, nên một bộ quy tắc mơ hồ làm yếu câu chuyện tuân thủ của bạn. Hãy quyết định một lộ trình triển khai theo giai đoạn: tự sửa những gì có thể, ngân sách cho việc dọn dẹp, rồi mới đặt cổng.

2. **Khi bạn áp dụng công cụ định dạng lần đầu lên mã cũ, bạn sẽ giữ cho lần định dạng lại đó không phá hỏng git blame và không nhấn chìm các đánh giá như thế nào?** Bảng đánh đổi cảnh báo về diff ban đầu lớn, và phần phản mẫu nêu việc trộn các commit định dạng lại với các thay đổi logic. Một lần định dạng lại quét toàn bộ viết lại hàng nghìn dòng và khiến blame chỉ vào lần định dạng lại thay vì tác giả thực sự, điều gây hại cho bất kỳ ai gỡ lỗi nhiều năm sau. Hãy thực hiện việc định dạng lại như một commit cô lập, được gắn nhãn rõ ràng, và đăng ký nó trong một tệp bỏ qua blame để lịch sử vẫn hữu ích. Với kiểm toán viên lần theo ai đã thay đổi gì, sự cô lập đó là khác biệt giữa bằng chứng sạch và nhiễu. Hãy thống nhất trình tự trước khi chạm vào mã, không phải sau.

3. **Ai sở hữu bảng thuật ngữ đặt tên và từ vựng miền nghiệp vụ của bạn, và một thuật ngữ mới được thêm vào như thế nào?** Chương này gọi việc đặt tên là quyết định về khả năng đọc có đòn bẩy cao nhất và yêu cầu bạn viết từ vựng miền nghiệp vụ vào một bảng thuật ngữ chung. Không có chủ sở hữu được nêu tên, cùng một khái niệm có ba tên khác nhau giữa các đội, và các công cụ phân tích tĩnh và tìm kiếm mất độ tin cậy. Hãy mang các ví dụ về khái niệm đã có tên mâu thuẫn trong cơ sở mã của bạn làm tín hiệu cụ thể. Giao cho một chủ sở hữu duy nhất và một con đường đề xuất nhẹ, để thêm hoặc đổi tên một thuật ngữ là một thay đổi nhỏ, được đánh giá thay vì một cuộc tranh cãi trong mọi pull request. Câu trả lời thay đổi việc hội nhập: nhân viên mới đọc một bảng thuật ngữ thay vì dịch ngược ý định từ mã không nhất quán.

4. **Với mỗi ngôn ngữ, bạn có áp dụng nguyên một hướng dẫn phong cách được công nhận của cộng đồng hay nhà cung cấp không, và những khác biệt riêng thực sự được biện minh ở đâu?** Chương này lập luận bạn nên lấy một tiêu chuẩn có sẵn làm đường cơ sở và chỉ lập tài liệu những khác biệt mà tổ chức của bạn cần, vì một tiêu chuẩn riêng tốn kém để viết và lạ với nhân viên mới. Lực kéo đối lập là có thật: một ràng buộc nội bộ (quy tắc bảo mật, khung phát triển cũ, yêu cầu về khả năng tiếp cận) đôi khi thực sự xung đột với mặc định cộng đồng, và mỗi khác biệt bạn giữ là một quy tắc mà giờ bạn sở hữu và bảo trì mãi mãi. Hãy mang danh sách khác biệt đề xuất đến cuộc họp, mỗi khác biệt kèm ràng buộc cụ thể thúc đẩy nó, và sẵn sàng cắt bất kỳ khác biệt nào chỉ là sở thích. Trong bối cảnh doanh nghiệp và chính phủ, một đường cơ sở khớp với cộng đồng ngôn ngữ rộng hơn cũng có nghĩa là nhà thầu và nhà cung cấp mới đến đã sẵn thông thạo, rút ngắn hội nhập và củng cố bằng chứng về khả năng bảo trì mà kiểm toán viên tìm kiếm.

5. **Trong một cơ sở mã đa ngôn ngữ, những quy ước nào thực sự phổ quát và những quy ước nào ở lại cục bộ theo ngôn ngữ, và làm thế nào bạn ngăn cấu hình của từng kho mã trôi dạt?** Chương này yêu cầu các khái niệm nhất quán (xử lý lỗi, cấu trúc ghi nhật ký, bố cục dự án) qua các ngôn ngữ ngay cả khi cú pháp khác nhau, và yêu cầu cấu hình theo từng ngôn ngữ được cung cấp từ một kho trung tâm để các dịch vụ mới tự thừa hưởng tiêu chuẩn. Căng thẳng là việc ép thành ngữ của ngôn ngữ này lên ngôn ngữ khác tạo ra mã vụng về, không đúng thành ngữ, trong khi để mỗi đội tự rẽ nhánh cấu hình của mình kết thúc bằng việc "tiêu chuẩn" chẳng có nghĩa gì. Hãy mang bản kiểm kê các cấu hình linter và công cụ định dạng theo từng kho mã hiện tại cùng một bản so sánh cho thấy chúng đã trôi dạt xa nhau đến đâu làm tín hiệu cụ thể. Với một tổ chức lớn chạy hàng chục dịch vụ, hãy quyết định cơ chế phân phối (biểu mẫu, khung dựng sẵn, một gói cấu hình dùng chung) để một thay đổi quy tắc lan truyền một lần thay vì bị sao chép tay vào từng kho mã.

6. **Khi nào việc tắt một quy tắc là chính đáng, ai rà soát việc ngăn chặn, và làm thế nào bạn giữ cho việc tắt hàng loạt không làm rỗng tiêu chuẩn?** Phần phản mẫu đánh dấu việc ngăn chặn nội tuyến lan rộng là dấu hiệu của một quy tắc sai hoặc một đội đã bỏ cuộc, nhưng một chính sách cứng nhắc không ngoại lệ đẩy mọi người viết mã tệ hơn chỉ để thỏa mãn linter. Hãy thống nhất một con đường nhẹ: một sự ngăn chặn phải kèm lý do, nằm ở phạm vi hẹp nhất có thể, và hiển thị trong đánh giá thay vì bị chôn trong một tệp bỏ qua toàn cục. Hãy mang số lượng ngăn chặn hiện tại theo từng quy tắc và từng kho mã, vì một quy tắc bị ngăn chặn hàng trăm lần đang nói với bạn điều gì đó về quy tắc, không phải về mã. Trong công việc chịu quy định và khu vực công, các sự ngăn chặn hàng loạt không có giải thích làm yếu trực tiếp câu chuyện kiểm toán, vì đường ống không còn có thể cho thấy mã được hợp nhất thực sự đã vượt qua các cổng đã thống nhất.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ thắng, vì vậy hãy áp dụng các mặc định công cụ định dạng và linter của cộng đồng cho một ngôn ngữ duy nhất của bạn ngay từ ngày đầu và nối chúng vào hook trước commit và CI trước khi kỹ sư thứ hai đến. Đừng viết một phong cách riêng mà bạn không có thời gian bảo trì: cấu hình được gửi trong kho mã chính là toàn bộ tiêu chuẩn. Khi bạn thêm ngôn ngữ thứ hai, hãy với tới hướng dẫn chuẩn của ngôn ngữ đó thay vì phát minh quy ước từ đầu.

**Doanh nghiệp nhỏ.** Không có chuyên gia công cụ riêng và ngân sách eo hẹp, hãy hoàn toàn dựa vào công cụ định dạng có chính kiến miễn phí đi kèm hoặc cùng với ngôn ngữ của bạn, và chấp nhận mặc định của nó thay vì tinh chỉnh. Đây là trường hợp rõ ràng nên mua hơn xây: duy trì một bộ quy tắc riêng tốn thời gian bạn không có, trong khi một công cụ định dạng có sẵn không tốn gì và chấm dứt tranh cãi về phong cách ngay lập tức. Giữ cấu hình trong kho mã để nhà thầu duy nhất bạn thuê năm sau thừa hưởng nó mà không cần một cuộc trò chuyện.

**Doanh nghiệp lớn.** Ở quy mô lớn, công việc là quản trị trên nhiều đội: một kho tiêu chuẩn kỹ thuật trung tâm giữ các cấu hình công cụ định dạng và linter dùng chung cho từng ngôn ngữ, các dịch vụ mới được sinh ra từ biểu mẫu kéo các cấu hình đó, và các cổng CI chặn các lần hợp nhất không tuân thủ. Đánh phiên bản bộ quy tắc như mã và đưa các thay đổi qua một cuộc xem xét định kỳ để tiêu chuẩn phát triển có chủ đích thay vì trôi dạt. Lợi ích là kỹ sư di chuyển giữa các đội vào mã quen thuộc, và công cụ tự động tạo ra tín hiệu đáng tin cậy vì mọi kho mã đều nhất quán.

**Chính phủ.** Mua sắm và trách nhiệm giải trình định hình lựa chọn: bắt buộc một phong cách cụ thể và bộ quy tắc bảo mật như một phần của yêu cầu cấp phép vận hành, và để đường ống phát ra một báo cáo cho thấy mọi thay đổi được hợp nhất đã vượt qua các cổng đã thống nhất làm bằng chứng kiểm toán. Vì công cụ định dạng được áp dụng tự động, mã từ nhiều nhà cung cấp và nhà thầu trông nhất quán, bảo vệ công việc bảo trì công lâu sau khi các hợp đồng kết thúc. Hãy ưu tiên các đường cơ sở của cộng đồng được công nhận hơn các quy tắc riêng để tiêu chuẩn minh bạch và bất kỳ nhà cung cấp nào trong tương lai cũng có thể áp dụng mà không bị khóa chặt vào sở hữu độc quyền.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp bốn người áp dụng các mặc định công cụ định dạng và linter của cộng đồng cho ngôn ngữ duy nhất của mình ngay từ ngày đầu, nối chúng vào hook trước commit và CI để không ai tranh cãi về khoảng trắng trong đánh giá. Vì cấu hình nằm trong chính kho mã, những người được tuyển thứ năm và thứ sáu tự thừa hưởng nó và không bao giờ thấy một bình luận về định dạng. Khi đội sau đó thêm ngôn ngữ thứ hai, họ với tới hướng dẫn chuẩn của ngôn ngữ đó thay vì phát minh một phong cách riêng mà họ không có thời gian bảo trì.

**Doanh nghiệp lớn.** Một ngân hàng lớn chạy các dịch vụ bằng Java, Python và TypeScript qua hàng chục đội. Ngân hàng công bố một kho "tiêu chuẩn kỹ thuật" trung tâm giữ các cấu hình công cụ định dạng và linter dùng chung cho mỗi ngôn ngữ. Các dịch vụ mới được sinh ra từ một biểu mẫu kéo các cấu hình đó, nên mọi kho mã bắt đầu đã tuân thủ. CI chặn việc hợp nhất khi có bất kỳ vi phạm nào, và một cuộc xem xét hằng quý chi phối các thay đổi quy tắc. Thời gian hội nhập của kỹ sư chuyển giữa các đội giảm đáng kể, vì mọi kho mã đều trông quen thuộc.

**Chính phủ.** Một cơ quan khu vực công hiện đại hóa một hệ thống cũ bắt buộc một bộ quy tắc linter về khả năng tiếp cận và bảo mật như một phần của yêu cầu cấp phép vận hành (ATO), sự phê duyệt chính thức cần thiết để chạy hệ thống trong môi trường thực. Sự tuân thủ phong cách trở thành một phần của bằng chứng kiểm toán: đường ống tạo ra một báo cáo cho thấy toàn bộ mã được hợp nhất đã vượt qua các cổng [phân tích tĩnh](https://en.wikipedia.org/wiki/Static_program_analysis) đã thống nhất. Vì công cụ định dạng được áp dụng tự động, các nhà thầu từ nhiều nhà cung cấp tạo ra mã nhất quán về mặt hình thức, làm cho công việc bảo trì dài hạn của chính phủ dễ hơn sau khi các hợp đồng kết thúc.

## Luận chứng kinh doanh: động lực, ROI và TCO

Chi phí áp dụng tiêu chuẩn chủ yếu là một lần: chọn hướng dẫn, nối công cụ và áp dụng một commit định dạng lại lớn ban đầu. Chi phí lặp lại thấp, vì việc thực thi được tự động hóa. Chi phí của việc *không* áp dụng tiêu chuẩn là lặp lại và cộng dồn: mỗi lần đánh giá tốn vài phút cho phong cách, mỗi lần hội nhập chậm hơn, các công cụ phân tích tĩnh tạo ra nhiễu, và mã không nhất quán che giấu lỗi. Trong một tổ chức lớn, những phút đó cộng lại thành mất mát tương đương toàn thời gian.

Lợi tức thể hiện ở độ trễ đánh giá giảm, ít bình luận đánh giá liên quan đến phong cách hơn, hội nhập nhanh hơn, và tín hiệu cao hơn từ công cụ tự động. Trong các môi trường chịu quy định còn có thêm lợi tức về sự sẵn sàng kiểm toán: các biện pháp kiểm soát được thực thi, chứng minh được làm giảm công sức và rủi ro của các cuộc rà soát tuân thủ. Để thuyết phục ban lãnh đạo, hãy trình bày tiêu chuẩn như một đòn bẩy chi phí thấp, hiệu quả cao lên năng suất lập trình viên và tư thế kiểm toán, và đặt một con số lên chi phí hiện tại của sự thiếu nhất quán bằng cách dùng phân tích bình luận đánh giá và dữ liệu khảo sát hội nhập.

## Phản mẫu và cạm bẫy

- **Phong cách bị tranh cãi trong đánh giá mã:** dấu hiệu việc thực thi chưa được tự động hóa; hãy chuyển quy tắc vào công cụ.
- **Tài liệu tiêu chuẩn không ai đọc:** một trang wiki không có thực thi chỉ là đồ trang trí; mỗi quy tắc cần một cơ chế.
- **Quy tắc tràn lan:** hàng trăm quy tắc chi li làm chậm công việc mà không ngăn được lỗi.
- **Cấu hình trôi dạt:** mỗi kho mã rẽ nhánh cấu hình linter riêng cho đến khi "tiêu chuẩn" chẳng còn nghĩa lý.
- **Định dạng lại toàn bộ kho mã giữa chừng công việc tính năng:** trộn commit định dạng lại với thay đổi logic phá hủy việc đánh giá và blame; hãy thực hiện các lần định dạng lại lớn trong các commit cô lập, gắn nhãn rõ ràng.
- **Phớt lờ linter bằng các ngăn chặn hàng loạt:** các lệnh tắt nội tuyến lan rộng báo hiệu một quy tắc sai hoặc một đội đã bỏ cuộc.
- **Tiêu chuẩn không có chủ sở hữu:** không có chủ sở hữu rõ ràng nghĩa là các quy tắc không bao giờ phát triển và mục nát.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Phong cách theo từng tác giả và phản ứng; không có cấu hình dùng chung; định dạng bị tranh cãi trong đánh giá và được giải quyết bởi người quan tâm nhất vào ngày hôm đó.
- **Mức 2, Phát triển:** Từng đội áp dụng công cụ định dạng và linter, nhưng cấu hình và bộ quy tắc khác nhau giữa các đội và các kho mã, nên sự nhất quán dừng lại ở ranh giới của mỗi đội.
- **Mức 3, Chuẩn hóa:** Các cấu hình dùng chung trung tâm theo từng ngôn ngữ được lập thành tài liệu và thực thi toàn tổ chức; CI chặn các lần hợp nhất không tuân thủ; các kho mã mới tự thừa hưởng tiêu chuẩn thông qua biểu mẫu hoặc khung dựng sẵn.
- **Mức 4, Quản lý:** Tiêu chuẩn được đo lường và kiểm soát bằng dữ liệu: tỷ lệ vi phạm, số lượng ngăn chặn, bình luận đánh giá liên quan đến phong cách và thời gian hội nhập được theo dõi so với đường cơ sở, và các thay đổi quy tắc được thăng cấp hoặc loại bỏ dựa trên bằng chứng đó thay vì ý kiến.
- **Mức 5, Điều phối:** Tiêu chuẩn được cải tiến liên tục và tích hợp trong toàn tổ chức; thành ngữ đa ngôn ngữ và từ vựng miền nghiệp vụ được lập thành tài liệu và thực thi, việc thực thi gần như không ma sát, và bộ quy tắc thích ứng khi ngôn ngữ, công cụ và nhu cầu tổ chức dịch chuyển.

## Ý tưởng để thảo luận

- Lằn ranh giữa một quy tắc được thực thi và một hướng dẫn có tài liệu tin vào phán đoán của kỹ sư nằm ở đâu?
- Tổ chức nên xử lý thế nào một quy tắc cộng đồng được yêu thích xung đột với một ràng buộc nội bộ thực sự?
- Ai sở hữu các tiêu chuẩn, và các thay đổi quy tắc được đề xuất, tranh luận và triển khai như thế nào mà không gây xáo trộn?
- Trong một cơ sở mã đa ngôn ngữ, quy ước nào nên thực sự phổ quát và quy ước nào nên ở lại cục bộ theo ngôn ngữ?
- Làm thế nào bạn áp dụng tiêu chuẩn lên một cơ sở mã cũ lớn mà không cần một lần định dạng lại đồng loạt gây xáo trộn?
- Công cụ hỗ trợ bởi AI nên đóng vai trò gì trong việc gợi ý hoặc thực thi các thành ngữ vượt ra ngoài định dạng cơ học?

## Những điểm cần ghi nhớ

- Coi phong cách là vấn đề đã giải quyết, tự động hóa để con người đánh giá thiết kế và tính đúng đắn.
- Áp dụng các tiêu chuẩn cộng đồng có sẵn và chỉ lập tài liệu những khác biệt.
- Thực thi ở các tầng trình soạn thảo, trước commit và CI, với CI là cổng có thẩm quyền.
- Giữ bộ quy tắc nhỏ, có thể bảo vệ và được quản trị tập trung.
- Đặt tên và thành ngữ, không phải khoảng trắng, mới là nơi khả năng đọc thực sự được giành lấy.

## Tài liệu tham khảo và đọc thêm

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt và David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell và Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (biên tập), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* và các hướng dẫn phong cách ngôn ngữ (như các ví dụ tham chiếu)
