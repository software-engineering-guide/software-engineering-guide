# 8.2 Hạ tầng dưới dạng mã và cấu hình

## Tổng quan và động lực

[Hạ tầng dưới dạng mã](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) nghĩa là xác định và cung cấp hạ tầng (mạng, máy chủ, cơ sở dữ liệu, bộ cân bằng tải, quyền) qua các tệp định nghĩa đọc được bằng máy thay vì nhấp chuột thủ công trên bảng điều khiển hay tập lệnh tùy nghi. [Quản lý cấu hình](https://en.wikipedia.org/wiki/Configuration_management) mở rộng cùng ý tưởng đó sang các thiết lập và trạng thái của hệ thống một khi chúng đã tồn tại. Cùng nhau chúng biến hạ tầng từ một hiện vật thủ công, mong manh thành một sản phẩm có phiên bản, rà soát được, tái lập được của cùng kỷ luật kỹ thuật bạn dùng cho mã ứng dụng.

Với các đội lớn, IaC không phải tiện lợi mà là cần thiết. Khi hàng trăm kỹ sư cần môi trường và hàng nghìn tài nguyên phải nhất quán qua các khu vực và tài khoản, cung cấp thủ công không theo kịp và không giữ đúng được. Hạ tầng cấu hình bằng con người sớm muộn trôi vào những máy chủ "bông tuyết" độc nhất mà không ai hiểu hết và không dựng lại đáng tin được sau sự cố. Mã hóa hạ tầng làm nó nhất quán, kiểm toán được và dùng một lần. Bất kỳ môi trường nào cũng tạo lại được từ định nghĩa của nó, và bất kỳ thay đổi nào cũng là một diff rà soát được.

Các tổ chức doanh nghiệp và chính phủ có thêm một lợi ích quyết định nữa: quản trị thực thi được. Yêu cầu bảo mật và tuân thủ, như mã hóa khi lưu trữ, phân đoạn mạng, khu vực được phê duyệt, và gắn thẻ cho phân bổ chi phí, có thể được nhúng trực tiếp vào mã và kiểm tra tự động trước khi bất cứ thứ gì được cung cấp. Thay vì kiểm toán hạ tầng sau sự việc và đuổi theo vi phạm, bạn giữ hạ tầng không tuân thủ không bao giờ tồn tại. Sự chuyển dịch từ phát hiện sang ngăn ngừa này là lý do cốt lõi IaC đã trở thành nền tảng của thực hành nền tảng hiện đại.

## Các nguyên tắc chính

- Ưu tiên định nghĩa khai báo mô tả trạng thái mong muốn hơn tập lệnh mệnh lệnh mô tả các bước.
- Lưu mọi định nghĩa hạ tầng trong quản lý phiên bản, được rà soát như bất kỳ mã nào khác.
- Coi hạ tầng là bất biến: thay thế thay vì sửa tại chỗ.
- Làm việc cung cấp lũy đẳng để áp dụng cùng định nghĩa lặp lại cho cùng kết quả.
- Phát hiện và đối chiếu độ trôi, môi trường trực tiếp phân kỳ khỏi định nghĩa đã khai báo, liên tục; mã, không phải hệ thống trực tiếp, là nguồn sự thật.
- Ghép hạ tầng từ các mô-đun có phiên bản, tái sử dụng được thay vì sao chép và dán.
- Mã hóa chính sách thành mã, các quy tắc tổ chức được diễn đạt thành mã kiểm tra được bằng máy, để lan can là tự động, không phải khuyến cáo.
- Giữ bí mật ngoài định nghĩa; tham chiếu chúng từ một trình quản lý bí mật chuyên dụng.

## Khuyến nghị

### Chọn công cụ khai báo và cấu trúc nó quanh các mô-đun

Hãy áp dụng một công cụ IaC khai báo, như [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi, hoặc một lựa chọn gốc đám mây như CloudFormation, và chuẩn hóa trên nó toàn tổ chức để tránh bối cảnh công cụ phân mảnh. Thực hành kiến trúc then chốt là tính mô-đun: xây các mô-đun nhỏ, được lập tài liệu tốt, có phiên bản nắm bắt các mẫu phổ biến (một mạng tuân thủ, một cơ sở dữ liệu được gia cố, một dịch vụ chuẩn). Các đội rồi ghép môi trường từ những mô-đun này thay vì tự viết tài nguyên thô. Điều này lan truyền mặc định tốt và thiết lập bảo mật tự động và giảm mạnh sự trùng lặp.

### Quản lý trạng thái có chủ đích

Công cụ khai báo theo dõi ánh xạ giữa mã và tài nguyên thật trong một tệp trạng thái. Hãy lưu trạng thái từ xa trong một backend dùng chung, được mã hóa, kiểm soát truy cập, và dùng khóa để các sửa đổi đồng thời không làm hỏng nó. Đừng bao giờ giữ trạng thái trên laptop, và đừng bao giờ sửa nó bằng tay trừ khi là hành động phục hồi cuối cùng. Trạng thái nhạy cảm, vì nó có thể chứa siêu dữ liệu tài nguyên và bí mật, nên hãy bảo vệ nó tương ứng.

### Xây hạ tầng bất biến với ảnh vàng

Thay vì vá các máy chủ đang chạy, hãy nướng một "ảnh vàng" có phiên bản (một ảnh máy hay container được cấu hình sẵn, gia cố) và triển khai các thể hiện mới từ nó. Khi bạn cần một thay đổi hay bản vá, hãy dựng một ảnh mới và tung ra, cho nghỉ hưu các thể hiện cũ. Điều này loại bỏ trôi cấu hình, làm hoàn tác tầm thường, và giữ mọi thể hiện giống hệt nhau và truy vết được về một bản dựng tốt đã biết. Đường ống ảnh tự động nên gồm gia cố bảo mật và quét, để tuân thủ được xây vào ở cấp ảnh.

### Phát hiện và đối chiếu trôi cấu hình

Trôi xảy ra khi môi trường trực tiếp phân kỳ khỏi định nghĩa của nó, thường vì ai đó thực hiện một thay đổi thủ công khẩn cấp. Hãy chạy phát hiện trôi thường xuyên so sánh trạng thái thực với trạng thái khai báo và gắn cờ các khác biệt. Coi trôi như một khiếm khuyết: đối chiếu bằng cách cập nhật mã và áp dụng lại, không phải bằng cách để thay đổi thủ công tại chỗ. Với các hệ thống cần thực thi cấu hình liên tục, hãy dùng một công cụ quản lý cấu hình liên tục hội tụ các máy chủ về trạng thái khai báo của chúng.

### Áp dụng GitOps và triển khai dựa trên kéo

Trong mô hình GitOps, một kho Git giữ trạng thái mong muốn khai báo của hệ thống, và một tác tử tự động chạy bên trong môi trường đích liên tục kéo trạng thái đó và đối chiếu hệ thống trực tiếp cho khớp. Điều này lật ngược mô hình đẩy truyền thống. Không hệ thống bên ngoài nào cần thông tin xác thực thường trực để đổi môi trường, vì môi trường kéo cấu hình của chính nó. GitOps cho bạn dấu vết kiểm toán đầy đủ (mọi thay đổi là một commit), hoàn tác dễ (hoàn nguyên commit), và sửa trôi mạnh (tác tử liên tục tái khẳng định trạng thái mong muốn). Nó đặc biệt mạnh cho [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) và cho các tổ chức muốn một nguồn sự thật duy nhất, rà soát được.

### Thực thi lan can bằng chính sách dưới dạng mã

Hãy diễn đạt quy tắc tổ chức, như khu vực được phép, mã hóa bắt buộc, thẻ cần có và phơi bày công khai bị cấm, thành chính sách kiểm tra được bằng máy dùng công cụ như Open Policy Agent (OPA) hoặc một công cụ chính sách gốc nền tảng như Sentinel. Chạy các kiểm tra này trong đường ống trước khi cung cấp, để vi phạm bị chặn tự động. Chính sách dưới dạng mã biến ý định của đội bảo mật thành một kiểm soát thực thi được, áp dụng đồng đều, và nó mở rộng cho hàng nghìn thay đổi theo cách rà soát thủ công không bao giờ làm được.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| IaC khai báo (Terraform/Pulumi) | Tái lập được, rà soát được, phát hiện trôi được | Đường cong học; độ phức tạp quản lý trạng thái | Hầu hết đội ở quy mô |
| Tập lệnh mệnh lệnh | Quen thuộc; linh hoạt cho việc một lần | Không lũy đẳng; khó kiểm toán và lặp lại | Trường hợp hẹp, chuyển tiếp |
| Bất biến + ảnh vàng | Không trôi; hoàn tác tầm thường | Chi phí đường ống dựng ảnh | Đội máy cần nhất quán |
| Quản lý cấu hình khả biến | Kiểm soát liên tục chi tiết | Rủi ro trôi; hội tụ chậm hơn | Máy chủ cũ hoặc sống lâu |
| GitOps (dựa trên kéo) | Dấu vết kiểm toán mạnh; tự phục hồi | Cần tác tử trong cụm và kỷ luật Git | Kubernetes và cloud-native |
| Chính sách dưới dạng mã | Lan can tự động, đồng đều | Công sức viết chính sách ban đầu | Môi trường chịu quy định |

Căng thẳng chính là giữa linh hoạt và kiểm soát. Cách tiếp cận thủ công và mệnh lệnh cảm thấy nhanh hơn cho một thay đổi đơn lẻ, nhưng chúng tích tụ sự không nhất quán ẩn trở nên tê liệt ở quy mô. Hạ tầng khai báo, bất biến, được chính sách quản trị đòi hỏi đầu tư ban đầu nhiều hơn và một sự chuyển dịch văn hóa thật, vì kỹ sư phải thôi thực hiện thay đổi nhanh trên bảng điều khiển, nhưng nó đền đáp khoản đầu tư đó nhiều lần về độ tin cậy, khả năng kiểm toán, và khả năng xây lại bất cứ thứ gì theo yêu cầu.

## Câu hỏi để thảo luận với đội của bạn

1. **Ai sở hữu thư viện mô-đun dùng chung, và một cải tiến trong mô-đun đến mọi đội dùng nó thế nào?** Mô-đun chỉ sinh lời nếu bản sửa và mặc định đã gia cố lan truyền, và điều đó đòi quyền sở hữu rõ ràng và đánh phiên bản thật, không phải một thư mục mọi người sao chép. Hãy quyết định ai bảo trì các mô-đun mạng tuân thủ và cơ sở dữ liệu gia cố, bạn đánh phiên bản chúng thế nào (đánh phiên bản ngữ nghĩa với nhật ký thay đổi), và các đội kéo bản nâng cấp mà không báo động thế nào. Ở quy mô đây là sự khác biệt giữa sửa một cấu hình sai một lần và đuổi theo nó qua cả nghìn tài nguyên chỉnh tay. Hãy mang bằng chứng: hôm nay có bao nhiêu bản sao riêng biệt của cùng một mẫu, một bản sửa bảo mật mất bao lâu để đến mọi môi trường, và các đội ghim phiên bản mô-đun hay để nổi. Nếu một bản vá trọng yếu không đến được cả hệ sinh thái trong vài ngày, tính mô-đun của bạn chỉ là bề ngoài.

2. **Nhịp phát hiện trôi của bạn là gì, và điều gì thực sự xảy ra khi tìm thấy trôi?** Trôi là môi trường trực tiếp lặng lẽ phân kỳ khỏi trạng thái khai báo, thường từ một thay đổi khẩn cấp trên bảng điều khiển, và chấp nhận nó biến mã của bạn thành hư cấu. Hãy quyết định bạn so sánh trạng thái thực với trạng thái khai báo bao lâu một lần (hằng đêm là mặc định hợp lý) và, quan trọng hơn, quyết định phản ứng: đối chiếu bằng cách cập nhật mã và áp dụng lại, không bao giờ bằng cách để thay đổi thủ công tại chỗ. Trong bối cảnh chịu quy định đây là yêu cầu kiểm soát, vì kiểm toán viên cần trạng thái khai báo khớp thực tế liên tục. Hãy mang con số hiện tại của bạn: mỗi tuần bao nhiêu tài nguyên trôi, chúng ở trạng thái trôi bao lâu, và có ai chịu trách nhiệm đóng chúng. Coi mỗi lần trôi là khiếm khuyết có chủ sở hữu, nếu không bảo đảm nguồn sự thật xói mòn cho đến khi không ai tin mã.

3. **Bạn đã chuyển sang GitOps và đối chiếu dựa trên kéo chưa, hay vẫn còn một hệ thống bên ngoài giữ thông tin xác thực thường trực để đổi môi trường sản xuất?** Trong mô hình kéo, một tác tử bên trong môi trường đích liên tục đối chiếu hệ thống trực tiếp với Git, loại bỏ nhu cầu bất kỳ hệ thống bên ngoài nào giữ quyền ghi, và nó tái khẳng định trạng thái mong muốn để trôi tự sửa. Đó là tư thế bảo mật và kiểm toán mạnh, vì mọi thay đổi là một commit và không người vận hành nào cần thông tin xác thực sản xuất thường trực. Chi phí là thật: một tác tử trong cụm phải chạy và kỷ luật Git nghiêm ngặt, nên hãy cân nhắc nó với tự động hóa dựa trên đẩy hiện tại. Hãy mang danh sách ai và cái gì hiện có thể thay đổi môi trường sản xuất trực tiếp, và những thay đổi đó để lại dấu vết kiểm toán nào. Với Kubernetes và các vùng bảo đảm cao, sự chuyển dịch này thường đáng; với một nhúm tài nguyên tĩnh nó có thể thừa.

4. **Trạng thái hạ tầng của bạn được lưu, khóa và kiểm soát truy cập thế nào, và điều gì xảy ra vào ngày nó bị hỏng hoặc mất?** Trạng thái là bản đồ giữa mã và tài nguyên thật, nên một tệp trạng thái mất hay hỏng có thể để công cụ mù với tài nguyên nó đã tạo và cám dỗ ai đó vào một lần áp dụng lại phá hủy. Với một đội lớn rủi ro nhân lên, vì nhiều kỹ sư áp dụng trên trạng thái dùng chung cần một backend từ xa, được mã hóa, có khóa để các lần chạy đồng thời không đè lên nhau. Hãy cân nhắc sự tiện lợi của một trạng thái lớn với bán kính ảnh hưởng nó tạo ra, và cân nhắc tách trạng thái theo môi trường hoặc theo miền để một sai lầm duy nhất không làm sập mọi thứ. Hãy mang sự thật: trạng thái hôm nay sống ở đâu, khóa có được thực thi không, ai đọc được nó (nó có thể chứa bí mật), và bạn đã bao giờ diễn tập phục hồi chưa. Trong bối cảnh doanh nghiệp và chính phủ, hãy coi backend trạng thái là tài sản nhạy cảm, kiểm soát truy cập với bản sao lưu, nhật ký kiểm toán và sổ tay phục hồi riêng, vì mất nó là mất bản ghi về những gì tồn tại.

5. **Khi một tình huống khẩn cấp thật sự đòi thay đổi thủ công, đường phá kính được phê duyệt là gì, và thay đổi đó được gấp trở lại vào mã thế nào?** Mọi thực hành IaC trưởng thành rốt cuộc gặp sự cố 3 giờ sáng nơi chờ đường ống là không chấp nhận được, và câu hỏi trung thực không phải liệu thay đổi thủ công có bao giờ xảy ra mà là bạn kiềm chế chúng thế nào. Hãy quyết định từ trước ai được bỏ qua đường ống, họ được chạm vào gì, hành động được ghi nhật ký thế nào, và hạn chót mà thay đổi phải được đối chiếu vào mã hoặc hoàn nguyên. Không có thỏa thuận đó, ngoại lệ khẩn cấp lặng lẽ thành thói quen hằng ngày và ClickOps trở lại qua cửa sau. Hãy mang bằng chứng: quý trước có bao nhiêu thay đổi ngoài luồng, mỗi cái chưa được đối chiếu bao lâu, và phát hiện trôi có thực sự bắt được chúng. Với các cơ quan chịu quy định và công, một quy trình phá kính có tài liệu với ghi nhật ký tự động thường là yêu cầu kiểm soát, vì kiểm toán viên kỳ vọng cả việc khẩn cấp có thể xảy ra lẫn việc mỗi lần để lại dấu vết và đưa hệ thống về trạng thái khai báo.

6. **Bao nhiêu đường cơ sở bảo mật và tuân thủ của bạn được diễn đạt thành chính sách tự động chặn một thay đổi tồi, so với quy tắc sống trong tài liệu và dựa vào ai đó nhớ?** Lan can viết bằng văn xuôi trong wiki bị vi phạm thường xuyên, vì chúng phụ thuộc vào mọi kỹ sư đọc và áp dụng dưới áp lực hạn chót, trong khi cùng quy tắc diễn đạt thành chính sách dưới dạng mã từ chối thay đổi không tuân thủ trước khi nó bao giờ được cung cấp. Với một tổ chức lớn đây là cách duy nhất ý định của đội bảo mật mở rộng cho hàng nghìn thay đổi mà không thành nút thắt rà soát. Hãy cân nhắc chi phí ban đầu của việc viết và bảo trì chính sách với chi phí lặp lại của rà soát thủ công và khắc phục sau sự việc, và quyết định các kiểm soát nào (mã hóa, khu vực được duyệt, thẻ bắt buộc, không phơi bày công khai) không thể thương lượng đủ để thực thi như cổng cứng. Hãy mang danh sách quy tắc đường cơ sở hiện tại của bạn và đánh dấu cái nào tự động so với khuyến cáo, cộng mỗi cái bị vi phạm bao lâu một lần trên thực tế. Trong bối cảnh doanh nghiệp và chính phủ, chính sách tự động biến một cuộc kiểm toán từ nhiều tuần thu thập bằng chứng thủ công thành một truy vấn trên các kiểm soát được thực thi, và nó biến tuân thủ từ phát hiện thành ngăn ngừa.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ thắng, vì vậy hãy đặt toàn bộ ngăn xếp trong một kho khai báo duy nhất (Terraform là mặc định phổ biến), giữ trạng thái trong backend được quản lý, mã hóa, và đưa mọi thay đổi qua pull request ngay cả với đội ba người. Bỏ qua bộ máy nền tảng nặng: không đội mô-đun trung tâm, chưa có công cụ chính sách, chỉ quản lý phiên bản và kỷ luật không bao giờ nhấp trong bảng điều khiển. Chỉ điều đó đã cho bạn môi trường tái lập được mà bạn có thể gỡ bỏ để tiết kiệm tiền và dựng lại cho buổi demo kế tiếp.

**Doanh nghiệp nhỏ.** Không có chuyên gia nền tảng riêng, hãy dựa vào dịch vụ được quản lý và bất kỳ IaC nào nhà cung cấp đám mây hay nhà bán hàng của bạn đã hỗ trợ thay vì dựng công cụ đặt riêng bạn không bảo trì nổi. Ưu tiên mua một nền tảng lưu trữ có mặc định hợp lý (mã hóa, sao lưu, vá lỗi) được xử lý giúp bạn hơn xây một đường ống ảnh vàng bạn không có ai chạy. Đóng khung mục tiêu hẹp: đưa nhúm tài nguyên trọng yếu của bạn vào mã để bạn dựng lại sau sự cố hay khi một nhà thầu rời đi.

**Doanh nghiệp lớn.** Vấn đề cốt lõi là nhất quán qua nhiều đội, tài khoản và khu vực, vì vậy hãy đầu tư vào một thư viện mô-đun dùng chung có phiên bản, trạng thái từ xa có khóa, và chính sách dưới dạng mã được thực thi trong đường ống. Một đội nền tảng trung tâm xuất bản mô-đun và lan can đã gia cố trong khi các đội sản phẩm tự phục vụ trong đó, và phát hiện trôi chạy liên tục để hàng nghìn tài nguyên ở trạng thái đã biết. Hãy lập ngân sách cho chi phí liên tục của việc bảo trì mô-đun và chính sách, vì giá trị của chúng đến từ việc một bản sửa hay mặc định đã gia cố lan truyền khắp nơi cùng lúc.

**Chính phủ.** Quy tắc mua sắm, kiểm định và trách nhiệm giải trình công đẩy bạn về hạ tầng bất biến, commit đã ký, và đối chiếu GitOps bên trong một vùng đã kiểm định, để không người vận hành nào giữ thông tin xác thực thường trực đổi môi trường sản xuất. Hãy mã hóa đường cơ sở bảo mật yêu cầu vào ảnh vàng và chính sách dưới dạng mã, và để lịch sử commit phục vụ như bằng chứng kiểm toán chống giả mạo, luôn sẵn có. Ưu tiên công cụ mở, di chuyển được hơn định dạng độc quyền bẫy bạn, và làm quy trình phá kính cùng việc ghi nhật ký của nó tường minh để thay đổi khẩn cấp vẫn thỏa mãn yêu cầu kiểm soát cấu hình.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp năm người định nghĩa toàn bộ thiết lập AWS của mình, gồm VPC, cơ sở dữ liệu và dịch vụ container, trong một kho Terraform duy nhất với trạng thái giữ trong backend S3 mã hóa và khóa qua DynamoDB. Mọi thay đổi đi qua pull request, nên ngay cả một kỹ sư trực một mình cũng thấy chính xác cái gì sẽ đổi trước khi chạy apply. Khi cần một môi trường staging mới cho một buổi demo lớn, họ sao chép một mô-đun nhỏ và dựng nó trong vài phút, và gỡ nó nhanh như vậy để giữ hóa đơn đám mây thấp.

**Doanh nghiệp lớn.** Một nhà bán lẻ đa quốc gia quản lý hạ tầng qua nhiều tài khoản đám mây và khu vực. Một đội nền tảng trung tâm xuất bản các mô-đun Terraform có phiên bản cho mạng, cơ sở dữ liệu và khung dịch vụ tuân thủ, và thực thi chính sách OPA từ chối bất kỳ tài nguyên nào thiếu mã hóa hoặc thẻ phân bổ chi phí. Các đội sản phẩm tự cung cấp môi trường theo kiểu tự phục vụ, nhưng mọi thay đổi chảy qua đường ống, nơi chính sách được kiểm tra tự động. Phát hiện trôi chạy hằng đêm và mở phiếu cho bất kỳ thay đổi thủ công nào, giữ hàng nghìn tài nguyên liên tục ở trạng thái đã biết, tuân thủ.

**Chính phủ.** Một cơ quan quốc phòng vận hành trong môi trường bảo đảm cao xây ảnh vàng đã gia cố nhúng đường cơ sở bảo mật yêu cầu, và chỉ triển khai các thể hiện bất biến từ những ảnh đó. Toàn bộ hạ tầng được khai báo trong Git và được một tác tử GitOps đối chiếu bên trong vùng đã kiểm định, nên không người vận hành nào giữ thông tin xác thực thường trực để đổi trực tiếp môi trường sản xuất. Mọi thay đổi là một commit đã ký. Điều này cho kiểm toán viên một lịch sử đầy đủ, chống giả mạo và thỏa mãn yêu cầu giám sát liên tục cùng kiểm soát cấu hình mà không cần thu thập bằng chứng thủ công.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của IaC đến từ tốc độ, độ tin cậy và giảm rủi ro. Môi trường từng mất nhiều tuần cung cấp thủ công theo phiếu có thể được tạo trong vài phút, giải phóng kỹ sư và tăng tốc dự án. Khả năng tái lập cắt giảm mạnh thời gian phục hồi sau thất bại, vì bất kỳ môi trường nào cũng dựng lại được từ mã. Thực thi chính sách tự động giảm tần suất và chi phí của sự cố bảo mật và phát hiện kiểm toán, có thể đáng kể với các tổ chức chịu quy định.

Trên sổ cái TCO, chi phí áp dụng gồm công cụ, đào tạo, xây dựng thư viện mô-đun và chính sách, và kỷ luật thôi thực hiện thay đổi thủ công. Chi phí của việc không áp dụng dốc hơn và cộng dồn theo thời gian: hạ tầng bông tuyết không ai dựng lại được, cung cấp chậm và dễ lỗi, cấu hình bảo mật sai dẫn đến vi phạm, và kiểm toán ngốn nhiều tuần công sức thủ công. Với ban lãnh đạo, hãy đóng khung IaC là biến hạ tầng từ khoản nợ không được quản lý thành tài sản được quản trị, tái lập được, và là cơ chế khiến bảo mật cùng tuân thủ tự động thay vì khát vọng.

## Phản mẫu và cạm bẫy

- **ClickOps trong môi trường sản xuất.** Thay đổi bằng tay trong bảng điều khiển bảo đảm trôi và phá hủy khả năng tái lập.
- **Bí mật trong mã.** Gắn cứng thông tin xác thực trong tệp định nghĩa làm chúng rò vào lịch sử phiên bản và trạng thái.
- **Định nghĩa nguyên khối, không mô-đun hóa.** Một cấu hình khổng lồ không ai dám đổi trở nên giòn như thiết lập thủ công mà nó thay thế.
- **Trạng thái không được quản lý.** Tệp trạng thái cục bộ hoặc không khóa dẫn đến hỏng và mất hạ tầng.
- **Chấp nhận trôi.** Để thay đổi thủ công tại chỗ xói mòn bảo đảm nguồn sự thật cho đến khi mã là hư cấu.
- **Chính sách như tài liệu.** Quy tắc sống trong wiki thay vì kiểm tra tự động bị vi phạm thường xuyên.
- **Sinh sôi sao chép-dán.** Nhân bản cấu hình qua các đội nghĩa là bản sửa và cải tiến không bao giờ lan.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Hạ tầng được cung cấp thủ công qua bảng điều khiển và tập lệnh tùy nghi. Môi trường không nhất quán, không có tài liệu, và không tái lập đáng tin được, và phục hồi sau thất bại chậm và không chắc chắn.

**Mức 2: Phát triển.** Một số hạ tầng được mã hóa, nhưng thực hành khác nhau theo đội. Quản lý trạng thái không nhất quán, trôi phổ biến, bí mật đôi khi rò vào định nghĩa, và chính sách được thực thi, nếu có, qua rà soát thủ công.

**Mức 3: Chuẩn hóa.** IaC khai báo là tiêu chuẩn có tài liệu toàn tổ chức, được xây từ các mô-đun dùng chung có phiên bản với trạng thái được quản lý, từ xa, có khóa. Chính sách dưới dạng mã thực thi lan can trong đường ống, bí mật được tham chiếu từ một trình quản lý chuyên dụng, và phát hiện trôi chạy theo nhịp đều đặn.

**Mức 4: Quản lý.** Thực hành được đo theo đường cơ sở. Bạn theo dõi tỷ lệ trôi và thời gian trung bình để đối chiếu, mức áp dụng phiên bản mô-đun qua các đội, vi phạm chính sách bị chặn so với lọt qua, thời gian chờ cung cấp, và phần tài nguyên thực sự nằm dưới mã. Các chỉ số này chặn cổng thay đổi và dẫn dắt nơi bạn đầu tư, để quyết định dựa trên bằng chứng thay vì giai thoại.

**Mức 5: Điều phối.** Hạ tầng bất biến và do GitOps thúc đẩy, tự phục hồi trước trôi, với bằng chứng tuân thủ được tạo tự động. Thư viện mô-đun và chính sách cải thiện liên tục từ cách dùng thực và sự cố, và thực hành hạ tầng được tích hợp với hoạch định bảo mật, chi phí và phân phối để toàn bộ hệ sinh thái thích ứng khi yêu cầu dịch chuyển.

## Ý tưởng để thảo luận

- Lằn ranh giữa mô-đun được quản trị tập trung và quyền tự chủ của đội để định nghĩa hạ tầng tùy chỉnh nên nằm ở đâu?
- Bạn xử lý thay đổi khẩn cấp thật sự phải bỏ qua đường ống thế nào mà không bình thường hóa ClickOps?
- Chiến lược đúng để quản lý và bảo mật trạng thái qua nhiều tài khoản và đội là gì?
- Khi nào quản lý cấu hình khả biến vẫn được biện minh so với hạ tầng hoàn toàn bất biến?
- Làm sao bạn giữ thư viện chính sách-dưới-dạng-mã thẳng hàng với yêu cầu bảo mật và quy định tiến hóa?
- Một lộ trình di chuyển thực tế cho hạ tầng cũ có trước IaC trông thế nào?

## Những điểm cần ghi nhớ

- Xác định hạ tầng một cách khai báo, đánh phiên bản nó, và coi nó là mã rà soát được, tái lập được.
- Xây từ các mô-đun nhỏ, có phiên bản để lan truyền mặc định tốt và loại bỏ trùng lặp.
- Ưu tiên hạ tầng bất biến và ảnh vàng để xóa bỏ trôi và đơn giản hóa hoàn tác.
- Quản lý trạng thái có chủ đích và giữ bí mật ngoài định nghĩa.
- Áp dụng GitOps cho dấu vết kiểm toán mạnh và đối chiếu tự phục hồi.
- Thực thi lan can bằng chính sách dưới dạng mã để tuân thủ được ngăn ngừa vào tồn tại, không phải kiểm toán sau sự việc.

## Tài liệu tham khảo và đọc thêm

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy (biên tập), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois và John Willis, *The DevOps Handbook*.
- Weaveworks, các bài viết nền tảng về "GitOps" (Alexis Richardson et al.).
- Tài liệu Open Policy Agent và ngôn ngữ chính sách Rego.
- NIST Special Publication 800-53, kiểm soát bảo mật và quyền riêng tư (họ quản lý cấu hình).
