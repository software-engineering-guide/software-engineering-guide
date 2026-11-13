# 2.4 Chiến lược kiểm thử

## Tổng quan và động lực

Một chiến lược [kiểm thử](https://en.wikipedia.org/wiki/Software_testing) là tập hợp các lựa chọn có chủ đích về cái gì cần kiểm thử, ở mức nào, tự động đến đâu và với độ tin cậy ra sao, để đội của bạn có thể thay đổi mã nhanh chóng mà không làm hỏng nó. Kiểm thử là thứ cho phép một tổ chức lớn triển khai thường xuyên và an toàn. Chúng mã hóa hành vi mong đợi, bắt các hồi quy và cho kỹ sư sự tự tin để [tái cấu trúc](https://en.wikipedia.org/wiki/Code_refactoring). Không có một chiến lược mạch lạc, kiểm thử có xu hướng đi theo một trong hai hướng xấu: vắng mặt (phát triển chậm chạp, dựa trên nỗi sợ) hoặc phình to (hàng nghìn bài kiểm thử chậm, chập chờn mà không ai tin).

Với một đội lớn, chiến lược quan trọng hơn bất kỳ bài kiểm thử đơn lẻ nào. Hàng trăm kỹ sư làm việc trong một cơ sở mã chung cần một lưới an toàn nhanh, đáng tin cậy. Không có nó, mọi thay đổi đều rủi ro và mỗi bản phát hành biến thành một thử thách thủ công. Các bài kiểm thử cũng hoạt động như tài liệu có thể thực thi về hành vi dự kiến, vô giá khi các tác giả ban đầu đã đi nơi khác. Chiến lược quyết định bộ kiểm thử của bạn là tài sản đẩy nhanh phân phối hay là gánh nặng kéo nó xuống.

Trong bối cảnh doanh nghiệp và chính phủ, kiểm thử mang thêm trọng lượng. Quy định có thể yêu cầu độ bao phủ kiểm thử và bằng chứng có tài liệu. Các hệ thống quan trọng về an toàn và hướng đến công dân đòi hỏi mức đảm bảo cao. Kiểm thử khả năng tiếp cận và bảo mật có thể được yêu cầu về mặt pháp lý. Vì vậy chiến lược phải cân bằng tốc độ, độ tin cậy, chi phí và tuân thủ, và phải coi độ bao phủ là một tín hiệu, không phải mục tiêu để bị lách.

## Các nguyên tắc chính

- Kiểm thử để có sự tự tin thay đổi, không phải để đạt một con số.
- Ưu tiên các bài kiểm thử nhanh, đáng tin cậy, cô lập. Kiểm thử chậm hoặc chập chờn làm xói mòn niềm tin khiến một bộ kiểm thử trở nên hữu ích.
- Đẩy các bài kiểm thử xuống mức thấp nhất mang lại sự tự tin thực sự, và dành các bài kiểm thử chậm, rộng cho rủi ro tích hợp thực sự.
- Một bài kiểm thử chập chờn là một bài kiểm thử hỏng. Hãy coi sự chập chờn là lỗi hạng nhất.
- Độ bao phủ là một tín hiệu, không phải mục tiêu. Độ bao phủ cao của mã tầm thường chứng minh rất ít.
- Kiểm thử hành vi và hợp đồng, không phải chi tiết triển khai, để các bài kiểm thử của bạn sống sót qua tái cấu trúc.
- Biến kiểm thử phi chức năng (khả năng tiếp cận, hiệu năng, bảo mật) thành một phần của chiến lược, không phải chuyện nghĩ đến sau.

## Khuyến nghị

### Dùng kim tự tháp kiểm thử làm mặc định, và biết những lời phê bình nó

Hãy mặc định có nhiều [kiểm thử đơn vị](https://en.wikipedia.org/wiki/Unit_testing) nhanh, ít [kiểm thử tích hợp](https://en.wikipedia.org/wiki/Integration_testing) hơn, và một số lượng nhỏ các bài kiểm thử đầu-cuối, vì chi phí và độ mong manh tăng khi phạm vi lớn lên. Cũng hãy biết những lời phê bình: hình dạng nên theo kiến trúc của bạn, không phải giáo điều. Một hệ thống nhiều dịch vụ có thể cần một tầng tích hợp lớn hơn ("chiếc cúp kiểm thử"), và mục tiêu thực sự là độ tin cậy trên mỗi đơn vị chi phí và tốc độ, không phải một hình bóng cụ thể. Dù làm gì, hãy tránh kim tự tháp ngược gồm chủ yếu các bài kiểm thử đầu-cuối chậm.

### Áp dụng TDD, BDD và phát triển dựa trên đặc tả ở nơi chúng có ích

Dùng [phát triển hướng kiểm thử](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) để dẫn dắt thiết kế và đảm bảo khả năng kiểm thử, đặc biệt cho logic phức tạp. Nó là một kỷ luật thiết kế cũng như kiểm thử. Dùng [phát triển hướng hành vi](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) để diễn đạt các bài kiểm thử bằng ngôn ngữ miền mà bạn chia sẻ với các bên liên quan, có giá trị cho tiêu chí chấp nhận trong các môi trường chịu quy định hoặc nặng về yêu cầu. Phát triển dựa trên đặc tả đi xa hơn một bước: nó coi một đặc tả có thể thực thi (hành vi đã thống nhất, được diễn đạt bằng ví dụ) là nguồn sự thật duy nhất vừa dẫn dắt việc triển khai vừa xác minh nó. Điều này tỏa sáng ở nơi yêu cầu phải truy vết được đến bằng chứng chấp nhận, như trong các chương trình của chính phủ và chịu quy định. Liên quan đến cả ba là **[kiểm thử dịch chuyển sang trái](https://en.wikipedia.org/wiki/Shift-left_testing)**: đưa việc xác minh càng sớm càng tốt trong vòng đời, viết các bài kiểm thử cùng lúc hoặc trước mã và chạy chúng liên tục, để bạn bắt lỗi khi chi phí sửa rẻ nhất, thay vì trong các giai đoạn kiểm thử muộn hay trên môi trường thực. Không cái nào là bắt buộc ở mọi nơi. Hãy áp dụng chúng nơi chúng thêm sự rõ ràng.

### Dùng các kỹ thuật nâng cao cho mã có giá trị cao

Dùng kiểm thử dựa trên thuộc tính để kiểm tra các bất biến trên nhiều đầu vào được sinh ra, bắt các trường hợp biên mà kiểm thử dựa trên ví dụ bỏ sót. Dùng [kiểm thử mờ](https://en.wikipedia.org/wiki/Fuzzing) trên các bộ phân tích cú pháp và ranh giới đầu vào không đáng tin cậy để tìm lỗi sập và lỗ hổng bảo mật. Dùng [kiểm thử đột biến](https://en.wikipedia.org/wiki/Mutation_testing) để đo xem các bài kiểm thử của bạn có thực sự phát hiện được lỗi được tiêm vào hay không, một tín hiệu chất lượng tốt hơn nhiều so với độ bao phủ thô. Dùng kiểm thử ảnh chụp nhanh một cách thận trọng cho đầu ra tuần tự hóa, và coi chừng cái bẫy phê duyệt lại ảnh chụp một cách mù quáng.

### Quản lý dữ liệu kiểm thử và dùng dữ liệu tổng hợp

Làm cho các bài kiểm thử xác định bằng dữ liệu kiểm thử được kiểm soát, cô lập, và tránh các fixture khả biến dùng chung liên kết các bài kiểm thử với nhau. Sinh [dữ liệu tổng hợp](https://en.wikipedia.org/wiki/Synthetic_data) phản ánh các đặc tính của môi trường thực mà không phơi bày thông tin cá nhân thực, điều thiết yếu ở nơi quy tắc riêng tư cấm dùng dữ liệu môi trường thực trong các môi trường kiểm thử. Cung cấp nhà máy hoặc trình xây dựng để mỗi bài kiểm thử có thể dựng chính xác dữ liệu nó cần.

### Coi kiểm thử chập chờn là lỗi

Phát hiện sự chập chờn một cách tự động, chuyển các bài kiểm thử chập chờn ra khỏi đường chặn, và sửa hoặc xóa chúng theo hạn chót. Một bộ kiểm thử thất bại ngẫu nhiên huấn luyện kỹ sư phớt lờ các thất bại, phá hủy toàn bộ giá trị của nó. Hãy theo dõi tỷ lệ chập chờn và biến độ tin cậy thành một chỉ số chất lượng tường minh cho chính bộ kiểm thử.

### Dùng độ bao phủ như tín hiệu, và thêm kiểm thử phi chức năng

Đo độ bao phủ để tìm các khu vực chưa được kiểm thử, nhưng đừng biến nó thành mục tiêu cứng mời gọi việc lách bằng các bài kiểm thử không có khẳng định. Bổ sung nó bằng kiểm thử đột biến để có chiều sâu. Xây dựng kiểm thử khả năng tiếp cận (kiểm tra tự động cộng kiểm toán thủ công), kiểm thử hiệu năng (đường cơ sở tải và độ trễ cùng phát hiện hồi quy) và kiểm thử bảo mật (quét phụ thuộc, [phân tích tĩnh](https://en.wikipedia.org/wiki/Static_program_analysis) và kiểm thử động) vào đường ống.

## Đánh đổi: ưu và nhược điểm

| Loại kiểm thử / thực hành | Ưu điểm | Nhược điểm |
|---|---|---|
| Kiểm thử đơn vị | Nhanh, chính xác, rẻ, ổn định | Bỏ sót lỗi tích hợp và cấp hệ thống |
| Kiểm thử tích hợp | Bắt lỗi giao diện và nối dây | Chậm hơn; thiết lập nhiều hơn; mong manh hơn |
| Kiểm thử đầu-cuối | Độ tin cậy cao nhất về hành vi thực | Chậm, chập chờn, tốn kém để bảo trì |
| TDD | Thiết kế tốt hơn, đảm bảo khả năng kiểm thử | Đường cong học tập; ban đầu có cảm giác chậm |
| Kiểm thử dựa trên thuộc tính | Tìm trường hợp biên, mã hóa bất biến | Đòi hỏi tư duy theo thuộc tính; khó viết hơn |
| Kiểm thử đột biến | Thước đo thực sự về hiệu quả kiểm thử | Tốn tính toán; chạy chậm |
| Mục tiêu độ bao phủ cao | Làm lộ mã chưa được kiểm thử | Có thể bị lách; có thể khuyến khích kiểm thử giá trị thấp |

Sự đánh đổi trung tâm là độ tin cậy so với tốc độ và chi phí. Các bài kiểm thử rộng hơn cho nhiều độ tin cậy hơn nhưng chạy chậm hơn và hỏng thường xuyên hơn. Các bài kiểm thử hẹp hơn nhanh và ổn định nhưng bỏ sót lỗi cấp hệ thống. Sự pha trộn đúng tối đa hóa độ tin cậy trên mỗi giây phản hồi và mỗi giờ bảo trì. Và kiểm thử quá mức là một chế độ thất bại thực sự: một bộ kiểm thử phình to gồm các bài kiểm thử dư thừa, chậm, mong manh có thể tốn kém hơn các lỗi mà nó ngăn chặn.

## Câu hỏi để thảo luận với đội của bạn

1. **Những kiểm thử phi chức năng nào, khả năng tiếp cận, hiệu năng và bảo mật, nên chặn một bản phát hành, và những kiểm thử nào chỉ nên báo cáo?** Chương này lập luận rằng kiểm thử phi chức năng thuộc về chiến lược chứ không phải chuyện nghĩ đến sau, và lưu ý rằng khả năng tiếp cận có thể được yêu cầu về mặt pháp lý và kiểm thử bảo mật có thể là một phần của bằng chứng cấp phép vận hành. Với một hệ thống lớn hoặc hướng đến công dân, một cổng chặn làm chậm phân phối, nhưng một lỗi khả năng tiếp cận hay bảo mật bị phát hiện trên môi trường thực mang chi phí khắc phục, danh tiếng và pháp lý vượt xa chi phí của bài kiểm thử. Hãy mang những tín hiệu quyết định điều đó: mức độ tiếp xúc quy định của bạn, hệ thống có hướng đến công dân không, và những lỗi này hiện thoát ra môi trường thực thường xuyên đến mức nào. Hãy biến các kiểm tra được yêu cầu về mặt pháp lý thành chặn và để các kiểm tra rủi ro thấp hơn báo cáo cùng xu hướng, để cổng phản ánh rủi ro thực thay vì giáo điều. Câu trả lời trực tiếp đặt ra điều gì có thể và không thể được hợp nhất.

2. **Bạn có đặt một tỷ lệ phần trăm độ bao phủ cứng làm cổng không, và nếu có, điều gì ngăn kỹ sư lách nó bằng các bài kiểm thử không có khẳng định?** Chương này kiên quyết rằng độ bao phủ là một tín hiệu, không phải mục tiêu, rằng độ bao phủ cao của mã tầm thường chứng minh rất ít, và rằng một mục tiêu cứng mời gọi việc lách. Một con số duy nhất áp đặt qua một tổ chức lớn luôn tạo ra các bài kiểm thử thực thi mã mà không khẳng định gì, làm tăng chỉ số và hạ thấp độ tin cậy thực. Hãy mang một tín hiệu tốt hơn vào cuộc thảo luận: điểm kiểm thử đột biến trên các mô-đun có giá trị cao nhất của bạn, đo xem các bài kiểm thử có thực sự phát hiện được lỗi được tiêm vào không. Dùng độ bao phủ để tìm các khu vực chưa được kiểm thử và kiểm thử đột biến để có chiều sâu, và cưỡng lại việc biến một trong hai thành mục tiêu mà ban lãnh đạo theo dõi riêng lẻ. Hãy quyết định nơi con số thực sự có ích và nơi nó chỉ mời gọi sân khấu.

3. **Chính sách của bạn là gì khi bộ kiểm thử phát triển quá chậm để kỹ sư chờ đợi nó?** Sự đánh đổi trung tâm của chương này là độ tin cậy so với tốc độ và chi phí, và nó gọi tên kiểm thử quá mức là một chế độ thất bại thực sự khi một bộ kiểm thử phình to, dư thừa, chậm tốn kém hơn các lỗi mà nó ngăn chặn. Trong một đội lớn, thời gian chạy bộ kiểm thử là cái thuế chung được trả cho mọi thay đổi, và một bộ kiểm thử mà mọi người học cách bỏ qua mất toàn bộ giá trị của nó. Hãy mang bằng chứng: thời gian đồng hồ của CI, các bài kiểm thử chậm nhất, và bao nhiêu độ bao phủ đầu-cuối dư thừa trùng lặp các kiểm thử đơn vị rẻ hơn. Đẩy các bài kiểm thử xuống mức thấp nhất mang lại sự tự tin thực sự, song song hóa, và xóa các bài kiểm thử chậm dư thừa theo hạn chót. Tối ưu hóa độ tin cậy trên mỗi giây phản hồi, không phải số lượng kiểm thử thô, là mục tiêu.

4. **Khi một bài kiểm thử trở nên chập chờn, ai sở hữu nó, nó phải được sửa hoặc xóa nhanh đến mức nào, và điều gì thực thi hạn chót đó?** Chương này coi một bài kiểm thử chập chờn là một bài kiểm thử hỏng, một lỗi hạng nhất, vì một bộ kiểm thử thất bại ngẫu nhiên huấn luyện một đội lớn phớt lờ các bản dựng đỏ và âm thầm phá hủy lưới an toàn mà mọi người phụ thuộc vào. Áp lực đối lập là có thật: cách ly một bài kiểm thử chập chờn gỡ nút thắt cho phân phối hôm nay nhưng có rủi ro che giấu một lỗi gián đoạn thực sự, trong khi chặn vì nó làm đình trệ hàng trăm kỹ sư vì một thất bại có thể thuần túy là nhiễu. Hãy mang bằng chứng giải quyết điều đó: tỷ lệ chập chờn hiện tại của bạn, các bài kiểm thử nằm trong cách ly bao lâu trước khi có ai chạm đến, và bao nhiêu bài kiểm thử bị cách ly hóa ra che giấu một lỗi thực. Giao một chủ sở hữu cho mỗi bài kiểm thử bị cách ly, đặt hạn chót cứng để sửa hoặc xóa, và theo dõi độ tin cậy như một chỉ số tường minh cho bộ kiểm thử. Trong bối cảnh doanh nghiệp và chính phủ nơi một bản dựng xanh là một phần của bằng chứng phát hành, một đống cách ly không được quản lý cũng là một rủi ro kiểm toán, vì bạn đang phát hành dựa trên một tín hiệu mà bạn đã âm thầm đồng ý không tin.

5. **Bạn có được phép dùng dữ liệu môi trường thực trong môi trường kiểm thử không, và nếu không, bạn sẽ sinh dữ liệu tổng hợp đủ trung thực để bắt lỗi thực sự như thế nào?** Chương này nói thẳng rằng quy tắc riêng tư thường cấm dữ liệu cá nhân thực trong kiểm thử, và dữ liệu tổng hợp phải phản ánh đặc tính của môi trường thực nếu không các bài kiểm thử của bạn cho sự tự tin sai. Với một tổ chức lớn, căng thẳng nằm giữa độ trung thực và tuân thủ: dữ liệu môi trường thực bắt được các trường hợp biên lộn xộn mà dữ liệu tổng hợp bỏ sót, nhưng mỗi bản sao của nó nhân lên rủi ro và nghĩa vụ của bạn. Hãy mang những chi tiết cụ thể: bộ dữ liệu nào chứa dữ liệu cá nhân hoặc chịu quy định, quy tắc riêng tư và nơi lưu trữ dữ liệu của bạn thực sự yêu cầu gì, và các fixture hiện tại của bạn tái hiện các phân phối và trường hợp biên thấy ở môi trường thực tốt đến đâu. Hãy chuẩn hóa nhà máy hoặc trình xây dựng để mỗi bài kiểm thử dựng chính xác dữ liệu nó cần, và đầu tư vào việc sinh dữ liệu tổng hợp khớp với phân phối nhân khẩu học và khối lượng thực. Trong các chương trình chính phủ và chịu quy định, dùng dữ liệu công dân trong môi trường kiểm thử không phải là đường tắt, đó là một vụ vi phạm phải báo cáo, vì vậy chiến lược dữ liệu phải được giải quyết trước khi môi trường đầu tiên được dựng lên.

6. **TDD, BDD hay phát triển dựa trên đặc tả nên được mong đợi thay vì tùy chọn ở đâu, và ai quyết định?** Chương này trình bày những điều này như các kỷ luật cần áp dụng ở nơi chúng thêm sự rõ ràng, không phải mệnh lệnh cho mọi dòng mã, nhưng một đội lớn hưởng lợi từ một mặc định chung để thực hành không phân mảnh theo từng đội. Sự đánh đổi là giữa lợi ích thiết kế và truy vết (các đặc tả có thể thực thi mà chuyên gia chính sách có thể rà soát, các bài kiểm thử sống sót qua tái cấu trúc) với đường cong học tập thực sự và sự chậm chạp ban đầu khiến một mệnh lệnh đại trà phản tác dụng. Hãy mang bằng chứng để xác định phạm vi: mô-đun nào mang logic phức tạp hoặc tỷ lệ thay đổi thất bại cao, nơi tiêu chí chấp nhận phải truy vết được đến yêu cầu, và các đội đã thực hành những điều này báo cáo thế nào về tốc độ và tỷ lệ lỗi. Hãy dành kỳ vọng cho logic phức tạp và các khu vực nặng về yêu cầu, và để mã đơn giản hơn tự chọn. Trong các chương trình chính phủ và chịu quy định nơi phần mềm phải truy vết được đến luật mà nó triển khai, phát triển dựa trên đặc tả với bằng chứng chấp nhận có thể thực thi ít là sở thích mà nhiều là con đường đến cấp phép vận hành của bạn, vì vậy hãy nêu rõ nơi nó là bắt buộc.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Một đội nhỏ không thể bố trí QA, vì vậy hãy làm cho bộ kiểm thử xứng đáng với chỗ đứng của nó: các kiểm thử đơn vị nhanh trên mỗi commit cộng với một vài bài kiểm thử đầu-cuối trên đường duy nhất trả tiền cho bạn, và không gì bạn sẽ không bảo trì. Bỏ qua mục tiêu độ bao phủ và kiểm thử logic mà bạn sợ làm hỏng nhất, để bạn có thể phát hành nhiều lần mỗi ngày mà không cần một lượt hồi quy thủ công. Hãy sửa một bài kiểm thử chập chờn ngay trong ngày, vì ở giai đoạn này một bộ kiểm thử mà đội học cách phớt lờ còn tệ hơn không có bộ kiểm thử nào.

**Doanh nghiệp nhỏ.** Không có kỹ sư kiểm thử riêng và ngân sách eo hẹp, hãy dựa vào kiểm thử có sẵn trong các khung và công cụ bạn đang chạy thay vì một bộ khung riêng mà bạn không thể hỗ trợ. Ưu tiên một nhúm kiểm tra bảo vệ doanh thu và niềm tin khách hàng, và dùng CI được lưu trữ để bạn không phải tự bảo trì hạ tầng dựng. Hãy ưu tiên mua dịch vụ quét khả năng tiếp cận và bảo mật hơn là tự xây, vì một lỗi bị bỏ sót có thể tốn nhiều hơn một năm dùng công cụ.

**Doanh nghiệp lớn.** Qua nhiều đội, vấn đề chiến lược là nhất quán: một mặc định kim tự tháp chung, cách ly kiểm thử chập chờn tự động, và các cổng phi chức năng có cùng ý nghĩa ở mọi nơi, để một bản dựng xanh đáng tin bất kể ai tạo ra nó. Hãy ngân sách thời gian chạy bộ kiểm thử như một khoản thuế chung và song song hóa mạnh mẽ, vì thời gian đồng hồ CI được trả trong mỗi thay đổi bởi mọi kỹ sư. Hãy quản lý điểm độ bao phủ và đột biến như các tín hiệu danh mục với chủ sở hữu rõ ràng, không phải những con số mà ban lãnh đạo theo dõi riêng lẻ.

**Chính phủ.** Mua sắm và giám sát biến kiểm thử thành bằng chứng, không chỉ là vệ sinh kỹ thuật. Hãy diễn đạt các quy tắc đủ điều kiện và chính sách thành các đặc tả có thể thực thi được chuyên gia miền rà soát, để bạn có thể truy vết phần mềm đến luật mà nó triển khai, và biến kiểm thử khả năng tiếp cận và bảo mật thành chặn vì chúng được yêu cầu về mặt pháp lý và là một phần của bằng chứng cấp phép vận hành. Dùng dữ liệu tổng hợp được sinh ra để khớp với các phân phối thực, vì dữ liệu công dân trong môi trường kiểm thử là một vụ vi phạm phải báo cáo, và giữ các hiện vật kiểm thử có thể kiểm toán để một người rà soát bên ngoài có thể xác nhận chính xác điều gì đã được xác minh.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp năm người không thể thuê đội QA, vì vậy dựa vào một bộ kiểm thử đơn vị nhanh chạy trên mỗi commit cộng với một vài bài kiểm thử đầu-cuối bao quát đường từ đăng ký đến thanh toán trả tiền cho họ. Những người sáng lập bỏ qua độ bao phủ toàn diện và thay vào đó kiểm thử logic mà họ sợ làm hỏng nhất, cho phép họ phát hành nhiều lần mỗi ngày mà không cần lượt hồi quy thủ công. Khi một bài kiểm thử chập chờn bắt đầu thất bại ngẫu nhiên, họ sửa nó ngay trong ngày, vì một bộ kiểm thử mà đội học cách phớt lờ còn tệ hơn không có ở giai đoạn mà niềm tin là tất cả.

**Doanh nghiệp lớn.** Một nền tảng thương mại điện tử lớn duy trì hàng nghìn kiểm thử đơn vị nhanh chạy trên mỗi commit trong vài phút, một bộ kiểm thử tích hợp tập trung quanh các ranh giới thanh toán và kho hàng, và một bộ nhỏ các kiểm thử đầu-cuối cho các hành trình thanh toán quan trọng. Các kiểm thử đầu-cuối chập chờn được tự động cách ly và giao để sửa. Vì kỹ sư tin bộ kiểm thử, họ triển khai nhiều lần mỗi ngày, tự tin rằng một bản dựng đỏ có nghĩa là một vấn đề thực.

**Chính phủ.** Một hệ thống trợ cấp quốc gia hoạt động dưới sự giám sát của quy định dùng BDD để diễn đạt các quy tắc đủ điều kiện thành các đặc tả có thể thực thi do chuyên gia chính sách rà soát, cung cấp bằng chứng truy vết được rằng phần mềm triển khai luật. Nó dùng dữ liệu tổng hợp được sinh ra để khớp với các phân phối nhân khẩu học thực, vì quy tắc riêng tư cấm dữ liệu công dân trong môi trường kiểm thử. Kiểm thử khả năng tiếp cận là bắt buộc và chặn phát hành, vì dịch vụ phải dùng được cho mọi công dân. Và kiểm thử bảo mật là một phần của bằng chứng cấp phép vận hành (ATO), sự phê duyệt chính thức để chạy hệ thống trong môi trường thực.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của kiểm thử là khả năng thay đổi phần mềm nhanh chóng và an toàn, nền tảng của tốc độ phân phối bền vững. Một bộ kiểm thử tự động đáng tin cậy thay thế [kiểm thử hồi quy](https://en.wikipedia.org/wiki/Regression_testing) thủ công chậm, đắt đỏ và bắt lỗi khi chi phí sửa rẻ nhất, trước khi phát hành thay vì trên môi trường thực. Trong một hệ thống chịu quy định hoặc hướng đến công dân, chi phí của một lỗi trên môi trường thực (khắc phục, danh tiếng và rủi ro pháp lý tiềm tàng) vượt xa chi phí của những bài kiểm thử lẽ ra đã bắt được nó.

Chi phí áp dụng là thật: bạn viết và bảo trì các bài kiểm thử, và xây dựng hạ tầng [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Nhưng chi phí của việc không kiểm thử cao hơn và cộng dồn: phát triển dựa trên nỗi sợ chậm đến mức bò, hồi quy thường xuyên, và các quy trình phát hành thủ công không thể mở rộng. Cũng có chi phí của kiểm thử quá mức, nên lập luận là cho một chiến lược được thiết kế tốt, không phải số lượng kiểm thử tối đa. Để thuyết phục ban lãnh đạo, hãy kết nối bộ kiểm thử với tần suất triển khai, tỷ lệ thay đổi thất bại và thời gian phục hồi trung bình, và định lượng công sức kiểm thử thủ công mà nó thay thế và các sự cố môi trường thực mà nó ngăn chặn.

## Phản mẫu và cạm bẫy

- **Kiểm thử hình que kem:** chủ yếu là các bài kiểm thử đầu-cuối chậm trên một nền đơn vị mỏng; chậm, chập chờn, tốn kém.
- **Độ bao phủ như mục tiêu:** chạy theo một tỷ lệ phần trăm bằng các bài kiểm thử không có khẳng định hoặc tầm thường không chứng minh được gì.
- **Kiểm thử chi tiết triển khai:** các bài kiểm thử gắn với nội bộ, hỏng mỗi lần tái cấu trúc, làm nản lòng việc thay đổi.
- **Dung thứ sự chập chờn:** các thất bại ngẫu nhiên huấn luyện đội phớt lờ các bản dựng đỏ.
- **Dữ liệu kiểm thử khả biến dùng chung:** các bài kiểm thử can thiệp lẫn nhau và thất bại không thể đoán trước.
- **Dùng dữ liệu môi trường thực trong kiểm thử:** một vụ vi phạm riêng tư và tuân thủ đang chờ xảy ra.
- **Bỏ qua kiểm thử phi chức năng:** khả năng tiếp cận, hiệu năng và bảo mật chỉ được phát hiện trên môi trường thực.
- **Bộ kiểm thử không được tin:** không đáng tin đến mức kỹ sư thường xuyên chạy lại hoặc bỏ qua nó, phủ nhận mục đích của nó.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Kiểm thử thủ công và phản ứng; độ bao phủ tự động ở mức tối thiểu; hồi quy thường xuyên và bị bắt muộn, thường do người dùng chứ không phải bộ kiểm thử.
- **Mức 2, Phát triển:** Có các kiểm thử đơn vị tự động và một số kiểm thử tích hợp, nhưng bộ kiểm thử chậm hoặc chập chờn, niềm tin thấp, và thực hành khác nhau nhiều từ đội này sang đội khác.
- **Mức 3, Chuẩn hóa:** Một bộ kiểm thử cân bằng, nhanh, đáng tin cậy chặn mọi thay đổi; một mặc định kim tự tháp được lập thành tài liệu, chính sách kiểm thử chập chờn, và kiểm thử phi chức năng (khả năng tiếp cận, hiệu năng, bảo mật) được thực thi nhất quán giữa các đội.
- **Mức 4, Quản lý:** Sức khỏe bộ kiểm thử được đo và kiểm soát theo các đường cơ sở; tỷ lệ chập chờn, thời gian đồng hồ CI, điểm đột biến trên các mô-đun giá trị cao, và tỷ lệ lỗi thoát ra được theo dõi và xem xét; độ bao phủ là một tín hiệu trong số nhiều tín hiệu, và các cổng kích hoạt dựa trên bằng chứng thay vì ý kiến.
- **Mức 5, Điều phối:** Các kỹ thuật nâng cao (dựa trên thuộc tính, đột biến, mờ) nhắm vào mã có giá trị cao; kiểm thử được tích hợp với các chỉ số phân phối như tần suất triển khai, tỷ lệ thay đổi thất bại và thời gian phục hồi trung bình; tổ chức liên tục định hình lại bộ kiểm thử theo kiến trúc và rủi ro của mình, loại bỏ các kiểm thử dư thừa và đầu tư vào nơi bằng chứng cho thấy lỗi vẫn thoát ra.

## Ý tưởng để thảo luận

- Phân phối kiểm thử của bạn thực sự có hình dạng nào, và nó có khớp với kiến trúc và rủi ro của bạn không?
- Làm thế nào bạn quyết định khi nào một đoạn mã đáng được kiểm thử dựa trên thuộc tính hoặc đột biến so với kiểm thử theo ví dụ?
- Chính sách của bạn cho các kiểm thử chập chờn là gì, và nó có thực sự được thực thi không?
- Làm thế nào bạn sinh dữ liệu tổng hợp thực tế mà không làm rò rỉ thông tin nhạy cảm?
- Độ bao phủ thực sự giúp bạn ở đâu, và nó đã bị lách ở đâu?
- Các bài kiểm thử do AI sinh ra nên được rà soát thế nào để chúng thêm độ tin cậy thay vì nhiễu?

## Những điểm cần ghi nhớ

- Kiểm thử để có sự tự tin thay đổi; tối ưu hóa độ tin cậy trên mỗi đơn vị tốc độ và chi phí.
- Dùng kim tự tháp làm mặc định nhưng định hình kiểm thử theo kiến trúc của bạn.
- Coi kiểm thử chập chờn là lỗi và độ bao phủ là một tín hiệu, không phải mục tiêu.
- Áp dụng các kỹ thuật nâng cao ở nơi giá trị biện minh cho chi phí.
- Đưa kiểm thử khả năng tiếp cận, hiệu năng và bảo mật vào chiến lược, và dùng dữ liệu tổng hợp để bảo vệ quyền riêng tư.

## Tài liệu tham khảo và đọc thêm

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin và Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, các bài viết về Kim tự tháp Kiểm thử và các mẫu liên quan đến kiểm thử
