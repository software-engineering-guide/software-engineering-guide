# 6.1 Strategi dan kesiapan AI

## Tinjauan dan motivasi

[Kecerdasan buatan](https://en.wikipedia.org/wiki/Artificial_intelligence) telah berubah dari kebaruan riset menjadi kemampuan inti yang kini diharapkan dari organisasi besar untuk dikerahkan secara bertanggung jawab dan pada skala besar. Bagi enterprise dan lembaga pemerintah, pertanyaan sebenarnya bukan lagi apakah AI dapat melakukan sesuatu yang mengesankan dalam demo. Melainkan apakah investasi tertentu menyelesaikan masalah nyata lebih baik daripada alternatifnya, dapat dioperasikan dengan aman selama bertahun-tahun, dan dapat selamat dari audit, pengadaan, dan pengawasan publik. Strategi AI adalah disiplin memutuskan di mana menerapkan AI, di mana menghindarinya, dan fondasi apa yang Anda butuhkan sebelum model pertama mencapai produksi.

Bagi tim besar, skala dan inersia menaikkan taruhan. Inisiatif yang dibingkai buruk dapat membakar anggaran, mengalihkan insinyur berbakat, dan mengikis kepercayaan regulator dan warga ketika gagal di depan umum. Yang dipilih baik dapat mengotomatisasi pekerjaan membosankan, memunculkan wawasan dari data yang tak pernah dapat Anda jangkau sebelumnya, dan membebaskan orang terampil untuk kerja bernilai lebih tinggi. Bedanya jarang pada model itu sendiri. Ia bermuara pada seberapa baik Anda membingkai masalah, seberapa siap data dan talenta Anda, dan seberapa jujur kasus bisnis Anda.

Konteks pemerintah dan teregulasi menambah kendala. Badan publik harus membenarkan pengeluaran, menjamin transparansi, menghindari diskriminasi melanggar hukum, dan tetap bertanggung jawab kepada pejabat terpilih dan publik. Aturan pengadaan dapat melarang lock-in sumber tunggal, menuntut keterjelasan, dan mewajibkan vendor mengekspos perilaku model. Di sini, perlakukan kepatuhan, kemampuan diaudit, dan opsi keluar sebagai persyaratan kelas satu, bukan renungan belakangan.

## Prinsip utama

- Mulailah dari masalah yang layak diselesaikan, bukan dari teknologi yang mencari penggunaan.
- Pilih pendekatan paling sederhana yang memenuhi kebutuhan; AI adalah satu opsi di antara banyak, dan sering bukan yang terbaik.
- Perlakukan kesiapan data, talenta, dan kematangan platform sebagai prasyarat, bukan jalur kerja paralel untuk dibereskan belakangan.
- Buat keputusan bangun-versus-beli secara eksplisit dan tinjau ulang seiring pasar dan kemampuan Anda berubah.
- Kuantifikasi total biaya kepemilikan, termasuk operasi, pemantauan, dan penggantian akhirnya, bukan hanya lisensi atau percontohan.
- Rancang untuk keluar sejak hari pertama: hindari arsitektur yang membuat berganti vendor atau model sangat mahal.
- Dalam pengaturan teregulasi dan publik, perlakukan transparansi, kepatuhan pengadaan, dan akuntabilitas sebagai kendala desain.
- Ukur biaya *tidak* bertindak di samping biaya bertindak.

## Rekomendasi

### Bingkai masalah sebelum memilih teknologi

Tulis pernyataan masalah satu halaman. Namai keputusan atau tugas yang ingin Anda perbaiki, garis dasar saat ini, hasil terukur yang Anda inginkan, dan apa yang terjadi ketika sistem salah. Lalu tanyakan apakah masalah itu bahkan cocok untuk AI. Adakah data relevan yang cukup? Apakah tugasnya berbasis pola alih-alih berbasis aturan? Dapatkah Anda menoleransi jawaban probabilistik? Dapatkah manusia memeriksa keluarannya? Banyak masalah lebih baik diselesaikan dengan perangkat lunak deterministik, desain proses yang lebih baik, atau sekadar kebersihan data yang lebih baik. Tuliskan secara eksplisit di mana AI *bukan* kecocokan yang baik: misalnya keputusan yang harus dapat dijelaskan sempurna menurut hukum, atau di mana biaya kesalahan langka katastrofik dan mustahil ditangkap.

### Gunakan pohon keputusan bangun-versus-beli-versus-fine-tune-versus-prompt

Bergeraklah dari yang termurah dan tercepat ke yang termahal dan paling terkendali:

1. **Beri prompt pada model ter-hosting yang ada.** Jika model serba guna (seperti Claude dari Anthropic, atau tawaran sebanding dari penyedia lain) menyelesaikan masalah dengan prompting dan pengambilan yang cermat, lakukan itu dulu. Biaya terendah, iterasi tercepat, tanpa infrastruktur pelatihan.
2. **Perkaya dengan pengambilan atau perkakas.** Jika celahnya pengetahuan atau tindakan, tambahkan [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), yang mengambil dokumen relevan saat kueri dan menyuplainya ke model sebagai konteks, dan pemakaian perkakas sebelum menyentuh bobot model.
3. **Fine-tune atau adaptasi.** Jika prompting tidak dapat mencapai akurasi, nada, atau format yang dibutuhkan secara konsisten, [fine-tune](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) model lebih kecil pada data Anda: yaitu melatih lebih lanjut model terlatih pada contoh Anda untuk mengkhususkannya. Ini membeli kendali dengan biaya pipeline [MLOps](https://en.wikipedia.org/wiki/MLOps) (operasi pembelajaran mesin).
4. **Beli produk khusus.** Untuk ranah terdefinisi baik (pemrosesan dokumen, penilaian penipuan), produk vendor matang dapat mengalahkan apa pun yang Anda bangun.
5. **Bangun dari nol.** Sisihkan pelatihan [model fondasi](https://en.wikipedia.org/wiki/Foundation_model) (model besar yang dilatih pada data luas dan dapat diadaptasi ke banyak tugas) untuk organisasi dengan data unik, talenta mendalam, dan alasan strategis. Bagi hampir semua enterprise dan lembaga, ini pilihan yang salah.

### Tetapkan prasyarat data, talenta, dan platform

Audit data Anda untuk ketersediaan, kualitas, pelabelan, silsilah, dan dasar hukum penggunaan. Pastikan Anda benar-benar berhak memakainya untuk AI, termasuk data pribadi atau pihak ketiga apa pun. Nilai talenta dengan jujur: Anda butuh ilmuwan data, dan juga insinyur ML, insinyur data, manajer produk yang memahami sistem probabilistik, dan peninjau yang dapat mengevaluasi keluaran. Sebelum Anda berskala, dirikan garis dasar platform: pelacakan eksperimen, registri model (sistem pencatat versi model terlatih dan status persetujuannya), pemantauan, dan penyajian aman, agar setiap kasus penggunaan baru tidak menciptakan ulang operasi.

### Tangani konteks teregulasi dan pemerintah dengan sengaja

Libatkan tim pengadaan, hukum, dan risiko sejak dini. Wajibkan vendor mengungkap asal-usul model, praktik data pelatihan, hasil evaluasi, dan keterbatasan yang diketahui. Pilih kontrak yang memberi portabilitas data dan prompt Anda, dan hindari format proprietari yang menjebak Anda. Di mana sesuai, terbitkan tujuan dan pengamanan sistem AI yang menghadap publik, dan beri orang saluran untuk menggugat keputusan otomatis. Selaraskan dengan kerangka yang diakui (lihat bab 6.5) agar audit menemukan proses terdokumentasi dan dapat dipertahankan.

### Hitung total biaya kepemilikan dan jaga dari lock-in

Modelkan biaya siklus hidup penuh: inferensi atau lisensi, pipeline data, tinjauan manusia, pemantauan, pelatihan ulang, respons insiden, dan penonaktifan. Bandingkan dengan biaya status quo dan alternatifnya. Kurangi lock-in dengan menaruh model di balik antarmuka internal, menjaga prompt dan dataset evaluasi tetap portabel, dan sesekali menguji penyedia kedua.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan | Terbaik ketika |
|---|---|---|---|
| Prompt model ter-hosting | Cepat, murah, tanpa infra, mudah berganti | Kendali lebih sedikit, biaya per panggilan, pertanyaan berbagi data | Prototipe, tugas luas, persyaratan tak pasti |
| Augmentasi pengambilan | Membumikan jawaban pada data Anda, dapat diperbarui | Kualitas pengambilan sulit, menambah infra | Tugas padat pengetahuan |
| Fine-tune model lebih kecil | Kendali, biaya per panggilan lebih rendah pada skala, opsi on-prem | Butuh MLOps, data, dan pemeliharaan | Tugas stabil, bervolume tinggi, khusus |
| Beli produk | Teruji, didukung, cepat bernilai | Biaya lisensi, lock-in, kecocokan terbatas | Masalah komoditas terdefinisi baik |
| Bangun model fondasi | Kendali dan diferensiasi maksimum | Biaya sangat besar, talenta langka, risiko tinggi | Nyaris tidak pernah, di luar lab perbatasan |

Trade-off dominannya adalah kendali versus biaya dan kecepatan. Prompting memberi kecepatan dan fleksibilitas paling besar tetapi kendali paling sedikit; membangun memberi kendali paling besar tetapi menuntut sumber daya yang sedikit organisasi seharusnya keluarkan. Kebanyakan tim besar harus hidup di tengah: prompt dan ambil dulu, fine-tune secara selektif, dan beli untuk kebutuhan komoditas. Lock-in menukar kenyamanan jangka pendek dengan risiko jangka panjang, dan itu penting terutama di pemerintah, di mana kewajiban keluar multitahun lazim.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Di mana masing-masing tiga kasus penggunaan kandidat teratas kita berada pada tangga prompt-lalu-ambil-lalu-fine-tune-lalu-beli-lalu-bangun, dan bukti apa yang akan menggesernya satu anak tangga?** Ini penting karena sebagian besar pemborosan pengeluaran AI datang dari memulai satu anak tangga terlalu tinggi: melatih model ketika prompting cermat akan berhasil. Bagi tim besar, menyepakati tangga sebagai bawaan bersama mencegah setiap kelompok menciptakan ulang pipeline mahal. Bawa pernyataan masalah satu halaman untuk setiap kandidat, garis dasar saat ini, dan pembacaan jujur apakah celahnya pengetahuan (pengambilan), konsistensi (fine-tuning), atau komoditas yang sudah terselesaikan (beli). Dalam pengaturan enterprise dan pemerintah, tambahkan biaya pengadaan dan audit setiap anak tangga, karena model yang di-fine-tune menyeret beban MLOps yang tidak dibawa panggilan ter-hosting. Jawabannya harus memungkinkan Anda menghentikan atau menurunkan setidaknya satu proyek berlebih cakupan di ruangan.

2. **Apa rencana keluar konkret kita untuk vendor atau model yang paling kita andalkan, dan sudahkah kita benar-benar mengujinya?** Lock-in murah diterima dan mahal diurai, dan di pemerintah Anda mungkin memikul kewajiban keluar multitahun yang tak dapat Anda penuhi jika tak pernah dilatih. Bawa daftar fitur proprietari yang Anda andalkan, apakah prompt dan dataset evaluasi portabel, dan bagaimana model duduk di balik antarmuka internal (atau tidak). Sinyal yang diawasi adalah apakah ada yang pernah menjalankan rangkaian evaluasi Anda terhadap penyedia kedua; jika tidak, rencana keluar Anda harapan, bukan rencana. Jika jawaban jujurnya berpindah akan memakan berbulan-bulan dan menulis ulang kode inti, perlakukan itu sebagai cacat desain untuk diperbaiki sekarang, bukan jembatan untuk dilintasi kelak.

3. **Apa yang dikatakan kartu skor kesiapan yang jujur tentang hak data kita, dan kasus penggunaan mana yang didiskualifikasinya hari ini?** Melewatkan kesiapan data adalah kegagalan yang menenggelamkan percontohan secara diam-diam: model berfungsi, tetapi Anda tak pernah punya dasar hukum memakai datanya, atau tak berlabel dan tanpa silsilah. Bagi organisasi besar, data pribadi dan pihak ketiga menimbulkan batas persetujuan dan kontraktual yang bervariasi menurut yurisdiksi dan dataset. Bawa audit ketersediaan, kualitas, pelabelan, silsilah, dan dasar hukum untuk setiap kandidat, dan bersedialah menandai sebagian kasus penggunaan terblokir sampai fondasi data ada. Dalam pengaturan teregulasi dan publik, dasar hukum yang tak dapat dipakai bukan penundaan, melainkan penghentian keras, dan mendanai kerja kesiapan harus menjadi baris eksplisit dalam rencana alih-alih renungan belakangan.

4. **Bagaimana kita akan tahu kasus penggunaan AI yang hidup benar-benar berfungsi, dan bukti apa yang akan membuat kita menghentikannya?** Kebanyakan portofolio AI mengumpulkan zombi: percontohan yang dikirim, mengesankan seseorang, dan kini berjalan selamanya tanpa ada yang memeriksa apakah mereka masih layak biayanya. Sepakati garis dasar dan metrik keberhasilan sebelum peluncuran, lalu tetapkan ambang hentikan eksplisit, agar keputusan berhenti dibuat di muka alih-alih dibela pada saat itu. Bawa metrik saat ini, biaya pengawasan manusia per hasil, dan drift yang telah Anda lihat sejak peluncuran. Untuk portofolio enterprise dan pemerintah, namai siapa yang meninjau setiap sistem pada irama tetap dan siapa yang memegang wewenang memensiunkannya; kasus penggunaan yang tak dipertanggungjawabkan siapa pun untuk ditinjau adalah yang tak akan pernah dimatikan siapa pun.

5. **Di mana manusia tetap dalam lingkaran, berapa biaya pengawasan itu, dan sudahkah kita benar-benar menganggarkannya?** Kasus penggunaan AI yang tampak termurah adalah yang diam-diam mengasumsikan otomasi penuh, lalu membocorkan biaya lewat tinjauan, koreksi, dan eskalasi yang dipaksa kenyataan kembali masuk. Putuskan dengan sengaja keputusan mana yang harus dikonfirmasi orang, mana yang boleh diambil model sendiri, dan mana yang tidak boleh pernah diambilnya, lalu hargai waktu manusia yang disiratkannya. Bawa volume kasus berkeyakinan rendah, biaya jawaban salah, dan jalur eskalasi saat ini. Dalam pengaturan teregulasi dan publik, kaitkan setiap keputusan otomatis dengan pejabat yang bertanggung jawab dan jalur banding, karena pengawasan yang tak dapat Anda gambarkan adalah pengawasan yang tidak Anda miliki.

6. **Apakah kita punya talenta dan platform untuk menjalankan apa yang kita usulkan, atau kita diam-diam mengasumsikan kapasitas yang tidak kita miliki?** Rencana AI ambisius gagal lebih sedikit pada model daripada pada fondasi tak glamor: tak ada yang memelihara pipeline, tak ada yang dapat mengevaluasi keluaran, tak ada platform untuk men-deploy. Cocokkan setiap kasus penggunaan kandidat dengan keterampilan dan infrastruktur yang benar-benar dibutuhkannya, dan jujurlah di mana celahnya adalah perekrutan, mitra, atau alasan untuk tidak membangun. Bawa inventaris siapa yang dapat memiliki setiap sistem di produksi, platform apa yang akan dijalankannya, dan kemampuan mana yang harus Anda beli. Untuk organisasi besar atau publik, tambahkan lead time pengadaan dan perekrutan, karena rencana yang bergantung pada talenta yang tak dapat Anda rekrut dalam jendela yang relevan adalah rencana untuk kurang memberikan.

## Lensa sektor

**Startup.** Kecepatan dan kelangsungan hidup mendominasi. Pilih satu kasus penggunaan sempit yang menyentuh nilai inti Anda, kirim di model ter-hosting di balik antarmuka tipis, dan batasi pengeluaran dengan keras. Hindari membangun infrastruktur atau melatih model: sumber daya Anda yang paling langka adalah perhatian rekayasa, dan pipeline fine-tune yang tak dapat Anda pelihara adalah liabilitas, bukan parit. Jaga berpindah tetap murah agar Anda dapat mengikuti pasar yang bergerak cepat.

**Bisnis kecil.** Anda kemungkinan tidak punya ilmuwan data dan anggaran ketat, jadi perlakukan AI sebagai sesuatu yang Anda beli tertanam dalam perkakas yang sudah Anda pakai, bukan program yang Anda isi stafnya. Bingkai kesiapan sebagai pertanyaan kebersihan data dan privasi alih-alih proyek pembelajaran mesin: ketahui data pelanggan apa yang Anda pegang, apa yang boleh Anda lakukan dengannya, dan di mana jawaban otomatis yang salah akan membuat Anda kehilangan pelanggan. Pilih vendor yang membuat AI opsional, transparan, dan mudah dimatikan.

**Enterprise.** Masalahnya tata kelola portofolio lintas banyak tim: tangga bangun-versus-beli bersama, penilaian kesiapan yang konsisten, serta analisis lock-in dan total biaya agar kelompok berhenti menciptakan ulang pipeline mahal. Anggarkan beban MLOps dan pengawasan manusia secara eksplisit, bakukan lapisan antarmuka agar penyedia tetap dapat ditukar, dan kelola kasus penggunaan AI sebagai portofolio dengan metrik jelas dan kriteria hentikan alih-alih sebaran percontohan.

**Pemerintah.** Transparansi, aturan pengadaan, dan akuntabilitas membentuk setiap pilihan. Pilih sistem yang mengutip sumber resmi alih-alih menghasilkan kebijakan, jaga manusia tetap bertanggung jawab atas keputusan berdampak, dan tuntut portabilitas data dan pengungkapan keterbatasan model dalam kontrak. Terbitkan deskripsi bahasa sederhana dan jalur banding, hormati kewajiban keluar multitahun yang Anda tandatangani, dan jaga AI di luar keputusan penilaian akhir yang harus berada pada pejabat yang bertanggung jawab.

## Contoh

**Startup.** Startup penjadwalan lima orang ingin menambah fitur bahasa alami "pesankan saya rapat" tanpa menarik kedua insinyurnya dari produk inti. Ia memilih masalah terkecil yang penting, mengurai permintaan menjadi usulan waktu, dan mengirimnya dengan model ter-hosting di balik API internal tipis agar dapat berpindah penyedia kelak. Tim menetapkan batas pengeluaran bulanan keras, melacak apakah pengguna menerima waktu yang disarankan, dan sepakat meninjau ulang model yang di-fine-tune hanya jika volume pernah membenarkan kerja tambahan.

**Enterprise.** Sebuah perusahaan asuransi multinasional ingin mempercepat triase klaim. Alih-alih melatih model pesanan, ia membingkai masalah secara sempit (rutekan dan ringkas klaim masuk), membuat prototipe dengan model ter-hosting plus pengambilan atas dokumen polisnya, dan mengukur terhadap waktu penanganan dan akurasi manusia. Baru setelah membuktikan nilai ia me-fine-tune model lebih kecil untuk jenis klaim bervolume tertinggi guna memotong biaya per panggilan. Ia menjaga model di balik API internal agar dapat berpindah penyedia, dan memodelkan TCO tiga tahun yang mencakup tinjauan manusia atas kasus berkeyakinan rendah.

**Pemerintah.** Sebuah otoritas pajak nasional mempertimbangkan asisten AI untuk membantu staf menjawab pertanyaan warga. Karena jawaban itu menyentuh kewajiban hukum, lembaga mendesakkan transparansi: sistem hanya dapat memunculkan panduan resmi dengan kutipan, tidak pernah menciptakan kebijakan, dan manusia meninjau setiap saran otomatis sebelum keluar. Pengadaan mewajibkan vendor mengungkap keterbatasan model dan memberi portabilitas data, dan lembaga menerbitkan deskripsi bahasa sederhana sistem dan jalur banding. Ia menjaga AI sepenuhnya di luar keputusan penilaian akhir, menyisihkannya untuk pejabat yang bertanggung jawab.

## Kasus bisnis: motivasi, ROI, dan TCO

Strategi AI ada untuk membantu Anda menghindari dua kegagalan cermin: berinvestasi berlebihan pada AI yang tak pernah membayar, dan berinvestasi kurang sementara pesaing atau lembaga sebaya melaju. ROI datang dari tenaga kerja yang dihemat, waktu siklus yang dikurangi, tingkat galat yang diturunkan, dan kemampuan baru yang dimungkinkan. Ukur ini terhadap garis dasar sejati, dan diskon untuk biaya nyata pengawasan manusia, yang jarang lenyap.

TCO harus mencakup butir baris tak glamor: pipeline data, pemantauan, pelatihan ulang seiring dunia menyimpang, tinjauan keamanan, dan penonaktifan akhirnya. Percontohan yang tampak murah dapat menjadi mahal begitu berjalan pada skala besar selama bertahun-tahun. Sajikan juga biaya *tidak* mengadopsi: layanan lebih lambat, biaya manual lebih tinggi, dan penyimpangan strategis. Ajukan kasus kepada pimpinan dengan pandangan portofolio: beberapa taruhan berkeyakinan tinggi, metrik keberhasilan jelas, kriteria hentikan untuk kegagalan, dan penilaian kesiapan yang menunjukkan fondasi data dan talenta ada. Minta pimpinan mendanai kesiapan secara eksplisit; lewatkan, dan Anda menjamin pengerjaan ulang mahal.

## Anti-pola dan jebakan

- **Solusi yang mencari masalah.** Membeli AI karena rekan melakukannya, lalu memburu kasus penggunaan.
- **Melewatkan kesiapan data.** Meluncurkan model pada data yang tak tersedia, tak berlabel, atau tak dapat dipakai secara hukum.
- **Keputusan digerakkan demo.** Berkomitmen berdasarkan demo mengilap tanpa evaluasi kualitas-produksi.
- **Mengabaikan lingkaran manusia.** Mengasumsikan otomasi penuh dan kurang menganggarkan tinjauan, di mana sebagian besar biaya bersembunyi.
- **Lock-in senyap.** Membangun dalam di atas fitur proprietari satu vendor tanpa rencana keluar.
- **Meremehkan operasi.** Memperlakukan deployment sebagai garis finis alih-alih awal kewajiban pemeliharaan.
- **Kepatuhan sebagai renungan belakangan.** Memasang transparansi dan kemampuan diaudit setelah desain, dengan biaya berlipat.

## Model kematangan

1. **Memulai.** Eksperimen ad hoc, tanpa strategi bersama, keputusan digerakkan sensasi dan antusiasme individu.
2. **Mengembangkan.** Pembingkaian masalah ada untuk sebagian proyek; garis dasar platform pertama muncul; bangun-versus-beli dibahas namun tidak konsisten.
3. **Membakukan.** Portofolio kasus penggunaan AI dengan metrik jelas, pohon keputusan terdokumentasi, penilaian kesiapan, serta analisis lock-in dan TCO, diterapkan konsisten lintas tim.
4. **Mengelola.** Portofolio diukur: kesiapan, ROI, TCO, dan biaya pengawasan manusia dilacak terhadap garis dasar; kriteria hentikan ditegakkan atas bukti; dampak pengiriman dan kualitas menggerakkan setiap keputusan go atau no-go.
5. **Mengorkestrasi.** Strategi AI terintegrasi dengan perencanaan bisnis dan risiko; kesiapan dijaga terus-menerus; organisasi rutin memensiunkan, mengganti, dan menentukan ulang cakupan sistem AI berdasarkan bukti, menyeimbangkan ulang portofolio seiring pasar dan gambaran risiko bergeser.

## Gagasan untuk didiskusikan

- Bagaimana Anda memutuskan kapan masalah benar-benar tidak cocok untuk AI, dan siapa yang berwenang mengatakan tidak?
- Ambang kesiapan apa yang harus menggerbangi proyek dari percontohan ke produksi?
- Seberapa banyak lock-in yang dapat diterima sebagai ganti waktu-ke-nilai lebih cepat?
- Di pemerintah, bagaimana kewajiban transparansi harus membentuk pilihan bangun-versus-beli?
- Bagaimana Anda menjaga estimasi TCO tetap jujur ketika vendor dan penggemar punya insentif meremehkannya?
- Siapa yang memiliki portofolio AI, dan bagaimana keputusan menghentikan dibuat?

## Poin-poin utama

- Strategi dimulai dengan masalah nyata dan garis dasar jujur, bukan dengan teknologi.
- Pilih opsi paling sederhana: prompt, lalu ambil, lalu fine-tune, lalu beli, dan jarang bangun dari nol.
- Kesiapan data, talenta, dan platform adalah prasyarat; mendanainya bagian dari rencana.
- Konteks teregulasi dan pemerintah membutuhkan transparansi, kepatuhan pengadaan, dan opsi keluar secara desain.
- Modelkan TCO penuh dan biaya ketidakbertindakan, dan jaga dari lock-in vendor sejak keputusan arsitektur pertama.

## Referensi dan bacaan lanjutan

- Ajay Agrawal, Joshua Gans, dan Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
