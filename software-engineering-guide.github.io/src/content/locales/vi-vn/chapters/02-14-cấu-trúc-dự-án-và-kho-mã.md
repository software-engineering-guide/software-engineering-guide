# 2.14 Cấu trúc dự án và kho mã

## Tổng quan và động lực

Cấu trúc dự án và kho mã là sự tổ chức vật lý của một cơ sở mã: các thư mục, tệp và quy ước đặt tên quyết định một thứ cụ thể nằm ở đâu. Một *kho mã* (repository, thường viết tắt là "repo") là vật chứa được [quản lý phiên bản](https://en.wikipedia.org/wiki/Version_control) giữ các tệp của một dự án và lịch sử của chúng. Một *dự án*, đôi khi gọi là *giải pháp* khi nó nhóm nhiều thành phần liên quan, là đơn vị logic của phần mềm bạn đang xây dựng. Cấu trúc là bản đồ bạn dùng để tìm, hiểu và thay đổi phần mềm đó.

Trong một đội nhỏ, một người có thể giữ toàn bộ bố cục trong đầu. Trong một đội lớn, với hàng trăm hoặc hàng nghìn kỹ sư, thường xuyên chuyển giữa các đội, và nhà thầu ra vào, mỗi kho mã được tổ chức khác nhau lại tính một khoản thuế nhận thức mới. Khi bạn mở một kho mã lạ, bạn nên đoán được mã nguồn, kiểm thử, tài liệu và cấu hình triển khai nằm ở đâu mà không phải đọc sổ tay. Khi mọi kho mã trả lời những câu hỏi đó theo cùng một cách, việc di chuyển rẻ và hội nhập nhanh. Khi mỗi kho mã là một bông tuyết riêng biệt, mỗi lần chuyển ngữ cảnh biến thành một dự án nghiên cứu nhỏ.

Trong bối cảnh doanh nghiệp và chính phủ, cấu trúc nhất quán cũng là mối quan tâm về kiểm soát và đảm bảo. Kiểm toán viên, người rà soát bảo mật và người bảo trì dài hạn, thường làm việc nhiều năm sau khi các tác giả ban đầu đã đi, cần xác định vị trí một cách đáng tin cậy các tài liệu đặc tả, tệp giấy phép, chính sách bảo mật và định nghĩa dựng. Một bố cục dễ đoán cũng cho phép các công cụ tự động (bộ quét, bộ phân tích phụ thuộc, kiểm tra tuân thủ) hoạt động giống nhau qua cả một danh mục hệ thống. Vì vậy chương này coi cấu trúc là một quy ước bạn quyết định một lần và áp dụng ở mọi nơi. Nó liên quan chặt chẽ đến tiêu chuẩn và phong cách viết mã (chương 2.1), quản lý phiên bản và mã nguồn (chương 2.6), và tài liệu (chương 2.7).

## Các nguyên tắc chính

- Tuân theo *[nguyên tắc ít bất ngờ nhất](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: bố cục nên khớp với những gì một kỹ sư có kinh nghiệm mong đợi, để không phải ghi nhớ gì cả.
- Nhất quán qua các kho mã thắng sự thông minh cục bộ; một cấu trúc đủ đồng nhất ở mọi nơi có giá trị hơn cấu trúc hoàn hảo ở một nơi.
- [README](https://en.wikipedia.org/wiki/README) là cửa trước; người mới nên tự định hướng chỉ từ nó.
- Làm cho cấu trúc tự mô tả thông qua đặt tên, để thư mục và tệp tự công bố mục đích của chúng.
- Thực thi cấu trúc bằng khung dựng sẵn và biểu mẫu, không phải bằng ý chí và bình luận đánh giá.
- Tách các mối quan tâm một cách vật lý: mã nguồn, kiểm thử, tài liệu, bản dựng và triển khai thuộc về những nơi riêng biệt, dễ đoán.
- Tổ chức các phụ thuộc để chúng chảy theo một hướng, từ lõi ổn định hướng về rìa biến động.

## Khuyến nghị

### Áp dụng bố cục cấp cao nhất nhất quán

Xác định một tập thư mục cấp cao nhất chuẩn mà mọi kho mã dùng khi áp dụng được, và lập tài liệu mỗi thư mục để làm gì. Một quy ước phổ biến, trung lập với nhà cung cấp bao gồm: một thư mục mã nguồn (thường là `src`) cho mã môi trường thực; một thư mục kiểm thử (thường là `test` hoặc `tests`) cho các bài kiểm thử tự động; một thư mục `docs` cho tài liệu; một thư mục `build` cho định nghĩa dựng và đầu ra; một thư mục `deploy` cho triển khai và *[hạ tầng dưới dạng mã](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (các định nghĩa đọc được bằng máy của máy chủ, mạng và dịch vụ, được đề cập trong chương 8.2); một thư mục `scripts` cho tự động hóa và công cụ lập trình viên; một thư mục `examples` cho các ví dụ chạy được; và một thư mục `spec` hoặc `specification` cho đặc tả yêu cầu và thiết kế. Không phải kho nào cũng cần mọi thư mục, nhưng ở nơi một mối quan tâm tồn tại, nó nên nằm ở chỗ được mong đợi với tên được mong đợi.

### Biến README thành điểm vào

Yêu cầu một tệp README ở gốc kho mã làm điểm khởi đầu duy nhất, chuẩn tắc. Nó nên nêu dự án là gì, cách dựng và chạy nó, cách chạy kiểm thử, nơi tìm tài liệu sâu hơn, ai sở hữu nó, và cách đóng góp. README không phải toàn bộ bộ tài liệu; nó là chỉ mục trỏ đến phần còn lại (chương 2.7). Hãy coi một README bị thiếu hoặc lỗi thời là một khiếm khuyết, vì đó là thứ đầu tiên mọi kỹ sư mới, kiểm toán viên hay người tích hợp sẽ đọc.

### Chuẩn hóa tệp trình soạn thảo và cấu hình

Commit cấu hình trình soạn thảo và công cụ dùng chung vào kho mã để mọi người đóng góp nhận được hành vi nhất quán một cách tự động. Một tệp `.editorconfig` (một tệp đơn giản, không phụ thuộc trình soạn thảo xác định quy tắc khoảng trắng, thụt lề và ký tự xuống dòng) giữ cho định dạng cơ bản đồng nhất qua các trình soạn thảo và hệ điều hành khác nhau. Thêm một tệp bỏ qua cho hệ thống quản lý phiên bản (để đầu ra dựng và hiện vật cục bộ không bao giờ bị commit), cùng với các cấu hình công cụ định dạng và linter dùng chung được mô tả trong chương 2.1. Những tệp này khiến các quy ước của kho mã trở nên chủ động, không chỉ được lập tài liệu.

### Xác định quy ước đặt tên và thư mục

Hãy thống nhất các quy ước đặt tên thư mục và tệp (kiểu viết hoa, dấu phân cách, số ít so với số nhiều, và các hậu tố bắt buộc như những hậu tố đánh dấu kiểm thử) và áp dụng chúng đồng nhất. Tên nên tiết lộ ý định và khớp với từ vựng miền nghiệp vụ dùng ở nơi khác trong tổ chức. Mục tiêu đơn giản: một đường dẫn nên truyền đạt ý nghĩa, để đọc tên một thư mục hay tệp cho bạn biết bên trong có gì mà không cần mở nó.

### Tổ chức các tầng và phụ thuộc một cách có chủ đích

Cấu trúc cơ sở mã sao cho các tầng kiến trúc của nó hiện ra trong bố cục thư mục, và các phụ thuộc chảy theo một hướng duy nhất, hợp lý. Chính sách cấp cao hơn không nên phụ thuộc vào chi tiết cấp thấp. Mã dùng chung, ổn định nên nằm ở nơi nhiều mô-đun có thể với tới mà không tạo chu trình. Khi bạn làm cho việc phân tầng trở nên vật lý, phản ánh trong cây thư mục, kỹ sư có nhiều khả năng tôn trọng nó hơn, và các vi phạm dễ phát hiện hơn trong đánh giá và trong các kiểm tra phụ thuộc tự động.

### Thực thi cấu trúc bằng khung dựng sẵn và biểu mẫu

Cung cấp *[khung dựng sẵn](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, việc sinh tự động một dự án khởi đầu, để các kho mã mới bắt đầu đã đúng. Một *biểu mẫu* hoặc *cookiecutter* (một bộ khung dự án có tham số sinh ra một kho mã làm sẵn từ câu trả lời cho vài câu hỏi) mã hóa bố cục chuẩn, README, các tệp cấu hình và thiết lập [CI](https://en.wikipedia.org/wiki/Continuous_integration) vào một nơi. Khi kỹ sư tạo dịch vụ mới từ một biểu mẫu dùng chung, sự nhất quán trở thành mặc định thay vì khát vọng, và các cải tiến cho biểu mẫu chảy vào các dự án tương lai.

### Giữ cấu trúc nhất quán qua nhiều kho mã ở quy mô lớn

Hãy coi chính bố cục là một tiêu chuẩn được quản trị: được duy trì tập trung như bất kỳ tiêu chuẩn kỹ thuật nào khác (chương 1.7), và được đánh phiên bản như mã (chương 2.6). Công bố nó, cung cấp các biểu mẫu triển khai nó, và chỉ cho phép sai lệch thông qua một quy trình ngoại lệ có tài liệu, để "tiêu chuẩn" giữ được ý nghĩa của nó. Ở quy mô danh mục, gần như toàn bộ giá trị của cấu trúc đến từ tính đồng nhất qua các kho mã, nên sự trôi dạt là rủi ro chính cần quản lý.

### Để cấu trúc cung cấp thông tin cho lựa chọn monorepo so với nhiều kho

Liên hệ cấu trúc với quyết định ranh giới kho mã được đề cập trong chương 2.6. Một *[monorepo](https://en.wikipedia.org/wiki/Monorepo)* (một kho chứa nhiều dự án) cần một quy ước nội bộ rõ ràng để tách các dự án và mã dùng chung của chúng, để cây duy nhất vẫn điều hướng được. Một cách tiếp cận *nhiều kho* (nhiều kho nhỏ, mỗi dự án hoặc dịch vụ một kho) cần sự nhất quán xuyên kho mạnh, để mỗi kho vẫn quen thuộc dù nó đứng riêng. Dù cách nào, một cấu trúc có tài liệu, có biểu mẫu là thứ giữ cho việc điều hướng dễ đoán. Lựa chọn ranh giới thay đổi nơi bạn áp dụng quy ước, không phải việc bạn có cần một quy ước hay không.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Bố cục chuẩn nghiêm ngặt toàn tổ chức | Quen thuộc tức thì; kỹ sư di chuyển được; công cụ đồng nhất | Thỉnh thoảng không phù hợp với dự án khác thường; cần quản trị |
| Tự do bố cục theo từng đội | Tối ưu cục bộ; tự chủ cao | Phân mảnh; chuyển ngữ cảnh tốn kém; công cụ không nhất quán |
| Khung dựng sẵn và biểu mẫu | Kho mã đúng theo mặc định; thay đổi lan truyền | Bảo trì biểu mẫu; rủi ro trôi khỏi các kho được sinh ra |
| Phân cấp thư mục sâu, phân tầng | Cấu trúc tường minh; ranh giới rõ ràng | Chi phí điều hướng; đường dẫn dài; rủi ro thiết kế quá mức |
| Bố cục phẳng, nông | Dễ quét; ít nghi thức | Tách biệt kém; vỡ ra khi dự án lớn lên |

Sự đánh đổi chi phối là đồng nhất so với tự chủ. Một bố cục chuẩn duy nhất loại bỏ ma sát cho nhiều kỹ sư chuyển giữa các cơ sở mã, với cái giá là thỉnh thoảng có dự án mà nhu cầu không khớp gọn với khuôn mẫu. Trong một tổ chức lớn, lợi ích tập thể từ sự quen thuộc hầu như luôn vượt trội tổn thất cục bộ đó. Đó là lý do tư thế được khuyến nghị là một tiêu chuẩn mặc định mạnh cộng với một con đường ngoại lệ có tài liệu (chương 1.7), thay vì sự đồng nhất cứng nhắc hay tự do không được quản lý. Sự đánh đổi thứ cấp là độ sâu so với đơn giản: đủ cấu trúc để tách các mối quan tâm thực, nhưng không nhiều đến mức điều hướng biến thành chuyến đi bộ qua các thư mục rỗng.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi một kỹ sư chuyển sang một kho mã lạ của chúng ta, mất bao lâu để họ tìm thấy kiểm thử, cấu hình triển khai và người sở hữu?** Đây là khoản thuế điều hướng mà cấu trúc tồn tại để loại bỏ, và ở quy mô danh mục nó được trả hàng nghìn lần mỗi năm theo từng phần nhỏ cộng lại thành thời gian kỹ thuật mất đi nghiêm trọng. Điểm của nguyên tắc ít bất ngờ nhất là một kỹ sư có kinh nghiệm nên đoán được mã nguồn, kiểm thử, tài liệu và triển khai nằm ở đâu mà không phải đọc sổ tay, vì vậy phép thử trung thực là liệu việc đoán đó có thành công qua các kho mã của bạn không. Hãy mang một con số thực đến cuộc họp: tự đo thời gian định hướng trong hai hoặc ba kho mã nội bộ lạ, hoặc lấy dữ liệu hội nhập về người mới gia nhập mất bao lâu để thực hiện thay đổi đầu tiên. Nếu câu trả lời được đo bằng nhiều ngày nghiên cứu thay vì vài phút nhận ra, bạn đã định lượng chi phí của các kho mã bông tuyết, và nó biện minh cho khoản đầu tư một lần vào một bố cục chuẩn mà mọi kho mã đều chia sẻ.

2. **Các tầng kiến trúc của chúng ta có hiện ra trong cây thư mục không, hay các chu trình phụ thuộc ẩn trong một bố cục phẳng?** Cấu trúc không chỉ là chuyện dễ tìm: khi bạn làm cho việc phân tầng trở nên vật lý, kỹ sư tôn trọng nó và người đánh giá cùng các kiểm tra phụ thuộc tự động có thể phát hiện vi phạm, trong khi một đống phẳng để sự liên kết không đúng và chu trình len lỏi mà không bị chú ý cho đến khi thay đổi trở nên nguy hiểm. Trên một hệ thống lớn, tồn tại lâu, đây là thứ giữ cho chính sách cấp cao hơn không âm thầm phụ thuộc vào chi tiết cấp thấp, và đó chính là loại xói mòn rẻ để ngăn chặn và đắt để gỡ. Hãy mang đồ thị phụ thuộc của bạn hoặc chạy một kiểm tra nhanh: có chu trình không, và có gì ổn định đang phụ thuộc vào thứ biến động không? Câu trả lời nên đẩy bạn phản ánh các tầng trong thư mục và thêm các kiểm tra hướng phụ thuộc tự động, để các ranh giới hiển thị trong cây và được thực thi trong đường ống thay vì chỉ sống trong mô hình tinh thần của ai đó.

3. **Các kho mã mới của chúng ta có bắt đầu đúng từ một biểu mẫu, hay chúng ta dựa vào một trang wiki và thiện chí?** Cấu trúc được thực thi bằng khung dựng sẵn là mặc định; cấu trúc được mô tả trong một tài liệu thì trôi dạt, vì thực tế đi theo thứ sinh ra kho mã, không phải thứ một trang nói chúng nên trông thế nào. Với một tổ chức lớn hoặc chịu quy định, đây cũng là mối quan tâm về đảm bảo: khi mọi kho được sinh từ một biểu mẫu chung, bộ quét bảo mật, bộ phân tích phụ thuộc và kiểm toán viên tìm thấy giấy phép, chính sách bảo mật, đặc tả và định nghĩa dựng ở cùng một nơi mỗi lần, qua các nhà cung cấp và qua nhiều năm. Hãy mang bằng chứng: bao nhiêu kho mã gần đây của bạn được dựng sẵn từ biểu mẫu chuẩn so với lắp ráp bằng tay, và những kho từ biểu mẫu đã trôi xa đến đâu kể từ đó? Hành động là biến biểu mẫu thành cách dễ duy nhất để bắt đầu một kho, quản trị nó như một tiêu chuẩn có phiên bản với con đường ngoại lệ có tài liệu, và phát hiện sự trôi dạt tự động, vì tính đồng nhất là nơi gần như toàn bộ giá trị của cấu trúc nằm.

4. **Chúng ta đã quyết định tiêu chuẩn của mình trải qua một monorepo hay nhiều kho riêng biệt chưa, và cùng quy ước đó có thực sự đứng vững ở cả hai phía của ranh giới đó không?** Lựa chọn ranh giới kho mã thay đổi nơi bạn áp dụng quy ước, không phải việc bạn có cần một quy ước hay không, và làm sai nghĩa là một cây khổng lồ không ai điều hướng được hoặc một đám kho mã mỗi cái có cảm giác xa lạ. Một monorepo cần một quy ước nội bộ rõ ràng để tách các dự án và mã dùng chung của chúng để cây duy nhất vẫn điều hướng được, trong khi cách tiếp cận nhiều kho cần sự nhất quán xuyên kho mạnh để mỗi kho đứng riêng vẫn quen thuộc. Hãy mang bản kiểm kê hiện tại: bạn có bao nhiêu kho, mã dùng chung được tách thế nào bên trong bất kỳ monorepo nào, và một phép thử tính giờ xem một kỹ sư có thể tìm một dự án trong cây lớn nhanh như tìm một dự án trong kho đứng riêng không. Với một doanh nghiệp lớn hoặc chương trình chính phủ nơi các nhà cung cấp khác nhau giao các kho riêng, hãy quyết định có chủ đích phần nào của quy ước là phổ quát và phần nào đặc thù theo ranh giới, vì kiểm toán viên và công cụ nền tảng phải hoạt động giống nhau dù mã đến dưới dạng một cây hay năm mươi.

5. **Ai sở hữu tiêu chuẩn cấu trúc của chúng ta, và điều gì thực sự xảy ra khi một dự án thực sự không khớp với nó?** Ở quy mô danh mục gần như toàn bộ giá trị của cấu trúc đến từ tính đồng nhất, nên các rủi ro thực sự là một tiêu chuẩn không có chủ sở hữu mục nát và một con đường ngoại lệ mơ hồ đến mức mọi đội âm thầm phát minh bố cục riêng. Căng thẳng là giữa sự đồng nhất cứng nhắc không phù hợp dự án khác thường nào và tự do không được quản lý làm phân mảnh mọi thứ, và câu trả lời lành mạnh là một mặc định mạnh cộng với một quy trình ngoại lệ có tài liệu, có thể kiểm toán được quản trị bởi một chủ sở hữu được nêu tên và đánh phiên bản như mã. Hãy mang bằng chứng: có một chủ sở hữu chịu trách nhiệm duy nhất không, một tài liệu tiêu chuẩn có phiên bản kèm nhật ký thay đổi, một nhật ký các ngoại lệ đã cấp và vì sao, và một số lượng các sai lệch không có tài liệu mà bạn có thể tìm thấy ngoài thực tế. Trong bối cảnh doanh nghiệp và chính phủ, một ngoại lệ không ai ghi lại là một khoảng trống kiểm soát, vì vậy hãy gắn mỗi sai lệch với một lý do bằng văn bản và một ngày xem xét, và bảo đảm các hợp đồng mua sắm bắt buộc bố cục cũng nêu tên ai có thể phê duyệt những sai lệch khỏi nó.

6. **README và các tệp cấu hình được commit của chúng ta có làm cho các quy ước chủ động, hay chỉ mang tính trang trí?** README là cửa trước, còn `.editorconfig`, tệp bỏ qua và cấu hình linter được commit là thứ khiến các quy ước tự thực thi, nhưng đây là những thứ đầu tiên lỗi thời và cuối cùng được chú ý cho đến khi một kiểm toán viên hay người mới gia nhập không thể dựng được dự án. Căng thẳng là giữa một README gọn gàng giữ được cập nhật và một README kỹ lưỡng trôi dạt, và giữa việc tin mọi người định dạng mã đúng và để cấu hình dùng chung thực thi điều đó tự động. Hãy mang một mẫu: lấy năm kho và kiểm tra bao nhiêu README thực sự nêu dự án là gì, cách dựng, kiểm thử và chạy nó, và ai sở hữu nó, và bao nhiêu kho mang các tệp cấu hình dùng chung thay vì dựa vào thói quen cá nhân. Với một tổ chức lớn hoặc chịu quy định, nơi người tích hợp, người rà soát bảo mật và người bảo trì dài hạn đọc README trước mọi thứ khác, hãy coi một cửa trước bị thiếu hoặc lỗi thời là khiếm khuyết có chủ sở hữu, và kiểm tra sự hiện diện của tệp cấu hình tự động để sự tuân thủ không phụ thuộc vào thiện chí.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ thắng, vì vậy hãy thống nhất một bố cục đơn giản, đủ phẳng cho kho mã đầu tiên của bạn (src, test, docs, scripts, một README đầy đủ, một `.editorconfig` và các tệp bỏ qua) và lưu nó thành một biểu mẫu nhẹ ngay buổi chiều đó. Sinh dịch vụ thứ hai từ nó để cả hai kho cảm thấy quen thuộc và một nhà thầu mới hội nhập trong vài giờ thay vì dịch ngược một bông tuyết. Cưỡng lại các phân cấp sâu và quản trị nặng mà bạn chưa cần; toàn bộ lợi tức ở đây là hai người sáng lập và một nhà thầu chia sẻ một bản đồ.

**Doanh nghiệp nhỏ.** Không có chuyên gia nền tảng và ngân sách eo hẹp, hãy áp dụng bố cục quy ước mà ngôn ngữ hoặc khung của bạn đã giả định thay vì phát minh một cái, để công cụ có sẵn và bất kỳ nhân viên mới nào đến đã được huấn luyện sẵn. Hãy mua khung dựng sẵn (một trình sinh của khung hoặc một biểu mẫu cookiecutter) thay vì tự xây, và dành công sức khan hiếm của bạn để giữ một README đầy đủ luôn cập nhật. README đó là bảo hiểm rẻ nhất bạn có cho ngày người duy nhất biết bố cục chuyển đi.

**Doanh nghiệp lớn.** Qua nhiều đội và hàng trăm kho mã, mục tiêu là đồng nhất: công bố một tiêu chuẩn cấu trúc có phiên bản, sinh mọi dịch vụ mới từ các biểu mẫu dùng chung, phát hiện sự trôi dạt tự động, và chỉ cho phép sai lệch thông qua một quy trình ngoại lệ có tài liệu. Vì mọi kho trông giống nhau, một kỹ sư được điều sang đội mới làm việc hiệu quả trong vài giờ và các bộ quét bảo mật cùng phụ thuộc toàn danh mục tìm thấy giấy phép, chính sách bảo mật và định nghĩa dựng ở cùng một nơi mỗi lần. Hãy ngân sách tường minh cho việc bảo trì biểu mẫu và phát hiện trôi dạt, vì sự duy trì đó là thứ giữ cho tiêu chuẩn có ý nghĩa ở quy mô lớn.

**Chính phủ.** Mua sắm, tính minh bạch và trách nhiệm giải trình dài hạn định hình bố cục, vì vậy hãy bắt buộc một cấu trúc chung trong các tiêu chuẩn phân phối ràng buộc mọi nhà cung cấp. Yêu cầu một thư mục `specification` nối mã với yêu cầu đã được phê duyệt, một tệp giấy phép và chính sách bảo mật ở gốc, và một thư mục `deploy` chứa các định nghĩa hạ tầng dưới dạng mã, để kiểm toán viên xác định vị trí hiện vật tuân thủ theo cùng một cách trong mọi hệ thống. Vì các nhà thầu từ các nhà cung cấp khác nhau đều theo một bản đồ, việc bảo trì sau khi hợp đồng kết thúc tốn ít hơn nhiều, và công chúng có được một dấu vết có thể bảo vệ, kiểm tra được từ yêu cầu đến mã đang chạy.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp ba người thống nhất một bố cục chuẩn đơn giản cho kho mã đầu tiên (src, test, docs, scripts, một README đầy đủ, một .editorconfig và các tệp bỏ qua) và lưu nó thành một biểu mẫu nhẹ. Khi họ dựng dịch vụ thứ hai một tháng sau, họ sinh nó từ biểu mẫu đó, nên cả hai kho đã cảm thấy quen thuộc và nhà thầu mới hội nhập trong một buổi chiều. Họ cưỡng lại các phân cấp thư mục sâu mà họ chưa cần, giữ cây đủ phẳng để quét nhìn một lần. Chi phí là một buổi chiều thiết lập, và nó giúp họ khỏi sự tràn lan bông tuyết vốn sẽ biến mọi kho mã tương lai thành một dự án nghiên cứu nhỏ.

**Doanh nghiệp lớn.** Một nhà bán lẻ đa quốc gia vận hành hàng trăm dịch vụ qua nhiều ngôn ngữ. Đội nền tảng của họ công bố một tiêu chuẩn cấu trúc kho mã có phiên bản và một tập biểu mẫu dự án triển khai nó. Mọi dịch vụ mới được sinh từ một biểu mẫu, nên nó đến với các thư mục chuẩn `src`, `test`, `docs`, `deploy` và `scripts`, một README đầy đủ, một `.editorconfig`, các tệp bỏ qua, và một đường ống CI đang hoạt động. Vì mọi kho mã trông giống nhau, một kỹ sư được điều sang đội mới làm việc hiệu quả trong vài giờ, và các bộ quét bảo mật và phụ thuộc toàn tổ chức chạy đồng nhất vì chúng luôn tìm thấy tệp ở nơi chúng mong đợi.

**Chính phủ.** Một cơ quan quốc gia hiện đại hóa các hệ thống cũ bắt buộc một bố cục kho mã chung như một phần của tiêu chuẩn phân phối cho mọi nhà cung cấp. Mỗi kho mã phải chứa một thư mục `specification` nối mã với yêu cầu đã được phê duyệt, một README có tài liệu, một tệp giấy phép và chính sách bảo mật ở gốc, và một thư mục `deploy` chứa các định nghĩa hạ tầng dưới dạng mã (chương 8.2). Vì các nhà thầu từ các nhà cung cấp khác nhau đều theo cùng một cấu trúc, kiểm toán viên của cơ quan có thể xác định vị trí hiện vật tuân thủ theo cùng một cách trong mọi hệ thống, và bảo trì dài hạn sau khi hợp đồng kết thúc tốn ít hơn nhiều vì những người bảo trì đến đã biết bản đồ.

## Luận chứng kinh doanh: động lực, ROI và TCO

Chi phí áp dụng một tiêu chuẩn cấu trúc chủ yếu là một lần: thống nhất bố cục, xây dựng biểu mẫu và lập tài liệu quy ước. Chi phí lặp lại thấp, tập trung vào việc bảo trì biểu mẫu và quản trị ngoại lệ. Chi phí của việc *không* có tiêu chuẩn là lặp lại và cộng dồn: mọi kỹ sư mở một kho mã lạ trả một khoản thuế điều hướng, mọi lần hội nhập chậm hơn, và công cụ tự động phải được cấu hình cho từng kho vì không có gì nằm ở nơi bạn mong đợi. Trong một tổ chức lớn, những ma sát nhỏ này nhân lên thành tổn thất nghiêm trọng về thời gian kỹ thuật.

Lợi tức thể hiện ở hội nhập nhanh hơn, di chuyển giữa các đội rẻ hơn, tín hiệu cao hơn từ công cụ toàn danh mục, và, trong bối cảnh chịu quy định, chi phí kiểm toán và bảo trì dài hạn thấp hơn, vì các hiện vật luôn tìm thấy được. *Tổng chi phí sở hữu* (TCO, nghĩa là toàn bộ chi phí vòng đời của việc xây dựng, vận hành và bảo trì một hệ thống) giảm nhiều nhất ở các hệ thống tồn tại lâu, nơi những người bảo trì hưởng lợi từ cấu trúc dễ đoán thường không phải là các tác giả đã tạo ra nó. Để thuyết phục ban lãnh đạo, hãy đóng khung cấu trúc như một tiêu chuẩn chi phí thấp, hiệu quả cao cải thiện năng suất lập trình viên và sự sẵn sàng kiểm toán, và đặt một con số lên chi phí hiện tại của sự thiếu nhất quán bằng dữ liệu thời gian hội nhập và công sức bỏ ra để tìm đồ trong các kho mã lạ.

## Phản mẫu và cạm bẫy

- **Kho mã bông tuyết:** mỗi kho được tổ chức khác nhau, nên từng cái phải được học lại từ đầu.
- **README bị thiếu hoặc lỗi thời:** không có cửa trước, buộc người mới dịch ngược cách dựng và chạy dự án.
- **Cấu trúc bằng tài liệu, không phải bằng biểu mẫu:** một trang wiki mô tả bố cục chuẩn, nhưng không gì sinh ra hay thực thi nó, nên thực tế trôi khỏi nó.
- **Biểu mẫu trôi dạt:** các kho được sinh từ biểu mẫu phân kỳ theo thời gian và các cải tiến cho biểu mẫu không bao giờ đến được chúng.
- **Phân cấp thiết kế quá mức:** những tầng thư mục gần như rỗng lồng sâu thêm nghi thức mà không giúp điều hướng.
- **Trộn các mối quan tâm:** mã nguồn, kiểm thử, đầu ra dựng và bí mật lẫn lộn với nhau mà không có sự tách biệt rõ ràng.
- **Commit đầu ra dựng và hiện vật cục bộ:** các tệp sinh ra được commit vì quy tắc bỏ qua chưa bao giờ được thiết lập, làm ô nhiễm lịch sử và diff.
- **Vi phạm tầng bị cấu trúc phẳng che giấu:** không có ranh giới vật lý, nên chu trình phụ thuộc và liên kết không đúng len lỏi mà không bị chú ý.

## Mô hình trưởng thành

- **Mức 1 (Khởi đầu):** Mỗi kho mã được các tác giả của nó tổ chức tùy nghi, phản ứng với bất cứ điều gì thời điểm đó cần; bố cục rất khác nhau; README bị thiếu hoặc không đáng tin; người mới phải được dẫn dắt qua từng kho bằng tay.
- **Mức 2 (Phát triển):** Các quy ước cơ bản tồn tại không chính thức và nhiều kho mã giống nhau; một số đội giữ một bố cục khởi đầu của riêng mình; nhưng không có tiêu chuẩn có thẩm quyền, không có khung dựng sẵn dùng chung, và cấu trúc trôi dạt rõ rệt từ đội này sang đội khác.
- **Mức 3 (Chuẩn hóa):** Một tiêu chuẩn cấu trúc có tài liệu, có phiên bản được thực thi trong toàn tổ chức; các kho mã mới được sinh từ các biểu mẫu dùng chung mang bố cục chuẩn, README, các tệp cấu hình và CI; sai lệch đi qua một quy trình ngoại lệ có tài liệu thay vì xảy ra trong im lặng.
- **Mức 4 (Quản lý):** Sự tuân thủ tiêu chuẩn được đo và kiểm soát bằng dữ liệu: các kiểm tra tự động báo cáo tỷ lệ kho khớp bố cục, các kho từ biểu mẫu đã trôi bao xa, độ đầy đủ của README, và các vi phạm hướng phụ thuộc, tất cả được theo dõi theo đường cơ sở; thời gian hội nhập và điều hướng được đo; các ngoại lệ được ghi lại và xem xét, và các thay đổi biểu mẫu được phê duyệt dựa trên bằng chứng thay vì ý kiến.
- **Mức 5 (Điều phối):** Cấu trúc được cải tiến liên tục và thích ứng: các cải tiến biểu mẫu tự động lan truyền đến các kho mã hiện có, quản trị cấu trúc được tích hợp với công cụ bảo mật, tuân thủ và nền tảng, và tiêu chuẩn tiến hóa có chủ đích khi ngôn ngữ, kiến trúc và danh mục dịch chuyển, giữ tính đồng nhất cao trong khi tổ chức thay đổi xung quanh nó.

## Ý tưởng để thảo luận

- Những thư mục cấp cao nhất nào nên thực sự phổ quát trong tổ chức của bạn, và những thư mục nào nên tùy chọn?
- Làm thế nào bạn giữ các kho mã được sinh từ biểu mẫu khỏi trôi xa nó theo thời gian?
- Lằn ranh giữa một phân cấp phân tầng hữu ích và nghi thức thư mục thiết kế quá mức nằm ở đâu?
- Tiêu chuẩn cấu trúc của bạn nên khác nhau thế nào, nếu có, giữa monorepo và cách tiếp cận nhiều kho?
- Quy trình ngoại lệ phù hợp cho một dự án có nhu cầu thực sự không khớp với bố cục chuẩn là gì?
- Bao nhiêu phần cấu trúc của bạn có thể được kiểm tra tự động, và phần nào vẫn dựa vào đánh giá của con người?
- Ai sở hữu tiêu chuẩn cấu trúc và các biểu mẫu của nó, và các thay đổi được đề xuất và triển khai như thế nào?

## Những điểm cần ghi nhớ

- Tổ chức mọi kho mã sao cho bất kỳ kỹ sư nào cũng điều hướng được bất kỳ cơ sở mã nào theo mong đợi, tuân theo nguyên tắc ít bất ngờ nhất.
- Áp dụng bố cục cấp cao nhất nhất quán (mã nguồn, kiểm thử, tài liệu, dựng, triển khai, tập lệnh, ví dụ, đặc tả) và biến README thành điểm vào.
- Commit cấu hình trình soạn thảo và công cụ (như `.editorconfig`) để các quy ước chủ động, không chỉ được viết ra.
- Thực thi cấu trúc bằng khung dựng sẵn và biểu mẫu để các kho mã mới đúng theo mặc định.
- Ở quy mô lớn, giá trị nằm ở tính đồng nhất: quản trị tiêu chuẩn, quản lý sự trôi dạt, và chỉ cho phép sai lệch bằng ngoại lệ có tài liệu.

## Tài liệu tham khảo và đọc thêm

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt và David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck và Hyrum Wright (biên tập), *Software Engineering at Google*
- Scott Chacon và Ben Straub, *Pro Git*
- Tài liệu dự án EditorConfig (như một tiêu chuẩn tham chiếu cho cấu hình trình soạn thảo)
