# 12.1 Thuật ngữ

Bảng thuật ngữ này định nghĩa các thuật ngữ và từ viết tắt dùng xuyên suốt cẩm nang. Các mục được nhóm theo thứ tự chữ cái của thuật ngữ tiếng Anh. Nơi một mục có từ viết tắt phổ biến, nó được đặt trong ngoặc đơn. Các định nghĩa được cố ý viết ngắn gọn; hãy tham khảo chương liên quan để có phần xử lý đầy đủ hơn.

## A

**[ABAC (Attribute-Based Access Control, Kiểm soát truy cập dựa trên thuộc tính)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: Mô hình ủy quyền cấp quyền truy cập dựa trên các thuộc tính được đánh giá của người dùng, tài nguyên, hành động và môi trường (ví dụ phòng ban, mức thông quan, giờ trong ngày) thay vì vai trò cố định. Nó cho kiểm soát mịn, dẫn dắt bởi chính sách với cái giá là phức tạp hơn RBAC.

**[Accessibility (a11y, Khả năng tiếp cận)](https://en.wikipedia.org/wiki/Computer_accessibility)**: Thực hành thiết kế và xây dựng phần mềm để người khuyết tật có thể nhận thức, hiểu, điều hướng và tương tác với nó. Số-từ "a11y" viết tắt 11 chữ cái giữa "a" và "y."

**ADR (Architecture Decision Record, Hồ sơ quyết định kiến trúc)**: Một tài liệu ngắn, có phiên bản ghi lại một quyết định kiến trúc hay kỹ thuật đáng kể, ngữ cảnh của nó, các phương án đã xem xét, và hệ quả. ADR tạo lịch sử bền vững, rà soát được về vì sao một hệ thống như hiện tại.

**Aggregate (Tập hợp)**: Trong Thiết kế Hướng Miền, một cụm đối tượng miền được coi là một đơn vị duy nhất cho thay đổi dữ liệu, với một thực thể đóng vai gốc tập hợp thực thi các bất biến. Tập hợp xác định ranh giới nhất quán và giao dịch.

**[API (Application Programming Interface, Giao diện lập trình ứng dụng)](https://en.wikipedia.org/wiki/API)**: Một hợp đồng xác định qua đó một phần mềm yêu cầu dịch vụ hay dữ liệu từ phần mềm khác. API được thiết kế tốt giấu chi tiết triển khai và cung cấp giao diện ổn định, có phiên bản.

**API-first (API trước)**: Cách tiếp cận phát triển trong đó hợp đồng API được thiết kế và thống nhất trước khi triển khai, để bên tiêu thụ và bên cung cấp làm việc song song theo một đặc tả chung.

**arc42**: Cấu trúc mở, dựa trên mẫu để lập tài liệu kiến trúc phần mềm, tổ chức thành mười hai mục bao quát ngữ cảnh, ràng buộc, khối xây dựng, thời gian chạy, triển khai và quyết định.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Một đặc tả W3C xác định vai trò, trạng thái và thuộc tính làm các thành phần web động và tùy biến dễ hiểu với công nghệ hỗ trợ như trình đọc màn hình.

**ASR (Architecturally Significant Requirement, Yêu cầu có ý nghĩa kiến trúc)**: Một yêu cầu có tác động đo được, rộng lên kiến trúc, như ràng buộc về hiệu năng, khả dụng, bảo mật hay quy định. ASR thúc đẩy các quyết định thiết kế có hệ quả nhất.

**ASVS (Application Security Verification Standard)**: Một tiêu chuẩn OWASP cung cấp danh sách kiểm tra có bậc về yêu cầu và kiểm thử bảo mật để thiết kế, xây dựng và xác minh ứng dụng an toàn.

**[Autoscaling (Co giãn tự động)](https://en.wikipedia.org/wiki/Autoscaling)**: Việc điều chỉnh tự động số thể hiện tính toán đang chạy (hoặc kích thước của chúng) theo tải, để năng lực bám theo nhu cầu mà không cần can thiệp thủ công. Nó bổ sung, nhưng không thay thế, hoạch định năng lực có chủ đích.

**[Availability (Tính khả dụng)](https://en.wikipedia.org/wiki/Availability)**: Tỷ lệ thời gian một hệ thống hoạt động và phục vụ được yêu cầu, thường được diễn đạt bằng "số chín" (ví dụ 99,9%). Đó là mục tiêu độ tin cậy cốt lõi được mã hóa trong SLO và SLA.

## B

**Backpressure (Áp lực ngược)**: Cơ chế kiểm soát luồng trong đó một thành phần chịu tải báo hiệu cho nhà sản xuất thượng nguồn chậm lại, ngăn hàng đợi không giới hạn và thất bại dây chuyền. Nó trung tâm với hệ thống luồng và hướng thông điệp đáng tin cậy.

**[BDD (Behaviour-Driven Development, Phát triển hướng hành vi)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: Thực hành cộng tác diễn đạt yêu cầu thành các ví dụ hành vi cụ thể, con người đọc được (thường dạng Given/When/Then) đồng thời làm kiểm thử chấp nhận tự động.

**BFF (Backend for Frontend)**: Mẫu kiến trúc trong đó một dịch vụ backend chuyên dụng được xây cho một frontend hay loại client cụ thể, điều chỉnh việc định hình và gộp dữ liệu theo nhu cầu của client đó.

**[BI (Business Intelligence, Trí tuệ kinh doanh)](https://en.wikipedia.org/wiki/Business_intelligence)**: Các công cụ, quy trình và thực hành thu thập, tích hợp và phân tích dữ liệu kinh doanh để hỗ trợ báo cáo, bảng điều khiển và ra quyết định.

**Blameless postmortem (Rút kinh nghiệm không đổ lỗi)**: Một buổi rà soát sự cố tập trung vào nguyên nhân hệ thống và học hỏi thay vì lỗi cá nhân, trên tiền đề rằng mọi người hành động hợp lý theo thông tin và khuyến khích họ có.

**[Blue-green deployment (Triển khai xanh-lục)](https://en.wikipedia.org/wiki/Blue-green_deployment)**: Chiến lược phát hành chạy hai môi trường sản xuất giống hệt ("xanh" và "lục"), định tuyến lưu trữ tới một cái trong khi cái kia được cập nhật, cho phép chuyển và hoàn tác gần như tức thì.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Một hàm xếp hạng được dùng rộng rãi cho tìm kiếm toàn văn, chấm điểm một tài liệu khớp truy vấn đến đâu bằng tần suất thuật ngữ, tần suất tài liệu nghịch đảo và độ dài tài liệu. Đó là mặc định xếp hạng từ vựng của nhiều công cụ tìm kiếm.

**Bounded context (Ngữ cảnh giới hạn)**: Trong Thiết kế Hướng Miền, một ranh giới tường minh trong đó một mô hình miền cụ thể và ngôn ngữ phổ quát của nó áp dụng nhất quán. Nó ngăn các khái niệm bị trộn lẫn qua các phần khác nhau của hệ thống lớn.

**Build cache (Bộ đệm bản dựng)**: Kho lưu các đầu ra bản dựng đã tính trước đó, khóa theo đầu vào tạo ra chúng, để công việc không đổi được tái sử dụng thay vì dựng lại. Bộ đệm bản dựng từ xa dùng chung cho phép cả đội và CI của nó tái sử dụng kết quả của nhau.

**[Bus factor (Hệ số xe buýt)](https://en.wikipedia.org/wiki/Bus_factor)**: Số người phải mất đi (theo nghĩa bóng "bị xe buýt đụng") trước khi một dự án đình trệ vì thiếu tri thức thiết yếu. Hệ số xe buýt thấp báo hiệu chuyên môn tập trung, không có tài liệu và rủi ro tổ chức.

## C

**[Cache eviction policy (Chính sách loại bỏ bộ đệm)](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: Quy tắc bộ đệm dùng để quyết định loại mục nào khi đầy, như ít dùng gần đây nhất (LRU) hay ít dùng thường xuyên nhất (LFU). Chính sách định hình tỷ lệ trúng và, cùng với nó, giá trị của bộ đệm.

**[Cache invalidation (Vô hiệu hóa bộ đệm)](https://en.wikipedia.org/wiki/Cache_invalidation)**: Vấn đề loại bỏ hay cập nhật dữ liệu đệm khi nguồn bên dưới đổi, để người đọc không thấy giá trị cũ. Nó nổi tiếng là một trong những vấn đề khó nhất trong tính toán.

**[Cache stampede (Dồn dập bộ đệm)](https://en.wikipedia.org/wiki/Cache_stampede)**: Kiểu thất bại trong đó nhiều client cùng trượt bộ đệm cho cùng một khóa và đồng loạt đánh vào nguồn gốc, làm nó quá tải. Gộp yêu cầu và hết hạn so le ngăn nó. Còn gọi là thundering herd.

**Canary release (Phát hành canary)**: Kỹ thuật triển khai phơi phiên bản mới cho một tập con nhỏ người dùng hay lưu lượng trước, giám sát vấn đề, rồi mở rộng dần nếu chỉ số vẫn lành mạnh.

**[CAP theorem (Định lý CAP)](https://en.wikipedia.org/wiki/CAP_theorem)**: Nguyên lý nói một kho dữ liệu phân tán chỉ đảm bảo được tối đa hai trong Nhất quán, Khả dụng và Chịu phân vùng cùng lúc; vì phân vùng không tránh được, người thiết kế thực chất đánh đổi nhất quán với khả dụng trong chúng.

**[C4 model (Mô hình C4)](https://en.wikipedia.org/wiki/C4_model)**: Cách tiếp cận nhẹ để trực quan hóa kiến trúc phần mềm ở bốn cấp trừu tượng: Ngữ cảnh Hệ thống, Container, Thành phần và Mã.

**[CD (Continuous Delivery / Continuous Deployment, Phân phối liên tục / Triển khai liên tục)](https://en.wikipedia.org/wiki/Continuous_delivery)**: Phân phối liên tục giữ phần mềm ở trạng thái có thể phát hành để triển khai bất cứ lúc nào với phê duyệt thủ công; Triển khai liên tục tự động phát hành mọi thay đổi vượt qua quy trình.

**[CDN (Content Delivery Network, Mạng phân phối nội dung)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Mạng phân tán địa lý gồm các máy chủ biên đệm và phục vụ nội dung gần người dùng, cắt độ trễ và giảm tải hạ tầng nguồn.

**Chain-of-thought prompting (Gợi ý chuỗi suy nghĩ)**: Kỹ thuật gợi ý yêu cầu mô hình ngôn ngữ đi qua các bước suy luận trung gian trước khi đưa câu trả lời cuối, cải thiện hiệu suất trên bài toán nhiều bước với cái giá là đầu ra dài hơn, chậm hơn.

**[CI (Continuous Integration, Tích hợp liên tục)](https://en.wikipedia.org/wiki/Continuous_integration)**: Thực hành thường xuyên hợp nhất thay đổi của nhà phát triển vào nhánh chính chung, mỗi lần hợp nhất được xác thực bằng bản dựng và bộ kiểm thử tự động để phát hiện vấn đề tích hợp sớm.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Quy trình kết hợp Tích hợp liên tục và Phân phối/Triển khai liên tục tự động hóa việc dựng, kiểm thử và phát hành phần mềm.

**CMMC (Cybersecurity Maturity Model Certification)**: Chương trình của Bộ Quốc phòng Hoa Kỳ chứng nhận mức trưởng thành an ninh mạng của nhà thầu xử lý thông tin hợp đồng liên bang và thông tin không mật được kiểm soát.

**[Cohesion (Tính gắn kết)](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: Mức độ các phần tử bên trong một mô-đun thuộc về nhau và phục vụ một mục đích duy nhất, xác định rõ. Gắn kết cao, ghép với ghép nối thấp, là dấu hiệu của thiết kế bảo trì được.

**Context window (Cửa sổ ngữ cảnh)**: Lượng văn bản tối đa, đo bằng token, mà mô hình ngôn ngữ có thể xét cùng lúc, bao gồm đầu vào và đầu ra. Đó là ngân sách khan hiếm mà thiết kế gợi ý và ngữ cảnh phải quản lý có chủ đích.

**[Conway's Law (Định luật Conway)](https://en.wikipedia.org/wiki/Conway's_law)**: Quan sát rằng cấu trúc của một hệ thống có xu hướng phản chiếu cấu trúc giao tiếp của tổ chức xây nó. "Điều động Conway nghịch" cố ý định hình đội để tạo kiến trúc mong muốn.

**Core Web Vitals**: Tập thước đo hiệu năng web lấy người dùng làm trung tâm do Google định nghĩa (như Largest Contentful Paint, Interaction to Next Paint và Cumulative Layout Shift) đo tải, tương tác và ổn định hình ảnh.

**[Cost of delay (Chi phí trì hoãn)](https://en.wikipedia.org/wiki/Cost_of_delay)**: Chi phí kinh tế của việc chưa hoàn thành một thứ, diễn đạt dưới dạng giá trị mất trên một đơn vị thời gian. Làm nó tường minh biến ưu tiên từ ý kiến thành số học, và nền tảng cho quy tắc sắp thứ tự như công-việc-ngắn-nhất-có-trọng-số-trước.

**[Coupling (Ghép nối)](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: Mức độ phụ thuộc lẫn nhau giữa các mô-đun hay dịch vụ. Ghép nối lỏng giới hạn hiệu ứng lan của thay đổi và là mục tiêu trung tâm của kiến trúc tốt.

**CQRS (Command Query Responsibility Segregation)**: Mẫu tách mô hình dùng để thay đổi trạng thái (lệnh) khỏi mô hình dùng để đọc trạng thái (truy vấn), cho phép mỗi cái được tối ưu và mở rộng độc lập.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Danh mục công khai các lỗ hổng bảo mật đã công bố, mỗi cái được gán mã định danh duy nhất để công cụ và đội tham chiếu cùng một lỗi không mơ hồ.

**CWV**: Xem Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing, Kiểm thử bảo mật ứng dụng động)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Kiểm thử bảo mật thăm dò một ứng dụng đang chạy từ bên ngoài, không truy cập mã nguồn, để tìm lỗ hổng xuất hiện lúc chạy.

**Data-ink ratio (Tỷ lệ mực dữ liệu)**: Nguyên tắc của Edward Tufte cho rằng một biểu đồ nên dùng phần lớn mực cho chính dữ liệu và ít cho trang trí, loại bỏ đường lưới, viền và rác biểu đồ không cung cấp thông tin.

**[Data mesh (Lưới dữ liệu)](https://en.wikipedia.org/wiki/Data_mesh)**: Kiến trúc dữ liệu phân tán và mô hình vận hành coi dữ liệu là sản phẩm do các đội miền sở hữu, được hỗ trợ bởi hạ tầng nền tảng tự phục vụ và quản trị liên kết.

**[Data visualisation (Trực quan hóa dữ liệu)](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: Thực hành mã hóa dữ liệu dưới dạng hình ảnh (vị trí, độ dài, màu sắc và tương tự) để mẫu hình, so sánh và xu hướng trở nên nhận thức được và quyết định được thông tin tốt hơn.

**[DDD (Domain-Driven Design, Thiết kế hướng miền)](https://en.wikipedia.org/wiki/Domain-driven_design)**: Cách tiếp cận thiết kế phần mềm đặt mô hình vào miền kinh doanh, dùng ngôn ngữ phổ quát chung, ngữ cảnh giới hạn và các khối xây dựng như thực thể, đối tượng giá trị và tập hợp.

**Design tokens (Token thiết kế)**: Các giá trị có tên, không phụ thuộc nền tảng (màu sắc, khoảng cách, kiểu chữ và tương tự) mã hóa quyết định thiết kế để chia sẻ nhất quán qua hệ thống thiết kế và nhiều sản phẩm.

**DevEx / DevX (Developer Experience, Trải nghiệm nhà phát triển)**: Chất lượng tổng thể của tương tác hằng ngày của nhà phát triển với công cụ, nền tảng và quy trình, bao gồm ma sát, tốc độ phản hồi và tải nhận thức.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Văn hóa và tập thực hành thống nhất phát triển phần mềm và vận hành để rút ngắn chu kỳ phân phối, tăng tần suất triển khai và cải thiện độ tin cậy qua tự động hóa và quyền sở hữu chung.

**DORA (DevOps Research and Assessment)**: Chương trình nghiên cứu và bốn chỉ số phân phối được dùng rộng rãi của nó (tần suất triển khai, thời gian chờ cho thay đổi, tỷ lệ thay đổi thất bại và thời gian khôi phục dịch vụ) dùng để đối chuẩn hiệu suất phân phối phần mềm.

**DPIA (Data Protection Impact Assessment, Đánh giá tác động bảo vệ dữ liệu)**: Một đánh giá có cấu trúc, được GDPR yêu cầu cho xử lý rủi ro cao, xác định và giảm thiểu rủi ro riêng tư trước khi dự án tiến hành.

**Drift (configuration, Trôi cấu hình)**: Sự phân kỳ dần của trạng thái thực của hệ thống khỏi trạng thái khai báo hay dự định, thường do thay đổi thủ công gây ra; Hạ tầng dưới dạng mã và GitOps nhằm phát hiện và sửa nó.

**Drift (model, Trôi mô hình)**: Trong học máy, sự suy giảm hiệu suất mô hình theo thời gian khi tính chất thống kê của dữ liệu đầu vào (trôi dữ liệu) hoặc quan hệ đang mô hình hóa (trôi khái niệm) thay đổi.

**[DR (Disaster Recovery, Khôi phục thảm họa)](https://en.wikipedia.org/wiki/Disaster_recovery)**: Chiến lược, quy trình và hạ tầng để khôi phục dịch vụ và dữ liệu sau một sự kiện gián đoạn lớn, thường được chi phối bởi mục tiêu RTO và RPO.

**[DRY (Don't Repeat Yourself, Đừng lặp lại chính mình)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Nguyên tắc thiết kế nói mỗi mẩu tri thức nên có một biểu diễn duy nhất, có thẩm quyền, giảm trùng lặp và rủi ro cập nhật không nhất quán.

## E

**East-west traffic (Lưu lượng đông-tây)**: Lưu lượng mạng giữa các dịch vụ bên trong một hệ thống hay trung tâm dữ liệu, đối lập với lưu lượng bắc-nam giữa hệ thống và client bên ngoài. Lưới dịch vụ thường chi phối lưu lượng đông-tây.

**[Edge computing (Điện toán biên)](https://en.wikipedia.org/wiki/Edge_computing)**: Chạy tính toán và lưu trữ gần nơi dữ liệu được tạo hay tiêu thụ thay vì ở vị trí trung tâm, để cắt độ trễ và băng thông. Mạng phân phối nội dung là dạng sớm, phổ biến của nó.

**[Elasticity (Tính đàn hồi)](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: Khả năng của hệ thống tự động có được và giải phóng tài nguyên theo nhu cầu thay đổi, để năng lực bám sát tải.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Mẫu tích hợp dữ liệu nạp dữ liệu thô vào kho đích trước và biến đổi ở đó, khai thác quy mô của kho dữ liệu và lakehouse hiện đại.

**[Embedding (Nhúng vector)](https://en.wikipedia.org/wiki/Word_embedding)**: Biểu diễn văn bản, hình ảnh hay dữ liệu khác thành vector số dày đặc, định vị sao cho các mục giống nhau nằm gần nhau. Embedding vận hành tìm kiếm ngữ nghĩa và vector và sinh tăng cường truy xuất.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Tiêu chuẩn châu Âu quy định yêu cầu tiếp cận cho sản phẩm và dịch vụ ICT, được mua sắm khu vực công khắp EU tham chiếu và căn chỉnh với WCAG.

**Error budget (Ngân sách lỗi)**: Lượng không đáng tin cậy được phép bởi một SLO trong một kỳ; khi cạn, các đội ưu tiên công việc độ tin cậy hơn tính năng mới. Nó hòa giải căng thẳng giữa vận tốc và ổn định.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Mẫu tích hợp dữ liệu trích xuất dữ liệu từ nguồn, biến đổi nó thành hình dạng đích, và nạp vào điểm đến như kho dữ liệu.

**[EU AI Act (Đạo luật AI của EU)](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: Quy định của Liên minh châu Âu phân loại hệ thống AI theo rủi ro và áp đặt nghĩa vụ tương ứng, cấm một số cách dùng và quản lý chặt hệ thống rủi ro cao.

**[Eventual consistency (Nhất quán cuối cùng)](https://en.wikipedia.org/wiki/Eventual_consistency)**: Mô hình nhất quán trong hệ thống phân tán trong đó các bản sao có thể tạm thời phân kỳ nhưng hội tụ về cùng trạng thái khi cập nhật thôi lan truyền.

## F

**[Feature flag / feature toggle (Cờ tính năng)](https://en.wikipedia.org/wiki/Feature_toggle)**: Cơ chế bật hay tắt chức năng lúc chạy mà không triển khai lại, dùng cho tung ra dần, thí nghiệm và kiểm soát vận hành.

**Feature store (Kho đặc trưng)**: Hệ thống tập trung để định nghĩa, lưu và phục vụ các đặc trưng học máy được tuyển chọn một cách nhất quán cho cả huấn luyện và suy luận, giảm trùng lặp và lệch huấn luyện/phục vụ.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Chương trình chính phủ Hoa Kỳ chuẩn hóa đánh giá bảo mật, ủy quyền và giám sát liên tục cho dịch vụ đám mây mà cơ quan liên bang dùng.

**Few-shot prompting (Gợi ý ít mẫu)**: Cung cấp cho mô hình ngôn ngữ một nhúm ví dụ đã làm trong gợi ý để minh họa tác vụ và định dạng đầu ra mong muốn, đối lập với gợi ý không mẫu (zero-shot), chỉ đưa chỉ dẫn mà không có ví dụ.

**FinOps**: Kỷ luật và thực hành văn hóa mang trách nhiệm tài chính cho chi tiêu đám mây biến đổi, trao cho các đội kỹ thuật, tài chính và kinh doanh quyền sở hữu chung về chi phí và giá trị.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Luật Hoa Kỳ yêu cầu cơ quan liên bang triển khai, lập tài liệu và giám sát chương trình an toàn thông tin, được vận hành phần lớn qua hướng dẫn NIST.

**Flow efficiency (Hiệu quả luồng)**: Tỷ lệ tổng thời gian chờ mà một mục công việc dành để được làm việc tích cực thay vì chờ, tính bằng thời gian tạo giá trị chia cho tổng thời gian chờ. Hầu hết hệ thống thấp đáng ngạc nhiên, thường dưới 15 phần trăm.

**Four-eyes principle (Nguyên tắc bốn mắt)**: Kiểm soát đòi một hành động đáng kể được ít nhất hai người rà soát hay phê duyệt, giảm khả năng lỗi hay sai phạm.

**[Fuzz testing (fuzzing, Kiểm thử fuzz)](https://en.wikipedia.org/wiki/Fuzzing)**: Kỹ thuật kiểm thử tự động đưa đầu vào sai định dạng, ngẫu nhiên hay bất ngờ vào chương trình để tìm sập, lỗi bảo mật và khiếm khuyết trường hợp biên.

## G

**[GDPR (General Data Protection Regulation, Quy định chung về bảo vệ dữ liệu)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: Quy định của Liên minh châu Âu chi phối việc xử lý dữ liệu cá nhân, trao quyền cho cá nhân và áp đặt nghĩa vụ lên bên kiểm soát và bên xử lý, với hình phạt đáng kể khi không tuân thủ.

**GitOps**: Mô hình vận hành dùng Git làm nguồn sự thật duy nhất cho hạ tầng và ứng dụng khai báo, với tự động hóa liên tục đối soát hệ thống sống với trạng thái đã commit.

**Golden path / paved road (Đường vàng / đường lát sẵn)**: Cách mặc định được hỗ trợ tốt, có chính kiến để xây và phát hành phần mềm trong tổ chức, được thiết kế để làm lựa chọn an toàn, tuân thủ, đáng tin cậy là lựa chọn dễ nhất.

**Golden record (Bản ghi vàng)**: Trong quản lý dữ liệu chủ, phiên bản duy nhất, đã đối soát, có thẩm quyền của một thực thể kinh doanh (như khách hàng) được lắp từ nhiều hệ thống nguồn qua quy tắc khớp và sống sót.

**[Gradual typing (Kiểu dần)](https://en.wikipedia.org/wiki/Gradual_typing)**: Cách tiếp cận hệ thống kiểu cho phép kiểu tĩnh và động cùng tồn tại trong một cơ sở mã, để kiểu được thêm dần vào chương trình kiểu động. Gợi ý kiểu và trình kiểm tra kiểu tùy chọn là ví dụ phổ biến.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Ngôn ngữ truy vấn và runtime cho API cho phép client yêu cầu chính xác dữ liệu họ cần trong một lệnh gọi, dùng lược đồ có kiểu mạnh.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Khung gọi thủ tục từ xa hiệu năng cao, hợp đồng trước dùng HTTP/2 và, thường, Protocol Buffers cho giao tiếp dịch vụ-với-dịch vụ hiệu quả.

## H

**Hermetic build (Bản dựng kín)**: Bản dựng chỉ phụ thuộc vào các đầu vào được khai báo tường minh và được cô lập khỏi môi trường máy chủ, nên tạo cùng đầu ra ở bất cứ đâu. Tính kín là nền tảng của bản dựng tái tạo được và bộ đệm đáng tin cậy.

**[HSM (Hardware Security Module, Mô-đun bảo mật phần cứng)](https://en.wikipedia.org/wiki/Hardware_security_module)**: Thiết bị phần cứng chống can thiệp tạo, lưu và dùng khóa mật mã, cung cấp bảo vệ khóa mạnh hơn cách tiếp cận chỉ phần mềm.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Luật Hoa Kỳ, trong số những điều khác, đặt yêu cầu bảo vệ thông tin sức khỏe được bảo vệ (PHI) và chi phối việc sử dụng và tiết lộ nó.

**Horizontal scaling (Mở rộng ngang)**: Tăng năng lực bằng thêm nhiều thể hiện hay nút ("mở rộng ra") thay vì làm một nút đơn mạnh hơn. Nó nâng đỡ hầu hết kiến trúc quy mô lớn, có khả năng phục hồi.

## I

**[IaC (Infrastructure as Code, Hạ tầng dưới dạng mã)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: Thực hành định nghĩa và cung cấp hạ tầng qua cấu hình máy đọc được, được quản lý phiên bản thay vì quy trình thủ công, cho phép lặp lại và rà soát.

**[IAM (Identity and Access Management, Quản lý danh tính và truy cập)](https://en.wikipedia.org/wiki/Identity_management)**: Khung chính sách và công nghệ bảo đảm đúng danh tính có đúng quyền truy cập vào đúng tài nguyên vào đúng thời điểm.

**IDP / IdP**: "IDP" thường chỉ Nền tảng Nhà phát triển Nội bộ, tầng công cụ tự phục vụ trừu tượng hóa hạ tầng cho các đội sản phẩm; "IdP" chỉ Nhà cung cấp Danh tính, dịch vụ xác thực người dùng và phát hành khẳng định. Ngữ cảnh phân biệt hai cái.

**[Idempotency (Tính lũy đẳng)](https://en.wikipedia.org/wiki/Idempotence)**: Thuộc tính trong đó thực hiện một thao tác nhiều lần có cùng hiệu ứng như thực hiện một lần, thiết yếu cho thử lại an toàn trong hệ thống phân tán và API.

**[i18n (Internationalisation, Quốc tế hóa)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: Thiết kế và xây dựng phần mềm để thích ứng với các ngôn ngữ, khu vực và quy ước văn hóa khác nhau mà không cần thay đổi kỹ thuật. Số-từ viết tắt 18 chữ cái giữa "i" và "n."

**Immutable artefact (Hiện vật bất biến)**: Đầu ra bản dựng mà, một khi được tạo và đánh phiên bản, không bao giờ bị sửa; mọi thay đổi tạo phiên bản mới. Tính bất biến làm bản phát hành tái tạo được và cho phép bạn dựng một lần và thăng cấp cùng hiện vật qua các môi trường.

**InnerSource**: Việc áp dụng thực hành phát triển mã nguồn mở (minh bạch, kho dùng chung và đóng góp xuyên đội) bên trong một tổ chức đơn lẻ.

**IaC drift**: Xem Drift (configuration).

**[Inverted index (Chỉ mục nghịch đảo)](https://en.wikipedia.org/wiki/Inverted_index)**: Cấu trúc dữ liệu cốt lõi của công cụ tìm kiếm, ánh xạ mỗi thuật ngữ tới danh sách tài liệu chứa nó, để truy vấn được trả lời mà không quét mọi tài liệu.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Tiêu chuẩn quốc tế quy định yêu cầu cho Hệ thống Quản lý An toàn Thông tin (ISMS), cung cấp khung chứng nhận được để quản lý rủi ro an toàn thông tin.

**ISO/IEC 42001**: Tiêu chuẩn quốc tế quy định yêu cầu cho Hệ thống Quản lý AI, trao cho tổ chức khung chứng nhận được để quản trị phát triển và sử dụng AI có trách nhiệm.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Định dạng token gọn, được ký (và tùy chọn được mã hóa) dùng để truyền các tuyên bố giữa các bên, thường cho xác thực và ủy quyền trong hệ thống web và API.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Phương pháp luồng việc tinh gọn trực quan hóa công việc trên bảng, giới hạn công việc đang làm, và quản lý luồng để cải thiện thông lượng và khả năng dự đoán.

**[KISS (Keep It Simple, Stupid, Giữ nó đơn giản)](https://en.wikipedia.org/wiki/KISS_principle)**: Nguyên tắc thiết kế ưu tiên giải pháp đơn giản nhất đáp ứng nhu cầu, với lý do độ phức tạp không cần thiết tăng chi phí và rủi ro.

**KMS (Key Management Service, Dịch vụ quản lý khóa)**: Hệ thống tạo, lưu, xoay vòng và kiểm soát truy cập khóa mật mã, thường được hậu thuẫn bởi mô-đun bảo mật phần cứng.

**[KPI (Key Performance Indicator, Chỉ số hiệu suất chính)](https://en.wikipedia.org/wiki/Performance_indicator)**: Thước đo định lượng được dùng để theo dõi tiến độ tới một mục tiêu kinh doanh hay vận hành cụ thể.

## L

**Lakehouse**: Kiến trúc dữ liệu kết hợp lưu trữ rẻ, linh hoạt của hồ dữ liệu với quản lý, giao dịch và tính năng hiệu năng của kho dữ liệu.

**[Lead time (Thời gian chờ)](https://en.wikipedia.org/wiki/Lead_time)**: Thời gian trôi qua từ khi một thay đổi được yêu cầu (hoặc commit) đến khi nó được giao vào sản xuất; chỉ số phân phối DORA cốt lõi.

**[Least privilege (Đặc quyền tối thiểu)](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: Nguyên tắc bảo mật chỉ cấp cho mỗi người dùng, tiến trình hay hệ thống quyền truy cập tối thiểu cần để thực hiện chức năng, giới hạn thiệt hại từ xâm phạm hay lỗi.

**[Little's Law (Định luật Little)](https://en.wikipedia.org/wiki/Little's_law)**: Kết quả của lý thuyết hàng đợi nói số mục trung bình trong một hệ thống ổn định bằng tốc độ đến trung bình nhân thời gian trung bình mỗi mục ở trong hệ thống. Nó nối công việc đang làm, thông lượng và thời gian chờ.

**[LLM (Large Language Model, Mô hình ngôn ngữ lớn)](https://en.wikipedia.org/wiki/Large_language_model)**: Mô hình học máy được huấn luyện trên kho văn bản rất lớn để dự đoán và sinh ngôn ngữ, có khả năng thực hiện các tác vụ như tóm tắt, dịch và sinh mã.

**[l10n (Localisation, Bản địa hóa)](https://en.wikipedia.org/wiki/Language_localisation)**: Điều chỉnh phần mềm đã quốc tế hóa cho một địa phương cụ thể, gồm dịch, định dạng và quy ước văn hóa. Số-từ viết tắt 10 chữ cái giữa "l" và "n."

## M

**[MDM (Master Data Management, Quản lý dữ liệu chủ)](https://en.wikipedia.org/wiki/Master_data_management)**: Kỷ luật và công cụ tạo và duy trì cái nhìn duy nhất, có thẩm quyền, nhất quán về các thực thể kinh doanh cốt lõi (như khách hàng hay sản phẩm) qua các hệ thống.

**MITRE ATT&CK**: Cơ sở tri thức công khai, được tuyển chọn về chiến thuật và kỹ thuật của đối thủ trong thế giới thật, được dùng rộng rãi để hoạch định bài tập đội đỏ, dẫn dắt kỹ thuật phát hiện và mô tả mối đe dọa bằng từ vựng chung.

**Mean Time to Recovery (MTTR, Thời gian khôi phục trung bình)**: Thời gian trung bình để khôi phục dịch vụ sau thất bại; chỉ số độ tin cậy và quản lý sự cố phổ biến.

**[Mob programming (Lập trình đám đông)](https://en.wikipedia.org/wiki/Mob_programming)**: Thực hành trong đó cả đội cùng làm một tác vụ trên cùng một máy tính, luân phiên ai gõ, để chia sẻ tri thức và đưa quyết định tập thể.

**[MLOps (Machine Learning Operations, Vận hành học máy)](https://en.wikipedia.org/wiki/MLOps)**: Tập thực hành triển khai, giám sát và bảo trì mô hình học máy trong sản xuất một cách đáng tin cậy và hiệu quả, mở rộng nguyên tắc DevOps cho vòng đời ML.

**[Monorepo (Kho đơn)](https://en.wikipedia.org/wiki/Monorepo)**: Một kho quản lý phiên bản duy nhất giữ mã cho nhiều dự án hoặc cả tổ chức, cho phép công cụ dùng chung và thay đổi xuyên dự án nguyên tử với cái giá là công cụ mở rộng chuyên biệt.

**mTLS (mutual TLS)**: Cấu hình Transport Layer Security trong đó cả hai bên trình và xác minh chứng chỉ, nên mỗi bên xác thực bên kia. Đó là mặc định cho lưu lượng dịch vụ-với-dịch vụ trong lưới dịch vụ và mạng zero-trust. Xem thêm [xác thực lẫn nhau](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing (Kiểm thử đột biến)](https://en.wikipedia.org/wiki/Mutation_testing)**: Kỹ thuật cố ý đưa lỗi nhỏ ("đột biến") vào mã để kiểm tra bộ kiểm thử có phát hiện được chúng không, đo hiệu quả thật của bộ kiểm thử.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Thước đo chất lượng xếp hạng thưởng cho việc đặt kết quả rất liên quan gần đầu danh sách kết quả, được chuẩn hóa để điểm so sánh được qua các truy vấn. Đó là chỉ số chủ đạo trong đánh giá độ liên quan tìm kiếm.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Cơ quan liên bang Hoa Kỳ có các Ấn phẩm Đặc biệt và khung là tiêu chuẩn được tham chiếu rộng rãi cho an ninh mạng, riêng tư và AI.

**NIST AI RMF (AI Risk Management Framework)**: Khung NIST tự nguyện để xác định, đánh giá và quản lý rủi ro liên quan đến hệ thống AI qua vòng đời của chúng, tổ chức quanh các chức năng Quản trị, Lập bản đồ, Đo lường và Quản lý.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Danh mục kiểm soát bảo mật và riêng tư của NIST cho hệ thống thông tin liên bang, được dùng rộng rãi làm đường cơ sở vượt xa chính phủ.

**NIST SP 800-171**: Ấn phẩm NIST quy định yêu cầu bảo vệ thông tin không mật được kiểm soát (CUI) trong hệ thống phi liên bang, trung tâm với tuân thủ của nhà thầu quốc phòng.

**[NFR (Non-Functional Requirement, Yêu cầu phi chức năng)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: Yêu cầu mô tả hệ thống nên hành xử thế nào (các phẩm chất như hiệu năng, bảo mật, độ tin cậy hay khả dụng) thay vì nó thực hiện chức năng gì.

**North-south traffic (Lưu lượng bắc-nam)**: Lưu lượng mạng giữa một hệ thống và client bên ngoài (vào và ra khỏi trung tâm dữ liệu hay cụm), đối lập với lưu lượng đông-tây giữa các dịch vụ nội bộ. Cổng API thường chi phối lưu lượng bắc-nam.

## O

**Observability (Khả năng quan sát)**: Mức độ trạng thái bên trong của hệ thống có thể được suy ra từ đầu ra bên ngoài của nó, thường đạt được qua đo từ xa: chỉ số, nhật ký và vết.

**[OKR (Objectives and Key Results, Mục tiêu và Kết quả then chốt)](https://en.wikipedia.org/wiki/OKR)**: Khung đặt mục tiêu ghép một mục tiêu định tính với vài kết quả then chốt đo được để căn chỉnh và tập trung tổ chức.

**OpenTelemetry (OTel)**: Tiêu chuẩn mở và bộ công cụ trung lập nhà cung cấp để tạo, thu thập và xuất dữ liệu đo từ xa (vết, chỉ số và nhật ký) từ phần mềm.

**OPA (Open Policy Agent)**: Công cụ chính sách đa dụng, mã nguồn mở đánh giá chính sách (viết bằng ngôn ngữ Rego) để thực thi quy tắc ủy quyền và cấu hình xuyên ngăn xếp, cho phép chính sách dưới dạng mã.

**OSPO (Open Source Program Office, Văn phòng chương trình mã nguồn mở)**: Chức năng tổ chức phối hợp chiến lược mã nguồn mở, quản trị, tuân thủ và gắn kết cộng đồng, quản lý cả tiêu thụ lẫn đóng góp.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Cộng đồng phi lợi nhuận tạo ra các tài nguyên bảo mật ứng dụng được dùng rộng rãi, miễn phí, gồm OWASP Top Ten và ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Phần mở rộng của định lý CAP nói rằng nếu có Phân vùng, hệ thống đánh đổi Khả dụng với Nhất quán, Còn không (trong vận hành bình thường) nó đánh đổi Độ trễ với Nhất quán.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Tiêu chuẩn bảo mật do ngành thẻ thanh toán duy trì, quy định yêu cầu cho các tổ chức lưu, xử lý hay truyền dữ liệu chủ thẻ.

**[Penetration testing (Kiểm thử xâm nhập)](https://en.wikipedia.org/wiki/Penetration_test)**: Cuộc tấn công mô phỏng, được ủy quyền lên một hệ thống bởi người kiểm thử lành nghề để tìm và chứng minh các lỗ hổng khai thác được trước khi kẻ tấn công thật làm, giao dưới dạng phát hiện được ưu tiên, hành động được.

**[PII (Personally Identifiable Information, Thông tin nhận dạng cá nhân)](https://en.wikipedia.org/wiki/Personal_data)**: Thông tin có thể nhận dạng một cá nhân cụ thể, một mình hoặc kết hợp với dữ liệu khác; việc xử lý nó được chi phối bởi luật riêng tư và chính sách nội bộ.

**Platform engineering (Kỹ thuật nền tảng)**: Kỷ luật xây và vận hành nền tảng tự phục vụ nội bộ và đường vàng giảm tải nhận thức và đẩy nhanh các đội sản phẩm.

**POUR**: Bốn nguyên tắc dẫn dắt của Hướng dẫn Tiếp cận Nội dung Web: nội dung phải Nhận thức được (Perceivable), Vận hành được (Operable), Hiểu được (Understandable) và Vững chắc (Robust).

**Production readiness review (Rà soát sẵn sàng sản xuất)**: Một kiểm tra có cấu trúc, chạy trước khi một dịch vụ vận hành hay nhận quyền sở hữu trực ca, xác nhận nó đáp ứng tiêu chuẩn về khả năng quan sát, độ tin cậy, bảo mật, sổ tay vận hành và hỗ trợ vận hành.

**[Prompt engineering (Kỹ thuật gợi ý)](https://en.wikipedia.org/wiki/Prompt_engineering)**: Thực hành thiết kế và tinh chỉnh chỉ dẫn, ngữ cảnh và ví dụ trao cho mô hình ngôn ngữ để có đầu ra đáng tin cậy, chất lượng cao, được coi là kỷ luật kỹ thuật có phiên bản, được kiểm thử thay vì thử và sai.

**[Prompt injection (Tiêm gợi ý)](https://en.wikipedia.org/wiki/Prompt_injection)**: Cuộc tấn công trong đó đầu vào được chế tạo khiến mô hình ngôn ngữ phớt lờ chỉ dẫn dự định và làm theo của kẻ tấn công, chất tương tự thời AI của lỗi tiêm. Đó là rủi ro bảo mật trung tâm của ứng dụng LLM.

**Property-based testing (Kiểm thử dựa trên thuộc tính)**: Kỹ thuật kiểm thử kiểm tra các thuộc tính đã nêu đúng qua nhiều đầu vào tự động sinh, thay vì chỉ dựa vào ví dụ chọn tay.

**Pull request (PR) / merge request (MR, Yêu cầu kéo / yêu cầu hợp nhất)**: Tập thay đổi đề xuất được nộp để rà soát và thảo luận trước khi hợp nhất vào nhánh chung, đơn vị rà soát mã chính trong hầu hết quy trình.

**Purple team (Đội tím)**: Bài tập cộng tác trong đó đội bảo mật tấn công (đỏ) và phòng thủ (xanh) làm việc cùng nhau theo thời gian thực, để các cuộc tấn công và phát hiện nhằm bắt chúng được điều chỉnh với nhau.

## Q

**Quality gate (Cổng chất lượng)**: Điểm kiểm tra tự động trong quy trình phải vượt qua (ví dụ đạt ngưỡng độ phủ, bảo mật hay hiệu năng) trước khi một thay đổi tiến tiếp.

**[Quorum (Túc số)](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: Trong hệ thống phân tán, số nút tối thiểu phải đồng ý để một thao tác (như đọc hay ghi) được coi là thành công, dùng để duy trì nhất quán bất chấp thất bại.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Mô hình phân công trách nhiệm gắn nhãn mỗi người tham gia trong một tác vụ hay quyết định là Thực hiện (Responsible), Chịu trách nhiệm (Accountable), Được tham vấn (Consulted) hay Được thông báo (Informed).

**[RAG (Retrieval-Augmented Generation, Sinh tăng cường truy xuất)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: Kỹ thuật làm nền cho đầu ra của mô hình ngôn ngữ bằng cách trước tiên truy xuất tài liệu hay dữ liệu liên quan và cung cấp chúng làm ngữ cảnh, cải thiện độ chính xác và giảm ảo giác.

**[RBAC (Role-Based Access Control, Kiểm soát truy cập dựa trên vai trò)](https://en.wikipedia.org/wiki/Role-based_access_control)**: Mô hình ủy quyền gán quyền cho vai trò và vai trò cho người dùng, đơn giản hóa quản trị bằng quản lý truy cập ở cấp vai trò.

**[Red team (Đội đỏ)](https://en.wikipedia.org/wiki/Red_team)**: Nhóm mô phỏng một đối thủ thực tế, thường chống lại cả tổ chức và không cảnh báo người phòng thủ, để kiểm thử phát hiện và ứng phó thay vì chỉ liệt kê lỗ hổng. Đối lập với đội xanh (phòng thủ).

**[Reference data (Dữ liệu tham chiếu)](https://en.wikipedia.org/wiki/Reference_data)**: Danh sách mã và phân loại được kiểm soát, thay đổi chậm dùng để phân loại dữ liệu khác, như mã quốc gia, tiền tệ và giá trị trạng thái. Quản trị nó như từ vựng dùng chung, có phiên bản giữ các hệ thống nhất quán.

**Rego**: Ngôn ngữ chính sách khai báo mà Open Policy Agent dùng để diễn đạt quy tắc cho quyết định ủy quyền và cấu hình.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Phong cách kiến trúc cho ứng dụng mạng dùng các thao tác không trạng thái qua HTTP trên tài nguyên có địa chỉ, được đánh giá cao vì đơn giản và công cụ rộng rãi.

**[Reverse proxy (Proxy ngược)](https://en.wikipedia.org/wiki/Reverse_proxy)**: Máy chủ đứng trước một hay nhiều dịch vụ backend và chuyển tiếp yêu cầu client tới chúng, thường cung cấp kết thúc TLS, cân bằng tải, bộ đệm và điểm vào duy nhất.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Đề xuất bằng văn bản được lưu hành để lấy phản hồi trước một quyết định hay thay đổi kỹ thuật đáng kể, thúc đẩy minh bạch và quyền sở hữu chung. (Thuật ngữ cũng gọi tên loạt tài liệu tiêu chuẩn Internet.)

**[ROI (Return on Investment, Lợi tức đầu tư)](https://en.wikipedia.org/wiki/Return_on_investment)**: Thước đo giá trị thu được từ một khoản đầu tư so với chi phí của nó, dùng để biện minh và ưu tiên quyết định kỹ thuật và công nghệ.

**[RPA (Robotic Process Automation, Tự động hóa quy trình bằng robot)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: "Robot" phần mềm tự động hóa tác vụ lặp lại, dựa trên quy tắc bằng cách tương tác với giao diện người dùng và hệ thống hiện có như một người.

**RPO (Recovery Point Objective, Mục tiêu điểm khôi phục)**: Lượng mất dữ liệu tối đa chấp nhận được đo bằng thời gian (ví dụ "tối đa năm phút"), xác định dữ liệu phải được bảo vệ thường xuyên thế nào.

**RTO (Recovery Time Objective, Mục tiêu thời gian khôi phục)**: Thời lượng tối đa chấp nhận được để khôi phục một dịch vụ sau gián đoạn, dẫn dắt thiết kế và đầu tư khôi phục thảm họa.

## S

**Saga**: Mẫu quản lý nhất quán dữ liệu qua các dịch vụ trong một giao dịch phân tán bằng sắp thứ tự các giao dịch cục bộ và phát hành hành động bù khi một bước thất bại.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Khung áp dụng thực hành agile và tinh gọn qua doanh nghiệp lớn, phối hợp nhiều đội; được đánh giá cao vì cấu trúc và bị chỉ trích vì có thể nặng nề.

**[SAST (Static Application Security Testing, Kiểm thử bảo mật ứng dụng tĩnh)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Kiểm thử bảo mật phân tích mã nguồn, bytecode hay nhị phân mà không thực thi chúng để tìm lỗ hổng sớm trong phát triển.

**SBOM (Software Bill of Materials, Danh mục vật liệu phần mềm)**: Bản kiểm kê chính thức, máy đọc được các thành phần và phụ thuộc trong một phần mềm, dùng để quản lý rủi ro chuỗi cung ứng và lỗ hổng.

**SCA (Software Composition Analysis, Phân tích thành phần phần mềm)**: Công cụ xác định thành phần mã nguồn mở và bên thứ ba trong cơ sở mã và gắn cờ lỗ hổng đã biết và rủi ro giấy phép.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Khung agile tổ chức công việc thành các vòng lặp độ dài cố định (sprint) với vai trò, sự kiện và hiện vật xác định để giao các phần tăng trưởng giá trị.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Luật Hoa Kỳ yêu cầu cơ quan liên bang làm công nghệ điện tử và thông tin của họ tiếp cận được với người khuyết tật, trong thực hành căn chỉnh với WCAG.

**Semantic search (Tìm kiếm ngữ nghĩa)**: Tìm kiếm khớp theo ý nghĩa thay vì từ khóa chính xác, thường bằng so sánh embedding của truy vấn và tài liệu. Nó thường được kết hợp với tìm kiếm từ vựng trong cách tiếp cận lai.

**[Service mesh (Lưới dịch vụ)](https://en.wikipedia.org/wiki/Service_mesh)**: Tầng hạ tầng chuyên dụng, thường triển khai bằng proxy sidecar, xử lý mối quan tâm giao tiếp dịch vụ-với-dịch vụ như mutual TLS, thử lại, thời gian chờ, chuyển lưu lượng và khả năng quan sát, giữ chúng ngoài mã ứng dụng.

**Sidecar**: Tiến trình hay container hỗ trợ được triển khai cạnh một thể hiện ứng dụng chính để cung cấp năng lực hỗ trợ (như proxy lưới dịch vụ) mà không đổi chính ứng dụng.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Hệ thống tổng hợp và tương quan nhật ký và sự kiện bảo mật qua một môi trường để cho phép phát hiện, cảnh báo và điều tra.

**[SLA (Service Level Agreement, Thỏa thuận mức dịch vụ)](https://en.wikipedia.org/wiki/Service-level_agreement)**: Cam kết chính thức giữa nhà cung cấp dịch vụ và khách hàng quy định mức dịch vụ kỳ vọng và hệ quả của việc trượt chúng.

**SLI (Service Level Indicator, Chỉ báo mức dịch vụ)**: Thước đo định lượng về một khía cạnh chất lượng dịch vụ, như độ trễ yêu cầu hay tỷ lệ lỗi, nuôi các SLO.

**SLO (Service Level Objective, Mục tiêu mức dịch vụ)**: Giá trị hay khoảng mục tiêu cho một SLI xác định mức độ tin cậy mong muốn, tạo cơ sở cho ngân sách lỗi.

**SLSA (Supply-chain Levels for Software Artifacts)**: Khung các yêu cầu bảo mật có bậc để cải thiện tính toàn vẹn và nguồn gốc của hiện vật phần mềm qua quá trình dựng và phát hành.

**SOAR (Security Orchestration, Automation, and Response)**: Công cụ và thực hành tự động hóa và phối hợp vận hành bảo mật, như sổ tay kịch bản phân loại và ứng phó, để cải thiện tốc độ và nhất quán.

**SOC 2 (System and Organisation Controls 2)**: Khung kiểm toán và báo cáo, dựa trên Tiêu chí Dịch vụ Tin cậy của AICPA, đánh giá kiểm soát của một tổ chức dịch vụ về bảo mật, khả dụng, toàn vẹn xử lý, bảo mật thông tin và riêng tư.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Năm nguyên tắc thiết kế hướng đối tượng (Trách nhiệm đơn, Mở/Đóng, Thay thế Liskov, Phân tách giao diện và Đảo ngược phụ thuộc) thúc đẩy mã bảo trì được, linh hoạt.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Luật Hoa Kỳ thiết lập yêu cầu về báo cáo tài chính và kiểm soát nội bộ trong công ty đại chúng, có hệ quả với hệ thống CNTT hỗ trợ dữ liệu tài chính.

**SPACE**: Khung đo năng suất nhà phát triển qua năm chiều: Hài lòng và an sinh, Hiệu suất, Hoạt động, Giao tiếp và cộng tác, và Hiệu quả và luồng, cảnh báo chống thước đo một chỉ số.

**[SRE (Site Reliability Engineering, Kỹ thuật độ tin cậy hệ thống)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: Kỷ luật áp dụng cách tiếp cận kỹ thuật phần mềm cho vận hành, dùng SLO, ngân sách lỗi và tự động hóa để chạy hệ thống đáng tin cậy ở quy mô.

**SSDF (Secure Software Development Framework)**: Khung của NIST (SP 800-218) gồm các thực hành phát triển an toàn cấp cao, trải qua chuẩn bị tổ chức, bảo vệ phần mềm, tạo phần mềm bảo mật tốt và ứng phó lỗ hổng.

**[Static analysis (Phân tích tĩnh)](https://en.wikipedia.org/wiki/Static_program_analysis)**: Xem xét mã nguồn, bytecode hay nhị phân mà không thực thi để tìm khiếm khuyết, vi phạm phong cách và lỗi bảo mật, thường qua linter, trình kiểm tra kiểu và bộ phân tích chuyên dụng nối vào trình soạn thảo và quy trình.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Phân loại mô hình hóa mối đe dọa chia mối đe dọa thành Giả mạo (Spoofing), Can thiệp (Tampering), Chối bỏ (Repudiation), Tiết lộ thông tin (Information disclosure), Từ chối dịch vụ (Denial of service) và Nâng đặc quyền (Elevation of privilege).

## T

**[TCO (Total Cost of Ownership, Tổng chi phí sở hữu)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: Chi phí toàn vòng đời của một hệ thống hay quyết định, gồm mua lại, vận hành, bảo trì và loại bỏ cuối cùng, không chỉ giá ban đầu.

**[TDD (Test-Driven Development, Phát triển hướng kiểm thử)](https://en.wikipedia.org/wiki/Test-driven_development)**: Thực hành viết một kiểm thử tự động thất bại trước mã làm nó đạt, rồi tái cấu trúc, theo chu kỳ ngắn lặp lại để dẫn dắt thiết kế và bảo đảm độ phủ.

**[Technical debt (Nợ kỹ thuật)](https://en.wikipedia.org/wiki/Technical_debt)**: Chi phí tương lai ngụ ý của việc chọn giải pháp tiện lợi bây giờ thay vì giải pháp tốt hơn mất nhiều thời gian hơn, phải được quản lý có chủ đích thay vì tích lũy vô thức.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Sơ đồ trọng số kinh điển chấm điểm tầm quan trọng của một thuật ngữ với một tài liệu bằng tần suất nó xuất hiện ở đó, bù lại bởi mức phổ biến của nó qua cả kho. Nó nằm dưới phần lớn xếp hạng tìm kiếm từ vựng.

**[Theory of constraints (Lý thuyết ràng buộc)](https://en.wikipedia.org/wiki/Theory_of_constraints)**: Cách tiếp cận quản lý cho rằng thông lượng của hệ thống bị giới hạn bởi một nút thắt duy nhất tại bất kỳ thời điểm nào, nên nỗ lực cải thiện nên tập trung vào ràng buộc đó cho đến khi nó dịch chuyển nơi khác.

**[Threat modelling (Mô hình hóa mối đe dọa)](https://en.wikipedia.org/wiki/Threat_model)**: Thực hành có cấu trúc xác định, liệt kê và ưu tiên các mối đe dọa tiềm tàng với một hệ thống để phòng thủ được thiết kế sớm.

**Toil (Lao động nhàm chán)**: Trong SRE, công việc vận hành thủ công, lặp lại, tự động hóa được, mở rộng tuyến tính với dịch vụ và không mang giá trị lâu dài; giảm nó giải phóng năng lực cho kỹ thuật.

**Trunk-based development (Phát triển trên thân chính)**: Thực hành kiểm soát nguồn trong đó nhà phát triển tích hợp thay đổi nhỏ thường xuyên vào một nhánh chung duy nhất, tối thiểu hóa nhánh sống lâu và nỗi đau hợp nhất.

**[Type inference (Suy luận kiểu)](https://en.wikipedia.org/wiki/Type_inference)**: Tính năng ngôn ngữ tự động suy ra kiểu của biểu thức, cho phần lớn sự an toàn của kiểu tĩnh mà không đòi mọi kiểu phải được viết ra bằng tay.

**[Type system (Hệ thống kiểu)](https://en.wikipedia.org/wiki/Type_system)**: Tập quy tắc ngôn ngữ dùng để gán và kiểm tra kiểu, bắt cả lớp lỗi trước khi chương trình chạy và lập tài liệu ý định. Hệ thống kiểu trải từ động đến tĩnh và từ yếu đến mạnh.

## U

**Ubiquitous language (Ngôn ngữ phổ quát)**: Trong Thiết kế Hướng Miền, từ vựng chung, chính xác được nhà phát triển và chuyên gia miền dùng nhất quán, và phản ánh trực tiếp trong mã và mô hình.

**[UAT (User Acceptance Testing, Kiểm thử chấp nhận người dùng)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Kiểm thử do người dùng cuối hay đại diện của họ thực hiện để xác nhận hệ thống đáp ứng nhu cầu kinh doanh trước khi được chấp nhận phát hành.

**[UX / UI (User Experience / User Interface, Trải nghiệm người dùng / Giao diện người dùng)](https://en.wikipedia.org/wiki/User_experience)**: Trải nghiệm người dùng là chất lượng tổng thể của tương tác của một người với sản phẩm; Giao diện người dùng là bề mặt hình ảnh và tương tác cụ thể qua đó tương tác diễn ra.

## V

**[Value object (Đối tượng giá trị)](https://en.wikipedia.org/wiki/Value_object)**: Trong Thiết kế Hướng Miền, đối tượng bất biến được xác định hoàn toàn bởi thuộc tính của nó thay vì danh tính riêng biệt, như một số tiền hay khoảng ngày.

**[Value stream mapping (Lập bản đồ dòng giá trị)](https://en.wikipedia.org/wiki/Value-stream_mapping)**: Kỹ thuật vẽ mọi bước từ ý tưởng đến giá trị được giao, phân biệt thời gian tạo giá trị với thời gian chờ, để nút thắt, bàn giao và vòng làm lại trở nên hiển thị và cải thiện được.

**[Vector database (Cơ sở dữ liệu vector)](https://en.wikipedia.org/wiki/Vector_database)**: Kho dữ liệu được tối ưu để lập chỉ mục và tìm kiếm vector embedding nhiều chiều theo độ tương tự, xương sống phổ biến của tìm kiếm ngữ nghĩa và sinh tăng cường truy xuất.

**Vertical scaling (Mở rộng dọc)**: Tăng năng lực bằng làm một nút đơn mạnh hơn ("mở rộng lên"), đơn giản nhưng cuối cùng bị giới hạn bởi máy lớn nhất có sẵn.

**[VCS (Version Control System, Hệ thống quản lý phiên bản)](https://en.wikipedia.org/wiki/Version_control)**: Công cụ, như Git, ghi lại thay đổi của tệp theo thời gian để lịch sử được rà soát, nhánh được duy trì và công việc được phối hợp.

**[Vulnerability scanning (Quét lỗ hổng)](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: Kiểm tra tự động hệ thống, container hay mã so với cơ sở dữ liệu điểm yếu và cấu hình sai đã biết. Nó rộng và rẻ, và bổ sung độ sâu của kiểm thử xâm nhập thủ công.

## W

**[WCAG (Web Content Accessibility Guidelines, Hướng dẫn Tiếp cận Nội dung Web)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Tập hướng dẫn được W3C công nhận quốc tế, tổ chức quanh các nguyên tắc POUR và mức tuân thủ A, AA và AAA, để làm nội dung web tiếp cận được.

**Wardley map (Bản đồ Wardley)**: Kỹ thuật chiến lược trực quan định vị năng lực theo giá trị với người dùng và mức trưởng thành tiến hóa của chúng, để thông tin cho quyết định xây/mua và đầu tư.

**Work in progress (WIP) limit (Giới hạn công việc đang làm)**: Giới hạn số mục được phép ở một giai đoạn nhất định của luồng việc cùng lúc, thực hành Kanban cốt lõi cải thiện luồng bằng làm lộ nút thắt và kiềm chế chi phí chung của quá nhiều công việc song song.

**WSJF (Weighted Shortest Job First, Công việc ngắn nhất có trọng số trước)**: Phương pháp ưu tiên sắp thứ tự công việc bằng chia chi phí trì hoãn của nó cho thời lượng ước tính, để các mục ngắn nhất, nhạy thời gian nhất, giá trị cao nhất được làm trước.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Lỗ hổng web trong đó kẻ tấn công tiêm script độc hại thực thi trong trình duyệt của người dùng khác, có thể đánh cắp dữ liệu hoặc chiếm phiên.

## Y

**[YAGNI (You Aren't Gonna Need It, Bạn sẽ không cần nó)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Nguyên tắc khuyên chống xây chức năng theo suy đoán, với lý do nhu cầu dự đoán thường không thành hiện thực và thêm chi phí và độ phức tạp.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: Mô hình bảo mật không giả định tin cậy ngầm dựa trên vị trí mạng và liên tục xác minh mọi yêu cầu truy cập theo danh tính, thiết bị và ngữ cảnh, theo châm ngôn "không bao giờ tin, luôn xác minh."
