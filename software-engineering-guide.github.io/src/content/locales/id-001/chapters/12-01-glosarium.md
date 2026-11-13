# 12.1 Glosarium

Glosarium ini mendefinisikan istilah dan akronim yang dipakai di seluruh buku
panduan. Entri dikelompokkan menurut abjad. Istilah dipertahankan dalam bentuk
aslinya (kebanyakan istilah teknis baku dipakai apa adanya dalam bahasa
Indonesia), diurutkan menurut huruf pertamanya, sementara definisinya ditulis
dalam bahasa Indonesia. Di mana entri punya akronim umum, ia ditampilkan dalam
tanda kurung. Definisi sengaja ringkas; rujuk bab yang relevan untuk pembahasan
lebih lengkap.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: Model otorisasi yang memberi akses berdasarkan atribut yang dievaluasi dari pengguna, sumber daya, tindakan, dan lingkungan (misalnya departemen, tingkat izin, waktu dalam sehari) alih-alih peran tetap. Ia menawarkan kendali berbutir halus yang digerakkan kebijakan dengan harga kerumitan lebih besar daripada RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: Praktik merancang dan membangun perangkat lunak agar penyandang disabilitas dapat mempersepsi, memahami, menavigasi, dan berinteraksi dengannya. Numeronim "a11y" menyingkat 11 huruf di antara "a" dan "y."

**ADR (Architecture Decision Record)**: Dokumen pendek berversi yang menangkap satu keputusan arsitektural atau teknis signifikan, konteksnya, opsi yang dipertimbangkan, dan konsekuensinya. ADR menciptakan riwayat tahan lama yang dapat ditinjau tentang mengapa suatu sistem seperti adanya.

**Aggregate**: Dalam Domain-Driven Design, gugus objek domain yang diperlakukan sebagai satu kesatuan untuk perubahan data, dengan satu entitas bertindak sebagai akar aggregate yang menegakkan invarian. Aggregate mendefinisikan batas konsistensi dan transaksi.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)**: Kontrak terdefinisi yang dipakai satu perangkat lunak untuk meminta layanan atau data dari yang lain. API yang dirancang baik menyembunyikan detail implementasi dan menyediakan antarmuka stabil berversi.

**API-first**: Pendekatan pengembangan di mana kontrak API dirancang dan disepakati sebelum implementasi, agar konsumen dan penyedia dapat bekerja paralel terhadap spesifikasi bersama.

**arc42**: Struktur terbuka berbasis templat untuk mendokumentasikan arsitektur perangkat lunak, diorganisasi menjadi dua belas bagian yang mencakup konteks, kendala, blok bangunan, runtime, deployment, dan keputusan.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Spesifikasi W3C yang mendefinisikan peran, status, dan properti yang membuat komponen web dinamis dan khusus dapat dipahami teknologi bantu seperti pembaca layar.

**ASR (Architecturally Significant Requirement)**: Persyaratan yang punya efek terukur dan luas pada arsitektur, seperti kendala kinerja, ketersediaan, keamanan, atau regulasi. ASR menggerakkan keputusan desain paling berdampak.

**ASVS (Application Security Verification Standard)**: Standar OWASP yang menyediakan daftar periksa berjenjang persyaratan dan tes keamanan untuk merancang, membangun, dan memverifikasi aplikasi aman.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)**: Penyesuaian otomatis jumlah instans komputasi yang berjalan (atau ukurannya) sebagai respons terhadap beban, agar kapasitas mengikuti permintaan tanpa intervensi manual. Ia melengkapi, tetapi tidak menggantikan, perencanaan kapasitas yang disengaja.

**[Availability](https://en.wikipedia.org/wiki/Availability)**: Proporsi waktu sistem beroperasi dan mampu melayani permintaan, sering diekspresikan dalam "sembilan" (misalnya 99,9%). Ia target keandalan inti yang dikodifikasi dalam SLO dan SLA.

## B

**Backpressure**: Mekanisme kendali aliran di mana komponen di bawah beban memberi sinyal produsen hulu untuk melambat, mencegah antrean tak terbatas dan kegagalan berkaskade. Ia sentral bagi sistem streaming dan berbasis pesan yang andal.

**[BDD (Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: Praktik kolaboratif yang mengekspresikan persyaratan sebagai contoh perilaku konkret yang dapat dibaca manusia (sering dalam bentuk Given/When/Then) yang sekaligus menjadi tes penerimaan otomatis.

**BFF (Backend for Frontend)**: Pola arsitektural di mana layanan backend khusus dibangun untuk frontend atau jenis klien tertentu, menyesuaikan pembentukan dan agregasi data dengan kebutuhan klien itu.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: Perkakas, proses, dan praktik untuk mengumpulkan, mengintegrasikan, dan menganalisis data bisnis guna mendukung pelaporan, dasbor, dan pengambilan keputusan.

**Blameless postmortem**: Tinjauan insiden yang berfokus pada sebab sistemik dan pembelajaran alih-alih kesalahan individu, dengan premis bahwa orang bertindak masuk akal mengingat informasi dan insentif yang mereka punya.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)**: Strategi rilis yang menjalankan dua lingkungan produksi identik ("blue" dan "green"), mengarahkan lalu lintas ke satu sementara yang lain diperbarui, memungkinkan peralihan dan rollback nyaris seketika.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Fungsi peringkat yang dipakai luas untuk pencarian teks penuh yang menilai seberapa baik dokumen cocok dengan query memakai frekuensi istilah, frekuensi dokumen terbalik, dan panjang dokumen. Ia bawaan peringkat leksikal di banyak mesin pencari.

**Bounded context**: Dalam Domain-Driven Design, batas eksplisit di dalam mana model domain tertentu dan ubiquitous language-nya berlaku konsisten. Ia mencegah konsep dicampuradukkan di bagian berbeda sistem besar.

**Build cache**: Penyimpanan keluaran build yang sebelumnya dihitung, dikunci oleh masukan yang menghasilkannya, agar kerja yang tak berubah dipakai ulang alih-alih dibangun ulang. Build cache jarak jauh bersama memungkinkan seluruh tim dan CI-nya memakai ulang hasil satu sama lain.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)**: Jumlah orang yang harus hilang (secara kiasan "ditabrak bus") sebelum proyek macet karena kekurangan pengetahuan esensial. Bus factor rendah menandakan keahlian terkonsentrasi tak terdokumentasi dan risiko organisasi.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: Aturan yang dipakai cache untuk memutuskan entri mana yang dibuang ketika penuh, seperti least recently used (LRU) atau least frequently used (LFU). Kebijakan membentuk hit rate dan, bersamanya, nilai cache.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)**: Masalah menghapus atau memperbarui data ter-cache setelah sumber mendasarnya berubah, agar pembaca tidak melihat nilai usang. Ia terkenal sebagai salah satu masalah tersulit dalam komputasi.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)**: Mode kegagalan di mana banyak klien meleset dari cache untuk kunci yang sama sekaligus dan semuanya menghantam origin bersamaan, membebaninya. Penggabungan permintaan dan kedaluwarsa bertahap mencegahnya. Juga disebut thundering herd.

**Canary release**: Teknik deployment yang memaparkan versi baru ke subset kecil pengguna atau lalu lintas lebih dulu, memantau masalah, lalu memperluas peluncuran secara progresif jika metrik tetap sehat.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)**: Prinsip yang menyatakan bahwa penyimpanan data terdistribusi dapat menjamin paling banyak dua dari Consistency, Availability, dan Partition tolerance secara bersamaan; karena partisi tak terhindarkan, perancang secara efektif menukar konsistensi dengan ketersediaan selama partisi.

**[Model C4](https://en.wikipedia.org/wiki/C4_model)**: Pendekatan ringan untuk memvisualisasikan arsitektur perangkat lunak pada empat tingkat abstraksi: System Context, Containers, Components, dan Code.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: Continuous Delivery menjaga perangkat lunak dalam keadaan dapat dirilis agar dapat di-deploy kapan saja dengan persetujuan manual; Continuous Deployment secara otomatis merilis setiap perubahan yang lulus jalur.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Jaringan server tepi yang terdistribusi geografis yang men-cache dan menyajikan konten dekat pengguna, memangkas latensi dan meringankan infrastruktur origin.

**Chain-of-thought prompting**: Teknik prompting yang meminta model bahasa menelusuri langkah penalaran antara sebelum memberi jawaban akhir, memperbaiki kinerja pada masalah multilangkah dengan harga keluaran lebih panjang dan lambat.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: Praktik sering menggabungkan perubahan developer ke mainline bersama, setiap merge divalidasi oleh build dan rangkaian tes otomatis untuk mendeteksi masalah integrasi sejak dini.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Jalur gabungan Continuous Integration dan Continuous Delivery/Deployment yang mengotomatiskan membangun, menguji, dan merilis perangkat lunak.

**CMMC (Cybersecurity Maturity Model Certification)**: Program Departemen Pertahanan AS yang mensertifikasi kematangan keamanan siber kontraktor yang menangani informasi kontrak federal dan controlled unclassified information.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: Sejauh mana elemen di dalam modul saling terkait dan melayani satu tujuan terdefinisi baik. Kohesi tinggi, berpasangan dengan kopling rendah, adalah ciri khas desain yang dapat dipelihara.

**Context window**: Jumlah teks maksimum, diukur dalam token, yang dapat dipertimbangkan model bahasa sekaligus, mencakup masukan dan keluarannya. Ia anggaran langka yang harus dikelola desain prompt dan konteks dengan sengaja.

**[Hukum Conway](https://en.wikipedia.org/wiki/Conway's_law)**: Pengamatan bahwa struktur sistem cenderung mencerminkan struktur komunikasi organisasi yang membangunnya. "Manuver Conway terbalik" dengan sengaja membentuk tim untuk menghasilkan arsitektur yang diinginkan.

**Core Web Vitals**: Himpunan metrik kinerja web berpusat pengguna yang didefinisikan Google (seperti Largest Contentful Paint, Interaction to Next Paint, dan Cumulative Layout Shift) yang mengukur pemuatan, interaktivitas, dan stabilitas visual.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)**: Biaya ekonomi karena sesuatu belum selesai, diekspresikan sebagai nilai yang hilang per satuan waktu. Membuatnya eksplisit mengubah prioritisasi dari opini menjadi aritmetika, dan mendasari aturan pengurutan seperti weighted shortest job first.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: Tingkat saling ketergantungan antar modul atau layanan. Kopling longgar membatasi efek riak perubahan dan merupakan sasaran sentral arsitektur yang baik.

**CQRS (Command Query Responsibility Segregation)**: Pola yang memisahkan model yang dipakai untuk mengubah state (command) dari model yang dipakai untuk membaca state (query), memungkinkan masing-masing dioptimalkan dan diskalakan secara independen.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Katalog publik kerentanan keamanan yang diungkap, masing-masing diberi pengenal unik agar perkakas dan tim dapat merujuk cacat yang sama tanpa ambiguitas.

**CWV**: Lihat Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Pengujian keamanan yang menyelidiki aplikasi yang berjalan dari luar, tanpa akses ke kode sumber, untuk menemukan kerentanan yang muncul saat runtime.

**Data-ink ratio**: Prinsip dari Edward Tufte yang menyatakan bahwa grafik harus menghabiskan sebagian besar tintanya untuk data itu sendiri dan sedikit untuk hiasan, menghapus garis kisi, batas, dan chartjunk yang tidak menginformasikan.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: Arsitektur data terdesentralisasi dan model operasi yang memperlakukan data sebagai produk milik tim domain, didukung infrastruktur platform layanan mandiri dan tata kelola federasi.

**[Data visualisation](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: Praktik mengodekan data dalam bentuk visual (posisi, panjang, warna, dan sejenisnya) agar pola, perbandingan, dan tren dapat dipersepsi dan keputusan menjadi lebih terinformasi.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: Pendekatan desain perangkat lunak yang memusatkan model pada domain bisnis, memakai ubiquitous language bersama, bounded context, dan blok bangunan seperti entity, value object, dan aggregate.

**Design tokens**: Nilai bernama dan agnostik-platform (warna, jarak, tipografi, dan sejenisnya) yang mengodekan keputusan desain agar dapat dibagikan konsisten lintas design system dan banyak produk.

**DevEx / DevX (Developer Experience)**: Kualitas keseluruhan interaksi harian developer dengan perkakas, platform, dan proses, mencakup gesekan, kecepatan umpan balik, dan beban kognitif.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Budaya dan seperangkat praktik yang menyatukan pengembangan dan operasi perangkat lunak untuk mempersingkat siklus penyampaian, menaikkan frekuensi deployment, dan memperbaiki keandalan lewat otomasi dan kepemilikan bersama.

**DORA (DevOps Research and Assessment)**: Program riset dan empat metrik penyampaian yang dipakai luas (frekuensi deployment, lead time untuk perubahan, laju kegagalan perubahan, dan waktu memulihkan layanan) yang dipakai untuk membandingkan kinerja penyampaian perangkat lunak.

**DPIA (Data Protection Impact Assessment)**: Penilaian terstruktur, diwajibkan di bawah GDPR untuk pemrosesan berisiko tinggi, yang mengidentifikasi dan memitigasi risiko privasi sebelum proyek berlanjut.

**Drift (konfigurasi)**: Penyimpangan bertahap state aktual sistem dari state yang dideklarasikan atau dimaksudkan, umumnya disebabkan perubahan manual; Infrastructure as Code dan GitOps bertujuan mendeteksi dan mengoreksinya.

**Drift (model)**: Dalam machine learning, degradasi kinerja model seiring waktu ketika sifat statistik data masukan (data drift) atau hubungan yang dimodelkan (concept drift) berubah.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**: Strategi, prosedur, dan infrastruktur untuk memulihkan layanan dan data setelah peristiwa disruptif besar, biasanya diatur oleh target RTO dan RPO.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Prinsip desain yang menyatakan bahwa setiap potong pengetahuan harus punya satu representasi otoritatif, mengurangi duplikasi dan risiko pembaruan tak konsisten.

## E

**East-west traffic**: Lalu lintas jaringan antar layanan di dalam sistem atau pusat data, berlawanan dengan lalu lintas north-south antara sistem dan klien eksternal. Service mesh biasanya mengatur lalu lintas east-west.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)**: Menjalankan komputasi dan penyimpanan dekat tempat data dihasilkan atau dikonsumsi alih-alih di lokasi pusat, untuk memangkas latensi dan bandwidth. Content delivery network adalah bentuk awal yang meluas.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: Kemampuan sistem memperoleh dan melepas sumber daya secara otomatis sebagai respons terhadap permintaan yang berubah, agar kapasitas mengikuti beban dengan ketat.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Pola integrasi data yang memuat data mentah ke penyimpanan target lebih dulu dan mentransformasinya di sana, memanfaatkan skala gudang data dan lakehouse modern.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)**: Representasi teks, gambar, atau data lain sebagai vektor numerik padat, diposisikan agar butir serupa berada berdekatan. Embedding menggerakkan pencarian semantik dan vektor serta retrieval-augmented generation.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Standar Eropa yang menspesifikasikan persyaratan aksesibilitas untuk produk dan layanan ICT, dirujuk pengadaan sektor publik di seluruh UE dan selaras dengan WCAG.

**Error budget (anggaran galat)**: Jumlah ketidakandalan yang diizinkan SLO selama suatu periode; ketika habis, tim memprioritaskan kerja keandalan di atas fitur baru. Ia mendamaikan ketegangan antara velositas dan stabilitas.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Pola integrasi data yang mengekstrak data dari sumber, mentransformasinya ke bentuk target, dan memuatnya ke tujuan seperti gudang data.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: Regulasi Uni Eropa yang mengklasifikasikan sistem AI menurut risiko dan memberlakukan kewajiban sesuai, melarang penggunaan tertentu dan mengatur ketat sistem berisiko tinggi.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)**: Model konsistensi dalam sistem terdistribusi di mana replika dapat menyimpang sementara tetapi konvergen ke state yang sama setelah pembaruan berhenti merambat.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)**: Mekanisme untuk mengaktifkan atau menonaktifkan fungsionalitas saat runtime tanpa redeploy, dipakai untuk peluncuran bertahap, eksperimen, dan kendali operasional.

**Feature store**: Sistem terpusat untuk mendefinisikan, menyimpan, dan menyajikan fitur machine-learning terkurasi secara konsisten untuk pelatihan maupun inferensi, mengurangi duplikasi dan training/serving skew.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Program pemerintah AS yang membakukan penilaian keamanan, otorisasi, dan pemantauan berkelanjutan untuk layanan cloud yang dipakai lembaga federal.

**Few-shot prompting**: Memberi model bahasa segelintir contoh terkerjakan dalam prompt untuk mendemonstrasikan tugas dan format keluaran yang diinginkan, berlawanan dengan zero-shot prompting, yang memberi instruksi tanpa contoh.

**FinOps**: Disiplin dan praktik budaya yang membawa akuntabilitas finansial ke belanja cloud yang bervariasi, memberi tim rekayasa, keuangan, dan bisnis kepemilikan bersama atas biaya dan nilai.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Undang-undang AS yang mewajibkan lembaga federal mengimplementasikan, mendokumentasikan, dan memantau program keamanan informasi, dioperasionalkan sebagian besar lewat panduan NIST.

**Flow efficiency (efisiensi aliran)**: Proporsi total lead time yang dihabiskan butir kerja untuk dikerjakan aktif alih-alih menunggu, dihitung sebagai waktu bernilai-tambah dibagi total lead time. Kebanyakan sistem mengejutkan rendahnya, sering di bawah 15 persen.

**Four-eyes principle**: Kendali yang mewajibkan tindakan signifikan ditinjau atau disetujui oleh setidaknya dua orang, mengurangi peluang galat atau penyalahgunaan.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: Teknik pengujian otomatis yang memberi program masukan cacat, acak, atau tak terduga untuk menemukan crash, cacat keamanan, dan cacat kasus tepi.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: Regulasi Uni Eropa yang mengatur pemrosesan data pribadi, memberi individu hak dan memberlakukan kewajiban pada pengendali dan prosesor, dengan penalti signifikan untuk ketidakpatuhan.

**GitOps**: Model operasional yang memakai Git sebagai sumber kebenaran tunggal untuk infrastruktur dan aplikasi deklaratif, dengan otomasi terus-menerus merekonsiliasi sistem hidup ke state yang di-commit.

**Golden path / paved road (jalan beraspal)**: Cara bawaan yang didukung baik dan beropini untuk membangun dan mengirim perangkat lunak dalam organisasi, dirancang untuk menjadikan pilihan aman, patuh, dan andal sebagai yang termudah.

**Golden record**: Dalam master data management, versi tunggal, terekonsiliasi, dan otoritatif dari entitas bisnis (seperti pelanggan) yang dirakit dari banyak sistem sumber lewat aturan pencocokan dan survivorship.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)**: Pendekatan sistem tipe yang membiarkan pengetikan statis dan dinamis hidup berdampingan dalam satu basis kode, agar tipe dapat ditambahkan secara inkremental ke program berketik dinamis. Petunjuk tipe dan pemeriksa tipe opsional adalah contoh umum.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Bahasa query dan runtime untuk API yang memungkinkan klien meminta persis data yang dibutuhkan dalam satu panggilan, memakai skema berketik kuat.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Kerangka remote procedure call berkinerja tinggi dan kontrak-dulu yang memakai HTTP/2 dan, biasanya, Protocol Buffers untuk komunikasi layanan-ke-layanan yang efisien.

## H

**Hermetic build**: Build yang bergantung hanya pada masukan yang dideklarasikan eksplisit dan terisolasi dari lingkungan host, sehingga menghasilkan keluaran sama di mana pun. Hermeticity adalah fondasi build yang dapat direproduksi dan caching yang andal.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: Perangkat keras tahan-rusak yang menghasilkan, menyimpan, dan memakai kunci kriptografi, memberikan perlindungan kunci lebih kuat daripada pendekatan hanya-perangkat-lunak.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Undang-undang AS yang, antara lain, menetapkan persyaratan untuk melindungi informasi kesehatan terlindungi (PHI) dan mengatur penggunaan serta pengungkapannya.

**Horizontal scaling**: Menaikkan kapasitas dengan menambah lebih banyak instans atau node ("scaling out") alih-alih membuat satu node lebih kuat. Ia menopang sebagian besar arsitektur skala besar yang tangguh.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: Praktik mendefinisikan dan menyediakan infrastruktur lewat konfigurasi yang dapat dibaca mesin dan dikendalikan versi alih-alih proses manual, memungkinkan keberulangan dan tinjauan.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**: Kerangka kebijakan dan teknologi yang memastikan identitas yang tepat punya akses yang tepat ke sumber daya yang tepat pada waktu yang tepat.

**IDP / IdP**: "IDP" umumnya menyatakan Internal Developer Platform, lapisan perkakas layanan mandiri yang mengabstraksi infrastruktur bagi tim produk; "IdP" menyatakan Identity Provider, layanan yang mengautentikasi pengguna dan menerbitkan asersi. Konteks membedakan keduanya.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)**: Sifat di mana melakukan operasi berkali-kali punya efek sama dengan melakukannya sekali, esensial untuk retry aman dalam sistem terdistribusi dan API.

**[i18n (Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: Merancang dan membangun perangkat lunak agar dapat diadaptasi ke bahasa, wilayah, dan konvensi budaya berbeda tanpa perubahan rekayasa. Numeronim menyingkat 18 huruf di antara "i" dan "n."

**Immutable artefact**: Keluaran build yang, begitu dihasilkan dan diberi versi, tak pernah dimodifikasi; perubahan apa pun menghasilkan versi baru. Ketakberubahan membuat rilis dapat direproduksi dan memungkinkan Anda membangun sekali dan mempromosikan artefak yang sama lintas lingkungan.

**InnerSource**: Penerapan praktik pengembangan sumber terbuka (transparansi, repositori bersama, dan kontribusi lintas tim) di dalam satu organisasi.

**IaC drift**: Lihat Drift (konfigurasi).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)**: Struktur data inti mesin pencari, memetakan tiap istilah ke daftar dokumen yang memuatnya, agar query dapat dijawab tanpa memindai setiap dokumen.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Standar internasional yang menspesifikasikan persyaratan untuk Information Security Management System (ISMS), menyediakan kerangka dapat disertifikasi untuk mengelola risiko keamanan informasi.

**ISO/IEC 42001**: Standar internasional yang menspesifikasikan persyaratan untuk AI Management System, memberi organisasi kerangka dapat disertifikasi untuk mengatur pengembangan dan penggunaan AI secara bertanggung jawab.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Format token ringkas, bertanda tangan (dan opsional terenkripsi) yang dipakai menyampaikan klaim antar pihak, umum untuk autentikasi dan otorisasi dalam sistem web dan API.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Metode alur kerja lean yang memvisualisasikan kerja di papan, membatasi kerja dalam proses, dan mengelola aliran untuk memperbaiki throughput dan keterprediksian.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: Prinsip desain yang memilih solusi paling sederhana yang memenuhi kebutuhan, dengan alasan bahwa kerumitan tak perlu menaikkan biaya dan risiko.

**KMS (Key Management Service)**: Sistem untuk membuat, menyimpan, merotasi, dan mengendalikan akses ke kunci kriptografi, sering didukung hardware security module.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**: Ukuran terkuantifikasi yang dipakai melacak kemajuan menuju sasaran bisnis atau operasional tertentu.

## L

**Lakehouse**: Arsitektur data yang menggabungkan penyimpanan murah dan fleksibel data lake dengan fitur manajemen, transaksi, dan kinerja gudang data.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)**: Waktu berlalu dari perubahan diminta (atau di-commit) hingga disampaikan ke produksi; metrik penyampaian DORA inti.

**[Least privilege (hak istimewa paling sedikit)](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: Prinsip keamanan yang memberi tiap pengguna, proses, atau sistem hanya akses minimum yang dibutuhkan untuk menjalankan fungsinya, membatasi kerusakan dari pembobolan atau galat.

**[Hukum Little](https://en.wikipedia.org/wiki/Little's_law)**: Hasil dari teori antrean yang menyatakan bahwa jumlah rata-rata butir dalam sistem stabil sama dengan laju kedatangan rata-rata dikali waktu rata-rata tiap butir dalam sistem. Ia menghubungkan kerja dalam proses, throughput, dan lead time.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**: Model machine-learning yang dilatih pada korpus teks sangat besar untuk memprediksi dan menghasilkan bahasa, mampu tugas seperti peringkasan, terjemahan, dan pembuatan kode.

**[l10n (Localisation)](https://en.wikipedia.org/wiki/Language_localisation)**: Mengadaptasi perangkat lunak yang terinternasionalisasi ke lokal tertentu, termasuk terjemahan, format, dan konvensi budaya. Numeronim menyingkat 10 huruf di antara "l" dan "n."

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**: Disiplin dan perkakas untuk membuat dan memelihara pandangan tunggal, otoritatif, dan konsisten atas entitas bisnis inti (seperti pelanggan atau produk) lintas sistem.

**MITRE ATT&CK**: Basis pengetahuan publik terkurasi tentang taktik dan teknik musuh dunia nyata, dipakai luas untuk merencanakan latihan red-team, memandu rekayasa deteksi, dan menggambarkan ancaman dalam kosakata bersama.

**Mean Time to Recovery (MTTR)**: Waktu rata-rata yang dibutuhkan untuk memulihkan layanan setelah kegagalan; metrik keandalan dan manajemen insiden yang umum.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**: Praktik di mana seluruh tim bekerja bersama pada tugas yang sama di komputer yang sama, merotasi siapa yang mengetik, untuk berbagi pengetahuan dan membuat keputusan secara kolektif.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: Himpunan praktik yang men-deploy, memantau, dan memelihara model machine-learning di produksi secara andal dan efisien, memperluas prinsip DevOps ke siklus hidup ML.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Satu repositori kendali versi yang menampung kode banyak proyek atau seluruh organisasi, memungkinkan perkakas bersama dan perubahan lintas proyek atomik dengan harga perkakas penskalaan khusus.

**mTLS (mutual TLS)**: Konfigurasi Transport Layer Security di mana kedua pihak menyajikan dan memverifikasi sertifikat, sehingga masing-masing mengautentikasi yang lain. Ia bawaan untuk lalu lintas layanan-ke-layanan dalam service mesh dan jaringan zero-trust. Lihat juga [mutual authentication](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)**: Teknik yang dengan sengaja memperkenalkan cacat kecil ("mutan") ke dalam kode untuk memeriksa apakah rangkaian tes mendeteksinya, mengukur efektivitas nyata rangkaian itu.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Metrik kualitas peringkat yang menghargai penempatan hasil sangat relevan di dekat puncak daftar hasil, dinormalkan agar skor dapat dibandingkan lintas query. Ia andalan evaluasi relevansi pencarian.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Lembaga federal AS yang Special Publication dan kerangkanya adalah standar yang dirujuk luas untuk keamanan siber, privasi, dan AI.

**NIST AI RMF (AI Risk Management Framework)**: Kerangka sukarela NIST untuk mengidentifikasi, menilai, dan mengelola risiko terkait sistem AI sepanjang siklus hidupnya, diorganisasi sekitar fungsi Govern, Map, Measure, dan Manage.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Katalog NIST kendali keamanan dan privasi untuk sistem informasi federal, dipakai luas sebagai garis dasar jauh melampaui pemerintah.

**NIST SP 800-171**: Publikasi NIST yang menspesifikasikan persyaratan untuk melindungi controlled unclassified information (CUI) di sistem non-federal, sentral bagi kepatuhan kontraktor pertahanan.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: Persyaratan yang menggambarkan bagaimana sistem harus berperilaku (kualitasnya seperti kinerja, keamanan, keandalan, atau kebergunaan) alih-alih fungsi apa yang dijalankannya.

**North-south traffic**: Lalu lintas jaringan antara sistem dan klien eksternalnya (masuk dan keluar pusat data atau klaster), berlawanan dengan lalu lintas east-west antar layanan internal. API gateway biasanya mengatur lalu lintas north-south.

## O

**Observability (observabilitas)**: Sejauh mana state internal sistem dapat disimpulkan dari keluaran eksternalnya, biasanya dicapai lewat telemetri: metrik, log, dan jejak.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: Kerangka penetapan sasaran yang memasangkan objective kualitatif dengan beberapa key result terukur untuk menyelaraskan dan memfokuskan organisasi.

**OpenTelemetry (OTel)**: Standar terbuka dan perangkat netral-vendor untuk menghasilkan, mengumpulkan, dan mengekspor data telemetri (jejak, metrik, dan log) dari perangkat lunak.

**OPA (Open Policy Agent)**: Mesin kebijakan serba guna sumber terbuka yang mengevaluasi kebijakan (ditulis dalam bahasa Rego) untuk menegakkan aturan otorisasi dan konfigurasi di seluruh tumpukan, memungkinkan policy as code.

**OSPO (Open Source Program Office)**: Fungsi organisasi yang mengoordinasikan strategi sumber terbuka, tata kelola, kepatuhan, dan keterlibatan komunitas, mengelola konsumsi maupun kontribusi.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Komunitas nirlaba yang menghasilkan sumber daya keamanan aplikasi yang dipakai luas dan tersedia bebas, termasuk OWASP Top Ten dan ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Perluasan teorema CAP yang menyatakan bahwa jika ada Partition, sistem menukar Availability dengan Consistency, Else (dalam operasi normal) ia menukar Latency dengan Consistency.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Standar keamanan yang dipelihara industri kartu pembayaran yang menspesifikasikan persyaratan bagi organisasi yang menyimpan, memproses, atau mentransmisikan data pemegang kartu.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)**: Serangan simulasi yang diotorisasi pada sistem oleh penguji terampil untuk menemukan dan mendemonstrasikan kerentanan yang dapat dieksploitasi sebelum penyerang nyata, disampaikan sebagai temuan berprioritas yang dapat ditindaklanjuti.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**: Informasi yang dapat mengidentifikasi individu tertentu, sendiri atau dikombinasikan dengan data lain; penanganannya diatur hukum privasi dan kebijakan internal.

**Platform engineering**: Disiplin membangun dan mengoperasikan platform layanan mandiri internal dan golden path yang mengurangi beban kognitif dan mempercepat tim produk.

**POUR**: Empat prinsip pemandu Web Content Accessibility Guidelines: konten harus Perceivable (dapat dipersepsi), Operable (dapat dioperasikan), Understandable (dapat dipahami), dan Robust (tangguh).

**Production readiness review**: Pemeriksaan terstruktur, dijalankan sebelum layanan go-live atau mengambil kepemilikan on-call, yang memastikan ia memenuhi standar untuk observabilitas, keandalan, keamanan, runbook, dan dukungan operasional.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)**: Praktik merancang dan menyempurnakan instruksi, konteks, dan contoh yang diberikan kepada model bahasa untuk mendapat keluaran andal berkualitas tinggi, diperlakukan sebagai disiplin rekayasa berversi dan teruji alih-alih coba-coba.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)**: Serangan di mana masukan yang dirancang menyebabkan model bahasa mengabaikan instruksi yang dimaksudkan dan mengikuti instruksi penyerang, analog era-AI dari cacat injeksi. Ia risiko keamanan sentral aplikasi LLM.

**Property-based testing**: Teknik pengujian yang memeriksa bahwa properti yang dinyatakan berlaku di banyak masukan yang dihasilkan otomatis, alih-alih hanya mengandalkan contoh yang dipilih tangan.

**Pull request (PR) / merge request (MR)**: Himpunan perubahan yang diusulkan dan diajukan untuk tinjauan dan diskusi sebelum digabung ke cabang bersama, unit utama tinjauan kode di sebagian besar alur kerja.

**Purple team**: Latihan kolaboratif di mana tim keamanan ofensif (red) dan defensif (blue) bekerja bersama secara waktu nyata, sehingga serangan dan deteksi yang dimaksudkan menangkapnya disetel satu terhadap yang lain.

## Q

**Quality gate**: Titik pemeriksaan otomatis dalam jalur yang harus dilewati (misalnya memenuhi ambang cakupan, keamanan, atau kinerja) sebelum perubahan dapat maju.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: Dalam sistem terdistribusi, jumlah minimum node yang harus setuju agar operasi (seperti baca atau tulis) dianggap berhasil, dipakai menjaga konsistensi meski ada kegagalan.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Model penugasan tanggung jawab yang melabeli tiap peserta dalam tugas atau keputusan sebagai Responsible, Accountable, Consulted, atau Informed.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: Teknik yang mendasari keluaran model bahasa dengan lebih dulu mengambil dokumen atau data relevan dan menyediakannya sebagai konteks, memperbaiki akurasi dan mengurangi halusinasi.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**: Model otorisasi yang menetapkan izin ke peran dan peran ke pengguna, menyederhanakan administrasi dengan mengelola akses di tingkat peran.

**[Red team](https://en.wikipedia.org/wiki/Red_team)**: Kelompok yang meniru musuh realistis, sering terhadap seluruh organisasi dan tanpa peringatan kepada pembela, untuk menguji deteksi dan respons alih-alih sekadar mendaftar kerentanan. Kontraskan dengan tim blue (defensif).

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)**: Daftar kode dan klasifikasi terkendali yang berubah lambat yang dipakai untuk mengategorikan data lain, seperti kode negara, mata uang, dan nilai status. Mengaturnya sebagai kosakata bersama berversi menjaga sistem tetap konsisten.

**Rego**: Bahasa kebijakan deklaratif yang dipakai Open Policy Agent untuk mengekspresikan aturan bagi keputusan otorisasi dan konfigurasi.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Gaya arsitektural untuk aplikasi jaringan yang memakai operasi stateless melalui HTTP pada sumber daya yang dapat dialamatkan, dihargai karena kesederhanaan dan perkakas luas.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)**: Server yang duduk di depan satu atau lebih layanan backend dan meneruskan permintaan klien ke sana, umumnya menyediakan terminasi TLS, load balancing, caching, dan titik masuk tunggal.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Usulan tertulis yang diedarkan untuk umpan balik sebelum keputusan atau perubahan teknis signifikan, memupuk transparansi dan kepemilikan bersama. (Istilah ini juga menamai seri dokumen standar Internet.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**: Ukuran nilai yang diperoleh dari investasi relatif terhadap biayanya, dipakai untuk membenarkan dan memprioritaskan keputusan rekayasa dan teknologi.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: "Robot" perangkat lunak yang mengotomatiskan tugas berulang berbasis aturan dengan berinteraksi dengan antarmuka dan sistem yang ada sebagaimana manusia.

**RPO (Recovery Point Objective)**: Jumlah kehilangan data maksimum yang dapat diterima diukur dalam waktu (misalnya "hingga lima menit"), mendefinisikan seberapa sering data harus dilindungi.

**RTO (Recovery Time Objective)**: Durasi maksimum yang dapat diterima untuk memulihkan layanan setelah gangguan, memandu desain dan investasi pemulihan bencana.

## S

**Saga**: Pola untuk mengelola konsistensi data lintas layanan dalam transaksi terdistribusi dengan mengurutkan transaksi lokal dan menerbitkan tindakan kompensasi ketika suatu langkah gagal.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Kerangka untuk menerapkan praktik agile dan lean di enterprise besar, mengoordinasikan banyak tim; dihargai karena strukturnya dan dikritik karena potensi keberatannya.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Pengujian keamanan yang menganalisis kode sumber, bytecode, atau biner tanpa mengeksekusinya untuk menemukan kerentanan sejak dini dalam pengembangan.

**SBOM (Software Bill of Materials)**: Inventaris formal yang dapat dibaca mesin atas komponen dan dependensi dalam sebuah perangkat lunak, dipakai mengelola risiko rantai pasok dan kerentanan.

**SCA (Software Composition Analysis)**: Perkakas yang mengidentifikasi komponen sumber terbuka dan pihak ketiga dalam basis kode dan menandai kerentanan serta risiko lisensi yang diketahui.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Kerangka agile yang mengorganisasi kerja menjadi iterasi berpanjang tetap (sprint) dengan peran, acara, dan artefak terdefinisi untuk menyampaikan kenaikan nilai.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Hukum AS yang mewajibkan lembaga federal membuat teknologi elektronik dan informasinya dapat diakses penyandang disabilitas, dalam praktik selaras dengan WCAG.

**Semantic search**: Pencarian yang mencocokkan berdasarkan makna alih-alih kata kunci persis, biasanya dengan membandingkan embedding query dan dokumen. Sering digabung dengan pencarian leksikal dalam pendekatan hibrida.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)**: Lapisan infrastruktur khusus, biasanya diimplementasikan dengan proxy sidecar, yang menangani urusan komunikasi layanan-ke-layanan seperti mutual TLS, retry, timeout, pergeseran lalu lintas, dan observabilitas, menjaganya di luar kode aplikasi.

**Sidecar**: Proses atau kontainer pembantu yang di-deploy di samping instans aplikasi utama untuk menyediakan kapabilitas pendukung (seperti proxy service-mesh) tanpa mengubah aplikasi itu sendiri.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Sistem yang mengagregasi dan mengorelasikan log dan peristiwa keamanan di seluruh lingkungan untuk memungkinkan deteksi, peringatan, dan investigasi.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: Komitmen formal antara penyedia layanan dan pelanggannya yang menspesifikasikan tingkat layanan yang diharapkan dan konsekuensi meleset darinya.

**SLI (Service Level Indicator)**: Ukuran kuantitatif suatu aspek kualitas layanan, seperti latensi permintaan atau laju galat, yang memberi makan SLO.

**SLO (Service Level Objective)**: Nilai atau rentang target untuk SLI yang mendefinisikan tingkat keandalan yang diinginkan, membentuk dasar anggaran galat.

**SLSA (Supply-chain Levels for Software Artifacts)**: Kerangka persyaratan keamanan berjenjang untuk memperbaiki integritas dan provenans artefak perangkat lunak melalui proses build dan rilis.

**SOAR (Security Orchestration, Automation, and Response)**: Perkakas dan praktik yang mengotomatiskan dan mengoordinasikan operasi keamanan, seperti triase dan playbook respons, untuk memperbaiki kecepatan dan konsistensi.

**SOC 2 (System and Organisation Controls 2)**: Kerangka audit dan laporan, berdasarkan Trust Services Criteria AICPA, yang menilai kendali organisasi layanan untuk keamanan, ketersediaan, integritas pemrosesan, kerahasiaan, dan privasi.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Lima prinsip desain berorientasi objek (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, dan Dependency Inversion) yang mendorong kode yang dapat dipelihara dan fleksibel.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Undang-undang AS yang menetapkan persyaratan pelaporan keuangan dan kendali internal di perusahaan publik, dengan implikasi bagi sistem TI yang mendukung data keuangan.

**SPACE**: Kerangka untuk mengukur produktivitas developer pada lima dimensi: Satisfaction dan well-being, Performance, Activity, Communication dan collaboration, serta Efficiency dan flow, mengingatkan terhadap ukuran metrik tunggal.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: Disiplin yang menerapkan pendekatan rekayasa perangkat lunak pada operasi, memakai SLO, anggaran galat, dan otomasi untuk menjalankan sistem andal pada skala besar.

**SSDF (Secure Software Development Framework)**: Kerangka NIST (SP 800-218) praktik pengembangan aman tingkat tinggi, mencakup menyiapkan organisasi, melindungi perangkat lunak, menghasilkan perangkat lunak yang diamankan dengan baik, dan merespons kerentanan.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)**: Memeriksa kode sumber, bytecode, atau biner tanpa mengeksekusinya untuk menemukan cacat, pelanggaran gaya, dan cacat keamanan, biasanya lewat linter, pemeriksa tipe, dan penganalisis khusus yang dihubungkan ke editor dan jalur.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Taksonomi pemodelan ancaman yang mengategorikan ancaman sebagai Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, dan Elevation of privilege.

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: Biaya seumur hidup penuh suatu sistem atau keputusan, termasuk akuisisi, operasi, pemeliharaan, dan pemensiunan akhir, bukan hanya harga awal.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**: Praktik menulis tes otomatis yang gagal sebelum kode yang membuatnya lulus, lalu refactoring, dalam siklus pendek berulang untuk menggerakkan desain dan memastikan cakupan.

**[Technical debt (utang teknis)](https://en.wikipedia.org/wiki/Technical_debt)**: Biaya masa depan tersirat dari memilih solusi praktis sekarang daripada yang lebih baik yang memakan waktu lebih lama, yang harus dikelola dengan sengaja alih-alih ditimbun tanpa sadar.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Skema pembobotan klasik yang menilai pentingnya istilah bagi dokumen berdasarkan seberapa sering ia muncul di sana, diimbangi seberapa umum ia di seluruh korpus. Ia mendasari banyak peringkat pencarian leksikal.

**[Theory of constraints (teori kendala)](https://en.wikipedia.org/wiki/Theory_of_constraints)**: Pendekatan manajemen yang berpandangan bahwa throughput sistem dibatasi oleh satu kemacetan pada satu waktu, sehingga upaya perbaikan harus berfokus pada kendala itu sampai ia berpindah ke tempat lain.

**[Threat modelling (pemodelan ancaman)](https://en.wikipedia.org/wiki/Threat_model)**: Praktik terstruktur mengidentifikasi, mendaftar, dan memprioritaskan ancaman potensial terhadap sistem agar pertahanan dapat dirancang masuk sejak dini.

**Toil**: Dalam SRE, kerja operasional manual, berulang, dan dapat diotomatisasi yang berskala linear dengan layanan dan tidak memberi nilai abadi; mengurangi toil membebaskan kapasitas untuk rekayasa.

**Trunk-based development**: Praktik kendali sumber di mana developer sering mengintegrasikan perubahan kecil ke satu cabang bersama, meminimalkan cabang berumur panjang dan nyeri merge.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)**: Fitur bahasa yang menyimpulkan tipe ekspresi secara otomatis, memberi banyak keamanan pengetikan statis tanpa mewajibkan setiap tipe ditulis dengan tangan.

**[Type system](https://en.wikipedia.org/wiki/Type_system)**: Himpunan aturan yang dipakai bahasa untuk menetapkan dan memeriksa tipe, menangkap seluruh kelas galat sebelum program berjalan dan mendokumentasikan maksud. Sistem tipe berkisar dari dinamis ke statis dan dari lemah ke kuat.

## U

**Ubiquitous language**: Dalam Domain-Driven Design, kosakata bersama yang presisi yang dipakai konsisten oleh developer dan pakar domain, dan tercermin langsung dalam kode dan model.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Pengujian yang dilakukan pengguna akhir atau perwakilannya untuk memastikan sistem memenuhi kebutuhan bisnis sebelum diterima untuk rilis.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: User Experience adalah kualitas keseluruhan interaksi seseorang dengan produk; User Interface adalah permukaan visual dan interaktif spesifik tempat interaksi itu terjadi.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)**: Dalam Domain-Driven Design, objek tak dapat diubah yang didefinisikan sepenuhnya oleh atributnya alih-alih identitas berbeda, seperti jumlah uang atau rentang tanggal.

**[Value stream mapping (pemetaan aliran nilai)](https://en.wikipedia.org/wiki/Value-stream_mapping)**: Teknik menggambar setiap langkah dari gagasan hingga nilai terkirim, membedakan waktu bernilai-tambah dari waktu tunggu, sehingga kemacetan, serah terima, dan putaran pengerjaan ulang menjadi terlihat dan dapat diperbaiki.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)**: Penyimpanan data yang dioptimalkan untuk mengindeks dan mencari vektor embedding berdimensi tinggi menurut kemiripan, tulang punggung umum pencarian semantik dan retrieval-augmented generation.

**Vertical scaling**: Menaikkan kapasitas dengan membuat satu node lebih kuat ("scaling up"), yang sederhana tetapi pada akhirnya dibatasi mesin terbesar yang tersedia.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)**: Perkakas, seperti Git, yang merekam perubahan pada berkas dari waktu ke waktu agar riwayat dapat ditinjau, cabang dapat dipelihara, dan kerja dapat dikoordinasikan.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: Inspeksi otomatis sistem, kontainer, atau kode terhadap basis data kelemahan dan salah konfigurasi yang diketahui. Ia luas dan murah, dan melengkapi kedalaman pengujian penetrasi manual.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Himpunan pedoman W3C yang diakui internasional, diorganisasi sekitar prinsip POUR dan tingkat kesesuaian A, AA, dan AAA, untuk membuat konten web dapat diakses.

**Wardley map**: Teknik strategi visual yang memposisikan kapabilitas menurut nilainya bagi pengguna dan kematangan evolusionernya, untuk menginformasikan keputusan bangun/beli dan investasi.

**Work in progress (WIP) limit (batas kerja dalam proses)**: Batas berapa banyak butir yang boleh berada pada tahap tertentu alur kerja sekaligus, praktik Kanban inti yang memperbaiki aliran dengan mengekspos kemacetan dan menahan overhead terlalu banyak kerja paralel.

**WSJF (Weighted Shortest Job First)**: Metode prioritisasi yang mengurutkan kerja dengan membagi biaya penundaannya dengan estimasi durasinya, sehingga butir terpendek, paling sensitif waktu, dan bernilai tertinggi dikerjakan lebih dulu.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Kerentanan web di mana penyerang menyuntikkan skrip berbahaya yang dieksekusi di browser pengguna lain, berpotensi mencuri data atau membajak sesi.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Prinsip yang menyarankan agar tidak membangun fungsionalitas secara spekulatif, dengan alasan bahwa kebutuhan yang diantisipasi sering tak terwujud dan menambah biaya serta kerumitan.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: Model keamanan yang mengasumsikan tak ada kepercayaan implisit berdasarkan lokasi jaringan dan terus-menerus memverifikasi setiap permintaan akses terhadap identitas, perangkat, dan konteks, mengikuti pepatah "jangan pernah percaya, selalu verifikasi."
