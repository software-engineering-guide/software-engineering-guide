# 2.15 Gỡ lỗi và xử lý sự cố

## Tổng quan và động lực

Gỡ lỗi là công việc có kỷ luật để tìm hiểu vì sao một hệ thống làm điều mà nó không nên làm, và xử lý sự cố là cùng kỹ năng đó hướng vào một hệ thống môi trường thực đang chạy dưới áp lực thời gian. Cả hai đều là [phương pháp khoa học](https://en.wikipedia.org/wiki/Scientific_method) áp dụng cho lỗi: bạn quan sát một hành vi bất ngờ, hình thành một giả thuyết về nguyên nhân của nó, thiết kế một thí nghiệm có thể xác nhận hoặc bác bỏ nó, và để bằng chứng, không phải linh cảm của bạn, cho bạn biết nên thay đổi gì. Làm theo cách này, gỡ lỗi là một kỹ năng kỹ thuật học được, dạy được. Làm như truyền miệng, nó trở thành mê tín: đổi những dòng ngẫu nhiên, khởi động lại máy chủ và hy vọng.

Với một đội lớn, sự khác biệt này đắt đỏ. Một lỗi khó đơn lẻ có thể kéo các kỹ sư qua nhiều dịch vụ, tiêu tốn giờ trực ca và làm đình trệ một bản phát hành. Khi mỗi người gỡ lỗi theo bản năng, công sức đó không cộng dồn, vì không ai có thể tái hiện hay giải thích những gì người khác đã thử. Khi đội chia sẻ một phương pháp (tái hiện trước, cô lập bằng tìm kiếm, ghi lại lỗi trong một bài kiểm thử thất bại, rồi mới sửa), cùng công sức đó biến thành một quy trình lặp lại được và một bộ kiểm thử hồi quy ngày càng lớn. Gỡ lỗi kết nối chặt với chiến lược kiểm thử (chương 2.4), với chất lượng phần mềm (chương 2.11), và với các thói quen xây dựng (chương 2.9) khiến mã chẩn đoán được ngay từ đầu.

Trong bối cảnh doanh nghiệp và chính phủ, rủi ro tăng lên. Các lỗi doanh nghiệp vượt qua ranh giới dịch vụ và đội, nên người thấy triệu chứng hiếm khi là người sở hữu nguyên nhân. Các hệ thống chính phủ thêm những ràng buộc mà hầu hết kỹ sư chưa bao giờ gặp: môi trường cách ly mạng hoặc bị hạn chế nơi bạn không thể gắn trình gỡ lỗi vào môi trường thực, các bản dựng tái tạo được phải được chẩn đoán từ hiện vật, và dấu vết kiểm toán phải ghi lại bạn đã thay đổi gì và vì sao. Ở cả ba, mục tiêu là như nhau: thay đoán mò bằng bằng chứng.

## Các nguyên tắc chính

- **Tái hiện trước khi bạn lý thuyết hóa.** Một lỗi bạn không thể kích hoạt theo yêu cầu là một tin đồn, không phải khiếm khuyết.
- **Gỡ lỗi là kiểm tra giả thuyết.** Nêu điều bạn tin, rồi thiết kế thí nghiệm rẻ nhất có thể chứng minh bạn sai.
- **Đọc lỗi và dấu vết ngăn xếp trước.** Hệ thống thường cho bạn biết nó hỏng ở đâu trước khi bạn thay đổi một dòng.
- **Tìm kiếm không gian vấn đề, đừng quét nó.** Chia đôi vùng nghi vấn ở mỗi bước thay vì đọc từ trên xuống dưới.
- **Rút gọn đến mức tối thiểu.** Lược bỏ trường hợp cho đến khi chỉ còn tác nhân thiết yếu.
- **Mỗi lần một thay đổi.** Chỉnh sửa bừa bãi phá hủy bằng chứng lẽ ra cho bạn biết thay đổi nào quan trọng.
- **Ghi lại lỗi trong một bài kiểm thử thất bại trước khi bạn sửa.** Bản sửa chỉ được chứng minh khi bài kiểm thử đó chuyển xanh và giữ xanh.
- **Tìm nguyên nhân gốc, không phải triệu chứng gần nhất.** Một bản vá che giấu triệu chứng để khiếm khuyết quay lại.

## Khuyến nghị

### Tái hiện khiếm khuyết một cách đáng tin cậy trước khi thay đổi bất cứ điều gì

Việc đầu tiên của bạn là một bản tái hiện đáng tin cậy: một tập các bước hoặc một ca tự động kích hoạt lỗi theo yêu cầu. Không có nó bạn không thể phân biệt một bản sửa thực với một sự trùng hợp, vì triệu chứng có thể đến và đi vì những lý do bạn chưa bao giờ kiểm soát. Xác định đầu vào, môi trường, phiên bản và thời điểm. Nếu lỗi xuất hiện không liên tục, hãy săn biến ẩn khiến nó xuất hiện (một bản ghi dữ liệu cụ thể, một ranh giới đồng hồ, một yêu cầu đồng thời) cho đến khi bản tái hiện đáng tin cậy. Một bản tái hiện đáng tin cậy là hiện vật có giá trị nhất duy nhất trong gỡ lỗi, vì mọi thứ sau nó trở nên đo lường được.

### Đọc lỗi, nhật ký và dấu vết ngăn xếp trước khi chạm vào mã

Trước khi bạn hình thành một lý thuyết, hãy đọc những gì hệ thống đã nói với bạn. [Dấu vết ngăn xếp](https://en.wikipedia.org/wiki/Stack_trace) (bản ghi chuỗi gọi hàm tại thời điểm thất bại) thường nêu tên tệp, dòng và chuỗi đã thất bại. Thông báo ngoại lệ, các dòng nhật ký xung quanh nó và các giá trị trong phạm vi thu hẹp việc tìm kiếm trước khi bạn thay đổi bất cứ điều gì. Kỹ sư lãng phí hàng giờ để lý thuyết hóa về các nguyên nhân mà traceback đã loại trừ ngay dòng đầu tiên. Hãy coi đầu ra lỗi là nhân chứng đầu tiên, đọc nó cẩn thận và đầy đủ, và chỉ sau đó mới quyết định điều tra gì.

### Cô lập bằng tìm kiếm nhị phân trong không gian vấn đề

Đừng quét mã từ trên xuống dưới. Hãy tìm kiếm nó. Dùng [tìm kiếm nhị phân](https://en.wikipedia.org/wiki/Binary_search_algorithm): tìm một điểm nơi trạng thái vẫn tốt và một điểm nơi nó đã xấu, rồi kiểm tra điểm giữa, và lặp lại, chia đôi vùng nghi vấn mỗi lần. Điều này biến một cuộc tìm kiếm nghìn dòng thành mười câu hỏi. Khi hồi quy xuất hiện qua một dải commit, hãy áp dụng cùng ý tưởng cho lịch sử bằng chia đôi: `git bisect` đi qua dải commit, và bạn đánh dấu từng bản sửa đổi là tốt hay xấu cho đến khi nó nêu tên chính xác thay đổi đã đưa vào khiếm khuyết. Hãy tự động hóa phép thử tốt-hay-xấu và việc chia đôi tự chạy.

### Rút gọn thành một ví dụ tái hiện tối thiểu

Một khi bạn có thể kích hoạt lỗi, hãy thu nhỏ nó. Một [ví dụ tái hiện tối thiểu](https://en.wikipedia.org/wiki/Minimal_reproducible_example) là đầu vào và đường mã nhỏ nhất vẫn thất bại: loại bỏ dữ liệu, tính năng và bước cho đến khi bất kỳ sự loại bỏ nào nữa khiến lỗi biến mất. Rút gọn không phải việc vặt; mỗi yếu tố bạn loại bỏ là một nguyên nhân bạn đã loại trừ, nên trường hợp tối thiểu thường chỉ thẳng vào khiếm khuyết. Khi đầu vào lớn hoặc có cấu trúc, hãy tự động hóa việc thu nhỏ bằng [gỡ lỗi delta](https://en.wikipedia.org/wiki/Delta_debugging), một thuật toán loại bỏ có hệ thống các khối của một đầu vào thất bại để tìm tập con thất bại tối thiểu. Một bản tái hiện nhỏ, tự đủ cũng là báo cáo lỗi tốt nhất có thể trao cho một đội khác.

### Trang bị bằng nhật ký, rồi dùng trình gỡ lỗi tương tác

Hãy khớp công cụ với lỗi. Ghi nhật ký và trang bị có mục tiêu tốt nhất khi bạn cần thấy hành vi theo thời gian, qua các tiến trình, hoặc trong một môi trường bạn không thể tạm dừng. Một trình gỡ lỗi tương tác, cho phép bạn đặt điểm dừng, bước từng dòng và kiểm tra trạng thái sống, tốt nhất khi bạn có thể chạy mã cục bộ và cần theo dõi sát một lần thực thi. Hãy thêm công cụ đo đạc như một thí nghiệm có chủ đích gắn với một giả thuyết, không phải các câu lệnh in rải rác, và loại bỏ nó hoặc thăng cấp thành nhật ký có cấu trúc vĩnh viễn một khi lỗi đã được giải quyết. Trên môi trường thực, hãy dựa vào gỡ lỗi dựa trên khả năng quan sát: các sự kiện có số lượng phần tử cao và truy vết phân tán (chương 9.2) cho phép bạn theo dõi một yêu cầu qua nhiều dịch vụ, thường là cách duy nhất để gỡ lỗi một hệ thống phân tán mà bạn không thể gắn trình gỡ lỗi vào.

### Viết một bài kiểm thử thất bại nắm bắt lỗi trước khi bạn sửa

Trước khi bạn viết bản sửa, hãy viết một bài kiểm thử thất bại vì lỗi. Điều này làm ba việc cùng lúc: nó chứng minh bạn thực sự hiểu nguyên nhân, nó xác định chính xác "đã sửa" nghĩa là gì, và nó trở thành một người bảo vệ vĩnh viễn. Sau đó thực hiện bản sửa và xem bài kiểm thử chuyển xanh. Bài kiểm thử đó giờ gia nhập bộ của bạn như một người bảo vệ [kiểm thử hồi quy](https://en.wikipedia.org/wiki/Regression_testing), để cùng khiếm khuyết không thể quay lại mà không bị chú ý. Thực hành này gắn gỡ lỗi trực tiếp với chiến lược kiểm thử của bạn (chương 2.4): mỗi lỗi khó bạn giải quyết để lại bộ kiểm thử mạnh hơn khi bạn tìm thấy nó, và một bài kiểm thử chập chờn nhận cùng sự đối xử (tái hiện tính không xác định, rồi bảo vệ chống lại nó) thay vì một chú thích thử lại.

### Tìm nguyên nhân gốc, và giữ phân tích không đổ lỗi

Sửa triệu chứng không phải là sửa lỗi. Truy vết thất bại về nguồn gốc thực của nó, hỏi vì sao ở mỗi tầng cho đến khi bạn đến một nguyên nhân bạn có thể loại bỏ thay vì che giấu. Với các khiếm khuyết đã đến môi trường thực, hãy tiến hành phân tích nguyên nhân gốc không đổ lỗi như một phần của quản lý sự cố (chương 9.3): tập trung vào các điều kiện hệ thống và quy trình đã cho phép lỗi được phát hành và tồn tại, không bao giờ vào cá nhân đã viết dòng mã đó. Đổ lỗi đẩy thông tin xuống ngầm, và gỡ lỗi chạy trên thông tin. Đầu ra vừa là một bản sửa vừa là một thay đổi về cách loại khiếm khuyết đó được bắt sớm hơn lần sau.

## Đánh đổi: ưu và nhược điểm

| Cách tiếp cận | Ưu điểm | Nhược điểm |
|---|---|---|
| Ghi nhật ký và trang bị | Hoạt động trên môi trường thực và hệ thống phân tán; nắm bắt hành vi theo thời gian | Nhiễu, chi phí và nhật ký tràn lan; có thể làm nhiễu các lỗi thời điểm |
| Trình gỡ lỗi tương tác | Kiểm tra trạng thái sống chính xác; nhanh cho lỗi cục bộ | Vô dụng trong môi trường môi trường thực hạn chế hoặc cách ly mạng; có thể che giấu lỗi đồng thời |
| Kỷ luật tái hiện trước | Biến đoán mò thành đo lường; cho phép một bài kiểm thử thất bại | Chậm lúc đầu; một số lỗi thực sự khó kích hoạt |
| Tìm kiếm nhị phân và chia đôi | Cô lập nhanh, kể cả trong mã lạ | Cần phép thử tốt-hay-xấu đáng tin cậy; khó khi các lỗi tương tác |
| Rút gọn gỡ lỗi delta | Tự động thu nhỏ đầu vào khổng lồ về tác nhân | Chi phí thiết lập; giả định thất bại là xác định |
| Sửa triệu chứng ngay | Khôi phục dịch vụ nhanh dưới áp lực | Để nguyên nhân gốc quay lại; tích tụ nợ |

Căng thẳng trung tâm là tốc độ so với độ chắc chắn. Trong một sự cố môi trường thực bạn có thể cần cầm máu trước (hoàn tác hoặc vá triệu chứng) để khôi phục dịch vụ, và điều đó là chính đáng. Sai lầm là dừng ở đó. Hãy giải quyết căng thẳng bằng cách tách hai việc: giảm nhẹ nhanh để bảo vệ người dùng, rồi tái hiện, tìm nguyên nhân gốc, và thêm người bảo vệ hồi quy trước khi bạn coi khiếm khuyết là đã đóng. Một bản sửa triệu chứng mà không có theo dõi là một lỗi bạn đã đồng ý gặp lại.

## Câu hỏi để thảo luận với đội của bạn

1. **Khi ai đó gặp một lỗi khó, việc đầu tiên họ làm là gì, tái hiện hay đoán?** Câu trả lời trung thực cho thấy đội bạn có một phương pháp chung hay một căn phòng đầy truyền miệng riêng tư. Hãy nhờ mọi người kể thành tiếng khiếm khuyết khó gần nhất của họ: họ có lấy được bản tái hiện đáng tin cậy trước không, hay bắt đầu thay đổi mã và khởi động lại mọi thứ? Một đội tái hiện trước có thể chuyển một lỗi giữa các người, vì bản tái hiện đi theo; một đội đoán mò thì không thể, vì mỗi lần thử không lặp lại được. Điều này quan trọng hơn khi đội lớn lên, vì người thấy triệu chứng ngày càng không phải là người có thể sửa. Nếu mặc định là đoán, hãy thống nhất tái hiện trước như một chuẩn mực và biến một bản tái hiện sạch thành giá vé vào một phiếu lỗi.

2. **Những lỗi chúng ta sửa có quay lại không, và chúng ta có biết nếu chúng quay lại không?** Một khiếm khuyết quay lại là khiếm khuyết mà nguyên nhân gốc chưa bao giờ được loại bỏ và bản sửa chưa bao giờ được bảo vệ bằng một bài kiểm thử. Hãy lấy quý vừa qua của các sự cố và phiếu mở lại và đếm xem bao nhiêu cái là lặp lại hoặc họ hàng gần của các lỗi trước. Mỗi lần lặp lại là bằng chứng rằng đội đã vá triệu chứng, bỏ qua bài kiểm thử thất bại, hoặc dừng phân tích nguyên nhân gốc quá sớm. Cách sửa là một quy tắc: không lỗi nào được đóng cho đến khi một bài kiểm thử thất bại trên hành vi cũ đạt trên hành vi mới và gia nhập bộ kiểm thử. Hãy mang một lỗi tái diễn gần đây và hỏi người bảo vệ nào sẽ đã bắt được nó, vì người bảo vệ đó là thứ bạn đã thiếu.

3. **Chúng ta có gỡ lỗi được các hệ thống môi trường thực của mình không, xét theo cách chúng ta được phép chạm vào chúng?** Trong các môi trường doanh nghiệp và đặc biệt là chính phủ, bạn thường không thể gắn trình gỡ lỗi, không thể tái hiện với dữ liệu thực, và không thể thay đổi một hệ thống đang chạy mà không có dấu vết kiểm toán. Nếu kỹ thuật gỡ lỗi duy nhất của bạn là một trình gỡ lỗi tương tác cục bộ, bạn bị mù chính xác ở nơi những lỗi khó nhất sống. Hãy hỏi một thất bại môi trường thực thực sự để lại bằng chứng gì: nhật ký có cấu trúc, truy vết phân tán (chương 9.2), bản đổ lõi, hay hiện vật dựng tái tạo được. Hãy quyết định ngay bây giờ bạn phải thu thập gì theo mặc định để một sự cố tương lai chẩn đoán được, vì bạn không thể thêm công cụ đo đạc vào một thất bại đã xảy ra. Trong các bối cảnh chịu quy định, hãy xác nhận rằng cùng dấu vết đó cũng thỏa mãn nghĩa vụ kiểm toán của bạn.

4. **Khi một sự cố môi trường thực buộc chúng ta phải cầm máu nhanh, làm thế nào chúng ta bảo đảm nguyên nhân gốc vẫn được tìm ra sau đó?** Trong một sự cố, hoàn tác hoặc vá triệu chứng là bước đầu đúng để bảo vệ người dùng, nhưng nguy cơ là phiếu việc đóng ngay khoảnh khắc dịch vụ trở lại và khiếm khuyết nền tảng không bao giờ được chẩn đoán. Với một đội lớn đây là nơi nợ tích tụ vô hình, vì cùng loại thất bại nổi lên lại trên một dịch vụ khác và một kỹ sư trực ca khác nhiều tháng sau. Hãy mang vài sự cố mức nghiêm trọng một gần nhất của bạn và kiểm tra từng cái: một bản tái hiện, phân tích nguyên nhân gốc và người bảo vệ hồi quy có theo sau việc giảm nhẹ không, hay câu chuyện kết thúc ở "dịch vụ đã khôi phục"? Hãy thống nhất một quy tắc tường minh rằng một sự cố đã giảm nhẹ vẫn mở cho đến khi nguyên nhân gốc được hiểu và bảo vệ, và nêu tên ai sở hữu việc theo dõi đó. Trong bối cảnh doanh nghiệp và chính phủ, hãy gắn điều này với quy trình quản lý sự cố của bạn (chương 9.3) để cuộc rà soát sau sự cố là một bước bắt buộc, có thể kiểm toán thay vì một phép lịch sự trượt đi khi đám cháy tiếp theo bắt đầu.

5. **Chúng ta thực sự có thể dựng lại bao nhiêu phần của một thất bại sau sự việc, và ai quyết định chúng ta thu thập gì theo mặc định?** Bạn không thể gắn công cụ đo đạc vào một thất bại đã xảy ra, nên khả năng chẩn đoán của bất kỳ sự cố nào được cố định từ trước bởi các nhật ký, truy vết, chỉ số và bản đổ bạn đã chọn phát ra. Cân nhắc đối lập là chi phí và nhiễu: các sự kiện có số lượng phần tử cao và truy vết đầy đủ không miễn phí, và ghi nhật ký quá mức chôn vùi tín hiệu trong khi thổi phồng lưu trữ và, trong bối cảnh chịu quy định, rủi ro lưu giữ dữ liệu của bạn. Hãy mang một sự cố thực gần đây và hỏi nó để lại bằng chứng gì, rồi làm ngược lại xem bạn ước mình đã thu thập gì và việc giữ nó tốn bao nhiêu. Hãy quyết định có chủ đích tín hiệu nào bật theo mặc định so với được lấy mẫu hoặc tùy chọn, và ghi lại quyết định đó để nó là chính sách, không phải tai nạn. Với một hệ thống doanh nghiệp hoặc chính phủ, hãy thêm ai chịu trách nhiệm cho ngân sách khả năng quan sát đó và liệu dấu vết được thu thập có cũng thỏa mãn các nghĩa vụ kiểm toán, riêng tư và nơi lưu trữ dữ liệu không.

6. **Chúng ta có coi gỡ lỗi là một kỹ năng được dạy, đo được, hay kỹ sư mới thẩm thấu nó một cách tự nhiên?** Gỡ lỗi học được, nhưng hầu hết các đội không bao giờ dạy nó một cách tường minh, nên người mới vào thừa hưởng bất cứ truyền miệng nào ở gần nhất, và phương pháp tái hiện trước lan truyền không đồng đều hoặc không lan. Căng thẳng là việc dạy có chủ đích (lập trình theo cặp trên các lỗi khó, viết ra các phát hiện sau sự cố, theo dõi các chỉ số) tốn thời gian của người cấp cao mà luôn có cảm giác cần ở nơi khác. Hãy mang hai con số đến cuộc thảo luận: tỷ lệ khiếm khuyết lặp lại và thời gian chẩn đoán của bạn, vì nếu bạn không đo được chúng bạn không thể biết phương pháp của mình đang cải thiện hay suy giảm. Hãy cân nhắc liệu hội nhập có bao gồm một bài tập gỡ lỗi thực không và các phát hiện nguyên nhân gốc có thực sự nuôi dưỡng việc phát hiện sớm hơn không. Trong một tổ chức lớn hoặc công, một thực hành gỡ lỗi có tài liệu, được đo cũng trở thành bằng chứng về sự chặt chẽ kỹ thuật mà kiểm toán viên, cơ quan quản lý và cơ quan giám sát ngày càng mong thấy.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với một nhúm kỹ sư và không còn dư thời gian, mục tiêu của bạn là làm cho lỗi rẻ để tái hiện và không thể quên, không phải xây quy trình nặng. Hãy dựa vào `git bisect`, một bản tái hiện cục bộ nhanh, và một bài kiểm thử thất bại cho mỗi lỗi đã sửa, vì thói quen đó tốn vài phút và ngăn bạn trả lại cùng một khiếm khuyết trong khi bạn đang cố phát hành. Bỏ qua các cuộc phân tích hậu sự cố chính thức, nhưng đừng bao giờ bỏ qua bài kiểm thử hồi quy: nó là hiện vật duy nhất đủ nhỏ để luôn gánh được và đủ giá trị để luôn giữ.

**Doanh nghiệp nhỏ.** Bạn có thể không có chuyên gia độ tin cậy hay khả năng quan sát riêng và ngân sách công cụ eo hẹp, vì vậy hãy ưu tiên những gì bộ công nghệ của bạn đã cho: dấu vết ngăn xếp dễ đọc, nhật ký có cấu trúc, và truy vết tích hợp trong các khung và dịch vụ lưu trữ bạn đã mua. Khi bạn đánh giá một nền tảng mới, hãy cân nhắc nó làm cho thất bại chẩn đoán được đến đâu, vì một công cụ rẻ che giấu điều gì đã sai tốn của bạn nhiều thời gian đoán mò hơn nhiều so với số tiền giấy phép tiết kiệm được. Tái hiện trước và mỗi lần một thay đổi là các kỷ luật miễn phí hoàn vốn nhanh nhất khi không ai có thời gian dư.

**Doanh nghiệp lớn.** Các lỗi khó của bạn vượt qua ranh giới dịch vụ và đội, nên người thấy triệu chứng hiếm khi sở hữu nguyên nhân, và một phương pháp chung quan trọng hơn kỹ năng của bất kỳ cá nhân nào. Hãy chuẩn hóa tái hiện trước, cô lập bằng tìm kiếm nhị phân, một bài kiểm thử thất bại trước khi sửa, và phân tích hậu sự cố không đổ lỗi qua các đội, và đầu tư vào truy vết phân tán (chương 9.2) để một yêu cầu có thể được theo dõi qua các dịch vụ. Hãy quản lý gỡ lỗi như một năng lực được đo: theo dõi tỷ lệ khiếm khuyết lặp lại và thời gian chẩn đoán, và đưa các phát hiện nguyên nhân gốc trở lại vào phát hiện sớm hơn để cùng loại thất bại không đi dạo khắp bản đồ dịch vụ của bạn.

**Chính phủ.** Quy tắc mua sắm, môi trường bị hạn chế và trách nhiệm giải trình trước công chúng định hình cách bạn được phép gỡ lỗi. Bạn thường không thể gắn trình gỡ lỗi vào môi trường thực hoặc sao chép dữ liệu công dân vào laptop, vì vậy hãy thiết kế để chẩn đoán từ những gì được phép: bản dựng tái tạo được, bản ghi tổng hợp trong một khu vực cô lập, và nhật ký cùng truy vết có cấu trúc được thu thập theo mặc định. Hãy ghi lại mọi bước chẩn đoán và mọi thay đổi trong dấu vết kiểm toán, và yêu cầu các nhà cung cấp phơi bày đủ đo đạc từ xa và khả năng tái tạo bản dựng để bạn điều tra thất bại một cách độc lập thay vì phụ thuộc vào lời của nhà cung cấp.

## Ví dụ

**Công ty khởi nghiệp.** Một đội bốn kỹ sư liên tục thấy thanh toán thất bại với một phần người dùng, nhưng không bao giờ trong kiểm thử. Thay vì đoán, một kỹ sư lấy một bản tái hiện đáng tin cậy bằng cách phát lại chính xác tải trọng yêu cầu thất bại, rồi đọc dấu vết ngăn xếp mà họ đã bỏ qua, chỉ vào một lệnh gọi phân tích ngày tháng. Một lần `git bisect` nhanh qua các commit của tuần nêu tên thay đổi đã chuyển một thư viện ngày tháng. Họ viết một bài kiểm thử thất bại với dấu thời gian vi phạm, sửa bộ phân tích, xem bài kiểm thử chuyển xanh và giữ nó trong bộ. Toàn bộ cuộc điều tra mất một buổi chiều vì họ tái hiện trước khi lý thuyết hóa, và lỗi không bao giờ quay lại.

**Doanh nghiệp lớn.** Một nền tảng thanh toán thấy các lần hết thời gian chờ gián đoạn mà không đội nào giải thích được, vì triệu chứng hiện ở thanh toán nhưng nguyên nhân nằm cách ba dịch vụ. Các kỹ sư trực ca dùng truy vết phân tán (chương 9.2) để theo dõi một yêu cầu thất bại qua các ranh giới dịch vụ và tìm thấy một lệnh gọi hạ nguồn thỉnh thoảng bế tắc dưới tải đồng thời, một [điều kiện chạy đua](https://en.wikipedia.org/wiki/Race_condition) kinh điển nơi kết quả phụ thuộc vào thời điểm không may giữa các luồng. Họ tái hiện nó bằng một kiểm thử tải, ghi lại trong một bài kiểm thử tích hợp thất bại, sửa việc khóa, và tiến hành một cuộc phân tích hậu sự cố không đổ lỗi (chương 9.3) thêm một khoảng truy vết và một cảnh báo để lần xuất hiện tiếp theo được bắt trong vài phút, không phải vài ngày.

**Chính phủ.** Một cơ quan trợ cấp vận hành hệ thống hồ sơ của mình trong một môi trường cách ly mạng nơi kỹ sư không thể gắn trình gỡ lỗi vào môi trường thực và không thể sao chép dữ liệu công dân vào laptop. Một khiếm khuyết tính toán nổi lên trong đối chiếu. Đội gỡ lỗi từ những gì môi trường cho phép: nhật ký có cấu trúc, một bản dựng tái tạo được mà họ có thể dựng lên trong một khu vực kiểm thử cô lập, và các bản ghi tổng hợp tái tạo ca thất bại. Mọi bước chẩn đoán được ghi lại trong dấu vết kiểm toán, bản sửa được giao kèm một bài kiểm thử thất bại-rồi-đạt làm bằng chứng, và phân tích nguyên nhân gốc nuôi dưỡng một kiểm tra trước phát hành mới. Vì bản tái hiện dùng dữ liệu tổng hợp, không bản ghi công dân nào rời khỏi ranh giới.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của gỡ lỗi có kỷ luật được đo bằng giờ kỹ sư không bị lãng phí đoán mò và bằng các khiếm khuyết không tái diễn. Một lỗi gián đoạn chưa được chẩn đoán có thể tiêu tốn nhiều ngày của người cấp cao và các lần leo thang trực ca lặp lại; một phương pháp tái hiện trước biến điều đó thành một nhiệm vụ có giới hạn, ủy quyền được, và thói quen bài kiểm thử thất bại ngăn cùng một khiếm khuyết tính tiền bạn quý sau. Trong một tổ chức lớn, hiệu ứng cộng dồn của việc không bao giờ trả lại cùng một lỗi là đáng kể, và nó trực tiếp cải thiện tỷ lệ thay đổi thất bại và thời gian phục hồi trung bình mà ban lãnh đạo vốn đã theo dõi.

Tổng chi phí sở hữu chủ yếu là đào tạo và công cụ, và khiêm tốn. Bạn cần các quy ước chung (tái hiện trước, mỗi lần một thay đổi, một bài kiểm thử thất bại trước bản sửa), trình gỡ lỗi và truy vết vốn đã phổ biến trong bộ công cụ, và khoản đầu tư khả năng quan sát được mô tả trong chương 9.2. Chi phí ẩn lớn hơn là phương án thay thế: một văn hóa mê tín nơi kỹ sư áp dụng các thay đổi bừa bãi, triệu chứng được vá rồi quay lại, và tải trực ca tăng không giới hạn. Chỉ riêng việc giảm công việc lặp lại trực ca thường đã biện minh cho khoản đầu tư, và lập luận với ban lãnh đạo đơn giản nhất khi nêu là ít sự cố lặp lại hơn và phục hồi nhanh hơn với chi phí một lần cho thói quen và công cụ đo đạc.

## Phản mẫu và cạm bẫy

- **Gỡ lỗi bừa bãi:** thay đổi nhiều thứ cùng lúc, nên ngay cả một bản sửa cũng không dạy bạn gì về nguyên nhân.
- **Sửa mà không tái hiện:** tuyên bố chiến thắng trên một lỗi mà bạn chưa bao giờ kích hoạt được theo yêu cầu.
- **Phớt lờ đầu ra lỗi:** lý thuyết hóa về các nguyên nhân mà dấu vết ngăn xếp đã loại trừ.
- **Vá triệu chứng:** dập tắt triệu chứng trong khi nguyên nhân gốc sống sót để quay lại.
- **Câu lệnh in tràn lan:** đầu ra gỡ lỗi rải rác để lại trong mã, thêm nhiễu thay vì một thí nghiệm gắn với giả thuyết.
- **Bỏ qua bài kiểm thử hồi quy:** sửa lỗi nhưng không để lại người bảo vệ, nên nó có thể âm thầm quay lại.
- **Thử lại các bài kiểm thử chập chờn:** che giấu tính không xác định bằng thử lại thay vì gỡ lỗi điều kiện chạy đua nền tảng hoặc [heisenbug](https://en.wikipedia.org/wiki/Heisenbug), một lỗi thay đổi hoặc biến mất ngay khoảnh khắc bạn cố quan sát nó.
- **Phân tích hậu sự cố đổ lỗi:** trừng phạt tác giả, đẩy xuống ngầm thông tin mà gỡ lỗi phụ thuộc.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Gỡ lỗi là truyền miệng cá nhân và phản ứng. Kỹ sư đoán, áp dụng các thay đổi bừa bãi, và khởi động lại mọi thứ. Lỗi được sửa ở triệu chứng, bản tái hiện hiếm, và cùng các khiếm khuyết tái diễn. Môi trường thực khó chẩn đoán, và không ai có thể chuyển một lỗi cho ai khác vì không lần thử nào lặp lại được.
- **Mức 2, Phát triển:** Một số kỹ sư tái hiện đáng tin cậy, đọc dấu vết ngăn xếp, và dùng trình gỡ lỗi, nhưng thực hành không nhất quán và khác nhau theo người và theo đội. Ghi nhật ký tồn tại nhưng ồn ào và không có cấu trúc. Các bản sửa đôi khi được giao kèm một bài kiểm thử thất bại, thường không, và phân tích nguyên nhân gốc chỉ xảy ra khi có ai đó khăng khăng.
- **Mức 3, Chuẩn hóa:** Tái hiện trước, cô lập bằng tìm kiếm nhị phân, mỗi lần một thay đổi, và một bài kiểm thử thất bại trước bản sửa là các chuẩn mực của đội được lập thành tài liệu và thực thi trong toàn tổ chức. Chia đôi và rút gọn gỡ lỗi delta là thực hành phổ biến. Môi trường thực có ghi nhật ký và truy vết có cấu trúc (chương 9.2), và phân tích hậu sự cố không đổ lỗi (chương 9.3) là phản ứng chuẩn cho mọi khiếm khuyết thoát ra.
- **Mức 4, Quản lý:** Thực hành gỡ lỗi được đo và kiểm soát theo các đường cơ sở. Tỷ lệ khiếm khuyết lặp lại, thời gian chẩn đoán, số phiếu mở lại, và tỷ lệ các bản sửa được giao kèm bài kiểm thử hồi quy được theo dõi cho từng đội và xem xét theo chu kỳ. Hoàn thành tái hiện và nguyên nhân gốc được coi là các cổng thay vì ý định tốt, và các xu hướng so với đường cơ sở dẫn dắt nơi bạn đầu tư vào công cụ, đào tạo và khả năng quan sát.
- **Mức 5, Điều phối:** Gỡ lỗi là một kỹ năng được dạy, tích hợp với chất lượng (chương 2.11) và quản lý sự cố (chương 9.3), và toàn bộ vòng lặp thích ứng liên tục. Khả năng quan sát được thiết kế vào để hầu hết lỗi môi trường thực chẩn đoán được mà không cần trình gỡ lỗi, mỗi lỗi được giải quyết củng cố bộ kiểm thử hồi quy, và các phát hiện nguyên nhân gốc nuôi dưỡng phát hiện sớm hơn để các loại khiếm khuyết được ngăn chặn thay vì chẩn đoán lại. Tổ chức cân bằng lại công sức khi hệ thống và chế độ thất bại của nó tiến hóa, và tỷ lệ khiếm khuyết lặp lại tiếp tục giảm.

## Ý tưởng để thảo luận

1. Bao nhiêu phần các lỗi gần đây của bạn được tái hiện đáng tin cậy trước khi có ai thay đổi mã, và phần đó nói gì về phương pháp của bạn?
2. Khi một hồi quy xuất hiện, đội bạn có với tới chia đôi, hay đọc mã bằng tay cho đến khi ai đó phát hiện ra?
3. Hệ thống môi trường thực của bạn hiện chẩn đoán được đến đâu, và bạn sẽ đánh đổi gì để có thể thu thập về một thất bại đã xảy ra?
4. Các bản sửa của bạn có đều đặn được giao kèm một bài kiểm thử thất bại-rồi-đạt không, và nếu không, kỷ luật đó vỡ ra ở đâu?
5. Bạn xử lý các bài kiểm thử chập chờn thế nào: gỡ lỗi tính không xác định, hay che đậy nó bằng thử lại?
6. Gỡ lỗi có được dạy có chủ đích cho kỹ sư mới, hay họ được để thẩm thấu truyền miệng một cách tự nhiên?

## Những điểm cần ghi nhớ

- Gỡ lỗi là kiểm tra giả thuyết: tái hiện đáng tin cậy, đọc lỗi và dấu vết ngăn xếp, rồi cô lập bằng tìm kiếm nhị phân và chia đôi thay vì quét.
- Rút gọn thất bại thành một ví dụ tái hiện tối thiểu, dùng gỡ lỗi delta cho đầu vào lớn, vì mỗi yếu tố bị loại bỏ là một nguyên nhân bị loại trừ.
- Khớp công cụ với lỗi: trang bị và truy vết cho môi trường thực và hệ thống phân tán (chương 9.2), trình gỡ lỗi tương tác cho điều tra cục bộ.
- Viết một bài kiểm thử thất bại nắm bắt lỗi trước khi bạn sửa, để bản sửa được chứng minh và khiếm khuyết được bảo vệ mãi mãi (chương 2.4).
- Tìm và loại bỏ nguyên nhân gốc, tiến hành phân tích hậu sự cố không đổ lỗi (chương 9.3), và coi gỡ lỗi là một kỹ năng học được, không phải truyền miệng.
- Mỗi lần thay đổi một thứ; thay đổi bừa bãi và vá triệu chứng phá hủy bằng chứng và mời lỗi quay lại.

## Tài liệu tham khảo và đọc thêm

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller và Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (thuật toán gỡ lỗi delta)
- Brian W. Kernighan và Rob Pike, *The Practice of Programming* (chương về gỡ lỗi)
- Andrew Hunt và David Thomas, *The Pragmatic Programmer* (các chương về gỡ lỗi và khẳng định)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (chương về gỡ lỗi)
- John Regehr, "Reducers Are Fuzzers" và các bài viết liên quan về rút gọn ca kiểm thử
- Charity Majors, Liz Fong-Jones và George Miranda, *Observability Engineering* (gỡ lỗi môi trường thực bằng đo đạc từ xa có số lượng phần tử cao và truy vết)
- Betsy Beyer, Chris Jones, Jennifer Petoff và Niall Richard Murphy, biên tập, *Site Reliability Engineering* (phân tích hậu sự cố không đổ lỗi và gỡ lỗi môi trường thực)
