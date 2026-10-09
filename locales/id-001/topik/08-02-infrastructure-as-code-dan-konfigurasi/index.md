# 8.2 Infrastructure as code dan konfigurasi

## Tinjauan dan motivasi

[Infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) berarti mendefinisikan dan menyediakan infrastruktur (jaringan, server, basis data, load balancer, izin) lewat berkas definisi yang dapat dibaca mesin alih-alih klik konsol manual atau skrip ad hoc. [Manajemen konfigurasi](https://en.wikipedia.org/wiki/Configuration_management) memperluas gagasan yang sama ke pengaturan dan keadaan sistem begitu mereka ada. Bersama-sama keduanya mengubah infrastruktur dari artefak buatan tangan yang rapuh menjadi produk berversi, dapat ditinjau, dan dapat direproduksi dari disiplin rekayasa yang sama yang Anda pakai untuk kode aplikasi.

Bagi tim besar, IaC bukan kemudahan melainkan keharusan. Ketika ratusan insinyur membutuhkan lingkungan dan ribuan sumber daya harus tetap konsisten lintas wilayah dan akun, penyediaan manual tak dapat mengimbangi dan tak dapat tetap benar. Infrastruktur yang dikonfigurasi manusia, cepat atau lambat, menyimpang menjadi server "snowflake" unik yang tak dipahami sepenuhnya siapa pun dan tak dapat dibangun ulang dengan andal setelah kegagalan. Mengodifikasi infrastruktur membuatnya konsisten, dapat diaudit, dan sekali pakai. Lingkungan mana pun dapat diciptakan ulang dari definisinya, dan perubahan apa pun adalah diff yang dapat ditinjau.

Organisasi enterprise dan pemerintah mendapat satu manfaat lagi yang menentukan: tata kelola yang dapat ditegakkan. Persyaratan keamanan dan kepatuhan, seperti enkripsi saat diam, segmentasi jaringan, wilayah yang disetujui, dan penandaan untuk alokasi biaya, dapat ditanamkan langsung ke dalam kode dan diperiksa otomatis sebelum apa pun disediakan. Alih-alih mengaudit infrastruktur setelah kejadian dan mengejar pelanggaran, Anda mencegah infrastruktur tak patuh pernah ada. Pergeseran dari deteksi ke pencegahan ini adalah alasan inti IaC menjadi fondasi praktik platform modern.

## Prinsip utama

- Pilih definisi deklaratif yang mendeskripsikan keadaan yang diinginkan daripada skrip imperatif yang mendeskripsikan langkah.
- Simpan semua definisi infrastruktur dalam kontrol versi, ditinjau seperti kode lain.
- Perlakukan infrastruktur sebagai tak berubah: ganti alih-alih memodifikasi di tempat.
- Jadikan penyediaan idempoten agar menerapkan definisi yang sama berulang kali menghasilkan hasil yang sama.
- Deteksi dan rekonsiliasi drift, lingkungan langsung yang menyimpang dari definisi yang dideklarasikan, secara terus-menerus; kode, bukan sistem langsung, adalah sumber kebenaran.
- Susun infrastruktur dari modul berversi yang dapat dipakai ulang alih-alih salin-tempel.
- Kodekan kebijakan sebagai kode, aturan organisasi yang diekspresikan sebagai kode yang dapat diperiksa mesin, agar guardrail otomatis, bukan anjuran.
- Jauhkan rahasia dari definisi; rujuk dari manajer rahasia khusus.

## Rekomendasi

### Pilih perkakas deklaratif dan susun di sekitar modul

Adopsi perkakas IaC deklaratif, seperti [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi, atau opsi cloud-native seperti CloudFormation, dan bakukan di seluruh organisasi agar Anda menghindari lanskap perkakas yang terfragmentasi. Praktik arsitektur kuncinya adalah modularitas: bangun modul kecil, terdokumentasi baik, dan berversi yang menangkap pola umum (jaringan patuh, basis data yang diperkeras, layanan standar). Tim kemudian menyusun lingkungan dari modul ini alih-alih menulis sumber daya mentah. Ini menyebarkan bawaan baik dan pengaturan keamanan secara otomatis dan secara dramatis mengurangi duplikasi.

### Kelola state dengan sengaja

Perkakas deklaratif melacak pemetaan antara kode dan sumber daya nyata dalam berkas state. Simpan state secara jarak jauh di backend bersama, terenkripsi, dan terkendali aksesnya, dan pakai penguncian agar modifikasi bersamaan tidak dapat merusaknya. Jangan pernah menyimpan state di laptop, dan jangan pernah menyuntingnya dengan tangan kecuali sebagai tindakan pemulihan upaya terakhir. State bersifat sensitif, karena dapat memuat metadata sumber daya dan rahasia, jadi lindungi sesuai.

### Bangun infrastruktur tak berubah dengan golden image

Alih-alih menambal server yang berjalan, panggang "golden image" berversi (citra mesin atau kontainer yang telah dikonfigurasi dan diperkeras) dan deploy instans segar darinya. Ketika Anda butuh perubahan atau tambalan, bangun citra baru dan luncurkan, memensiunkan instans lama. Ini menghilangkan drift konfigurasi, membuat rollback sepele, dan menjaga setiap instans identik serta dapat ditelusuri ke build yang diketahui baik. Pipeline citra otomatis harus menyertakan pengerasan keamanan dan pemindaian, sehingga kepatuhan tertanam pada tingkat citra.

### Deteksi dan rekonsiliasi drift konfigurasi

Drift terjadi ketika lingkungan langsung menyimpang dari definisinya, biasanya karena seseorang membuat perubahan manual darurat. Jalankan deteksi drift reguler yang membandingkan keadaan aktual dengan keadaan yang dideklarasikan dan menandai perbedaannya. Perlakukan drift sebagai cacat: rekonsiliasi dengan memperbarui kode dan menerapkan ulang, bukan dengan membiarkan perubahan manual di tempatnya. Untuk sistem yang membutuhkan penegakan konfigurasi berkelanjutan, pakai perkakas manajemen konfigurasi yang terus mengonvergensikan host ke keadaan yang dideklarasikan.

### Adopsi GitOps dan deployment berbasis pull

Dalam model GitOps, repositori Git menyimpan keadaan yang diinginkan sistem yang dideklarasikan, dan agen otomatis yang berjalan di dalam lingkungan target terus menarik keadaan itu dan merekonsiliasi sistem langsung agar cocok. Ini membalik model push tradisional. Tak ada sistem eksternal yang butuh kredensial tetap untuk mengubah lingkungan, karena lingkungan menarik konfigurasinya sendiri. GitOps memberi Anda jejak audit lengkap (setiap perubahan adalah commit), rollback mudah (kembalikan commit), dan koreksi drift kuat (agen terus menegaskan ulang keadaan yang diinginkan). Ia sangat kuat untuk [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) dan untuk organisasi yang menginginkan satu sumber kebenaran yang dapat ditinjau.

### Tegakkan guardrail dengan policy as code

Ekspresikan aturan organisasi, seperti wilayah yang diizinkan, enkripsi wajib, tag yang disyaratkan, dan paparan publik yang dilarang, sebagai kebijakan yang dapat diperiksa mesin memakai perkakas seperti Open Policy Agent (OPA) atau mesin kebijakan bawaan platform seperti Sentinel. Jalankan pemeriksaan ini dalam pipeline sebelum penyediaan, agar pelanggaran diblokir otomatis. Policy as code mengubah maksud tim keamanan menjadi kontrol yang dapat dieksekusi dan diterapkan seragam, dan ia berskala ke ribuan perubahan dengan cara yang tak pernah dapat dilakukan tinjauan manual.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan | Paling cocok |
|---|---|---|---|
| IaC deklaratif (Terraform/Pulumi) | Dapat direproduksi, dapat ditinjau, drift dapat dideteksi | Kurva belajar; kompleksitas manajemen state | Hampir semua tim pada skala besar |
| Skrip imperatif | Dikenal; fleksibel untuk sekali pakai | Tidak idempoten; sulit diaudit dan diulang | Kasus sempit dan transisional |
| Tak berubah + golden image | Tanpa drift; rollback sepele | Overhead pipeline build citra | Armada yang butuh konsistensi |
| Manajemen konfigurasi mutable | Kendali berkelanjutan halus | Risiko drift; konvergensi lebih lambat | Host warisan atau berumur panjang |
| GitOps (berbasis pull) | Jejak audit kuat; menyembuhkan diri | Membutuhkan agen dalam klaster dan disiplin Git | Kubernetes dan cloud-native |
| Policy as code | Guardrail otomatis dan seragam | Upaya penulisan kebijakan di muka | Lingkungan teregulasi |

Ketegangan utamanya antara fleksibilitas dan kendali. Pendekatan manual dan imperatif terasa lebih cepat untuk satu perubahan, tetapi mengakumulasi inkonsistensi tersembunyi yang melumpuhkan pada skala besar. Infrastruktur deklaratif, tak berubah, dan diatur kebijakan meminta investasi di muka lebih besar dan pergeseran budaya nyata, karena insinyur harus berhenti membuat perubahan konsol cepat, tetapi ia membayar investasi itu berkali-kali lipat dalam keandalan, kemampuan diaudit, dan kemampuan membangun ulang apa pun sesuai permintaan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Siapa yang memiliki pustaka modul bersama, dan bagaimana perbaikan dalam modul mencapai setiap tim yang memakainya?** Modul hanya terbayar jika perbaikan dan bawaan yang diperkeras merambat, dan itu membutuhkan kepemilikan jelas dan versioning nyata, bukan folder yang disalin semua orang. Putuskan siapa yang memelihara modul jaringan-patuh dan basis-data-diperkeras, bagaimana Anda memversikannya (semantic versioning dengan changelog), dan bagaimana tim menarik peningkatan tanpa latihan kebakaran. Pada skala besar ini beda antara memperbaiki salah konfigurasi sekali dan mengejarnya di seribu sumber daya yang disunting tangan. Bawa bukti: berapa salinan berbeda pola yang sama ada hari ini, berapa lama perbaikan keamanan mencapai setiap lingkungan, dan apakah tim menyematkan versi modul atau membiarkannya mengambang. Jika tambalan kritis tak dapat mencapai seluruh properti dalam hitungan hari, modularitas Anda hanya kosmetik.

2. **Apa irama deteksi drift Anda, dan apa yang sebenarnya terjadi ketika drift ditemukan?** Drift adalah lingkungan langsung yang diam-diam menyimpang dari keadaan yang dideklarasikan, biasanya karena perubahan konsol darurat, dan menoleransinya mengubah kode Anda menjadi fiksi. Putuskan seberapa sering Anda membandingkan keadaan aktual dengan keadaan yang dideklarasikan (semalam adalah bawaan masuk akal) dan, lebih penting, putuskan responsnya: rekonsiliasi dengan memperbarui kode dan menerapkan ulang, tidak pernah dengan membiarkan perubahan manual di tempatnya. Dalam pengaturan teregulasi ini persyaratan kontrol, karena auditor membutuhkan keadaan yang dideklarasikan cocok dengan kenyataan secara terus-menerus. Bawa angka saat ini: berapa sumber daya yang menyimpang setiap minggu, berapa lama mereka tetap menyimpang, dan apakah ada yang akuntabel menutupnya. Perlakukan setiap drift sebagai cacat dengan pemilik, atau jaminan sumber-kebenaran terkikis sampai tak ada yang memercayai kode.

3. **Sudahkah Anda pindah ke GitOps dan rekonsiliasi berbasis pull, atau sistem eksternal masih memegang kredensial tetap untuk mengubah produksi?** Dalam model pull, agen di dalam lingkungan target terus merekonsiliasi sistem langsung ke Git, yang menghilangkan kebutuhan sistem luar mana pun memegang akses tulis, dan ia menegaskan ulang keadaan yang diinginkan sehingga drift mengoreksi diri. Itu postur keamanan dan audit yang kuat, karena setiap perubahan adalah commit dan tak ada operator yang butuh kredensial produksi tetap. Biayanya nyata: agen dalam klaster untuk dijalankan dan disiplin Git yang ketat, jadi timbang terhadap otomasi berbasis push Anda saat ini. Bawa daftar siapa dan apa yang saat ini dapat mengubah produksi secara langsung, dan jejak audit apa yang ditinggalkan perubahan itu. Untuk Kubernetes dan enklave berjaminan tinggi pergeseran ini biasanya sepadan; untuk segelintir sumber daya statis mungkin berlebihan.

4. **Bagaimana state infrastruktur Anda disimpan, dikunci, dan dikendalikan aksesnya, dan apa yang terjadi pada hari ia rusak atau hilang?** State adalah peta antara kode Anda dan sumber daya nyata, jadi berkas state yang hilang atau rusak dapat membuat perkakas buta terhadap sumber daya yang diciptakannya dan menggoda seseorang pada penerapan ulang destruktif. Bagi tim besar risikonya berlipat, karena banyak insinyur yang menerapkan terhadap state bersama butuh backend jarak jauh, terenkripsi, dan terkunci agar proses bersamaan tidak saling menimpa. Timbang kenyamanan satu state besar terhadap radius ledakan yang diciptakannya, dan pertimbangkan memecah state per lingkungan atau per ranah agar satu kesalahan tidak dapat menjatuhkan segalanya. Bawa faktanya: di mana state tinggal hari ini, apakah penguncian ditegakkan, siapa yang dapat membacanya (ia dapat memuat rahasia), dan apakah Anda pernah melatih pemulihan. Dalam pengaturan enterprise dan pemerintah, perlakukan backend state sebagai aset sensitif yang dikendalikan aksesnya dengan cadangan, log audit, dan runbook pemulihan sendiri, karena kehilangannya adalah kehilangan catatan Anda tentang apa yang ada.

5. **Ketika keadaan darurat sungguhan menuntut perubahan manual, apa jalur break-glass yang disahkan, dan bagaimana perubahan itu dilipat kembali ke dalam kode?** Setiap praktik IaC yang matang akhirnya bertemu insiden pukul 3 pagi di mana menunggu pipeline tidak dapat diterima, dan pertanyaan jujurnya bukan apakah perubahan manual pernah terjadi tetapi bagaimana Anda menahannya. Putuskan di muka siapa yang boleh melewati pipeline, apa yang boleh mereka sentuh, bagaimana tindakan dicatat, dan tenggat saat perubahan harus direkonsiliasi ke dalam kode atau dikembalikan. Tanpa kesepakatan itu, pengecualian darurat diam-diam menjadi kebiasaan harian dan ClickOps kembali lewat pintu belakang. Bawa bukti: berapa perubahan di luar jalur terjadi kuartal lalu, berapa lama masing-masing tetap tak terekonsiliasi, dan apakah deteksi drift benar-benar menangkapnya. Untuk badan teregulasi dan publik, prosedur break-glass terdokumentasi dengan pencatatan otomatis sering persyaratan kontrol, karena auditor mengharapkan baik bahwa keadaan darurat mungkin terjadi maupun bahwa setiap kejadian meninggalkan jejak dan mengembalikan sistem ke keadaan yang dideklarasikan.

6. **Seberapa banyak baseline keamanan dan kepatuhan Anda diekspresikan sebagai kebijakan yang otomatis memblokir perubahan buruk, versus aturan yang hidup dalam dokumen dan bergantung pada seseorang mengingatnya?** Guardrail yang ditulis sebagai prosa di wiki dilanggar rutin, karena bergantung pada setiap insinyur membaca dan menerapkannya di bawah tekanan tenggat, sedangkan aturan yang sama diekspresikan sebagai policy as code menolak perubahan tak patuh sebelum pernah disediakan. Bagi organisasi besar ini satu-satunya cara maksud tim keamanan berskala ke ribuan perubahan tanpa menjadi hambatan tinjauan. Timbang biaya di muka menulis dan memelihara kebijakan terhadap biaya berulang tinjauan manual dan remediasi setelah kejadian, dan putuskan kontrol mana (enkripsi, wilayah disetujui, tag wajib, tanpa paparan publik) yang cukup tak dapat ditawar untuk ditegakkan sebagai gerbang keras. Bawa daftar aturan baseline Anda saat ini dan tandai mana yang otomatis versus anjuran, plus seberapa sering masing-masing dilanggar dalam praktik. Dalam konteks enterprise dan pemerintah, kebijakan otomatis mengubah audit dari berminggu-minggu pengumpulan bukti manual menjadi kueri terhadap kontrol yang ditegakkan, dan mengubah kepatuhan dari deteksi menjadi pencegahan.

## Lensa sektor

**Startup.** Kecepatan menang, jadi taruh seluruh tumpukan Anda dalam satu repositori deklaratif (Terraform adalah bawaan umum), simpan state di backend terkelola terenkripsi, dan alirkan setiap perubahan melalui pull request bahkan dengan tim tiga orang. Lewati aparatus platform berat: tanpa tim modul pusat, belum ada mesin kebijakan, cukup kontrol versi dan disiplin untuk tidak pernah mengeklik di konsol. Itu saja memberi Anda lingkungan yang dapat direproduksi yang bisa dirobohkan untuk menghemat uang dan dibangun ulang untuk demo berikutnya.

**Bisnis kecil.** Tanpa spesialis platform khusus, bersandarlah pada layanan terkelola dan IaC apa pun yang sudah didukung penyedia cloud atau vendor Anda daripada mendirikan perkakas pesanan yang tak dapat Anda pelihara. Pilih membeli platform ter-hosting yang bawaan masuk akalnya (enkripsi, cadangan, penambalan) ditangani untuk Anda daripada membangun pipeline golden-image yang tak punya orang untuk menjalankannya. Bingkai tujuan secara sempit: masukkan segelintir sumber daya kritis Anda ke dalam kode agar Anda dapat membangunnya ulang setelah kegagalan atau kontraktor yang pergi.

**Enterprise.** Masalah intinya konsistensi lintas banyak tim, akun, dan wilayah, jadi berinvestasilah pada pustaka modul bersama berversi, state jarak jauh terkunci, dan policy as code yang ditegakkan dalam pipeline. Tim platform pusat menerbitkan modul dan guardrail yang diperkeras sementara tim produk melayani diri sendiri di dalamnya, dan deteksi drift berjalan terus-menerus agar ribuan sumber daya tetap dalam keadaan yang diketahui. Anggarkan biaya berkelanjutan memelihara modul dan kebijakan, karena nilainya datang dari perbaikan atau bawaan yang diperkeras merambat ke mana-mana sekaligus.

**Pemerintah.** Aturan pengadaan, akreditasi, dan akuntabilitas publik mendorong Anda ke infrastruktur tak berubah, commit bertanda tangan, dan rekonsiliasi GitOps di dalam enklave terakreditasi, sehingga tak ada operator yang memegang kredensial tetap untuk mengubah produksi. Kodekan baseline keamanan yang disyaratkan ke dalam golden image dan policy as code, dan biarkan riwayat commit menjadi bukti audit yang tahan-rusak dan tersedia terus-menerus. Pilih perkakas terbuka dan portabel daripada format proprietari yang menjebak Anda, dan jadikan prosedur break-glass dan pencatatannya eksplisit agar perubahan darurat tetap memenuhi persyaratan kendali konfigurasi.

## Contoh

**Startup.** Startup lima orang mendefinisikan seluruh penyiapan AWS-nya, yaitu VPC, basis data, dan layanan kontainer, dalam satu repositori Terraform dengan state disimpan di backend S3 terenkripsi dan penguncian lewat DynamoDB. Setiap perubahan melalui pull request, sehingga bahkan insinyur on-call tunggal dapat melihat persis apa yang akan berubah sebelum menjalankan apply. Ketika mereka butuh lingkungan staging segar untuk demo besar, mereka menyalin modul kecil dan mendirikannya dalam hitungan menit, dan merobohkannya secepat itu untuk menjaga tagihan cloud rendah.

**Enterprise.** Sebuah pengecer multinasional mengelola infrastruktur di beberapa akun dan wilayah cloud. Tim platform pusat menerbitkan modul Terraform berversi untuk jaringan patuh, basis data, dan perancah layanan, dan menegakkan kebijakan OPA yang menolak sumber daya apa pun yang tak memiliki enkripsi atau tag alokasi biaya. Tim produk menyediakan lingkungan mereka sendiri secara swalayan, tetapi setiap perubahan mengalir melalui pipeline, di mana kebijakan diperiksa otomatis. Deteksi drift berjalan semalam dan membuka tiket untuk setiap perubahan manual, menjaga ribuan sumber daya terus-menerus dalam keadaan yang diketahui dan patuh.

**Pemerintah.** Sebuah lembaga pertahanan yang beroperasi di lingkungan berjaminan tinggi membangun golden image yang diperkeras yang menanamkan baseline keamanan yang disyaratkan, dan hanya men-deploy instans tak berubah dari citra itu. Semua infrastruktur dideklarasikan di Git dan direkonsiliasi oleh agen GitOps di dalam enklave terakreditasi, sehingga tak ada operator yang memegang kredensial tetap untuk mengubah produksi secara langsung. Setiap perubahan adalah commit bertanda tangan. Ini memberi auditor riwayat lengkap yang tahan-rusak dan memenuhi persyaratan pemantauan berkelanjutan dan kendali konfigurasi tanpa pengumpulan bukti manual.

## Kasus bisnis: motivasi, ROI, dan TCO

ROI IaC datang dari kecepatan, keandalan, dan pengurangan risiko. Lingkungan yang dulu memakan berminggu-minggu penyediaan manual digerakkan tiket dapat dibuat dalam hitungan menit, yang membebaskan insinyur dan mempercepat proyek. Reprodusibilitas memangkas waktu pemulihan setelah kegagalan, karena lingkungan mana pun dapat dibangun ulang dari kode. Penegakan kebijakan otomatis mengurangi frekuensi dan biaya insiden keamanan dan temuan audit, yang bagi organisasi teregulasi dapat substansial.

Pada buku besar TCO, biaya adopsi mencakup perkakas, pelatihan, membangun pustaka modul dan kebijakan, dan disiplin untuk berhenti membuat perubahan manual. Biaya tidak mengadopsi lebih curam dan bertambah seiring waktu: infrastruktur snowflake yang tak dapat dibangun ulang siapa pun, penyediaan lambat dan rawan galat, salah konfigurasi keamanan yang mengarah pada pelanggaran, dan audit yang menghabiskan berminggu-minggu upaya manual. Bagi pimpinan, bingkai IaC sebagai mengubah infrastruktur dari liabilitas tak terkelola menjadi aset teratur yang dapat direproduksi, dan sebagai mekanisme yang membuat keamanan dan kepatuhan otomatis alih-alih aspirasional.

## Anti-pola dan jebakan

- **ClickOps di produksi.** Membuat perubahan dengan tangan di konsol menjamin drift dan menghancurkan reprodusibilitas.
- **Rahasia dalam kode.** Menanam kredensial dalam berkas definisi membocorkannya ke riwayat versi dan state.
- **Definisi monolitik tanpa modul.** Satu konfigurasi raksasa yang tak berani diubah siapa pun menjadi serapuh penyiapan manual yang digantikannya.
- **State tak terkelola.** Berkas state lokal atau tak terkunci menyebabkan kerusakan dan infrastruktur hilang.
- **Drift ditoleransi.** Membiarkan perubahan manual di tempatnya mengikis jaminan sumber-kebenaran sampai kode adalah fiksi.
- **Kebijakan sebagai dokumentasi.** Aturan yang hidup di wiki alih-alih pemeriksaan otomatis dilanggar rutin.
- **Perbanyakan salin-tempel.** Menduplikasi konfigurasi antartim berarti perbaikan dan peningkatan tak pernah menyebar.

## Model kematangan

**Tingkat 1: Memulai.** Infrastruktur disediakan secara manual lewat konsol dan skrip ad hoc. Lingkungan tidak konsisten, tak terdokumentasi, dan tak dapat direproduksi dengan andal, dan pemulihan dari kegagalan lambat dan tak pasti.

**Tingkat 2: Mengembangkan.** Sebagian infrastruktur dikodifikasi, tetapi praktik bervariasi menurut tim. Manajemen state tidak konsisten, drift lazim, rahasia kadang bocor ke definisi, dan kebijakan ditegakkan, jika sama sekali, lewat tinjauan manual.

**Tingkat 3: Membakukan.** IaC deklaratif adalah standar terdokumentasi di seluruh organisasi, dibangun dari modul bersama berversi dengan state jarak jauh terkelola dan terkunci. Policy as code menegakkan guardrail dalam pipeline, rahasia dirujuk dari manajer khusus, dan deteksi drift berjalan pada irama reguler.

**Tingkat 4: Mengelola.** Praktik diukur terhadap garis dasar. Anda melacak tingkat drift dan mean time to reconcile, adopsi versi modul antartim, pelanggaran kebijakan yang diblokir versus yang lolos, lead time penyediaan, dan pangsa sumber daya yang benar-benar berada di bawah kode. Metrik ini menggerbangi perubahan dan mengarahkan di mana Anda berinvestasi, sehingga keputusan bertumpu pada bukti alih-alih anekdot.

**Tingkat 5: Mengorkestrasi.** Infrastruktur tak berubah dan digerakkan GitOps, menyembuhkan diri terhadap drift, dengan bukti kepatuhan dihasilkan otomatis. Pustaka modul dan kebijakan terus membaik dari pemakaian dan insiden nyata, dan praktik infrastruktur terintegrasi dengan perencanaan keamanan, biaya, dan pengiriman sehingga seluruh properti beradaptasi seiring persyaratan bergeser.

## Gagasan untuk didiskusikan

- Di mana garis seharusnya berada antara modul yang diatur secara terpusat dan otonomi tim untuk mendefinisikan infrastruktur kustom?
- Bagaimana Anda menangani perubahan darurat sungguhan yang harus melewati pipeline, tanpa menormalkan ClickOps?
- Apa strategi yang tepat untuk mengelola dan mengamankan state di banyak akun dan tim?
- Kapan manajemen konfigurasi mutable masih dibenarkan versus infrastruktur sepenuhnya tak berubah?
- Bagaimana Anda menjaga pustaka policy-as-code tetap selaras dengan persyaratan keamanan dan regulasi yang berkembang?
- Seperti apa jalur migrasi realistis untuk infrastruktur warisan yang mendahului IaC?

## Poin-poin utama

- Definisikan infrastruktur secara deklaratif, versikan, dan perlakukan sebagai kode yang dapat ditinjau dan direproduksi.
- Bangun dari modul kecil berversi untuk menyebarkan bawaan baik dan menghilangkan duplikasi.
- Pilih infrastruktur tak berubah dan golden image untuk menghapus drift dan menyederhanakan rollback.
- Kelola state dengan sengaja dan jauhkan rahasia dari definisi.
- Adopsi GitOps untuk jejak audit kuat dan rekonsiliasi yang menyembuhkan diri.
- Tegakkan guardrail dengan policy as code agar kepatuhan dicegah menjadi ada, bukan diaudit setelah kejadian.

## Referensi dan bacaan lanjutan

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, dan Niall Richard Murphy (ed.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, dan John Willis, *The DevOps Handbook*.
- Weaveworks, tulisan dasar "GitOps" (Alexis Richardson et al.).
- Dokumentasi Open Policy Agent dan bahasa kebijakan Rego.
- NIST Special Publication 800-53, kontrol keamanan dan privasi (keluarga manajemen konfigurasi).
