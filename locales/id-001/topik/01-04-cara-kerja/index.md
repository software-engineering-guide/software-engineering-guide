# 1.4 Cara kerja

## Tinjauan dan motivasi

"Cara kerja" menggambarkan bagaimana tim Anda sebenarnya berkoordinasi, merencanakan, berkomunikasi, dan menyerahkan hasil sehari-hari. Bagaimana pekerjaan dipecah? Siapa berbicara dengan siapa, dan kapan? Bagaimana kemajuan dilacak, dan bagaimana keputusan serta pengetahuan mengalir?

Sebagian besar organisasi mengadopsi metodologi bernama, [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), atau kerangka penskalaan tertentu, dan mengira upacaranya sama dengan nilai di baliknya. Keduanya tidak sama. Metodologi yang mengubah pengiriman perangkat lunak lahir sebagai reaksi terhadap proses yang berat dan digerakkan serah terima. Tujuannya adalah umpan balik cepat, batch kecil, dan tim yang diberdayakan. Adopsi hanya ritualnya, standup, sprint, story point, tanpa prinsipnya, dan Anda mendapat biaya proses tanpa manfaatnya: agile ala [kultus kargo](https://en.wikipedia.org/wiki/Cargo_cult).

Bagi tim besar, di sinilah niat baik berhasil atau gagal. Seribu insinyur tidak dapat semuanya berada di satu ruangan, menghadiri rapat yang sama, atau berbagi konteks tersirat yang sama. Semakin besar Anda, semakin Anda harus bersandar pada komunikasi tertulis, kolaborasi asinkron, dan koordinasi ringan alih-alih rapat dan obrolan di lorong. Skala mengubah fisikanya. Praktik yang bekerja indah untuk delapan orang yang sekantor dapat runtuh untuk delapan puluh orang yang tersebar. Dan kerangka penskalaan yang menjanjikan perbaikan sering memperkenalkan kembali serah terima dan sentralisasi yang justru hendak dihapus oleh [agile](https://en.wikipedia.org/wiki/Agile_software_development).

Enterprise dan pemerintah merasakan setiap tekanan ini dengan kekuatan penuh. Mereka melintasi banyak zona waktu, mencampur staf tetap dengan kontraktor dan vendor, dan sering membawa gerbang tahap dan pelaporan yang diwajibkan. Di sini, cara kerja yang mengutamakan dokumen, asinkron, dan berfokus pada hasil bukanlah kemewahan. Itulah satu-satunya yang dapat diskalakan. Rekomendasi di bawah ini lebih memilih menyesuaikan prinsip dengan konteks daripada mengimpor kerangka secara bulat-bulat, dan lebih memilih praktik tertulis, asinkron, dan transparan yang memungkinkan tenaga kerja besar, tersebar, dan campuran benar-benar berkolaborasi.

## Prinsip utama

- Adopsi prinsip, bukan ritual; pahami mengapa sebuah praktik ada sebelum menirunya.
- Batch kecil dan umpan balik cepat mengalahkan rencana besar dan siklus panjang.
- Pilih aliran (membatasi pekerjaan dalam proses) daripada pembatasan waktu yang kaku bila cocok.
- Estimasi untuk memungkinkan percakapan dan perencanaan, bukan untuk memproduksi presisi palsu.
- Jadikan komunikasi asinkron dan tertulis sebagai bawaan; sisakan waktu sinkron untuk yang benar-benar membutuhkannya.
- Buat pekerjaan dan keputusan terlihat dan terdokumentasi agar siapa pun dapat menyusul tanpa rapat.
- Optimalkan hasil yang dikirim, bukan aktivitas yang dilakukan atau kapasitas yang dimanfaatkan.

## Rekomendasi

### Sesuaikan Agile, Scrum, Kanban, dan Lean dengan konteks

Perlakukan ini sebagai kotak perkakas, bukan agama. Sprint Scrum yang dibatasi waktu cocok untuk tim dengan pekerjaan penemuan yang diuntungkan oleh irama perencanaan dan tinjauan yang teratur. Aliran kontinu Kanban dan batas pekerjaan-dalam-proses yang eksplisit cocok untuk tim dengan pekerjaan yang tak terduga dan digerakkan interupsi seperti platform dan operasi. Fokus [Lean](https://en.wikipedia.org/wiki/Lean_software_development) pada menghilangkan pemborosan dan memperpendek lead time menopang keduanya. Pilihlah dengan sengaja. Campurlah bila membantu; banyak tim menjalankan "[Scrumban](https://en.wikipedia.org/wiki/Scrumban)." Pertahankan praktik yang menciptakan nilai, dan buang upacara yang telah menjadi ritual kosong. Ujian untuk praktik apa pun sederhana. Apakah ia memperpendek umpan balik, mengurangi ukuran batch, atau meningkatkan kejelasan? Jika tidak, pertanyakan.

### Skalakan dengan hati-hati, bukan kultus kargo

Kerangka penskalaan, [SAFe](https://en.wikipedia.org/wiki/Scaled_agile_framework) (Scaled Agile Framework), LeSS (Large-Scale Scrum), "model Spotify" yang dipopulerkan, menjanjikan koordinasi banyak tim. Dekati dengan mata skeptis. SAFe membawa struktur dan sering dipilih enterprise besar dan pemerintah karena kelengkapannya dan ekosistem pelatihannya, tetapi dapat memperkenalkan kembali perencanaan berat, hierarki, dan serah terima yang melemahkan ketangkasan. LeSS tetap lebih dekat dengan prinsip lean, tetapi menuntut perubahan organisasi yang nyata. "Model" Spotify adalah potret budaya yang berkembang dari satu perusahaan, bukan templat, dan Spotify sendiri tidak menjalankannya seperti yang dibayangkan orang. Pilih menskalakan dengan mengurangi kebutuhan akan koordinasi, melalui topologi tim di bab sebelumnya, alih-alih memasang kerangka koordinasi pada struktur yang terpecah.

### Estimasi dengan jujur dan ringan

Story point dan velocity membantu tim Anda merencanakan pekerjaannya sendiri dalam waktu dekat dan membicarakan kompleksitas relatif. Keduanya bukan metrik produktivitas, mata uang lintas tim, atau janji. Jangan pernah menjadikan velocity target: ia akan dipermainkan lewat inflasi poin. Untuk perkiraan jangka lebih panjang, pilih menghitung throughput dan memakai data cycle time historis, yang sering lebih akurat daripada menjumlahkan estimasi. Banyak tim matang memangkas beban estimasi dengan memecah pekerjaan menjadi potongan kecil yang serupa dan sekadar menghitungnya. Apa pun metodenya, ingat bahwa estimasi adalah perkiraan di bawah ketidakpastian, bukan komitmen. Sampaikan sebagai rentang.

### Jadikan komunikasi asinkron dan mengutamakan dokumen sebagai bawaan

Dalam organisasi besar yang tersebar, rapat sinkron tidak dapat diskalakan, dan mengucilkan orang di zona waktu lain. Jadikan menulis sebagai bawaan: dokumen desain, [catatan keputusan](https://en.wikipedia.org/wiki/Architectural_decision), pembaruan status tertulis, dan tiket menyeluruh yang membawa cukup konteks untuk ditindaklanjuti tanpa percakapan langsung. Rekam dan ringkas rapat yang tidak dapat dihindari. Budaya mengutamakan dokumen memungkinkan seseorang di zona waktu lain berkontribusi penuh, memungkinkan anggota baru dan kontraktor beradaptasi dengan membaca, dan meninggalkan catatan yang tahan lama. Sisakan waktu sinkron untuk kolaborasi yang sejati, membangun hubungan, dan menjernihkan ambiguitas dengan cepat. Lindungi blok besar waktu fokus dari fragmentasi rapat.

### Bekerja dengan baik lintas zona waktu, kontraktor, dan vendor

Tenaga kerja yang tersebar dan campuran adalah norma pada skala besar. Rancang untuk "[follow-the-sun](https://en.wikipedia.org/wiki/Follow-the-sun)," di mana serah terima bersifat tertulis dan lengkap, bukan lisan. Tetapkan beberapa jam inti yang tumpang-tindih untuk kontak sinkron yang Anda butuhkan, dan bagi ketidaknyamanan jam rapat secara adil alih-alih selalu membebani wilayah yang sama. Untuk kontraktor dan vendor, investasikan lebih pada konteks tertulis, antarmuka yang jelas, dan perkakas bersama, karena mereka tidak memiliki pengetahuan tersirat yang dikumpulkan staf tetap Anda. Bawa vendor ke papan dan dokumentasi terlihat yang sama alih-alih mengelola mereka lewat kanal terpisah yang buram. Bila bisa, susun kontrak di sekitar hasil, bukan jam.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
| --- | --- | --- |
| Agile (interaksi pemangku kepentingan) | Kolaborasi tinggi dan nilai tercepat | Membutuhkan kepercayaan dan fleksibilitas |
| Scrum (sprint berbatas waktu) | Irama teratur, ritme dapat diprediksi, refleksi bawaan | Beban upacara; kurang cocok untuk pekerjaan digerakkan interupsi |
| Kanban (aliran kontinu, batas WIP) | Fleksibel, mengungkap hambatan, bagus untuk ops | Kurang berirama; butuh disiplin membatasi WIP |
| SAFe / kerangka penskalaan berat | Struktur, pelatihan, akrab bagi organisasi besar dan pemerintah | Memperkenalkan kembali hierarki dan serah terima; dapat mencekik ketangkasan |
| LeSS / penskalaan ringan | Tetap dekat dengan prinsip lean | Menuntut perubahan organisasi mendalam |
| Asinkron / mengutamakan dokumen | Skalabel lintas zona waktu; tahan lama; inklusif | Lebih lambat untuk topik ambigu; butuh disiplin menulis |

Trade-off menyeluruhnya adalah koordinasi versus otonomi, dan struktur versus kemampuan beradaptasi. Lebih banyak kerangka dan koordinasi sinkron membeli prediktabilitas dan keselarasan, dengan biaya kecepatan, beban, dan pemberdayaan tim. Lebih sedikit kerangka membeli kecepatan dan kepemilikan, dengan biaya kemungkinan ketidakselarasan di antara banyak tim. Bagi sebagian besar organisasi besar, jawaban terbaik adalah irama bersama yang minimal ditambah praktik tertulis yang kuat. Itu mengurangi beban koordinasi pada sumbernya alih-alih mengelolanya dengan proses yang lebih berat.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Jika pimpinan menginginkan prediktabilitas yang dijanjikan kerangka penskalaan, bagaimana Anda memberikannya tanpa memperkenalkan kembali serah terima yang dimaksudkan agile untuk dihapus?** Enterprise besar dan program pemerintah sering mewajibkan perencanaan big-room ala SAFe dan pelaporan gerbang tahap karena badan pengawas menuntut perkiraan dan koordinasi yang dapat mereka lihat. Pertimbangan yang bersaing itu nyata: pimpinan membutuhkan prediktabilitas dan keselarasan di antara banyak tim, dan kerangka berat membelinya dengan biaya kecepatan, beban, dan serah terima yang justru memperlambat pengiriman. Bawa bukti ke diskusi, seperti berapa banyak minggu kerja yang lenyap ke acara perencanaan dan koordinasi dependensi lintas tim, dan apakah acara itu menghilangkan dependensi atau sekadar memunculkannya. Langkah yang lebih kuat adalah menskalakan dengan mengurangi kebutuhan koordinasi melalui topologi tim, lalu memenuhi pelaporan dari papan hidup dan antarmuka tertulis alih-alih dari maraton perencanaan. Putuskan koordinasi mana yang nyata dan mana yang upacara, dan berikan pimpinan perkiraan yang mereka butuhkan dari data throughput dan cycle time alih-alih dari beban kerangka.

2. **Apa yang akan benar-benar Anda lakukan untuk mencegah velocity diubah menjadi metrik produktivitas lintas tim?** Story point membantu satu tim merencanakan pekerjaannya sendiri dalam waktu dekat, dan menjadi tak berharga begitu dibandingkan antartim atau ditetapkan sebagai target, karena inflasi poin adalah respons yang rasional. Dalam organisasi besar, dorongan untuk menggulung velocity menjadi dasbor yang dibandingkan para eksekutif sangat kuat, dan diam-diam merusak estimasi yang diandalkan tim. Bawa bukti penyimpangan: apakah poin menginflasi dari waktu ke waktu, apakah tim menggelembungkan estimasi, apakah ada yang diberi peringkat berdasarkan velocity? Pilih menghitung throughput dan memakai data cycle time historis untuk perkiraan apa pun yang meninggalkan tim, dan sampaikan estimasi sebagai rentang di bawah ketidakpastian, bukan janji. Jawabannya harus menghasilkan kesepakatan eksplisit bahwa velocity tidak pernah meninggalkan tim, dan bahwa perkiraan lintas tim memakai metrik aliran.

3. **Apa batas konkret Anda untuk "tertulis," dan keputusan mana yang memang masih membutuhkan percakapan sinkron?** Bawaan mengutamakan dokumen adalah hal yang dapat diskalakan lintas zona waktu, kontraktor, dan vendor, dan memerlukan disiplin menulis yang sesungguhnya yang belum dimiliki semua orang. Jadilah spesifik tentang batasnya: apakah tiket membawa cukup konteks untuk ditindaklanjuti tanpa panggilan langsung, apakah keputusan masuk ke catatan yang tahan lama, apakah rapat yang tak terhindarkan direkam dan diringkas? Untuk program enterprise dan pemerintah yang mencampur staf tetap dengan kontraktor yang tidak memiliki pengetahuan tersirat, konteks tertulis adalah yang memungkinkan tenaga kerja campuran dan tersebar berkontribusi penuh. Trade-off-nya, topik ambigu atau kontroversial sering lebih cepat diselesaikan secara sinkron, jadi namai secara eksplisit dan sisakan waktu sinkron yang langka untuknya. Putuskan siapa yang menanggung biaya membangun kebiasaan menulis dan jam rapat yang tidak nyaman, dan bagi biaya itu secara adil alih-alih selalu membebani wilayah yang sama.

4. **Upacara mana dari yang kita jalankan saat ini yang akan bertahan jika masing-masing dinilai murni dari apakah ia memperpendek umpan balik, mengecilkan ukuran batch, atau meningkatkan kejelasan?** Upacara menumpuk diam-diam: standup di sini, sesi refinement di sana, tinjauan dan retro dan acara perencanaan, sampai tim besar menghabiskan lebih banyak minggunya dalam rapat berulang daripada dalam pekerjaan yang dilayani rapat itu. Pertimbangan yang bersaing itu nyata, karena ritual yang terasa seperti beban murni bagi satu orang bisa jadi satu-satunya tempat tim yang tersebar membangun konteks bersama atau memunculkan hambatan. Bawa bukti ke diskusi: total jam rapat berulang per orang per minggu, kehadiran dan keterlibatan dalam tiap upacara, dan keputusan atau sinyal apa yang sebenarnya dihasilkan masing-masing yang tidak mungkin berasal dari pembaruan tertulis. Untuk program enterprise atau pemerintah tempat setiap tim menjalankan irama yang sama yang dipaksakan, biaya majemuknya sangat besar, jadi sepakati ujian eksplisit yang harus dilulusi setiap upacara untuk mempertahankan slotnya, dan bersedialah memotong atau menggabungkan yang bertahan hanya karena kebiasaan.

5. **Ketika pekerjaan macet, apakah kita tahu di mana ia sebenarnya menunggu, dan apakah kita mengelola aliran atau sekadar mengisi staf?** Dalam kebanyakan pekerjaan pengetahuan, sebuah tugas menghabiskan jauh lebih banyak hidupnya menunggu di antrean, serah terima, dan tinjauan daripada dikerjakan secara aktif, namun tim secara naluriah menanggapi pengiriman lambat dengan menambah orang atau mendorong utilisasi lebih tinggi, yang memperpanjang antrean alih-alih memperpendeknya. Ketegangannya adalah membatasi pekerjaan dalam proses terasa seperti membiarkan kapasitas menganggur, dan orang yang tampak menganggur membuat manajer dan badan pengawas gelisah. Bawa bukti yang mengungkap kebenaran: distribusi cycle time, rasio waktu aktif terhadap total lead time, di mana item tersangkut terhambat di papan Anda, dan bagaimana batas pekerjaan-dalam-proses (batas jumlah item yang berjalan sekaligus) mengubah throughput saat Anda menegakkannya. Bagi organisasi besar atau pemerintah yang diukur dari utilisasi staf, ini membingkai ulang target dari menjaga semua orang sibuk menjadi menjaga pekerjaan selesai tetap mengalir, dan pergeseran itu sering menjadi satu-satunya tuas terbesar atas kecepatan pengiriman.

6. **Bagaimana cara kerja kita akan menyerap orang-orang yang bukan staf tetap di zona waktu inti kita, yaitu kontraktor, vendor, dan wilayah yang berselisih banyak jam dari kantor pusat?** Pada skala besar tenaga kerja campuran dan tersebar adalah norma, dan praktik yang disetel untuk tim inti yang sekantor diam-diam mengucilkan semua orang lain: vendor yang dikelola lewat kanal pribadi, kontraktor tanpa konteks tersirat, wilayah yang hari kerjanya tidak pernah tumpang-tindih dengan rapat keputusan. Pertimbangannya saling menarik, karena antarmuka tertulis yang lebih ketat dan serah terima tertulis yang lengkap memerlukan disiplin nyata dan memperlambat koordinasi informal cepat yang dinikmati kelompok sekantor. Bawa bukti seperti siapa yang rutin absen dari rapat tempat keputusan dibuat, seberapa sering wilayah dengan selisih waktu terhambat menunggu serah terima, dan apakah vendor bekerja di papan terlihat yang sama dengan staf atau di jalur terpisah yang buram. Untuk program enterprise dan pemerintah yang mencampur staf tetap, kontraktor, dan vendor di banyak zona waktu di bawah pelaporan yang diwajibkan, perlakukan praktik tertulis, transparan, dan follow-the-sun sebagai garis dasar yang memungkinkan seluruh tenaga kerja berkontribusi, dan bagi beban jam yang tidak nyaman alih-alih selalu memaksakannya pada wilayah yang sama.

## Lensa sektor

**Startup.** Dengan segelintir orang dan runway terbatas, lewati katalog upacara dan jalankan dengan aliran seringan mungkin: papan bersama, pembaruan harian tertulis singkat, dan keputusan tercatat dalam dokumen agar tak seorang pun terhambat menunggu rekan bangun tidur. Jadikan menulis sebagai bawaan sejak hari pertama, karena kebiasaan asinkron jauh lebih murah dibangun pada lima orang daripada ditambal pada lima puluh. Jangan adopsi kerangka penskalaan yang tidak akan Anda butuhkan selama bertahun-tahun; keuntungan Anda adalah hampir tidak ada yang perlu dikoordinasikan, jadi lindungi itu.

**Bisnis kecil.** Tanpa pelatih agile atau manajer pengiriman dan dengan anggaran ketat, pilih praktik siap pakai daripada kerangka yang dibeli dengan biaya pelatihan dan sertifikasi yang tidak dapat Anda benarkan. Pilih satu metodologi yang cocok dengan pekerjaan Anda, Kanban untuk pekerjaan layanan yang digerakkan interupsi atau irama Scrum ringan untuk pekerjaan proyek, dan tahan godaan membeli perkakas berat padahal papan sederhana dan tiket yang jelas sudah cukup. Belanjakan upaya koordinasi Anda yang langka untuk menuliskan hal-hal sehingga tim kecil tidak tersandera ingatan satu orang.

**Enterprise.** Di banyak tim, masalahnya adalah biaya koordinasi dan konsistensi: irama bersama yang minimal, definisi bersama tentang apa arti "tertulis," dan metrik aliran yang dapat digulung tanpa menjadikan velocity target lintas tim. Skalakan dengan mengurangi kebutuhan koordinasi melalui topologi tim alih-alih memasang kerangka yang memperkenalkan kembali serah terima, dan atur cara kerja sebagai sesuatu yang disetel dari bukti, bukan peluncuran sekali jalan. Bakukan antarmuka dan pelaporan agar pengawasan terpenuhi dari papan hidup alih-alih dari maraton perencanaan.

**Pemerintah.** Aturan pengadaan, gerbang tahap yang diwajibkan, dan akuntabilitas publik membentuk setiap pilihan, dan tenaga kerja campuran staf tetap, kontraktor, dan vendor melintasi banyak zona waktu di bawah pelaporan kemajuan yang diwajibkan. Pilih cara kerja yang mengutamakan dokumen dan transparan, tempat setiap pekerjaan membawa konteks tertulis penuh pada papan yang terlihat oleh staf dan vendor sama-sama, sehingga laporan status langsung berasal dari catatan alih-alih dari rapat terpisah. Susun kontrak vendor di sekitar hasil dan visibilitas bersama alih-alih penagihan per jam yang buram, dan perlakukan jejak tertulis yang dapat diaudit sebagai aset kepatuhan, bukan beban.

## Contoh

**Startup.** Sebuah startup delapan orang yang tersebar melewatkan katalog upacara Scrum lengkap dan berjalan dengan papan Kanban bersama ditambah pembaruan harian tertulis singkat di Slack. Karena kedua pendirinya berada di zona waktu berbeda, mereka menjadikan menulis sebagai bawaan sejak hari pertama: setiap keputusan masuk ke dokumen, sehingga tak seorang pun terhambat menunggu yang lain bangun. Ketika kemudian mereka merekrut di zona waktu ketiga, orientasi sebagian besar hanyalah membaca, dan kebiasaan asinkron diskalakan tanpa perubahan. Praktik yang tidak pernah mereka adopsi, rapat status sinkron, adalah yang tidak pernah mereka rindukan.

**Enterprise.** Sebuah bank multinasional meluncurkan kerangka penskalaan di ratusan tim, lengkap dengan perencanaan big-room kuartalan. Keselarasan membaik di atas kertas, tetapi pengiriman melambat. Tim menghabiskan berhari-hari dalam acara perencanaan dan mengoordinasikan dependensi lintas tim yang dimunculkan kerangka tetapi tidak dihapusnya. Bank mengoreksi arah. Ia hanya mempertahankan keselarasan lintas tim ringan yang benar-benar dibutuhkan, menata ulang tim agar memiliki aliran nilainya dari ujung ke ujung, dan memindahkan sebagian besar koordinasi ke antarmuka tertulis dan pembaruan asinkron. Lead time pengiriman turun, dan maraton perencanaan yang melelahkan menyusut menjadi sinkronisasi terfokus yang sesekali.

**Pemerintah.** Sebuah lembaga pemerintah yang menyampaikan layanan warga bekerja dengan staf tetap di satu wilayah dan tim kontraktor di dua wilayah lain, melintasi banyak zona waktu, di bawah pelaporan kemajuan yang diwajibkan. Lembaga itu mengadopsi cara kerja berbasis Kanban yang mengutamakan dokumen. Setiap pekerjaan membawa konteks tertulis penuh pada papan bersama yang terlihat oleh staf dan vendor sama-sama. Serah terima antarwilayah bersifat tertulis dan lengkap. Laporan status yang diwajibkan langsung berasal dari papan alih-alih dari rapat terpisah. Ini memungkinkan tenaga kerja campuran yang tersebar berkolaborasi terus-menerus, memenuhi pelaporan pengawasan sebagai hasil sampingan, dan memangkas ketergantungan lembaga pada rapat lintas zona waktu yang sulit dijadwalkan.

## Kasus bisnis: motivasi, ROI, dan TCO

Argumen ekonominya bertumpu pada efisiensi aliran. Dalam kebanyakan pekerjaan pengetahuan, waktu yang dihabiskan satu unit pekerjaan untuk dikerjakan secara aktif hanyalah sebagian kecil dari total lead time-nya. Sisanya menunggu: di antrean, di rapat, di serah terima, di jeda zona waktu. Cara kerja yang mengecilkan ukuran batch, membatasi pekerjaan dalam proses, dan mengganti hambatan sinkron dengan aliran asinkron tertulis menyerang penantian itu secara langsung. Imbalannya adalah lead time lebih pendek dan throughput lebih tinggi tanpa menambah orang, ditambah lebih sedikit cacat, karena umpan balik tiba lebih cepat selagi konteks masih segar.

Timbang biaya mengadopsi terhadap biaya status quo. Mengutamakan dokumen, asinkron, dan aliran lean terutama menelan perubahan kebiasaan dan sedikit investasi awal pada penulisan dan perkakas. Tidak memerlukan lisensi mahal. Kerangka penskalaan berat, sebaliknya, membawa biaya nyata: pelatihan, sertifikasi, peran khusus, dan beban berkelanjutan dari acara perencanaan besar. Hanya kebutuhan koordinasi yang sejati yang membenarkannya. Biaya tidak berbuat apa-apa tampak sebagai kalender jenuh rapat, kontributor jarak jauh yang terkucil, upacara kultus kargo yang menghabiskan waktu tanpa memperbaiki hasil, dan pengiriman lambat. Untuk meyakinkan pimpinan, ukur lead time pengiriman, frekuensi deployment, dan persentase minggu kerja yang hilang ke rapat bernilai rendah. Perbaikan kecil pada aliran di seluruh tenaga kerja besar berjumlah menjadi keuntungan kapasitas yang besar.

## Anti-pola dan jebakan

- Agile kultus kargo: menjalankan upacara tanpa prinsip dasarnya.
- Velocity sebagai target: mengundang inflasi poin dan menghancurkan kegunaan metrik.
- Pemujaan kerangka: memaksakan SAFe atau templat "model Spotify" terlepas dari kecocokan.
- Estimasi sebagai komitmen: memperlakukan perkiraan di bawah ketidakpastian sebagai janji mengikat.
- Budaya digerakkan rapat: menjadikan panggilan sinkron sebagai bawaan yang mengucilkan zona waktu lain.
- Keputusan tak terdokumentasi: pengetahuan terperangkap di kepala orang dan percakapan masa lalu.
- Kotak hitam vendor: mengelola kontraktor lewat kanal samping buram alih-alih visibilitas bersama.
- Obsesi utilisasi: memaksimalkan kesibukan semua orang alih-alih aliran pekerjaan yang selesai.

## Model kematangan

- **Tingkat 1, Memulai.** Proses ad hoc atau kultus kargo; tim menjalankan upacara pinjaman tanpa prinsip di baliknya, atau berimprovisasi tanpa metode bersama sama sekali. Komunikasi digerakkan rapat dan tak terdokumentasi, keputusan hidup di kepala orang, dan estimasi diperlakukan sebagai janji. Kontributor yang tersebar, kontraktor, dan zona waktu berselisih dikoordinasikan secara lisan dan dibiarkan terhambat setiap kali orang yang tepat sedang tidur.
- **Tingkat 2, Mengembangkan.** Tim individual mengadopsi metodologi bernama seperti Scrum atau Kanban dan mengikutinya dengan cukup konsisten, tetapi praktik berbeda dari tim ke tim dan upacara sering hafalan. Beberapa tim menulis dokumen desain dan catatan keputusan sementara yang lain masih mengandalkan rapat. Estimasi dan koordinasi terjadi, tetapi tanpa batas bersama tentang apa arti "tertulis," sehingga konteks masih bocor dan serah terima lintas tim tetap berat.
- **Tingkat 3, Membakukan.** Praktik dipilih dengan sengaja agar sesuai dengan pekerjaan dan didokumentasikan sebagai ekspektasi seluruh organisasi: irama bersama yang minimal, batas terdefinisi untuk konteks tertulis dalam tiket dan catatan keputusan, komunikasi asinkron yang mengutamakan dokumen sebagai bawaan, dan estimasi dipakai untuk percakapan alih-alih kendali. Standar ditegakkan secara konsisten, sehingga kontraktor atau anggota baru di tim mana pun dapat beradaptasi dengan membaca, dan vendor bekerja di papan terlihat yang sama dengan staf.
- **Tingkat 4, Mengelola.** Cara kerja diukur terhadap garis dasar alih-alih diasumsikan. Tim melacak lead time pengiriman, distribusi cycle time, frekuensi deployment, throughput, dan persentase minggu kerja yang hilang ke rapat bernilai rendah, dan mengawasi velocity yang dipermainkan lewat inflasi poin. Batas pekerjaan-dalam-proses ditegakkan berdasarkan bukti, aliran dikelola alih-alih utilisasi, dan data, bukan opini, memutuskan upacara mana yang mempertahankan slotnya dan di mana antrean memanjang. Pelaporan kepada pimpinan dan badan pengawas langsung berasal dari metrik hidup ini.
- **Tingkat 5, Mengorkestrasi.** Organisasi terus menyetel cara kerjanya dari metrik aliran dan bukti retrospektif, dan kebutuhan koordinasi diminimalkan pada sumbernya melalui topologi tim alih-alih dikelola dengan proses yang lebih berat. Cara kerja, metrik pengiriman, dan desain organisasi terintegrasi dan beradaptasi seiring bergesernya tenaga kerja, pasar, dan gambaran regulasi; tim campuran yang tersebar dari staf, kontraktor, dan vendor di banyak zona waktu berkolaborasi dengan mulus, dan praktik yang tidak lagi sepadan dengan biayanya dihentikan tanpa upacara.

## Gagasan untuk didiskusikan

- Upacara mana yang akan kita pertahankan jika dinilai murni dari nilai yang diciptakannya?
- Apakah kita menskalakan dengan menambah kerangka atau dengan mengurangi kebutuhan koordinasi?
- Apakah velocity kita alat bantu perencanaan atau target yang diam-diam kita permainkan?
- Keputusan dan status apa yang hanya hidup di rapat dan ingatan orang, dan seharusnya ditulis?
- Zona waktu siapa yang menanggung biaya rapat sinkron kita, dan apakah itu adil?
- Apakah kontraktor dan vendor kita bekerja dalam aliran terlihat yang sama dengan staf kita?

## Poin-poin utama

- Adopsi prinsip di balik metodologi, bukan hanya ritualnya.
- Pilih Agile, Kanban, atau campuran agar sesuai dengan pekerjaan; utamakan batch kecil dan umpan balik cepat.
- Dekati kerangka penskalaan secara skeptis; skalakan dengan mengurangi koordinasi, bukan menambah proses.
- Gunakan estimasi untuk percakapan dan perkiraan, tidak pernah sebagai target produktivitas atau janji.
- Jadikan komunikasi asinkron yang mengutamakan dokumen sebagai bawaan agar tim besar, tersebar, dan campuran dapat berkolaborasi.
- Optimalkan hasil dan aliran, bukan aktivitas atau utilisasi.

## Referensi dan bacaan lanjutan

- David J. Anderson, "Kanban: Successful Evolutionary Change for Your Technology Business"
- Donald Reinertsen, "The Principles of Product Development Flow"
- Mary dan Tom Poppendieck, "Lean Software Development: An Agile Toolkit"
- Craig Larman dan Bas Vodde, "Large-Scale Scrum (LeSS)"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (metrik pengiriman)
- Agile Manifesto dan dua belas prinsipnya
- Henrik Kniberg, "Scaling Agile @ Spotify" (dengan peringatan bahwa itu potret, bukan model)
- Handbook publik GitLab tentang kerja asinkron dan remote-first
