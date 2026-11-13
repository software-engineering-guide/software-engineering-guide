# 11.2 Quy trình phân phối

## Tổng quan và động lực

Quy trình phân phối là dòng công việc biến một ý tưởng đã xác thực thành phần mềm đang chạy trong tay người dùng (một cách đáng tin cậy, lặp lại được và đo được) rồi đưa dữ liệu kết quả thu được ngược lại vào khám phá (chương 11.1). Đó là con đường được công nghiệp hóa từ một commit mã đến một thay đổi sản xuất đến một hiệu ứng đã đo lên người dùng và doanh nghiệp. Trong khi khám phá trả lời *cái gì và vì sao*, phân phối trả lời *chúng ta phát hành nó an toàn thế nào, nhanh đến đâu, và nó có thực sự hiệu quả không*.

Chương này cố ý mang tính tích hợp. Cơ chế nằm chi tiết ở nơi khác: chiến lược kiểm thử (chương 2.4), tự động hóa kiểm thử và quy trình (chương 8.5), [tích hợp liên tục](https://en.wikipedia.org/wiki/Continuous_integration) và [phân phối liên tục](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) và chiến lược triển khai (chương 8.1), hạ tầng dưới dạng mã (chương 8.2), độ tin cậy và SLO (mục tiêu mức dịch vụ, chương 9.1), và thí nghiệm (chương 7.4). Ở đây chúng ta lắp ráp chúng thành một quy trình đầu-cuối duy nhất và, quan trọng, gắn các **chỉ số kết quả** cho bạn biết cả cỗ máy có đang tạo ra giá trị hay chỉ đơn thuần tạo ra các bản phát hành.

Với các đội lớn, quy trình phân phối là khoản đầu tư đòn bẩy cao nhất đơn lẻ vào hiệu quả kỹ thuật. Một thập kỷ nghiên cứu, nổi bật nhất là chương trình DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) được tóm tắt trong *Accelerate*, cho thấy các đội có quy trình phân phối nhanh, tự động, rủi ro thấp vượt trội về thông lượng *và* ổn định *và* kết quả tổ chức. Niềm tin cũ rằng tốc độ và an toàn đánh đổi nhau là sai theo kinh nghiệm. Trong doanh nghiệp, một quy trình mạnh là thứ cho phép hàng trăm kỹ sư tích hợp mà không sụp vào hỗn loạn hợp nhất và sân khấu phát hành thủ công. Trong chính phủ, nó thay các bản phát hành "đại bùng nổ" nhiều nghi thức, hằng quý, được ăn cả ngã về không (lịch sử là nguyên nhân hàng đầu của các chương trình thất bại) bằng những thay đổi nhỏ, đảo ngược được, kiểm toán được, thỏa mãn nghĩa vụ kiểm soát thay đổi *thông qua* tự động hóa thay vì bất chấp nó.

## Các nguyên tắc chính

- **Tự động hóa mọi thứ lặp lại được.** Bước thủ công chậm, dễ lỗi và không kiểm toán được.
- **Lô nhỏ, phát hành thường xuyên.** Thay đổi nhỏ dễ rà soát, kiểm thử, phát hành và đảo ngược hơn.
- **Xây chất lượng vào.** Kiểm thử và cổng tự động nhanh bắt lỗi trước sản xuất, không phải sau.
- **Tách triển khai khỏi phát hành.** Phát hành mã trong bóng tối; bật tính năng bằng cờ khi sẵn sàng.
- **Làm mọi thứ đảo ngược được.** Hoàn tác nhanh và phơi bày tiến dần biến triển khai từ canh bạc thành thí nghiệm.
- **Quy trình là nguồn sự thật.** Nếu nó không có trong quản lý phiên bản và quy trình, nó đã không xảy ra.
- **Đo kết quả, không chỉ đầu ra.** Số lần triển khai là đầu ra; một chỉ số đã dịch chuyển là kết quả.

## Khuyến nghị

### Tự động hóa bộ kiểm thử và chặn cổng theo nó

Tự động hóa kiểm thử là nền tảng làm phân phối nhanh trở nên an toàn. Hãy triển khai danh mục kiểm thử cân bằng, phần lớn tự động (chương 2.4): nhiều kiểm thử đơn vị nhanh, ít kiểm thử tích hợp và hợp đồng hơn, một số ít kiểm thử đầu-cuối, cộng các kiểm tra bảo mật (SAST/DAST/SCA: phân tích tĩnh, động và thành phần phần mềm), khả năng tiếp cận và hiệu năng tự động. Chạy chúng như **cổng chất lượng** trong quy trình để không thay đổi nào đến sản xuất mà không vượt qua. Giữ bộ kiểm thử nhanh và đáng tin: một bộ chậm hoặc chập chờn bị đi vòng, đánh bại mục đích của nó (chương 8.5). Hãy nhắm quy trình cho nhà phát triển một tín hiệu đạt/trượt rõ ràng trong vài phút sau một commit.

### Thực hành tích hợp liên tục và phân phối liên tục

**Tích hợp liên tục (CI):** mỗi nhà phát triển hợp nhất các thay đổi nhỏ vào nhánh chính thường xuyên (lý tưởng hằng ngày), mỗi lần hợp nhất kích hoạt một lần dựng và chạy kiểm thử tự động. Điều này được hỗ trợ tốt nhất bởi phát triển trên thân chính (chương 2.6), giữ nhánh ngắn hạn và tích hợp liên tục. **Phân phối liên tục (CD):** mọi thay đổi vượt qua quy trình *luôn ở trạng thái có thể phát hành* và có thể triển khai theo yêu cầu. **Triển khai liên tục** đi thêm một bước: mọi thay đổi đạt đều tự động triển khai lên sản xuất. Chọn mức tự động hóa phù hợp với hồ sơ rủi ro của bạn; môi trường bị quản lý có thể dừng ở phân phối liên tục với bước thăng cấp được kiểm soát (chương 8.1), nhưng vẫn nên tự động hóa mọi thứ cho đến cổng đó.

### Triển khai an toàn bằng chiến lược tiến dần

Hãy tách **triển khai** (mã chạy trong sản xuất) khỏi **phát hành** (người dùng trải nghiệm thay đổi), và phơi bày thay đổi dần dần:

- **[Cờ tính năng](https://en.wikipedia.org/wiki/Feature_toggle)** cho phép bạn triển khai mã trong bóng tối và phát hành cho các phân khúc theo yêu cầu, và hoàn tác tức thì bằng cách chuyển cờ.
- **Phát hành canary** định tuyến một phần trăm nhỏ lưu lượng tới phiên bản mới, theo dõi chỉ số sức khỏe trước khi mở rộng.
- **Triển khai xanh-lục** giữ hai môi trường và chuyển lưu lượng nguyên tử, với hoàn tác tức thì.
- **Triển khai cuốn chiếu** thay các thể hiện dần dần.
- **Phân phối tiến dần** kết hợp cờ, canary và phân tích tự động để thăng cấp hoặc hoàn tác dựa trên tín hiệu trực tiếp.

Ghép mọi chiến lược với hoàn tác tự động được kích hoạt bởi vi phạm SLO hoặc đốt ngân sách lỗi (tốc độ các thất bại tiêu thụ ngân sách không đáng tin cậy được phép; chương 9.1). Xem chương 8.1 về cơ chế.

### Gắn công cụ đo chỉ số kết quả: đo quy trình và tác động

Một quy trình phân phối phát hành nhanh nhưng phát hành sai thứ là lãng phí nhanh. Hãy đo ở ba cấp:

1. **Dòng chảy phân phối, bốn chỉ số DORA:**
   - *Tần suất triển khai:* bạn phát hành lên sản xuất thường xuyên thế nào.
   - *[Thời gian chờ](https://en.wikipedia.org/wiki/Lead_time) cho thay đổi:* từ commit đến sản xuất.
   - *Tỷ lệ thay đổi thất bại:* phần trăm bản phát hành gây suy giảm.
   - *Thời gian khôi phục sau triển khai thất bại:* bạn khôi phục dịch vụ nhanh thế nào (trước đây là MTTR, thời gian khôi phục trung bình).
   Người hiệu suất đỉnh triển khai theo yêu cầu, với thời gian chờ dưới một giờ, tỷ lệ thất bại thấp, và khôi phục trong vài phút. Thêm **chỉ số luồng** từ tư duy dòng giá trị (thời gian chu kỳ, [công việc đang làm](https://en.wikipedia.org/wiki/Work_in_process), hiệu quả luồng) để thấy công việc chờ ở đâu.

2. **Độ tin cậy và chất lượng, SLI và SLO** (chỉ báo và mục tiêu mức dịch vụ; chương 9.1): dịch vụ có đang đáp ứng mục tiêu độ tin cậy và cam kết thuộc tính chất lượng (chương 11.1) sau mỗi thay đổi không?

3. **Kết quả kinh doanh và người dùng** (chương 7.3–7.4): thay đổi có dịch chuyển các kết quả then chốt và KPI mà khám phá đã xác định không? Đây là nơi phát hành gặp thí nghiệm: phát hành sau một cờ, đo so với nhóm đối chứng, và chỉ giữ cái thắng.

### Khép vòng lặp về khám phá

Hành động cuối của quy trình phân phối không phải triển khai; mà là **bằng chứng**. Chỉ số kết quả (kích hoạt có tăng, thời gian thanh toán có giảm, phiếu hỗ trợ có giảm) chảy ngược vào quy trình khám phá (chương 11.1) làm cơ sở cho vòng canh bạc tiếp theo. Khi khám phá và phân phối được nối bằng vòng phản hồi này, tổ chức trở thành hệ thống học: giả thuyết được phát hành, đo, và hoặc được mở rộng hoặc bị đảo ngược, liên tục.

### Làm phân phối kiểm toán được và được quản trị

Trong bối cảnh doanh nghiệp và chính phủ, hãy coi chính quy trình là một kiểm soát tuân thủ. Vì mọi thay đổi chảy qua quản lý phiên bản và quy trình tự động, bạn có được dấu vết kiểm toán bất biến "miễn phí": ai đổi gì, kiểm thử và phê duyệt nào chặn cổng nó, và khi nào nó được triển khai. Mã hóa phân tách nhiệm vụ, rà soát bắt buộc và kiểm tra chính sách thành **chính sách dưới dạng mã** (quy tắc quản trị diễn đạt dưới dạng máy thực thi được, được quản lý phiên bản; chương 8.2) để kiểm soát thay đổi được thực thi tự động và chứng minh liên tục (chương 4.6 và 10.2), thay vì dựng lại thủ công trước kiểm toán.

## Đánh đổi: ưu và nhược điểm

| Quyết định | Ưu điểm | Nhược điểm |
|---|---|---|
| **Triển khai liên tục (tự động lên sản xuất)** | Phản hồi nhanh nhất; lô nhỏ nhất; ít lao động thủ công nhất | Đòi kiểm thử, giám sát, hoàn tác trưởng thành; khó với cổng bị quản lý |
| **Phân phối liên tục với thăng cấp thủ công** | Điểm kiểm soát con người/tuân thủ; thân thiện kiểm toán | Chậm hơn; rủi ro dồn thay đổi lại ở cổng |
| **Cờ tính năng** | Tách triển khai/phát hành; hoàn tác tức thì; nhắm mục tiêu | Nợ cờ và độ phức tạp tổ hợp nếu không tỉa |
| **Canary / phân phối tiến dần** | Giới hạn bán kính ảnh hưởng; thăng cấp dựa trên dữ liệu | Cần khả năng quan sát mạnh và quản lý lưu lượng |
| **Xanh-lục** | Chuyển và hoàn tác tức thì | Nhân đôi chi phí môi trường; di chuyển có trạng thái/dữ liệu phức tạp |
| **Quy trình phát hành thủ công nặng** | Cảm giác được kiểm soát; quen với kiểm toán viên | Chậm, dễ lỗi, không tái tạo được, kiểm toán kém trong thực tế |

Niềm tin đánh đổi lịch sử, *đi nhanh hơn thì bạn sẽ làm hỏng nhiều hơn*, là cái then chốt cần cho nghỉ hưu. Bằng chứng cho thấy các thực hành tăng tốc độ (tự động hóa, lô nhỏ, kiểm thử nhanh, khả năng đảo ngược) là *chính* các thực hành tăng sự ổn định. Các đánh đổi thật là về **đầu tư và độ chi tiết kiểm soát**, không phải tốc độ-so-với-an-toàn.

## Câu hỏi để thảo luận với đội của bạn

1. **Hồ sơ rủi ro thực của bạn là gì, và nó có biện minh cho việc dừng ở phân phối liên tục thay vì đi đến triển khai liên tục không?** Chọn mức tự động hóa là quyết định thật, không phải mặc định. Triển khai liên tục cho phản hồi nhanh nhất và lô nhỏ nhất, nhưng nó đòi kiểm thử trưởng thành, khả năng quan sát mạnh và hoàn tác tức thì, nên bối cảnh bị quản lý có thể hợp lý dừng ở cổng thăng cấp được kiểm soát. Hãy mang bằng chứng: tỷ lệ thay đổi thất bại, thời gian khôi phục, và độ đáng tin của bộ kiểm thử của bạn, vì chúng cho bạn biết tự động-lên-sản-xuất có an toàn hôm nay không. Với doanh nghiệp và chính phủ, hãy tự động hóa mọi thứ cho đến cổng và làm chính cổng thành chính sách dưới dạng mã, để bước của con người thêm kiểm soát mà không thêm lao động thủ công. Nếu bạn chưa tin quy trình bắt được một thay đổi tệ, hãy đầu tư vào cổng và khả năng quan sát trước khi bật công tắc.

2. **Quy trình của bạn có tạo được bằng chứng kiểm toán mà cơ quan quản lý sẽ hỏi, mà không ai phải dựng lại bằng tay không?** Hãy coi chính quy trình là một kiểm soát tuân thủ. Mỗi thay đổi nên mang dấu vết bất biến về ai đổi gì, kiểm thử và phê duyệt nào chặn cổng nó, và khi nào nó được triển khai, được tạo tự động. Trong doanh nghiệp và chính phủ, hãy mã hóa phân tách nhiệm vụ và rà soát bắt buộc thành chính sách dưới dạng mã để kiểm soát thay đổi được thực thi và chứng minh liên tục thay vì được lắp trong hoảng loạn trước kiểm toán. Tín hiệu cần mang: chọn một thay đổi sản xuất gần đây và thử tạo toàn bộ dấu vết phê duyệt-và-kiểm thử của nó trong năm phút. Nếu bạn không làm được, bạn đang trả tiền cho chuẩn bị kiểm toán thủ công và mang rủi ro mà tự động hóa sẽ loại bỏ.

3. **Khi một bản phát hành bắt đầu suy giảm trong sản xuất, cái gì kích hoạt hoàn tác, và nó có tự động không?** Khả năng đảo ngược là thứ làm tốc độ hợp lý thay vì liều lĩnh, nên kích hoạt hoàn tác xứng đáng được thiết kế tường minh. Hãy quyết định liệu vi phạm SLO hay đốt ngân sách lỗi có hoàn tác tự động, hay một con người phải nhận ra, quyết định và hành động trong khi người dùng chịu khổ. Hãy mang vài sự cố gần nhất của bạn và đo khoảng cách giữa "chỉ số bắt đầu suy giảm" và "thay đổi bị đảo ngược"; khoảng cách đó là bán kính ảnh hưởng thật của bạn. Với đội lớn phát hành nhiều lần mỗi ngày, hoàn tác thủ công không mở rộng, và cờ cộng phân tích canary cho phép bạn thăng cấp hoặc đảo ngược dựa trên tín hiệu trực tiếp. Nếu câu trả lời của bạn là "ai đó bị gọi và tìm ra cách," bạn đang coi mỗi lần triển khai là canh bạc không đảo ngược.

4. **Khi bạn phát hành một tính năng, bạn có đo liệu nó có thực sự dịch chuyển chỉ số nó được định dịch chuyển, hay đếm lần triển khai rồi đi tiếp?** Một quy trình phát hành nhanh mà không bao giờ kiểm tra tác động là lãng phí nhanh, và khoảng cách giữa đầu ra và kết quả là nơi phần lớn đầu tư phân phối lặng lẽ rò rỉ. Với tổ chức lớn, hàng trăm bản phát hành mỗi tuần khiến cám dỗ coi tần suất triển khai là bảng điểm, vậy mà tần suất đo chuyển động, không phải giá trị; lực kéo đối lập là đo kết quả tốn công cụ đo, nhóm đối chứng, và kỷ luật để một tính năng thua ở trạng thái tắt. Hãy mang vài tính năng đã phát hành gần nhất và, với mỗi cái, chỉ số mục tiêu khám phá đã xác định, đo trước-và-sau, và bạn đã làm gì khi nó không dịch chuyển. Trong danh mục doanh nghiệp và chính phủ, hãy nêu ai xem xét kết quả theo nhịp cố định và ai có thẩm quyền cho nghỉ hưu một tính năng đã phát hành nhưng không bao giờ sinh lời, vì một thay đổi không ai chịu trách nhiệm đo là thay đổi không ai sẽ tắt. Phép thử trung thực là liệu bạn có chỉ ra được một tính năng bạn đã đảo ngược *vì* bằng chứng nói nó thua.

5. **Quy trình của bạn mất bao lâu để cho nhà phát triển tín hiệu đạt/trượt, và họ có đủ tin kiểm thử để không đi vòng chúng không?** Tốc độ phản hồi và lòng tin vào bộ kiểm thử là thứ làm cổng chất lượng thực sự chặn thay vì bị đi vòng, và cả hai xói mòn âm thầm khi cơ sở mã lớn lên. Với đội lớn, một bộ chạy bốn mươi phút hoặc chập chờn một lần trong mười lần dạy hàng trăm kỹ sư hợp nhất khi đỏ, tắt kiểm tra, hay chạy lại đến khi xanh, lặng lẽ loại bỏ sự an toàn từng biện minh cho việc đi nhanh ngay từ đầu; cân nhắc đối lập là độ phủ và tính thực của kiểm thử so với tốc độ phản hồi và độ ổn định, và đẩy cái nào quá mức làm suy yếu cái kia. Hãy mang thời lượng quy trình hiện tại, tỷ lệ chạy lại do chập chờn, và bất kỳ bằng chứng nào về cổng bị bỏ qua hoặc đánh dấu không chặn. Trong bối cảnh doanh nghiệp và chính phủ nơi các cổng đó cũng mang SAST, DAST và kiểm tra chính sách thỏa mãn tuân thủ, một cổng bị đi vòng vừa là rủi ro chất lượng vừa là khoảng trống kiểm toán, nên hãy đo liệu cổng thực sự bắt buộc hay chỉ mang tính khuyến nghị. Nếu nhà phát triển không nêu được vì sao họ tin một bản dựng xanh, cổng chỉ là đồ trang trí.

6. **Ai sở hữu việc giữ con đường phân phối nhất quán qua các đội và tỉa nợ cờ tính năng, hay mỗi đội đang phát minh lại quy trình của riêng mình?** Khi một tổ chức lớn lên, phân phối hoặc hội tụ về một con đường lát sẵn dùng chung hoặc phân mảnh thành hàng chục quy trình riêng với cổng không tương thích, dấu vết kiểm toán không đồng đều, và cờ sống lâu hơn mục đích của chúng. Căng thẳng là thật: một con đường lát sẵn trung tâm cho bạn sự nhất quán, quản trị và hiệu quả theo quy mô, nhưng một mệnh lệnh phớt lờ ràng buộc thực của đội sinh ra quy trình bóng và oán giận, nên con đường lát sẵn phải đủ tốt để các đội sẵn lòng tham gia. Hãy mang bản kiểm kê có bao nhiêu quy trình riêng biệt tồn tại hôm nay, việc tạo và loại bỏ cờ được quản trị thế nào, và thời gian chờ cùng chất lượng kiểm toán khác nhau bao nhiêu giữa đội tốt nhất và tệ nhất của bạn. Trong bối cảnh doanh nghiệp và chính phủ, hãy thêm góc tuân thủ: quy trình không nhất quán nghĩa là bằng chứng phân tách nhiệm vụ và kiểm soát thay đổi được chứng minh khác nhau (hoặc không) ở mỗi đội, và một con đường lát sẵn được kiểm toán duy nhất với chính sách dưới dạng mã biến điều đó từ canh bạc theo từng đội thành đảm bảo của tổ chức. Nếu không ai sở hữu việc loại bỏ cờ cũ, nợ tổ hợp cuối cùng sẽ làm hệ thống không kiểm thử được.

## Góc nhìn theo lĩnh vực

**Công ty khởi nghiệp.** Tốc độ là sinh tồn, nên hãy mua quy trình thay vì xây: nối phát triển trên thân chính với một bộ chạy CI lưu trữ, chặn cổng mọi lần hợp nhất bằng kiểm thử đơn vị nhanh và quét bảo mật, và triển khai thẳng lên sản xuất sau một dịch vụ cờ tính năng lưu trữ. Bỏ qua đội nền tảng và công cụ riêng; nguồn lực khan hiếm nhất của bạn là sự chú ý của kỹ sư, và một quy trình một nhà phát triển đa năng bảo trì được thắng một quy trình cầu kỳ không ai có thời gian sửa. Theo dõi bốn chỉ số DORA trên bảng điều khiển đơn giản từ ngày đầu để bạn học luồng của mình sớm và cho nhà đầu tư thấy bạn phát hành hằng ngày mà không làm hỏng gì.

**Doanh nghiệp nhỏ.** Không có kỹ sư phát hành riêng và ngân sách eo hẹp, hãy coi phân phối là thứ bạn lắp từ dịch vụ được quản lý thay vì hệ thống bạn bố trí nhân sự: CI/CD được quản lý, công cụ cờ lưu trữ, và nền tảng đám mây xử lý tung ra và hoàn tác cho bạn. Chống lại việc xây hạ tầng quy trình tùy biến bạn không đủ sức bảo trì, và giữ con đường đủ đơn giản để ai trực ca hiểu được dưới áp lực. Ưu tiên công cụ cung cấp sẵn phân phối tiến dần và hoàn tác một cú nhấp, vì đó là những năng lực biến một lần triển khai thứ Sáu đáng sợ thành thường lệ.

**Doanh nghiệp lớn.** Vấn đề cốt lõi là nhất quán qua nhiều đội: một quy trình đường lát sẵn được hỗ trợ với cổng kiểm thử, bảo mật và chính sách dưới dạng mã tự động mà các đội tham gia thay vì phát minh lại. Chuẩn hóa giao diện để chỉ số DORA và SLO so sánh được qua tổ chức, lập ngân sách tường minh cho năng lực nền tảng duy trì đường lát sẵn, và quản lý cờ tính năng và suy giảm thời gian chờ như tài sản được quản trị thay vì văn hóa dân gian theo từng đội. Quản trị và kiểm toán đi kèm tự động khi mọi thay đổi chảy qua cùng con đường có phiên bản, có cổng.

**Chính phủ.** Quy tắc mua sắm, minh bạch và trách nhiệm giải trình công định hình quy trình, nên hãy ưu tiên phân phối liên tục dừng ở cổng thăng cấp tự động thực thi phân tách nhiệm vụ và phê duyệt bắt buộc dưới dạng chính sách dưới dạng mã. Làm chính quy trình thành kiểm soát tuân thủ: mỗi thay đổi mang dấu vết kiểm toán bất biến thỏa mãn nghĩa vụ kiểm soát thay đổi và quyền vận hành mà không cần dựng lại thủ công. Thay các bản phát hành "đại bùng nổ" nhiều nghi thức bằng thay đổi nhỏ, đảo ngược được, tách rời để bạn thử nghiệm một luồng hướng công chúng ở một vùng, đo tỷ lệ lỗi và hoàn tất, và hoàn tác trong vài phút nếu nó suy giảm.

## Ví dụ

**Công ty khởi nghiệp.** Một đội ba kỹ sư phát hành công cụ phân tích B2B bắt đầu bằng triển khai tay vào chiều thứ Sáu, nghĩa là một lần phát hành đáng sợ mỗi tuần và một cuối tuần lo lắng. Trong một buổi chiều họ dựng phát triển trên thân chính với quy trình GitHub Actions: kiểm thử đơn vị nhanh, linter và quét bảo mật chặn cổng mọi lần hợp nhất, và một bản dựng đạt triển khai thẳng lên sản xuất sau cờ LaunchDarkly. Tần suất triển khai nhảy từ hằng tuần lên nhiều lần mỗi ngày, và vì mỗi tính năng mới phát hành trong bóng tối và bật cho một khách hàng thân thiện trước, một lỗi xuất CSV được bắt và tắt trong vài phút thay vì thành sự cố thứ Hai. Họ theo dõi bốn chỉ số DORA trên bảng điều khiển đơn giản để cho nhà đầu tư thấy đội phát hành hằng ngày mà không làm hỏng gì.

**Doanh nghiệp lớn.** Một công ty bảo hiểm toàn cầu hợp nhất 40 đội lên một quy trình đường lát sẵn dùng chung (bộ công cụ mặc định được hỗ trợ, tích hợp sẵn mà các đội tham gia; chương 8.4): phát triển trên thân chính, cổng kiểm thử và bảo mật tự động, và triển khai canary với hoàn tác tự động khi vi phạm SLO. Tần suất triển khai tăng từ hằng tháng lên nhiều lần mỗi ngày; thời gian chờ giảm từ sáu tuần xuống dưới một ngày; tỷ lệ thay đổi thất bại giảm vì lô nhỏ và cổng tự động. Quan trọng nhất, tính năng sản phẩm nay phát hành sau cờ và được đo so với đối chứng, nên công ty bảo hiểm gắn được mỗi bản phát hành với hiệu ứng của nó lên tỷ lệ hoàn tất báo giá, nối trực tiếp quy trình phân phối với các kết quả then chốt phía khám phá của chương 11.1.

**Chính phủ.** Một cơ quan công thay các bản phát hành "đại bùng nổ" hằng quý (mỗi bản là một cuối tuần bước thủ công và là nguồn sự cố thường xuyên) bằng quy trình phân phối liên tục dừng ở cổng thăng cấp tự động thực thi phân tách nhiệm vụ và phê duyệt bắt buộc dưới dạng chính sách dưới dạng mã. Mỗi thay đổi mang dấu vết kiểm toán bất biến thỏa mãn nghĩa vụ kiểm soát thay đổi và ATO (quyền vận hành) của cơ quan (chương 4.6). Bản phát hành trở nên nhỏ, thường xuyên và đảo ngược được; thời gian khôi phục giảm từ nhiều ngày xuống vài phút; và vì triển khai được tách khỏi phát hành qua cờ, cơ quan có thể thử nghiệm một luồng trợ cấp mới với một vùng trước khi tung ra toàn quốc, đo tỷ lệ hoàn tất và lỗi trước khi cam kết.

## Luận chứng kinh doanh: động lực, ROI và TCO

Lợi tức của đầu tư vào quy trình phân phối nằm trong số được chứng minh bằng bằng chứng tốt nhất trong phần mềm. Thời gian chờ nhanh hơn và tần suất triển khai cao hơn nghĩa là ý tưởng đến người dùng (và bắt đầu trả giá trị, hoặc được sửa) sớm hơn. Tỷ lệ thay đổi thất bại thấp hơn và khôi phục nhanh hơn nghĩa là ít ngừng hoạt động hơn, ít chữa cháy hơn, và ít thiệt hại danh tiếng và quy định hơn. Nghiên cứu DORA nối các năng lực này với hiệu suất thương mại và tổ chức vượt trội, không chỉ sự thoải mái của kỹ thuật. Hiệu ứng cộng dồn quan trọng: một đội phát hành và học hằng ngày lặp thường xuyên gấp 20–30 lần so với đội phát hành hằng tháng, và tốc độ học đó mang tính quyết định qua vòng đời sản phẩm.

Về **[tổng chi phí sở hữu](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, tự động hóa chuyển chi phí từ lao động thủ công vĩnh viễn sang khoản đầu tư quy trình một lần cộng bảo trì. Một bản phát hành thủ công tiêu giờ kỹ sư cấp cao mỗi lần, mở rộng kém, và tạo bằng chứng kiểm toán yếu. Một quy trình tự động phân bổ chi phí đó, rồi *giảm* nó khi khối lượng lớn lên, trong khi tạo bằng chứng mạnh hơn liên tục. Khả năng đảo ngược hạ chính chi phí của thất bại: khi bất kỳ thay đổi nào cũng hoàn tác được trong vài giây, chi phí kỳ vọng của một lần triển khai tệ sụp đổ, đó là thứ làm đi nhanh hợp lý thay vì liều lĩnh.

Để lập luận với ban lãnh đạo, hãy đo đường cơ sở hiện tại bằng bốn chỉ số DORA và số giờ thủ công tiêu mỗi bản phát hành, rồi định lượng lao động thủ công đã loại bỏ và ngừng hoạt động tránh được. Chi phí áp dụng là thật, cụ thể là kỹ thuật quy trình, đầu tư kiểm thử, và năng lực nền tảng/đường lát sẵn (chương 8.4), nhưng chi phí của việc *không* đầu tư được trả liên tục trong phản hồi chậm, rủi ro ngày phát hành, kiệt sức của kỹ sư và nỗi đau kiểm toán. Lập luận quyết định là liên kết với khám phá: một quy trình phân phối nhanh, được đo là thứ làm các canh bạc đã xác thực của quy trình khám phá thực sự kiểm thử được trong sản xuất.

## Phản mẫu và cạm bẫy

- **Đo đầu ra, không đo kết quả:** ăn mừng số lần triển khai trong khi chỉ số mục tiêu nằm yên.
- **Bộ kiểm thử chậm hoặc chập chờn:** cổng mà nhà phát triển học cách phớt lờ hoặc đi vòng.
- **Phát hành đại bùng nổ, thưa thớt:** lô lớn rủi ro, khó gỡ lỗi và khó đảo ngược.
- **Gộp triển khai và phát hành:** không có cờ tính năng, nên mỗi lần triển khai là canh bạc hướng người dùng không đảo ngược.
- **Sân khấu phát hành thủ công:** danh mục kiểm tra chạy tay chậm, không nhất quán và kiểm toán kém.
- **Quy trình tự động, không có khả năng quan sát:** phát hành nhanh mà không thể phát hiện hay chẩn đoán suy giảm.
- **Nợ cờ tính năng:** cờ không bao giờ bị loại bỏ, tích lũy thành độ phức tạp tổ hợp không kiểm thử được.
- **Lách chỉ số DORA:** chia nhỏ lần triển khai để thổi phồng tần suất thay vì cải thiện luồng.
- **Không có vòng phản hồi:** kết quả không bao giờ được đo, nên phân phối không bao giờ thông tin cho chu kỳ khám phá tiếp theo.

## Mô hình trưởng thành

- **Mức 1, Khởi đầu:** Bản phát hành thủ công, thưa thớt, nhiều nghi thức; kiểm thử chủ yếu thủ công và chạy tay; thành công được đo là "nó đã phát hành"; hoàn tác đau đớn và ứng biến; không có ý niệm chung về cách phân phối nên hoạt động.
- **Mức 2, Phát triển:** Một số đội dựng CI với bản dựng tự động và vài kiểm thử; bản phát hành được lên lịch; giám sát cơ bản tồn tại; thực hành khác nhau theo đội và chỉ số DORA chưa được theo dõi, nên phân phối tốt hơn ở từng điểm nhưng không nhất quán qua tổ chức.
- **Mức 3, Chuẩn hóa:** Một quy trình đường lát sẵn có tài liệu được thực thi toàn tổ chức: phân phối liên tục với cổng kiểm thử và bảo mật tự động, triển khai tiến dần với hoàn tác, và phân tách nhiệm vụ được thực thi dưới dạng chính sách dưới dạng mã. Quy trình cung cấp dấu vết kiểm toán bất biến, và mọi đội theo cùng con đường có phiên bản thay vì con đường riêng.
- **Mức 4, Quản lý:** Quy trình được đo và kiểm soát theo đường cơ sở. Bốn chỉ số DORA (tần suất triển khai, thời gian chờ, tỷ lệ thay đổi thất bại, thời gian khôi phục), mức đạt SLO, đốt ngân sách lỗi, và chỉ số luồng như thời gian chu kỳ và công việc đang làm được theo dõi so với mục tiêu, và cổng cùng hoàn tác kích hoạt theo ngưỡng đo được thay vì phán đoán. Nợ cờ, tỷ lệ kiểm thử chập chờn và suy giảm thời gian chờ được giám sát, và mỗi quyết định tiếp tục hay dừng được đưa ra dựa trên bằng chứng.
- **Mức 5, Điều phối:** Phân phối được cải thiện liên tục và tích hợp với khám phá và hoạch định rủi ro. Triển khai liên tục chạy nơi phù hợp với phân phối tiến dần và hoàn tác tự động; tính năng phát hành như thí nghiệm đo được mà chỉ số kết quả quay lại vòng canh bạc tiếp theo; hiệu suất DORA đỉnh được duy trì qua các đội nhờ đường lát sẵn; và tổ chức thích ứng điều chỉnh lại cổng, ngưỡng và năng lực khi tải, rủi ro và cơ cấu sản phẩm dịch chuyển.

## Ý tưởng để thảo luận

1. Bốn chỉ số DORA hiện tại của bạn là gì, và nút thắt lớn nhất trong dòng chảy từ commit đến sản xuất của bạn ở đâu?
2. Hôm nay bạn có tách được triển khai khỏi phát hành không? Nếu không, cờ tính năng sẽ đổi gì về rủi ro của bạn?
3. Bộ kiểm thử của bạn chạy mất bao lâu, và nhà phát triển có đủ tin nó để không đi vòng không?
4. Khi bạn phát hành tính năng gần nhất, bạn có đo liệu nó có dịch chuyển chỉ số nó được định dịch chuyển không?
5. Trong bối cảnh bị quản lý, quy trình kiểm soát thay đổi của bạn làm chậm phân phối *hay* được thực thi tự động qua quy trình?
6. Cờ tính năng nào trong cơ sở mã của bạn lẽ ra đã bị loại bỏ từ nhiều tháng trước?

## Những điểm cần ghi nhớ

- Quy trình phân phối biến ý tưởng đã xác thực thành phần mềm đang chạy, được đo, và đưa kết quả ngược lại khám phá (chương 11.1).
- Tự động hóa toàn bộ con đường: **cổng kiểm thử** nhanh, **CI/CD**, và **hạ tầng dưới dạng mã**, với quy trình là nguồn sự thật.
- **Tách triển khai khỏi phát hành** và dùng chiến lược tiến dần (cờ, canary, xanh-lục) với hoàn tác tự động.
- Đo ở ba cấp: chỉ số **DORA/luồng**, **độ tin cậy/SLO**, và **kết quả kinh doanh/người dùng**.
- Tốc độ và sự ổn định là **bổ sung cho nhau**, không phải đánh đổi: các thực hành mang lại cái này mang lại cái kia.
- Quy trình cũng là **kiểm soát tuân thủ**: tự động hóa tạo dấu vết kiểm toán bất biến, liên tục.
- ROI nhanh, được chứng minh tốt (DORA), và cộng dồn; chi phí chính của việc không đầu tư được trả liên tục.

## Tài liệu tham khảo và đọc thêm

- *Accelerate: The Science of Lean Software and DevOps*, của Nicole Forsgren, Jez Humble, Gene Kim (các chỉ số DORA và bằng chứng).
- *Continuous Delivery*, của Jez Humble và David Farley (văn bản nền tảng).
- *The DevOps Handbook*, của Kim, Humble, Debois, Willis.
- *The Phoenix Project*, của Gene Kim, Kevin Behr, George Spafford (tường thuật về luồng).
- *Site Reliability Engineering*, của Beyer, Jones, Petoff, Murphy, biên tập (SLI/SLO, ngân sách lỗi).
- *Team Topologies*, của Matthew Skelton và Manuel Pais (đường lát sẵn và thiết kế đội phân phối).
- *Feature Flags / progressive delivery*, các bài viết của Pete Hodgson và cộng đồng LaunchDarkly/Split.
- Google DORA, các báo cáo *Accelerate State of DevOps* (hằng năm).
- Kim, Gene, *The Unicorn Project* (góc nhìn trải nghiệm nhà phát triển về luồng).
- Reinertsen, Donald, *The Principles of Product Development Flow* (kích thước lô, hàng đợi, kinh tế luồng).
