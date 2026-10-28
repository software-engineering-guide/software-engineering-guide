# 10.3 Pengadaan, sumber terbuka, dan lisensi

## Tinjauan dan motivasi

Hampir setiap sistem perangkat lunak modern sebagian besar dirakit dari komponen yang ditulis orang lain. [Perangkat lunak sumber terbuka](https://en.wikipedia.org/wiki/Open-source_software) membentuk fondasi sistem operasi, bahasa, kerangka kerja, basis data, dan infrastruktur cloud. Ia masuk ke enterprise lewat dua jalan: lewat [pengadaan](https://en.wikipedia.org/wiki/Procurement) yang disengaja, dan lewat pernyataan `import` santai oleh pengembang individual. Bab ini membahas melakukan konsumsi itu (dan, di mana cocok, kontribusi) dengan sengaja. Itu berarti strategi, kepatuhan lisensi, pemahaman atas kewajiban dan risiko copyleft, dan rencana untuk [akhir masa pakai](https://en.wikipedia.org/wiki/End-of-life_(product)) yang tak terelakkan dari komponen yang Anda andalkan.

Bagi tim besar taruhannya sekaligus hukum, operasional, dan strategis. Secara hukum, [lisensi](https://en.wikipedia.org/wiki/Software_license) sumber terbuka adalah kontrak yang dapat ditegakkan dengan kewajiban nyata. Salah menata [copyleft](https://en.wikipedia.org/wiki/Copyleft) (lisensi yang dapat mewajibkan karya turunan dibagikan dengan ketentuan sama) dapat, dalam kasus terburuk, memaksa pengungkapan sumber proprietari atau memicu litigasi. Pelanggaran lisensi bahkan dapat memblokir akuisisi atau penawaran umum selama [uji tuntas](https://en.wikipedia.org/wiki/Due_diligence). Secara operasional, dependensi tak terkelola membusuk: komponen tak lagi dipelihara, mengumpulkan kerentanan, dan mencapai akhir masa pakai sementara masih terkubur dalam di produksi. Secara strategis, sumber terbuka lebih dari masukan penghemat biaya. Ia cara menghindari [lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in), menarik talenta, dan membentuk ekosistem yang Anda andalkan, keuntungan yang hanya Anda tangkap jika terlibat dengan sengaja.

Pemerintah punya dimensi tambahan. Banyak yurisdiksi kini punya kebijakan eksplisit yang mengutamakan sumber terbuka, standar terbuka, dan berbagi kode antarlembaga. Ini sering diekspresikan sebagai "uang publik, kode publik": prinsip bahwa perangkat lunak yang didanai pembayar pajak harus, secara bawaan, tersedia bagi publik. Jadi insinyur sektor publik harus menavigasi baik kepatuhan lisensi maupun mandat aktif untuk memilih, menerbitkan, dan memakai ulang sumber terbuka. Bab ini bertujuan membuat semuanya dapat dikelola pada skala besar.

## Prinsip utama

- **Sumber terbuka adalah rantai pasok, bukan barang gratis.** Perlakukan komponen yang dikonsumsi dengan ketelitian sama seperti pemasok kritis mana pun.
- **Lisensi adalah kewajiban, bukan izin untuk diabaikan.** Setiap dependensi membawa ketentuan; ketahui sebelum Anda mengirim.
- **Copyleft adalah kendala desain, bukan tabu.** Lisensi copyleft dapat dipakai dan berharga; mereka hanya mengharuskan Anda memahami bagaimana Anda menggabungkan dan mendistribusikan perangkat lunak.
- **Konsumsi dengan sengaja, berkontribusi secara strategis.** Putuskan apa yang dibawa masuk dan, di mana melayani Anda, berinvestasi pada upstreaming alih-alih fork.
- **Inventarisasi segalanya.** Anda tak dapat mematuhi, mengamankan, atau memperbarui apa yang tak dapat Anda lihat; SBOM (software bill of materials, inventaris lengkap komponen dalam perangkat lunak Anda) adalah syarat dasar.
- **Rencanakan akhir masa pakai sejak awal.** Setiap dependensi suatu hari tak lagi dipelihara; ketahui jalan keluar Anda sebelum dipaksa mengambilnya.
- **Di pemerintah, bawaannya terbuka.** Pilih [standar terbuka](https://en.wikipedia.org/wiki/Open_standard) dan sumber terbuka, dan terbitkan kode uang-publik kecuali ada alasan spesifik untuk tidak.

## Rekomendasi

### Tetapkan strategi sumber terbuka dan kebijakan konsumsi

Terbitkan kebijakan jelas tentang bagaimana pengembang boleh membawa sumber terbuka ke organisasi: lisensi mana yang disetujui di muka, mana yang butuh tinjauan, dan mana yang dilarang untuk kasus penggunaan Anda. Sediakan jalur persetujuan cepat dan bergesekan rendah. Kebijakan yang lebih lambat daripada menyalin kode akan sekadar diabaikan. Bedakan konteks, karena lisensi yang sama berperilaku berbeda ketika komponen dipakai secara internal sebagai layanan, ditanam dalam produk terdistribusi, atau ditautkan ke aplikasi proprietari. Jadikan jalur mudah sebagai jalur patuh: repositori internal terkurasi berisi komponen terperiksa, pemindaian otomatis di pipeline, dan panduan jelas yang dapat diikuti pengembang tanpa menelepon pengacara untuk kasus rutin.

### Kelola kepatuhan lisensi, kewajiban, dan risiko copyleft

Kenali keluarga lisensi dan kewajibannya. [Lisensi permisif](https://en.wikipedia.org/wiki/Permissive_software_license) (seperti MIT, BSD, dan Apache 2.0) terutama mensyaratkan atribusi dan pelestarian pemberitahuan; Apache 2.0 menambah pemberian paten eksplisit. Copyleft lemah (seperti [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) dan MPL) mengharuskan Anda membagikan modifikasi pada berkas yang tercakup tetapi umumnya membiarkan Anda menggabungkan dengan kode proprietari. Copyleft kuat (seperti [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License)) dapat mewajibkan seluruh karya terdistribusi ditawarkan dengan ketentuan sama. Copyleft jaringan ([AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)) memperluas kewajiban itu ke perangkat lunak yang ditawarkan lewat jaringan, bukan hanya didistribusikan sebagai biner. Kewajiban yang paling penting bergantung pada dua hal: apakah Anda mendistribusikan perangkat lunak, dan seberapa erat Anda menggabungkan komponen. Otomatiskan kepatuhan: pindai dependensi untuk lisensi, hasilkan dan kirim berkas atribusi dan pemberitahuan yang disyaratkan, dan gerbangi build pada kebijakan agar lisensi terlarang tidak dapat diam-diam masuk ke produksi.

### Dirikan Open Source Program Office (OSPO)

Jika Anda mengonsumsi sumber terbuka pada skala besar, ciptakan titik fokus, OSPO, yang memiliki strategi sumber terbuka, kebijakan, perkakas kepatuhan, tata kelola kontribusi, dan hubungan komunitas. OSPO menekan kekacauan setiap tim membuat keputusannya sendiri. Ia menyediakan keahlian yang tak dapat dipelihara tim individual. Dan ia menangkap nilai strategis: memutuskan proyek mana untuk diinvestasikan, kapan berkontribusi ke hulu, dan bagaimana merilis proyek sumber terbuka Anda sendiri dengan baik. Bahkan OSPO kecil (kadang satu orang plus kelompok kerja lintas fungsi) secara dramatis memperbaiki konsistensi dan mengurangi risiko hukum dibanding bebas-semua.

### Atur kontribusi dan, di mana cocok, penerbitan

Putuskan dengan sengaja kapan berkontribusi kembali. Mengirim perbaikan dan fitur ke hulu pada proyek yang Anda andalkan mengurangi beban pemeliharaan Anda, karena Anda berhenti membawa tambalan pribadi. Ia juga membangun niat baik dan pengaruh, dan memperkuat komponen yang kritis bagi Anda. Beri pengembang proses jelas dan cepat untuk kontribusi yang disetujui, termasuk bagaimana kekayaan intelektual dan perjanjian kontributor ditangani. Ketika Anda merilis proyek sumber terbuka sendiri, lakukan dengan benar: pilih lisensi yang tepat, dokumentasikan tata kelola, dan berkomitmen pada kepengurusan. Proyek terlantar merugikan reputasi Anda lebih daripada tanpa proyek.

### Penuhi mandat sumber terbuka pemerintah dan "uang publik, kode publik"

Tim sektor publik harus memperlakukan keterbukaan sebagai bawaan. Pilih standar terbuka untuk menghindari lock-in dan bekerja lintas lembaga serta vendor. Terbitkan kode sumber yang dikembangkan dengan dana publik secara terbuka, kecuali pengecualian spesifik dan terdokumentasi berlaku: untuk komponen sensitif keamanan, hak pihak ketiga, atau kekhawatiran privasi. Pakai ulang sebelum membangun: periksa apakah lembaga lain sudah merilis kode yang cocok. Tanamkan ekspektasi ini ke pengadaan, agar vendor menyerahkan kode terbuka, dapat dipakai ulang, dan terdokumentasi baik dengan pemerintah mempertahankan hak yang sesuai, alih-alih kotak hitam proprietari yang tak dapat dipelihara atau dibagikan lembaga.

### Kelola dependensi dan perangkat lunak akhir masa pakai

Pelihara inventaris hidup (SBOM) setiap komponen beserta versi, lisensi, dan status pemeliharaannya. Jaga dependensi cukup mutakhir. Pembaruan kecil dan sering jauh lebih murah dan aman daripada lompatan besar yang jarang. Awasi proyek hulu untuk pengumuman akhir masa pakai dan jendela dukungan keamanan, dan rencanakan migrasi sebelum dukungan berakhir, bukan setelah kerentanan memaksa kerepotan. Untuk komponen kritis yang berisiko ditinggalkan, putuskan di muka apakah Anda akan mendanai pemelihara, menyumbang pemeliharaan sendiri, fork, atau mengganti. Lacak akhir masa pakai untuk perangkat lunak komersial dan sumber terbuka sama-sama, dan pegang kehabisan dukungan pada standar yang sama seperti risiko operasional lain.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan |
|---|---|---|
| Konsumsi sumber terbuka bebas | Pengiriman cepat; daya ungkit besar; tanpa biaya lisensi | Kewajiban lisensi, keamanan, dan pemeliharaan yang kini Anda miliki |
| Daftar izin lisensi ketat | Risiko hukum rendah; dapat diprediksi | Memperlambat tim; mungkin mengecualikan komponen yang benar-benar berguna |
| Hanya lisensi permisif | Kewajiban minimal; mudah digabung | Melepas proyek copyleft berharga; resiprositas lebih sedikit |
| Terima copyleft di mana cocok | Akses ke ekosistem kuat; manfaat resiprositas | Membutuhkan kehati-hatian dalam penggabungan dan distribusi |
| Berkontribusi ke hulu | Beban tambalan pribadi lebih sedikit; pengaruh; niat baik | Upaya berkelanjutan; overhead IP dan proses |
| Bangun proprietari sebagai gantinya | Kendali penuh; tanpa kewajiban eksternal | Biaya tinggi; menciptakan ulang komoditas; Anda memeliharanya selamanya |
| Pemerintah terbitkan-secara-bawaan | Transparansi; pemakaian ulang; menghindari lock-in | Upaya penerbitan; tinjauan keamanan; kepengurusan berkelanjutan |

Ketegangan sentralnya antara kecepatan pengembang dan kendali. Kunci segalanya di balik tinjauan berat, dan pengembang mengakali kebijakan. Itu menciptakan dependensi bayangan tak terkelola, yang lebih buruk daripada pendekatan permisif-tetapi-terlihat. Biarkan sepenuhnya tak terkendali, dan Anda mengumpulkan utang hukum dan keamanan secara tak terlihat. Resolusinya otomasi dan kurasi: jadikan jalur patuh sebagai jalur tercepat, lewat komponen terperiksa, pemindaian pipeline, dan bawaan jelas, agar Anda mendapat kendali tanpa gesekan. Soal copyleft, trade-off-nya bukan "berisiko versus aman" tetapi "dipahami versus tidak." Copyleft sepenuhnya dapat dipakai begitu Anda tahu bagaimana Anda menggabungkan dan mendistribusikan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa aturan eksplisit Anda untuk copyleft kuat dan jaringan di konteks internal, terdistribusi, dan dilayani-jaringan?** Copyleft adalah kendala desain, bukan tabu, dan kewajiban bergantung pada dua hal: apakah Anda mendistribusikan perangkat lunak dan seberapa erat Anda menggabungkan komponen. GPL dalam perkakas internal berperilaku sangat berbeda dari GPL yang ditautkan ke produk yang Anda kirim, dan AGPL memperluas kewajiban pengungkapan ke perangkat lunak yang Anda tawarkan hanya lewat jaringan, yang mengubah perhitungan bangun-versus-adopsi Anda untuk apa pun yang Anda jalankan sebagai layanan. Tuliskan aturan per konteks, agar pengembang tahu tanpa menelepon pengacara bahwa (misalnya) permisif disetujui di muka di mana-mana, copyleft kuat tak masalah secara internal tetapi diblokir dari produk terkirim, dan AGPL butuh tinjauan sebelum menyentuh layanan berjaringan. Bawa bukti: pindai pohon dependensi Anda saat ini dan temukan di mana komponen copyleft sudah berada relatif terhadap batas distribusi Anda. Lalu gerbangi build pada kebijakan itu, karena aturan yang tak ditegakkan pemindai mana pun adalah aturan yang akan dilanggar pengembang secara tak sengaja.

2. **Apakah Anda butuh Open Source Program Office, dan siapa yang memiliki kebijakan lisensi, pemindaian, dan keputusan kontribusi hari ini?** Jika jawaban jujurnya "tak ada" atau "setiap tim memutuskan," Anda menjalankan bebas-semua yang mengumpulkan utang hukum dan keamanan secara tak terlihat. OSPO, bahkan satu orang plus kelompok kerja lintas fungsi, menekan kekacauan itu dan menangkap nilai strategis: proyek hulu mana untuk diinvestasikan, kapan berkontribusi, dan bagaimana merilis proyek Anda sendiri dengan baik. Bawa bukti ke rapat: dapatkah ada yang menghasilkan daftar lisensi yang disetujui saat ini, SBOM, dan nama orang yang akan menjawab pertanyaan copyleft selama uji tuntas akuisisi? Jawabannya harus menetapkan kepemilikan jelas dan menjadikan jalur patuh sebagai jalur tercepat, lewat komponen terperiksa dan pemindaian pipeline, agar pengembang mendapat kendali tanpa gesekan. Kebijakan yang lebih lambat daripada menyalin kode akan sekadar diabaikan.

3. **Dependensi mana yang paling menyakitkan jika ditinggalkan besok, dan apa respons yang diputuskan di muka untuk masing-masing?** Setiap dependensi akhirnya mencapai akhir masa pakai, dan versi mahal dari peristiwa itu adalah menemukan komponen inti kehilangan dukungan berbulan-bulan lalu, hanya ketika kerentanan memaksa perhatian. Untuk komponen kritis Anda yang berisiko ditinggalkan, putuskan di muka apakah Anda akan mendanai pemelihara, menyumbang pemeliharaan sendiri, fork, atau mengganti. Bawa bukti: dari SBOM Anda, daftarkan komponen yang kegagalannya akan menghentikan layanan kritis pendapatan atau misi, dan catat status pemeliharaan serta jendela dukungan keamanan masing-masing. Jawabannya harus mengubah akhir masa pakai dari kejutan menjadi risiko operasional terlacak dengan migrasi terencana, dipegang pada standar sama seperti risiko lain. Menjaga dependensi mutakhir dalam langkah kecil dan sering jauh lebih murah daripada lompatan besar yang jarang dan dipaksa.

4. **Dapatkah Anda menghasilkan SBOM lengkap dan mutakhir yang menjangkau seluruh pohon dependensi transitif Anda, dan secepat apa?** Ketika kerentanan berita utama mendarat di pustaka yang banyak dipakai, pertanyaan pertama pimpinan adalah "apakah kita terpapar, dan di mana?" Tim yang tak dapat menjawab dalam hitungan jam sudah tertinggal, karena risiko nyata biasanya bersembunyi beberapa lapis dalam di dependensi yang tak dipilih siapa pun dengan sengaja. Pertimbangan yang bersaing adalah biaya dan derau: inventaris transitif penuh di banyak layanan menghasilkan daftar besar yang terus berubah, dan peringatan berlebih melatih orang mengabaikannya, jadi Anda harus memutuskan kedalaman dan keparahan apa yang benar-benar memicu tindakan. Bawa bukti ke diskusi: coba hasilkan SBOM segar untuk satu layanan produksi sekarang, hitung berapa banyak komponen langsung versus transitif, dan ukur berapa lama. Untuk badan enterprise atau pemerintah, kaitkan ini dengan target respons insiden konkret dan dengan kewajiban regulasi apa pun untuk mengungkap komponen terdampak, karena mandat melaporkan paparan yang tak dapat Anda enumerasi adalah mandat yang akan Anda langgar.

5. **Kapan dependensi kritis layak didanai, dikontribusi, atau dirawat, alih-alih diperlakukan sebagai gratis?** Sebagian besar organisasi mengonsumsi sumber terbuka seolah utilitas, lalu terkejut ketika komponen yang menopang layanan pendapatan ternyata satu sukarelawan tak dibayar. Memutuskan dengan sengaja untuk mendanai pemelihara, mengirim perbaikan ke hulu, atau merilis dan merawat proyek Anda sendiri mengubah masukan gratis yang rapuh menjadi yang tahan lama dan terpengaruhi, dan menghentikan insinyur Anda membawa tambalan pribadi melalui setiap peningkatan. Ketegangannya adalah kontribusi dan kepengurusan berbiaya waktu rekayasa nyata dan berkelanjutan serta membawa overhead kekayaan intelektual dan proses, sehingga Anda tak dapat melakukannya untuk segalanya. Bawa bukti: dari SBOM Anda, tandai segelintir komponen yang kegagalannya akan menghentikan layanan kritis misi, dan catat jumlah pemelihara, pendanaan, dan berapa tambalan pribadi yang sudah Anda bawa terhadap masing-masing. Untuk organisasi besar atau publik, timbang biaya reputasi rilis sumber terbuka terlantar yang Anda terbitkan dengan gembar-gembor, dan, di pemerintah, perlakukan kepengurusan berkelanjutan atas kode uang-publik terbitan sebagai bagian penyampaian, bukan tambahan opsional.

6. **Apakah pengadaan Anda benar-benar menyerahkan kode terbuka, dapat dipakai ulang, dan terdokumentasi baik dengan hak yang Anda butuhkan, atau kotak hitam proprietari yang tak dapat Anda pelihara atau tinggalkan?** Kontrak yang ditulis tanpa keahlian sumber terbuka rutin menyerahkan kendali kepada vendor yang akan Anda sesali: format tertutup, tanpa hak menerbitkan atau memodifikasi, dan dependensi yang tak dapat ditambal lembaga ketika vendor pergi. Menata ini dengan benar sejak dini jauh lebih murah daripada menemukan saat perpanjangan bahwa Anda tak dapat pergi. Pertimbangan yang bersaing adalah kecepatan dan pilihan vendor: menuntut penyerahan terbuka dan portabilitas dapat mempersempit bidang dan memperlambat penghargaan, dan sebagian pemasok yang benar-benar berguna menolaknya. Bawa bukti: tarik dua kontrak terbaru dan periksa apakah mereka menspesifikasikan ketentuan lisensi, penyerahan kode sumber, standar dokumentasi, penyediaan SBOM, dan hak yang dipertahankan organisasi. Untuk pengadaan enterprise, hubungkan ini dengan analisis lock-in dan total biaya; untuk pemerintah, hubungkan dengan mandat terbuka-secara-bawaan dan "uang publik, kode publik," dan dengan proses pengecualian terdokumentasi yang memungkinkan Anda menutup hanya bagian sensitif keamanan alih-alih seluruh sistem.

## Lensa sektor

**Startup.** Anda merakit hampir semuanya dari sumber terbuka dan tak punya pengacara, jadi jaga aturan satu halaman: lisensi permisif seperti MIT dan Apache 2.0 disetujui di muka, copyleft kuat tak masalah untuk perkakas internal tetapi diblokir dari produk terkirim, dan apa pun yang aneh mendapat tinjauan cepat pendiri. Tambahkan pemindaian lisensi dan kerentanan ke pipeline dan simpan SBOM sejak hari pertama, karena saat termurah menata ini dengan benar adalah sebelum uji tuntas pengakuisisi menyisir pohon dependensi Anda. Jangan melarang copyleft karena takut; pahami, lalu lanjutkan.

**Bisnis kecil.** Tanpa spesialis sumber terbuka dan anggaran ketat, bersandarlah pada perkakas alih-alih headcount: pemindai di build dan daftar lisensi disetujui yang pendek melakukan sebagian besar pekerjaan yang dilakukan seseorang. Bingkai konsumsi sebagai beli-versus-bangun dengan jujur, karena menciptakan ulang komponen terbuka yang terpelihara baik biasanya pilihan mahal, tetapi begitu juga bergantung pada satu yang tak pernah Anda inventarisasi. Simpan catatan sederhana apa yang Anda pakai dan di bawah lisensi apa, agar kuesioner keamanan pelanggan atau peringatan kerentanan tidak menjadi kerepotan.

**Enterprise.** Pada skala besar masalahnya konsistensi lintas banyak tim, jadi dirikan OSPO untuk memiliki kebijakan, pemindaian otomatis, pembuatan atribusi, dan tata kelola kontribusi, dan jadikan jalur patuh sebagai jalur tercepat lewat komponen terkurasi dan terperiksa. Tegakkan aturan copyleft per konteks di pipeline, pelihara SBOM di seluruh layanan, dan kelola kemutakhiran dependensi dan akhir masa pakai sebagai risiko operasional terlacak. Perlakukan sumber terbuka sebagai manajemen rantai pasok untuk mayoritas basis kode Anda, dengan bukti siap audit untuk uji tuntas akuisisi.

**Pemerintah.** Keterbukaan sering diwajibkan, bukan opsional, jadi pilih standar terbuka sebagai bawaan dan terbitkan kode uang-publik kecuali pengecualian terdokumentasi berlaku untuk keamanan, hak pihak ketiga, atau privasi. Pakai ulang sebelum membangun dengan memeriksa katalog lintas pemerintah, dan tanamkan penyerahan terbuka, dapat dipakai ulang, terdokumentasi baik serta hak yang dipertahankan ke pengadaan agar Anda menerima kode yang dapat dipelihara alih-alih kotak hitam proprietari. Pegang kode terbitan pada kepengurusan nyata, dan jaga proses pengecualian sempit dan transparan agar ia menutup hanya yang harus.

## Contoh

**Startup.** Startup empat orang yang membangun aplikasi seluler merakit hampir semuanya dari sumber terbuka dan tak punya pengacara. Alih-alih melarang copyleft karena takut, para pendiri menulis kebijakan satu halaman: lisensi permisif seperti MIT dan Apache 2.0 disetujui di muka, copyleft kuat seperti GPL tak masalah untuk perkakas internal tetapi diblokir dari aplikasi terkirim untuk menghindari kewajiban pengungkapan, dan apa pun yang tak biasa mendapat tinjauan cepat pendiri. Mereka menambah pemindaian lisensi dan kerentanan ke pipeline agar lisensi terlarang tak dapat menyelinap ke rilis, menyimpan SBOM sejak hari pertama, dan mengirim perbaikan kecil ke pustaka kritis ke hulu agar berhenti membawa tambalan pribadi melalui setiap peningkatan. Menata ini dengan benar sejak dini juga menyelamatkan mereka dari kejutan menyakitkan ketika uji tuntas pengakuisisi akhirnya menyisir pohon dependensi.

**Enterprise.** Sebuah vendor perangkat lunak yang mengirim produk terdistribusi menjalankan OSPO. OSPO memelihara daftar lisensi disetujui, repositori komponen terkurasi internal, dan pemindaian lisensi serta kerentanan otomatis di setiap pipeline. Ketika pengembang menarik dependensi baru, pipeline memeriksa lisensinya terhadap kebijakan, menghasilkan pemberitahuan atribusi yang dikirim bersama produk, dan menandai apa pun yang butuh tinjauan. Komponen copyleft kuat diizinkan untuk perkakas internal tetapi diblokir dari produk terdistribusi, untuk menghindari kewajiban pengungkapan. Perusahaan mengirim perbaikan ke hulu untuk beberapa dependensi kritis. Itu menghapus tumpukan tambalan pribadi yang dulu dibawa insinyurnya melalui setiap peningkatan.

**Pemerintah.** Sebuah layanan digital nasional beroperasi di bawah kebijakan "uang publik, kode publik." Layanan baru dibangun di atas standar terbuka, dikembangkan secara terbuka di repositori kode publik secara bawaan, dan dipakai ulang lintas lembaga. Templat pengadaannya mewajibkan vendor menyerahkan kode terbuka, terdokumentasi baik, dan dapat dipakai ulang, dengan pemerintah mempertahankan hak menerbitkan dan memodifikasi. Sebelum memulai komponen baru, tim mencari di katalog lintas pemerintah untuk kode yang dapat dipakai ulang yang sudah ada. Modul sensitif keamanan dikecualikan dari penerbitan lewat proses terdokumentasi, bukan dengan membuat seluruh sistem tertutup.

## Kasus bisnis: motivasi, ROI, dan TCO

Mengelola sumber terbuka dengan baik adalah beda antara menangkap daya ungkitnya yang besar dan membayar biaya tersembunyinya. Sumber terbuka memungkinkan organisasi besar berdiri di atas fondasi yang tak pernah mampu dibangunnya. Tetapi [total biaya kepemilikan](https://en.wikipedia.org/wiki/Total_cost_of_ownership) mencakup kepatuhan, penambalan keamanan, dan migrasi akhirnya, biaya yang tiba terlepas dari apakah Anda merencanakannya. Pengelolaan yang disengaja mengubah krisis tak terprediksi dan mahal menjadi biaya kecil, stabil, dan terencana. Krisis itu mencakup pelanggaran copyleft yang ditemukan selama uji tuntas akuisisi, migrasi darurat dari komponen terlantar, atau kerentanan dalam dependensi yang tak diketahui siapa pun ada.

Biaya adopsi sederhana dibanding paparan: OSPO atau kelompok kerja, perkakas pemindaian, dan disiplin menjaga inventaris. Biaya *tidak* mengadopsi tampak sebagai liabilitas hukum, uji tuntas gagal, insiden keamanan yang ditelusuri ke dependensi tak ditambal, dan biaya bertambah dari peningkatan yang ditunda yang akhirnya memaksa migrasi big-bang menyakitkan. Ketika Anda mengajukan kasus kepada pimpinan, bingkai manajemen sumber terbuka sebagai manajemen rantai pasok untuk mayoritas basis kode Anda. Catat juga sisi positif strategis: lock-in yang dihindari, pengiriman lebih cepat, daya tarik talenta, dan pengaruh atas ekosistem yang Anda andalkan. Di pemerintah, tambahkan dimensi mandat. Keterbukaan sering diwajibkan, bukan opsional, dan melakukannya dengan baik menghindari ketidakpatuhan dan pengeluaran publik terduplikasi.

## Anti-pola dan jebakan

- **Pelisensian salin-tempel.** Pengembang menarik komponen tanpa pemeriksaan lisensi, menemukan kewajiban hanya saat audit atau akuisisi.
- **Tanpa inventaris.** Tak mampu menjawab "apa yang kita pakai dan di bawah lisensi apa?" ketika pertanyaan kerentanan atau lisensi muncul.
- **Kepanikan copyleft.** Melarang semua copyleft karena takut alih-alih memahami, melepas ekosistem berharga.
- **Rilis sumber terbuka terlantar.** Menerbitkan proyek dengan gembar-gembor lalu tak pernah memeliharanya, merusak reputasi.
- **Mengabaikan dependensi transitif.** Memeriksa dependensi langsung sementara risiko nyata bersembunyi beberapa lapis dalam.
- **Kejutan akhir masa pakai.** Menemukan komponen inti kehilangan dukungan berbulan-bulan lalu, hanya ketika kerentanan memaksa perhatian.
- **Kebijakan lebih lambat daripada menyalin.** Proses kepatuhan begitu berat sehingga pengembang mengakalinya, menciptakan dependensi bayangan tak terlihat.
- **Kotak hitam pemerintah.** Mengadakan sistem proprietari yang tak dapat dipelihara, dibagikan, atau ditinggalkan lembaga, melanggar prinsip terbuka-secara-bawaan.

## Model kematangan

**Tingkat 1: Memulai.** Pengembang menambah sumber terbuka bebas tanpa kebijakan atau inventaris. Lisensi tak diperiksa dan kewajiban copyleft tak diketahui. Akhir masa pakai ditemukan secara kebetulan, biasanya ketika kerentanan memaksa perhatian. Tak ada yang memiliki strategi sumber terbuka.

**Tingkat 2: Mengembangkan.** Kebijakan dasar dan daftar lisensi disetujui ada, dan sebagian tim mengikutinya. Pemindaian terjadi, tetapi sering manual, terlambat, atau hanya pada beberapa proyek. Inventaris disimpan untuk sistem utama sementara dependensi transitif tak dipetakan. Kontribusi dan penanganan akhir masa pakai ad hoc dan tidak konsisten antartim.

**Tingkat 3: Membakukan.** OSPO atau setara memiliki strategi, kebijakan, dan perkakas di seluruh organisasi. Pemindaian lisensi dan kerentanan otomatis di setiap pipeline, berkas atribusi dan pemberitahuan dihasilkan otomatis, dan build digerbangi sehingga lisensi terlarang tak dapat masuk. SBOM dipelihara hingga pohon transitif, kontribusi mengikuti proses terdokumentasi, akhir masa pakai dilacak dengan migrasi terencana, dan tim pemerintah menerbitkan secara bawaan.

**Tingkat 4: Mengelola.** Program diukur dan dikendalikan terhadap garis dasar. Anda melacak cakupan pemindaian kebijakan di seluruh layanan, mean time untuk menambal kerentanan dependensi yang diungkap, pangsa komponen di dalam jendela dukungan keamanannya, tingkat lolos pelanggaran lisensi, lag kemutakhiran dependensi, dan jumlah tambalan pribadi yang dibawa ke hulu. Penempatan copyleft relatif terhadap batas distribusi dipantau, dan metrik terhadap target menggerakkan setiap keputusan go atau no-go alih-alih opini.

**Tingkat 5: Mengorkestrasi.** Sumber terbuka adalah aset strategis yang terus diperbaiki dan terintegrasi di seluruh organisasi. Kepatuhan sepenuhnya otomatis dan komponen tak patuh tak dapat mencapai produksi. Anda berinvestasi dengan sengaja pada proyek hulu kritis, berkontribusi rutin, dan merawat proyek Anda sendiri yang dijalankan baik. Kemutakhiran dependensi dan akhir masa pakai dikelola secara adaptif seiring risiko dan metrik bergeser, dan keterbukaan menjadi keunggulan kompetitif dan sipil sejati.

## Gagasan untuk didiskusikan

- Di mana garis yang tepat antara bawaan permisif cepat dan kendali yang dibutuhkan untuk menghindari utang hukum dan keamanan?
- Kapan organisasi harus mendanai atau memelihara dependensi hulu kritis alih-alih memperlakukannya gratis?
- Bagaimana Anda memutuskan komponen Anda sendiri mana yang layak dirilis dan dirawat sebagai sumber terbuka?
- Untuk pemerintah, apa proses yang dapat dipertahankan untuk mengecualikan komponen dari terbitkan-secara-bawaan tanpa mengikis prinsipnya?
- Seberapa dalam ke dependensi transitif tinjauan lisensi dan keamanan harus berjalan secara realistis?
- Apakah copyleft jaringan (AGPL) mengubah perhitungan bangun-versus-adopsi Anda untuk perangkat lunak yang Anda tawarkan sebagai layanan?

## Poin-poin utama

- Sumber terbuka adalah mayoritas sebagian besar basis kode dan harus dikelola sebagai rantai pasok, bukan diperlakukan gratis dan tanpa konsekuensi.
- Lisensi membawa kewajiban nyata; pahami keluarga permisif, copyleft lemah, copyleft kuat, dan copyleft jaringan serta bagaimana distribusi dan penggabungan memicu kewajiban.
- Jadikan jalur patuh sebagai jalur tercepat lewat kurasi, pemindaian otomatis, dan bawaan jelas, atau pengembang akan mengakali kebijakan.
- Dirikan OSPO untuk memiliki strategi, kepatuhan, kontribusi, dan kepengurusan pada skala besar.
- Pelihara SBOM, jaga dependensi mutakhir dalam langkah kecil, dan rencanakan akhir masa pakai sebelum ia memaksa krisis.
- Di pemerintah, pilih standar terbuka sebagai bawaan dan terbitkan kode uang-publik, pakai ulang sebelum membangun.

## Referensi dan bacaan lanjutan

- Heather Meeker, *Open (Source) for Business* dan *Open Source for Business*
- Van Lindberg, *Intellectual Property and Open Source*
- The Linux Foundation dan TODO Group, *OSPO guides* dan *Open Source Program Office resources*
- OpenChain (ISO/IEC 5230), *Open Source Licence Compliance*
- Spesifikasi Software Package Data Exchange (SPDX, ISO/IEC 5962)
- Spesifikasi SBOM CycloneDX
- Free Software Foundation, *GNU General Public Licence* dan *GPL FAQ*
- Open Source Initiative, *The Open Source Definition* dan daftar lisensi yang disetujui
- Free Software Foundation Europe, *Public Money, Public Code*
- U.S. Federal Source Code Policy dan panduan Code.gov
- UK Government, *Technology Code of Practice* dan prinsip standar terbuka
