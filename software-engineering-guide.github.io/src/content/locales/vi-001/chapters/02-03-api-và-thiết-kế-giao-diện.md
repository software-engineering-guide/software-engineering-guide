# 2.3 API và thiết kế giao diện

## Tổng quan và động lực

[API](https://en.wikipedia.org/wiki/API) (giao diện lập trình ứng dụng) là hợp đồng qua đó một phần mềm cung cấp năng lực cho phần mềm khác. Đó là nơi các đội, hệ thống và tổ chức gặp nhau, và là thứ bền vững nhất và đắt đỏ nhất khi làm sai. Bạn có thể tái cấu trúc chữ ký của một hàm nội bộ một cách tự do. Một API đã công bố thì khác: đó là lời hứa với những người dùng mà bạn có thể không bao giờ gặp, và phá vỡ nó là phá vỡ họ. Khi các tổ chức tách [khối đơn](https://en.wikipedia.org/wiki/Monolithic_application) thành các dịch vụ và mở các năng lực cho đối tác và công chúng, API trở thành bề mặt sản phẩm chính và rủi ro tích hợp chính.

Với các đội lớn, API là thứ cho phép mọi người làm việc độc lập. Một giao diện được thiết kế tốt cho phép bạn thay đổi bên trong mà không phải điều phối với mọi người dùng, đó chính là toàn bộ ý nghĩa của một ranh giới dịch vụ. Một giao diện thiết kế kém làm rò rỉ chi tiết nội bộ, buộc phải triển khai đồng loạt, và biến một tập hợp dịch vụ thành một khối đơn phân tán: các dịch vụ tách rời nhau nhưng liên kết chặt đến mức phải được xây dựng và triển khai cùng nhau. Thiết kế API của bạn trực tiếp quyết định các đội của bạn có thể di chuyển độc lập đến mức nào.

Trong bối cảnh doanh nghiệp và chính phủ, API còn mang các nghĩa vụ về tuân thủ, bảo mật và tuổi thọ. Một API khu vực công có thể được yêu cầu tuân theo [tiêu chuẩn mở](https://en.wikipedia.org/wiki/Open_standard), giữ ổn định nhiều năm, và phục vụ các nhà phát triển bên ngoài mà bạn không thể điều phối. API doanh nghiệp là nền tảng của các tích hợp đối tác với mức dịch vụ theo hợp đồng. Tất cả điều này nâng cao tiêu chuẩn đối với kỷ luật phiên bản, [khả năng tương thích ngược](https://en.wikipedia.org/wiki/Backward_compatibility), quản trị và trải nghiệm của nhà phát triển.

## Các nguyên tắc chính

- Thiết kế hợp đồng trước. Giao diện là một quyết định sản phẩm có chủ đích, không phải sản phẩm phụ của việc triển khai.
- Tối ưu hóa cho trải nghiệm của người dùng, không phải sự tiện lợi của bạn.
- Coi khả năng tương thích ngược là một lời hứa. Các thay đổi phá vỡ cần một phiên bản mới và một con đường di chuyển.
- Làm cho việc dễ làm là việc đúng: mặc định hợp lý, lỗi dễ đoán, quy ước nhất quán.
- Thiết kế cho thất bại. [Tính lũy đẳng](https://en.wikipedia.org/wiki/Idempotence) (một yêu cầu lặp lại có cùng tác dụng như một yêu cầu đơn), thử lại, phân trang và [giới hạn tốc độ](https://en.wikipedia.org/wiki/Rate_limiting) là những mối quan tâm hạng nhất, không phải nghĩ đến sau.
- Chọn kiểu giao thức cho phù hợp với tương tác, không phải theo mốt.
- Quản trị API như sản phẩm, với chủ sở hữu, vòng đời và tài liệu.

## Khuyến nghị

### Làm việc theo hướng API-trước và dựa trên hợp đồng

Hãy xác định và rà soát hợp đồng API, bao gồm các tài nguyên, thao tác, lược đồ và ngữ nghĩa lỗi của nó, trước khi bạn viết phần triển khai. Dùng một đặc tả có thể đọc bằng máy, để hợp đồng có thể sinh ra tài liệu, khung mã máy khách và máy chủ, máy chủ giả lập và việc xác thực. Khi đó người dùng có thể bắt đầu tích hợp với bản giả lập trong lúc bạn xây dựng, và hợp đồng trở thành nguồn sự thật duy nhất mà cả hai phía kiểm thử đối chiếu.

### Chọn kiểu tương tác một cách có chủ đích

Hãy chọn giữa [REST](https://en.wikipedia.org/wiki/REST) (chuyển trạng thái đại diện), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC) và [nhắn tin hướng sự kiện](https://en.wikipedia.org/wiki/Event-driven_architecture) dựa trên tương tác, không phải sở thích cá nhân. Dùng REST cho các giao diện hướng tài nguyên, tương tác rộng rãi, có thể lưu đệm. Dùng GraphQL khi các máy khách đa dạng cần các lần đọc linh hoạt, tổng hợp trên một đồ thị phong phú. Dùng gRPC cho các cuộc gọi hiệu năng cao, định kiểu mạnh giữa các dịch vụ nội bộ. Dùng nhắn tin hướng sự kiện cho các quy trình bất đồng bộ, tách rời và để lan truyền thay đổi trạng thái. Nhiều hệ thống lớn dùng nhiều kiểu cùng lúc, mỗi kiểu ở nơi nó phù hợp.

### Đánh phiên bản và ngừng dùng một cách có kỷ luật

Hãy áp dụng một chiến lược phiên bản tường minh và một chính sách ngừng dùng được công bố: cách bạn phân loại thay đổi, bạn hỗ trợ các phiên bản cũ trong bao lâu, và cách bạn thông báo cho người dùng. Vạch một lằn ranh rõ ràng giữa các thay đổi tương thích ngược (thêm trường tùy chọn, điểm cuối mới) và các thay đổi phá vỡ (xóa hoặc đổi tên trường, thay đổi kiểu hoặc ngữ nghĩa). Không bao giờ dùng lại ý nghĩa của một trường hiện có. Cho người dùng các khoảng chồng lấp để di chuyển, và truyền đạt mốc thời gian từ rất sớm.

### Làm cho ngữ nghĩa lỗi nhất quán và đọc được bằng máy

Trả về các lỗi có cấu trúc, dễ đoán: mã ổn định đọc được bằng máy, thông báo cho con người đọc, và đủ ngữ cảnh để hành động mà không làm rò rỉ nội bộ nhạy cảm. Dùng cùng ngữ nghĩa trạng thái trên mọi điểm cuối, để máy khách có thể xử lý lỗi một cách đồng nhất. Hãy lập tài liệu mọi lỗi mà người dùng có thể gặp.

### Xây dựng sẵn tính lũy đẳng, phân trang và giới hạn tốc độ

Làm cho các thao tác ghi an toàn để thử lại bằng cách hỗ trợ khóa lũy đẳng, để một máy khách thử lại sau khi hết thời gian chờ không tính phí hai lần hoặc tạo hai lần. Phân trang mọi điểm cuối danh sách ngay từ ngày đầu, và ưu tiên phân trang theo con trỏ cho các tập dữ liệu lớn hoặc thay đổi. Áp dụng và lập tài liệu các giới hạn tốc độ, và trả về trạng thái giới hạn hiện tại cho máy khách để họ có thể lùi lại một cách êm ái.

### Quản trị API và đầu tư vào trải nghiệm nhà phát triển

Hãy coi mỗi API là một sản phẩm, với một chủ sở hữu, một vòng đời và một mục trong danh mục. Thiết lập một buổi rà soát thiết kế hoặc một hội đồng tiêu chuẩn API để các giao diện nhất quán giữa các đội. Đầu tư vào trải nghiệm nhà phát triển: tài liệu tham chiếu chính xác, hướng dẫn bắt đầu nhanh, ví dụ, môi trường thử nghiệm và nhật ký thay đổi. Trong một hệ sinh thái lớn, một cổng thông tin hoặc danh mục giúp các API dễ tìm thấy là thiết yếu.

## Đánh đổi: ưu và nhược điểm

| Kiểu | Phù hợp nhất cho | Ưu điểm | Nhược điểm |
|---|---|---|---|
| REST / HTTP | API công khai, hướng tài nguyên | Phổ biến, lưu đệm được, đơn giản, tương tác tốt | Lấy dữ liệu thừa/thiếu; nhiều vòng đi về; hợp đồng lỏng lẻo trừ khi được đặc tả |
| GraphQL | Đọc linh hoạt cho nhiều máy khách | Truy vấn do máy khách chỉ định; một điểm cuối; lược đồ mạnh | Độ phức tạp về lưu đệm và giới hạn tốc độ; rủi ro chi phí truy vấn; độ phức tạp ở máy chủ |
| gRPC | Cuộc gọi hiệu năng cao nội bộ | Nhanh, gọn, định kiểu mạnh, hỗ trợ luồng | Hỗ trợ trình duyệt kém; kém dễ đọc với con người; công cụ nặng hơn |
| Hướng sự kiện | Quy trình bất đồng bộ, tách rời | Liên kết lỏng; mở rộng được; chịu lỗi | Khó suy luận hơn; nhất quán cuối cùng; độ phức tạp vận hành |

Các chiến lược phiên bản đánh đổi sự ổn định lấy chi phí bảo trì. Hỗ trợ nhiều phiên bản cũ bảo vệ người dùng, nhưng nó nhân lên lượng mã bạn phải bảo trì và kiểm thử. Khả năng tương thích ngược đánh đổi sự tự do của chính bạn lấy sự ổn định cho người dùng, thường là sự đánh đổi đúng cho một API được dùng rộng rãi. Bức tranh lớn: cái giá của một quyết định API tồi được trả bởi mọi người dùng trong suốt vòng đời của giao diện. Vì vậy đáng để dành nhiều công sức thiết kế ở ranh giới hơn hầu như bất cứ nơi nào khác.

## Câu hỏi để thảo luận với đội của bạn

1. **Làm thế nào bạn phân loại một thay đổi là tương thích ngược hay phá vỡ, và kiểm tra tự động nào bắt một sự phá vỡ âm thầm trước khi nó được phát hành?** Chương này vạch một lằn ranh cứng: thêm trường tùy chọn và điểm cuối mới là an toàn, trong khi xóa hoặc đổi tên trường, thay đổi kiểu, hoặc dùng lại ý nghĩa của một trường sẽ phá vỡ người dùng. Trong một đội lớn, người thực hiện thay đổi thường không thể thấy mọi người dùng, nên một chỉnh sửa "nhỏ" có thể âm thầm phá vỡ các đối tác mà bạn không bao giờ nói chuyện. Hãy mang tín hiệu cụ thể đến cuộc họp: bạn có chạy các kiểm tra tương thích hợp đồng tự động trong CI đối chiếu với đặc tả đã công bố không, hay dựa vào việc ai đó nhớ quy tắc. Trong bối cảnh doanh nghiệp và chính phủ, nơi một thay đổi phá vỡ buộc phải di chuyển phối hợp qua mọi đối tác và có thể kéo dài qua các thay đổi nhà cung cấp và chính quyền, chi phí tăng theo số lượng người dùng. Hãy quyết định các quy tắc phân loại và nối một cổng tương thích, để một thay đổi không tương thích làm hỏng bản dựng thay vì làm hỏng một tích hợp.

2. **Những nguyên thủy độ tin cậy nào, khóa lũy đẳng, phân trang và giới hạn tốc độ, là bắt buộc trên mọi điểm cuối mới ngay từ ngày đầu?** Chương này khăng khăng rằng đây là những mối quan tâm hạng nhất, vì việc bổ sung khóa lũy đẳng vào một điểm cuối tính phí đang chạy hoặc thêm phân trang vào một danh sách đã phát hành tự nó là một thay đổi phá vỡ. Một hệ sinh thái lớn khuếch đại điều này: một điểm cuối hoạt động trong kiểm thử sụp đổ dưới khối lượng dữ liệu thực, và một thao tác ghi không lũy đẳng biến một gián đoạn mạng thành các khoản phí trùng lặp. Hãy mang bằng chứng về những điểm cuối hiện tại nào thiếu các thứ này và một cơn bão thử lại sẽ gây ra điều gì. Hãy biến các mặc định thành không thể thương lượng cho điểm cuối mới: phân trang con trỏ trên mọi danh sách, khóa lũy đẳng trên mọi thao tác ghi, giới hạn tốc độ được lập tài liệu trả về trạng thái hiện tại của chúng. Điều đó biến một cuộc di chuyển bắt buộc trong tương lai thành một thói quen thiết kế một lần.

3. **Bạn có thực sự thiết kế và rà soát hợp đồng trước khi viết phần triển khai, hay giao diện rò rỉ ra từ mã?** Khuyến nghị API-trước yêu cầu một đặc tả đọc được bằng máy, được rà soát từ đầu, sinh ra tài liệu, khung mã và bản giả lập và cho phép người dùng tích hợp với bản giả lập trong lúc bạn xây dựng. Khi hợp đồng chạy sau phần triển khai, giao diện phơi bày cấu trúc cơ sở dữ liệu nội bộ và thay đổi mỗi khi phần triển khai thay đổi, đó là phản mẫu hàng đầu trong chương này. Tín hiệu cần xem xét: liệu một người dùng có thể bắt đầu tích hợp với bản giả lập của bạn ngay hôm nay, hay họ phải chờ một phần phụ trợ đang chạy. Với các API công khai và đối tác, nơi giao diện là bề mặt sản phẩm và là thứ đắt đỏ nhất khi làm sai, dành một ngày cho hợp đồng tiết kiệm được nhiều tuần xáo trộn hỗ trợ. Hãy biến việc rà soát hợp đồng thành một bước bắt buộc trước khi việc triển khai bắt đầu.

4. **Khi hai đội cần phơi bày cùng một năng lực, kiểu tương tác nào thắng, và ai có thẩm quyền nói không với giao thức thứ tư?** Chương này bảo bạn chọn REST, GraphQL, gRPC hay nhắn tin hướng sự kiện theo mức độ phù hợp với tương tác, nhưng ở quy mô lớn rủi ro thực sự là mỗi đội chọn sở thích riêng và người dùng đối mặt với một quy ước khác ở mỗi điểm cuối. Một tổ chức lớn trả giá cho sự phân mảnh đó bằng thư viện máy khách, cổng, giám sát, và tải nhận thức của mọi người tích hợp giờ phải học bốn thành ngữ thay vì một. Hãy mang bản kiểm kê các giao thức đã chạy trong môi trường thực, tương tác mà mỗi giao thức được chọn để phục vụ, và những người dùng trải qua nhiều hơn một giao thức. Cân nhắc đối lập là thực sự: một mặc định chung giảm sự tràn lan, nhưng một mệnh lệnh cứng nhắc buộc các vấn đề dạng gRPC vào một lỗ dạng REST. Hãy nêu tên cơ quan tiêu chuẩn hoặc hội đồng kiến trúc sở hữu quy trình ngoại lệ, vì trong các hệ thống doanh nghiệp và chính phủ, sự sinh sôi của các kiểu trở thành cái thuế vĩnh viễn lên tích hợp và là vấn đề khó đảo ngược một khi các đối tác phụ thuộc vào từng kiểu.

5. **Chính sách ngừng dùng được công bố của chúng ta là gì, và chúng ta có thể chứng minh mình thực sự tôn trọng khoảng thời gian hỗ trợ mà mình quảng bá không?** Chương này coi việc đánh phiên bản và ngừng dùng là kỷ luật: một chính sách bằng văn bản về các phiên bản cũ sống bao lâu, người dùng được thông báo ra sao, và họ được chồng lấp bao nhiêu để di chuyển. Một lời hứa mà bạn không thể thực thi còn tệ hơn không có, vì một hệ sinh thái lớn bao gồm những người dùng mà bạn không bao giờ nói chuyện, những người sẽ tiếp tục gọi một phiên bản đã ngừng cho đến khi nó hỏng trên môi trường thực. Hãy mang bằng chứng đến cuộc thảo luận: bạn đang mang bao nhiêu phiên bản đang sống, mức sử dụng thực tế trên mỗi phiên bản, bạn có thể thấy người dùng nào vẫn gọi một điểm cuối đã ngừng dùng không, và lần chấm dứt gần nhất của bạn được thông báo trước bao lâu. Áp lực đối lập là chi phí bảo trì so với sự ổn định của người dùng, và cả hai đều là thật. Với các đối tác doanh nghiệp theo mức dịch vụ hợp đồng và các API khu vực công phải tồn tại qua các chính quyền và thay đổi nhà cung cấp, khoảng thời gian hỗ trợ là một cam kết có thể tồn tại lâu hơn đội đã đưa ra nó, vì vậy hãy quyết định ai sở hữu nó và làm thế nào một lần chấm dứt được chứng minh là an toàn trước khi nó xảy ra.

6. **Làm sao chúng ta biết trải nghiệm nhà phát triển của mình tốt, hay chúng ta chỉ đang giả định điều đó vì API hoạt động với chúng ta?** Chương này đóng khung mỗi API như một sản phẩm mà mức độ chấp nhận phụ thuộc vào tài liệu tham chiếu chính xác, hướng dẫn bắt đầu nhanh, ví dụ, môi trường thử nghiệm, nhật ký thay đổi và một danh mục dễ tìm thấy. Các đội thường xuyên nhầm "API hoạt động" với "API dùng được", và khoảng trống hiện ra ở các phiếu hỗ trợ, các tích hợp thất bại, và những người dùng âm thầm bỏ cuộc. Hãy mang các tín hiệu đo được thay vì ý kiến: thời gian đến lần gọi thành công đầu tiên của một người tích hợp mới, khối lượng phiếu hỗ trợ cho mỗi điểm cuối, tài liệu đã công bố lỗi thời đến đâu so với hợp đồng thực, và liệu một người mới có thể tự phục vụ từ cổng thông tin mà không cần gửi email cho đội của bạn. Căng thẳng là tài liệu và cổng thông tin tốn công sức thực sự cạnh tranh với việc phát hành tính năng, nhưng trong một hệ sinh thái lớn, trải nghiệm nhà phát triển kém đẩy chi phí tích hợp lên hàng trăm người dùng cùng lúc. Trong chính phủ, nơi một API mở phục vụ các nhà phát triển bên ngoài mà bạn không thể điều phối và tính minh bạch thường được bắt buộc, một giao diện dùng được, có tài liệu tốt, dễ tìm thấy là một phần của nghĩa vụ giải trình trước công chúng, không phải điều dễ chịu thêm vào.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với hai hoặc ba kỹ sư và không có thời gian cho nghi thức, hãy giữ hợp đồng nhẹ nhưng có thật: một đặc tả đọc được bằng máy duy nhất mà các khách hàng đối tác thiết kế đầu tiên của bạn có thể tích hợp trong lúc bạn xây dựng. Chưa cần dựng cổng API, danh mục hay hội đồng quản trị, nhưng hãy khóa chặt hai thói quen đau đớn nếu thêm sau, khóa lũy đẳng trên thao tác ghi và phân trang con trỏ trên danh sách, vì bổ sung chúng vào một điểm cuối đang chạy là một thay đổi phá vỡ mà bạn không thể gánh. Ưu tiên một kiểu tương tác, hầu như luôn là REST, để bạn không mang sự tràn lan giao thức vào năm đầu tiên.

**Doanh nghiệp nhỏ.** Không có chuyên gia API riêng và ngân sách eo hẹp, hãy dựa vào các công cụ sinh tài liệu, bản giả lập và khung mã máy khách từ một đặc tả để một người đa năng có thể bảo trì giao diện mà không cần chuyên môn giao thức sâu. Hãy cân nhắc kỹ mua hay xây: một cổng có sẵn hoặc một nền tảng quản lý API cho bạn giới hạn tốc độ, khóa và cổng nhà phát triển mà bạn nếu không sẽ phải tự làm bằng tay. Giữ bề mặt nhỏ và các quy ước nhất quán, vì mỗi điểm cuối thêm và mỗi định dạng lỗi riêng lẻ là thứ mà một đội mỏng phải hỗ trợ mãi mãi.

**Doanh nghiệp lớn.** Qua nhiều đội tự chủ, vấn đề trung tâm là nhất quán mà không trở thành nút thắt: một hướng dẫn phong cách chung, một buổi rà soát tiêu chuẩn API, một danh mục giúp các giao diện dễ tìm thấy, và các kiểm tra tương thích ngược tự động trong CI để một sự phá vỡ âm thầm làm hỏng bản dựng thay vì một tích hợp. Hãy quản trị mỗi API như một sản phẩm với một chủ sở hữu được nêu tên, một vòng đời và một chính sách ngừng dùng được công bố, và đo mức độ chấp nhận, tải hỗ trợ và tần suất thay đổi phá vỡ để danh mục luôn khỏe mạnh. Hãy chuẩn hóa các kiểu tương tác và quy tắc phiên bản trong toàn tổ chức, vì ở quy mô này sự phân mảnh là mặc định đắt đỏ.

**Chính phủ.** Quy tắc mua sắm, yêu cầu tiêu chuẩn mở và trách nhiệm giải trình trước công chúng định hình mọi lựa chọn. Hãy công bố hợp đồng công khai, tuân theo các tiêu chuẩn mở được bắt buộc, và cung cấp một môi trường thử nghiệm và tài liệu tham chiếu để các nhà phát triển bên ngoài mà bạn không thể điều phối có thể tự phục vụ. Hãy coi khả năng tương thích ngược dài hạn là yêu cầu chính sách, vì các tích hợp phải tồn tại qua các chính quyền và thay đổi nhà cung cấp, và làm cho các thay đổi phá vỡ hiếm, được quản trị chặt chẽ và được thông báo từ rất sớm. Giữ API và tài liệu của nó đủ minh bạch để chịu được sự soi xét của công chúng và kiểm toán, và tránh các định dạng độc quyền có thể bẫy một chính quyền tương lai.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp giai đoạn hạt giống phát hành API công khai đầu tiên viết hợp đồng thành một đặc tả đọc được bằng máy trước khi lập trình, để hai khách hàng đối tác thiết kế của họ có thể tích hợp với một bản giả lập trong lúc phần phụ trợ vẫn đang được xây dựng. Ngay cả khi chỉ có một nhúm người dùng, họ thêm khóa lũy đẳng vào điểm cuối tính phí và phân trang con trỏ vào mọi danh sách, vì bổ sung chúng sau khi các đối tác phụ thuộc vào API sẽ là một thay đổi phá vỡ mà họ không thể gánh. Hợp đồng trả trước tốn một ngày và tiết kiệm nhiều tuần qua lại hỗ trợ.

**Doanh nghiệp lớn.** Một công ty thanh toán lớn phơi bày một API REST công khai cho hàng nghìn thương nhân. Mọi điểm cuối ghi chấp nhận một khóa lũy đẳng, nên việc thử lại do mạng không bao giờ tạo ra khoản phí trùng lặp. Mọi điểm cuối danh sách dùng phân trang con trỏ. Lỗi mang mã ổn định được lập tài liệu trong một tài liệu tham chiếu công khai. Một chính sách ngừng dùng chính thức đảm bảo một khoảng thời gian hỗ trợ dài cho bất kỳ phiên bản nào, kèm thông báo trước và hướng dẫn di chuyển. Kỷ luật này là lợi thế cạnh tranh: những người tích hợp tin rằng API sẽ không hỏng dưới chân họ.

**Chính phủ.** Một dịch vụ số quốc gia công bố một API mở cho dữ liệu công dân, tuân theo các tiêu chuẩn mở được bắt buộc và một quy trình thiết kế API-trước. Hợp đồng được đặc tả và rà soát trước khi xây dựng, được công bố trong một danh mục API chính phủ trung tâm, và được cung cấp cùng một môi trường thử nghiệm, để các nhà phát triển bên thứ ba, những người không thể được điều phối riêng lẻ, có thể tự tích hợp. Khả năng tương thích ngược dài hạn là yêu cầu chính sách, vì các tích hợp phải tồn tại qua các chính quyền và thay đổi nhà cung cấp. Vì vậy các thay đổi phá vỡ hiếm và được quản trị chặt chẽ.

## Luận chứng kinh doanh: động lực, ROI và TCO

Thiết kế API tốt giảm chi phí tích hợp, thường là chi phí lớn nhất trong việc kết nối các hệ thống và hội nhập đối tác. Với một API rõ ràng, ổn định, có tài liệu tốt, người dùng tích hợp trong vài ngày mà không cần một phiếu hỗ trợ nào. Một API tồi tạo ra tải hỗ trợ vô tận, các tích hợp thất bại và thiệt hại danh tiếng. Khi bản thân API là sản phẩm, trải nghiệm nhà phát triển trực tiếp thúc đẩy mức độ chấp nhận và doanh thu.

Chi phí ẩn lớn nhất là các thay đổi phá vỡ. Mỗi thay đổi phá vỡ buộc phải di chuyển phối hợp qua mọi người dùng, cả các đội nội bộ lẫn đối tác bên ngoài, và tổng chi phí tăng theo số lượng người dùng và mức độ khó khăn khi họ phải di chuyển đồng loạt. Đầu tư trả trước vào thiết kế dựa trên hợp đồng, khả năng tương thích ngược và kỷ luật phiên bản tránh được những sự kiện di chuyển đắt đỏ, toàn tổ chức này. Khi nói chuyện với ban lãnh đạo, hãy trình bày chất lượng API như điểm đòn bẩy cho sự tự chủ của đội, sự tăng trưởng hệ sinh thái đối tác và việc tránh các cuộc di chuyển bắt buộc tốn kém. Theo dõi thời gian tích hợp, khối lượng phiếu hỗ trợ và tần suất thay đổi phá vỡ làm bằng chứng của bạn.

## Phản mẫu và cạm bẫy

- **API triển khai-trước:** giao diện làm rò rỉ cấu trúc cơ sở dữ liệu nội bộ và thay đổi mỗi khi phần triển khai thay đổi.
- **Thay đổi phá vỡ âm thầm:** dùng lại một trường hoặc siết chặt xác thực mà không tăng phiên bản phá vỡ người dùng một cách khó đoán.
- **Giao diện lắm lời:** các thiết kế đòi hỏi nhiều vòng đi về cho một thao tác logic, làm hại hiệu năng và tính dùng được.
- **Quy ước không nhất quán:** mỗi điểm cuối tự phát minh cách đặt tên, định dạng lỗi và phân trang, nên máy khách không thể khái quát hóa.
- **Không phân trang hay giới hạn tốc độ:** các điểm cuối hoạt động trong kiểm thử và sụp đổ dưới khối lượng dữ liệu hoặc tải thực.
- **Thao tác ghi không lũy đẳng:** thử lại gây ra bản trùng lặp; một gián đoạn mạng đơn lẻ làm hỏng dữ liệu.
- **Sinh sôi phiên bản:** quá nhiều phiên bản đang sống mà không ngừng dùng, nhân lên chi phí bảo trì cho đến khi không quản lý nổi.
- **Tài liệu như chuyện nghĩ đến sau:** tài liệu tham chiếu không có hoặc lỗi thời đẩy toàn bộ chi phí tích hợp sang người dùng.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** API xuất hiện từ phần triển khai như một sản phẩm phụ; không có quy ước chung; giao diện làm rò rỉ cấu trúc cơ sở dữ liệu nội bộ; các thay đổi phá vỡ phổ biến, không được thông báo, và bị phát hiện khi tích hợp của một người dùng thất bại.
- **Mức 2, Phát triển:** Một số đội tuân theo các quy ước REST cơ bản, đánh phiên bản không chính thức và viết tài liệu bằng tay, nhưng thực hành không nhất quán giữa các đội; tính lũy đẳng, phân trang và giới hạn tốc độ xuất hiện ở một số điểm cuối mà không ở những điểm cuối khác; người dùng vẫn học những điều kỳ quặc của từng API theo từng trường hợp.
- **Mức 3, Chuẩn hóa:** Thiết kế hợp đồng-trước với đặc tả đọc được bằng máy được lập thành tài liệu và thực thi toàn tổ chức; một chính sách ngừng dùng được công bố, ngữ nghĩa lỗi nhất quán, và tính lũy đẳng, phân trang con trỏ cùng giới hạn tốc độ bắt buộc áp dụng cho mọi điểm cuối mới; một hướng dẫn phong cách chung và một buổi rà soát tiêu chuẩn API giữ các giao diện nhất quán giữa các đội.
- **Mức 4, Quản lý:** Danh mục API được đo lường và kiểm soát theo các đường cơ sở: các kiểm tra tương thích ngược tự động chặn mọi thay đổi trong CI, và bạn theo dõi thời gian đến lần gọi thành công đầu tiên, khối lượng phiếu hỗ trợ cho mỗi điểm cuối, tần suất thay đổi phá vỡ, số phiên bản đang sống và mức sử dụng từng điểm cuối để các quyết định ngừng dùng và thiết kế dựa trên bằng chứng thay vì ý kiến. Mỗi API là một sản phẩm được quản trị trong một danh mục với chủ sở hữu được nêu tên, và các chỉ số kích hoạt hành động khi một dịch vụ lệch khỏi mục tiêu.
- **Mức 5, Điều phối:** Chiến lược API được cải tiến liên tục và tích hợp trong toàn tổ chức; danh mục, cổng, quy tắc phiên bản và cổng tương thích hoạt động như một hệ thống; tổ chức thường xuyên loại bỏ, hợp nhất và điều chỉnh phạm vi các giao diện dựa trên mức chấp nhận và chi phí đo được; các tiêu chuẩn về kiểu tương tác và phiên bản thích ứng khi hệ sinh thái, đối tác và công nghệ dịch chuyển, và các thay đổi phá vỡ hiếm và được quản lý tốt.

## Ý tưởng để thảo luận

- Làm thế nào bạn quyết định khi nào một API nội bộ đủ ổn định để công bố ra bên ngoài?
- Khoảng thời gian hỗ trợ phù hợp cho các phiên bản đã ngừng dùng trong bối cảnh của bạn là bao nhiêu, và ai trả cho nó?
- GraphQL hay gRPC nên thay thế REST ở đâu trong nội bộ, và chúng sẽ thêm phức tạp hơn giá trị ở đâu?
- Làm thế nào bạn thực thi tính nhất quán của API qua nhiều đội tự chủ mà không trở thành nút thắt?
- API mà AI có thể sử dụng và giao diện công cụ cho tác tử nên thay đổi quy ước thiết kế của bạn như thế nào?
- Những kiểm tra tự động nào có thể bắt các thay đổi không tương thích ngược trước khi chúng được phát hành?

## Những điểm cần ghi nhớ

- Thiết kế hợp đồng trước; API là một sản phẩm và một lời hứa dài hạn.
- Khả năng tương thích ngược bảo vệ người dùng; các thay đổi phá vỡ cần phiên bản mới và con đường di chuyển.
- Chọn REST, GraphQL, gRPC hay sự kiện theo mức độ phù hợp với tương tác, không theo mốt.
- Xây dựng sẵn tính lũy đẳng, phân trang, giới hạn tốc độ và lỗi nhất quán từ ngày đầu.
- Quản trị API như sản phẩm với chủ sở hữu, danh mục và trải nghiệm nhà phát triển mạnh.

## Tài liệu tham khảo và đọc thêm

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (luận án)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* và *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- Đặc tả OpenAPI; JSON Schema (như các tiêu chuẩn tham chiếu)
- Martin Kleppmann, *Designing Data-Intensive Applications*
