# 12.2 Daftar periksa

Daftar periksa ini adalah rujukan cepat praktis yang siap pakai. Salin daftar periksa mana pun ke templat pull request, halaman wiki, tiket, atau agenda rapat tinjauan, dan sesuaikan butirnya dengan konteks Anda. Perlakukan setiap butir sebagai sesuatu yang dapat diverifikasi seseorang dan dijawab ya atau tidak. Daftar periksa adalah alat bantu ingatan dan standar bersama, bukan pengganti penilaian; hapus butir yang tidak berlaku dan tambahkan butir yang dibutuhkan domain Anda.

Panduan agar dipakai dengan baik:

- Jaga daftar periksa cukup pendek agar orang benar-benar menyelesaikannya. Jika daftar periksa rutin dilewati, ia terlalu panjang atau terlalu umum.
- Otomatiskan butir apa pun yang dapat diverifikasi mesin (format, tes, pemindaian) agar manusia menghabiskan perhatian pada butir penilaian.
- Beri versi pada daftar periksa Anda dan tinjau secara berkala. Daftar periksa yang tak pernah berubah kemungkinan tidak dipakai.
- Bedakan butir pemblokir dari butir saran bila perbedaan itu penting bagi proses Anda.

## Daftar periksa tinjauan kode

Untuk peninjau yang memeriksa perubahan orang lain.

- [ ] Perubahan melakukan apa yang dikatakan deskripsi dan tiket terkaitnya.
- [ ] Cakupan terfokus pada satu kepentingan logis; perubahan yang tidak terkait dipisahkan.
- [ ] Desain sesuai dengan arsitektur yang ada dan tidak memperkenalkan kopling yang sebenarnya mudah dihindari.
- [ ] Kasus tepi, jalur galat, dan mode kegagalan ditangani, bukan hanya jalur bahagia.
- [ ] Tes ada, bermakna, dan akan gagal jika perilaku mengalami regresi.
- [ ] Penamaan, struktur, dan komentar membuat kode dapat dipahami pembaca di masa depan.
- [ ] Tidak ada rahasia, kredensial, token, atau data pribadi yang di-commit.
- [ ] Masukan sensitif keamanan divalidasi, di-encode, atau diparameterisasi dengan tepat.
- [ ] Antarmuka publik, kontrak, dan kompatibilitas mundur dipertahankan atau diberi versi dengan sengaja.
- [ ] Logging, metrik, dan pelaporan galat memadai untuk mengoperasikan perubahan di produksi.
- [ ] Dokumentasi, runbook, dan konfigurasi diperbarui agar sesuai dengan perubahan.
- [ ] Umpan balik dipisahkan menjadi isu pemblokir versus saran, dan dirumuskan tentang kodenya.

## Daftar periksa penulis pull request

Untuk penulis sebelum meminta tinjauan.

- [ ] PR cukup kecil dan terfokus untuk ditinjau dengan cermat dalam satu kali duduk.
- [ ] Deskripsi menyatakan apa yang berubah, mengapa, dan bagaimana diverifikasi.
- [ ] Tiket, isu, atau dokumen desain terkait memberi peninjau konteks yang diperlukan.
- [ ] Semua pemeriksaan otomatis lulus secara lokal atau di CI (build, lint, format, tes, pemindaian).
- [ ] Perilaku baru dan yang berubah tercakup oleh tes.
- [ ] Refactor mekanis dipisahkan dari perubahan perilaku.
- [ ] Tinjauan diri selesai: Anda telah membaca diff Anda sendiri baris demi baris.
- [ ] Tidak ada kode debug, blok yang dikomentari, rahasia, atau berkas tersasar yang tersisa.
- [ ] Migrasi basis data, feature flag, dan perubahan konfigurasi didokumentasikan dan dapat dibalik.
- [ ] Perubahan yang memutus kompatibilitas ditandai eksplisit dengan jalur migrasi.
- [ ] Tangkapan layar, rekaman, atau contoh keluaran disertakan di mana membantu tinjauan.
- [ ] Peninjau yang tepat dan penyetuju berbasis peran yang diperlukan diminta.

## Definition of Done

Standar bersama yang harus dipenuhi butir kerja sebelum dianggap selesai.

- [ ] Kriteria penerimaan dalam tiket semuanya terpenuhi dan dapat didemonstrasikan.
- [ ] Kode ditinjau sejawat dan disetujui oleh peninjau yang diperlukan.
- [ ] Tes otomatis ditulis, lulus, dan digabung bersama perubahan.
- [ ] Kode digabung ke mainline dan di-deploy dengan bersih melalui jalur.
- [ ] Tidak ada cacat diketahui pada ambang keparahan yang disepakati yang masih terbuka.
- [ ] Dokumentasi, teks bantuan, dan runbook diperbarui.
- [ ] Observabilitas tersedia: log, metrik, dan peringatan yang relevan ada.
- [ ] Implikasi keamanan dan privasi telah dipertimbangkan dan ditangani.
- [ ] Persyaratan aksesibilitas untuk perubahan terpenuhi di mana menghadap pengguna.
- [ ] Feature flag dikonfigurasi dan rencana peluncuran disepakati.
- [ ] Pemilik produk atau pemangku kepentingan telah menerima hasilnya.
- [ ] Kerja lanjutan apa pun dicatat sebagai tiket terlacak, tidak dibiarkan implisit.

## Kesiapan peluncuran produksi / go-live

Sebelum mengirim perubahan signifikan atau layanan baru ke produksi.

- [ ] Rencana peluncuran didokumentasikan, termasuk langkah bertahap atau canary dan kriteria keberhasilan.
- [ ] Rencana rollback didokumentasikan, diuji, dan dapat dijalankan dengan cepat.
- [ ] Pengujian kapasitas dan beban menunjukkan sistem memenuhi permintaan yang diharapkan dan puncak.
- [ ] Pemantauan, dasbor, dan peringatan aktif dan divalidasi sebelum peluncuran.
- [ ] Cakupan on-call dijadwalkan dan para penanggap mengenal sistem.
- [ ] Runbook ada untuk skenario kegagalan dan operasional yang paling mungkin.
- [ ] Dependensi, integrasi, dan pihak ketiga dikonfirmasi siap dan batas laju dipahami.
- [ ] Tinjauan keamanan dan persetujuan yang diperlukan selesai.
- [ ] Migrasi data, jika ada, diuji ujung-ke-ujung dengan pembatalan terverifikasi.
- [ ] Feature flag memungkinkan menonaktifkan perubahan tanpa redeploy.
- [ ] Persetujuan hukum, privasi, dan kepatuhan diperoleh di mana diperlukan.
- [ ] Rencana komunikasi mencakup pemangku kepentingan, dukungan, dan pelanggan.
- [ ] Keputusan go/no-go dibuat oleh pemilik bernama terhadap kriteria eksplisit.

## Daftar periksa tinjauan keamanan / model ancaman

Untuk menilai postur keamanan suatu perubahan atau sistem.

- [ ] Batas kepercayaan dan aliran data diidentifikasi dan didokumentasikan.
- [ ] Autentikasi ditegakkan pada setiap titik masuk yang membutuhkannya.
- [ ] Pemeriksaan otorisasi menegakkan hak istimewa paling sedikit untuk setiap tindakan dan sumber daya.
- [ ] Semua masukan eksternal divalidasi, dan keluaran di-encode untuk tujuannya.
- [ ] Rahasia disimpan di vault terkelola, tidak pernah di kode atau konfigurasi, dan dapat dirotasi.
- [ ] Data dienkripsi dalam transit dan saat diam sesuai tuntutan klasifikasi.
- [ ] Dependensi dipindai untuk kerentanan yang diketahui dan dijaga mutakhir.
- [ ] Risiko injeksi, deserialisasi, dan SSRF dimitigasi untuk masukan tidak tepercaya.
- [ ] Peristiwa relevan keamanan dicatat tanpa merekam data sensitif.
- [ ] Pembatasan laju, kuota, dan perlindungan penyalahgunaan menjaga endpoint yang terekspos.
- [ ] Pesan galat tidak membocorkan stack trace, internal, atau detail sensitif.
- [ ] Ancaman yang diidentifikasi melalui STRIDE atau sejenisnya dicatat dengan mitigasi atau risiko yang diterima.
- [ ] Pengujian keamanan (SAST, DAST, atau uji penetrasi) direncanakan atau selesai.

## Daftar periksa privasi dan perlindungan data (gaya DPIA)

Untuk pemrosesan yang melibatkan data pribadi atau sensitif.

- [ ] Data pribadi yang dikumpulkan diinventarisasi, diklasifikasikan, dan diminimalkan hingga yang dibutuhkan.
- [ ] Dasar hukum atau otoritas untuk setiap tujuan pemrosesan didokumentasikan.
- [ ] Pembatasan tujuan ditegakkan: data dipakai hanya untuk tujuan yang dinyatakan.
- [ ] Periode retensi didefinisikan dan penghapusan atau anonimisasi diotomatisasi.
- [ ] Hak subjek data (akses, koreksi, penghapusan, portabilitas) dapat dipenuhi.
- [ ] Persetujuan, di mana diandalkan, diberikan secara bebas, spesifik, dan dapat dicabut.
- [ ] Pihak ketiga dan prosesor terikat oleh ketentuan perlindungan data yang memadai.
- [ ] Transfer lintas batas punya mekanisme transfer hukum yang sesuai.
- [ ] Akses ke data pribadi dibatasi, dicatat, dan ditinjau.
- [ ] Risiko privasi terhadap individu dinilai dan dimitigasi atau dieskalasi.
- [ ] Proses deteksi dan pemberitahuan pembobolan data didefinisikan.
- [ ] Pilihan privasi sejak desain dan bawaan didokumentasikan untuk fitur.
- [ ] Petugas perlindungan data atau peninjau privasi telah menyetujui di mana diperlukan.

## Daftar periksa aksesibilitas (WCAG)

Untuk antarmuka yang menghadap pengguna, selaras dengan prinsip WCAG.

- [ ] Semua konten dapat dijangkau dan dioperasikan hanya dengan papan ketik.
- [ ] Urutan fokus logis dan indikator fokus yang terlihat ada.
- [ ] Kontras warna teks memenuhi rasio target (biasanya 4,5:1 untuk teks isi).
- [ ] Gambar dan konten non-teks punya teks alternatif yang bermakna.
- [ ] Kolom formulir punya label terkait dan pesan galat yang jelas.
- [ ] Judul, landmark, dan struktur ditandai secara semantik.
- [ ] Komponen interaktif mengekspos nama, peran, dan status yang benar ke teknologi bantu.
- [ ] Konten mengalir ulang dan tetap dapat dipakai pada zoom 200% dan di layar kecil.
- [ ] Batas waktu dapat disesuaikan, dan gerakan atau konten yang diputar otomatis dapat dijeda.
- [ ] Warna bukan satu-satunya cara menyampaikan informasi.
- [ ] Media punya teks sulih suara (caption) dan, bila perlu, transkrip atau deskripsi audio.
- [ ] Antarmuka diuji dengan pembaca layar dan perkakas aksesibilitas otomatis.

## Daftar periksa tinjauan desain API

Sebelum menerbitkan atau mengubah API.

- [ ] Penamaan sumber daya dan operasi konsisten dan dapat diprediksi.
- [ ] Kontrak dispesifikasikan dalam skema yang dapat dibaca mesin (misalnya OpenAPI).
- [ ] Strategi versi didefinisikan dan kompatibilitas mundur dipertahankan atau dikelola.
- [ ] Paginasi, pemfilteran, dan pengurutan mengikuti konvensi yang konsisten.
- [ ] Respons galat memakai struktur, kode, dan pesan yang dapat ditindaklanjuti secara konsisten.
- [ ] Autentikasi dan otorisasi dispesifikasikan untuk setiap operasi.
- [ ] Validasi masukan dan batas ukuran didefinisikan dan ditegakkan.
- [ ] Idempotensi didefinisikan untuk operasi di mana pengulangan diharapkan.
- [ ] Batas laju, kuota, dan perilaku throttling didokumentasikan.
- [ ] Timeout, retry, dan semantik kegagalan jelas bagi klien.
- [ ] Paparan data sensitif dalam respons diminimalkan dan dibenarkan.
- [ ] Dokumentasi mencakup contoh untuk setiap operasi dan kasus galat.
- [ ] Kebijakan deprekasi dan garis waktu penghentian didefinisikan.

## Daftar periksa tinjauan keputusan arsitektur (ADR)

Untuk meninjau catatan keputusan arsitektur yang diusulkan.

- [ ] Konteks dan masalah yang diselesaikan dinyatakan dengan jelas.
- [ ] Keputusan dinyatakan tanpa ambiguitas sebagai satu pilihan.
- [ ] Setidaknya dua alternatif realistis dipertimbangkan dan dibandingkan.
- [ ] Konsekuensi, baik positif maupun negatif, didokumentasikan.
- [ ] Dampak non-fungsional (kinerja, keamanan, biaya, kemampuan dioperasikan) ditangani.
- [ ] Keputusan selaras dengan prinsip dan ADR sebelumnya, atau menggantikannya secara eksplisit.
- [ ] Tim dan pemangku kepentingan terdampak dikonsultasikan.
- [ ] Reversibilitas dan biaya perubahan dinilai.
- [ ] Asumsi dan kendala dibuat eksplisit.
- [ ] Status (diusulkan, diterima, digantikan) ditetapkan dan diberi tanggal.
- [ ] Keputusan dapat ditemukan dan ditautkan dari sistem yang relevan.
- [ ] Tindakan lanjutan atau migrasi apa pun dicatat sebagai kerja terlacak.

## Daftar periksa respons insiden

Selama insiden produksi aktif.

- [ ] Umumkan insiden dan tugaskan satu komandan insiden.
- [ ] Nilai dan komunikasikan keparahan, cakupan, dan dampak pelanggan.
- [ ] Buka kanal komunikasi khusus dan catatan insiden.
- [ ] Tugaskan peran jelas: komandan, pemimpin komunikasi, dan pemimpin operasi.
- [ ] Utamakan mitigasi dan pemulihan layanan di atas analisis akar masalah.
- [ ] Posting pembaruan status berkala kepada pemangku kepentingan pada irama tetap.
- [ ] Catat linimasa peristiwa, tindakan, dan keputusan seiring terjadi.
- [ ] Eskalasikan ke penanggap tambahan atau vendor bila perlu.
- [ ] Beri tahu hukum, keamanan, dan kepatuhan jika data atau regulasi terlibat.
- [ ] Verifikasi perbaikan dan pastikan sistem telah pulih sepenuhnya.
- [ ] Tutup insiden secara formal dan komunikasikan penyelesaiannya.
- [ ] Jadwalkan postmortem tanpa menyalahkan sebelum orang-orang bubar.

## Daftar periksa postmortem

Untuk tinjauan retrospektif setelah insiden.

- [ ] Tinjauan dilakukan tanpa menyalahkan dan berfokus pada sistem dan faktor penyumbang.
- [ ] Linimasa insiden yang faktual dan berstempel waktu didokumentasikan.
- [ ] Dampak pelanggan dan bisnis dikuantifikasi (durasi, cakupan, biaya).
- [ ] Deteksi dianalisis: bagaimana dan kapan masalah disadari.
- [ ] Respons dianalisis: apa yang membantu dan apa yang memperlambat pemulihan.
- [ ] Penyebab penyumbang diidentifikasi, bukan hanya satu akar masalah.
- [ ] Apa yang berjalan baik dicatat, begitu pula apa yang berjalan salah.
- [ ] Butir tindakan spesifik, ditugaskan ke pemilik, dan punya tanggal jatuh tempo.
- [ ] Butir tindakan menangani pencegahan, deteksi, dan mitigasi.
- [ ] Butir lanjutan dilacak sampai selesai di backlog normal.
- [ ] Postmortem dibagikan luas agar orang lain dapat belajar darinya.
- [ ] Pola sistemik lintas insiden ditinjau secara berkala.

## Daftar periksa kesiapan on-call

Sebelum seseorang mengambil giliran on-call.

- [ ] Penanggap punya akses ke semua sistem, dasbor, dan perkakas yang dibutuhkan.
- [ ] Peringatan menjangkau penanggap dengan andal dan diuji.
- [ ] Jalur eskalasi dan kontak on-call sekunder diketahui dan terkini.
- [ ] Runbook ada untuk peringatan paling umum dan paling parah.
- [ ] Penanggap telah menyelesaikan onboarding atau shadowing untuk sistem ini.
- [ ] Perubahan terbaru, insiden berjalan, dan isu yang diketahui diserahterimakan.
- [ ] Ambang peringatan disetel untuk meminimalkan derau dan panggilan palsu.
- [ ] Penanggap tahu cara mengumumkan insiden dan menjangkau komandan.
- [ ] Akses ke produksi dimungkinkan dari lingkungan kerja penanggap.
- [ ] Kanal komunikasi dan kontak pemangku kepentingan didokumentasikan.
- [ ] Jadwal on-call diterbitkan dan cakupan tidak memiliki celah.
- [ ] Kompensasi, ekspektasi, dan batas beban kerja untuk on-call jelas.

## Daftar periksa definisi SLO

Saat mendefinisikan service level objective.

- [ ] Perjalanan pengguna atau kapabilitas yang dilindungi SLO diidentifikasi dengan jelas.
- [ ] Service level indicator (SLI) didefinisikan sebagai besaran yang jelas dan terukur.
- [ ] SLI diukur dari sudut pandang pengguna bila memungkinkan.
- [ ] Target objective ditetapkan pada tingkat yang benar-benar dibutuhkan pengguna, bukan 100%.
- [ ] Jendela pengukuran (misalnya 28 hari bergulir) dispesifikasikan.
- [ ] Anggaran galat yang diturunkan dari target dihitung dan dipahami.
- [ ] Kebijakan mendefinisikan apa yang terjadi ketika anggaran galat habis.
- [ ] Sumber data untuk SLI andal dan terinstrumentasi.
- [ ] Peringatan terikat pada laju pembakaran, bukan hanya pelanggaran ambang.
- [ ] Pemilik dan pemangku kepentingan menyepakati SLO realistis dan bermakna.
- [ ] SLO didokumentasikan dan terlihat di dasbor.
- [ ] Jadwal ada untuk meninjau dan merevisi SLO seiring layanan berevolusi.

## Daftar periksa jalur CI/CD

Untuk jalur continuous integration dan delivery.

- [ ] Setiap commit memicu build dan pelaksanaan tes otomatis.
- [ ] Jalur gagal cepat dan melaporkan hasil dengan jelas kepada penulis.
- [ ] Linting, format, dan analisis statis berjalan otomatis.
- [ ] Tes unit, integrasi, dan ujung-ke-ujung yang relevan berjalan di jalur.
- [ ] Pemindaian keamanan dan dependensi berjalan pada setiap build.
- [ ] Artefak build diberi versi, tak dapat diubah, dan disimpan di registri.
- [ ] Rahasia disuntikkan dengan aman dan tidak pernah dicetak di log.
- [ ] Deployment otomatis dan dapat diulang lintas lingkungan.
- [ ] Strategi deployment (canary, blue-green, rolling) didefinisikan dan dipakai.
- [ ] Rollback otomatis atau satu tindakan terdokumentasi.
- [ ] Izin jalur mengikuti hak istimewa paling sedikit dan dapat diaudit.
- [ ] Konfigurasi jalur disimpan di kendali versi sebagai kode.
- [ ] Provenans build dan software bill of materials dihasilkan di mana diperlukan.

## Daftar periksa tinjauan infrastruktur sebagai kode

Untuk meninjau infrastruktur yang didefinisikan sebagai kode.

- [ ] Perubahan diekspresikan sepenuhnya dalam kode dan diterapkan melalui jalur.
- [ ] Rencana atau keluaran dry-run ditinjau sebelum diterapkan.
- [ ] State disimpan dengan aman dengan penguncian untuk mencegah perubahan bersamaan.
- [ ] Sumber daya mengikuti konvensi penamaan, penandaan, dan kepemilikan.
- [ ] Peran dan kebijakan IAM hak istimewa paling sedikit dipakai, tanpa wildcard di mana dapat dihindari.
- [ ] Paparan jaringan diminimalkan; tidak ada akses publik yang tak disengaja.
- [ ] Rahasia dan nilai sensitif dirujuk dari vault, tidak ditulis keras.
- [ ] Enkripsi diaktifkan untuk penyimpanan, basis data, dan transit.
- [ ] Perubahan idempoten dan aman diterapkan ulang.
- [ ] Radius ledakan dipahami; perubahan destruktif ditandai.
- [ ] Dampak biaya dari perubahan dipertimbangkan.
- [ ] Modul dapat dipakai ulang, diberi versi, dan diuji.
- [ ] Deteksi drift tersedia untuk menangkap perubahan di luar jalur.

## Daftar periksa rilis model AI/ML

Sebelum merilis model machine learning ke produksi.

- [ ] Penggunaan yang dimaksudkan, cakupan, dan keterbatasan model didokumentasikan.
- [ ] Provenans data pelatihan dan evaluasi, lisensi, dan persetujuan diverifikasi.
- [ ] Data dan model diberi versi dan dapat direproduksi.
- [ ] Kinerja dievaluasi pada data uji tertahan yang representatif.
- [ ] Keadilan dan bias dinilai di subkelompok yang relevan.
- [ ] Model dievaluasi terhadap petahana atau garis dasar.
- [ ] Mode kegagalan, kasus tepi, dan perilaku di luar distribusi dipahami.
- [ ] Risiko keselamatan, penyalahgunaan, dan keluaran berbahaya dinilai dan dimitigasi.
- [ ] Pemantauan drift, kualitas data, dan degradasi kinerja tersedia.
- [ ] Rollback atau fallback ke model sebelumnya atau jalur berbasis aturan ada.
- [ ] Pengawasan manusia atau banding disediakan untuk keputusan berdampak.
- [ ] Tinjauan privasi mencakup data pelatihan serta masukan dan keluaran inferensi.
- [ ] Kartu model atau dokumentasi setara diterbitkan untuk pemangku kepentingan.

## Daftar periksa kualitas jalur data

Untuk jalur data yang memberi makan analitik atau produk.

- [ ] Skema data sumber divalidasi dan perubahan skema terdeteksi.
- [ ] Ingesti menangani rekaman terlambat, duplikat, dan tak berurutan dengan benar.
- [ ] Pemeriksaan kualitas data (kelengkapan, keunikan, rentang) berjalan otomatis.
- [ ] Rekaman gagal dikarantina dan dimunculkan, tidak dijatuhkan diam-diam.
- [ ] Transformasi diuji dengan masukan representatif dan kasus tepi.
- [ ] Jalur idempoten dan aman dijalankan ulang setelah kegagalan.
- [ ] Kesegaran dan latensi keluaran dipantau terhadap ekspektasi.
- [ ] Lineage didokumentasikan agar konsumen tahu dari mana data berasal.
- [ ] Data pribadi dan sensitif diklasifikasikan, disamarkan, atau dibatasi dengan tepat.
- [ ] Backfill dan pemrosesan ulang didukung dan didokumentasikan.
- [ ] Peringatan memberi tahu pemilik tentang kegagalan dan pelanggaran kualitas.
- [ ] Kebijakan retensi dan penghapusan ditegakkan pada data tersimpan.
- [ ] Konsumen hilir dan SLA didokumentasikan.

## Daftar periksa asupan sumber terbuka dan tinjauan lisensi

Sebelum mengadopsi komponen sumber terbuka.

- [ ] Lisensi komponen diidentifikasi dan ada dalam daftar yang disetujui.
- [ ] Kewajiban lisensi (atribusi, copyleft, pemberitahuan) dipahami dan dipenuhi.
- [ ] Kompatibilitas lisensi dengan model distribusi Anda dikonfirmasi.
- [ ] Proyek aktif dipelihara dan punya komunitas sehat.
- [ ] Kerentanan yang diketahui diperiksa dan versinya mutakhir.
- [ ] Dependensi dan dependensi transitifnya diinventarisasi.
- [ ] Postur keamanan dan riwayat insiden masa lalu ditinjau.
- [ ] Komponen memenuhi kebutuhan nyata tanpa duplikasi signifikan.
- [ ] Biaya keluar dan kemampuan penggantian komponen dipertimbangkan.
- [ ] Komponen dicatat dalam software bill of materials.
- [ ] Pemilik bernama bertanggung jawab melacak pembaruan dan advisori.
- [ ] Kebijakan kontribusi-kembali dan fork internal diikuti jika dimodifikasi.

## Daftar periksa risiko vendor / pihak ketiga

Sebelum mengorientasikan vendor atau layanan eksternal.

- [ ] Kebutuhan bisnis dan data yang akan diakses vendor didefinisikan dengan jelas.
- [ ] Postur keamanan vendor dinilai (sertifikasi, audit, kuesioner).
- [ ] Ketentuan pemrosesan data, kepemilikan, dan penghapusan saat keluar jelas secara kontraktual.
- [ ] Subprosesor dan lokasi data vendor diungkap dan dapat diterima.
- [ ] Kepatuhan terhadap regulasi yang relevan diverifikasi.
- [ ] Komitmen uptime, dukungan, dan SLA didokumentasikan.
- [ ] Kewajiban dan garis waktu pemberitahuan pembobolan ada dalam kontrak.
- [ ] Akses dibatasi pada hak istimewa paling sedikit dan dapat dicabut.
- [ ] Kesinambungan bisnis dan dampak kegagalan vendor dinilai.
- [ ] Rencana keluar dan migrasi data ada untuk menghindari lock-in.
- [ ] Biaya, ketentuan perpanjangan, dan klausul perubahan harga dipahami.
- [ ] Vendor ditambahkan ke register risiko dengan tanggal tinjauan.

## Daftar periksa kesiapan kepatuhan pemerintah (gaya ATO / FedRAMP)

Untuk sistem yang membutuhkan otorisasi formal untuk beroperasi.

- [ ] Batas sistem dan aliran data didefinisikan dan didiagramkan.
- [ ] Data dikategorikan menurut tingkat dampak dan kepekaan.
- [ ] Garis dasar kendali yang berlaku dipilih dan disesuaikan.
- [ ] Rencana keamanan sistem mendokumentasikan bagaimana setiap kendali diimplementasikan.
- [ ] Kendali diimplementasikan, dibuktikan, dan dipetakan ke rencana.
- [ ] Pemantauan berkelanjutan dan pemindaian kerentanan beroperasi.
- [ ] Rencana tindakan dan tonggak melacak temuan terbuka sampai remediasi.
- [ ] Kendali akses, pencatatan audit, dan manajemen identitas memenuhi persyaratan.
- [ ] Enkripsi memakai algoritma yang disetujui dan modul tervalidasi.
- [ ] Rencana respons insiden didokumentasikan dan diuji.
- [ ] Rencana kontingensi dan pemulihan bencana didokumentasikan dan diuji.
- [ ] Penilaian atau audit independen atas kendali selesai.
- [ ] Pejabat pemberi otorisasi memiliki penilaian risiko yang dibutuhkan untuk memberikan otorisasi.
- [ ] Pemicu otorisasi ulang dan irama otorisasi berkelanjutan didefinisikan.
