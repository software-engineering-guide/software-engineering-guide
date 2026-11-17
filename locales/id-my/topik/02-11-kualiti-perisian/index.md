# 2.11 Kualiti perisian

## Tinjauan dan motivasi

[Kualiti perisian](https://en.wikipedia.org/wiki/Software_quality) adalah seberapa baik sebuah sistem memenuhi kebutuhan yang dinyatakan dan ekspektasi yang wajar. Itu berarti lebih dari apakah ia berfungsi: itu berarti apakah sistem andal, aman, dapat dipelihara, dapat digunakan, berkinerja, dan sesuai dengan tujuannya dari waktu ke waktu. Kualiti lebih luas daripada pengujian. Pengujian (bab 2.4) adalah satu kegiatan yang mengungkap cacat. Kualiti adalah seluruh disiplin membangun hal yang tepat dengan baik, dan mengetahui, dengan bukti, bahwa Anda telah melakukannya. Sistem dapat lolos setiap tes dan tetap berkualitas rendah bila tidak dapat dipelihara, tidak dapat diakses, atau cocok dengan buruk dengan apa yang sebenarnya dibutuhkan pengguna.

Pada tim besar, kualiti tidak dapat hidup di satu kepala atau kebiasaan satu tim. Ratusan insinyur, banyak produk, dan sistem berumur panjang membutuhkan definisi kualiti bersama, proses eksplisit untuk menjaminnya, dan pengukuran yang memberi tahu Anda apakah ia membaik atau memburuk. Tanpa itu, "kualiti" menjadi aspirasi samar yang kalah dalam setiap argumen melawan tenggat, dan cacat menumpuk sampai perubahan menjadi lambat dan berisiko.

Dalam konteks enterprise dan pemerintah, taruhannya naik lebih tinggi. Sistem yang diatur, kritis keselamatan, dan menghadap warga harus mendemonstrasikan kualiti, bukan sekadar menegaskannya: proses terdokumentasi, bukti yang dapat dilacak, dan verifikasi independen sering wajib. Kualiti yang buruk membawa biaya keuangan, hukum, dan reputasi langsung, dan di beberapa ranah membahayakan orang. Disiplin kualiti yang disengaja, dibangun dari model, proses, pengukuran, dan budaya, adalah yang mengubah kualiti dari kecelakaan menjadi hasil yang dikelola.

## Prinsip utama

- Kualiti adalah kesesuaian dengan tujuan ditambah kepatuhan pada persyaratan; definisikan keduanya secara eksplisit.
- Kualiti dibangun masuk, bukan diuji masuk; verifikasi menemukan cacat, tetapi pencegahan menghindarinya.
- Bedakan [jaminan kualiti](https://en.wikipedia.org/wiki/Quality_assurance) (apakah proses kita sehat?) dari [kendali kualiti](https://en.wikipedia.org/wiki/Quality_control) (apakah produk ini baik?).
- Verifikasi bertanya "apakah kita membangunnya dengan benar?"; validasi bertanya "apakah kita membangun hal yang benar?"
- Ukur kualiti dengan sekumpulan kecil metrik bermakna; perlakukan metrik sebagai sinyal, bukan target.
- Biaya cacat naik semakin lambat ia ditemukan, jadi geser kegiatan kualiti lebih awal.
- Kualiti adalah sifat seluruh organisasi dan budayanya, bukan gerbang di akhir.

## Rekomendasi

### Adopsi model kualiti bersama seperti ISO/IEC 25010

Beri organisasi Anda kosakata bersama tentang kualiti dengan mengadopsi model kualiti produk yang diakui. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) mendefinisikan karakteristik termasuk kesesuaian fungsional, efisiensi kinerja, kompatibilitas, kegunaan, keandalan, keamanan, kemudahan pemeliharaan, dan portabilitas. Gunakan untuk membuat kualiti konkret: untuk setiap sistem, putuskan karakteristik mana yang paling penting dan apa arti "cukup baik" untuk masing-masing. Karakteristik kualiti produk ini adalah **atribut kualiti** yang sama yang menggerakkan arsitektur (bab 3.1). Kualiti dan arsitektur adalah dua pandangan atas satu perhatian, jadi biarkan keduanya berbagi satu daftar prioritas alih-alih dua yang bersaing.

### Pisahkan jaminan kualiti dari kendali kualiti

Perlakukan jaminan kualiti (QA) dan kendali kualiti (QC) sebagai kegiatan yang berbeda tetapi saling melengkapi. QA berorientasi proses dan preventif: ia memperbaiki cara pekerjaan dilakukan, lewat standar, tinjauan, definisi selesai, dan pelatihan, agar cacat kecil kemungkinannya muncul sejak awal. QC berorientasi produk dan detektif: ia memeriksa produk kerja aktual, seperti pengujian, [tinjauan kode](https://en.wikipedia.org/wiki/Code_review), dan audit, untuk menangkap cacat yang sempat masuk. Organisasi yang matang berinvestasi pada keduanya, tetapi condong ke QA, kerana mencegah cacat lebih murah daripada menemukan dan memperbaikinya.

### Jalankan proses manajemen kualiti perisian yang eksplisit

Jadikan kualiti proses yang dikelola, bukan harapan yang diam. Untuk pekerjaan penting, tulis rencana kualiti yang menyatakan karakteristik kualiti target, kegiatan jaminan dan kendali, kriteria penerimaan, dan siapa yang bertanggung jawab. Jalin ke dalam praktik yang sudah Anda miliki: tinjauan kode (bab 2.5) sebagai kendali sekaligus cara berbagi pengetahuan, strategi pengujian (bab 2.4) sebagai jaring pengaman otomatis, dan [analisis statis](https://en.wikipedia.org/wiki/Static_program_analysis) sebagai inspeksi berkelanjutan. Tinjau data kualiti secara berkala dan bertindak atas tren, alih-alih hanya bereaksi terhadap insiden.

### Praktikkan verifikasi dan validasi sebagai disiplin yang berbeda

Verifikasi mengonfirmasi bahwa produk kerja memenuhi spesifikasinya, sehingga masukan yang tepat pada setiap tahap menghasilkan keluaran yang tepat, lewat tinjauan, analisis statis, dan pengujian terhadap persyaratan. Validasi mengonfirmasi bahwa sistem yang selesai benar-benar memenuhi kebutuhan pengguna dan penggunaan yang dimaksudkan, lewat pengujian pengguna, pengujian penerimaan, pilot, dan umpan balik lapangan. Anda memerlukan keduanya. Sistem dapat benar terhadap spesifikasi yang cacat (terverifikasi tetapi tidak valid), atau dapat menjawab kebutuhan nyata sambil tetap mengandung cacat (valid tetapi tidak terverifikasi). Dalam lingkungan yang diatur, [verifikasi dan validasi](https://en.wikipedia.org/wiki/Verification_and_validation) independen (IV&V) oleh pihak yang terpisah dari pengembang mungkin diwajibkan.

### Ukur kualiti dengan metrik yang bermakna

Pilih sekumpulan kecil metrik yang mencerminkan hasil kualiti dan pendorongnya, dan awasi dari waktu ke waktu. Ukuran yang berguna mencakup kepadatan cacat, kadar cacat yang lolos (cacat yang ditemukan di produksi versus sebelum rilis), waktu rata-rata mendeteksi dan memperbaiki, kadar kegagalan perubahan, sinyal kesihatan kode seperti kompleksitas dan duplikasi, serta sinyal validasi seperti masalah yang dilaporkan pengguna dan kesesuaian aksesibilitas. Jauhi metrik pajangan dan yang dapat dipermainkan: metrik yang menjadi target berhenti mengukur kenyataan. Pasangkan angka dengan sinyal kualitatif dari tinjauan dan umpan balik pengguna.

### Karakterisasi dan kelola cacat secara sistematis

Perlakukan cacat sebagai data, bukan sekadar kebakaran untuk dipadamkan. Klasifikasikan menurut kadar keparahan, jenis, dan akar penyebab. Lacak dari penemuan hingga penyelesaian. Cari pola agar Anda dapat mencegah kekambuhan. Gunakan teknik seperti [analisis akar penyebab](https://en.wikipedia.org/wiki/Root_cause_analysis) dan kategorisasi cacat untuk membedakan kesalahan sekali jalan dari kelemahan sistemik. Salurkan apa yang Anda pelajari kembali ke QA, lewat standar yang diperbarui, tes tambahan, dan tinjauan yang diperbaiki, agar kelas cacat yang sama tidak kembali. Cacat yang diperbaiki tanpa memahami penyebabnya adalah cacat yang Anda undang kembali.

### Kelola biaya kualiti dengan sengaja

Pahami ekonomi kualiti lewat kategori klasik: biaya pencegahan (pelatihan, standar, desain yang baik, perkakas), biaya penilaian (tinjauan, pengujian, audit), dan biaya kegagalan (pengerjaan ulang internal sebelum rilis, ditambah kegagalan eksternal yang ditemukan pengguna, yang jauh lebih mahal). Geser investasi Anda menuju pencegahan dan penilaian awal, kerana setiap dolar di sana menghindari banyak dolar biaya kegagalan kelak. Buat biaya ini terlihat, agar "kami tidak punya waktu untuk kualiti" dilihat apa adanya: pilihan untuk membelanjakan lebih banyak pada kegagalan.

### Bangun budaya kualiti

Jadikan kualiti tanggung jawab semua orang, dimiliki tim yang membangun perisian, alih-alih diserahkan ke departemen QA hilir yang memeriksanya di akhir. Pemimpin harus menghargai hasil kualiti, membuat aman untuk melaporkan cacat dan nyaris-celaka, dan memperlakukan data kualiti sebagai alat belajar, bukan tongkat. Pendekatan tanpa menyalahkan terhadap cacat membawa masalah ke permukaan lebih awal. Pendekatan yang menyalahkan menyembunyikannya sampai mahal.

## Trade-off: kelebihan dan kekurangan

| Praktik / pilihan | Kelebihan | Kekurangan |
|---|---|---|
| Model kualiti formal (ISO 25010) | Kosakata bersama; prioritas eksplisit | Beban bila diterapkan dogmatis |
| Jaminan kualiti berat (pencegahan) | Cacat lebih sedikit; total biaya lebih rendah | Investasi di muka; lebih lambat menunjukkan hasil |
| Kendali kualiti berat (inspeksi) | Menangkap cacat yang lolos | Mahal; menemukan cacat terlambat |
| V&V independen | Jaminan tinggi; objektif | Mahal; lebih lambat; bisa terasa memusuhi |
| Metrik kualiti yang kaya | Visibilitas; peringatan dini | Risiko permainan; beban pengukuran |
| Tim QA khusus | Fokus dan keahlian | Dapat melepas tanggung jawab dari pengembang |
| Kualiti dimiliki tim | Kepemilikan; umpan balik cepat | Memerlukan disiplin dan keterampilan di mana-mana |

Trade-off pusatnya adalah investasi versus jaminan, dibentuk oleh waktu. Pencegahan memakan uang sekarang untuk menghindari biaya kegagalan yang lebih besar kelak. Jadi kadar kualiti yang secara ekonomi tepat bukan maksimum; melainkan titik di mana biaya marjinal jaminan tambahan sama dengan biaya kegagalan yang dihindarinya. Titik itu tinggi untuk sistem kritis keselamatan dan lebih rendah untuk perkakas internal berpertaruhan rendah. Ketegangan berulang lainnya adalah kepemilikan. Kelompok QA pusat membangun keahlian tetapi dapat membiarkan pengembang melepas tanggung jawab. Kualiti yang dimiliki tim membangun kepemilikan tetapi menuntut keterampilan dan disiplin di mana-mana.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Ketika kelas cacat yang sama muncul dua kali, apakah kita menjalankan analisis akar penyebab, atau hanya memperbaikinya lagi?** Cacat yang diperbaiki tanpa memahami penyebabnya adalah cacat yang Anda undang kembali, dan pada tim besar akar penyebab yang sama dapat muncul di banyak layanan sebelum ada yang menghubungkan titik-titiknya. Memperlakukan cacat sebagai data (diklasifikasi menurut keparahan, jenis, dan penyebab, lalu ditambang untuk pola) adalah yang membedakan tim yang semakin andal dari yang tetap sibuk memperbaiki ulang kesalahan yang sama. Bawa pelacak cacat Anda ke rapat dan cari tanda tangan yang berulang: berapa banyak insiden terbaru yang berbagi penyebab yang tidak pernah Anda tangani secara sistemik? Jawabannya harus memberi makan pencegahan, sehingga penyebab berulang menggerakkan standar yang diperbarui, pembantu bersama baru, tes tambahan, atau daftar periksa tinjauan yang lebih baik, kerana begitulah perbaikan di satu tempat menghentikan seluruh kelas agar tidak kembali.

2. **Apakah aman di tim kita melaporkan cacat atau nyaris-celaka, dan apa yang terjadi pada orang yang mengangkatnya?** Kualiti adalah sifat budaya, dan pendekatan tanpa menyalahkan membawa masalah ke permukaan lebih awal sementara yang menyalahkan menyembunyikannya sampai mahal, yang dalam sistem yang diatur atau menghadap warga dapat berarti kegagalan publik atau penalti. Ini paling penting pada skala besar, di mana insinyur yang paling dekat dengan risiko sering junior dan insentif untuk diam kuat. Bawa sinyal jujur: apakah nyaris-celaka dicatat dan dibahas, atau lenyap? Apakah postmortem menyebut penyebab atau menyebut orang? Tindakannya adalah menjadikan data kualiti alat belajar alih-alih tongkat, menghargai orang yang memunculkan masalah, dan menjalankan postmortem tanpa menyalahkan, kerana Anda tidak dapat mencegah apa yang ditakuti tim Anda untuk dilaporkan.

3. **Dapatkah validasi benar-benar menghentikan rilis, dan siapa yang memegang wewenang itu ketika tenggat mendekat?** Verifikasi (apakah kita membangunnya dengan benar?) dan validasi (apakah kita membangun hal yang benar?) adalah disiplin yang berbeda, dan validasi hanya bertaring jika pemeriksaan aksesibilitas yang gagal, tes penerimaan yang gagal, atau riset pengguna yang memberatkan benar-benar dapat memblokir pengiriman. Dalam konteks enterprise dan pemerintah ini sering wajib, kadang lewat verifikasi dan validasi independen oleh pihak yang terpisah dari pengembang, dan "kami tetap merilisnya" bukan jawaban yang diterima badan pengawas. Bawa beberapa rilis terakhir Anda: apakah sinyal kualiti pernah benar-benar menghentikan satu, atau gerbang selalu mengalah pada tanggal? Jika validasi tidak pernah memblokir rilis, ia hiasan, dan perbaikannya adalah menuliskan kriteria penerimaan ke dalam rencana kualiti di muka, menamai siapa yang memiliki keputusan jalan/tidak, dan memberi keputusan itu wewenang nyata yang independen dari tekanan pengiriman.

4. **Apakah kita benar-benar tahu biaya kualiti buruk kita, dan apakah kita dengan sengaja menggeser pengeluaran dari kegagalan ke pencegahan?** Biaya kualiti buruk (COPQ) adalah uang yang hilang pada pengerjaan ulang internal, insiden produksi, perbaikan darurat, beban dukungan, pengguna yang hilang, dan penalti, dan hampir selalu lebih besar daripada pengeluaran terlihat untuk tinjauan dan pengujian. Pada tim besar biaya kegagalan tersebar di kanal insiden, antrean dukungan, dan pengerjaan ulang yang tidak dicatat siapa pun sebagai pengerjaan ulang, sehingga tetap tak terlihat sampai seseorang menjumlahkannya. Ketegangannya adalah bahwa pencegahan memakan uang sekarang, dalam siklus anggaran, untuk menghindari biaya kegagalan yang jatuh kemudian dan jatuh pada anggaran orang lain, yang membuat pertukaran itu mudah ditunda selamanya. Bawa angka nyata: jumlah dan biaya insiden, jam pengerjaan ulang, kadar cacat yang lolos, dan pembagian pengeluaran saat ini di antara pencegahan, penilaian, dan kegagalan, lalu putuskan apakah campuran harus bergeser lebih awal. Untuk sistem enterprise dan pemerintah, di mana sebagian besar biaya seumur hidup jatuh setelah rilis pertama, letakkan COPQ di depan orang yang memegang anggaran, kerana angka yang dapat dilihat badan pengawas jauh lebih sulit ditukar daripada seruan samar pada "kualiti".

5. **Metrik kualiti kita yang mana yang diam-diam telah menjadi target, dan perilaku apa yang kini didorongnya?** Metrik yang menjadi target berhenti mengukur kenyataan: kejar peratusan cakupan dan Anda mendapat tes yang ditulis untuk menggerakkan angka, bukan tes yang menangkap cacat. Pada skala besar ini berbahaya, kerana dasbor utama yang dibagikan di puluhan tim menetapkan insentif bagi semuanya, dan metrik yang dapat dipermainkan menyebarkan permainan ke mana-mana sekaligus. Pertimbangan yang bersaing adalah bahwa Anda tetap membutuhkan pengukuran, jadi jawabannya jarang "buang metrik" melainkan "pasangkan dengan sinyal tandingan dan baca bersama bukti kualitatif dari tinjauan dan pengguna". Bawa kumpulan metrik Anda saat ini dan, untuk masing-masing, tanyakan apa yang dapat dilakukan seseorang di bawah tekanan untuk menggerakkannya tanpa memperbaiki kualiti, dan apakah Anda pernah melihatnya terjadi. Dalam konteks yang diatur dan menghadap warga, waspadai khususnya metrik kepatuhan yang tampak hijau sementara validasi yang mendasarinya (aksesibilitas, hasil pengguna nyata) tidak pernah benar-benar dijalankan, kerana auditor akhirnya akan menguji kenyataan di balik angka.

6. **Siapa yang memiliki kualiti di sini: tim yang menulis kode, atau kelompok terpisah di akhir, dan mana yang sebenarnya kita beri sumber daya?** Kepemilikan membentuk segalanya di hilir, kerana silo QA hilir membiarkan pengembang melepas tanggung jawab atas kode yang mereka tulis, sementara kualiti yang dimiliki tim membangun kepemilikan dengan biaya menuntut keterampilan dan disiplin di setiap tim. Pada tim besar ini bukan salah satu: pola berkelanjutan biasanya tim memiliki kualiti lewat tinjauan kode dan tes otomatis, didukung kelompok pusat kecil yang memelihara standar, menjalankan jaminan kualiti sebagai perbaikan proses, dan membimbing, alih-alih memeriksa kualiti masuk di akhir. Bawa peta jujur tentang di mana pekerjaan kualiti saat ini terjadi, siapa yang bertanggung jawab ketika cacat lolos, dan di mana anggaran serta personel sebenarnya berada versus di mana retorika mengatakan kualiti hidup. Untuk organisasi enterprise dan pemerintah, tambahkan persyaratan verifikasi dan validasi independen: sebagian rezim jaminan mewajibkan pihak terpisah, jadi putuskan dengan sengaja kontrol mana yang menjadi milik tim pengiriman dan mana yang harus tetap independen untuk memenuhi audit.

## Lensa sektor

**Startup.** Kecepatan lebih penting daripada upacara, jadi namai dua atau tiga karakteristik kualiti yang benar-benar melindungi produk Anda, biasanya keandalan dan kemudahan pemeliharaan, dan biarkan polesan menunggu. Miliki kualiti di seluruh tim dengan tinjauan kode dan rangkaian tes otomatis sederhana alih-alih mendirikan kelompok QA terpisah yang tidak sanggup Anda isi stafnya. Ketika kelas bug yang sama muncul dua kali, habiskan dua puluh menit untuk akar penyebab dan tambahkan satu pembantu bersama ditambah tes, agar pencegahan tetap murah dan kadar kegagalan perubahan Anda tetap rendah sambil bergerak cepat.

**Bisnis kecil.** Tanpa spesialis kualiti khusus dan dengan anggaran ketat, bersandarlah pada kualiti yang tertanam dalam perkakas dan platform yang Anda beli alih-alih proses yang harus Anda jalankan. Ketika memilih perisian, perlakukan bukti kualiti vendor sebagai bagian dari pembelian: postur keamanan, aksesibilitas, daya tanggap dukungan, dan seberapa sering rilis mereka rusak. Lacak segelintir sinyal murah dan jujur (insiden produksi, masalah yang dilaporkan pelanggan, waktu perbaikan) alih-alih program metrik rumit yang tidak ada orang untuk memeliharanya.

**Enterprise.** Pekerjaannya adalah konsistensi di banyak tim: adopsi model kualiti bersama seperti ISO/IEC 25010, pisahkan jaminan kualiti (proses) dari kendali kualiti (produk), dan jalankan tinjauan biaya kualiti yang menggeser pengeluaran ke pencegahan. Jaga kualiti dimiliki tim pengiriman, didukung kelompok pusat kecil yang memelihara standar dan dasbor untuk kadar cacat yang lolos, kadar kegagalan perubahan, dan tren kesihatan kode. Bakukan kosakata dan gerbang agar kelompok berhenti menciptakan ulang praktik kualiti, sambil memberi tim ruang untuk memenuhi standar itu dengan cara mereka sendiri.

**Pemerintah.** Pengadaan, transparansi, dan akuntabilitas publik menetapkan bingkai, jadi tuliskan persyaratan kualiti ke dalam kontrak dan wajibkan bukti kualiti yang terdokumentasi dan dapat dilacak alih-alih pernyataan. Harapkan verifikasi dan validasi independen oleh pihak yang terpisah dari pengembang, kesesuaian aksesibilitas yang wajib, dan catatan cacat dengan keparahan dan akar penyebab disimpan sebagai bagian dari jejak audit. Laporkan angka biaya kualiti buruk (pengerjaan ulang, banding, kegagalan layanan) kepada badan pengawas, dan beri validasi wewenang nyata untuk memblokir rilis yang akan mengecewakan warga yang bergantung padanya.

## Contoh

**Startup.** Sebuah startup lima orang memutuskan bahwa untuk produk awalnya, keandalan dan kemudahan pemeliharaan adalah karakteristik kualiti yang penting, dan membiarkan polesan sempurna-piksel menunggu. Kualiti dimiliki seluruh tim: tinjauan kode dan rangkaian tes otomatis sederhana adalah kendalinya, dan tidak ada kelompok QA terpisah untuk melempar cacat. Ketika kelas bug yang sama muncul dua kali, mereka menghabiskan dua puluh menit pada pandangan akar penyebab cepat dan menambahkan satu pembantu bersama ditambah tes, sehingga tidak berulang alih-alih diperbaiki ulang dengan tangan setiap kali. Kebiasaan kecil pencegahan itu menjaga kadar kegagalan perubahan mereka tetap rendah selagi mereka masih bergerak cepat.

**Enterprise.** Sebuah firma jasa keuangan besar mengadopsi ISO/IEC 25010 sebagai kosakata kualitinya dan, untuk setiap produk, mencatat kadar target untuk keandalan, keamanan, dan kemudahan pemeliharaan. Tim memiliki kualiti: tinjauan kode dan tes otomatis adalah kendali di pipeline, sementara kelompok pusat kecil menjalankan QA dengan memelihara standar dan membimbing. Dasbor kualiti melacak kadar cacat yang lolos, kadar kegagalan perubahan, dan tren kesihatan kode. Cacat diklasifikasi dan dicari akar penyebabnya, dan penyebab berulang menggerakkan pembaruan pada pustaka bersama dan daftar periksa. Pimpinan meninjau data biaya kualiti tiap kuartal dan telah menggeser pengeluaran ke pencegahan, memangkas baik insiden produksi maupun biaya memperbaikinya.

**Pemerintah.** Sebuah lembaga nasional yang menyampaikan platform tunjangan yang menghadap warga bekerja di bawah rezim jaminan yang mensyaratkan bukti kualiti terdokumentasi. Ia menjalankan proses manajemen kualiti formal dengan rencana kualiti per rilis, ditambah verifikasi dan validasi independen oleh tim yang terpisah dari pengembang. Verifikasi memeriksa setiap produk kerja terhadap persyaratan yang dilacak ke kebijakan. Validasi mencakup pengujian kesesuaian aksesibilitas dan riset pengguna dengan warga nyata, dan keduanya dapat memblokir rilis. Cacat dilacak dengan keparahan dan akar penyebab sebagai bagian dari jejak audit, dan angka biaya kualiti buruk (pengerjaan ulang, banding, dan kegagalan layanan) diserahkan kepada badan pengawas untuk membenarkan investasi berkelanjutan dalam pencegahan.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil kualiti adalah total biaya kepemilikan yang lebih rendah dan kecepatan pengiriman yang stabil. Biaya kualiti punya dua sisi. Pengeluaran yang baik, pencegahan dan penilaian, terlihat dan dapat dikendalikan: desain, standar, tinjauan, pengujian, dan perkakas. Biaya kualiti buruk (COPQ) lebih besar tetapi sering tersembunyi: pengerjaan ulang internal, insiden produksi, perbaikan darurat, dukungan pelanggan, pengguna yang hilang, penalti regulasi, dan kerusakan reputasi. Studi sejak "Quality Is Free" Crosby secara konsisten menemukan bahwa total biaya kualiti buruk melampaui biaya mencegahnya, dan bahwa cacat menjadi jauh lebih mahal semakin lambat Anda menangkapnya: isu yang ditemukan dalam desain memakan sebagian kecil dari isu yang sama yang ditemukan di produksi.

Bagi pimpinan, argumennya bukan "belanjakan lebih banyak untuk kualiti." Melainkan "belanjakan lebih awal untuk membelanjakan lebih sedikit secara keseluruhan." Kuantifikasi COPQ dari data Anda sendiri (jumlah dan biaya insiden, jam pengerjaan ulang, kadar cacat yang lolos) dan tunjukkan bagaimana pencegahan serta penilaian awal menurunkannya. Hubungkan kualiti dengan hasil bisnis: keandalan mempertahankan pelanggan, kemudahan pemeliharaan menjaga perubahan mendatang tetap murah, dan keamanan serta aksesibilitas menjauhkan Anda dari masalah hukum. Dalam sistem enterprise dan pemerintah berumur panjang, di mana sebagian besar biaya jatuh setelah rilis pertama, dimensi kemudahan pemeliharaan dan keandalan dari kualiti mendominasi biaya seumur hidup. Itu menjadikan investasi kualiti awal salah satu keputusan berdaya ungkit tertinggi yang dapat Anda buat.

## Anti-pola dan jebakan

- **Kualiti sebagai gerbang akhir:** memeriksa kualiti masuk di akhir alih-alih membangunnya masuk, sehingga cacat ditemukan ketika paling mahal.
- **Mencampuradukkan pengujian dengan kualiti:** mengira tes yang lolos berarti kualiti tinggi, mengabaikan kemudahan pemeliharaan, kegunaan, dan kesesuaian dengan tujuan.
- **QA sebagai silo terpisah:** tim hilir yang "memiliki kualiti," membiarkan pengembang melepas tanggung jawab atas kode yang mereka tulis.
- **Teater metrik:** mengejar peratusan cakupan atau jumlah cacat sebagai target, yang mengundang permainan dan menyembunyikan kualiti nyata.
- **Verifikasi tanpa validasi:** membangun spesifikasi dengan benar tanpa pernah memeriksa bahwa spesifikasi memenuhi kebutuhan nyata.
- **Tanpa analisis akar penyebab:** memperbaiki cacat satu per satu tanpa menangani penyebab sistemik, sehingga kelas yang sama berulang.
- **Mengabaikan biaya kualiti buruk:** memperlakukan kualiti sebagai biaya murni kerana biaya kegagalan tersembunyi dan tak terukur.

## Model kematangan

**Kadar 1 (Memulai).** Kualiti tidak terdefinisi dan ad hoc. Ia bergantung pada ketekunan individu, diperiksa terutama lewat pengujian manual di akhir, dan cacat ditangani secara reaktif saat muncul. Tidak ada model bersama, tidak ada metrik, dan tidak ada garis antara jaminan dan kendali.

**Kadar 2 (Mengembangkan).** Praktik dasar muncul: tinjauan kode, tes otomatis, dan pelacak cacat. Sebagian data kualiti dikumpulkan, tetapi tidak merata, dan setiap tim melakukannya dengan caranya sendiri. Kualiti masih sebagian besar dipandang sebagai pengujian, pencegahan minimal, verifikasi terjadi, dan validasi informal.

**Kadar 3 (Membakukan).** Organisasi mengadopsi model kualiti bersama (seperti ISO/IEC 25010), memisahkan QA dari QC, dan menjalankan proses manajemen kualiti dengan rencana kualiti dan kriteria penerimaan, terdokumentasi dan diterapkan konsisten di semua tim. Verifikasi dan validasi berbeda dan disengaja, dan cacat diklasifikasi serta dicari akar penyebabnya menurut skema yang disepakati.

**Kadar 4 (Mengelola).** Kualiti diukur dan dikendalikan terhadap garis dasar. Sekumpulan kecil metrik bermakna dilacak dari waktu ke waktu (kepadatan cacat, kadar cacat yang lolos, waktu rata-rata mendeteksi dan memperbaiki, kadar kegagalan perubahan, dan sinyal kesihatan kode seperti kompleksitas dan duplikasi), dan biaya kualiti dikuantifikasi di seluruh pencegahan, penilaian, dan kegagalan. Gerbang penerimaan dan kualiti ditegakkan berdasarkan bukti alih-alih opini, tren ditinjau pada irama tetap, dan validasi benar-benar dapat memblokir rilis.

**Kadar 5 (Mengorkestrasi).** Kualiti adalah disiplin yang terus diperbaiki dan dimiliki secara budaya yang terintegrasi dengan perencanaan bisnis dan risiko. Pencegahan adalah penekanannya, data biaya kualiti memandu ke mana investasi pergi, dan temuan akar penyebab secara sistematis mencegah kekambuhan. Tim memiliki kualiti dari ujung ke ujung, metrik memberi makan perbaikan berkelanjutan, dan organisasi menyesuaikan praktik kualitinya seiring bergesernya produk, risiko, dan regulasi. Ini selaras dengan kadar lebih tinggi model kematangan di bab 10.8.

## Gagasan untuk didiskusikan

- Karakteristik kualiti ISO/IEC 25010 mana yang paling penting untuk sistem Anda, dan apa arti "cukup baik" untuk masing-masing?
- Di mana organisasi Anda berada pada campuran pengeluaran pencegahan-penilaian-kegagalan, dan haruskah bergeser?
- Apakah Anda membedakan verifikasi dari validasi dalam praktik, atau menggabungkan keduanya menjadi "pengujian"?
- Apakah kualiti dimiliki tim yang membangun perisian, atau didelegasikan ke kelompok terpisah, dan apa yang akan berubah jika Anda memindahkannya?
- Berapa biaya kualiti buruk Anda yang sebenarnya, dan dapatkah Anda mengukurnya cukup baik untuk membuat kasus bisnis?
- Metrik kualiti Anda yang mana yang merupakan sinyal sejati, dan mana yang telah menjadi target yang dapat dipermainkan?

## Poin-poin utama

- Kualiti lebih luas daripada pengujian: ia kesesuaian dengan tujuan ditambah kepatuhan, di seluruh karakteristik seperti keandalan, keamanan, dan kemudahan pemeliharaan.
- Gunakan model kualiti bersama (ISO/IEC 25010) agar atribut kualiti eksplisit dan selaras dengan arsitektur (bab 3.1).
- Pisahkan jaminan kualiti (cegah, proses) dari kendali kualiti (deteksi, produk), dan condong ke pencegahan.
- Praktikkan verifikasi (dibangun dengan benar) dan validasi (dibangun hal yang benar) sebagai disiplin yang berbeda.
- Ukur kualiti dengan beberapa metrik bermakna, dan karakterisasi cacat menurut keparahan dan akar penyebab untuk mencegah kekambuhan.
- Kelola biaya kualiti: pencegahan dan penilaian awal jauh lebih murah daripada kegagalan, terutama pada sistem berumur panjang.
- Bangun budaya kualiti tanpa menyalahkan di mana tim memiliki kualiti, didukung tinjauan kode (bab 2.5) dan strategi pengujian (bab 2.4).

## Referensi dan bacaan lanjutan

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, area pengetahuan Software Quality.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- Seri ISO/IEC 25000 (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones dan Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (konteks proses jaminan kualiti dan V&V).
