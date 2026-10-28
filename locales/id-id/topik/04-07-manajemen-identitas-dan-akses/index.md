# 4.7 Manajemen identitas dan akses

## Tinjauan dan motivasi

Setiap permintaan yang mengenai sistem Anda membawa klaim implisit: *saya diizinkan melakukan ini*. Manajemen identitas dan akses (IAM) adalah disiplin memutuskan apakah klaim itu benar. Ia menjawab dua pertanyaan terpisah yang terus dikaburkan orang. [Autentikasi](https://en.wikipedia.org/wiki/Authentication) membuktikan siapa Anda. [Otorisasi](https://en.wikipedia.org/wiki/Authorization) memutuskan apa yang boleh Anda lakukan setelah membuktikannya. Jaga kedua gagasan itu tetap berbeda di kepala Anda dan setengah kebingungan di bidang ini lenyap.

Bagi tim besar, identitas diam-diam menjadi kendali terpenting yang Anda miliki. Bab 4.3 menegaskan bahwa identitas adalah perimeter baru, dan bab 4.1 membangun zero trust di atasnya: ketika Anda berhenti memercayai jaringan, satu-satunya hal tersisa untuk dipercaya adalah identitas terverifikasi dan kebijakan eksplisit. Pergeseran itu berarti alur reset kata sandi yang lemah atau akun layanan yang terlupakan bukan lagi bug kecil. Itu pintu depan. Sebagian besar pembobolan nyata bukan eksploit cerdas atas cacat keamanan memori; melainkan kredensial curian, izin terlalu luas, dan akun yang seharusnya dimatikan berbulan-bulan lalu.

Taruhannya naik dalam pengaturan enterprise dan pemerintah. Enterprise global mengelola puluhan direktori yang tumpang tindih, ribuan joiner dan leaver per bulan, dan mitra yang membutuhkan akses terbatas ke sebagian sistem Anda. Lembaga pemerintah menambahkan kredensial kartu pintar, tingkat jaminan identitas yang diwajibkan, dan auditor yang akan bertanya, secara tertulis, persis siapa yang dapat menyentuh catatan tertentu pada hari tertentu. Bab ini berpendirian tentang cara membangun lapisan identitas yang menjawab pertanyaan itu dengan baik tanpa menggilas orang-orang Anda hingga berhenti.

## Prinsip utama

- **Autentikasi dan otorisasi adalah masalah berbeda.** Membuktikan identitas dan memberi izin membutuhkan desain terpisah dan tinjauan terpisah.
- **Satu identitas, banyak sistem.** Konsolidasikan ke satu sumber kebenaran per populasi identitas; sebaran direktori adalah bug keamanan.
- **Hak istimewa paling sedikit secara bawaan.** Mulai dari akses nol dan tambahkan dengan sengaja, untuk manusia dan mesin.
- **Setiap kredensial bersifat sementara.** Pilih kredensial berumur pendek yang diterbitkan otomatis daripada rahasia berumur panjang.
- **Deprovisioning sama pentingnya dengan provisioning.** Akses yang hidup lebih lama daripada kebutuhannya adalah risiko murni.
- **Tahan phishing mengalahkan mudah diingat.** Gerakkan autentikasi menuju passkey dan faktor berbasis perangkat keras.
- **Mesin juga identitas.** Beban kerja, pipeline, dan layanan membutuhkan identitas terkelola, bukan kunci statis bersama.
- **Akses adalah siklus hidup, bukan peristiwa.** Beri, tinjau, dan cabut menurut jadwal, dan buktikan Anda melakukannya.

## Rekomendasi

### Pisahkan autentikasi dari otorisasi, dan pusatkan keduanya

Autentikasi lewat satu penyedia identitas (IdP), sistem yang memverifikasi identitas dan menerbitkan token yang dipercaya sistem lain. Lalu biarkan setiap aplikasi membuat keputusan otorisasinya sendiri dari identitas dan atribut yang dibawa token itu. Pemisahan ini memungkinkan Anda memperkuat autentikasi sekali, untuk semua orang, sambil menjaga logika izin berbutir halus dekat dengan data yang dilindunginya. Adopsi [single sign-on](https://en.wikipedia.org/wiki/Single_sign-on) (SSO), di mana satu autentikasi memberi akses ke banyak aplikasi, agar orang Anda punya satu login kuat alih-alih empat puluh yang lemah. Federasi memperluas kepercayaan yang sama melintasi batas organisasi, memungkinkan identitas mitra mengakses sistem Anda tanpa Anda mengelola kata sandi mereka.

### Gunakan protokol modern untuk apa yang sebenarnya diperuntukkan masing-masing

Tiga standar mengerjakan sebagian besar pekerjaan, dan masing-masing punya tugas. **OpenID Connect (OIDC)** adalah lapisan identitas yang dibangun di atas [OAuth](https://en.wikipedia.org/wiki/OAuth) 2.0; pakai untuk menjawab *siapa pengguna ini* bagi masuk web dan seluler. **OAuth 2.0** adalah kerangka otorisasi untuk akses terdelegasi; pakai untuk membiarkan aplikasi memanggil API atas nama pengguna tanpa pernah melihat kata sandinya (bab 2.3). **Security Assertion Markup Language (SAML)** adalah standar federasi berbasis XML yang lebih tua; ia tetap kuda beban untuk SSO enterprise ke aplikasi bisnis yang mapan. Kekeliruan umum adalah meraih OAuth untuk melakukan autentikasi langsung. OAuth memberi akses ke sumber daya; OIDC duduk di atasnya untuk menetapkan identitas. Pilih OIDC untuk masuk berhadapan pengguna yang baru, pertahankan SAML di tempat katalog enterprise Anda menuntutnya, dan jangan menciptakan format token sendiri.

### Jadikan autentikasi tahan phishing

Kata sandi saja tidak dapat dipertahankan pada skala besar. Wajibkan autentikasi multifaktor (MFA), yang memadukan sesuatu yang Anda tahu, sesuatu yang Anda miliki, dan sesuatu yang Anda adalah, untuk setiap akun manusia tanpa pengecualian. Lalu melangkahlah melewati faktor lemah: kode sekali pakai lewat SMS dapat di-phishing dan di-SIM-swap. Tujuan kuatnya adalah [passkey](https://en.wikipedia.org/wiki/Passkey) dan standar WebAuthn di baliknya (API peramban untuk autentikasi kunci publik), yang mengikat login pada kunci privat yang dipegang perangkat keras dan pada origin situs yang asli, sehingga halaman palsu tidak dapat memanen apa pun yang layak dicuri. Passkey juga tanpa kata sandi, yang akan disyukuri pengguna Anda. Perlakukan pemulihan akun dan reset kata sandi sebagai bagian permukaan autentikasi, karena penyerang yang tidak dapat mengalahkan MFA Anda akan sekadar menyerang alur reset.

### Kelola siklus hidup joiner-mover-leaver, dan deprovisioning cepat

Identitas adalah siklus hidup. **Joiner** membutuhkan akses yang tepat pada hari pertama. **Mover** yang berganti peran membutuhkan akses baru dan, yang krusial, membutuhkan akses lama dicabut, atau mereka perlahan mengumpulkan kunci seluruh gedung. **Leaver** harus kehilangan semua akses dengan segera, idealnya dalam menit setelah hari terakhir mereka, di setiap sistem. Gerakkan ini dari sumber otoritatif, biasanya sistem sumber daya manusia, agar perubahan status di sana otomatis menyediakan dan mencabut hilir. Otomatiskan. Daftar periksa offboarding manual selalu melewatkan sesuatu, dan akun yang terlewat adalah yang muncul di laporan insiden.

### Pilih model otorisasi dan ekspresikan sebagai policy-as-code

Beri izin lewat [kendali akses berbasis peran](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC), di mana Anda menetapkan izin ke peran fungsi pekerjaan dan menetapkan orang ke peran, karena mudah dinalar dan mudah diaudit. Raih [kendali akses berbasis atribut](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) di tempat Anda butuh keputusan sadar konteks berdasarkan atribut seperti departemen, klasifikasi data, lokasi, atau waktu. Kebanyakan organisasi matang menjalankan hibrida: RBAC untuk pemberian kasar, ABAC untuk kondisi halus. Apa pun pilihan Anda, ekspresikan otorisasi sebagai **policy-as-code**: aturan yang ditulis dalam bentuk dikontrol versi, dapat diuji, dan dapat ditinjau alih-alih diklik ke konsol. Policy-as-code membuat keputusan akses dapat diaudit, dapat dibandingkan, dan konsisten lintas lingkungan, dan memungkinkan Anda menguji perubahan izin sebelum dikirim.

### Tegakkan hak istimewa paling sedikit dengan akses just-in-time dan PAM

Terapkan [prinsip hak istimewa paling sedikit](https://en.wikipedia.org/wiki/Principle_of_least_privilege): setiap identitas mendapat akses minimum yang dibutuhkannya dan tidak lebih. Hak istimewa tetap (standing) adalah musuh, karena izin yang diberikan permanen adalah izin yang tersedia bagi penyerang mana pun yang mendarat di akun itu kapan saja. Pilih **akses just-in-time (JIT)**, di mana orang meminta hak yang ditinggikan untuk jendela terbatas, mendapatkannya setelah persetujuan, dan kehilangannya secara otomatis ketika jendela menutup. Untuk akun paling berbahaya Anda, adopsi **privileged access management (PAM)**: sistem yang memvault kredensial administratif, menengahi dan merekam sesi berhak istimewa, dan menerbitkan peninggian sesuai permintaan. Tujuannya akses admin tetap nol, sehingga bahkan laptop yang sepenuhnya terkompromi tidak menghasilkan sesuatu yang tahan lama.

### Beri mesin dan beban kerja identitas sejati

Manusia hanya separuh identitas Anda. Layanan, pipeline, kontainer, dan fungsi semuanya mengautentikasi ke sesuatu, dan terlalu sering dengan rahasia berumur panjang yang ditempel ke berkas konfigurasi. Ganti kunci statis dengan **identitas beban kerja** terkelola: kredensial berumur pendek yang diterbitkan otomatis ke beban kerja berdasarkan di mana ia berjalan dan apa ia. Gunakan mutual TLS (mTLS), di mana kedua sisi koneksi menunjukkan sertifikat, untuk autentikasi antarlayanan. Simpan rahasia yang tersisa di pengelola rahasia khusus dengan rotasi, tidak pernah di kode sumber atau citra (bab 4.2). Kredensial beban kerja berumur pendek yang dirotasi otomatis menghapus penyebab tunggal paling umum kebocoran kredensial cloud.

### Jadikan identitas control plane, dan tinjau akses secara berkelanjutan

Dalam arsitektur zero trust (bab 4.1), identitas adalah tempat kebijakan diputuskan dan ditegakkan, jadi berinvestasilah di sana sebagaimana mestinya. Lalu tutup lingkarannya dengan **tinjauan akses**, juga disebut rekertifikasi: menurut jadwal, pemilik setiap sistem mengonfirmasi bahwa setiap orang dan mesin dengan akses masih membutuhkannya, dan mencabut apa yang tak dapat mereka benarkan. Umpankan setiap peristiwa autentikasi dan otorisasi ke jejak audit yang menjawab *siapa mengakses apa, kapan, dan di bawah kebijakan apa* (bab 4.6). Tinjauan akses adalah cara Anda melawan privilege creep, akumulasi izin perlahan yang tak ada satu pemberian pun yang tampak tak masuk akal tetapi bersama-sama membuat akun jauh terlalu berkuasa.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| IdP terpusat dengan SSO | Satu login kuat, kebijakan konsisten, audit mudah | Titik kegagalan tunggal; pemadaman mengunci semua orang |
| RBAC | Sederhana, dapat diaudit, familier | Ledakan peran; kasar untuk kebutuhan peka konteks |
| ABAC | Berbutir halus, sadar konteks, berskala dengan atribut | Lebih sulit dirancang, diuji, dan dinalar |
| Passkey / WebAuthn | Tahan phishing, tanpa kata sandi, kuat | Alur pemulihan dan kehilangan perangkat butuh desain hati-hati |
| Akses just-in-time | Hampir nol hak istimewa tetap | Gesekan; butuh jalur persetujuan cepat dan andal |
| Federasi dengan mitra | Tanpa pengelolaan kata sandi eksternal; kepercayaan terbatas | Kepercayaan bergantung pada kebersihan mitra sendiri |
| Kunci layanan berumur panjang | Sangat mudah disiapkan | Rawan bocor; penyebab teratas pembobolan kredensial |

Ketegangan pusatnya adalah keamanan versus gesekan. Setiap kendali yang mengecilkan permukaan serangan (MFA di segalanya, peninggian JIT, masa hidup kredensial pendek) juga menambah satu langkah pada hari seseorang, dan orang menyiasati kendali yang terlalu menyakitkan. Selesaikan dengan menjadikan jalur aman sebagai jalur mudah: SSO agar autentikasi kuat hanya satu ketukan, passkey agar tak ada kata sandi untuk diketik, dan provisioning otomatis agar akses yang tepat sekadar muncul. Belanjakan anggaran gesekan Anda di tempat radius ledakan terbesar, pada akses berhak istimewa dan produksi, dan jaga akses sehari-hari nyaris tanpa gesekan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Secepat apa Anda sebenarnya dapat mencabut semua akses untuk seseorang yang pergi hari ini, dan bagaimana Anda tahu itu berhasil?** Kecepatan deprovisioning adalah ukuran langsung kematangan identitas Anda, karena leaver yang aksesnya bertahan adalah akun tak terpantau dengan izin nyata. Dalam organisasi besar dengan puluhan sistem terputus, jawaban jujurnya sering "kami tidak yakin," dan celahnya biasanya aplikasi yang tak pernah tersambung ke penyedia identitas pusat. Bawa kepergian nyata terbaru dan telusuri setiap sistem yang dapat disentuhnya, memeriksa stempel waktu kapan setiap akses benar-benar berakhir. Putuskan target, seperti pencabutan penuh dalam satu jam setelah perubahan status sumber daya manusia, dan instrumentasikan agar Anda dapat membuktikannya alih-alih berharap. Jika sistem mana pun bergantung pada seseorang mengingat langkah manual, itulah akun yang akan dipakai pembobolan mendatang.

2. **Di mana Anda masih punya akses berhak istimewa tetap dan kredensial statis berumur panjang, dan apa yang diperlukan untuk menghilangkannya?** Hak admin tetap dan kunci layanan permanen adalah dua aset yang paling diinginkan penyerang, karena tahan lama dan berkuasa. Inventarisasi setiap manusia dengan akses produksi atau administratif selalu-aktif dan setiap layanan yang mengautentikasi dengan kunci statis, lalu tanyakan dengan jujur mana yang dapat pindah ke peninggian just-in-time atau identitas beban kerja berumur pendek. Pertimbangan yang bersaing adalah ketakutan operasional: tim mempertahankan akses tetap karena momen break-glass terasa lebih aman dengannya, sehingga Anda harus membuat peninggian darurat cepat dan andal sebelum mengambil hak tetap itu. Bawa daftar itu ke diskusi dan peringkatkan butir menurut radius ledakan, menargetkan akses produksi dan administratif lebih dulu. Keadaan akhir yang dituju adalah akses admin tetap nol dan tak ada kunci statis yang hidup lebih lama daripada satu deploy.

3. **Apakah Anda punya satu identitas otoritatif per orang dan per beban kerja, atau beberapa, dan apa harga sebaran itu bagi Anda?** Sebaran direktori, di mana manusia yang sama ada sebagai lima akun di lima sistem dengan atribut yang menyimpang, adalah tempat celah deprovisioning dan akses yatim lahir. Mengonsolidasikan ke satu sumber kebenaran per populasi identitas adalah salah satu investasi berpengungkit tertinggi yang dapat dilakukan tim besar, karena setiap kendali hilir bergantung pada mengetahui bahwa dua catatan adalah orang yang sama. Bawa inventaris penyimpanan identitas Anda dan petakan mana yang otoritatif versus mana yang salinan nyaman yang tak diatur siapa pun. Pertukarannya adalah bahwa konsolidasi migrasi besar yang tak glamor yang bersaing dengan pekerjaan fitur untuk perhatian. Putuskan apakah biaya berkelanjutan sebaran, dalam rasa sakit audit dan risiko pembobolan, membenarkan mendanai migrasi itu sekarang alih-alih setelah insiden berikutnya.

4. **Apakah faktor autentikasi terkuat Anda benar-benar tahan phishing, dan apa yang menghalangi Anda memensiunkan kata sandi selamanya?** Faktor yang tak dapat di-phishing penyerang adalah yang mengakhiri pencurian kredensial sebagai jalur pembobolan dominan Anda, dan passkey yang terikat WebAuthn adalah satu-satunya opsi yang dapat di-deploy luas yang melewati standar itu. Dalam organisasi besar gambaran jujurnya biasanya campuran: passkey untuk sebagian, kode sekali pakai lewat SMS untuk yang lain, dan ekor panjang aplikasi warisan yang masih menerima kata sandi saja. Pertimbangan yang bersaing itu nyata, karena passkey menggeser masalah sulit ke pemulihan dan kehilangan perangkat, dan alur pemulihan yang canggung menjadi target lunak baru yang sekadar dialihi penyerang. Bawa angka cakupan menurut jenis faktor, daftar aplikasi yang masih kembali ke kata sandi, dan jalur pemulihan akun yang dirancang yang akan Anda percayai terhadap upaya rekayasa sosial yang gigih. Dalam pengaturan enterprise dan pemerintah, kaitkan target dengan tingkat jaminan yang diwajibkan, karena sistem berjaminan tinggi yang masih mengizinkan faktor yang dapat di-phishing punya celah kepatuhan sekaligus keamanan.

5. **Bagaimana Anda memutuskan akses apa yang didapat setiap identitas, dan dapatkah Anda membandingkan, menguji, dan membuktikan keputusan itu sebelum dikirim?** Jarak antara "seseorang mengklik izin ke konsol" dan "kebijakan dikontrol versi yang ditinjau" adalah beda antara model akses yang dapat Anda audit dan yang hanya dapat Anda mohonkan maaf. Bagi tim besar tekanannya membiarkan setiap aplikasi menumbuhkan aturan pesanannya sendiri, yang diam-diam menghasilkan ledakan peran di sisi RBAC dan kondisi tak teruji di sisi ABAC, sampai tak seorang pun dapat mengatakan apa yang sebenarnya diizinkan suatu pemberian. Pertimbangan yang bersaing adalah kecepatan pengiriman, karena mengekspresikan otorisasi sebagai policy-as-code menambah langkah tinjauan yang tidak dimiliki klik konsol, dan tim di bawah tenggat membenci gesekan itu sampai audit gagal pertama atau pemberian terlalu luas membuat kasusnya bagi mereka. Bawa perubahan izin nyata dan telusuri bagaimana ia akan diusulkan, diuji, ditinjau, dan di-rollback, plus hitungan berapa banyak peran yang Anda punya dan berapa yang tak dapat dijelaskan siapa pun. Dalam pengaturan enterprise dan pemerintah, auditor akan meminta Anda menunjukkan persis siapa yang dapat mengakses catatan dan di bawah aturan apa pada hari tertentu, dan hanya kebijakan yang dapat dibandingkan dan diuji yang menjawabnya tanpa perebutan.

6. **Kapan tinjauan akses terakhir mencabut sesuatu yang nyata, dan siapa yang bertanggung jawab ketika privilege creep tak terkendali?** Tinjauan akses adalah kendali yang melawan akumulasi perlahan izin yang tak ada satu pemberian pun yang tampak tak masuk akal, dan tinjauan yang tak pernah mencabut apa pun adalah teater tinjauan yang menghasilkan kertas kerja alih-alih keselamatan. Dalam organisasi besar mode kegagalannya adalah stempel karet: pemilik sistem merekertifikasi ratusan entri dalam satu duduk, menyetujui semuanya karena mengevaluasi tiap entri secara sungguh-sungguh itu membosankan dan insentif menjaga akses tetap mengalir lebih kuat daripada insentif memotongnya. Pertimbangan yang bersaing adalah bahwa tinjauan bermakna memakan waktu pemilik dan sesekali merusak alur kerja seseorang ketika akses yang diam-diam mereka andalkan lenyap, sehingga Anda harus membuat tinjauan bertarget dan digerakkan risiko alih-alih daftar tak terdiferensiasi. Bawa tingkat pencabutan dari siklus terakhir Anda, rata-rata jumlah entitlement per orang, dan bukti siapa yang memiliki rekertifikasi setiap sistem. Dalam pengaturan enterprise dan pemerintah, namai pejabat yang bertanggung jawab untuk setiap tinjauan dan irama yang menjadi tanggungannya, karena privilege creep yang tak menjadi tanggung jawab siapa pun untuk ditangkap adalah kondisi persis yang dieksploitasi auditor dan penyerang.

## Lensa sektor

**Startup.** Beli identitas, jangan bangun. Satu penyedia identitas ter-hosting dengan SSO, passkey diwajibkan, dan offboarding sekali klik memberi segelintir insinyur postur kelas enterprise dengan biaya per kursi. Bersandarlah pada identitas beban kerja bawaan penyedia agar tidak ada satu pun kunci cloud berumur panjang di pipeline Anda, dan pakai OIDC dan OAuth 2.0 siap pakai alih-alih menciptakan penanganan token yang tak sanggup Anda pelihara.

**Bisnis kecil.** Tanpa spesialis identitas di staf, pilih SSO dan MFA yang sudah dibundel dalam perkakas yang Anda bayar, dan nyalakan alih-alih berbelanja platform terpisah. Perlakukan masalah joiner-mover-leaver sebagai daftar periksa tertulis singkat yang terikat pada siapa pun yang memiliki perekrutan, dan pilih passkey karena menghapus beban helpdesk reset kata sandi yang tak sanggup Anda tugaskan kepada siapa pun. Hindari login bersama, karena itu kebiasaan murah yang kelak membuat atribusi dan pencabutan mustahil.

**Enterprise.** Pekerjaannya konsolidasi dan tata kelola lintas banyak direktori dan tim: satu penyedia identitas otoritatif yang digerakkan sistem sumber daya manusia, alur joiner-mover-leaver otomatis, RBAC untuk fungsi pekerjaan dengan ABAC untuk konteks, dan manajemen akses berhak istimewa dengan perekaman sesi. Ekspresikan otorisasi sebagai policy-as-code agar perubahan dapat dibandingkan dan diuji, jalankan tinjauan akses terjadwal yang benar-benar mencabut, dan bakukan antarmuka agar aplikasi tersambung ke identitas pusat alih-alih masing-masing menumbuhkan loginnya sendiri.

**Pemerintah.** Pengadaan, transparansi, dan akuntabilitas publik menggerakkan desain. Ikat autentikasi pada kredensial perangkat keras seperti kartu pintar PIV atau CAC, tetapkan tingkat jaminan identitas menurut NIST SP 800-63 agar sistem berisiko lebih tinggi menuntut faktor berjaminan lebih tinggi, dan simpan log audit tak berubah yang menjawab persis siapa mengakses apa dan kapan. Terbitkan penanganan bahasa sederhana atas identitas yang menghadap warga, jaga tumpukan identitas pelanggan dan tenaga kerja terpisah, dan pastikan setiap tindakan berhak istimewa pada sistem sensitif ditengahi dan direkam untuk auditor yang akan bertanya.

## Contoh

**Startup.** Sebuah startup dua puluh orang tidak dapat mengisi staf tim identitas, jadi ia membelinya. Setiap karyawan masuk lewat satu penyedia identitas ter-hosting dengan SSO ke email, hosting kode, konsol cloud, dan aplikasi internal, dan passkey diwajibkan sehingga tidak ada kata sandi untuk di-phishing. Offboarding sekali klik: menonaktifkan orang di penyedia identitas memutus akses di mana-mana sekaligus. Untuk produknya sendiri, mereka memakai OIDC untuk masuk pengguna dan OAuth 2.0 agar integrasi dapat memanggil API mereka dengan token terbatas. Autentikasi layanan-ke-cloud memakai identitas beban kerja bawaan penyedia, sehingga tak ada satu pun kunci cloud berumur panjang di mana pun dalam pipeline mereka. Ini berbiaya biaya per kursi sederhana dan membeli postur identitas yang lebih kuat daripada yang dijalankan banyak enterprise.

**Enterprise.** Sebuah bank multinasional telah menumpuk selama satu dekade empat direktori dan ratusan aplikasi, sebagian difederasi lewat SAML, sebagian dengan login lokal sendiri. Ia mendanai program konsolidasi: satu penyedia identitas otoritatif, digerakkan sistem sumber daya manusia, dengan alur joiner-mover-leaver otomatis yang menyediakan saat perekrutan dan mencabut dalam menit setelah pemutusan. RBAC mencakup fungsi pekerjaan standar sementara ABAC menegakkan aturan residensi data dan izin untuk akses lintas batas. Administrator tidak memegang akses produksi tetap; mereka meminta peninggian just-in-time lewat sistem manajemen akses berhak istimewa yang merekam setiap sesi. Tinjauan akses kuartalan memaksa pemilik sistem merekertifikasi atau mencabut, dan setiap keputusan diekspresikan sebagai policy-as-code sehingga auditor dapat membandingkan persis apa yang berubah dan kapan.

**Pemerintah.** Sebuah lembaga federal menerbitkan kartu pintar personal identity verification (PIV), dan padanan militernya, common access card (CAC), kepada tenaga kerjanya, sehingga autentikasi terikat pada kredensial perangkat keras alih-alih kata sandi. Programnya mengikuti pendekatan federal identity, credential, and access management (FICAM) dan menetapkan tingkat jaminan identitas menurut pedoman National Institute of Standards and Technology NIST SP 800-63, sehingga sistem berisiko lebih tinggi menuntut kredensial berjaminan lebih tinggi. Layanan yang menghadap warga memakai tumpukan identitas pelanggan terpisah pada tingkat jaminan lebih rendah dengan MFA kuat. Tinjauan akses dan log audit tak berubah memberi makan langsung bukti otorisasi berkelanjutan lembaga (bab 4.6), dan setiap tindakan berhak istimewa pada sistem terklasifikasi ditengahi dan direkam.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil investasi identitas datang dari memindahkan vektor pembobolan dominan Anda keluar dari zona bahaya. Kredensial curian dan akun berizin berlebih menggerakkan bagian besar insiden nyata, dan masing-masing membawa ekor berat: respons insiden, denda regulasi, notifikasi pembobolan, dan kerusakan reputasi yang bertahan. MFA tahan phishing saja menghilangkan jalur intrusi paling umum, dan deprovisioning otomatis menutup celah akun yatim yang mengubah kepergian rutin menjadi paparan. Ini termasuk pengurangan risiko termurah per dolar yang dikeluarkan.

Total biaya kepemilikan nyata tetapi terbatas. Ia mencakup lisensi penyedia identitas, platform manajemen akses berhak istimewa dan rahasia, rekayasa untuk menyambungkan setiap aplikasi ke identitas pusat, dan upaya berkelanjutan tinjauan akses. Biaya yang lebih besar bersifat organisasi: mengonsolidasikan direktori dan memasang SSO pada aplikasi warisan adalah kerja lambat dan tak glamor yang bersaing dengan fitur. Timbang terhadap alternatifnya. Identitas terfragmentasi membelanjakan uang yang sama selamanya dalam bentuk offboarding manual, perebutan audit, dan reset kata sandi helpdesk, ditambah biaya akhir pembobolan yang dibuat mungkin oleh fragmentasi. Ketika mengajukan kasus kepada pimpinan, bingkai identitas sebagai control plane untuk zero trust: konsolidasi dan otomasi adalah investasi sekali jalan yang menurunkan risiko pembobolan sekaligus biaya berulang audit, offboarding, dan dukungan akses.

## Anti-pola dan jebakan

- **Akun yatim.** Akses yang hidup lebih lama daripada orang atau tujuannya, terutama akun layanan tak terpantau dan kontraktor yang terlupakan.
- **Admin tetap di mana-mana.** Akses berhak istimewa selalu-aktif alih-alih peninggian just-in-time, memberi akun admin terkompromi mana pun kekuasaan tahan lama.
- **Kunci statis berumur panjang.** Kredensial layanan yang ditempel ke konfigurasi atau CI yang tak pernah kedaluwarsa dan akhirnya bocor.
- **Sebaran direktori.** Orang yang sama sebagai banyak akun tak terkelola, sehingga tak ada perubahan yang sepenuhnya merambat.
- **Akun bersama.** Kredensial dipakai beberapa orang, menghancurkan atribusi dan membuat pencabutan mustahil.
- **SMS sebagai faktor kuat Anda.** Memperlakukan kode sekali pakai yang dapat di-phishing dan di-SIM-swap sebagai MFA yang cukup.
- **Ledakan peran.** Begitu banyak peran RBAC sempit sehingga model menjadi tak dapat diaudit dan tak seorang pun tahu apa yang diberikan suatu peran.
- **Deprovisioning sebagai daftar periksa manual.** Langkah offboarding manusia yang pasti melewatkan satu akun yang penting.
- **OAuth dipakai untuk autentikasi.** Memperlakukan token akses sebagai bukti identitas alih-alih memakai OIDC.
- **Teater tinjauan.** Rekertifikasi akses distempel karet tanpa ada yang sungguh-sungguh mengevaluasi kebutuhan.

## Model kematangan

- **Tingkat 1, Memulai:** Setiap aplikasi punya login sendiri. Kata sandi tanpa MFA konsisten. Provisioning dan offboarding manual, reaktif, dan lambat; akun yatim menumpuk. Kredensial layanan adalah kunci statis berumur panjang. Tidak ada tinjauan akses; izin diberikan dan tak pernah ditinjau ulang.
- **Tingkat 2, Mengembangkan:** SSO mencakup aplikasi utama lewat penyedia identitas pusat, tetapi cakupan tidak merata antartim. MFA diwajibkan untuk sebagian besar akses manusia. RBAC dasar ada. Joiner-mover-leaver sebagian diotomatisasi dari sistem sumber daya manusia. Sebagian akun berhak istimewa di-vault. Tinjauan akses terjadi sesekali dan tidak konsisten.
- **Tingkat 3, Membakukan:** Penyedia identitas terkonsolidasi bersifat otoritatif untuk tenaga kerja, dengan provisioning otomatis dan deprovisioning cepat yang ditegakkan di seluruh organisasi. MFA tahan phishing adalah standar dan terdokumentasi. RBAC plus ABAC diekspresikan sebagai policy-as-code. Manajemen akses berhak istimewa dengan perekaman sesi ada. Identitas beban kerja menggantikan sebagian besar kunci statis. Tinjauan akses terjadwal ditegakkan dan diaudit terhadap kebijakan tertulis yang diikuti setiap tim.
- **Tingkat 4, Mengelola:** Program identitas diukur terhadap garis dasar dan dikendalikan dengan data. Anda melacak waktu deprovisioning dari perubahan status sumber daya manusia sampai pencabutan penuh, cakupan MFA dan passkey menurut populasi, jumlah akun dengan hak istimewa tetap, jumlah kunci statis berumur panjang yang masih dipakai, jumlah akun yatim, dan tingkat pencabutan tinjauan akses. Metrik membawa target, seperti pencabutan penuh dalam satu jam dan nol pemberian admin tetap baru bersih, dan pelanggaran ambang memicu penyelidikan alih-alih angkat bahu. Perubahan otorisasi diuji dalam pipeline dan setiap go atau no-go pada pemberian akses digerakkan bukti, bukan kebiasaan.
- **Tingkat 5, Mengorkestrasi:** Identitas adalah control plane yang terus diperbaiki untuk zero trust, terintegrasi dengan keamanan, risiko, dan perencanaan joiner-mover-leaver di seluruh organisasi. Passkey adalah bawaan dan kata sandi sedang dipensiunkan. Nol hak istimewa tetap dicapai lewat peninggian just-in-time, dan semua beban kerja memakai kredensial berumur pendek yang dirotasi otomatis dan mTLS. Otorisasi sepenuhnya policy-as-code. Tinjauan akses berkelanjutan dan digerakkan risiko, deprovisioning nyaris seketika, dan setiap keputusan menghasilkan bukti audit secara otomatis. Model beradaptasi seiring sinyal risiko bergeser, mengetatkan atau melonggarkan akses secara dinamis alih-alih pada irama tetap.

## Gagasan untuk didiskusikan

1. Apa yang diperlukan untuk mencapai akses administratif tetap nol, dan jalur break-glass apa yang akan membuatnya aman?
2. Di mana ABAC layak kompleksitasnya di lingkungan Anda versus tetap pada RBAC biasa?
3. Seagresif apa Anda harus memensiunkan kata sandi demi passkey, dan alur pemulihan apa yang menggantikannya?
4. Aplikasi mana yang masih di luar penyedia identitas pusat Anda, dan apa yang menahannya di sana?
5. Bagaimana Anda memberi mitra dan pelanggan akses terbatas tanpa mewarisi kebersihan keamanan mereka?
6. Metrik tunggal apa yang paling baik menangkap kecepatan deprovisioning Anda, dan apakah Anda mengukurnya hari ini?

## Poin-poin utama

- Autentikasi membuktikan siapa Anda; otorisasi memutuskan apa yang boleh Anda lakukan. Rancang dan tinjau secara terpisah.
- Konsolidasikan ke satu penyedia identitas otoritatif dengan SSO; sebaran direktori adalah cacat keamanan, bukan kenyamanan.
- Otomatiskan siklus hidup joiner-mover-leaver dan jadikan deprovisioning cepat dan dapat dibuktikan.
- Gunakan OIDC untuk masuk pengguna, OAuth 2.0 untuk akses API terdelegasi, dan SAML di tempat katalog enterprise membutuhkannya; jangan pakai OAuth sebagai autentikasi.
- Gerakkan autentikasi menuju passkey dan WebAuthn yang tahan phishing; wajibkan MFA di mana-mana dan perlakukan faktor lemah sebagai solusi sementara.
- Tegakkan hak istimewa paling sedikit dengan akses just-in-time dan manajemen akses berhak istimewa; tuju hak admin tetap nol.
- Beri mesin identitas sejati dengan kredensial beban kerja berumur pendek dan mTLS; hilangkan kunci statis berumur panjang.
- Jadikan identitas control plane untuk zero trust (bab 4.1), dan tutup lingkaran dengan tinjauan akses berkelanjutan dan bukti audit (bab 4.6).

## Referensi dan bacaan lanjutan

- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines* (jaminan identitas, autentikasi, dan tingkat federasi)
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations*
- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*, keluarga Access Control (AC) dan Identification and Authentication (IA)
- The OAuth 2.0 Authorisation Framework, IETF RFC 6749, dan OAuth 2.0 Security Best Current Practice
- Spesifikasi OpenID Connect Core 1.0, OpenID Foundation
- Spesifikasi Security Assertion Markup Language (SAML) 2.0, OASIS
- Web Authentication (WebAuthn) Level 2, Rekomendasi W3C, dan spesifikasi passkey FIDO2 / FIDO Alliance
- Arsitektur dan playbook Federal Identity, Credential, and Access Management (FICAM), U.S. General Services Administration
- FIPS 201, *Personal Identity Verification (PIV) of Federal Employees and Contractors*
- Dokumentasi Open Policy Agent (OPA), Cloud Native Computing Foundation (policy-as-code untuk otorisasi)
