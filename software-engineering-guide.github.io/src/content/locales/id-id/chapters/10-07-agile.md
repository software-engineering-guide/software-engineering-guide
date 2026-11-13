# 10.7 Agile

## Tinjauan dan motivasi

[Agile](https://en.wikipedia.org/wiki/Agile_software_development) adalah pola pikir untuk menyampaikan perangkat lunak (dan nilai) secara iteratif, inkremental, dan dalam kolaborasi erat dengan orang yang akan memakainya. Dikodifikasi dalam *Manifesto for Agile Software Development* tahun 2001, ia paling baik dipahami bukan sebagai proses tetapi sebagai seperangkat **nilai dan prinsip**: mengutamakan individu dan interaksi, perangkat lunak berfungsi, kolaborasi dengan pelanggan, dan tanggap terhadap perubahan, di atas bawaan yang berat rencana, berat kontrak, dan berat dokumentasi yang mendahuluinya. Kerangka seperti [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), dan [Extreme Programming](https://en.wikipedia.org/wiki/Extreme_programming) (XP) adalah *implementasi* dari pola pikir itu. Ia titik awal yang berguna, tetapi bukan pola pikir itu sendiri. Bab ini melengkapi bab 1.4 (cara kerja, yang meninjau metode secara luas) dengan mendalami Agile secara khusus.

Agile digerakkan oleh kekuatan yang sama yang menghidupi jalur penemuan dan penyampaian (bab 11.1–11.2): persyaratan perangkat lunak *ditemukan*, tidak diketahui sepenuhnya di muka, dan dunia berubah lebih cepat daripada yang dapat diserap rencana panjang. Penyampaian big-bang yang merencanakan semuanya lebih dulu berulang kali menghasilkan sistem yang terlambat, melebihi anggaran, dan, yang terburuk, salah, karena semua pembelajaran tiba di akhir, saat paling mahal untuk ditindaklanjuti. Taruhan inti Agile sederhana: siklus pendek membangun perangkat lunak nyata yang berfungsi dan mendapat umpan balik nyata mengalahkan siklus panjang spekulasi. Jika dilakukan baik, ia mengurangi risiko secara berkelanjutan alih-alih menundanya.

Untuk tim besar, enterprise, dan pemerintah, Agile sekaligus kuat dan sering dirusak. Enterprise mengadopsinya di ratusan tim dan sering mereduksinya menjadi ritual ("sekarang kami stand-up") tanpa mengubah cara keputusan dibuat atau nilai diukur. Pemerintah merangkul Agile dengan sengaja, karena penyampaian iteratif yang berpusat pada pengguna terbukti mengurangi risiko program publik besar: U.S. Digital Service dan *Digital Services Playbook*-nya, Government Digital Service Inggris dan Service Standard, serta reformasi pengadaan agile semuanya lahir sebagian sebagai respons terhadap kegagalan [waterfall](https://en.wikipedia.org/wiki/Waterfall_model) berprofil tinggi. Hadiahnya nyata. Begitu juga mode kegagalan "agile hanya nama".

## Prinsip utama

- **Hargai empat nilai Manifesto** (orang, perangkat lunak berfungsi, kolaborasi, dan ketanggapan) di atas artefak proses.
- **Sampaikan perangkat lunak berfungsi secara sering** dalam kenaikan kecil; perangkat lunak berfungsi adalah ukuran utama kemajuan.
- **Sambut perubahan**, bahkan yang terlambat; kemampuan beradaptasi adalah fitur, bukan kegagalan.
- **Bangun di sekitar tim yang termotivasi, diberdayakan, dan mengorganisasi diri.**
- **Berkolaborasi terus-menerus dengan pengguna dan pemangku kepentingan.**
- **Refleksikan dan perbaiki** pada irama teratur.
- **Jaga kecepatan yang manusiawi** dan keunggulan teknis: kecepatan tanpa keahlian runtuh.

## Rekomendasi

### Berlabuh pada nilai dan prinsip, bukan upacara

Rekomendasi Agile terpenting adalah memimpin dengan *mengapa*. Tim yang menggelar stand-up harian, sprint review, dan retrospektif, tetapi masih berkomitmen pada cakupan tetap di tanggal tetap, menyembunyikan kabar buruk, dan tak pernah mengubah rencana, tidak agile. Itu waterfall dengan rapat. Pakai dua belas prinsip sebagai daftar periksa untuk ketangkasan sejati. Apakah Anda sering menyampaikan perangkat lunak berfungsi? Dapatkah Anda menyambut perubahan di iterasi berikutnya? Apakah tim yang memutuskan *bagaimana* mengerjakan? Apakah pelanggan benar-benar dalam lingkaran? Jika upacara tidak menghasilkan hasil itu, perbaiki hasilnya, bukan upacaranya.

### Pilih kerangka sebagai titik awal, bukan agama

Pilih kerangka yang cocok dengan kerja dan adaptasikan:

- **Scrum:** sprint berbatas waktu, backlog berprioritas, dan peran terdefinisi (product owner, scrum master, developer). Baik untuk penyampaian fitur dengan product owner yang jelas; lemah ketika kerja sangat digerakkan interupsi.
- **Kanban:** aliran kontinu dengan batas kerja-dalam-proses (WIP) eksplisit dan sistem tarik. Baik untuk dukungan, operasi, dan kedatangan tak terduga (dan langsung berlandaskan teori aliran dan antrean, lihat bab 11.2, 11.3). Membatasi WIP memperpendek lead time ([Hukum Little](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Extreme Programming (XP):** praktik rekayasa termasuk [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development), [pair programming](https://en.wikipedia.org/wiki/Pair_programming), [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration), refactoring, rilis kecil. Tulang punggung teknis yang membuat kerangka apa pun berkelanjutan.
- **Scrumban** dan campuran: kombinasi pragmatis yang dituju banyak tim matang.

Kerangka adalah perancah. Simpan yang membantu, buang yang tidak, dan jangan biarkan "kerangka bilang begitu" mengalahkan "prinsip menjelaskan mengapa".

### Tuntut keunggulan teknis

Agile tanpa disiplin rekayasa cepat merosot menjadi produksi cepat kode yang tak dapat dipelihara, "dark scrum", di mana tim ber-sprint ke lubang tar cacat dan [utang teknis](https://en.wikipedia.org/wiki/Technical_debt). Praktik XP bukan tambahan opsional. Continuous integration (bab 8.1), pengujian otomatis (bab 2.4), refactoring, pengembangan berbasis trunk (bab 2.6), dan desain bersih (bab 2.2) adalah yang memungkinkan tim terus mengubah perangkat lunak dengan murah, yang merupakan seluruh premis ketangkasan. Kecepatan berkelanjutan penting karena alasan yang sama: tim yang kelelahan tak dapat mempertahankan kualitas atau ketanggapan.

### Skalakan dengan hati-hati, dan pilih pengurangan skala

Kerangka penskalaan, seperti SAFe (Scaled Agile Framework), LeSS, Nexus, dan Scrum@Scale, mengoordinasikan banyak tim menuju tujuan bersama. Ia dapat membantu, tetapi membawa peringatan (menggemakan bab 1.4): kerangka penskalaan berat sering memperkenalkan kembali perintah-dan-kendali serta overhead berat rencana yang ingin dihapus Agile. Sebelum mengadopsi kerangka besar, cobalah *pengurangan skala* (descaling). Organisasikan di sekitar tim independen berselaras aliran dengan kepemilikan jelas dan dependensi lintas tim minimal (bab 1.2), sehingga Anda butuh lebih sedikit mesin koordinasi sejak awal. Di mana koordinasi benar-benar diperlukan, tambahkan struktur teringan yang berfungsi, dan kaitkan dengan hasil (OKR, objectives and key results, bab 11.1), bukan keluaran.

### Wujudkan ketangkasan di enterprise dan pemerintah

Penyampaian adaptif dan kendala institusional dapat hidup berdampingan, tetapi butuh desain yang disengaja:

- **Tata kelola hibrida:** inti penyampaian adaptif di dalam cangkang pendanaan/kepatuhan prediktif (bab 10.6), agar iterasi memuaskan alih-alih melawan pengawasan.
- **Pengadaan agile:** kontrak modular berbasis hasil dan kenaikan lebih pendek alih-alih satu megakontrak cakupan tetap; di sinilah Agile sektor publik paling sering berhasil atau gagal.
- **Kepatuhan sambil jalan:** bangun audit, aksesibilitas (bab 5.3), dan keamanan (bab 4.1) ke dalam kenaikan lewat otomasi dan fitness function (pemeriksaan otomatis yang terus memverifikasi properti arsitektural dan kualitas; bab 8.5, 1.6), bukan gerbang terlambat.
- **Akses pengguna nyata:** yang tersulit dan terpenting. Tim butuh kontak sejati dengan warga atau pelanggan, yang sering dihalangi aturan pengadaan dan keamanan.

### Perbaiki terus-menerus, dan sungguh-sungguh

Retrospektif adalah mesin perbaikan Agile, dan tak berharga jika tak menghasilkan perubahan. Jalankan retrospektif yang menghasilkan sedikit tindakan konkret berpemilik, dan benar-benar selesaikan sebelum yang berikutnya. Ukur hasil (apakah perubahan menggerakkan key result? lihat bab 11.1) dan aliran (apakah lead time menyusut? lihat bab 11.2, 11.3). Jangan ukur velositas: ia sinyal kapasitas yang menjadi kebohongan begitu dipakai sebagai target produktivitas.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| **Agile (adaptif)** | Umpan balik cepat; menyerap perubahan; nilai dini dan berkelanjutan | Lebih sulit menetapkan cakupan/biaya di muka; menuntut pelanggan terlibat dan disiplin |
| **Waterfall (prediktif)** | Cakupan dapat diprediksi; ramah kontrak/audit | Umpan balik terlambat; risiko big-bang; kurang cocok untuk persyaratan tak pasti |
| **Scrum** | Irama, peran, fokus; dipahami luas | Overhead upacara; kesulitan dengan kerja yang digerakkan interupsi |
| **Kanban** | Aliran, batas WIP, fleksibel; hebat untuk ops | Kurang struktur; butuh disiplin menahan batas |
| **Penskalaan berat (SAFe)** | Mengoordinasikan banyak tim; akrab bagi organisasi besar | Dapat memperkenalkan kembali perintah-dan-kendali; berat upacara |
| **Pengurangan skala / otonomi tim** | Overhead koordinasi lebih sedikit; tim lebih cepat | Butuh kopling rendah dan platform/kepemilikan kuat |

Ketegangan penentunya **kemampuan beradaptasi versus keterprediksian**, dan salah baca klasiknya adalah bahwa Agile berarti "tanpa rencana." Bukan. Ia berarti merencanakan terus-menerus dan berkomitmen pada *hasil dan irama* sambil membiarkan *cakupan* lentur. Jebakan berulang lainnya adalah memperlakukan Agile sebagai *hanya* proses (upacara) atau *hanya* rekayasa (XP). Ia butuh keduanya.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Dalam konteks enterprise atau pemerintah Anda, apakah kontrak Anda modular dan berbasis hasil, atau penyampaian terkunci dalam satu megakontrak cakupan tetap?** Pengadaan agile adalah tempat ketangkasan sektor publik paling sering berhasil atau gagal, karena satu kontrak harga tetap, cakupan tetap memaksa waterfall apa pun yang tim penyampaian sebut rapat mereka. Kontrak modular berbasis hasil dengan kenaikan lebih pendek membiarkan cakupan lentur ke inti berharga dalam pendanaan tetap, persis pola di balik keberhasilan sektor publik modern dan penawar kegagalan big-bang masa lalu. Bawa bukti: lihat kontrak Anda saat ini dan tanyakan apakah vendor dibayar untuk perangkat lunak berfungsi yang didemonstrasikan atau untuk cakupan tetap yang ditandatangani bertahun-tahun lalu. Jawabannya harus membentuk cara Anda menstruktur pengadaan berikutnya jauh lebih daripada kerangka mana yang diadopsi tim Anda secara internal. Anda tak dapat adaptif dalam penyampaian sementara kontrak Anda mewajibkan go-live jauh yang semua-atau-tidak-sama-sekali.

2. **Apakah audit, aksesibilitas, dan keamanan dibangun ke setiap kenaikan lewat otomasi, atau ditempelkan sebagai gerbang terlambat?** Kepatuhan-sambil-jalan adalah yang memungkinkan penyampaian adaptif hidup berdampingan dengan kendala institusional: bangun pemeriksaan ke dalam kenaikan lewat otomasi dan fitness function alih-alih menyimpannya untuk perebutan pra-rilis. Gerbang kepatuhan terlambat memperkenalkan kembali risiko big-bang yang justru ingin dihapus Agile, karena masalah mahal muncul di akhir saat paling sulit diperbaiki. Bawa bukti: untuk kenaikan terakhir Anda, periksa apakah aksesibilitas, keamanan, dan bukti audit diverifikasi otomatis di pipeline atau ditunda ke tinjauan manual sebelum peluncuran. Jawabannya harus mendorong properti ini ke pemeriksaan otomatis kontinu, sehingga pengawasan terpuaskan oleh tindakan membangun alih-alih fase terpisah. Ini juga yang menjaga program teregulasi jujur di antara audit alih-alih hanya pada minggu-minggu sebelumnya.

3. **Bagaimana Anda tahu jika tim Anda ber-sprint ke utang teknis, dan apa yang melindungi kecepatan berkelanjutan di bawah tekanan peluncuran?** Agile tanpa disiplin rekayasa merosot menjadi dark scrum, di mana tim ber-sprint cepat ke lubang tar cacat dan kode tak dapat dipelihara, dan tim kelelahan tak dapat mempertahankan kualitas atau ketanggapan. Praktik XP (continuous integration, pengujian otomatis, refactoring, pengembangan berbasis trunk) adalah yang memungkinkan tim terus mengubah perangkat lunak dengan murah, yang merupakan seluruh premis ketangkasan, jadi mereka bukan tambahan opsional untuk dikorbankan ketika tenggat mendekat. Bawa bukti: lacak apakah lead time menyusut atau tumbuh, apakah laju cacat naik, dan apakah tim diam-diam bekerja lebih lama untuk mencapai tiap sprint. Jawabannya harus menjadikan keunggulan teknis dan kecepatan manusiawi tak dapat ditawar, karena kecepatan yang dibeli dengan mengorbankan keahlian runtuh dalam beberapa iterasi. Ukur aliran dan hasil, jangan pernah velositas sebagai target, karena begitu Anda menjadikan sinyal kapasitas sebagai sasaran produktivitas, ia menjadi kebohongan.

4. **Sebelum meraih kerangka penskalaan berat, sudahkah Anda mencoba mengurangi dependensi lintas tim yang menciptakan kebutuhan koordinasi sejak awal?** Ini paling penting bagi organisasi besar, karena refleks ketika banyak tim harus mengirim bersama adalah membeli kerangka seperti SAFe, LeSS, atau Scrum@Scale, dan mesin penskalaan berat sering menyelundupkan kembali perintah-dan-kendali serta overhead berat rencana yang ingin dihapus Agile. Pertimbangan yang bersaing nyata: sebagian koordinasi memang diperlukan, dan pengurangan skala menjadi tim independen berselaras aliran menuntut kopling rendah, kepemilikan jelas, dan platform cukup matang agar tim melayani diri sendiri, yang mungkin belum Anda miliki. Bawa bukti ke diskusi: petakan dependensi aktual yang memaksa tim saling menunggu, dan tanyakan berapa yang akan bertahan dari desain ulang sengaja batas tim dan kepemilikan layanan. Dalam program enterprise dan pemerintah, di mana bagan organisasi puluhan tim lazim, pertanyaan jujurnya adalah apakah Anda menambah struktur koordinasi untuk mengompensasi arsitektur dan desain tim yang dapat Anda sederhanakan, sehingga Anda butuh koordinasi lebih sedikit sama sekali.

5. **Apakah tim Anda punya kontak sejati dan berulang dengan warga atau pelanggan yang mereka bangun untuknya, atau umpan balik tiba tersaring lewat proksi?** Kolaborasi pelanggan adalah satu dari empat nilai Manifesto, dan iterasi yang kekurangan kontak pengguna nyata diam-diam mengoptimalkan hal yang salah, kegagalan termahal yang seharusnya dicegah Agile. Ketegangannya adalah akses langsung sulit diatur pada skala besar dan sering dihalangi aturan pengadaan, privasi, dan keamanan yang harus dihormati organisasi besar dan publik, sehingga jalan mudahnya mengganti dengan proksi: analis bisnis, komite pemangku kepentingan, atau dek riset kuartal lalu. Bawa bukti: untuk beberapa kenaikan terakhir Anda, hitung berapa yang divalidasi dengan pengguna nyata yang benar-benar memakai perangkat lunak, dan berapa yang bertumpu pada opini seseorang tentang apa yang diinginkan pengguna. Untuk layanan pemerintah, tambahkan apakah uji kebergunaan Anda menjangkau orang yang paling terdampak, termasuk pengguna teknologi bantu dan mereka dengan kepercayaan diri digital rendah, karena layanan publik yang hanya berfungsi bagi mayoritas percaya diri telah gagal dalam kewajiban akuntabilitasnya meski setiap upacara berjalan tepat jadwal.

6. **Apakah tim Anda didanai dan diatur di sekitar hasil dan irama, atau di sekitar cakupan tetap yang diam-diam memaksa waterfall di balik upacara?** Inilah beda antara ketangkasan sejati dan agile palsu, dan ia diputuskan di atas tim, dalam cara uang dilepas dan keberhasilan dilaporkan, bukan dalam apakah stand-up terjadi. Tarikan yang bersaing adalah fungsi keuangan, portofolio, dan pengawasan dibangun untuk menyetujui cakupan tetap terhadap anggaran tetap bertahun-tahun sebelumnya, dan meminta mereka mendanai hasil dengan cakupan fleksibel terasa seperti kehilangan kendali yang akan mereka lawan. Bawa bukti: telusuri bagaimana inisiatif saat ini didanai dan apa yang dilaporkannya, dan periksa apakah tim diukur pada hasil dan aliran terkirim atau pada story point dan kepatuhan pada cakupan yang ditandatangani lama lalu. Dalam pengaturan enterprise dan pemerintah, kaitkan ini langsung dengan cangkang pendanaan dan kepatuhan (bab 10.6): jika uang terikat pada go-live jauh yang semua-atau-tidak-sama-sekali, tim tak dapat adaptif seberapa pun setia mereka menjalankan ritual, dan perbaikannya milik model tata kelola alih-alih tim penyampaian.

## Lensa sektor

**Startup.** Hiduplah dengan nilai-nilainya dan lewati debat kerangka. Kirim irisan berfungsi ke pengguna nyata setiap minggu, duduk cukup dekat dengan pendiri dan pelanggan awal agar umpan balik tiba harian, dan sambut perubahan arah begitu bukti mengatakan taruhan saat ini salah. Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi lindungi keunggulan teknis (continuous integration, tes otomatis, pengembangan berbasis trunk) bahkan di bawah tekanan peluncuran, karena disiplin itu yang menjaga Anda mampu berputar arah dengan murah minggu depan.

**Bisnis kecil.** Tanpa pelatih agile dan anggaran ketat, perlakukan Agile sebagai segelintir kebiasaan alih-alih program transformasi yang Anda staf-i: siklus mingguan singkat, papan terlihat dengan batas kerja-dalam-proses, dan satu perbaikan konkret setiap minggu yang benar-benar Anda selesaikan. Bersandarlah pada Kanban, yang butuh sedikit upacara dan cocok untuk kerja yang digerakkan interupsi, dan adopsi praktik yang tertanam dalam perkakas yang sudah Anda beli alih-alih mendirikan proses berat. Nilai upaya itu dari apakah Anda mengirim perangkat lunak berguna kepada pelanggan lebih sering, bukan dari seberapa dekat Anda meniru Scrum.

**Enterprise.** Masalahnya mengoordinasikan banyak tim tanpa memperkenalkan kembali perintah-dan-kendali. Pilih pengurangan skala, yaitu mengurangi dependensi lintas tim lewat desain tim berselaras aliran dan platform solid, sebelum mengadopsi kerangka penskalaan berat. Danai dan atur di sekitar hasil (OKR) dan irama alih-alih cakupan tahunan tetap dan story point, jadikan praktik rekayasa gaya XP tak dapat ditawar di semua tim, dan kelola penyampaian sebagai portofolio dengan metrik aliran dan ukuran hasil agar kelompok memperbaiki diri atas bukti alih-alih ritual.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Susun kontrak modular berbasis hasil dengan kenaikan lebih pendek alih-alih satu megakontrak cakupan tetap, karena pengadaan agile adalah tempat ketangkasan sektor publik paling sering berhasil atau gagal. Bangun audit, aksesibilitas, dan keamanan ke setiap kenaikan lewat otomasi agar pengawasan terpuaskan oleh tindakan membangun, terbitkan kemajuan dan bukti nilai publik kepada badan pengawas, dan perjuangkan akses sejati ke warga (termasuk pengguna teknologi bantu) setiap iterasi, karena itulah kendala yang paling sering dinegosiasikan hilang.

## Contoh

**Startup.** Startup lima orang melewati debat upacara dan menghidupi nilai Agile secara langsung. Ia mengirim irisan berfungsi ke pengguna nyata setiap minggu, duduk cukup dekat dengan pendiri dan pelanggan awal agar umpan balik tiba harian, dan menyambut perubahan arah minggu depan ketika bukti mengatakan taruhan saat ini salah. Tim menolak menukar keunggulan teknis dengan kecepatan, sehingga continuous integration, tes otomatis, dan pengembangan berbasis trunk tak dapat ditawar bahkan di bawah tekanan peluncuran, dan setiap retrospektif Jumat menghasilkan satu perubahan konkret yang benar-benar diselesaikan tim sebelum yang berikutnya. Ia tak pernah melacak velositas sebagai target, melainkan mengukur apakah kerja terkirim menggerakkan aktivasi dan apakah lead time menyusut.

**Enterprise.** Transformasi 60 tim sebuah telekomunikasi awalnya "melakukan Scrum" tetapi tak melihat perbaikan. Tim masih menerima cakupan tahunan tetap dan melapor velositas. Pengaturan ulang memfokuskan kembali pada prinsip: OKR kuartalan menggantikan mandat fitur, tim diorganisasi ulang untuk mengurangi dependensi lintas tim (pengurangan skala), dan praktik XP (CI, TDD, pengembangan berbasis trunk) dijadikan tak dapat ditawar. Lead time turun, cacat berkurang, dan, yang krusial, bisnis mulai mengukur hasil alih-alih story point, menghubungkan penyampaian Agile ke jalur penemuan (bab 11.1).

**Pemerintah.** Tim layanan digital membangun ulang aplikasi tunjangan yang menghadap warga memakai Agile di dalam cangkang tata kelola hibrida: kenaikan dua minggu yang menyampaikan perangkat lunak berfungsi dan teruji pengguna; aksesibilitas dan keamanan dibangun ke setiap kenaikan; dan pengadaan modular menggantikan satu kontrak harga tetap. Uji kebergunaan nyata dengan warga (termasuk pengguna teknologi bantu) setiap iterasi menangkap masalah yang akan dikirim proses waterfall lama. Program menyampaikan layanan yang dapat dipakai lebih awal dan menunjukkan nilai publik terukur kepada badan pengawas. Ini pola di balik keberhasilan sektor publik modern, dan penawar kegagalan big-bang masa lalu.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil Agile datang dari **pengurangan risiko dan realisasi nilai lebih cepat**. Dengan menyampaikan perangkat lunak berfungsi lebih awal dan sering, tim mengubah ketidakpastian menjadi bukti secara kontinu, menangkap kegagalan hal-salah dan tak-akan-berfungsi selagi murah, alih-alih di go-live yang jauh dan mahal. Riset di balik penyampaian modern (temuan DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), di bab 11.2) menunjukkan bahwa praktik yang dipromosikan Agile (batch kecil, rilis sering, umpan balik cepat, keunggulan teknis) berkorelasi dengan penyampaian lebih baik *dan* stabilitas *dan* kinerja organisasi. Kenaikan awal juga mulai mengembalikan nilai lebih cepat, memperbaiki waktu dan total ukuran ROI dibanding rilis big-bang yang tak mengembalikan apa pun sampai akhir.

Pada **[total biaya kepemilikan](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, Agile menurunkan biaya perubahan sepanjang umur sistem, asalkan disiplin rekayasanya nyata. Risiko dominannya adalah *agile palsu*: upacara tanpa prinsip atau keahlian, yang menambah overhead rapat sambil tak menyampaikan manfaat, dan dapat lebih buruk daripada waterfall yang jujur. Jadi kasus bisnisnya bersyarat. ROI tinggi ketika Anda mengadopsi Agile sebagai pola pikir-plus-rekayasa, dan nyaris nol (atau negatif) ketika Anda mengadopsinya sebagai ritual. Ajukan kasus kepada pimpinan dengan membingkai Agile sebagai pengurangan risiko kontinu dan pengukuran hasil, bukan sebagai "menjadi lebih cepat," dan dengan menegaskan bahwa investasinya mencakup praktik teknis, bukan hanya rapat baru.

## Anti-pola dan jebakan

- **Agile palsu / kultus kargo:** upacara dilakukan sementara keputusan, pendanaan, dan pola pikir tetap waterfall.
- **Velositas sebagai produktivitas:** mengubah estimasi kapasitas menjadi target, yang merusaknya ([Hukum Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dark scrum:** ber-sprint tanpa keunggulan teknis ke kode tak dapat dipelihara dan penuh cacat.
- **Retrospektif tanpa perubahan:** refleksi yang tak menghasilkan tindakan selesai.
- **Cakupan *dan* tanggal *dan* biaya tetap:** menyebutnya agile sementara kualitas diam-diam menyerap tekanan.
- **Pelanggan absen:** tanpa umpan balik pengguna nyata, sehingga iterasi mengoptimalkan hal yang salah.
- **Pemujaan kerangka:** "SAFe/Scrum bilang begitu" mengalahkan prinsip dan penilaian tim.
- **Penskalaan sebelum pengurangan skala:** menambah kerangka koordinasi berat alih-alih mengurangi dependensi.

## Model kematangan

- **Tingkat 1, Memulai.** Penyampaian waterfall atau ad hoc; rilis big-bang; kerja reaktif dan berat rencana, tanpa umpan balik iteratif dan tanpa rasa bersama mengapa Agile mungkin membantu.
- **Tingkat 2, Mengembangkan.** Beberapa tim mengadopsi upacara Agile (stand-up, sprint, retrospektif), tetapi praktik tidak konsisten di seluruh organisasi: pola pikir dan disiplin rekayasa tertinggal di belakang ritual, velositas diperlakukan sebagai keluaran, dan cakupan masih tetap di muka.
- **Tingkat 3, Membakukan.** Nilai dan prinsip benar-benar memandu kerja di seluruh organisasi, terdokumentasi dan diharapkan dari setiap tim: keunggulan teknis gaya XP (CI, pengujian otomatis, refactoring, pengembangan berbasis trunk) adalah praktik standar, tim mengorganisasi diri, pelanggan dilibatkan setiap iterasi, dan retrospektif menghasilkan perubahan konkret yang selesai.
- **Tingkat 4, Mengelola.** Penyampaian diukur dan dikendalikan terhadap garis dasar: tim melacak lead time, frekuensi deployment, laju kegagalan perubahan, dan laju lolosnya cacat (metrik aliran dan stabilitas gaya DORA), di samping ukuran hasil yang terkait key result, dan membandingkan masing-masing dengan garis dasar yang diketahui. Tindakan retrospektif dilacak sampai selesai, sinyal kecepatan berkelanjutan seperti lembur dan kelelahan dipantau, dan velositas tak pernah dipakai sebagai target produktivitas. Keputusan maju dan tahan bertumpu pada bukti ini alih-alih opini.
- **Tingkat 5, Mengorkestrasi.** Penyampaian adaptif terintegrasi dengan perencanaan bisnis dan risiko di seluruh organisasi: hasil (OKR) menggerakkan pendanaan dan irama, desain tim berdependensi rendah (pengurangan skala) meminimalkan overhead koordinasi, dan tata kelola hibrida memuaskan pengawasan tanpa memperlambat penyampaian. Perbaikan berkelanjutan bersifat budaya alih-alih seremonial, dan organisasi rutin menentukan ulang cakupan, menyusun ulang tim, dan menyeimbangkan ulang portofolionya seiring bukti dan gambaran risiko bergeser.

## Gagasan untuk didiskusikan

1. Nilai tim Anda terhadap dua belas prinsip Agile: di mana Anda agile dalam upacara tetapi tidak dalam substansi?
2. Apakah velositas di tim Anda dipakai sebagai perkiraan atau sebagai target, dan apa yang dilakukannya terhadap perilaku?
3. Praktik teknis XP mana yang hilang, dan bagaimana ketiadaannya muncul sebagai cacat atau perubahan lambat?
4. Sebelum mengadopsi kerangka penskalaan, dapatkah Anda mengurangi dependensi lintas tim sebagai gantinya?
5. Dalam konteks Anda, apa secara spesifik yang menghalangi akses pengguna nyata setiap iterasi, dan bagaimana Anda dapat menghapusnya?
6. Apa perubahan konkret terakhir yang benar-benar dihasilkan retrospektif?

## Poin-poin utama

- Agile adalah **pola pikir nilai dan prinsip**, bukan seperangkat upacara; kerangka adalah titik awal, bukan tujuan.
- Sampaikan **perangkat lunak berfungsi secara sering**, sambut perubahan, dan berdayakan **tim yang mengorganisasi diri**.
- **Keunggulan teknis (praktik XP) tak dapat ditawar.** Ketangkasan tanpanya menjadi pembusukan cepat.
- **Skalakan dengan hati-hati; pilih pengurangan skala.** Kurangi dependensi sebelum menambah kerangka koordinasi.
- Di enterprise/pemerintah, gabungkan **penyampaian adaptif dengan tata kelola hibrida dan pengadaan agile**, dan perjuangkan akses pengguna nyata.
- ROI-nya **pengurangan risiko kontinu dan nilai lebih awal**, tetapi hanya ketika Agile nyata, bukan ritual. Lihat bab 1.4, 11.1, 11.2, 10.6, dan 11.3.

## Referensi dan bacaan lanjutan

- Kent Beck et al., *Manifesto for Agile Software Development* dan dua belas prinsipnya (agilemanifesto.org, 2001).
- Ken Schwaber dan Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* dan *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton dan Manuel Pais, *Team Topologies* (desain tim dan pengurangan skala).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (bukti untuk praktik agile/DevOps).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
