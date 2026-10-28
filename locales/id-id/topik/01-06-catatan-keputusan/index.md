# 1.6 Catatan keputusan

## Tinjauan dan motivasi

**Catatan keputusan (decision record)** adalah dokumen yang menangkap sebuah keputusan penting beserta konteks dan konsekuensinya. Bentuk yang paling dikenal adalah **[catatan keputusan arsitektur](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, catatan singkat yang sebaiknya tak berubah yang merekam satu pilihan penting secara arsitektural, mengapa pilihan itu dibuat, dan apa akibatnya. Kumpulan lengkap catatan sebuah proyek adalah **log keputusannya (ADL)**, dan disiplin memeliharanya adalah bagian dari **manajemen pengetahuan arsitektur (AKM)**. Bab ini membangun di atas praktik pengambilan keputusan dan tata kelola dari bab 1.5, dengan fokus pada bagaimana Anda menulis, menyimpan, dan menjaga catatan keputusan pada skala besar.

Motivasinya sederhana, dan menyakitkan jika dipelajari dengan cara sulit. Pada sistem berumur panjang mana pun, pertanyaan yang paling mahal adalah "mengapa sih ini dibangun seperti ini?", yang diajukan berbulan-bulan atau bertahun-tahun kemudian oleh orang yang tidak ada di ruangan itu. Kode menunjukkan *apa* yang dilakukan sistem. Tes menunjukkan bahwa ia *bekerja*. Tetapi keduanya tidak menangkap *mengapa* Anda memilih jalan ini dibandingkan alternatif yang Anda pertimbangkan dan tolak. Tanpa catatan keputusan, alasan itu menguap bersama pergantian staf. Tim mengadili ulang pertanyaan yang sudah selesai, membalik keputusan baik karena alasan buruk, atau mempertahankan keputusan buruk karena takut. Catatan keputusan adalah surat murah untuk masa depan yang menjaga alasan.

Bagi tim besar, ini sama banyaknya alat koordinasi seperti alat bantu ingatan. Enterprise menjalankan puluhan tim yang membuat pilihan yang saling tumpang-tindih. Log keputusan bersama mengubah alasan yang diperoleh susah payah oleh satu tim menjadi aset yang dapat dipakai ulang, dan mencegah keputusan yang berbeda dan tidak kompatibel. Dalam konteks pemerintah dan yang diatur regulasi, catatan keputusan hampir wajib. Auditor, badan pengawas, dan kontraktor penerus semuanya membutuhkan alasan yang dapat dilacak yang menghubungkan persyaratan penting secara arsitektural dengan pilihan yang dibuat terhadapnya. Log keputusan yang terpelihara dengan baik sering menjadi pembeda antara sistem yang dapat Anda jamin dan audit dengan yang tidak.

## Prinsip utama

- **Catat *mengapa*, bukan hanya *apa*.** Konteks dan alternatif yang ditolak adalah intinya.
- **Satu keputusan per catatan.** Jaga setiap catatan spesifik dan berdiri sendiri.
- **Kecil dan ringan mengalahkan menyeluruh tetapi tak terpakai.** Catatan satu halaman yang ada mengalahkan laporan yang tidak pernah ditulis.
- **Beri cap waktu pada segalanya.** Biaya, kendala, dan vendor berubah; beri tanggal pada setiap klaim.
- **Pilih log hidup secara pragmatis.** Ketakberubahan adalah idealnya; dalam praktik, ubah dengan catatan bertanggal.
- **Kata-kata di atas singkatan.** "Keputusan" mengundang lebih banyak kontribusi daripada "ADR."
- **Jadikan keputusan mudah ditemukan dan, bila mungkin, dapat diuji.** Munculkan catatan yang tepat pada saat yang tepat; jaminkan dengan fitness function.

## Rekomendasi

### Tangkap struktur esensial

Catatan keputusan yang baik memiliki beberapa bagian esensial. Adaptasi templat yang dikenal alih-alih menciptakan sendiri:

- **Judul:** frasa imperatif singkat dalam kala kini ("Gunakan [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) untuk buku besar").
- **Status:** diusulkan, diterima, digantikan, usang.
- **Konteks:** situasi, gaya-gaya, prioritas bisnis, dan kendala yang membuat keputusan ini perlu; sertakan persyaratan penting secara arsitektural yang ditanganinya.
- **Keputusan:** pilihan yang diambil, dinyatakan dengan lugas.
- **Konsekuensi:** apa yang menjadi lebih mudah dan apa yang menjadi lebih sulit, keputusan lanjutan yang dipicu, dan risiko yang diterima.

Templat populer mencakup milik Michael Nygard (sederhana dan banyak diadopsi), milik Tyree dan Akerman (lebih rumit, dengan alternatif berbobot), MADR (Markdown Any Decision Records, kuat pada opsi dan untung-ruginya), dan Y-statement (bentuk terstruktur satu kalimat). Bakukan satu per organisasi, agar catatan dapat dibandingkan. Lihat bab 12.3 untuk templat salin-tempel.

### Tulis catatan yang spesifik, bertanggal, dan nyaris tak berubah

Jaga setiap catatan tentang tepat satu keputusan. Beri cap waktu pada klaim individual, terutama yang bergeser: harga, angka penskalaan, kemampuan vendor, syarat lisensi. Secara teori, catatan harus tak berubah. Ketika keputusan berubah, Anda menulis catatan *baru* yang menggantikan yang lama, mempertahankan sejarah. Dalam praktik, banyak tim mendapati pendekatan **dokumen hidup** lebih baik: sisipkan informasi baru ke catatan yang ada dengan cap tanggal dan catatan bahwa ia tiba setelah keputusan. Keduanya sah. Gaya tak berubah lebih kuat untuk jejak audit; gaya hidup lebih baik untuk pengetahuan tim sehari-hari. Pilih dengan sengaja, dan konsisten.

### Simpan catatan di tempat pekerjaan berlangsung

Taruh catatan keputusan di [kontrol versi](https://en.wikipedia.org/wiki/Version_control) bersama kode: direktori `decisions/` (atau `adr/`) berisi berkas [Markdown](https://en.wikipedia.org/wiki/Markdown), satu per keputusan, dinamai dengan frasa kata kerja imperatif huruf kecil yang dipisah tanda hubung (`choose-database.md`, `format-timestamps.md`). Ini memberi Anda sejarah, tinjauan, dan diff secara gratis, dan menjaga alasan di samping apa yang dijelaskannya. Jika tim Anda lebih suka [wiki](https://en.wikipedia.org/wiki/Wiki), Google Docs, atau pelacak ala Jira, gunakan itu. Perkakasnya jauh kurang penting daripada kebiasaan. Perkakas baris perintah ringan (seperti `adr-tools`) dapat membuat kerangka dan mengindeks catatan.

### Namai "keputusan," dan perluas melampaui arsitektur

Wawasan praktis dari banyak tim: label itu penting. Sebagian pengembang dan manajer berkeberatan dengan kata "arsitektur," dan "catatan" dapat terasa seperti administrasi setelah kejadian. Mengganti nama direktori menjadi sekadar "decisions" sering membalik sakelar. Tim mulai mencatat pilihan vendor, keputusan perencanaan, keputusan penjadwalan, keputusan data dan kepatuhan, semuanya dengan templat yang sama. Orang belajar lebih cepat dari kata-kata daripada singkatan, dan mereka berkontribusi lebih banyak ketika bingkainya adalah "bantu rekan masa depan Anda berpikir" alih-alih "isi formulir wajib."

### Tetapkan siklus hidup dan tata kelola

Agar catatan keputusan dapat diskalakan, sepakati proses di sekitarnya (di sinilah tata kelola bab 1.5 bertemu praktik):

- **Siapa yang dapat mengajukan satu, dan apa yang membenarkannya:** biasanya kontributor mana pun yang paham; ajukan catatan ketika pengembang masa depan akan membutuhkan *mengapa*, dan lewati untuk pilihan berisiko rendah, berdiri sendiri, atau sudah terdokumentasi.
- **Siklus hidup:** alur sederhana seperti *Memulai → Meneliti → Mengevaluasi → Mengimplementasi → Memelihara → Mengakhiri*, dengan kriteria penerimaan untuk berpindah antartahap (masalah dirumuskan, alternatif dipertimbangkan, trade-off didokumentasikan, pemangku kepentingan dikonsultasi).
- **Peran:** pengusul, peneliti, peninjau, penyetuju, dan pemelihara yang bertanggung jawab yang meninjau catatan secara berkala (setidaknya tahunan) dan mendorong pengakhiran akhirnya.
- **Tata kelola:** bagaimana konsensus, konflik, eskalasi, dan veto bekerja, dan kendala kepatuhan apa pun. Bersandarlah pada prinsip seperti *condong ke tindakan* dan *[disagree-and-commit](https://en.wikipedia.org/wiki/Disagree_and_commit)*, dan sisakan proses yang lebih berat untuk keputusan tak terbalikkan berdampak besar ("pintu satu arah").

### Buat keputusan dapat diuji dan ditemukan

Catatan keputusan *mendokumentasikan* sebuah keputusan; **fitness function** *menjaminnya*: pemeriksaan otomatis, dijalankan dalam [integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration) (CI), yang memverifikasi keputusan masih berlaku ("semua perubahan status harus memancarkan event," "tidak ada modul yang boleh mengimpor melintasi batas ini," dengan perkakas seperti ArchUnit). Ini mengubah tata kelola dari tinjauan manual berkala menjadi penegakan berkelanjutan yang skalabel, yang sangat berharga untuk tujuan regulasi dan audit (bab 3.1, 4.6, 8.5). Lalu munculkan catatan yang *tepat* pada saat yang *tepat*. Perkakas yang melampirkan keputusan relevan ke pull request, ketika pengembang menyentuh kode yang diaturnya, mengalahkan berharap orang membaca folder dokumen.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan |
|---|---|---|
| **ADR ringan (Nygard/MADR)** | Cepat ditulis, benar-benar ditulis; upacara rendah | Kurang ketat untuk keputusan taruhan tinggi yang diperdebatkan |
| **Templat berat (Tyree-Akerman)** | Alternatif berbobot; kuat untuk pilihan besar dan mahal | Lebih lambat; dapat mencegah pencatatan rutin |
| **Tak berubah + menggantikan** | Jejak audit bersih; sejarah terjaga | Lebih banyak catatan; pembaca harus menelusuri rantai |
| **Dokumen hidup (perubahan bertanggal)** | Satu sumber kebenaran terkini; mudah dipelihara | Cerita audit lebih lemah; risiko suntingan diam-diam |
| **Markdown dalam repo** | Berversi, dapat ditinjau, di samping kode | Kurang ramah bagi non-pengembang |
| **Wiki / perkakas dokumen** | Dapat diakses semua peran | Sejarah dan tinjauan lebih lemah; menyimpang dari kode |

Ketegangan intinya adalah **ketelitian versus adopsi**. Sistem paling teliti yang tidak dipakai siapa pun tidak mencatat apa-apa. Sistem teringan yang dipakai semua orang berlipat nilainya. Pilih ringan sebagai bawaan, dan sisakan proses lebih berat untuk beberapa keputusan yang mahal dan sulit dibalik.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Bagaimana catatan keputusan yang tepat akan sampai kepada pengembang pada saat ia menyentuh kode yang diaturnya, alih-alih mengendap dalam folder yang tidak dibuka siapa pun?** Log yang hanya ditulis merekam alasan yang tidak pernah mengubah perilaku, cara paling umum catatan keputusan gagal: mereka ada, dan tak seorang pun membacanya ketika penting. Pertimbangan yang bersaing adalah upaya, karena memunculkan catatan secara otomatis (melampirkannya ke pull request ketika seseorang mengedit kode yang diatur) memerlukan investasi perkakas yang tidak dibutuhkan wiki atau folder dokumen. Bawa bukti ke diskusi: ketika seseorang baru-baru ini membalik atau mengadili ulang pertanyaan yang sudah selesai, apakah catatan yang relevan dapat ditemukan saat itu, atau terkubur? Bagi organisasi besar yang menjalankan puluhan tim, kemudahan ditemukan adalah yang mengubah alasan hasil jerih payah satu tim menjadi aset yang dapat dipakai ulang alih-alih arsip pribadi. Putuskan apakah menyimpan catatan di kontrol versi di samping kode dan mengaitkannya ke alur pull request, agar catatan muncul di tempat pekerjaan berlangsung.

2. **Siapa pemelihara yang bertanggung jawab untuk setiap catatan, dan apa yang mencegah log Anda membusuk menjadi misinformasi yang percaya diri?** Mode kegagalan berbahaya log keputusan bukan folder kosong, melainkan folder penuh catatan yang biaya, kemampuan vendor, dan kendalanya diam-diam usang bertahun-tahun lalu. Setiap catatan membutuhkan pemilik yang bertanggung jawab yang meninjaunya secara berkala (setidaknya tahunan) dan mendorong penggantian atau pengakhiran, atau log membusuk menjadi cerita rakyat yang dikutip orang secara selektif dan kurang dipercaya. Bawa bukti: berapa banyak catatan Anda yang tidak bertanggal, berapa banyak yang menggambarkan vendor atau harga yang sejak itu berubah, dan kapan masing-masing terakhir ditinjau. Dalam konteks pemerintah dan yang diatur regulasi, ini lebih tajam, karena rantai tak berubah yang digantikan adalah persis yang diandalkan auditor dan kontraktor penerus untuk alasan yang dapat dilacak. Tetapkan siklus hidup Anda secara eksplisit, beri cap waktu pada klaim individual yang bergeser, dan tugaskan pemelihara, agar log tetap menjadi aset hidup alih-alih kuburan.

3. **Haruskah Anda membakukan satu templat di semua tim, dan seberapa ketat sebenarnya keputusan dengan taruhan tertinggi Anda memerlukannya?** Keterbandingan adalah manfaat nyata: ketika setiap tim memakai bentuk yang sama (Nygard, MADR, atau serupa), tim baru dapat menemukan tiga catatan sebelumnya dan mengadopsi alasannya dalam satu sore alih-alih sebulan debat. Ketegangan intinya adalah ketelitian versus adopsi, karena templat terberat yang tidak dipakai siapa pun tidak mencatat apa-apa, sementara yang teringan yang dipakai semua orang berlipat nilainya. Bawa bukti: apakah catatan benar-benar ditulis, dan secara terpisah, apakah ada keputusan besar, diperdebatkan, dan mahal yang kurang dianalisis karena bentuk ringan melewatkan penimbangan alternatif? Bagi enterprise yang mengoordinasikan pilihan yang tumpang-tindih di antara tim, templat bersama ditambah indeks yang dapat dicari mencegah keputusan yang berbeda dan tidak kompatibel. Pilih ringan sebagai bawaan untuk kasus umum, dan sepakati sebelumnya keputusan pintu satu arah mana yang layak mendapat bentuk lebih berat dengan alternatif berbobot.

4. **Apa yang sebenarnya membenarkan pengajuan catatan keputusan, dan siapa yang berwenang mengatakan suatu pilihan tidak membutuhkannya?** Tetapkan batas terlalu tinggi dan alasan di balik pilihan penting menguap; tetapkan terlalu rendah dan log dipenuhi hal sepele yang mengubur catatan yang benar-benar dibutuhkan orang. Bagi organisasi besar, ambang yang tidak jelas berarti setiap tim berimprovisasi sendiri, sehingga cakupan menjadi tidak merata dan tak seorang pun dapat percaya bahwa catatan yang hilang menandakan keputusan yang tidak penting. Bawa bukti ke diskusi: segelintir keputusan terbaru yang dicatat padahal tidak perlu, dan yang menyakitkan yang tidak dicatat dan kemudian membuat Anda menemukan ulang dengan biaya. Sepakati uji sederhana, seperti mencatat setiap kali pengembang masa depan akan membutuhkan *mengapa* dan melewati pilihan berisiko rendah, berdiri sendiri, atau sudah terdokumentasi. Dalam konteks pemerintah dan yang diatur regulasi, hitungannya bergeser, karena mandat audit mungkin mensyaratkan catatan untuk setiap persyaratan penting secara arsitektural terlepas dari apakah tim menilainya layak ditulis, jadi sebutkan keputusan mana yang tidak dapat ditawar sejak awal.

5. **Apakah catatan Anda adalah alasan sejati yang ditangkap pada saat keputusan, atau administrasi yang ditulis kemudian untuk memenuhi mandat?** Catatan yang dibuat setelah kejadian untuk menutup tiket cenderung mencuci opsi terpilih dan diam-diam menghilangkan alternatif yang sebenarnya ditimbang, persis informasi yang paling dibutuhkan pembaca masa depan. Tekanan yang bersaing itu nyata: menulis *mengapa* sebelum atau selama keputusan terasa lebih lambat daripada merilis, dan mengakui jalur yang ditolak secara tertulis memerlukan rasa aman psikologis yang tidak dimiliki sebagian tim. Bawa sampel catatan terbaru ke meja dan tanyakan dengan jujur apakah konteks dan alternatif yang ditolak terbaca sebagai pertimbangan nyata atau pembenaran yang direka belakangan. Bagi tim besar, catatan kosong lebih buruk daripada tidak ada, karena mengajari orang bahwa log tidak dapat dipercaya. Dalam audit enterprise dan pemerintah perbedaan ini tajam: badan pengawas dan kontraktor penerus bergantung pada alasan yang mencerminkan apa yang benar-benar dipertimbangkan, dan catatan yang terbaca sebagai sandiwara merusak jaminan yang seharusnya diberikan log.

6. **Keputusan dengan taruhan tertinggi mana yang dapat Anda jamin dengan fitness function otomatis, alih-alih percaya bahwa tinjauan manual berkala akan menangkap pelanggaran?** Catatan keputusan mendokumentasikan pilihan, tetapi hanya pemeriksaan otomatis yang dijalankan dalam integrasi berkelanjutan yang menjaga pilihan itu tidak terkikis diam-diam saat puluhan pengembang menyentuh kode selama bertahun-tahun. Trade-off-nya adalah investasi, karena menulis dan memelihara fitness function (dengan perkakas seperti ArchUnit) memakan waktu rekayasa, dan banyak keputusan, terutama pilihan proses atau vendor, sama sekali tidak dapat diuji secara mekanis. Bawa bukti: keputusan batas mana (dependensi modul, pemancaran event, aturan akses data) yang diam-diam dilanggar dan baru tertangkap terlambat dalam tinjauan atau di produksi. Bagi enterprise yang menjalankan banyak tim, fitness function mengubah tata kelola dari hambatan pusat menjadi penegakan berkelanjutan yang skalabel tanpa memperlambat semua orang. Dalam konteks pemerintah dan yang diatur regulasi, pemeriksaan otomatis yang selalu aktif adalah bukti audit yang jauh lebih kuat daripada tanda tangan pada tinjauan, karena membuktikan keputusan masih berlaku hari ini, bukan bahwa seseorang pernah menyetujuinya.

## Lensa sektor

**Startup.** Cukup kebiasaan itu dan tidak lebih: folder `decisions/` di repo utama Anda, dan catatan dua bagian (konteks dan pilihan) setiap kali Anda membuat keputusan yang akan dipertanyakan diri Anda di masa depan. Lewati siklus hidup, peran, dan penyetuju sepenuhnya, karena proses yang tidak dapat Anda pertahankan adalah proses yang akan Anda tinggalkan. Satu catatan yang menyelamatkan karyawan pertama Anda dari bertanya mengapa sistem dibangun begini sudah membayar seluruh praktik.

**Bisnis kecil.** Tanpa arsitek khusus dan waktu yang sedikit, taruh catatan di mana pun tim Anda sudah bekerja, entah wiki, dokumen bersama, atau repo, alih-alih membeli perkakas khusus. Kebiasaan jauh lebih penting daripada perkakas, jadi turunkan hambatannya: namai direktori `decisions` alih-alih `adr`, dan tangkap pilihan vendor serta beli-versus-bangun dalam satu tarikan napas dengan pilihan teknis. Ketika Anda bersandar pada kontraktor luar, catatan singkat bertanggal tentang mengapa Anda memilih vendor atau platform adalah asuransi murah terhadap terkunci pada pilihan yang tidak dapat dijelaskan siapa pun kelak.

**Enterprise.** Pekerjaannya adalah koordinasi di banyak tim: bakukan satu templat, terbitkan indeks lintas tim yang dapat dicari, dan dukung keputusan batas utama dengan fitness function agar pelanggaran menggagalkan build alih-alih menunggu tinjauan. Tugaskan pemelihara yang bertanggung jawab untuk setiap catatan dengan irama tinjauan, agar log tetap menjadi aset hidup alih-alih membusuk menjadi cerita rakyat. Jika dilakukan dengan baik, alasan satu tim pada pilihan sulit menjadi aset yang diadopsi tim berikutnya dalam satu sore alih-alih diadili ulang.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membuat catatan keputusan hampir wajib. Wajibkan catatan tak berubah yang digantikan untuk setiap persyaratan penting secara arsitektural, masing-masing menghubungkan pilihan dengan mandat atau kontrol kepatuhan yang dipenuhinya, sehingga badan pengawas menemukan alasan yang dapat dilacak, bukan rekonstruksi. Karena sistem publik berumur multitahun dan multivendor, log yang terpelihara baik sering menjadi yang memungkinkan kontraktor penerus memahami mengapa sistem berbentuk seperti itu dan melanjutkan pekerjaan tanpa mengadili ulang hal yang sudah selesai.

## Contoh

**Startup.** Sebuah startup lima orang menambahkan folder `decisions/` biasa ke repo utamanya, dengan catatan dua bagian (konteks dan pilihan) setiap kali seseorang membuat keputusan yang akan dipertanyakan diri mereka di masa depan. Tidak ada siklus hidup, tidak ada peran, dan tidak ada penyetuju: hanya kebiasaan menulis *mengapa* di samping kode. Ketika karyawan pertama mereka bergabung enam bulan kemudian, ia membaca seluruh folder dalam satu jam dan berhenti bertanya "mengapa ini dibangun begini?" Log ringan itu memakan menit per entri dan menyelamatkan mereka dari pajak penemuan ulang yang menggigit jauh sebelum tim membesar.

**Enterprise.** Sebuah pengecer dengan 30 tim rekayasa membakukan catatan berformat MADR di setiap repo, ditambah indeks pusat yang dapat dicari. Ketika tim baru menghadapi "[monorepo](https://en.wikipedia.org/wiki/Monorepo) vs. multirepo," mereka menemukan tiga catatan sebelumnya dengan konteks dan konsekuensi, dan mengadopsi alasannya dalam satu sore alih-alih sebulan debat. Keputusan batas utama (kepemilikan layanan, aturan akses data) didukung fitness function ArchUnit, sehingga pelanggaran menggagalkan build alih-alih tertangkap dalam tinjauan. Itulah tata kelola yang diskalakan tanpa hambatan pusat.

**Pemerintah.** Sebuah lembaga yang memodernisasi sistem tunjangan mewajibkan ADR untuk setiap persyaratan penting secara arsitektural, masing-masing menghubungkan keputusan dengan mandat atau kontrol kepatuhan yang dipenuhinya (aksesibilitas, residensi data, kemampuan diaudit). Catatan bersifat tak berubah dan digantikan, menghasilkan log yang dapat dilacak yang memenuhi tinjauan pengawasan. Yang krusial, ia juga memungkinkan kontraktor penerus memahami *mengapa* sistem berbentuk seperti itu, menjaga kesinambungan sepanjang umur multitahun dan multivendor yang khas pada program publik (bab 4.6, 10.4).

## Kasus bisnis: motivasi, ROI, dan TCO

Catatan keputusan memakan menit untuk ditulis dan beberapa menit lagi untuk ditinjau. Imbal hasilnya adalah biaya *keputusan ulang* yang dihindari dan biaya *pembalikan keliru* yang dihindari, keduanya besar dan berulang pada sistem berumur panjang. Setiap kali tim mengadili ulang pertanyaan yang sudah selesai, atau membalik pilihan yang sehat karena tak seorang pun ingat kendala di baliknya, mereka membayar dengan waktu insinyur senior dan sering dengan insiden. Log keputusan mengubah pajak berulang itu menjadi satu kali penulisan.

Pada **total biaya kepemilikan**, catatan keputusan termasuk dokumentasi berdaya ungkit tertinggi yang dapat Anda simpan, karena menargetkan aset yang paling sensitif terhadap pergantian orang: alasan. Orientasi lebih cepat (karyawan baru membaca *mengapa*, bukan hanya kode). Modernisasi lebih aman (bab 3.6: Anda dapat membedakan keputusan esensial dari yang insidental). Audit lebih murah (buktinya sudah ada). Biaya *tidak* menyimpannya tak terlihat di dasbor mana pun, dan berlipat diam-diam dengan setiap kepergian. Untuk meyakinkan pimpinan, tunjuk penemuan ulang mahal baru-baru ini, atau keputusan yang dibalik yang menyebabkan insiden, dan catat bahwa perbaikannya hampir tidak memakan biaya untuk dilembagakan.

## Anti-pola dan jebakan

- **Mencatat *apa* tanpa *mengapa*:** menghilangkan konteks dan alternatif yang ditolak, yang merupakan intinya.
- **Administrasi setelah kejadian:** catatan yang ditulis untuk memenuhi mandat, bukan untuk berpikir; terbaca kosong dan tak ada yang memercayainya.
- **Dokumen raksasa multikeputusan:** satu halaman besar yang tidak dapat dinavigasi atau digantikan dengan bersih.
- **Klaim tak bertanggal:** biaya dan kendala yang pernah benar, disajikan sebagai abadi.
- **Suntingan diam-diam:** mengubah sejarah keputusan tanpa catatan bertanggal, menghancurkan jejak audit.
- **Log hanya-tulis:** catatan yang dibuat dan tidak pernah dimunculkan pada saat relevan, sehingga tidak memengaruhi perilaku.
- **Penjagaan gerbang singkatan:** bersikeras pada "ADR" dan "arsitektur" sehingga mengecilkan hati kontribusi.
- **Tanpa siklus hidup:** catatan yang tidak pernah ditinjau, digantikan, atau diakhiri, membusuk menjadi misinformasi.

## Model kematangan

- **Tingkat 1 (Memulai):** Keputusan hidup di kepala orang, utas obrolan, dan pesan commit; penangkapan bersifat reaktif dan ad hoc, dan alasan rutin hilang bersama pergantian staf.
- **Tingkat 2 (Mengembangkan):** Beberapa tim menyimpan catatan, dalam beragam format dan templat, setiap kali individu ingat; praktiknya tidak konsisten antartim, tanpa log, penamaan, atau proses bersama.
- **Tingkat 3 (Membakukan):** Templat tunggal, penyimpanan dalam repo, serta siklus hidup dan tata kelola terdefinisi (kriteria ajukan/lewati, peran, irama tinjauan) didokumentasikan dan diterapkan secara konsisten di seluruh organisasi; catatan ditinjau dan digantikan alih-alih disunting diam-diam.
- **Tingkat 4 (Mengelola):** Log keputusan diukur terhadap garis dasar: cakupan (persentase keputusan penting secara arsitektural yang memiliki catatan), kesegaran (persentase catatan yang ditinjau dalam irama, ditambah jumlah klaim tak bertanggal atau usang), dan kemudahan ditemukan (seberapa sering catatan relevan benar-benar sampai ke pengembang yang mengubah kode yang diatur). Pemelihara yang bertanggung jawab bertindak berdasarkan metrik ini, menggantikan catatan usang dan menutup celah cakupan berdasarkan bukti, bukan anekdot.
- **Tingkat 5 (Mengorkestrasi):** Log keputusan lintas tim yang dapat dicari terintegrasi ke dalam pekerjaan harian: catatan relevan muncul otomatis pada perubahan yang diaturnya, keputusan utama dijamin oleh fitness function dalam integrasi berkelanjutan, dan log memberi makan orientasi, modernisasi, dan audit sebagai aset hidup. Organisasi terus memperbaiki praktik itu sendiri, mengakhiri, menggantikan, dan mengubah cakupan catatan seiring bergesernya sistem dan kendalanya, dan menyeimbangkan kembali di mana ia berinvestasi pada ketelitian seiring tumbuhnya portofolio keputusan.

## Gagasan untuk didiskusikan

1. Apa keputusan terakhir yang dibalik atau diadili ulang tim Anda karena tak seorang pun ingat alasan aslinya?
2. Apakah mengganti nama direktori `adr/` menjadi `decisions/` akan mengubah siapa yang berkontribusi dan apa yang dicatat?
3. Keputusan kritis Anda yang mana yang dapat dijamin oleh fitness function otomatis hari ini?
4. Tak berubah-dan-menggantikan atau dokumen hidup: mana yang cocok dengan kewajiban audit dan budaya Anda, dan mengapa?
5. Bagaimana seorang karyawan baru (atau kontraktor penerus) saat ini menemukan *mengapa* sistem Anda berbentuk seperti itu?
6. Apa yang membenarkan pengajuan catatan keputusan di tim Anda, dan apa yang membenarkan *tidak* mengajukannya?

## Poin-poin utama

- Catatan keputusan menangkap satu keputusan penting beserta **konteks dan konsekuensinya**: *mengapa*, bukan hanya *apa*.
- Jaga catatan **spesifik, bercap waktu, dan ringan**; bakukan satu templat (Nygard, MADR, atau serupa).
- Simpan **di kontrol versi di samping kode**; pertimbangkan menamainya "decisions" untuk memperluas kontribusi.
- Tetapkan **siklus hidup dan tata kelola** (kriteria ajukan/lewati, peran, irama tinjauan); sisakan proses berat untuk keputusan pintu satu arah.
- Buat keputusan **mudah ditemukan** pada saat perubahan dan, bila mungkin, **dapat diuji** lewat fitness function.
- ROI-nya adalah biaya penemuan ulang dan pembalikan keliru yang dihindari; kasus TCO paling kuat di tempat pergantian orang, modernisasi, dan audit paling penting. Lihat bab 1.5 (pengambilan keputusan dan tata kelola) dan bab 3.1 (dasar-dasar arsitektur).

## Referensi dan bacaan lanjutan

- Michael Nygard, "Documenting Architecture Decisions" (2011): ADR ringan yang mendasar.
- MADR: proyek Markdown Any Decision Records (adr.github.io/madr).
- Jeff Tyree dan Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" dan "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templat, contoh, dan panduan kerja tim (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness function).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" dan "Architecturally significant requirements."
