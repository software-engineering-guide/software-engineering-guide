# 12.3 Mẫu biểu

Các mẫu biểu này là điểm khởi đầu sẵn sàng sao chép-dán. Hãy nhấc bất kỳ mẫu nào vào wiki, kho hay hệ thống phiếu của bạn và điền vào các chỗ giữ chỗ trong ngoặc. Ghi chú in nghiêng và chú thích nội tuyến giải thích điều thuộc về mỗi mục; hãy xóa chúng khi mục đã được điền. Giữ mẫu biểu nhẹ: một mẫu bỏ qua nhanh hơn hoàn tất sẽ không được dùng. Hãy điều chỉnh tiêu đề và mục cho khớp tổ chức của bạn, nhưng bảo toàn ý định của từng phần.

Vài quy ước dùng bên dưới:

- Văn bản trong `[ngoặc vuông]` là chỗ giữ chỗ cần thay.
- Văn bản _in nghiêng_ hoặc `<!-- chú thích -->` là hướng dẫn cần xóa.
- Giữ tài liệu hoàn chỉnh ngắn nhất có thể mà vẫn trả lời các câu hỏi của nó.

## Hồ sơ quyết định kiến trúc (ADR)

```markdown
# ADR [NNNN]: [Tiêu đề ngắn của quyết định]

- Trạng thái: [Đề xuất | Chấp nhận | Ngừng hỗ trợ | Bị thay thế bởi ADR-XXXX]
- Ngày: [YYYY-MM-DD]
- Người quyết định: [tên hoặc vai trò]
- Người được tham vấn: [tên hoặc vai trò]

## Ngữ cảnh

<!-- Vấn đề, lực tác động hay ràng buộc nào thúc đẩy quyết định này?
     Nêu sự kiện và yêu cầu một cách trung lập. Chỉ gồm những gì một
     người đọc tương lai cần để hiểu vì sao quyết định là cần thiết. -->

## Quyết định

<!-- Nêu lựa chọn trong một hoặc hai câu rõ ràng: "Chúng tôi sẽ ..." -->

## Các phương án đã xem xét

<!-- Liệt kê các lựa chọn thực tế bạn đã cân nhắc và vì sao mỗi cái
     được chọn hay không. Nên có ít nhất hai phương án thay thế ở đây. -->

- Phương án A: [tóm tắt]; bị loại vì [lý do].
- Phương án B: [tóm tắt]; bị loại vì [lý do].
- Phương án được chọn: [tóm tắt]; được chọn vì [lý do].

## Hệ quả

<!-- Kết quả trung thực của quyết định, cả tốt lẫn xấu. -->

- Tích cực: [lợi ích có được]
- Tiêu cực: [chi phí, rủi ro hay giới hạn được chấp nhận]
- Tiếp theo: [di chuyển, công việc mới hay quyết định mà nó kích hoạt]

## Liên quan

<!-- Liên kết tới ADR, RFC, phiếu hay tài liệu trước đó mà nó liên quan. -->
```

## RFC / tài liệu thiết kế

```markdown
# RFC: [Tiêu đề]

- Tác giả: [tên]
- Trạng thái: [Bản nháp | Đang rà soát | Đã phê duyệt | Bị từ chối | Đã triển khai]
- Người rà soát: [tên hoặc vai trò]
- Tạo: [YYYY-MM-DD]
- Cập nhật lần cuối: [YYYY-MM-DD]
- Phiếu / theo dõi: [liên kết]

## Tóm tắt

<!-- Một đoạn: cái này đề xuất gì và vì sao nó quan trọng. Một người
     đọc nên nắm được bản chất chỉ từ mục này. -->

## Vấn đề và động lực

<!-- Chúng ta đang giải vấn đề gì? Ai bị ảnh hưởng? Chuyện gì xảy ra
     nếu chúng ta không làm gì? Gồm bối cảnh và ràng buộc liên quan. -->

## Mục tiêu và phi mục tiêu

- Mục tiêu: [thành công trông thế nào, đo được nơi có thể]
- Phi mục tiêu: [tường minh ngoài phạm vi, để ngăn phình phạm vi]

## Thiết kế đề xuất

<!-- Lõi của tài liệu. Mô tả cách tiếp cận, kiến trúc, mô hình dữ liệu,
     giao diện và luồng chính. Dùng sơ đồ nơi chúng làm rõ. Giải thích
     nó hoạt động thế nào, không chỉ nó là gì. -->

## Các phương án đã xem xét

<!-- Các cách tiếp cận khác và vì sao chúng không được chọn. Cho người
     đọc thấy không gian thiết kế đã được khám phá. -->

## Tác động và rủi ro

- Bảo mật và riêng tư: [hệ quả và biện pháp giảm thiểu]
- Hiệu năng và quy mô: [tải và hành vi kỳ vọng]
- Khả năng vận hành: [giám sát, kiểu thất bại, tung ra, hoàn tác]
- Chi phí: [tác động hạ tầng hay giấy phép]
- Tương thích ngược: [di chuyển và ngừng hỗ trợ]

## Kế hoạch kiểm thử và tung ra

<!-- Thay đổi sẽ được xác thực và phát hành an toàn thế nào. -->

## Câu hỏi mở

<!-- Vấn đề chưa giải quyết mà bạn muốn người rà soát cân nhắc. -->
```

## Rút kinh nghiệm / rà soát sự cố (không đổ lỗi)

```markdown
# Rút kinh nghiệm: [Tiêu đề sự cố]

- Mã sự cố: [ID]
- Ngày xảy ra sự cố: [YYYY-MM-DD]
- Tác giả: [tên]
- Trạng thái: [Bản nháp | Cuối cùng]
- Mức nghiêm trọng: [SEV1 | SEV2 | SEV3]

> Buổi rà soát này không đổ lỗi. Chúng tôi tập trung vào hệ thống và
> các yếu tố góp phần, không phải cá nhân. Mục tiêu là học và ngăn
> tái diễn.

## Tóm tắt

<!-- Hai hoặc ba câu: điều gì đã xảy ra, tác động, và giải quyết,
     người không chuyên đọc được. -->

## Tác động

- Thời lượng: [từ thời điểm bắt đầu đến thời điểm khôi phục, kèm múi giờ]
- Người dùng bị ảnh hưởng: [phạm vi và số lượng]
- Tác động kinh doanh: [doanh thu, SLA, danh tiếng, hoặc khác]

## Dòng thời gian

<!-- Chuỗi sự kiện có dấu thời gian, thực tế. Gồm phát hiện, leo thang,
     hành động chính và khôi phục. -->

- [HH:MM] [sự kiện]
- [HH:MM] [sự kiện]

## Các yếu tố góp phần

<!-- Chuỗi điều kiện dẫn đến sự cố. Ưu tiên "yếu tố góp phần" hơn một
     nguyên nhân gốc duy nhất. -->

## Phát hiện và ứng phó

- Nó được phát hiện thế nào? [cảnh báo, báo cáo khách hàng, v.v.]
- Cái gì giúp ứng phó?
- Cái gì làm chậm ứng phó?

## Điều đã tốt

<!-- Ghi nhận hành động hiệu quả và biện pháp bảo vệ đã hoạt động. -->

## Hành động

<!-- Cụ thể, có chủ sở hữu và có ngày. Giải quyết phòng ngừa, phát hiện
     và giảm thiểu. Theo dõi chúng trong tồn đọng thông thường. -->

| Hành động | Chủ sở hữu | Hạn | Loại (phòng ngừa/phát hiện/giảm thiểu) | Phiếu |
|--------|-------|----------|--------------------------------|--------|
| [hành động] | [tên] | [ngày] | [loại] | [liên kết] |

## Bài học rút ra

<!-- Điều tổ chức rộng hơn nên rút ra. -->
```

## Mô hình mối đe dọa (dựa trên STRIDE)

```markdown
# Mô hình mối đe dọa: [Tên hệ thống hoặc tính năng]

- Tác giả: [tên]
- Ngày: [YYYY-MM-DD]
- Người rà soát: [đầu mối bảo mật, chủ sở hữu]
- Phạm vi: [cái được và không được bao phủ]

## Tổng quan hệ thống

<!-- Mô tả ngắn về hệ thống, mục đích và người dùng của nó. -->

## Tài sản

<!-- Cái đáng bảo vệ: dữ liệu, thông tin xác thực, chức năng, danh
     tiếng. Ghi độ nhạy cảm của mỗi cái. -->

## Ranh giới tin cậy và luồng dữ liệu

<!-- Mô tả hoặc vẽ sơ đồ thành phần, kho dữ liệu, thực thể bên ngoài,
     và các ranh giới nơi lòng tin thay đổi. -->

## Mối đe dọa (STRIDE)

<!-- Với mỗi phần tử, xét các loại STRIDE. Ghi mỗi mối đe dọa đáng tin,
     rủi ro của nó, và biện pháp giảm thiểu hay rủi ro chấp nhận. -->

| Mối đe dọa | Loại STRIDE | Phần tử bị ảnh hưởng | Rủi ro (T/V/C) | Giảm thiểu | Trạng thái |
|--------|-----------------|------------------|--------------|------------|--------|
| [mối đe dọa] | Giả mạo (Spoofing) | [phần tử] | [rủi ro] | [kiểm soát] | [mở/đã giảm thiểu/chấp nhận] |
| [mối đe dọa] | Can thiệp (Tampering) | [phần tử] | [rủi ro] | [kiểm soát] | [trạng thái] |
| [mối đe dọa] | Chối bỏ (Repudiation) | [phần tử] | [rủi ro] | [kiểm soát] | [trạng thái] |
| [mối đe dọa] | Tiết lộ thông tin (Information disclosure) | [phần tử] | [rủi ro] | [kiểm soát] | [trạng thái] |
| [mối đe dọa] | Từ chối dịch vụ (Denial of service) | [phần tử] | [rủi ro] | [kiểm soát] | [trạng thái] |
| [mối đe dọa] | Nâng đặc quyền (Elevation of privilege) | [phần tử] | [rủi ro] | [kiểm soát] | [trạng thái] |

## Giả định và phụ thuộc

<!-- Giả định bảo mật được dựa vào và kiểm soát bên ngoài được tin. -->

## Vấn đề mở và theo dõi

<!-- Mối đe dọa cần thêm công việc, được theo dõi thành phiếu. -->
```

## Sổ tay vận hành

```markdown
# Sổ tay vận hành: [Tên tác vụ hoặc kịch bản]

- Dịch vụ: [tên dịch vụ]
- Chủ sở hữu: [đội]
- Rà soát lần cuối: [YYYY-MM-DD]
- Cảnh báo liên quan: [tên cảnh báo]

## Mục đích

<!-- Khi nào dùng sổ tay vận hành này và nó đạt được gì. -->

## Điều kiện tiên quyết

<!-- Quyền truy cập, công cụ và quyền hạn cần trước khi bắt đầu. -->

## Phát hiện / triệu chứng

<!-- Điều người vận hành quan sát: cảnh báo, dấu hiệu lỗi, bảng điều khiển. -->

## Chẩn đoán

<!-- Các kiểm tra từng bước để xác nhận vấn đề và thu hẹp nguyên nhân.
     Gồm các lệnh, truy vấn hay liên kết bảng điều khiển chính xác. -->

1. [bước và kết quả kỳ vọng]
2. [bước và kết quả kỳ vọng]

## Giải quyết

<!-- Các bước cụ thể, có thứ tự để sửa hoặc giảm thiểu. Ghi chú bất kỳ
     bước nào rủi ro hay không đảo ngược, và cách xác minh thành công. -->

1. [bước]
2. [xác minh khôi phục]

## Hoàn tác

<!-- Cách đảo ngược các hành động nếu giải quyết làm mọi thứ tệ hơn. -->

## Leo thang

<!-- Liên hệ ai và khi nào leo thang. Trực ca phụ, đội sở hữu, và liên
     hệ nhà cung cấp. -->

## Tham chiếu

<!-- Bảng điều khiển, sổ tay vận hành liên quan, tài liệu kiến trúc. -->
```

## README dịch vụ / mục danh mục dịch vụ

```markdown
# [Tên dịch vụ]

- Đội sở hữu: [đội]
- Trực ca: [liên kết vòng trực]
- Bậc / mức trọng yếu: [Bậc 1 | 2 | 3]
- Kho: [liên kết]
- Trạng thái: [Đang hoạt động | Ngừng hỗ trợ]

## Nó làm gì

<!-- Một đoạn về trách nhiệm của dịch vụ và bên tiêu thụ nó. -->

## Kiến trúc

<!-- Thành phần chính, phụ thuộc (thượng nguồn và hạ nguồn), và liên
     kết tới tài liệu thiết kế hay sơ đồ. -->

## Giao diện

- API / điểm cuối: [liên kết tới đặc tả]
- Sự kiện phát hành / tiêu thụ: [chủ đề]
- Kho dữ liệu: [cơ sở dữ liệu, bộ đệm, bucket]

## Thời gian chạy và triển khai

- Môi trường: [dev, staging, prod]
- Cách triển khai: [liên kết quy trình và cách làm]
- Cấu hình và cờ tính năng: [ở đâu và thế nào]

## Khả năng quan sát

- Bảng điều khiển: [liên kết]
- Cảnh báo: [liên kết]
- Nhật ký: [tìm ở đâu]
- SLO: [liên kết]

## Vận hành

- Sổ tay vận hành: [liên kết]
- Tác vụ thường gặp: [mở rộng, khởi động lại, nạp bù]
- Vấn đề và giới hạn đã biết: [ghi chú]

## Bắt đầu (cho người đóng góp mới)

<!-- Cách dựng, kiểm thử và chạy cục bộ. -->

## Liên hệ

- Kênh Slack / chat: [liên kết]
- Leo thang: [đường]
```

## Chính sách SLO / ngân sách lỗi

```markdown
# Chính sách SLO và ngân sách lỗi: [Tên dịch vụ hoặc hành trình]

- Chủ sở hữu: [đội]
- Ngày có hiệu lực: [YYYY-MM-DD]
- Nhịp rà soát: [ví dụ hằng quý]

## Chỉ báo mức dịch vụ (SLI)

<!-- Xác định chính xác từng SLI: đại lượng được đo, cách đo, và đo từ
     đâu (lý tưởng từ góc nhìn của người dùng). -->

| SLI | Định nghĩa | Nguồn dữ liệu |
|-----|-----------|-------------|
| Khả dụng | [ví dụ yêu cầu thành công / tổng yêu cầu] | [nguồn] |
| Độ trễ | [ví dụ tỷ lệ yêu cầu dưới X ms] | [nguồn] |

## Mục tiêu (SLO)

| SLI | Mục tiêu | Cửa sổ đo |
|-----|--------|--------------------|
| Khả dụng | [ví dụ 99,9%] | [ví dụ 28 ngày cuốn chiếu] |
| Độ trễ | [ví dụ 95% dưới 300 ms] | [28 ngày cuốn chiếu] |

## Ngân sách lỗi

<!-- Mức không đáng tin cậy được phép: 100% trừ mục tiêu, qua cửa sổ.
     Nêu ngân sách bằng thuật ngữ cụ thể (ví dụ phút/tháng). -->

- Ngân sách: [mức cho phép suy ra]

## Chính sách khi ngân sách cạn

<!-- Hệ quả đã thống nhất. Làm chúng cụ thể và thực thi được. -->

- [ví dụ Đóng băng bản phát hành tính năng không trọng yếu cho đến khi ngân sách phục hồi.]
- [ví dụ Ưu tiên công việc độ tin cậy trong chu kỳ hoạch định kế tiếp.]
- [ví dụ Leo thang lên lãnh đạo kỹ thuật nếu vi phạm hai cửa sổ liên tiếp.]

## Chính sách khi ngân sách lành mạnh

<!-- Rủi ro thêm mà đội có thể chấp nhận, ví dụ tung ra nhanh hơn. -->

## Cảnh báo

<!-- Cảnh báo tốc độ đốt và ngưỡng gắn với SLO này. -->
```

## Mục sổ đăng ký rủi ro

```markdown
## Rủi ro: [Tiêu đề rủi ro ngắn]

- Mã rủi ro: [ID]
- Ngày nêu: [YYYY-MM-DD]
- Chủ sở hữu: [tên hoặc vai trò chịu trách nhiệm quản lý rủi ro này]
- Loại: [bảo mật | vận hành | tuân thủ | tài chính | phân phối | nhà cung cấp]
- Trạng thái: [Mở | Đang giảm thiểu | Chấp nhận | Đóng]

### Mô tả

<!-- Phát biểu rủi ro dưới dạng: nguyên nhân -> sự kiện -> hậu quả.
     Cái gì có thể xảy ra, và vì sao nó quan trọng. -->

### Đánh giá

- Khả năng xảy ra: [Thấp | Vừa | Cao]
- Tác động: [Thấp | Vừa | Cao]
- Xếp hạng tổng thể: [suy ra từ khả năng x tác động]

### Kiểm soát hiện có

<!-- Cái gì đã giảm rủi ro này hôm nay. -->

### Kế hoạch giảm thiểu

<!-- Hành động dự kiến để giảm khả năng hay tác động, kèm chủ sở hữu
     và ngày. Nếu chấp nhận rủi ro, ghi ai đã chấp nhận và vì sao. -->

| Hành động | Chủ sở hữu | Hạn | Trạng thái |
|--------|-------|----------|--------|
| [hành động] | [tên] | [ngày] | [trạng thái] |

### Rà soát

- Ngày rà soát tiếp: [YYYY-MM-DD]
- Quyết định / ghi chú: [bất kỳ ký duyệt chấp nhận hay thay đổi nào]
```

## Bản một trang dự án / bản tóm tắt sản phẩm

```markdown
# [Tên dự án hoặc sản phẩm]: bản một trang

- Người bảo trợ: [tên]
- Trưởng dự án: [tên]
- Ngày: [YYYY-MM-DD]
- Trạng thái: [Ý tưởng | Đã phê duyệt | Đang tiến hành | Đã phát hành]

## Vấn đề

<!-- Một đoạn: vấn đề của khách hàng hay doanh nghiệp, và bằng chứng nó
     là thật và đáng giải. -->

## Đối tượng

<!-- Ai có vấn đề này và ai hưởng lợi khi giải nó. -->

## Giải pháp đề xuất

<!-- Mô tả ngắn về cái chúng ta sẽ xây hay đổi. Giữ ở mức ý định,
     không phải chi tiết triển khai. -->

## Vì sao bây giờ

<!-- Lý do làm điều này bây giờ thay vì sau. -->

## Chỉ số thành công

<!-- Chúng ta sẽ biết nó hiệu quả thế nào. Ưu tiên kết quả đo được. -->

- [chỉ số và mục tiêu]

## Phạm vi

- Trong phạm vi: [cái chúng ta sẽ làm]
- Ngoài phạm vi: [cái chúng ta sẽ không làm]

## Rủi ro và câu hỏi mở

<!-- Các bất định và phụ thuộc chính. -->

## Kế hoạch thô và cột mốc

<!-- Các giai đoạn cấp cao và thời điểm xấp xỉ. -->

## Chi phí và nguồn lực

<!-- Con người, thời gian và ngân sách cần. -->
```

## Ghi chú bàn giao trực ca

```markdown
# Bàn giao trực ca: [YYYY-MM-DD]

- Người giao: [tên]
- Người nhận: [tên]
- Dịch vụ: [tên]

## Trạng thái chung

<!-- Một dòng: yên tĩnh, ồn ào, hay vấn đề đang diễn ra. -->

## Sự cố đang mở

<!-- Bất kỳ sự cố đang hoạt động hay mới giải quyết mà người ứng phó
     tiếp theo phải biết, kèm liên kết. -->

- [sự cố, trạng thái, và cái còn lại]

## Thay đổi đang diễn ra hoặc đã lên kế hoạch

<!-- Triển khai, di chuyển, cửa sổ bảo trì hay thí nghiệm đang bay có
     thể gây cảnh báo. -->

## Cảnh báo ồn hoặc chập chờn

<!-- Cảnh báo đã kích hoạt và ý nghĩa thật của chúng, để người tiếp theo
     không bị đánh lạc hướng. Ghi mọi lần tắt tạm thời và hạn của chúng. -->

## Mục cần theo dõi

<!-- Chỉ số hay hệ thống đang xu hướng theo hướng đáng lo. -->

## Theo dõi đang chờ

<!-- Tác vụ trao cho ca tiếp theo, kèm liên kết tới phiếu. -->

## Ghi chú

<!-- Bất cứ điều gì khác hữu ích: đặc thù truy cập, vấn đề nhà cung cấp, ngữ cảnh. -->
```

## Yêu cầu thay đổi (cho kiểm soát thay đổi bị quản lý)

```markdown
# Yêu cầu thay đổi: [Tiêu đề thay đổi]

- Mã thay đổi: [ID]
- Người yêu cầu: [tên]
- Ngày nộp: [YYYY-MM-DD]
- Loại: [Tiêu chuẩn | Thường | Khẩn cấp]
- Ưu tiên: [Thấp | Vừa | Cao]
- Trạng thái: [Đã nộp | Đã phê duyệt | Bị từ chối | Đã triển khai | Đóng]

## Mô tả thay đổi

<!-- Cái gì đang đổi và vì sao. Tham chiếu phiếu hay yêu cầu. -->

## Hệ thống và thành phần bị ảnh hưởng

<!-- Dịch vụ, dữ liệu, môi trường và người dùng bị tác động. -->

## Biện minh và tác động kinh doanh

<!-- Lý do của thay đổi và tác động của việc không làm. -->

## Đánh giá rủi ro

- Mức rủi ro: [Thấp | Vừa | Cao]
- Tác động tiềm tàng nếu thay đổi thất bại: [mô tả]
- Tác động lên bảo mật, riêng tư hay tuân thủ: [mô tả]

## Kế hoạch triển khai

<!-- Các bước có thứ tự, bên chịu trách nhiệm và thời điểm. -->

## Kế hoạch kiểm thử và xác thực

<!-- Thành công sẽ được xác minh thế nào trước và sau thay đổi. -->

## Kế hoạch lùi / hoàn tác

<!-- Cách đảo ngược thay đổi nếu nó thất bại, và thời gian khôi phục. -->

## Lịch trình

- Cửa sổ đề xuất: [bắt đầu và kết thúc, kèm múi giờ]
- Thời gian ngừng dự kiến: [thời lượng hoặc không]

## Phê duyệt

| Vai trò | Tên | Quyết định | Ngày |
|------|------|----------|------|
| Chủ sở hữu thay đổi | [tên] | [phê duyệt/từ chối] | [ngày] |
| Người rà soát kỹ thuật | [tên] | [phê duyệt/từ chối] | [ngày] |
| Hội đồng tư vấn thay đổi | [tên] | [phê duyệt/từ chối] | [ngày] |

## Rà soát sau triển khai

<!-- Kết quả, vấn đề gặp phải, và liệu có cần lùi không. -->
```

## Đề cương Đánh giá tác động bảo vệ dữ liệu (DPIA)

```markdown
# Đánh giá tác động bảo vệ dữ liệu: [Tên hoạt động xử lý]

- Người đánh giá: [tên]
- Ngày: [YYYY-MM-DD]
- Người rà soát: [DPO / đầu mối riêng tư]
- Trạng thái: [Bản nháp | Đã rà soát | Đã phê duyệt]

## 1. Mô tả xử lý

<!-- Dữ liệu cá nhân nào được xử lý, thế nào, bởi ai, và vì mục đích gì.
     Gồm luồng dữ liệu từ thu thập đến xóa. -->

- Chủ thể dữ liệu: [dữ liệu về ai]
- Loại dữ liệu: [các loại dữ liệu cá nhân, ghi chú mọi loại đặc biệt]
- Mục đích: [vì sao dữ liệu được xử lý]
- Bên nhận và bên xử lý: [ai nhận hay xử lý dữ liệu]
- Thời hạn lưu giữ: [dữ liệu được giữ bao lâu và phương pháp xóa]
- Chuyển giao quốc tế: [điểm đến và cơ chế chuyển giao]

## 2. Cần thiết và tương xứng

<!-- Xử lý có cần thiết cho mục đích không? Đó có phải lựa chọn ít xâm
     phạm nhất không? Cơ sở hay thẩm quyền pháp lý là gì? -->

- Cơ sở / thẩm quyền pháp lý: [cơ sở cho từng mục đích]
- Tối thiểu hóa dữ liệu: [vì sao mỗi trường cần thiết]
- Biện minh độ chính xác và lưu giữ: [ghi chú]
- Quyền chủ thể dữ liệu được hỗ trợ thế nào: [truy cập, xóa, v.v.]

## 3. Tham vấn

<!-- Các bên liên quan, và nơi liên quan là chủ thể dữ liệu, đã được tham vấn. -->

## 4. Rủi ro với cá nhân

<!-- Xác định rủi ro riêng tư và đánh giá từng cái. -->

| Rủi ro với cá nhân | Khả năng | Mức nghiêm trọng | Tổng thể |
|---------------------|-----------|----------|---------|
| [ví dụ truy cập trái phép vào dữ liệu nhạy cảm] | [T/V/C] | [T/V/C] | [xếp hạng] |

## 5. Biện pháp giảm rủi ro

<!-- Với mỗi rủi ro, biện pháp giảm thiểu và rủi ro dư sau đó. -->

| Rủi ro | Biện pháp | Rủi ro dư | Người chấp nhận |
|------|---------|---------------|-------------|
| [rủi ro] | [kiểm soát] | [T/V/C] | [tên] |

## 6. Kết quả và ký duyệt

- Rủi ro dư chấp nhận được: [Có | Không]
- Biện pháp được phê duyệt bởi: [tên, vai trò]
- Cần tham vấn cơ quan giám sát: [Có | Không]
- Ngày rà soát: [YYYY-MM-DD]
```
