# 5.6 Kỹ thuật giao diện người dùng

## Tổng quan và động lực

Kỹ thuật giao diện người dùng là kỷ luật xây tầng hướng máy khách của phần mềm: mã chạy trong trình duyệt hoặc trên thiết bị và biến thiết kế, nội dung và dữ liệu thành một giao diện hoạt động. Nó trải rộng lựa chọn khung phát triển và kiến trúc, chiến lược kết xuất, quản lý trạng thái, hiệu năng và khả năng phục hồi qua sự đa dạng khổng lồ của trình duyệt, thiết bị và điều kiện mạng trong thế giới thực. Giao diện người dùng là nơi mọi công việc thượng nguồn (UX, thiết kế, nội dung, khả năng tiếp cận, quốc tế hóa) hoặc đến được người dùng thành công hoặc sụp đổ.

Với các đội lớn, giao diện người dùng đặc biệt thách thức, vì nó phơi ra trước một môi trường mà tổ chức không kiểm soát. Trình duyệt, thiết bị, kết nối và thiết lập của người dùng khác nhau rất nhiều, và nền tảng (web) tiến hóa liên tục. Ở quy mô lớn, các lựa chọn kiến trúc cộng dồn. Một khung phát triển được chọn hôm nay ràng buộc tuyển dụng, hiệu năng và khả năng bảo trì trong nhiều năm, và hàng nghìn quyết định nhỏ về kích thước gói và kết xuất cộng lại thành trải nghiệm người dùng thực sự nhận được. Tiêu chuẩn dùng chung, thư viện thành phần, ngân sách hiệu năng và mẫu kiến trúc là thứ giữ nhiều đội độc lập khỏi tạo ra một tổng thể chậm, không nhất quán, mong manh.

Sự liên quan với doanh nghiệp và chính phủ là cấp bách. Doanh nghiệp duy trì các ứng dụng sống lâu nơi tuổi thọ khung phát triển và khả năng bảo trì quan trọng hơn sự mới lạ, và nơi nhiều đội phải tương tác. Chính phủ phục vụ toàn thể công chúng, bao gồm người dùng thiết bị cũ, kết nối chậm hoặc tính theo dung lượng, và công nghệ hỗ trợ. Điều đó khiến hiệu năng, [nâng cấp tiến bộ](https://en.wikipedia.org/wiki/Progressive_enhancement) và khả năng phục hồi không phải sự trau chuốt tùy chọn mà là sự khác biệt giữa một dịch vụ hoạt động cho mọi người và một dịch vụ loại trừ những người thiệt thòi nhất. Một dịch vụ chính phủ chỉ hoạt động trên điện thoại mới nhất với kết nối nhanh đã thất bại nhiệm vụ của mình.

## Các nguyên tắc chính

- Giao diện người dùng chạy trong một môi trường bạn không kiểm soát; thiết kế cho sự biến thiên và thất bại.
- Chọn công nghệ nhàm chán, bền vững cho các hệ thống sống lâu; tối ưu cho khả năng bảo trì và tuyển dụng.
- Hiệu năng là một tính năng và, với nhiều người dùng, là điều kiện tiên quyết để tiếp cận.
- Nâng cấp tiến bộ: giao một trải nghiệm lõi hoạt động trước, rồi xếp lớp nâng cao.
- Gửi ít mã hơn; mã nhanh và đáng tin cậy nhất là mã bạn không phát hành.
- Khớp chiến lược kết xuất với loại nội dung và nhu cầu người dùng, không phải mốt.
- Khả năng phục hồi: giao diện nên suy giảm nhẹ nhàng, không vỡ, khi có chuyện sai.
- Tiêu chuẩn và tính năng nền tảng sống lâu hơn khung phát triển; hãy dựa vào nền tảng.

## Khuyến nghị

### Chọn khung phát triển vì tuổi thọ và độ phù hợp, không phải cường điệu

Hãy chọn công nghệ giao diện người dùng dựa trên vấn đề, đội, chân trời bảo trì và thị trường tuyển dụng, không phải cái đang thịnh hành. Với các hệ thống doanh nghiệp và chính phủ sống lâu, hãy ưu tiên các công nghệ trưởng thành, được hỗ trợ tốt với nguồn nhân tài lớn, thực hành phát hành ổn định, và đường nâng cấp rõ ràng. Cân nhắc tổng chi phí của sự xáo động khung phát triển: viết lại thì đắt và rủi ro. Ưu tiên các cách tiếp cận dựa vào [tiêu chuẩn web](https://en.wikipedia.org/wiki/Web_standards) để khoản đầu tư của bạn sống sót qua sự luân chuyển khung phát triển, và cô lập mã đặc thù khung phát triển sau các ranh giới để ứng dụng không bị làm con tin của vòng đời một thư viện.

### Khớp chiến lược kết xuất với nhu cầu

Các chiến lược kết xuất chính mỗi cái phù hợp với nội dung khác nhau. Kết xuất phía máy chủ (SSR) tạo ra lần vẽ đầu nhanh và SEO ([tối ưu công cụ tìm kiếm](https://en.wikipedia.org/wiki/Search_engine_optimization)) tốt và hoạt động mà không cần JavaScript phía máy khách, phù hợp trang nặng nội dung và hướng công chúng. [Sinh trang tĩnh](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) kết xuất trước lúc dựng cho tốc độ và khả năng lưu đệm tối đa, lý tưởng cho nội dung thay đổi không thường xuyên. Kết xuất phía máy khách (CSR) phù hợp với trải nghiệm tương tác cao, giống ứng dụng sau xác thực. Streaming và hydrat hóa tiến bộ gửi và kích hoạt trang dần dần để người dùng thấy và dùng nội dung sớm hơn. Nhiều hệ thống lớn pha trộn những thứ này theo từng tuyến thay vì chọn một cho toàn cục. Hãy quản lý trạng thái có chủ đích: giữ trạng thái máy chủ, trạng thái URL và trạng thái UI cục bộ riêng biệt, và tránh tập trung quá mức mọi thứ vào một kho toàn cục nặng nề.

### Coi hiệu năng là một kỷ luật có ngân sách, được đo

Hãy áp dụng ngân sách hiệu năng (giới hạn tường minh về kích thước gói, số yêu cầu và chỉ số then chốt) và thực thi chúng trong CI để hồi quy làm hỏng bản dựng. Theo dõi Core Web Vitals (tải, tương tác và ổn định thị giác) bằng giám sát người dùng thực từ thiết bị và mạng thực, không chỉ kiểm thử phòng thí nghiệm trên máy nhanh. Giảm JavaScript quyết liệt: tách mã và [tải lười](https://en.wikipedia.org/wiki/Lazy_loading) để người dùng chỉ tải những gì một khung nhìn cụ thể cần, hoãn công việc không quan trọng, và ưu tiên năng lực nền tảng hơn thư viện nặng. Tối ưu hình ảnh và phông chữ, lưu đệm hiệu quả, và đo trên thiết bị cấp thấp đại diện cùng kết nối chậm.

### Xây với nâng cấp tiến bộ và khả năng phục hồi

Hãy bắt đầu từ một đường cơ sở hoạt động với HTML ngữ nghĩa và ít hoặc không JavaScript, rồi nâng cấp cho máy khách có năng lực. Điều này bảo đảm nhiệm vụ lõi vẫn khả thi khi tập lệnh không tải được, thiết bị cũ, hay mạng chập chờn, một thực tế phổ biến chứ không phải trường hợp biên. Xử lý lỗi nhẹ nhàng: hiển thị các trạng thái hữu ích cho tải, rỗng, lỗi và ngoại tuyến thay vì màn hình trống hay vòng quay vô tận. Với các dịch vụ người ta phụ thuộc, hãy cân nhắc kỹ thuật ưu tiên-ngoại-tuyến để ứng dụng vẫn dùng được qua kết nối gián đoạn, đồng bộ khi kết nối quay lại.

### Bảo đảm tương thích đa trình duyệt, đa thiết bị và hỗ trợ

Hãy kiểm thử qua các trình duyệt, thiết bị và công nghệ hỗ trợ mà người dùng của bạn thực sự có, dựa trên phân tích thực thay vì máy của chính đội. Dùng nâng cấp tiến bộ và phát hiện tính năng thay vì giả định các tính năng nền tảng mới nhất sẵn có ở mọi nơi. Xây [đáp ứng](https://en.wikipedia.org/wiki/Responsive_web_design) (xem chương hệ thống thiết kế) để một cơ sở mã phục vụ từ điện thoại đến máy tính để bàn. Tích hợp khả năng tiếp cận và quốc tế hóa vào kiến trúc giao diện người dùng từ đầu, không phải các lượt làm sau.

### Quản trị giao diện người dùng như hạ tầng dùng chung

Hãy cung cấp thư viện thành phần dùng chung, linting, định dạng và công cụ dựng để các đội nhất quán và năng suất. Thiết lập hướng dẫn kiến trúc (cách cấu trúc ứng dụng, quản lý trạng thái và tách gói) và ngân sách hiệu năng được thực thi trong CI. Với các giao diện người dùng rất lớn, hãy cân nhắc kiến trúc mô-đun hay micro-frontend cho phép các đội triển khai độc lập, nhưng cân nhắc cẩn thận độ phức tạp và chi phí hiệu năng thêm vào, vì chúng không miễn phí.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| Khung phát triển trưởng thành phổ biến | Nguồn nhân tài lớn, ổn định, được hỗ trợ | Có thể mang gánh nặng cũ; chậm áp dụng tính năng mới nhất |
| Khung phát triển mới nhất | Tính năng hiện đại, cải thiện hiệu năng | Rủi ro xáo động, nguồn nhân tài nhỏ, tuổi thọ không chắc |
| SSR / SSG | Lần vẽ đầu nhanh, SEO, hoạt động không cần JS | Độ phức tạp máy chủ hay dựng, thách thức lưu đệm |
| CSR (SPA) | Tương tác phong phú, cảm giác như ứng dụng | Tải đầu chậm, phụ thuộc JS, chi phí SEO và khả năng phục hồi |
| JavaScript phía máy khách nặng | Tính năng phong phú | Hiệu năng kém trên thiết bị cấp thấp, mong manh |
| Nâng cấp tiến bộ | Có khả năng phục hồi, hòa nhập, hoạt động ở mọi nơi | Nhiều công sức thiết kế hơn để xác định đường cơ sở hoạt động |
| Micro-frontend | Triển khai độc lập theo đội, mở rộng | Độ phức tạp, phụ thuộc trùng lặp, chi phí hiệu năng |

Đánh đổi lặp lại là sự phong phú và tiện lợi cho lập trình viên so với tầm với, hiệu năng và khả năng phục hồi. Các cách tiếp cận nặng phía máy khách dễ chịu để xây và trình diễn trên máy nhanh, nhưng chúng loại trừ người dùng trên thiết bị và mạng yếu. Với đối tượng doanh nghiệp và đặc biệt là chính phủ, hãy nghiêng cán cân về hiệu năng, nâng cấp tiến bộ và độ bền, vì chi phí loại trừ người dùng cao và thường không thể thương lượng.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta cô lập mã đặc thù khung phát triển thế nào để ứng dụng không bị làm con tin của vòng đời một thư viện?** Với các hệ thống doanh nghiệp và chính phủ sống lâu, sự xáo động khung phát triển là khoản chi tránh được lớn nhất: viết lại thì đắt và rủi ro, và thư viện đang thịnh hành hôm nay ràng buộc tuyển dụng và bảo trì trong nhiều năm. Dựa vào tiêu chuẩn web và đặt mã đặc thù khung phát triển sau các ranh giới rõ ràng nghĩa là logic nghiệp vụ và nội dung của bạn sống sót qua lần luân chuyển khung kế tiếp. Hãy quyết định những đường nối đó ở đâu và liệu một kỹ sư mới có phân biệt được mã nền tảng với mã khung phát triển không. Hãy mang ước tính chi phí lần di chuyển khung gần nhất của bạn, hoặc cái đang lù lù sẽ tốn bao nhiêu. Nếu logic lõi của bạn bị hàn vào API của một thư viện, hãy định giá sự ghép nối đó trước khi bạn bảo vệ lựa chọn khung phát triển.

2. **Chúng ta khớp chiến lược kết xuất theo từng tuyến, hay ép một chiến lược lên cả sản phẩm?** Kết xuất phía máy chủ cho lần vẽ đầu nhanh và hoạt động không cần JavaScript phía máy khách cho nội dung công khai, sinh trang tĩnh tối đa hóa tốc độ cho các trang ít thay đổi, và kết xuất phía máy khách phù hợp với các bề mặt tương tác giống ứng dụng sau đăng nhập. Ép một chiến lược toàn cục hoặc làm chậm trang công khai bằng JavaScript nặng hoặc kỹ thuật hóa quá mức một trang nội dung đơn giản. Đây là câu hỏi tầm với với chính phủ, nơi một dịch vụ chỉ hoạt động sau khi một gói lớn tải xong loại trừ người dùng trên thiết bị cũ và kết nối chậm. Hãy mang các tuyến then chốt của bạn và gắn nhãn mỗi cái với chiến lược nó thực sự dùng hôm nay. Nếu một trang hướng công chúng cần JavaScript để hiển thị nội dung, hãy quyết định liệu đó là lựa chọn có chủ đích hay một tai nạn.

3. **Quản lý trạng thái của chúng ta kỷ luật đến đâu, và chúng ta có đang tập trung quá mức mọi thứ vào một kho toàn cục nặng nề không?** Giữ trạng thái máy chủ, trạng thái URL và trạng thái UI cục bộ riêng biệt ngăn sự ghép nối và các cơn bão kết xuất lại khiến giao diện người dùng lớn chậm và mong manh, vậy mà mặc định cám dỗ là đổ mọi thứ vào một kho toàn cục. Điều này cộng dồn ở quy mô lớn, nơi nhiều đội chạm vào một kho dùng chung tạo ra phụ thuộc ẩn và hiệu năng không đoán trước. Hãy thống nhất mỗi loại trạng thái thuộc về đâu và cái gì không thuộc về kho toàn cục. Hãy mang một thành phần kết xuất lại nhiều hơn mức cần và truy vì sao. Nếu câu trả lời là một kho trung tâm phình to, hãy quyết định ranh giới trước khi sự ghép nối đông cứng.

4. **Ngân sách hiệu năng của chúng ta là gì, chúng có làm hỏng bản dựng trong CI không, và chúng có được đo trên thiết bị người dùng của chúng ta thực sự có không?** Một ngân sách không ai thực thi là một điều ước, và một ngân sách chỉ đo trên laptop nhanh của đội mô tả một người dùng không tồn tại. Với một tổ chức lớn, ngân sách là cơ chế duy nhất giữ kích thước gói và Core Web Vitals trong tầm kiểm soát khi hàng chục đội thêm tính năng vào một bề mặt dùng chung, vì không người rà soát đơn lẻ nào bắt được mọi hồi quy bằng mắt. Áp lực đối lập là tốc độ phân phối: một thất bại bản dựng cứng vì vài kilobyte cảm thấy cản trở cho đến khi bạn định giá sự bỏ dở nó ngăn. Hãy mang ngân sách hiện tại của bạn, dữ liệu giám sát người dùng thực từ thiết bị cấp thấp và kết nối chậm, và danh sách các bản phát hành nơi một hồi quy lọt qua. Trong chính phủ, nơi nhiệm vụ là phục vụ toàn thể công chúng bao gồm người dùng điện thoại cũ và dữ liệu tính theo dung lượng, hãy gắn ngân sách với mười phần trăm chậm nhất người dùng của bạn thay vì trung vị, và biến cổng CI thành không thể thương lượng.

5. **Dịch vụ nào của chúng ta phải tiếp tục hoạt động khi không có JavaScript phía máy khách, và chúng ta đã thực sự kiểm thử con đường đó chưa?** Nâng cấp tiến bộ dễ tuyên bố và dễ lặng lẽ phá vỡ, vì con đường được nâng cấp là cái lập trình viên dùng mỗi ngày trong khi đường cơ sở mục nát chưa kiểm thử. Quyết định điều này có chủ đích quan trọng ở quy mô lớn, vì nhiều đội phát hành lên một nền tảng sẽ mỗi đội giả định tập lệnh luôn tải trừ khi một tiêu chuẩn dùng chung nói khác, và một phụ thuộc cứng đơn lẻ có thể phá nhiệm vụ lõi cho bất kỳ ai có gói không tải được. Đánh đổi là thật: một đường cơ sở không-JavaScript hoạt động tốn công sức thiết kế và ràng buộc cách bạn xây tương tác. Hãy mang các hành trình người dùng quan trọng của bạn, một bài kiểm thử tải từng cái với tập lệnh bị tắt hay thất bại, và bằng chứng về tần suất tập lệnh thực sự không tải được ngoài hiện trường. Với dịch vụ công, một biểu mẫu trợ cấp hay thuế sụp đổ khi một tập lệnh hết thời gian không phải trải nghiệm suy giảm, đó là một công dân không thể hoàn thành nghĩa vụ pháp lý, nên hãy coi đường cơ sở là yêu cầu tuân thủ, không phải điều dễ chịu.

6. **Khi nào micro-frontend thực sự xứng đáng với độ phức tạp của chúng, và ai quyết định trước khi một đội với tới một cái?** Triển khai độc lập theo đội hấp dẫn, nhưng micro-frontend mang độ phức tạp hệ thống phân tán, phụ thuộc trùng lặp, và thuế hiệu năng mà người dùng trả bằng tải chậm hơn. Không có điểm quyết định chung, các đội có hoài bão áp dụng chúng vì sự tiện lợi tổ chức từ lâu trước khi quy mô biện minh chi phí, và cả sản phẩm thừa hưởng chi phí chung. Cân nhắc đối lập là quyền tự chủ: các đội phát hành trên một cơ sở mã dùng chung có thể chặn nhau, và ở quy mô thực sự sự ghép nối đó bản thân là vấn đề tốn kém. Hãy mang số đội chạm vào bề mặt, sự tranh chấp triển khai bạn thực sự trải nghiệm hôm nay, và một ước tính đo được về sự trùng lặp tải trọng mà một lần tách sẽ đưa vào. Với các nền tảng doanh nghiệp và chính phủ, nơi quyết định kiến trúc ràng buộc nhiều đội trong nhiều năm và phải sống sót qua kiểm toán và bàn giao, hãy yêu cầu một ngưỡng tường minh, có tài liệu và một chủ sở hữu phê duyệt bước đi, thay vì để mỗi đội quyết định riêng.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Cả tốc độ lẫn tầm với đều quan trọng khi mỗi lượt đăng ký có giá trị, vì vậy hãy cưỡng lại ứng dụng một trang nặng cho các trang công khai. Hãy kết xuất phía máy chủ luồng tiếp thị và đăng ký của bạn để chúng tải nhanh trên điện thoại tầm trung và dữ liệu chập chờn mà khách hàng sớm của bạn dùng, và dành tương tác phía máy khách cho ứng dụng sau đăng nhập. Đặt một ngân sách kích thước gói đơn giản trong CI để một phụ thuộc cẩu thả không thể lặng lẽ làm phình trang, và dựa vào tiêu chuẩn web để giữ cơ sở mã nhỏ bảo trì được khi bạn tuyển người.

**Doanh nghiệp nhỏ.** Không có chuyên gia giao diện người dùng riêng và ngân sách eo hẹp, hãy ưu tiên một khung phát triển chính thống được hỗ trợ tốt hoặc một công cụ dựng trang được lưu trữ hơn bất cứ thứ gì làm riêng, để bạn tuyển từ nguồn nhân tài lớn và mua bảo trì thay vì bố trí nhân sự cho nó. Hãy đóng khung lựa chọn là độ bền: lựa chọn rẻ nhất là cái bạn không bị buộc viết lại sau hai năm. Hãy kiên quyết đòi trang nhanh, thân thiện di động và đánh dấu tiếp cận được ngay từ đầu, vì một thanh toán chậm hay hỏng làm bạn mất khách hàng mà bạn không gánh nổi.

**Doanh nghiệp lớn.** Vấn đề là sự nhất quán qua nhiều đội: một thư viện thành phần dùng chung, mẫu kiến trúc đã thống nhất, công cụ linting và dựng, và ngân sách hiệu năng được thực thi trong CI để không đội nào lặng lẽ làm hồi quy tổng thể. Hãy chọn khung phát triển vì tuổi thọ và tuyển dụng thay vì sự mới lạ, cô lập mã đặc thù khung phát triển sau các ranh giới để sống sót qua lần di chuyển kế tiếp, và khớp chiến lược kết xuất theo từng bề mặt. Hãy quản lý giao diện người dùng như hạ tầng dùng chung với giám sát người dùng thực, quản trị, và bản ghi kiểm toán được vì sao mỗi lựa chọn kiến trúc được đưa ra.

**Chính phủ.** Bạn phục vụ toàn thể công chúng, bao gồm người dùng thiết bị cũ, kết nối chậm hoặc tính theo dung lượng, và công nghệ hỗ trợ, nên nâng cấp tiến bộ và hiệu năng là nghĩa vụ, không phải sự trau chuốt. Hãy biến một đường cơ sở không-JavaScript hoạt động thành quy tắc cứng cho các dịch vụ hướng công dân, ngân sách các trang theo những người dùng chậm nhất thay vì trung vị, và giữ nhiệm vụ lõi hoàn thành được khi một tập lệnh thất bại. Mua sắm và minh bạch áp dụng: ưu tiên công nghệ bền vững, nghiêng về tiêu chuẩn, tránh khóa chặt một nhà cung cấp, lập tài liệu yêu cầu khả năng tiếp cận và hiệu năng trong hợp đồng, và có thể cho thấy dịch vụ hoạt động với người dùng thiệt thòi nhất, không chỉ thiết bị trình diễn.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp giai đoạn hạt giống bị cám dỗ xây trang tiếp thị và luồng đăng ký như một ứng dụng một trang nặng, nhưng khách hàng mục tiêu của họ là người mua sắm thường trên điện thoại tầm trung qua dữ liệu di động chập chờn. Hai người sáng lập thay vào đó kết xuất phía máy chủ các trang công khai để chúng tải nhanh và hoạt động trước khi bất kỳ JavaScript nào chạy, và dành tương tác phía máy khách cho ứng dụng sau đăng nhập. Họ đặt một ngân sách kích thước gói đơn giản trong CI để một phụ thuộc cẩu thả không thể lặng lẽ làm phình trang. Lần tải đầu gọn, nhanh cải thiện số lượt đăng ký một cách đo được, và việc dựa vào tiêu chuẩn web giữ cơ sở mã nhỏ của họ dễ bảo trì khi họ tuyển người.

**Doanh nghiệp lớn.** Một công ty dịch vụ tài chính hiện đại hóa một tập ứng dụng nội bộ và khách hàng đồ sộ bằng cách chuẩn hóa trên một khung phát triển trưởng thành, một thư viện thành phần dùng chung, và ngân sách hiệu năng được thực thi trong CI. Chiến lược kết xuất được chọn theo từng bề mặt: các trang kết xuất phía máy chủ, lưu đệm được cho tiếp thị và nội dung công khai, và một ứng dụng kết xuất phía máy khách sau đăng nhập cho bảng điều khiển tương tác. Ngân sách gói và giám sát người dùng thực bắt hồi quy trước phát hành, giữ thời gian tải nhanh qua nhiều đội của công ty và giảm rủi ro xáo động khung phát triển từng buộc phải viết lại tốn kém.

**Chính phủ.** Một đội dịch vụ số quốc gia xây các dịch vụ hướng công dân với nâng cấp tiến bộ như quy tắc cứng: mọi dịch vụ hoạt động với HTML ngữ nghĩa và kết xuất phía máy chủ trước, và JavaScript chỉ nâng cao. Điều này bảo đảm dịch vụ hoạt động trên điện thoại cũ, kết nối nông thôn chậm, và công nghệ hỗ trợ, những quần thể mà một chính phủ không thể loại trừ. Ngân sách hiệu năng giữ các trang nhẹ và nhanh trên thiết bị cấp thấp, và suy giảm nhẹ nhàng nghĩa là một tập lệnh thất bại không bao giờ chặn ai đó hoàn thành đơn xin trợ cấp. Kết quả là một dịch vụ nhanh, có khả năng phục hồi, tiếp cận được, và dùng được bởi toàn thể công chúng.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lựa chọn kỹ thuật giao diện người dùng thúc đẩy doanh thu, tầm với và chi phí. Hiệu năng gắn trực tiếp với chuyển đổi, tương tác và hoàn thành nhiệm vụ. Trải nghiệm nhanh hơn vượt trội hơn chậm hơn một cách đo được, và với người dùng trên thiết bị yếu, hiệu năng là ranh giới giữa dùng dịch vụ và bỏ dở. Nâng cấp tiến bộ và hỗ trợ đa thiết bị mở rộng đối tượng có thể tiếp cận, với chính phủ là một nhiệm vụ và với doanh nghiệp là thị phần. Lựa chọn khung phát triển và kiến trúc đúng đắn giảm tần suất và chi phí của việc viết lại, khoản chi tránh được lớn nhất trong kỹ thuật giao diện người dùng.

Về TCO, chi phí áp dụng là kỷ luật của ngân sách hiệu năng và kiểm thử, công sức của nâng cấp tiến bộ, và khoản đầu tư vào công cụ cùng thư viện thành phần dùng chung. Chi phí của việc không áp dụng được trả bằng trải nghiệm chậm làm mất người dùng và doanh thu, sự loại trừ người dùng cấp thấp và công nghệ hỗ trợ (với rủi ro pháp lý trong chính phủ), ứng dụng mong manh vỡ ngoài hiện trường, và sự xáo động khung phát triển cùng viết lại tốn kém do đuổi theo xu hướng. Vấn đề giao diện người dùng hiện ra dưới dạng bỏ dở lan tỏa và tải hỗ trợ thay vì một dòng đơn lẻ, nên dễ đầu tư thiếu.

Để trình bày lập luận với ban lãnh đạo, hãy nối Core Web Vitals và thời gian tải với phễu chuyển đổi và hoàn thành, định lượng người dùng bị loại trừ bởi cách tiếp cận nặng phía máy khách, và định giá chi phí của các lần viết lại đã qua hay đang lù lù so với sự ổn định của một kiến trúc bền vững, nghiêng về tiêu chuẩn. Đóng khung ngân sách hiệu năng và nâng cấp tiến bộ là giảm rủi ro và mở rộng tầm với.

## Phản mẫu và cạm bẫy

- **Đuổi theo khung phát triển**: viết lại trên thư viện mới nhất, chịu sự xáo động mà người dùng không được lợi.
- **Trải nghiệm chỉ-JavaScript**: không có gì hoạt động cho đến khi một gói lớn tải và chạy, loại trừ nhiều người dùng.
- **Chỉ kiểm thử trên thiết bị nhanh**: laptop hàng đầu của đội che giấu trải nghiệm người dùng thực.
- **Bỏ qua kích thước gói**: phụ thuộc tăng không giới hạn cho đến khi trang chậm ở mọi nơi.
- **Không có ngân sách hiệu năng**: hồi quy tích tụ trong im lặng qua từng bản phát hành.
- **Thất bại màn hình trống**: không có trạng thái tải, rỗng, lỗi hay ngoại tuyến; một yêu cầu thất bại làm vỡ trang.
- **Trạng thái toàn cục tập trung quá mức**: mọi thứ trong một kho, tạo ra ghép nối và bão kết xuất lại.
- **Micro-frontend sớm**: độ phức tạp hệ thống phân tán và tải trọng trùng lặp mà không có quy mô để biện minh.
- **Bỏ bê khả năng tiếp cận và i18n trong kiến trúc**: gắn thêm sau với chi phí cao.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Giao diện người dùng tùy nghi, xây theo từng đội không có tiêu chuẩn dùng chung. Mã phía máy khách nặng, không có ngân sách hiệu năng, chỉ kiểm thử trên thiết bị của chính đội. Lựa chọn khung phát triển do sở thích hay cường điệu, và một tập lệnh thất bại có thể để người dùng nhìn chằm chằm vào màn hình trống.

**Mức 2: Phát triển.** Một số đội áp dụng công cụ dùng chung và thư viện thành phần, nhưng thực hành không nhất quán trong tổ chức. Hiệu năng được đo thỉnh thoảng thay vì lập ngân sách hay thực thi. Chiến lược kết xuất thường đồng nhất bất kể loại nội dung, và kiểm thử đa thiết bị hạn chế và thủ công.

**Mức 3: Chuẩn hóa.** Khung phát triển và kiến trúc được chọn có chủ đích vì tuổi thọ, và các lựa chọn được lập tài liệu và thực thi toàn tổ chức. Chiến lược kết xuất được khớp theo từng bề mặt, nâng cấp tiến bộ và suy giảm nhẹ nhàng là tiêu chuẩn, và thư viện thành phần dùng chung, linting và công cụ dựng áp dụng cho mọi đội. Đa trình duyệt, khả năng tiếp cận và quốc tế hóa được xây vào thay vì gắn thêm.

**Mức 4: Quản lý.** Giao diện người dùng được đo và kiểm soát bằng dữ liệu. Ngân sách hiệu năng được thực thi trong CI để hồi quy làm hỏng bản dựng, và Core Web Vitals được theo dõi bằng giám sát người dùng thực từ thiết bị cấp thấp và kết nối chậm thực đối chiếu với đường cơ sở tường minh. Kích thước gói, độ bao phủ trạng thái lỗi và ngoại tuyến, và tỷ lệ người dùng được phục vụ trên các kết nối chậm nhất được báo cáo và rà soát, nên quyết định dựa trên bằng chứng thay vì ý kiến.

**Mức 5: Điều phối.** Hiệu năng, khả năng phục hồi và tầm với được cải thiện liên tục và gắn với kết quả kinh doanh trong toàn tổ chức. Giao diện người dùng dựa vào tiêu chuẩn web cho độ bền, cô lập phụ thuộc khung phát triển để di chuyển rẻ, và tiến hóa kiến trúc thích ứng khi thiết bị, nền tảng và dữ liệu người dùng thực dịch chuyển. Toàn thể công chúng và mọi thiết bị là hạng nhất, và thực hành giao diện người dùng được tích hợp với thiết kế, khả năng tiếp cận và hoạch định sản phẩm thay vì được coi là mối quan tâm riêng.

## Ý tưởng để thảo luận

- Làm sao bạn quyết định khi nào một lần di chuyển khung phát triển đáng với chi phí và rủi ro của nó?
- Ngưỡng Core Web Vitals và ngân sách gói nào nên là ngưỡng cứng làm hỏng bản dựng?
- Nâng cấp tiến bộ thiết yếu ở đâu, và một ứng dụng phía máy khách chấp nhận được ở đâu?
- Làm sao bạn giữ kiến trúc giao diện người dùng nhất quán qua nhiều đội tự chủ?
- Khi nào micro-frontend thực sự xứng đáng với độ phức tạp của chúng?
- Kiểm thử trên thiết bị thật và mạng chậm nên được xây vào đường ống thế nào?

## Những điểm cần ghi nhớ

- Giao diện người dùng chạy trong một môi trường bạn không kiểm soát: thiết kế cho sự biến thiên và thất bại.
- Chọn công nghệ bền vững, được hỗ trợ tốt cho các hệ thống sống lâu; dựa vào tiêu chuẩn web.
- Khớp chiến lược kết xuất (SSR, SSG, CSR, streaming) với nội dung và nhu cầu, thường pha trộn theo từng tuyến.
- Coi hiệu năng là một kỷ luật có ngân sách, được đo, thực thi trong CI với dữ liệu người dùng thực.
- Xây với nâng cấp tiến bộ để trải nghiệm lõi hoạt động ở mọi nơi.
- Gửi ít JavaScript hơn; tách mã, tải lười, và ưu tiên năng lực nền tảng.
- Đặc biệt với chính phủ, hiệu năng và khả năng phục hồi là điều kiện tiên quyết cho tiếp cận công bằng.

## Tài liệu tham khảo và đọc thêm

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (nâng cấp tiến bộ)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, các bài viết về hiệu năng, tách mã và chi phí của JavaScript
- Google, *Web Vitals* và hướng dẫn hiệu năng web.dev
- MDN Web Docs, tài liệu tham khảo về nền tảng web và nâng cấp tiến bộ
- Alex Russell, các bài luận về chi phí của JavaScript và sự đa dạng thiết bị
- UK Government Digital Service, hướng dẫn nâng cấp tiến bộ và giao diện người dùng
- WHATWG HTML Living Standard và các đặc tả nền tảng web của W3C
