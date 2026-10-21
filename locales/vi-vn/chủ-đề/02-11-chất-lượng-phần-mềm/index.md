# 2.11 Chất lượng phần mềm

## Tổng quan và động lực

[Chất lượng phần mềm](https://en.wikipedia.org/wiki/Software_quality) là mức độ một hệ thống đáp ứng các nhu cầu đã nêu và kỳ vọng hợp lý. Điều đó có nghĩa là nhiều hơn việc nó có chạy được không: nó có nghĩa là hệ thống có đáng tin cậy, bảo mật, bảo trì được, dùng được, hiệu năng tốt và phù hợp với mục đích của nó theo thời gian hay không. Chất lượng rộng hơn kiểm thử. Kiểm thử (chương 2.4) là một hoạt động làm lộ lỗi. Chất lượng là toàn bộ kỷ luật xây dựng đúng thứ và xây tốt, và biết, bằng bằng chứng, rằng bạn đã làm vậy. Một hệ thống có thể vượt qua mọi bài kiểm thử mà vẫn kém chất lượng nếu nó không bảo trì được, không tiếp cận được, hoặc phù hợp kém với những gì người dùng thực sự cần.

Trong một đội lớn, chất lượng không thể sống trong đầu một người hay thói quen của một đội. Hàng trăm kỹ sư, nhiều sản phẩm và các hệ thống tồn tại lâu cần một định nghĩa chung về chất lượng, các quy trình tường minh để đảm bảo nó, và các phép đo cho bạn biết nó đang tốt lên hay xấu đi. Không có điều đó, "chất lượng" trở thành một khát vọng mơ hồ thua mọi cuộc tranh luận với hạn chót, và lỗi chất đống cho đến khi thay đổi trở nên chậm và rủi ro.

Trong bối cảnh doanh nghiệp và chính phủ, rủi ro còn cao hơn. Các hệ thống chịu quy định, quan trọng về an toàn và hướng đến công dân phải chứng minh chất lượng, không chỉ khẳng định: quy trình có tài liệu, bằng chứng truy vết được và kiểm chứng độc lập thường là bắt buộc. Chất lượng kém mang chi phí tài chính, pháp lý và danh tiếng trực tiếp, và trong một số lĩnh vực nó đặt con người vào nguy hiểm. Một kỷ luật chất lượng có chủ đích, được xây từ mô hình, quy trình, đo lường và văn hóa, là thứ biến chất lượng từ một tai nạn thành một kết quả được quản lý.

## Các nguyên tắc chính

- Chất lượng là sự phù hợp với mục đích cộng với sự tuân thủ yêu cầu; hãy xác định cả hai một cách tường minh.
- Chất lượng được xây vào, không phải kiểm thử vào; kiểm chứng tìm ra lỗi, nhưng phòng ngừa tránh được chúng.
- Phân biệt [đảm bảo chất lượng](https://en.wikipedia.org/wiki/Quality_assurance) (quy trình của chúng ta có vững không?) với [kiểm soát chất lượng](https://en.wikipedia.org/wiki/Quality_control) (sản phẩm này có tốt không?).
- Kiểm chứng (verification) hỏi "chúng ta có xây đúng cách không?"; xác nhận (validation) hỏi "chúng ta có xây đúng thứ không?"
- Đo chất lượng bằng một bộ nhỏ các chỉ số có ý nghĩa; coi chỉ số là tín hiệu, không phải mục tiêu.
- Chi phí của một lỗi tăng lên khi nó được tìm thấy càng muộn, vì vậy hãy đẩy các hoạt động chất lượng sớm hơn.
- Chất lượng là thuộc tính của toàn bộ tổ chức và văn hóa của nó, không phải một cổng ở cuối.

## Khuyến nghị

### Áp dụng một mô hình chất lượng chung như ISO/IEC 25010

Hãy cho tổ chức của bạn một từ vựng chung về chất lượng bằng cách áp dụng một mô hình chất lượng sản phẩm được công nhận. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) xác định các đặc tính bao gồm sự phù hợp chức năng, hiệu quả hiệu năng, khả năng tương thích, tính dùng được, độ tin cậy, bảo mật, khả năng bảo trì và tính khả chuyển. Hãy dùng nó để làm chất lượng cụ thể: với mỗi hệ thống, hãy quyết định đặc tính nào quan trọng nhất và "đủ tốt" nghĩa là gì cho từng đặc tính. Các đặc tính chất lượng sản phẩm này chính là các **thuộc tính chất lượng** dẫn dắt kiến trúc (chương 3.1). Chất lượng và kiến trúc là hai góc nhìn của một mối quan tâm, vì vậy hãy để chúng chia sẻ một danh sách ưu tiên thay vì hai danh sách cạnh tranh.

### Tách đảm bảo chất lượng khỏi kiểm soát chất lượng

Hãy coi đảm bảo chất lượng (QA) và kiểm soát chất lượng (QC) là các hoạt động riêng biệt nhưng bổ sung cho nhau. QA hướng đến quy trình và phòng ngừa: nó cải thiện cách công việc được thực hiện, thông qua tiêu chuẩn, đánh giá, định nghĩa hoàn thành và đào tạo, để lỗi ít có khả năng xuất hiện ngay từ đầu. QC hướng đến sản phẩm và phát hiện: nó kiểm tra các sản phẩm công việc thực tế, như kiểm thử, [đánh giá mã](https://en.wikipedia.org/wiki/Code_review) và kiểm toán, để bắt các lỗi đã lọt vào. Một tổ chức trưởng thành đầu tư vào cả hai, nhưng nghiêng về QA, vì ngăn chặn lỗi rẻ hơn tìm và sửa chúng.

### Vận hành các quy trình quản lý chất lượng phần mềm tường minh

Hãy biến chất lượng thành một quy trình được quản lý, không phải một hy vọng thầm lặng. Với công việc quan trọng, hãy viết một kế hoạch chất lượng nêu các đặc tính chất lượng mục tiêu, các hoạt động đảm bảo và kiểm soát, tiêu chí chấp nhận, và ai chịu trách nhiệm. Đan nó vào các thực hành bạn đã có: đánh giá mã (chương 2.5) vừa là kiểm soát vừa là cách chia sẻ kiến thức, chiến lược kiểm thử (chương 2.4) là lưới an toàn tự động, và [phân tích tĩnh](https://en.wikipedia.org/wiki/Static_program_analysis) là kiểm tra liên tục. Hãy xem xét dữ liệu chất lượng đều đặn và hành động theo xu hướng, thay vì chỉ phản ứng với sự cố.

### Thực hành kiểm chứng và xác nhận như các kỷ luật riêng biệt

Kiểm chứng xác nhận rằng các sản phẩm công việc đáp ứng đặc tả của chúng, để đầu vào đúng của mỗi giai đoạn tạo ra đầu ra đúng, thông qua đánh giá, phân tích tĩnh và kiểm thử đối chiếu với yêu cầu. Xác nhận khẳng định rằng hệ thống hoàn chỉnh thực sự đáp ứng nhu cầu của người dùng và mục đích sử dụng dự kiến, thông qua kiểm thử người dùng, kiểm thử chấp nhận, thí điểm và phản hồi thực địa. Bạn cần cả hai. Một hệ thống có thể đúng đối với một đặc tả có khiếm khuyết (được kiểm chứng nhưng không hợp lệ), hoặc có thể giải quyết một nhu cầu thực trong khi vẫn chứa lỗi (hợp lệ nhưng không được kiểm chứng). Trong các môi trường chịu quy định, [kiểm chứng và xác nhận](https://en.wikipedia.org/wiki/Verification_and_validation) độc lập (IV&V) bởi một bên tách biệt với các nhà phát triển có thể là bắt buộc.

### Đo chất lượng bằng các chỉ số có ý nghĩa

Chọn một bộ nhỏ các chỉ số phản ánh kết quả chất lượng và các động lực của chúng, và theo dõi chúng theo thời gian. Các thước đo hữu ích bao gồm mật độ lỗi, tỷ lệ lỗi thoát ra (lỗi tìm thấy trên môi trường thực so với trước khi phát hành), thời gian trung bình để phát hiện và sửa, tỷ lệ thay đổi thất bại, các tín hiệu sức khỏe mã như độ phức tạp và sự trùng lặp, và các tín hiệu xác nhận như vấn đề do người dùng báo cáo và sự tuân thủ khả năng tiếp cận. Hãy tránh các chỉ số hào nhoáng và dễ bị lách: một chỉ số trở thành mục tiêu thì ngừng đo thực tế. Hãy ghép các con số với tín hiệu định tính từ đánh giá và phản hồi của người dùng.

### Đặc trưng hóa và quản lý lỗi một cách có hệ thống

Hãy coi lỗi là dữ liệu, không chỉ là đám cháy cần dập. Phân loại chúng theo mức độ nghiêm trọng, loại và nguyên nhân gốc. Theo dõi chúng từ lúc phát hiện đến lúc giải quyết. Tìm các mẫu hình để bạn có thể ngăn tái diễn. Dùng các kỹ thuật như [phân tích nguyên nhân gốc](https://en.wikipedia.org/wiki/Root_cause_analysis) và phân loại lỗi để phân biệt những sai lầm một lần với những điểm yếu mang tính hệ thống. Đưa những gì bạn học được trở lại QA, thông qua tiêu chuẩn cập nhật, kiểm thử bổ sung và đánh giá được cải thiện, để cùng một loại lỗi không quay lại. Một lỗi được sửa mà không hiểu nguyên nhân của nó là một lỗi bạn đã mời quay lại.

### Quản lý chi phí chất lượng một cách có chủ đích

Hãy hiểu kinh tế học chất lượng qua các loại cổ điển: chi phí phòng ngừa (đào tạo, tiêu chuẩn, thiết kế tốt, công cụ), chi phí thẩm định (đánh giá, kiểm thử, kiểm toán), và chi phí thất bại (làm lại nội bộ trước khi phát hành, cộng với các thất bại bên ngoài do người dùng tìm ra, tốn kém hơn nhiều). Hãy chuyển khoản đầu tư của bạn về phía phòng ngừa và thẩm định sớm, vì mỗi đồng ở đó tránh được nhiều đồng chi phí thất bại sau này. Hãy làm cho các chi phí này hiển thị, để "chúng ta không có thời gian cho chất lượng" được nhìn nhận đúng bản chất: một lựa chọn chi nhiều hơn cho thất bại.

### Xây dựng văn hóa chất lượng

Biến chất lượng thành trách nhiệm của mọi người, do các đội xây dựng phần mềm sở hữu, thay vì giao cho một bộ phận QA hạ nguồn kiểm tra nó ở cuối. Các nhà lãnh đạo nên thưởng cho kết quả chất lượng, làm cho việc báo cáo lỗi và suýt xảy ra sự cố trở nên an toàn, và coi dữ liệu chất lượng là công cụ học hỏi thay vì cây gậy. Cách tiếp cận không đổ lỗi với lỗi đưa vấn đề ra ánh sáng sớm. Cách đổ lỗi giấu chúng cho đến khi chúng đắt đỏ.

## Đánh đổi: ưu và nhược điểm

| Thực hành / lựa chọn | Ưu điểm | Nhược điểm |
|---|---|---|
| Mô hình chất lượng chính thức (ISO 25010) | Từ vựng chung; ưu tiên tường minh | Chi phí nếu áp dụng giáo điều |
| Đảm bảo chất lượng nặng (phòng ngừa) | Ít lỗi hơn; tổng chi phí thấp hơn | Đầu tư ban đầu; chậm cho thấy lợi tức |
| Kiểm soát chất lượng nặng (kiểm tra) | Bắt các lỗi lọt qua | Tốn kém; tìm lỗi muộn |
| V&V độc lập | Đảm bảo cao; khách quan | Tốn kém; chậm hơn; có thể có cảm giác đối đầu |
| Chỉ số chất lượng phong phú | Khả năng hiển thị; cảnh báo sớm | Rủi ro bị lách; chi phí đo lường |
| Đội QA chuyên trách | Tập trung và chuyên môn | Có thể làm các nhà phát triển trút trách nhiệm |
| Chất lượng do các đội sở hữu | Quyền sở hữu; phản hồi nhanh | Đòi hỏi kỷ luật và kỹ năng ở khắp nơi |

Sự đánh đổi trung tâm là đầu tư so với đảm bảo, được định hình bởi thời điểm. Phòng ngừa tốn tiền bây giờ để tránh chi phí thất bại lớn hơn sau này. Vì vậy mức chất lượng đúng về mặt kinh tế không phải là tối đa; đó là điểm mà chi phí biên của việc đảm bảo thêm bằng chi phí thất bại mà nó tránh được. Điểm đó cao với các hệ thống quan trọng về an toàn và thấp hơn với các công cụ nội bộ ít rủi ro. Căng thẳng lặp lại khác là quyền sở hữu. Các nhóm QA trung tâm xây dựng chuyên môn nhưng có thể để nhà phát triển trút trách nhiệm. Chất lượng do đội sở hữu xây dựng quyền sở hữu nhưng đòi hỏi kỹ năng và kỷ luật ở khắp nơi.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi cùng một loại lỗi xuất hiện hai lần, chúng ta có chạy phân tích nguyên nhân gốc hay chỉ sửa lại lần nữa?** Một lỗi được sửa mà không hiểu nguyên nhân là một lỗi bạn đã mời quay lại, và trong một đội lớn cùng một nguyên nhân gốc có thể nổi lên qua nhiều dịch vụ trước khi có ai nối các điểm lại. Coi lỗi là dữ liệu (được phân loại theo mức độ nghiêm trọng, loại và nguyên nhân, rồi được khai thác để tìm mẫu hình) là thứ phân biệt một đội ngày càng đáng tin cậy hơn với một đội cứ bận rộn sửa lại cùng một sai lầm. Hãy mang bộ theo dõi lỗi của bạn đến cuộc họp và tìm các dấu hiệu lặp lại: có bao nhiêu sự cố gần đây chia sẻ một nguyên nhân mà bạn chưa bao giờ giải quyết một cách hệ thống? Câu trả lời nên nuôi dưỡng phòng ngừa, để một nguyên nhân lặp lại thúc đẩy một tiêu chuẩn được cập nhật, một hàm hỗ trợ dùng chung mới, một bài kiểm thử bổ sung hoặc một danh sách kiểm tra đánh giá tốt hơn, vì đó là cách một bản sửa ở một nơi ngăn cả loại lỗi quay lại.

2. **Việc báo cáo một lỗi hay một suýt xảy ra sự cố có an toàn trong đội chúng ta không, và điều gì xảy ra với người nêu ra nó?** Chất lượng là thuộc tính của văn hóa, và cách tiếp cận không đổ lỗi đưa vấn đề ra ánh sáng sớm trong khi cách đổ lỗi giấu chúng cho đến khi đắt đỏ, điều mà trong một hệ thống chịu quy định hoặc hướng đến công dân có thể nghĩa là một thất bại công khai hoặc một khoản phạt. Điều này quan trọng nhất ở quy mô lớn, nơi kỹ sư gần rủi ro nhất thường là người trẻ và động cơ giữ im lặng rất mạnh. Hãy mang các tín hiệu trung thực: các suýt xảy ra sự cố có được ghi lại và thảo luận hay biến mất? Các cuộc phân tích hậu sự cố nêu nguyên nhân hay nêu tên người? Hành động là biến dữ liệu chất lượng thành công cụ học hỏi thay vì cây gậy, thưởng cho những người làm lộ ra vấn đề, và tổ chức phân tích hậu sự cố không đổ lỗi, vì bạn không thể ngăn chặn điều mà đội của bạn sợ báo cáo.

3. **Xác nhận có thực sự chặn được một bản phát hành không, và ai nắm thẩm quyền đó khi hạn chót đang đến gần?** Kiểm chứng (chúng ta có xây đúng cách không?) và xác nhận (chúng ta có xây đúng thứ không?) là các kỷ luật riêng biệt, và xác nhận chỉ có răng nếu một kiểm tra khả năng tiếp cận thất bại, một kiểm thử chấp nhận thất bại, hay một nghiên cứu người dùng bất lợi thực sự có thể chặn việc phát hành. Trong bối cảnh doanh nghiệp và chính phủ điều này thường bắt buộc, đôi khi qua kiểm chứng và xác nhận độc lập bởi một bên tách biệt với nhà phát triển, và "chúng tôi cứ phát hành" không phải là câu trả lời mà cơ quan giám sát chấp nhận. Hãy mang vài bản phát hành gần nhất của bạn: có tín hiệu chất lượng nào từng thực sự dừng một bản không, hay cổng luôn nhường cho ngày hạn? Nếu xác nhận chưa bao giờ chặn một bản phát hành, nó chỉ là đồ trang trí, và cách sửa là viết tiêu chí chấp nhận vào kế hoạch chất lượng từ đầu, nêu tên ai sở hữu quyết định đi hay không đi, và trao cho quyết định đó thẩm quyền thực sự độc lập với áp lực phân phối.

4. **Chúng ta có thực sự biết chi phí chất lượng kém của mình không, và chúng ta có đang chủ động chuyển chi tiêu từ thất bại sang phòng ngừa không?** Chi phí chất lượng kém (COPQ) là tiền mất vào làm lại nội bộ, sự cố môi trường thực, sửa khẩn cấp, tải hỗ trợ, người dùng mất đi và các khoản phạt, và nó gần như luôn lớn hơn khoản chi hiển thị cho đánh giá và kiểm thử. Trong một đội lớn, chi phí thất bại rải rác qua các kênh sự cố, hàng đợi hỗ trợ và việc làm lại mà không ai ghi là làm lại, nên chúng vô hình cho đến khi ai đó cộng chúng lại. Căng thẳng là phòng ngừa tốn tiền bây giờ, trong một chu kỳ ngân sách, để tránh chi phí thất bại đáp xuống sau và đáp xuống ngân sách của người khác, khiến sự đánh đổi dễ bị trì hoãn mãi mãi. Hãy mang con số thực: số lượng và chi phí sự cố, giờ làm lại, tỷ lệ lỗi thoát ra, và sự phân chia hiện tại của chi tiêu giữa phòng ngừa, thẩm định và thất bại, rồi quyết định liệu cơ cấu có nên dịch chuyển sớm hơn không. Với các hệ thống doanh nghiệp và chính phủ, nơi phần lớn chi phí vòng đời rơi vào sau bản phát hành đầu tiên, hãy đặt COPQ trước mặt những người nắm ngân sách, vì một con số mà cơ quan giám sát nhìn thấy khó bị đánh đổi hơn nhiều so với một lời kêu gọi mơ hồ về "chất lượng".

5. **Chỉ số chất lượng nào của chúng ta đã âm thầm trở thành mục tiêu, và chúng đang thúc đẩy hành vi nào?** Một chỉ số trở thành mục tiêu thì ngừng đo thực tế: chạy theo một tỷ lệ độ bao phủ và bạn có các bài kiểm thử được viết để dịch chuyển con số, không phải các bài kiểm thử bắt lỗi. Ở quy mô lớn điều này nguy hiểm, vì một bảng điều khiển tiêu đề được chia sẻ qua hàng chục đội đặt ra động cơ cho tất cả, và một chỉ số dễ bị lách lan truyền việc lách ở khắp nơi cùng lúc. Cân nhắc đối lập là bạn vẫn cần đo lường, nên câu trả lời hiếm khi là "bỏ chỉ số" mà là "ghép nó với một tín hiệu đối trọng và đọc nó cùng với bằng chứng định tính từ đánh giá và người dùng". Hãy mang bộ chỉ số hiện tại của bạn và, với mỗi chỉ số, hỏi một người chịu áp lực có thể làm gì để dịch chuyển nó mà không cải thiện chất lượng, và bạn đã thấy điều đó xảy ra chưa. Trong bối cảnh chịu quy định và hướng đến công dân, hãy đặc biệt cảnh giác với các chỉ số tuân thủ trông xanh trong khi việc xác nhận nền tảng (khả năng tiếp cận, kết quả người dùng thực) chưa bao giờ thực sự được thực hiện, vì một kiểm toán viên cuối cùng sẽ kiểm tra thực tế đằng sau con số.

6. **Ai sở hữu chất lượng ở đây: các đội viết mã, hay một nhóm riêng ở cuối, và chúng ta thực sự đang bố trí nguồn lực cho bên nào?** Quyền sở hữu định hình mọi thứ ở hạ nguồn, vì một ô QA hạ nguồn để nhà phát triển trút trách nhiệm cho mã họ viết, trong khi chất lượng do đội sở hữu xây dựng quyền sở hữu với cái giá là đòi hỏi kỹ năng và kỷ luật trong mọi đội. Trong một đội lớn đây không phải là hoặc cái này hoặc cái kia: mô hình bền vững thường là các đội sở hữu chất lượng thông qua đánh giá mã và kiểm thử tự động, được hỗ trợ bởi một nhóm trung tâm nhỏ duy trì tiêu chuẩn, vận hành đảm bảo chất lượng như cải tiến quy trình, và huấn luyện, thay vì kiểm tra chất lượng vào ở cuối. Hãy mang một bản đồ trung thực về nơi công việc chất lượng hiện đang diễn ra, ai chịu trách nhiệm khi một lỗi thoát ra, và nơi ngân sách cùng biên chế thực sự nằm so với nơi lời nói cho rằng chất lượng sống. Với các tổ chức doanh nghiệp và chính phủ, hãy thêm yêu cầu kiểm chứng và xác nhận độc lập: một số chế độ đảm bảo bắt buộc một bên riêng biệt, vì vậy hãy quyết định có chủ đích biện pháp kiểm soát nào thuộc về các đội phân phối và biện pháp nào phải giữ độc lập để thỏa mãn kiểm toán.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ quan trọng hơn nghi thức, vì vậy hãy gọi tên hai hoặc ba đặc tính chất lượng thực sự bảo vệ sản phẩm của bạn, thường là độ tin cậy và khả năng bảo trì, và để sự bóng bẩy chờ. Hãy để cả đội sở hữu chất lượng bằng đánh giá mã và một bộ kiểm thử tự động khiêm tốn thay vì dựng một nhóm QA riêng mà bạn không thể bố trí. Khi cùng một loại lỗi xuất hiện hai lần, hãy dành hai mươi phút cho nguyên nhân gốc và thêm một hàm hỗ trợ dùng chung cộng một bài kiểm thử, để phòng ngừa rẻ và tỷ lệ thay đổi thất bại của bạn thấp khi bạn di chuyển nhanh.

**Doanh nghiệp nhỏ.** Không có chuyên gia chất lượng riêng và ngân sách eo hẹp, hãy dựa vào chất lượng được tích hợp sẵn trong các công cụ và nền tảng bạn mua thay vì một quy trình bạn phải vận hành. Khi bạn chọn phần mềm, hãy coi bằng chứng chất lượng của nhà cung cấp là một phần của giao dịch mua: tư thế bảo mật, khả năng tiếp cận, độ phản hồi hỗ trợ, và mức độ các bản phát hành của họ gây hỏng. Theo dõi một nhúm tín hiệu rẻ, trung thực (sự cố môi trường thực, vấn đề do khách hàng báo cáo, thời gian sửa) thay vì một chương trình chỉ số cầu kỳ mà bạn không có ai bảo trì.

**Doanh nghiệp lớn.** Công việc là nhất quán qua nhiều đội: áp dụng một mô hình chất lượng chung như ISO/IEC 25010, tách đảm bảo chất lượng (quy trình) khỏi kiểm soát chất lượng (sản phẩm), và vận hành các cuộc rà soát chi phí chất lượng chuyển chi tiêu về phía phòng ngừa. Giữ chất lượng do các đội phân phối sở hữu, được hỗ trợ bởi một nhóm trung tâm nhỏ duy trì tiêu chuẩn và bảng điều khiển cho tỷ lệ lỗi thoát ra, tỷ lệ thay đổi thất bại và xu hướng sức khỏe mã. Chuẩn hóa từ vựng và các cổng để các nhóm thôi phát minh lại thực hành chất lượng, trong khi để các đội có chỗ đáp ứng các chuẩn đó theo cách riêng của họ.

**Chính phủ.** Mua sắm, tính minh bạch và trách nhiệm giải trình trước công chúng đặt ra khung, vì vậy hãy viết yêu cầu chất lượng vào hợp đồng và yêu cầu bằng chứng chất lượng có tài liệu, truy vết được thay vì khẳng định. Hãy mong đợi kiểm chứng và xác nhận độc lập bởi một bên tách biệt với nhà phát triển, tuân thủ khả năng tiếp cận bắt buộc, và hồ sơ lỗi với mức độ nghiêm trọng cùng nguyên nhân gốc được giữ như một phần của dấu vết kiểm toán. Báo cáo các con số chi phí chất lượng kém (làm lại, kháng nghị, thất bại dịch vụ) cho các cơ quan giám sát, và trao cho xác nhận thẩm quyền thực sự để chặn một bản phát hành sẽ làm hỏng những công dân phụ thuộc vào nó.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp năm người quyết định rằng với sản phẩm ban đầu, độ tin cậy và khả năng bảo trì là các đặc tính chất lượng quan trọng, và để sự bóng bẩy từng điểm ảnh chờ. Chất lượng do cả đội sở hữu: đánh giá mã và một bộ kiểm thử tự động khiêm tốn là các biện pháp kiểm soát, và không có nhóm QA riêng để giao lỗi. Khi cùng một loại lỗi xuất hiện hai lần, họ dành hai mươi phút xem xét nhanh nguyên nhân gốc và thêm một hàm hỗ trợ dùng chung cộng một bài kiểm thử, để nó ngừng tái diễn thay vì bị sửa lại bằng tay mỗi lần. Thói quen phòng ngừa nhỏ đó giữ tỷ lệ thay đổi thất bại của họ thấp trong khi họ vẫn đang di chuyển nhanh.

**Doanh nghiệp lớn.** Một công ty dịch vụ tài chính lớn áp dụng ISO/IEC 25010 làm từ vựng chất lượng và, với mỗi sản phẩm, ghi lại các mức mục tiêu cho độ tin cậy, bảo mật và khả năng bảo trì. Các đội sở hữu chất lượng: đánh giá mã và kiểm thử tự động là các biện pháp kiểm soát trong đường ống, trong khi một nhóm trung tâm nhỏ vận hành QA bằng cách duy trì tiêu chuẩn và huấn luyện. Một bảng điều khiển chất lượng theo dõi tỷ lệ lỗi thoát ra, tỷ lệ thay đổi thất bại và xu hướng sức khỏe mã. Lỗi được phân loại và truy nguyên nhân gốc, và các nguyên nhân lặp lại thúc đẩy cập nhật các thư viện dùng chung và danh sách kiểm tra. Ban lãnh đạo xem xét dữ liệu chi phí chất lượng hằng quý và đã chuyển chi tiêu về phía phòng ngừa, cắt giảm cả sự cố môi trường thực lẫn chi phí sửa chúng.

**Chính phủ.** Một cơ quan quốc gia cung cấp một nền tảng trợ cấp hướng đến công dân làm việc dưới một chế độ đảm bảo yêu cầu bằng chứng chất lượng có tài liệu. Cơ quan vận hành một quy trình quản lý chất lượng chính thức với một kế hoạch chất lượng cho mỗi bản phát hành, cộng với kiểm chứng và xác nhận độc lập bởi một đội tách biệt với các nhà phát triển. Kiểm chứng kiểm tra từng sản phẩm công việc đối chiếu với yêu cầu truy vết về chính sách. Xác nhận bao gồm kiểm thử tuân thủ khả năng tiếp cận và nghiên cứu người dùng với công dân thực, và cái nào cũng có thể chặn một bản phát hành. Lỗi được theo dõi với mức độ nghiêm trọng và nguyên nhân gốc như một phần của dấu vết kiểm toán, và các con số chi phí chất lượng kém (làm lại, kháng nghị và thất bại dịch vụ) được gửi cho các cơ quan giám sát để biện minh cho việc tiếp tục đầu tư vào phòng ngừa.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của chất lượng là tổng chi phí sở hữu thấp hơn và tốc độ phân phối ổn định. Chi phí của chất lượng có hai mặt. Khoản chi tốt, phòng ngừa và thẩm định, hiển thị và kiểm soát được: thiết kế, tiêu chuẩn, đánh giá, kiểm thử và công cụ. Chi phí chất lượng kém (COPQ) lớn hơn nhưng thường ẩn: làm lại nội bộ, sự cố môi trường thực, sửa khẩn cấp, hỗ trợ khách hàng, người dùng mất đi, tiền phạt quy định và thiệt hại danh tiếng. Các nghiên cứu từ "Quality Is Free" của Crosby đã luôn thấy rằng tổng chi phí chất lượng kém vượt xa chi phí ngăn chặn nó, và rằng lỗi trở nên đắt hơn nhiều khi bạn bắt chúng càng muộn: một vấn đề tìm thấy trong thiết kế tốn một phần nhỏ so với cùng vấn đề đó tìm thấy trên môi trường thực.

Với ban lãnh đạo, lập luận không phải là "chi nhiều hơn cho chất lượng". Mà là "chi sớm hơn để chi ít hơn tổng thể". Hãy định lượng COPQ từ dữ liệu của chính bạn (số lượng và chi phí sự cố, giờ làm lại, tỷ lệ lỗi thoát ra) và cho thấy phòng ngừa và thẩm định sớm kéo nó xuống thế nào. Kết nối chất lượng với kết quả kinh doanh: độ tin cậy giữ chân khách hàng, khả năng bảo trì giữ cho thay đổi trong tương lai rẻ, và bảo mật cùng khả năng tiếp cận giữ bạn khỏi rắc rối pháp lý. Trong các hệ thống doanh nghiệp và chính phủ tồn tại lâu, nơi phần lớn chi phí rơi vào sau bản phát hành đầu tiên, các chiều kích khả năng bảo trì và độ tin cậy của chất lượng chi phối chi phí vòng đời. Điều đó khiến đầu tư chất lượng sớm trở thành một trong những quyết định có đòn bẩy cao nhất bạn có thể đưa ra.

## Phản mẫu và cạm bẫy

- **Chất lượng như một cổng cuối cùng:** kiểm tra chất lượng vào ở cuối thay vì xây nó vào, nên lỗi được tìm thấy khi chúng đắt nhất.
- **Nhầm lẫn kiểm thử với chất lượng:** cho rằng kiểm thử đạt nghĩa là chất lượng cao, bỏ qua khả năng bảo trì, tính dùng được và sự phù hợp với mục đích.
- **QA như một ô riêng:** một đội hạ nguồn "sở hữu chất lượng", để nhà phát triển trút trách nhiệm cho mã họ viết.
- **Sân khấu chỉ số:** chạy theo tỷ lệ độ bao phủ hoặc số lỗi như mục tiêu, mời gọi việc lách và che giấu chất lượng thực.
- **Kiểm chứng không có xác nhận:** xây đặc tả đúng cách mà không bao giờ kiểm tra liệu đặc tả có đáp ứng nhu cầu thực không.
- **Không phân tích nguyên nhân gốc:** sửa từng lỗi riêng lẻ mà không giải quyết nguyên nhân hệ thống, nên cùng một loại tái diễn.
- **Phớt lờ chi phí chất lượng kém:** coi chất lượng là chi phí thuần túy vì chi phí thất bại bị ẩn và không được đo.

## Mô hình trưởng thành

**Mức 1 (Khởi đầu).** Chất lượng không được xác định và tùy nghi. Nó dựa vào sự cần mẫn của cá nhân, được kiểm tra chủ yếu bằng kiểm thử thủ công ở cuối, và lỗi được xử lý phản ứng khi chúng nổi lên. Không có mô hình chung, không có chỉ số, và không có ranh giới giữa đảm bảo và kiểm soát.

**Mức 2 (Phát triển).** Các thực hành cơ bản xuất hiện: đánh giá mã, kiểm thử tự động và một bộ theo dõi lỗi. Một số dữ liệu chất lượng được thu thập, nhưng không đồng đều, và mỗi đội làm theo cách riêng. Chất lượng vẫn chủ yếu được coi là kiểm thử, phòng ngừa tối thiểu, kiểm chứng diễn ra, và xác nhận không chính thức.

**Mức 3 (Chuẩn hóa).** Tổ chức áp dụng một mô hình chất lượng chung (như ISO/IEC 25010), tách QA khỏi QC, và vận hành các quy trình quản lý chất lượng với kế hoạch chất lượng và tiêu chí chấp nhận, được lập thành tài liệu và áp dụng nhất quán qua các đội. Kiểm chứng và xác nhận là riêng biệt và có chủ đích, và lỗi được phân loại và truy nguyên nhân gốc theo một lược đồ đã thống nhất.

**Mức 4 (Quản lý).** Chất lượng được đo và kiểm soát theo các đường cơ sở. Một bộ nhỏ các chỉ số có ý nghĩa được theo dõi theo thời gian (mật độ lỗi, tỷ lệ lỗi thoát ra, thời gian trung bình để phát hiện và sửa, tỷ lệ thay đổi thất bại, và các tín hiệu sức khỏe mã như độ phức tạp và sự trùng lặp), và chi phí chất lượng được định lượng qua phòng ngừa, thẩm định và thất bại. Các cổng chấp nhận và chất lượng được thực thi dựa trên bằng chứng thay vì ý kiến, xu hướng được xem xét theo chu kỳ cố định, và xác nhận thực sự có thể chặn một bản phát hành.

**Mức 5 (Điều phối).** Chất lượng là một kỷ luật được cải tiến liên tục, được sở hữu bằng văn hóa, tích hợp với hoạch định kinh doanh và rủi ro. Phòng ngừa là trọng tâm, dữ liệu chi phí chất lượng dẫn dắt nơi đầu tư đi tới, và các phát hiện nguyên nhân gốc ngăn chặn tái diễn một cách có hệ thống. Các đội sở hữu chất lượng từ đầu đến cuối, các chỉ số nuôi dưỡng cải tiến liên tục, và tổ chức điều chỉnh thực hành chất lượng khi sản phẩm, rủi ro và quy định dịch chuyển. Điều này phù hợp với các mức cao hơn của mô hình trưởng thành trong chương 10.8.

## Ý tưởng để thảo luận

- Đặc tính chất lượng ISO/IEC 25010 nào quan trọng nhất cho các hệ thống của bạn, và "đủ tốt" cho từng đặc tính là gì?
- Tổ chức của bạn nằm ở đâu trong cơ cấu chi tiêu phòng ngừa-thẩm định-thất bại, và nó có nên dịch chuyển không?
- Bạn có phân biệt kiểm chứng với xác nhận trong thực tế, hay gộp cả hai thành "kiểm thử"?
- Chất lượng do các đội xây phần mềm sở hữu, hay được giao cho một nhóm riêng, và điều gì sẽ thay đổi nếu bạn chuyển nó?
- Chi phí chất lượng kém thực sự của bạn là bao nhiêu, và bạn có thể đo nó đủ tốt để đưa ra lập luận kinh doanh không?
- Chỉ số chất lượng nào của bạn là tín hiệu thực sự, và chỉ số nào đã trở thành mục tiêu dễ bị lách?

## Những điểm cần ghi nhớ

- Chất lượng rộng hơn kiểm thử: đó là sự phù hợp với mục đích cộng với sự tuân thủ, qua các đặc tính như độ tin cậy, bảo mật và khả năng bảo trì.
- Dùng một mô hình chất lượng chung (ISO/IEC 25010) để các thuộc tính chất lượng tường minh và phù hợp với kiến trúc (chương 3.1).
- Tách đảm bảo chất lượng (phòng ngừa, quy trình) khỏi kiểm soát chất lượng (phát hiện, sản phẩm), và nghiêng về phòng ngừa.
- Thực hành kiểm chứng (xây đúng cách) và xác nhận (xây đúng thứ) như các kỷ luật riêng biệt.
- Đo chất lượng bằng vài chỉ số có ý nghĩa, và đặc trưng hóa lỗi theo mức độ nghiêm trọng và nguyên nhân gốc để ngăn tái diễn.
- Quản lý chi phí chất lượng: phòng ngừa và thẩm định sớm rẻ hơn nhiều so với thất bại, đặc biệt trong các hệ thống tồn tại lâu.
- Xây dựng văn hóa chất lượng không đổ lỗi nơi các đội sở hữu chất lượng, được hỗ trợ bởi đánh giá mã (chương 2.5) và chiến lược kiểm thử (chương 2.4).

## Tài liệu tham khảo và đọc thêm

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, lĩnh vực kiến thức Chất lượng Phần mềm.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- Bộ ISO/IEC 25000 (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones và Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (ngữ cảnh quy trình đảm bảo chất lượng và V&V).
