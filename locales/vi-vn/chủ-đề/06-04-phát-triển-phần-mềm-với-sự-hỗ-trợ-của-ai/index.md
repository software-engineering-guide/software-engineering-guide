# 6.4 Phát triển phần mềm với sự hỗ trợ của AI

## Tổng quan và động lực

Các trợ lý lập trình AI nay có thể sinh mã, hoàn thành hàm, viết kiểm thử, giải thích các hệ thống lạ, và giúp bạn [tái cấu trúc](https://en.wikipedia.org/wiki/Code_refactoring). Dùng tốt, chúng tăng tốc công việc thường lệ. Chúng hạ rào cản với các ngôn ngữ và khung phát triển lạ. Chúng lấy đi sự nhàm chán của mã mẫu.

Dùng tồi, chúng gây hại thật. Chúng có thể làm ngập cơ sở mã bằng mã trông hợp lý nhưng sai một cách tinh vi. Chúng có thể đưa vào lỗ hổng bảo mật, tạo rủi ro cấp phép, và làm mòn kỹ năng của các kỹ sư dựa vào chúng. Phát triển có hỗ trợ AI đồng thời là một công cụ năng suất thật và một rủi ro thật. Sự khác biệt gần như hoàn toàn nằm ở kỷ luật kỹ thuật bao quanh nó.

Với các đội lớn, thách thức là tính nhất quán và an toàn ở quy mô. Khi hàng trăm lập trình viên dùng trợ lý AI, những thói quen nhỏ của từng cá nhân cộng lại thành kết quả của tổ chức. Nếu mọi người chấp nhận gợi ý một cách thiếu phản biện, khối lượng rà soát và tỷ lệ lỗi tăng. Nếu bạn cung cấp chuẩn mực rõ ràng, mặc định tốt và xác minh mạnh, cùng những công cụ đó nâng thông lượng mà không hạ chất lượng. Câu chuyện năng suất cũng tinh tế hơn những gì nhà cung cấp tuyên bố. Lợi ích thực khác nhau nhiều theo nhiệm vụ, và cách đo ngây thơ, như đếm gợi ý được chấp nhận, sẽ đánh lừa bạn.

Bối cảnh doanh nghiệp và chính phủ thêm các ràng buộc sắc bén hơn. Mã chạm vào hệ thống chịu quy định, xử lý dữ liệu nhạy cảm, hay vận hành hạ tầng trọng yếu không thể được tin chỉ vì một AI tạo ra nó. Nguồn gốc cấp phép quan trọng khi mã sinh ra có thể lặp lại dữ liệu huấn luyện theo giấy phép hạn chế. Một số tổ chức phải giữ mã nguồn tại chỗ và hoàn toàn không thể gửi nó đến dịch vụ bên ngoài. Đặt ra chuẩn mực rõ ràng, thực thi được cho sự hỗ trợ của AI nay là một phần của lãnh đạo kỹ thuật có trách nhiệm. Trong số các trợ lý hiện có, các công cụ xây trên mô hình Claude của Anthropic là một lựa chọn hàng đầu bên cạnh các công cụ khác; các thực hành dưới đây áp dụng cho bất kỳ cái nào bạn chọn.

*Xem thêm:* chương 2.5 (rà soát mã và cộng tác), chương 2.4 (chiến lược kiểm thử), và chương 6.5 (AI có trách nhiệm và đáng tin cậy).

## Các nguyên tắc chính

- Kỹ sư, không phải trợ lý, chịu trách nhiệm về mọi dòng được commit.
- Mã do AI sinh ra là một bản nháp cần rà soát và xác minh, không bao giờ là sản phẩm hoàn chỉnh để tin cậy.
- Công sức xác minh nên tỷ lệ với rủi ro của mã, không phải với việc đầu ra trông tự tin đến đâu.
- Đo năng suất bằng các kết quả quan trọng (giá trị được giao, chất lượng, thời gian chu kỳ), không phải số gợi ý.
- Bảo vệ chống rủi ro bảo mật và cấp phép đưa vào qua mã sinh ra.
- Giữ gìn và phát triển kỹ năng kỹ thuật của con người; đừng để trợ lý làm rỗng nó.
- Minh bạch về nơi nào và cách nào sự hỗ trợ của AI được dùng.

## Khuyến nghị

### Dùng lập trình cặp với AI như công cụ soạn thảo và khám phá

Hãy hướng trợ lý vào những nhiệm vụ chúng tỏa sáng và lỗi rẻ để bắt: mã mẫu, khung kiểm thử, chuyển đổi định dạng, giải thích mã lạ, và khám phá các cách tiếp cận. Coi đầu ra của chúng là bản nháp đầu tiên. Hãy ở ghế lái. Đọc, hiểu và chỉnh sửa mọi gợi ý thay vì chấp nhận bằng lái tự động. Trong các miền lạ, hãy dùng trợ lý để học, nhưng kiểm tra các khẳng định của nó với tài liệu có thẩm quyền. Trợ lý có thể bịa ra API và nói sai hành vi với sự tự tin tuyệt đối.

### Rà soát, kiểm thử và xác minh mã do AI sinh ra như đầu vào không đáng tin

Hãy cho mã do AI sinh ra sự soi xét như bạn dành cho mã từ một thành viên mới, hoặc hơn. Một người rà soát nên hiểu nó đủ để giải thích và bảo trì nó. "AI đã viết nó" không bao giờ là câu trả lời chấp nhận được cho "vì sao cái này chạy?" Hãy đòi kiểm thử, và cảnh giác với các kiểm thử do AI sinh ra chỉ khẳng định hành vi hiện tại thay vì hành vi dự định. Chạy [phân tích tĩnh](https://en.wikipedia.org/wiki/Static_program_analysis), quét bảo mật và kiểm tra phụ thuộc. Với mã rủi ro cao (xác thực, [mật mã học](https://en.wikipedia.org/wiki/Cryptography), logic tài chính, hệ thống an toàn), hãy coi đầu ra của AI là điểm khởi đầu đòi hỏi xác minh của chuyên gia con người, không bao giờ là có thẩm quyền.

### Đo năng suất trung thực và đặt kỳ vọng thực tế

Bỏ qua các chỉ số phù phiếm như tỷ lệ chấp nhận hay số dòng được sinh ra. Thay vào đó hãy nhìn các tín hiệu phân phối và chất lượng theo thời gian: thời gian chu kỳ, tỷ lệ thay đổi thất bại, tỷ lệ lỗi lọt, và hiệu quả do lập trình viên tự báo cáo. Lợi ích là thật nhưng không đều: lớn với một số nhiệm vụ, không đáng kể hoặc âm với số khác. Thời gian tiết kiệm khi viết mã có thể bị mất lại khi rà soát và gỡ lỗi nó. Hãy đặt kỳ vọng với ban lãnh đạo tương ứng, để khoản đầu tư dựa trên bằng chứng thay vì cường điệu, và để các đội không bao giờ bị ép chấp nhận gợi ý không an toàn chỉ để đạt một chỉ số.

### Quản lý rủi ro bảo mật và cấp phép

Hãy quét mã sinh ra tìm lỗ hổng và mẫu không an toàn. Trợ lý có thể tái tạo các thành ngữ không an toàn từ dữ liệu huấn luyện. Đừng bao giờ dán bí mật, thông tin xác thực hay dữ liệu nhạy cảm vào prompt gửi đến dịch vụ bên ngoài. Ưu tiên các công cụ đáp ứng yêu cầu xử lý dữ liệu của bạn, gồm triển khai tại chỗ hoặc riêng tư nơi mã nguồn không thể rời môi trường. Hãy xử lý cả cấp phép. Mã sinh ra có thể giống dữ liệu huấn luyện có bản quyền, vì vậy hãy dùng công cụ và chính sách giảm rủi ro này, giữ nguồn gốc nơi bạn có thể, và chuyển bất cứ thứ gì đáng ngờ qua rà soát pháp lý. Theo dõi nguồn gốc các phụ thuộc mà trợ lý gợi ý, vì nó có thể đề xuất các gói bị bỏ rơi hoặc độc hại.

### Đặt chuẩn mực đội, công bố và duy trì kỹ năng

Hãy công bố hướng dẫn rõ ràng về khi nào và cách nào sự hỗ trợ của AI được dùng, dữ liệu nào không bao giờ được chia sẻ, và mỗi mức rủi ro đòi hỏi xác minh gì. Khuyến khích minh bạch về các đóng góp có hỗ trợ AI nơi nó quan trọng cho rà soát và trách nhiệm giải trình. Hãy giữ kỹ năng con người sắc bén có chủ đích. Bảo đảm các kỹ sư, đặc biệt là người mới, vẫn học các nền tảng thay vì giao phó sự hiểu biết của mình. Luân chuyển mọi người qua công việc xây chuyên môn sâu, và coi sự lệ thuộc quá mức là rủi ro dài hạn thực sự đối với năng lực của đội.

## Đánh đổi: ưu và nhược điểm

| Khía cạnh | Lợi ích của sự hỗ trợ AI | Rủi ro của sự hỗ trợ AI |
|---|---|---|
| Tốc độ | Mã mẫu và soạn thảo nhanh hơn | Thời gian mất khi rà soát mã sai |
| Làm quen | Vào ngôn ngữ/khung mới dễ hơn | Hiểu nông, API bịa đặt |
| Chất lượng | Nhiều kiểm thử hơn, tái cấu trúc nhanh hơn | Mã trông hợp lý nhưng sai tinh vi |
| Bảo mật | Có thể gợi ý bản sửa và quét | Có thể đưa vào lỗ hổng |
| Kỹ năng | Giải phóng thời gian cho công việc giá trị cao hơn | Làm mòn nền tảng nếu lạm dụng |
| Cấp phép | Tái sử dụng các mẫu phổ biến nhanh hơn | Phơi nhiễm nguồn gốc và giấy phép |

Đánh đổi trung tâm là tốc độ so với xác minh. AI chuyển công sức từ viết sang rà soát. Lợi ích ròng phụ thuộc vào việc thực hành rà soát và xác minh của bạn có đủ mạnh để bắt những gì trợ lý làm sai. Rà soát yếu dẫn đến chất lượng suy giảm. Rà soát mạnh và chuẩn mực rõ ràng nắm bắt phần lợi.

## Câu hỏi để thảo luận với đội của bạn

1. **Những phần nào của cơ sở mã của chúng ta hoàn toàn cấm sự hỗ trợ của AI, và chúng ta thực thi ranh giới đó thế nào?** Lòng tin đồng đều là cái bẫy: áp dụng cùng sự soi xét nhẹ cho xác thực, mật mã học, logic tài chính và hệ thống an toàn như cho mã mẫu là cách những lỗi tinh vi, tự tin đến được các đường trọng yếu. Với một đội lớn, một danh sách tường minh các mô-đun bị loại trừ hoặc chỉ rà soát bởi chuyên gia biến phán đoán cá nhân thành biện pháp bảo vệ của tổ chức. Hãy mang bản đồ rủi ro của cơ sở mã, chính sách hiện tại (nếu có), và cách bạn thực sự ngăn mã sinh ra đáp vào một mô-đun bị hạn chế: kiểm tra đường ống, quy tắc sở hữu, hay cổng rà soát. Trong bối cảnh quốc phòng, chịu quy định và an toàn trọng yếu, một số mô-đun nên loại trừ hoàn toàn sự hỗ trợ của AI. Câu trả lời nên tỷ lệ công sức xác minh với rủi ro của mã, không bao giờ với việc đầu ra trông tự tin đến đâu.

2. **Xu hướng thay đổi thất bại và lỗi lọt thực của chúng ta kể từ khi áp dụng trợ lý là gì, và chúng ta đang đo hay đang đoán?** Tuyên bố năng suất của nhà cung cấp và số đếm tỷ lệ chấp nhận là các chỉ số phù phiếm gây hiểu lầm, vì thời gian tiết kiệm khi viết mã có thể mất lại khi rà soát và gỡ lỗi. Để ban lãnh đạo đầu tư dựa trên bằng chứng thay vì cường điệu, bạn cần các tín hiệu phân phối và chất lượng theo thời gian: thời gian chu kỳ, tỷ lệ thay đổi thất bại, tỷ lệ lỗi lọt, và hiệu quả do lập trình viên tự báo cáo. Hãy mang bất kỳ con số thật nào bạn có, và trung thực nơi bạn không có. Rủi ro cần theo dõi là các đội bị ép chấp nhận gợi ý không an toàn chỉ để đạt một chỉ số. Câu trả lời nên thay số gợi ý bằng các thước đo kết quả, và đặt kỳ vọng rằng lợi ích là thật nhưng không đều, lớn với một số nhiệm vụ và âm với số khác.

3. **Nếu mã sinh ra lặp lại dữ liệu huấn luyện có giấy phép hạn chế hoặc kéo vào một phụ thuộc rủi ro, ai bắt được và khi nào?** Mã sinh ra có thể giống tài liệu có bản quyền hoặc đề xuất các gói bị bỏ rơi hay độc hại, và sự phơi nhiễm đó đáp vào sản phẩm của bạn dù có ai nhận ra hay không. Với doanh nghiệp và chính phủ, nguồn gốc cấp phép và rủi ro chuỗi cung ứng mang trọng lượng pháp lý mà cái nhún vai "AI đã viết nó" không qua nổi. Hãy mang việc quét bí mật hiện tại, kiểm tra giấy phép, và theo dõi nguồn gốc phụ thuộc, và xác định đường ống chạy từng cái ở đâu. Hãy thảo luận cái gì chuyển mã đáng ngờ qua rà soát pháp lý và ai sở hữu quyết định đó. Nếu bí mật có thể bị dán vào công cụ bên ngoài hoặc các gói chưa kiểm duyệt có thể hợp nhất mà không bị thách thức, hãy đóng các lỗ hổng đó trước khi mở rộng việc dùng trợ lý qua đội.

4. **Làm sao chúng ta giữ các kỹ sư, đặc biệt là người mới, học các nền tảng thay vì giao phó sự hiểu biết cho trợ lý?** Teo mòn kỹ năng là rủi ro chậm không bao giờ hiện trong vận tốc quý này, rồi hiện ra nhiều năm sau như một đội không thể gỡ lỗi, thiết kế hay rà soát mà không có prompt. Với một tổ chức lớn, lực kéo đối lập là có thật: trợ lý cho kỹ sư mới phát hành nhanh hơn hôm nay, và áp lực đạt mục tiêu phân phối chống lại công việc chậm hơn của việc xây chuyên môn sâu. Hãy mang bằng chứng về cách người của bạn thực sự trưởng thành: bao nhiêu phần người mới có thể giải thích mã họ đã hợp nhất, bao nhiêu giải quyết vấn đề không hỗ trợ mà việc làm quen của bạn vẫn đòi hỏi, và liệu các lần rà soát bắt được hiểu nông hay chỉ đóng dấu đầu ra chạy được. Hãy luân chuyển có chủ đích mọi người qua công việc xây sự thành thạo, và coi sự lệ thuộc quá mức là rủi ro năng lực, không phải khuyết điểm cá nhân. Trong chính phủ và các hệ thống trọng yếu sống lâu, lực lượng lao động có thể cần xây và xác minh hệ thống hàng thập kỷ mà không có công cụ nhà cung cấp, nên một lộ trình đào tạo bảo đảm các nền tảng trực tiếp là yêu cầu liên tục, không phải điều dễ chịu.

5. **Chúng ta thực sự được phép dùng trợ lý nào, cho nơi mã nguồn và dữ liệu phải ở lại, và làm sao ngăn một bí mật chạm đến prompt?** Ràng buộc xử lý dữ liệu quyết định công cụ trước năng suất: một trợ lý phát mã nguồn của bạn đến một dịch vụ bên ngoài có thể bị loại hoàn toàn, bất kể năng lực của nó. Với một đội lớn, căng thẳng là giữa sự tiện lợi của công cụ lưu trữ tốt nhất và yêu cầu rằng mã sở hữu, thông tin xác thực và dữ liệu nhạy cảm không bao giờ rời ranh giới của bạn. Hãy mang bản đồ phân loại dữ liệu, các tùy chọn triển khai mỗi công cụ ứng viên cung cấp (lưu trữ, riêng tư, tại chỗ), và các kiểm soát cụ thể giữ bí mật khỏi prompt: quét trước commit, lọc prompt, và đào tạo kỹ sư. Hãy quyết định công cụ nào được phép cho loại mã nào, và làm ranh giới thực thi được thay vì chỉ khuyến cáo. Trong bối cảnh chịu quy định, quốc phòng và mật, triển khai tại chỗ hoặc cách ly không khí có thể là lựa chọn hợp pháp duy nhất, và việc gửi mã nguồn đến bất kỳ dịch vụ bên ngoài nào phải bị cấm và chặn về mặt kỹ thuật, không chỉ bị can ngăn.

6. **Làm sao chúng ta biến thói quen cá nhân rải rác thành chuẩn mực nhất quán toàn tổ chức, và ai sở hữu chính sách khi công cụ tiến hóa?** Khi hàng trăm lập trình viên mỗi người tự ứng biến cách tiếp cận riêng, thói quen nhỏ cộng dồn thành kết quả tổ chức, và xác minh không nhất quán là nơi lỗi và phơi nhiễm lọt qua. Cân nhắc đối lập là tự chủ: các đội bực bội với mệnh lệnh trung ương nặng nề, vậy mà một cuộc tự do thì tạo ra chất lượng không đồng đều và không có biện pháp bảo vệ chung. Hãy mang hướng dẫn hiện tại (nếu có), bằng chứng nó được tuân theo đồng đều đến đâu, và một đề xuất về các mặc định tốt được nướng vào đường ống để con đường an toàn là con đường dễ. Hãy nêu tên một chủ sở hữu giữ chính sách hiện hành khi trợ lý đổi mỗi vài tháng, và một chuẩn mực công bố để người rà soát biết khi nào sự hỗ trợ của AI đã định hình một đóng góp. Với một doanh nghiệp hay cơ quan công, hãy gắn chuẩn mực với kiểm toán và trách nhiệm giải trình: một tiêu chuẩn có tài liệu, được thực thi mà kiểm toán viên có thể kiểm tra thắng một thực hành dân gian khác nhau theo đội và biến mất khi một người then chốt rời đi.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không có đường băng để lãng phí, hãy dựa vào trợ lý lưu trữ cho mã mẫu, kiểm thử và khung lạ, và để chúng tăng tốc công việc thường lệ. Giữ một quy tắc không thể thương lượng: một con người hiểu thay đổi rà soát mọi lần hợp nhất, vì một dòng sai tinh vi trong cơ sở mã năm người không có chỗ ẩn và không có ai khác để bắt. Thêm bộ quét bí mật và kiểm tra giấy phép sớm; chúng rẻ và ngăn các sai lầm đắt đỏ bạn không thể dọn sau.

**Doanh nghiệp nhỏ.** Bạn có lẽ không có chuyên gia bảo mật và ngân sách eo hẹp, vì vậy hãy ưu tiên trợ lý nhúng trong các công cụ bạn đã tin hơn là một thiết lập đặt riêng bạn phải bảo trì. Hãy đóng khung rủi ro bằng lời đơn giản: đừng bao giờ dán dữ liệu khách hàng hay thông tin xác thực vào prompt bên ngoài, và coi mã sinh ra chạm đến thanh toán hay xác thực là bản nháp để xác minh, không phải câu trả lời hoàn chỉnh. Chọn nhà cung cấp có điều khoản xử lý dữ liệu bạn thực sự đọc được và có tính năng AI bạn có thể tắt nếu chúng hành xử sai.

**Doanh nghiệp lớn.** Vấn đề là nhất quán và an toàn qua nhiều đội: chuẩn mực dùng chung theo mức rủi ro, rà soát và quét bắt buộc trong đường ống, và các chỉ số phân phối và chất lượng trung thực thay vì số chấp nhận. Hãy chuẩn hóa lựa chọn công cụ và mô hình triển khai để mã sở hữu ở trong ranh giới của bạn, lập ngân sách chi phí rà soát và sửa chữa mà trợ lý chuyển sang người rà soát, và loại trừ hoặc chặn cổng tường minh các mô-đun rủi ro cao. Hãy quản lý sự hỗ trợ của AI như một năng lực được quản trị có chủ sở hữu, không phải một mớ thói quen cá nhân.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy ưu tiên triển khai tại chỗ hoặc riêng tư nơi mã nguồn và dữ liệu nhạy cảm không thể rời môi trường, cấm gửi mã đến dịch vụ bên ngoài, và yêu cầu công bố các đóng góp có hỗ trợ AI để các quyết định vẫn kiểm toán được. Hãy bắt buộc quét bảo mật và cấp phép trên mọi mã sinh ra, loại trừ sự hỗ trợ của AI khỏi các mô-đun an toàn trọng yếu và mật, và giữ một lộ trình đào tạo bảo đảm lực lượng lao động công có thể xây và xác minh hệ thống mà không cần công cụ nhà cung cấp trong suốt vòng đời dài của các hệ thống nó sở hữu.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp SaaS sáu kỹ sư áp dụng trợ lý lập trình AI để đi nhanh hơn ở công việc thường lệ. Họ dựa vào chúng cho mã mẫu, kiểm thử và mã khung lạ, nhưng giữ quy tắc chắc chắn rằng một con người hiểu thay đổi phải rà soát mọi pull request, và thêm bộ quét bí mật và kiểm tra giấy phép vào đường ống. Với mã thanh toán và xác thực, các kỹ sư coi đầu ra của AI là bản nháp thô để xác minh từng dòng thay vì tin. Họ theo dõi thời gian chu kỳ và lỗi lọt thay vì đếm gợi ý được chấp nhận, và giữ được lợi ích mà không để chất lượng trượt.

**Doanh nghiệp lớn.** Một công ty thương mại điện tử lớn triển khai trợ lý lập trình AI với lan can. Họ cấm bí mật trong prompt. Họ yêu cầu con người rà soát, người rà soát được kỳ vọng hiểu mã. Họ thêm quét bảo mật trong đường ống và chọn triển khai riêng tư để mã sở hữu không bao giờ rời môi trường. Họ đo tác động qua thời gian chu kỳ và tỷ lệ thay đổi thất bại thay vì số chấp nhận. Họ thấy lợi ích vững chắc ở mã mẫu và kiểm thử, nhưng nhất quyết rà soát chuyên gia cho mã thanh toán, nơi họ coi đầu ra của AI là không đáng tin.

**Chính phủ.** Một tổ chức phần mềm quốc phòng chỉ cho phép sự hỗ trợ của AI qua một công cụ tại chỗ giữ mã mật và nhạy cảm trong ranh giới. Họ cấm gửi mã nguồn đến bất kỳ dịch vụ bên ngoài nào. Họ yêu cầu công bố các đóng góp có hỗ trợ AI trong rà soát mã và bắt buộc quét bảo mật và cấp phép trên mọi mã sinh ra. Họ loại trừ hoàn toàn sự hỗ trợ của AI khỏi một số mô-đun an toàn trọng yếu. Các kỹ sư mới theo một lộ trình đào tạo bảo đảm họ học nền tảng trực tiếp, để lực lượng lao động không mất khả năng xây và xác minh hệ thống mà không có hỗ trợ.

## Luận chứng kinh doanh: động lực, ROI và TCO

Động lực là phân phối nhanh hơn và bớt nhàm chán, để nhân tài kỹ thuật khan hiếm của bạn tập trung vào thiết kế, phán đoán và các vấn đề khó. ROI hiện ra là thời gian chu kỳ giảm cho các nhiệm vụ phù hợp và trải nghiệm lập trình viên được cải thiện, nhưng chỉ nơi xác minh giữ chất lượng cao. Các tuyên bố ROI ngây thơ dựa trên số gợi ý là gây hiểu lầm, và bạn nên bác bỏ chúng.

TCO bao gồm giấy phép công cụ, triển khai an toàn hoặc tại chỗ, quét bảo mật và cấp phép, và chi phí thường bị đánh giá thấp của việc rà soát và sửa đầu ra của AI. Chi phí của việc *không* áp dụng mang tính cạnh tranh: đối thủ có thể phân phối nhanh hơn và thu hút nhân tài kỳ vọng công cụ hiện đại. Chi phí của việc áp dụng cẩu thả là chất lượng xói mòn, sự cố bảo mật và phơi nhiễm pháp lý. Hãy lập luận với ban lãnh đạo bằng một chương trình thí điểm đo kết quả phân phối và chất lượng thực, ghép với một kế hoạch cụ thể về chuẩn mực, xác minh và bảo vệ dữ liệu.

## Phản mẫu và cạm bẫy

- **Chấp nhận bằng lái tự động.** Commit gợi ý mà không đọc hay hiểu chúng.
- **Chỉ số phù phiếm.** Đánh giá thành công qua tỷ lệ chấp nhận hay số dòng được sinh.
- **Bí mật trong prompt.** Dán thông tin xác thực hay dữ liệu nhạy cảm vào công cụ bên ngoài.
- **Tin kiểm thử của AI.** Chấp nhận kiểm thử sinh ra khóa chặt hành vi hiện tại, không phải hành vi dự định.
- **Bỏ qua nguồn gốc.** Bỏ sót rủi ro giấy phép và phụ thuộc trong mã sinh ra.
- **Teo mòn kỹ năng.** Để người mới giao phó sự hiểu biết và không bao giờ học nền tảng.
- **Lòng tin đồng đều.** Áp dụng cùng sự soi xét thấp cho mã an toàn trọng yếu như cho mã mẫu.

## Mô hình trưởng thành

1. **Khởi đầu.** Cá nhân dùng trợ lý tùy nghi và phản ứng; không chính sách, không đo lường; bí mật và sở hữu trí tuệ gặp rủi ro, và mã sinh ra được hợp nhất với bất kỳ sự soi xét nào mỗi người tình cờ áp dụng.
2. **Phát triển.** Hướng dẫn sử dụng cơ bản và quy tắc dữ liệu tồn tại, và một số quét bảo mật chạy, nhưng thực hành không nhất quán qua các đội: độ sâu xác minh khác nhau theo người, tuyên bố năng suất mang tính giai thoại, và mã rủi ro cao không được chặn cổng đáng tin cậy.
3. **Chuẩn hóa.** Chuẩn mực theo mức rủi ro được lập tài liệu và thực thi toàn tổ chức: rà soát bắt buộc của con người, quét bảo mật và cấp phép trong đường ống, triển khai an toàn hoặc tại chỗ khi cần, thực hành công bố, và một danh sách tường minh các mô-đun bị loại trừ hoặc chỉ rà soát bởi chuyên gia.
4. **Quản lý.** Thực hành được đo và kiểm soát theo đường cơ sở: thời gian chu kỳ, tỷ lệ thay đổi thất bại và tỷ lệ lỗi lọt được theo dõi trước và sau khi áp dụng, chi phí rà soát và sửa chữa được định lượng, sự cố rò bí mật và phơi nhiễm giấy phép được đếm, và các quyết định tiếp tục hay dừng về công cụ và mở rộng dựa trên bằng chứng đó thay vì tuyên bố của nhà cung cấp.
5. **Điều phối.** Sự hỗ trợ của AI được cải thiện liên tục và tích hợp trong toàn tổ chức: xác minh được xây vào đường ống như đường đi mặc định, phát triển kỹ năng có chủ đích và được theo dõi, chính sách thích ứng khi công cụ đổi mỗi vài tháng, và tổ chức thường xuyên đánh giá lại, thay thế và thu hẹp phạm vi các trợ lý khi bằng chứng và bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

- Yêu cầu xác minh nên khác nhau thế nào giữa mã mẫu và mã an toàn trọng yếu?
- Chỉ số năng suất nào thực sự phản ánh giá trị từ sự hỗ trợ của AI trong bối cảnh của bạn?
- Khi nào, nếu có, các đóng góp có hỗ trợ AI nên được công bố?
- Làm sao bạn ngăn xói mòn kỹ năng, đặc biệt với kỹ sư mới?
- Ràng buộc xử lý dữ liệu nào chi phối công cụ bạn được dùng?
- Làm sao bạn quản lý rủi ro cấp phép và nguồn gốc từ mã sinh ra?

## Những điểm cần ghi nhớ

- Kỹ sư vẫn chịu trách nhiệm; đầu ra của AI là bản nháp không đáng tin cần xác minh.
- Tỷ lệ xác minh với rủi ro, và đừng bao giờ tin mã AI an toàn trọng yếu mà không có rà soát của chuyên gia.
- Đo kết quả phân phối và chất lượng thực, không phải số gợi ý.
- Bảo vệ chống rủi ro bảo mật, rò rỉ dữ liệu và cấp phép bằng chính sách và công cụ.
- Đặt chuẩn mực rõ ràng và có chủ đích giữ gìn kỹ năng kỹ thuật của con người.

## Tài liệu tham khảo và đọc thêm

- Nicole Forsgren, Jez Humble và Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (về kỳ vọng thực tế và đo lường).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (về sự hiểu biết so với hiện vật mã).
- Titus Winters, Tom Manshreck và Hyrum Wright, *Software Engineering at Google*.
- GitClear và các nghiên cứu ngành liên quan về xu hướng chất lượng mã có hỗ trợ AI.
