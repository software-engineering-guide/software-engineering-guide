# 6.3 AI generatif dan aplikasi LLM

## Tinjauan dan motivasi

[AI generatif](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), dan khususnya [model bahasa besar](https://en.wikipedia.org/wiki/Large_language_model) (LLM), dapat menghasilkan teks yang fasih, kode, ringkasan, dan data terstruktur dari instruksi bahasa alami. Itu menjadikannya blok bangunan yang kuat untuk asisten, pencarian, pemrosesan dokumen, dan otomasi. Namun kekuatan itu datang dengan profil risiko yang khas. LLM bersifat probabilistik. Mereka dapat menghasilkan kebohongan yang meyakinkan ([halusinasi](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Mereka peka terhadap cara Anda memberi prompt. Dan mereka membuka permukaan serangan baru seperti [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection) (instruksi berbahaya yang diselundupkan ke masukan untuk membajak perilaku model). Jadi membangun aplikasi LLM yang dapat diandalkan lebih sedikit tentang model dan lebih banyak tentang rekayasa di sekelilingnya: bagaimana Anda menyuplai konteks, membumikan jawaban pada pengetahuan tepercaya, membatasi keluaran, dan mengevaluasi kualitas.

Bagi tim besar, aplikasi LLM menuntut pola baru yang berbeda dari perangkat lunak tradisional maupun pembelajaran mesin klasik. Sering tidak ada langkah pelatihan. Sebagai gantinya, perilaku dibentuk oleh prompt, konteks yang diambil, definisi perkakas, dan guardrail (pemeriksaan runtime yang membatasi masukan dan keluaran model). Itu menggeser upaya rekayasa ke manajemen konteks, kualitas pengambilan, orkestrasi, dan evaluasi. Enterprise yang mengadopsi LLM pada skala besar butuh pola bersama agar setiap tim tidak menemukan ulang mode kegagalan yang sama dengan cara sulit.

Organisasi pemerintah dan teregulasi menghadapi tuntutan tambahan. LLM yang mengarang kutipan kebijakan atau membocorkan data sensitif bukan sekadar bug; ia dapat menjadi insiden hukum atau keselamatan. Pengaturan ini membutuhkan pembumian pada sumber otoritatif, validasi keluaran ketat, pengawasan manusia untuk keluaran berdampak, dan catatan jelas tentang apa yang ditanyakan kepada sistem dan apa yang dihasilkannya. Teknik dalam bab ini (retrieval-augmented generation, guardrail, dan evaluasi ketat) adalah yang membuat LLM cukup aman untuk di-deploy dalam konteks berisiko tinggi. Model Claude dari Anthropic adalah satu opsi terkemuka di antara beberapa penyedia yang mumpuni; praktik di sini berlaku apa pun model yang Anda pilih.

## Prinsip utama

- Bumikan model pada pengetahuan tepercaya alih-alih mengandalkan apa yang dihafalnya.
- Perlakukan prompt dan konteks sebagai artefak yang direkayasa dan diversikan, bukan string sekali pakai.
- Asumsikan model dapat salah atau dimanipulasi; validasi keluaran dan batasi tindakan.
- Beri model hanya konteks dan perkakas yang dibutuhkannya, tidak lebih, untuk mengurangi galat dan permukaan serangan.
- Evaluasi terus-menerus dengan himpunan uji offline, metrik online, dan penilaian manusia.
- Jaga manusia dalam lingkaran untuk keluaran berdampak.
- Rancang dengan model sebagai komponen tak tepercaya di dalam sistem tepercaya.

## Rekomendasi

### Rekayasa prompt dan kelola konteks dengan sengaja

Perlakukan prompt sebagai kode: simpan dalam kontrol versi, tinjau perubahan, dan uji terhadap rangkaian contoh. Susun setiap prompt dengan jelas: peran dan tugas, kendala, persyaratan format, dan contoh di mana membantu. Perlakukan jendela konteks (rentang teks tetap yang dapat dipertimbangkan model sekaligus) sebagai sumber daya langka. Sertakan informasi paling relevan, urutkan dengan cermat, dan buang derau, karena konteks tak relevan atau berlebihan menurunkan kualitas dan menaikkan biaya. Untuk aplikasi multi-giliran, kelola keadaan percakapan secara eksplisit, merangkum atau memotong riwayat agar tetap dalam batas sambil mempertahankan yang penting. Pilih instruksi jelas dan contoh few-shot (segelintir demonstrasi kerja yang disertakan dalam prompt) daripada trik rumit yang patah begitu model berganti.

### Bumikan jawaban dengan retrieval-augmented generation (RAG)

Untuk tugas padat pengetahuan, ambil dokumen relevan dari korpus tepercaya dan suplai ke model sebagai konteks, dengan memerintahkannya menjawab hanya dari materi itu dan mengutip sumbernya. RAG menjaga pengetahuan tetap mutakhir tanpa pelatihan ulang, membatasi jawaban pada konten yang disetujui, dan memungkinkan sitasi dan verifikasi. Investasikan pada kualitas pengambilan: potong dokumen secara wajar, pilih [embedding](https://en.wikipedia.org/wiki/Word_embedding) (representasi vektor numerik yang menempatkan makna serupa berdekatan) yang cocok untuk ranah Anda, dan periksa apakah bagian yang diambil benar-benar memuat jawabannya, karena jawaban fasih yang dibangun di atas bagian yang salah lebih buruk daripada tanpa jawaban. Dan ketika tak ada yang relevan ditemukan, minta sistem mengatakannya alih-alih mengarang konten.

### Bangun agen dan pemakaian perkakas dengan menahan diri

LLM dapat memanggil perkakas (pencarian, basis data, kalkulator, API internal) dan dapat dirangkai menjadi agen yang merencanakan dan bertindak dalam banyak langkah. Ini menambah kemampuan nyata, tetapi juga melipatgandakan risiko: setiap perkakas adalah cara lain bagi model yang salah atau dimanipulasi untuk menyebabkan kerugian. Definisikan perkakas dengan skema presisi, validasi setiap argumen, terapkan hak istimewa paling sedikit, dan wajibkan konfirmasi atau persetujuan manusia untuk tindakan berdampak seperti mengirim komunikasi atau memindahkan uang. Jaga loop agen terbatas, dapat diamati, dan dapat diinterupsi. Mulailah dengan perkakas bercakupan ketat dan berfungsi tunggal sebelum Anda meraih otonomi terbuka.

### Tambah guardrail dan validasi keluaran

Bungkus model dengan lapisan pertahanan. Di jalur masuk, saring dan deteksi prompt injection, terutama ketika konten tak tepercaya (halaman web, dokumen pengguna) masuk ke konteks. Di jalur keluar, validasi struktur terhadap skema, periksa klaim terhadap sumber, saring konten tidak aman atau tidak patuh, dan tolak atau coba ulang ketika validasi gagal. Untuk keluaran terstruktur, urai dan verifikasi alih-alih memercayai pemformatan model. Jangan pernah biarkan keluaran model mentah memicu tindakan tak dapat dibalik tanpa validasi. Perlakukan mitigasi halusinasi sebagai properti sistem yang Anda capai lewat pembumian, sitasi, validasi, dan tinjauan manusia, bukan sesuatu yang dikelola model sendiri.

### Evaluasi secara offline, online, dan dengan manusia

Bangun rangkaian evaluasi berisi masukan representatif dengan keluaran yang diketahui benar atau diskor rubrik, dan jalankan pada setiap perubahan prompt atau model (evaluasi offline). Ukur perilaku nyata di produksi dengan metrik seperti keberhasilan tugas, tingkat eskalasi, dan umpan balik pengguna (evaluasi online). Untuk kualitas subjektif, pakai peninjau manusia dan, dengan hati-hati, penilaian berbasis model. Evaluasi adalah jaring pengaman yang memungkinkan Anda mengubah prompt dan model dengan percaya diri. Tanpanya, Anda terbang buta.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan | Terbaik ketika |
|---|---|---|---|
| Prompting murni | Sederhana, cepat, murah diubah | Pembumian terbatas, dapat berhalusinasi | Tugas luas, taruhan rendah |
| RAG | Mutakhir, membumi, dapat dikutip | Pengambilan sulit dilakukan benar | Tugas padat pengetahuan dan faktual |
| Agen dengan perkakas | Kuat, dapat bertindak | Permukaan serangan lebih besar, lebih sulit dikendalikan | Otomasi bercakupan baik dengan guardrail |
| Model lebih besar dan kuat | Kualitas dan penalaran lebih baik | Biaya dan latensi lebih tinggi | Tugas kompleks atau berisiko tinggi |
| Model lebih kecil dan murah | Cepat dan murah | Lebih lemah pada tugas sulit | Volume tinggi, tugas sederhana |

Ketegangan intinya adalah kemampuan versus kendali dan biaya. Otonomi lebih besar dan model lebih besar memberi nilai lebih, tetapi menuntut lebih banyak guardrail, lebih banyak evaluasi, dan lebih banyak uang. Pembumian lewat RAG meningkatkan keterpercayaan dengan biaya rekayasa pengambilan. Keseimbangan yang tepat bergantung pada taruhannya: aplikasi berisiko tinggi condong ke pembumian, validasi, dan pengawasan manusia, bahkan ketika itu lebih mahal.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Batas akurasi dan pembumian apa yang harus dilewati fitur LLM sebelum menghadapi publik, dan siapa yang menyetujui?** Jawaban fasih yang mengutip sumber salah atau menciptakan kebijakan lebih buruk daripada tanpa jawaban, dan di pemerintah kutipan karangan adalah insiden hukum, bukan bug. Bagi tim besar, batas eksplisit mencegah tiap kelompok menetapkan ambang pribadi sendiri berdasarkan firasat. Bawa definisi Anda tentang "cukup membumi": apakah setiap klaim harus dapat ditelusuri ke sumber yang diambil dan diverifikasi, apakah sistem harus menolak ketika pengambilan kosong, dan apa yang sebenarnya dicakup himpunan evaluasi adversarial Anda. Sinyal yang diawasi adalah apakah ada yang saat ini dapat mengirim perubahan prompt langsung ke pengguna tanpa proses regresi. Jika taruhannya hukum atau keselamatan, jawabannya harus mengalirkan keluaran berisiko tertinggi melalui peninjau manusia dengan wewenang nyata sebelum rilis.

2. **Fitur LLM kita yang mana diam-diam adalah agen, dan sudahkah setiap perkakas diberi hak istimewa paling sedikit dan gerbang manusia pada tindakan tak dapat dibalik?** Fitur apa pun yang membiarkan model memanggil perkakas atau bertindak dalam banyak langkah telah melintas ke wilayah agen, dan setiap perkakas adalah cara lain bagi model yang salah atau dimanipulasi menyebabkan kerugian. Bagi enterprise yang menyambungkan LLM ke API internal, pertanyaan ini memunculkan risiko yang disembunyikan label "asisten sederhana". Bawa inventaris setiap perkakas yang dapat dipanggil model, validasi argumennya, cakupan hak istimewanya, dan tindakan mana (mengirim komunikasi, memindahkan uang, mengubah catatan) yang membutuhkan konfirmasi. Diskusikan apakah loop agen terbatas, dapat diamati, dan dapat diinterupsi. Jawabannya harus mengetatkan cakupan dan menambah gerbang persetujuan manusia di mana pun tindakan berdampak atau tak dapat dibalik saat ini dapat dicapai tanpa satu pun.

3. **Bagaimana kita akan tahu dalam sehari bahwa kualitas pengambilan kita turun, mengingat jawaban yakin yang dibangun di atas bagian yang salah tampak baik-baik saja?** RAG membuat jawaban tepercaya hanya ketika pengambilan benar-benar memunculkan bagian yang memuat jawabannya, dan pengambilan membusuk diam-diam seiring dokumen berubah, potongan menjadi basi, atau embedding menyimpang dari ranah Anda. Karena model tetap menulis fasih di atas konteks buruk, pengguna mungkin tak mengeluh sampai kepercayaan sudah hilang. Bawa ukuran Anda saat ini untuk latensi dan recall pengambilan, bagaimana Anda memeriksa apakah bagian yang diambil benar-benar memuat jawaban, dan bagaimana kesegaran indeks mengimbangi perubahan dokumen. Untuk deployment berisiko tinggi atau publik, diskusikan pencatatan sumber yang diambil untuk audit agar Anda dapat menelusuri jawaban buruk ke bagian buruknya. Jika Anda tak punya evaluasi pengambilan sama sekali, Anda membumikan berdasarkan iman.

4. **Apakah kita memperlakukan prompt, konteks, dan himpunan evaluasi sebagai artefak yang diversikan dan ditinjau, atau sebagai string yang berserakan di notebook dan log obrolan?** Ketika prompt menyebar di banyak tim tanpa versi dan terduplikasi, perbaikan di satu tempat tak pernah mencapai yang lain, dan tak ada yang dapat mereproduksi apa yang diminta dari sistem kuartal lalu. Bagi tim besar, registri prompt bersama dan rangkaian regresi yang berjalan pada setiap perubahan memungkinkan Anda menukar model atau mengedit instruksi tanpa diam-diam merusak fitur dua tim jauhnya. Tarikan yang bersaing adalah kecepatan: insinyur beriterasi tercepat ketika menempel prompt lalu mengirim, jadi sepakati di mana garis antara eksperimen cepat dan apa pun yang menyentuh pengguna. Bawa di mana prompt Anda benar-benar berada hari ini, apakah himpunan evaluasi menggerbangi perubahan, dan bagaimana Anda memversikan korpus pengambilan bersama prompt. Dalam pengaturan enterprise dan pemerintah, tambahkan persyaratan audit: Anda mungkin harus menunjukkan persis prompt dan sumber mana yang menghasilkan keluaran tertentu berbulan-bulan kemudian, dan prompt yang tak dapat Anda rekonstruksi adalah catatan yang tak dapat Anda pertahankan.

5. **Seiring volume tumbuh, bagaimana kita mengendalikan biaya inferensi tanpa diam-diam menurunkan kualitas, dan siapa yang memiliki keputusan pemilihan model?** TCO fitur LLM didominasi inferensi per panggilan, dan biaya yang tampak sepele dalam percontohan bertambah cepat pada skala produksi, menggoda tim untuk diam-diam turun ke model lebih lemah dan berharap tak ada yang menyadari kualitas merosot. Bagi organisasi besar, membiarkan tiap tim memilih model dan batas biaya berdasarkan perasaan menghasilkan tagihan mengejutkan sekaligus kualitas tak konsisten. Trade-off sejatinya adalah kemampuan versus biaya dan latensi: model lebih besar bernalar lebih baik pada tugas sulit, yang lebih kecil lebih murah dan cepat pada tugas sederhana, dan caching, perutean, dan cakupan pengambilan semuanya menggeser angkanya. Bawa biaya per tugas terselesaikan, kualitas menurut tingkatan model pada himpunan evaluasi Anda, dan di mana kembung prompt atau konteks menggelembungkan pengeluaran token. Dalam penganggaran enterprise dan pemerintah, namai siapa yang menyetujui pilihan model dan plafon pengeluaran, karena baris biaya yang tak dimiliki siapa pun adalah yang tak dikendalikan siapa pun ketika lalu lintas melonjak tiga kali lipat.

6. **Data sensitif apa yang dapat mencapai model, ke mana data itu pergi, dan dapatkah kita membuktikan ia tetap dalam batas?** Setiap prompt, dokumen yang diambil, dan hasil perkakas dapat membawa data pribadi atau rahasia ke dalam model dan, dengan penyedia ter-hosting, keluar dari perimeter Anda, dan kebocoran di sini adalah insiden hukum atau keselamatan, bukan tiket cacat. Bagi tim besar yang menyambungkan LLM ke sistem internal, risikonya bersembunyi di perpipaan: korpus pengambilan yang memuat catatan yang tak seharusnya dilihat pengguna tertentu, atau log yang menangkap masukan mentah. Ketegangannya adalah kemampuan versus paparan, karena penyuntingan dan pembatasan ketat dapat menumpulkan fitur yang hendak Anda bangun. Bawa peta aliran data apa yang masuk ke konteks, ketentuan retensi dan pelatihan penyedia, dan bagaimana Anda menyunting, membatasi, dan mencatat bidang sensitif. Dalam pengaturan teregulasi dan publik, kaitkan ini dengan aturan residensi data, kewajiban retensi catatan, dan batas kontraktual tentang bagaimana vendor boleh memakai data Anda, karena pengawasan yang tak dapat Anda buktikan adalah pengawasan yang tidak Anda miliki.

## Lensa sektor

**Startup.** Kirim satu fitur LLM sempit yang menyentuh nilai inti Anda, dibangun di model ter-hosting dengan pengambilan atas konten Anda sendiri, dan simpan prompt di git di balik antarmuka tipis agar Anda dapat menukar penyedia. Jalankan berkas evaluasi kecil berisi pertanyaan nyata sebelum setiap perubahan, saring teks yang ditempel pengguna untuk menumpulkan prompt injection, dan batasi pengeluaran bulanan dengan keras. Tahan godaan agen dan self-hosting: loop pemanggilan perkakas tak terbatas yang tak dapat Anda awasi adalah liabilitas, bukan demo.

**Bisnis kecil.** Anda kemungkinan tidak punya spesialis ML, jadi beli fitur LLM yang tertanam dalam perkakas yang sudah Anda pakai alih-alih mengisi staf untuk membangun. Bingkai risiko sebagai pertanyaan sederhana: di mana jawaban salah yang yakin akan membuat Anda kehilangan pelanggan, dan siapa yang memeriksa keluaran sebelum keluar. Pilih vendor yang menunjukkan sumbernya, membiarkan Anda menjaga manusia dalam lingkaran, dan membuat AI mudah dimatikan ketika berperilaku buruk.

**Enterprise.** Masalahnya skala lintas banyak tim: terbitkan pola bersama untuk RAG, guardrail, dan skema perkakas, plus harness evaluasi umum dan registri prompt agar tiap kelompok berhenti menemukan ulang mode kegagalan yang sama. Anggarkan biaya inferensi dan tinjauan manusia secara eksplisit, bakukan lapisan antarmuka agar model tetap dapat ditukar, dan atur agen secara terpusat dengan hak istimewa paling sedikit, loop terbatas, dan pencatatan audit. Kelola fitur LLM sebagai portofolio dengan metrik dan kriteria hentikan, bukan sebaran percontohan.

**Pemerintah.** Transparansi, aturan pengadaan, dan akuntabilitas membentuk setiap pilihan. Bumikan secara ketat pada sumber yang disetujui dengan sitasi, tolak ketika pengambilan kosong, dan larang model menyatakan hukum yang tak dapat dikutipnya. Jaga pejabat yang bertanggung jawab meninjau keluaran berdampak, catat masukan dan sumber yang diambil untuk audit, jalankan himpunan evaluasi adversarial sebelum setiap rilis, dan tuntut pengungkapan keterbatasan model dan ketentuan penanganan data dalam kontrak.

## Contoh

**Startup.** Startup perkakas pengembang beranggota tiga orang menambah pembantu obrolan di atas dokumentasinya sendiri agar pengguna berhenti mengirim email pertanyaan dasar. Ia memakai RAG sehingga setiap jawaban mengutip halaman dokumen tertentu, menginstruksikan model untuk mengatakan "Saya tidak yakin, ini siapa yang bisa ditanya" ketika pengambilan kosong, dan menyimpan prompt di git. Sebelum setiap perubahan ia menjalankan prompt terhadap berkas kecil pertanyaan pengguna nyata untuk menangkap regresi, dan menyaring teks yang ditempel pengguna untuk menumpulkan prompt injection. Pembantu menangani pertanyaan umum dan diam-diam meneruskan sisanya ke kotak masuk bersama para pendiri.

**Enterprise.** Sebuah perusahaan perangkat lunak membangun asisten dukungan internal di atas dokumentasi produknya. Ia memakai [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) agar jawaban mengutip halaman dokumen tertentu, memerintahkan model mengatakan "Saya tidak tahu" ketika pengambilan gagal, dan memverifikasi bahwa setiap sumber yang dikutip benar-benar ada. Prompt dikontrol versinya dan diuji terhadap rangkaian pertanyaan dukungan nyata pada setiap perubahan. Asisten mengalihkan tiket rutin dan mengeskalasi apa pun yang berkeyakinan rendah ke agen manusia, sementara metrik online melacak tingkat penyelesaian dan koreksi.

**Pemerintah.** Sebuah lembaga publik men-deploy asisten LLM untuk membantu staf menyusun balasan atas pertanyaan warga. Pembumiannya ketat: model hanya dapat menyusun balasan dari panduan yang disetujui dengan sitasi, dan dilarang menyatakan kebijakan yang tidak ada dalam sumber yang diambil. Pejabat yang bertanggung jawab meninjau setiap draf sebelum keluar. Penyaringan masukan menjaga dari prompt injection dari dokumen yang diajukan warga, keluaran dicatat untuk audit, dan himpunan evaluasi berisi kueri adversarial dan kasus tepi berjalan sebelum setiap rilis untuk memastikan sistem menolak berspekulasi tentang urusan hukum.

## Kasus bisnis: motivasi, ROI, dan TCO

Aplikasi LLM memberi ROI dengan mengotomatisasi pekerjaan padat bahasa: menjawab pertanyaan, merangkum dokumen, menyusun konten, dan mengekstrak struktur dari teks tak terstruktur. Nilai tampak sebagai tiket yang dialihkan, penyusunan lebih cepat, tinjauan manual lebih sedikit, dan kemampuan swalayan baru. Karena sering tidak ada langkah pelatihan, waktu ke nilai pertama singkat, daya tarik utama.

TCO, bagaimanapun, didominasi biaya inferensi berkelanjutan, infrastruktur pengambilan, pipeline evaluasi, sistem guardrail, dan tinjauan manusia. Biaya per panggilan bertambah cepat pada skala besar, dan aplikasi tak terpantau dapat menyimpang ke perilaku tidak aman atau mahal. Biaya tidak mengadopsi adalah tertinggal dalam kualitas layanan dan produktivitas staf. Biaya mengadopsi dengan sembrono adalah insiden halusinasi publik atau kebocoran data. Ajukan kasus kepada pimpinan dengan memasangkan target produktivitas konkret dengan rencana keselamatan dan evaluasi konkret, dan dengan menganggarkan guardrail dan pengawasan manusia yang menjaga nilai tetap awet.

## Anti-pola dan jebakan

- **Memercayai keluaran fasih.** Menyangka teks yang yakin dan ditulis baik sebagai teks yang benar.
- **RAG tanpa evaluasi pengambilan.** Mengasumsikan pengambilan berfungsi dan tak pernah memeriksa apakah ia memunculkan bagian yang tepat.
- **Buta prompt injection.** Memasukkan konten tak tepercaya ke prompt tanpa pertahanan.
- **Agen tak terbatas.** Membiarkan agen mengambil tindakan berdampak tanpa batas atau persetujuan manusia.
- **Tanpa harness evaluasi.** Mengubah prompt dan model berdasarkan firasat, tanpa pengujian regresi.
- **Prompt menyebar.** Prompt berserakan, tanpa versi, dan terduplikasi di banyak tim.
- **Otomasi berlebihan.** Menyingkirkan manusia dari keputusan yang memikul bobot hukum atau keselamatan.

## Model kematangan

1. **Memulai.** Prompting ad hoc dalam proyek terisolasi; tanpa pembumian, guardrail, atau evaluasi; prompt berada di mana pun seseorang menempelnya, dan halusinasi ditemukan di produksi.
2. **Mengembangkan.** Sebagian tim menambah RAG dan versioning prompt, validasi keluaran dasar, dan himpunan evaluasi manual kecil, tetapi praktik bervariasi antartim dan bertumpu pada juara individu alih-alih ekspektasi bersama.
3. **Membakukan.** Pola terdokumentasi untuk RAG, guardrail, skema perkakas, dan versioning prompt ditegakkan di seluruh organisasi; evaluasi offline otomatis berjalan pada setiap perubahan prompt atau model; alur berisiko tinggi membawa metrik online dan tinjauan manusia.
4. **Mengelola.** Portofolio diukur terhadap garis dasar: recall pengambilan, tingkat halusinasi dan penolakan, cakupan pertahanan injeksi, biaya dan latensi per panggilan, serta tingkat eskalasi dan koreksi dilacak pada dasbor; gerbang rilis dan kriteria hentikan menyala atas bukti alih-alih opini, dan proses regresi memblokir perubahan apa pun yang menggeser metrik ke arah salah.
5. **Mengorkestrasi.** Evaluasi offline dan online berkelanjutan terikat pada hasil bisnis; pertahanan injeksi, agen, dan pembumian diatur dan dapat diamati; organisasi rutin memensiunkan, menyetel ulang, dan menentukan ulang cakupan fitur LLM, dan menukar model seiring kualitas, biaya, dan risiko bergeser.

## Gagasan untuk didiskusikan

- Bagaimana Anda memutuskan keluaran mana yang memerlukan tinjauan manusia sebelum dipakai?
- Apa standar Anda untuk "cukup membumi" sebelum jawaban dapat ditampilkan kepada pengguna?
- Bagaimana Anda bertahan dari prompt injection ketika konten tak tepercaya harus masuk ke konteks?
- Kapan agen layak risiko tambahannya dibanding desain panggilan tunggal yang lebih sederhana?
- Bagaimana Anda mengevaluasi kualitas subjektif pada skala besar tanpa terlalu bergantung pada penilaian berbasis model?
- Bagaimana Anda menjaga prompt tetap dapat dipelihara dan konsisten di banyak tim?

## Poin-poin utama

- Keandalan datang dari rekayasa di sekitar model: konteks, pembumian, guardrail, dan evaluasi.
- RAG membumikan jawaban pada sumber tepercaya dan memungkinkan sitasi dan verifikasi.
- Perlakukan model sebagai komponen tak tepercaya; validasi keluaran dan batasi pemakaian perkakas.
- Beri agen hak istimewa paling sedikit, loop terbatas, dan persetujuan manusia untuk tindakan berdampak.
- Evaluasi secara offline, online, dan dengan manusia terus-menerus; itulah yang membuat perubahan aman.

## Referensi dan bacaan lanjutan

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (panduan rekayasa).
- Louis-François Bouchard dan Louie Peters, *Building LLMs for Production*.
