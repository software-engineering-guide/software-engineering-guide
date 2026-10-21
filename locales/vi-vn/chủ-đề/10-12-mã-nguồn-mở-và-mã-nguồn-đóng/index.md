# 10.12 Mã nguồn mở và mã nguồn đóng

## Tổng quan và động lực

Gần như mọi hệ thống hiện đại là sự pha trộn giữa phần mềm bạn tự viết, phần mềm bạn mua, và phần mềm bạn lấy miễn phí. Hai trong ba loại đó đi kèm một lựa chọn căn bản: phần mềm là **mã nguồn mở** hay **mã nguồn đóng**? **[Phần mềm nguồn mở](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** được phân phối theo giấy phép trao cho mọi người quyền sử dụng, nghiên cứu, sửa đổi và phân phối lại mã nguồn, những chỉ dẫn con người đọc được xác định chương trình. **Phần mềm mã nguồn đóng**, còn gọi là **[phần mềm độc quyền](https://en.wikipedia.org/wiki/Proprietary_software)**, được phân phối như sản phẩm hoàn chỉnh mà nhà cung cấp giữ kín mã nguồn. Bạn có quyền chạy nó theo giấy phép, nhưng không có quyền xem xét hay thay đổi cách nó hoạt động. Một loại trung gian, **[phần mềm có sẵn mã nguồn](https://en.wikipedia.org/wiki/Source-available_software)**, công bố mã nguồn để đọc nhưng hạn chế sử dụng, sửa đổi hay phân phối lại. Nó *nhìn thấy được* nhưng không *mở* theo định nghĩa chuẩn.

Hai điều làm rõ quan trọng trước khi bạn so sánh. Thứ nhất, "miễn phí" mơ hồ. Cộng đồng phân biệt **miễn phí theo nghĩa tự do** (quyền sửa đổi và chia sẻ, đôi khi viết "libre") với **miễn phí theo nghĩa giá cả** (không tốn tiền, "gratis"). Mã nguồn mở nói về tự do, không nhất thiết về giá. Thứ hai, giấy phép mã nguồn mở chia thành hai họ. **[Giấy phép cho phép rộng rãi](https://en.wikipedia.org/wiki/Permissive_software_license)** (như [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD và Apache 2.0) cho bạn làm hầu như mọi thứ, gồm nhúng mã vào sản phẩm đóng. **Giấy phép [copyleft](https://en.wikipedia.org/wiki/Copyleft)** (như [Giấy phép Công cộng GNU](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) đòi các tác phẩm phái sinh bạn phân phối cũng được phát hành theo cùng điều khoản mở, một quy tắc có đi có lại mà những người chỉ trích đôi khi gọi là "lây lan" và những người ủng hộ gọi là "chia sẻ tương tự."

Chương này nhìn lựa chọn từ hai phía. Với tư cách **người tiêu dùng**, bạn quyết định có áp dụng một thành phần mã nguồn mở hay độc quyền. Với tư cách **nhà sản xuất**, bạn quyết định có mở mã nguồn phần mềm bạn đã xây không. Với doanh nghiệp lớn và đặc biệt chính phủ, cả hai quyết định mang trọng lượng vượt xa tệp giấy phép. Chúng chạm đến mua sắm (chương 10.3), chủ quyền số (chương 10.11), bảo mật chuỗi cung ứng (chương 4.2), khả năng tương tác (chương 3.8), và phép tính xây-hay-mua (chương 6.1).

## Các nguyên tắc chính

- **Giấy phép, không phải giá, định nghĩa "mở."** Hãy đọc giấy phép; miễn phí và mã nguồn mở là hai tuyên bố khác nhau.
- **Không mô hình nào vốn dĩ an toàn hơn.** Cả hai có thể xuất sắc hoặc cẩu thả; thực hành xung quanh mã quan trọng hơn sự cởi mở của nó.
- **Cởi mở là đòn bẩy giảm phụ thuộc.** Quyền tiếp cận mã nguồn là sự bảo vệ tối thượng chống [khóa chặt nhà cung cấp](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **Bạn luôn sở hữu gánh nặng vận hành.** Miễn phí để có không bao giờ miễn phí để chạy; [tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership) kể câu chuyện thật.
- **Yếu tố tạo khác biệt giữ đóng; hàng hóa thông dụng có thể mở.** Hãy mở mã nguồn cái không làm bạn khác biệt; bảo vệ cái làm vậy.
- **Copyleft có hệ quả.** Hãy hiểu nghĩa vụ có đi có lại trước khi nhúng mã copyleft vào sản phẩm bạn phân phối.
- **Một cộng đồng sống là tài sản; một kho bị bỏ rơi là gánh nặng.** Đánh giá dự án, không chỉ giấy phép.

## Khuyến nghị

### Đánh giá thành phần theo dự án, không chỉ giấy phép

Trước khi áp dụng bất kỳ phụ thuộc nào, mã nguồn mở hay độc quyền, hãy đánh giá sức khỏe của nó: nhịp phát hành, số lượng và sự đa dạng của người bảo trì, khả năng đáp ứng báo cáo bảo mật, và độ rộng áp dụng. Một thư viện mã nguồn mở một người bảo trì và một nhà cung cấp độc quyền nhỏ mang cùng **rủi ro hệ số xe buýt** (nguy cơ một dự án sụp đổ nếu một hay vài người then chốt rời đi). Ưu tiên các thành phần có cơ sở người đóng góp rộng hoặc nhà cung cấp vững mạnh tài chính, và ghi lại đánh giá như một phần của thẩm định (chương 10.2, 4.2).

### Đọc và theo dõi giấy phép như nghĩa vụ hạng nhất

Hãy duy trì bản kiểm kê mọi thành phần và giấy phép của nó, và thực thi chính sách về họ giấy phép nào chấp nhận được cho mục đích nào. Phân biệt then chốt là copyleft. Mã **cho phép rộng rãi** (MIT, Apache 2.0) nhìn chung có thể nhúng tự do vào sản phẩm đóng. **Copyleft mạnh** (GPL) có thể buộc bạn phát hành bản phái sinh được phân phối của chính mình theo cùng điều khoản. Dùng **phân tích thành phần phần mềm (SCA)** tự động, công cụ quét phụ thuộc của bạn để nhận diện thành phần, giấy phép và lỗ hổng đã biết, và tạo **danh mục vật liệu phần mềm (SBOM)**, danh sách chính thức mọi thành phần trong một sản phẩm (chương 10.3, 4.2).

### Đánh giá bảo mật theo thực hành, không theo độ cởi mở

Đừng giả định mã nguồn mở an toàn nhờ **lập luận "nhiều con mắt"** ([Định luật Linus](https://en.wikipedia.org/wiki/Linus%27s_law): "đủ nhiều con mắt thì mọi lỗi đều nông"). Và đừng giả định mã độc quyền an toàn nhờ **[bảo mật bằng che giấu](https://en.wikipedia.org/wiki/Security_through_obscurity)** (niềm tin sai lầm rằng giấu mã nguồn thì giấu được khiếm khuyết). Nhiều con mắt chỉ giúp nếu người có năng lực thực sự nhìn, và nhiều dự án được dùng rộng rãi được bảo trì mỏng. Cả hai mô hình mang **rủi ro chuỗi cung ứng**: mã nguồn mở qua phụ thuộc bị xâm phạm hoặc bị bỏ rơi, độc quyền qua mã khó hiểu và kênh cập nhật mà bạn không kiểm tra được. Hãy ghim phiên bản, xác minh nguồn gốc, quét liên tục, và theo dõi khuyến cáo bất kể mô hình (chương 4.2).

### Thiết kế cho lối thoát và khả năng tương tác

Ưu tiên các thành phần nói tiêu chuẩn mở và định dạng dữ liệu di chuyển được, để bạn thay chúng sau này (chương 3.8, 10.11). Với mã nguồn mở bạn có lối thoát tối thượng: nếu dự án đình trệ, bạn có thể **[rẽ nhánh](https://en.wikipedia.org/wiki/Fork_(software_development))** nó (tạo và duy trì bản sao của riêng bạn). Với phần mềm độc quyền, hãy thương lượng bảo vệ từ đầu: xuất dữ liệu ở định dạng mở, API có tài liệu, và **[ký quỹ mã nguồn](https://en.wikipedia.org/wiki/Source_code_escrow)** (thỏa thuận pháp lý nơi nhà cung cấp gửi mã nguồn cho bên thứ ba, được giao cho bạn nếu nhà cung cấp thất bại). Hãy thiết kế để không thành phần đơn lẻ nào, thuộc loại nào, giữ được hệ thống của bạn làm con tin.

### Cân nhắc tổng chi phí sở hữu, không phải giá niêm yết

Hãy so sánh các phương án theo **tổng chi phí sở hữu (TCO)**, chi phí toàn vòng đời đầy đủ gồm mua lại, tích hợp, vận hành, hỗ trợ, đào tạo, nâng cấp và thay thế cuối cùng, thay vì chỉ phí giấy phép. Mã nguồn mở thường đổi chi phí cấp phép lấy chi phí vận hành và nhân sự cao hơn. Phần mềm độc quyền thường đổi phí thuê bao khả đoán lấy khóa chặt và ít kiểm soát hơn. Hãy tính chi phí của chính mô hình: mã nguồn mở tự hỗ trợ cần kỹ năng nội bộ, trong khi phần mềm độc quyền cần năng lực quản lý nhà cung cấp.

### Với tư cách nhà sản xuất, hãy mở mã nguồn cái không làm bạn khác biệt

Hãy phân loại phần mềm của chính bạn thành cái mang lại lợi thế cạnh tranh hay sứ mệnh và cái là hạ tầng không tạo khác biệt. Giữ yếu tố tạo khác biệt độc quyền. Cân nhắc mở mã nguồn hạ tầng thông dụng, nơi một cộng đồng có thể chia sẻ bảo trì và cải thiện. Với chính phủ, hãy cân nhắc **"tiền công, mã công"** (nguyên tắc rằng phần mềm do người đóng thuế tài trợ nên công khai theo mặc định) như động lực của minh bạch, tái sử dụng và chủ quyền (chương 10.5, 10.11). Chọn giấy phép có chủ đích: cho phép rộng rãi để tối đa hóa áp dụng, copyleft để giữ hệ sinh thái mở.

## Đánh đổi: ưu và nhược điểm

| Chiều | Mã nguồn mở | Đóng / độc quyền |
|---|---|---|
| **Chi phí mua lại** | Thường bằng không | Phí giấy phép hoặc thuê bao |
| **Tổng chi phí sở hữu** | Chi phí chuyển sang vận hành và nhân sự | Khả đoán hơn, nhưng phí khóa chặt |
| **Kiểm soát & tùy biến** | Đầy đủ: bạn đọc và đổi được mã nguồn | Giới hạn ở những gì nhà cung cấp phơi ra |
| **Hỗ trợ & trách nhiệm giải trình** | Cộng đồng, hoặc bên thứ ba trả phí; không có một đầu mối duy nhất để chịu trách nhiệm | Hỗ trợ theo hợp đồng và một bên chịu trách nhiệm rõ ràng |
| **Tư thế bảo mật** | Kiểm toán được; "nhiều con mắt" nếu thực sự được bảo trì | Do nhà cung cấp quản lý; khó hiểu; che giấu không phải bảo vệ |
| **Tuổi thọ / bị bỏ rơi** | Rẽ nhánh được nếu được bảo trì; vẫn có thể héo úa | Phụ thuộc khả năng tồn tại và lộ trình của nhà cung cấp |
| **Khóa chặt nhà cung cấp** | Thấp: mã nguồn và định dạng mở cho phép thoát | Cao trừ khi được giảm nhẹ bằng tiêu chuẩn và ký quỹ |
| **Hệ sinh thái** | Cộng đồng mở và khả năng tương tác | Được tuyển chọn, tích hợp, đôi khi có tường chắn |

Căng thẳng lặp lại là **kiểm soát so với tiện lợi và trách nhiệm giải trình**. Mã nguồn mở tối đa hóa kiểm soát, khả năng kiểm toán và tự do khỏi khóa chặt, nhưng nó đòi bạn tự cung cấp năng lực, tích hợp và hỗ trợ. Phần mềm độc quyền giao một sản phẩm được hỗ trợ, tích hợp, chịu trách nhiệm với hợp đồng để thực thi, nhưng nó nhượng kiểm soát và mời gọi khóa chặt. Cách giải quyết hiếm khi là tất cả-hoặc-không. Hầu hết tài sản trưởng thành pha trộn nền tảng mã nguồn mở với hệ thống độc quyền nơi hỗ trợ, trách nhiệm giải trình hay năng lực chuyên biệt biện minh cho đánh đổi.

## Câu hỏi để thảo luận với đội của bạn

1. **Chúng ta có thực thi chính sách giấy phép với SCA tự động và SBOM trong đường ống không, đặc biệt để bắt copyleft mạnh trước khi nó được phát hành?** Nhúng một thư viện GPL vào sản phẩm độc quyền được phân phối có thể buộc bạn phát hành mã nguồn của chính mình, và bất ngờ đó thường nổi lên muộn, khi tốn kém để gỡ. Hãy duy trì bản kiểm kê mọi thành phần và giấy phép của nó, thực thi họ giấy phép nào chấp nhận được cho mục đích nào, và chạy phân tích thành phần phần mềm tự động để đường ống chặn vi phạm thay vì để luật sư bắt chúng lúc phát hành. Tạo SBOM như lẽ thường. Với tài sản lớn hay chính phủ, đây cũng là vệ sinh chuỗi cung ứng và thường là yêu cầu mua sắm. Hãy mang bản kiểm kê giấy phép hiện tại của bạn, hoặc thực tế là bạn không có, và quyết định ai sở hữu chính sách.

2. **Khi chúng ta áp dụng một phụ thuộc, chúng ta có đánh giá sức khỏe dự án và hệ số xe buýt như thẩm định không?** Một thư viện mã nguồn mở một người bảo trì và một nhà cung cấp độc quyền nhỏ mang cùng rủi ro: dự án sụp đổ nếu một hay vài người then chốt rời đi. Trước khi áp dụng bất cứ thứ gì, hãy đánh giá nhịp phát hành, số lượng và sự đa dạng của người bảo trì, khả năng đáp ứng báo cáo bảo mật, và độ rộng áp dụng, và ghi lại đánh giá. Không mô hình nào an toàn hơn theo mặc định; "nhiều con mắt" chỉ giúp nếu người có năng lực thực sự nhìn, và nhiều dự án được dùng rộng rãi được bảo trì mỏng. Hãy mang ba bốn phụ thuộc sản phẩm của bạn dựa vào nhiều nhất và hỏi, với mỗi cái, bao nhiêu người phải bỏ đi trước khi nó thành vấn đề của bạn. Nếu bạn không trả lời được, đó là đánh giá bạn nợ chính mình.

3. **Khi chúng ta mua phần mềm độc quyền, chúng ta có bảo đảm bảo vệ lối thoát từ đầu không?** Phần mềm độc quyền cung cấp trách nhiệm giải trình và tiện lợi đổi lấy kiểm soát, và chi phí ẩn là khóa chặt: chi phí chuyển đổi cho phép nhà cung cấp tăng giá hay làm giảm dịch vụ với ít kháng nghị. Hãy thương lượng các bảo vệ trước khi bạn ký, khi bạn còn đòn bẩy: xuất dữ liệu ở định dạng mở, API có tài liệu, và ký quỹ mã nguồn giao mã nguồn nếu nhà cung cấp thất bại. Với mã nguồn mở lối thoát của bạn là khả năng rẽ nhánh; với độc quyền bạn phải viết lối thoát vào hợp đồng. Hãy mang các hệ thống độc quyền trọng yếu nhất của bạn và hỏi chuyện gì thực sự xảy ra nếu nhà cung cấp tăng gấp đôi giá hoặc phá sản. Nếu câu trả lời là "chúng ta bị kẹt," hãy sửa hợp đồng lúc gia hạn.

4. **Với phần mềm chúng ta tự xây, chúng ta quyết định thế nào cái gì mở mã nguồn và cái gì giữ đóng, và ai giữ thẩm quyền đưa ra quyết định đó?** Làm sai theo một hướng và bạn trao đi chính mã tạo khác biệt cho bạn; làm sai theo hướng kia và bạn tích trữ hạ tầng thông dụng mà một cộng đồng sẽ sẵn lòng chia sẻ bảo trì. Áp lực đối lập là thật: kỹ sư muốn lợi ích tuyển dụng và danh tiếng của kho công khai, trong khi sản phẩm và pháp lý lo trao cho đối thủ lợi thế hay làm lộ một heuristic nhạy cảm bảo mật. Hãy mang phân loại trung thực các hệ thống của bạn thành tạo khác biệt sứ mệnh so với hạ tầng không tạo khác biệt, và nêu tên người hay hội đồng ký duyệt một bản phát hành, vì quyết định tùy nghi do ai đẩy kho lên đưa ra là cách viên ngọc quý bị rò rỉ. Với doanh nghiệp lớn câu hỏi là chiến lược danh mục, và với chính phủ nó va chạm "tiền công, mã công," nguyên tắc rằng phần mềm do người đóng thuế tài trợ nên công khai theo mặc định, nên hãy quyết định trước những ngoại lệ nào (an ninh quốc gia, phát hiện gian lận, dữ liệu cá nhân) biện minh cho việc giữ mã đóng.

5. **Các so sánh xây-hay-mua của chúng ta có nắm bắt tổng chi phí sở hữu đầy đủ, hay chúng ta vẫn coi phí giấy phép bằng không là chi phí bằng không?** Sai lầm tài chính phổ biến nhất với mã nguồn mở là đọc "miễn phí để có" thành "miễn phí để chạy," rồi phát hiện tích hợp, vận hành, ứng phó bảo mật và hỗ trợ trả phí lấn át bất kỳ giấy phép nào bạn đã tránh. Căng thẳng là thuê bao độc quyền trông đắt trên hóa đơn trong khi giấu phí khóa chặt, và thành phần mở trông miễn phí trên hóa đơn trong khi chuyển chi phí sang nhân sự của chính bạn. Hãy mang mô hình TCO cùng cơ sở cho hai ba quyết định thật: mua lại, tích hợp, vận hành, hỗ trợ, đào tạo, nâng cấp, ứng phó bảo mật, và thay thế cuối cùng, được định giá qua toàn bộ vòng đời thay vì năm đầu. Trong tài sản doanh nghiệp hay chính phủ, hãy thêm chi phí của chính mô hình vận hành, vì mã nguồn mở tự hỗ trợ đòi kỹ năng nội bộ bạn phải tuyển và giữ, và coi một phép so sánh bỏ qua những dòng đó là bằng chứng, không phải phân tích.

6. **Chúng ta đánh giá bảo mật của một thành phần theo thực hành, hay dựa vào nhãn cởi mở, dù là "nhiều con mắt" hay bí mật của mã đóng?** Cả hai mặc định đều là cái bẫy: "nhiều con mắt" chỉ bảo vệ bạn khi người có năng lực thực sự rà soát mã, và nhiều dự án mở được dùng rộng rãi chạy nhờ một người bảo trì kiệt sức, trong khi mã đóng dựa vào việc kẻ tấn công không thấy là bảo mật bằng che giấu, không phải kiểm soát. Cuộc tranh luận quan trọng vì nó đổi nơi bạn tiêu nỗ lực bảo mật khan hiếm, và câu trả lời trung thực là cả hai mô hình mang rủi ro chuỗi cung ứng, mã nguồn mở qua phụ thuộc bị xâm phạm hoặc bị bỏ rơi và độc quyền qua kênh cập nhật khó hiểu bạn không kiểm tra được. Hãy mang bằng chứng cho các thành phần trọng yếu nhất của bạn: ai thực sự rà soát chúng, khuyến cáo được vá nhanh thế nào, phiên bản có được ghim và nguồn gốc có được xác minh không, và bạn có tạo SBOM không. Với tài sản lớn hay chính phủ, hãy gắn điều này với nghĩa vụ mua sắm và quét liên tục, vì cơ quan quản lý sẽ hỏi bạn đã kiểm tra gì, không phải mã nguồn có công khai không.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Với ít đường băng bạn xây trên nền tảng mã nguồn mở vì không đủ sức trả phí giấy phép và muốn tự do rẽ nhánh nếu dự án đình trệ. Hãy chạy quét phân tích thành phần trước khi phát hành để một thư viện copyleft mạnh không lặng lẽ buộc bạn công bố mã nguồn của mình, và giữ yếu tố tạo khác biệt thực sự duy nhất của bạn đóng hoàn toàn. Mở mã nguồn một công cụ nhỏ, không trọng yếu nếu nó giúp tuyển dụng, nhưng đừng bố trí nhân sự cho gánh nặng bảo trì mà bạn không gánh nổi.

**Doanh nghiệp nhỏ.** Không có chuyên gia pháp lý hay nền tảng nội bộ, hãy coi giấy phép là rủi ro bạn không được đọc sai hơn là chủ đề bạn có thể làm chủ. Ưu tiên các công cụ độc quyền được hỗ trợ hoặc bản phân phối mã nguồn mở thương mại nơi nhà cung cấp sở hữu bản vá và trách nhiệm giải trình, vì tự hỗ trợ một ngăn xếp bạn không vận hành được là tiết kiệm giả. Khi bạn áp dụng thành phần miễn phí, hãy kiểm tra giấy phép của nó cho phép bạn sử dụng và dự án thực sự được bảo trì, không bị bỏ rơi.

**Doanh nghiệp lớn.** Ở quy mô, vấn đề là nhất quán qua nhiều đội: chính sách giấy phép bằng văn bản, phân tích thành phần phần mềm tự động và tạo SBOM trong mọi đường ống, và quyết định xây-hay-mua dựa trên TCO thay vì thói quen theo từng đội. Hãy quản lý phần mềm mở và độc quyền như một danh mục, chuẩn hóa bảo vệ lối thoát như định dạng mở và ký quỹ mã nguồn trong mua sắm, và theo dõi sức khỏe các phụ thuộc trọng yếu để một dự án bị bỏ rơi duy nhất không thành sự cố. Cũng quản trị phía nhà sản xuất, với quy tắc rõ ràng về những gì tổ chức mở mã nguồn so với giữ đóng.

**Chính phủ.** Quy tắc mua sắm, nghĩa vụ minh bạch và trách nhiệm giải trình công định hình mọi lựa chọn. Hãy cân nhắc "tiền công, mã công," nguyên tắc rằng phần mềm do người đóng thuế tài trợ nên công khai theo mặc định, để thúc đẩy tái sử dụng qua các cơ quan và chủ quyền số, trong khi khoét các ngoại lệ hẹp cho mã nhạy cảm bảo mật hoặc dữ liệu cá nhân. Yêu cầu bất kỳ nhà cung cấp độc quyền nào cung cấp xuất dữ liệu ở định dạng mở và ký quỹ mã nguồn để thất bại của nhà cung cấp không bỏ rơi dịch vụ công, và công bố mã nguồn không nhạy cảm để công dân kiểm toán các quy tắc chi phối họ.

## Ví dụ

**Công ty khởi nghiệp.** Một công ty khởi nghiệp ba người sáng lập xây toàn bộ sản phẩm trên nền tảng mã nguồn mở (Linux, một cơ sở dữ liệu mã nguồn mở, một khung web) vì không đủ sức trả phí giấy phép và muốn tự do rẽ nhánh nếu một dự án đình trệ. Trước khi phát hành, một người sáng lập chạy quét phân tích thành phần và bắt được một thư viện copyleft mạnh sẽ buộc họ công bố thuật toán ghép cặp độc quyền, nên họ thay bằng bản tương đương có giấy phép cho phép rộng rãi. Họ giữ thuật toán đó, yếu tố tạo khác biệt duy nhất, đóng hoàn toàn, và chỉ mở mã nguồn một công cụ ghi nhật ký nội bộ nhỏ để xây thiện chí và thu hút kỹ sư.

**Doanh nghiệp lớn.** Một công ty bảo hiểm lớn chạy nền tảng lõi trên nền tảng mã nguồn mở: Linux, một cơ sở dữ liệu mã nguồn mở được dùng rộng rãi, và một bộ điều phối container. Nhưng nó mua một bộ mô hình hóa bảo hiểm độc quyền, vì chuyên môn lĩnh vực, chứng nhận quy định và hợp đồng hỗ trợ của nhà cung cấp đáng giá phí và không có phương án mở tương đương. Nó trả thuê bao cho **mã nguồn mở thương mại** (bản phân phối được nhà cung cấp hỗ trợ của các thành phần mở) để có trách nhiệm giải trình và bản vá trên phần hạ tầng, trong khi giữ thuật toán định giá tạo khác biệt cho nó hoàn toàn độc quyền và nội bộ. Phân tích TCO (chương 10.10) thúc đẩy mỗi lựa chọn thay vì hệ tư tưởng.

**Chính phủ.** Một cơ quan thuế quốc gia, theo chính sách "tiền công, mã công," xây dịch vụ xác định điều kiện hưởng trợ cấp mới trên thành phần mã nguồn mở và tiêu chuẩn mở (chương 3.8), để các cơ quan khác tái sử dụng được và công dân kiểm toán được các quy tắc. Nó công bố mã không nhạy cảm trong kho công khai, chỉ giữ các heuristic phát hiện gian lận đóng vì lý do bảo mật. Điều này giảm khóa chặt nhà cung cấp và thúc đẩy chủ quyền số (chương 10.11). Quy tắc mua sắm (chương 10.3) yêu cầu bất kỳ thành phần độc quyền nào cung cấp xuất dữ liệu ở định dạng mở và ký quỹ mã nguồn, để bảo đảm tính liên tục nếu nhà cung cấp thất bại.

## Luận chứng kinh doanh: động lực, ROI và TCO

Sức hấp dẫn tài chính của mã nguồn mở, việc không có phí giấy phép, là phần kém đáng tin cậy nhất của luận chứng, vì mua lại chỉ là một phần nhỏ của TCO. Các lợi tức bền vững mang tính chiến lược: tự do khỏi khóa chặt (khả năng đổi hoặc bỏ nhà cung cấp mà không phải tái kiến trúc), khả năng kiểm toán cho bảo mật và tuân thủ, áp dụng nhanh hơn vì kỹ sư có thể thử trước khi cam kết, và bảo trì chung cho mã thông dụng qua cả ngành. Các chi phí bù trừ là thật. Bạn phải cung cấp tích hợp, vận hành, ứng phó bảo mật, và thường là hỗ trợ trả phí, và một dự án không được bảo trì chọn kém có thể tốn nhiều sự cố hơn bất kỳ giấy phép nào.

Luận chứng kinh doanh của phần mềm độc quyền là trách nhiệm giải trình và tiện lợi: một nhà cung cấp duy nhất chịu trách nhiệm về sản phẩm, hợp đồng hỗ trợ bạn có thể thực thi, tính năng tích hợp, và ngân sách khả đoán. Chi phí ẩn của nó là khóa chặt, chi phí chuyển đổi cho phép nhà cung cấp tăng giá hay làm giảm dịch vụ với ít kháng nghị, cộng sự phụ thuộc vào khả năng thanh toán và lộ trình của nhà cung cấp. Các **mô hình kinh doanh** phổ biến làm mờ ranh giới: **[lõi mở](https://en.wikipedia.org/wiki/Open-core_model)** (nền tảng mở với phần bổ sung độc quyền trả phí), **cấp phép kép** (cùng mã được cung cấp theo cả giấy phép copyleft và giấy phép thương mại trả phí), **[phần mềm như một dịch vụ](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (phần mềm chạy như dịch vụ lưu trữ bạn thuê, nơi mã nguồn có thể không liên quan vì bạn không bao giờ sở hữu bản nhị phân), và mô hình **hỗ trợ/thuê bao** bán dịch vụ xung quanh mã vốn miễn phí.

Với nhà sản xuất, ROI của việc **mở mã nguồn phần mềm không tạo khác biệt của chính bạn** có thể đáng kể. Người đóng góp bên ngoài giảm tải bảo trì của bạn. Dự án trở thành tài sản tuyển dụng và danh tiếng. Áp dụng bên ngoài làm tiêu chuẩn của bạn thành tiêu chuẩn thực tế. Với chính phủ, nó mang lại minh bạch và tái sử dụng qua khu vực công. Quy tắc chiến lược đơn giản: mở mã nguồn hàng hóa thông dụng để chia sẻ chi phí và nuôi hệ sinh thái, và giữ yếu tố tạo khác biệt đóng để bảo vệ lợi thế tài trợ cho mọi thứ khác.

## Phản mẫu và cạm bẫy

- **"Miễn phí nghĩa là miễn phí":** coi chi phí mua lại bằng không là TCO bằng không, rồi tài trợ thiếu vận hành và hỗ trợ.
- **Mù giấy phép:** nhúng mã copyleft mạnh vào sản phẩm độc quyền được phân phối và kích hoạt nghĩa vụ bạn chưa bao giờ lên kế hoạch.
- **Niềm tin vào "nhiều con mắt":** giả định một dự án mở đã được kiểm toán khi nó có một người bảo trì làm việc quá sức và không rà soát bảo mật.
- **Bảo mật bằng che giấu:** tin mã đóng an toàn đơn giản vì kẻ tấn công không đọc được nó.
- **Chủ nghĩa tuyệt đối hệ tư tưởng:** bắt buộc "tất cả mở" hay "tất cả độc quyền" thay vì chọn từng thành phần theo ưu điểm và TCO.
- **Phớt lờ nguồn gốc:** kéo phụ thuộc không có SBOM, ghim phiên bản hay xác minh chuỗi cung ứng (chương 4.2).
- **Mở mã nguồn viên ngọc quý:** phát hành chính mã tạo khác biệt cho bạn, trao đi lợi thế của mình.
- **Rẽ nhánh rồi quên:** rẽ nhánh một dự án bị bỏ rơi mà không có năng lực thực sự bảo trì bản rẽ nhánh.

## Mô hình trưởng thành

**Mức 1 (Khởi đầu).** Thành phần mã nguồn mở và độc quyền vào tài sản tùy nghi. Giấy phép không được đọc, không có bản kiểm kê hay SBOM, và lựa chọn giữa các mô hình được đưa ra theo thói quen hoặc chỉ theo giá. Rủi ro bị bỏ rơi và giấy phép chỉ nổi lên khi có gì đó hỏng, và mỗi đội phản ứng riêng.

**Mức 2 (Phát triển).** Một số đội bắt đầu thực hành cơ bản: bản kiểm kê thành phần và giấy phép, cái nhìn thô về giấy phép chấp nhận được, và phân tích thành phần phần mềm thỉnh thoảng. Quyết định xây-hay-mua và mở-hay-đóng được viết xuống, nhưng kỷ luật chắp vá và không nhất quán giữa các đội, nên bất ngờ về copyleft hay hệ số xe buýt vẫn có thể lọt qua nơi thói quen chưa bén rễ.

**Mức 3 (Chuẩn hóa).** Một khung có tài liệu chi phối cả tiêu thụ lẫn sản xuất toàn tổ chức. Thành phần được chọn theo TCO và sức khỏe dự án, giấy phép được thực thi tự động trong đường ống để vi phạm chặn bản dựng, SBOM được tạo như lẽ thường, và một chính sách tường minh nêu tổ chức mở mã nguồn gì so với giữ đóng gì. Bảo vệ lối thoát như định dạng mở và ký quỹ mã nguồn là tiêu chuẩn trong mua sắm, và mọi đội theo cùng quy tắc thay vì quy tắc riêng.

**Mức 4 (Quản lý).** Chương trình được đo và kiểm soát theo đường cơ sở. Tổ chức theo dõi các chỉ số như độ phủ SBOM qua các sản phẩm, tỷ lệ phụ thuộc vi phạm chính sách, thời gian trung bình để vá một lỗ hổng phụ thuộc đã công bố, điểm hệ số xe buýt và sức khỏe cho dự án trọng yếu, và TCO thực hiện so với ước tính đã biện minh cho mỗi lựa chọn. Ngưỡng kích hoạt hành động: một thành phần có bảo trì đình trệ hoặc độ trễ vá trôi quá mục tiêu bị gắn cờ thay thế dựa trên bằng chứng, và quyết định mở-hay-đóng và xây-hay-mua được xem xét theo con số thay vì bảo vệ theo thói quen.

**Mức 5 (Điều phối).** Chiến lược mã nguồn mở là năng lực kinh doanh có chủ đích, tích hợp trong toàn tổ chức và cải thiện liên tục. Tổ chức đóng góp cho và đôi khi quản gia các dự án nó phụ thuộc, mở mã nguồn phần mềm không tạo khác biệt của mình như lẽ thường, và đưa dữ liệu sức khỏe phụ thuộc và TCO ngược vào mua sắm, bảo mật và hoạch định sản phẩm. Nó thường lệ cân bằng lại danh mục phần mềm mở và độc quyền, thích ứng với các dịch chuyển về chi phí, rủi ro, chủ quyền và lợi thế chiến lược trước khi chúng buộc thành khủng hoảng.

## Ý tưởng để thảo luận

- Ở đâu trong tài sản của bạn việc mất một nhà cung cấp hay người bảo trì duy nhất sẽ là sinh tử, và kế hoạch thoát của bạn là gì?
- Hệ thống nào của chính bạn là hàng hóa thông dụng bạn có thể mở mã nguồn, và cái nào là yếu tố tạo khác biệt thật cần bảo vệ?
- Tổ chức của bạn coi "nhiều con mắt" là kiểm soát bảo mật thật hay giả định chưa được xem xét?
- Với độc giả khu vực công: mặc định "tiền công, mã công" sẽ đổi gì trong lần mua sắm tiếp theo của bạn?
- So sánh TCO của bạn nắm bắt tốt đến đâu chi phí vận hành và hỗ trợ mà mã nguồn mở chuyển sang bạn?

## Những điểm cần ghi nhớ

- **Mở so với đóng được định nghĩa bởi giấy phép**, không phải giá; hãy biết sự khác biệt giữa miễn phí theo nghĩa tự do và miễn phí theo nghĩa giá cả, và giữa cho phép rộng rãi và copyleft.
- **Không mô hình nào vốn dĩ an toàn hơn hay rẻ hơn.** Đánh giá thực hành của dự án và TCO đầy đủ của nó, không phải nhãn cởi mở.
- **Cởi mở là thuốc giải mạnh nhất cho khóa chặt**, mang lại khả năng kiểm toán, di chuyển và khả năng rẽ nhánh; phần mềm độc quyền cung cấp trách nhiệm giải trình và tiện lợi đổi lấy kiểm soát.
- **Quyết định từng thành phần theo ưu điểm**, và pha trộn mô hình có chủ đích thay vì theo hệ tư tưởng.
- **Với tư cách nhà sản xuất, hãy mở mã nguồn hàng hóa thông dụng và giữ yếu tố tạo khác biệt đóng**, và trong chính phủ, cân nhắc "tiền công, mã công" cho minh bạch, tái sử dụng và chủ quyền.

## Tài liệu tham khảo và đọc thêm

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft và những người khác, các đầu sách O'Reilly về chiến lược và vận hành mã nguồn mở
- Free Software Foundation, *The Free Software Definition* (và các văn bản Giấy phép Công cộng GNU)
- Open Source Initiative, *The Open Source Definition* và danh sách giấy phép được phê duyệt
- Free Software Foundation Europe, tài liệu chiến dịch *Public Money, Public Code*
- Yochai Benkler, *The Wealth of Networks*
