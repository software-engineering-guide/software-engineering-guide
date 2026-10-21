# 8.3 Container, điều phối và cloud-native

## Tổng quan và động lực

Một [container](https://en.wikipedia.org/wiki/OS-level_virtualization) đóng gói một ứng dụng cùng các phụ thuộc của nó thành một đơn vị duy nhất, di động, cô lập. Nó chạy giống nhau trên laptop, trong môi trường kiểm thử và trong môi trường sản xuất. Các nền tảng điều phối, nổi bật nhất là [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), lập lịch và quản lý số lượng lớn container qua các đội máy. Chúng xử lý việc đặt chỗ, co giãn, sức khỏe, mạng và phục hồi. [Cloud-native](https://en.wikipedia.org/wiki/Cloud-native_computing) là phong cách kiến trúc rộng hơn xây trên những nền tảng này: ứng dụng được thiết kế như các dịch vụ ghép lỏng, triển khai độc lập, co giãn ngang, giả định một hạ tầng động, tự phục hồi.

Với các đội lớn, container và điều phối giải quyết một bài toán khó. Bạn cần chạy nhiều dịch vụ, do nhiều đội xây, một cách đáng tin và hiệu quả trên hạ tầng dùng chung. Container cho mọi đội một hợp đồng đóng gói và thời gian chạy nhất quán, chấm dứt loại thất bại "chạy được trên máy tôi." Điều phối giấu từng máy sau một nền chung, để các đội triển khai lên một nền tảng thay vì lên máy chủ. Sự chuẩn hóa này là thứ cho phép bạn vận hành hàng trăm hay hàng nghìn dịch vụ mà không phải mọi đội phát minh lại triển khai, co giãn và khả năng phục hồi.

Các tổ chức doanh nghiệp và chính phủ áp dụng thu được tính di động, khả năng phục hồi, và một con đường tránh khóa chặt. Đổi lại, họ thừa hưởng độ phức tạp thật và trách nhiệm bảo mật mới. Một nền tảng container mạnh chính vì nó lập trình được và động, nghĩa là bạn phải quản trị nó cẩn thận. Nguồn gốc ảnh, cô lập đa người thuê, chính sách mạng và chi phí đều trở thành mối quan tâm cấp nền tảng. Các tổ chức khu vực công ngày càng thêm yêu cầu chủ quyền: kiểm soát dữ liệu cư trú ở đâu và ai truy cập được. Điều đó biến khả năng chạy khối lượng công việc nhất quán qua các môi trường được chọn thành năng lực chiến lược, không chỉ là chi tiết kỹ thuật.

## Các nguyên tắc chính

- Đóng gói ứng dụng thành các ảnh container nhỏ, đơn mục đích, bất biến.
- Thực hành vệ sinh ảnh: ảnh nền tối thiểu, phiên bản được ghim, quét lỗ hổng, và ký.
- Thiết kế ứng dụng không trạng thái và co giãn ngang bất cứ khi nào có thể, đưa trạng thái ra ngoài.
- Coi mô hình trạng thái-mong-muốn của nền tảng điều phối là nguồn sự thật và để nó tự phục hồi.
- Thực thi cô lập và quyền tối thiểu giữa người thuê, khối lượng công việc và không gian tên.
- Theo các nguyên tắc [mười hai yếu tố](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), một phương pháp luận để xây ứng dụng dùng một lần, cấu hình đặt ngoài, co giãn ngang, và mở rộng chúng cho thực tế của hệ phân tán.
- Làm chi phí thành mối quan tâm kỹ thuật hạng nhất, hiển thị, không phải chuyện nghĩ sau.
- Ưu tiên các trừu tượng di động, dựa trên tiêu chuẩn để giữ sự linh hoạt chiến lược.

## Khuyến nghị

### Thực hành vệ sinh ảnh nghiêm ngặt

Ảnh container là đơn vị cơ bản của lòng tin và triển khai, nên hãy đối xử với nó như vậy. Bắt đầu từ ảnh nền tối thiểu, đáng tin để thu nhỏ bề mặt tấn công. Ghim phiên bản phụ thuộc và ảnh nền để tái lập. Quét mọi ảnh tìm lỗ hổng đã biết trong đường ống dựng, và chặn những cái có phát hiện nghiêm trọng. Ký ảnh và xác minh chữ ký lúc triển khai, để chỉ ảnh đã duyệt, chưa sửa đổi mới chạy. Giữ một registry nội bộ được chọn lọc gồm các ảnh nền đã gia cố mà các đội dựng từ đó. Điều này lan truyền mặc định bảo mật tốt một cách tự động.

### Dùng các mẫu Kubernetes thay vì phát minh lại chúng

Kubernetes thưởng cho các đội áp dụng mẫu đã thiết lập của nó, và trừng phạt những đội chống lại mô hình của nó. Hãy dùng manifest khai báo cho trạng thái mong muốn. Thêm đầu dò sức khỏe để nền tảng phát hiện và thay thế thể hiện không khỏe. Đặt yêu cầu và giới hạn tài nguyên để bộ lập lịch đóng gói khối lượng công việc an toàn. Dùng co giãn ngang tự động cho nhu cầu đàn hồi. Với logic vận hành phải chạy liên tục, như quản lý một cơ sở dữ liệu, xoay vòng chứng chỉ, hay đối chiếu tài nguyên tùy chỉnh, hãy dùng mẫu toán tử (operator), mã hóa tri thức vận hành của con người vào phần mềm theo dõi trạng thái và hành động. Chống lại thôi thúc xây điều phối đặt riêng trên nền tảng. Ưu tiên các cấu trúc gốc.

### Thiết kế đa người thuê có chủ đích

Khi nhiều đội chia sẻ một cụm, cô lập là yêu cầu bảo mật và độ tin cậy, không phải điều dễ chịu. Hãy dùng không gian tên làm ranh giới người thuê. Thực thi hạn ngạch tài nguyên để không người thuê nào bỏ đói người khác. Áp dụng chính sách mạng để giới hạn lưu lượng ở những gì được cho phép tường minh. Dùng [kiểm soát truy cập dựa trên vai trò](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) để giới hạn mỗi đội làm được gì. Với khối lượng công việc có nhu cầu cô lập mạnh hơn, hãy cân nhắc cụm riêng hoặc hộp cát mạnh hơn. Hãy quyết định sớm mô hình của bạn là đa người thuê mềm (đội nội bộ đáng tin) hay đa người thuê cứng (khối lượng công việc không tin nhau), vì hai loại đòi hỏi kiểm soát rất khác nhau.

### Xây cloud-native, mười hai yếu tố và hơn thế

Phương pháp luận mười hai yếu tố, với phụ thuộc tường minh, cấu hình trong môi trường, tiến trình không trạng thái, tính dùng một lần, v.v., vẫn là đường cơ sở tuyệt vời cho các dịch vụ phát triển tốt trên nền tảng động. Hãy mở rộng nó cho thực tế thêm của hệ phân tích. Thiết kế cho thất bại một phần. Làm thao tác lũy đẳng và thử lại được. Phơi sức khỏe và đo từ xa. Coi khả năng quan sát là tính năng tích hợp thay vì phụ kiện. Đưa mọi trạng thái ra dịch vụ dữ liệu được quản lý, để các thể hiện ứng dụng vẫn dùng một lần và co giãn ngang.

### Lập kế hoạch đa đám mây, lai và chủ quyền một cách thực dụng

Tính di động có giá trị, nhưng hãy theo đuổi nó với mắt tỉnh táo. Chuẩn hóa trên các trừu tượng di động như container, Kubernetes và API mở, để khối lượng công việc có thể di chuyển nếu cần. Nhưng tránh cái bẫy từ chối mọi dịch vụ được quản lý, đổi năng suất thực lấy tính di động giả định. Với yêu cầu lai và chủ quyền, hãy thiết kế để cùng khối lượng công việc và đường ống chạy được ở một khu vực được chọn, một trung tâm dữ liệu riêng, hay một đám mây chủ quyền đáp ứng quy tắc pháp lý và cư trú dữ liệu. Làm ranh giới chủ quyền và cư trú tường minh trong kiến trúc và chính sách.

### Làm chi phí hiển thị với FinOps

Trong môi trường đám mây đàn hồi, chi phí là hệ quả trực tiếp của quyết định kỹ thuật, nên hãy trao cho kỹ sư khả năng nhìn thấy và trách nhiệm. Gắn thẻ tài nguyên để phân bổ chi phí. Quy chi tiêu cho các đội và dịch vụ. Hiển thị dữ liệu chi phí cạnh các chỉ số hiệu năng. Chọn kích thước vừa cho khối lượng công việc, dùng co giãn tự động để khớp nhu cầu, và thu hồi tài nguyên nhàn rỗi. Thiết lập một thực hành FinOps đưa kỹ thuật, tài chính và sản phẩm lại với nhau, để chi tiêu đám mây thành trách nhiệm chung, liên tục thay vì bất ngờ hằng quý.

## Đánh đổi: ưu và nhược điểm

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp nhất |
|---|---|---|---|
| Kubernetes | Mạnh, di động, hệ sinh thái khổng lồ | Phức tạp dốc; gánh nặng vận hành | Nhiều dịch vụ ở quy mô |
| Dịch vụ container được quản lý | Ít gánh nặng vận hành; khởi đầu nhanh hơn | Một ít khóa chặt; kiểm soát ít hơn | Đội muốn sự đơn giản |
| Một cụm dùng chung | Sử dụng tài nguyên hiệu quả | Cô lập khó hơn; bán kính ảnh hưởng | Người thuê nội bộ đáng tin |
| Một cụm cho mỗi người thuê | Cô lập mạnh | Chi phí và chi phí chung cao hơn | Khối lượng công việc không tin nhau hoặc chịu quy định |
| Tính di động đa đám mây | Linh hoạt; tránh khóa chặt | Dịch vụ mẫu số chung thấp nhất | Giảm thiểu rủi ro chiến lược |
| Dịch vụ được quản lý sâu trên một đám mây | Năng suất tối đa | Phụ thuộc nhà cung cấp | Đội chú trọng tốc độ |

Đánh đổi bao trùm là năng lực so với độ phức tạp. Kubernetes và kiến trúc cloud-native mang lại tính đàn hồi, khả năng phục hồi và vận tốc. Nhưng chúng áp đặt gánh nặng vận hành và nhận thức đáng kể mà các đội nhỏ thường xuyên đánh giá thấp. Tương tự, theo đuổi tính di động [đa đám mây](https://en.wikipedia.org/wiki/Multicloud) đầy đủ đánh đổi năng suất lấy lựa chọn. Câu trả lời đúng phụ thuộc vào quy mô và rủi ro. Các tổ chức lớn với nhiều đội và nhu cầu quản trị mạnh thường biện minh được khoản đầu tư. Các nỗ lực nhỏ hơn thường được phục vụ tốt hơn bởi dịch vụ được quản lý giấu độ phức tạp.

## Câu hỏi để thảo luận với đội của bạn

1. **Bạn có ký ảnh và xác minh chữ ký lúc triển khai không, và một lỗ hổng nghiêm trọng có thực sự chặn bản dựng không?** Ảnh là đơn vị lòng tin của bạn, nên chuỗi cung ứng quanh nó xứng đáng có cổng cứng, không phải cảnh báo. Hãy quyết định liệu chỉ ảnh đã ký, đã xác minh mới chạy được, liệu quét chặn phát hiện nghiêm trọng hay chỉ ghi nhật ký, và ai bảo trì registry được chọn lọc gồm ảnh nền đã gia cố mà các đội dựng từ đó. Với khối lượng công việc doanh nghiệp và chính phủ điều này thường là yêu cầu tuân thủ, và nó cũng là phòng thủ tốt nhất của bạn chống một phụ thuộc bị đầu độc đến môi trường sản xuất. Hãy mang trạng thái hiện tại: phần ảnh đang chạy đến từ nền đã gia cố của bạn, bao nhiêu mang CVE nghiêm trọng chưa vá, và liệu có ảnh chưa ký nào hiện lập lịch được. Nếu một phát hiện nghiêm trọng không dừng một lần triển khai, bộ quét của bạn chỉ là đồ trang trí.

2. **Yêu cầu, giới hạn và hạn ngạch tài nguyên ngăn một khối lượng công việc bỏ đói hàng xóm thế nào, mà không để năng lực đắt tiền nhàn rỗi?** Trên một cụm dùng chung, một khối lượng công việc không có giới hạn có thể làm sập hoặc làm nghẽn mọi thứ xung quanh, và hạn ngạch đặt quá rộng lãng phí lợi ích sử dụng biện minh cho nền tảng. Hãy quyết định mặc định hợp lý, ai điều chỉnh chúng, và bạn bắt khối lượng công việc không đặt yêu cầu nào thế nào. Ở quy mô đây vừa là kiểm soát độ tin cậy vừa là kiểm soát chi phí, vì chọn kích thước vừa là nơi phần lớn khoản tiết kiệm FinOps nằm. Hãy mang dữ liệu: mức sử dụng cụm hiện tại, khối lượng công việc bị trục xuất hay làm nghẽn bao lâu một lần, và không gian tên nào không có hạn ngạch. Mục tiêu là đóng gói dày, an toàn, nên hãy coi giới hạn bị thiếu là khiếm khuyết mà nền tảng từ chối.

3. **Trạng thái nào được phép sống bên trong container, và mọi thứ khác đi đâu?** Khả năng phục hồi cloud-native phụ thuộc vào các thể hiện dùng một lần mà nền tảng lập lịch lại tùy ý, và điều đó chỉ đúng nếu trạng thái quan trọng sống trong dịch vụ dữ liệu được quản lý thay vì trên đĩa cục bộ của container. Hãy quyết định quy tắc tường minh, vì trạng thái lưu trong container do tai nạn thành mất dữ liệu ở lần lập lịch lại kế tiếp. Với các đội di chuyển ứng dụng cũ đây thường là phần khó nhất, vì dịch vụ cũ giả định một hệ thống tệp cục bộ ổn định. Hãy mang một bản kiểm kê: dịch vụ nào ghi trạng thái cục bộ, cái nào dựa vào phiên dính hay ái lực nút, và cần gì để đưa mỗi cái ra ngoài. Cho đến khi trạng thái ở ngoài, bạn có container trông đàn hồi nhưng không thực sự di chuyển được.

4. **Khi nhiều đội chia sẻ một cụm, mô hình cô lập của bạn có được chọn có chủ đích là đa người thuê mềm hay cứng không, và các kiểm soát có khớp với lựa chọn đó không?** Không gian tên tách các đội nội bộ đáng tin, nhưng chúng không chứa nổi một khối lượng công việc thù địch hay bị xâm phạm tích cực, và coi người thuê mềm như cứng là sự cố bảo mật đang chờ. Hãy quyết định theo từng khối lượng công việc liệu người thuê chỉ cần chia sẻ công bằng hay phải được giả định không tin nhau, rồi khớp kiểm soát: không gian tên, hạn ngạch, chính sách mạng và RBAC cho trường hợp mềm, cụm riêng hoặc hộp cát mạnh hơn cho trường hợp cứng. Với một tổ chức lớn quyết định này thúc đẩy chi phí trực tiếp, vì một cụm cho mỗi người thuê đắt hơn nhiều so với không gian tên dùng chung, nên bạn muốn chỉ tiêu ngân sách cô lập nơi mô hình mối đe dọa đòi hỏi. Hãy mang bản kiểm kê người thuê: khối lượng công việc nào hôm nay chia sẻ một cụm, cái nào xử lý lưu lượng chịu quy định hoặc hướng bên ngoài, và chính sách mạng vẫn mặc định cho phép ở đâu. Trong bối cảnh doanh nghiệp và chính phủ, trộn khối lượng công việc không tin nhau dưới đa người thuê mềm chính là phát hiện kiểm toán viên sẽ gắn cờ, nên hãy nêu ranh giới trước khi họ làm.

5. **Bạn đang trả bao nhiêu cho tính di động đa đám mây, và bạn có bao giờ thực sự dùng nó không?** Chuẩn hóa trên container, Kubernetes và API mở giữ khối lượng công việc di chuyển được, nhưng từ chối mọi dịch vụ được quản lý để bảo toàn lựa chọn đó đánh đổi năng suất hằng ngày thực lấy tính di động mà tổ chức có thể không bao giờ dùng. Hãy quyết định nơi tính di động là yêu cầu đích thực, như nghĩa vụ chủ quyền hay lối thoát bạn đã ký, so với nơi nó là tấm chăn an ủi làm chậm mọi đội. Cân nhắc đối lập là tốc độ: dịch vụ được quản lý sâu phát hành tính năng nhanh hơn, và kiến trúc mẫu số chung thấp nhất là khoản thuế thường trực trên mọi đội. Hãy mang bằng chứng: dịch vụ được quản lý nào bạn đã tránh và điều đó tốn bao nhiêu thời gian kỹ thuật, bạn đã bao giờ chuyển khối lượng công việc giữa các nhà cung cấp chưa, và hợp đồng của bạn thực sự bắt buộc gì. Với các tổ chức chính phủ và chịu quy định áp dụng, quy tắc cư trú dữ liệu và đám mây chủ quyền có thể khiến tính di động không thể thương lượng, nên hãy thiết kế để cùng manifest và đường ống chạy ở khu vực chủ quyền và vùng riêng, nhưng trung thực rằng đó là chi phí tuân thủ chứ không phải bảo hiểm miễn phí.

6. **Mỗi đội có thấy mình chi bao nhiêu không, và có ai sở hữu hóa đơn trước khi nó thành bất ngờ không?** Trong một nền tảng đàn hồi, chi phí là đầu ra trực tiếp của quyết định kỹ thuật, vậy mà không có thẻ phân bổ chi phí và bảng điều khiển hiển thị, chi tiêu tích tụ vào một bể chung mà không ai thấy có trách nhiệm cho đến khi tài chính leo thang. Hãy quyết định bạn quy chi phí cho đội và dịch vụ thế nào, ai rà soát nó, và kỹ sư có thấy chi phí cạnh chỉ số hiệu năng hay chỉ nghe về nó mỗi quý. Căng thẳng là giữa trách nhiệm giải trình và ma sát: ép chi phí quá mạnh và mọi quyết định thành một cuộc thương lượng ngân sách, bỏ qua nó và khối lượng công việc nhàn rỗi, quá khổ lặng lẽ cộng dồn. Hãy mang các con số: chi tiêu hiện tại theo đội, bao nhiêu năng lực nhàn rỗi hoặc quá khổ, và một khối lượng công việc chạy mất kiểm soát sẽ được phát hiện nhanh đến đâu. Với ngân sách doanh nghiệp và chính phủ, chi tiêu đám mây không được quy chủ vừa là thất bại quản trị vừa là rủi ro tài chính thật, nên hãy dựng một thực hành FinOps đặt kỹ thuật, tài chính và sản phẩm vào cùng một cuộc trò chuyện thay vì đối chiếu sau sự việc.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Hãy với tới một dịch vụ container được quản lý thay vì cụm Kubernetes tự lưu trữ: với một vài dịch vụ và không có kỹ sư nền tảng, mặt phẳng điều khiển là sự phân tâm bạn không gánh nổi. Đóng gói ảnh nhỏ từ nền tối thiểu, ghim phiên bản, thêm một lần quét lỗ hổng vào bản dựng, và đẩy mọi trạng thái vào cơ sở dữ liệu được quản lý để các thể hiện vẫn dùng một lần. Bỏ qua không gian tên, toán tử và tính di động đa đám mây cho đến khi bạn thực sự có dịch vụ và con người để biện minh.

**Doanh nghiệp nhỏ.** Không có chuyên gia nền tảng riêng và ngân sách eo hẹp, hãy dựa mạnh vào dịch vụ được quản lý và để nhà cung cấp chạy điều phối mà bạn sẽ phải bố trí nhân sự. Coi nền tảng container là sàn bảo mật của bạn: ảnh tối thiểu, ghim phiên bản và một lần quét trong đường ống cho phần lớn sự bảo vệ với ít công sức. Ưu tiên mua một nền tảng được hỗ trợ hơn xây một cái, và giữ đủ tính di động, container chuẩn và API mở, để bạn không bị kẹt nếu giá hay điều khoản thay đổi.

**Doanh nghiệp lớn.** Nhiệm vụ là quản trị nền tảng qua nhiều đội: một đội nền tảng trung tâm cung cấp ảnh nền đã gia cố, cổng ký và quét, người thuê theo không gian tên với hạn ngạch, chính sách mạng và RBAC, cộng thẻ phân bổ chi phí và bảng điều khiển FinOps. Chuẩn hóa hợp đồng triển khai để hàng trăm dịch vụ vận hành giống nhau, và quản lý bảo mật, đa người thuê và chi phí tập trung trong khi các đội tự phục vụ triển khai. Hãy tài trợ đội nền tảng đúng mức, vì một nền tảng thiếu nguồn lực trở thành nút thắt mà cả tổ chức chờ đợi.

**Chính phủ.** Chủ quyền, cư trú dữ liệu và trách nhiệm giải trình công định hình kiến trúc. Hãy chạy khối lượng công việc trên container và Kubernetes chuẩn để cùng đường ống chạy ở khu vực chủ quyền và vùng tại chỗ đã kiểm định, và mã hóa ranh giới cư trú và truy cập thành chính sách thay vì quy ước. Lấy ảnh từ registry nội bộ đã gia cố, áp dụng đa người thuê cứng cho dữ liệu nhạy cảm nhất, và giữ tính di động mang lại khả năng phục hồi và đòn bẩy thương lượng, vì quy tắc mua sắm thường cấm khóa chặt nhà cung cấp duy nhất.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp sáu người đóng gói hai dịch vụ của mình thành ảnh container nhỏ dựng từ nền tối thiểu, và chạy chúng trên dịch vụ container được quản lý thay vì cụm Kubernetes tự lưu trữ, nên không ai phải trông nom mặt phẳng điều khiển. Họ ghim phiên bản ảnh nền và thêm quét lỗ hổng vào bản dựng, nhưng cố ý bỏ qua các tính năng điều phối nặng hơn cho đến khi họ thực sự có hơn một nhúm dịch vụ. Trạng thái sống trong một cơ sở dữ liệu Postgres được quản lý, giữ container dùng một lần và cho phép nền tảng khởi động lại hoặc co giãn chúng mà không mất dữ liệu.

**Doanh nghiệp lớn.** Một công ty viễn thông chạy vài trăm [vi dịch vụ](https://en.wikipedia.org/wiki/Microservices) trên các cụm Kubernetes dùng chung. Một đội nền tảng cung cấp ảnh nền đã gia cố, thực thi ký ảnh và cổng lỗ hổng, và cô lập các đơn vị kinh doanh vào không gian tên với hạn ngạch, chính sách mạng và RBAC. Thẻ phân bổ chi phí và bảng điều khiển FinOps quy chi tiêu cho từng dòng sản phẩm, và co giãn tự động chọn kích thước vừa cho năng lực theo nhu cầu. Các đội sản phẩm triển khai hàng chục lần một ngày lên một nền tảng nhất quán mà không quản lý máy chủ. Công ty giữ kiểm soát trung tâm về bảo mật và chi phí.

**Chính phủ.** Một cơ quan y tế quốc gia phải giữ dữ liệu công dân trong biên giới quốc gia và dưới sự kiểm soát pháp lý quốc gia. Nó chạy khối lượng công việc trên một khu vực đám mây chủ quyền dùng container và Kubernetes chuẩn, để cùng đường ống và manifest cũng chạy trong môi trường tại chỗ đã kiểm định cho dữ liệu nhạy cảm nhất. Ranh giới cư trú dữ liệu và truy cập được mã hóa thành chính sách, ảnh được lấy từ registry nội bộ đã gia cố, và đa người thuê cứng cô lập khối lượng công việc nhạy cảm. Tính di động qua khu vực chủ quyền và vùng riêng cho cơ quan khả năng phục hồi và đòn bẩy thương lượng mà không hy sinh tuân thủ.

## Luận chứng kinh doanh: động lực, ROI và TCO

ROI của container và điều phối đến từ mức sử dụng tài nguyên cao hơn, triển khai nhanh hơn và đáng tin hơn, co giãn đàn hồi khớp chi tiêu với nhu cầu, và khả năng phục hồi được cải thiện qua tự phục hồi. Chuẩn hóa trên một nền tảng chung giảm công sức trùng lặp qua các đội và tăng tốc làm quen, vì mọi dịch vụ theo cùng hợp đồng triển khai và vận hành.

Phân tích TCO phải trung thực về gánh nặng vận hành. Chi phí áp dụng gồm nhân sự kỹ thuật nền tảng, đào tạo, công cụ bảo mật cho ảnh và cụm, và công sức liên tục của việc chạy chính nền tảng. Chi phí của việc không áp dụng gồm triển khai đặt riêng không nhất quán qua các đội, sử dụng kém hạ tầng đắt tiền, co giãn thủ công giòn, và khó khăn đáp ứng yêu cầu phục hồi và chủ quyền. Với ban lãnh đạo, lập luận dựa vào quy mô. Dưới một số dịch vụ nhất định độ phức tạp có thể không đáng, và một dịch vụ được quản lý khôn ngoan hơn. Nhưng ở quy mô doanh nghiệp và chính phủ, một nền tảng cloud-native được quản trị thường là nền tảng tiết kiệm chi phí và phục hồi nhất, miễn là bạn tài trợ đội nền tảng để chạy nó đúng cách.

## Phản mẫu và cạm bẫy

- **Ảnh béo, chưa quét.** Ảnh phình dựng từ nền không đáng tin mang lỗ hổng không cần thiết và làm mọi thứ chậm.
- **Kubernetes cho mọi thứ.** Áp dụng bộ điều phối phức tạp cho một nhúm dịch vụ đơn giản mua độ phức tạp mà không có lợi.
- **Phớt lờ giới hạn tài nguyên.** Không có yêu cầu và giới hạn, một khối lượng công việc có thể bỏ đói hoặc làm sập hàng xóm.
- **Người thuê mềm cho khối lượng công việc thù địch.** Chỉ dựa vào không gian tên để cô lập người thuê không tin nhau là sự cố bảo mật đang chờ.
- **Container có trạng thái do tai nạn.** Lưu trạng thái quan trọng trong container dùng một lần dẫn đến mất dữ liệu khi lập lịch lại.
- **Mù chi phí.** Coi chi tiêu đám mây là chi phí chung cố định thay vì đầu ra kỹ thuật dẫn đến hóa đơn mất kiểm soát.
- **Sân khấu di động.** Từ chối mọi dịch vụ được quản lý để giữ tính di động mà tổ chức sẽ không bao giờ thực sự dùng.

## Mô hình trưởng thành

**Mức 1: Khởi đầu.** Container được dùng tùy nghi, nếu có. Ảnh dựng bằng tay và chưa quét, triển khai thủ công và phản ứng, và không có nền tảng dùng chung, khả năng nhìn thấy chi phí hay mô hình cô lập.

**Mức 2: Phát triển.** Các đội container hóa ứng dụng và áp dụng bộ điều phối, nhưng thực hành khác nhau giữa các nhóm. Quét ảnh, giới hạn tài nguyên và ký không nhất quán, và chi phí cùng đa người thuê không được quản trị có hệ thống.

**Mức 3: Chuẩn hóa.** Một nền tảng chuẩn hóa được lập tài liệu và thực thi toàn tổ chức: ảnh nền đã gia cố, cổng ký và quét, người thuê theo không gian tên với hạn ngạch và chính sách mạng, RBAC, và phân bổ chi phí. Mẫu cloud-native và mười hai yếu tố là chuẩn mực kỳ vọng thay vì lựa chọn cục bộ.

**Mức 4: Quản lý.** Nền tảng được đo và kiểm soát theo đường cơ sở. Bạn theo dõi mức sử dụng cụm, phần ảnh đang chạy dựng từ nền đã gia cố, lỗ hổng nghiêm trọng chưa vá, tần suất triển khai và tỷ lệ thay đổi thất bại, tỷ lệ trục xuất và làm nghẽn, và chi phí theo đội và dịch vụ so với ngân sách. Cổng được thực thi dựa trên bằng chứng này: giới hạn tài nguyên bị thiếu và ảnh chưa ký bị từ chối tự động, và lệch khỏi tiêu chuẩn kích hoạt hành động thay vì cảnh báo.

**Mức 5: Điều phối.** Nền tảng tự phục vụ và tự phục hồi, được tích hợp trong toàn tổ chức và thích ứng. FinOps liên tục chọn kích thước vừa và thu hồi năng lực, kiến trúc di động hỗ trợ yêu cầu lai và chủ quyền, và nền tảng cải thiện liên tục từ cách dùng đo được, cho nghỉ hưu và thay thế thành phần khi khối lượng công việc, chi phí và bức tranh rủi ro dịch chuyển.

## Ý tưởng để thảo luận

- Ở quy mô nào việc áp dụng Kubernetes thôi là độ phức tạp vì chính nó và bắt đầu sinh lời?
- Ranh giới đúng giữa đa người thuê mềm và cứng cho khối lượng công việc của bạn nằm ở đâu?
- Bạn nên đầu tư bao nhiêu vào tính di động đa đám mây so với năng suất của dịch vụ được quản lý sâu?
- Làm sao bạn trao cho kỹ sư trách nhiệm chi phí thực mà không biến mọi quyết định thành thương lượng ngân sách?
- Mô hình quản trị của bạn cho ảnh nền là gì, và ai bảo trì registry đã gia cố?
- Yêu cầu chủ quyền và cư trú dữ liệu định hình kiến trúc nền tảng của bạn thế nào?

## Những điểm cần ghi nhớ

- Container chuẩn hóa đóng gói và thời gian chạy; điều phối chuẩn hóa vận hành ở quy mô.
- Vệ sinh ảnh, nghĩa là ảnh tối thiểu, ghim, quét, ký, là bảo mật nền tảng.
- Dùng mẫu Kubernetes gốc và toán tử thay vì xây điều phối đặt riêng.
- Chọn mô hình đa người thuê có chủ đích dựa trên mức độ khối lượng công việc tin nhau.
- Theo mười hai yếu tố và mở rộng nó cho thực tế hệ phân tán như thất bại một phần và khả năng quan sát.
- Coi chi phí là đầu ra kỹ thuật và quản lý nó liên tục qua FinOps.

## Tài liệu tham khảo và đọc thêm

- Adam Wiggins, *The Twelve-Factor App* (phương pháp luận).
- Brendan Burns, Joe Beda và Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam và Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment và Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), định nghĩa cloud-native và bức tranh toàn cảnh.
