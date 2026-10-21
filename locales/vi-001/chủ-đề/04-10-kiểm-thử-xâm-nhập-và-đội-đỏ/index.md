# 4.10 Kiểm thử xâm nhập và đội đỏ

## Tổng quan và động lực

Bạn có thể xây mọi biện pháp kiểm soát mà mô hình mối đe dọa của bạn đòi hỏi mà vẫn không biết chúng có hoạt động không. Tài liệu nói tường lửa chặn cổng đó, rà soát mã nói đầu vào được xác thực, chính sách nói đặc quyền tối thiểu được thực thi. Bảo mật tấn công là cách bạn tìm ra điều đó có đúng không khi một kẻ tấn công có động cơ ấn vào nó. Chương này nói về việc cố ý tấn công hệ thống của chính bạn, dưới sự cho phép, để tìm điểm yếu trước khi một kẻ thù thật làm.

Kỷ luật này chạy dọc một dải. Ở đầu nhẹ là [quét lỗ hổng](https://en.wikipedia.org/wiki/Vulnerability_scanner): các công cụ tự động dò tìm lỗi đã biết và cấu hình sai. Ở giữa là [kiểm thử xâm nhập](https://en.wikipedia.org/wiki/Penetration_test): một con người lành nghề xâu chuỗi các điểm yếu để chứng minh khả năng khai thác đối với một mục tiêu xác định. Ở đầu xa là [đội đỏ](https://en.wikipedia.org/wiki/Red_team): một chiến dịch hướng mục tiêu mô phỏng một kẻ thù thật qua con người, quy trình và công nghệ, và kiểm thử khả năng phát hiện và phản ứng của bạn, không chỉ khả năng ngăn chặn. Mỗi cái trả lời một câu hỏi khác nhau, và nhầm lẫn chúng là cách phổ biến nhất để các tổ chức lãng phí tiền và tự an ủi bằng sự bảo đảm giả.

Chương này cố ý đứng riêng khỏi các chương láng giềng. Chương 4.4 bao quát vận hành bảo mật: phía phòng thủ, giám sát theo dõi mối đe dọa và phản ứng với chúng. Chương này là đối trọng tấn công kiểm thử liệu sự phòng thủ đó có thực sự hoạt động. Chương 4.9 bao quát vòng đời phát triển phần mềm an toàn, nơi bảo mật được xây vào cách mã được thiết kế và phát hành; kiểm thử tấn công xác thực sản phẩm của vòng đời đó từ bên ngoài. Nó cũng xây trên nền tảng và văn hóa của chương 4.1 và các thực hành bảo mật ứng dụng của chương 4.2.

Với các doanh nghiệp lớn, kiểm thử tấn công vừa là công cụ giảm rủi ro vừa là nghĩa vụ quy định. Các nhà xử lý thanh toán, ngân hàng và nhà cung cấp y tế đối mặt yêu cầu kiểm thử tường minh. Với chính phủ, rủi ro đạt tới an ninh quốc gia và niềm tin công chúng: kẻ thù ở đây là các quốc gia-nhà nước có nguồn lực dồi dào, và các hệ thống họ nhắm vào vận hành bầu cử, trợ cấp và hạ tầng quan trọng. Trong cả hai bối cảnh, giá trị đến không phải từ báo cáo mà từ những gì bạn sửa và bạn học phát hiện cuộc xâm nhập kế tiếp nhanh hơn bao nhiêu.

## Các nguyên tắc chính

- Khớp cuộc tham gia với câu hỏi: quét, kiểm thử xâm nhập và đội đỏ trả lời những điều khác nhau.
- Có sự cho phép bằng văn bản và quy tắc tham gia rõ ràng trước khi bất kỳ ai chạm vào một hệ thống.
- Phát hiện vô giá trị cho đến khi chúng được khắc phục và kiểm thử lại; hãy theo dõi chúng như mọi công việc khác.
- Một đội đỏ tồn tại để làm đội xanh tốt hơn, không phải để thắng.
- Mô phỏng kẻ thù thật và kỹ thuật của chúng, không phải danh sách kiểm tra chung chung.
- Đo phát hiện và phản ứng, không chỉ số lượng lỗ hổng tìm thấy.
- Đề phòng sân khấu: một cuộc tham gia được định phạm vi để vượt qua trông ấn tượng và chẳng chứng minh gì.

## Khuyến nghị

### Hiểu dải bảo mật tấn công

Hãy bắt đầu bằng việc gọi tên thứ bạn đang mua. Quét lỗ hổng rộng, tự động và rẻ; hãy chạy nó liên tục trên hệ sinh thái của bạn để bắt các [Lỗ hổng và Phơi nhiễm Thông dụng](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (CVE) đã biết và cấu hình sai. Nó tạo ra khối lượng và dương tính giả, và nó không thể nói với bạn liệu một lỗi có thực sự khai thác được trong ngữ cảnh. Kiểm thử xâm nhập đặt một người kiểm thử lành nghề đối với một mục tiêu xác định trong một cửa sổ cố định, xâu chuỗi các điểm yếu để chứng minh tác động thực: phát hiện của bộ quét này, kết hợp với quyền yếu kia, cho ra quản trị viên miền. Nó trả lời "thứ cụ thể này có thể bị phá không, và tệ đến đâu."

Đội đỏ trả lời một câu hỏi lớn hơn: "nếu một kẻ thù kiên quyết nhắm vào chúng ta, chúng ta có nhận ra không, và có ngăn được chúng không." Nó hướng mục tiêu (rút bộ dữ liệu này, với tới hệ thống điều khiển này), bao quát toàn bộ bề mặt tấn công bao gồm con người và truy cập vật lý, và thường chạy mà không cảnh báo người phòng thủ. [Đội tím](https://en.wikipedia.org/wiki/Red_team#Purple_team) sụp đổ bức tường: đỏ và xanh làm việc cùng nhau trong cùng một phòng, kẻ tấn công chạy một kỹ thuật và người phòng thủ xem công cụ của họ có bắt được không, điều chỉnh phát hiện theo thời gian thực. Đội tím thường mang lại cải thiện phòng thủ nhiều hơn mỗi đô la so với một đội đỏ bí mật, vì mỗi hành động trở thành một khoảnh khắc dạy học.

### Chọn hộp đen, hộp xám hay hộp trắng có chủ đích

Bạn nói với người kiểm thử bao nhiêu định hình những gì bạn học. Kiểm thử hộp đen không cho họ gì ngoài một mục tiêu, mô phỏng một kẻ tấn công bên ngoài không có kiến thức nội bộ; nó thực tế nhưng chậm, và người kiểm thử có thể dành cả ngân sách cho do thám mà một kẻ thù thật sẽ mất nhiều tháng. Kiểm thử hộp trắng trao mã nguồn, sơ đồ kiến trúc và thông tin xác thực, cho phép người kiểm thử đi sâu và bao quát nhiều hơn trong thời gian có sẵn. Hộp xám nằm giữa: một ít kiến thức, một ít thông tin xác thực, mô phỏng một kẻ tấn công đã làm bài tập về nhà hoặc một người trong cuộc ác ý.

Với hầu hết kiểm thử ứng dụng, hộp xám hay trắng cho lợi tức tốt hơn, vì bạn trả tiền cho chiều sâu phân tích, không phải để người kiểm thử khám phá lại cách bố trí mạng con của bạn. Dành hộp đen cho khi sự thực tế của giai đoạn khám phá bản thân là thứ bạn muốn kiểm thử, như đo xem một người ngoài có thể học được bao nhiêu từ dấu chân công khai của bạn. Hãy tường minh về cái bạn đang đặt hàng, vì một báo cáo hộp đen tìm thấy ít có thể nghĩa là bạn an toàn hoặc có thể nghĩa là người kiểm thử hết thời gian ở chu vi.

### Định phạm vi cẩn thận và viết quy tắc tham gia

Phạm vi là nơi các cuộc tham gia thành hay bại. Một tài liệu [quy tắc tham gia](https://en.wikipedia.org/wiki/Rules_of_engagement) xác định cái gì trong giới hạn và cái gì không, kỹ thuật nào được phép, cửa sổ kiểm thử, các hệ thống và mạng được bao quát, yêu cầu xử lý dữ liệu, và liên hệ khẩn cấp ở cả hai phía. Nó nêu tên các hệ thống sản xuất bị cấm hoặc cần cẩn thận, đặt một quy tắc dừng nếu người kiểm thử tìm thấy điều gì đó nguy hiểm đang xảy ra, và xác định điều gì xảy ra nếu họ tình cờ gặp hoạt động của kẻ tấn công thật hoặc dữ liệu thực sự nhạy cảm.

Hãy viết ra đường leo thang và một lá thư "ra khỏi nhà tù": giấy phép người kiểm thử có thể xuất trình nếu nhân viên bảo mật hay cơ quan thực thi pháp luật chất vấn họ giữa chừng. Hãy thống nhất trước cách các phát hiện được lưu và truyền, vì một báo cáo kiểm thử xâm nhập là bản đồ cách xâm phạm bạn và phải được bảo vệ tương xứng. Phạm vi hẹp tạo ra phát hiện sâu trên bề mặt nhỏ; phạm vi rộng tạo ra độ bao phủ nông của bề mặt lớn. Hãy chọn có chủ đích, và không bao giờ để phạm vi lặng lẽ mở rộng giữa chừng mà không cấp phép lại.

### Coi sự cho phép là lằn ranh giữa kiểm thử và tội phạm

Hành động duy nhất tách một người kiểm thử xâm nhập khỏi tội phạm là sự cho phép. Truy cập các hệ thống bạn không được phép truy cập là tội phạm theo các luật như [Đạo luật Lừa đảo và Lạm dụng Máy tính](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) ở Hoa Kỳ và các luật tương đương ở nơi khác, và ý định tốt không phải biện hộ. Sự cho phép phải đến bằng văn bản từ người có thẩm quyền thực sự để cấp nó, bao quát chính xác các hệ thống và kỹ thuật trong phạm vi, và được ký trước khi công việc bắt đầu.

Hệ thống bên thứ ba làm phức tạp điều này. Nhà cung cấp đám mây của bạn, các nhà cung cấp phần mềm-như-một-dịch-vụ, và bất kỳ hạ tầng dùng chung nào có thể có chính sách kiểm thử riêng, và bạn không thể cho phép một cuộc tấn công vào tài sản bạn không sở hữu. Hãy kiểm tra quy tắc của nhà cung cấp, xin phép ở nơi được yêu cầu, và giữ việc kiểm thử trong phạm vi thuê của chính bạn. Kỹ thuật xã hội nhắm vào nhân viên nêu ra các câu hỏi đạo đức và pháp lý về sự đồng ý và tổn hại tâm lý mà bạn phải nghĩ trước. Khi nghi ngờ, hãy đưa cố vấn pháp lý vào; chi phí của một cuộc trò chuyện là tầm thường so với chi phí của một sự cố truy cập trái phép.

### Cân nhắc đội nội bộ so với người kiểm thử bên thứ ba

Một đội đỏ nội bộ biết môi trường của bạn, xây dựng quan hệ với người phòng thủ, và có thể kiểm thử liên tục thay vì trong các đợt hằng năm. Sự quen thuộc đó cũng là một hạn chế: họ chia sẻ điểm mù và giả định tổ chức của bạn, và tính độc lập của họ có thể bị đặt câu hỏi khi họ báo cáo cho cùng ban lãnh đạo với các hệ thống họ kiểm thử. Các công ty bên thứ ba mang đôi mắt mới, kỹ năng chuyên biệt, và tính độc lập mà kiểm toán viên và cơ quan quản lý thường đòi hỏi, nhưng họ vào việc chậm, tốn hơn mỗi cuộc tham gia, và rời đi khi báo cáo được giao.

Hầu hết các chương trình trưởng thành dùng cả hai. Đội nội bộ xử lý mô phỏng kẻ thù liên tục, điều chỉnh phát hiện, và kiến thức môi trường sâu khiến đội tím hiệu quả. Công ty bên ngoài cung cấp xác thực độc lập định kỳ, đáp ứng yêu cầu độc lập của các tiêu chuẩn như PCI DSS, và dò những vùng mà chính người của bạn đã thôi nhìn thấy. Dùng cái nào, hãy kiên quyết rằng người kiểm thử đủ trình độ: chứng chỉ như OSCP (Chuyên gia Bảo mật Tấn công Được Chứng nhận) và kinh nghiệm đã chứng minh quan trọng hơn một bài thuyết trình bán hàng bóng bẩy.

### Chạy chương trình thưởng lỗi và công bố có phối hợp

Một chương trình [thưởng lỗi](https://en.wikipedia.org/wiki/Bug_bounty_program) mời các nhà nghiên cứu bên ngoài tìm và báo cáo lỗ hổng để đổi lấy sự ghi nhận và thanh toán. Nó cho bạn kiểm thử liên tục, từ cộng đồng qua một dải kỹ năng mà bạn không bao giờ tuyển hết cùng lúc, và bạn chỉ trả cho phát hiện thực. Nó không thay thế cho kiểm thử xâm nhập có cấu trúc, vì các nhà nghiên cứu đuổi theo những gì trả tiền và có thể bỏ qua cả các loại, nhưng nó là bổ sung mạnh phơi bày các cuộc tấn công sáng tạo.

Trước khi chạy một chương trình thưởng có trả tiền, bạn cần một chính sách [công bố lỗ hổng có phối hợp](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure): một cách được công bố, dễ tìm để bất kỳ ai báo cáo vấn đề bảo mật an toàn, một cam kết không truy cứu pháp lý các nhà nghiên cứu thiện chí, mốc thời gian phản hồi xác định, và một quy trình nội bộ để phân loại và sửa những gì đến. Một tệp security.txt và một địa chỉ báo cáo rõ ràng là tối thiểu. Các cơ quan chính phủ ngày càng bắt buộc chính sách công bố lỗ hổng cho các hệ thống hướng công chúng, và việc không có kênh không ngăn các nhà nghiên cứu tìm lỗi; nó chỉ ngăn họ nói với bạn một cách an toàn.

### Dùng giả định bị xâm phạm và mô phỏng kẻ thù

Kiểm thử chỉ chu vi giả định kẻ tấn công bắt đầu từ bên ngoài, nhưng các vụ xâm phạm thực thường bắt đầu với một thông tin xác thực bị lừa đảo hay một laptop bị xâm phạm đã ở bên trong. Một bài tập [giả định bị xâm phạm](https://en.wikipedia.org/wiki/Breach_and_attack_simulation) cho người kiểm thử bắt đầu với một chỗ đứng chân, như truy cập với tư cách một nhân viên thường, và hỏi họ có thể đi xa đến đâu từ đó. Điều này kiểm thử trực tiếp phân đoạn nội bộ, phát hiện và biện pháp kiểm soát bán kính ảnh hưởng của bạn, thay vì đặt cược mọi thứ vào một chu vi cuối cùng sẽ bị vượt qua. Nó thường là cách dùng thời gian của đội đỏ tốt hơn so với xem họ vật lộn với một rìa được gia cố.

Hãy neo chiến dịch vào hành vi kẻ thù thật bằng [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), một cơ sở tri thức công khai về các chiến thuật và kỹ thuật kẻ tấn công thực sự dùng, được tổ chức từ truy cập ban đầu đến rút dữ liệu. Mô phỏng kẻ thù chọn một tác nhân đe dọa được biết là nhắm vào ngành của bạn, tái tạo các kỹ thuật được ghi lại của chúng, và kiểm thử liệu bạn có phát hiện và dừng từng bước. Điều này hữu ích hơn nhiều so với một cuộc tấn công chung chung, vì nó ánh xạ phòng thủ của bạn với các kẻ thù cụ thể bạn đối mặt và tạo ra phát hiện mà tình báo mối đe dọa của bạn có thể ưu tiên.

### Đưa phát hiện cho đội xanh và kỹ thuật phát hiện

Điểm của tấn công là phòng thủ tốt hơn. Mỗi hành động của đội đỏ là một cơ hội để hỏi: công cụ của chúng ta có tạo tín hiệu không, có ai thấy không, và họ có phản ứng đúng không. Hãy chạy các cuộc tham gia để mỗi kỹ thuật ánh xạ với một phát hiện bạn đã có, cần xây, hoặc cần điều chỉnh. Đây là kỹ thuật phát hiện: biến hành vi của kẻ tấn công thành cảnh báo đáng tin, và là nơi giá trị đội đỏ cộng dồn. Một phát hiện rằng "chúng tôi không bị phát hiện trong di chuyển ngang" nên trở thành một quy tắc phát hiện mới, được kiểm thử bằng cách chạy lại kỹ thuật.

Bài tập bàn giấy mở rộng điều này sang ra quyết định. Hãy tập hợp những người sẽ phản ứng với một sự cố thật và đi qua một kịch bản thực tế trên giấy: ai tuyên bố sự cố, ai nói chuyện với pháp lý, ai quyết định đưa một hệ thống ngoại tuyến. Bài tập bàn giấy rẻ, phơi bày khoảng trống về vai trò và giao tiếp mà kiểm thử kỹ thuật bỏ sót, và chuẩn bị những con người quan trọng nhất khi quản lý sự cố của chương 9.3 hoạt động. Hãy ghép đội đỏ kỹ thuật với bài tập bàn giấy đều đặn để cả công cụ lẫn con người của bạn được thực hành.

### Theo dõi khắc phục và kiểm thử lại

Một báo cáo lỗ hổng mà không ai hành động là một khoản nợ, vì giờ bạn cố ý chạy một lỗi mà kiểm toán viên có thể trích dẫn. Hãy nuôi mọi phát hiện vào hệ thống theo dõi công việc bình thường của bạn với một chủ sở hữu, một mức nghiêm trọng và một ngày đến hạn gắn với rủi ro. Phát hiện nghiêm trọng được xử lý khẩn cấp; phát hiện thấp hơn nhập vào tồn đọng với ưu tiên trung thực. Chỉ số quan trọng là thời gian khắc phục, không phải thời gian báo cáo.

Kiểm thử lại khép vòng. Sau khi một bản sửa được phát hành, người kiểm thử (hoặc một kiểm tra tự động) xác nhận lỗ hổng thực sự đã hết và bản sửa không mở một lỗ hổng mới. Không có kiểm thử lại, "đã khắc phục" là một hy vọng, không phải sự thật, và nhiều phát hiện tái diễn vì một bản sửa không đầy đủ hoặc một hồi quy đưa chúng trở lại. Các tiêu chuẩn như PCI DSS yêu cầu vòng này tường minh. Hãy xây kiểm thử lại vào hợp đồng tham gia để nó không phải chuyện nghĩ sau bị quên.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Tốt nhất cho | Ưu điểm | Nhược điểm |
|---|---|---|---|
| Quét lỗ hổng | Bao phủ liên tục các lỗi đã biết | Rẻ, rộng, tự động, thường xuyên | Ồn; không chứng minh được khả năng khai thác |
| Kiểm thử xâm nhập | Chứng minh tác động lên mục tiêu xác định | Sâu, hiểu biết của con người; chuỗi khai thác thực | Tại một thời điểm; phạm vi hẹp; tốn kém |
| Đội đỏ | Kiểm thử phát hiện và phản ứng | Thực tế; thực hành con người và quy trình | Đắt; chậm; cần đội xanh trưởng thành |
| Đội tím | Cải thiện phát hiện nhanh | Học nhiều mỗi đô la; hợp tác | Kém thực tế hơn; cần cả hai đội có mặt |
| Thưởng lỗi | Khám phá liên tục từ cộng đồng | Trả theo phát hiện; kỹ năng đa dạng | Bao phủ không đều; gánh nặng phân loại; cần quy trình |

Căng thẳng cốt lõi là giữa tính thực tế và tốc độ học. Một đội đỏ bí mật là bài kiểm thử thực tế nhất bạn có thể chạy, nhưng bài học đến chậm và chỉ sau một chiến dịch đầy đủ, và một đội xanh chưa trưởng thành học được ít từ việc bị đánh bại trong im lặng. Đội tím hy sinh yếu tố bất ngờ để tối đa hóa tốc độ người phòng thủ cải thiện. Căng thẳng thứ hai là bề rộng so với chiều sâu: quét bao phủ mọi thứ một cách nông, trong khi một cuộc kiểm thử xâm nhập bao phủ một lát mỏng một cách sâu. Các chương trình trưởng thành xếp tầng những thứ này thay vì chọn một, chạy quét liên tục bên dưới kiểm thử sâu định kỳ và thỉnh thoảng các chiến dịch đội đỏ phạm vi đầy đủ. Nước đi sai là mua một cuộc kiểm thử xâm nhập hằng năm duy nhất, cất báo cáo vào hồ sơ, và gọi vấn đề là đã giải quyết.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi chúng ta đặt hàng kiểm thử tấn công, chúng ta có rõ mình thực sự đang hỏi câu hỏi nào, và cuộc tham gia có khớp với nó không?** Nhiều tổ chức mua một "kiểm thử xâm nhập" và nhận một bản quét lỗ hổng với tóm tắt do con người viết, rồi tin rằng họ đã kiểm thử phòng thủ của mình trong khi họ chỉ kiểm tra các lỗi đã biết. Số khác đặt hàng một đội đỏ khi năng lực phát hiện của họ chưa trưởng thành đến mức bài tập chỉ chứng minh điều ai cũng đã biết. Hãy mang ba phạm vi tham gia gần nhất và các báo cáo kết quả, và hỏi liệu mỗi cái có trả lời câu hỏi bạn cần được trả lời không: độ bao phủ các lỗ hổng đã biết, khả năng khai thác của một mục tiêu cụ thể, hay khả năng phát hiện và phản ứng với một cuộc xâm nhập. Câu trả lời nên định hình một hỗn hợp có chủ đích gồm quét, kiểm thử xâm nhập, và đội đỏ hay đội tím khớp với độ trưởng thành của bạn.

2. **Điều gì xảy ra với một phát hiện sau khi báo cáo đến, và làm sao chúng ta chứng minh nó đã được sửa?** Giá trị của bảo mật tấn công hoàn toàn nằm ở khắc phục, vậy mà nhiều chương trình đo thành công bằng kích thước báo cáo thay vì sự thu nhỏ của rủi ro. Hãy truy một phát hiện thực từ cuộc tham gia gần nhất của bạn: ai sở hữu nó, nó được ưu tiên so với công việc tính năng thế nào, khi nào nó được sửa, và có ai xác nhận bản sửa thực sự hoạt động không. Nếu bạn không đưa ra được dấu vết đó, kiểm thử của bạn đang tạo ra kiến thức mà bạn không hành động trên, tệ hơn không biết, vì giờ bạn cố ý bị phơi bày. Đầu ra của cuộc thảo luận này nên là một quy trình khắc phục được theo dõi với chủ sở hữu, hạn chót dựa trên rủi ro, và kiểm thử lại bắt buộc được xây vào mọi hợp đồng.

3. **Đội đỏ của chúng ta đang làm đội xanh tốt hơn, hay chỉ ghi điểm?** Một đội đỏ ăn mừng chiến thắng không bị phát hiện và tích trữ kỹ thuật của nó thì giải trí và vô dụng. Mối quan hệ nên mang tính hợp tác bên dưới bề mặt đối kháng: mỗi kỹ thuật không bị phát hiện nên trở thành một quy tắc phát hiện mới, mỗi con đường thành công nên thông tin cho phân đoạn, và hai đội nên họp tổng kết cùng nhau. Hãy hỏi người phòng thủ của bạn họ đã học gì từ cuộc tham gia đội đỏ gần nhất và liệu có phát hiện hay biện pháp kiểm soát cụ thể nào đã thay đổi do đó không. Nếu câu trả lời trung thực là không, bạn đang trả tiền cho sân khấu, và bạn nên dịch chuyển hướng tới đội tím và mô phỏng kẻ thù được gắn tường minh với kỹ thuật phát hiện.

4. **Trước cuộc tham gia kế tiếp, chúng ta có sự cho phép bằng văn bản cho mọi tài sản trong phạm vi, bao gồm cả những thứ chúng ta không sở hữu không?** Sự cho phép là lằn ranh giữa một cuộc kiểm thử xâm nhập và một sự cố tội phạm máy tính, và trong một tổ chức lớn các hệ thống người kiểm thử sẽ chạm vào hiếm khi nằm trong một ranh giới sở hữu duy nhất: chúng trải qua các phạm vi thuê đám mây, nền tảng phần mềm-như-một-dịch-vụ, mạng được quản lý, và hạ tầng dùng chung mà một đối tác hay nhà cung cấp kiểm soát. Áp lực cạnh tranh là tốc độ, vì đuổi theo sự cho phép đã ký và chính sách kiểm thử của nhà cung cấp thì chậm và cám dỗ bỏ qua khi hạn chót lù lù. Hãy mang bản nháp quy tắc tham gia, bản kiểm kê tài sản với chủ sở hữu được nêu tên cho mỗi hệ thống, chính sách kiểm thử của đám mây và nhà cung cấp liên quan, và lá thư cho phép đã ký mà người kiểm thử có thể xuất trình nếu bị chất vấn giữa chừng. Với công việc doanh nghiệp và chính phủ, rủi ro là cấp bách: một lần dò không được phép vào một nền tảng dùng chung có thể vi phạm hợp đồng, kích hoạt báo cáo quy định, hoặc, với một cơ quan công, thành tiêu đề báo về chính phủ tấn công các hệ thống nó không có quyền chạm vào, nên cố vấn pháp lý phải ký duyệt trước khi bất kỳ ai bắt đầu.

5. **Chúng ta đang đầu tư vào đội đỏ nội bộ, công ty bên ngoài, hay cả hai, và sự phân chia đó có khớp với những gì chúng ta thực sự cần không?** Đây là quyết định xây-so-với-mua với tiền thật và hệ quả nhiều năm: một đội nội bộ tốn lương và công cụ và mang lại mô phỏng kẻ thù liên tục cùng kiến thức môi trường sâu, trong khi các công ty bên ngoài tốn hơn mỗi cuộc tham gia nhưng mang đôi mắt mới, kỹ năng chuyên biệt, và tính độc lập mà kiểm toán viên và cơ quan quản lý đòi hỏi. Căng thẳng là mỗi bên bao quát điểm mù của bên kia, nên coi chúng là thay thế thay vì bổ sung thường để lại khoảng trống. Hãy mang chi tiêu hiện tại của bạn cho mỗi bên, chứng chỉ và thành tích đã chứng minh của những người làm việc, nhịp các cuộc tham gia, và yêu cầu độc lập mà tiêu chuẩn của bạn áp đặt. Trong một doanh nghiệp chịu quy định, PCI DSS và các chế độ tương tự có thể buộc kiểm thử độc lập bên ngoài bất kể đội nội bộ của bạn tốt đến đâu; trong chính phủ, quy tắc mua sắm và nhu cầu cho thấy đánh giá khoảng cách tay trước khi cấp phép vận hành thường khiến một bên thứ ba được công nhận là bắt buộc, không tùy chọn.

6. **Chúng ta có một kênh an toàn để các nhà nghiên cứu bên ngoài báo cáo lỗ hổng không, và chúng ta có sẵn sàng xử lý những gì đến không?** Một tổ chức lớn hướng công chúng đã bị các nhà nghiên cứu dò xét dù có mời họ hay không, và câu hỏi duy nhất là liệu họ có thể nói với bạn an toàn hay bị buộc công bố hoặc bán những gì họ tìm thấy. Cân nhắc đối lập là sự sẵn sàng: mở một chính sách công bố có phối hợp hay một chương trình thưởng lỗi có trả tiền tạo ra báo cáo đến và gánh nặng phân loại, và một chương trình trả tiền cho phát hiện mà nó không bao giờ sửa tệ hơn không có. Hãy mang tệp security.txt và địa chỉ báo cáo hiện tại của bạn nếu có, quy trình tiếp nhận và phân loại, mốc thời gian phản hồi bạn có thể cam kết trung thực, và năng lực tồn đọng để khắc phục những gì đến. Với các cơ quan chính phủ, một chính sách công bố lỗ hổng trên các hệ thống công khai ngày càng là chỉ thị hơn là phép lịch sự, và với doanh nghiệp một chương trình thưởng được vận hành tốt vừa là nguồn phát hiện sáng tạo vừa là bằng chứng trưởng thành trong thẩm định khách hàng, nên quyết định ít là có nên có một kênh hay không mà là liệu bạn có đủ nhân sự để tôn trọng nó.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Bạn không thể gánh một đội đỏ nội bộ, vì vậy hãy xếp tầng độ bao phủ rẻ. Nối quét lỗ hổng vào đường ống triển khai để bắt lỗi phụ thuộc đã biết trên mỗi bản dựng, công bố một tệp security.txt và một chính sách công bố có phối hợp đơn giản để các nhà nghiên cứu liên hệ được với bạn, và đặt hàng một cuộc kiểm thử xâm nhập hộp xám duy nhất từ một công ty có uy tín trước thương vụ doanh nghiệp đầu tiên, theo dõi mỗi phát hiện đến khi có bản sửa được xác nhận. Tốc độ quan trọng hơn một chương trình rộng: chọn một bài kiểm thử mở khóa một thương vụ hay đóng rủi ro lớn nhất của bạn và bỏ qua phần còn lại cho đến khi bạn lớn.

**Doanh nghiệp nhỏ.** Không có chuyên gia bảo mật trong biên chế và ngân sách eo hẹp, hãy mua thay vì xây. Dùng một dịch vụ quét được quản lý và thuê một công ty kiểm thử xâm nhập bên ngoài theo nhịp khiêm tốn thay vì dựng bất kỳ năng lực nội bộ nào, và bảo đảm hợp đồng của bạn bao gồm một lần kiểm thử lại để "đã sửa" được chứng minh, không giả định. Nước đi có giá trị cao nhất, chi phí thấp nhất của bạn là một cách công bố cho bất kỳ ai báo cáo lỗi cộng với kỷ luật vá nhanh, vì hầu hết các vụ xâm phạm thực tế vào một doanh nghiệp cỡ bạn đến qua các điểm yếu đã biết, chưa vá.

**Doanh nghiệp lớn.** Ở quy mô lớn thách thức là quản trị qua nhiều đội. Hãy chạy quét liên tục bên dưới các cuộc kiểm thử xâm nhập bên ngoài độc lập định kỳ thỏa mãn các tiêu chuẩn như PCI DSS, duy trì một đội đỏ nội bộ cho mô phỏng kẻ thù liên tục và đội tím, và quản lý khắc phục như một danh mục được theo dõi với chủ sở hữu, hạn chót dựa trên rủi ro, và kiểm thử lại bắt buộc. Hãy đưa mọi kỹ thuật không bị phát hiện vào kỹ thuật phát hiện, và tạo bằng chứng kiểm toán, độ bao phủ, mốc thời gian và tỷ lệ đóng, mà tuân thủ và hội đồng quản trị của bạn mong đợi.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình toàn bộ chương trình. Hãy duy trì chính sách công bố lỗ hổng trên các hệ thống hướng công chúng như các chỉ thị ngày càng yêu cầu, dùng các đánh giá viên độc lập được công nhận cho kiểm thử xâm nhập kiểm soát giấy phép vận hành của một hệ thống, và mô hình hóa mô phỏng kẻ thù theo các tác nhân quốc gia-nhà nước cụ thể mà các đối tác tình báo của bạn đánh dấu. Hãy xử lý sự cho phép, phạm vi và xử lý dữ liệu với sự chặt chẽ thêm vì các hệ thống vận hành bầu cử, trợ cấp và hạ tầng quan trọng, và biến kiểm thử lại thành điều kiện tiên quyết để giữ bất kỳ hệ thống nào hoạt động.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp fintech hai mươi người không thể gánh một đội đỏ nội bộ, nên xếp tầng những gì có thể. Quét lỗ hổng tự động chạy trên mỗi lần triển khai qua đường ống của nó, bắt sớm các lỗi phụ thuộc đã biết. Nó công bố một tệp security.txt và một chính sách công bố có phối hợp đơn giản, rồi mở một chương trình thưởng lỗi khiêm tốn trên một nền tảng công khai khi sản phẩm ổn định, trả tiền cho các nhà nghiên cứu thật cho lỗi thật. Trước khi ký khách hàng doanh nghiệp đầu tiên, nó đặt hàng một cuộc kiểm thử xâm nhập hộp xám của ứng dụng từ một công ty có uy tín, theo dõi mọi phát hiện đến khi đóng trong bộ theo dõi vấn đề bình thường, và trả tiền cho một lần kiểm thử lại để xác nhận các bản sửa. Cách tiếp cận xếp tầng này cho độ bao phủ bảo mật đáng tin ở mức chi phí công ty khởi nghiệp duy trì được, và báo cáo kiểm thử xâm nhập trở thành bằng chứng nó có thể chia sẻ trong thẩm định khách hàng.

**Doanh nghiệp lớn.** Một nhà bán lẻ đa quốc gia xử lý thanh toán thẻ phải đáp ứng PCI DSS, đòi hỏi cả kiểm thử xâm nhập nội bộ lẫn bên ngoài ít nhất hằng năm và sau những thay đổi đáng kể, cộng kiểm thử phân đoạn để chứng minh môi trường chủ thẻ được cô lập. Nó chạy quét liên tục qua hàng nghìn tài sản, đặt hàng các cuộc kiểm thử xâm nhập bên ngoài độc lập để thỏa mãn tiêu chuẩn, và duy trì một đội đỏ nội bộ chạy các bài tập giả định bị xâm phạm dựa trên MITRE ATT&CK đối với các tác nhân đe dọa được biết là nhắm vào bán lẻ. Đội đỏ làm việc chặt chẽ với chức năng vận hành bảo mật của chương 4.4: mỗi kỹ thuật không bị phát hiện trở thành một phiếu kỹ thuật phát hiện, và các buổi đội tím hằng quý điều chỉnh cảnh báo. Khắc phục được theo dõi với hạn chót dựa trên rủi ro, và toàn bộ chương trình tạo ra bằng chứng kiểm toán mà tuân thủ của chương 4.6 đòi hỏi.

**Chính phủ.** Một cơ quan quốc gia vận hành các hệ thống trợ cấp công dân đối mặt kẻ thù quốc gia-nhà nước và một nhiệm vụ công chúng bảo vệ dữ liệu cá nhân nhạy cảm. Nó duy trì chính sách công bố lỗ hổng trên mọi hệ thống hướng công chúng, như các chỉ thị chính phủ ngày càng yêu cầu, trao cho các nhà nghiên cứu một kênh an toàn để báo lỗi. Các đánh giá viên bên thứ ba độc lập thực hiện kiểm thử xâm nhập như một phần quy trình cấp phép trước khi bất kỳ hệ thống nào hoạt động, và giám sát liên tục bao gồm quét liên tục. Cơ quan chạy mô phỏng kẻ thù mô hình hóa theo các nhóm đe dọa cụ thể mà đối tác tình báo của nó đánh dấu, và các bài tập bàn giấy đều đặn diễn tập ứng phó sự cố và phối hợp pháp lý mà một vụ xâm phạm thực sẽ đòi hỏi. Phát hiện nuôi một chương trình khắc phục chính thức với mốc thời gian bắt buộc, và kiểm thử lại là điều kiện tiên quyết để giữ giấy phép vận hành của một hệ thống.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của bảo mật tấn công là vụ xâm phạm bạn không phải chịu. Một vụ xâm phạm dữ liệu nghiêm trọng tốn hàng triệu về ứng phó trực tiếp, tiền phạt quy định, trách nhiệm pháp lý, khách hàng bỏ đi và thiệt hại danh tiếng, và yếu tố đắt nhất đơn lẻ là một cuộc xâm nhập không bị phát hiện bao lâu. Đội đỏ và đội tím tấn công trực tiếp con số đó bằng cách thu hẹp khoảng cách giữa xâm phạm và phát hiện. Một cuộc kiểm thử xâm nhập tìm thấy một con đường khai thác được đến cơ sở dữ liệu khách hàng của bạn, được sửa trước khi kẻ tấn công tìm thấy, hoàn vốn cho toàn bộ chương trình nhiều lần trong một sự cố được tránh duy nhất.

Cũng có những động lực cứng. PCI DSS bắt buộc kiểm thử xâm nhập cho bất kỳ ai xử lý dữ liệu thẻ. Các khung và chế độ cấp phép chính phủ yêu cầu đánh giá độc lập trước và trong khi vận hành. Khách hàng doanh nghiệp đòi các báo cáo kiểm thử xâm nhập gần đây như điều kiện hợp đồng. Trong các trường hợp này kiểm thử không tùy chọn, và câu hỏi chỉ là liệu bạn có rút ra giá trị bảo mật thực từ số tiền bạn dù sao cũng phải chi.

Tổng chi phí sở hữu bao gồm nhiều hơn phí tham gia. Hãy ngân sách cho công cụ và nhân sự của một đội nội bộ nếu bạn xây một cái, gánh nặng phân loại của một chương trình thưởng lỗi, và trên hết là công việc khắc phục mà phát hiện tạo ra, nơi chi tiêu thực sự đáp xuống. Một chương trình đặt hàng kiểm thử nhưng tài trợ thiếu cho việc sửa là điều tệ nhất của cả hai thế giới: nó trả tiền cho tin xấu rồi trả lần nữa khi phát hiện bị bỏ qua bị khai thác. Để trình bày lập luận với ban lãnh đạo, hãy nối kiểm thử với các chỉ số họ theo dõi: thời gian trung bình để phát hiện, thời gian trung bình để khắc phục, phát hiện kiểm toán đã đóng, và mức giảm rủi ro trên các tài sản quan trọng nhất của bạn.

## Phản mẫu và cạm bẫy

- **Quét-và-đổi-tên:** bán một bản quét lỗ hổng như một cuộc kiểm thử xâm nhập, giao đầu ra của công cụ mà không có xác thực của con người hay xâu chuỗi khai thác.
- **Báo cáo rồi quên:** coi sản phẩm bàn giao là mục tiêu, cất các phát hiện vào hồ sơ, và không bao giờ theo dõi khắc phục hay kiểm thử lại.
- **Định phạm vi để vượt qua:** thu hẹp cuộc tham gia để các hệ thống có khả năng thất bại nhất tiện thể nằm ngoài giới hạn, tạo ra một báo cáo sạch vô nghĩa.
- **Đội đỏ như bảng điểm:** một đội đối kháng tích trữ kỹ thuật và ăn mừng chiến thắng thay vì làm người phòng thủ tốt hơn.
- **Kiểm thử một đội xanh chưa trưởng thành một cách bí mật:** chạy một đội đỏ lén lút trước khi bạn có bất kỳ năng lực phát hiện nào, nên bài tập chỉ chứng minh điều bạn đã biết.
- **Không có sự cho phép hoặc phạm vi mơ hồ:** bắt đầu công việc mà không có phép bằng văn bản, hoặc để phạm vi trôi vào các hệ thống bạn không sở hữu, rước thảm họa pháp lý.
- **Ám ảnh chu vi:** chỉ kiểm thử rìa bên ngoài trong khi bỏ qua thực tế giả định-bị-xâm-phạm rằng kẻ tấn công bắt đầu từ bên trong.
- **Bỏ qua kênh công bố:** không có cách an toàn cho nhà nghiên cứu bên ngoài báo lỗi, nên họ công bố công khai hoặc bán thay thế.
- **Chỉ số sân khấu:** đếm lỗ hổng tìm thấy thay vì rủi ro giảm, phát hiện cải thiện, và thời gian khắc phục rút ngắn.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Kiểm thử thỉnh thoảng và phản ứng, thường là một cuộc kiểm thử xâm nhập hằng năm duy nhất làm để đánh dấu ô, hoặc chỉ được kích hoạt sau một sự cố. Báo cáo được cất vào hồ sơ với ít theo đuổi, khắc phục không được theo dõi, không có kênh công bố, và việc phát hiện một cuộc xâm nhập thực chưa được kiểm thử và có khả năng vắng mặt.
- **Mức 2, Phát triển:** Quét lỗ hổng và kiểm thử xâm nhập tồn tại nhưng không nhất quán qua các đội, với một số nhóm quét liên tục và số khác không hề. Phát hiện được nắm bắt ở đâu đó, dù chủ sở hữu và hạn chót rải rác, kiểm thử lại là tùy nghi, và một kênh công bố có phối hợp có thể tồn tại cho một số hệ thống nhưng không phải toàn hệ sinh thái.
- **Mức 3, Chuẩn hóa:** Kiểm thử tấn công là một chương trình có tài liệu được thực thi toàn tổ chức, không phải một sự kiện. Quét chạy liên tục bên dưới các cuộc kiểm thử xâm nhập theo lịch được đặt hàng theo nhịp xác định và sau những thay đổi lớn, quy tắc tham gia và sự cho phép là thực hành tiêu chuẩn, mọi phát hiện được theo dõi đến khi đóng với chủ sở hữu và hạn chót dựa trên rủi ro, kiểm thử lại là bắt buộc, và một chính sách công bố có phối hợp bao quát mọi hệ thống hướng công chúng.
- **Mức 4, Quản lý:** Chương trình được đo và kiểm soát theo các đường cơ sở. Bạn theo dõi thời gian trung bình để phát hiện và để khắc phục, phần trăm kỹ thuật của đội đỏ tạo ra tín hiệu, độ bao phủ phát hiện đối với các kỹ thuật MITRE ATT&CK liên quan đến ngành của bạn, tỷ lệ tái diễn phát hiện, và thời gian phản hồi công bố, và bạn giữ mỗi chỉ số theo một mục tiêu và hành động khi nó trôi. Bài tập giả định bị xâm phạm và mô phỏng kẻ thù là thường lệ, một đội đỏ vận hành liên tục, phát hiện nuôi kỹ thuật phát hiện, và quyết định đi hay không đi dựa trên bằng chứng thay vì ý kiến.
- **Mức 5, Điều phối:** Đội đỏ và đội tím được tích hợp trong toàn tổ chức và thích ứng. Mọi kỹ thuật ánh xạ với một phát hiện đã kiểm thử, mô phỏng kẻ thù theo dõi các tác nhân đe dọa cụ thể hiện đang nhắm vào ngành của bạn khi tình báo dịch chuyển, và chương trình liên tục tinh chỉnh phạm vi, kỹ thuật và chỉ số khi nó học. Kiểm thử tấn công, vận hành bảo mật, kỹ thuật phát hiện và ứng phó sự cố vận hành như một vòng lặp thu hẹp khoảng cách giữa xâm phạm và phát hiện một cách đo được theo thời gian.

## Ý tưởng để thảo luận

1. Nếu một kẻ tấn công thật có chỗ đứng chân với tư cách nhân viên thường hôm nay, chúng với tới được bao xa trước khi ai nhận ra, và làm sao bạn biết?
2. Cuộc tham gia nào gần đây của bạn thực sự thực tế, và cuộc nào được định phạm vi để các thất bại có khả năng tiện thể nằm ngoài giới hạn?
3. Còn bao nhiêu phát hiện từ cuộc kiểm thử trước của bạn đang mở, và điều đó nói gì về việc kiểm thử hay khắc phục mới là nút thắt thực của bạn?
4. Các nhà nghiên cứu bên ngoài có cách an toàn, hiển nhiên để báo cáo một lỗ hổng cho bạn không, và điều gì xảy ra khi một báo cáo đến?
5. Lần cuối những người ứng phó sự cố của bạn diễn tập một vụ xâm phạm trên giấy là khi nào, và bài tập bàn giấy có phơi bày khoảng trống mà kiểm thử kỹ thuật bỏ sót không?
6. Bạn đang đo lỗ hổng tìm thấy, hay đang đo phát hiện cải thiện và rủi ro giảm?

## Những điểm cần ghi nhớ

- Bảo mật tấn công là một dải: quét tìm lỗi đã biết, kiểm thử xâm nhập chứng minh khả năng khai thác, và đội đỏ kiểm thử phát hiện và phản ứng. Hãy khớp cuộc tham gia với câu hỏi.
- Sự cho phép bằng văn bản và quy tắc tham gia rõ ràng là lằn ranh giữa kiểm thử bảo mật và tội phạm; không bao giờ bỏ qua chúng, đặc biệt trên các hệ thống bạn không sở hữu đầy đủ.
- Giá trị nằm ở khắc phục và kiểm thử lại, không phải báo cáo. Hãy theo dõi mọi phát hiện với một chủ sở hữu, hạn chót dựa trên rủi ro và một bản sửa được xác nhận.
- Một đội đỏ tồn tại để làm đội xanh tốt hơn. Hãy đưa phát hiện vào kỹ thuật phát hiện, ưu tiên đội tím và các bài tập giả định bị xâm phạm, và neo các chiến dịch vào kỹ thuật kẻ thù thật qua MITRE ATT&CK.
- Đo phát hiện và phản ứng, không chỉ số lượng lỗ hổng, và đề phòng các cuộc tham gia được định phạm vi để vượt qua, vốn tạo ra sự thoải mái mà không có bảo mật.

## Tài liệu tham khảo và đọc thêm

- Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*
- Peter Kim, *The Hacker Playbook 3: Practical Guide to Penetration Testing*
- Jim O'Gorman, Devon Kearns và Mati Aharoni, *Metasploit: The Penetration Tester's Guide*
- Joe Vest và James Tubberville, *Red Team Development and Operations: A Practical Guide*
- MITRE, khung và cơ sở tri thức *MITRE ATT&CK*
- Payment Card Industry Security Standards Council, *PCI DSS Requirements and Testing Procedures* và *Penetration Testing Guidance*
- National Institute of Standards and Technology, *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*
- Dafydd Stuttard và Marcus Pinto, *The Web Application Hacker's Handbook*
