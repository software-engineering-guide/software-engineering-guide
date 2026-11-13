# 12.2 Danh sách kiểm tra

Các danh sách kiểm tra này là tham chiếu nhanh thực tế, dùng ngay. Hãy sao chép bất kỳ danh sách nào vào mẫu pull request, trang wiki, phiếu, hay chương trình họp rà soát, và điều chỉnh các mục cho khớp ngữ cảnh của bạn. Hãy coi mỗi mục là thứ một người có thể xác minh và trả lời có hoặc không. Một danh sách kiểm tra là công cụ nhớ và tiêu chuẩn chung, không phải thứ thay thế phán đoán; hãy xóa các mục không áp dụng và thêm các mục mà lĩnh vực của bạn đòi hỏi.

Hướng dẫn để dùng chúng tốt:

- Giữ danh sách kiểm tra đủ ngắn để mọi người thực sự hoàn tất. Nếu một danh sách thường xuyên bị bỏ qua, nó quá dài hoặc quá chung chung.
- Tự động hóa bất kỳ mục nào máy xác minh được (định dạng, kiểm thử, quét) để con người dành sự chú ý cho các mục cần phán đoán.
- Đánh phiên bản danh sách kiểm tra của bạn và rà soát định kỳ. Một danh sách không bao giờ đổi có lẽ không được dùng.
- Phân biệt mục chặn với mục khuyến nghị khi sự phân biệt quan trọng với quy trình của bạn.

## Danh sách kiểm tra rà soát mã

Dành cho người rà soát đang xem xét thay đổi của người khác.

- [ ] Thay đổi làm đúng điều mô tả và phiếu liên kết của nó nói.
- [ ] Phạm vi tập trung vào một mối quan tâm logic duy nhất; thay đổi không liên quan được tách ra.
- [ ] Thiết kế khớp kiến trúc hiện có và không đưa vào một ghép nối dễ tránh hơn.
- [ ] Trường hợp biên, đường lỗi và kiểu thất bại được xử lý, không chỉ con đường suôn sẻ.
- [ ] Kiểm thử tồn tại, có ý nghĩa, và sẽ thất bại nếu hành vi thoái lui.
- [ ] Cách đặt tên, cấu trúc và chú thích làm mã dễ hiểu với người đọc tương lai.
- [ ] Không có bí mật, thông tin xác thực, token hay dữ liệu cá nhân nào được commit.
- [ ] Đầu vào nhạy cảm bảo mật được xác thực, mã hóa hoặc tham số hóa phù hợp.
- [ ] Giao diện công khai, hợp đồng và khả năng tương thích ngược được bảo toàn hoặc được đánh phiên bản có chủ đích.
- [ ] Ghi nhật ký, chỉ số và báo cáo lỗi đủ để vận hành thay đổi trong sản xuất.
- [ ] Tài liệu, sổ tay vận hành và cấu hình được cập nhật khớp với thay đổi.
- [ ] Phản hồi được tách thành vấn đề chặn so với gợi ý, và diễn đạt về mã.

## Danh sách kiểm tra cho tác giả pull request

Dành cho tác giả trước khi yêu cầu rà soát.

- [ ] PR đủ nhỏ và tập trung để rà soát cẩn thận trong một lần ngồi.
- [ ] Mô tả nêu cái gì đã đổi, vì sao, và nó được xác minh thế nào.
- [ ] Phiếu, vấn đề hay tài liệu thiết kế liên kết cho người rà soát ngữ cảnh cần thiết.
- [ ] Mọi kiểm tra tự động đạt cục bộ hoặc trong CI (dựng, lint, định dạng, kiểm thử, quét).
- [ ] Hành vi mới và đã đổi được kiểm thử bao phủ.
- [ ] Tái cấu trúc cơ học được tách khỏi thay đổi hành vi.
- [ ] Tự rà soát hoàn tất: bạn đã đọc diff của chính mình từng dòng.
- [ ] Không còn mã gỡ lỗi, khối bị chú thích, bí mật hay tệp lạc.
- [ ] Di chuyển cơ sở dữ liệu, cờ tính năng và thay đổi cấu hình được lập tài liệu và đảo ngược được.
- [ ] Thay đổi gây vỡ được nêu rõ kèm con đường di chuyển.
- [ ] Ảnh chụp màn hình, bản ghi hay đầu ra mẫu được kèm nơi chúng hỗ trợ rà soát.
- [ ] Người rà soát đúng và mọi người phê duyệt theo vai trò bắt buộc được yêu cầu.

## Định nghĩa Hoàn thành

Tiêu chuẩn chung một mục công việc phải đáp ứng trước khi được coi là hoàn tất.

- [ ] Mọi tiêu chí chấp nhận trong phiếu đều đạt và trình diễn được.
- [ ] Mã được đồng nghiệp rà soát và được người rà soát bắt buộc phê duyệt.
- [ ] Kiểm thử tự động được viết, đạt, và hợp nhất cùng thay đổi.
- [ ] Mã được hợp nhất vào nhánh chính và triển khai sạch qua quy trình.
- [ ] Không còn lỗi đã biết ở ngưỡng nghiêm trọng đã thống nhất còn mở.
- [ ] Tài liệu, văn bản trợ giúp và sổ tay vận hành được cập nhật.
- [ ] Khả năng quan sát có sẵn: nhật ký, chỉ số và cảnh báo liên quan tồn tại.
- [ ] Hệ quả về bảo mật và riêng tư đã được xem xét và giải quyết.
- [ ] Yêu cầu tiếp cận cho thay đổi được đáp ứng nơi hướng người dùng.
- [ ] Cờ tính năng được cấu hình và kế hoạch tung ra được thống nhất.
- [ ] Chủ sở hữu sản phẩm hay bên liên quan đã chấp nhận kết quả.
- [ ] Mọi công việc tiếp theo được ghi thành phiếu được theo dõi, không để ngầm.

## Sẵn sàng ra mắt / vận hành sản xuất

Trước khi phát hành một thay đổi đáng kể hoặc dịch vụ mới lên sản xuất.

- [ ] Kế hoạch tung ra được lập tài liệu, gồm các bước theo giai đoạn hoặc canary và tiêu chí thành công.
- [ ] Kế hoạch hoàn tác được lập tài liệu, kiểm thử, và thực hiện được nhanh.
- [ ] Kiểm thử năng lực và tải cho thấy hệ thống đáp ứng nhu cầu kỳ vọng và đỉnh.
- [ ] Giám sát, bảng điều khiển và cảnh báo đang chạy và được xác thực trước khi ra mắt.
- [ ] Bao phủ trực ca được lên lịch và người ứng phó biết hệ thống.
- [ ] Sổ tay vận hành tồn tại cho các kịch bản thất bại và vận hành có khả năng nhất.
- [ ] Phụ thuộc, tích hợp và bên thứ ba được xác nhận sẵn sàng và giới hạn tốc độ được hiểu.
- [ ] Rà soát bảo mật và các ký duyệt bắt buộc hoàn tất.
- [ ] Di chuyển dữ liệu, nếu có, được kiểm thử đầu-cuối với phương án lùi đã xác minh.
- [ ] Cờ tính năng cho phép tắt thay đổi mà không triển khai lại.
- [ ] Phê duyệt pháp lý, riêng tư và tuân thủ được thu thập nơi cần.
- [ ] Kế hoạch truyền thông bao quát các bên liên quan, hỗ trợ và khách hàng.
- [ ] Quyết định tiếp tục/dừng được đưa ra bởi chủ sở hữu có tên theo tiêu chí tường minh.

## Danh sách kiểm tra rà soát bảo mật / mô hình hóa mối đe dọa

Để đánh giá tư thế bảo mật của một thay đổi hay hệ thống.

- [ ] Ranh giới tin cậy và luồng dữ liệu được xác định và lập tài liệu.
- [ ] Xác thực được thực thi ở mọi điểm vào đòi nó.
- [ ] Kiểm tra ủy quyền thực thi đặc quyền tối thiểu cho mọi hành động và tài nguyên.
- [ ] Mọi đầu vào bên ngoài được xác thực, và đầu ra được mã hóa cho nơi đến của nó.
- [ ] Bí mật được lưu trong kho được quản lý, không bao giờ trong mã hay cấu hình, và xoay vòng được.
- [ ] Dữ liệu được mã hóa khi truyền và khi lưu như phân loại yêu cầu.
- [ ] Phụ thuộc được quét lỗ hổng đã biết và được giữ cập nhật.
- [ ] Rủi ro tiêm, giải tuần tự hóa và SSRF được giảm thiểu với đầu vào không tin cậy.
- [ ] Sự kiện liên quan bảo mật được ghi nhật ký mà không ghi dữ liệu nhạy cảm.
- [ ] Giới hạn tốc độ, hạn ngạch và bảo vệ chống lạm dụng canh giữ điểm cuối bị phơi.
- [ ] Thông báo lỗi không làm rò rỉ dấu vết ngăn xếp, nội bộ hay chi tiết nhạy cảm.
- [ ] Mối đe dọa xác định qua STRIDE hay tương tự được ghi lại kèm biện pháp giảm thiểu hoặc rủi ro chấp nhận.
- [ ] Kiểm thử bảo mật (SAST, DAST hay kiểm thử xâm nhập) được lên kế hoạch hoặc hoàn tất.

## Danh sách kiểm tra riêng tư và bảo vệ dữ liệu (kiểu DPIA)

Dành cho xử lý liên quan dữ liệu cá nhân hay nhạy cảm.

- [ ] Dữ liệu cá nhân thu thập được kiểm kê, phân loại, và tối thiểu hóa theo nhu cầu.
- [ ] Cơ sở hay thẩm quyền pháp lý cho từng mục đích xử lý được lập tài liệu.
- [ ] Giới hạn mục đích được thực thi: dữ liệu chỉ được dùng cho các mục đích đã nêu.
- [ ] Thời hạn lưu giữ được xác định và việc xóa hay ẩn danh được tự động hóa.
- [ ] Quyền của chủ thể dữ liệu (truy cập, sửa, xóa, di chuyển) có thể được đáp ứng.
- [ ] Sự đồng ý, nơi được dựa vào, được cho một cách tự do, cụ thể, và thu hồi được.
- [ ] Bên thứ ba và bên xử lý bị ràng buộc bởi điều khoản bảo vệ dữ liệu đầy đủ.
- [ ] Chuyển giao xuyên biên giới có cơ chế chuyển giao pháp lý phù hợp.
- [ ] Truy cập dữ liệu cá nhân bị hạn chế, được ghi nhật ký và rà soát.
- [ ] Rủi ro riêng tư với cá nhân được đánh giá và giảm thiểu hoặc leo thang.
- [ ] Quy trình phát hiện và thông báo vi phạm dữ liệu được xác định.
- [ ] Lựa chọn riêng tư theo thiết kế và mặc định được lập tài liệu cho tính năng.
- [ ] Cán bộ bảo vệ dữ liệu hay người rà soát riêng tư đã ký duyệt nơi cần.

## Danh sách kiểm tra khả năng tiếp cận (WCAG)

Dành cho giao diện hướng người dùng, căn chỉnh theo nguyên tắc WCAG.

- [ ] Mọi nội dung tiếp cận và vận hành được chỉ bằng bàn phím.
- [ ] Thứ tự tiêu điểm hợp lý và có chỉ báo tiêu điểm nhìn thấy được.
- [ ] Độ tương phản màu văn bản đạt tỷ lệ mục tiêu (thường 4,5:1 cho văn bản thân).
- [ ] Hình ảnh và nội dung phi văn bản có văn bản thay thế có ý nghĩa.
- [ ] Trường biểu mẫu có nhãn liên kết và thông báo lỗi rõ ràng.
- [ ] Tiêu đề, mốc và cấu trúc được đánh dấu theo ngữ nghĩa.
- [ ] Thành phần tương tác phơi tên, vai trò và trạng thái đúng cho công nghệ hỗ trợ.
- [ ] Nội dung tái bố cục và vẫn dùng được ở mức phóng to 200% và trên màn hình nhỏ.
- [ ] Giới hạn thời gian điều chỉnh được, và nội dung chuyển động hay tự phát có thể tạm dừng.
- [ ] Màu sắc không phải phương tiện duy nhất truyền đạt thông tin.
- [ ] Phương tiện có phụ đề và, nơi cần, bản ghi chép hoặc mô tả âm thanh.
- [ ] Giao diện được kiểm thử bằng trình đọc màn hình và công cụ tiếp cận tự động.

## Danh sách kiểm tra rà soát thiết kế API

Trước khi công bố hoặc thay đổi một API.

- [ ] Cách đặt tên tài nguyên và thao tác nhất quán và khả đoán.
- [ ] Hợp đồng được đặc tả trong lược đồ máy đọc được (ví dụ OpenAPI).
- [ ] Chiến lược phiên bản được xác định và khả năng tương thích ngược được bảo toàn hoặc quản lý.
- [ ] Phân trang, lọc và sắp xếp theo quy ước nhất quán.
- [ ] Phản hồi lỗi dùng cấu trúc, mã và thông báo hành động được nhất quán.
- [ ] Xác thực và ủy quyền được đặc tả cho mọi thao tác.
- [ ] Xác thực đầu vào và giới hạn kích thước được xác định và thực thi.
- [ ] Tính lũy đẳng được xác định cho thao tác nơi kỳ vọng thử lại.
- [ ] Giới hạn tốc độ, hạn ngạch và hành vi bóp được lập tài liệu.
- [ ] Thời gian chờ, thử lại và ngữ nghĩa thất bại rõ ràng với client.
- [ ] Phơi bày dữ liệu nhạy cảm trong phản hồi được tối thiểu hóa và biện minh.
- [ ] Tài liệu gồm ví dụ cho từng thao tác và trường hợp lỗi.
- [ ] Chính sách ngừng hỗ trợ và mốc khai tử được xác định.

## Danh sách kiểm tra rà soát quyết định kiến trúc (ADR)

Để rà soát một hồ sơ quyết định kiến trúc đề xuất.

- [ ] Ngữ cảnh và vấn đề đang giải quyết được nêu rõ.
- [ ] Quyết định được phát biểu không mơ hồ như một lựa chọn duy nhất.
- [ ] Ít nhất hai phương án thực tế được xem xét và so sánh.
- [ ] Hệ quả, cả tích cực lẫn tiêu cực, được lập tài liệu.
- [ ] Tác động phi chức năng (hiệu năng, bảo mật, chi phí, khả năng vận hành) được giải quyết.
- [ ] Quyết định căn chỉnh với nguyên tắc hiện có và ADR trước, hoặc thay thế chúng tường minh.
- [ ] Các đội và bên liên quan bị ảnh hưởng đã được tham vấn.
- [ ] Khả năng đảo ngược và chi phí thay đổi được đánh giá.
- [ ] Giả định và ràng buộc được làm tường minh.
- [ ] Trạng thái (đề xuất, chấp nhận, bị thay thế) được đặt và ghi ngày.
- [ ] Quyết định tìm thấy được và liên kết từ các hệ thống liên quan.
- [ ] Mọi hành động tiếp theo hay di chuyển được ghi thành công việc được theo dõi.

## Danh sách kiểm tra ứng phó sự cố

Trong một sự cố sản xuất đang diễn ra.

- [ ] Tuyên bố sự cố và giao một chỉ huy sự cố duy nhất.
- [ ] Đánh giá và truyền đạt mức nghiêm trọng, phạm vi và tác động khách hàng.
- [ ] Mở một kênh giao tiếp chuyên dụng và hồ sơ sự cố.
- [ ] Giao vai trò rõ ràng: chỉ huy, trưởng truyền thông và trưởng vận hành.
- [ ] Ưu tiên giảm thiểu và khôi phục dịch vụ hơn phân tích nguyên nhân gốc.
- [ ] Đăng cập nhật trạng thái đều đặn cho các bên liên quan theo nhịp đặt sẵn.
- [ ] Ghi dòng thời gian sự kiện, hành động và quyết định khi chúng xảy ra.
- [ ] Leo thang tới người ứng phó hay nhà cung cấp thêm khi cần.
- [ ] Thông báo pháp lý, bảo mật và tuân thủ nếu dữ liệu hay quy định liên quan.
- [ ] Xác minh bản sửa và xác nhận hệ thống đã hoàn toàn phục hồi.
- [ ] Chính thức đóng sự cố và truyền đạt giải quyết.
- [ ] Lên lịch buổi rút kinh nghiệm không đổ lỗi trước khi mọi người tản đi.

## Danh sách kiểm tra rút kinh nghiệm

Dành cho buổi rà soát nhìn lại sau một sự cố.

- [ ] Buổi rà soát không đổ lỗi và tập trung vào hệ thống và yếu tố góp phần.
- [ ] Dòng thời gian thực tế, có dấu thời gian của sự cố được lập tài liệu.
- [ ] Tác động khách hàng và kinh doanh được định lượng (thời lượng, phạm vi, chi phí).
- [ ] Phát hiện được phân tích: vấn đề được nhận ra thế nào và khi nào.
- [ ] Ứng phó được phân tích: cái gì giúp và cái gì làm chậm khôi phục.
- [ ] Nguyên nhân góp phần được xác định, không chỉ một nguyên nhân gốc duy nhất.
- [ ] Điều đã tốt được ghi lại, cũng như điều đã sai.
- [ ] Hành động cụ thể, giao cho chủ sở hữu, và có hạn.
- [ ] Hành động giải quyết phòng ngừa, phát hiện và giảm thiểu.
- [ ] Mục theo dõi được theo dõi đến hoàn thành trong tồn đọng thông thường.
- [ ] Bản rút kinh nghiệm được chia sẻ rộng để người khác học.
- [ ] Mẫu hình hệ thống qua các sự cố được rà soát định kỳ.

## Danh sách kiểm tra sẵn sàng trực ca

Trước khi ai đó nhận một ca trực.

- [ ] Người ứng phó có quyền truy cập vào mọi hệ thống, bảng điều khiển và công cụ họ cần.
- [ ] Cảnh báo đến người ứng phó đáng tin cậy và được kiểm thử.
- [ ] Đường leo thang và liên hệ trực ca phụ được biết và hiện hành.
- [ ] Sổ tay vận hành tồn tại cho cảnh báo phổ biến nhất và nghiêm trọng nhất.
- [ ] Người ứng phó đã hoàn tất làm quen hoặc theo dõi cho các hệ thống này.
- [ ] Thay đổi gần đây, sự cố đang diễn ra và vấn đề đã biết được bàn giao.
- [ ] Ngưỡng cảnh báo được điều chỉnh để tối thiểu hóa nhiễu và cuộc gọi sai.
- [ ] Người ứng phó biết cách tuyên bố sự cố và liên hệ chỉ huy.
- [ ] Truy cập sản xuất khả thi từ môi trường làm việc của người ứng phó.
- [ ] Kênh giao tiếp và liên hệ bên liên quan được lập tài liệu.
- [ ] Lịch trực được công bố và bao phủ không có khoảng trống.
- [ ] Bồi thường, kỳ vọng và giới hạn khối lượng công việc của trực ca rõ ràng.

## Danh sách kiểm tra định nghĩa SLO

Khi định nghĩa mục tiêu mức dịch vụ.

- [ ] Hành trình người dùng hay năng lực mà SLO bảo vệ được xác định rõ.
- [ ] Chỉ báo mức dịch vụ (SLI) được xác định là đại lượng rõ ràng, đo được.
- [ ] SLI được đo từ góc nhìn người dùng nơi có thể.
- [ ] Mục tiêu được đặt ở mức người dùng thực sự cần, không phải 100%.
- [ ] Cửa sổ đo (ví dụ 28 ngày cuốn chiếu) được chỉ định.
- [ ] Ngân sách lỗi suy ra từ mục tiêu được tính và hiểu.
- [ ] Một chính sách xác định điều xảy ra khi ngân sách lỗi cạn.
- [ ] Nguồn dữ liệu cho SLI đáng tin cậy và có gắn công cụ đo.
- [ ] Cảnh báo gắn với tốc độ đốt, không chỉ vi phạm ngưỡng.
- [ ] Chủ sở hữu và bên liên quan đồng ý SLO thực tế và có ý nghĩa.
- [ ] SLO được lập tài liệu và hiển thị trên bảng điều khiển.
- [ ] Có lịch để rà soát và sửa SLO khi dịch vụ tiến hóa.

## Danh sách kiểm tra quy trình CI/CD

Dành cho quy trình tích hợp và phân phối liên tục.

- [ ] Mỗi commit kích hoạt một lần dựng và chạy kiểm thử tự động.
- [ ] Quy trình thất bại nhanh và báo kết quả rõ ràng cho tác giả.
- [ ] Lint, định dạng và phân tích tĩnh chạy tự động.
- [ ] Kiểm thử đơn vị, tích hợp và đầu-cuối liên quan chạy trong quy trình.
- [ ] Quét bảo mật và phụ thuộc chạy ở mỗi bản dựng.
- [ ] Hiện vật dựng được đánh phiên bản, bất biến và lưu trong registry.
- [ ] Bí mật được tiêm an toàn và không bao giờ in trong nhật ký.
- [ ] Triển khai được tự động hóa và lặp lại được qua các môi trường.
- [ ] Chiến lược triển khai (canary, xanh-lục, cuốn chiếu) được xác định và dùng.
- [ ] Hoàn tác được tự động hóa hoặc là một hành động có tài liệu duy nhất.
- [ ] Quyền quy trình theo đặc quyền tối thiểu và kiểm toán được.
- [ ] Cấu hình quy trình được lưu trong quản lý phiên bản dưới dạng mã.
- [ ] Nguồn gốc bản dựng và danh mục vật liệu phần mềm được tạo nơi cần.

## Danh sách kiểm tra rà soát hạ tầng dưới dạng mã

Để rà soát hạ tầng được định nghĩa dưới dạng mã.

- [ ] Thay đổi được diễn đạt hoàn toàn bằng mã và áp dụng qua quy trình.
- [ ] Một đầu ra kế hoạch hay chạy thử được rà soát trước khi áp dụng.
- [ ] Trạng thái được lưu an toàn với khóa để ngăn thay đổi đồng thời.
- [ ] Tài nguyên theo quy ước đặt tên, gắn thẻ và quyền sở hữu.
- [ ] Vai trò và chính sách IAM đặc quyền tối thiểu được dùng, không dùng ký tự đại diện nơi tránh được.
- [ ] Phơi bày mạng được tối thiểu hóa; không truy cập công khai ngoài ý muốn.
- [ ] Bí mật và giá trị nhạy cảm được tham chiếu từ kho, không mã hóa cứng.
- [ ] Mã hóa được bật cho lưu trữ, cơ sở dữ liệu và truyền.
- [ ] Thay đổi lũy đẳng và an toàn để áp dụng lại.
- [ ] Bán kính ảnh hưởng được hiểu; thay đổi phá hủy được nêu rõ.
- [ ] Tác động chi phí của thay đổi được xem xét.
- [ ] Mô-đun tái sử dụng được, có phiên bản và được kiểm thử.
- [ ] Phát hiện trôi có sẵn để bắt thay đổi ngoài luồng.

## Danh sách kiểm tra phát hành mô hình AI/ML

Trước khi phát hành mô hình học máy lên sản xuất.

- [ ] Mục đích sử dụng, phạm vi và giới hạn của mô hình được lập tài liệu.
- [ ] Nguồn gốc, giấy phép và sự đồng ý của dữ liệu huấn luyện và đánh giá được xác minh.
- [ ] Dữ liệu và mô hình được đánh phiên bản và tái tạo được.
- [ ] Hiệu suất được đánh giá trên dữ liệu kiểm thử đại diện, giữ riêng.
- [ ] Công bằng và thiên kiến được đánh giá qua các nhóm con liên quan.
- [ ] Mô hình được đánh giá so với mô hình đương nhiệm hoặc đường cơ sở.
- [ ] Kiểu thất bại, trường hợp biên và hành vi ngoài phân phối được hiểu.
- [ ] Rủi ro an toàn, lạm dụng và đầu ra có hại được đánh giá và giảm thiểu.
- [ ] Giám sát trôi, chất lượng dữ liệu và suy giảm hiệu suất có sẵn.
- [ ] Tồn tại phương án hoàn tác hay quay về mô hình trước hoặc đường dựa trên quy tắc.
- [ ] Giám sát hay kháng nghị của con người được cung cấp cho quyết định có hệ quả.
- [ ] Rà soát riêng tư bao quát dữ liệu huấn luyện và đầu vào, đầu ra suy luận.
- [ ] Thẻ mô hình hay tài liệu tương đương được công bố cho các bên liên quan.

## Danh sách kiểm tra chất lượng quy trình dữ liệu

Dành cho quy trình dữ liệu nuôi phân tích hoặc sản phẩm.

- [ ] Lược đồ dữ liệu nguồn được xác thực và thay đổi lược đồ được phát hiện.
- [ ] Việc nạp xử lý đúng bản ghi muộn, trùng lặp và sai thứ tự.
- [ ] Kiểm tra chất lượng dữ liệu (đầy đủ, duy nhất, khoảng giá trị) chạy tự động.
- [ ] Bản ghi thất bại được cách ly và làm lộ, không bị bỏ im lặng.
- [ ] Phép biến đổi được kiểm thử với đầu vào đại diện và trường hợp biên.
- [ ] Quy trình lũy đẳng và an toàn để chạy lại sau thất bại.
- [ ] Độ mới và độ trễ của đầu ra được giám sát so với kỳ vọng.
- [ ] Phả hệ được lập tài liệu để bên tiêu thụ biết dữ liệu đến từ đâu.
- [ ] Dữ liệu cá nhân và nhạy cảm được phân loại, che giấu hoặc hạn chế phù hợp.
- [ ] Nạp bù và xử lý lại được hỗ trợ và lập tài liệu.
- [ ] Cảnh báo thông báo cho chủ sở hữu về thất bại và vi phạm chất lượng.
- [ ] Chính sách lưu giữ và xóa được thực thi trên dữ liệu đã lưu.
- [ ] Bên tiêu thụ hạ nguồn và SLA được lập tài liệu.

## Danh sách kiểm tra tiếp nhận mã nguồn mở và rà soát giấy phép

Trước khi áp dụng một thành phần mã nguồn mở.

- [ ] Giấy phép của thành phần được xác định và nằm trong danh sách được phê duyệt.
- [ ] Nghĩa vụ giấy phép (ghi công, copyleft, thông báo) được hiểu và đáp ứng.
- [ ] Khả năng tương thích giấy phép với mô hình phân phối của bạn được xác nhận.
- [ ] Dự án được bảo trì tích cực và có cộng đồng lành mạnh.
- [ ] Lỗ hổng đã biết được kiểm tra và phiên bản hiện hành.
- [ ] Phụ thuộc và các phụ thuộc bắc cầu của nó được kiểm kê.
- [ ] Tư thế bảo mật và lịch sử sự cố quá khứ được rà soát.
- [ ] Thành phần đáp ứng nhu cầu thật mà không trùng lặp đáng kể.
- [ ] Chi phí thoát và khả năng thay thế của thành phần được xem xét.
- [ ] Thành phần được ghi trong danh mục vật liệu phần mềm.
- [ ] Một chủ sở hữu có tên chịu trách nhiệm theo dõi cập nhật và khuyến cáo.
- [ ] Chính sách đóng góp ngược và rẽ nhánh nội bộ được tuân theo nếu có sửa đổi.

## Danh sách kiểm tra rủi ro nhà cung cấp / bên thứ ba

Trước khi tiếp nhận nhà cung cấp hay dịch vụ bên ngoài.

- [ ] Nhu cầu kinh doanh và dữ liệu nhà cung cấp sẽ truy cập được xác định rõ.
- [ ] Tư thế bảo mật của nhà cung cấp được đánh giá (chứng nhận, kiểm toán, bảng câu hỏi).
- [ ] Điều khoản xử lý dữ liệu, quyền sở hữu và xóa khi thoát rõ ràng theo hợp đồng.
- [ ] Nhà thầu phụ và vị trí dữ liệu của nhà cung cấp được tiết lộ và chấp nhận được.
- [ ] Tuân thủ quy định liên quan được xác minh.
- [ ] Cam kết thời gian hoạt động, hỗ trợ và SLA được lập tài liệu.
- [ ] Nghĩa vụ và thời hạn thông báo vi phạm nằm trong hợp đồng.
- [ ] Truy cập được giới hạn đặc quyền tối thiểu và thu hồi được.
- [ ] Liên tục kinh doanh và tác động của thất bại nhà cung cấp được đánh giá.
- [ ] Kế hoạch thoát và di chuyển dữ liệu tồn tại để tránh khóa chặt.
- [ ] Chi phí, điều khoản gia hạn và điều khoản đổi giá được hiểu.
- [ ] Nhà cung cấp được thêm vào sổ đăng ký rủi ro kèm ngày rà soát.

## Danh sách kiểm tra sẵn sàng tuân thủ chính phủ (kiểu ATO / FedRAMP)

Dành cho hệ thống đòi ủy quyền vận hành chính thức.

- [ ] Ranh giới hệ thống và luồng dữ liệu được xác định và vẽ sơ đồ.
- [ ] Dữ liệu được phân loại theo mức tác động và độ nhạy cảm.
- [ ] Đường cơ sở kiểm soát áp dụng được chọn và điều chỉnh.
- [ ] Một kế hoạch bảo mật hệ thống lập tài liệu cách mỗi kiểm soát được triển khai.
- [ ] Kiểm soát được triển khai, chứng minh và ánh xạ tới kế hoạch.
- [ ] Giám sát liên tục và quét lỗ hổng đang vận hành.
- [ ] Kế hoạch hành động và cột mốc theo dõi phát hiện còn mở đến khi khắc phục.
- [ ] Kiểm soát truy cập, ghi nhật ký kiểm toán và quản lý danh tính đáp ứng yêu cầu.
- [ ] Mã hóa dùng thuật toán được phê duyệt và mô-đun đã xác thực.
- [ ] Kế hoạch ứng phó sự cố được lập tài liệu và kiểm thử.
- [ ] Kế hoạch dự phòng và khôi phục thảm họa được lập tài liệu và kiểm thử.
- [ ] Đánh giá hoặc kiểm toán độc lập về kiểm soát hoàn tất.
- [ ] Quan chức ủy quyền có đánh giá rủi ro cần thiết để cấp ủy quyền.
- [ ] Tác nhân tái ủy quyền và nhịp ủy quyền liên tục được xác định.
