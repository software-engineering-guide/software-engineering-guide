# 2.5 Tinjauan kode dan kolaborasi

## Tinjauan dan motivasi

[Tinjauan kode](https://en.wikipedia.org/wiki/Code_review) adalah praktik meminta seseorang selain penulis memeriksa sebuah perubahan sebelum digabung. Ini salah satu kegiatan kualitas dan berbagi pengetahuan berdaya ungkit tertinggi yang dimiliki organisasi perangkat lunak, dan bagi tim besar ia juga mekanisme koordinasi dan budaya utama. Tinjauan menangkap cacat, menyebarkan pengetahuan tentang basis kode, menegakkan standar, dan membimbing insinyur, tetapi hanya bila dilakukan dengan baik. Bila dilakukan buruk, ia menjadi hambatan, sumber gesekan, atau cap karet yang memberi jaminan palsu.

Bagi tim besar, tinjauan adalah tempat kerja individual bertemu kepemilikan kolektif. Sering ia menjadi titik sentuh utama antara insinyur yang selain itu bekerja sendiri, sehingga normanya membentuk cara seluruh organisasi berkolaborasi. Tinjauan menyebarkan pengetahuan agar tidak ada bagian sistem yang hanya dipahami satu orang, yang mengurangi risiko [bus factor](https://en.wikipedia.org/wiki/Bus_factor), bahaya ketika pengetahuan berada pada terlalu sedikit orang, yang menghantui sistem besar berumur panjang. Ia juga menciptakan jejak audit tentang siapa mengubah apa dan siapa menyetujuinya.

Dalam konteks enterprise dan pemerintah, tinjauan sering membawa dimensi kepatuhan. [Pemisahan tugas](https://en.wikipedia.org/wiki/Separation_of_duties) (tak seorang pun mengendalikan seluruh perubahan sensitif), persetujuan wajib, dan keterlacakan sering menjadi kontrol yang diwajibkan. Perubahan yang menyentuh sistem sensitif mungkin perlu ditinjau oleh peran tertentu, dan catatan tinjauan menjadi bukti audit. Tantangan Anda adalah memenuhi kontrol ini sambil menjaga tinjauan tetap cepat dan konstruktif, alih-alih mengubahnya menjadi upacara.

## Prinsip utama

- Tinjau untuk memperbaiki perubahan dan berbagi pengetahuan, bukan untuk pamer.
- Perubahan kecil mendapat tinjauan lebih baik, jadi jaga pull request (PR) tetap terfokus dan berukuran wajar.
- Latensi tinjauan adalah biaya seluruh tim. Perputaran cepat menjaga semua orang tetap bergerak.
- Otomatiskan hal mekanis (gaya, tes, pemindaian keamanan) agar manusia meninjau desain dan kebenaran.
- Pisahkan isu pemblokir dari saran dan preferensi, dan eksplisit tentang mana yang mana.
- Kritik kodenya, bukan orangnya. Norma umpan balik menentukan apakah tinjauan membangun kepercayaan atau mengikisnya.
- Penulis bertanggung jawab membuat perubahan mudah ditinjau.

## Rekomendasi

### Buat pull request kecil dan terdeskripsikan dengan baik

Jaga setiap perubahan terfokus pada satu perhatian logis dan cukup kecil untuk ditinjau dengan cermat. PR besar mendapat tinjauan dangkal. Berikan deskripsi yang jelas tentang apa yang berubah, mengapa, dan bagaimana Anda memverifikasinya, agar peninjau punya konteks. Pisahkan refaktor mekanis dan perubahan perilaku ke PR terpisah, agar masing-masing mudah dinalar. Deskripsi yang baik adalah kontribusi tunggal terpenting penulis bagi kualitas tinjauan.

### Tetapkan standar dan daftar periksa tinjauan

Rincikan apa yang harus dicari peninjau: kebenaran, kecocokan desain, kecukupan tes, implikasi keamanan, keterbacaan, dan kepatuhan pada standar. Daftar periksa ringan menjaga tinjauan tetap konsisten dan mencegah dimensi penting terlewat, tanpa mengubah tinjauan menjadi centang kotak. Definisikan apa yang memerlukan tinjauan, siapa yang dapat menyetujui, dan persetujuan berbasis peran yang dibutuhkan untuk area sensitif.

### Tetapkan dan pantau norma latensi tinjauan

Sepakati target perputaran, misalnya menanggapi dalam satu hari kerja, dan jadikan tinjauan bagian kelas satu dari hari itu alih-alih sesuatu yang diselipkan terakhir. Antrean tinjauan yang panjang menghentikan pengiriman dan menggoda insinyur ke perubahan yang membengkak dan bergelombang. Pantau waktu-hingga-tinjauan-pertama dan waktu-hingga-gabung, dan perlakukan latensi yang berkelanjutan sebagai masalah proses untuk diperbaiki, bukan kegagalan pribadi.

### Otomatiskan semua yang mekanis

Jalankan format, [linting](https://en.wikipedia.org/wiki/Lint_(software)), tes, dan pemindaian keamanan serta dependensi di [integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration) (CI), agar peninjau tidak pernah menghabiskan perhatian pada hal itu. Sisakan tinjauan manusia untuk hal yang tidak dapat dinilai mesin: apakah desainnya benar, apakah pendekatannya cocok dengan sistem, apakah tesnya bermakna, dan apakah kodenya masih masuk akal kelak.

### Gunakan pair dan mob programming di tempat yang cocok

Gunakan [pair programming](https://en.wikipedia.org/wiki/Pair_programming), di mana dua insinyur menulis kode bersama di satu stasiun kerja, untuk pekerjaan kompleks atau berisiko tinggi, orientasi, dan transfer pengetahuan. Ia tinjauan berkelanjutan, dan sering menghilangkan kebutuhan langkah tinjauan terpisah. Gunakan [mob programming](https://en.wikipedia.org/wiki/Mob_programming), di mana seluruh tim mengerjakan satu tugas sekaligus, untuk keputusan desain kritis atau untuk menyebarkan pengetahuan tentang area rumit ke seluruh tim. Anggap keduanya pelengkap tinjauan asinkron, dipilih menurut konteks, bukan pengganti yang diwajibkan di mana-mana.

### Adopsi tinjauan otomatis dan berbantuan AI dengan hati-hati

Gunakan perkakas tinjauan otomatis dan asisten AI untuk menangkap isu umum, menyarankan perbaikan, dan meringankan beban peninjau, tetapi perlakukan keluarannya sebagai masukan, bukan otoritas. Tinjauan AI bagus pada isu permukaan dan konsistensi, dan buruk pada penilaian desain mendalam dan konteks sistem. Pertahankan manusia yang bertanggung jawab atas setiap persetujuan, terutama untuk perubahan yang sensitif keamanan dan relevan kepatuhan.

### Tetapkan norma umpan balik yang konstruktif

Tetapkan norma yang menjaga umpan balik spesifik, baik hati, dan terfokus pada kode. Dorong peninjau untuk mengajukan pertanyaan alih-alih mengeluarkan perintah, menjelaskan alasan di balik permintaan, dan memuji kerja yang baik. Tandai kekhawatiran pemblokir dan saran opsional dengan jelas (misalnya, dengan memberi awalan pada catatan non-pemblokir). Norma ini menentukan apakah tinjauan memperkuat tim atau menumbuhkan kebencian.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Tinjauan PR asinkron | Fleksibel; terdokumentasi; berskala lintas zona waktu | Latensi; kehilangan nuansa; bisa terasa memusuhi |
| Pair programming | Tinjauan berkelanjutan; transfer pengetahuan cepat; kualitas tinggi | Dua orang pada satu tugas; melelahkan; lebih sulit dijadwalkan |
| Mob programming | Keselarasan seluruh tim; menyebarkan pengetahuan mendalam | Mahal secara agregat; bukan untuk pekerjaan rutin |
| Multi-peninjau wajib | Jaminan kuat; ramah kepatuhan | Lebih lambat; menyebarkan tanggung jawab; tekanan antrean |
| Tinjauan berbantuan AI | Cepat, tak kenal lelah pada isu umum; mengurangi beban | Melewatkan konteks sistem; keyakinan palsu bila terlalu dipercaya |

Ketegangan intinya adalah ketelitian versus kecepatan. Tinjauan yang lebih dalam menangkap lebih banyak, tetapi memperlambat pengiriman dan dapat membuat penulis frustrasi. Tinjauan yang lebih cepat menjaga aliran, tetapi berisiko dangkal. Jalan keluarnya adalah menyesuaikan kedalaman tinjauan dengan risiko perubahan, sehingga perubahan sepele mendapat tinjauan ringan dan yang berisiko mendapat tinjauan dalam, dan mengotomatiskan pekerjaan mekanis agar upaya manusia terkonsentrasi di tempat yang penting.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa yang dianggap terlalu besar untuk satu pull request, dan apakah Anda memisahkan refaktor mekanis dari perubahan perilaku?** Bab ini menyatakan dengan gamblang bahwa PR besar mendapat tinjauan dangkal dan bahwa penulis memiliki kemudahan tinjauan, dan meminta Anda memisahkan refaktor dari perubahan perilaku agar masing-masing mudah dinalar. Pada tim besar PR raksasa menjamin cap karet, yang memberi jaminan palsu sambil membiarkan cacat nyata lolos. Bawa buktinya: distribusi ukuran PR Anda dan bagaimana kedalaman tinjauan turun seiring diff membesar. Sepakati norma ukuran yang praktis dan kebiasaan mendaratkan refaktor murni terpisah dari perubahan logika, agar peninjau benar-benar dapat memegang setiap perubahan di kepalanya. Satu disiplin itu mengangkat kualitas setiap tinjauan yang menyusul.

2. **Bagaimana Anda membedakan keberatan pemblokir dari saran opsional, dan apakah konvensi itu benar-benar dipakai?** Bab ini meminta Anda memisahkan isu pemblokir dari preferensi dan eksplisit tentang mana yang mana, dan menandai pemblokiran atas preferensi sebagai anti-pola yang korosif. Tanpa konvensi bersama, opini gaya peninjau terbaca sebagai perubahan wajib, yang menumbuhkan kebencian dan memperlambat pengiriman di seluruh tim. Bawa contoh dari tinjauan terbaru di mana preferensi menghentikan penggabungan sebagai sinyal konkret. Adopsi penanda ringan, misalnya awalan yang menandai catatan non-pemblokir, agar penulis langsung tahu apa yang harus berubah versus apa yang saran. Itu menjaga tinjauan terfokus pada kebenaran dan desain alih-alih selera.

3. **Siapa yang harus menyetujui perubahan pada kode yang sensitif keamanan atau relevan kepatuhan, dan bagaimana perutean itu ditegakkan?** Bab ini menjelaskan persetujuan berbasis peran, aturan kepemilikan kode, dan pemisahan tugas di mana tak seorang pun mengendalikan seluruh perubahan sensitif, dengan persetujuan dicatat sebagai bukti audit. Dalam konteks enterprise dan pemerintah ini kontrol yang diwajibkan, dan risikonya adalah mereka dilewati atau berubah menjadi hambatan yang membekukan pengiriman. Bawa sinyalnya: modul mana yang sensitif, dan apakah aturan kepemilikan saat ini merutekan perubahan itu ke penyetuju yang tepat secara otomatis. Kodekan perutean dalam konfigurasi kepemilikan kode dan pasangkan dengan pemeriksaan otomatis dan perubahan kecil, agar kontrol terpenuhi tanpa antrean penjaga gerbang manusia. Putuskan ini dengan sengaja alih-alih menemukan celahnya saat audit.

4. **Target latensi tinjauan apa yang benar-benar telah Anda sepakati, dan apakah Anda mengukur dan menegakkannya, atau hanya aspirasi?** Bab ini memperlakukan latensi tinjauan sebagai biaya seluruh tim dan meminta Anda memantau waktu-hingga-tinjauan-pertama dan waktu-hingga-gabung, memperlakukan keterlambatan berkelanjutan sebagai masalah proses, bukan kegagalan pribadi. Pada tim besar antrean tinjauan tanpa pemilik diam-diam memajaki semua orang: penulis menggabung perubahan lebih besar untuk menghindari penantian, perubahan itu lalu mendapat tinjauan lebih dangkal, dan lead time pengiriman melayang naik tanpa satu pun biang keladi. Pertimbangan yang bersaing adalah bahwa target latensi yang keras dapat mendorong peninjau membaca sekilas, sehingga kecepatan dan kedalaman harus diseimbangkan, bukan ditukar secara buta. Bawa buktinya: distribusi waktu-hingga-tinjauan-pertama Anda saat ini, bagaimana ia bervariasi menurut tim dan ukuran perubahan, dan di mana tinjauan paling lama mengendap. Dalam konteks enterprise dan pemerintah, kaitkan target dengan metrik aliran yang sudah dilacak pimpinan, karena kontrol multi-peninjau wajib tanpa norma latensi menjadi hambatan yang membekukan pengiriman dan menggoda orang memutari kontrol itu sepenuhnya.

5. **Untuk jenis perubahan apa Anda memercayai tinjauan otomatis dan berbantuan AI, dan di mana manusia harus tetap bertanggung jawab?** Bab ini mengatakan perlakukan keluaran tinjauan AI sebagai masukan, bukan otoritas: kuat pada isu permukaan dan konsistensi, lemah pada penilaian desain mendalam dan konteks sistem, dengan manusia bertanggung jawab atas setiap persetujuan. Tanpa batas eksplisit, tim besar hanyut ke kepercayaan berlebih, di mana komentar bot hijau terbaca sebagai tinjauan yang lolos dan risiko desain serta keamanan yang nyata meluncur di bawah keyakinan palsu. Tarikan yang bersaing adalah bahwa tinjauan AI memang meringankan beban dan menangkap cacat umum tanpa lelah, jadi melarangnya membuang daya ungkit. Bawa buktinya: di mana saran otomatis menangkap isu nyata, di mana ia menghasilkan derau, dan jenis perubahan mana (sensitif keamanan, relevan kepatuhan, arsitektural) yang tidak akan pernah Anda biarkan ditandatangani mesin sendirian. Untuk pekerjaan enterprise dan pemerintah, namai siapa yang memegang akuntabilitas atas persetujuan ketika asisten AI ikut serta, karena audit akan menanyakan siapa yang meninjau perubahan, dan "perkakasnya" bukan jawaban yang diterima regulator.

6. **Di mana pairing atau mobbing harus menggantikan tinjauan asinkron, dan bagaimana Anda memakai tinjauan untuk mengurangi risiko bus factor dengan sengaja?** Bab ini membingkai pair dan mob programming sebagai tinjauan berkelanjutan yang dipilih menurut konteks, dan menyebut tinjauan sebagai mekanisme yang menyebarkan pengetahuan agar tidak ada bagian sistem yang hanya dipahami satu orang. Jika dibiarkan implisit, pengetahuan terkonsentrasi: pakar yang sama meninjau setiap perubahan pada sebuah subsistem, tinjauan berubah menjadi cap karet karena tak seorang pun dapat menantangnya, dan risiko bus factor tumbuh persis di tempat sistem paling kritis. Pertimbangan yang bersaing adalah biaya, karena mobbing memakai waktu seluruh tim dan pairing mengikat dua insinyur, sehingga Anda tidak dapat mewajibkannya di mana-mana. Bawa buktinya: modul mana yang hanya punya satu peninjau yang kredibel, di mana orientasi tersendat, dan di mana area rumit akan diuntungkan sesi langsung daripada utas komentar. Dalam organisasi besar atau publik, perlakukan penyebaran pengetahuan yang disengaja sebagai manajemen risiko, karena sistem berumur panjang yang bagian kritisnya bergantung pada satu orang adalah liabilitas operasional dan kesinambungan, bukan sekadar ketidaknyamanan penempatan staf.

## Lensa sektor

**Startup.** Dengan tiga atau empat insinyur, jaga tinjauan tetap ringan: persetujuan satu rekan pada pull request kecil, pemeriksaan mekanis di CI, dan tanpa peninjau kedua wajib yang akan menghentikan penggabungan. Tujuan sebenarnya kurang soal kepatuhan dibandingkan memastikan lebih dari satu orang memahami setiap bagian sistem, jadi berpasanganlah pada bagian berisiko dan perlakukan itu sebagai orientasi. Jangan bangun perutean kepemilikan kode berat yang akan segera Anda lampaui; norma bersama perubahan kecil yang terdeskripsikan baik membeli sebagian besar manfaat dengan biaya hampir nol.

**Bisnis kecil.** Anda kecil kemungkinan punya spesialis perkakas tinjauan, jadi bersandarlah pada apa yang diberikan platform hosting Anda (misalnya layanan Git terkelola) secara bawaan alih-alih membangun otomasi kustom. Beli integrasi linting, tes, dan pemindaian keamanan alih-alih memeliharanya, agar sedikit insinyur Anda membelanjakan menit tinjauan yang langka pada desain dan kebenaran. Pertahankan satu aturan sederhana, setiap perubahan mendapat sepasang mata lain, dan tahan diri dari menambah proses yang tidak ada orang untuk memeliharanya.

**Enterprise.** Tantangannya adalah konsistensi di banyak tim: standar bersama, aturan kepemilikan kode yang merutekan perubahan sensitif ke penyetuju yang tepat, dan persetujuan berbasis peran yang dicatat sebagai bukti audit. Otomatiskan pemeriksaan mekanis di seluruh organisasi agar tinjauan manusia terkonsentrasi pada desain, dan lacak latensi tinjauan sebagai metrik aliran agar kontrol multi-peninjau wajib tidak diam-diam menjadi hambatan. Sesuaikan kedalaman tinjauan dengan risiko perubahan lewat kebijakan terdokumentasi, agar perubahan sepele tetap cepat sementara yang berisiko tinggi mendapat pemisahan tugas dan pengawasan lebih dalam.

**Pemerintah.** Kendali perubahan sering wajib: setiap perubahan produksi ditinjau dan disetujui oleh seseorang selain penulis, dengan catatan disimpan sebagai bukti audit untuk memenuhi persyaratan pemisahan tugas. Pilih jejak yang transparan dan dapat dilacak tentang siapa menulis, siapa menyetujui, dan pemeriksaan mana yang lolos, dan berinvestasilah pada otomasi serta perubahan kecil yang sering agar kontrol tidak membekukan pengiriman. Di tempat perkakas tinjauan diadakan, tuntut log audit yang dapat diekspor dan hindari lock-in, karena bukti harus hidup lebih lama daripada vendor tunggal mana pun dan bertahan dari pengawasan publik.

## Contoh

**Startup.** Sebuah startup empat insinyur menjaga setiap pull request tetap kecil dan meminta persetujuan satu rekan sebelum digabung, kurang untuk kepatuhan dibandingkan untuk memastikan tak seorang pun menjadi satu-satunya yang memahami suatu bagian sistem. CI menjalankan formatter dan tes, sehingga manusia membelanjakan menit tinjauan mereka yang sedikit pada desain dan kebenaran alih-alih spasi. Ketika tim menghadapi bagian rumit dari alur pembayaran, dua dari mereka berpasangan mengerjakannya alih-alih bertukar komentar asinkron, yang sekaligus menjadi orientasi bagi karyawan terbaru.

**Enterprise.** Sebuah perusahaan perangkat lunak besar mewajibkan setidaknya satu tinjauan penyetuju pada setiap perubahan, ditambah persetujuan kedua untuk perubahan pada modul sensitif keamanan yang diidentifikasi oleh aturan kepemilikan kode. CI menangani semua pemeriksaan gaya dan tes, sehingga peninjau berfokus pada desain dan kebenaran. Tim melacak waktu-hingga-tinjauan-pertama dan memperlakukan median yang naik sebagai sinyal untuk menyeimbangkan ulang beban kerja. Insinyur baru diorientasi lewat pairing, yang mempersingkat jalan mereka untuk berkontribusi secara mandiri.

**Pemerintah.** Sebuah lembaga nasional yang beroperasi di bawah persyaratan kendali perubahan yang ketat mewajibkan setiap perubahan produksi ditinjau dan disetujui oleh seseorang selain penulis, dengan persetujuan dicatat untuk audit. Agar kontrol ini tidak menjadi hambatan, lembaga berinvestasi pada pemeriksaan otomatis dan perubahan kecil yang sering, dan menetapkan norma respons tinjauan di hari yang sama. Jejak tinjauan, mencakup siapa menulis, siapa menyetujui, dan pemeriksaan apa yang lolos, menjadi bagian dari bukti kepatuhan untuk setiap rilis, memenuhi persyaratan pemisahan tugas tanpa membekukan pengiriman.

## Kasus bisnis: motivasi, ROI, dan TCO

Tinjauan kode membayar Anda kembali dalam tiga mata uang: cacat yang tertangkap sebelum produksi, pengetahuan yang tersebar di tim, dan standar yang ditegakkan secara otomatis dari waktu ke waktu. Menangkap cacat dalam tinjauan jauh lebih murah daripada menangkapnya di produksi, dan manfaat berbagi pengetahuan mengurangi risiko orang kunci yang dapat sangat merugikan organisasi saat seseorang pergi. Tinjauan juga mekanisme penularan budaya yang menjaga tim yang tumbuh tetap koheren.

Biaya tinjauan adalah waktu insinyur dan sedikit latensi, keduanya dapat dikelola dengan praktik yang baik. Biaya *tidak* meninjau, atau meninjau dengan buruk, mencakup cacat produksi, pengetahuan yang terkotak-kotak, kode yang tidak konsisten, dan, di lingkungan yang diatur, audit yang gagal dan temuan kepatuhan. Tinjauan yang terlalu berat juga punya biaya nyata sendiri: antrean panjang, gelombang yang membengkak, insinyur yang patah semangat. Untuk meyakinkan pimpinan, hubungkan praktik tinjauan dengan tingkat kegagalan perubahan, lead time pengiriman, dan kecepatan orientasi, dan lacak latensi tinjauan sebagai metrik aliran eksplisit.

## Anti-pola dan jebakan

- **Cap karet:** persetujuan tanpa pemeriksaan nyata, memberi jaminan palsu dan hanya memenuhi huruf kontrol.
- **PR raksasa:** ribuan baris yang hanya dapat dibaca sekilas, menjamin tinjauan dangkal.
- **Tinjauan hanya-nitpick:** berfokus pada hal sepele sambil melewatkan desain dan kebenaran, sering karena pemeriksaan mekanis tidak diotomatiskan.
- **Tinjauan sebagai penjagaan gerbang:** memakai tinjauan untuk menegaskan dominasi atau menghalangi orang lain, meracuni kolaborasi.
- **Antrean lambat:** tinjauan yang mengendap berhari-hari, menghentikan pengiriman dan mendorong penggabungan.
- **Terlalu memercayai tinjauan AI:** memperlakukan saran otomatis sebagai otoritatif dan menjatuhkan penilaian manusia pada perubahan berisiko.
- **Memblokir atas preferensi:** menyajikan opini gaya pribadi sebagai perubahan wajib tanpa membedakannya dari cacat nyata.

## Model kematangan

- **Tingkat 1, Memulai:** Tinjauan ad hoc dan reaktif. Sering dilewati atau dilakukan tidak konsisten, isu mekanis mendominasi komentar, norma umpan balik belum ditetapkan, dan jejak persetujuan apa pun bersifat insidental, bukan disengaja.
- **Tingkat 2, Mengembangkan:** Praktik tinjauan dasar ada tetapi bervariasi dari tim ke tim. Tinjauan diwajibkan di beberapa tempat dan lambat atau opsional di tempat lain, otomasi parsial, dan ukuran serta kualitas pull request berayun lebar tanpa ekspektasi bersama.
- **Tingkat 3, Membakukan:** Standar didokumentasikan dan ditegakkan di seluruh organisasi. PR kecil terfokus, format, linting, tes, dan pemindaian keamanan otomatis di CI, daftar periksa yang jelas, konvensi pemblokir-versus-saran yang eksplisit, dan aturan kepemilikan kode yang merutekan perubahan sensitif ke penyetuju yang tepat.
- **Tingkat 4, Mengelola:** Tinjauan diukur dan dikendalikan terhadap garis dasar. Waktu-hingga-tinjauan-pertama, waktu-hingga-gabung, kedalaman tinjauan versus risiko perubahan, tingkat cacat yang lolos, dan tingkat kegagalan perubahan dilacak; latensi berkelanjutan diperlakukan sebagai masalah proses; dan data menentukan di mana menyeimbangkan ulang beban peninjau dan di mana kontrol memperlambat pengiriman tanpa menambah jaminan.
- **Tingkat 5, Mengorkestrasi:** Tinjauan terus diperbaiki dan terintegrasi di seluruh organisasi. Kedalaman beradaptasi dengan risiko perubahan, pairing, mobbing, dan bantuan AI dipakai dengan sengaja dengan manusia yang bertanggung jawab, penyebaran pengetahuan dan risiko bus factor dikelola secara disengaja, dan tinjauan secara terukur memperbaiki kualitas, aliran pengiriman, dan orientasi.

## Gagasan untuk didiskusikan

- Berapa target latensi tinjauan yang tepat untuk tim Anda, dan apa yang mencegah Anda mencapainya?
- Bagaimana Anda menyesuaikan kedalaman tinjauan dengan risiko perubahan tanpa menambah birokrasi?
- Di mana pairing atau mobbing mengungguli tinjauan asinkron dalam konteks Anda?
- Seberapa jauh tinjauan berbantuan AI boleh dipercaya, dan untuk jenis perubahan apa?
- Bagaimana Anda menjaga umpan balik tinjauan tetap konstruktif seiring tim tumbuh dan semakin beragam?
- Bagaimana Anda memenuhi persyaratan persetujuan kepatuhan tanpa menciptakan hambatan?

## Poin-poin utama

- Jaga pull request kecil dan terdeskripsikan baik; penulis memiliki kemudahan tinjauan.
- Otomatiskan yang mekanis agar manusia meninjau desain, kebenaran, dan tes.
- Lacak dan kelola latensi tinjauan sebagai biaya aliran seluruh tim.
- Sesuaikan kedalaman tinjauan dengan risiko perubahan, dan bedakan isu pemblokir dari preferensi.
- Gunakan pairing, mobbing, dan bantuan AI sebagai pelengkap yang sesuai konteks, menjaga manusia tetap bertanggung jawab.

## Referensi dan bacaan lanjutan

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (sebagai contoh rujukan)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (tentang pair programming)
- Woody Zuill, tulisan tentang mob programming
- Michael Lopp, *Managing Humans* (tentang kolaborasi rekayasa)
