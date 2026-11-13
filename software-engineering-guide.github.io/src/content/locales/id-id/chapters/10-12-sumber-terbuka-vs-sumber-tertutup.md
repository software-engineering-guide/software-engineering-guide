# 10.12 Sumber terbuka vs sumber tertutup

## Tinjauan dan motivasi

Hampir setiap sistem modern adalah campuran perangkat lunak yang Anda tulis, perangkat lunak yang Anda beli, dan perangkat lunak yang Anda ambil gratis. Dua dari tiga itu datang dengan pilihan mendasar: apakah perangkat lunaknya **sumber terbuka** atau **sumber tertutup**? **[Perangkat lunak sumber terbuka](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** didistribusikan di bawah lisensi yang memberi semua orang hak untuk memakai, mempelajari, memodifikasi, dan mendistribusikan ulang kode sumber, instruksi yang dapat dibaca manusia yang mendefinisikan program. **Perangkat lunak sumber tertutup**, juga disebut **[perangkat lunak proprietari](https://en.wikipedia.org/wiki/Proprietary_software)**, didistribusikan sebagai produk jadi yang kode sumbernya dirahasiakan vendor. Anda mendapat hak menjalankannya di bawah lisensi, tetapi bukan memeriksa atau mengubah cara kerjanya. Kategori tengah, **[perangkat lunak source-available](https://en.wikipedia.org/wiki/Source-available_software)**, menerbitkan sumber untuk dibaca tetapi membatasi penggunaan, modifikasi, atau distribusi ulang. Ia *terlihat* tetapi tidak *terbuka* menurut definisi baku.

Dua klarifikasi penting sebelum membandingkan keduanya. Pertama, "gratis" itu ambigu. Komunitas membedakan **gratis-sebagai-kebebasan** (kebebasan memodifikasi dan berbagi, kadang ditulis "libre") dari **gratis-sebagai-harga** (tanpa biaya, "gratis"). Sumber terbuka tentang kebebasan, belum tentu harga. Kedua, lisensi sumber terbuka terbagi dua keluarga. **[Lisensi permisif](https://en.wikipedia.org/wiki/Permissive_software_license)** (seperti [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD, dan Apache 2.0) membiarkan Anda melakukan hampir apa saja, termasuk menanamkan kode ke produk tertutup. Lisensi **[copyleft](https://en.wikipedia.org/wiki/Copyleft)** (seperti [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) mewajibkan karya turunan yang Anda distribusikan juga dirilis di bawah ketentuan terbuka yang sama, aturan timbal balik yang kadang disebut "viral" oleh pengkritik dan "share-alike" oleh pendukung.

Bab ini melihat pilihan dari dua sisi. Sebagai **konsumen**, Anda memutuskan apakah mengadopsi komponen sumber terbuka atau proprietari. Sebagai **produsen**, Anda memutuskan apakah membuka sumber perangkat lunak yang Anda bangun. Untuk enterprise besar dan terutama pemerintah, kedua keputusan membawa bobot jauh melampaui berkas lisensi. Keduanya menyentuh pengadaan (bab 10.3), kedaulatan digital (bab 10.11), keamanan rantai pasok (bab 4.2), interoperabilitas (bab 3.8), dan kalkulus bangun-atau-beli (bab 6.1).

## Prinsip utama

- **Lisensi, bukan harga, yang mendefinisikan "terbuka."** Baca lisensinya; bebas-biaya dan sumber-terbuka adalah klaim berbeda.
- **Tak ada model yang secara inheren lebih aman.** Keduanya bisa luar biasa atau lalai; praktik di sekitar kode lebih penting daripada keterbukaannya.
- **Keterbukaan adalah tuas pengurangan ketergantungan.** Akses ke sumber adalah perlindungan akhir terhadap [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **Anda selalu memikul beban operasional.** Gratis-diperoleh tak pernah gratis-dijalankan; [total biaya kepemilikan](https://en.wikipedia.org/wiki/Total_cost_of_ownership) menceritakan kisah sebenarnya.
- **Pembeda tetap tertutup; komoditas boleh dibuka.** Buka sumber apa yang tidak membedakan Anda; jaga yang membedakan.
- **Copyleft punya konsekuensi.** Pahami kewajiban timbal balik sebelum menanamkan kode copyleft ke produk yang Anda distribusikan.
- **Komunitas hidup adalah aset; repositori terbengkalai adalah liabilitas.** Nilai proyeknya, bukan hanya lisensinya.

## Rekomendasi

### Evaluasi komponen berdasarkan proyek, bukan hanya lisensi

Sebelum mengadopsi dependensi apa pun, sumber terbuka atau proprietari, nilai kesehatannya: irama rilis, jumlah dan keragaman pemelihara, ketanggapan terhadap laporan keamanan, dan keluasan adopsi. Pustaka sumber terbuka satu pemelihara dan vendor proprietari kecil membawa **risiko bus factor** yang sama (bahaya proyek runtuh jika satu atau beberapa orang kunci pergi). Pilih komponen dengan basis kontributor luas atau vendor yang sehat finansial, dan catat penilaian sebagai bagian uji tuntas (bab 10.2, 4.2).

### Baca dan lacak lisensi sebagai kewajiban kelas satu

Pelihara inventaris setiap komponen dan lisensinya, dan tegakkan kebijakan keluarga lisensi mana yang dapat diterima untuk penggunaan mana. Pembedaan kritisnya adalah copyleft. Kode **permisif** (MIT, Apache 2.0) umumnya dapat ditanamkan ke produk tertutup dengan bebas. **Copyleft kuat** (GPL) dapat mewajibkan Anda merilis turunan terdistribusi Anda sendiri dengan ketentuan yang sama. Pakai **software composition analysis (SCA)** otomatis, perkakas yang memindai dependensi Anda untuk mengidentifikasi komponen, lisensi, dan kerentanan yang diketahui, dan menghasilkan **software bill of materials (SBOM)**, daftar formal setiap komponen dalam produk (bab 10.3, 4.2).

### Nilai keamanan dari praktik, bukan dari keterbukaan

Jangan berasumsi sumber terbuka aman karena **argumen "banyak mata"** ([Hukum Linus](https://en.wikipedia.org/wiki/Linus%27s_law): "dengan cukup banyak mata, semua bug menjadi dangkal"). Dan jangan berasumsi kode proprietari aman lewat **[security-through-obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity)** (keyakinan keliru bahwa menyembunyikan sumber menyembunyikan cacat). Banyak mata hanya membantu jika orang yang berkualifikasi benar-benar melihat, dan banyak proyek yang dipakai luas dipelihara tipis. Kedua model membawa **risiko rantai pasok**: sumber terbuka lewat dependensi yang dibobol atau terbengkalai, proprietari lewat kode buram dan kanal pembaruan yang tak dapat Anda periksa. Sematkan versi, verifikasi asal-usul, pindai terus-menerus, dan pantau advisori apa pun modelnya (bab 4.2).

### Rancang untuk jalan keluar dan interoperabilitas

Pilih komponen yang berbicara standar terbuka dan format data portabel, agar dapat Anda ganti kelak (bab 3.8, 10.11). Dengan sumber terbuka Anda mendapat jalan keluar tertinggi: jika proyek macet, Anda dapat men-**[fork](https://en.wikipedia.org/wiki/Fork_(software_development))**-nya (membuat dan memelihara salinan sendiri). Dengan perangkat lunak proprietari, negosiasikan perlindungan di muka: ekspor data dalam format terbuka, API terdokumentasi, dan **[escrow kode sumber](https://en.wikipedia.org/wiki/Source_code_escrow)** (pengaturan hukum di mana vendor menitipkan sumber pada pihak ketiga, dilepas kepada Anda jika vendor gagal). Rancang agar tak ada satu komponen pun, jenis apa pun, yang dapat menyandera sistem Anda.

### Timbang total biaya kepemilikan, bukan harga label

Bandingkan opsi pada **total biaya kepemilikan (TCO)**, biaya seumur hidup penuh termasuk akuisisi, integrasi, operasi, dukungan, pelatihan, peningkatan, dan penggantian akhir, alih-alih biaya lisensi saja. Sumber terbuka sering menukar biaya lisensi dengan biaya operasional dan staf lebih tinggi. Perangkat lunak proprietari sering menukar biaya langganan yang dapat diprediksi dengan lock-in dan kendali lebih sedikit. Sertakan biaya modelnya sendiri: sumber terbuka yang didukung sendiri butuh keterampilan internal, sementara perangkat lunak proprietari butuh kapasitas manajemen vendor.

### Sebagai produsen, buka sumber apa yang tidak membedakan Anda

Klasifikasikan perangkat lunak Anda sendiri menjadi yang memberi keunggulan kompetitif atau misi dan yang perpipaan tak membedakan. Jaga pembeda tetap proprietari. Pertimbangkan membuka sumber infrastruktur komoditas, di mana komunitas dapat berbagi pemeliharaan dan perbaikan. Untuk pemerintah, timbang **"public money, public code"** (prinsip bahwa perangkat lunak yang didanai pembayar pajak harus tersedia untuk publik secara bawaan) sebagai pendorong transparansi, penggunaan ulang, dan kedaulatan (bab 10.5, 10.11). Pilih lisensi dengan sengaja: permisif untuk memaksimalkan adopsi, copyleft untuk menjaga ekosistem tetap terbuka.

## Trade-off: kelebihan dan kekurangan

| Dimensi | Sumber terbuka | Tertutup / proprietari |
|---|---|---|
| **Biaya akuisisi** | Biasanya nol untuk diperoleh | Biaya lisensi atau langganan |
| **Total biaya kepemilikan** | Biaya bergeser ke operasi dan staf | Lebih dapat diprediksi, tetapi premi lock-in |
| **Kendali & kustomisasi** | Penuh: Anda dapat membaca dan mengubah sumber | Terbatas pada apa yang diekspos vendor |
| **Dukungan & akuntabilitas** | Komunitas, atau pihak ketiga berbayar; tak ada satu pihak yang bisa dimintai tanggung jawab | Dukungan kontraktual dan pihak akuntabel yang jelas |
| **Postur keamanan** | Dapat diaudit; "banyak mata" jika benar-benar dipelihara | Dikelola vendor; buram; kekaburan bukan perlindungan |
| **Umur panjang / pengabaian** | Dapat di-fork jika dipelihara; masih bisa layu | Bergantung pada kelangsungan vendor dan peta jalan |
| **Vendor lock-in** | Rendah: sumber dan format terbuka memungkinkan keluar | Tinggi kecuali dimitigasi standar dan escrow |
| **Ekosistem** | Komunitas terbuka dan interoperabilitas | Terkurasi, terintegrasi, kadang bertembok |

Ketegangan berulangnya **kendali versus kenyamanan dan akuntabilitas**. Sumber terbuka memaksimalkan kendali, auditabilitas, dan kebebasan dari lock-in, tetapi meminta Anda menyediakan kapabilitas, integrasi, dan dukungan sendiri. Perangkat lunak proprietari memberikan produk yang didukung, terintegrasi, dan akuntabel dengan kontrak untuk ditegakkan, tetapi melepas kendali dan mengundang lock-in. Resolusinya jarang semua-atau-tidak-sama-sekali. Kebanyakan properti matang mencampur fondasi sumber terbuka dengan sistem proprietari di mana dukungan, akuntabilitas, atau kapabilitas khusus membenarkan trade-off.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah kita menegakkan kebijakan lisensi dengan SCA dan SBOM otomatis di pipeline, terutama untuk menangkap copyleft kuat sebelum dikirim?** Menanamkan pustaka GPL ke produk proprietari yang didistribusikan dapat mewajibkan Anda merilis sumber sendiri, dan kejutan itu biasanya muncul terlambat, saat mahal untuk dibatalkan. Pelihara inventaris setiap komponen dan lisensinya, tegakkan keluarga lisensi mana yang dapat diterima untuk penggunaan mana, dan jalankan software composition analysis secara otomatis agar pipeline memblokir pelanggaran alih-alih pengacara menangkapnya saat pengiriman. Hasilkan SBOM sebagai hal biasa. Untuk properti besar atau pemerintah, ini juga kebersihan rantai pasok dan sering persyaratan pengadaan. Bawa inventaris lisensi Anda saat ini, atau fakta bahwa Anda tidak punya, dan putuskan siapa yang memiliki kebijakannya.

2. **Ketika kita mengadopsi dependensi, apakah kita menilai kesehatan proyek dan bus factor sebagai uji tuntas?** Pustaka sumber terbuka satu pemelihara dan vendor proprietari kecil membawa risiko yang sama: proyek runtuh jika satu atau beberapa orang kunci pergi. Sebelum mengadopsi apa pun, nilai irama rilis, jumlah dan keragaman pemelihara, ketanggapan terhadap laporan keamanan, dan keluasan adopsi, dan catat penilaian. Tak ada model yang lebih aman secara bawaan; "banyak mata" hanya membantu jika orang berkualifikasi benar-benar melihat, dan banyak proyek yang dipakai luas dipelihara tipis. Bawa tiga atau empat dependensi yang paling diandalkan produk Anda dan tanyakan, untuk masing-masing, berapa orang yang harus pergi sebelum menjadi masalah Anda. Jika tak dapat menjawab, itulah penilaian yang Anda utang pada diri sendiri.

3. **Ketika kita membeli proprietari, apakah kita mengamankan perlindungan keluar di muka?** Perangkat lunak proprietari menawarkan akuntabilitas dan kenyamanan sebagai ganti kendali, dan biaya tersembunyinya lock-in: biaya peralihan yang memungkinkan vendor menaikkan harga atau menurunkan layanan dengan sedikit jalur ganti rugi. Negosiasikan perlindungan sebelum menandatangani, saat Anda masih punya daya ungkit: ekspor data dalam format terbuka, API terdokumentasi, dan escrow kode sumber yang melepas sumber jika vendor gagal. Dengan sumber terbuka jalan keluar Anda adalah kemampuan fork; dengan proprietari Anda harus menulis jalan keluar ke dalam kontrak. Bawa sistem proprietari paling kritis Anda dan tanyakan apa yang sebenarnya terjadi jika vendor menggandakan harga atau bangkrut. Jika jawabannya "kita terjebak," perbaiki kontrak saat perpanjangan.

4. **Untuk perangkat lunak yang kita bangun sendiri, bagaimana kita memutuskan apa yang dibuka sumbernya dan apa yang tetap tertutup, dan siapa yang memegang wewenang membuat keputusan itu?** Salah di satu arah dan Anda menyerahkan kode yang membedakan Anda; salah di arah lain dan Anda menimbun perpipaan komoditas yang pemeliharaannya akan dengan senang hati dibagi komunitas. Tekanan yang bersaing nyata: insinyur menginginkan sisi positif rekrutmen dan reputasi dari repositori publik, sementara produk dan hukum khawatir menyerahkan keunggulan kepada pesaing atau mengekspos heuristik sensitif keamanan. Bawa klasifikasi jujur sistem Anda menjadi pembeda misi versus infrastruktur tak membedakan, dan namai orang atau dewan yang menyetujui rilis, karena keputusan ad hoc yang dibuat siapa pun yang mendorong repositori adalah cara permata mahkota bocor. Untuk enterprise besar pertanyaannya strategi portofolio, dan untuk pemerintah ia berbenturan dengan "public money, public code," prinsip bahwa perangkat lunak yang didanai pembayar pajak harus publik secara bawaan, jadi putuskan di muka pengecualian mana (keamanan nasional, deteksi penipuan, data pribadi) yang membenarkan menjaga kode tetap tertutup.

5. **Apakah perbandingan bangun-atau-beli kita menangkap total biaya kepemilikan penuh, atau kita masih memperlakukan biaya lisensi nol sebagai biaya nol?** Kesalahan finansial paling umum dengan sumber terbuka adalah membaca "gratis diperoleh" sebagai "gratis dijalankan," lalu menemukan bahwa integrasi, operasi, respons keamanan, dan dukungan berbayar melampaui lisensi mana pun yang Anda hindari. Ketegangannya adalah langganan proprietari tampak mahal di faktur sambil menyembunyikan premi lock-in, dan komponen terbuka tampak gratis di faktur sambil menggeser biaya ke staf Anda sendiri. Bawa model TCO sepadan untuk dua atau tiga keputusan nyata: akuisisi, integrasi, operasi, dukungan, pelatihan, peningkatan, respons keamanan, dan penggantian akhir, dihargai selama umur penuh alih-alih tahun pertama. Di properti enterprise atau pemerintah, tambahkan biaya model operasi itu sendiri, karena sumber terbuka yang didukung sendiri menuntut keterampilan internal yang harus Anda rekrut dan pertahankan, dan perlakukan perbandingan yang menghilangkan baris-baris itu sebagai bukti, bukan analisis.

6. **Apakah kita menilai keamanan komponen dari praktiknya, atau bersandar pada label keterbukaan, baik "banyak mata" maupun kerahasiaan kode tertutup?** Kedua bawaan adalah jebakan: "banyak mata" hanya melindungi Anda ketika orang berkualifikasi benar-benar meninjau kode, dan banyak proyek terbuka yang dipakai luas berjalan pada satu pemelihara yang kelelahan, sementara sumber tertutup yang bergantung pada penyerang tidak melihatnya adalah security through obscurity, bukan kendali. Perdebatan ini penting karena mengubah di mana Anda membelanjakan upaya keamanan yang langka, dan jawaban jujurnya kedua model membawa risiko rantai pasok, sumber terbuka lewat dependensi yang dibobol atau terbengkalai dan proprietari lewat kanal pembaruan buram yang tak dapat Anda periksa. Bawa bukti untuk komponen paling kritis Anda: siapa yang sebenarnya meninjaunya, seberapa cepat advisori ditambal, apakah versi disematkan dan asal-usul diverifikasi, dan apakah Anda menghasilkan SBOM. Untuk properti besar atau pemerintah, kaitkan ini dengan kewajiban pengadaan dan pemindaian berkelanjutan, karena regulator akan bertanya apa yang Anda periksa, bukan apakah sumbernya publik.

## Lensa sektor

**Startup.** Dengan runway tipis Anda membangun di atas fondasi sumber terbuka karena tak sanggup membayar biaya lisensi dan Anda ingin kebebasan melakukan fork jika proyek macet. Jalankan pemindaian composition-analysis sebelum mengirim agar pustaka copyleft kuat tidak diam-diam mewajibkan Anda menerbitkan sumber sendiri, dan jaga satu pembeda nyata Anda tetap tertutup ketat. Buka sumber perkakas kecil non-kritis jika membantu rekrutmen, tetapi jangan mengisi staf beban pemeliharaan yang tak dapat Anda pikul.

**Bisnis kecil.** Tanpa spesialis hukum atau platform internal, perlakukan lisensi sebagai risiko yang tidak boleh Anda salah baca alih-alih topik yang dapat Anda kuasai. Pilih perkakas proprietari yang didukung atau distribusi sumber terbuka komersial di mana vendor memiliki tambalan dan akuntabilitas, karena mendukung sendiri tumpukan yang tak dapat Anda operasikan adalah penghematan semu. Ketika Anda memang mengadopsi komponen gratis, periksa bahwa lisensinya mengizinkan penggunaan Anda dan bahwa proyek benar-benar dipelihara, tidak terbengkalai.

**Enterprise.** Pada skala besar masalahnya konsistensi lintas banyak tim: kebijakan lisensi tertulis, software composition analysis dan pembuatan SBOM otomatis di setiap pipeline, dan keputusan bangun-atau-beli berbasis TCO alih-alih kebiasaan per tim. Kelola perangkat lunak terbuka dan proprietari sebagai satu portofolio, bakukan perlindungan keluar seperti format terbuka dan escrow kode sumber dalam pengadaan, dan lacak kesehatan dependensi kritis agar satu proyek terbengkalai tidak menjadi insiden. Atur sisi produsen juga, dengan aturan jelas tentang apa yang dibuka sumbernya oleh organisasi versus dijaga tertutup.

**Pemerintah.** Aturan pengadaan, kewajiban transparansi, dan akuntabilitas publik membentuk setiap pilihan. Timbang "public money, public code," prinsip bahwa perangkat lunak yang didanai pembayar pajak harus publik secara bawaan, untuk memajukan penggunaan ulang lintas lembaga dan kedaulatan digital, sambil menyisihkan pengecualian sempit untuk kode sensitif keamanan atau data pribadi. Wajibkan pemasok proprietari mana pun menyediakan ekspor data dalam format terbuka dan escrow kode sumber agar kegagalan vendor tidak mendamparkan layanan publik, dan terbitkan sumber non-sensitif agar warga dapat mengaudit aturan yang mengatur mereka.

## Contoh

**Startup.** Startup tiga pendiri membangun seluruh produknya di atas fondasi sumber terbuka (Linux, basis data sumber terbuka, kerangka web) karena tak sanggup membayar lisensi dan ingin kebebasan melakukan fork jika proyek macet. Sebelum mengirim, satu pendiri menjalankan pemindaian composition-analysis dan menangkap pustaka copyleft kuat yang akan memaksa mereka menerbitkan algoritma pencocokan proprietari mereka, sehingga mereka menggantinya dengan padanan berlisensi permisif. Mereka menjaga algoritma itu, satu-satunya pembeda mereka, tertutup ketat, dan hanya membuka sumber perkakas logging internal kecil untuk membangun niat baik dan menarik insinyur.

**Enterprise.** Sebuah perusahaan asuransi besar menjalankan platform intinya di atas fondasi sumber terbuka: Linux, basis data sumber terbuka yang dipakai luas, dan orkestrator kontainer. Tetapi ia membeli suite pemodelan aktuaria proprietari, karena keahlian domain vendor, sertifikasi regulasi, dan kontrak dukungannya sepadan dengan biayanya dan tak ada alternatif terbuka sebanding. Ia membayar langganan untuk **sumber terbuka komersial** (distribusi komponen terbuka yang didukung vendor) untuk mendapat akuntabilitas dan tambalan pada perpipaan, sambil menjaga algoritma penetapan harga yang membedakannya tetap proprietari dan internal. Analisis TCO (bab 10.10) menggerakkan setiap pilihan alih-alih ideologi.

**Pemerintah.** Sebuah badan pajak nasional, di bawah kebijakan "public money, public code," membangun layanan kelayakan tunjangan baru di atas komponen sumber terbuka dan standar terbuka (bab 3.8), agar lembaga lain dapat memakainya ulang dan warga dapat mengaudit aturannya. Ia menerbitkan kode non-sensitif di repositori publik, hanya mempertahankan heuristik deteksi penipuan tertutup demi alasan keamanan. Ini mengurangi vendor lock-in dan memajukan kedaulatan digital (bab 10.11). Aturan pengadaan (bab 10.3) mewajibkan setiap komponen proprietari menyediakan ekspor data dalam format terbuka dan escrow kode sumber, untuk menjamin kesinambungan jika pemasok gagal.

## Kasus bisnis: motivasi, ROI, dan TCO

Daya tarik finansial sumber terbuka, ketiadaan biaya lisensi, adalah bagian paling tidak andal dari kasusnya, karena akuisisi hanya pecahan kecil TCO. Imbal hasil tahan lama bersifat strategis: kebebasan dari lock-in (kemampuan mengganti atau melepas pemasok tanpa arsitektur ulang), auditabilitas untuk keamanan dan kepatuhan, adopsi lebih cepat karena insinyur dapat mencoba sebelum berkomitmen, dan pemeliharaan bersama kode komoditas lintas seluruh industri. Biaya penyeimbangnya nyata. Anda harus menyediakan integrasi, operasi, respons keamanan, dan sering dukungan berbayar, dan proyek tak terpelihara yang dipilih buruk dapat lebih mahal dalam insiden daripada lisensi mana pun.

Kasus bisnis perangkat lunak proprietari adalah akuntabilitas dan kenyamanan: satu vendor bertanggung jawab atas produk, kontrak dukungan yang dapat Anda tegakkan, fitur terintegrasi, dan penganggaran yang dapat diprediksi. Biaya tersembunyinya lock-in, biaya peralihan yang memungkinkan vendor menaikkan harga atau menurunkan layanan dengan sedikit jalur ganti rugi, plus ketergantungan pada solvabilitas dan peta jalan vendor. **Model bisnis** umum mengaburkan garis: **[open core](https://en.wikipedia.org/wiki/Open-core_model)** (basis terbuka dengan add-on proprietari berbayar), **lisensi ganda** (kode yang sama ditawarkan di bawah lisensi copyleft dan lisensi komersial berbayar), **[software as a service](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (perangkat lunak berjalan sebagai layanan terhosting yang Anda sewa, di mana sumber mungkin tidak relevan karena Anda tak pernah memiliki binernya), dan model **dukungan/langganan** yang menjual layanan di sekitar kode yang gratis.

Bagi produsen, ROI **membuka sumber perangkat lunak non-pembeda Anda sendiri** bisa substansial. Kontributor luar mengurangi beban pemeliharaan Anda. Proyek menjadi aset rekrutmen dan reputasi. Adopsi eksternal menjadikan standar Anda yang de facto. Untuk pemerintah, ia memberikan transparansi dan penggunaan ulang lintas sektor publik. Aturan strategisnya sederhana: buka sumber komoditas untuk berbagi biayanya dan menumbuhkan ekosistem, dan jaga pembeda tetap tertutup untuk melindungi keunggulan yang mendanai segalanya.

## Anti-pola dan jebakan

- **"Gratis berarti gratis":** memperlakukan biaya akuisisi nol sebagai TCO nol, lalu kurang mendanai operasi dan dukungan.
- **Buta lisensi:** menanamkan kode copyleft kuat ke produk proprietari terdistribusi dan memicu kewajiban yang tak pernah direncanakan.
- **Percaya "banyak mata":** mengasumsikan proyek terbuka diaudit padahal ia punya satu pemelihara kelebihan beban dan tanpa tinjauan keamanan.
- **Security-through-obscurity:** meyakini sumber tertutup aman hanya karena penyerang tak dapat membacanya.
- **Absolutisme ideologis:** mewajibkan "semua terbuka" atau "semua proprietari" alih-alih memilih per komponen berdasarkan merit dan TCO.
- **Mengabaikan asal-usul:** menarik dependensi tanpa SBOM, penyematan versi, atau verifikasi rantai pasok (bab 4.2).
- **Membuka sumber permata mahkota:** merilis kode yang justru membedakan Anda, menyerahkan keunggulan Anda.
- **Fork-lalu-lupa:** mem-fork proyek terbengkalai tanpa kapasitas untuk benar-benar memelihara fork itu.

## Model kematangan

**Tingkat 1 (Memulai).** Komponen sumber terbuka dan proprietari masuk ke properti secara ad hoc. Lisensi tak dibaca, tak ada inventaris atau SBOM, dan pilihan antar model dibuat berdasarkan kebiasaan atau harga semata. Risiko pengabaian dan lisensi muncul hanya ketika ada yang rusak, dan tiap tim bereaksi sendiri.

**Tingkat 2 (Mengembangkan).** Beberapa tim memulai praktik dasar: inventaris komponen dan lisensi, pandangan kasar tentang lisensi yang dapat diterima, dan software composition analysis sesekali. Keputusan bangun-atau-beli dan terbuka-atau-tertutup dituliskan, tetapi disiplinnya tambal-sulam dan tidak konsisten dari tim ke tim, sehingga kejutan copyleft atau bus factor masih dapat lolos di mana kebiasaan belum mengakar.

**Tingkat 3 (Membakukan).** Kerangka terdokumentasi mengatur baik konsumsi maupun produksi di seluruh organisasi. Komponen dipilih berdasarkan TCO dan kesehatan proyek, lisensi ditegakkan otomatis di pipeline sehingga pelanggaran memblokir build, SBOM dihasilkan sebagai hal biasa, dan kebijakan eksplisit menyatakan apa yang dibuka sumbernya oleh organisasi versus dijaga tertutup. Perlindungan keluar seperti format terbuka dan escrow kode sumber standar dalam pengadaan, dan setiap tim mengikuti aturan yang sama alih-alih aturannya sendiri.

**Tingkat 4 (Mengelola).** Program diukur dan dikendalikan terhadap garis dasar. Organisasi melacak metrik seperti cakupan SBOM di seluruh produk, pangsa dependensi yang melanggar kebijakan, waktu rata-rata menambal kerentanan dependensi yang diungkap, skor bus-factor dan kesehatan untuk proyek kritis, dan TCO terealisasi terhadap estimasi yang membenarkan tiap pilihan. Ambang memicu tindakan: komponen yang pemeliharaannya macet atau latensi tambalannya melayang melewati target ditandai untuk diganti atas bukti, dan keputusan terbuka-atau-tertutup serta bangun-atau-beli ditinjau terhadap angka alih-alih dibela oleh kebiasaan.

**Tingkat 5 (Mengorkestrasi).** Strategi sumber terbuka adalah kapabilitas bisnis yang disengaja, terintegrasi di seluruh organisasi dan terus diperbaiki. Organisasi berkontribusi dan kadang menjadi pengurus proyek yang diandalkannya, membuka sumber perangkat lunak non-pembedanya sebagai hal biasa, dan memberi makan data kesehatan dependensi dan TCO kembali ke pengadaan, keamanan, dan perencanaan produk. Ia rutin menyeimbangkan ulang portofolio perangkat lunak terbuka dan proprietari, beradaptasi dengan pergeseran biaya, risiko, kedaulatan, dan keunggulan strategis sebelum memaksa krisis.

## Gagasan untuk didiskusikan

- Di mana dalam properti Anda kehilangan satu vendor atau pemelihara akan eksistensial, dan apa rencana keluar Anda?
- Sistem Anda sendiri yang mana yang komoditas yang dapat Anda buka sumbernya, dan mana pembeda sejati untuk dilindungi?
- Apakah organisasi Anda memperlakukan "banyak mata" sebagai kendali keamanan nyata atau asumsi yang tak diperiksa?
- Untuk pembaca sektor publik: apa yang akan diubah bawaan "public money, public code" pada pengadaan berikutnya?
- Seberapa baik perbandingan TCO Anda menangkap biaya operasional dan dukungan yang digeser sumber terbuka kepada Anda?

## Poin-poin utama

- **Terbuka vs. tertutup didefinisikan oleh lisensi**, bukan harga; ketahui bedanya gratis-sebagai-kebebasan dan gratis-sebagai-harga, dan antara permisif dan copyleft.
- **Tak ada model yang secara inheren lebih aman atau lebih murah.** Nilai praktik proyek dan TCO penuhnya, bukan label keterbukaan.
- **Keterbukaan adalah penawar lock-in terkuat**, memberikan auditabilitas, portabilitas, dan kemampuan fork; perangkat lunak proprietari menawarkan akuntabilitas dan kenyamanan sebagai ganti kendali.
- **Putuskan per komponen berdasarkan merit**, dan campur model dengan sengaja alih-alih berdasarkan ideologi.
- **Sebagai produsen, buka sumber komoditas dan jaga pembeda tetap tertutup**, dan di pemerintah, timbang "public money, public code" untuk transparansi, penggunaan ulang, dan kedaulatan.

## Referensi dan bacaan lanjutan

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft dan lainnya, berbagai judul O'Reilly tentang strategi dan operasi sumber terbuka
- Free Software Foundation, *The Free Software Definition* (dan teks GNU General Public License)
- Open Source Initiative, *The Open Source Definition* dan daftar lisensi yang disetujui
- Free Software Foundation Europe, materi kampanye *Public Money, Public Code*
- Yochai Benkler, *The Wealth of Networks*
