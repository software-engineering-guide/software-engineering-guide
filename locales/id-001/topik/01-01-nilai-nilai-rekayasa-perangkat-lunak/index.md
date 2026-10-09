# 1.1 Nilai-nilai rekayasa perangkat lunak

## Tinjauan dan motivasi

Nilai-nilai [rekayasa perangkat lunak](https://en.wikipedia.org/wiki/Software_engineering) adalah keyakinan bersama, norma, dan perilaku sehari-hari yang membentuk cara orang membangun perangkat lunak bersama-sama. Nilai bukanlah poster di dinding atau kata-kata dalam buku pegangan karyawan. Nilai adalah apa yang benar-benar terjadi ketika sebuah insiden membangunkan seseorang pukul 3 pagi, ketika seorang insinyur junior tidak setuju dengan seorang principal engineer, atau ketika tenggat waktu berbenturan dengan kualitas. Nilai adalah sistem tak kasatmata di bawah setiap keputusan teknis.

Dalam tim kecil, nilai menyebar begitu saja: orang duduk bersama, menyerap norma, dan mengoreksi diri sendiri. Dalam tim yang lebih besar, penyebaran alami itu gagal. Anda kini harus membuat nilai menjadi eksplisit, menuliskannya, meminta para pemimpin memberi teladan, dan memperkuatnya lewat sistem Anda. Jika dilewatkan, budaya terpecah menjadi puluhan mikro-budaya yang tidak kompatibel dan diam-diam membebani setiap kolaborasi.

Bagi tim yang lebih besar, taruhannya bersifat struktural. Nilai yang lemah tampak sebagai pergantian karyawan, keputusan yang lambat, pengetahuan yang ditimbun, dan insiden berulang yang akar masalahnya tidak pernah benar-benar diperbaiki. Nilai yang kuat tampak sebagai perubahan yang cepat, aman, dan andal: insinyur mengangkat masalah sejak dini, belajar dari kegagalan, dan mengambil kepemilikan. Jarak antara dua keadaan ini sering kali lebih lebar daripada pilihan teknologi mana pun.

Organisasi enterprise dan pemerintah merasakan hal ini dengan tajam, karena mereka bekerja dalam skala besar, di bawah sorotan, dan dalam rentang waktu panjang. Sistem yang dibangun hari ini mungkin berjalan selama satu dekade atau lebih, dikelola oleh orang-orang yang tidak pernah bertemu penulis aslinya. Dalam situasi ini, budayalah yang membawa maksud melintasi waktu dan pergantian orang.

Perusahaan yang diatur regulasi menghadapi satu tekanan lagi: godaan untuk menggantikan kepercayaan dengan proses. Ketika akuntabilitas tinggi dan kesalahan terlihat, refleksnya adalah menumpuk kontrol, persetujuan, dan penyalahan. Hal ini dapat dimengerti, tetapi justru berbalik merugikan. Organisasi yang paling andal, aman, dan patuh biasanya adalah yang memiliki budaya belajar terkuat, bukan yang paling menghukum. Nilai dan kepatuhan adalah sekutu, bukan lawan.

## Prinsip utama

- [Rasa aman psikologis](https://en.wikipedia.org/wiki/Psychological_safety) adalah fondasi; tanpanya, setiap praktik lain memburuk.
- Kegagalan adalah data. Pembelajaran tanpa menyalahkan mengubah insiden menjadi perbaikan yang bertahan lama.
- Kepemilikan berarti akuntabilitas atas hasil, bukan hanya keluaran: "Anda yang membangun, Anda yang menjalankan."
- Menulis adalah berpikir. Budaya yang menuliskan keputusannya memperluas skala penilaiannya.
- Ritme yang berkelanjutan mengalahkan aksi heroik; [kelelahan kerja (burnout)](https://en.wikipedia.org/wiki/Occupational_burnout) adalah kegagalan sistem, bukan kegagalan pribadi.
- [Keberagaman, kesetaraan, dan inklusi](https://en.wikipedia.org/wiki/Diversity,_equity,_and_inclusion) adalah kekuatan rekayasa yang meningkatkan kualitas keputusan.
- Nilai diteladani dari atas dan diperkuat dari bawah; tindakan pemimpin lebih berbobot daripada kata-katanya.

## Rekomendasi

### Bangun rasa aman psikologis secara sengaja

Rasa aman psikologis adalah keyakinan bersama bahwa Anda dapat bersuara, bertanya, mengakui kesalahan, dan menantang keputusan tanpa takut dipermalukan atau dihukum. Dalam studi skala besar, ini adalah prediktor tunggal terkuat bagi efektivitas tim. Bangunlah dengan sengaja. Minta para pemimpin mengakui kesalahan mereka sendiri secara terbuka ("ini kesalahan yang saya buat dan apa yang saya pelajari"). Sambut kabar buruk dengan rasa ingin tahu, bukan hukuman. Undang perbedaan pendapat secara terbuka dalam rapat. Putar giliran siapa yang berbicara pertama, agar suara senior tidak mengarahkan diskusi. Dan jadikan wajar untuk berkata "saya tidak tahu" dan "saya butuh bantuan."

### Praktikkan pembelajaran tanpa menyalahkan

Ketika sesuatu rusak, lihatlah kondisi yang memungkinkan kegagalan itu, bukan orang yang memicunya. Terapkan [postmortem](https://en.wikipedia.org/wiki/Postmortem_documentation) tanpa menyalahkan: catatan tertulis tentang apa yang terjadi, kronologi, faktor penyebab, dan butir tindakan konkret dengan penanggung jawab dan tanggal. Mulailah dari anggapan bahwa semua orang bertindak wajar berdasarkan apa yang mereka ketahui saat itu. Tanyakan "apa yang membuat hal ini mudah keliru?" alih-alih "siapa yang salah?" Dan lacak butir tindakan sampai selesai. Budaya postmortem yang tidak pernah menutup tindak lanjutnya hanyalah sandiwara.

### Tetapkan model kepemilikan yang jelas

"Anda yang membangun, Anda yang menjalankan" membuat tim yang menulis sebuah layanan bertanggung jawab mengoperasikannya, termasuk jaga siaga (on-call). Ini memperketat lingkaran umpan balik antara keputusan desain dan kesulitan operasional, dan itu meningkatkan kualitas. Padukan dengan katalog layanan yang mencatat, untuk setiap sistem, siapa pemiliknya, cara menghubungi mereka, dependensinya, dan runbook-nya. Jaga kepemilikan tetap eksplisit dan tidak tumpang-tindih. Kepemilikan yang kabur adalah cara sistem membusuk dan insiden berlarut-larut. Ketika sebuah tim benar-benar tidak mampu mengoperasikan sistem sendirian, berikan dukungan platform alih-alih menyebarkan akuntabilitas.

### Pupuk budaya menulis

Menulis mempertajam pemikiran Anda, dan menghasilkan artefak yang bertahan melintasi zona waktu dan tahun. Jadikan dokumen desain dan catatan keputusan sebagai rutinitas untuk perubahan penting: dokumen singkat yang menyatakan masalah, opsi yang dipertimbangkan, pendekatan yang diusulkan, dan trade-off, diedarkan untuk dikomentari sebelum Anda membangun. Ini memunculkan ketidaksepakatan sejak dini, ketika masih murah, dan meninggalkan catatan tahan lama tentang mengapa Anda memutuskan demikian. Jaga agar templat ringan dan ekspektasi sebanding dengan bobot keputusan. Dan beri penghargaan secara terbuka untuk tulisan yang baik.

### Lindungi ritme yang berkelanjutan

Budaya pahlawan, tempat segelintir orang berulang kali menyelamatkan organisasi lewat upaya yang tidak berkelanjutan, adalah gejala kelemahan, bukan kebajikan. Budaya itu membuat orang kelelahan, memusatkan pengetahuan secara berbahaya, dan menyembunyikan masalah mendasar yang seharusnya Anda perbaiki. Maka ukur dan kelola beban on-call. Jika satu orang terus-menerus dipanggil, perlakukan itu sebagai cacat yang harus direkayasa hilang. Jadikan cuti hal yang wajar, lindungi waktu fokus, dan nilai keluaran dalam satu kuartal, bukan satu minggu.

### Perlakukan DEI sebagai kekuatan rekayasa

Tim yang beragam membuat keputusan yang lebih baik. Mereka menimbang lebih banyak sudut pandang dan lebih jarang jatuh ke [groupthink](https://en.wikipedia.org/wiki/Groupthink) dan titik buta, dan itu sangat penting bagi aksesibilitas, keamanan, dan pelayanan populasi yang luas. Bangun inklusi ke dalam rekayasa sehari-hari Anda: dokumentasi yang dapat diakses, bahasa yang inklusif dalam kode dan antarmuka, praktik rapat yang memungkinkan suara yang lebih pendiam berkontribusi, dan pembagian yang adil antara pekerjaan yang glamor dan pekerjaan perekat (glue work).

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
| --- | --- | --- |
| Postmortem tanpa menyalahkan | Mengungkap akar masalah yang sebenarnya; membangun kepercayaan; mendorong perbaikan sistemik | Dapat terasa seperti "tanpa akuntabilitas" bagi pihak luar; membutuhkan disiplin untuk menutup tindakan |
| "Anda yang membangun, Anda yang menjalankan" | Lingkaran umpan balik kualitas yang ketat; kepemilikan yang jelas | Beban on-call; memerlukan dukungan platform yang kuat agar tidak berujung burnout |
| Budaya dokumen-dulu / RFC | Keputusan tahan lama; skalabel melewati pergantian orang; ramah asinkron | Lebih lambat untuk perubahan sepele; berisiko menjadi birokrasi jika berlebihan |
| Ritme berkelanjutan | Retensi, keandalan, kecepatan jangka panjang | Terasa lebih lambat saat krisis; menuntut pimpinan menjaga garis |

Ketegangan utamanya adalah kecepatan jangka pendek versus kesehatan jangka panjang. Aksi heroik dan penyalahan membeli sekejap rasa terkendali, lalu keruntuhan lambat pada moral dan keandalan. Pembelajaran tanpa menyalahkan, kepemilikan, dan ritme berkelanjutan terasa lebih lambat dalam satu minggu mana pun, tetapi berlipat ganda menjadi kecepatan yang jauh lebih tinggi selama kuartal dan tahun. Para pemimpin harus bersedia menyerap ketidaknyamanan jangka pendek demi melindungi kapasitas jangka panjang.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Bagaimana Anda menjaga agar "tanpa menyalahkan" tidak terbaca sebagai "tanpa akuntabilitas" oleh auditor, eksekutif, dan publik?** Di perusahaan yang diatur regulasi atau lembaga pemerintah yang diawasi, postmortem yang tidak menyebut pelaku bisa tampak seperti upaya menutup-nutupi bagi orang di luar rekayasa. Pertimbangan yang bersaing itu nyata: Anda membutuhkan kejujuran yang hanya dihasilkan oleh sikap tanpa menyalahkan, dan Anda juga membutuhkan pengambil keputusan yang percaya bahwa kegagalan ditangani. Bawa bukti konkret ke diskusi, seperti tingkat kekambuhan insiden dan tingkat penyelesaian butir tindakan postmortem, karena sistem yang konsisten menutup tindak lanjutnya jelas akuntabel meski tanpa kambing hitam. Pisahkan dua pertanyaan yang disatukan oleh budaya menyalahkan: apa yang membuat hal ini mudah keliru, dan apakah ada yang bertindak dengan kelalaian atau itikad buruk yang sesungguhnya. Jika jawaban Anda adalah bahwa akuntabilitas berada dalam memperbaiki kondisi dan menutup tindakan, maka publikasikan mekanisme itu agar pihak luar dapat melihat akuntabilitas yang mereka cari.

2. **Tim mana yang memikul sistem on-call yang secara realistis tidak dapat mereka operasikan, dan siapa yang membayar kesenjangan itu?** "Anda yang membangun, Anda yang menjalankan" memperketat lingkaran umpan balik, dan mengandaikan tim memiliki dukungan platform untuk menjalankan apa yang dibangunnya. Pada skala enterprise dan pemerintah, sebagian tim mewarisi sistem lama, kotak hitam vendor, atau infrastruktur lintas bidang yang tidak mungkin benar-benar dimiliki sendirian oleh tim kecil. Trade-off-nya berada di antara menyebarkan akuntabilitas (buruk) dan membuat tim gagal pada pager yang tidak dapat mereka jawab (juga buruk). Bawa data panggilan: jika satu orang atau satu tim terus-menerus dipanggil, perlakukan itu sebagai cacat yang harus direkayasa hilang, bukan lencana kehormatan. Jawabannya harus memberi tahu Anda di mana berinvestasi pada tim platform, peluncuran bertahap, dan runbook yang mutakhir, sehingga kepemilikan tetap jelas sementara beban operasional tetap manusiawi.

3. **Apakah perilaku yang benar-benar Anda promosikan sesuai dengan nilai yang Anda terbitkan?** Nilai membusuk menjadi sinisme begitu para pemimpin menghargai apa yang dikecam oleh poster, dan pada skala besar kesenjangan ini tetap tak terlihat sampai pergantian karyawan dan penimbunan pengetahuan secara diam-diam mengungkapkannya. Tinjau dengan teliti siklus promosi terakhir Anda: apakah itu menghargai pemadaman kebakaran dan aksi heroik, atau pencegahan kebakaran dan pekerjaan perekat yang menjaga tim besar tetap sehat? Organisasi enterprise dan pemerintah memperparah risikonya, karena sistem tingkat yang kaku dan masa kerja yang panjang membiarkan insentif yang tidak selaras berjalan bertahun-tahun sebelum ada yang mengoreksi. Bawa bukti nyata, seperti siapa yang dipromosikan, siapa yang dipuji di depan umum, dan apa yang sebenarnya dilakukan orang-orang itu. Jika aksi heroik mendapat ganjaran, Anda sedang melatih organisasi Anda untuk memproduksi krisis yang kemudian dirayakan penyelesaiannya, dan perbaikannya adalah mengubah insentif, bukan seni dinding.

4. **Bagaimana Anda benar-benar tahu apakah rasa aman psikologis tinggi atau rendah pada tim tertentu, alih-alih menganggapnya dari bagan organisasi?** Rasa aman adalah fondasi bagi setiap praktik lain, dan juga hal yang paling mudah menipu diri sendiri, karena tim dengan rasa aman paling sedikit adalah yang paling kecil kemungkinannya memberi tahu Anda. Pada skala besar, rata-rata dari seribu orang menyembunyikan variasi yang penting: satu manajer dapat diam-diam menjalankan tim berbasis ketakutan di dalam organisasi yang sehat. Pertimbangan yang bersaing adalah keterusterangan versus kenyamanan, karena pertanyaan survei yang mengungkap masalah nyata adalah yang paling enggan dijawab jujur, dan mengumpulkan sinyal itu sendiri dapat terasa tidak aman. Bawa bukti konkret, bukan firasat: hasil tingkat tim dari instrumen rasa aman yang tervalidasi, tingkat orang mengakui kesalahan secara tertulis, laporan nyaris-celaka yang muncul sebelum menjadi insiden, dan tema wawancara keluar. Untuk badan enterprise atau pemerintah, pastikan data tetap di tingkat tim dan tidak pernah dipakai menghukum tim berskor rendah, karena begitu skor rasa aman menjadi tongkat, ia berhenti mengukur rasa aman dan mulai mengukur ketakutan terhadap pengukuran.

5. **Seberapa besar beban on-call dan aksi heroik Anda yang sebenarnya, dan apakah Anda menghargai orang yang mencegah kebakaran atau yang memadamkannya?** Ritme berkelanjutan adalah tempat niat baik diam-diam runtuh di bawah tekanan pengiriman, dan organisasi besar dapat berjalan di atas lembur tak terlihat segelintir orang yang kelelahan selama bertahun-tahun sebelum menyadarinya. Ketegangannya jujur: aksi heroik memang menyelamatkan Anda saat itu, dan bergantung padanya memusatkan pengetahuan, menyembunyikan cacat sistemik, dan membuat insinyur Anda yang paling berdedikasi kelelahan. Bawa data operasional ke diskusi: jumlah panggilan per orang per minggu, deploy di luar jam kerja, distribusi beban on-call di antara tim, dan seberapa banyak yang jatuh pada nama-nama yang sama bulan demi bulan. Lihat juga siapa yang dihargai siklus promosi terakhir Anda. Di enterprise dan lembaga pemerintah dengan tangga tingkat yang kaku dan masa kerja panjang, budaya yang membayar pemadaman kebakaran dapat bertahan tanpa tantangan selama satu dekade, sehingga jawabannya harus memberi tahu Anda di mana merekayasa pager agar turun dan bagaimana menjadikan pencegahan kebakaran tindakan yang jelas layak dipromosikan.

6. **Keputusan penting mana dalam dua tahun terakhir yang tidak memiliki catatan tertulis tentang alasannya, dan apa harganya ketika para penulisnya sudah pergi?** Budaya menulis adalah yang membawa maksud melintasi pergantian orang, dan ketiadaannya tak terlihat sampai saat seseorang perlu mengubah sistem yang tidak lagi dipahami siapa pun. Tarikan yang bersaing adalah kecepatan: menulis dokumen desain atau catatan keputusan terasa seperti gesekan saat itu, dan bila berlebihan berubah menjadi birokrasi yang memperlambat perubahan sepele. Bawa bukti untuk mengkalibrasinya: persentase perubahan penting yang memiliki dokumen desain atau catatan keputusan, seberapa sering orang benar-benar dapat menemukan dan mengutip alasan di balik arsitektur yang ada, dan berapa lama insinyur baru menjadi produktif pada layanan yang tidak terdokumentasi. Bagi organisasi enterprise dan pemerintah yang sistemnya hidup lebih lama daripada masa kerja semua orang yang membangunnya, dan yang mungkin menghadapi audit atau pengawasan keterbukaan informasi, catatan tertulis adalah memori institusional sekaligus bukti uji tuntas, sehingga jawabannya harus menarik garis di tempat bobot keputusan membenarkan penulisan dan tidak lebih rendah.

## Lensa sektor

**Startup.** Nilai masih menyebar begitu saja, jadi jangan mengimpor proses yang berat, tetapi sebutkan satu atau dua perilaku yang paling penting, biasanya kejujuran tanpa menyalahkan tentang kesalahan dan kecenderungan mengangkat kabar buruk sejak dini. Para pendiri menentukan nada dengan mengakui kesalahan mereka sendiri secara terbuka, karena dalam tim kecil satu reaksi tajam di Slack dapat mengajari semua orang menyembunyikan masalah selama berbulan-bulan. Runway Anda yang terbatas adalah alasan untuk melindungi rasa aman, bukan melewatkannya: tim yang menyembunyikan bug jauh lebih mahal daripada retro lima menit.

**Bisnis kecil.** Tanpa spesialis budaya rekayasa khusus dan dengan anggaran ketat, bersandarlah pada ritual ringan alih-alih perkakas yang harus dibeli atau diurus. Kanal insiden bersama, log keputusan satu halaman, dan kebiasaan bertanya "apa yang membuat ini mudah keliru?" tidak memerlukan biaya dan membawa sebagian besar nilainya. Bersikaplah sengaja juga pada garis beli-versus-bangun untuk praktik: gunakan templat postmortem siap pakai dan rotasi on-call sederhana alih-alih membangun sistem khusus yang tidak dapat Anda pelihara.

**Enterprise.** Pada skala besar, tugasnya adalah konsistensi tanpa keseragaman: pembelajaran tanpa menyalahkan, kepemilikan jelas yang tidak tumpang-tindih, dan budaya menulis menjadi norma seluruh organisasi dengan perkakas, ekspektasi, dan katalog layanan di belakangnya. Tata kelola dan audit mendorong Anda ke arah kontrol, jadi buktikan bahwa budaya belajar yang kuat adalah opsi yang paling andal dan patuh, dan tunjukkan dengan metrik kekambuhan insiden dan penutupan butir tindakan. Perhatikan variasi antartim, karena rata-rata menyembunyikan kantong berbasis ketakutan yang diam-diam membocorkan talenta dan pengetahuan.

**Pemerintah.** Aturan pengadaan, kewajiban transparansi, dan akuntabilitas publik membentuk cara nilai diekspresikan, terutama terkait penyalahan. Postmortem yang tidak menyebut pelaku bisa terbaca sebagai upaya menutup-nutupi oleh pengawas luar, jadi publikasikan mekanismenya, tunjukkan bahwa akuntabilitas berada dalam memperbaiki kondisi dan menutup tindakan, dan biarkan warga serta auditor melihatnya. Karena sistem hidup lebih lama daripada pemerintahan dan pergantian staf diukur dalam tahun, perlakukan catatan keputusan tertulis sebagai memori institusional sekaligus bukti uji tuntas di bawah pengawasan keterbukaan informasi.

## Contoh

**Startup.** Sebuah startup berenam berjalan dengan kepercayaan dan obrolan di lorong, sehingga tidak ada yang menuliskan nilai tim. Ketika seorang insinyur pendiri mendorong migrasi yang buruk dan CTO membentaknya di Slack, ruangan menjadi sunyi, dan dua bug berikutnya diam-diam disembunyikan alih-alih diangkat. Tim pulih dengan mengadopsi satu kebiasaan ringan: obrolan lima menit "apa yang membuat ini mudah keliru?" tanpa menyalahkan setelah setiap insiden, tanpa templat. Ritual kecil itu menjaga budaya alami tetap sehat tanpa beban proses yang akan dibutuhkan organisasi yang lebih besar.

**Enterprise.** Sebuah perusahaan jasa keuangan besar mengalami pemadaman besar ketika perubahan konfigurasi rutin merambat ke seluruh layanan. Dalam budaya menyalahkan, insinyur yang mendorong perubahan itu akan ditegur, dan selesai. Sebaliknya, postmortem tanpa menyalahkan menunjukkan bahwa perkakas deployment membuat perubahan berbahaya tampak identik dengan yang aman, bahwa tidak ada peluncuran bertahap, dan bahwa runbook sudah usang. Perusahaan berinvestasi pada peluncuran progresif dan validasi konfigurasi, dan perubahan serupa kini gagal dengan aman. Memilih untuk melihat sistem alih-alih orangnya menghasilkan perbaikan rekayasa yang bertahan lama.

**Pemerintah.** Sebuah lembaga layanan digital pemerintah mengadopsi "Anda yang membangun, Anda yang menjalankan" bersama proses [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (request for comments) yang ketat dengan dokumen-dulu. Karena sistemnya harus bertahan melewati pergantian pemerintahan politik dan pergantian staf yang diukur dalam tahun, setiap keputusan penting dicatat dalam dokumen desain yang menjelaskan konteks dan trade-off. Insinyur baru, dan kontraktor yang datang, dapat membaca alasan di balik arsitektur berusia satu dekade alih-alih merekayasa baliknya. [Memori institusional](https://en.wikipedia.org/wiki/Institutional_memory) tertulis itulah yang memungkinkan lembaga menjaga layanan publik tetap andal meski pergantian tinggi dan persyaratan akuntabilitas yang ketat.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil budaya itu nyata tetapi tidak langsung, itulah sebabnya ia kronis kekurangan dana. Sepanjang umur sebuah sistem, biaya dominan bukanlah membangunnya. Biaya itu adalah pemeliharaan, penanganan insiden, pengerjaan ulang, dan biaya kehilangan serta merekrut kembali orang-orang terampil. Budaya belajar yang kuat memperbaiki setiap hal ini. Postmortem tanpa menyalahkan mengurangi insiden berulang. Kepemilikan yang jelas mengurangi waktu rata-rata pemulihan. Budaya menulis menurunkan biaya [orientasi](https://en.wikipedia.org/wiki/Onboarding) dan biaya keputusan yang dibuat tanpa mengetahui alasan yang mendahuluinya.

Ambil pergantian karyawan saja. Mengganti seorang insinyur tingkat menengah biasanya menelan biaya antara setengah hingga dua kali gaji tahunannya setelah menghitung perekrutan, masa penyesuaian, dan pengetahuan institusional yang ikut keluar pintu. Jika budaya yang lebih sehat memangkas pergantian yang disesalkan bahkan hanya beberapa poin persentase di organisasi seribu orang, penghematannya jauh melampaui biaya sederhana menjalankan postmortem dan menulis dokumen. Biaya adopsi sebagian besar adalah perhatian pimpinan dan sedikit beban proses. Biaya tidak mengadopsi dibayar terus-menerus dan tanpa terlihat: pengiriman yang lebih lambat, insiden berulang, dan talenta yang diam-diam pergi.

Untuk meyakinkan pimpinan, hubungkan budaya dengan metrik yang sudah dilacak para eksekutif: lead time pengiriman, tingkat kegagalan perubahan, waktu rata-rata pemulihan, kekambuhan insiden, dan pergantian yang disesalkan. Bingkai rasa aman psikologis bukan sebagai manfaat lunak melainkan sebagai mekanisme yang membuat setiap investasi rekayasa lain membuahkan hasil, karena tim yang tidak aman menyembunyikan masalah yang justru hendak diperbaiki oleh investasi-investasi itu.

## Anti-pola dan jebakan

- Tinjauan insiden yang menyalahkan dan mempermalukan: mendorong masalah ke bawah tanah dan orang berhenti melapor.
- Pemujaan pahlawan: menghargai pemadaman kebakaran daripada pencegahan kebakaran melanggengkan kebakaran.
- "Nilai" yang dilanggar pemimpin: nilai yang dinyatakan namun dibantah perilaku menumbuhkan sinisme.
- Kepemilikan tanpa dukungan: menugaskan on-call untuk sistem yang tidak mungkin dioperasikan tim secara realistis.
- Proses sebagai pengganti kepercayaan: menumpuk persetujuan alih-alih membangun rasa aman yang sejati.
- Sandiwara dokumen: menulis dokumen yang tidak dibaca siapa pun atau tidak pernah memengaruhi keputusan.
- Inklusi sebagai kotak centang: merekrut demi keberagaman sambil mengecualikan suara yang sama dari keputusan.

## Model kematangan

- Tingkat 1, Memulai: Nilai bersifat kebetulan dan digerakkan kepribadian. Insiden berarti penyalahan, pengetahuan hidup di beberapa kepala, dan aksi heroik adalah cara segala sesuatu dikerjakan. Tidak ada yang menuliskan apa yang diyakini tim atau bagaimana ia berperilaku di bawah tekanan.
- Tingkat 2, Mengembangkan: Beberapa tim memulai postmortem tanpa menyalahkan, menulis dokumen desain sesekali, dan membicarakan kepemilikan, tetapi praktiknya tidak konsisten, diterapkan tidak merata, dan belum diperkuat oleh pimpinan. Apakah Anda mendapat tim yang sehat sebagian besar soal keberuntungan.
- Tingkat 3, Membakukan: Pembelajaran tanpa menyalahkan, kepemilikan jelas yang tidak tumpang-tindih, dan budaya menulis adalah norma seluruh organisasi yang terdokumentasi, dengan templat, katalog layanan, dan ekspektasi on-call yang terdefinisi. Para pemimpin meneladankan nilai dan perilaku yang sama diharapkan di mana-mana, bukan hanya di tempat seorang manajer baik kebetulan berada.
- Tingkat 4, Mengelola: Budaya diukur terhadap garis dasar dan dikendalikan dengan data. Anda melacak skor rasa aman psikologis tingkat tim, kekambuhan insiden, tingkat penutupan butir tindakan postmortem, distribusi beban on-call, waktu rata-rata pemulihan, dan pergantian yang disesalkan, dan Anda bertindak berdasarkan angka ketika sebuah tim menyimpang. Hapus insentif pemadaman kebakaran berdasarkan bukti, dan hargai pencegahan kebakaran karena kini Anda bisa melihatnya.
- Tingkat 5, Mengorkestrasi: Budaya terus diperbaiki dan terintegrasi dengan cara seluruh organisasi merencanakan, merekrut, dan mempromosikan. Rasa aman tinggi, pembelajaran cepat, dan praktik beradaptasi seiring bukti dan konteks berubah. Organisasi menyeimbangkan kembali beban on-call, menyegarkan catatan keputusan, dan mengembangkan normanya dengan sengaja alih-alih menunggu krisis memaksa persoalannya.

## Gagasan untuk didiskusikan

- Di mana dalam organisasi kita orang tidak merasa aman untuk berkata "saya tidak tahu" atau "saya tidak setuju," dan mengapa?
- Apakah tinjauan insiden kita mengubah sistem, atau hanya menunjuk kesalahan lalu berlalu?
- Apakah kita menghargai aksi heroik yang seharusnya kita rekayasa hilang?
- Keputusan penting mana dari dua tahun terakhir yang tidak memiliki catatan tertulis tentang alasannya?
- Seberapa merata pekerjaan perekat dan beban on-call dibagi di antara tim?
- Apakah nilai yang kita nyatakan sesuai dengan apa yang sebenarnya membuat orang dipromosikan di sini?

## Poin-poin utama

- Nilai adalah sistem operasi tak kasatmata di balik setiap keputusan teknis; pada skala besar, nilai harus eksplisit.
- Rasa aman psikologis bersifat mendasar; tanpanya, praktik lain membusuk.
- Pembelajaran tanpa menyalahkan mengubah kegagalan menjadi perbaikan sistemik yang bertahan lama.
- Kepemilikan yang jelas ("Anda yang membangun, Anda yang menjalankan") memperketat lingkaran umpan balik kualitas.
- Budaya menulis memperluas skala penilaian lintas zona waktu dan pergantian orang.
- Ritme berkelanjutan dan inklusi adalah pengali kecepatan jangka panjang, bukan biaya.

## Referensi dan bacaan lanjutan

- Amy C. Edmondson, "The Fearless Organisation" dan "Teaming"
- Google re:Work / Project Aristotle research on team effectiveness
- Sidney Dekker, "The Field Guide to Understanding 'Human Error'"
- John Allspaw, "Blameless PostMortems and a Just Culture" (Etsy Code as Craft)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate: The Science of Lean Software and DevOps"
- Gene Kim et al., "The Phoenix Project" dan "The DevOps Handbook"
- Camille Fournier, "The Manager's Path"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Tom DeMarco dan Timothy Lister, "Peopleware: Productive Projects and Teams"
