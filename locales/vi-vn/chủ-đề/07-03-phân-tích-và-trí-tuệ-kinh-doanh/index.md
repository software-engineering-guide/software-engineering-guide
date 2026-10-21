# 7.3 Phân tích và trí tuệ kinh doanh

## Tổng quan và động lực

Phân tích và trí tuệ kinh doanh biến dữ liệu được quản trị, được thiết kế kỹ thuật thành hiểu biết và hành động. [Trí tuệ kinh doanh](https://en.wikipedia.org/wiki/Business_intelligence) (BI) theo truyền thống nghĩa là báo cáo, bảng điều khiển và công cụ tự phục vụ cho phép mọi người thấy điều gì đang xảy ra trong doanh nghiệp. Phân tích là thực hành rộng hơn của việc đặt và trả lời câu hỏi bằng dữ liệu, từ mô tả đơn giản về quá khứ đến các mô hình đề xuất nên làm gì tiếp theo. Cùng nhau, chúng là cách một tổ chức nhìn thấy chính mình.

Với các đội lớn, tầng này là nơi dữ liệu hoặc xứng đáng được giữ lại hoặc trở thành nguồn gây nhầm lẫn. Khi hàng nghìn nhân viên có thể tự xây báo cáo, rủi ro không phải là quá ít thông tin mà là quá nhiều thông tin xung đột: ba bảng điều khiển cho ba con số doanh thu khác nhau, cái nào cũng bảo vệ được, không cái nào có thẩm quyền. Doanh nghiệp sống chết với những con số trong bộ slide hội đồng quản trị và hồ sơ quy định. Các cơ quan chính phủ báo cáo với cơ quan lập pháp, cơ quan giám sát và công chúng. Trong cả hai, một chỉ số có nghĩa khác nhau với những người khác nhau là một khoản nợ. Một biểu đồ gây hiểu lầm, dù vô tình, có thể thúc đẩy các quyết định sai tốn kém hoặc làm xói mòn lòng tin công chúng.

Ý tưởng then chốt để thuần hóa điều này ở quy mô lớn là [lớp ngữ nghĩa](https://en.wikipedia.org/wiki/Semantic_layer): một định nghĩa trung tâm, được quản trị về các chỉ số và chiều mà mọi công cụ và báo cáo đều lấy từ đó, để "khách hàng hoạt động" hay "doanh thu hằng tháng" được tính theo một cách thống nhất ở mọi nơi. Xung quanh ý tưởng đó là các kỷ luật của trực quan hóa trung thực, thiết kế bảng điều khiển có chủ đích, và quản lý sự lan tràn mà tự phục vụ chắc chắn tạo ra. Chương này chỉ cho bạn cách trao cho mọi người quyền truy cập dữ liệu rộng rãi mà không từ bỏ một phiên bản duy nhất của sự thật.

## Các nguyên tắc chính

- Nên có một định nghĩa được quản trị cho mỗi chỉ số quan trọng, được dùng ở mọi nơi.
- Khớp loại phân tích với câu hỏi: mô tả, chẩn đoán, dự đoán, hay đề xuất.
- Tự phục vụ mạnh mẽ nhưng phải được quản trị để ngăn lan tràn chỉ số.
- Biểu đồ phải trung thực; mục tiêu là hiểu biết, không phải thuyết phục bằng bóp méo.
- Bảng điều khiển nên thúc đẩy quyết định, không chỉ hiển thị dữ liệu.
- Chứng nhận nội dung đáng tin để người tiêu dùng biết nên dựa vào cái gì.
- Chọn lọc và cho nghỉ hưu; nhiều bảng điều khiển hơn không phải nhiều hiểu biết hơn.
- Nhúng phân tích nơi quyết định được đưa ra, thay vì chỉ trong một cổng BI riêng.

## Khuyến nghị

### Hiểu bốn loại phân tích

Phân tích mô tả báo cáo điều đã xảy ra. Phân tích chẩn đoán giải thích vì sao nó xảy ra. [Phân tích dự đoán](https://en.wikipedia.org/wiki/Predictive_analytics) dự báo điều có khả năng xảy ra. [Phân tích đề xuất](https://en.wikipedia.org/wiki/Prescriptive_analytics) khuyến nghị nên làm gì về nó. Hầu hết tổ chức đầu tư quá mức vào bảng điều khiển mô tả và đầu tư thiếu vào chẩn đoán và hành động. Hãy đẩy công việc của bạn lên bậc thang này có chủ đích. Ghép mỗi chỉ số quan trọng với khả năng đào sâu vào nguyên nhân, và nối dự đoán với các quyết định và can thiệp cụ thể. Như vậy phân tích thay đổi hành vi thay vì chỉ mô tả nó.

### Xây lớp ngữ nghĩa và quản trị chỉ số

Hãy xác định chỉ số và chiều một lần, trong một lớp ngữ nghĩa trung tâm, và để mọi công cụ BI, sổ tay và báo cáo nhúng tính toán từ các định nghĩa đó. Điều này giết chết vấn đề kinh điển của các con số phân kỳ. Nó cũng làm logic chỉ số được quản lý phiên bản, kiểm thử được và rà soát được. Hãy quản trị chỉ số như một API: mỗi chỉ số được chứng nhận có chủ sở hữu, định nghĩa rõ ràng và nhật ký thay đổi. Giữ chỉ số được chứng nhận tách khỏi chỉ số thử nghiệm, để người tiêu dùng biết cái nào có thẩm quyền.

### Cho phép tự phục vụ trong lan can

Hãy trao cho nhà phân tích và người dùng kinh doanh quyền truy cập tự phục vụ để khám phá dữ liệu. Các đội BI trung tâm không trả lời được mọi câu hỏi, và nút thắt chỉ đẩy mọi người về bảng tính. Nhưng hãy cung cấp lan can: các tập dữ liệu được chứng nhận đã chọn lọc, lớp ngữ nghĩa cho chỉ số nhất quán, mẫu và đào tạo. Mục tiêu đơn giản: làm con đường dễ dùng định nghĩa được quản trị. Đánh dấu các bậc nội dung (được chứng nhận, được đội hỗ trợ, và cá nhân) để tự do khám phá không giả làm sự thật chính thức.

### Thiết kế bảng điều khiển cho quyết định

Hãy bắt đầu mọi bảng điều khiển từ quyết định nó hỗ trợ và khán giả đưa ra quyết định đó. Dẫn đầu bằng vài chỉ số quan trọng. Cung cấp ngữ cảnh (mục tiêu, xu hướng, so sánh) để các con số diễn giải được, và cho phép đào sâu để chẩn đoán. Chống lại thôi thúc nhồi mọi biểu đồ có sẵn vào một trang. Một bảng điều khiển trả lời "chúng ta có đúng hướng không, và nếu không thì tôi nên nhìn ở đâu?" đáng giá hơn nhiều so với cái hiển thị năm mươi chỉ số mà không ai hành động.

### Thực hành trực quan hóa dữ liệu trung thực

Hãy chọn kiểu biểu đồ phù hợp với dữ liệu: đường cho xu hướng theo thời gian, cột cho so sánh giữa các danh mục. Tránh biểu đồ tròn cho bất cứ thứ gì hơn vài lát. Bắt đầu trục biểu đồ cột từ số không, giữ thang nhất quán, và tránh trục kép tạo ra tương quan giả. Dùng màu có mục đích và dễ tiếp cận, không phải để trang trí. Ghi nhãn rõ ràng, và cho thấy độ bất định nơi nó quan trọng. Phép thử đơn giản: một người xem có hiểu biết có đi đến cùng kết luận mà dữ liệu ủng hộ, hay thiết kế đã đẩy họ về kết luận khác?

### Chọn lọc nội dung và chống lan tràn

Tự phục vụ không có chọn lọc tạo ra hàng nghìn bảng điều khiển cũ, trùng lặp và bị bỏ rơi. Hãy áp dụng quản lý vòng đời: theo dõi mức sử dụng, lưu trữ nội dung không dùng, loại bỏ bản trùng, và định kỳ chứng nhận lại những gì còn lại. Làm danh mục được chứng nhận dễ tìm, để mọi người tái sử dụng nội dung đáng tin thay vì xây lại. Một tập nhỏ hơn các bảng điều khiển đáng tin, được bảo trì tốt thắng một nghĩa địa lan tràn.

### Nhúng phân tích và báo cáo vận hành

Không phải mọi phân tích thuộc về một cổng riêng. Hãy nhúng các chỉ số và báo cáo liên quan trực tiếp vào các ứng dụng vận hành nơi mọi người đã làm việc, như CRM (hệ thống [quản lý quan hệ khách hàng](https://en.wikipedia.org/wiki/Customer_relationship_management)), hệ thống quản lý hồ sơ vụ việc, hay công cụ phiếu hỗ trợ, để hiểu biết đến đúng điểm quyết định. Với báo cáo vận hành có yêu cầu độ trễ hay định dạng chặt (hóa đơn, bản sao kê, hồ sơ quy định), hãy dùng báo cáo chuyên dụng. Đừng kéo giãn bảng điều khiển tương tác để làm một việc nó vừa vặn kém.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Đội BI tập trung | Nhất quán, được quản trị, kiểm soát chất lượng | Nút thắt, phản hồi chậm | Báo cáo chịu quy định |
| BI tự phục vụ | Nhanh, mở rộng được, trao quyền cho người dùng | Lan tràn, chỉ số không nhất quán | Khám phá rộng |
| Lớp ngữ nghĩa | Một sự thật, tái sử dụng được, được quản trị | Mô hình hóa và bảo trì ban đầu | Mọi tổ chức vượt quy mô nhỏ |
| Phân tích nhúng | Hiểu biết tại điểm quyết định | Chi phí kỹ thuật, khó quản trị hơn | Quy trình vận hành |
| Bảng điều khiển phong phú | Cái nhìn toàn diện | Quá tải, tỷ lệ hành động thấp | Hiếm khi lý tưởng |
| Bảng điều khiển tập trung | Thúc đẩy quyết định | Đòi kỷ luật biên tập | Hầu hết trường hợp sử dụng |

Căng thẳng cốt lõi là truy cập so với nhất quán. Khóa BI bên trong một đội trung tâm bảo đảm con số nhất quán, nhưng nó bỏ đói tổ chức khỏi câu trả lời kịp thời và nuôi bảng tính bóng. Tự phục vụ hoàn toàn trao quyền cho mọi người, nhưng nó nhân lên chỉ số xung đột và nội dung cũ. Bạn không phải chọn phe. Hãy kết hợp truy cập tự phục vụ rộng với một lớp ngữ nghĩa được quản trị và chứng nhận, để mọi người tự do khám phá trong khi các con số quan trọng vẫn duy nhất và đáng tin.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn đã đầu tư vào lớp ngữ nghĩa chưa, và bạn có quản trị mỗi chỉ số được chứng nhận như một API với chủ sở hữu, định nghĩa và nhật ký thay đổi không?** Ý tưởng trung tâm của chương là một định nghĩa được quản trị cho mỗi chỉ số mà mọi công cụ, sổ tay và báo cáo nhúng tính từ đó, giết chết vấn đề kinh điển ba bảng điều khiển cho ba con số doanh thu. Với các doanh nghiệp có bộ slide hội đồng quản trị và hồ sơ quy định phụ thuộc vào một con số duy nhất, và các cơ quan có bản công bố công khai phải khớp với con số nội bộ, một chỉ số phân kỳ là khoản nợ trực tiếp. Đánh đổi là thật: lớp ngữ nghĩa cần mô hình hóa ban đầu và bảo trì liên tục. Hãy mang bằng chứng: đếm hôm nay có bao nhiêu định nghĩa của chỉ số quan trọng nhất của bạn và một lần đối chiếu hiện tốn bao nhiêu giờ nhà phân tích. Nếu số đếm lớn hơn một, lớp ngữ nghĩa tự trả giá, và quản trị chỉ số với chủ sở hữu cùng nhật ký thay đổi giữ nó duy nhất theo thời gian.

2. **Ranh giới giữa tự do tự phục vụ và lan tràn chỉ số ở đâu, và lan can nào giữ con đường dễ là con đường được quản trị?** Chương lập luận rằng bạn không nên chọn giữa BI trung tâm khóa chặt và tự phục vụ không kiềm chế: đội trung tâm thành nút thắt đẩy mọi người về bảng tính, trong khi tự phục vụ hoàn toàn nhân lên chỉ số xung đột và bảng điều khiển cũ. Cách giải quyết là truy cập rộng trên các tập dữ liệu được chứng nhận, lớp ngữ nghĩa, mẫu, và các bậc nội dung rõ ràng (được chứng nhận, được đội hỗ trợ, cá nhân) để khám phá không giả làm sự thật chính thức. Hãy mang tín hiệu cụ thể: có bao nhiêu bảng điều khiển, bao nhiêu cái thực sự được dùng, và người tiêu dùng có phân biệt được nội dung đáng tin với thử nghiệm không. Nếu mọi người không phân biệt được, chứng nhận và quản lý vòng đời (theo dõi mức sử dụng, lưu trữ cái không dùng, chứng nhận lại phần còn lại) nên trở thành thực hành thường trực, vì một tập đáng tin nhỏ hơn thắng một nghĩa địa lan tràn.

3. **Biểu đồ của bạn có đủ trung thực để sống sót qua soi xét không, và ai kiểm tra rằng thiết kế ủng hộ kết luận mà dữ liệu thực sự bảo đảm?** Chương đặt một phép thử rõ ràng: một người xem có hiểu biết có đi đến cùng kết luận dữ liệu ủng hộ, hay thiết kế đã đẩy họ đi nơi khác? Trục bị cắt cụt, trục kép tạo tương quan giả, và biểu đồ tròn 3D là các cạm bẫy được nêu tên. Với các bản công bố của chính phủ cho công dân và hồ sơ chịu quy định, một biểu đồ gây hiểu lầm vô tình làm xói mòn lòng tin công chúng hoặc mời một kết luận bất lợi, nên sự trung thực ở đây là mối quan tâm quản trị, không chỉ gu. Hãy mang một ví dụ nơi một biểu đồ trong tổ chức của bạn đã làm khán giả hiểu lầm, và quyết định liệu bạn cần các tiêu chuẩn trực quan hóa (trục cột từ số không, thang nhất quán, độ bất định được thể hiện) được thực thi trên nội dung công bố. Câu trả lời nên đặt kỳ vọng rà soát cho bất cứ thứ gì rời khỏi tòa nhà.

4. **Bảng điều khiển nào của bạn thực sự thay đổi một quyết định, và tiêu chí của bạn để cho nghỉ hưu một cái không làm vậy là gì?** Chương nhấn mạnh một bảng điều khiển nên bắt đầu từ quyết định nó hỗ trợ, vậy mà hầu hết tổ chức lớn tích lũy các bảng điều khiển phù phiếm được theo dõi và không bao giờ được hành động theo, bị nhầm với văn hóa dựa trên dữ liệu. Điều này quan trọng ở quy mô vì mỗi bảng điều khiển mang chi phí ẩn: nó phải được bảo trì, chỉ số của nó giữ nhất quán với lớp ngữ nghĩa, và sự hiện diện của nó làm loãng sự chú ý khỏi các báo cáo thực sự thúc đẩy hành động. Lực kéo đối lập là mọi người cảm thấy an toàn hơn với nhiều khả năng nhìn thấy hơn, và không đội nào thích bảng điều khiển của mình bị lưu trữ. Hãy mang dữ liệu đo từ xa về mức sử dụng (ai mở từng bảng điều khiển, bao lâu một lần, và có hành động hạ nguồn nào theo sau không) và một danh sách thẳng thắn các quyết định mà bảng điều khiển hàng đầu của bạn được cho là cung cấp thông tin. Với doanh nghiệp, điều này nuôi việc chọn lọc danh mục và kiểm soát chi phí giấy phép; với cơ quan chính phủ, nó cũng trả lời câu hỏi giám sát về việc chi tiêu báo cáo có tạo ra giá trị vận hành đo được hay chỉ là các màn hình không ai đọc.

5. **Bạn có đầu tư quá mức vào mô tả quá khứ trong khi giá trị nằm ở chẩn đoán, dự đoán và đề xuất không, và cái gì sẽ đẩy một chỉ số then chốt lên bậc thang đó?** Chương đóng khung bốn loại phân tích (mô tả, chẩn đoán, dự đoán, đề xuất) và cảnh báo rằng hầu hết tổ chức chất đống bảng điều khiển mô tả trong khi đầu tư thiếu vào chẩn đoán và hành động thực sự thay đổi kết quả. Với một đội lớn, mắc kẹt ở mô tả nghĩa là nhà phân tích dành thời gian báo cáo lại điều mọi người đã biết, trong khi câu hỏi khó hơn về vì sao nó xảy ra và làm gì tiếp không được trả lời. Căng thẳng là công việc chẩn đoán và dự đoán cần kỹ thuật dữ liệu sâu hơn, quản trị mô hình và kỹ năng phân tích, nên dễ tài trợ thêm một bảng điều khiển hơn. Hãy mang tỷ lệ hiện tại của công sức phân tích qua bốn loại và một chỉ số nơi đào sâu vào nguyên nhân hay dự báo sẽ thay đổi rõ ràng một quyết định. Trong một doanh nghiệp, điều này nối phân tích với biên lợi nhuận và rủi ro; trong một cơ quan công, công việc dự đoán và đề xuất (ví dụ dự báo nhu cầu cho một dịch vụ) cũng phải mang biện pháp bảo vệ về khả năng giải thích và công bằng trước khi nó cung cấp thông tin cho quyết định về công dân.

6. **Hiểu biết cần đến bên trong những công cụ mọi người đã làm việc ở đâu, và ở đâu bạn nên dùng báo cáo vận hành phù hợp mục đích thay vì bảng điều khiển?** Chương phân biệt BI tương tác với phân tích nhúng và với báo cáo vận hành chuyên dụng như hóa đơn, bản sao kê và hồ sơ quy định, và cảnh báo không kéo giãn bảng điều khiển làm việc nó vừa vặn kém. Điều này quan trọng với đội lớn vì nhân viên tuyến đầu hiếm khi rời CRM hay hệ thống quản lý hồ sơ để tham khảo một cổng BI riêng, nên hiểu biết chỉ sống trong cổng không được dùng vào lúc quyết định. Các cân nhắc đối lập là chi phí kỹ thuật và quản trị: nhúng chỉ số vào ứng dụng vận hành khó xây hơn và khó giữ nhất quán với định nghĩa được chứng nhận, trong khi báo cáo chính xác đến từng điểm ảnh cần độ trễ và định dạng chặt mà công cụ bảng điều khiển không bảo đảm được. Hãy mang bản đồ nơi quyết định thực sự được đưa ra và cái nào hiện đòi ai đó đổi công cụ để tìm con số. Với một doanh nghiệp, điều này định hình nơi đầu tư công sức kỹ thuật; với một cơ quan chính phủ, hồ sơ theo luật và bản sao kê hướng công dân thường có quy tắc định dạng và lưu giữ pháp lý khiến báo cáo chuyên dụng là bắt buộc chứ không tùy chọn.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy xác định vài chỉ số cốt lõi của bạn một lần, ngay cả trong công cụ nhẹ, để bộ slide hội đồng và bảng điều khiển sản phẩm không bao giờ bất đồng. Bỏ qua nền tảng lớp ngữ nghĩa nặng: một nguồn định nghĩa dùng chung duy nhất và một danh sách ngắn các bảng điều khiển đáng tin là đủ khi đội còn nhỏ xíu. Tốc độ quan trọng hơn độ bóng bẩy ở đây, vì vậy hãy ưu tiên công cụ BI lưu trữ bạn trỏ vào kho ngay hôm nay hơn bất cứ thứ gì bạn phải xây.

**Doanh nghiệp nhỏ.** Không có chuyên gia BI riêng, hãy dựa vào phân tích đã nhúng sẵn trong công cụ bạn sở hữu, như CRM hay phần mềm kế toán, thay vì dựng một nền tảng riêng. Hãy đóng khung lựa chọn như mua-so-với-xây và để mua thắng theo mặc định; rủi ro của bạn là văn hóa bảng tính nơi mỗi người mang một con số "doanh thu" khác nhau, nên hãy thống nhất vài định nghĩa quan trọng và viết chúng ra. Ưu tiên công cụ làm báo cáo được chứng nhận dễ chia sẻ và khó vô tình phân nhánh.

**Doanh nghiệp lớn.** Vấn đề cốt lõi là nhất quán qua nhiều đội: hãy đầu tư vào một lớp ngữ nghĩa được quản trị, chứng nhận nội dung đáng tin, và quản lý sự lan tràn bảng điều khiển như một vòng đời liên tục với chủ sở hữu, theo dõi mức sử dụng và chứng nhận lại. Hãy coi mỗi chỉ số được chứng nhận như một API với định nghĩa, chủ sở hữu và nhật ký thay đổi, và tách nội dung được chứng nhận khỏi thử nghiệm để tự phục vụ không giả làm sự thật chính thức. Lập ngân sách tường minh cho công sức mô hình hóa và chọn lọc, vì ở quy mô lớn lựa chọn thay thế là nhà phân tích đối chiếu các con số phân kỳ vô thời hạn.

**Chính phủ.** Con số công bố phải khớp với con số nội bộ và sống sót qua soi xét của công chúng và cơ quan lập pháp, nên một lớp ngữ nghĩa được quản trị và các tiêu chuẩn trực quan hóa được thực thi (trục từ số không, thang trung thực, độ bất định được thể hiện) là yêu cầu trách nhiệm giải trình, không phải điều dễ chịu. Quy tắc mua sắm có thể ràng buộc công cụ BI bạn mua được và đòi khả năng di chuyển dữ liệu, vì vậy hãy tránh khóa chặt vào logic chỉ số độc quyền của một nhà cung cấp. Giữ các bản công bố công khai được chứng nhận tách khỏi phân tích thử nghiệm, và cho công dân những biểu đồ đủ trung thực để một người xem có hiểu biết đi đến kết luận mà dữ liệu thực sự bảo đảm.

## Ví dụ

**Công ty khởi nghiệp.** Tại một chợ giai đoạn đầu, hai người sáng lập mỗi người giữ một bảng tính "doanh thu hằng tháng," và các con số không bao giờ khớp khi họ chuẩn bị bộ slide hội đồng. Họ định nghĩa chỉ số một lần trong một lớp ngữ nghĩa nhỏ, trỏ một công cụ BI duy nhất vào đó, và đánh dấu một danh sách ngắn các bảng điều khiển là cái đáng tin mà mọi người nên dùng. Báo cáo chuyển từ một cuộc đối chiếu đêm Chủ nhật thành một đường liên kết họ mở được tự tin.

**Doanh nghiệp lớn.** Một công ty viễn thông chịu cảnh tài chính, tiếp thị và vận hành mỗi bên báo cáo số "thuê bao hoạt động" khác nhau. Họ giới thiệu một lớp ngữ nghĩa xác định mỗi chỉ số cốt lõi một lần, chuyển các bảng điều khiển sang tính từ nó, và chứng nhận một tập báo cáo đáng tin đã chọn lọc trong khi lưu trữ hàng nghìn cái cũ. Báo cáo hội đồng thôi là bài tập đối chiếu, và việc áp dụng tự phục vụ tăng vì mọi người tin các con số.

**Chính phủ.** Một sở y tế công xây các bảng điều khiển được chứng nhận lấy từ một lớp ngữ nghĩa được quản trị, để số ca và tỷ lệ được tính giống hệt nhau qua ra quyết định nội bộ và bản công bố công khai. Các tiêu chuẩn trực quan hóa giữ biểu đồ công bố cho công dân trung thực (trục từ số không, dải bất định rõ ràng), bảo vệ lòng tin công chúng. Các báo cáo nhúng hiển thị chỉ số địa phương bên trong các công cụ quản lý hồ sơ mà nhân viên tuyến đầu đã dùng.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của phân tích và BI được vận hành tốt đến từ quyết định nhanh hơn, tốt hơn và cắt giảm lãng phí. Khi mọi người tin một bộ số duy nhất, các cuộc họp thôi là tranh cãi về bảng tính của ai đúng và trở thành thảo luận về nên làm gì. Tự phục vụ giảm tồn đọng của các đội trung tâm, và một lớp ngữ nghĩa ngăn chi phí lặp lại của việc đối chiếu các chỉ số phân kỳ. Bảng điều khiển trung thực, tập trung vào quyết định nâng tỷ lệ hiểu biết biến thành hành động.

Chi phí áp dụng gồm giấy phép nền tảng BI, xây dựng và bảo trì lớp ngữ nghĩa, công sức chọn lọc và đào tạo. Hãy cân nhắc nó so với chi phí của việc không áp dụng: nhà phân tích và giám đốc lãng phí hàng giờ đối chiếu các con số xung đột, quyết định đưa ra dựa trên biểu đồ gây hiểu lầm, một đống bảng điều khiển không bảo trì, và, trong bối cảnh công, lòng tin bị xói mòn khi các con số công bố mâu thuẫn nhau. Với ban lãnh đạo, lập luận đơn giản. Một lớp ngữ nghĩa được quản trị cộng tự phục vụ có chọn lọc là sự khác biệt giữa dữ liệu là tài sản mọi người tin và nguồn gây nhầm lẫn cùng làm lại thường trực.

## Phản mẫu và cạm bẫy

- Mỗi đội tính chỉ số chính theo cách riêng, tạo ra các con số xung đột.
- Bảng điều khiển xây để hiển thị mọi thứ thay vì hỗ trợ một quyết định.
- Biểu đồ gây hiểu lầm (trục cắt cụt, trục kép, biểu đồ tròn 3D) bóp méo kết luận.
- Coi tự phục vụ là sự thay thế cho quản trị thay vì bổ sung cho nó.
- Hàng nghìn bảng điều khiển cũ, trùng lặp không có quản lý vòng đời.
- Bảng điều khiển phù phiếm không ai hành động, bị nhầm với văn hóa dựa trên dữ liệu.
- Kéo giãn BI tương tác để tạo tài liệu quy định chính xác từng điểm ảnh.
- Không chứng nhận, nên người tiêu dùng không phân biệt được nội dung đáng tin với thử nghiệm.

## Mô hình trưởng thành

1. **Khởi đầu.** Báo cáo được xây tùy nghi trong bảng tính, chỉ số được định nghĩa không nhất quán, và biểu đồ thường gây hiểu lầm. Không có lớp ngữ nghĩa, chứng nhận hay chọn lọc, nên các con số phân kỳ là chuẩn mực.
2. **Phát triển.** Một công cụ BI đã có với vài bảng điều khiển dùng chung, nhưng định nghĩa chỉ số vẫn phân kỳ giữa các đội. Tự phục vụ không được kiểm soát và lan tràn bắt đầu; vài nhóm có thể mô hình hóa chỉ số cẩn thận, nhưng thực hành không nhất quán và không gì được thực thi toàn tổ chức.
3. **Chuẩn hóa.** Một lớp ngữ nghĩa xác định các chỉ số cốt lõi một lần, được lập tài liệu và thực thi qua mọi công cụ và báo cáo. Nội dung được chứng nhận được phân biệt với thử nghiệm, tự phục vụ vận hành trong lan can, tiêu chuẩn trực quan hóa được công bố, và quản lý vòng đời nội dung là thực hành thường trực thay vì dọn dẹp thỉnh thoảng.
4. **Quản lý.** Hệ sinh thái phân tích được đo theo đường cơ sở. Mức sử dụng bảng điều khiển được theo dõi và nội dung không dùng được định lượng và cho nghỉ hưu theo nhịp; số định nghĩa phân kỳ của các chỉ số chính được giám sát hướng về một; tuân thủ rà soát biểu đồ, việc áp dụng tự phục vụ và thời gian-đến-câu-trả-lời được theo dõi; và chi phí đối chiếu cùng thời gian chờ thay đổi chỉ số được đo để độ lệch khỏi định nghĩa được chứng nhận được bắt và sửa dựa trên bằng chứng.
5. **Điều phối.** Chỉ số được quản trị như API với chủ sở hữu và nhật ký thay đổi, phân tích trải từ mô tả đến đề xuất và nối với hành động cụ thể, và báo cáo được nhúng tại các điểm quyết định. Tổ chức tin một phiên bản duy nhất của sự thật ở mọi nơi, tích cực kiềm chế lan tràn, và liên tục thu hẹp phạm vi và chứng nhận lại phân tích khi doanh nghiệp và câu hỏi của nó thay đổi.

## Ý tưởng để thảo luận

- Hôm nay có bao nhiêu định nghĩa khác nhau của chỉ số quan trọng nhất của bạn?
- Bảng điều khiển nào của bạn thực sự thay đổi quyết định, và cái nào chỉ được theo dõi?
- Một biểu đồ trong tổ chức của bạn đã làm khán giả hiểu lầm ở đâu, vô tình hay không?
- Bạn có đầu tư quá mức vào mô tả quá khứ so với chẩn đoán và hành động không?
- Một bậc chứng nhận cho nội dung sẽ làm gì với lòng tin và tái sử dụng trong tổ chức của bạn?
- Làm sao bạn cân bằng nhu cầu của công dân hay cơ quan quản lý về biểu đồ trung thực với lực kéo về biểu đồ thuyết phục?

## Những điểm cần ghi nhớ

- Hãy xác định mỗi chỉ số quan trọng một lần trong một lớp ngữ nghĩa được quản trị dùng ở mọi nơi.
- Đẩy phân tích lên bậc thang từ mô tả sang chẩn đoán, dự đoán và đề xuất.
- Cho phép tự phục vụ trong lan can; chứng nhận nội dung đáng tin.
- Thiết kế bảng điều khiển quanh quyết định, không quanh dữ liệu có sẵn.
- Làm mọi biểu đồ trung thực; mục tiêu là hiểu biết, không phải thuyết phục.
- Chọn lọc không thương tiếc và cho nghỉ hưu nội dung cũ để chống lan tràn.
- Nhúng phân tích tại điểm quyết định, và dùng báo cáo vận hành phù hợp mục đích.

## Tài liệu tham khảo và đọc thêm

- Edward Tufte, "The Visual Display of Quantitative Information."
- Stephen Few, "Show Me the Numbers" và "Information Dashboard Design."
- Cole Nussbaumer Knaflic, "Storytelling with Data."
- Alberto Cairo, "How Charts Lie."
- Ralph Kimball và Margy Ross, "The Data Warehouse Toolkit."
- Darrell Huff, "How to Lie with Statistics."
- Benn Stancil và những người khác, các bài viết về lớp ngữ nghĩa và kho chỉ số.
