# 10.11 Kedaulatan digital

## Tinjauan dan motivasi

[Kedaulatan digital](https://en.wikipedia.org/wiki/Digital_sovereignty) adalah sejauh mana organisasi, negara, atau blok mempertahankan kendali bermakna atas data, perangkat lunak, dan infrastrukturnya sendiri. Artinya kendali atas di mana data secara fisik berada, hukum dan pemerintah mana yang dapat memaksa akses atasnya, dan apakah sistem kritis dapat terus beroperasi tanpa bergantung pada kekuatan asing atau satu vendor. Ia punya beberapa dimensi: **[kedaulatan data](https://en.wikipedia.org/wiki/Data_sovereignty)** (yurisdiksi dan hukum siapa yang mengatur data), **kedaulatan operasional** (kemampuan menjalankan dan mengadministrasi sistem tanpa izin atau kehadiran pihak ketiga), **kedaulatan perangkat lunak** (akses dan kendali atas sumber dan evolusinya), dan **kedaulatan rantai pasok** (bebas dari titik sumbat dalam perangkat keras, layanan, dan dependensi). Bab ini berada di bagian manajemen karena kedaulatan pada dasarnya adalah keputusan strategi, pengadaan, dan risiko (bab 10.1–10.3) dengan konsekuensi teknis yang dalam.

Motivasinya telah bergeser dari teoretis menjadi mendesak. [Komputasi awan](https://en.wikipedia.org/wiki/Cloud_computing) memusatkan sebagian besar infrastruktur dunia pada segelintir penyedia, kebanyakan di bawah yurisdiksi satu negara. Hukum ekstrateritorial seperti [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) AS (yang dapat memaksa penyedia mengungkap data di mana pun ia disimpan) berbenturan dengan rezim seperti [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) UE, ketegangan yang mengkristal dalam putusan *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)* yang membatalkan Privacy Shield UE-AS. Tambahkan guncangan geopolitik, sanksi, dan risiko penyedia diputus, dan ketergantungan menjadi kerentanan strategis, bukan sekadar catatan kaki manajemen vendor. Kedaulatan adalah disiplin memutuskan, dengan sengaja, seberapa banyak ketergantungan itu yang dapat dipikul dengan aman oleh sistem dan data paling kritis Anda.

Untuk enterprise dan terutama pemerintah taruhannya langsung. Multinasional harus mendamaikan rezim perlindungan data yang bertentangan dan menghindari lock-in yang dapat diubah regulator atau peristiwa geopolitik menjadi migrasi eksistensial. Pemerintah memegang data (catatan kesehatan, pajak, pertahanan, identitas warga) yang paparannya ke yurisdiksi asing adalah soal keamanan nasional dan kepercayaan publik. Itulah mengapa tawaran "sovereign cloud", inisiatif seperti [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X) UE, dan sertifikasi nasional seperti SecNumCloud Prancis bermunculan. Tujuannya bukan autarki. Melainkan kendali proporsional yang dicocokkan dengan kepekaan apa yang dipertaruhkan.

## Prinsip utama

- **Kedaulatan adalah spektrum, bukan sakelar.** Cocokkan derajat kendali dengan kepekaan data dan beban kerja.
- **Lokasi bukan yurisdiksi.** Data yang disimpan lokal masih dapat dijangkau secara hukum oleh pemerintah asing; residensi saja bukan kedaulatan.
- **Rancang untuk jalan keluar.** Kemampuan meninggalkan penyedia adalah ukuran kedaulatan yang paling benar.
- **[Standar terbuka](https://en.wikipedia.org/wiki/Open_standard) dan [sumber terbuka](https://en.wikipedia.org/wiki/Open-source_software) mengurangi ketergantungan:** keduanya perkakas otonomi strategis, bukan sekadar penghemat biaya.
- **Kendalikan kunci.** Siapa yang memegang dan mengendalikan kunci enkripsi sering lebih penting daripada di mana byte berada.
- **Hindari menukar satu lock-in dengan yang lain.** Satu vendor "berdaulat" dapat sama tertawannya dengan hyperscaler.
- **Bersikap proporsional.** Kedaulatan punya biaya nyata; berlebihan di mana-mana memboroskan uang dan memperlambat penyampaian.

## Rekomendasi

### Klasifikasikan data dan beban kerja menurut kepekaan kedaulatan

Tidak semuanya butuh perlindungan yang sama. Klasifikasikan data dan sistem menurut konsekuensi akses yurisdiksi asing atau hilangnya penyedia. Beban kerja publik dan berisiko rendah dapat berada di infrastruktur hyperscale global demi skala dan biaya. Data sangat sensitif (keamanan nasional, kesehatan, identitas warga, catatan teregulasi) membenarkan kendali kedaulatan lebih kuat. Pemeringkatan ini, logika berbasis risiko yang sama dengan klasifikasi data di bab 4.5, adalah yang menjaga kedaulatan terjangkau, memusatkan kendali mahal di tempat ia dibenarkan alih-alih melokalkan segalanya.

### Pahami yurisdiksi, bukan hanya residensi

**Residensi data** (lokasi fisik atau geografis tempat data disimpan) diperlukan tetapi tidak cukup. Yang penting secara hukum adalah *yurisdiksi*: pemerintah mana yang dapat memaksa pengungkapan, dan di bawah hukum mana. Set data yang disimpan di pusat data dalam negeri yang dioperasikan penyedia berkantor pusat asing masih dapat dijangkau di bawah hukum negara asal penyedia itu (masalah CLOUD Act). Petakan paparan hukum setiap sistem: kantor pusat penyedia, hukum yang berlaku, dan keputusan kecukupan atau mekanisme transfer apa pun (Standard Contractual Clauses, EU-US Data Privacy Framework). Lalu perlakukan peta hukum itu sebagai bagian kelas satu arsitektur (bab 4.5, 4.6).

### Rancang untuk portabilitas dan reversibilitas

Kendali kedaulatan paling tahan lama adalah jalan keluar yang kredibel. Pilih standar terbuka dan format portabel (bab 3.8). Kontainerisasi beban kerja agar dapat berpindah. Simpan infrastruktur sebagai kode (bab 8.2) agar lingkungan dapat dibangun ulang di tempat lain. Hindari ketergantungan mendalam pada layanan proprietari satu penyedia untuk sistem paling kritis Anda. Pelihara dan secara berkala *uji* rencana keluar, escrow data dan konfigurasi plus jalur terlatih ke alternatif, agar "kami bisa pergi jika harus" adalah fakta yang didemonstrasikan, bukan harapan. Ini penawar **[vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in)**, kondisi tidak mampu berganti penyedia tanpa biaya atau gangguan yang melarang.

### Pakai infrastruktur berdaulat dan kendali kunci di mana dibenarkan

Untuk tingkat paling sensitif, ada kendali teknis lebih kuat: tawaran **sovereign cloud** (region cloud yang dioperasikan oleh atau bermitra dengan entitas dalam yurisdiksi, kadang bersertifikat seperti SecNumCloud), **[confidential computing](https://en.wikipedia.org/wiki/Confidential_computing)** (eksekusi tepercaya berbasis perangkat keras yang menjaga data tetap terenkripsi bahkan saat diproses), dan kunci enkripsi yang dikendalikan pelanggan: **bring your own key (BYOK)** dan, lebih kuat, **hold your own key (HYOK)**, di mana penyedia tidak pernah punya akses ke kunci yang membuka data. Mengendalikan kunci dapat memberikan banyak manfaat praktis kedaulatan bahkan di infrastruktur bersama. Data yang tak dapat didekripsi penyedia adalah data yang tak dapat diungkapnya secara bermakna.

### Pilih sumber terbuka dan ekosistem terbuka untuk otonomi strategis

Perangkat lunak sumber terbuka dan standar terbuka adalah tuas kedaulatan terkuat, karena menghapus sakelar mati satu vendor. Sumbernya dapat dijalankan, diaudit, di-fork, dan dipelihara terlepas dari satu pemasok mana pun (bab 10.3, 3.8). Kebijakan sektor publik "public money, public code" dan inisiatif seperti Gaia-X mencerminkan ini. Sumber terbuka tidak otomatis berdaulat. Ia tetap butuh orang terampil untuk menjalankan dan mendukungnya, dan rantai pasoknya perlu diamankan (bab 4.2). Tetapi ia mengubah ketergantungan pada vendor menjadi ketergantungan pada komunitas dan kapabilitas Anda sendiri, yang jauh lebih mudah dikendalikan.

### Atur kedaulatan sebagai risiko proporsional, bukan mutlak

Dirikan kerangka risiko kedaulatan di samping tata kelola lain Anda (bab 10.2, 1.5). Nilai risiko konsentrasi dan yurisdiksi platform utama. Putuskan tingkat kedaulatan target per tingkat data, dan timbang terhadap biaya, kapabilitas, dan kecepatan penyampaian. Tujuannya posisi yang dapat dipertahankan dan terdokumentasi ("beban kerja ini menerima ketergantungan hyperscale; yang ini menuntut kendali dalam yurisdiksi; inilah postur keluar kami"), ditinjau seiring geopolitik dan regulasi berubah, bukan sikap mutlak sekali jalan.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| **Cloud hyperscale global** | Skala, fitur, biaya rendah, kecepatan | Paparan yurisdiksi; risiko konsentrasi dan lock-in |
| **Sovereign cloud / penyedia dalam yurisdiksi** | Kendali hukum; cocok keamanan nasional; kepercayaan | Biaya lebih tinggi; fitur lebih sedikit; sering skala lebih kecil; lock-in baru |
| **Kendali kunci (BYOK/HYOK) di infra bersama** | Banyak manfaat dengan biaya lebih rendah; mempertahankan skala | Kerumitan operasional; risiko manajemen kunci; tidak mutlak |
| **Sumber terbuka / dihosting sendiri** | Dapat diaudit, dapat di-fork, tanpa sakelar mati vendor | Butuh kapabilitas internal; Anda memiliki operasi dan keamanannya |
| **Mandat lokalisasi data** | Kepatuhan regulasi; jaminan politik | Mahal; memecah data; dapat mengurangi ketahanan dan kegunaan |

Ketegangan penentunya **kendali versus kapabilitas dan biaya**. Kedaulatan maksimum (dihosting sendiri, dalam yurisdiksi, sumber terbuka, sepenuhnya portabel) mengorbankan skala, fitur, dan kecepatan platform global. Kapabilitas maksimum menerima ketergantungan dan paparan yurisdiksi. Resolusinya pemeringkatan: bayar untuk kedaulatan di mana konsekuensi membenarkan, dan ambil ketergantungan pragmatis di mana tidak.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sudahkah kita memeringkat data dan beban kerja menurut kepekaan kedaulatan, agar kendali mahal hanya mendarat di tempat ia dibenarkan?** Kedaulatan adalah spektrum, bukan sakelar, dan melokalkan segalanya membakar uang, melepas kapabilitas, dan bahkan dapat mengurangi ketahanan dengan mempersempit opsi Anda. Klasifikasikan setiap sistem menurut konsekuensi akses yurisdiksi asing atau hilangnya penyedia: beban kerja publik dan berisiko rendah dapat berada di infrastruktur hyperscale global, sementara data keamanan nasional, kesehatan, atau identitas warga membenarkan kendali lebih kuat. Ini logika berbasis risiko yang sama dengan klasifikasi data, dan itulah yang menjaga kedaulatan terjangkau. Bawa sistem permata mahkota Anda dan hosting saat ini, dan tanyakan apakah perlindungan sepadan dengan kepekaan. Jika Anda melindungi segalanya sama rata, hampir pasti Anda membayar berlebih di satu tempat dan terpapar di tempat lain.

2. **Apakah standar terbuka dan sumber terbuka bagian dari strategi kedaulatan kita, atau kita memperlakukannya hanya sebagai penghemat biaya?** Sumber yang dapat Anda jalankan, audit, fork, dan pelihara menghapus sakelar mati satu vendor, salah satu tuas otonomi terkuat yang Anda miliki. Standar terbuka dan format portabel adalah yang memungkinkan jalan keluar kredibel, dan jalan keluar kredibel adalah ukuran kedaulatan yang paling benar. Jebakan yang lebih halus adalah lepas dari hyperscaler hanya untuk menjadi sepenuhnya tertawan satu vendor "berdaulat" tanpa jalan keluar: Anda menukar satu lock-in dengan yang lain. Bawa platform paling kritis Anda dan tanyakan seberapa erat masing-masing terikat pada layanan proprietari satu penyedia. Di mana jawabannya "sangat erat," standar terbuka dan lingkungan terkontainerisasi yang dapat dibangun ulang adalah cara termurah melonggarkan cengkeraman.

3. **Siapa yang memiliki kerangka risiko kedaulatan kita, dan seberapa sering kita meninjau ulang sikap seiring hukum dan geopolitik bergeser?** Posisi kedaulatan yang ditetapkan sekali dan tak pernah ditinjau menjadi fiksi begitu putusan, sanksi, atau hukum baru mendarat, dan guncangan itu kini tiba secara teratur. Dirikan kerangka hidup di samping tata kelola lain Anda: nilai risiko konsentrasi dan yurisdiksi platform utama, tetapkan tingkat kedaulatan target per tingkat data, dan dokumentasikan posisi yang dapat dipertahankan yang dapat Anda tunjukkan kepada regulator. Namai pemilik dan irama tinjauan. Bawa pertanyaan bagaimana sanksi atau putusan merugikan terhadap penyedia utama Anda akan menimpa layanan kritis Anda minggu depan; jika tak ada yang dapat menjawab, kerangkanya belum ada.

4. **Siapa yang memegang kunci enkripsi untuk data paling sensitif kita, dan dapatkah penyedia kita dipaksa menyerahkan data itu dalam bentuk terbaca?** Residensi dan bahkan region "berdaulat" bernilai kecil jika operator mempertahankan kunci, karena perintah pengungkapan lalu menjangkau data terdekripsi di mana pun byte berada. Mengendalikan kunci sendiri, lewat bring your own key atau hold your own key yang lebih kuat, di mana penyedia tak pernah melihatnya, sering memberikan sebagian besar manfaat praktis kedaulatan di infrastruktur bersama dengan sepersekian biaya merelokasi segalanya. Pertimbangan yang bersaing bersifat operasional: manajemen kunci tak kenal ampun, dan kunci yang hilang atau salah ditangani dapat mengunci Anda dari data sendiri sama pastinya dengan sanksi apa pun. Bawa inventaris set data mana yang terenkripsi, siapa yang sebenarnya memegang tiap kunci, dan apa jalur pemulihan Anda jika kunci hilang, lalu petakan terhadap tingkat kedaulatan Anda. Untuk enterprise dan pemerintah, perlakukan kustodi kunci sebagai garis yang menentukan apakah perintah pengungkapan asing mengembalikan ciphertext atau plaintext, dan jadikan itu persyaratan pengadaan alih-alih pemasangan belakangan.

5. **Dapatkah kita benar-benar meninggalkan penyedia utama kita dalam kerangka waktu yang berarti, dan kapan terakhir kita melatihnya?** Jalan keluar kredibel adalah ukuran kedaulatan yang paling benar, namun kebanyakan rencana keluar hidup di atas kertas dan tak pernah dijalankan, sehingga portabilitas tetap harapan alih-alih fakta yang didemonstrasikan. Ketegangannya biaya dan fokus: melatih keluar, menjaga beban kerja terkontainerisasi, dan memegang escrow data dan konfigurasi semuanya memakan perhatian rekayasa yang akan lebih suka dihabiskan tekanan penyampaian di tempat lain. Bawa sistem paling kritis Anda, perkiraan jujur berapa lama migrasi paksa akan memakan waktu, daftar layanan proprietari yang diandalkannya, dan tanggal latihan aktual terakhir Anda (jika ada). Untuk organisasi besar atau publik yang memikul kewajiban keluar multitahun dalam kontrak, keluar yang tak dilatih adalah komitmen yang mungkin tak dapat Anda penuhi secara hukum, jadi perlakukan irama latihan sebagai bagian biaya menjalankan sistem, bukan latihan opsional.

6. **Untuk setiap sistem permata mahkota, apakah kita tahu pemerintah mana yang secara hukum dapat memaksa akses ke sana hari ini, terlepas dari di mana data secara fisik berada?** Lokasi bukan yurisdiksi: data di pusat data dalam negeri masih dapat dijangkau di bawah hukum negara asal operator berkantor pusat asing, dan tim rutin keliru menganggap residensi sebagai perlindungan hukum. Bagian sulitnya adalah jawabannya membutuhkan masukan hukum dan pengadaan, bukan hanya diagram arsitektur, dan peta bergeser seiring keputusan kecukupan, putusan, dan mekanisme transfer berubah. Bawa, untuk setiap set data kritis, kantor pusat penyedia, hukum yang menjangkaunya, dan mekanisme transfer yang Anda andalkan, dan jujurlah di mana tak ada yang benar-benar tahu. Dalam pengaturan teregulasi dan publik, paparan hukum tak terpetakan pada data warga atau keamanan nasional adalah temuan yang menunggu terjadi di audit berikutnya, jadi danai pemetaan hukum seeksplisit Anda mendanai infrastruktur.

## Lensa sektor

**Startup.** Kecepatan dan runway mendominasi, jadi beli kedaulatan sebagai fitur tipis alih-alih membangun tumpukan berdaulat yang tak sanggup Anda staf-i. Jika yurisdiksi pelanggan adalah kendalanya, deploy ke opsi dalam-region penyedia Anda yang ada, pegang kunci enkripsi sendiri agar operator tak dapat mendekripsi catatan sensitif, dan jaga beban kerja terkontainerisasi agar tetap portabel. Itu menutup kesepakatan pada biaya tahap seed dan menghindari arsitektur ulang yang tak punya runway.

**Bisnis kecil.** Tanpa spesialis kedaulatan dan anggaran ketat, perlakukan ini sebagai soal tinjauan kontrak dan pemilihan vendor, bukan program rekayasa. Pilih vendor yang menawarkan region dalam yurisdiksi, ketentuan pemrosesan data transparan, dan kunci yang dipegang pelanggan sebagai fitur standar, dan baca klausul subprosesor dan pengungkapan sebelum menandatangani. Menghosting sendiri demi kedaulatan jarang sepadan di sini: Anda akan mewarisi beban operasi dan keamanan tanpa orang untuk memikulnya.

**Enterprise.** Tugasnya tata kelola portofolio lintas banyak tim: pemeringkatan bersama data menurut kepekaan kedaulatan, tampilan risiko konsentrasi seberapa banyak beban kritis berada pada satu penyedia atau satu yurisdiksi, dan kendali kunci, portabilitas, dan latihan keluar yang dibakukan agar tiap kelompok berhenti membuat taruhan sendiri yang tak terkoordinasi. Anggarkan biaya lebih tinggi dan beban operasional tingkat sensitif secara eksplisit, dan pegang sikap terdokumentasi yang dapat diaudit yang dapat Anda tunjukkan kepada regulator. Kelola kedaulatan sebagai risiko hidup dengan metrik dan irama tinjauan, bukan migrasi sekali jalan.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Pilih infrastruktur berdaulat bersertifikat (misalnya kualifikasi gaya SecNumCloud) dan standar terbuka serta sumber terbuka agar platform dapat dipelihara terlepas dari satu pemasok mana pun, dan wajibkan portabilitas dan pengungkapan paparan hukum dalam kontrak itu sendiri. Terbitkan deskripsi bahasa sederhana di mana data warga berada dan siapa yang dapat menjangkaunya, cadangkan kendali berdaulat mahal untuk tingkat yang benar-benar sensitif, dan jaga layanan publik kurang sensitif di infrastruktur global yang lebih murah.

## Contoh

**Startup.** Startup health-tech kecil mendapat pelanggan rumah sakit pertamanya di Jerman, yang mensyaratkan data pasien tetap di bawah yurisdiksi UE. Alih-alih membangun berlebihan tumpukan berdaulat yang tak sanggup dibayar, para pendiri men-deploy ke region UE penyedia cloud yang sudah ada, memegang kunci enkripsi sendiri agar penyedia tak dapat mendekripsi catatan sensitif, dan menjaga beban kerja terkontainerisasi agar tetap portabel. Ini membeli sebagian besar manfaat kedaulatan yang dibutuhkan pelanggan dengan biaya yang dapat dipikul tim tahap seed, dan menutup kesepakatan tanpa arsitektur ulang menyeluruh.

**Enterprise.** Sebuah bank multinasional harus menjaga data pelanggan tertentu di dalam UE dan di luar jangkauan hukum pengungkapan asing. Alih-alih meninggalkan penyedia cloud globalnya, ia memeringkat propertinya. Beban kerja umum tetap di region hyperscale demi skala. Data pelanggan teregulasi berjalan di region UE dengan enkripsi **hold your own key** (penyedia tak dapat mendekripsinya) dan rencana keluar teruji ke penyedia alternatif. Ini memuaskan regulator dan selera risiko konsentrasi bank sendiri (bab 10.2) tanpa migrasi menyeluruh yang merusak kapabilitas.

**Pemerintah.** Sebuah dinas kesehatan nasional menyimpan rekam medis warga dan menilai paparan ke yurisdiksi asing tidak dapat diterima. Ia mengadakan sovereign cloud, yaitu infrastruktur yang dioperasikan entitas dalam negeri di bawah sertifikasi nasional (mis. gaya SecNumCloud), dengan confidential computing untuk pemrosesan paling sensitif, dan mewajibkan standar terbuka (bab 3.8) dan komponen sumber terbuka agar platform dapat dipelihara terlepas dari satu pemasok mana pun. Biaya lebih tinggi dan set fitur lebih sempit diterima sebagai harga kendali keamanan nasional dan kepercayaan publik. Sementara itu, layanan kurang sensitif (portal informasi publik) tetap di infrastruktur global yang lebih murah.

## Kasus bisnis: motivasi, ROI, dan TCO

Ekonomi kedaulatan digital asimetris, dan paling baik dibingkai sebagai asuransi terhadap peristiwa berprobabilitas rendah berdampak tinggi. Biayanya terlihat dan berulang: infrastruktur berdaulat dan dalam yurisdiksi biasanya lebih mahal, menawarkan lebih sedikit layanan terkelola, dan menuntut lebih banyak kapabilitas operasional internal, semuanya menaikkan total biaya kepemilikan dan dapat memperlambat penyampaian. Manfaatnya sebagian besar bencana yang dihindari: denda regulasi dan arsitektur ulang paksa setelah putusan seperti *Schrems II*, hilangnya akses yang mengakhiri bisnis jika penyedia disanksi atau diputus, atau kerusakan reputasi dan keamanan nasional dari pengungkapan asing atas data sensitif. Karena risiko ekor itu parah dan makin masuk akal, investasi proporsional dalam kedaulatan, terutama kendali murah-tetapi-kuat seperti kepemilikan kunci, portabilitas, dan standar terbuka, sering bernilai harapan positif kuat, meski tampak sebagai biaya murni di spreadsheet kondisi mapan.

Jebakan di kedua sisi adalah ketidakproporsionalan. *Kurang* berinvestasi membiarkan data dan sistem kritis terpapar pada satu yurisdiksi atau vendor tanpa jalan keluar, mengubah risiko yang dapat dikelola menjadi eksistensial. *Terlalu* berinvestasi, dengan melokalkan segalanya dan menolak semua platform global, membakar uang, melepas kapabilitas, dan dapat *mengurangi* ketahanan dengan mempersempit opsi Anda. Untuk mengajukan kasus kepada pimpinan, ikat belanja kedaulatan pada pemeringkatan risiko data-dan-beban kerja. Kuantifikasi paparan konsentrasi dan yurisdiksi sistem permata mahkota. Beri harga kendali murah (kunci, portabilitas, latihan keluar) yang mengurangi risikonya. Cadangkan infrastruktur berdaulat mahal untuk tingkat yang benar-benar membenarkannya.

## Anti-pola dan jebakan

- **Teater kedaulatan:** mengiklankan residensi data dalam negeri sementara penyedia berkantor pusat asing mempertahankan akses hukum ke data.
- **Menyamakan enkripsi dengan kedaulatan:** mengenkripsi data tetapi membiarkan penyedia memegang kunci, sehingga ia masih dapat dipaksa mendekripsi.
- **Rotasi berlebihan:** melokalkan dan menghosting sendiri segalanya dengan biaya merusak dan kapabilitas berkurang, terlepas dari kepekaan.
- **Lock-in tunggal baru:** lepas dari hyperscaler dengan menjadi sepenuhnya tertawan satu vendor "berdaulat" tanpa jalan keluar.
- **Tanpa keluar teruji:** rencana keluar yang ada di atas kertas tetapi tak pernah dilatih, sehingga portabilitas tak terbukti.
- **Mengabaikan rantai pasok manusia:** mengasumsikan sumber terbuka atau hosting sendiri memberi kedaulatan tanpa orang terampil untuk menjalankannya.
- **Sikap statis:** menetapkan posisi kedaulatan sekali dan tak pernah meninjau ulang seiring hukum dan geopolitik bergeser.

## Model kematangan

- **Tingkat 1 (Memulai):** Kedaulatan tidak dipertimbangkan dan reaktif; data dan sistem kritis berada di mana pun yang termurah, tanpa peta risiko yurisdiksi atau konsentrasi dan tanpa pemilik.
- **Tingkat 2 (Mengembangkan):** Residensi data ditangani untuk data teregulasi paling jelas pada sebagian proyek, tetapi yurisdiksi, kendali kunci, dan jalan keluar tidak dipertimbangkan secara sistematis; praktik bervariasi tim demi tim, dan ketergantungan pada satu penyedia tak diperiksa.
- **Tingkat 3 (Membakukan):** Data dan beban kerja diperingkat menurut kepekaan kedaulatan di bawah kebijakan terdokumentasi yang diterapkan di seluruh organisasi; yurisdiksi dipetakan; kendali kunci, portabilitas, dan standar terbuka diwajibkan pada tingkat sensitif; rencana keluar ada dan diwajibkan alih-alih opsional.
- **Tingkat 4 (Mengelola):** Sikap diukur dan dikendalikan terhadap garis dasar: risiko konsentrasi (pangsa beban kritis pada satu penyedia atau yurisdiksi), cakupan kepemilikan kunci pada set data sensitif, kelengkapan pemetaan yurisdiksi, dan waktu keluar yang dilatih dilacak sebagai metrik, dilaporkan ke tata kelola, dan ditegakkan terhadap ambang, sehingga ketergantungan yang melayang memicu tindakan atas bukti alih-alih setelah guncangan.
- **Tingkat 5 (Mengorkestrasi):** Kedaulatan terus diperbaiki dan terintegrasi di seluruh organisasi: kerangka risiko hidup memberi makan arsitektur, pengadaan, dan perencanaan risiko secara bawaan, keluar rutin dilatih, dan organisasi secara adaptif menentukan ulang cakupan tingkat, menyeimbangkan ulang penyedia, dan merevisi sikapnya seiring putusan, sanksi, dan regulasi bergeser.

## Gagasan untuk didiskusikan

1. Untuk set data paling sensitif Anda, pemerintah mana yang secara hukum dapat memaksa akses ke sana hari ini, dan apakah Anda tahu?
2. Apakah residensi data Anda kedaulatan sejati, atau penyedia berkantor pusat asing masih memegang kunci dan paparan hukumnya?
3. Dapatkah Anda benar-benar meninggalkan penyedia cloud utama jika harus, dan pernahkah Anda mengujinya?
4. Beban kerja Anda yang mana yang benar-benar butuh infrastruktur berdaulat, dan mana yang Anda lindungi berlebihan dengan biaya tak perlu?
5. Di mana mengendalikan kunci enkripsi Anda sendiri akan memberi sebagian besar manfaat kedaulatan dengan sepersekian biaya?
6. Bagaimana sanksi, pemadaman, atau putusan hukum terhadap penyedia utama Anda akan memengaruhi layanan kritis Anda minggu depan?

## Poin-poin utama

- Kedaulatan digital adalah kendali proporsional atas data, perangkat lunak, dan infrastruktur Anda, di dimensi data, operasional, perangkat lunak, dan rantai pasok.
- **Lokasi bukan yurisdiksi:** residensi saja tidak mencegah akses hukum asing; petakan siapa yang dapat memaksa pengungkapan.
- **Rancang untuk keluar** dan **kendalikan kunci Anda:** portabilitas dan kepemilikan kunci adalah kendali berdaya ungkit tertinggi dan berbiaya terendah.
- **Standar terbuka dan sumber terbuka** adalah perkakas otonomi strategis; cadangkan **sovereign cloud** mahal untuk tingkat yang membenarkannya.
- Atur kedaulatan sebagai **risiko proporsional yang hidup** (bab 10.2, 10.3, 4.5, 4.6, 3.8), menghindari baik perlindungan kurang maupun rotasi berlebihan yang merusak.
- ROI-nya asuransi terhadap risiko ekor parah (regulasi, geopolitik, dan lock-in) yang dihargai terhadap biaya nyata yang berulang.

## Referensi dan bacaan lanjutan

- European Court of Justice, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Regulation (EU) 2016/679, *General Data Protection Regulation (GDPR)*; Regulation (EU) 2023/2854, *Data Act*.
- U.S. *Clarifying Lawful Overseas Use of Data (CLOUD) Act* (2018).
- ANSSI, kerangka kualifikasi *SecNumCloud* (Prancis).
- Gaia-X European Association for Data and Cloud (inisiatif Gaia-X).
- ENISA, laporan tentang keamanan cloud dan sertifikasi keamanan siber UE (EUCS).
- Julia Pohle dan Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, tulisan tentang otonomi digital Eropa dan ketergantungan pada penyedia asing.
- Kai Zenner dan lainnya, analisis kebijakan kedaulatan digital UE (sebagai konteks; verifikasi sumber terkini).
