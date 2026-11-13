# 8.7 Hệ thống xây dựng và quản lý artifact

## Tổng quan và động lực

Bản dựng là nơi mã nguồn của bạn trở thành thứ bạn có thể phát hành. Mọi đường ống trong chương 8.1 bắt đầu từ đây: trước khi bạn có thể kiểm thử, quét, triển khai hay thăng cấp bất cứ thứ gì, một hệ thống xây dựng phải biến một cây tệp nguồn thành một artifact cụ thể, một tệp nhị phân đã biên dịch, một gói, một ảnh container, hay một bó tài sản tĩnh. Nếu bước đầu tiên đó chậm, chập chờn hay không tái lập được, mọi bước sau thừa hưởng thiệt hại. Một bản dựng tạo ra đầu ra khác nhau trên hai máy làm suy yếu mọi kiểm thử bạn chạy và mọi phê duyệt bạn thu thập, vì thứ bạn thẩm định không chứng minh được là thứ bạn phát hành.

Chương này nói về bước đầu tiên đó và đầu ra của nó: hệ thống xây dựng tạo artifact, và quản lý artifact lưu trữ, đánh phiên bản, bảo mật và thăng cấp chúng. Nó cố ý hẹp hơn chương 8.1, vốn bao quát toàn bộ đường ống tích hợp liên tục và phân phối liên tục (CI/CD). Ở đây chủ đề là bản dựng và các artifact nó phát ra. Nó bổ sung cho chương 2.10 về quản lý cấu hình phần mềm, chi phối cách bạn theo dõi và kiểm soát đầu vào, và chương 2.18 về quản lý phụ thuộc và chuỗi cung ứng, chi phối mã bên thứ ba bạn kéo vào. Bản dựng là nơi các đầu vào đó gặp nhau: mã nguồn, phụ thuộc và cấu hình của bạn đều hội tụ thành một đầu ra bất biến.

Với các đội lớn, rủi ro là cụ thể. Khi hàng trăm kỹ sư chờ các bản dựng nhiều phút nhiều lần một ngày, tổng thời gian mất vượt xa gần như mọi chi phí kỹ thuật khác. Khi artifact khả biến, không được theo dõi, hoặc được dựng lại theo từng môi trường, bạn mất khả năng nói chắc chắn cái gì đang chạy trong môi trường sản xuất. Trong bối cảnh doanh nghiệp và chính phủ, khả năng truy vết đó không tùy chọn. Kiểm toán viên và cán bộ bảo mật cần bằng chứng rằng tệp nhị phân trong môi trường sản xuất đến từ mã nguồn đã rà soát, được dựng bởi hệ thống đáng tin, với chuỗi lưu giữ được ghi lại. Một thực hành xây dựng và artifact có kỷ luật biến bằng chứng đó thành sản phẩm phụ của công việc bình thường thay vì cuộc chạy vạy trước mỗi kiểm toán.

## Các nguyên tắc chính

- Bản dựng là bước đầu của phân phối: coi tốc độ và tính đúng của nó là mối quan tâm sản xuất.
- Hướng tới bản dựng tái lập được và, nơi khả thi, kín (hermetic): cùng đầu vào, cùng đầu ra, mọi lúc.
- Dựng một artifact một lần, rồi thăng cấp đúng artifact đó qua các môi trường.
- Làm artifact bất biến và định địa chỉ theo nội dung, và đánh phiên bản có ý nghĩa.
- Lưu artifact trong một kho được quản lý với lưu giữ, kiểm soát truy cập và nguồn gốc.
- Lưu đệm tích cực, nhưng coi bộ nhớ đệm là ranh giới bảo mật, không chỉ mánh tốc độ.
- Nắm bắt nguồn gốc, chữ ký và danh mục vật liệu lúc dựng, không phải sau sự việc.

## Khuyến nghị

### Coi bản dựng là bước đầu của phân phối

Hệ thống xây dựng của bạn là hạ tầng sản xuất, và bạn nên tài trợ và bảo trì nó như vậy. Việc xây artifact nhanh, đúng là nền móng mà CI/CD (chương 8.1) dựa trên. Khi các đội coi bản dựng là chuyện nghĩ sau, một đống tập lệnh shell không ai sở hữu, họ trả giá bằng đường ống chập chờn, lỗi "chạy được trên máy tôi" bí ẩn, và phản hồi chậm xói mòn toàn bộ luồng kỹ thuật mô tả trong Phần 11. Hãy giao cho bản dựng một chủ sở hữu, một định nghĩa được giữ trong quản lý phiên bản cạnh mã (chương 2.14 về cấu trúc kho), và cùng kỷ luật rà soát như bất kỳ hệ thống trọng yếu nào khác.

### Làm bản dựng tái lập được và, nơi bạn có thể, kín

Một [bản dựng tái lập được](https://en.wikipedia.org/wiki/Reproducible_builds) tạo ra đầu ra giống hệt từng bit từ cùng mã nguồn, để bất kỳ ai cũng dựng lại độc lập và xác minh một artifact khớp với nguồn của nó. Đây là thuộc tính cho phép bạn tin rằng một tệp nhị phân không bị can thiệp giữa commit và triển khai. Đạt được nó nghĩa là loại bỏ các nguồn bất định: dấu thời gian nhúng, đường dẫn tệp tuyệt đối, ngẫu nhiên thứ tự dựng, và lệnh tải qua mạng có kết quả trôi theo thời gian.

Một bản dựng kín đi xa hơn bằng cách khai báo mọi đầu vào từ trước và chạy trong môi trường cô lập không với tới mạng hay trạng thái môi trường của máy chủ. Không gì đi vào bản dựng ngoài những gì bạn khai báo: phiên bản toolchain được ghim, phụ thuộc được ghim, tệp nguồn tường minh. Tính kín là thứ làm khả năng tái lập đáng tin thay vì may mắn. Tính kín hoàn toàn có chi phí thật về công cụ và kỷ luật, nên hãy coi nó là một hướng đi hơn là nhị phân. Ngay cả tiến bộ một phần, ghim phiên bản trình biên dịch, vendor hoặc khóa phụ thuộc, lột dấu thời gian, mua cho bạn phần lớn lòng tin với một phần nhỏ công sức.

### Phân giải phụ thuộc tất định bằng lockfile

Mọi bản dựng kéo vào mã bên thứ ba, và cách bạn phân giải nó quyết định bản dựng của bạn có tất định không. Một [lockfile](https://en.wikipedia.org/wiki/Lock_file) ghi lại phiên bản được phân giải chính xác và băm mật mã của mọi phụ thuộc trực tiếp và bắc cầu, để một bản dựng nhiều tháng sau phân giải ra đúng cùng đồ thị. Hãy commit lockfile, coi thay đổi của nó là sự kiện rà soát được, và xác minh băm ở mỗi lần tải để một gói thượng nguồn bị biến đổi không lọt qua mà không bị chú ý. Đây là mặt thời gian dựng của kỷ luật chuỗi cung ứng trong chương 2.18. Không có lockfile, "hôm qua nó dựng được" không cho bạn biết gì về cái nó sẽ dựng hôm nay, vì một khoảng phiên bản nổi có thể lặng lẽ kéo bản phát hành mới, hoặc kẻ tấn công có thể xuất bản một bản độc hại.

### Dùng bản dựng gia tăng và bộ nhớ đệm, cục bộ và từ xa

Không ai nên dựng lại thứ chưa thay đổi. Bản dựng gia tăng theo dõi đầu vào nào nuôi đầu ra nào và chỉ dựng lại các phần bị thay đổi ảnh hưởng. Một bộ nhớ đệm bản dựng lưu đầu ra của công việc trước, khóa theo băm của đầu vào, để một đích chưa đổi được lấy ra thay vì tính lại. Bộ nhớ đệm cục bộ tăng tốc vòng lặp của một lập trình viên; bộ nhớ đệm bản dựng từ xa hoặc phân tán chia sẻ kết quả qua cả đội và đội CI, để người đầu tiên dựng một đầu vào cho trước trả chi phí và mọi người khác nhận một lần trúng đệm. Trên một monorepo lớn đây là sự khác biệt giữa bản dựng mười phút và mười giây.

Lợi ích là tốc độ phản hồi của lập trình viên, một trong những khoản đầu tư đòn bẩy cao nhất bạn có thể làm. Phản hồi nhanh, đúng giữ kỹ sư trong dòng chảy và rút ngắn vòng lặp giữa viết mã và biết nó hoạt động không. Dù vậy hãy bảo vệ tính đúng của bộ nhớ đệm cẩn thận: một khóa đệm bỏ sót một đầu vào thật (một biến môi trường, một phiên bản công cụ) tạo ra kết quả cũ gây điên đầu khi gỡ lỗi. Bộ nhớ đệm chỉ đáng tin bằng mức đầy đủ của việc băm đầu vào của nó.

### Chọn công cụ xây dựng khớp với quy mô của bạn

Công cụ xây dựng nằm trên một phổ. Ở đầu nhẹ, [Make](https://en.wikipedia.org/wiki/Make_(software)) và công cụ gốc ngôn ngữ mô hình hóa một đồ thị phụ thuộc đơn giản và đủ cho một dịch vụ đơn hoặc kho nhỏ. Ở giữa, công cụ hệ sinh thái như Gradle và Maven cho thế giới Java, hay toolchain chuẩn cho Go, Rust và JavaScript, thêm phân giải phụ thuộc và quy ước. Ở đầu nặng, các hệ thống dựa trên đồ thị như [Bazel](https://en.wikipedia.org/wiki/Bazel_(software)) và công cụ xây monorepo tương tự mô hình hóa toàn bộ bản dựng như một [đồ thị có hướng không chu trình](https://en.wikipedia.org/wiki/Directed_acyclic_graph) kín, chi tiết của các đích, cho phép tính gia tăng chính xác, bộ nhớ đệm từ xa và thực thi từ xa qua một cơ sở mã lớn.

Công cụ nặng hơn sinh lời khi bạn có nhiều dự án phụ thuộc nhau, một monorepo lớn (chương 2.14), hoặc thời gian dựng bóp nghẹt các đội. Nó tốn khoản đầu tư thật: đường cong học dốc hơn, công sức di chuyển, và một đội chuyên trách bảo trì định nghĩa bản dựng. Đừng áp dụng công cụ tầm Bazel vì nó thời thượng. Hãy áp dụng khi đồ thị dựng của bạn đủ lớn để việc lưu đệm chi tiết và song song thu hồi nhiều thời gian kỹ thuật hơn chi phí chạy công cụ. Với hầu hết hệ thống nhỏ và vừa, một công cụ hệ sinh thái tốt với bộ nhớ đệm từ xa là điểm ngọt.

### Lưu artifact trong một kho được quản lý

Một khi bạn đã dựng artifact, nó cần một ngôi nhà. Một [kho artifact](https://en.wikipedia.org/wiki/Software_repository) (còn gọi là registry) lưu gói, ảnh container và tệp nhị phân của bạn với đánh phiên bản, kiểm soát truy cập và siêu dữ liệu. Nó là đối tác của kho mã nguồn: nguồn vào, artifact ra, cả hai được quản lý. Một kho tốt cho bạn một nơi đáng tin duy nhất để xuất bản và lấy artifact nội bộ, ủy quyền và lưu đệm artifact bên ngoài để bạn không với ra internet công cộng ở mỗi bản dựng, và ghi lại ai đã xuất bản gì và khi nào. Ảnh container có quy ước registry riêng, và các kiểu gói khác có quy ước của chúng, nhưng kỷ luật là như nhau: không gì chạy trong môi trường sản xuất mà không đến từ một kho được quản lý, kiểm soát truy cập.

### Đánh phiên bản artifact và làm chúng bất biến, định địa chỉ theo nội dung

Hãy cho mỗi artifact một phiên bản có ý nghĩa. [Đánh phiên bản ngữ nghĩa](https://en.wikipedia.org/wiki/Software_versioning) (major.minor.patch) truyền đạt bản chất của một thay đổi cho người tiêu dùng: tăng major báo hiệu thay đổi phá vỡ, minor thêm tính năng tương thích, patch sửa lỗi. Cạnh phiên bản đọc được bởi con người, hãy định danh mỗi artifact bằng băm mật mã của nội dung, để nó được định địa chỉ theo nội dung. Một địa chỉ nội dung, thường gọi là digest, là dấu vân tay đổi nếu một byte đổi, cho phép bạn tham chiếu đúng một artifact không mơ hồ và phát hiện mọi sự can thiệp.

Hãy làm artifact đã xuất bản bất biến: một khi phiên bản được xuất bản, nó không bao giờ đổi. Xuất bản lại các byte khác dưới cùng phiên bản là mối nguy chuỗi cung ứng và cơn ác mộng gỡ lỗi, vì hai người có thể giữ "phiên bản 1.4.2" và có phần mềm khác nhau. Thẻ khả biến như "latest" tiện cho con người nhưng, với bất cứ thứ gì quan trọng, phải luôn phân giải về một digest bất biến cụ thể mà bạn ghi lại. Hãy triển khai theo digest, không theo thẻ nổi, để thứ bạn đã kiểm thử chứng minh được là thứ bạn chạy.

### Dựng một lần, thăng cấp khắp nơi

Hãy dựng một artifact một lần, rồi di chuyển đúng artifact đó qua các môi trường: phát triển, staging, sản xuất. Quy tắc "dựng một lần, thăng cấp khắp nơi" này là thực hành quản lý artifact quan trọng nhất đơn lẻ. Nếu bạn dựng lại theo môi trường, bạn đã vứt bỏ bảo đảm rằng artifact đã kiểm thử là artifact đã triển khai, vì mỗi lần dựng lại có thể kéo một phụ thuộc khác hoặc chạy trên một máy hơi khác. Thăng cấp là một thao tác siêu dữ liệu: bạn đánh dấu một digest đã dựng, đã kiểm thử là được duyệt cho môi trường kế tiếp, và bạn cấu hình nó cho môi trường đó qua cấu hình đặt ngoài (chương 2.10) thay vì dựng lại. Điều này giữ tệp nhị phân không đổi và cấu hình biến đổi, chính xác sự tách biệt bạn muốn cho cả độ tin cậy lẫn khả năng kiểm toán.

### Nắm bắt nguồn gốc, ký artifact và tạo SBOM

Lúc dựng, hãy ghi lại artifact đến từ đâu và chứng minh nó chưa bị thay đổi. Nguồn gốc là tuyên bố có chữ ký về cách một artifact được dựng: commit nguồn nào, bộ dựng nào, đầu vào nào. Ký một artifact cho phép người tiêu dùng xác minh tính xác thực và toàn vẹn trước khi chạy nó, và xác minh chữ ký lúc triển khai khép vòng. Một [danh mục vật liệu phần mềm](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM), bản kiểm kê đầy đủ các thành phần và phụ thuộc bên trong một artifact, cho phép bạn trả lời "chúng ta có bị ảnh hưởng không?" trong vài phút khi một lỗ hổng mới được công bố, thay vì dành nhiều ngày lục tìm nhật ký dựng.

Các khung như SLSA (Supply-chain Levels for Software Artifacts) cho bạn một mô hình phân bậc cho tính toàn vẹn thời gian dựng: các bậc cao hơn đòi bản dựng kín, cô lập và nguồn gốc không giả mạo được. Hãy tạo tất cả điều này trong bản dựng, nơi thông tin có thẩm quyền và rẻ để thu thập, không phải dựng lại sau đó khi nó đắt và không đáng tin. Công việc này phục vụ trực tiếp vòng đời phát triển phần mềm an toàn của chương 4.9 và các mối quan tâm chuỗi cung ứng của chương 2.18.

### Bảo mật bộ nhớ đệm và quản lý lưu giữ cùng chi phí

Một bộ nhớ đệm bản dựng dùng chung là một ranh giới tin cậy dùng chung. Nếu kẻ tấn công ghi được một mục bị đầu độc, mọi người tiêu dùng lấy nó chạy mã bị xâm phạm, và lợi thế tốc độ thành bề mặt tấn công. Hãy bảo vệ bộ nhớ đệm bằng xác thực, giới hạn quyền ghi hẹp (thường chỉ CI đáng tin, không bao giờ laptop lập trình viên), và bảo đảm khóa đệm băm mọi đầu vào thật để một mục bị đầu độc hay cũ không giả làm hợp pháp. Hãy coi đầu độc bộ nhớ đệm là mô hình mối đe dọa thật, đặc biệt với bộ nhớ đệm từ xa dùng chung qua các đội.

Artifact cũng tích tụ chi phí. Ảnh container và đầu ra bản dựng lớn, và một registry không giới hạn lớn lên cho đến khi hóa đơn lưu trữ và tra cứu chậm buộc vấn đề. Hãy xác định chính sách lưu giữ: giữ mọi artifact đã thăng cấp lên sản xuất và mọi thứ được hệ thống đang chạy tham chiếu, tự động cho hết hạn các bản dựng phát triển và pull request cũ, và ghi lại những gì bạn đã xóa. Mục tiêu là một kho giữ những gì bạn cần cho khả năng tái lập và kiểm toán trong khi bỏ bớt nhiễu, ở mức chi phí bạn chọn có ý thức thay vì cái làm bạn bất ngờ.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Công cụ dựng đồ thị nặng (tầm Bazel) | Gia tăng chi tiết, bộ nhớ đệm và thực thi từ xa, mở rộng đến monorepo khổng lồ | Đường cong học dốc, chi phí di chuyển, cần đội dựng chuyên trách |
| Công cụ dựng nhẹ (Make, gốc) | Đơn giản, chi phí chung thấp, áp dụng nhanh | Gia tăng và lưu đệm kém ở quy mô, tính kín yếu |
| Bộ nhớ đệm bản dựng từ xa/phân tán | Kết quả chia sẻ, tăng tốc mạnh qua cả đội | Bề mặt đầu độc bộ nhớ đệm, tính đúng phụ thuộc băm đầu vào đầy đủ |
| Bản dựng kín hoàn toàn | Khả năng tái lập đáng tin, nguồn gốc mạnh | Chi phí công cụ và kỷ luật thật, quy trình cục bộ khó hơn |
| Dựng một lần, thăng cấp khắp nơi | Artifact đã kiểm thử bằng artifact đã phát hành, dấu vết kiểm toán sạch | Đòi cấu hình đặt ngoài và thăng cấp có kỷ luật |
| Artifact bất biến, định địa chỉ theo nội dung | Chống giả mạo, tham chiếu không mơ hồ | Kém tiện hơn thẻ nổi, nhiều lưu trữ hơn để quản lý |
| Lưu giữ artifact dài | Khả năng tái lập đầy đủ và lịch sử kiểm toán | Chi phí lưu trữ, tra cứu chậm hơn nếu không có chính sách dọn |

Căng thẳng lặp lại là giữa tốc độ và lòng tin. Bộ nhớ đệm, đội dựng dùng chung và thẻ nổi đều làm bản dựng nhanh hơn và tiện hơn, và mỗi cái, dùng cẩu thả, làm yếu khả năng nói chính xác bạn đã dựng gì và chứng minh nó không bị can thiệp. Hãy giải quyết bằng cách biến con đường đáng tin thành con đường nhanh. Một băm đầu vào đầy đủ làm bộ nhớ đệm vừa nhanh vừa đúng. Triển khai theo digest nhanh như triển khai theo thẻ và an toàn hơn nhiều. Tạo SBOM trong bản dựng tốn vài giây và tiết kiệm nhiều ngày. Bạn hiếm khi phải chọn tốc độ thay vì tính toàn vẹn nếu bạn thiết kế tính toàn vẹn vào con đường nhanh ngay từ đầu.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta có thể dựng lại artifact sản xuất quý trước hôm nay và nhận cùng các byte không, và nếu không, thiếu gì?** Đây là phép thử sắc nhất về kỷ luật xây dựng của bạn, vì khả năng tái lập phụ thuộc vào toolchain được ghim, phụ thuộc được khóa và bất định được loại bỏ cùng hoạt động. Hãy chọn một artifact cụ thể đã phát hành vài tháng trước và thực sự thử dựng lại nó từ commit nguồn đã ghi. Những gì bạn học từ nỗ lực đó đáng giá hơn bất kỳ tài liệu chính sách nào: có thể một khoảng phụ thuộc đã nổi, có thể phiên bản trình biên dịch chưa bao giờ được ghim, có thể một dấu thời gian bị nhúng. Các khoảng trống bạn tìm thấy là tồn đọng tái lập của bạn, và đóng chúng là thứ cho phép bạn tin rằng thứ bạn kiểm toán là thứ bạn chạy, điều quan trọng cực kỳ trong bối cảnh chịu quy định và chính phủ nơi chuỗi lưu giữ đó là yêu cầu pháp lý.

2. **Chúng ta dựng mỗi artifact một lần và thăng cấp nó, hay dựng lại theo môi trường, và làm sao chúng ta chứng minh cái nào?** Nhiều đội tin rằng họ thăng cấp một artifact duy nhất nhưng phát hiện, khi nhìn kỹ, rằng staging và môi trường sản xuất mỗi nơi kích hoạt một bản dựng mới với đầu vào hơi khác. Hãy truy một bản phát hành thật từ commit đến môi trường sản xuất và xác nhận liệu đúng cùng digest đã di chuyển qua mọi môi trường hay byte mới đã được tạo ra giữa đường. Nếu bạn thấy dựng lại, bạn đã tìm thấy nơi bảo đảm kiểm thử của bạn yếu hơn bạn nghĩ, vì artifact đã kiểm thử và artifact đã triển khai không chứng minh được là giống hệt. Cách sửa, đặt cấu hình ra ngoài để tệp nhị phân giữ không đổi trong khi thiết lập thay đổi, sinh lời ở cả độ tin cậy lẫn một câu chuyện kiểm toán sạch hơn nhiều.

3. **Nếu một lỗ hổng nghiêm trọng được công bố trong một thư viện phổ biến ngày mai, chúng ta liệt kê nhanh đến đâu mọi artifact chứa nó?** Câu hỏi này kiểm tra liệu thực hành nguồn gốc và SBOM thời gian dựng của bạn là thật hay khát vọng. Khi một thành phần được dùng rộng rãi hóa ra khai thác được, các tổ chức phục hồi trong vài giờ là những tổ chức tạo danh mục vật liệu lúc dựng và lưu nó cùng mỗi artifact; những tổ chức phục hồi trong vài tuần đang grep nhật ký dựng và phỏng vấn kỹ sư. Hãy đi qua kịch bản một cách cụ thể với một thư viện bạn thực sự phụ thuộc và đo thời gian câu trả lời mất hôm nay. Khoảng cách giữa thời gian đó và "vài phút" là thước đo trực tiếp phơi nhiễm chuỗi cung ứng của bạn, và nó nối thẳng với công việc vòng đời phát triển an toàn trong chương 4.9.

4. **Bản dựng của chúng ta tốn bao nhiêu thời gian kỹ thuật mỗi ngày, và lập luận kinh doanh để làm chúng nhanh hơn là gì?** Độ trễ bản dựng là khoản thuế trả ở mọi thay đổi bởi mọi kỹ sư, và ở quy mô một đội lớn tổng số dễ bị đánh giá thấp vì không lần chờ đơn lẻ nào cảm thấy đắt. Thống nhất đo nó biến một lời phàn nàn mơ hồ thành con số bạn cân nhắc với chi phí của bộ nhớ đệm từ xa, tính gia tăng tốt hơn, hay công cụ dựng nặng hơn. Hãy mang thời gian dựng cục bộ và CI trung vị và tệ nhất, số bản dựng mỗi ngày, và ước tính trung thực một bản dựng chậm đẩy ai đó ra khỏi dòng chảy vào chuyển ngữ cảnh bao lâu một lần. Cân nhắc đối lập là bản dựng nhanh hơn không miễn phí: bộ nhớ đệm từ xa và thực thi phân tán thêm hạ tầng để chạy và bảo mật, và công cụ nặng hơn thêm một đội bảo trì. Với một tổ chức doanh nghiệp hay chính phủ, hãy tính chi phí thông lượng và tinh thần của phản hồi chậm qua nhiều đội, thường lấn át hóa đơn hạ tầng và chính là cách đóng khung mà ban lãnh đạo đã tài trợ.

5. **Ai ghi được vào bộ nhớ đệm bản dựng dùng chung của chúng ta, và cái gì ngăn một mục bị đầu độc đến môi trường sản xuất?** Một bộ nhớ đệm dùng chung đánh đổi chiến thắng tốc độ lấy một ranh giới tin cậy mới, và cùng cơ chế cho kết quả của một kỹ sư phục vụ cả đội cũng cho một mục bị hỏng hoặc độc hại xâm phạm mọi người lấy nó. Với một đội lớn bán kính ảnh hưởng là cả tổ chức, nên điều này xứng đáng một quyết định có chủ đích thay vì bất cứ mặc định nào của công cụ. Hãy mang danh sách ai và cái gì giữ quyền ghi cho mỗi bộ nhớ đệm, liệu việc ghi có được giới hạn ở CI đáng tin thay vì laptop lập trình viên, và liệu khóa đệm của bạn có băm mọi đầu vào thật để một mục cũ hay bị đầu độc không giả làm hợp pháp. Căng thẳng là các kiểm soát chặt nhất làm chậm con đường tiện nơi lập trình viên đẩy mục đệm từ máy của họ. Trong bối cảnh doanh nghiệp và chính phủ, hãy coi đầu độc bộ nhớ đệm là mối đe dọa tường minh trong mô hình chuỗi cung ứng và yêu cầu cùng kiểm soát truy cập, ghi nhật ký và rà soát như bạn áp dụng cho bất kỳ hệ thống sản xuất nào khác có thể tiêm mã vào một bản phát hành.

6. **Ở điểm nào đồ thị dựng của chúng ta biện minh cho công cụ nặng hơn, và làm sao chúng ta biết đã vượt qua nó?** Lựa chọn giữa công cụ hệ sinh thái nhẹ và hệ thống dựa trên đồ thị như Bazel là một trong những quyết định đắt và khó đảo ngược hơn trong lĩnh vực này, vì di chuyển một cơ sở mã lớn sang định nghĩa dựng chi tiết tốn nhiều tháng và một đội chuyên trách. Quyết định ngưỡng từ trước giữ bạn khỏi hoặc áp dụng độ phức tạp bạn không cần vì thời thượng, hoặc bám vào công cụ nhẹ rất lâu sau khi thời gian dựng bóp nghẹt mọi đội. Hãy mang kích thước và mức phụ thuộc lẫn nhau của đồ thị dựng, chỉ số dựng và trúng đệm hiện tại, và ước tính thực tế chi phí di chuyển và bảo trì liên tục so với thời gian kỹ thuật mà công cụ sẽ thu hồi. Lực kéo đối lập là công cụ nặng mang lại tính gia tăng chính xác và thực thi từ xa mà không gì khác sánh được ở quy mô, nhưng chỉ nếu đồ thị của bạn thực sự đủ lớn để hoàn vốn. Với một doanh nghiệp hay cơ quan lớn, hãy cân nhắc cả liệu bảo đảm tính kín và nguồn gốc của công cụ có giúp thỏa mãn yêu cầu kiểm toán và chuỗi cung ứng, có thể dịch chuyển phép tính vượt khỏi tốc độ thô.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một đội nhỏ xíu và không có đường băng cho hạ tầng dựng, hãy giữ nó nhẹ: dùng công cụ dựng gốc ngôn ngữ, áp dụng lockfile từ ngày đầu, và triển khai ảnh container theo digest thay vì thẻ "latest", vì những thói quen đó tốn gần như không gì và tha cho bạn cả một loại đau "chạy được trên máy tôi" về sau. Chống lại công cụ dựng đồ thị nặng; nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư. Một bộ nhớ đệm bản dựng từ xa là nâng cấp duy nhất đáng với tới một khi bản dựng bắt đầu trườn qua vài phút.

**Doanh nghiệp nhỏ.** Không có kỹ sư dựng riêng, hãy dựa vào dịch vụ được quản lý thay vì chạy hạ tầng artifact của riêng bạn: một registry lưu trữ và bộ nhớ đệm dựng sẵn của nhà cung cấp CI cho bạn đánh phiên bản, lưu giữ và kiểm soát truy cập mà không cần đội nền tảng. Đóng khung lựa chọn mua hơn xây, đặt chính sách hết hạn tự động để chi phí lưu trữ khả đoán, và bảo đảm những điều cơ bản có mặt, phụ thuộc được khóa và triển khai bất biến, ghim digest, vì chúng bảo vệ bạn ngay cả khi không ai theo dõi đường ống toàn thời gian.

**Doanh nghiệp lớn.** Qua nhiều đội vấn đề là nhất quán: một nền tảng dựng dùng chung có chủ, một kho artifact chung, và tiêu chuẩn được thực thi cho lockfile, ký, SBOM và dựng-một-lần-thăng-cấp để không nhóm nào phát minh lại một đường ống không đáng tin. Hãy đầu tư vào bộ nhớ đệm từ xa và, nơi đồ thị dựng biện minh, công cụ dựa trên đồ thị, và coi bộ nhớ đệm như ranh giới tin cậy được quản trị với quyền ghi có phạm vi và ghi nhật ký kiểm toán. Quản lý artifact như một hệ sinh thái được kiểm soát với chính sách lưu giữ và nguồn gốc để bất kỳ thành phần sản xuất nào truy vết được về mã nguồn đã rà soát theo yêu cầu.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công khiến tính toàn vẹn thời gian dựng là yêu cầu tuân thủ, không phải điều dễ chịu. Hãy căn chỉnh đường ống theo một khung phân bậc như SLSA, chạy bản dựng trong môi trường cô lập, hạn chế mạng từ toolchain được ghim, và ủy quyền phụ thuộc bên thứ ba qua một kho nội bộ quét và duyệt chúng trước khi dùng. Lưu SBOM và nguồn gốc đã ký bất biến trong nhiều năm mà luật lưu giữ hồ sơ yêu cầu, chỉ triển khai artifact đã ký, định danh theo digest, và sẵn sàng chứng thực với kiểm toán viên và công chúng rằng phần mềm trong môi trường sản xuất chính xác là cái đã được rà soát và phê duyệt.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười lăm người chạy một monorepo nhỏ bắt đầu với công cụ dựng gốc ngôn ngữ và phản hồi nhanh, là lựa chọn đúng ở quy mô của họ. Khi họ lớn lên, thời gian dựng trườn qua năm phút và kỹ sư bắt đầu chuyển ngữ cảnh khi chờ. Thay vì nhảy sang công cụ dựng đồ thị nặng, họ thêm một bộ nhớ đệm bản dựng từ xa chia sẻ giữa máy lập trình viên và CI, cắt hầu hết bản dựng xuống vài giây vì đích chưa đổi được lấy ra, không dựng lại. Họ áp dụng lockfile cho mọi ngôn ngữ, triển khai ảnh container theo digest thay vì thẻ "latest", và bật hết hạn tự động cho bản dựng ảnh pull request để hóa đơn registry giữ phẳng. Toàn bộ nỗ lực tốn vài tuần và mua lại hàng giờ thời gian kỹ thuật mỗi ngày.

**Doanh nghiệp lớn.** Một công ty dịch vụ tài chính toàn cầu chạy một monorepo lớn qua hàng trăm kỹ sư và áp dụng hệ thống dựng dựa trên đồ thị với bộ nhớ đệm từ xa và thực thi từ xa, vì ở quy mô của họ tính gia tăng chi tiết thu hồi nhiều thời gian kỹ thuật hơn chi phí đội dựng. Mỗi artifact được dựng kín trong môi trường cô lập, ký, và xuất bản lên registry được quản lý kèm SBOM và nguồn gốc đã ký. Triển khai diễn ra theo digest nội dung, và một công cụ chính sách từ chối chạy bất kỳ ảnh nào có chữ ký không xác minh được. Artifact được thăng cấp, không bao giờ dựng lại, từ staging lên sản xuất, nên tệp nhị phân vượt kiểm thử chứng minh được là cái phục vụ khách hàng. Khi kiểm toán viên yêu cầu truy một thành phần sản xuất về mã nguồn đã rà soát, chuỗi lưu giữ là một truy vấn, không phải một cuộc điều tra.

**Chính phủ.** Một cơ quan thuế quốc gia hiện đại hóa hệ thống coi tính toàn vẹn chuỗi cung ứng thời gian dựng là yêu cầu tuân thủ, căn chỉnh đường ống với một khung phân bậc như SLSA. Bản dựng chạy trong môi trường cô lập, hạn chế mạng từ toolchain được ghim và phụ thuộc được khóa, nên đầu ra tái lập được và xác minh độc lập được. Mỗi artifact mang SBOM và nguồn gốc đã ký, lưu bất biến nhiều năm để thỏa mãn luật lưu giữ hồ sơ. Phụ thuộc bên thứ ba được ủy quyền qua một kho nội bộ quét và duyệt chúng trước khi bất kỳ bản dựng nào dùng, giữ mã chưa thẩm định hoàn toàn ngoài mạng. Vì cơ quan chỉ triển khai artifact đã ký, đã thăng cấp, định danh theo digest, nó có thể chứng thực với cơ quan quản lý và công chúng rằng phần mềm xử lý tờ khai của công dân chính xác là cái đã được rà soát và phê duyệt.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của kỷ luật xây dựng và artifact hiện ra trước hết là thời gian kỹ thuật thu hồi. Bản dựng chậm đánh thuế mọi kỹ sư ở mọi thay đổi, và chi phí cộng dồn qua một tổ chức lớn: cắt vài phút khỏi một bản dựng chạy hàng nghìn lần một ngày thu hồi nhiều người-năm mỗi năm và, khó định lượng hơn nhưng thật không kém, giữ kỹ sư trong dòng chảy thay vì chuyển ngữ cảnh. Một bộ nhớ đệm từ xa và tính gia tăng tốt thường tự hoàn vốn trong vài tuần. Artifact tái lập được, thăng cấp-một-lần giảm cả một loại sự cố "nó chạy được ở staging", hạ tỷ lệ thay đổi thất bại và thời gian phục hồi trung bình, các chỉ số phân phối mà lãnh đạo đã theo dõi.

Lợi tức lớn hơn, ít hiển thị hơn là giảm rủi ro. Artifact đã ký, SBOM và nguồn gốc biến một sự cố chuỗi cung ứng từ tình trạng khẩn cấp nhiều tuần thành phản ứng có phạm vi, kéo dài vài giờ, và chúng biến kiểm toán từ cuộc diễn tập cháy thành một truy vấn. Trong bối cảnh chịu quy định và chính phủ, khả năng truy vết đó là điều kiện tiên quyết để hoạt động, nên khoản đầu tư không tùy chọn mà mang tính cấu trúc. Tổng chi phí sở hữu chạy ngược lại khi bạn bỏ bê điều này: artifact khả biến và bản dựng không tái lập được tích tụ thành một hệ sinh thái không ai giải trình trọn vẹn được, lưu trữ lớn không giới hạn khi không có chính sách lưu giữ, và mỗi cuộc kiểm toán cùng mỗi sự cố tốn hơn mức nó cần. Để lập luận với ban lãnh đạo, hãy gắn tốc độ dựng với thông lượng kỹ thuật và gắn tính toàn vẹn artifact với chi phí kiểm toán và phơi nhiễm vi phạm, cả hai họ đã tài trợ.

## Phản mẫu và cạm bẫy

- **Dựng lại theo môi trường:** tạo byte mới cho staging và sản xuất, bỏ bảo đảm rằng artifact đã kiểm thử là artifact đã triển khai.
- **Triển khai theo thẻ nổi:** chạy "latest" hay thẻ khả biến thay vì digest bất biến, nên cái chạy khó đoán và không truy vết được.
- **Không có lockfile:** khoảng phiên bản nổi cho phép bản dựng lặng lẽ kéo phụ thuộc khác hoặc độc hại theo thời gian.
- **Khóa đệm không đầy đủ:** bỏ sót một đầu vào thật khỏi khóa đệm, tạo kết quả cũ phí nhiều ngày gỡ lỗi.
- **Bộ nhớ đệm dùng chung không bảo mật:** để người ghi không đáng tin đầu độc bộ nhớ đệm từ xa nên người tiêu dùng lấy và chạy đầu ra bị xâm phạm.
- **Bản dựng bất định:** dấu thời gian nhúng, đường dẫn tuyệt đối, và công cụ không ghim khiến đầu ra thay đổi và làm mất xác minh.
- **Áp dụng công cụ nặng quá sớm:** gánh độ phức tạp tầm Bazel trước khi đồ thị dựng đủ lớn để biện minh.
- **SBOM và nguồn gốc như chuyện nghĩ sau:** dựng lại siêu dữ liệu chuỗi cung ứng sau bản dựng, khi nó đắt và không đáng tin, thay vì tạo trong bản dựng.
- **Lưu giữ không giới hạn:** không bao giờ cho artifact cũ hết hạn cho đến khi chi phí lưu trữ và tra cứu chậm buộc một cuộc dọn dẹp hoảng loạn.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Bản dựng là tập lệnh tùy nghi không ai sở hữu, thường chạy từ máy lập trình viên. Đầu ra bất định, phụ thuộc nổi không lockfile, artifact được dựng lại theo môi trường và triển khai bằng thẻ khả biến, và không có bộ nhớ đệm dùng chung, không ký, không danh mục vật liệu.
- **Mức 2, Phát triển:** Một số đội đã chuyển bản dựng vào CI từ định nghĩa được commit và áp dụng lockfile, nhưng thực hành không nhất quán toàn tổ chức. Artifact có thể rơi vào kho được quản lý với đánh phiên bản cơ bản, và bộ nhớ đệm cục bộ hoặc từ xa đơn giản tăng tốc các bản dựng phổ biến, nhưng dựng lại theo môi trường vẫn xảy ra và nguồn gốc chắp vá.
- **Mức 3, Chuẩn hóa:** Bản dựng tái lập được, phần lớn kín được lập tài liệu và thực thi toàn tổ chức, với toolchain được ghim và bộ nhớ đệm từ xa dùng chung có khóa băm mọi đầu vào thật. Artifact bất biến, định địa chỉ theo nội dung, đánh phiên bản ngữ nghĩa, dựng một lần và thăng cấp khắp nơi, được ký, và đi kèm SBOM. Truy cập bộ nhớ đệm được kiểm soát và chính sách lưu giữ được áp dụng nhất quán qua các đội.
- **Mức 4, Quản lý:** Hệ sinh thái dựng được đo và kiểm soát theo đường cơ sở. Thời gian dựng, tỷ lệ trúng đệm, thời gian phản hồi lập trình viên và chi phí lưu trữ được theo dõi với mục tiêu tường minh, hồi quy kích hoạt hành động, và xác minh chữ ký cùng nguồn gốc được thực thi lúc triển khai để một kiểm tra thất bại chặn phát hành. Tính toàn vẹn chuỗi cung ứng thời gian dựng được đánh giá theo một khung phân bậc như SLSA, và các con số dẫn dắt nơi bạn đầu tư tiếp.
- **Mức 5, Điều phối:** Thực hành dựng, đệm, artifact và chuỗi cung ứng được cải thiện liên tục và tích hợp trong toàn tổ chức. Công cụ, lưu giữ và tư thế bảo mật thích ứng khi bạn học từ sự cố và kiểm toán, thực thi và lưu đệm từ xa được điều chỉnh khi cơ sở mã tiến hóa, và tính toàn vẹn thời gian dựng được dệt vào vòng đời phát triển an toàn rộng hơn thay vì bắt vít vào sau.

## Ý tưởng để thảo luận

1. Thời gian dựng cục bộ trung vị và tệ nhất hiện tại của bạn là bao nhiêu, và bộ nhớ đệm từ xa sẽ làm gì với mỗi cái?
2. Artifact nào của bạn hôm nay được triển khai bằng thẻ khả biến, và cần gì để triển khai mọi cái theo digest?
3. Đồ thị dựng của bạn biện minh cho công cụ nặng hơn ở đâu, và công cụ đó sẽ tốn hơn tiết kiệm ở đâu?
4. Ai ghi được vào bộ nhớ đệm dựng dùng chung của bạn, và cái gì ngăn một mục bị đầu độc đến môi trường sản xuất?
5. Bạn có thể tạo một SBOM đã ký cho thứ cuối cùng bạn phát hành không, và nếu không, bước nhỏ nhất hướng tới đó là gì?
6. Chính sách lưu giữ của bạn cho artifact dựng là gì, và lưu trữ hôm nay tốn bạn bao nhiêu so với mức nó nên tốn?

## Những điểm cần ghi nhớ

- Bản dựng là bước đầu của phân phối: hãy tài trợ tốc độ và tính đúng của nó như mối quan tâm sản xuất, vì mọi thứ hạ nguồn thừa hưởng khiếm khuyết của nó.
- Làm bản dựng tái lập được và, nơi khả thi, kín, với toolchain được ghim và lockfile, để artifact bạn kiểm toán chứng minh được là cái bạn phát hành.
- Lưu đệm và dựng gia tăng, cục bộ và từ xa, nhưng băm mọi đầu vào thật và bảo mật bộ nhớ đệm, vì bộ nhớ đệm dùng chung là ranh giới tin cậy dùng chung.
- Dựng mỗi artifact một lần, làm nó bất biến và định địa chỉ theo nội dung, đánh phiên bản có ý nghĩa, và thăng cấp đúng artifact đó qua các môi trường.
- Tạo nguồn gốc, chữ ký và SBOM lúc dựng và lưu artifact với lưu giữ và kiểm soát truy cập, biến tính toàn vẹn chuỗi cung ứng và sẵn sàng kiểm toán thành sản phẩm phụ của công việc bình thường.

## Tài liệu tham khảo và đọc thêm

- Jez Humble và David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*
- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Titus Winters, Tom Manshreck và Hyrum Wright (biên tập), *Software Engineering at Google: Lessons Learned from Programming Over Time*
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering: How Google Runs Production Systems*
- Peter Smith, *Software Build Systems: Principles and Experience*
- The Open Source Security Foundation, *SLSA: Supply-chain Levels for Software Artifacts* (đặc tả)
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
