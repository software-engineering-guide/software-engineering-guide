# 12.6 Peta jalan adopsi

Lampiran ini adalah panduan praktis untuk meluncurkan praktik dalam buku ini
secara *inkremental*. Instruksi terpenting dalam seluruh buku panduan,
diulang di setiap bab, adalah **adopsi secara inkremental; jangan big-bang**.
Transformasi yang mencoba mengubah segalanya sekaligus tidak mengubah apa pun
secara tahan lama: ia menghabiskan niat baik, membebani tim, dan runtuh pada
krisis pertama. Transformasi yang dimulai dari nyeri nyata, menyampaikan
kemenangan yang terlihat, dan berlipat dari sana dapat menggerakkan organisasi
beribu-ribu orang dalam beberapa tahun.

Peta jalan ini memberi Anda prinsip adopsi, urutan berbasis kematangan dari 90
hari pertama hingga dua tahun lebih, kerangka prioritisasi dengan contoh kerja,
kemenangan cepat domain demi domain, panduan khusus untuk enterprise dan
pemerintah, cara mengukur keberhasilan, dan mode kegagalan yang harus dihindari.

## Prinsip adopsi

Prinsip-prinsip ini berlaku terlepas dari ukuran, sektor, atau kematangan awal Anda.

- **Mulai dari nyeri, bukan dari kerangka.** Temukan hal yang paling menyakitkan,
  entah rilis lambat, pemadaman sering, audit gagal, atau pergantian karyawan, dan
  perbaiki itu lebih dulu. Nyeri menciptakan permintaan dan perlindungan politik
  yang tak pernah dapat diberikan mandat dari atas. Tak ada yang menolak kelegaan.
- **Jalan beraspal di atas mandat.** Jadikan cara yang direkomendasikan cara yang
  *termudah*. Golden path yang lebih cepat, lebih aman, dan lebih terdokumentasi
  memenangkan adopsi atas kebaikannya sendiri; kebijakan yang lebih lambat daripada
  jalan pintas akan dihindari. Berinvestasilah pada jalan beraspal sebelum Anda
  mendeprekasi jalan tanah.
- **Ukur hasil, bukan aktivitas.** Lacak apakah perubahan memperbaiki penyampaian,
  keandalan, postur keamanan, atau hasil pengguna, bukan berapa tim yang menghadiri
  pelatihan atau mencentang kotak. Instrumentasi sebelum Anda mengubah agar dapat
  membuktikan efeknya.
- **Amankan sponsor eksekutif, dan pertahankan.** Perubahan berkelanjutan butuh
  eksekutif akuntabel yang melindungi pendanaan, menyingkirkan hambatan, dan
  menahan garis ketika transformasi menjadi tidak nyaman. Sponsor bukan acara
  peluncuran; ia hubungan berkelanjutan yang harus Anda peroleh kembali dengan hasil.
- **Sukarelawan sebelum wajib militer.** Mulailah dengan tim yang *ingin* berubah.
  Keberhasilan mereka menjadi kisah rujukan yang menarik mayoritas yang enggan.
  Memaksa yang menolak lebih dulu menghasilkan kepatuhan berniat buruk dan kisah
  peringatan.
- **Jadikan dapat dibalik di mana bisa.** Pilih perubahan yang dapat Anda pilot,
  ukur, dan rollback. Keputusan "pintu dua arah" yang dapat dibalik boleh bergerak
  cepat; cadangkan proses berat untuk yang benar-benar tak dapat dibalik.
- **Tunjukkan kemenangan dini dan sering.** Kirim sesuatu yang terlihat dalam
  minggu, bukan kuartal. Momentum adalah sumber daya; belanjakan kemenangan pertama
  untuk mendanai yang berikutnya.
- **Temui tim di mana mereka berada.** Satu bar kematangan yang diterapkan seragam
  tidak adil dan melemahkan semangat. Urutkan menurut kesiapan dan nyeri tiap tim.

## Pengurutan berbasis kematangan

Cakrawala di bawah bersifat kumulatif: masing-masing dibangun di atas yang
sebelumnya. Tanggal adalah panduan, bukan tenggat; organisasi besar atau sangat
teregulasi dapat menjalankan tiap fase lebih lama. Polanya (*stabilkan, lalu
bakukan, lalu skalakan, lalu pertahankan*) berlaku terlepas dari laju.

### 90 hari pertama: Stabilkan dan buktikan

Sasaran: tetapkan garis dasar, pilih satu atau dua masalah unggulan, dan sampaikan
kemenangan pertama yang kredibel dengan tim yang bersedia.

- [ ] Namai sponsor eksekutif akuntabel dan koalisi pemandu kecil.
- [ ] Tetapkan garis dasar empat metrik DORA (frekuensi deployment, lead time, laju
      kegagalan perubahan, waktu pemulihan) meski angkanya kasar.
- [ ] Jalankan penilaian ringan terhadap model kematangan di bab 12.4 untuk
      menemukan celah terbesar.
- [ ] Pilih satu atau dua tim pilot yang *sukarela* dan punya nyeri nyata.
- [ ] Perbaiki satu masalah berprofil tinggi dari ujung ke ujung (mis. otomatiskan
      deployment satu tim, atau tambahkan SLO ke satu layanan kritis).
- [ ] Dirikan catatan keputusan bersama (ADR) dan tempat menerbitkan hasil.
- [ ] Sepakati bagaimana Anda akan mengukur keberhasilan *sebelum* mengubah apa pun.

### Hingga 6 bulan: Bakukan pola pemenang

Sasaran: ubah keberhasilan pilot menjadi pola yang berulang dan terdokumentasi dan
tawarkan sebagai jalan beraspal kepada kohort tim berikutnya.

- [ ] Terbitkan golden path dari pilot sebagai templat, jalur, dan dokumentasi
      yang dapat dipakai ulang.
- [ ] Dirikan tim platform atau tim pemungkin (bahkan virtual) untuk memiliki dan
      mendukung jalan beraspal.
- [ ] Gulirkan pola ke tiga sampai lima tim lagi, memprioritaskan menurut dampak
      dan kesiapan.
- [ ] Perkenalkan gerbang kualitas dan keamanan otomatis (linting, tes, SAST/SCA)
      ke jalur bersama sebagai bawaan, bukan tambahan.
- [ ] Mulai praktik tinjauan insiden tanpa menyalahkan dan terbitkan postmortem
      secara internal.
- [ ] Dirikan forum tata kelola ringan (tinjauan arsitektur, kepengurusan jalan
      beraspal) yang membuka blokir alih-alih menjaga gerbang.

### Hingga 12 bulan: Skalakan di seluruh organisasi

Sasaran: jadikan jalan beraspal bawaan untuk sebagian besar kerja baru dan mulai
memensiunkan praktik warisan terburuk.

- [ ] Perluas wewenang tim platform; terbitkan katalog layanan dan kartu skor.
- [ ] Tetapkan garis dasar seluruh organisasi: SLO untuk layanan tingkat-1, kendali
      keamanan di setiap jalur, pemeriksaan aksesibilitas di build front-end.
- [ ] Lacak laju adopsi per tim dan jadikan datanya terlihat.
- [ ] Mulai modernisasi warisan yang disengaja pada sistem berisiko tertinggi
      memakai pola strangler-fig dan branch-by-abstraction.
- [ ] Lipat pengukuran ke dalam perencanaan: tim meninjau tren DORA dan keandalan
      mereka dalam ritme operasi normal.
- [ ] Investasikan pada pemungkinan (pelatihan internal, mentoring, komunitas
      praktik) agar kapabilitas menyebar lebih cepat daripada mandat.

### 2+ tahun: Pertahankan dan perbaiki terus-menerus

Sasaran: praktik menjadi "cara kita bekerja," bukan program, dan organisasi
memperbaikinya tanpa dorongan pusat.

- [ ] Pensiunkan program transformasi sebagai inisiatif bernama; tanamkan kerjanya
      dalam tata kelola dan operasi platform normal.
- [ ] Perlakukan jalan beraspal sebagai produk dengan peta jalan, pengguna, dan
      metrik kepuasannya sendiri (survei pengalaman developer).
- [ ] Kelola utang teknis dan modernisasi sebagai portofolio tetap, bukan dorongan
      sekali jalan.
- [ ] Jalankan penilaian ulang kematangan berkala dan sesuaikan standar ke atas
      seiring lantai naik.
- [ ] Jaga dari regresi: pertahankan sponsor, terus ukur, dan segarkan praktik
      seiring teknologi dan ancaman berevolusi.

## Kerangka prioritisasi

Anda akan selalu punya lebih banyak perbaikan daripada kapasitas untuk
melakukannya. Prioritaskan dengan model sederhana yang dapat dipertahankan alih-alih
suara terlantang di ruangan.

Beri skor tiap inisiatif kandidat pada tiga dimensi:

- **Dampak (1–5):** Seberapa banyak ini akan memperbaiki hasil nyata (kecepatan
  penyampaian, keandalan, keamanan, biaya, atau nilai pengguna), dan untuk berapa
  banyak tim atau pengguna?
- **Upaya (1–5):** Seberapa banyak kerja, koordinasi, dan gangguan untuk
  menyampaikannya? (Lebih tinggi = lebih banyak upaya.)
- **Bobot risiko (0,5–2,0):** Pengali untuk urgensi dan paparan. Isu keamanan,
  kepatuhan, dan keselamatan membawa bobot lebih tinggi; yang bagus-dimiliki
  membawa lebih rendah.

Skor peringkat yang berguna adalah:

```
Prioritas = (Dampak × Bobot risiko) ÷ Upaya
```

Beri peringkat menurut prioritas menurun. Urutkan butir teratas, tetapi selalu
jaga setidaknya satu "kemenangan cepat" yang cepat dan berupaya rendah tetap
berjalan untuk mempertahankan momentum, dan tinjau ulang skor tiap kuartal seiring
kondisi berubah.

### Contoh kerja

| Inisiatif | Dampak | Upaya | Bobot risiko | Prioritas | Urutan |
|---|---|---|---|---|---|
| Otomatiskan deployment untuk layanan pendapatan teratas | 5 | 2 | 1,5 | 3,75 | Sekarang |
| Tambahkan SLO dan peringatan ke layanan tingkat-1 | 4 | 2 | 1,5 | 3,00 | Sekarang |
| Perkenalkan SAST/SCA ke jalur bersama | 4 | 2 | 2,0 | 4,00 | Sekarang |
| Gulirkan design system ke semua front-end | 4 | 5 | 1,0 | 0,80 | Nanti |
| Migrasikan batch mainframe ke cloud | 5 | 5 | 1,5 | 1,50 | Bertahap |
| Bakukan ADR lintas tim | 3 | 1 | 1,0 | 3,00 | Sekarang (kemenangan cepat) |
| Adopsi bahasa pemrograman baru di seluruh organisasi | 2 | 5 | 0,5 | 0,20 | Tunda |

Dalam contoh ini, kerja jalur keamanan memuncaki daftar karena bobot risikonya
yang tinggi dan upaya yang sederhana, sementara perubahan bahasa seluruh organisasi
jatuh ke dasar meski antusiasme, karena dampaknya rendah dan upaya serta
gangguannya tinggi. Kerangka membuat trade-off itu eksplisit dan dapat
didiskusikan, yang merupakan nilai sebenarnya.

## Kemenangan cepat domain demi domain

Setiap bagian buku punya langkah pertama berbiaya rendah dan bersinyal tinggi.
Mulailah di sini.

| Bagian | Kemenangan cepat "mulai di sini" |
|---|---|
| **Fondasi (budaya, tim, proses)** | Adopsi ADR ringan dan jalankan satu retrospektif tanpa menyalahkan; jadikan keputusan dan pembelajaran terlihat. |
| **Keahlian pemrograman** | Nyalakan auto-formatter dan linter di CI sebagai bawaan yang ditegakkan, agar gaya berhenti menjadi topik tinjauan. |
| **Arsitektur** | Tulis satu keputusan arsitektur satu halaman dan diagram konteks C4 untuk sistem terpenting Anda. |
| **Keamanan** | Tambahkan pemindaian dependensi (SCA) dan pemindaian rahasia ke jalur; aktifkan untuk satu repositori kritis dulu. |
| **UX / desain** | Jalankan tiga uji kebergunaan murah pada alur dengan lalu lintas tertinggi; perbaiki isu teratas yang Anda amati. |
| **AI / ML** | Tulis pembingkaian masalah satu halaman dan pemeriksaan kesiapan data sebelum kerja model apa pun; definisikan bagaimana Anda akan mengevaluasi keberhasilan. |
| **Data / analitik** | Definisikan satu metrik "north-star" yang disepakati dan satu dasbor tepercaya; pensiunkan yang bertentangan. |
| **DevOps / platform** | Bawa satu tim ke jalur build-test-deploy yang sepenuhnya otomatis dan dokumentasikan sebagai templat. |
| **Operasi / keandalan** | Definisikan SLI dan satu SLO untuk perjalanan pengguna paling kritis Anda; beri peringatan pada gejala, bukan sebab. |
| **Enterprise / pemerintah** | Petakan kendali Anda saat ini ke satu kerangka (NIST CSF, ISO 27001, atau SOC 2) dan otomatiskan bukti untuk satu kendali. |

## Panduan khusus untuk enterprise

Organisasi mapan yang besar membawa skala, banyak tim, warisan mendalam, dan
overhead manajemen perubahan berat. Sesuaikan peta jalan sebagaimana mestinya.

- **Federasikan, jangan pusatkan segalanya.** Satu tim pusat tak dapat melayani
  ratusan tim produk. Pakai tim platform untuk menyediakan jalan beraspal dan tim
  pemungkin untuk membimbing, sementara tim produk mempertahankan kepemilikan.
  (Lihat Team Topologies.)
- **Hormati Hukum Conway.** Arsitektur Anda akan mencerminkan bagan organisasi Anda.
  Jika Anda menginginkan layanan terpisah, Anda butuh tim terpisah yang berdaya;
  reorganisasi dengan sengaja alih-alih melawan serat.
- **Perlakukan warisan sebagai portofolio.** Anda tak dapat memodernisasi segalanya.
  Beri peringkat sistem warisan menurut risiko dan nilai bisnis, dan terapkan
  migrasi strangler-fig pada yang sedikit yang penting; bekukan atau hentikan sisanya
  dengan sengaja.
- **Manajemen perubahan adalah kerja nyata.** Pada skala besar, komunikasi, pelatihan,
  dan penyelarasan insentif bukan overhead: mereka adalah transformasinya. Anggarkan
  pemungkinan, komunitas praktik, dan evangelisasi internal secara eksplisit.
- **Waspadai refleks mandat.** Organisasi besar condong ke memo kebijakan. Tahan.
  Mandat tanpa jalan beraspal menghasilkan centang kotak; jalan beraspal tanpa
  mandat menghasilkan adopsi sejati.
- **Selaraskan insentif dan pendanaan.** Geser dari pendanaan proyek ke tim produk
  tahan lama agar perbaikan bertahan melewati tanggal akhir proyek. Hargai hasil,
  bukan keluaran.

## Panduan khusus untuk pemerintah

Organisasi sektor publik menambah siklus pengadaan, gerbang kepatuhan, manajemen
kontraktor, pendanaan multitahun, dan kewajiban transparansi. Ini masukan desain,
bukan dalih.

- **Rancang untuk ATO sejak hari pertama.** Otorisasi untuk beroperasi dan gerbang
  pemantauan berkelanjutan (menurut NIST RMF / 800-37) dapat mendominasi garis waktu.
  Bangun kendali keamanan dan pengumpulan bukti ke dalam jalur lebih awal agar
  kepatuhan kontinu, bukan perebutan terlambat yang memblokir.
- **Beli secara inkremental.** Pengadaan multitahun big-bang melembagakan kegagalan
  big-bang yang diperingatkan buku ini. Pilih kontrak modular, penghargaan lebih
  kecil, dan pernyataan kerja berbasis hasil yang memungkinkan iterasi.
- **Kelola vendor dan integrator sebagai bagian tim.** Banyak rekayasa pemerintah
  disampaikan kontraktor. Tulis jalan beraspal, gerbang kualitas, dan persyaratan
  transparansi ke dalam kontrak, dan pastikan pengetahuan serta kode berpindah ke
  pemerintah untuk menghindari lock-in dan risiko bus-factor.
- **Rencanakan di sekitar siklus pendanaan.** Apropriasi multitahun dan tahunan
  membatasi apa yang dapat Anda komitmenkan. Urutkan kerja agar tiap kenaikan
  terdanai menyampaikan nilai mandiri dan tidak mendamparkan Anda di tengah
  transformasi jika pendanaan bergeser.
- **Aksesibilitas dan bahasa sederhana adalah kewajiban hukum.** Section 508, ADA,
  WCAG, dan mandat bahasa sederhana adalah persyaratan, bukan peningkatan. Tanamkan
  pemeriksaan aksesibilitas ke jalur dan tinjauan konten ke alur kerja.
- **Transparansi adalah fitur.** FOIA, mandat sumber terbuka ("public money, public
  code"), dan standar layanan terbit berarti kerja Anda tunduk pada pengawasan
  publik. Rancang untuknya: catatan jelas, terbuka di mana sesuai, dan data kinerja
  terbit yang jujur.
- **Ikuti pola sektor publik yang terbukti.** U.S. Digital Services Playbook,
  GOV.UK Service Standard, dan USWDS mengodekan pelajaran yang diperoleh susah payah;
  adopsi alih-alih menciptakan ulang.

## Mengukur keberhasilan adopsi

Ukur baik indikator *utama* (sinyal dini bahwa perubahan mengakar) maupun indikator
*tertinggal* (hasil yang akhirnya Anda pedulikan). Perhatikan tren, bukan satu
pembacaan, dan jangan pernah biarkan metrik menjadi target untuk dimainkan.

| Jenis | Indikator | Apa yang diceritakannya |
|---|---|---|
| Utama | Jumlah tim di jalan beraspal | Seberapa cepat adopsi menyebar |
| Utama | Cakupan gerbang jalur (tes, SAST, a11y) | Seberapa tertanam kualitas/keamanan |
| Utama | Skor survei pengalaman developer | Apakah jalan beraspal benar-benar membantu |
| Utama | Persentase keputusan yang dicatat sebagai ADR | Apakah budaya menulis/belajar nyata |
| Tertinggal | Frekuensi deployment (DORA) | Throughput penyampaian |
| Tertinggal | Lead time untuk perubahan (DORA) | Kecepatan dari commit ke produksi |
| Tertinggal | Laju kegagalan perubahan (DORA) | Kualitas proses penyampaian |
| Tertinggal | Waktu memulihkan layanan (DORA) | Ketahanan operasional |
| Tertinggal | Tren frekuensi dan keparahan insiden | Perbaikan keandalan seiring waktu |
| Tertinggal | Temuan audit / kegagalan kendali | Postur kepatuhan |
| Tertinggal | Retensi dan pergantian | Apakah budaya membaik |

Empat metrik DORA adalah ukuran hasil lintas industri yang paling tervalidasi untuk
penyampaian; perlakukan perbaikan di keempatnya sekaligus sebagai sinyal utama, dan
jaga dari memperbaiki satu dengan mengorbankan yang lain.

## Mode kegagalan umum dan cara menghindarinya

| Mode kegagalan | Seperti apa wujudnya | Cara menghindarinya |
|---|---|---|
| **Peluncuran big-bang** | Mengubah segalanya untuk semua orang sekaligus; program runtuh oleh bobotnya sendiri. | Urutkan menurut nyeri dan kesiapan; pilot, buktikan, lalu skalakan. |
| **Mandat tanpa jalan beraspal** | Kebijakan mewajibkan cara baru, tetapi cara baru lebih lambat; tim patuh di atas kertas dan menghindarinya. | Bangun jalan yang lebih mudah dan lebih baik *dulu*; peroleh adopsi atas merit. |
| **Memuja kerangka** | Menyalin SAFe, model Spotify, atau struktur organisasi lain tanpa konteks mereka. | Mulai dari nyeri dan prinsip Anda sendiri; adaptasi, jangan transplantasi. |
| **Mengukur aktivitas, bukan hasil** | Merayakan pelatihan selesai dan kotak tercentang sementara penyampaian dan keandalan tak bergerak. | Instrumentasi hasil (DORA, insiden, nilai pengguna) sejak awal. |
| **Transformasi mendahulukan perkakas** | Membeli platform dan mengharapkan budaya mengikuti. | Pimpin dengan praktik dan jalan beraspal; perkakas melayani mereka, bukan sebaliknya. |
| **Kehilangan sponsor** | Juara eksekutif pergi atau melepaskan diri; program macet. | Lembagakan perubahan dalam tata kelola normal; bangun koalisi, bukan titik kegagalan tunggal. |
| **Metrik kesombongan dan pengakal-akalan** | Angka cakupan atau velositas naik sementara kualitas turun. | Pakai metrik sebagai sinyal dengan ukuran penyeimbang; jangan pernah sebagai satu-satunya target. |
| **Merebus lautan pada warisan** | Mencoba memodernisasi segalanya, tidak menyampaikan apa pun. | Beri peringkat menurut risiko dan nilai; cekik yang kritis sedikit, bekukan sisanya. |
| **Kelelahan transformasi** | Perubahan tak berujung tanpa imbalan terlihat; tim melepaskan diri. | Kirim kemenangan dini; lindungi kecepatan berkelanjutan; biarkan program berakhir dan menjadi kerja normal. |
| **Mengabaikan bagan organisasi** | Arsitektur baru melawan struktur tim yang ada. | Terapkan manuver Conway terbalik: bentuk tim sesuai arsitektur yang Anda inginkan. |

## Versi tersingkat

Jika Anda tidak mengingat apa pun lagi dari lampiran ini:

1. Temukan nyeri terbesar dan perbaiki dengan tim yang bersedia.
2. Ubah perbaikan itu menjadi jalan beraspal yang benar-benar lebih mudah daripada cara lama.
3. Ukur hasilnya, tunjukkan kemenangan, dan pakai untuk mendanai langkah berikutnya.
4. Ulangi, melebarkan lingkaran, sampai jalan beraspal sekadar cara Anda bekerja.
5. Pertahankan sponsor, terus ukur, dan jangan pernah big-bang.

Lihat **bab 12.4** untuk model kematangan yang menjangkarkan penilaian, dan
**bab 12.2** untuk daftar periksa peluncuran, tinjauan, dan audit yang
mengoperasionalkan tiap langkah.
