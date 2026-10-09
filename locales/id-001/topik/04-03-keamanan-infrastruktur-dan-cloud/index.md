# 4.3 Keamanan infrastruktur dan cloud

## Tinjauan dan motivasi

Aplikasi berjalan di atas infrastruktur, dan kini infrastruktur itu sebagian besar berbasis cloud, terdefinisi-perangkat-lunak, dan selalu berubah. Satu insinyur kini dapat menyediakan basis data, membuka jalur jaringan, atau memberi izin dengan satu perintah, pada skala dan kecepatan yang tak pernah diantisipasi kendali perubahan tradisional. Kekuatan itulah persis mengapa salah konfigurasi, bukan eksploit eksotis, adalah penyebab utama pembobolan cloud. Bucket penyimpanan yang tak sengaja publik atau peran akses yang terlalu luas dapat mengekspos seluruh data organisasi dalam hitungan detik.

Bagi enterprise besar, infrastruktur cloud mencakup beberapa penyedia, ribuan akun, dan campuran layanan terkelola, kontainer, dan fungsi serverless. Permukaan serangan bukan perimeter statis. Ia kumpulan sumber daya dan identitas yang hidup dan menyebar. Bagi pemerintah, kompleksitas yang sama bertemu rezim otorisasi ketat, mandat residensi data, dan batas klasifikasi yang membentuk setiap pilihan arsitektural. Dalam keduanya, lapisan identitas telah menjadi perimeter baru: siapa dapat melakukan apa, pada sumber daya mana, di bawah kondisi apa.

Bab ini membahas cara mengamankan fondasi itu: [manajemen identitas dan akses](https://en.wikipedia.org/wiki/Identity_management) (IAM), [segmentasi jaringan](https://en.wikipedia.org/wiki/Network_segmentation), [enkripsi](https://en.wikipedia.org/wiki/Encryption) dan [manajemen kunci](https://en.wikipedia.org/wiki/Key_management), keamanan beban kerja kontainer dan [serverless](https://en.wikipedia.org/wiki/Serverless_computing), serta manajemen postur berkelanjutan yang menjaga properti cloud yang bergerak cepat dari hanyut ke bahaya.

## Prinsip utama

- **Identitas adalah perimeter.** Keputusan akses bertumpu pada identitas kuat dan otorisasi berbutir halus, bukan lokasi jaringan.
- **Hak istimewa paling sedikit, selalu.** Setiap identitas, manusia atau mesin, mendapat izin minimum yang dibutuhkan, dan tidak lebih.
- **Segmentasikan untuk menahan.** Bagi jaringan dan beban kerja agar kompromi di satu area tidak dapat menyebar bebas.
- **Enkripsi di mana-mana.** Lindungi data saat transit dan saat disimpan secara bawaan, dengan kunci yang dikelola baik.
- **Tak berubah dan deklaratif.** Definisikan infrastruktur sebagai kode (IaC), deploy secara tak berubah, dan perlakukan penyimpangan (drift) sebagai cacat.
- **Verifikasi berkelanjutan.** Postur bukan audit sekali jalan; pindai dan tegakkan secara berkelanjutan.
- **Konfigurasi aman secara bawaan.** Keadaan bawaan sumber daya mana pun harus terkunci, bukan terbuka.

## Rekomendasi

### Rancang manajemen identitas dan akses dengan sengaja

IAM adalah bagian terpenting keamanan cloud, dan yang paling sering salah dikelola.

- Gunakan **[kendali akses berbasis peran](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** untuk memberi izin menurut fungsi pekerjaan, dan **[kendali akses berbasis atribut](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** di tempat keputusan yang lebih halus dan sadar konteks dibutuhkan (berdasarkan tag, lingkungan, klasifikasi data, atau waktu).
- Hilangkan kredensial statis berumur panjang demi token berumur pendek yang diterbitkan otomatis dan federasi identitas beban kerja.
- Tegakkan [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (autentikasi multifaktor) untuk semua akses manusia dan wajibkan autentikasi kuat untuk tindakan berhak istimewa.
- Terapkan hak istimewa paling sedikit dengan ketat: mulai dari nol dan tambahkan izin dengan sengaja. Tinjau dan pangkas izin yang tak dipakai secara berkala; akses cenderung menumpuk.
- Pisahkan tugas agar tak ada identitas tunggal yang dapat membuat sekaligus menyetujui perubahan sensitif.
- Gunakan akun atau proyek khusus untuk menciptakan batas keras antarlingkungan (produksi, staging, pengembangan) dan antarunit bisnis.

### Segmentasikan jaringan dan mikrosegmentasikan beban kerja

Jaringan datar membiarkan penyerang berkeliaran menyamping begitu mereka masuk. Bagi dan tahan.

- Segmentasikan pada tingkat jaringan menjadi tingkatan dan zona, hanya mengizinkan lalu lintas yang secara sah dibutuhkan setiap tingkat.
- Terapkan **mikrosegmentasi** agar beban kerja individual hanya berkomunikasi dengan rekan spesifik yang dibutuhkannya, ditegakkan oleh kebijakan sadar-identitas alih-alih aturan subnet luas.
- Tolak secara bawaan lalu lintas timur-barat; wajibkan aturan izin eksplisit.
- Taruh penyimpanan data sensitif di subnet privat tanpa eksposur internet langsung, dijangkau hanya lewat jalur terkendali.
- Gunakan konektivitas privat ke layanan terkelola alih-alih merutekan lewat internet publik di tempat memungkinkan.

### Enkripsi data dan kelola kunci dengan benar

Enkripsi hanya sekuat manajemen kunci di baliknya.

- Enkripsi **saat transit** dengan [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) terkini di mana-mana, termasuk lalu lintas antarlayanan internal.
- Enkripsi **saat disimpan** secara bawaan untuk semua penyimpanan, basis data, dan cadangan.
- Kelola kunci dengan **Key Management Service (KMS)**, dan pakai **[Hardware Security Module](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** untuk kunci berjaminan tertinggi dan untuk persyaratan regulasi.
- Rotasi kunci menurut jadwal dan dukung rotasi cepat saat dugaan kompromi.
- Kendalikan dan audit siapa yang dapat memakai dan mengelola kunci terpisah dari siapa yang dapat mengakses data, sehingga penjagaan kunci menegakkan pemisahan tugas.
- Pertimbangkan kunci yang dikelola pelanggan di tempat regulasi atau kepercayaan kontraktual mewajibkan organisasi memegang kunci alih-alih penyedia.

### Amankan kontainer, Kubernetes, dan serverless

Setiap model komputasi membawa risikonya sendiri.

- **Kontainer:** bangun dari citra dasar minimal dan tepercaya; pindai citra untuk kerentanan sebelum deployment; jalankan sebagai non-root; jadikan sistem berkas hanya-baca di tempat memungkinkan; dan jangan pernah menanam rahasia ke dalam citra.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** aktifkan RBAC dan batasi akun layanan dengan ketat; terapkan kebijakan jaringan untuk mikrosegmentasi; gunakan admission controller dan mesin kebijakan untuk menegakkan standar; batasi kontainer berhak istimewa; isolasi beban kerja sensitif; dan jaga control plane serta node tetap tertambal.
- **Serverless:** terapkan hak istimewa paling sedikit pada peran eksekusi setiap fungsi (sumber umum izin berlebih); validasi semua masukan peristiwa; kelola rahasia lewat penyimpanan rahasia platform; dan pantau pola pemanggilan anomali.

Apa pun modelnya, jaga runtime tetap tertambal dan citra tetap segar. Kontainer hanya seaman perangkat lunak di dalamnya.

### Kelola postur keamanan cloud secara berkelanjutan

Cloud berubah jauh terlalu cepat untuk diimbangi audit manual berkala.

- Adopsi perkakas **Cloud Security Posture Management (CSPM)** untuk mendeteksi salah konfigurasi, eksposur publik, dan pelanggaran kebijakan secara berkelanjutan di seluruh akun.
- Definisikan kebijakan keamanan sebagai kode dan tegakkan saat deployment agar konfigurasi buruk diblokir sebelum mendarat.
- Pilih pencegahan (pagar pembatas yang menghentikan salah konfigurasi) daripada deteksi (peringatan setelah kejadian), dan padukan keduanya.
- Pelihara inventaris sumber daya dan identitas yang akurat; Anda tidak dapat mengamankan apa yang tidak dapat Anda lihat.
- Lacak dan perbaiki penyimpangan antara infrastruktur-sebagai-kode yang dideklarasikan dan keadaan berjalan sebenarnya.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| RBAC | Sederhana, dapat dipahami, mudah diaudit | Kasar, ledakan peran pada skala besar |
| ABAC | Berbutir halus, sadar konteks, berskala dengan tag | Kompleks dirancang dan dinalar |
| Kunci dikelola penyedia (KMS) | Mudah, terintegrasi, beban operasional rendah | Penyedia memegang penjagaan; kendali lebih sedikit |
| Kunci dikelola pelanggan/HSM | Kendali penuh, memenuhi mandat ketat | Beban operasional, risiko kehilangan kunci |
| Pagar pembatas preventif | Menghentikan salah konfigurasi sebelum terjadi | Dapat memblokir pekerjaan sah, butuh penyetelan |
| CSPM detektif saja | Fleksibel, tidak memblokir | Kerusakan dapat terjadi sebelum terdeteksi |
| Mikrosegmentasi | Penahanan gerak lateral yang kuat | Kompleksitas operasional, sebaran kebijakan |

Trade-off dominannya adalah kendali versus beban operasional. Kendali lebih ketat (kunci dikelola pelanggan, mikrosegmentasi ketat, ABAC) mengurangi risiko, tetapi menuntut keahlian dan pemeliharaan yang sulit dipertahankan tim kecil. Tingkat yang tepat bergantung pada seberapa sensitif datanya dan regulasi apa yang berlaku. Pendekatan pragmatis melapisi bawaan aman yang kuat untuk semua orang, lalu menyisihkan ketelitian ekstra untuk sistem berisiko tertinggi, dan memilih pagar pembatas otomatis yang menjadikan pilihan aman sebagai bawaan alih-alih disiplin manual.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Di mana Anda akan menarik batas akun atau proyek yang keras, dan apa yang termasuk di dalam masing-masing?** Akun dan proyek khusus menciptakan penahanan terkuat yang ditawarkan cloud, sehingga kompromi di pengembangan tidak dapat menjangkau produksi dan satu unit bisnis tidak dapat menyentuh data unit lain. Putuskan skema batas Anda sebelum properti tumbuh menjadi ribuan akun, karena memasang isolasi pada struktur datar lambat dan berisiko. Untuk pekerjaan enterprise dan pemerintah, batas ini juga memetakan bersih ke pemisahan lingkungan, klasifikasi data, dan batas radius ledakan yang diharapkan auditor. Bawa diagram saat ini tentang beban kerja mana yang berbagi akun hari ini dan tandai di mana satu peran terlalu luas menjangkau produksi dan nonproduksi. Jika data sensitif berada di akun yang sama dengan beban kerja eksperimental, itulah batas yang diperbaiki lebih dulu.

2. **Apa standar Anda tentang siapa yang dapat mengelola kunci versus siapa yang dapat mengakses data terenkripsi?** Enkripsi hanya sekuat manajemen kunci, dan memisahkan penjagaan kunci dari akses data mengubah KMS Anda menjadi titik penegakan pemisahan tugas. Putuskan siapa yang boleh membuat, merotasi, dan memakai kunci, dan pastikan himpunan itu tidak tumpang tindih dengan orang yang dapat membaca data yang dilindungi kunci itu. Untuk sistem teregulasi dan pemerintah, ini sering menggerakkan pilihan antara kunci dikelola penyedia dan kunci dikelola pelanggan atau HSM, yang membawa lebih banyak kendali dan lebih banyak risiko operasional kehilangan kunci. Bawa kebijakan kunci Anda saat ini dan periksa apakah ada identitas tunggal yang dapat mengelola kunci sekaligus membaca data di baliknya, karena itu celah senyap yang umum. Jika penjagaan dan akses tidak dipisahkan, enkripsi saat disimpan melindungi Anda kurang dari yang disarankan dasbor.

3. **Bagaimana Anda akan menjadikan bawaan aman tak terhindarkan dalam landing zone Anda alih-alih sekadar direkomendasikan?** Salah konfigurasi, bukan eksploit eksotis, adalah penyebab utama pembobolan cloud, dan perbaikannya adalah pagar pembatas preventif yang memblokir basis data publik atau bucket tak terenkripsi sebelum mendarat, bukan peringatan setelah kejadian. Putuskan kebijakan mana yang akan Anda tegakkan saat deploy (tanpa penyimpanan publik, enkripsi aktif secara bawaan, tag wajib) dan mana yang hanya akan Anda deteksi dan laporkan. Bagi tim besar, menyandikan ini ke landing zone dan templat infrastruktur-sebagai-kode berarti setiap akun baru mewarisi perlindungan tanpa upaya per tim, mengubah keamanan dari pajak berulang menjadi investasi sekali jalan. Bawa temuan salah konfigurasi bulan terakhir Anda dan tanyakan mana yang akan dihentikan sepenuhnya oleh pagar pembatas preventif. Jika manajemen postur Anda hanya detektif, kerusakan dapat terjadi sebelum ada yang melihat peringatan, jadi pindahkan pemeriksaan berdampak tertinggi ke pencegahan.

4. **Bagaimana Anda menghilangkan kredensial statis berumur panjang tanpa merusak otomasi yang diam-diam bergantung padanya?** Kunci akses tertanam yang tak pernah kedaluwarsa termasuk penyebab pembobolan cloud yang paling umum, karena satu kunci bocor dalam skrip, log, atau repositori memberi penyerang akses tahan lama. Tarikan yang bersaing bersifat operasional: pekerjaan CI warisan, tugas cron, dan integrasi pihak ketiga sering mengasumsikan kunci statis ada, dan memindahkannya ke token berumur pendek atau federasi identitas beban kerja memakan waktu rekayasa yang tak dijadwalkan siapa pun. Bagi tim besar, jalur migrasi bersama (terbitkan token otomatis, tetapkan standar kedaluwarsa, dan beri peringatan pada kunci berumur panjang baru mana pun) mencegah setiap kelompok menciptakan jawaban yang lebih lemah sendiri. Bawa inventaris setiap kredensial statis yang dipakai, usianya, radius ledakannya, dan apakah sistem yang diberinya dapat menerima identitas terfederasi hari ini. Dalam pengaturan enterprise dan pemerintah, kaitkan tenggat dengan siklus audit dan otorisasi, karena kredensial yang hidup lebih lama daripada orang yang membuatnya persis temuan yang menghentikan otorisasi berkelanjutan.

5. **Ketika sumber daya salah konfigurasi atau kunci terkompromi, secepat apa Anda dapat mendeteksi, menahan, dan memperbaikinya, dan sudahkah Anda mengukurnya?** Bucket publik atau peran terlalu luas hanya berbahaya selama jendelanya tetap terbuka, sehingga waktu rata-rata mendeteksi dan memperbaiki adalah angka yang benar-benar membatasi paparan Anda. Ketegangannya antara pagar pembatas preventif yang menghentikan kesalahan saat deploy dan manajemen postur detektif yang menangkap apa yang lolos, dan Anda butuh angka jujur untuk keduanya alih-alih asumsi menenangkan bahwa pagar pembatas mencakup segalanya. Bawa temuan salah konfigurasi dan penyimpangan kuartal terakhir Anda dengan stempel waktu, median waktu dari diperkenalkan sampai diperbaiki, dan catatan latihan rotasi kompromi kunci. Untuk properti enterprise dan pemerintah yang mencakup ribuan akun, sepakati siapa yang memiliki remediasi untuk temuan yang jelas bukan milik tim siapa pun, karena peringatan tanpa responden yang bertanggung jawab adalah peringatan yang menua menjadi insiden.

6. **Bagaimana Anda akan menjaga postur keamanan konsisten di beberapa cloud, akun, dan tim tanpa memperlambat semua orang?** Properti multi-cloud dan multiakun terfragmentasi cepat: setiap penyedia punya model IAM sendiri, bawaan sendiri, dan perkakas postur sendiri, sehingga kebijakan yang ditegakkan di satu tempat diam-diam lapuk di tempat lain. Pertukarannya antara kendali pusat yang menjamin konsistensi dan otonomi lokal yang memungkinkan tim bergerak cepat, dan condong terlalu jauh ke salah satu entah menghambat pengiriman atau membiarkan standar menyimpang. Bawa peta cakupan Anda saat ini: akun mana yang mewarisi pagar pembatas landing-zone, mana yang tak terkelola, dan di mana kendali yang sama diekspresikan tiga cara berbeda di berbagai penyedia. Untuk organisasi besar atau publik, tambahkan sudut audit, karena auditor mengharapkan satu standar yang dapat dipertahankan diterapkan di mana-mana, dan kendali yang ada di cloud utama Anda tetapi tidak di cloud sekunder adalah celah yang akan ditemukan penyerang atau penilai yang gigih lebih dulu.

## Lensa sektor

**Startup.** Kecepatan dan kelangsungan hidup menang, jadi bersandarlah sepenuhnya pada bawaan aman yang dikirim gratis: enkripsi saat disimpan aktif, penyimpanan privat kecuali manusia membukanya, MFA pada akun root, dan identitas beban kerja bawaan penyedia alih-alih kunci akses yang ditempel. Jangan dirikan platform CSPM atau kabelkan mikrosegmentasi dengan tangan yang tak sanggup Anda pelihara; satu pagar pembatas yang memblokir basis data yang dibuka ke internet membeli sebagian besar perlindungan untuk satu sore kerja. Jaga segalanya dalam infrastruktur-sebagai-kode sejak awal agar pengerasan berskala bersama Anda alih-alih menjadi penulisan ulang belakangan.

**Bisnis kecil.** Tanpa insinyur keamanan khusus dan dengan anggaran ketat, pilih layanan terkelola yang bawaannya sudah dikeraskan dan yang manajemen kuncinya ditangani untuk Anda, alih-alih membangun disiplin KMS sendiri. Perlakukan keamanan cloud sebagai pertanyaan kebersihan konfigurasi: ketahui bucket dan basis data apa yang ada, jaga privat, wajibkan MFA, dan nyalakan pemeriksaan postur bawaan penyedia yang datang tanpa biaya tambahan. Ketika membeli perkakas, pilih yang menandai eksposur publik dan penyimpanan tak terenkripsi secara bawaan, karena kedua kesalahan itu menyebabkan sebagian besar pembobolan yang dapat dihindari.

**Enterprise.** Masalah sebenarnya konsistensi di ribuan akun dan banyak tim, sehingga pekerjaannya pekerjaan platform: landing zone yang menyediakan setiap akun dalam keadaan dikeraskan, pagar pembatas yang ditegakkan sebagai policy-as-code, dan CSPM memindai penyimpangan secara berkelanjutan. Bakukan model IAM, aturan penjagaan kunci, dan garis dasar segmentasi agar kelompok berhenti menciptakan versi yang lebih lemah, dan ukur postur di seluruh properti alih-alih memercayai kata setiap tim. Anggarkan rekayasa berkelanjutan untuk menjaga kebijakan tetap mutakhir seiring penyedia menambah layanan dan properti tumbuh.

**Pemerintah.** Aturan pengadaan, mandat residensi data, dan rezim otorisasi membentuk setiap pilihan, sehingga kendali keamanan berlipat sebagai bukti audit. Pilih manajemen kunci tervalidasi FIPS dengan penjagaan dipisahkan dari akses data, wilayah terisolasi yang menjaga data di dalam batas nasional, dan citra kontainer bertanda tangan dan terpindai dengan admission control ketat. Terbitkan pengamanan yang bisa, masukkan manajemen postur berkelanjutan langsung ke otorisasi berkelanjutan, dan wajibkan vendor mengungkapkan bawaan konfigurasinya serta mendukung kendali segmentasi dan penjagaan kunci yang dituntut batas klasifikasi Anda.

## Contoh

**Startup.** Sebuah startup kecil menjalankan segalanya di satu akun cloud dan tidak dapat mengisi staf tim platform, jadi ia bersandar pada bawaan yang dikirim aman: enkripsi saat disimpan aktif secara bawaan, bucket penyimpanan privat kecuali manusia secara eksplisit membukanya, dan MFA diwajibkan pada akun root. Alih-alih kunci akses berumur panjang yang ditempel ke CI, ia memakai identitas beban kerja bawaan penyedia sehingga pipeline mendapat kredensial berumur pendek secara otomatis. Satu pagar pembatas gratis yang menandai basis data apa pun yang dibuka ke internet menyelamatkan mereka dari kesalahan cloud yang paling umum dan paling mahal, dengan biaya satu sore untuk menyiapkannya.

**Enterprise.** Sebuah perusahaan media yang menjalankan ribuan akun di dua penyedia cloud menegakkan pola landing-zone: setiap akun disediakan dari templat dengan enkripsi saat disimpan aktif secara bawaan, tanpa akses publik pada penyimpanan, tag wajib, dan garis dasar kebijakan pagar pembatas. CSPM memindai penyimpangan secara berkelanjutan, dan federasi identitas beban kerja telah menghilangkan kunci berumur panjang untuk sistem CI. Ketika pengembang tak sengaja mencoba membuka basis data ke internet, kebijakan preventif memblokir perubahan dan membuka tiket secara otomatis.

**Pemerintah.** Sebuah lembaga terkait pertahanan beroperasi di wilayah cloud terisolasi dengan residensi data ditegakkan oleh kebijakan sehingga tak ada data yang meninggalkan batas nasional. Kunci paling sensitif hidup di HSM tervalidasi FIPS (Federal Information Processing Standards), dengan penjagaan kunci dipisahkan dari akses data untuk menegakkan pemisahan tugas. Klaster Kubernetes memakai kebijakan jaringan ketat dan admission control; setiap citra kontainer dipindai dan ditandatangani sebelum boleh berjalan. Manajemen postur berkelanjutan masuk langsung ke bukti otorisasi berkelanjutan lembaga.

## Kasus bisnis: motivasi, ROI, dan TCO

Keamanan infrastruktur cloud adalah tempat investasi kecil mencegah kerugian katastrofik kelas berita utama. Total biaya kepemilikan mencakup perkakas CSPM, layanan manajemen kunci, waktu rekayasa untuk merancang IAM hak istimewa paling sedikit dan segmentasi, dan upaya berkelanjutan untuk menjaga kebijakan tetap mutakhir. Biaya ini nyata tetapi sederhana. Biaya melewatkannya adalah satu sumber daya salah konfigurasi yang mengekspos seluruh basis data pelanggan, beserta denda regulasi, biaya notifikasi, dan kerusakan merek yang bertahan lama yang menyusul. Pembobolan salah konfigurasi cloud termasuk insiden paling umum dan paling dapat dicegah di industri.

Otomasi dan penggunaan ulang memperkuat ROI. Sandikan bawaan aman ke landing zone dan templat infrastruktur-sebagai-kode, dan setiap akun dan beban kerja baru mewarisi perlindungan tanpa upaya per tim, mengubah keamanan dari pajak manual berulang menjadi investasi platform sekali jalan. Untuk pemerintah dan enterprise teregulasi, manajemen postur yang kuat juga menurunkan biaya audit dan otorisasi berkelanjutan dengan menghasilkan bukti secara otomatis. Ketika mengajukan kasus kepada pimpinan, tekankan bahwa lapisan identitas dan konfigurasi kini vektor pembobolan utama, bahwa salah konfigurasi dapat dicegah, dan bahwa pagar pembatas memangkas risiko sekaligus gesekan tinjauan manual.

## Anti-pola dan jebakan

- **Izin wildcard.** Memberi akses `*` luas "agar semuanya berjalan" dan tak pernah mengetatkannya.
- **Kunci statis berumur panjang.** Kunci akses tertanam dalam skrip dan CI yang tak pernah kedaluwarsa dan akhirnya bocor.
- **Jaringan datar.** Tanpa segmentasi, sehingga satu host terkompromi menjangkau segalanya.
- **Publik tak sengaja.** Penyimpanan dan basis data terekspos ke internet lewat pengaturan bawaan atau ceroboh.
- **Enkripsi tanpa disiplin kunci.** Mengaktifkan enkripsi tetapi membiarkan akses kunci terbuka lebar atau tak pernah merotasi.
- **Rahasia tertanam dalam citra.** Kredensial tertanam dalam citra kontainer yang menyebar ke mana pun citra berjalan.
- **Peran serverless berizin berlebih.** Fungsi diberi jauh lebih banyak dari yang dibutuhkan karena pembatasan dilewati.
- **Postur hanya-audit.** Mendeteksi salah konfigurasi setelah kejadian alih-alih mencegahnya saat deploy.
- **Mengabaikan penyimpangan.** Membiarkan lingkungan berjalan menyimpang dari infrastruktur-sebagai-kode sampai tak seorang pun tahu keadaan sebenarnya.

## Model kematangan

**Tingkat 1: Memulai.** Penyediaan manual digerakkan oleh siapa pun yang membutuhkan sumber daya. Izin wildcard luas dan kunci statis berumur panjang. Jaringan datar tanpa segmentasi. Enkripsi diterapkan tidak konsisten, jika ada. Tidak ada manajemen postur; salah konfigurasi muncul hanya setelah insiden memaksa pertanyaannya.

**Tingkat 2: Mengembangkan.** Beberapa peran IAM dan MFA muncul, dan enkripsi saat disimpan dinyalakan untuk penyimpanan utama, tetapi praktik bervariasi dari tim ke tim. Tingkatan jaringan dasar ada tanpa tolak-bawaan. Tinjauan konfigurasi terjadi berkala dan dengan tangan. Infrastruktur sebagian didefinisikan sebagai kode, sehingga pengerasan bergantung pada kelompok mana yang menyediakan akun.

**Tingkat 3: Membakukan.** RBAC dan ABAC hak istimewa paling sedikit dengan kredensial berumur pendek terdokumentasi dan ditegakkan di seluruh organisasi. Segmentasi memakai tolak-bawaan timur-barat. Enkripsi saat transit dan saat disimpan aktif secara bawaan, dengan kunci di KMS pada jadwal rotasi dan penjagaan dipisahkan dari akses data. Pengerasan kontainer dan Kubernetes adalah standar, dan CSPM berjalan terhadap kebijakan terdefinisi yang diterapkan konsisten di setiap akun.

**Tingkat 4: Mengelola.** Postur diukur, bukan diasumsikan. Anda melacak metrik bernama terhadap garis dasar dan target: bagian identitas dalam garis dasar hak istimewa paling sedikit, waktu rata-rata mendeteksi dan memperbaiki salah konfigurasi dan penyimpangan, cakupan pagar pembatas dan CSPM di seluruh akun, kepatuhan rotasi kunci, dan jumlah kredensial berumur panjang yang bertahan. Temuan ditriase menurut radius ledakan, remediasi punya pemilik dan sasaran tingkat layanan, dan data tren pada angka ini menggerakkan ke mana upaya pengerasan berikutnya pergi.

**Tingkat 5: Mengorkestrasi.** Bawaan aman ditanam ke landing zone dan infrastruktur-sebagai-kode sehingga setiap sumber daya lahir dalam keadaan dikeraskan, dan kendali beradaptasi seiring properti dan gambaran ancaman bergeser. Mikrosegmentasi memakai kebijakan sadar-identitas; kunci dikelola pelanggan dan HSM melindungi sistem berjaminan tertinggi dengan pemisahan penjagaan. Pagar pembatas preventif memblokir salah konfigurasi saat deploy, penyimpangan terdeteksi dan diperbaiki otomatis, dan bukti postur masuk ke otorisasi berkelanjutan secara otomatis. Keamanan terintegrasi dengan pengiriman dan perencanaan risiko, dan organisasi rutin memensiunkan dan menentukan ulang cakupan kendali seiring penyedia, layanan, dan regulasi berubah.

## Gagasan untuk didiskusikan

1. Di mana ABAC layak kompleksitasnya versus tetap pada RBAC di lingkungan Anda?
2. Bagaimana Anda menghilangkan kredensial berumur panjang tanpa merusak otomasi warisan?
3. Apa pembagian yang tepat antara pagar pembatas preventif dan manajemen postur detektif?
4. Sistem mana yang membenarkan kunci dikelola pelanggan atau HSM mengingat biaya operasionalnya?
5. Bagaimana Anda menjaga izin hak istimewa paling sedikit agar tidak diam-diam menumpuk kembali menjadi hak istimewa berlebih?
6. Bagaimana kompleksitas multi-cloud harus mengubah pendekatan Anda terhadap postur dan kebijakan yang konsisten?

## Poin-poin utama

- Identitas adalah perimeter baru; investasikan pada IAM hak istimewa paling sedikit dengan kredensial berumur pendek.
- Segmentasikan jaringan dan mikrosegmentasikan beban kerja untuk menahan kompromi.
- Enkripsi saat transit dan saat disimpan secara bawaan, dan kelola kunci dengan KMS/HSM dan pemisahan penjagaan.
- Keraskan kontainer, Kubernetes, dan serverless; jaga runtime dan citra tetap tertambal.
- Pilih pagar pembatas preventif daripada deteksi setelah kejadian, dan kelola postur secara berkelanjutan.
- Tanamkan bawaan aman ke landing zone dan infrastruktur-sebagai-kode agar perlindungan berskala otomatis.
- Salah konfigurasi, bukan eksploit eksotis, adalah penyebab utama pembobolan cloud, dan ia dapat dicegah.

## Referensi dan bacaan lanjutan

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Centre for Internet Security, *CIS Benchmarks* (penyedia cloud, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* dan *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini dan lainnya, literatur rekayasa *Cloud security posture and detection*
- Pilar keamanan Well-Architected penyedia (sebagai panduan arsitektural netral vendor)
