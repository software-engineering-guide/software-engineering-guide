# 2.11 Kualitas perangkat lunak

## Tinjauan dan motivasi

[Kualitas perangkat lunak](https://en.wikipedia.org/wiki/Software_quality) adalah seberapa baik sebuah sistem memenuhi kebutuhan yang dinyatakan dan ekspektasi yang wajar. Itu berarti lebih dari apakah ia berfungsi: itu berarti apakah sistem andal, aman, dapat dipelihara, dapat digunakan, berkinerja, dan sesuai dengan tujuannya dari waktu ke waktu. Kualitas lebih luas daripada pengujian. Pengujian (bab 2.4) adalah satu kegiatan yang mengungkap cacat. Kualitas adalah seluruh disiplin membangun hal yang tepat dengan baik, dan mengetahui, dengan bukti, bahwa Anda telah melakukannya. Sistem dapat lolos setiap tes dan tetap berkualitas rendah bila tidak dapat dipelihara, tidak dapat diakses, atau cocok dengan buruk dengan apa yang sebenarnya dibutuhkan pengguna.

Pada tim besar, kualitas tidak dapat hidup di satu kepala atau kebiasaan satu tim. Ratusan insinyur, banyak produk, dan sistem berumur panjang membutuhkan definisi kualitas bersama, proses eksplisit untuk menjaminnya, dan pengukuran yang memberi tahu Anda apakah ia membaik atau memburuk. Tanpa itu, "kualitas" menjadi aspirasi samar yang kalah dalam setiap argumen melawan tenggat, dan cacat menumpuk sampai perubahan menjadi lambat dan berisiko.

Dalam konteks enterprise dan pemerintah, taruhannya naik lebih tinggi. Sistem yang diatur, kritis keselamatan, dan menghadap warga harus mendemonstrasikan kualitas, bukan sekadar menegaskannya: proses terdokumentasi, bukti yang dapat dilacak, dan verifikasi independen sering wajib. Kualitas yang buruk membawa biaya keuangan, hukum, dan reputasi langsung, dan di beberapa ranah membahayakan orang. Disiplin kualitas yang disengaja, dibangun dari model, proses, pengukuran, dan budaya, adalah yang mengubah kualitas dari kecelakaan menjadi hasil yang dikelola.

## Prinsip utama

- Kualitas adalah kesesuaian dengan tujuan ditambah kepatuhan pada persyaratan; definisikan keduanya secara eksplisit.
- Kualitas dibangun masuk, bukan diuji masuk; verifikasi menemukan cacat, tetapi pencegahan menghindarinya.
- Bedakan [jaminan kualitas](https://en.wikipedia.org/wiki/Quality_assurance) (apakah proses kita sehat?) dari [kendali kualitas](https://en.wikipedia.org/wiki/Quality_control) (apakah produk ini baik?).
- Verifikasi bertanya "apakah kita membangunnya dengan benar?"; validasi bertanya "apakah kita membangun hal yang benar?"
- Ukur kualitas dengan sekumpulan kecil metrik bermakna; perlakukan metrik sebagai sinyal, bukan target.
- Biaya cacat naik semakin lambat ia ditemukan, jadi geser kegiatan kualitas lebih awal.
- Kualitas adalah sifat seluruh organisasi dan budayanya, bukan gerbang di akhir.

## Rekomendasi

### Adopsi model kualitas bersama seperti ISO/IEC 25010

Beri organisasi Anda kosakata bersama tentang kualitas dengan mengadopsi model kualitas produk yang diakui. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) mendefinisikan karakteristik termasuk kesesuaian fungsional, efisiensi kinerja, kompatibilitas, kegunaan, keandalan, keamanan, kemudahan pemeliharaan, dan portabilitas. Gunakan untuk membuat kualitas konkret: untuk setiap sistem, putuskan karakteristik mana yang paling penting dan apa arti "cukup baik" untuk masing-masing. Karakteristik kualitas produk ini adalah **atribut kualitas** yang sama yang menggerakkan arsitektur (bab 3.1). Kualitas dan arsitektur adalah dua pandangan atas satu perhatian, jadi biarkan keduanya berbagi satu daftar prioritas alih-alih dua yang bersaing.

### Pisahkan jaminan kualitas dari kendali kualitas

Perlakukan jaminan kualitas (QA) dan kendali kualitas (QC) sebagai kegiatan yang berbeda tetapi saling melengkapi. QA berorientasi proses dan preventif: ia memperbaiki cara pekerjaan dilakukan, lewat standar, tinjauan, definisi selesai, dan pelatihan, agar cacat kecil kemungkinannya muncul sejak awal. QC berorientasi produk dan detektif: ia memeriksa produk kerja aktual, seperti pengujian, [tinjauan kode](https://en.wikipedia.org/wiki/Code_review), dan audit, untuk menangkap cacat yang sempat masuk. Organisasi yang matang berinvestasi pada keduanya, tetapi condong ke QA, karena mencegah cacat lebih murah daripada menemukan dan memperbaikinya.

### Jalankan proses manajemen kualitas perangkat lunak yang eksplisit

Jadikan kualitas proses yang dikelola, bukan harapan yang diam. Untuk pekerjaan penting, tulis rencana kualitas yang menyatakan karakteristik kualitas target, kegiatan jaminan dan kendali, kriteria penerimaan, dan siapa yang bertanggung jawab. Jalin ke dalam praktik yang sudah Anda miliki: tinjauan kode (bab 2.5) sebagai kendali sekaligus cara berbagi pengetahuan, strategi pengujian (bab 2.4) sebagai jaring pengaman otomatis, dan [analisis statis](https://en.wikipedia.org/wiki/Static_program_analysis) sebagai inspeksi berkelanjutan. Tinjau data kualitas secara berkala dan bertindak atas tren, alih-alih hanya bereaksi terhadap insiden.

### Praktikkan verifikasi dan validasi sebagai disiplin yang berbeda

Verifikasi mengonfirmasi bahwa produk kerja memenuhi spesifikasinya, sehingga masukan yang tepat pada setiap tahap menghasilkan keluaran yang tepat, lewat tinjauan, analisis statis, dan pengujian terhadap persyaratan. Validasi mengonfirmasi bahwa sistem yang selesai benar-benar memenuhi kebutuhan pengguna dan penggunaan yang dimaksudkan, lewat pengujian pengguna, pengujian penerimaan, pilot, dan umpan balik lapangan. Anda memerlukan keduanya. Sistem dapat benar terhadap spesifikasi yang cacat (terverifikasi tetapi tidak valid), atau dapat menjawab kebutuhan nyata sambil tetap mengandung cacat (valid tetapi tidak terverifikasi). Dalam lingkungan yang diatur, [verifikasi dan validasi](https://en.wikipedia.org/wiki/Verification_and_validation) independen (IV&V) oleh pihak yang terpisah dari pengembang mungkin diwajibkan.

### Ukur kualitas dengan metrik yang bermakna

Pilih sekumpulan kecil metrik yang mencerminkan hasil kualitas dan pendorongnya, dan awasi dari waktu ke waktu. Ukuran yang berguna mencakup kepadatan cacat, tingkat cacat yang lolos (cacat yang ditemukan di produksi versus sebelum rilis), waktu rata-rata mendeteksi dan memperbaiki, tingkat kegagalan perubahan, sinyal kesehatan kode seperti kompleksitas dan duplikasi, serta sinyal validasi seperti masalah yang dilaporkan pengguna dan kesesuaian aksesibilitas. Jauhi metrik pajangan dan yang dapat dipermainkan: metrik yang menjadi target berhenti mengukur kenyataan. Pasangkan angka dengan sinyal kualitatif dari tinjauan dan umpan balik pengguna.

### Karakterisasi dan kelola cacat secara sistematis

Perlakukan cacat sebagai data, bukan sekadar kebakaran untuk dipadamkan. Klasifikasikan menurut tingkat keparahan, jenis, dan akar penyebab. Lacak dari penemuan hingga penyelesaian. Cari pola agar Anda dapat mencegah kekambuhan. Gunakan teknik seperti [analisis akar penyebab](https://en.wikipedia.org/wiki/Root_cause_analysis) dan kategorisasi cacat untuk membedakan kesalahan sekali jalan dari kelemahan sistemik. Salurkan apa yang Anda pelajari kembali ke QA, lewat standar yang diperbarui, tes tambahan, dan tinjauan yang diperbaiki, agar kelas cacat yang sama tidak kembali. Cacat yang diperbaiki tanpa memahami penyebabnya adalah cacat yang Anda undang kembali.

### Kelola biaya kualitas dengan sengaja

Pahami ekonomi kualitas lewat kategori klasik: biaya pencegahan (pelatihan, standar, desain yang baik, perkakas), biaya penilaian (tinjauan, pengujian, audit), dan biaya kegagalan (pengerjaan ulang internal sebelum rilis, ditambah kegagalan eksternal yang ditemukan pengguna, yang jauh lebih mahal). Geser investasi Anda menuju pencegahan dan penilaian awal, karena setiap dolar di sana menghindari banyak dolar biaya kegagalan kelak. Buat biaya ini terlihat, agar "kami tidak punya waktu untuk kualitas" dilihat apa adanya: pilihan untuk membelanjakan lebih banyak pada kegagalan.

### Bangun budaya kualitas

Jadikan kualitas tanggung jawab semua orang, dimiliki tim yang membangun perangkat lunak, alih-alih diserahkan ke departemen QA hilir yang memeriksanya di akhir. Pemimpin harus menghargai hasil kualitas, membuat aman untuk melaporkan cacat dan nyaris-celaka, dan memperlakukan data kualitas sebagai alat belajar, bukan tongkat. Pendekatan tanpa menyalahkan terhadap cacat membawa masalah ke permukaan lebih awal. Pendekatan yang menyalahkan menyembunyikannya sampai mahal.

## Trade-off: kelebihan dan kekurangan

| Praktik / pilihan | Kelebihan | Kekurangan |
|---|---|---|
| Model kualitas formal (ISO 25010) | Kosakata bersama; prioritas eksplisit | Beban bila diterapkan dogmatis |
| Jaminan kualitas berat (pencegahan) | Cacat lebih sedikit; total biaya lebih rendah | Investasi di muka; lebih lambat menunjukkan hasil |
| Kendali kualitas berat (inspeksi) | Menangkap cacat yang lolos | Mahal; menemukan cacat terlambat |
| V&V independen | Jaminan tinggi; objektif | Mahal; lebih lambat; bisa terasa memusuhi |
| Metrik kualitas yang kaya | Visibilitas; peringatan dini | Risiko permainan; beban pengukuran |
| Tim QA khusus | Fokus dan keahlian | Dapat melepas tanggung jawab dari pengembang |
| Kualitas dimiliki tim | Kepemilikan; umpan balik cepat | Memerlukan disiplin dan keterampilan di mana-mana |

Trade-off pusatnya adalah investasi versus jaminan, dibentuk oleh waktu. Pencegahan memakan uang sekarang untuk menghindari biaya kegagalan yang lebih besar kelak. Jadi tingkat kualitas yang secara ekonomi tepat bukan maksimum; melainkan titik di mana biaya marjinal jaminan tambahan sama dengan biaya kegagalan yang dihindarinya. Titik itu tinggi untuk sistem kritis keselamatan dan lebih rendah untuk perkakas internal berpertaruhan rendah. Ketegangan berulang lainnya adalah kepemilikan. Kelompok QA pusat membangun keahlian tetapi dapat membiarkan pengembang melepas tanggung jawab. Kualitas yang dimiliki tim membangun kepemilikan tetapi menuntut keterampilan dan disiplin di mana-mana.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Ketika kelas cacat yang sama muncul dua kali, apakah kita menjalankan analisis akar penyebab, atau hanya memperbaikinya lagi?** Cacat yang diperbaiki tanpa memahami penyebabnya adalah cacat yang Anda undang kembali, dan pada tim besar akar penyebab yang sama dapat muncul di banyak layanan sebelum ada yang menghubungkan titik-titiknya. Memperlakukan cacat sebagai data (diklasifikasi menurut keparahan, jenis, dan penyebab, lalu ditambang untuk pola) adalah yang membedakan tim yang semakin andal dari yang tetap sibuk memperbaiki ulang kesalahan yang sama. Bawa pelacak cacat Anda ke rapat dan cari tanda tangan yang berulang: berapa banyak insiden terbaru yang berbagi penyebab yang tidak pernah Anda tangani secara sistemik? Jawabannya harus memberi makan pencegahan, sehingga penyebab berulang menggerakkan standar yang diperbarui, pembantu bersama baru, tes tambahan, atau daftar periksa tinjauan yang lebih baik, karena begitulah perbaikan di satu tempat menghentikan seluruh kelas agar tidak kembali.

2. **Apakah aman di tim kita melaporkan cacat atau nyaris-celaka, dan apa yang terjadi pada orang yang mengangkatnya?** Kualitas adalah sifat budaya, dan pendekatan tanpa menyalahkan membawa masalah ke permukaan lebih awal sementara yang menyalahkan menyembunyikannya sampai mahal, yang dalam sistem yang diatur atau menghadap warga dapat berarti kegagalan publik atau penalti. Ini paling penting pada skala besar, di mana insinyur yang paling dekat dengan risiko sering junior dan insentif untuk diam kuat. Bawa sinyal jujur: apakah nyaris-celaka dicatat dan dibahas, atau lenyap? Apakah postmortem menyebut penyebab atau menyebut orang? Tindakannya adalah menjadikan data kualitas alat belajar alih-alih tongkat, menghargai orang yang memunculkan masalah, dan menjalankan postmortem tanpa menyalahkan, karena Anda tidak dapat mencegah apa yang ditakuti tim Anda untuk dilaporkan.

3. **Dapatkah validasi benar-benar menghentikan rilis, dan siapa yang memegang wewenang itu ketika tenggat mendekat?** Verifikasi (apakah kita membangunnya dengan benar?) dan validasi (apakah kita membangun hal yang benar?) adalah disiplin yang berbeda, dan validasi hanya bertaring jika pemeriksaan aksesibilitas yang gagal, tes penerimaan yang gagal, atau riset pengguna yang memberatkan benar-benar dapat memblokir pengiriman. Dalam konteks enterprise dan pemerintah ini sering wajib, kadang lewat verifikasi dan validasi independen oleh pihak yang terpisah dari pengembang, dan "kami tetap merilisnya" bukan jawaban yang diterima badan pengawas. Bawa beberapa rilis terakhir Anda: apakah sinyal kualitas pernah benar-benar menghentikan satu, atau gerbang selalu mengalah pada tanggal? Jika validasi tidak pernah memblokir rilis, ia hiasan, dan perbaikannya adalah menuliskan kriteria penerimaan ke dalam rencana kualitas di muka, menamai siapa yang memiliki keputusan jalan/tidak, dan memberi keputusan itu wewenang nyata yang independen dari tekanan pengiriman.

4. **Apakah kita benar-benar tahu biaya kualitas buruk kita, dan apakah kita dengan sengaja menggeser pengeluaran dari kegagalan ke pencegahan?** Biaya kualitas buruk (COPQ) adalah uang yang hilang pada pengerjaan ulang internal, insiden produksi, perbaikan darurat, beban dukungan, pengguna yang hilang, dan penalti, dan hampir selalu lebih besar daripada pengeluaran terlihat untuk tinjauan dan pengujian. Pada tim besar biaya kegagalan tersebar di kanal insiden, antrean dukungan, dan pengerjaan ulang yang tidak dicatat siapa pun sebagai pengerjaan ulang, sehingga tetap tak terlihat sampai seseorang menjumlahkannya. Ketegangannya adalah bahwa pencegahan memakan uang sekarang, dalam siklus anggaran, untuk menghindari biaya kegagalan yang jatuh kemudian dan jatuh pada anggaran orang lain, yang membuat pertukaran itu mudah ditunda selamanya. Bawa angka nyata: jumlah dan biaya insiden, jam pengerjaan ulang, tingkat cacat yang lolos, dan pembagian pengeluaran saat ini di antara pencegahan, penilaian, dan kegagalan, lalu putuskan apakah campuran harus bergeser lebih awal. Untuk sistem enterprise dan pemerintah, di mana sebagian besar biaya seumur hidup jatuh setelah rilis pertama, letakkan COPQ di depan orang yang memegang anggaran, karena angka yang dapat dilihat badan pengawas jauh lebih sulit ditukar daripada seruan samar pada "kualitas".

5. **Metrik kualitas kita yang mana yang diam-diam telah menjadi target, dan perilaku apa yang kini didorongnya?** Metrik yang menjadi target berhenti mengukur kenyataan: kejar persentase cakupan dan Anda mendapat tes yang ditulis untuk menggerakkan angka, bukan tes yang menangkap cacat. Pada skala besar ini berbahaya, karena dasbor utama yang dibagikan di puluhan tim menetapkan insentif bagi semuanya, dan metrik yang dapat dipermainkan menyebarkan permainan ke mana-mana sekaligus. Pertimbangan yang bersaing adalah bahwa Anda tetap membutuhkan pengukuran, jadi jawabannya jarang "buang metrik" melainkan "pasangkan dengan sinyal tandingan dan baca bersama bukti kualitatif dari tinjauan dan pengguna". Bawa kumpulan metrik Anda saat ini dan, untuk masing-masing, tanyakan apa yang dapat dilakukan seseorang di bawah tekanan untuk menggerakkannya tanpa memperbaiki kualitas, dan apakah Anda pernah melihatnya terjadi. Dalam konteks yang diatur dan menghadap warga, waspadai khususnya metrik kepatuhan yang tampak hijau sementara validasi yang mendasarinya (aksesibilitas, hasil pengguna nyata) tidak pernah benar-benar dijalankan, karena auditor akhirnya akan menguji kenyataan di balik angka.

6. **Siapa yang memiliki kualitas di sini: tim yang menulis kode, atau kelompok terpisah di akhir, dan mana yang sebenarnya kita beri sumber daya?** Kepemilikan membentuk segalanya di hilir, karena silo QA hilir membiarkan pengembang melepas tanggung jawab atas kode yang mereka tulis, sementara kualitas yang dimiliki tim membangun kepemilikan dengan biaya menuntut keterampilan dan disiplin di setiap tim. Pada tim besar ini bukan salah satu: pola berkelanjutan biasanya tim memiliki kualitas lewat tinjauan kode dan tes otomatis, didukung kelompok pusat kecil yang memelihara standar, menjalankan jaminan kualitas sebagai perbaikan proses, dan membimbing, alih-alih memeriksa kualitas masuk di akhir. Bawa peta jujur tentang di mana pekerjaan kualitas saat ini terjadi, siapa yang bertanggung jawab ketika cacat lolos, dan di mana anggaran serta personel sebenarnya berada versus di mana retorika mengatakan kualitas hidup. Untuk organisasi enterprise dan pemerintah, tambahkan persyaratan verifikasi dan validasi independen: sebagian rezim jaminan mewajibkan pihak terpisah, jadi putuskan dengan sengaja kontrol mana yang menjadi milik tim pengiriman dan mana yang harus tetap independen untuk memenuhi audit.

## Lensa sektor

**Startup.** Kecepatan lebih penting daripada upacara, jadi namai dua atau tiga karakteristik kualitas yang benar-benar melindungi produk Anda, biasanya keandalan dan kemudahan pemeliharaan, dan biarkan polesan menunggu. Miliki kualitas di seluruh tim dengan tinjauan kode dan rangkaian tes otomatis sederhana alih-alih mendirikan kelompok QA terpisah yang tidak sanggup Anda isi stafnya. Ketika kelas bug yang sama muncul dua kali, habiskan dua puluh menit untuk akar penyebab dan tambahkan satu pembantu bersama ditambah tes, agar pencegahan tetap murah dan tingkat kegagalan perubahan Anda tetap rendah sambil bergerak cepat.

**Bisnis kecil.** Tanpa spesialis kualitas khusus dan dengan anggaran ketat, bersandarlah pada kualitas yang tertanam dalam perkakas dan platform yang Anda beli alih-alih proses yang harus Anda jalankan. Ketika memilih perangkat lunak, perlakukan bukti kualitas vendor sebagai bagian dari pembelian: postur keamanan, aksesibilitas, daya tanggap dukungan, dan seberapa sering rilis mereka rusak. Lacak segelintir sinyal murah dan jujur (insiden produksi, masalah yang dilaporkan pelanggan, waktu perbaikan) alih-alih program metrik rumit yang tidak ada orang untuk memeliharanya.

**Enterprise.** Pekerjaannya adalah konsistensi di banyak tim: adopsi model kualitas bersama seperti ISO/IEC 25010, pisahkan jaminan kualitas (proses) dari kendali kualitas (produk), dan jalankan tinjauan biaya kualitas yang menggeser pengeluaran ke pencegahan. Jaga kualitas dimiliki tim pengiriman, didukung kelompok pusat kecil yang memelihara standar dan dasbor untuk tingkat cacat yang lolos, tingkat kegagalan perubahan, dan tren kesehatan kode. Bakukan kosakata dan gerbang agar kelompok berhenti menciptakan ulang praktik kualitas, sambil memberi tim ruang untuk memenuhi standar itu dengan cara mereka sendiri.

**Pemerintah.** Pengadaan, transparansi, dan akuntabilitas publik menetapkan bingkai, jadi tuliskan persyaratan kualitas ke dalam kontrak dan wajibkan bukti kualitas yang terdokumentasi dan dapat dilacak alih-alih pernyataan. Harapkan verifikasi dan validasi independen oleh pihak yang terpisah dari pengembang, kesesuaian aksesibilitas yang wajib, dan catatan cacat dengan keparahan dan akar penyebab disimpan sebagai bagian dari jejak audit. Laporkan angka biaya kualitas buruk (pengerjaan ulang, banding, kegagalan layanan) kepada badan pengawas, dan beri validasi wewenang nyata untuk memblokir rilis yang akan mengecewakan warga yang bergantung padanya.

## Contoh

**Startup.** Sebuah startup lima orang memutuskan bahwa untuk produk awalnya, keandalan dan kemudahan pemeliharaan adalah karakteristik kualitas yang penting, dan membiarkan polesan sempurna-piksel menunggu. Kualitas dimiliki seluruh tim: tinjauan kode dan rangkaian tes otomatis sederhana adalah kendalinya, dan tidak ada kelompok QA terpisah untuk melempar cacat. Ketika kelas bug yang sama muncul dua kali, mereka menghabiskan dua puluh menit pada pandangan akar penyebab cepat dan menambahkan satu pembantu bersama ditambah tes, sehingga tidak berulang alih-alih diperbaiki ulang dengan tangan setiap kali. Kebiasaan kecil pencegahan itu menjaga tingkat kegagalan perubahan mereka tetap rendah selagi mereka masih bergerak cepat.

**Enterprise.** Sebuah firma jasa keuangan besar mengadopsi ISO/IEC 25010 sebagai kosakata kualitasnya dan, untuk setiap produk, mencatat tingkat target untuk keandalan, keamanan, dan kemudahan pemeliharaan. Tim memiliki kualitas: tinjauan kode dan tes otomatis adalah kendali di pipeline, sementara kelompok pusat kecil menjalankan QA dengan memelihara standar dan membimbing. Dasbor kualitas melacak tingkat cacat yang lolos, tingkat kegagalan perubahan, dan tren kesehatan kode. Cacat diklasifikasi dan dicari akar penyebabnya, dan penyebab berulang menggerakkan pembaruan pada pustaka bersama dan daftar periksa. Pimpinan meninjau data biaya kualitas tiap kuartal dan telah menggeser pengeluaran ke pencegahan, memangkas baik insiden produksi maupun biaya memperbaikinya.

**Pemerintah.** Sebuah lembaga nasional yang menyampaikan platform tunjangan yang menghadap warga bekerja di bawah rezim jaminan yang mensyaratkan bukti kualitas terdokumentasi. Ia menjalankan proses manajemen kualitas formal dengan rencana kualitas per rilis, ditambah verifikasi dan validasi independen oleh tim yang terpisah dari pengembang. Verifikasi memeriksa setiap produk kerja terhadap persyaratan yang dilacak ke kebijakan. Validasi mencakup pengujian kesesuaian aksesibilitas dan riset pengguna dengan warga nyata, dan keduanya dapat memblokir rilis. Cacat dilacak dengan keparahan dan akar penyebab sebagai bagian dari jejak audit, dan angka biaya kualitas buruk (pengerjaan ulang, banding, dan kegagalan layanan) diserahkan kepada badan pengawas untuk membenarkan investasi berkelanjutan dalam pencegahan.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil kualitas adalah total biaya kepemilikan yang lebih rendah dan kecepatan pengiriman yang stabil. Biaya kualitas punya dua sisi. Pengeluaran yang baik, pencegahan dan penilaian, terlihat dan dapat dikendalikan: desain, standar, tinjauan, pengujian, dan perkakas. Biaya kualitas buruk (COPQ) lebih besar tetapi sering tersembunyi: pengerjaan ulang internal, insiden produksi, perbaikan darurat, dukungan pelanggan, pengguna yang hilang, penalti regulasi, dan kerusakan reputasi. Studi sejak "Quality Is Free" Crosby secara konsisten menemukan bahwa total biaya kualitas buruk melampaui biaya mencegahnya, dan bahwa cacat menjadi jauh lebih mahal semakin lambat Anda menangkapnya: isu yang ditemukan dalam desain memakan sebagian kecil dari isu yang sama yang ditemukan di produksi.

Bagi pimpinan, argumennya bukan "belanjakan lebih banyak untuk kualitas." Melainkan "belanjakan lebih awal untuk membelanjakan lebih sedikit secara keseluruhan." Kuantifikasi COPQ dari data Anda sendiri (jumlah dan biaya insiden, jam pengerjaan ulang, tingkat cacat yang lolos) dan tunjukkan bagaimana pencegahan serta penilaian awal menurunkannya. Hubungkan kualitas dengan hasil bisnis: keandalan mempertahankan pelanggan, kemudahan pemeliharaan menjaga perubahan mendatang tetap murah, dan keamanan serta aksesibilitas menjauhkan Anda dari masalah hukum. Dalam sistem enterprise dan pemerintah berumur panjang, di mana sebagian besar biaya jatuh setelah rilis pertama, dimensi kemudahan pemeliharaan dan keandalan dari kualitas mendominasi biaya seumur hidup. Itu menjadikan investasi kualitas awal salah satu keputusan berdaya ungkit tertinggi yang dapat Anda buat.

## Anti-pola dan jebakan

- **Kualitas sebagai gerbang akhir:** memeriksa kualitas masuk di akhir alih-alih membangunnya masuk, sehingga cacat ditemukan ketika paling mahal.
- **Mencampuradukkan pengujian dengan kualitas:** mengira tes yang lolos berarti kualitas tinggi, mengabaikan kemudahan pemeliharaan, kegunaan, dan kesesuaian dengan tujuan.
- **QA sebagai silo terpisah:** tim hilir yang "memiliki kualitas," membiarkan pengembang melepas tanggung jawab atas kode yang mereka tulis.
- **Teater metrik:** mengejar persentase cakupan atau jumlah cacat sebagai target, yang mengundang permainan dan menyembunyikan kualitas nyata.
- **Verifikasi tanpa validasi:** membangun spesifikasi dengan benar tanpa pernah memeriksa bahwa spesifikasi memenuhi kebutuhan nyata.
- **Tanpa analisis akar penyebab:** memperbaiki cacat satu per satu tanpa menangani penyebab sistemik, sehingga kelas yang sama berulang.
- **Mengabaikan biaya kualitas buruk:** memperlakukan kualitas sebagai biaya murni karena biaya kegagalan tersembunyi dan tak terukur.

## Model kematangan

**Tingkat 1 (Memulai).** Kualitas tidak terdefinisi dan ad hoc. Ia bergantung pada ketekunan individu, diperiksa terutama lewat pengujian manual di akhir, dan cacat ditangani secara reaktif saat muncul. Tidak ada model bersama, tidak ada metrik, dan tidak ada garis antara jaminan dan kendali.

**Tingkat 2 (Mengembangkan).** Praktik dasar muncul: tinjauan kode, tes otomatis, dan pelacak cacat. Sebagian data kualitas dikumpulkan, tetapi tidak merata, dan setiap tim melakukannya dengan caranya sendiri. Kualitas masih sebagian besar dipandang sebagai pengujian, pencegahan minimal, verifikasi terjadi, dan validasi informal.

**Tingkat 3 (Membakukan).** Organisasi mengadopsi model kualitas bersama (seperti ISO/IEC 25010), memisahkan QA dari QC, dan menjalankan proses manajemen kualitas dengan rencana kualitas dan kriteria penerimaan, terdokumentasi dan diterapkan konsisten di semua tim. Verifikasi dan validasi berbeda dan disengaja, dan cacat diklasifikasi serta dicari akar penyebabnya menurut skema yang disepakati.

**Tingkat 4 (Mengelola).** Kualitas diukur dan dikendalikan terhadap garis dasar. Sekumpulan kecil metrik bermakna dilacak dari waktu ke waktu (kepadatan cacat, tingkat cacat yang lolos, waktu rata-rata mendeteksi dan memperbaiki, tingkat kegagalan perubahan, dan sinyal kesehatan kode seperti kompleksitas dan duplikasi), dan biaya kualitas dikuantifikasi di seluruh pencegahan, penilaian, dan kegagalan. Gerbang penerimaan dan kualitas ditegakkan berdasarkan bukti alih-alih opini, tren ditinjau pada irama tetap, dan validasi benar-benar dapat memblokir rilis.

**Tingkat 5 (Mengorkestrasi).** Kualitas adalah disiplin yang terus diperbaiki dan dimiliki secara budaya yang terintegrasi dengan perencanaan bisnis dan risiko. Pencegahan adalah penekanannya, data biaya kualitas memandu ke mana investasi pergi, dan temuan akar penyebab secara sistematis mencegah kekambuhan. Tim memiliki kualitas dari ujung ke ujung, metrik memberi makan perbaikan berkelanjutan, dan organisasi menyesuaikan praktik kualitasnya seiring bergesernya produk, risiko, dan regulasi. Ini selaras dengan tingkat lebih tinggi model kematangan di bab 10.8.

## Gagasan untuk didiskusikan

- Karakteristik kualitas ISO/IEC 25010 mana yang paling penting untuk sistem Anda, dan apa arti "cukup baik" untuk masing-masing?
- Di mana organisasi Anda berada pada campuran pengeluaran pencegahan-penilaian-kegagalan, dan haruskah bergeser?
- Apakah Anda membedakan verifikasi dari validasi dalam praktik, atau menggabungkan keduanya menjadi "pengujian"?
- Apakah kualitas dimiliki tim yang membangun perangkat lunak, atau didelegasikan ke kelompok terpisah, dan apa yang akan berubah jika Anda memindahkannya?
- Berapa biaya kualitas buruk Anda yang sebenarnya, dan dapatkah Anda mengukurnya cukup baik untuk membuat kasus bisnis?
- Metrik kualitas Anda yang mana yang merupakan sinyal sejati, dan mana yang telah menjadi target yang dapat dipermainkan?

## Poin-poin utama

- Kualitas lebih luas daripada pengujian: ia kesesuaian dengan tujuan ditambah kepatuhan, di seluruh karakteristik seperti keandalan, keamanan, dan kemudahan pemeliharaan.
- Gunakan model kualitas bersama (ISO/IEC 25010) agar atribut kualitas eksplisit dan selaras dengan arsitektur (bab 3.1).
- Pisahkan jaminan kualitas (cegah, proses) dari kendali kualitas (deteksi, produk), dan condong ke pencegahan.
- Praktikkan verifikasi (dibangun dengan benar) dan validasi (dibangun hal yang benar) sebagai disiplin yang berbeda.
- Ukur kualitas dengan beberapa metrik bermakna, dan karakterisasi cacat menurut keparahan dan akar penyebab untuk mencegah kekambuhan.
- Kelola biaya kualitas: pencegahan dan penilaian awal jauh lebih murah daripada kegagalan, terutama pada sistem berumur panjang.
- Bangun budaya kualitas tanpa menyalahkan di mana tim memiliki kualitas, didukung tinjauan kode (bab 2.5) dan strategi pengujian (bab 2.4).

## Referensi dan bacaan lanjutan

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, area pengetahuan Software Quality.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- Seri ISO/IEC 25000 (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones dan Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (konteks proses jaminan kualitas dan V&V).
