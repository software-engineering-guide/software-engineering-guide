# 3.6 Hiện đại hóa hệ thống cũ

## Tổng quan và động lực

[Hệ thống cũ](https://en.wikipedia.org/wiki/Legacy_system) là những hệ thống vận hành thế giới. Các sổ cái ngân hàng lõi, công cụ thuế và trợ cấp, hệ thống kiểm soát không lưu và quốc phòng, quản lý hợp đồng bảo hiểm, và các sổ đăng ký chính phủ mà xã hội dựa vào thường đã có tuổi đời hàng thập kỷ. Nhiều hệ thống được viết bằng [COBOL](https://en.wikipedia.org/wiki/COBOL) (Ngôn ngữ Hướng Kinh doanh Thông dụng) hoặc các công nghệ cũ hơn, và chúng vẫn xử lý phần lớn các giao dịch quan trọng. "Hệ thống cũ" không phải là một lời xúc phạm. Nó có nghĩa là hệ thống đủ giá trị để sống sót, đủ quan trọng để thất bại là thảm họa, và đủ cũ để thay đổi nó một cách an toàn là khó. Hiện đại hóa hệ thống cũ là kỷ luật cải thiện, di chuyển hoặc thay thế các hệ thống này mà không phá vỡ các dịch vụ thiết yếu chúng cung cấp.

Đây là vấn đề mang tính doanh nghiệp và chính phủ một cách không cân xứng, và là nơi xảy ra các thất bại CNTT lớn nhất, công khai nhất. Một phần rất lớn các giao dịch chính trên toàn thế giới vẫn chạm vào các hệ thống [máy tính lớn](https://en.wikipedia.org/wiki/Mainframe_computer). Một phần lớn mã sản xuất trong các tổ chức lớn nằm trong các ngôn ngữ cũ do một nhóm chuyên gia già đi, thu hẹp duy trì. Chính phủ mang gánh nặng nhất: nghĩa vụ luật định được mã hóa qua nhiều thập kỷ, chu kỳ mua sắm và ngân sách tồn tại lâu hơn các nhiệm kỳ chính quyền, và dịch vụ công dân không thể bị gián đoạn. Rủi ro chủ đạo không phải là những hệ thống này cũ, vì nhiều hệ thống chạy xuất sắc. Mà là kiến thức để duy trì chúng đang nghỉ hưu, các nền tảng ngày càng tốn kém và bị ràng buộc, và cám dỗ "cứ viết lại nó" dẫn đến một số thất bại đắt đỏ nhất trong lịch sử lĩnh vực này.

Chương này bao quát các mẫu hiện đại hóa tăng dần thực sự hiệu quả (cây đa bóp nghẹt và phân nhánh bằng trừu tượng), cách đánh giá và ưu tiên rủi ro hệ thống cũ, việc quản lý các hệ sinh thái máy tính lớn và COBOL, kỷ luật [di chuyển dữ liệu](https://en.wikipedia.org/wiki/Data_migration) và chạy song song, và trên hết là cách cưỡng lại cám dỗ viết lại lớn. Niềm tin trung tâm là hiện đại hóa thành công hầu như luôn tăng dần, dựa trên bằng chứng, và liên tục mang lại giá trị. Nó không bao giờ là một cú nổ lớn kéo dài nhiều năm.

## Các nguyên tắc chính

- **Hệ thống cũ nghĩa là có giá trị và mang tính nền tảng, không chỉ đơn thuần là già.** Hãy tôn trọng những gì hệ thống làm trước khi bạn chạm vào; nó mã hóa hàng thập kỷ quy tắc nghiệp vụ khó khăn mới có.
- **Tăng dần thắng nổ lớn, gần như luôn luôn.** Thay thế từng mảnh sau một giao diện ổn định; mang lại giá trị liên tục và giữ rủi ro nhỏ.
- **Viết lại lớn là chế độ thất bại mặc định.** Viết lại toàn bộ thường xuyên vượt tiến độ, giao thiếu, và bị hủy; hãy nhìn thôi thúc này với sự nghi ngờ sâu sắc.
- **Bạn không thể hiện đại hóa những gì bạn không hiểu.** [Kỹ thuật đảo ngược](https://en.wikipedia.org/wiki/Reverse_engineering) và lập tài liệu hành vi (bao gồm các quy tắc không có tài liệu) trước khi thay thế nó.
- **Di chuyển dữ liệu là nơi các dự án chết.** Dữ liệu cũ hơn, bẩn hơn và vướng víu hơn bất cứ ai mong đợi; hãy lên kế hoạch cho nó như một nỗ lực hạng nhất.
- **Chạy cũ và mới song song để xây dựng niềm tin.** Chạy kép và so sánh bắt các sai lệch trước khi chuyển đổi.
- **Ưu tiên theo rủi ro và giá trị, không theo tuổi.** Hiện đại hóa cái rủi ro nhất và giá trị nhất trước, không phải cái đơn giản là cũ nhất.
- **Giữ đèn sáng trong khi bạn thay động cơ.** Dịch vụ phải tiếp tục chạy suốt; không có thời gian ngừng chấp nhận được đối với các hệ thống công dân hay tài chính quan trọng.

## Khuyến nghị

### Hiện đại hóa tăng dần bằng mẫu cây đa bóp nghẹt

**Cây đa bóp nghẹt** (đặt tên theo loài dây leo mọc quanh một cái cây và dần dần thay thế nó) là con ngựa thồ của hiện đại hóa an toàn. Đặt một tầng định tuyến (cổng API, mặt tiền hoặc proxy) phía trước hệ thống cũ. Sau đó, từng năng lực một, xây bản thay thế trong một hệ thống hiện đại và chuyển hướng phần lưu lượng đó sang nó, để phần còn lại trên hệ thống cũ. Theo thời gian hệ thống mới lớn lên và hệ thống cũ thu nhỏ, cho đến khi nó có thể được loại bỏ. Điều này mang lại giá trị liên tục, giữ mỗi thay đổi nhỏ và đảo ngược được, tránh một cuộc chuyển đổi rủi ro, và cho phép bạn dừng hoặc ưu tiên lại bất cứ lúc nào. Nó là điều ngược lại của nổ lớn. Hệ thống cũ tiếp tục chạy và tiếp tục kiếm sống trong khi bạn thay thế nó xung quanh.

### Dùng phân nhánh bằng trừu tượng cho các đường nối nội bộ

Khi bạn cần thay thế một thành phần mà nhiều phần của hệ thống phụ thuộc vào, hãy dùng **phân nhánh bằng trừu tượng**. Đưa vào một tầng trừu tượng (một giao diện) trên cài đặt hiện có, di chuyển các bên gọi để phụ thuộc vào trừu tượng, xây cài đặt mới phía sau cùng trừu tượng đó, chuyển đổi (thường sau một [cờ tính năng](https://en.wikipedia.org/wiki/Feature_toggle), dần dần), và cuối cùng gỡ bỏ cài đặt cũ. Điều này cho phép một thành phần lớn được thay thế tăng dần trên dòng phát triển chính mà không cần một nhánh sống lâu, giữ hệ thống có thể phát hành suốt thời gian. Nó kết hợp tự nhiên với cây đa bóp nghẹt: mặt tiền xử lý các đường nối bên ngoài, phân nhánh bằng trừu tượng xử lý các đường nối bên trong.

### Đánh giá và ưu tiên rủi ro hệ thống cũ một cách có chủ đích

Trước khi hiện đại hóa, hãy xây dựng một bản kiểm kê và đánh giá rủi ro tỉnh táo về toàn bộ hệ sinh thái. Với mỗi hệ thống, chấm điểm theo mức độ quan trọng với kinh doanh, rủi ro kỹ thuật (lỗi thời, nền tảng không còn được hỗ trợ, phơi nhiễm bảo mật), tần suất thay đổi, và quan trọng nhất là **rủi ro kiến thức** (bao nhiêu người vẫn có thể duy trì nó, và họ gần nghỉ hưu đến đâu). Vẽ các hệ thống lên một lưới rủi ro-so-với-giá-trị. Ưu tiên hiện đại hóa cái vừa rủi ro cao vừa giá trị cao. Cân nhắc để yên các hệ thống ổn định, ít thay đổi, được hiểu rõ ngay cả khi chúng cũ, vì một hệ thống đang chạy tốt mà không ai cần thay đổi không phải là một tình huống khẩn cấp. Việc đánh giá này biến "mọi thứ đều cũ và đáng sợ" thành một lộ trình có thể bảo vệ, có trình tự.

### Quản lý hệ sinh thái máy tính lớn và COBOL, không chỉ thay thế nó

Không phải mọi hệ thống máy tính lớn hay COBOL nên, hoặc có thể một cách an toàn, được thay thế sớm. Ưu tiên ngắn hạn thường là **quản lý**: nắm bắt kiến thức trước khi nó nghỉ hưu. Hãy lập tài liệu các quy tắc nghiệp vụ mà mã mã hóa (phần lớn không có tài liệu và không thể thay thế), đầu tư vào các bài kiểm thử tự động ghim hành vi hiện tại để thay đổi trong tương lai an toàn, tuyển dụng và đào tạo chéo người bảo trì, và hiện đại hóa các thực hành phân phối xung quanh (quản lý mã nguồn, [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI), kiểm thử tự động) ngay cả khi lõi vẫn giữ nguyên. Ở nơi bạn hiện đại hóa, ưu tiên phơi bày các năng lực cũ qua API hiện đại (đóng gói) như bước đầu tiên. Hãy xử lý việc dịch COBOL-sang-ngôn-ngữ-hiện-đại tự động một cách thận trọng, vì nó tạo ra mã chạy được nhưng thường tái tạo trung thành logic khó hiểu. Nguồn lực khan hiếm nhất là sự thấu hiểu, không phải sức tính toán.

### Coi di chuyển dữ liệu và chạy kép là cốt lõi của dự án

Phần khó nhất và rủi ro nhất của hầu hết các nỗ lực hiện đại hóa là **dữ liệu**. Nó đồ sộ, chất lượng kém và không nhất quán, và đầy ý nghĩa không có tài liệu tích tụ qua nhiều thập kỷ. Hãy phân tích hồ sơ và làm sạch nó, ánh xạ lược đồ cũ sang mới một cách tường minh, và xây dựng di chuyển tự động, lặp lại được với đối soát đầy đủ (số đếm, checksum, tổng nghiệp vụ) để bạn chứng minh không có gì bị mất hay thay đổi. Giảm rủi ro chuyển đổi bằng **chạy kép** (chạy song song): vận hành hệ thống cũ và mới cạnh nhau trên cùng đầu vào và so sánh đầu ra cho đến khi hệ thống mới khớp với hệ thống cũ đến ngưỡng tin cậy của bạn. Chỉ khi đó mới chuyển đổi, và giữ khả năng hoàn tác. Với các hệ thống thực sự quan trọng, hãy di chuyển và chuyển đổi theo từng lát thay vì tất cả cùng lúc.

### Quản lý cám dỗ viết lại lớn

Bản năng vứt bỏ hệ thống cũ lộn xộn và xây một hệ thống mới sạch từ đầu rất mạnh, và nó gần như luôn sai với các hệ thống lớn, quan trọng. Viết lại toàn bộ đánh giá thấp giá trị ẩn trong mã "xấu xí" (trường hợp biên, quy tắc quy định, hành vi tương thích-lỗi mà người dùng thật phụ thuộc), mất nhiều thời gian hơn dự kiến rất nhiều, không mang lại giá trị nào cho đến cuối, và thường bị hủy sau khi chi tiêu khổng lồ. Hãy mặc định hiện đại hóa tăng dần. Dành viết lại cho các trường hợp nền tảng thực sự không bền vững và các con đường tăng dần đã cạn. Ngay cả khi đó, hãy phân rã việc viết lại thành các mảnh có thể giao độc lập qua mẫu bóp nghẹt thay vì một bản phát hành nổ lớn duy nhất. Khi ban lãnh đạo thúc đẩy viết lại toàn bộ, hãy kiên quyết đặt câu hỏi: giá trị nào được phát hành trong ba tháng đầu, và điều gì xảy ra nếu chương trình bị dừng giữa chừng?

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Cây đa bóp nghẹt (tăng dần) | Giá trị liên tục, rủi ro thấp, đảo ngược được, giữ dịch vụ chạy | Tổng thời gian dài hơn, phải chạy hai hệ thống song song, chi phí tích hợp |
| Viết lại nổ lớn | Tờ giấy trắng, mã mới không bị ràng buộc bởi hệ thống cũ | Tỷ lệ thất bại rất cao, không có giá trị đến cuối, chi phí khổng lồ, mất quy tắc nghiệp vụ |
| Đóng gói (bọc bằng API) | Nhanh, rủi ro thấp, hiện đại hóa truy cập mà không chạm lõi | Lõi vẫn là hệ thống cũ; trì hoãn, không giải quyết, rủi ro cơ bản |
| Để nguyên (quản lý) | Không có rủi ro dự án; rẻ nhất ngắn hạn | Rủi ro kiến thức và nền tảng tiếp tục tích tụ; cuối cùng bị buộc hành động |

Đánh đổi cơ bản là tốc độ chuyển đổi so với rủi ro thất bại, và hiện đại hóa hệ thống cũ là miền nơi sự đánh đổi này lệch nhất. Việc viết lại nổ lớn "nhanh, sạch" là ảo ảnh liên tục tạo ra kết quả chậm nhất và đắt nhất: một chương trình bị hủy và một hệ thống vẫn chưa được hiện đại hóa. Các cách tiếp cận tăng dần có vẻ chậm hơn và đòi hỏi chạy hai hệ thống song song, nhưng chúng mang lại giá trị suốt quá trình, giữ rủi ro nhỏ và đảo ngược được, và là con đường đáng tin cậy theo kinh nghiệm. Phán đoán thực sự là giữa việc quản lý một hệ thống cũ ổn định thêm một thời gian và bắt đầu thay thế tăng dần ngay bây giờ. Hãy để quỹ đạo rủi ro dẫn dắt quyết định đó, đặc biệt là rủi ro kiến thức, thay vì sự khó chịu với công nghệ cũ.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn có chỗ để đặt một tầng định tuyến phía trước hệ thống cũ không, và nếu không, cần gì để tạo ra một cái?** Cây đa bóp nghẹt phụ thuộc vào một đường nối: một cổng API, mặt tiền hoặc proxy mà qua đó bạn có thể chuyển hướng từng năng lực một sang cài đặt mới. Nhiều hệ thống cũ không có đường nối như vậy, nên bước tăng dần hiện đại hóa đầu tiên thường chỉ là xây điểm chặn, và công việc đó dễ bị đánh giá thấp. Hãy mang sơ đồ tích hợp hiện tại và hỏi lưu lượng có thể bị chặn ở đâu theo từng năng lực mà không cần chuyển đổi nổ lớn. Nếu không có chỗ nào, phân nhánh bằng trừu tượng trên một đường nối nội bộ có thể là bước khởi đầu thay thế. Không có tầng định tuyến thì bạn không có con đường tăng dần, đúng là cách các tổ chức bị đẩy trở lại việc viết lại vốn thường thất bại.

2. **Bạn đã thực sự vẽ hệ sinh thái của mình lên lưới rủi ro-so-với-giá-trị chưa, hay lộ trình của bạn bị dẫn dắt bởi hệ thống nào cảm thấy cũ nhất?** Chương này nhấn mạnh bạn hiện đại hóa cái rủi ro cao và giá trị cao trước, và cố ý để yên các hệ thống ổn định, ít thay đổi, được hiểu rõ ngay cả khi chúng cổ xưa. Không có lưới tường minh, sự chú ý chảy về lời phàn nàn to nhất hoặc công nghệ ít hợp thời nhất, và những quả bom hẹn giờ thực sự (một hệ thống quan trọng với hai người bảo trì gần nghỉ hưu) phải chờ. Hãy chấm điểm mỗi hệ thống theo mức độ quan trọng kinh doanh, rủi ro kỹ thuật, tần suất thay đổi và rủi ro kiến thức, rồi sắp trình tự từ góc trên-bên-phải. Hãy mang lưới đó đến cuộc họp làm bản đồ chung. Rủi ro kiến thức xứng đáng được gán trọng số nặng nhất, vì đó là đầu vào duy nhất chỉ tệ đi và không thể mua lại khi con người đã rời đi.

3. **Khi bạn chuyển đổi, bạn sẽ chứng minh thế nào rằng không một bản ghi nào bị mất hay thay đổi, và ai ký duyệt bằng chứng đó?** Di chuyển dữ liệu là nơi các dự án này chết, và niềm tin đến từ đối soát: số hàng, checksum, và tổng kiểm soát nghiệp vụ khớp nhau giữa cũ và mới, cộng với chạy kép so sánh đầu ra trên cùng đầu vào cho đến khi chúng khớp ở ngưỡng cao. Với một hệ thống trợ cấp hay sổ cái, một sai lệch là một công dân bị trả thiếu hoặc một xu bị mất, nên bằng chứng phải làm hài lòng một kiểm toán viên, không chỉ một kỹ sư. Hãy quyết định ngay bây giờ bạn sẽ đối soát các tổng nào, ngưỡng tin cậy nào kích hoạt chuyển đổi, và bạn sẽ chạy cũ và mới song song trong bao lâu. Giữ khả năng hoàn tác suốt thời gian, và chuyển đổi theo từng lát thay vì tất cả cùng lúc. Những sai lệch bạn tìm thấy trong chạy kép thường là các quy tắc hệ thống cũ không có tài liệu mà bạn phải bảo tồn, nên hãy coi mỗi cái là một khám phá, không chỉ là một lỗi.

4. **Hệ thống cũ nào của bạn đang được quản lý so với đang được chủ động thay thế, và ai quyết định cái nào là cái nào?** Chương này vạch một lằn ranh có chủ đích giữa các hệ thống đáng ổn định tại chỗ (lập tài liệu quy tắc, thêm kiểm thử đặc tính, đào tạo chéo người bảo trì) và các hệ thống đáng thay thế tăng dần, và hai loại đòi hỏi tài trợ và nhân sự rất khác nhau. Với một tổ chức lớn mối nguy là sự trôi dạt: một hệ thống được gắn nhãn "quản lý tạm thời" âm thầm thành "quản lý mãi mãi" cho đến khi người bảo trì cuối cùng nghỉ hưu và lựa chọn được đưa ra thay bạn trong khủng hoảng. Các cân nhắc đối lập là chi phí quản lý và sự lỗi thời của nền tảng ở một bên, so với rủi ro và xáo trộn của việc thay thế ở bên kia, và rủi ro kiến thức nên làm cán cân nghiêng vì nó chỉ tệ đi. Hãy mang lưới rủi ro-so-với-giá-trị, số người bảo trì và chân trời nghỉ hưu của từng hệ thống, và một chủ sở hữu tường minh cho quyết định quản-lý-hay-thay-thế. Trong các hệ sinh thái doanh nghiệp và chính phủ, hãy nêu tên một nhịp rà soát và một viên chức chịu trách nhiệm cho từng hệ thống, vì một phân loại không ai xem lại là một quyết định không ai đang đưa ra.

5. **Khi ban lãnh đạo yêu cầu viết lại toàn bộ, câu trả lời thường trực của bạn là gì, và bạn có thể cho thấy một con đường tăng dần phát hành gì trong ba tháng đầu không?** Viết lại nổ lớn là chế độ thất bại mặc định, nhưng nó vẫn được tài trợ vì tờ giấy trắng dễ bán còn cây đa bóp nghẹt thì không. Một đội lớn cần một phản hồi đã được diễn tập để cuộc tranh luận được thắng bằng bằng chứng thay vì bằng người cấp cao nhất trong phòng. Căng thẳng thực sự là một số nền tảng thực sự không bền vững và việc viết lại là chính đáng, nên câu trả lời không thể là từ chối toàn bộ: nó phải cân nhắc liệu các đường nối tăng dần còn tồn tại không so với chi phí thực của việc giữ nền tảng cũ sống. Hãy mang giá trị mà bước tăng dần đầu tiên sẽ mang lại, tỷ lệ thất bại lịch sử của các lần viết lại tương đương, và một phân rã của bất kỳ lần viết lại đề xuất nào thành các mảnh có thể phát hành độc lập. Trong chính phủ, nơi một chương trình nhiều năm bị hủy đốt tiền công trước mắt mọi người, hãy kiên quyết yêu cầu bất kỳ lần viết lại nào cũng phải mang lại giá trị sớm và sống sót khi bị dừng giữa chừng mà không mất trắng.

6. **Bạn sẽ nắm bắt các quy tắc nghiệp vụ bị khóa trong mã cũ nhất của mình thế nào trước khi những người hiểu chúng đã ra đi?** Phần lớn giá trị trong một hệ thống cũ là hành vi không có tài liệu mà hàng thập kỷ trường hợp biên, quy định và các bản sửa tương thích-lỗi đã tích tụ, và nó sống trong một nhóm chuyên gia sắp nghỉ hưu đang thu hẹp chứ không phải trong bất kỳ bản ghi bằng văn bản nào. Với một tổ chức lớn đây là rủi ro duy nhất không thể mua lại khi con người đã rời đi, nên nó xứng đáng được tài trợ trước công việc nền tảng dễ thấy hơn. Lực kéo đối lập là nắm bắt kiến thức (tài liệu, kiểm thử đặc tính, kỹ thuật đảo ngược, đào tạo chéo) có vẻ như chi phí chung không phát hành gì, đúng là lý do nó bị trì hoãn. Hãy mang bản kiểm kê ai nắm kiến thức quan trọng, họ gần rời đi đến đâu, và độ bao phủ kiểm thử nào ghim hành vi hiện tại hôm nay. Trong bối cảnh chịu quy định và công, hãy coi các quy tắc luật định được mã hóa trong mã cũ là một tài sản tuân thủ: mất chúng âm thầm không phải là nợ kỹ thuật, mà là một sự phơi nhiễm pháp lý.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hệ thống cũ của bạn là MVP vội vã của chính bạn, không phải một máy tính lớn: một bản mẫu nay mang doanh thu và ai cũng sợ chạm vào. Đừng viết lại nó. Hãy bọc mô-đun đáng sợ nhất sau một giao diện sạch, thêm kiểm thử đặc tính để ghim hành vi của nó, và tách chức năng ra tăng dần để mỗi bản phát hành nhỏ mang lại giá trị và thu nhỏ rủi ro. Bạn không có đường băng cho việc xây lại từ đầu, nên tính tùy chọn quan trọng hơn sự thanh nhã.

**Doanh nghiệp nhỏ.** Bạn không có đội hiện đại hóa và ngân sách eo hẹp, nên bước đi thực tế thường là giữ cho một hệ thống đang chạy tiếp tục chạy: nắm bắt những gì một người hiểu nó biết, đưa nó vào quản lý mã nguồn cùng vài bài kiểm thử tự động, và dựa vào nhà cung cấp hoặc sản phẩm đóng gói thay vì xây lại theo yêu cầu riêng. Hãy đóng khung quyết định là mua so với xây, và ưu tiên mua khi năng lực là hàng hóa phổ thông. Dành công sức hạn chế của bạn cho hệ thống duy nhất mà thất bại của nó sẽ dừng doanh nghiệp, không phải cho bất cứ thứ gì chỉ trông cũ nhất.

**Doanh nghiệp lớn.** Vấn đề là quy mô danh mục: hàng chục hệ thống, nhiều đội, và rủi ro kiến thức khắp hệ sinh thái. Hãy chạy một đánh giá rủi ro-so-với-giá-trị chung, chuẩn hóa trên các mẫu tăng dần (cây đa bóp nghẹt và phân nhánh bằng trừu tượng), và coi di chuyển dữ liệu cùng chạy kép là các kỷ luật hạng nhất với đối soát mà mọi người tin cậy. Quản trị hiện đại hóa như một danh mục liên tục theo quỹ đạo rủi ro thay vì một loạt dự án anh hùng rải rác, và ngân sách tường minh cho quản lý cùng nắm bắt kiến thức để không hệ thống quan trọng nào phụ thuộc vào một người bảo trì sắp nghỉ hưu.

**Chính phủ.** Nghĩa vụ luật định được mã hóa qua nhiều thập kỷ, quy tắc mua sắm, và các dịch vụ công dân không thể gián đoạn khiến thay thế nổ lớn đặc biệt nguy hiểm. Hãy ưu tiên di chuyển cây đa bóp nghẹt tăng dần với chuyển đổi từng lát một, chứng minh qua đối soát và chạy song song dài rằng không một hồ sơ công dân nào bị mất hay tính sai, và giữ khả năng hoàn tác suốt thời gian. Mua sắm nên đòi hỏi khả năng di động dữ liệu và công khai quy tắc nghiệp vụ thay vì dịch mờ đục, và bất kỳ chương trình nhiều năm nào cũng phải mang lại giá trị có thể kiểm toán sớm và sống sót qua sự soi xét công khai nếu bị dừng giữa chừng.

## Ví dụ

**Công ty khởi nghiệp.** MVP ban đầu của một công ty khởi nghiệp ba năm tuổi đã trở thành một dạng hệ thống cũ của riêng nó: một bản mẫu vội vã nay xử lý doanh thu thật và ai cũng sợ chạm vào. Thay vì viết lại, đội bọc mô-đun tệ nhất sau một giao diện sạch, thêm kiểm thử đặc tính để ghim hành vi hiện tại, và chuyển chức năng ra khỏi nó từng mảnh một qua vài tháng. Mỗi bản phát hành nhỏ mang lại giá trị và thu nhỏ phần đáng sợ, nên công ty khởi nghiệp có một hệ thống bảo trì được mà không đặt cược cả công ty vào việc xây lại từ đầu mà họ không kham nổi.

**Doanh nghiệp lớn.** Một công ty bảo hiểm lớn chạy quản lý hợp đồng trên một hệ thống COBOL máy tính lớn đáng tin cậy nhưng đắt để thay đổi và do một nhúm kỹ sư gần nghỉ hưu duy trì. Thay vì viết lại, công ty bọc máy tính lớn bằng API hiện đại và áp dụng cây đa bóp nghẹt: các năng lực báo giá-và-mua cùng tự phục vụ mới được xây trên một nền tảng hiện đại và định tuyến qua một mặt tiền, trong khi hồ sơ hợp đồng lõi ở lại máy tính lớn. Song song, đội lập tài liệu quy tắc nghiệp vụ và thêm [kiểm thử đặc tính](https://en.wikipedia.org/wiki/Characterization_test) quanh COBOL. Qua nhiều năm, hết năng lực này đến năng lực khác rời khỏi máy tính lớn, mỗi bản phát hành mang lại giá trị, cho đến khi phần lõi còn lại có thể được loại bỏ theo điều kiện của công ty bảo hiểm thay vì trong khủng hoảng.

**Chính phủ.** Một cơ quan an sinh xã hội phải hiện đại hóa hệ thống tính toán trợ cấp hàng thập kỷ trả cho hàng triệu công dân và không thể bị gián đoạn hay trả sai. Cơ quan bác bỏ việc thay thế nổ lớn sau khi nghiên cứu các chương trình thất bại tương đương. Thay vào đó họ phân tích hồ sơ và làm sạch dữ liệu, xây dựng di chuyển tự động với đối soát đầy đủ theo tổng kiểm soát, và chạy công cụ trợ cấp mới song song với công cụ cũ nhiều tháng, đưa cho cả hai cùng các hồ sơ yêu cầu và so sánh mọi phép tính, điều tra từng sai lệch (thường phát hiện các quy tắc hệ thống cũ không có tài liệu phải được bảo tồn). Chỉ khi hệ thống mới khớp hệ thống cũ ở độ tin cậy rất cao họ mới chuyển đổi từng loại trợ cấp một, giữ khả năng hoàn tác suốt thời gian. Mặt tiền bóp nghẹt cho phép công dân thấy một dịch vụ liên tục xuyên suốt quá trình chuyển đổi.

## Luận chứng kinh doanh: động lực, ROI và TCO

Hiện đại hóa hệ thống cũ có một luận chứng kinh doanh bất thường, vì chi phí lớn nhất thường là chi phí của *việc không hành động* và rủi ro lớn nhất là bản thân dự án hiện đại hóa. Những chi phí tăng dần của việc không hiện đại hóa là cụ thể: bảo trì và giấy phép tăng trên các nền tảng lỗi thời, lực lượng chuyên gia ngày càng khan hiếm và đắt đỏ, không thể đáp ứng nhanh các yêu cầu quy định hay dịch vụ mới, và sự phơi nhiễm ngày càng tăng với một thất bại thảm khốc khi không còn ai hiểu hệ thống. Đối lại, chi phí hiện đại hóa là cao, và làm theo kiểu nổ lớn nó mang xác suất thất bại thực sự cao. Đó chính là lý do cách tiếp cận tăng dần quan trọng với ROI: nó biến một canh bạc lớn duy nhất thành một chuỗi các canh bạc nhỏ mà mỗi cái đều trả lại giá trị và có thể dừng lại.

Hãy trình bày lập luận với ban lãnh đạo bằng cách đóng khung lại lựa chọn. Câu hỏi không phải là "hiện đại hóa hay không." Mà là "hiện đại hóa tăng dần ngay bây giờ, hay trả chi phí quản lý leo thang và đối mặt một cuộc hiện đại hóa bị ép buộc, rủi ro cao hơn sau này trong khủng hoảng." Hãy định lượng TCO của hiện trạng (chi phí nền tảng và giấy phép, phần phụ trội cho kỹ năng khan hiếm, chi phí có trọng số rủi ro của một sự cố không thể phục hồi) và so sánh với một chương trình theo giai đoạn giảm rủi ro và chi phí với mỗi bước tăng dần trong khi giữ dịch vụ chạy. Quan trọng là phải kiên quyết yêu cầu bất kỳ lần viết lại đề xuất nào cũng được cấu trúc để mang lại giá trị sớm và thường xuyên. Một chương trình không mang lại gì trong ba năm và có thể bị hủy với tổn thất toàn phần không phải là một khoản đầu tư; đó là một canh bạc. Lập luận ROI mạnh nhất cho cách tiếp cận bóp nghẹt là tính tùy chọn: giá trị được phát hành liên tục và tổ chức có thể điều chỉnh hướng đi bất cứ lúc nào.

## Phản mẫu và cạm bẫy

- **Viết lại nổ lớn.** Thay thế nhiều năm, được ăn cả ngã về không, không mang lại giá trị đến cuối và thường bị hủy với chi phí lớn.
- **Viết lại mà không hiểu.** Thay thế mã có quy tắc nghiệp vụ chưa bao giờ được lập tài liệu, âm thầm bỏ qua các trường hợp biên mà người dùng thật và luật pháp phụ thuộc.
- **Đánh giá thấp dữ liệu.** Coi di chuyển dữ liệu là chuyện nghĩ sau trong khi nó là phần khó nhất, rủi ro nhất của dự án.
- **Bỏ qua chạy kép.** Chuyển sang hệ thống mới mà không so sánh song song, chỉ phát hiện sai lệch sau khi chúng ảnh hưởng đến người thật.
- **Dịch tự động như một giải pháp.** Dịch máy COBOL sang ngôn ngữ hiện đại và tin rằng việc đã xong, tạo ra mã khó hiểu tái tạo nguyên văn logic cũ.
- **Hiện đại hóa theo tuổi, không theo rủi ro.** Dồn công sức vào các hệ thống cũ-nhưng-ổn-định trong khi các hệ thống rủi ro cao, thay đổi nhiều phải chờ.
- **Mất kiến thức.** Để những người bảo trì cuối cùng nghỉ hưu mà không nắm bắt quy tắc nghiệp vụ và thêm kiểm thử đặc tính.
- **Không có hoàn tác.** Chuyển đổi mà không có đường quay lại khi hệ thống mới hành xử sai dưới tải thật và dữ liệu thật.

## Mô hình trưởng thành

- **Mức 1: Khởi đầu.** Các hệ thống cũ bị sợ hãi và đóng băng; thay đổi bị né tránh. Không có bản kiểm kê hay đánh giá rủi ro. Hiện đại hóa, nếu được thử, là một lần viết lại được ăn cả ngã về không tùy nghi vì bực bội. Kiến thức nằm trong vài cái đầu sắp nghỉ hưu và không có gì được viết ra.
- **Mức 2: Phát triển.** Một số đội có bản kiểm kê và cảm nhận sơ bộ về rủi ro, và một vài hệ thống cũ được bọc bằng API để truy cập. Các mẫu tăng dần được biết đến nhưng áp dụng không đều, và tư duy vẫn trôi về các lần viết lại nổ lớn. Di chuyển dữ liệu được thử nhưng bị đánh giá thấp, và thực hành khác nhau rất nhiều giữa các đội.
- **Mức 3: Chuẩn hóa.** Các hệ thống được ưu tiên theo rủi ro và giá trị bằng một phương pháp có tài liệu, toàn tổ chức. Các mẫu tăng dần (cây đa bóp nghẹt, phân nhánh bằng trừu tượng) là mặc định được thực thi, và mọi cuộc hiện đại hóa theo một cẩm nang chuẩn. Di chuyển dữ liệu là nỗ lực có kế hoạch, được đối soát với chạy kép trước chuyển đổi, và nắm bắt kiến thức cùng kiểm thử đặc tính là thực hành bắt buộc thay vì tùy chọn.
- **Mức 4: Quản lý.** Hiện đại hóa được đo và kiểm soát bằng dữ liệu. Hệ sinh thái mang các đường cơ sở: số người bảo trì và chân trời nghỉ hưu cho mỗi hệ thống, độ bao phủ kiểm thử đặc tính, tỷ lệ đối soát di chuyển đạt, số sai lệch chạy kép, và giá trị phát hành mỗi bước tăng dần, tất cả được theo dõi theo mục tiêu. Các quyết định quản-lý-hay-thay-thế và các lời gọi đi hay không đi cho chuyển đổi được đưa ra dựa trên bằng chứng này, và một hệ thống trôi quá ngưỡng rủi ro kiến thức kích hoạt hành động thay vì chờ khủng hoảng.
- **Mức 5: Điều phối.** Hiện đại hóa là liên tục, tích hợp với hoạch định kinh doanh và rủi ro, và thích ứng. Danh mục được cân bằng lại theo quỹ đạo rủi ro (đặc biệt là rủi ro kiến thức) khi nó dịch chuyển, thay thế tăng dần là thường lệ và ít kịch tính, mỗi bước tăng dần mang lại giá trị và đảo ngược được, và tổ chức điều khiển nhịp độ có chủ đích. Bài học từ mỗi cuộc di chuyển phản hồi vào cẩm nang chung để cả hệ sinh thái cải thiện theo thời gian.

## Ý tưởng để thảo luận

1. Với hệ thống cũ quan trọng nhất của bạn, bao nhiêu người vẫn có thể duy trì nó, và họ gần rời đi đến đâu?
2. Bạn bị cám dỗ bởi việc viết lại nổ lớn ở đâu, và một cách tiếp cận tăng dần có thể phát hành giá trị gì trong ba tháng đầu thay thế?
3. Các quy tắc nghiệp vụ trong những hệ thống cũ nhất của bạn được lập tài liệu tốt đến đâu, và chúng sẽ ra sao nếu mã bị thay thế?
4. Bạn đã phân tích hồ sơ dữ liệu bạn cần di chuyển chưa, và bạn có biết nó thực sự bẩn và vướng víu đến mức nào không?
5. Những hệ thống cũ-nhưng-ổn-định nào bạn đang dành năng lượng hiện đại hóa mà bạn có thể để yên một cách an toàn?
6. Bạn có thể chạy hệ thống mới song song với hệ thống cũ và chứng minh chúng khớp nhau trước khi chuyển đổi không?

## Những điểm cần ghi nhớ

- Hệ thống cũ nghĩa là có giá trị và mang tính nền tảng; hãy tôn trọng và hiểu một hệ thống trước khi bạn thay đổi nó.
- Hiện đại hóa tăng dần với cây đa bóp nghẹt và phân nhánh bằng trừu tượng, mang lại giá trị liên tục và giữ mỗi thay đổi nhỏ và đảo ngược được.
- Coi viết lại nổ lớn là chế độ thất bại mặc định; dành nó cho các nền tảng thực sự không bền vững và ngay cả khi đó hãy phân rã nó.
- Ưu tiên theo rủi ro và giá trị (đặc biệt là rủi ro kiến thức), không theo tuổi; một số hệ thống cũ tốt nhất nên được quản lý, không thay thế.
- Di chuyển dữ liệu và chạy kép là trái tim của nỗ lực; phân tích hồ sơ, đối soát, chạy song song, và giữ khả năng hoàn tác.
- Luận chứng kinh doanh mạnh nhất là tính tùy chọn: hiện đại hóa tăng dần biến một canh bạc lớn, rủi ro thành nhiều canh bạc nhỏ trả lại giá trị.

## Tài liệu tham khảo và đọc thêm

- Michael Feathers, *Working Effectively with Legacy Code*
- Martin Fowler, "StranglerFigApplication" và "BranchByAbstraction"
- Sam Newman, *Monolith to Microservices*
- Nicholas Carr / các nghiên cứu ngành về sự phụ thuộc vào máy tính lớn và COBOL (bối cảnh về quy mô của các hệ sinh thái hệ thống cũ)
- Robert Annett, *Working with Legacy Systems*
- Eric Evans, *Domain-Driven Design* (tầng chống tham nhũng)
- Gregor Hohpe, *Enterprise Integration Patterns* và *The Software Architect Elevator*
- Standish Group *CHAOS Report* (bằng chứng về tỷ lệ thất bại của dự án lớn và viết lại)
