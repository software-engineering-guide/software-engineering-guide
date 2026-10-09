# 9.3 Manajemen insiden

## Tinjauan dan motivasi

[Manajemen insiden](https://en.wikipedia.org/wiki/Incident_management) adalah disiplin mendeteksi, merespons, menyelesaikan, dan belajar dari gangguan layanan yang tak terencana. Setiap sistem yang tidak sepele akhirnya gagal, jadi pertanyaannya bukan apakah insiden terjadi tetapi seberapa baik Anda menanganinya. Manajemen insiden yang baik menjaga dampak dan durasi gangguan tetap kecil, mengoordinasikan orang di bawah tekanan, berkomunikasi jujur dengan yang terdampak, dan mengubah setiap kegagalan menjadi perbaikan tahan lama. Ia memadukan kesiapan operasional, peran jelas, komunikasi tenang, dan budaya belajar.

Bagi tim besar, manajemen insiden adalah tempat kompleksitas organisasi benar-benar menggigit. Insiden serius dapat melibatkan banyak layanan, beberapa tim, eksekutif, pelanggan, regulator, dan publik, sekaligus, di bawah tekanan waktu dan dengan informasi tak lengkap. Tanpa struktur bersama, respons jatuh ke kekacauan: upaya terduplikasi, keputusan bertentangan, kebisuan terhadap pemangku kepentingan, dan kepahlawanan yang membakar orang. Proses insiden yang terdefinisi baik memberi semua orang cara dikenal untuk terhubung, sumber kebenaran tunggal, dan wewenang keputusan jelas, agar kelompok besar dapat bertindak koheren dalam krisis.

Taruhan enterprise dan pemerintah tinggi. Jasa keuangan menghadapi tenggat pelaporan regulasi untuk pemadaman besar. Insiden kesehatan dapat memengaruhi keselamatan pasien. Kegagalan layanan pemerintah dapat menghentikan warga mengakses tunjangan, mengajukan pajak, atau menjangkau layanan darurat. Akuntabilitas publik berarti pemadaman terlihat dan diawasi. Praktik on-call berkelanjutan juga kewajiban kepedulian: rotasi yang kekurangan staf dan dikelola buruk menyebabkan [kelelahan](https://en.wikipedia.org/wiki/Occupational_burnout) dan pergantian staf yang akhirnya memperburuk keandalan. Manajemen insiden karenanya berada di tempat keunggulan operasional, kesejahteraan manusia, dan kepercayaan institusional bertemu.

*Lihat juga:* bab 9.1 (site reliability engineering), bab 9.2 (observabilitas dan pemantauan), dan bab 1.1 (budaya rekayasa: budaya insiden tanpa menyalahkan dan berorientasi belajar).

## Prinsip utama

- **Struktur mengalahkan kepahlawanan.** Struktur komando terdefinisi memungkinkan banyak orang berkoordinasi; bergantung pada segelintir pahlawan tidak berskala dan membakar mereka.
- **Peran, bukan jabatan.** Dalam insiden, peran jelas seperti komandan insiden dan pemimpin komunikasi lebih penting daripada pangkat organisasi.
- **Berkomunikasi lebih awal dan sering.** Pembaruan sering dan jujur kepada pemangku kepentingan membangun kepercayaan bahkan ketika kabarnya buruk; kebisuan menghancurkannya.
- **Pisahkan koordinasi dari investigasi.** Orang yang menjalankan insiden tidak boleh sekaligus menunduk men-debug.
- **On-call harus berkelanjutan.** Rotasi, kompensasi, dan batas beban melindungi orang yang melindungi sistem.
- **Tanpa menyalahkan secara bawaan.** Orang bertindak wajar mengingat apa yang mereka ketahui; menyalahkan menyembunyikan penyebab sistemik yang sebenarnya.
- **Pembelajaran adalah intinya.** Insiden yang tak menghasilkan perbaikan tahan lama adalah penderitaan yang sia-sia.
- **Pelihara memori organisasi.** [Postmortem](https://en.wikipedia.org/wiki/Postmortem_documentation) dan tindakannya harus dapat ditemukan dan dipakai ulang, bukan hilang setelah seminggu.

## Rekomendasi

### Jalankan rotasi on-call yang berkelanjutan

Rancang on-call agar manusiawi dan efektif. Jaga rotasi cukup besar agar tak seorang pun on-call terlalu sering, sediakan tingkat primer dan sekunder (eskalasi), dan tetapkan ekspektasi jelas untuk waktu pengakuan dan respons. Kompensasi on-call secara adil, entah lewat bayaran atau waktu libur, dan perlakukan sebagai kerja nyata. Lacak beban peringatan per shift, dan perlakukan rotasi berisik yang merusak tidur sebagai bug untuk diperbaiki dengan memangkas panggilan palsu, bukan sebagai normal. Ikuti matahari lintas zona waktu di mana bisa, agar orang on-call pada jam terjaga mereka. Pastikan setiap insinyur on-call punya [runbook](https://en.wikipedia.org/wiki/Runbook), akses, dan wewenang untuk bertindak, dan bahwa serah terima shift mentransfer konteks dengan sengaja.

### Tetapkan komando insiden dan tingkat keparahan

Adopsi [sistem komando insiden](https://en.wikipedia.org/wiki/Incident_Command_System) yang terinspirasi respons darurat. **Komandan insiden** memiliki koordinasi dan keputusan, bukan perbaikan teknis. Mereka mendelegasikan, melacak tindakan, dan menjaga respons bergerak. Peran pendukung mencakup **pemimpin operasi atau teknis** yang mengarahkan investigasi langsung, **pemimpin komunikasi** yang menangani pembaruan internal dan eksternal, dan **juru catat** yang mencatat linimasa. Definisikan **tingkat keparahan** (misalnya SEV1 untuk pemadaman kritis, meluas, atau memengaruhi keselamatan hingga SEV3 untuk masalah kecil) dengan kriteria jelas, karena keparahan menentukan siapa dipanggil, seberapa cepat, dan seberapa banyak organisasi dimobilisasi. Siapa pun harus dapat mendeklarasikan insiden, dan Anda harus condong ke mendeklarasikan.

### Berkomunikasi selama insiden, secara internal dan publik

Siapkan satu kanal koordinasi sebagai sumber kebenaran, dan kirim pembaruan pada irama tetap, bahkan ketika pembaruannya hanya "masih menyelidiki." Secara internal, jaga pimpinan dan tim terdampak tetap terinformasi lewat pemimpin komunikasi, agar penanggap tidak diinterupsi. Secara eksternal, pakai halaman status dan, untuk insiden signifikan, pemberitahuan pelanggan atau publik yang jujur tentang dampak dan perkiraan penyelesaian tanpa menjanjikan berlebihan. Untuk layanan teregulasi dan pemerintah, ketahui kewajiban dan tenggat pelaporan wajib Anda di muka, dan siapkan templat. Tujuannya agar pemangku kepentingan selalu mendengar lebih banyak dari Anda daripada dari desas-desus.

### Selenggarakan postmortem tanpa menyalahkan dan dorong tindakan korektif

Setelah insiden signifikan mana pun, tulis **postmortem tanpa menyalahkan**: linimasa faktual, dampak, faktor kontribusi, apa yang berjalan baik, apa yang berjalan buruk, dan di mana Anda beruntung. Tanpa menyalahkan berarti berfokus pada bagaimana sistem dan proses memungkinkan kegagalan, bukan siapa yang dihukum, karena [keamanan psikologis](https://en.wikipedia.org/wiki/Psychological_safety) adalah yang menghasilkan catatan jujur dan pembelajaran nyata. Setiap postmortem menghasilkan **tindakan korektif** dengan pemilik dan tanggal jatuh tempo, diprioritaskan menurut efeknya pada risiko masa depan. Lacak sampai tuntas di backlog rekayasa normal. Postmortem yang tindakannya tak pernah selesai hanyalah teater.

### Belajar dari insiden dan bangun memori organisasi

Postmortem individual perlu, tetapi tidak cukup sendiri. Tinjau insiden secara agregat untuk menemukan tema berulang, kelemahan sistemik, dan kelas kegagalan yang layak perbaikan struktural. Jadikan postmortem dapat dicari dan bagikan luas, agar pelajaran melintasi batas tim. Beri makan apa yang Anda pelajari kembali ke runbook, pelatihan, tinjauan arsitektur, dan batas kesiapan produksi. Pertimbangkan tinjauan keandalan berkala dan game day atau [latihan chaos](https://en.wikipedia.org/wiki/Chaos_engineering) yang melatih respons dan memunculkan celah sebelum insiden nyata melakukannya. Perlakukan kumpulan insiden Anda sebagai aset strategis yang menangkap pengetahuan operasional yang diperoleh dengan susah payah.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Komando insiden formal | Respons terkoordinasi dan berskala | Overhead untuk insiden kecil |
| Ambang rendah untuk mendeklarasikan | Menangkap masalah lebih awal | Alarm palsu sesekali |
| Transparansi status publik | Membangun kepercayaan, mengurangi desas-desus | Memaparkan kegagalan, mengundang pengawasan |
| Postmortem tanpa menyalahkan | Pembelajaran jujur, keselamatan | Dapat terasa tanpa akuntabilitas jika disalahgunakan |
| Rotasi on-call besar | Berkelanjutan, kelelahan lebih sedikit | Butuh lebih banyak staf terlatih, mengencerkan konteks |

Trade-off sentralnya antara overhead proses dan manfaat koordinasi. Struktur insiden berat tak ternilai pada SEV1 yang melintasi banyak tim tetapi berlebihan untuk gangguan kecil, jadi setel proses menurut keparahan. Transparansi menukar rasa malu jangka pendek dengan kepercayaan jangka panjang. Organisasi yang berkomunikasi terbuka selama pemadaman umumnya menjaga lebih banyak niat baik daripada yang membisu. Tanpa menyalahkan kadang disalahbaca sebagai kurangnya akuntabilitas, tetapi akuntabilitas yang dituntutnya kolektif dan sistemik: tim memiliki perbaikan kondisi yang memungkinkan kegagalan, yang bekerja jauh lebih baik daripada mengorbankan individu.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Berapa banyak orang yang dapat menjalankan insiden sebagai komandan, dan dapatkah Anda menamai tiga yang bukan manajer senior?** Bergantung pada satu atau dua pahlawan untuk menyelamatkan setiap insiden rapuh dan menjamin kelelahan mereka, dan peran komandan insiden tentang koordinasi, bukan pangkat teknis, jadi ia tak boleh secara bawaan jatuh ke orang senior yang sama setiap kali. Bawa daftar ke diskusi: daftarkan semua orang yang terlatih memegang peran komandan dan kapan terakhir mereka benar-benar menjalankannya. Bagi organisasi besar insiden serius dapat melintasi banyak tim pukul 3 pagi, dan Anda butuh komandan terlatih tersedia di setiap zona waktu, bukan satu pakar yang sedang tidur. Rotasikan peran dan alirkan komandan baru melalui game day agar keterampilan menyebar. Jawabannya memberi tahu apakah respons Anda berskala dengan organisasi atau patah begitu orang terbaik Anda tak tersedia.

2. **Apakah Anda tahu tenggat pelaporan pemadaman wajib Anda, dan apakah templat serta pemiliknya siap sebelum SEV1 berikutnya?** Jasa keuangan menghadapi tenggat pelaporan regulasi untuk pemadaman besar, insiden kesehatan menyentuh keselamatan pasien, dan kegagalan pemerintah menghalangi warga dari tunjangan atau layanan darurat, sehingga jendela pelaporan yang terlewat mengubah pemadaman teknis menjadi masalah hukum. Tengah SEV1 adalah waktu terburuk untuk menemukan Anda punya empat jam memberi tahu regulator dan tanpa templat. Bawa kewajiban sebenarnya: regulator mana, ambang mana memicu laporan, apa tenggatnya, dan siapa yang berwenang mengajukan. Tetapkan ini ke peran pemimpin komunikasi di muka agar penanggap tak pernah ditarik dari perbaikan untuk menyusun pengajuan. Jawabannya harus menghasilkan templat siap, pemilik bernama, dan tingkat keparahan yang otomatis memicu jam pelaporan.

3. **Kapan terakhir Anda melatih insiden besar dengan game day, dan celah apa yang terungkap?** Game day dan latihan chaos melatih respons dan memunculkan celah sebelum insiden nyata melakukannya, dan keadaan akhir matang dalam bab ini adalah respons mulus dan terlatih baik, bukan respons yang diciptakan di bawah tekanan. Rencana yang tak pernah dilatih menyembunyikan asumsi rusak: runbook basi, akses hilang, jalur eskalasi yang buntu, halaman status yang tak dapat diperbarui siapa pun. Bawa temuan latihan terakhir, atau jika tidak ada, perlakukan itu sebagai temuan. Untuk sistem enterprise dan pemerintah di mana pemadaman diawasi publik, latihan adalah cara Anda menunjukkan kompetensi alih-alih berimprovisasi di depan warga dan regulator. Jawabannya harus menetapkan irama game day dan memberi makan setiap celah yang terungkap ke runbook, tinjauan akses, dan batas kesiapan produksi.

4. **Berapa beban peringatan sebenarnya pada rotasi tersibuk Anda, dan maukah Anda membawa pager itu sendiri?** Rotasi berisik yang merusak tidur adalah bug, bukan lencana kehormatan, dan kelelahan peringatan adalah tempat penanggap melewatkan atau lambat mengakui keadaan darurat sungguhan, jadi pertanyaan manusiawi dan pertanyaan keandalan adalah pertanyaan yang sama. Tekanan yang bersaing adalah memangkas panggilan terasa seperti menurunkan kewaspadaan, padahal dalam praktik banjir panggilan palsu menurunkannya jauh lebih banyak. Bawa angkanya: panggilan per shift, berapa yang menyala di luar jam kerja, berapa yang dapat ditindaklanjuti, dan waktu pengakuan untuk yang penting. Tetapkan plafon eksplisit untuk panggilan per shift dan perlakukan rotasi mana pun yang melampauinya sebagai pekerjaan untuk diperbaiki dengan menyetel atau menghapus peringatan. Bagi organisasi besar atau pemerintah, on-call berkelanjutan adalah kewajiban kepedulian dan tuas retensi, karena insinyur berpengalaman yang membawa pengetahuan sistem tak tergantikan adalah persis yang diusir rotasi brutal, dan membangun kembali pengetahuan itu berbiaya jauh lebih besar daripada mengisi staf rotasi secara manusiawi.

5. **Berapa pecahan tindakan korektif kuartal lalu yang benar-benar selesai, dan siapa yang akuntabel ketika tidak?** Postmortem yang tindakannya tak pernah selesai menghasilkan insiden yang sama lagi, jadi disiplin yang memisahkan pembelajaran nyata dari teater adalah apakah perbaikan terkirim, bukan apakah tulisannya enak dibaca. Ketegangannya adalah tindakan korektif bersaing dengan kerja fitur di backlog yang sama, dan tanpa pemilik bernama, tanggal jatuh tempo, dan irama tinjauan mereka diam-diam kalah di setiap pertarungan prioritas. Bawa buku besarnya: setiap tindakan dari postmortem terbaru, pemiliknya, tanggal jatuh temponya, dan statusnya, plus hitungan insiden yang berulang karena perbaikan macet. Lacak ini di backlog rekayasa normal dan tinjau penyelesaian sebagai metrik terhadap garis dasar, agar tindakan yang menua atau dijatuhkan muncul alih-alih lenyap. Dalam pengaturan enterprise dan pemerintah, tindakan korektif yang belum selesai setelah pemadaman terlapor adalah jenis temuan yang disambar auditor atau badan pengawas, jadi penyelesaian adalah pengaman rekayasa sekaligus soal akuntabilitas yang dapat didemonstrasikan.

6. **Apakah semua orang merasa aman mendeklarasikan insiden lebih awal dan berbicara jujur dalam postmortem, atau ketakutan akan disalahkan memperlambat mereka?** Budaya tanpa menyalahkan adalah yang menghasilkan catatan jujur yang mengungkap penyebab sistemik, dan ambang rendah untuk mendeklarasikan adalah yang menangkap masalah selagi kecil, jadi keduanya bergantung pada orang tidak takut bahwa mengangkat tangan akan dipakai melawan mereka. Kekhawatiran yang bersaing adalah tanpa menyalahkan terbaca sebagai kurangnya akuntabilitas, tetapi akuntabilitas yang dituntutnya kolektif: tim memiliki perbaikan kondisi yang memungkinkan kegagalan alih-alih mengorbankan siapa pun yang terakhir menyentuhnya. Bawa bukti yang benar-benar dapat Anda amati: seberapa cepat insiden dideklarasikan versus berapa lama masalah menggelegak lebih dulu, apakah insinyur junior pernah mendeklarasikan, dan apakah postmortem menamai kondisi kontribusi atau diam-diam menamai seseorang. Untuk organisasi besar atau publik, keamanan psikologis rapuh dan mudah dibatalkan oleh satu tinjauan yang digerakkan menyalahkan atau satu pemimpin yang menghukum pembawa pesan, jadi awasi sinyal bahwa orang mengelilingi proses, dan perlakukan deklarasi dini yang jujur sebagai perilaku untuk dilindungi alih-alih risiko untuk dikelola.

## Lensa sektor

**Startup.** Dengan segelintir insinyur dan tanpa runway tersisa, jaga proses satu halaman: siapa pun yang memperhatikan mendeklarasikan, satu orang berkoordinasi, satu orang menyelidiki, satu orang memberi tahu pelanggan, dan tak ada orang lain yang menyentuh produksi. Lewati tingkat keparahan formal dan peran khusus yang tak dapat Anda isi staf, tetapi tulis catatan satu halaman tanpa menyalahkan, karena pada ukuran Anda satu kegagalan berulang dapat menenggelamkan Anda. Bersandarlah pada halaman status ter-hosting dan perkakas paging daripada membangun perkakas koordinasi.

**Bisnis kecil.** Anda tidak punya spesialis keandalan khusus dan anggaran ketat, jadi beli perkakas insiden yang tertanam dalam layanan pemantauan dan paging yang sudah Anda bayar daripada membangun sendiri. Perlakukan on-call sebagai tugas bersama dengan batas jelas dan manusiawi agar tidak membakar satu atau dua orang yang memahami sistem. Tulis postmortem singkat dan benar-benar selesaikan perbaikannya, karena dengan tim kecil pemadaman berulang membuat Anda kehilangan pelanggan yang tak mudah digantikan.

**Enterprise.** Tantangannya mengoordinasikan banyak tim di bawah tekanan, jadi bakukan sistem komando insiden, kriteria keparahan bersama, dan sumber kebenaran tunggal agar SEV1 yang melintasi layanan tidak terfragmentasi. Berinvestasilah pada komandan terlatih di setiap zona waktu, agregasikan postmortem menjadi memori organisasi yang dapat dicari, dan atur tindakan korektif sampai tuntas dengan pemilik dan jejak audit. Kelola beban on-call sebagai metrik seluruh armada agar tak ada rotasi yang diam-diam menjadi tidak manusiawi.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk respons. Ketahui tenggat dan ambang pelaporan pemadaman wajib Anda di muka, siapkan templat pengajuan dan pemilik berwenang bernama, dan terbitkan pembaruan status jujur serta skrip pusat panggilan agar warga tak pernah dibiarkan menebak. Bagikan postmortem di seluruh lembaga, beri makan ke perencanaan ketahanan untuk periode puncak, dan perlakukan catatan insiden masa lalu sebagai bukti yang dapat Anda tunjukkan kepada badan pengawas bahwa kegagalan menghasilkan perbaikan tahan lama.

## Contoh

**Startup.** Startup enam orang bangun dengan API-nya mengembalikan galat dan semua orang menumpuk di utas obrolan yang sama sekaligus. Terbakar oleh kekacauan, mereka menulis satu halaman dasar insiden: siapa pun yang memperhatikan mendeklarasikan insiden dan menjadi koordinator, satu orang menyelidiki, satu orang memposting pembaruan sederhana kepada pelanggan, dan tak ada orang lain yang menyentuh produksi. Pemadaman berikutnya berjalan tenang dan selesai dalam empat puluh menit. Catatan singkat tanpa menyalahkan menemukan migrasi yang berjalan tanpa langkah cadangan, dan mereka menambah pemeriksaan itu ke skrip deploy mereka hari itu juga.

**Enterprise.** Sebuah penyedia perangkat lunak-sebagai-layanan besar mengalami pemadaman parsial selama jam kerja. Insinyur on-call mendeklarasikan SEV1, dan komandan insiden mengambil alih koordinasi sementara pemimpin teknis menyelidiki dan pemimpin komunikasi memposting pembaruan ke halaman status publik setiap dua puluh menit. Eksekutif mengikuti kanal pimpinan alih-alih menginterupsi penanggap. Layanan kembali dalam sembilan puluh menit. Postmortem tanpa menyalahkan minggu berikutnya menemukan pengaman yang hilang di pipeline deployment dan menghasilkan tiga tindakan korektif dengan pemilik. Tinjauan agregat kemudian menunjukkan ini insiden terkait deploy ketiga kuartal itu, yang memicu investasi struktural pada peluncuran yang lebih aman.

**Pemerintah.** Sistem pembayaran sebuah lembaga tunjangan gagal pada hari bervolume tinggi, menghalangi warga menerima dukungan. Proses insiden lembaga memobilisasi komandan, penanggap teknis, dan pemimpin komunikasi yang mengoordinasikan pesan publik dan memenuhi persyaratan regulasi untuk melaporkan pemadaman besar dalam jendela tetap. Halaman status dan skrip pusat panggilan menjaga warga dan staf tetap terinformasi. Postmortem tanpa menyalahkan, dibagikan di seluruh lembaga, memberi makan pelajaran ke runbook dan tinjauan kesiapan produksi, dan kumpulan insiden masa lalu menginformasikan perencanaan kapasitas dan ketahanan tahun berikutnya untuk periode puncak.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil manajemen insiden yang matang tampak sebagai dampak per insiden yang berkurang dan insiden berulang yang lebih sedikit. Respons lebih cepat dan terkoordinasi lebih baik memperpendek pemadaman, yang langsung menghemat pendapatan, penalti, dan biaya remediasi. Postmortem dan tindakan korektif yang disiplin terus menghilangkan seluruh kelas kegagalan, sehingga laju insiden turun seiring waktu. On-call berkelanjutan mengurangi biaya kelelahan dan pergantian staf yang sangat besar dan sering tersembunyi di antara insinyur berpengalaman, yang mahal diganti dan membawa pengetahuan sistem tak tergantikan.

Biaya adopsi sederhana dibanding manfaatnya: pelatihan komando insiden, perkakas untuk koordinasi dan komunikasi status, waktu yang dihabiskan untuk postmortem, dan staf yang dibutuhkan untuk rotasi manusiawi. Biaya tidak mengadopsi parah dan berulang: respons kacau yang memperpanjang pemadaman, kebisuan yang mengikis kepercayaan pelanggan dan publik, penalti regulasi karena pelaporan terlewat, insiden berulang dari tindakan yang tak diselesaikan siapa pun, dan staf on-call yang patah semangat. Untuk mengajukan kasus kepada pimpinan, kuantifikasi insiden terbaru menurut durasi dan dampak, tunjukkan bagaimana koordinasi dan tindakan korektif yang diselesaikan akan mempersingkatnya atau mencegah pengulangan, dan bingkai on-call berkelanjutan sebagai retensi dan manajemen risiko, bukan pemanjaan.

## Anti-pola dan jebakan

- **Budaya pahlawan.** Bergantung pada satu atau dua orang untuk menyelamatkan setiap insiden rapuh dan menjamin kelelahan mereka.
- **Tanpa komandan jelas.** Tanpa seseorang yang memiliki koordinasi, penanggap menduplikasi kerja, bertentangan, dan kehilangan linimasa.
- **Menjadi bisu.** Menahan pembaruan selama pemadaman melahirkan desas-desus, kepanikan, dan ketidakpercayaan yang bertahan.
- **Permainan menyalahkan.** Menghukum individu mendorong kejujuran ke bawah tanah dan menyembunyikan penyebab sistemik yang perlu Anda perbaiki.
- **Teater postmortem.** Menulis postmortem yang tindakan korektifnya tak pernah diselesaikan menghasilkan insiden yang sama lagi.
- **On-call yang lelah peringatan.** Rotasi berisik menguras penanggap sehingga mereka melewatkan atau lambat mengakui keadaan darurat sungguhan.
- **Kebingungan keparahan.** Tingkat keparahan yang tak terdefinisi atau diterapkan tidak konsisten menyebabkan respons kurang pada insiden serius dan berlebihan pada yang remeh.

## Model kematangan

**Tingkat 1, Memulai.** Insiden ditangani ad hoc oleh siapa pun yang memperhatikan, dan respons reaktif serta diimprovisasi. Tak ada peran, tingkat keparahan, atau postmortem terdefinisi. On-call, jika ada sama sekali, informal dan menegangkan, dan kegagalan yang sama berulang karena tak ada yang dipelajari secara tahan lama.

**Tingkat 2, Mengembangkan.** Rotasi on-call dasar dan definisi keparahan ada, dan sebagian insiden mendapat postmortem, tetapi praktik tidak konsisten lintas tim. Peran tidak jelas selama respons, satu tim mungkin menjalankan insiden disiplin sementara tim berikutnya jatuh ke kekacauan, dan tindakan korektif dilacak sembarangan jika sama sekali.

**Tingkat 3, Membakukan.** Sistem komando insiden formal dengan peran jelas dan kriteria keparahan didokumentasikan dan dipakai konsisten di seluruh organisasi. Postmortem tanpa menyalahkan adalah standar untuk insiden signifikan, tindakan korektif dicatat dengan pemilik dan tanggal jatuh tempo, on-call dikompensasi, dan satu kanal koordinasi serta praktik halaman status ditegakkan di seluruh organisasi alih-alih diserahkan kepada tiap tim.

**Tingkat 4, Mengelola.** Program insiden diukur dan dikendalikan terhadap garis dasar. Anda melacak waktu mendeteksi, waktu mengakui, waktu menyelesaikan, panggilan per shift, tingkat penyelesaian tindakan korektif, dan tingkat insiden berulang, dan Anda meninjau metrik ini pada irama untuk menangkap regresi. Tingkat keparahan diterapkan cukup konsisten sehingga datanya tepercaya, beban peringatan dipegang di bawah plafon eksplisit, dan keputusan go atau no-go selama dan setelah insiden digerakkan bukti alih-alih naluri.

**Tingkat 5, Mengorkestrasi.** Manajemen insiden terus diperbaiki dan terintegrasi di seluruh organisasi. Respons mulus dan terlatih baik lewat game day reguler, analisis agregat mendorong investasi struktural yang menghilangkan seluruh kelas kegagalan, dan postmortem membentuk memori organisasi yang dapat dicari yang memberi makan runbook, pelatihan, tinjauan arsitektur, dan perencanaan kapasitas. Sistem beradaptasi seiring tumbuh, dan laju serta dampak insiden menurun seiring waktu.

## Gagasan untuk didiskusikan

- Kriteria apa yang membedakan tingkat keparahan Anda, dan apakah semua orang menerapkannya secara konsisten?
- Bagaimana Anda menjaga on-call berkelanjutan seiring sistem tumbuh tanpa terus menambah orang?
- Siapa yang berwenang membuat keputusan mahal, seperti failover atau rollback, selama insiden langsung?
- Seberapa transparan Anda harus terhadap pelanggan dan publik selama pemadaman, dan di mana batasnya?
- Bagaimana Anda memastikan tindakan korektif benar-benar selesai alih-alih terkatung-katung di backlog?
- Apa yang dibutuhkan untuk mengubah kumpulan postmortem Anda menjadi memori organisasi yang benar-benar dapat dipakai ulang?

## Poin-poin utama

- Setiap sistem gagal; kematangan diukur dari seberapa baik Anda merespons dan belajar, bukan dari menghindari semua insiden.
- Struktur komando insiden yang jelas dengan peran dan tingkat keparahan terdefinisi memungkinkan kelompok besar berkoordinasi di bawah tekanan.
- Berkomunikasilah lebih awal, sering, dan jujur kepada pemangku kepentingan internal dan eksternal; kebisuan menghancurkan kepercayaan.
- Jaga on-call berkelanjutan lewat rotasi adil, kompensasi, dan pengurangan peringatan berisik tanpa henti.
- Selenggarakan postmortem tanpa menyalahkan yang menghasilkan tindakan korektif yang dimiliki dan dilacak, dan selesaikan.
- Pembelajaran agregat dan memori organisasi yang dapat dicari mengubah insiden individual menjadi perbaikan abadi.

## Referensi dan bacaan lanjutan

- Betsy Beyer et al., *Site Reliability Engineering* (bab tentang manajemen insiden dan postmortem)
- Betsy Beyer et al., *The Site Reliability Workbook* (praktik on-call dan respons insiden)
- John Allspaw, *Blameless PostMortems and a Just Culture* (Etsy engineering)
- Sidney Dekker, *The Field Guide to Understanding Human Error*
- Charles Perrow, *Normal Accidents: Living with High-Risk Technologies*
- U.S. Federal Emergency Management Agency, materi rujukan *Incident Command System (ICS)*
- PagerDuty, *Incident Response Documentation* (praktik sumber terbuka)
