# 10.8 Model kematangan

## Tinjauan dan motivasi

[Model kematangan](https://en.wikipedia.org/wiki/Maturity_model) adalah cara terstruktur untuk menilai seberapa mampu dan konsisten praktik Anda di suatu domain, dan untuk menggambarkan jalur memperbaikinya. Ia mendefinisikan tangga kecil berisi tingkat. Di dasar, kerja bersifat ad hoc dan reaktif. Di puncak, kerja diukur, dikelola, dan terus dioptimalkan. Setiap anak tangga punya ciri teramati yang dapat Anda periksa.

Model kematangan mengubah pertanyaan samar ("apakah kita bagus dalam hal ini?") menjadi jawaban yang dapat diulang ("kita di tingkat 2 di sini, tingkat 4 di sana, dan inilah yang dibutuhkan tingkat 3"). Buku ini memakai model lima tingkat di setiap bab dan mengonsolidasikannya di bab 12.4. Bab ini tentang disiplinnya sendiri: bagaimana model bekerja, kapan membantu, dan bagaimana menyesatkan.

Alasan pentingnya sederhana. Organisasi besar tak dapat memperbaiki apa yang tak dapat mereka lihat. Di lusinan tim, kapabilitas sangat bervariasi dan tak terlihat. Sebagian tim punya pengujian luar biasa dan keamanan lemah; yang lain sebaliknya. Model kematangan memberi Anda kosakata bersama dan tolok ukur umum, sehingga celah menjadi dapat dibandingkan, investasi dapat diprioritaskan, dan kemajuan dapat dilacak seiring waktu alih-alih sekadar ditegaskan. Contoh terkenal mencakup CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), untuk proses), model DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (kinerja penyampaian perangkat lunak), OWASP SAMM (Software Assurance Maturity Model) dan BSIMM (Building Security In Maturity Model) untuk keamanan perangkat lunak, TMMi (Test Maturity Model integration, untuk pengujian), model Agile Fluency, dan model kematangan manajemen data, plus papan skor internal yang tak terhitung.

Untuk enterprise dan terutama pemerintah, model kematangan membawa bobot khusus. Kontrak pemerintah sudah lama memakai tingkat penilaian CMMI sebagai kualifikasi pemasok, dan kerangka seperti CMMC AS ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) mengikat kematangan keamanan siber langsung ke kelayakan untuk pekerjaan pertahanan. Itu memberi model kematangan taring nyata. Itu juga menciptakan risiko sentral bab ini: ketika suatu tingkat menjadi gerbang atau target, orang mengoptimalkan penilaian alih-alih kapabilitas mendasar. Dipakai baik, model kematangan adalah cermin. Dipakai buruk, ia teater.

## Prinsip utama

- **Kematangan adalah sarana, bukan tujuan.** Sasarannya kapabilitas dan hasil, bukan angka tingkat.
- **Nilai untuk belajar, bukan untuk mencetak skor.** Penilaian diri jujur mengalahkan penilaian yang menyanjung.
- **Lebih tinggi tak selalu lebih baik.** Target yang tepat bergantung pada risiko, konteks, dan biaya.
- **Ukur per domain, bukan satu nilai global.** Kapabilitas tak merata; satu angka menyembunyikannya.
- **Prioritaskan celah berkematangan terendah dan berisiko tertinggi lebih dulu.**
- **Waspadai [Hukum Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Begitu suatu tingkat menjadi target, ia berhenti mengukur kapabilitas.
- **Nilai ulang secara berkala.** Kematangan melayang seiring orang, sistem, dan ancaman berubah.

## Rekomendasi

### Pilih model yang tepat untuk domain

Cocokkan model dengan kapabilitas yang ingin Anda perbaiki, dan pilih model mapan berbasis bukti daripada yang dikarang bila ada:

- **Proses dan penyampaian:** CMMI (kematangan proses luas), model kapabilitas DORA (kinerja penyampaian, berlandaskan riset, bab 11.2).
- **Keamanan:** OWASP SAMM dan BSIMM (praktik keamanan perangkat lunak), CMMC (keamanan siber pertahanan).
- **Pengujian dan kualitas:** TMMi.
- **Agile dan cara kerja:** model Agile Fluency (bab 10.7).
- **Data:** model kematangan manajemen data (DMM, DCAM).

Untuk penggunaan internal, skala sederhana empat atau lima tingkat yang diterapkan per kapabilitas (seperti dilakukan buku ini) sering lebih dapat ditindaklanjuti daripada kerangka eksternal berat. Cadangkan model formal yang dinilai pihak luar untuk tempat di mana ia diwajibkan secara kontraktual.

### Nilai dengan jujur dan per kapabilitas

Jalankan penilaian yang menghasilkan kebenaran, bukan kenyamanan. Libatkan orang yang mengerjakan. Kumpulkan bukti alih-alih opini. Beri skor setiap kapabilitas secara terpisah, agar gambaran mencerminkan kenyataan: kuat di sini, lemah di sana. Penilaian diri yang dipakai memandu perbaikan lebih berharga daripada penilaian eksternal yang dipakai meraih lencana, karena yang pertama menghargai keterusterangan dan yang kedua menghargai presentasi. Bab 12.4 menyediakan penilaian diri terkonsolidasi di setiap domain dalam buku ini; pakai sebagai instrumen awal.

### Pakai kematangan untuk memprioritaskan, bukan menghukum

Keluaran penilaian adalah backlog perbaikan berprioritas, bukan rapor untuk menyalahkan. Gabungkan kematangan dengan risiko. Kapabilitas tingkat 1 di area berisiko rendah mungkin baik-baik saja. Kapabilitas tingkat 2 di area kritis keselamatan atau kepatuhan mendesak. Arahkan investasi ke celah di mana kematangan rendah bertemu risiko tinggi, dan kaitkan kerja dengan hasil (bab 11.1) agar perbaikan diukur dari hasil, bukan dari mendaki tangga demi tangga itu sendiri.

### Tetapkan tingkat target dengan sengaja: lebih tinggi tidak gratis

Setiap tingkat naik memakan upaya dan sering menambah bobot proses. Target yang tepat jarang "tingkat 5 di mana-mana." Ia tingkat di mana kapabilitas tambahan masih membenarkan biaya tambahan untuk risiko domain itu. Kapabilitas teregulasi dan kritis keselamatan mungkin benar-benar butuh anak tangga teratas, dan audit sering mensyaratkan setidaknya tingkat 3 "terdefinisi". Banyak lainnya terlayani baik di tingkat 3 dan hanya akan menumpuk birokrasi jika didorong lebih jauh. Tentukan target per kapabilitas, dan berhenti mendaki ketika imbal hasil yang disesuaikan risiko berhenti.

### Jaga dari teater kematangan

Satu mode kegagalan yang menghancurkan nilai model kematangan adalah mengoptimalkan skor. Waspadai penilaian yang menilai terlalu murah hati, bukti yang dirakit hanya untuk penilaian, atau klaim "tingkat 5" yang dibantah insiden produksi. Jaga penilaian terikat pada perilaku teramati dan hasil nyata. Rotasi atau periksa penilai Anda secara eksternal. Perlakukan skor diri yang mencurigakan tinggi sebagai bau. Saat tingkat menjadi tujuan, model berhenti mengatakan kebenaran kepada Anda.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| **Model formal yang dinilai (CMMI, CMMC)** | Dapat dibandingkan, diakui secara kontraktual, ketat | Mahal; mengundang akal-akalan; dapat membatukan proses |
| **Papan skor internal ringan** | Cepat, dapat ditindaklanjuti, overhead rendah | Kurang dapat dibandingkan secara eksternal; mudah dibiaskan |
| **Model kapabilitas berbasis bukti (DORA)** | Terikat pada hasil nyata; didukung riset | Cakupan lebih sempit; butuh metrik nyata |
| **Satu nilai kematangan keseluruhan** | Sederhana dikomunikasikan | Menyembunyikan kapabilitas tak merata; menyesatkan |
| **Penilaian per kapabilitas** | Prioritisasi akurat dan dapat ditindaklanjuti | Lebih banyak upaya; tanpa angka judul tunggal |

Ketegangan sentralnya **penilaian sebagai cermin vs. penilaian sebagai target**. Model yang sama yang membantu tim melihat dirinya dengan jelas menjadi kontraproduktif seketika suatu tingkat diikat pada imbalan, kelayakan, atau status. Makin penting suatu tingkat, makin banyak energi mengalir ke penampakan kematangan alih-alih substansinya.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Haruskah kita menjaga penilaian diri internal yang terus terang terpisah dari tingkat yang dinilai secara kontraktual, dan siapa memiliki masing-masing?** Ketika tingkat CMMC atau CMMI menggerbangi pendapatan, penilaian dan kebenaran saling menjauh, karena energi mengalir ke lulus alih-alih memperbaiki. Bagi enterprise besar atau pemasok pemerintah, celah itu adalah tempat risiko bersembunyi: Anda lulus audit dan tetap terpapar. Jalankan dua buku dengan sengaja. Simpan penilaian formal untuk kelayakan, dan simpan papan skor internal blak-blakan yang tak ada orang dihargai karena menggelembungkannya. Namai pemilik untuk masing-masing, dan perlakukan jarak apa pun di antaranya sebagai sinyal untuk diselidiki, bukan untuk ditutup-tutupi. Bawa insiden terbaru, nyaris-celaka, dan pembusukan pasca-penilaian ke rapat sebagai bukti buku mana yang mengatakan kebenaran.

2. **Untuk setiap domain, apakah kita mengadopsi model mapan berbasis bukti atau mengarang papan skor sendiri, dan apakah itu keputusan yang tepat?** Model mapan (DORA untuk penyampaian, SAMM atau BSIMM untuk keamanan, TMMi untuk pengujian) membawa riset dan keterbandingan eksternal yang tak dapat ditandingi kisi buatan sendiri. Skala internal empat tingkat yang ringan lebih cepat dan lebih dapat ditindaklanjuti, dan sering pilihan lebih baik untuk kemudi internal. Jebakannya adalah mengarang kerangka khusus yang berat dengan semua upacara model formal dan tanpa dasar bukti. Putuskan per domain: cadangkan model formal yang dinilai untuk tempat kontrak mewajibkannya, pakai model berbasis bukti bila ada dan cocok, dan simpan skala per kapabilitas sederhana untuk sisanya. Bawa daftar domain, tandai model mana yang dipakai masing-masing hari ini, dan tantang setiap papan skor karangan.

3. **Siapa yang menjalankan penilaian kita, bagaimana kita menangkap penilaian yang murah hati, dan seberapa sering kita menilai ulang?** Penilaian yang menilai dirinya sendiri menyanjung dirinya sendiri, dan kematangan melayang seiring orang, sistem, dan ancaman berubah, sehingga penilaian berumur dua tahun sering fiksi. Rotasi penilai atau datangkan pemeriksa eksternal, dan perlakukan skor diri yang mencurigakan tinggi sebagai bau untuk dikejar, bukan kemenangan untuk dirayakan. Tetapkan irama penilaian ulang yang terkait seberapa cepat tiap domain berubah: keamanan lebih sering daripada, katakanlah, dokumentasi. Kumpulkan bukti dan libatkan orang yang mengerjakan alih-alih mengumpulkan opini dari manajer. Jika jawaban Anda satu tim menilai dirinya sendiri setahun sekali tanpa pemeriksaan silang, Anda mengukur kenyamanan, bukan kapabilitas.

4. **Tingkat kematangan target apa yang sebenarnya dibutuhkan tiap kapabilitas, dan di mana mendorong lebih tinggi hanya membeli bobot proses?** Lebih tinggi tidak gratis: setiap tingkat naik memakan upaya dan biasanya menambah upacara, sehingga sasaran menyeluruh tingkat 5 di mana-mana menguras anggaran perbaikan terbatas ke birokrasi yang tak akan dibayar lunas oleh sebagian domain. Bagi organisasi besar target yang tepat bervariasi menurut kapabilitas, karena area berisiko rendah di tingkat 2 mungkin sepenuhnya aman sementara area kritis keselamatan atau kepatuhan di tingkat yang sama adalah darurat. Bawa peringkat risiko per kapabilitas, perkiraan jujur berapa biaya anak tangga berikutnya dalam upaya dan proses, dan lantai audit atau kontraktual apa pun, karena banyak audit mensyaratkan setidaknya tingkat 3 terdefinisi. Dalam pengaturan enterprise dan pemerintah, sebagian kapabilitas teregulasi benar-benar butuh anak tangga teratas sementara kebanyakan terlayani baik di tingkat 3, jadi tentukan target dengan sengaja, kapabilitas demi kapabilitas, dan berhenti mendaki begitu imbal hasil yang disesuaikan risiko berhenti.

5. **Terakhir kali kita menaikkan tingkat kematangan, apakah hasil yang hendak dilindunginya benar-benar membaik, atau hanya skor yang bergerak?** Tingkat yang naik sementara insiden, lead time, atau laju cacat tetap datar adalah Hukum Goodhart beraksi: begitu angka menjadi target, ia berhenti mengukur kapabilitas. Bagi tim besar ini lolos dengan mudah, karena penilaian yang berhasil terasa seperti kemajuan bahkan ketika produksi bercerita lain. Ikat tingkat tiap kapabilitas pada metrik hasil nyata sebelum Anda berinvestasi, lalu bawa bukti sebelum-dan-sesudah ke diskusi: insiden per kuartal, laju kegagalan perubahan, waktu pemulihan, apa pun yang ingin diperbaiki kapabilitas itu. Dalam portofolio enterprise dan pemerintah di mana tingkat yang dinilai menggerbangi kelayakan, celahnya berbahaya, karena tingkat dapat naik atas bukti yang dirakit sementara praktik mendasar diam-diam membusuk, dan bukti pertamanya adalah pembobolan, pemadaman, atau audit gagal.

6. **Apakah kita mengomunikasikan satu nilai kematangan judul atau gambaran per kapabilitas, dan apakah tingkat pernah diikat pada imbalan, peringkat, atau kedudukan tim?** Satu angka keseluruhan mudah dipresentasikan kepada pimpinan dan menyembunyikan persis ketaksamaan yang penting, karena penyampaian kuat dapat menutupi kapabilitas keamanan tingkat 1; peta panas per kapabilitas lebih banyak kerja namun menunjukkan di mana kematangan rendah bertemu risiko tinggi. Pertanyaan yang lebih sulit adalah bagaimana skor dipakai, karena saat tingkat diikat pada imbalan atau peringkat tim, pelaporan jujur mati dan upaya mengalir ke penampakan kematangan alih-alih substansi. Bawa peta panas, dan catatan terus terang setiap tempat di mana tingkat saat ini memberi makan tinjauan kinerja, keputusan anggaran, atau kartu skor vendor. Untuk enterprise dan pemasok pemerintah, di mana tingkat yang dinilai dapat menggerbangi pendapatan dan kelayakan, jelaskan nilai mana yang membawa konsekuensi dan mana yang hanya ada untuk mengemudikan, karena gambaran kematangan yang orang dihargai karena menggelembungkannya berhenti menggambarkan kenyataan.

## Lensa sektor

**Startup.** Model formal yang dinilai adalah overhead yang tak sanggup Anda tanggung di runway pendek. Jalankan penilaian diri satu jam pada skala sederhana di segelintir kapabilitas, perbaiki hanya celah berkematangan terendah yang menghalangi sesuatu yang konkret (katakanlah, kuesioner keamanan dari pelanggan enterprise pertama Anda), dan biarkan sisanya. Penilaian harus berbiaya satu sore, bukan konsultan, dan keluarannya satu tindakan berikutnya alih-alih skor tinggi seragam yang tak Anda butuhkan maupun sanggup danai.

**Bisnis kecil.** Tanpa penilai khusus dan anggaran ketat, pinjam model publik ringan alih-alih memesan kerangka khusus: daftar periksa penyampaian atau keamanan singkat yang dapat Anda beri skor sendiri. Perlakukan sebagai percakapan tahunan tentang di mana titik lemah akan membuat Anda kehilangan pelanggan, bukan program tetap. Jaga murah dan blak-blakan, karena skor menyanjung yang Anda bayar vendor untuk menghasilkannya kurang berharga daripada yang jujur yang Anda kerjakan sendiri dalam satu sore.

**Enterprise.** Nilainya adalah papan skor per kapabilitas bersama yang diterapkan konsisten di banyak tim, sehingga celah menjadi dapat dibandingkan dan anggaran perbaikan mengalir ke tempat kematangan rendah bertemu risiko tinggi. Jaga keras dari teater kematangan begitu tingkat memberi makan anggaran atau status: rotasi atau periksa penilai secara eksternal, dan kelola hasil sebagai peta panas yang mengarahkan investasi jalur beraspal (bab 4.2) alih-alih tabel liga yang meranking tim dan membunuh pelaporan jujur.

**Pemerintah.** Tingkat kematangan sering harfiah sebuah gerbang di sini: CMMC untuk pekerjaan pertahanan, penilaian CMMI sebagai kualifikasi pemasok. Penuhi tingkat yang disyaratkan dengan kapabilitas sejati, dan jaga penilaian diri internal yang terus terang terpisah dari penilaian formal agar lantai audit tak diam-diam menjadi langit-langit. Dokumentasikan bukti secara transparan bagi penilai, dan perlakukan jarak antara tingkat tersertifikasi dan praktik nyata sebagai risiko akuntabel untuk ditutup, bukan administrasi untuk diarsipkan.

## Contoh

**Startup.** Startup SaaS sepuluh orang menjalankan penilaian diri satu jam terhadap skala empat tingkat sederhana yang mencakup penyampaian, pengujian, keamanan, dan on-call. Ia menemukan penyampaian dan pengujian di tingkat 3 tetapi keamanan macet di tingkat 1, yang penting karena ia akan menandatangani pelanggan enterprise pertamanya dengan kuesioner keamanan. Maka para pendiri menghabiskan bulan berikutnya menaikkan hanya keamanan ke tingkat 2 yang dapat dipertahankan dan membiarkan sisanya, alih-alih mengejar skor tinggi seragam yang belum mereka butuhkan maupun sanggup danai.

**Enterprise.** Sebuah firma jasa keuangan menilai 40 timnya dengan papan skor per kapabilitas ringan (penyampaian, pengujian, keamanan, observabilitas, on-call). Peta panas mengungkap bahwa kematangan keamanan paling tertinggal di tempat paparan regulasi tertinggi, sehingga tim platform mendanai perkakas keamanan jalur beraspal (bab 4.2) untuk tim-tim itu lebih dulu. Karena penilaian dipakai memprioritaskan investasi alih-alih meranking tim, manajer melapor jujur. Penilaian ulang setahun kemudian menunjukkan pergerakan nyata, dan, yang krusial, insiden keamanan lebih sedikit, bukan hanya skor lebih tinggi.

**Pemerintah.** Kontraktor pertahanan harus mencapai tingkat CMMC yang disyaratkan untuk menawar pekerjaan, dan integrator sistem memegang penilaian CMMI sebagai kualifikasi kontrak. Di sini tingkat kematangan adalah gerbang harfiah menuju pendapatan. Versi yang dijalankan baik memperlakukan tingkat yang disyaratkan sebagai lantai untuk kapabilitas sejati dan menjaga penilaian diri internal yang terus terang terpisah dari penilaian formal. Versi yang dijalankan buruk merakit bukti untuk penilaian dan membiarkan praktik nyata membusuk sehari sesudahnya, lulus audit sambil tetap terpapar.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil penilaian kematangan datang dari **investasi terarah**. Anggaran perbaikan terbatas. Dibelanjakan buta, ia mendanai apa pun yang paling lantang. Penilaian kematangan menunjukkan di mana kapabilitas paling lemah terhadap risiko, sehingga belanja yang sama membeli lebih banyak pengurangan risiko dan perbaikan hasil. Penilaian itu sendiri murah, hanya berhari-hari tinjauan terstruktur berbasis bukti, dibandingkan dengan biaya program perbaikan yang salah alokasi atau, lebih buruk, celah kapabilitas tak terdeteksi yang muncul sebagai pembobolan, pemadaman, atau audit gagal.

Pada **total biaya kepemilikan**, disiplin ini murah ketika Anda menjaganya ringan dan mahal ketika ia mengeras menjadi birokrasi penilaian. Biaya tersembunyi dominan adalah *teater kematangan*: upaya yang dihabiskan menghasilkan penampakan kematangan tak mengembalikan apa pun dan dapat menutupi risiko nyata, yang berarti ROI negatif. Untuk mengajukan kasus kepada pimpinan, sajikan kematangan sebagai lensa risiko-dan-investasi, peta panas yang mengubah "perbaiki semuanya" menjadi "perbaiki tiga hal ini dulu," dan anggarkan secara eksplisit melawan godaan mengejar tingkat demi tingkat itu sendiri. Di mana tingkat diwajibkan secara kontraktual (CMMC, CMMI), ROI-nya langsung: itu harga kelayakan, dan tujuannya memenuhinya dengan kapabilitas nyata alih-alih kepura-puraan mahal.

## Anti-pola dan jebakan

- **Tingkat sebagai tujuan:** mengejar angka alih-alih kapabilitas yang dimaksudkan diwakilinya.
- **Teater kematangan:** merakit bukti untuk penilaian sementara praktik nyata membusuk.
- **Satu nilai global:** skor kematangan tunggal yang menyembunyikan ketaksamaan berbahaya.
- **Lebih-tinggi-selalu-lebih-baik:** mendorong setiap kapabilitas ke tingkat 5 terlepas dari risiko atau biaya.
- **Nilai sekali, tak pernah lagi:** penilaian sekali jalan diperlakukan sebagai kebenaran permanen.
- **Meranking tim untuk menyalahkan:** memakai kematangan untuk hukuman, yang membunuh pelaporan jujur.
- **Pemujaan model:** mengikuti upacara kerangka berat melampaui titik gunanya.
- **Mengabaikan hasil:** mendaki tangga sementara penyampaian, keandalan, atau keamanan tidak membaik.

## Model kematangan

- **Tingkat 1, Memulai.** Tak ada gagasan bersama tentang kematangan; kapabilitas diasumsikan, tak merata, dan tak terukur; penilaian apa pun bersifat reaktif, dipicu insiden atau tuntutan audit alih-alih terencana.
- **Tingkat 2, Mengembangkan.** Beberapa tim menjalankan penilaian ad hoc terhadap suatu skala, tetapi model, irama, dan ketelitian bervariasi tim demi tim; hasil dipakai tak konsisten dan bukti tipis, sehingga menilai demi penampakan adalah risiko yang selalu ada.
- **Tingkat 3, Membakukan.** Satu model per kapabilitas dan irama penilaian didokumentasikan dan diterapkan di seluruh organisasi; penilaian berbasis bukti, melibatkan orang yang mengerjakan, dan memberi makan backlog perbaikan berprioritas alih-alih rapor.
- **Tingkat 4, Mengelola.** Kematangan diukur dan dikendalikan dengan data: tingkat tiap kapabilitas dilacak terhadap garis dasar, diikat pada metrik hasil (insiden, lead time, laju kegagalan perubahan), dan dinilai ulang pada irama tetap, sehingga drift dan penilaian murah hati muncul sebagai angka alih-alih opini, dan target ditetapkan dengan sengaja per domain terhadap risiko dan biaya.
- **Tingkat 5, Mengorkestrasi.** Penilaian terintegrasi di seluruh organisasi dan terus diperbaiki: kematangan, risiko, dan hasil menginformasikan investasi sebagai satu gambaran adaptif, target diseimbangkan ulang seiring ancaman dan konteks bergeser, penilai dirotasi atau diperiksa secara eksternal sebagai hal biasa, dan praktik aktif memensiunkan upacara yang tak lagi sepadan biayanya.

## Gagasan untuk didiskusikan

1. Kapabilitas Anda yang mana yang Anda asumsikan matang tanpa bukti?
2. Di mana kematangan terendah Anda bertepatan dengan risiko tertinggi Anda, dan apakah ke sanalah anggaran perbaikan Anda pergi?
3. Apakah tingkat kematangan apa pun di organisasi Anda adalah target atau gerbang? Perilaku apa yang dihasilkannya?
4. Apa tingkat target yang tepat untuk setiap kapabilitas, dan di mana mendaki lebih jauh hanya menambah birokrasi?
5. Apakah tim Anda akan melaporkan kematangan mereka dengan jujur, atau cara Anda memakai skor menghukum keterusterangan?
6. Ketika terakhir Anda "meningkatkan kematangan," apakah hasil benar-benar berubah?

## Poin-poin utama

- Model kematangan menilai kapabilitas terhadap tangga tingkat dan menggambarkan jalur memperbaiki: cermin, bukan trofi.
- Pilih model mapan berbasis bukti per domain (CMMI, DORA, SAMM/BSIMM, CMMC); skala per kapabilitas ringan sering paling dapat ditindaklanjuti.
- **Nilai dengan jujur, per kapabilitas**, dan pakai hasilnya untuk **memprioritaskan menurut risiko**, bukan untuk meranking atau menyalahkan.
- **Lebih tinggi tak selalu lebih baik:** tetapkan tingkat target dengan sengaja terhadap risiko dan biaya.
- Waspadai **teater kematangan** dan **Hukum Goodhart**: tingkat yang menjadi target berhenti mengukur kapabilitas.
- Lihat bab 12.4 untuk penilaian diri kematangan terkonsolidasi buku ini, dan bagian kematangan setiap bab.

## Referensi dan bacaan lanjutan

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (asal-usul kematangan proses perangkat lunak).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (pemikiran kapabilitas, bukan tingkat kematangan, untuk penyampaian).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore dan Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), tentang penggunaan dan penyalahgunaannya.
