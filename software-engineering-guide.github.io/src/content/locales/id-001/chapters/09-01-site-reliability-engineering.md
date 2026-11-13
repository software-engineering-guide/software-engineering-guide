# 9.1 Site reliability engineering

## Tinjauan dan motivasi

[Site reliability engineering](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) menerapkan praktik rekayasa perangkat lunak pada menjalankan sistem produksi. Alih-alih memperlakukan operasi sebagai kerja manual digerakkan tiket yang terpisah dari pengembangan, SRE memperlakukan keandalan sebagai masalah rekayasa yang Anda selesaikan dengan kode, pengukuran, dan tujuan layanan yang jelas. Gagasan intinya, dipopulerkan Google tetapi kini luas, sederhana: orang yang menjaga sistem tetap berjalan harus menghabiskan sebagian besar waktunya membangun otomasi dan memperbaiki sistem, bukan memadamkan kegagalan yang sama dengan tangan berulang kali.

Bagi tim besar, ini penting karena skala menaikkan nilai keandalan sekaligus biaya salah menatanya. Ketika satu layanan mendukung jutaan pengguna atau ribuan konsumen internal, satu jam downtime berarti pendapatan hilang, transaksi terlewat, dan kepercayaan terkikis. Operasi manual yang berfungsi baik untuk segelintir server runtuh di bawah ratusan layanan dan [deployment berkelanjutan](https://en.wikipedia.org/wiki/Continuous_deployment). SRE memberi Anda bahasa bersama untuk keandalan, cara membuat trade-off antara mengirim fitur dan menjaga kestabilan menjadi eksplisit, dan cara mempertahankan garis itu secara konsisten di banyak tim.

Konteks enterprise dan pemerintah menambah bobot. Industri teregulasi seperti perbankan, kesehatan, dan layanan publik sering memikul komitmen ketersediaan hukum atau kontraktual, persyaratan audit, dan sedikit toleransi terhadap pemadaman yang memengaruhi warga atau keselamatan. Layanan digital pemerintah makin menerbitkan target keandalan dan data kinerjanya secara terbuka. SRE memberi Anda cara yang ketat dan berbasis bukti untuk mendefinisikan apa arti "cukup andal," mengukurnya dengan jujur, dan membela prioritas rekayasa kepada pimpinan dan badan pengawas dengan data alih-alih opini.

*Lihat juga:* bab 9.2 (observabilitas dan pemantauan), bab 9.3 (manajemen insiden), dan bab 3.5 (skalabilitas, kinerja, dan ketahanan).

## Prinsip utama

- **Keandalan adalah fitur terpenting.** Sistem yang tidak berfungsi tak berharga seberapa pun banyak fiturnya, tetapi keandalan sempurna tidak dapat dicapai maupun sepadan biayanya.
- **Definisikan keandalan dengan tujuan terukur.** Service level indicator (SLI), objective (SLO), dan agreement (SLA) mengubah ekspektasi samar menjadi angka yang dapat disepakati semua orang.
- **100 persen adalah target yang salah.** Pengguna tak dapat membedakan sistem yang sangat andal dan yang sempurna andal, jadi bidik "cukup andal" dan belanjakan sisa anggaran untuk kecepatan.
- **Anggaran galat menyelaraskan insentif.** Selisih antara SLO dan 100 persen adalah anggaran risiko yang dibagi pengembang dan operator, menggantikan perdebatan dengan aritmetika.
- **Toil adalah musuh.** Kerja operasional yang berulang, manual, dan dapat diotomatisasi harus diukur, dibatasi, dan dihilangkan secara sistematis.
- **Otomatiskan dengan sengaja.** Otomasi adalah cara tim kecil mengoperasikan sistem besar; berinvestasi di dalamnya adalah aktivitas rekayasa kelas satu.
- **Pembelajaran tanpa menyalahkan.** Kegagalan diperlakukan sebagai peluang memperbaiki sistem dan proses, bukan menghukum individu.

## Rekomendasi

### Definisikan SLI, SLO, dan SLA dengan sengaja

Mulailah dari sudut pandang pengguna. **[Service level indicator](https://en.wikipedia.org/wiki/Service-level_indicator)** adalah ukuran kuantitatif perilaku layanan, seperti proporsi permintaan yang dilayani di bawah 300 milidetik atau pecahan respons sukses. Pilih sejumlah kecil SLI yang benar-benar mencerminkan kebahagiaan pengguna: ketersediaan, latensi, kebenaran, dan kesegaran adalah yang umum. **[Service level objective](https://en.wikipedia.org/wiki/Service-level_objective)** adalah nilai atau rentang target untuk SLI, misalnya "99,9 persen permintaan sukses dalam jendela bergulir 28 hari." **[Service level agreement](https://en.wikipedia.org/wiki/Service-level_agreement)** adalah kontrak dengan konsekuensi (pengembalian dana, penalti) yang melekat pada tingkat yang dijanjikan. Jaga SLO Anda lebih ketat daripada SLA, agar Anda mendapat peringatan sebelum melanggar komitmen. Terbitkan SLO Anda, tinjau setiap kuartal, dan perlakukan sebagai dokumen hidup yang mengetat atau melonggar seiring Anda belajar.

### Adopsi anggaran galat dan tegakkan

Anggaran galat adalah `100% dikurangi SLO`. Jika SLO Anda 99,9 persen, anggaran Anda 0,1 persen ketidakandalan per jendela, sekitar 43 menit per bulan. Belanjakan untuk risiko terencana: rilis agresif, eksperimen, dan uji kegagalan terkendali. Ketika anggaran sehat, tim dapat mengirim cepat. Ketika habis, kebijakan harus otomatis menggeser prioritas ke kerja keandalan dan menghentikan perubahan berisiko sampai sistem pulih. Kekuatan anggaran galat adalah Anda menyepakatinya di muka, sehingga ia menghilangkan emosi dan politik dari saat pemadaman.

### Ukur dan kurangi toil

Toil adalah kerja operasional yang manual, berulang, dapat diotomatisasi, taktis, dan tumbuh seiring sistem. Lacak persentase waktu SRE yang dihabiskan untuk toil dan tetapkan plafon, biasanya sekitar 50 persen, agar setidaknya separuh waktu rekayasa Anda tercurah untuk perbaikan tahan lama. Simpan backlog proyek pengurangan toil, prioritaskan menurut frekuensi dikali biaya, dan rayakan membunuh tugas berulang sebanyak mengirim fitur baru. **Mandat otomasi** membuat ini eksplisit: prosedur manual apa pun yang Anda lakukan lebih dari jumlah kali tertentu menjadi kandidat otomasi atau perkakas swalayan.

### Rencanakan kapasitas dan perkirakan permintaan

Modelkan beban yang diharapkan dari tren historis, peluncuran terencana, dan proyeksi bisnis. Gabungkan perkiraan pertumbuhan organik dengan peristiwa sekali jalan seperti kampanye pemasaran, tenggat pajak, atau periode pendaftaran tunjangan yang sangat penting di pemerintah. Jaga ruang kepala di atas puncak, uji beban untuk memeriksa asumsi Anda, dan otomatiskan penskalaan di mana bisa sambil menjaga [rencana kapasitas](https://en.wikipedia.org/wiki/Capacity_planning) yang ditinjau manusia untuk komitmen besar. Lacak lead time penyediaan agar kekurangan tak pernah menangkap Anda lengah.

### Perlakukan keandalan sebagai fitur dengan biaya nyata

Setiap "sembilan" tambahan ketersediaan biasanya berbiaya jauh lebih banyak dalam redundansi, pengujian, dan kecanggihan operasional daripada yang sebelumnya. Jadikan biaya sembilan eksplisit, agar pemilik produk memilih target dengan mata terbuka. Rancang untuk degradasi anggun, agar kegagalan parsial memberi layanan berkurang alih-alih pemadaman total. Berinvestasilah pada redundansi dan failover sebanding dengan SLO, bukan merata di setiap komponen.

### Pilih model organisasi SRE

Tak ada satu struktur yang benar. Tim SRE **terpusat** memberi konsistensi, keahlian mendalam, dan perkakas bersama, tetapi dapat menjadi hambatan atau tempat pembuangan masalah orang lain. Model **tertanam** menempatkan SRE di dalam tim produk untuk kolaborasi erat, tetapi berisiko inkonsistensi dan isolasi. Banyak organisasi besar memakai hibrida: tim platform dan standar pusat plus insinyur keandalan tertanam, dengan model keterlibatan jelas yang mendefinisikan kapan layanan memenuhi syarat untuk dukungan SRE dan batas kesiapan produksi apa yang harus dilewatinya lebih dulu.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| SLO ketat (lebih banyak sembilan) | Kepercayaan pengguna lebih tinggi, memenuhi kontrak | Biaya naik, pengiriman fitur lebih lambat |
| SLO longgar (lebih sedikit sembilan) | Mengirim lebih cepat, biaya lebih rendah | Risiko pengguna pergi dan penalti SLA |
| SRE terpusat | Konsistensi, keahlian bersama | Hambatan, jauh dari produk |
| SRE tertanam | Kolaborasi erat, konteks | Inkonsistensi, sulit diisi staf |
| Investasi otomasi berat | Berskala, mengurangi toil | Biaya di muka, otomasi sendiri dapat gagal |

Rekayasa keandalan sebenarnya tentang membelanjakan sumber daya terbatas dengan bijak. Mengejar sembilan tambahan yang bahkan tak dapat dirasakan pengguna memboroskan uang yang dapat mendanai fitur atau menurunkan harga. Sebaliknya, kurang berinvestasi pada sistem yang kegagalannya menyebabkan kerugian nyata adalah kelalaian. Kerangka anggaran galat ada justru untuk membuat trade-off ini terlihat dan dapat dinegosiasikan alih-alih implisit dan memicu perselisihan. Trade-off model organisasi sama nyatanya: jawaban yang tepat bergantung pada ukuran perusahaan, kematangan rekayasa, dan seberapa seragam layanan Anda.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **SLI persis mana yang mencerminkan apa yang benar-benar dirasakan pengguna Anda, dan dapatkah Anda menunjukkan ia bukan metrik kesombongan?** Pilih indikator yang salah dan setiap dasbor tampak hijau sementara pengguna menderita, yaitu jebakan SLI kesombongan yang diperingatkan bab ini. Bawa data nyata ke diskusi: ukur perjalanan pengguna yang sama dari jalur permintaan nyata (login ke dasbor, checkout ke konfirmasi) alih-alih CPU server atau pemeriksaan kesehatan backend. Bagi tim besar, satu SLI buruk merambat: puluhan layanan mewarisinya, peringatan menyala pada hal yang salah, dan anggaran galat berhenti bermakna. Dalam pengaturan enterprise dan pemerintah di mana SLA membawa pengembalian dana atau dampak pada warga, SLI Anda adalah bukti yang Anda bela kepada auditor, jadi ia harus langsung dapat ditelusuri ke keberhasilan terlihat pengguna. Jika Anda tak dapat menarik garis dari angka ke pengalaman pengguna, ganti angkanya.

2. **Apa yang harus dibuktikan layanan sebelum tim SRE Anda mengambilnya on-call, dan siapa yang mengatakan tidak?** Tanpa batas kesiapan produksi, tim SRE pusat menjadi tempat pembuangan setiap layanan tak stabil dan tenggelam dalam utang teknis orang lain. Tuliskan kriteria masuk: SLO yang dimiliki, runbook berfungsi, peringatan yang dapat ditindaklanjuti, ruang kapasitas, dan jalur deploy-dan-rollback yang didemonstrasikan. Bagi organisasi besar model keterlibatan ini yang menjaga tim keandalan agar tidak menjadi hambatan yang memperlambat semua orang. Dalam pengaturan teregulasi tinjauan kesiapan berfungsi ganda sebagai kontrol yang dapat Anda tunjukkan kepada badan pengawas. Putuskan siapa yang memegang wewenang menolak onboarding, karena batas yang tak ditegakkan siapa pun bukan batas, dan jawabannya mengubah apakah SRE berskala atau runtuh di bawah nyeri warisan.

3. **Seberapa jauh di muka Anda menyediakan kapasitas untuk puncak terprediksi terbesar Anda, dan apakah Anda tahu lead time penyediaan Anda?** Mengasumsikan elastisitas cloud instan dan tak terbatas mengundang kekurangan selama puncak yang paling penting, dan puncak itu (tenggat pajak, jendela pendaftaran, peristiwa obral) adalah saat kegagalan paling terlihat dan paling mahal. Bawa angkanya: beban puncak historis, perkiraan pertumbuhan, kelipatan yang Anda uji beban, dan lead time nyata memperoleh kapasitas reservasi besar atau instans khusus. Untuk layanan musiman pemerintah puncaknya bisa beberapa kali beban normal dan tak mungkin terlewat secara politik, jadi menyediakan berminggu-minggu di muka mengalahkan berharap autoscaling mengimbangi. Jawabannya harus menetapkan kalender konkret: kapan Anda menguji beban, kapan Anda mengunci kapasitas, dan siapa yang memiliki keputusan go.

4. **Ketika anggaran galat Anda habis, apa yang sebenarnya terjadi, dan siapa yang berwenang menegakkannya?** Anggaran galat yang tak pernah ditindaklanjuti ketika habis hanyalah hiasan, dan saat pemadaman adalah waktu terburuk untuk menegosiasikan kebijakan dari nol. Tarikan yang bersaing nyata: peluncuran yang dijanjikan, tenggat pendapatan, atau pengumuman publik akan menekan keras terhadap pembekuan perubahan berisiko. Bawa data burn-rate, teks kebijakan yang disepakati di muka, dan catatan beberapa kali terakhir anggaran dilanggar, agar Anda dapat melihat apakah pembekuan benar-benar bertahan. Bagi tim besar anggaran hanya menyelaraskan insentif jika setiap kelompok mewarisi penegakan yang sama, jadi putuskan di muka siapa yang menandatangani override dan bagaimana pengecualian itu dicatat. Dalam pengaturan enterprise dan pemerintah di mana SLA membawa penalti atau dampak pada warga, jejak override menjadi artefak audit, jadi namai pemilik akuntabel sekarang alih-alih berimprovisasi ketika anggaran sudah habis.

5. **Berapa pecahan minggu tim SRE Anda yang berupa toil, dan apakah itu angka terukur atau perasaan?** Toil yang tak dihitung siapa pun diam-diam mengembang sampai tim menghabiskan semua waktunya memadamkan kebakaran dan tak ada yang membangun perbaikan tahan lama, yang persis jebakan yang ada untuk dihindari SRE. Ketegangannya adalah mengukur toil sendiri adalah kerja, dan insinyur di bawah tekanan tenggat menolak mencatat ke mana jam mereka pergi. Bawa sampel jujur: satu atau dua minggu waktu terlacak terhadap definisi toil bersama (manual, berulang, dapat diotomatisasi, taktis, dan berskala dengan sistem), plus backlog proyek otomasi yang diperingkat menurut frekuensi dikali biaya. Untuk organisasi besar plafon 50 persen hanya bermakna jika dilaporkan dan dibela tim demi tim, jadi sepakati siapa yang meninjau angka dan apa yang terjadi ketika tim melanggarnya. Dalam konteks teregulasi dan pemerintah, membatasi toil membebaskan spesialis langka untuk kerja kontrol dan audit yang terdesak operasi manual, jadi perlakukan angka toil sebagai sinyal kapasitas yang harus dilihat pimpinan.

6. **Model organisasi SRE mana yang Anda jalankan, dan bukti apa yang akan memberi tahu bahwa ia berhenti cocok?** Tim terpusat memberi konsistensi dan perkakas bersama tetapi dapat menjadi hambatan; model tertanam memberi konteks tetapi menyimpang ke inkonsistensi; hibrida yang dipilih sebagian besar organisasi besar butuh model keterlibatan jelas atau ia mewarisi kelemahan keduanya. Bawa sinyal yang mengungkap ketegangan: berapa lama layanan menunggu dukungan SRE, seberapa banyak praktik keandalan bervariasi antartim, dan apakah insinyur tertanam merasa terputus dari komunitas profesional. Jawaban yang tepat bergantung pada ukuran perusahaan, kematangan rekayasa, dan seberapa seragam layanan Anda, jadi tinjau ulang seiring itu berubah alih-alih memperlakukan pilihan pertama sebagai permanen. Untuk badan enterprise atau pemerintah dengan banyak tim dan persyaratan keseragaman ketat, kelompok standar-dan-platform pusat plus insinyur keandalan tertanam biasanya menyeimbangkan konsistensi terhadap konteks lokal, tetapi hanya jika model keterlibatan dan batas kesiapan produksi tertulis dan ada yang memilikinya.

## Lensa sektor

**Startup.** Dengan segelintir insinyur dan tanpa runway untuk tim keandalan khusus, pilih satu SLO pada perjalanan pengguna yang paling penting dan bagi on-call ke seluruh tim. Bersandarlah pada layanan terkelola penyedia cloud Anda dan pemantauan bawaan alih-alih membangun infrastruktur observabilitas, dan tulis postmortem singkat di dokumen bersama agar perbaikan melekat. Kecepatan lebih penting daripada proses di sini: SLO longgar yang benar-benar Anda tegakkan mengalahkan yang rumit yang tak diawasi siapa pun.

**Bisnis kecil.** Tanpa spesialis untuk menjalankan keandalan, perlakukan sebagai disiplin yang Anda beli lewat platform Anda: pemantauan uptime ter-hosting, basis data terkelola, dan perkakas halaman status alih-alih tumpukan pesanan. Tetapkan satu atau dua SLO yang terikat pada transaksi yang membayar tagihan, dan putuskan dengan jujur kegagalan mana yang akan membuat Anda kehilangan pelanggan. Beli ketahanan di mana lebih murah daripada membangun, dan jaga beban operasional cukup ringan agar insinyur Anda yang ada dapat memikulnya di samping kerja fitur.

**Enterprise.** Tantangannya konsistensi lintas banyak tim: kosakata SLO bersama, kebijakan anggaran galat umum, dan batas kesiapan produksi yang dilewati setiap layanan sebelum SRE mengambilnya on-call. Kelompok platform-dan-standar pusat plus insinyur keandalan tertanam menjaga praktik seragam tanpa menjadi hambatan, dan tata kelola membutuhkan anggaran galat dilaporkan dan ditegakkan sama di mana-mana. Anggarkan infrastruktur observabilitas dan investasi otomasi secara eksplisit, dan kelola keandalan sebagai portofolio dengan metrik yang dapat dilihat pimpinan.

**Pemerintah.** Layanan publik sering membawa target ketersediaan terbitan, komitmen undang-undang, dan kewajiban audit, sehingga keputusan SLO dan anggaran galat menjadi catatan yang Anda bela kepada badan pengawas. Aturan pengadaan dapat membatasi pemantauan dan hosting yang dapat Anda pakai, dan ekspektasi transparansi mendorong Anda menerbitkan data keandalan di dasbor status publik. Rencanakan puncak musiman ekstrem seperti tenggat pajak dan jendela pendaftaran tunjangan berminggu-minggu di muka, dan jaga budaya postmortem tanpa menyalahkan agar kegagalan publik mendorong perbaikan sistem alih-alih menyalahkan individu.

## Contoh

**Startup.** Startup sepuluh orang menjalankan satu aplikasi web dan membagi on-call di antara tiga insinyur. Alih-alih membangun tim keandalan yang tak mampu dibayar, ia memilih satu SLO bermakna: 99,5 persen keberhasilan pada alur login-ke-dasbor, diukur dari permintaan pengguna nyata. Ketika API pihak ketiga yang flaky mulai menghabiskan anggaran itu, tim menghabiskan satu hari Jumat menambah retry dan cache alih-alih mengirim fitur berikutnya, lalu menulis postmortem dua paragraf di dokumen bersama agar perbaikan melekat.

**Enterprise.** Sebuah perusahaan pembayaran global menetapkan SLO ketersediaan 99,99 persen untuk API transaksinya, yang memberi anggaran galat sekitar empat menit per bulan. Tim platform SRE pusat memiliki [observabilitas](https://en.wikipedia.org/wiki/Observability_(software)) bersama, perkakas insiden, dan kebijakan anggaran galat, sementara insinyur keandalan tertanam bekerja di dalam setiap kelompok produk. Ketika fitur deteksi penipuan baru menghabiskan separuh anggaran bulanan dalam seminggu, kebijakan yang disepakati di muka membekukan rilis non-kritis sampai kerja keandalan memulihkan ruang kepala. Eksekutif menerima ini tanpa perdebatan, karena mereka telah meratifikasi kebijakan itu di muka.

**Pemerintah.** Sebuah otoritas pajak nasional menjalankan layanan pengajuan daring dengan puncak musiman ekstrem di sekitar tenggat tahunan. Tim SRE-nya memperkirakan permintaan dari tahun-tahun sebelumnya plus perubahan penduduk dan kebijakan, menguji beban hingga beberapa kali puncak normal, dan menyediakan kapasitas berminggu-minggu di muka. SLO menghadap publik untuk ketersediaan dan latensi halaman dipasang di dasbor status. Budaya [postmortem](https://en.wikipedia.org/wiki/Postmortem_documentation) tanpa menyalahkan (meninjau kegagalan untuk memperbaiki sistem alih-alih menetapkan kesalahan individu) dan mandat otomasi terus memangkas intervensi manual yang dulu mendominasi musim pengajuan, membebaskan staf untuk memperbaiki sistem alih-alih merawatnya melewati setiap tenggat.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil SRE datang dari tiga sumber: downtime yang dihindari, tenaga kerja operasional lebih sedikit, dan pengiriman aman lebih cepat. Downtime untuk layanan besar dapat berbiaya ribuan hingga jutaan per jam dalam pendapatan hilang, penalti, dan remediasi, sehingga bahkan peningkatan keandalan sederhana membayar tim dengan cepat. Pengurangan toil mengubah biaya manual berulang menjadi investasi otomasi sekali jalan, sehingga total biaya kepemilikan turun seiring skala tumbuh alih-alih naik seiringnya. Anggaran galat memungkinkan bisnis mengirim lebih cepat ketika keandalan sehat, menangkap nilai fitur yang akan ditinggalkan operasi terlalu hati-hati.

Biaya adopsi nyata. SRE membutuhkan insinyur terampil, infrastruktur observabilitas, dan perubahan budaya yang bersaing dengan tenggat fitur. Tetapi biaya tidak mengadopsi lebih tinggi pada skala besar: headcount operasional tak terbatas, pemadaman tak terduga, kelelahan dan pergantian staf, dan kerusakan reputasi yang sulit dikuantifikasi tetapi mudah diderita. Untuk mengajukan kasus kepada pimpinan, bingkai SRE sebagai manajemen risiko dengan imbal hasil terukur. Sajikan biaya insiden dan operasi manual saat ini, target SLO yang terikat pada komitmen bisnis, dan pengurangan yang diproyeksikan pada keduanya. Jangkarkan argumen pada anggaran galat sebagai alat tata kelola yang memberi pimpinan tuas atas trade-off keandalan-versus-kecepatan.

## Anti-pola dan jebakan

- **SRE sebagai operasi yang diganti nama.** Mengganti nama tim ops tanpa waktu rekayasa, mandat otomasi, dan wewenang untuk menolak tidak mengubah apa-apa.
- **Membidik 100 persen.** Mengejar keandalan sempurna memboroskan uang dan memblokir pengiriman demi keuntungan yang tak dapat dirasakan pengguna.
- **SLI kesombongan.** Mengukur CPU server alih-alih keberhasilan terlihat pengguna memberi angka yang tampak baik sementara pengguna menderita.
- **Anggaran galat tanpa gigi.** Anggaran yang tak pernah ditegakkan ketika habis hanyalah hiasan.
- **Toil tanpa pengukuran.** Jika Anda tidak melacak toil, ia diam-diam menghabiskan tim sampai tak ada kerja perbaikan terjadi.
- **SRE sebagai tempat pembuangan.** Tim terpusat yang mewarisi setiap layanan tak stabil tanpa batas kesiapan tenggelam dalam utang teknis orang lain.
- **Mengabaikan lead time kapasitas.** Mengasumsikan elastisitas cloud instan dan tak terbatas mengundang kekurangan selama puncak yang paling penting.

## Model kematangan

**Tingkat 1, Memulai.** Operasi manual dan reaktif. Tak ada SLO formal, keandalan adalah soal opini, dan insiden yang sama berulang sementara pemadaman kebakaran mendominasi. Otomasi apa pun bersifat kebetulan, dan tak ada yang memiliki keandalan sebagai perhatian rekayasa.

**Tingkat 2, Mengembangkan.** Sebagian layanan punya SLI dan SLO dasar serta pemantauan dan peringatan sederhana, tetapi praktik sangat bervariasi antartim. Toil diakui namun tidak diukur, otomasi ad hoc, dan postmortem terjadi tidak konsisten. Keandalan membaik di kantong-kantong tempat individu mendorongnya, bukan karena organisasi mewajibkannya.

**Tingkat 3, Membakukan.** SLI, SLO, dan kebijakan anggaran galat didokumentasikan dan diterapkan konsisten lintas tim. Toil didefinisikan dan dilacak, perencanaan kapasitas rutin, model keterlibatan SRE dengan tinjauan kesiapan produksi ada, dan otomasi adalah jalur kerja yang didanai alih-alih proyek sampingan. Praktik keandalan tertulis dan ditegakkan di seluruh organisasi.

**Tingkat 4, Mengelola.** Program keandalan diukur dan dikendalikan dengan data terhadap garis dasar. Burn rate anggaran galat, persentase toil, pencapaian SLO, mean time to recovery, dan lead time penyediaan dilacak sebagai metrik, ditinjau pada irama tetap, dan dipakai untuk memegang tim pada target mereka. Pelanggaran anggaran memicu pembekuan yang disepakati, kapasitas diperkirakan terhadap model permintaan, dan setiap keputusan go atau no-go bertumpu pada bukti alih-alih opini.

**Tingkat 5, Mengorkestrasi.** Rekayasa keandalan terintegrasi di seluruh organisasi dan terus diperbaiki. Kebijakan anggaran galat otomatis dan dihormati di mana-mana, sebagian besar operasi swalayan, kapasitas disediakan secara proaktif, dan data keandalan menggerakkan trade-off adaptif antara kecepatan dan stabilitas. Organisasi rutin menentukan ulang cakupan SLO, memensiunkan toil, dan menyeimbangkan ulang investasi keandalan seiring bisnis dan gambaran risiko bergeser.

## Gagasan untuk didiskusikan

- Bagaimana organisasi harus menetapkan SLO pertamanya ketika tak punya data keandalan historis sebagai jangkar?
- Ketika anggaran galat habis tetapi peluncuran besar sudah dijanjikan, siapa yang berwenang mengesampingkan pembekuan, dan bagaimana keputusan itu dicatat?
- Apakah model SRE terpusat, tertanam, atau hibrida yang tepat untuk organisasi Anda, dan apa yang memicu perubahan?
- Bagaimana Anda menilai sembilan tambahan ketersediaan terhadap fitur yang dapat didanai investasi yang sama?
- Apa yang dihitung sebagai toil dalam konteks Anda, dan di mana garis antara penilaian manual berharga dan pengulangan yang dapat dihilangkan?
- Bagaimana target keandalan harus berbeda antara layanan pemerintah menghadap warga dan perkakas enterprise internal?

## Poin-poin utama

- SRE menerapkan rekayasa perangkat lunak pada operasi, memperlakukan keandalan sebagai fitur terukur dan dapat didanai.
- SLI, SLO, dan SLA mengubah keandalan dari opini menjadi angka yang disepakati; jaga SLO lebih ketat daripada SLA.
- Anggaran galat menyelaraskan pengembang dan operator dengan membuat trade-off keandalan-versus-kecepatan eksplisit dan dinegosiasikan di muka.
- Ukur dan batasi toil, dan perlakukan otomasi sebagai rekayasa kelas satu agar operasi berskala sub-linear.
- Rencanakan kapasitas dari perkiraan permintaan dan hormati lead time penyediaan, terutama untuk puncak musiman.
- Pilih model organisasi SRE dengan sengaja dan definisikan model keterlibatan serta batas kesiapan produksi yang jelas.

## Referensi dan bacaan lanjutan

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
