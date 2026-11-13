# 4.1 Nền tảng và văn hóa bảo mật

## Tổng quan và động lực

Bảo mật không phải là một tính năng bạn gắn thêm vào cuối, và nó không phải là công việc của một đội chuyên biệt ngồi tách khỏi kỹ thuật. Trong một tổ chức lớn, bảo mật là một thuộc tính của cách toàn bộ hệ thống được thiết kế, xây dựng, vận hành và quản trị. Khi hàng nghìn kỹ sư phát hành mã qua hàng trăm dịch vụ, mắt xích yếu nhất quyết định mức thiệt hại một sự cố có thể gây ra. Một thùng lưu trữ cấu hình sai, một phụ thuộc chưa vá, hay một tài khoản dịch vụ được cấp quá nhiều đặc quyền có thể phơi bày hàng triệu bản ghi. Nền tảng và văn hóa là thứ ngăn điều đó xảy ra ở quy mô lớn.

Với doanh nghiệp, rủi ro là về tài chính và danh tiếng: chi phí xâm phạm, tiền phạt quy định, khách hàng bỏ đi và định giá sụt giảm. Với chính phủ, chúng mở rộng đến an ninh quốc gia, niềm tin công chúng và tính liên tục của các dịch vụ thiết yếu. Cả hai bối cảnh chia sẻ một sự thật khó chịu: bạn không thể thực thi bảo mật thuần túy qua các biện pháp kiểm soát và cổng chặn. Nó phải được nội tâm hóa bởi những người làm công việc. Một văn hóa nơi kỹ sư hiểu các mối đe dọa, cảm thấy quyền sở hữu, và được thưởng khi nêu lên mối lo ngại tạo ra kết quả tốt hơn nhiều so với văn hóa dựa vào một đội bảo mật quá tải đóng vai thủ môn.

Chương này trình bày các mô hình tư duy và thực hành văn hóa làm nền cho mọi chương bảo mật khác trong hướng dẫn này. Nó bao quát việc biến bảo mật thành việc của mọi người, [mô hình hóa mối đe dọa](https://en.wikipedia.org/wiki/Threat_model), vòng đời phát triển an toàn, các nguyên tắc kiến trúc nền tảng như [phòng thủ theo chiều sâu](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) và [không tin cậy](https://en.wikipedia.org/wiki/Zero_trust_security_model), và cách ưu tiên công việc bảo mật theo rủi ro thực thay vì nỗi sợ hay mốt.

*Xem thêm:* chương 4.2 (bảo mật ứng dụng), chương 4.3 (bảo mật hạ tầng và đám mây), chương 4.4 (vận hành bảo mật) và chương 4.6 (tuân thủ và quản trị) xây trên những nền tảng này.

## Các nguyên tắc chính

- **Bảo mật là việc của mọi người.** Mỗi kỹ sư, quản lý sản phẩm và người vận hành sở hữu tính bảo mật của những gì họ xây. Đội bảo mật hỗ trợ, tư vấn và kiểm toán; nó không và không thể làm công việc một mình.
- **Giả định bị xâm phạm.** Thiết kế như thể kẻ tấn công đã ở bên trong. Giảm thiểu những gì một thành phần bị xâm phạm có thể với tới.
- **Phòng thủ theo chiều sâu.** Không biện pháp kiểm soát đơn lẻ nào là đủ. Xếp tầng các biện pháp độc lập để thất bại của một cái không có nghĩa là thất bại của tất cả.
- **[Đặc quyền tối thiểu](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Cấp quyền truy cập tối thiểu cần thiết, trong thời gian tối thiểu, và tự động thu hồi khi không còn cần.
- **Dịch chuyển sang trái.** Tìm và sửa vấn đề sớm nhất có thể, khi chúng rẻ nhất để khắc phục.
- **Ưu tiên theo rủi ro.** Dành công sức ở nơi sự kết hợp giữa khả năng xảy ra và tác động cao nhất, được dẫn dắt bởi bộ ba CIA (tính bảo mật, toàn vẹn và sẵn sàng), không phải bất cứ thứ gì lên tin tức tuần này.
- **Học hỏi không đổ lỗi.** Coi các sự cố bảo mật và suýt xảy ra là cơ hội học hỏi, không phải dịp để trừng phạt.

## Khuyến nghị

### Thiết lập chương trình nhà vô địch bảo mật

Hãy nhúng một nhà vô địch bảo mật được chỉ định vào mỗi đội kỹ thuật. Nhà vô địch không phải chuyên gia bảo mật toàn thời gian. Họ là các kỹ sư được đào tạo thêm và có đường dây trực tiếp đến đội bảo mật trung tâm. Họ rà soát thiết kế, phân loại phát hiện, trả lời câu hỏi của đồng đội, và mang bối cảnh bảo mật vào hoạch định. Điều này mở rộng chuyên môn bảo mật qua tổ chức mà không phải tuyển một chuyên gia cho mỗi đội, và nó xây dựng niềm tin, vì lời khuyên đến từ một đồng nghiệp thực sự biết cơ sở mã.

Hãy hỗ trợ nhà vô địch thực sự: một diễn đàn đều đặn để chia sẻ những gì họ học, ngân sách cho đào tạo và hội nghị, sự ghi nhận trong đánh giá hiệu suất, và thời gian được dành ra khỏi cam kết phân phối của họ. Một chương trình nhà vô địch chỉ tồn tại trên giấy không tạo ra gì.

### Thực hành mô hình hóa mối đe dọa thường xuyên

Mô hình hóa mối đe dọa là thói quen có kỷ luật hỏi "điều gì có thể sai?" trước khi bạn xây. Hãy làm nó cho dịch vụ mới, tính năng lớn và bất kỳ thay đổi nào với ranh giới tin cậy. Giữ nó đủ nhẹ để nó thực sự xảy ra thường xuyên.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** là một danh sách kiểm tra thực tế ánh xạ với các thuộc tính bảo mật: Giả mạo (xác thực), Can thiệp (toàn vẹn), Chối bỏ (không thể chối bỏ), Tiết lộ thông tin (bảo mật), Từ chối dịch vụ (sẵn sàng), và Nâng đặc quyền (cấp quyền). Hãy đi qua từng luồng dữ liệu và hỏi mỗi loại áp dụng thế nào.
- **PASTA** (Quy trình Mô phỏng Tấn công và Phân tích Mối đe dọa) là phương pháp bảy giai đoạn nặng hơn, lấy rủi ro làm trung tâm, gắn các mối đe dọa kỹ thuật với tác động kinh doanh; hãy dùng nó cho các hệ thống giá trị cao.
- **[Cây tấn công](https://en.wikipedia.org/wiki/Attack_tree)** phân rã một mục tiêu ("đánh cắp dữ liệu khách hàng") thành các bước phân nhánh mà kẻ tấn công sẽ thực hiện, giúp bạn tìm và cắt tỉa các con đường.

Hãy giữ các mô hình mối đe dọa như tài liệu sống cạnh mã, và xem lại chúng bất cứ khi nào kiến trúc thay đổi.

### Xây dựng vòng đời phát triển phần mềm an toàn

Hãy đan bảo mật vào mọi giai đoạn thay vì coi nó như một cổng cuối cùng:

- **Yêu cầu:** nắm bắt yêu cầu bảo mật và riêng tư cùng với yêu cầu chức năng.
- **Thiết kế:** mô hình hóa mối đe dọa và rà soát ranh giới tin cậy.
- **Cài đặt:** thực thi tiêu chuẩn lập trình an toàn, rà soát mã, và quét bí mật trước commit.
- **Kiểm thử:** chạy [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (kiểm thử bảo mật ứng dụng tĩnh), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (kiểm thử bảo mật ứng dụng động), và quét phụ thuộc trong đường ống (xem chương 4.4).
- **Phát hành:** xác minh nguồn gốc, ký các sản phẩm, và kiểm tra cấu hình.
- **Vận hành:** giám sát, vá và phản ứng.

Điểm của dịch chuyển sang trái không phải là dồn mọi công việc lên sớm hơn và làm kỹ sư choáng ngợp. Mà là bắt các loại khiếm khuyết rẻ hơn nhiều để sửa sớm.

### Áp dụng các nguyên tắc kiến trúc không tin cậy

Bảo mật chu vi truyền thống giả định mọi thứ bên trong mạng là đáng tin. Giả định đó thất bại ngay khoảnh khắc kẻ tấn công có một chỗ đứng chân. Không tin cậy thay sự tin cậy mạng ngầm định bằng xác minh tường minh, liên tục: xác thực và cấp quyền cho mọi yêu cầu dựa trên danh tính, tư thế thiết bị và ngữ cảnh, bất kể nó đến từ đâu trên mạng. Hãy kết hợp danh tính mạnh, cấp quyền đặc quyền tối thiểu, phân đoạn vi mô, và [mã hóa](https://en.wikipedia.org/wiki/Encryption) ở mọi nơi. Không tin cậy là một hành trình, không phải một sản phẩm, vì vậy hãy tiếp cận nó từng bước một.

### Ưu tiên theo rủi ro bằng bộ ba CIA

Hãy đóng khung mọi tài sản và biện pháp kiểm soát quanh **Tính bảo mật**, **Toàn vẹn** và **Sẵn sàng**. Không phải dữ liệu nào cũng cần cùng mức bảo vệ: một trang tiếp thị công khai và một cơ sở dữ liệu hồ sơ y tế có nhu cầu bảo mật khác nhau một trời một vực. Hãy phân loại tài sản, ước tính khả năng xảy ra và tác động của sự xâm phạm, và hướng công sức bảo mật khan hiếm vào các tổ hợp rủi ro cao nhất. Hãy viết ra các quyết định rủi ro của bạn để người khác có thể rà soát và bảo vệ chúng sau này.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Đội bảo mật trung tâm sở hữu mọi bảo mật | Chuyên môn sâu, tiêu chuẩn nhất quán | Nút thắt, kỹ sư thờ ơ, không mở rộng được |
| Bảo mật phân tán (nhà vô địch) | Mở rộng được, xây dựng quyền sở hữu, phản hồi nhanh hơn | Cần đầu tư, kỹ năng không đồng đều, cần điều phối |
| Mô hình hóa mối đe dọa nặng ngay từ đầu cho mọi thứ | Kỹ lưỡng, bắt được lỗi thiết kế | Làm chậm phân phối, có thể thành làm cho có |
| Mô hình hóa mối đe dọa nhẹ, nhắm theo rủi ro | Nhanh, tập trung vào điều quan trọng | Có thể bỏ sót mối đe dọa trong hệ thống "rủi ro thấp" |
| Cổng nghiêm ngặt chặn phát hành | Thực thi tuân thủ | Ma sát, khuyến khích cách lách |

Căng thẳng trung tâm là giữa tốc độ và sự bảo đảm. Nghiêng quá xa về phía cổng chặn và kiểm soát trung tâm, bạn tạo ra ma sát mà kỹ sư tìm đường vòng, sinh ra CNTT bóng tối và sự oán giận. Nghiêng quá xa về phía tự chủ mà không hỗ trợ, bạn có bảo mật không nhất quán, không được kiểm toán. Câu trả lời bền vững là một văn hóa mạnh với lan can hỗ trợ: tự động hóa ở nơi bạn có thể, con người ở nơi cần phán đoán, và luôn được giải thích thay vì chỉ áp đặt.

## Câu hỏi để thảo luận với đội của bạn

1. **Hệ thống nào của bạn xứng đáng với mô hình hóa mối đe dọa hạng nặng, và ai quyết định bậc?** Trong một hệ sinh thái lớn bạn không thể chạy phân tích PASTA bảy giai đoạn cho mọi dịch vụ, nên bạn cần một quy tắc tường minh cho khi nào một lượt STRIDE 30 phút là đủ và khi nào một hệ thống giá trị cao xứng đáng với mô hình hóa sâu, dẫn dắt bởi tác động kinh doanh. Hãy neo quyết định vào phân loại CIA của bạn: hệ thống giữ hồ sơ chịu quy định, luồng thanh toán, hay logic xác thực ở trên cùng, còn một trang tiếp thị công khai thì không. Với công việc doanh nghiệp và chính phủ, kiểm toán viên sẽ yêu cầu bạn bảo vệ vì sao một hệ thống nhất định được mô hình hóa theo cách đó, nên hãy viết ra tiêu chí phân bậc và nêu tên chủ sở hữu áp dụng chúng. Hãy mang phân loại tài sản hiện tại và danh sách các dịch vụ không có mô hình mối đe dọa đến cuộc họp, vì khoảng cách giữa chúng là rủi ro thực của bạn. Nếu bạn không thống nhất được ngưỡng, bạn sẽ mặc định mô hình hóa mọi thứ một cách nhẹ hoặc không gì một cách sâu, và cả hai đều thất bại.

2. **Khi một nhà vô địch bảo mật và một hạn chót phân phối va chạm, ai thực sự có thể dừng bản phát hành?** Một chương trình nhà vô địch chỉ thay đổi kết quả nếu nhà vô địch mang thẩm quyền thực, không chỉ đào tạo thêm và thiện chí. Hãy quyết định trước liệu một nhà vô địch có thể chặn một lần phát hành không, họ có leo thang lên đội AppSec trung tâm không, và mức nghiêm trọng nào của phát hiện biện minh cho việc dừng phân phối so với chỉ theo dõi nó. Điều này quan trọng nhất dưới áp lực, khi một quản lý sản phẩm muốn bỏ qua một lỗi thiết kế vào tuần trước khi ra mắt, chính là lúc các lỗi chưa xử lý tốn nhất để sửa. Hãy mang một ví dụ gần đây nơi một mối lo ngại bảo mật gặp hạn chót và truy ai quyết định và bằng cách nào, vì câu chuyện đó tiết lộ đường leo thang thực của bạn. Nếu câu trả lời trung thực là phân phối luôn thắng, nhà vô địch của bạn chỉ là đồ trang trí và bạn nên sửa động lực trước khi thêm nhiều nhà vô địch hơn.

3. **"Giả định bị xâm phạm" cụ thể thay đổi gì trong buổi rà soát thiết kế kế tiếp của bạn?** Nguyên tắc dễ gật đầu đồng ý và khó biến thành thao tác, vì vậy hãy ghim nó vào các cam kết cụ thể: ranh giới tin cậy nào bạn sẽ siết, nơi nào bạn sẽ thêm phân đoạn vi mô, và bạn sẽ thu nhỏ những gì một tài khoản dịch vụ bị xâm phạm đơn lẻ có thể với tới thế nào. Với một đội lớn, phần thưởng là giảm bán kính ảnh hưởng, để kẻ tấn công đáp xuống một dịch vụ không thể xoay sang kho dữ liệu phía sau. Trong bối cảnh doanh nghiệp và chính phủ điều này cũng định hình các quyết định đặc quyền tối thiểu và thông tin xác thực sống ngắn của bạn, vốn rẻ để thiết kế vào và đau đớn để trang bị bổ sung. Hãy mang một sơ đồ dịch vụ thật và hỏi kẻ tấn công làm gì sau khi chúng sở hữu tầng web, rồi cam kết hai thay đổi khoanh vùng trong quý này. Sự đồng ý mơ hồ rằng xâm phạm xảy ra là vô giá trị trừ khi nó dịch chuyển một quyền, một quy tắc mạng, hay thời hạn của một thông tin xác thực.

4. **Làm sao bạn biết văn hóa bảo mật của mình thực sự đang cải thiện, và chỉ số nào bạn sẽ bảo vệ trước hội đồng quản trị?** Tỷ lệ hoàn thành đào tạo và số phiếu dễ thu thập và gần như vô dụng, vì chúng đo hoạt động thay vì giảm rủi ro, và một tổ chức lớn chìm trong chúng. Hãy chọn các chỉ số kết quả mà bạn thực sự dám đặt ngân sách lên: thời gian trung vị để khắc phục các phát hiện mức nghiêm trọng cao, tỷ lệ dịch vụ mang mô hình mối đe dọa hiện hành, phần các sự cố được bắt trước môi trường thực, và tỷ lệ suýt xảy ra được tự báo cáo, vốn nên tăng khi niềm tin lớn lên thay vì giảm. Cân nhắc đối lập là mọi chỉ số tốt đều có thể bị lách, vì vậy hãy ghép mỗi chỉ số với một chỉ số đối trọng và xem xu hướng thay vì ảnh chụp. Hãy mang bảng điều khiển hiện tại của bạn và hỏi những con số nào sẽ thay đổi nếu bảo mật thực sự tệ đi; những cái không đổi là đồ trang trí. Trong bối cảnh doanh nghiệp và chính phủ, cơ quan quản lý hay ủy ban kiểm toán sẽ hỏi bằng chứng rằng các biện pháp kiểm soát hoạt động, vì vậy hãy chọn chỉ số bạn bảo vệ được dưới sự soi xét thay vì những cái chỉ trông xanh.

5. **Điều gì thực sự xảy ra lần kế tiếp một kỹ sư báo cáo một sai lầm, và quy trình của bạn không đổ lỗi trong thực tế hay chỉ trên slide?** Học hỏi không đổ lỗi là nguyên tắc được tuyên bố nhiều nhất và sống ít nhất, vì sự cố nghiêm trọng đầu tiên thử xem ban lãnh đạo có thực sự có ý đó không. Hãy quyết định trước cách bạn tách trách nhiệm sửa một vấn đề khỏi sự trừng phạt vì đã gây ra nó, và ai chạy buổi rà soát sau sự cố để nó vẫn xoay quanh các hệ thống hỏng thay vì các cá nhân bị nêu tên. Căng thẳng là thật: các bên liên quan muốn ai đó chịu trách nhiệm, nhưng trừng phạt người báo cáo bảo đảm sai lầm kế tiếp vẫn bị giấu cho đến khi nó thành một vụ xâm phạm. Hãy mang hai buổi rà soát sự cố gần nhất của bạn và kiểm tra xem chúng đổ lỗi cho một người hay một biện pháp kiểm soát, và kỹ sư nêu lên cảnh báo được cảm ơn hay lặng lẽ bị gạt sang bên. Với chính phủ và doanh nghiệp chịu quy định, các quy tắc công bố xâm phạm bắt buộc nâng rủi ro lên nữa, vì một văn hóa che giấu sai lầm cũng sẽ bỏ lỡ các hạn chót báo cáo mang hình phạt pháp lý.

6. **Ai sở hữu ma sát của công cụ dịch-chuyển-sang-trái của bạn, và bạn đang mua nó, xây nó, hay chìm trong nó?** Phân tích tĩnh và động tự động, quét phụ thuộc và quét bí mật là xương sống của vòng đời phát triển an toàn, nhưng một đường ống làm ngập kỹ sư bằng dương tính giả dạy họ phớt lờ đầu ra bảo mật, tệ hơn không quét gì cả. Hãy quyết định ai điều chỉnh công cụ, ai phân loại phát hiện, và bạn mua một nền tảng tích hợp hay lắp ráp các bộ quét mã nguồn mở mà sau đó bạn phải tự bảo trì. Các cân nhắc cạnh tranh là độ bao phủ so với nhiễu và kiểm soát so với chi phí: một bộ quét rẻ cứ kêu sói đến đốt cháy niềm tin mà một chương trình nhà vô địch phải mất nhiều năm xây. Hãy mang tỷ lệ dương tính giả hiện tại, thời gian trung bình kỹ sư chờ một kiểm tra chặn, và danh sách các đội đã lặng lẽ tắt một cổng. Trong doanh nghiệp lớn và chính phủ, hãy thêm góc độ mua sắm và lan tràn công cụ, vì mười đội mỗi đội tự mua bộ quét riêng tạo ra độ bao phủ không nhất quán mà không kiểm toán viên nào đối soát được.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Không có đội bảo mật và đường băng ít ỏi, văn hóa là biện pháp kiểm soát duy nhất bạn gánh nổi. Hãy biến một buổi mô hình hóa mối đe dọa 30 phút trên bảng trắng thành thói quen trước bất kỳ tính năng nào chạm vào xác thực hay thanh toán, bật đặc quyền tối thiểu và MFA ở mọi nơi vì chúng không tốn gì, và giữ một kênh không đổ lỗi nơi bất kỳ ai cũng có thể nêu một lo ngại. Bỏ qua quy trình và công cụ nặng nề; các kỹ sư sáng lập không thể duy trì nó, và kỷ luật bạn xây bây giờ là thứ cho phép người mua doanh nghiệp tin bạn sau này.

**Doanh nghiệp nhỏ.** Bạn không có chuyên gia bảo mật riêng và ngân sách eo hẹp, vì vậy hãy dựa vào mặc định an toàn trong các công cụ bạn đã mua thay vì dựng đường ống riêng. Ưu tiên các nền tảng được quản lý thực thi MFA, vá lỗi và đặc quyền tối thiểu giúp bạn, và coi bảo mật là câu hỏi vệ sinh dữ liệu: biết bạn đang giữ dữ liệu nhạy cảm nào và ai có thể với tới nó. Khi bạn phải chọn xây-so-với-mua, hãy mua, vì một biện pháp kiểm soát được quản lý mà bạn giữ cập nhật thắng một cái làm riêng mà bạn để mục nát.

**Doanh nghiệp lớn.** Ở quy mô hàng trăm dịch vụ và hàng nghìn kỹ sư, thách thức là sự nhất quán và quản trị qua nhiều đội. Hãy chạy một chương trình nhà vô địch bảo mật, chuẩn hóa các bậc mô hình hóa mối đe dọa gắn với phân loại CIA, và cung cấp mẫu đường lát sẵn cùng kiểm tra đường ống tự động để mọi đội thừa hưởng mặc định tốt. Hãy theo dõi chỉ số khắc phục và độ bao phủ theo các đường cơ sở, và giữ một dấu vết kiểm toán cho thấy vì sao mỗi hệ thống được mô hình hóa và kiểm soát theo cách đó.

**Chính phủ.** Quy tắc mua sắm, nghĩa vụ minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Các nguyên tắc không tin cậy và thông tin xác thực sống ngắn thường được bắt buộc bởi chính sách hành pháp, và bạn phải có thể cho kiểm toán viên thấy một lý do dựa trên rủi ro, có tài liệu về nơi ngân sách gia cố đã đi. Hãy ưu tiên các hệ thống giữ hồ sơ công dân nhạy cảm nhất trước, công bố các biện pháp bảo vệ ở nơi công chúng có quyền biết, và yêu cầu nhà cung cấp công khai các hạn chế thay vì chấp nhận các hộp đen mờ đục.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp mười người không có đội bảo mật và không có ngân sách cho nó, nên hai kỹ sư sáng lập biến mô hình hóa mối đe dọa thành thói quen bảng trắng 30 phút trước bất kỳ tính năng nào chạm vào xác thực hay thanh toán, hỏi điều gì có thể sai và ai muốn nó xảy ra. Họ áp dụng vài thói quen nền tảng không tốn gì: đặc quyền tối thiểu trên mọi vai trò đám mây, MFA trên mọi tài khoản, và một kênh không đổ lỗi nơi bất kỳ ai cũng có thể nêu lo ngại mà không sợ bị trách. Khi sau này họ gọi vốn và người mua doanh nghiệp hỏi họ xử lý bảo mật thế nào, văn hóa sớm đó cho phép họ trả lời trung thực thay vì chạy vạy bịa ra một cái.

**Doanh nghiệp lớn.** Một ngân hàng toàn cầu với 6.000 kỹ sư chạy một chương trình nhà vô địch bảo mật với một nhà vô địch được đào tạo cho mỗi đội. Nhà vô địch tham dự một hội nhóm hằng tháng, hoàn thành đào tạo hằng quý, và dẫn dắt mô hình hóa mối đe dọa cho mọi dịch vụ mới bằng STRIDE. Đội AppSec trung tâm duy trì các mẫu đường lát sẵn và kiểm tra đường ống tự động. Qua hai năm, thời gian trung vị để khắc phục các phát hiện mức nghiêm trọng cao giảm từ 45 ngày xuống 9, và mô hình hóa mối đe dọa giai đoạn thiết kế đã bắt một lỗi cấp quyền trong một API thanh toán trước khi nó đến môi trường thực, tránh một sự cố phải báo cáo có khả năng xảy ra.

**Chính phủ.** Một cơ quan thuế quốc gia hiện đại hóa hệ thống cũ áp dụng các nguyên tắc không tin cậy do chính sách hành pháp bắt buộc. Mọi lệnh gọi dịch vụ nội bộ được xác thực bằng thông tin xác thực sống ngắn và cấp quyền theo từng yêu cầu; các đoạn mạng không còn trao sự tin cậy. Cơ quan mô hình hóa mối đe dọa cho mỗi dịch vụ hướng đến công dân đối chiếu với các cây tấn công bắt nguồn từ "rút dữ liệu người nộp thuế" và "sửa một tờ khai." Ưu tiên theo rủi ro, căn chỉnh theo các mức tác động CIA, tập trung ngân sách gia cố vào các hệ thống giữ hồ sơ nhạy cảm nhất trước.

## Luận chứng kinh doanh: động lực, ROI và TCO

Chi phí xây dựng văn hóa bảo mật là thật: thời gian của nhà vô địch, đào tạo, công cụ, và lực cản khiêm tốn của việc thực hiện mô hình hóa mối đe dọa và rà soát. Nhưng chi phí đó nhỏ so với chi phí của việc không làm. Một vụ xâm phạm dữ liệu lớn trung bình lên đến hàng triệu khi bạn tính điều tra, thông báo, khắc phục, tiền phạt quy định, rủi ro pháp lý và mất kinh doanh. Các vụ xâm phạm của chính phủ thêm sự gián đoạn sứ mệnh và xói mòn niềm tin công chúng mà không hóa đơn nào nắm bắt hết.

Lợi tức đầu tư bảo mật đến từ ba nơi: **sự cố được tránh** (vụ xâm phạm không bao giờ xảy ra), **chi phí khắc phục giảm** (khiếm khuyết sửa lúc thiết kế tốn một phần nhỏ so với sửa trên môi trường thực), và **phân phối nhanh hơn** (đường lát sẵn và kiểm tra tự động cho phép các đội phát hành tự tin thay vì chờ rà soát thủ công). Khi bạn trình bày lập luận với ban lãnh đạo, hãy đóng khung bảo mật là quản lý rủi ro có nhãn giá, không phải một điều tốt trừu tượng. Hãy cho thấy tổn thất kỳ vọng (khả năng nhân tác động) của các rủi ro hàng đầu, chi phí để giảm chúng, và rủi ro vẫn còn lại. Giám đốc điều hành tài trợ cho việc giảm rủi ro mà họ đo được.

## Phản mẫu và cạm bẫy

- **Sân khấu bảo mật.** Các biện pháp kiểm soát trông ấn tượng nhưng không giảm rủi ro thực, được áp dụng để thỏa mãn một cuộc kiểm toán hơn là để bảo vệ bất cứ thứ gì.
- **Đội bảo mật như một cổng ở cuối.** Phát hiện lỗi thiết kế vào tuần trước khi ra mắt, khi chúng tốn nhất để sửa và có khả năng bị bỏ qua nhất.
- **Văn hóa đổ lỗi.** Trừng phạt kỹ sư báo cáo một sai lầm bảo đảm sai lầm kế tiếp vẫn bị giấu.
- **Mô hình hóa mối đe dọa làm cho có.** Điền một mẫu không ai đọc, tạo ra tài liệu tách rời khỏi kiến trúc thực.
- **Biện pháp kiểm soát một-cỡ-cho-tất-cả.** Áp dụng cùng một quy trình nặng nề cho một trang web công khai và một hệ thống thanh toán, lãng phí công sức và sinh ra oán giận.
- **Ưu tiên do nỗi sợ dẫn dắt.** Đuổi theo bất cứ lỗ hổng nào đang thịnh hành trên tin tức thay vì thứ thực sự đe dọa tài sản của bạn.
- **Nhà vô địch chỉ trên danh nghĩa.** Gọi tên nhà vô địch mà không cho họ thời gian, đào tạo hay thẩm quyền.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Bảo mật là phản ứng và tập trung. Rà soát diễn ra muộn nếu có, và không có mô hình hóa mối đe dọa. Sự cố thúc đẩy các bản sửa tùy nghi. Kỹ sư coi bảo mật là vấn đề của người khác, và không có tiêu chuẩn chung.

**Mức 2: Phát triển.** Một đội bảo mật tồn tại và định nghĩa tiêu chuẩn, nhưng thực hành không nhất quán qua các đội. Một số mô hình hóa mối đe dọa xảy ra trên các dự án lớn và không có ở các dự án khác. Đào tạo cơ bản có sẵn. Bảo mật vẫn bị coi là một cổng chặn, và dịch chuyển sang trái là khát vọng hơn là thực tế.

**Mức 3: Chuẩn hóa.** Nhà vô địch bảo mật được nhúng vào mọi đội. Mô hình hóa mối đe dọa là thường lệ cho dịch vụ mới, được phân bậc theo phân loại CIA, và vòng đời phát triển an toàn được lập tài liệu và thực thi toàn tổ chức. Ưu tiên theo rủi ro dẫn dắt công việc, tiêu chuẩn lập trình an toàn và kiểm tra đường ống là đường lát sẵn mặc định, và các buổi rà soát sau sự cố không đổ lỗi là chuẩn mực.

**Mức 4: Quản lý.** Kết quả bảo mật được đo và kiểm soát theo các đường cơ sở. Tổ chức theo dõi thời gian trung vị để khắc phục các phát hiện mức nghiêm trọng cao, độ bao phủ mô hình mối đe dọa, phần các sự cố được bắt trước môi trường thực, và tỷ lệ báo cáo suýt xảy ra, chia theo từng đội. Thẩm quyền của nhà vô địch để dừng một bản phát hành được xác định và thực sự được thực hiện. Các quyết định rủi ro được định lượng là khả năng nhân tác động, được ghi lại và rà soát theo nhịp cố định, để các khoảng trống kiểm soát hiện ra dưới dạng dữ liệu thay vì bất ngờ.

**Mức 5: Điều phối.** Bảo mật thực sự là việc của mọi người và được tích hợp với phân phối, rủi ro và hoạch định kinh doanh. Mô hình hóa mối đe dọa và thiết kế an toàn là thói quen và nhẹ nhàng, và các nguyên tắc không tin cậy phần lớn đã thành hiện thực. Các chỉ số thúc đẩy cải tiến liên tục, tổ chức học từ các lần suýt xảy ra qua các đội, và các biện pháp kiểm soát tự động thích ứng khi bức tranh mối đe dọa và kiến trúc thay đổi.

## Ý tưởng để thảo luận

1. Làm sao bạn đo liệu một văn hóa bảo mật có thực sự cải thiện, ngoài việc đếm số lần hoàn thành đào tạo?
2. Ranh giới đúng giữa những gì nhà vô địch bảo mật xử lý và những gì đội trung tâm sở hữu nằm ở đâu?
3. Làm sao bạn giữ mô hình hóa mối đe dọa có giá trị mà không để nó thành một ô đánh dấu quan liêu?
4. Một kiến trúc không tin cậy đầy đủ có thực tế với hệ sinh thái cũ của bạn không, và nếu không, tập con thực dụng là gì?
5. Công việc bảo mật nên được ưu tiên thế nào so với phân phối tính năng khi cả hai cạnh tranh cho cùng các kỹ sư?
6. Những động lực nào thực sự thay đổi hành vi của kỹ sư hướng đến quyền sở hữu bảo mật?

## Những điểm cần ghi nhớ

- Bảo mật là một thuộc tính văn hóa của các tổ chức lớn, không phải một nhiệm vụ giao cho một đội.
- Nhà vô địch bảo mật mở rộng chuyên môn và quyền sở hữu qua kỹ thuật.
- Mô hình hóa mối đe dọa (STRIDE, PASTA, cây tấn công) phơi bày lỗi thiết kế sớm và rẻ.
- Một SDLC an toàn và tư duy dịch chuyển sang trái bắt khiếm khuyết khi chúng tốn ít nhất.
- Phòng thủ theo chiều sâu, đặc quyền tối thiểu và không tin cậy là các nguyên tắc kiến trúc nền tảng.
- Bộ ba CIA và ưu tiên theo rủi ro hướng công sức khan hiếm đến nơi nó quan trọng nhất.
- Chi phí xây dựng văn hóa bảo mật nhỏ hơn nhiều so với chi phí của các vụ xâm phạm nó ngăn chặn.

## Tài liệu tham khảo và đọc thêm

- Adam Shostack, *Threat Modelling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard và Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer và cộng sự (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, hướng dẫn *Threat Modelling* và *Security Champions*
