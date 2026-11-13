# 4.4 Operasi keamanan

## Tinjauan dan motivasi

Pencegahan itu perlu, tetapi tidak pernah cukup. Musuh yang gigih, kerentanan baru, dan kesalahan manusia biasa berarti sebagian ancaman akan lolos dari pertahanan Anda. Operasi keamanan adalah disiplin menemukannya dengan cepat, merespons dengan baik, dan memasukkan apa yang Anda pelajari kembali ke pertahanan yang lebih kuat. Ia beda antara insiden yang tertahan dalam menit dan yang membusuk berbulan-bulan sebelum ada yang menyadari.

Dalam organisasi besar, operasi keamanan harus bekerja pada skala dan kecepatan. Ribuan layanan menghasilkan lautan log. Ratusan kerentanan baru diungkap setiap minggu. Deployment tidak pernah berhenti. Operasi manual dan artisanal sama sekali tidak dapat mengimbangi. Jawabannya menanamkan keamanan ke pipeline pengiriman ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), mengotomatisasi deteksi dan respons, dan membangun otot untuk menangani insiden dengan tenang ketika menghantam. Bagi pemerintah, operasi keamanan juga membawa kewajiban undang-undang: tenggat pelaporan insiden yang diwajibkan, pengungkapan kerentanan terkoordinasi, dan ketelitian forensik yang tahan pengawasan hukum.

Bab ini membahas mengintegrasikan keamanan ke pipeline, mengelola kerentanan dan penambalan, merespons insiden dan melakukan forensik, menjalankan deteksi lewat [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) dan SOAR, serta memvalidasi pertahanan lewat red dan purple teaming dan [uji penetrasi](https://en.wikipedia.org/wiki/Penetration_test).

## Prinsip utama

- **Otomatiskan yang rutin.** Mesin menangani pemindaian, korelasi, dan respons berulang agar manusia berfokus pada penilaian.
- **Geser keamanan ke pipeline.** Pengujian dan gerbang hidup di [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (integrasi berkelanjutan dan pengiriman berkelanjutan), memberi umpan balik cepat di tempat insinyur sudah bekerja.
- **Asumsikan pembobolan dan bersiaplah.** Latih respons insiden sebelum Anda membutuhkannya; insiden bukan waktu untuk berimprovisasi.
- **Ukur dan kurangi waktu.** Waktu rata-rata mendeteksi dan waktu rata-rata merespons adalah metrik yang paling penting.
- **Pembelajaran tanpa menyalahkan.** Setiap insiden dan nyaris-insiden menjadi pelajaran yang mengeraskan sistem, bukan pencarian orang untuk dihukum.
- **Validasi pertahanan secara adversarial.** Uji keamanan Anda seperti yang akan dilakukan penyerang sungguhan, lalu perbaiki apa yang mereka temukan.
- **Rekayasa deteksi adalah produk.** Perlakukan deteksi sebagai kode: dikontrol versi, diuji, dan terus diperbaiki.

## Rekomendasi

### Bangun DevSecOps ke dalam pipeline

Integrasikan pengujian keamanan otomatis langsung ke integrasi dan pengiriman berkelanjutan agar umpan balik mencapai insinyur dalam menit:

- **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Static Application Security Testing) menganalisis kode sumber untuk pola rentan saat dikomit.
- **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Dynamic Application Security Testing) menyelidiki aplikasi yang berjalan untuk cacat yang dapat dieksploitasi.
- **SCA** (Software Composition Analysis) menandai dependensi yang diketahui rentan.
- **Pemindaian IaC** memeriksa infrastruktur-sebagai-kode untuk konfigurasi tak aman sebelum di-deploy.
- **Pemindaian rahasia** memblokir kredensial agar tidak masuk ke repositori.

Setel perkakas ini tanpa ampun untuk mengendalikan positif palsu. Pemindai yang berteriak serigala akan diabaikan. Tetapkan gerbang berbasis risiko: blokir pada temuan keparahan tinggi dan keyakinan tinggi, dan lacak sisanya tanpa menghentikan pengiriman. Anda menginginkan sinyal yang cepat dan tepercaya, bukan tembok derau.

### Kelola kerentanan dan tambal secara sistematis

Arus stabil kerentanan menuntut proses sistematis dan terprioritaskan, bukan kepanikan baru pada setiap berita utama.

- Pelihara inventaris aset yang akurat agar Anda tahu apa yang dapat terdampak oleh kerentanan tertentu.
- Prioritaskan remediasi menurut risiko nyata: gabungkan keparahan, kemampuan dieksploitasi (apakah sedang dieksploitasi di alam liar?), eksposur, dan kekritisan aset alih-alih menambal berdasarkan skor mentah saja.
- Tetapkan dan tegakkan **SLA remediasi** (service-level agreement) menurut tingkat keparahan, dan ukur kepatuhannya.
- Otomatiskan penambalan di tempat Anda dapat dengan aman, terutama untuk infrastruktur dan dependensi.
- Jalankan program **pengungkapan kerentanan terkoordinasi** dengan saluran penerimaan yang jelas dan, bila sesuai, [bug bounty](https://en.wikipedia.org/wiki/Bug_bounty_program), agar peneliti eksternal dapat melaporkan cacat secara bertanggung jawab alih-alih membuangnya ke publik.

### Bersiaplah untuk dan jalankan respons insiden

Ketika insiden menghantam, proses yang dilatih lebih berharga daripada perkakas mana pun.

- Pelihara **rencana respons insiden** dengan peran terdefinisi (komandan insiden, pemimpin komunikasi, penyelidik), klasifikasi keparahan, dan jalur eskalasi.
- Tetapkan fase yang jelas: **persiapan, deteksi dan analisis, penahanan, pemberantasan, pemulihan, dan tinjauan pasca-insiden.**
- Pertahankan bukti dengan benar untuk **[forensik](https://en.wikipedia.org/wiki/Digital_forensics)**: tangkap log, memori, dan citra disk dengan rantai penjagaan terdokumentasi agar temuan bertahan secara hukum dan analisis kokoh.
- Rencanakan **komunikasi pembobolan** sebelumnya: siapa yang memberi tahu pelanggan, regulator, dan publik, pada garis waktu apa, dengan keterlibatan hukum dan humas. Jam regulasi (sering 72 jam atau kurang) mulai berdetak saat penemuan.
- Jalankan **latihan tabletop** secara berkala agar tim mengenal rencana sebelum krisis nyata, dan lakukan tinjauan pasca-insiden tanpa menyalahkan yang menghasilkan perbaikan konkret.

### Operasikan deteksi dengan SIEM dan SOAR, dan rekayasa deteksi

Satukan sinyal keamanan Anda dan bertindaklah atasnya pada skala besar.

- Gunakan **SIEM** (Security Information and Event Management) untuk mengagregasi dan mengorelasikan log dan peristiwa dari seluruh properti, memunculkan pola mencurigakan.
- Gunakan **SOAR** (Security Orchestration, Automation, and Response) untuk mengotomatisasi triase dan playbook respons: memperkaya peringatan, mengisolasi host, menonaktifkan kredensial, dan membuka kasus tanpa menunggu manusia untuk langkah rutin.
- Praktikkan **rekayasa deteksi**: perlakukan aturan deteksi sebagai kode berversi dan teruji yang selaras dengan kerangka seperti [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), ukur tingkat positif benar dan palsunya, dan terus perbaiki cakupan teknik musuh nyata.
- Pastikan pencatatan komprehensif dan tahan-rusak di seluruh aplikasi dan infrastruktur; Anda tidak dapat mendeteksi apa yang tidak Anda catat.

### Validasi pertahanan dengan red dan purple teaming serta uji penetrasi

Menguji pertahanan Anda seperti yang akan dilakukan penyerang adalah satu-satunya cara mengetahui mereka benar-benar berfungsi.

- **Uji penetrasi** memberikan penilaian terfokus pada satu titik waktu atas sistem tertentu, sering untuk kepatuhan.
- **[Red teaming](https://en.wikipedia.org/wiki/Red_team)** mensimulasikan musuh realistis yang mengejar tujuan di seluruh lingkungan Anda, menguji deteksi dan respons maupun pencegahan.
- **Purple teaming** mempertemukan penyerang (red) dan pembela (blue) secara kolaboratif sehingga setiap serangan simulasi segera memperbaiki deteksi dan kendali, mengubah latihan menjadi kemampuan yang bertahan.
- Masukkan semua temuan kembali ke rekayasa deteksi, remediasi, dan pelatihan.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Gerbang pipeline memblokir | Menghentikan masalah yang diketahui agar tidak dikirim | Gesekan, positif palsu membuat tim frustrasi |
| Pemindaian tidak memblokir | Gesekan rendah, pengiriman cepat | Masalah mungkin terkirim; butuh disiplin memperbaiki |
| SOC internal | Konteks dalam, kendali penuh | Mahal, sulit diisi 24/7 |
| Deteksi/respons terkelola | Cakupan 24/7, keahlian siap pakai | Konteks lebih sedikit, ketergantungan vendor |
| Penambalan otomatis | Cepat, menutup jendela dengan cepat | Risiko perubahan yang merusak |
| Red teaming sering | Validasi realistis, menemukan celah nyata | Mahal, padat sumber daya |
| Program bug bounty | Penemuan dari kerumunan, cakupan baik | Beban triase, biaya hadiah, derau |

Ketegangan inti adalah kecepatan versus jaminan, dan cakupan versus biaya. Gerbang memblokir dan penambalan otomatis memaksimalkan jaminan tetapi menambah gesekan dan risiko. Pendekatan tidak memblokir bergerak lebih cepat tetapi bergantung pada tindak lanjut. Deteksi sepanjang waktu esensial pada skala besar namun mahal dibangun secara internal, yang mendorong banyak organisasi ke model hibrida. Jalur yang berkelanjutan mengotomatisasi rutin berkeyakinan tinggi, menyimpan perhatian manusia untuk penilaian sejati, dan terus menyetel keseimbangan memakai hasil terukur alih-alih ketakutan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa SLA remediasi Anda menurut keparahan, dan apa yang sebenarnya menegakkannya?** Arus stabil kerentanan membutuhkan proses sistematis dan terprioritaskan, bukan kepanikan baru pada setiap berita utama, dan SLA menurut tingkat keparahan adalah cara Anda menjaga laju. Putuskan jam Anda (misalnya, kritis dalam hari, tinggi dalam minggu) dan, sama pentingnya, bagaimana Anda mengukur kepatuhan dan siapa yang bertanggung jawab ketika tenggat meleset. Prioritaskan menurut risiko nyata, menggabungkan keparahan dengan kemampuan dieksploitasi di alam liar, eksposur, dan kekritisan aset, alih-alih menambal berdasarkan skor CVSS mentah saja. Bawa backlog temuan terbuka Anda saat ini yang diurutkan menurut usia dan keparahan, karena kritis yang belum ditambal melewati jendelanya adalah bukti yang penting. Jika SLA tidak punya penegakan dan pemilik, ia angan-angan, dan pemindaian tanpa remediasi hanya membangun utang audit dan rasa aman palsu.

2. **Ketika insiden menghantam pukul 2 pagi, siapa komandan insiden dan secepat apa jam regulasi mulai berdetak?** Proses yang dilatih lebih berharga daripada perkakas mana pun, jadi Anda butuh peran bernama (komandan insiden, pemimpin komunikasi, penyelidik), tingkat keparahan terdefinisi, dan jalur eskalasi yang tertulis sebelum krisis. Jam regulasi sering 72 jam atau kurang dan mulai saat penemuan, jadi putuskan sebelumnya siapa yang memberi tahu pelanggan, regulator, dan publik, dan pastikan hukum dan humas terlibat. Mempertahankan bukti forensik dengan rantai penjagaan terdokumentasi harus terjadi sebelum ada yang membangun ulang host terkompromi, atau Anda kehilangan kemampuan memahami atau membuktikan apa yang terjadi. Bawa tanggal latihan tabletop terakhir Anda, karena jika sudah lama atau tak pernah, rencana Anda belum teruji. Untuk tim pemerintah, tenggat pelaporan undang-undang membuat ini tidak opsional, jadi latih jalur notifikasi, bukan hanya respons teknis.

3. **Tindakan respons rutin mana yang akan Anda biarkan dilakukan SOAR tanpa manusia dalam lingkaran?** Otomasi adalah pengali kekuatan yang memungkinkan tim ramping mencakup properti besar, dan metrik yang penting adalah waktu rata-rata merespons, yang dapat dipotong playbook otomatis dari jam menjadi menit. Putuskan tindakan berkeyakinan tinggi mana (mengisolasi host, mencabut kredensial, membuka kasus) yang Anda percayai berjalan otomatis, dan mana yang membutuhkan penilaian manusia lebih dulu. Risikonya positif palsu memicu tindakan yang mengganggu, jadi kaitkan otomasi dengan kualitas deteksi dan setel tanpa ampun, karena sistem yang berteriak serigala akan dimatikan. Bawa volume peringatan dan tingkat positif palsu Anda saat ini, karena angka itu memberi tahu playbook mana yang aman diotomatisasi hari ini. Jika setiap langkah respons menunggu manusia, Anda tidak akan mengimbangi pada skala besar, dan dwell time, yang menggerakkan biaya pembobolan, akan tetap tinggi.

4. **Temuan pipeline mana yang memblokir rilis, mana yang hanya dilacak, dan siapa yang menjaga tingkat positif palsu cukup rendah agar insinyur masih memercayai gerbang?** Pemindai yang berteriak serigala akan diabaikan, dan begitu insinyur kehilangan kepercayaan pada gerbang mereka melobi untuk menghapusnya, sehingga nilai DevSecOps bertumpu pada kualitas sinyal alih-alih cakupan mentah. Ketegangannya nyata: blokir terlalu sedikit dan kode rentan terkirim; blokir terlalu banyak dan Anda menambah gesekan, memperlambat pengiriman, dan membakar niat baik. Bawa tingkat positif benar dan palsu untuk setiap pemindai (SAST, DAST, SCA, IaC, dan pemindaian rahasia), seberapa sering tim menimpa atau menekan gerbang, dan usia temuan yang hanya Anda lacak tanpa memperbaiki. Untuk enterprise atau badan pemerintah yang menjalankan ratusan pipeline, tetapkan kebijakan blokir-versus-lacak secara terpusat dan setel dengan data, karena gerbang yang berbeda sewenang-wenang dari tim ke tim menciptakan celah audit sekaligus kesan bahwa keamanan itu semaunya.

5. **Seberapa yakin Anda bahwa deteksi Anda masih mencakup teknik yang akan dipakai penyerang nyata, dan siapa yang memilikinya sebagai kode teruji dan berversi?** Deteksi meluruh diam-diam seiring lingkungan dan musuh Anda berevolusi, sehingga himpunan aturan yang tampak komprehensif tahun lalu dapat kehilangan cakupan jauh sebelum insiden akhirnya mengungkap celahnya. Memperlakukan deteksi sebagai kode, dikontrol versi, diuji, dan dipetakan ke kerangka seperti MITRE ATT&CK, adalah yang memisahkan praktik rekayasa dari tumpukan peringatan basi, namun ia bersaing untuk waktu analis langka yang sama dengan triase langsung. Bawa peta cakupan ATT&CK Anda saat ini, tingkat positif benar dan palsu terukur dari deteksi teratas Anda, dan hasil latihan purple-team terakhir Anda, karena pengujian kolaboratif red-dan-blue adalah cara tercepat membuktikan deteksi mana yang benar-benar menyala. Dalam pengaturan enterprise dan pemerintah di mana kerangka mungkin diwajibkan, kaitkan setiap deteksi dengan pemilik bernama dan irama tinjauan, karena cakupan yang tak dipelihara siapa pun adalah cakupan yang Anda temukan hilang hanya setelah pembobolan.

6. **Apakah Anda membangun deteksi dan respons secara internal, membeli deteksi dan respons terkelola, atau memadukan keduanya, dan sudahkah Anda menghargai berapa biaya cakupan sepanjang waktu sejati?** Dwell time menggerakkan biaya pembobolan, sehingga jam yang tak tercakup (malam, akhir pekan, hari libur) persis ketika penyusup yang tak terdeteksi melakukan kerusakan paling banyak, namun mengisi staf pusat operasi keamanan 24/7 secara internal mahal dan sulit dipertahankan. Pertukarannya konteks dan kendali versus biaya dan kecepatan menuju cakupan: tim internal mengenal properti Anda secara mendalam tetapi lambat dan mahal dibangun, sementara penyedia terkelola memberi keahlian instan sepanjang waktu dengan harga konteks lebih tipis dan ketergantungan vendor. Bawa jam cakupan Anda saat ini, waktu rata-rata mendeteksi dan merespons Anda di luar jam kerja, volume peringatan Anda, dan pembacaan jujur apakah Anda dapat merekrut dan mempertahankan analis yang dibutuhkan pusat yang dijalankan sendiri. Untuk pemerintah dan enterprise teregulasi, timbang residensi data, izin personel, dan kewajiban pelaporan undang-undang yang harus dapat dipenuhi penyedia, dan pastikan kontrak mempertahankan ketelitian forensik dan rantai penjagaan yang dituntut proses hukum.

## Lensa sektor

**Startup.** Kecepatan dan kelangsungan hidup lebih dulu, jadi beli keamanan sebagai produk sampingan perkakas yang sudah Anda jalankan alih-alih mengisi staf operasi. Sambungkan pemindai gratis ke CI untuk memblokir kebocoran rahasia dan dependensi yang diketahui rentan saat komit, teruskan log ke layanan terkelola berbiaya rendah dengan segelintir peringatan bernilai tinggi, dan tulis rencana insiden satu halaman (siapa yang dihubungi, cara merotasi kredensial, snapshot sebelum membangun ulang) sebelum Anda pernah membutuhkannya. Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi otomatiskan yang rutin dan tahan diri dari mendirikan pusat operasi keamanan yang tak sanggup Anda jalankan terus.

**Bisnis kecil.** Tanpa spesialis keamanan khusus dan dengan anggaran ketat, bersandarlah pada deteksi dan respons terkelola dan pada fitur keamanan yang sudah dibangun ke dalam platform Anda. Perlakukan penambalan dan inventaris aset sebagai kebiasaan berpengungkit tertinggi: ketahui apa yang Anda jalankan, jaga mutakhir, dan tegakkan tenggat remediasi sederhana menurut keparahan. Pilih vendor yang menangani pemantauan sepanjang waktu, penerimaan pengungkapan terkoordinasi, dan penangkapan forensik untuk Anda, dan latih satu hal yang tidak dapat Anda alihdayakan, yaitu memutuskan siapa yang menyatakan insiden dan siapa yang berbicara dengan pelanggan.

**Enterprise.** Tantangannya konsistensi di banyak tim dan ratusan pipeline: kebijakan gerbang blokir-versus-lacak bersama, SLA remediasi yang ditegakkan di seluruh organisasi, platform SIEM dan SOAR dengan deteksi terukur, dan purple teaming yang mengubah setiap latihan menjadi cakupan baru. Kelola operasi keamanan sebagai portofolio dengan dasbor untuk waktu rata-rata mendeteksi dan merespons, kepatuhan SLA, dan presisi deteksi, dan putuskan dengan sengaja di mana kedalaman internal mengalahkan skala terkelola. Anggarkan biaya pengawasan manusia untuk triase dan penyetelan secara eksplisit, karena otomasi menggeser upaya alih-alih menghapusnya.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Tenggat pelaporan insiden undang-undang dan pengungkapan kerentanan terkoordinasi adalah kewajiban, bukan opsi, jadi latih jalur notifikasi ke otoritas nasional sehati-hati respons teknis, dan pertahankan bukti forensik di bawah rantai penjagaan yang tahan pengawasan hukum. Pilih kontrak yang menjaga logika dan data deteksi tetap portabel, tuntut agar penyedia terkelola mana pun memenuhi persyaratan residensi dan izin, dan harapkan penilaian red-team serta pemindaian berkelanjutan memberi masukan ke proses otorisasi yang dapat dipercaya publik.

## Contoh

**Startup.** Sebuah startup tanpa pusat operasi keamanan menyambungkan pemindai gratis ke pipeline CI-nya sehingga kebocoran rahasia dan dependensi yang diketahui rentan tertangkap saat komit, memblokir hanya pada temuan berkeyakinan tinggi agar kedua insinyur tidak tenggelam dalam derau. Mereka menulis rencana insiden satu halaman sebelum membutuhkannya: siapa yang dihubungi, cara merotasi kredensial, dan men-snapshot host terkompromi sebelum membangunnya ulang agar dapat mempelajari apa yang terjadi. Mereka meneruskan log ke layanan terkelola berbiaya rendah dan menyetel beberapa peringatan pada peristiwa yang benar-benar menandakan pembobolan, sehingga masalah muncul dalam jam alih-alih berbulan-bulan yang diperlukan untuk menyadarinya secara tak sengaja.

**Enterprise.** Sebuah perusahaan software-as-a-service menjalankan SAST, SCA, IaC, dan pemindaian rahasia di setiap pipeline, memblokir hanya pada temuan keparahan tinggi berkeyakinan tinggi dan melacak sisanya di dasbor dengan SLA remediasi. SIEM memberi makan platform SOAR yang mengisolasi host dan mencabut kredensial secara otomatis pada peringatan berkeyakinan tinggi, memotong waktu rata-rata merespons dari jam menjadi menit. Latihan purple-team kuartalan terhadap teknik MITRE ATT&CK langsung menghasilkan aturan deteksi baru, terus menutup celah cakupan.

**Pemerintah.** Sebuah lembaga federal mengoperasikan pusat operasi keamanan (SOC) dengan pelaporan insiden yang diwajibkan kepada otoritas siber nasional dalam tenggat undang-undang. Ia menjalankan program pengungkapan kerentanan terkoordinasi dengan saluran penerimaan publik sebagaimana diwajibkan kebijakan, dan mempertahankan bukti forensik di bawah prosedur rantai penjagaan ketat yang cocok untuk proses hukum. Penilaian red-team tahunan dan pemindaian kerentanan berkelanjutan memberi masukan ke otorisasi berkelanjutan lembaga dan SLA remediasi berbasis risikonya.

## Kasus bisnis: motivasi, ROI, dan TCO

Hampir semua tentang kasus operasi keamanan bermuara pada dwell time: semakin lama penyerang tak terdeteksi, semakin mahal pembobolan. Studi secara konsisten menunjukkan insiden yang tertahan cepat berbiaya jauh lebih murah daripada yang berlarut berbulan-bulan. Total biaya kepemilikan mencakup perkakas (SIEM, SOAR, pemindai), staf atau layanan terkelola untuk deteksi dan respons, dan waktu untuk membangun serta melatih proses insiden. Terhadap itu berdiri biaya tidak berinvestasi: pembobolan yang ditemukan terlambat, menyebar lintas sistem, menarik denda regulasi, notifikasi wajib, litigasi, dan kerusakan reputasi, semuanya diperburuk oleh kekacauan respons yang tak dilatih.

ROI datang dari deteksi dan respons lebih cepat, otomasi yang memungkinkan tim ramping mencakup properti besar, dan perbaikan pencegahan yang diumpankan kembali dari setiap insiden dan latihan. DevSecOps khususnya membayar dengan menangkap masalah di pipeline di tempat murah, alih-alih di produksi di tempat mahal dan publik. Ketika mengajukan kasus kepada pimpinan, beri angka pada waktu rata-rata mendeteksi dan merespons Anda saat ini, tunjukkan bagaimana itu terkait dwell time dan biaya, dan bingkai otomasi sebagai pengali kekuatan yang menghindari menumbuhkan jumlah personel selaras dengan properti. Untuk pemerintah, tekankan bahwa kewajiban pelaporan dan pengungkapan undang-undang membuat operasi yang matang tidak opsional.

## Anti-pola dan jebakan

- **Kelelahan peringatan.** Begitu banyak peringatan sehingga analis tak lagi menyimak dan melewatkan yang nyata.
- **Pemindaian tanpa remediasi.** Menghasilkan temuan yang tak diperbaiki siapa pun, menciptakan rasa aman palsu dan utang audit.
- **Tanpa rencana insiden.** Berimprovisasi selama krisis, membuang menit-menit kritis dan salah menangani bukti.
- **Menghancurkan bukti.** Membangun ulang host terkompromi sebelum menangkap forensik, kehilangan kemampuan memahami atau membuktikan apa yang terjadi.
- **Budaya menyalahkan dalam tinjauan.** Menghukum responden sehingga insiden berikutnya disembunyikan atau ditangani defensif.
- **Pentesting hanya demi kepatuhan.** Satu tes tahunan untuk memuaskan auditor, dengan temuan diabaikan sampai tahun depan.
- **Gerbang memblokir dengan positif palsu tinggi.** Mengikis kepercayaan sampai insinyur menuntut gerbang dihapus sepenuhnya.
- **Deteksi atur-dan-lupakan.** Aturan yang meluruh seiring lingkungan dan musuh berevolusi, diam-diam kehilangan cakupan.

## Model kematangan

**Tingkat 1: Memulai.** Operasi keamanan ad hoc dan reaktif. Pengujian keamanan manual dan jarang, dan tidak ada pencatatan pusat atau SIEM. Tidak ada rencana insiden, sehingga respons diimprovisasi saat itu juga. Penambalan terjadi hanya ketika berita utama memaksanya, dan pertahanan tidak pernah diuji secara adversarial.

**Tingkat 2: Mengembangkan.** Praktik dasar muncul tetapi tidak konsisten antartim. Sebagian pipeline menjalankan pemindai sementara yang lain tidak, dan pencatatan pusat ada di kantong-kantong. Rencana insiden dasar terdokumentasi namun jarang dilatih, penambalan mengikuti garis waktu longgar, dan pentest tahunan memuaskan kepatuhan tanpa banyak mengubah. Cakupan dan ketelitian bergantung pada tim mana yang Anda tanya.

**Tingkat 3: Membakukan.** Praktik terdokumentasi dan ditegakkan di seluruh organisasi. Pemindaian DevSecOps penuh dengan gerbang berbasis risiko diterapkan konsisten, SIEM mengorelasikan peristiwa, dan playbook SOAR awal berjalan. Respons insiden dilatih dengan tabletop dan tinjauan tanpa menyalahkan, SLA remediasi menurut keparahan ditegakkan dengan pemilik bernama, dan pengungkapan kerentanan terkoordinasi serta red teaming rutin adalah norma alih-alih pengecualian.

**Tingkat 4: Mengelola.** Operasi diukur dan dikendalikan terhadap garis dasar. Waktu rata-rata mendeteksi dan merespons, kepatuhan SLA menurut tingkat keparahan, cakupan pemindaian, tingkat positif benar dan palsu deteksi, dan dwell time dilacak di dasbor dan ditinjau pada irama. Deteksi membawa presisi dan recall terukur yang dipetakan ke MITRE ATT&CK, keputusan otomasi digerbangi pada data positif palsu alih-alih harapan, dan metrik yang menyimpang melewati garis dasarnya memicu respons terdefinisi alih-alih tak terlihat.

**Tingkat 5: Mengorkestrasi.** Operasi keamanan terus diperbaiki, terintegrasi di seluruh organisasi, dan adaptif. Rekayasa deteksi, purple teaming, remediasi, dan tinjauan insiden memberi makan satu siklus yang beradaptasi dengan teknik musuh baru saat muncul. Playbook otomatis menangani yang rutin di seluruh properti sehingga manusia berkonsentrasi pada penilaian, keamanan direncanakan bersama pengiriman dan risiko, dan setiap insiden dan latihan terukur mengeraskan sistem sementara metrik inti terus menurun.

## Gagasan untuk didiskusikan

1. Temuan pipeline mana yang harus memblokir rilis, dan mana yang sekadar dilacak?
2. Bangun SOC internal, pakai deteksi dan respons terkelola, atau padukan keduanya, dan mengapa?
3. Bagaimana Anda menjaga aturan deteksi agar tidak meluruh seiring lingkungan Anda berevolusi?
4. Seagresif apa penambalan harus diotomatisasi mengingat risiko perubahan yang merusak?
5. Seperti apa tinjauan pasca-insiden yang benar-benar tanpa menyalahkan dalam budaya Anda?
6. Bagaimana Anda mengukur apakah red dan purple teaming benar-benar memperbaiki pertahanan Anda?

## Poin-poin utama

- Pencegahan akhirnya gagal; operasi ada untuk mendeteksi dan merespons dengan cepat.
- Tanamkan SAST, DAST, SCA, IaC, dan pemindaian rahasia dalam pipeline dengan gerbang berbasis risiko.
- Prioritaskan penambalan menurut kemampuan dieksploitasi nyata dan kekritisan aset, di bawah SLA yang ditegakkan.
- Latih respons insiden, pertahankan bukti forensik, dan rencanakan komunikasi pembobolan sebelumnya.
- Gunakan SIEM dan SOAR untuk mengorelasikan dan mengotomatisasi; perlakukan deteksi sebagai kode yang direkayasa dan diuji.
- Validasi pertahanan dengan pentesting, red teaming, dan purple teaming kolaboratif.
- Dwell time menggerakkan biaya pembobolan, jadi waktu rata-rata mendeteksi dan merespons adalah metrik yang penting.

## Referensi dan bacaan lanjutan

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin dan lainnya, *Logging and Log Management* / literatur SIEM
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, panduan *Coordinated Vulnerability Disclosure* dan spesifikasi *CVSS*
