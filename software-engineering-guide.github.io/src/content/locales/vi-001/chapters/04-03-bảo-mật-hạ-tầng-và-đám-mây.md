# 4.3 Bảo mật hạ tầng và đám mây

## Tổng quan và động lực

Ứng dụng chạy trên hạ tầng, và ngày nay hạ tầng đó phần lớn dựa trên đám mây, được định nghĩa bằng phần mềm và luôn thay đổi. Một kỹ sư đơn lẻ giờ có thể cung cấp một cơ sở dữ liệu, mở một đường mạng, hay cấp một quyền chỉ bằng một lệnh, ở quy mô và tốc độ mà kiểm soát thay đổi truyền thống chưa bao giờ lường trước. Quyền năng đó chính là lý do cấu hình sai, không phải các khai thác kỳ lạ, là nguyên nhân hàng đầu của các vụ xâm phạm đám mây. Một thùng lưu trữ vô tình công khai hay một vai trò truy cập quá rộng có thể phơi bày dữ liệu của cả tổ chức trong vài giây.

Với các doanh nghiệp lớn, hạ tầng đám mây trải qua nhiều nhà cung cấp, hàng nghìn tài khoản, và một hỗn hợp dịch vụ được quản lý, container và hàm serverless. Bề mặt tấn công không phải một chu vi tĩnh. Nó là một tập hợp sống động, lan rộng của tài nguyên và danh tính. Với chính phủ, cùng độ phức tạp đó gặp các chế độ cấp phép nghiêm ngặt, yêu cầu về nơi lưu trữ dữ liệu, và ranh giới phân loại định hình mọi lựa chọn kiến trúc. Ở cả hai, tầng danh tính đã trở thành chu vi mới: ai có thể làm gì, với tài nguyên nào, dưới điều kiện nào.

Chương này bao quát cách bảo mật nền móng đó: [quản lý danh tính và truy cập](https://en.wikipedia.org/wiki/Identity_management) (IAM), [phân đoạn mạng](https://en.wikipedia.org/wiki/Network_segmentation), [mã hóa](https://en.wikipedia.org/wiki/Encryption) và [quản lý khóa](https://en.wikipedia.org/wiki/Key_management), bảo mật của container và khối lượng công việc [serverless](https://en.wikipedia.org/wiki/Serverless_computing), và quản lý tư thế liên tục giữ cho một hệ sinh thái đám mây thay đổi nhanh không trôi vào nguy hiểm.

## Các nguyên tắc chính

- **Danh tính là chu vi.** Các quyết định truy cập dựa vào danh tính mạnh và cấp quyền mịn, không phải vị trí mạng.
- **Đặc quyền tối thiểu, luôn luôn.** Mọi danh tính, con người hay máy, nhận quyền tối thiểu cần thiết, không hơn.
- **Phân đoạn để khoanh vùng.** Chia mạng và khối lượng công việc để một sự xâm phạm ở một khu vực không thể lan tự do.
- **Mã hóa ở mọi nơi.** Bảo vệ dữ liệu khi truyền và khi lưu theo mặc định, với khóa được quản lý tốt.
- **Bất biến và khai báo.** Định nghĩa hạ tầng dưới dạng mã (IaC), triển khai bất biến, và coi sự trôi là khiếm khuyết.
- **Xác minh liên tục.** Tư thế không phải một cuộc kiểm toán một lần; hãy quét và thực thi liên tục.
- **Cấu hình an toàn theo mặc định.** Trạng thái mặc định của bất kỳ tài nguyên nào nên bị khóa chặt, không mở.

## Khuyến nghị

### Thiết kế quản lý danh tính và truy cập có chủ đích

IAM là phần quan trọng nhất của bảo mật đám mây, và là phần bị quản lý sai thường xuyên nhất.

- Dùng **[kiểm soát truy cập dựa trên vai trò](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** để cấp quyền theo chức năng công việc, và **[kiểm soát truy cập dựa trên thuộc tính](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** ở nơi cần các quyết định mịn hơn, nhận biết ngữ cảnh (dựa trên thẻ, môi trường, phân loại dữ liệu, hay thời gian).
- Loại bỏ thông tin xác thực tĩnh sống lâu, thay bằng token sống ngắn được cấp tự động và liên kết danh tính khối lượng công việc.
- Thực thi [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (xác thực đa yếu tố) cho mọi truy cập của con người và yêu cầu xác thực mạnh cho các hành động đặc quyền.
- Áp dụng đặc quyền tối thiểu một cách chặt chẽ: bắt đầu từ không và thêm quyền có chủ đích. Thường xuyên rà soát và tỉa bớt các quyền không dùng; quyền truy cập có xu hướng tích tụ.
- Tách biệt nhiệm vụ để không danh tính đơn lẻ nào có thể vừa thực hiện vừa phê duyệt các thay đổi nhạy cảm.
- Dùng tài khoản hoặc dự án riêng để tạo ranh giới cứng giữa các môi trường (sản xuất, thử nghiệm, phát triển) và giữa các đơn vị kinh doanh.

### Phân đoạn mạng và phân đoạn vi mô khối lượng công việc

Mạng phẳng cho kẻ tấn công đi ngang một khi đã vào bên trong. Hãy chia và khoanh vùng.

- Phân đoạn ở mức mạng thành các tầng và vùng, chỉ cho phép lưu lượng mà mỗi tầng chính đáng cần.
- Áp dụng **phân đoạn vi mô** để các khối lượng công việc riêng lẻ chỉ giao tiếp với những đối tác cụ thể chúng cần, được thực thi bằng chính sách nhận biết danh tính thay vì quy tắc mạng con rộng.
- Mặc định từ chối lưu lượng đông-tây; yêu cầu các quy tắc cho phép tường minh.
- Đặt các kho dữ liệu nhạy cảm trong mạng con riêng tư không tiếp xúc trực tiếp với internet, chỉ được với tới qua các đường được kiểm soát.
- Dùng kết nối riêng tới các dịch vụ được quản lý thay vì định tuyến qua internet công cộng ở nơi có thể.

### Mã hóa dữ liệu và quản lý khóa đúng cách

Mã hóa chỉ mạnh bằng việc quản lý khóa đằng sau nó.

- Mã hóa **khi truyền** bằng [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Bảo mật Tầng Vận chuyển) hiện hành ở mọi nơi, bao gồm lưu lượng dịch vụ-với-dịch vụ nội bộ.
- Mã hóa **khi lưu** theo mặc định cho mọi kho lưu trữ, cơ sở dữ liệu và bản sao lưu.
- Quản lý khóa bằng một **Dịch vụ Quản lý Khóa (KMS)**, và dùng **[Mô-đun Bảo mật Phần cứng](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** cho các khóa bảo đảm cao nhất và cho yêu cầu quy định.
- Xoay vòng khóa theo lịch và hỗ trợ xoay vòng nhanh khi nghi ngờ bị xâm phạm.
- Kiểm soát và kiểm toán ai có thể dùng và quản lý khóa tách biệt với ai có thể truy cập dữ liệu, để việc giữ khóa thực thi sự tách biệt nhiệm vụ.
- Cân nhắc khóa do khách hàng quản lý ở nơi quy định hoặc niềm tin hợp đồng yêu cầu tổ chức giữ khóa thay vì nhà cung cấp.

### Bảo mật container, Kubernetes và serverless

Mỗi mô hình tính toán mang rủi ro riêng.

- **Container:** dựng từ các ảnh nền tối giản, đáng tin; quét ảnh tìm lỗ hổng trước khi triển khai; chạy không phải root; làm hệ thống tệp chỉ đọc ở nơi có thể; và không bao giờ nướng bí mật vào ảnh.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** bật RBAC và giới hạn chặt tài khoản dịch vụ; áp dụng chính sách mạng cho phân đoạn vi mô; dùng bộ kiểm soát nhận vào và công cụ chính sách để thực thi tiêu chuẩn; hạn chế container đặc quyền; cô lập khối lượng công việc nhạy cảm; và giữ mặt phẳng điều khiển cùng các nút được vá.
- **Serverless:** áp dụng đặc quyền tối thiểu cho vai trò thực thi của từng hàm (một nguồn cấp quyền thừa phổ biến); xác thực mọi đầu vào sự kiện; quản lý bí mật qua kho bí mật của nền tảng; và giám sát các mẫu gọi bất thường.

Dù mô hình nào, hãy giữ môi trường chạy được vá và ảnh luôn mới. Một container chỉ an toàn bằng phần mềm bên trong nó.

### Quản lý tư thế bảo mật đám mây liên tục

Đám mây thay đổi quá nhanh để các cuộc kiểm toán thủ công định kỳ theo kịp.

- Áp dụng công cụ **Quản lý Tư thế Bảo mật Đám mây (CSPM)** để liên tục phát hiện cấu hình sai, phơi bày công khai và vi phạm chính sách qua các tài khoản.
- Định nghĩa chính sách bảo mật dưới dạng mã và thực thi nó lúc triển khai để các cấu hình xấu bị chặn trước khi chúng hạ cánh.
- Ưu tiên phòng ngừa (lan can ngăn cấu hình sai) hơn phát hiện (cảnh báo sau sự việc), và kết hợp cả hai.
- Duy trì một bản kiểm kê chính xác tài nguyên và danh tính; bạn không thể bảo mật những gì bạn không thấy.
- Theo dõi và khắc phục sự trôi giữa hạ tầng-dưới-dạng-mã đã khai báo và trạng thái đang chạy thực tế.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| RBAC | Đơn giản, dễ hiểu, dễ kiểm toán | Thô, bùng nổ vai trò ở quy mô lớn |
| ABAC | Mịn, nhận biết ngữ cảnh, mở rộng theo thẻ | Phức tạp để thiết kế và suy luận |
| Khóa do nhà cung cấp quản lý (KMS) | Dễ, tích hợp, gánh nặng vận hành thấp | Nhà cung cấp giữ khóa; ít kiểm soát hơn |
| Khóa do khách hàng quản lý/HSM | Kiểm soát toàn bộ, đáp ứng yêu cầu nghiêm ngặt | Chi phí vận hành, rủi ro mất khóa |
| Lan can phòng ngừa | Chặn cấu hình sai trước khi xảy ra | Có thể chặn công việc chính đáng, cần điều chỉnh |
| Chỉ CSPM phát hiện | Linh hoạt, không chặn | Thiệt hại có thể xảy ra trước khi phát hiện |
| Phân đoạn vi mô | Khoanh vùng di chuyển ngang mạnh | Độ phức tạp vận hành, chính sách lan tràn |

Đánh đổi chi phối là kiểm soát so với gánh nặng vận hành. Các biện pháp kiểm soát chặt hơn (khóa do khách hàng quản lý, phân đoạn vi mô nghiêm ngặt, ABAC) giảm rủi ro, nhưng chúng đòi hỏi chuyên môn và bảo trì mà các đội nhỏ khó duy trì. Mức đúng phụ thuộc vào độ nhạy cảm của dữ liệu và quy định nào áp dụng. Một cách tiếp cận thực dụng xếp tầng mặc định an toàn mạnh cho mọi người, rồi dành thêm sự chặt chẽ cho các hệ thống rủi ro cao nhất, và nó ưu tiên các lan can tự động khiến lựa chọn an toàn là mặc định thay vì một kỷ luật thủ công.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn sẽ vạch ranh giới tài khoản hay dự án cứng ở đâu, và cái gì thuộc về bên trong mỗi ranh giới?** Tài khoản và dự án riêng tạo ra sự khoanh vùng mạnh nhất mà đám mây cung cấp, để một sự xâm phạm trong phát triển không thể với tới sản xuất và một đơn vị kinh doanh không thể chạm vào dữ liệu của đơn vị khác. Hãy quyết định lược đồ ranh giới trước khi hệ sinh thái của bạn lớn đến hàng nghìn tài khoản, vì trang bị bổ sung cô lập lên một cấu trúc phẳng chậm và rủi ro. Với công việc doanh nghiệp và chính phủ, những ranh giới này cũng ánh xạ gọn với tách biệt môi trường, phân loại dữ liệu, và các giới hạn bán kính ảnh hưởng mà kiểm toán viên mong thấy. Hãy mang một sơ đồ hiện tại về khối lượng công việc nào chung tài khoản hôm nay và đánh dấu nơi một vai trò quá rộng đơn lẻ trải qua cả sản xuất và phi sản xuất. Nếu dữ liệu nhạy cảm nằm trong cùng tài khoản với khối lượng công việc thử nghiệm, đó là ranh giới cần sửa đầu tiên.

2. **Tiêu chuẩn của bạn về ai có thể quản lý khóa so với ai có thể truy cập dữ liệu được mã hóa là gì?** Mã hóa chỉ mạnh bằng quản lý khóa, và tách việc giữ khóa khỏi truy cập dữ liệu biến KMS của bạn thành một điểm thực thi cho tách biệt nhiệm vụ. Hãy quyết định ai có thể tạo, xoay vòng và dùng khóa, và bảo đảm tập đó không chồng lên những người có thể đọc dữ liệu mà các khóa đó bảo vệ. Với các hệ thống chịu quy định và chính phủ, điều này thường thúc đẩy lựa chọn giữa khóa do nhà cung cấp quản lý và khóa do khách hàng quản lý hay HSM, vốn mang nhiều kiểm soát hơn và nhiều rủi ro vận hành mất khóa hơn. Hãy mang các chính sách khóa hiện tại và kiểm tra xem có danh tính đơn lẻ nào vừa quản lý một khóa vừa đọc dữ liệu đằng sau nó không, vì đó là một khoảng trống im lặng phổ biến. Nếu việc giữ khóa và truy cập không được tách, mã hóa khi lưu đang bảo vệ bạn ít hơn bảng điều khiển gợi ý.

3. **Làm thế nào bạn sẽ khiến mặc định an toàn không thể tránh trong vùng hạ cánh của mình thay vì chỉ được khuyến nghị?** Cấu hình sai, không phải khai thác kỳ lạ, là nguyên nhân hàng đầu của xâm phạm đám mây, và cách sửa là lan can phòng ngừa chặn một cơ sở dữ liệu công khai hay thùng không mã hóa trước khi nó hạ cánh, không phải cảnh báo sau sự việc. Hãy quyết định chính sách nào bạn sẽ thực thi lúc triển khai (không lưu trữ công khai, mã hóa bật theo mặc định, thẻ bắt buộc) và cái nào bạn chỉ phát hiện và báo cáo. Với một đội lớn, mã hóa những điều này vào vùng hạ cánh và mẫu hạ tầng-dưới-dạng-mã nghĩa là mọi tài khoản mới thừa hưởng bảo vệ mà không cần công sức theo từng đội, biến bảo mật từ một khoản thuế lặp lại thành khoản đầu tư một lần. Hãy mang các phát hiện cấu hình sai tháng trước của bạn và hỏi cái nào một lan can phòng ngừa sẽ chặn hoàn toàn. Nếu quản lý tư thế của bạn chỉ phát hiện, thiệt hại có thể xảy ra trước khi ai thấy cảnh báo, vì vậy hãy chuyển các kiểm tra tác động cao nhất sang phòng ngừa.

4. **Làm thế nào bạn loại bỏ thông tin xác thực tĩnh sống lâu mà không làm hỏng tự động hóa lặng lẽ phụ thuộc vào chúng?** Khóa truy cập nhúng không bao giờ hết hạn là một trong những nguyên nhân phổ biến nhất của xâm phạm đám mây, vì một khóa bị rò rỉ đơn lẻ trong tập lệnh, nhật ký hay kho mã trao cho kẻ tấn công quyền truy cập bền vững. Lực kéo đối lập là vận hành: các công việc CI cũ, tác vụ cron và tích hợp bên thứ ba thường giả định một khóa tĩnh tồn tại, và chuyển chúng sang token sống ngắn hay liên kết danh tính khối lượng công việc tốn thời gian kỹ thuật mà không ai lập lịch. Với một đội lớn, một đường di chuyển dùng chung (cấp token tự động, đặt tiêu chuẩn hết hạn, và báo động trên bất kỳ khóa sống lâu mới nào) ngăn mỗi nhóm phát minh câu trả lời yếu hơn của riêng họ. Hãy mang bản kiểm kê mọi thông tin xác thực tĩnh đang dùng, tuổi của nó, bán kính ảnh hưởng, và liệu hệ thống nó nuôi có chấp nhận danh tính liên kết hôm nay không. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn hạn chót với chu kỳ kiểm toán và cấp phép, vì một thông tin xác thực sống lâu hơn người tạo ra nó chính xác là phát hiện làm đình trệ một sự cấp phép liên tục.

5. **Khi một tài nguyên bị cấu hình sai hoặc một khóa bị xâm phạm, bạn phát hiện, khoanh vùng và khắc phục nhanh đến đâu, và bạn đã đo điều đó chưa?** Một thùng công khai hay một vai trò quá rộng chỉ nguy hiểm bằng cửa sổ nó còn mở, nên thời gian trung bình để phát hiện và khắc phục là con số thực sự giới hạn mức phơi nhiễm của bạn. Căng thẳng là giữa lan can phòng ngừa chặn sai lầm lúc triển khai và quản lý tư thế phát hiện bắt những gì lọt qua, và bạn cần con số trung thực cho cả hai thay vì giả định an ủi rằng lan can bao quát mọi thứ. Hãy mang các phát hiện cấu hình sai và trôi quý trước của bạn với dấu thời gian, thời gian trung vị từ lúc đưa vào đến lúc khắc phục, và hồ sơ diễn tập cho một lần xoay vòng khi khóa bị xâm phạm. Với các hệ sinh thái doanh nghiệp và chính phủ trải qua hàng nghìn tài khoản, hãy thống nhất ai sở hữu việc khắc phục cho một phát hiện mà đội của không ai hiển nhiên sở hữu, vì một cảnh báo không có người phản hồi chịu trách nhiệm là một cảnh báo già đi thành sự cố.

6. **Làm thế nào bạn giữ tư thế bảo mật nhất quán qua nhiều đám mây, tài khoản và đội mà không làm mọi người chậm như rùa?** Các hệ sinh thái đa đám mây và đa tài khoản phân mảnh nhanh: mỗi nhà cung cấp có mô hình IAM, mặc định và công cụ tư thế riêng, nên một chính sách được thực thi ở một nơi lặng lẽ lỡ ở nơi khác. Đánh đổi là giữa kiểm soát trung tâm bảo đảm nhất quán và quyền tự chủ cục bộ cho phép các đội di chuyển nhanh, và nghiêng quá xa bên nào cũng hoặc làm nghẽn phân phối hoặc để tiêu chuẩn trôi. Hãy mang bản đồ độ bao phủ hiện tại của bạn: tài khoản nào thừa hưởng lan can vùng hạ cánh, cái nào không được quản lý, và nơi cùng một biện pháp kiểm soát được biểu đạt theo ba cách khác nhau qua các nhà cung cấp. Với một tổ chức lớn hoặc công, hãy thêm góc độ kiểm toán, vì kiểm toán viên mong một tiêu chuẩn có thể bảo vệ được áp dụng ở mọi nơi, và một biện pháp kiểm soát tồn tại ở đám mây chính nhưng không ở đám mây phụ là một khoảng trống mà một kẻ tấn công hay người đánh giá kiên trì sẽ tìm thấy đầu tiên.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ và sự sống còn thắng, nên hãy hoàn toàn dựa vào mặc định an toàn được phát hành miễn phí: mã hóa khi lưu bật, lưu trữ riêng tư trừ khi một người mở nó, MFA trên tài khoản gốc, và danh tính khối lượng công việc tích hợp sẵn của nhà cung cấp thay vì khóa truy cập dán vào. Đừng dựng một nền tảng CSPM hay tự làm phân đoạn vi mô mà bạn không thể bảo trì; một lan can đơn lẻ chặn một cơ sở dữ liệu mở ra internet mua phần lớn bảo vệ với công sức một buổi chiều. Hãy giữ mọi thứ trong hạ tầng-dưới-dạng-mã ngay từ đầu để việc gia cố mở rộng cùng bạn thay vì trở thành một lần viết lại sau này.

**Doanh nghiệp nhỏ.** Không có kỹ sư bảo mật riêng và ngân sách eo hẹp, hãy ưu tiên các dịch vụ được quản lý có mặc định đã gia cố và việc quản lý khóa được xử lý giúp bạn, thay vì tự xây kỷ luật KMS. Hãy coi bảo mật đám mây là câu hỏi vệ sinh cấu hình: biết thùng và cơ sở dữ liệu nào tồn tại, giữ chúng riêng tư, yêu cầu MFA, và bật các kiểm tra tư thế gốc của nhà cung cấp không tốn thêm phí. Khi bạn mua công cụ, hãy ưu tiên những cái đánh dấu phơi bày công khai và lưu trữ không mã hóa ngay từ đầu, vì hai sai lầm đó gây ra hầu hết các vụ xâm phạm có thể tránh được.

**Doanh nghiệp lớn.** Vấn đề thực sự là sự nhất quán qua hàng nghìn tài khoản và nhiều đội, nên công việc là công việc nền tảng: vùng hạ cánh cung cấp mọi tài khoản đã gia cố, lan can được thực thi dưới dạng chính sách-dưới-dạng-mã, và CSPM quét liên tục tìm sự trôi. Hãy chuẩn hóa mô hình IAM, quy tắc giữ khóa và đường cơ sở phân đoạn để các nhóm thôi phát minh lại phiên bản yếu hơn, và đo tư thế trên toàn hệ sinh thái thay vì tin lời từng đội. Hãy ngân sách công việc kỹ thuật liên tục để giữ chính sách hiện hành khi nhà cung cấp thêm dịch vụ và khi hệ sinh thái lớn lên.

**Chính phủ.** Quy tắc mua sắm, yêu cầu về nơi lưu trữ dữ liệu và chế độ cấp phép định hình mọi lựa chọn, nên các biện pháp kiểm soát bảo mật kiêm bằng chứng kiểm toán. Hãy ưu tiên quản lý khóa được xác nhận FIPS với việc giữ khóa tách biệt khỏi truy cập dữ liệu, các vùng cô lập giữ dữ liệu trong biên giới quốc gia, và ảnh container được ký, quét với kiểm soát nhận vào nghiêm ngặt. Hãy công bố các biện pháp bảo vệ bạn có thể, đưa quản lý tư thế liên tục trực tiếp vào sự cấp phép liên tục, và yêu cầu nhà cung cấp công khai mặc định cấu hình của họ và hỗ trợ các biện pháp kiểm soát phân đoạn và giữ khóa mà ranh giới phân loại của bạn đòi hỏi.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp nhỏ chạy mọi thứ trong một tài khoản đám mây và không thể bố trí đội nền tảng, nên dựa vào mặc định được phát hành an toàn: mã hóa khi lưu bật theo mặc định, thùng lưu trữ riêng tư trừ khi một người mở tường minh, và MFA bắt buộc trên tài khoản gốc. Thay vì khóa truy cập sống lâu dán vào CI, nó dùng danh tính khối lượng công việc tích hợp sẵn của nhà cung cấp để đường ống nhận thông tin xác thực sống ngắn tự động. Một lan can miễn phí đơn lẻ đánh dấu bất kỳ cơ sở dữ liệu nào mở ra internet cứu họ khỏi sai lầm đám mây phổ biến nhất và tốn kém nhất, với chi phí là một buổi chiều để thiết lập.

**Doanh nghiệp lớn.** Một công ty truyền thông chạy hàng nghìn tài khoản qua hai nhà cung cấp đám mây áp dụng một mẫu vùng hạ cánh: mọi tài khoản được cung cấp từ một mẫu với mã hóa khi lưu bật theo mặc định, không truy cập công khai vào lưu trữ, thẻ bắt buộc, và một đường cơ sở chính sách lan can. CSPM liên tục quét tìm sự trôi, và liên kết danh tính khối lượng công việc đã loại bỏ khóa sống lâu cho các hệ thống CI. Khi một nhà phát triển vô tình cố mở một cơ sở dữ liệu ra internet, một chính sách phòng ngừa chặn thay đổi và tự động tạo phiếu.

**Chính phủ.** Một cơ quan liên quan quốc phòng vận hành trong một vùng đám mây cô lập với nơi lưu trữ dữ liệu được thực thi bằng chính sách để không dữ liệu nào rời biên giới quốc gia. Các khóa nhạy cảm nhất sống trong HSM được xác nhận FIPS (Tiêu chuẩn Xử lý Thông tin Liên bang), với việc giữ khóa tách biệt khỏi truy cập dữ liệu để thực thi tách biệt nhiệm vụ. Các cụm Kubernetes dùng chính sách mạng nghiêm ngặt và kiểm soát nhận vào; mọi ảnh container được quét và ký trước khi được phép chạy. Quản lý tư thế liên tục nuôi trực tiếp bằng chứng cấp phép liên tục của cơ quan.

## Luận chứng kinh doanh: động lực, ROI và TCO

Bảo mật hạ tầng đám mây là nơi một khoản đầu tư nhỏ ngăn chặn các tổn thất thảm khốc, cỡ tiêu đề báo. Tổng chi phí sở hữu bao gồm công cụ CSPM, dịch vụ quản lý khóa, thời gian kỹ thuật để thiết kế IAM đặc quyền tối thiểu và phân đoạn, và công sức liên tục để giữ chính sách hiện hành. Những chi phí này là thật nhưng khiêm tốn. Chi phí của việc bỏ qua là một tài nguyên cấu hình sai đơn lẻ phơi bày cả cơ sở dữ liệu khách hàng, cùng với tiền phạt quy định, chi phí thông báo, và thiệt hại thương hiệu lâu dài theo sau. Các vụ xâm phạm do cấu hình sai đám mây nằm trong số các sự cố phổ biến nhất và có thể ngăn chặn nhất trong ngành.

Tự động hóa và tái sử dụng khuếch đại ROI. Hãy mã hóa mặc định an toàn vào vùng hạ cánh và mẫu hạ tầng-dưới-dạng-mã, và mọi tài khoản cùng khối lượng công việc mới thừa hưởng bảo vệ mà không cần công sức theo từng đội, biến bảo mật từ một khoản thuế thủ công lặp lại thành khoản đầu tư nền tảng một lần. Với chính phủ và doanh nghiệp chịu quy định, quản lý tư thế mạnh cũng hạ chi phí kiểm toán và cấp phép liên tục bằng cách tạo bằng chứng tự động. Khi bạn trình bày lập luận với ban lãnh đạo, hãy nhấn mạnh rằng tầng danh tính và cấu hình nay là vectơ xâm phạm chính, rằng cấu hình sai là có thể ngăn chặn, và rằng lan can cắt giảm cả rủi ro lẫn ma sát của rà soát thủ công.

## Phản mẫu và cạm bẫy

- **Quyền ký tự đại diện.** Cấp truy cập `*` rộng "để mọi thứ chạy được" và không bao giờ siết lại.
- **Khóa tĩnh sống lâu.** Khóa truy cập nhúng trong tập lệnh và CI không bao giờ hết hạn và cuối cùng rò rỉ.
- **Mạng phẳng.** Không phân đoạn, nên một máy chủ bị xâm phạm với tới mọi thứ.
- **Công khai do vô tình.** Lưu trữ và cơ sở dữ liệu bị phơi ra internet qua thiết lập mặc định hay cẩu thả.
- **Mã hóa không có kỷ luật khóa.** Bật mã hóa nhưng để quyền truy cập khóa mở rộng hoặc không bao giờ xoay vòng.
- **Bí mật nướng vào ảnh.** Thông tin xác thực nhúng trong ảnh container lan ra mọi nơi ảnh chạy.
- **Vai trò serverless cấp quyền thừa.** Các hàm được cấp nhiều hơn hẳn nhu cầu vì bỏ qua việc giới hạn phạm vi.
- **Tư thế chỉ kiểm toán.** Phát hiện cấu hình sai sau sự việc thay vì ngăn chúng lúc triển khai.
- **Bỏ qua sự trôi.** Để môi trường đang chạy phân kỳ khỏi hạ tầng-dưới-dạng-mã cho đến khi không ai biết trạng thái thực.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Cung cấp thủ công do ai cần tài nguyên thực hiện. Quyền ký tự đại diện rộng và khóa tĩnh sống lâu. Mạng phẳng không phân đoạn. Mã hóa áp dụng không nhất quán, nếu có. Không có quản lý tư thế; cấu hình sai chỉ hiện ra sau khi một sự cố buộc đặt câu hỏi.

**Mức 2: Phát triển.** Một số vai trò IAM và MFA xuất hiện, và mã hóa khi lưu được bật cho các kho chính, nhưng thực hành khác nhau theo đội. Các tầng mạng cơ bản tồn tại mà không mặc định từ chối. Rà soát cấu hình xảy ra định kỳ và thủ công. Hạ tầng được định nghĩa một phần dưới dạng mã, nên việc gia cố phụ thuộc vào nhóm nào đã cung cấp tài khoản.

**Mức 3: Chuẩn hóa.** RBAC và ABAC đặc quyền tối thiểu với thông tin xác thực sống ngắn được lập tài liệu và thực thi toàn tổ chức. Phân đoạn dùng mặc định từ chối đông-tây. Mã hóa khi truyền và khi lưu bật theo mặc định, với khóa trong KMS theo lịch xoay vòng và việc giữ khóa tách biệt khỏi truy cập dữ liệu. Gia cố container và Kubernetes là tiêu chuẩn, và CSPM chạy đối chiếu với chính sách xác định được áp dụng nhất quán qua mọi tài khoản.

**Mức 4: Quản lý.** Tư thế được đo, không phải giả định. Bạn theo dõi các chỉ số có tên so với đường cơ sở và mục tiêu: tỷ lệ danh tính trong đường cơ sở đặc quyền tối thiểu của chúng, thời gian trung bình để phát hiện và khắc phục cấu hình sai và sự trôi, độ bao phủ lan can và CSPM qua các tài khoản, tuân thủ xoay vòng khóa, và số thông tin xác thực sống lâu còn tồn tại. Phát hiện được phân loại theo bán kính ảnh hưởng, khắc phục có chủ sở hữu và mục tiêu mức dịch vụ, và dữ liệu xu hướng về những con số này dẫn dắt nơi nỗ lực gia cố kế tiếp đi.

**Mức 5: Điều phối.** Mặc định an toàn được dựng vào vùng hạ cánh và hạ tầng-dưới-dạng-mã để mọi tài nguyên sinh ra đã được gia cố, và các biện pháp kiểm soát thích ứng khi hệ sinh thái và bức tranh mối đe dọa dịch chuyển. Phân đoạn vi mô dùng chính sách nhận biết danh tính; khóa do khách hàng quản lý và HSM bảo vệ các hệ thống bảo đảm cao nhất với việc tách biệt giữ khóa. Lan can phòng ngừa chặn cấu hình sai lúc triển khai, sự trôi được tự động phát hiện và khắc phục, và bằng chứng tư thế nuôi sự cấp phép liên tục một cách tự động. Bảo mật được tích hợp với phân phối và hoạch định rủi ro, và tổ chức thường xuyên loại bỏ và điều chỉnh phạm vi biện pháp kiểm soát khi nhà cung cấp, dịch vụ và quy định thay đổi.

## Ý tưởng để thảo luận

1. ABAC đáng với độ phức tạp của nó ở đâu so với việc giữ RBAC trong môi trường của bạn?
2. Làm sao bạn loại bỏ thông tin xác thực sống lâu mà không làm hỏng tự động hóa cũ?
3. Sự phân chia đúng giữa lan can phòng ngừa và quản lý tư thế phát hiện là gì?
4. Hệ thống nào biện minh cho khóa do khách hàng quản lý hay HSM xét chi phí vận hành của chúng?
5. Làm sao bạn giữ các quyền đặc quyền tối thiểu không lặng lẽ tích tụ trở lại thành đặc quyền thừa?
6. Độ phức tạp đa đám mây nên thay đổi cách tiếp cận của bạn về tư thế và chính sách nhất quán thế nào?

## Những điểm cần ghi nhớ

- Danh tính là chu vi mới; hãy đầu tư vào IAM đặc quyền tối thiểu với thông tin xác thực sống ngắn.
- Phân đoạn mạng và phân đoạn vi mô khối lượng công việc để khoanh vùng sự xâm phạm.
- Mã hóa khi truyền và khi lưu theo mặc định, và quản lý khóa bằng KMS/HSM với tách biệt việc giữ khóa.
- Gia cố container, Kubernetes và serverless; giữ môi trường chạy và ảnh được vá.
- Ưu tiên lan can phòng ngừa hơn phát hiện sau sự việc, và quản lý tư thế liên tục.
- Dựng mặc định an toàn vào vùng hạ cánh và hạ tầng-dưới-dạng-mã để bảo vệ mở rộng tự động.
- Cấu hình sai, không phải khai thác kỳ lạ, là nguyên nhân hàng đầu của xâm phạm đám mây, và nó có thể ngăn chặn.

## Tài liệu tham khảo và đọc thêm

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Centre for Internet Security, *CIS Benchmarks* (các nhà cung cấp đám mây, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* và *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini và những người khác, tài liệu kỹ thuật *Cloud security posture and detection*
- Các trụ cột bảo mật Well-Architected của nhà cung cấp (như hướng dẫn kiến trúc trung lập nhà cung cấp)
