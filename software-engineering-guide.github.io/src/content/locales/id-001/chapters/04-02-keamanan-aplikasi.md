# 4.2 Keamanan aplikasi

## Tinjauan dan motivasi

Keamanan aplikasi adalah tempat ancaman abstrak bertemu kode konkret. Sebagian besar pembobolan yang menjadi berita utama berakar pada cacat lapisan aplikasi: injeksi, alur autentikasi yang rusak, rahasia yang terekspos, atau dependensi yang terkompromi. Bagi tim besar yang merilis banyak layanan, bagian sulitnya bukan mengetahui bahwa cacat ini ada. Melainkan mencegahnya secara konsisten di basis kode yang menyebar yang ditulis ribuan tangan selama bertahun-tahun.

Bagi enterprise, keamanan aplikasi adalah soal kepercayaan pelanggan dan kewajiban regulasi. Cacat dalam alur login atau jalur pembayaran dapat memicu penipuan, denda, dan pengungkapan pembobolan wajib. Sistem pemerintah menghadapi risiko teknis yang sama dengan data berisiko lebih tinggi: kelayakan tunjangan, catatan pajak, data peradilan pidana, dan infrastruktur nasional. Dalam kedua pengaturan, aplikasi adalah pintu depan, dan penyerang mengujinya terus-menerus dan secara otomatis.

Bab ini membahas praktik yang menjaga aplikasi tangguh: mengetahui dan bertahan terhadap kelas kerentanan umum, memvalidasi masukan dan meng-encode keluaran, mendapatkan autentikasi dan otorisasi dengan benar, mengelola rahasia, dan mengamankan rantai pasok perangkat lunak yang makin menentukan permukaan serangan nyata Anda.

*Lihat juga:* bab 4.1 (fondasi keamanan, pemodelan ancaman, dan siklus hidup pengembangan aman), bab 10.3 (rantai pasok sumber terbuka dan lisensi), dan bab 10.2 (SBOM, risiko, dan jaminan).

## Prinsip utama

- **Jangan pernah memercayai masukan.** Perlakukan semua data yang melintasi batas kepercayaan sebagai bermusuhan sampai divalidasi.
- **Bawaan aman.** Jalur aman harus menjadi jalur mudah; perilaku tak aman harus memerlukan upaya yang disengaja dan terlihat.
- **Gagal tertutup (fail closed).** Ketika pemeriksaan keamanan tidak dapat selesai, tolak akses alih-alih mengizinkannya.
- **Pertahanan berlapis di lapisan aplikasi.** Padukan validasi, encoding, parameterisasi, dan perlindungan kerangka kerja; jangan bergantung pada satu.
- **Hak istimewa paling sedikit untuk identitas dan token.** Batasi kredensial secara sempit dan kedaluwarsakan dengan cepat.
- **Dependensi Anda adalah kode Anda.** Anda bertanggung jawab atas keamanan segala yang Anda kirim, termasuk komponen pihak ketiga dan sumber terbuka.
- **Standar mengalahkan improvisasi.** Gunakan kerangka kerja yang teruji seperti ASVS [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) alih-alih menciptakan kendali keamanan sendiri.

## Rekomendasi

### Kenali dan pertahankan diri terhadap OWASP Top 10, verifikasi dengan ASVS

OWASP Top 10 adalah daftar garis dasar industri tentang risiko aplikasi web paling kritis: kendali akses yang rusak, kegagalan kriptografis, injeksi, desain tak aman, salah konfigurasi keamanan, komponen rentan, kegagalan autentikasi, kegagalan integritas data, kegagalan pencatatan, dan server-side request forgery. Perlakukan sebagai pengetahuan wajib bagi setiap insinyur, bukan sekadar rujukan kepatuhan untuk diarsipkan.

Untuk standar yang ketat dan dapat diuji, adopsi **OWASP Application Security Verification Standard (ASVS)**. ASVS mendefinisikan persyaratan keamanan pada tiga tingkat jaminan, memberi Anda kendali konkret dan dapat diaudit untuk dirancang dan diuji. Pilih tingkat yang sesuai dengan risiko setiap aplikasi, dan verifikasi terhadapnya.

### Validasi masukan dan encode keluaran

Cacat injeksi tetap termasuk yang paling merusak justru karena begitu mudah diperkenalkan. Bertahanlah dengan kendali berlapis:

- **Validasi masukan** terhadap allow-list ketat (tipe, panjang, format, rentang yang diharapkan). Tolak alih-alih membersihkan di tempat Anda bisa.
- **Gunakan kueri berparameter** dan [prepared statement](https://en.wikipedia.org/wiki/Prepared_statement) untuk semua akses basis data; jangan pernah membangun SQL dengan penggabungan string. Gunakan query builder dan ORM (object-relational mapper) yang aman dengan benar.
- **Encode keluaran** secara kontekstual. HTML, atribut HTML, JavaScript, URL, dan CSS masing-masing membutuhkan encoding berbeda. Bersandarlah pada auto-escaping kerangka kerja dan pahami batasnya.
- **Cegah [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** dengan encoding keluaran plus Content Security Policy yang kuat sebagai lapisan kedua.
- **Cegah injeksi perintah dan templat** dengan menghindari pemanggilan shell dengan data tak tepercaya dan dengan memakai templat tanpa logika atau tersandbox.

### Dapatkan autentikasi dan otorisasi dengan benar

Autentikasi membuktikan siapa pengguna. Otorisasi memutuskan apa yang boleh mereka lakukan. Keduanya sering gagal, jadi dapatkan dengan benar.

- Pilih protokol yang mapan: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** untuk otorisasi terdelegasi dan **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** untuk autentikasi. Jangan membangunnya dari nol.
- Tegakkan **[autentikasi multifaktor](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, terutama untuk akses berhak istimewa dan administratif.
- Simpan kata sandi hanya sebagai hash bergaram memakai algoritma modern, lambat, dan memory-hard (seperti [Argon2](https://en.wikipedia.org/wiki/Argon2) atau [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Jangan pernah menyimpan atau mencatat kredensial teks biasa.
- Kelola **sesi** dengan hati-hati: hasilkan token kuat secara kriptografis, setel flag cookie secure dan HttpOnly, rotasi saat hak istimewa berubah, dan kedaluwarsakan sesi menganggur.
- Tegakkan **otorisasi di server untuk setiap permintaan**, memeriksa bahwa principal terautentikasi memiliki atau boleh mengakses sumber daya spesifik tersebut. Otorisasi tingkat objek yang rusak (mengakses catatan pengguna lain dengan mengubah ID) adalah salah satu cacat API paling umum dan parah.
- Pusatkan logika otorisasi di mana praktis agar kebijakan konsisten dan dapat diaudit.

### Kelola rahasia dan rotasi kunci

Rahasia yang dikodekan keras dalam kode sumber adalah penyebab pembobolan yang abadi. Bangun kebiasaan disiplin seputar manajemen rahasia:

- Simpan rahasia di pengelola rahasia atau vault khusus, tidak pernah di kode sumber, berkas konfigurasi, atau variabel lingkungan yang dikomit ke kontrol versi.
- Pindai komit dan repositori untuk rahasia yang bocor secara otomatis, dan blokir penggabungan yang memperkenalkannya.
- Rotasi kunci dan kredensial secara berkala dan segera setelah dugaan eksposur apa pun. Pilih kredensial berumur pendek yang diterbitkan otomatis daripada yang statis dan berumur panjang.
- Terapkan hak istimewa paling sedikit pada setiap rahasia: batasi pada persis apa yang dibutuhkannya.
- Enkripsi rahasia saat disimpan dan saat transit, dan audit akses ke dalamnya.

### Amankan rantai pasok perangkat lunak

Aplikasi modern sebagian besar dirakit dari komponen pihak ketiga, yang menjadikan rantai pasok permukaan serangan utama.

- Pelihara **[Software Bill of Materials](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** untuk setiap aplikasi agar Anda tahu persis apa yang Anda kirim dan dapat merespons cepat ketika kerentanan baru muncul.
- Pindai dependensi secara berkelanjutan (Software Composition Analysis, atau SCA) dan perbaiki komponen yang diketahui rentan dengan segera.
- Sematkan dan verifikasi versi dependensi; gunakan lockfile dan registri tepercaya.
- Adopsi **SLSA** (Supply-chain Levels for Software Artifacts) untuk meningkatkan integritas build, dan hasilkan atestasi **provenance** yang menjelaskan bagaimana artefak dibangun.
- **Tanda tangani artefak** dan verifikasi tanda tangan sebelum deployment agar Anda dapat memercayai bahwa yang berjalan adalah yang Anda bangun.
- Amankan sistem build itu sendiri; pipeline CI yang terkompromi dapat menyuntikkan kode berbahaya ke setiap konsumen hilir.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Beli/adopsi penyedia identitas (OIDC) | Teruji, MFA bawaan, lebih sedikit kode untuk diamankan | Ketergantungan vendor, upaya integrasi, biaya |
| Bangun autentikasi khusus | Kendali penuh, tanpa dependensi eksternal | Sangat mudah keliru, pemeliharaan tinggi |
| Validasi allow-list ketat | Memblokir seluruh kelas kerentanan | Dapat merusak kasus tepi yang sah, lebih banyak kerja di muka |
| Kredensial berumur pendek | Jendela pembobolan kecil, pencabutan otomatis | Membutuhkan infrastruktur penerbitan yang kokoh |
| Pembaruan dependensi agresif | Lebih sedikit kerentanan yang diketahui | Churn, potensi perubahan yang merusak, beban tes |
| SBOM + penandatanganan + provenance | Respons insiden cepat, kepercayaan yang dapat diverifikasi | Investasi perkakas dan proses, perubahan budaya |

Trade-off yang berulang adalah ketelitian di muka versus paparan berkelanjutan. Membangun autentikasi khusus atau melewatkan kebersihan dependensi terasa lebih cepat hari ini dan memakan biaya sangat besar kelak. Mengadopsi standar teruji dan kendali rantai pasok otomatis memakan upaya sekarang, tetapi mengubah risiko tak terbatas dan tak terduga menjadi risiko yang terkelola dan terbatas. Bagi tim besar, pengali otomasi paling penting: kendali yang diterapkan sekali dalam templat jalan-beraspal melindungi setiap layanan yang memakainya.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Kendali ASVS mana yang akan Anda tanamkan ke kerangka kerja jalan-beraspal agar insinyur mendapatkannya gratis?** Langkah berpengungkit tertinggi bagi tim besar adalah menjadikan jalur aman sebagai bawaan, sehingga kendali yang ditulis sekali dalam kerangka kerja bersama melindungi setiap layanan yang mengadopsinya. Putuskan persyaratan ASVS mana (kueri berparameter, encoding keluaran, flag sesi aman, pemeriksaan otorisasi sisi server) yang termasuk dalam templat dan bukan dalam ingatan setiap insinyur. Untuk portofolio enterprise dan pemerintah, putuskan juga aplikasi mana yang membutuhkan ASVS Tingkat 2 versus Tingkat 3, dan kaitkan dengan sensitivitas data yang disentuh masing-masing. Bawa daftar layanan Anda dan tandai mana yang sudah mewarisi bawaan ini dan mana yang mengimplementasikan ulang keamanan dengan tangan, karena yang dibuat tangan adalah tempat injeksi dan kendali akses rusak bersembunyi. Jika bawaan aman hanya hidup di halaman wiki, ia akan dilewati di bawah tekanan pengiriman, jadi taruh di kode.

2. **Bagaimana Anda akan menemukan dan memperbaiki otorisasi tingkat objek yang rusak di setiap API, bukan hanya yang baru?** Mengakses catatan pengguna lain dengan mengubah ID adalah salah satu cacat API paling umum dan parah, dan ia bersembunyi di endpoint lama yang mendahului standar Anda saat ini. Otorisasi sisi server pada setiap permintaan dan setiap objek adalah aturannya, tetapi bagian sulitnya memverifikasi ia bertahan di basis kode menyebar berumur bertahun-tahun yang ditulis banyak tangan. Putuskan apakah Anda akan memusatkan logika otorisasi, menambah tes otomatis yang mencoba akses lintas tenant, atau menjalankan pengujian bertarget terhadap API berisiko tertinggi Anda lebih dulu. Bawa inventaris endpoint yang mengekspos pengidentifikasi objek dan peringkatkan menurut sensitivitas apa yang dikembalikannya. Tanpa penyapuan yang disengaja, Anda akan terus mengirim cacat ini dan menemukannya hanya ketika peneliti atau penyerang menemukannya.

3. **Apa rencana Anda untuk kerentanan dependensi luas berikutnya: secepat apa Anda dapat menemukan dan menambal setiap layanan yang terdampak?** Ketika cacat kritis mendarat di pustaka populer, perusahaan dengan SBOM akurat mengidentifikasi layanan terdampak dalam hitungan jam sementara yang lain menghabiskan berminggu-minggu mencari, dan jurang kecepatan itu menentukan seberapa besar kerusakan yang Anda alami. Putuskan sekarang apakah Anda menghasilkan Software Bill of Materials untuk setiap artefak, apakah pemindaian dependensi berjalan di setiap pipeline, dan siapa yang memiliki keputusan tambalan darurat. Bagi pembeli teregulasi dan pemerintah, SBOM dan provenance bertanda tangan makin menjadi syarat berbisnis, sehingga kesiapan ini juga melindungi pendapatan. Bawa jawaban jujur dari latihan: pilih pustaka yang Anda pakai luas dan ukur berapa lama mendaftar setiap layanan yang mengirimnya. Jika jawabannya diukur dalam hari, investasikan pada inventaris dan penandatanganan sebelum insiden berikutnya memaksa Anda.

4. **Bagaimana Anda akan beralih dari rahasia statis berumur panjang ke kredensial berumur pendek yang diterbitkan otomatis, dan sistem mana yang memblokirnya hari ini?** Rahasia yang dikodekan keras dan berumur panjang adalah penyebab pembobolan yang abadi, dan perbaikannya, kredensial berumur pendek yang diterbitkan sesuai permintaan, bergantung pada infrastruktur penerbitan yang sering tidak dapat dipakai sistem lama. Bagi tim besar bahayanya adopsi yang tidak merata: platform modern merotasi kunci setiap jam sementara layanan warisan masih mengirim kata sandi basis data statis dalam berkas konfigurasi. Putuskan beban kerja mana yang dapat memakai pengelola rahasia atau sistem identitas beban kerja sekarang, mana yang butuh investasi lebih dulu, dan siapa yang memiliki runbook rotasi begitu kunci diduga bocor. Bawa inventaris setiap kredensial yang dipakai, masa hidupnya, radius ledakannya jika terekspos, dan apakah pemindaian komit akan menangkapnya sebelum penggabungan. Dalam pengaturan enterprise dan pemerintah, kaitkan ini dengan audit: pemeriksa makin mengharapkan bukti rotasi, akses terbatas, dan pencatatan akses untuk setiap rahasia, dan kredensial statis yang tak dapat Anda rotasi tanpa downtime adalah temuan yang menunggu ditulis.

5. **Di mana Anda masih menjalankan autentikasi buatan sendiri atau tidak konsisten, dan apa rencana untuk mengonsolidasikannya ke protokol teruji?** Membangun autentikasi adalah salah satu cara termudah memperkenalkan cacat halus yang dapat dieksploitasi, namun kebanyakan properti besar membawa setidaknya satu alur login warisan yang mendahului keputusan membakukan pada OAuth 2.0 dan OIDC. Tekanan yang bersaing itu nyata: memigrasikan alur lama berisiko merusak pengguna dan integrasi yang ada, sementara membiarkannya di tempat membuat target bernilai tinggi kurang terlindungi. Putuskan apakah Anda mengonsolidasikan pada satu penyedia identitas, menegakkan MFA seragam, dan menetapkan tenggat memensiunkan setiap alur pesanan, atau menerima pengecualian terdokumentasi dengan kendali kompensasi. Bawa peta setiap jalur autentikasi di armada, mana yang menegakkan MFA, mana yang menyimpan kata sandi dengan hash memory-hard modern, dan mana yang khusus. Untuk portofolio enterprise dan pemerintah, tambahkan sudut kepatuhan: standar seperti NIST SP 800-63 menetapkan ekspektasi konkret untuk jaminan identitas, dan alur buatan sendiri yang tak dapat mendemonstrasikannya tidak akan selamat dari audit atau tinjauan authority-to-operate.

6. **Bagaimana Anda memverifikasi bahwa kendali ini benar-benar bertahan di produksi, dan dapatkah Anda membuktikannya dengan bukti alih-alih penegasan?** Menulis bawaan aman tidak sama dengan mengetahui setiap layanan masih menghormatinya, dan kendali diam-diam membusuk seiring kode berubah, pengecualian menumpuk, dan endpoint baru dikirim. Bagi tim besar pertanyaannya cakupan: layanan mana yang menjalankan analisis statis, pemindaian dependensi, dan pengujian dinamis atau penetrasi, dan bagaimana Anda tahu yang melewatkannya bukan aplikasi berisiko tertinggi Anda? Putuskan verifikasi apa yang wajib dalam pipeline versus berkala, siapa yang menriase temuan, dan bukti apa yang Anda simpan untuk menunjukkan kendali diuji dan lulus pada tanggal tertentu. Bawa peta cakupan Anda saat ini, waktu rata-rata remediasi menurut keparahan, dan daftar aplikasi tanpa tes terbaru. Dalam konteks teregulasi dan pemerintah, bukti ini bukan opsional: auditor, pejabat pemberi otorisasi, dan penyelidik pembobolan semuanya meminta bukti bahwa kendali diverifikasi, dan kebijakan tanpa catatan tes jarang memuaskan mereka.

## Lensa sektor

**Startup.** Dengan dua atau tiga insinyur dan tanpa spesialis keamanan, pengungkit Anda adalah mewarisi keamanan alih-alih membangunnya: adopsi penyedia OIDC terkelola, bersandarlah pada kerangka kerja yang ORM-nya memparameterkan kueri secara bawaan, dan simpan rahasia di pengelola rahasia platform Anda alih-alih berkas `.env` yang mungkin tak sengaja dikomit rekan. Nyalakan pemindaian dependensi otomatis yang membuka pull request tambalan, dan anggap itu cukup untuk sekarang. Jangan bangun autentikasi atau kripto khusus, karena satu kueri tersuntik atau satu kunci bocor dapat mengakhiri perusahaan sebelum punya pelanggan.

**Bisnis kecil.** Anda kemungkinan tidak punya spesialis keamanan aplikasi dan anggaran ketat, jadi beli kendali yang tertanam dalam perkakas dan platform yang sudah Anda bayar alih-alih mengisi staf fungsi khusus. Pilih penyedia identitas ter-hosting dengan MFA termasuk, basis data terkelola yang mengarahkan Anda ke akses berparameter, dan host repositori yang memindai komit untuk rahasia bocor secara bawaan. Pusatkan perhatian langka Anda pada dasar-dasar OWASP Top 10 yang menyebabkan sebagian besar pembobolan nyata, dan pilih vendor yang mengirim bawaan aman yang tak dapat Anda matikan sembarangan.

**Enterprise.** Lintas banyak tim tantangannya konsistensi: tanamkan kendali ASVS ke kerangka kerja jalan-beraspal agar setiap layanan baru mewarisi kueri berparameter, encoding keluaran, sesi aman, dan otorisasi sisi server secara gratis. Jalankan SBOM akurat dan pemindaian dependensi seluruh armada agar kerentanan pustaka luas berikutnya menjadi urusan jam, bukan minggu, dan pusatkan kebijakan otorisasi agar akses lintas tenant dapat diuji. Bakukan pada satu penyedia identitas dengan MFA yang ditegakkan, dan kelola keamanan aplikasi sebagai portofolio yang diatur dengan tingkat ASVS bertingkat risiko dan bukti yang diaudit.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk kendali yang harus Anda demonstrasikan, bukan sekadar implementasikan. Verifikasi layanan yang menghadap warga terhadap OWASP ASVS pada tingkat yang cocok dengan sensitivitas data, tanda tangani setiap artefak yang di-deploy dan atestasi provenance-nya menurut SLSA untuk memenuhi mandat rantai pasok, dan terbitkan kredensial berumur pendek dari vault pusat dengan pencatatan akses penuh. Harapkan menunjukkan kepada auditor dan pejabat pemberi otorisasi rantai penjagaan terdokumentasi dari kode sumber ke produksi, dan selaraskan jaminan identitas dengan standar terbit seperti NIST SP 800-63.

## Contoh

**Startup.** Tim SaaS tiga insinyur melewatkan membangun loginnya sendiri dan mengadopsi penyedia OIDC terkelola pada hari pertama, mendapat MFA dan reset kata sandi yang aman tanpa menulis kode kritis-keamanan yang tak sanggup mereka salahkan. Mereka bersandar pada ORM kerangka kerja sehingga kueri berparameter secara bawaan, menyimpan rahasia di pengelola rahasia platform alih-alih berkas `.env` yang mungkin tak sengaja dikomit rekan, dan menyalakan pemindaian dependensi otomatis yang membuka pull request ketika pustaka perlu ditambal. Tak satu pun ini memperlambat tim, dan itu berarti satu kunci bocor atau satu kueri tersuntik tidak mengakhiri perusahaan sebelum punya pelanggan.

**Enterprise.** Sebuah platform ritel yang melayani puluhan juta pembeli membakukan autentikasi pada OIDC lewat satu penyedia identitas, menegakkan MFA untuk staf dan autentikasi step-up untuk perubahan akun bernilai tinggi. Semua akses basis data melalui ORM yang dikonfigurasi memparameterkan kueri, dan Content Security Policy mendukung encoding keluaran. Setelah kerentanan yang dipublikasikan luas pada pustaka pencatatan populer, SBOM perusahaan memungkinkannya mengidentifikasi setiap layanan terdampak dalam hitungan jam dan menambalnya dalam dua hari, sementara pesaing tanpa inventaris menghabiskan berminggu-minggu mencari.

**Pemerintah.** Sebuah lembaga tunjangan federal membangun layanan yang menghadap warga yang diverifikasi terhadap OWASP ASVS Tingkat 2, dengan Tingkat 3 untuk komponen yang menangani catatan paling sensitif. Rahasia hidup di vault pusat yang menerbitkan kredensial berumur pendek; pemindaian komit memblokir kunci bocor mana pun. Setiap artefak yang di-deploy ditandatangani dan provenance-nya diatestasi menurut SLSA, memenuhi mandat federal untuk rantai pasok perangkat lunak yang dapat diverifikasi dan memberi auditor rantai penjagaan yang jelas dari sumber ke produksi.

## Kasus bisnis: motivasi, ROI, dan TCO

Pengeluaran keamanan aplikasi membeli turun kategori pembobolan yang paling mungkin dan paling mahal. Total biaya kepemilikan mencakup perkakas (pemindai, pengelola rahasia, penyedia identitas), waktu insinyur untuk memperbaiki temuan, dan gesekan ringan bawaan aman. Terhadap itu, timbang biaya melewatkannya: pembobolan injeksi dan kendali-akses-rusak rutin mengekspos jutaan catatan, memicu denda regulasi, notifikasi wajib, kerugian penipuan, sprint remediasi, dan kerusakan reputasi yang menekan pendapatan selama bertahun-tahun.

ROI paling kuat ketika kendali diotomatisasi dan dipakai ulang. Satu integrasi identitas yang dikonfigurasi baik, satu lapisan kueri yang dikeraskan dalam kerangka kerja bersama, dan satu pipeline yang memblokir dependensi rentan melindungi seluruh armada dengan biaya marginal per layanan. Kendali rantai pasok khususnya telah beralih dari opsional menjadi esensial: dependensi yang terkompromi dapat mengubah setiap pelanggan Anda menjadi korban, dan regulator serta pembeli enterprise makin mewajibkan SBOM dan provenance bertanda tangan sebagai syarat berbisnis. Ketika mengajukan kasus kepada pimpinan, kaitkan investasi dengan risiko spesifik yang dinamai dan dengan persyaratan pengadaan serta kepatuhan yang memblokir pendapatan jika Anda gagal memenuhinya.

## Anti-pola dan jebakan

- **Menggulirkan kripto atau autentikasi sendiri.** Hampir selalu menghasilkan cacat halus yang dapat dieksploitasi.
- **Validasi hanya di sisi klien.** Mudah dilewati; server harus memvalidasi ulang segalanya.
- **Pembersihan berbasis blocklist.** Mencoba membuang karakter "buruk" alih-alih meng-allow-list yang baik; penyerang menemukan celahnya.
- **Rahasia di kode sumber atau berkas lingkungan.** Penyebab paling umum kebocoran kredensial.
- **Mengabaikan otorisasi pada akses objek.** Mengasumsikan pengguna terautentikasi boleh mengakses objek apa pun yang ID-nya dapat ia tebak.
- **Dependensi atur-dan-lupakan.** Tidak pernah memperbarui komponen pihak ketiga sampai pembobolan memaksanya.
- **Memperlakukan Top 10 sebagai garis finis.** Ia lantai, bukan standar komprehensif; gunakan ASVS untuk kedalaman.
- **Mencatat data sensitif.** Kata sandi, token, dan PII (personally identifiable information) dalam log menjadi pembobolan yang menunggu terjadi.

## Model kematangan

**Tingkat 1: Memulai.** Keamanan aplikasi bergantung pada pengetahuan pengembang individual dan bereaksi hanya setelah insiden. Tidak ada kendali standar. Rahasia berada di kode sumber. Dependensi jarang diperbarui. Autentikasi khusus dan ad hoc, dan cacat injeksi atau kendali-akses-rusak ditemukan karena keberuntungan alih-alih proses.

**Tingkat 2: Mengembangkan.** Praktik dasar muncul tetapi bervariasi dari tim ke tim. Kesadaran OWASP Top 10 menyebar, sebagian perlindungan tingkat kerangka kerja ada, dan pengelola rahasia ada namun dipakai tidak merata. Pemindaian dependensi berjalan sesekali. Sistem baru mengadopsi penyedia identitas standar, sementara layanan lama mempertahankan alur login buatan sendiri tak tersentuh.

**Tingkat 3: Membakukan.** Kendali terdokumentasi dan ditegakkan di seluruh organisasi. Persyaratan berbasis ASVS ditetapkan per tingkat risiko, kueri berparameter dan encoding keluaran adalah norma, dan penyedia identitas pusat dengan MFA diwajibkan. Rahasia dikelola dan dipindai otomatis, SBOM dihasilkan, dan pemindaian dependensi berjalan di setiap pipeline.

**Tingkat 4: Mengelola.** Praktik diukur dan dikendalikan terhadap garis dasar. Cakupan pemindaian dan tes, waktu rata-rata remediasi menurut keparahan, bagian layanan yang mewarisi bawaan jalan-beraspal, usia rotasi kredensial dan rahasia, serta kesesuaian ASVS semuanya dilacak di dasbor. Pengecualian dicatat dengan tanggal kedaluwarsa, penyimpangan dari garis dasar memicu tindakan, dan rilis digerbangi pada ambang keamanan terdefinisi alih-alih keputusan sesaat.

**Tingkat 5: Mengorkestrasi.** Keamanan terus diperbaiki dan terintegrasi di seluruh organisasi. Bawaan aman tertanam dalam kerangka kerja jalan-beraspal sehingga jalur aman otomatis, kredensial berumur pendek dipakai di mana-mana, dan jaminan rantai pasok penuh dengan penandatanganan dan provenance (SLSA) adalah standar. Verifikasi berkelanjutan, respons terhadap kerentanan baru cepat dan terukur, dan setiap insiden memberi masukan ke templat bersama sehingga satu perbaikan mengeraskan seluruh armada.

## Gagasan untuk didiskusikan

1. Di mana logika otorisasi harus berada agar konsisten sekaligus dapat dipelihara di banyak layanan?
2. Seagresif apa Anda harus memperbarui dependensi mengingat pertukaran antara paparan dan churn?
3. Tingkat ASVS apa yang cocok untuk setiap kelas aplikasi dalam portofolio Anda?
4. Bagaimana Anda menghilangkan rahasia berumur panjang tanpa menciptakan infrastruktur penerbitan yang rapuh?
5. Apa yang diperlukan agar organisasi Anda menghasilkan dan mengonsumsi SBOM serta provenance untuk setiap artefak?
6. Bagaimana Anda menjaga bawaan aman agar tidak dimatikan di bawah tekanan pengiriman?

## Poin-poin utama

- OWASP Top 10 adalah pengetahuan esensial; ASVS menyediakan standar yang dapat diuji.
- Lapisi validasi masukan, parameterisasi, dan encoding keluaran untuk mengalahkan injeksi dan XSS.
- Gunakan protokol teruji (OAuth 2.0, OIDC) dan tegakkan MFA; jangan pernah membangun autentikasi dari nol.
- Tegakkan otorisasi di sisi server untuk setiap permintaan dan setiap objek.
- Jaga rahasia di luar kode sumber, kelola secara terpusat, dan rotasi ke kredensial berumur pendek.
- Rantai pasok adalah permukaan serangan utama; gunakan SBOM, SCA, penandatanganan, dan provenance (SLSA).
- Kendali yang otomatis dan dapat dipakai ulang melindungi seluruh armada dengan biaya marginal per layanan.

## Referensi dan bacaan lanjutan

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard dan Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation dan OpenSSF, kerangka *SLSA* dan panduan *Supply-chain Security*
