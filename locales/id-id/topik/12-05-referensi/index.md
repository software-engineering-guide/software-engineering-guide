# 12.5 Referensi

Bagian ini mengonsolidasikan perangkat rujukan buku panduan: padanan ke body of
knowledge SWEBOK, indeks standar dan kerangka yang dikutip di seluruh buku, dan
bibliografi terkurasi bacaan yang direkomendasikan. Sumber per bab juga muncul
dalam bagian *Referensi dan bacaan lanjutan* di akhir setiap bab.

---

# Padanan SWEBOK

Buku panduan ini selaras dengan **SWEBOK V4.0** dari IEEE Computer Society
(Software Engineering Body of Knowledge). Seluruh 18 area pengetahuan tercakup;
tabel memetakan masing-masing ke bab yang membahasnya, dan buku panduan lalu
melangkah jauh melampaui SWEBOK ke AI, data, UX, DevOps, keberlanjutan, aliran,
dan teknologi kepentingan publik.

| Area pengetahuan SWEBOK V4.0 | Bab utama |
|---|---|
| 1. Software Requirements | 2.8, 11.1, 5.1 |
| 2. Software Architecture | 3.1, 3.2, 3.3 |
| 3. Software Design | 2.2, 3.1 |
| 4. Software Construction | 2.9, 2.1 |
| 5. Software Testing | 2.4, 8.5 |
| 6. Software Engineering Operations | 9.1, 9.2, 9.3, 8.1 |
| 7. Software Maintenance | 3.7, 3.6, 10.4 |
| 8. Software Configuration Management | 2.10, 2.6, 8.2 |
| 9. Software Engineering Management | 10.1, 10.6, 10.2 |
| 10. Software Engineering Process | 1.4, 10.7, 10.8 |
| 11. Software Engineering Models and Methods | 2.12, 3.1, 2.2 |
| 12. Software Quality | 2.11, 2.4, 3.1 |
| 13. Software Security | 4.1, 4.2, 4.3, 4.4 |
| 14. Software Engineering Professional Practice | 10.5, 1.1, 1.3 |
| 15. Software Engineering Economics | 10.10, 10.1, 9.4 |
| 16. Computing Foundations | 2.13, 3.3, 3.4 |
| 17. Mathematical Foundations | 2.13, 11.3 |
| 18. Engineering Foundations | 2.13, 3.1 |

---

# Standar dan kerangka

Lampiran ini adalah indeks terorganisasi standar, kerangka, dan regulasi nyata yang
dirujuk di seluruh buku panduan. Ia alat bantu navigasi, bukan manual kepatuhan:
selalu konsultasikan sumber otoritatif dan, bila relevan, penasihat hukum atau
audit yang berkualifikasi untuk teks terkini dan penerapannya pada konteks Anda.

Entri dikelompokkan menurut domain. Masing-masing menamai standar atau kerangka,
badan penerbitnya, cakupan satu baris, dan bab atau domain tempat ia paling
relevan. Di mana nama lazim disingkat, singkatan ditampilkan. Nomor dokumen dan
judul diberikan hanya bila mapan; tidak ada URL yang disertakan.

## Cara memakai lampiran ini

- **Regulasi** (misalnya GDPR, HIPAA) mengikat secara hukum dalam yurisdiksi dan
  sektornya. Mereka menetapkan kewajiban, bukan hanya praktik baik.
- **Standar** (misalnya ISO/IEC 27001, WCAG) adalah spesifikasi formal, sering dapat
  disertifikasi. Sebagian sukarela; sebagian diwajibkan oleh hukum atau kontrak.
- **Kerangka** (misalnya NIST CSF, NIST AI RMF) adalah panduan terstruktur, biasanya
  sukarela, yang Anda sesuaikan dengan profil risiko Anda.
- Keberlakuan bergantung pada yurisdiksi, sektor, jenis data, dan ketentuan
  kontraktual. Banyak organisasi harus memenuhi beberapa sekaligus.

## Keamanan dan privasi

| Standar / kerangka | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Persyaratan untuk Information Security Management System (ISMS). | 4.1–4.6 Keamanan dan kepatuhan |
| ISO/IEC 27002 | ISO / IEC | Panduan dan himpunan kendali yang mendukung ISO/IEC 27001. | 4.1–4.4 Keamanan |
| ISO/IEC 27017 / 27018 | ISO / IEC | Kendali keamanan khusus cloud (27017) dan perlindungan PII di cloud (27018). | 4.3 Keamanan infrastruktur dan cloud; 4.5 Privasi |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Kerangka sukarela yang diorganisasi sekitar Govern, Identify, Protect, Detect, Respond, Recover. | 4.1, 4.4 Dasar dan operasi keamanan |
| NIST SP 800-53 | National Institute of Standards and Technology | Katalog kendali keamanan dan privasi untuk sistem informasi. | 4.3, 4.6 Keamanan cloud dan kepatuhan |
| NIST SP 800-63 | National Institute of Standards and Technology | Pedoman identitas digital dan jaminan autentikasi. | 4.2, 4.3 Keamanan aplikasi dan infrastruktur |
| OWASP Top Ten | Open Worldwide Application Security Project | Risiko keamanan aplikasi web paling kritis, diperbarui berkala. | 4.2 Keamanan aplikasi |
| OWASP ASVS | Open Worldwide Application Security Project | Persyaratan dan tes berjenjang untuk memverifikasi keamanan aplikasi. | 2.4, 4.2 Pengujian dan keamanan aplikasi |
| OWASP SAMM | Open Worldwide Application Security Project | Model kematangan untuk membangun dan menilai program keamanan perangkat lunak. | 4.1 Dasar keamanan dan budaya |
| STRIDE | Berasal dari Microsoft | Taksonomi pemodelan ancaman untuk mengklasifikasikan ancaman. | 4.2 Keamanan aplikasi |
| MITRE ATT&CK | MITRE | Basis pengetahuan taktik dan teknik musuh untuk deteksi dan pertahanan. | 4.4 Operasi keamanan |
| SLSA | Open Source Security Foundation (OpenSSF) | Kerangka berjenjang untuk integritas dan provenans rantai pasok perangkat lunak. | 4.2, 8.1, 10.3 Rantai pasok dan penyampaian |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Format standar untuk software bill of materials. | 4.2, 10.3 Keamanan aplikasi dan lisensi |
| PCI DSS | PCI Security Standards Council | Persyaratan keamanan untuk menangani data kartu pembayaran. | 4.2, 4.5, 4.6 Keamanan, privasi, kepatuhan |

## Kepatuhan dan pemerintah

### Amerika Serikat

| Regulasi / kerangka | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Pengaman untuk informasi kesehatan terlindungi (PHI). | 4.5, 4.6 Privasi dan kepatuhan |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Persyaratan pelaporan keuangan dan kendali internal untuk perusahaan publik. | 4.6, 10.2 Kepatuhan dan audit |
| FISMA | US Congress | Persyaratan program keamanan informasi untuk lembaga federal. | 4.3, 4.6 Keamanan cloud dan kepatuhan |
| FedRAMP | US General Services Administration / FedRAMP PMO | Otorisasi keamanan terstandar untuk layanan cloud yang dipakai lembaga federal. | 4.3, 4.6 Keamanan cloud dan kepatuhan |
| NIST SP 800-171 | National Institute of Standards and Technology | Perlindungan controlled unclassified information (CUI) di sistem non-federal. | 4.6 Kepatuhan (rantai pasok pertahanan) |
| CMMC | US Department of Defence | Sertifikasi kematangan keamanan siber kontraktor pertahanan. | 4.6 Kepatuhan (pertahanan) |
| FIPS 140-3 | National Institute of Standards and Technology | Persyaratan keamanan untuk modul kriptografi. | 4.3 Keamanan infrastruktur dan cloud |
| CCPA / CPRA | State of California | Hak privasi konsumen dan kewajiban bisnis di California. | 4.5 Privasi dan perlindungan data |

### Uni Eropa dan Britania Raya

| Regulasi / standar | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| GDPR | European Union | Regulasi menyeluruh tentang pemrosesan data pribadi. | 4.5, 4.6 Privasi dan kepatuhan |
| UK GDPR / Data Protection Act 2018 | United Kingdom | Rezim perlindungan data Britania pasca-Brexit. | 4.5, 4.6 Privasi dan kepatuhan |
| eIDAS | European Union | Kerangka untuk identifikasi elektronik dan layanan kepercayaan. | 4.2, 4.3 Keamanan |
| NIS2 Directive | European Union | Kewajiban keamanan siber untuk entitas esensial dan penting. | 4.4, 4.6 Operasi keamanan dan kepatuhan |
| DORA (Digital Operational Resilience Act) | European Union | Persyaratan ketahanan operasional untuk sektor keuangan. | 9.1, 10.2 Keandalan dan audit |
| EU AI Act | European Union | Regulasi berbasis risiko atas sistem AI (lihat tata kelola AI di bawah). | 6.1, 6.5 Strategi AI dan AI yang bertanggung jawab |

## Aksesibilitas

| Standar | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Pedoman untuk konten web yang dapat diakses, dengan tingkat kesesuaian A/AA/AAA. | 5.3 Aksesibilitas; 5.1–5.6 UX dan frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Peran, status, dan properti untuk aplikasi internet kaya yang dapat diakses. | 5.3, 5.6 Aksesibilitas dan frontend |
| Section 508 | US Access Board / US federal law | Persyaratan aksesibilitas untuk ICT federal AS, selaras dengan WCAG. | 5.3 Aksesibilitas (pemerintah AS) |
| EN 301 549 | ETSI / CEN / CENELEC | Persyaratan aksesibilitas Eropa untuk pengadaan ICT, selaras dengan WCAG. | 5.3 Aksesibilitas (sektor publik UE) |
| ADA (Americans with Disabilities Act) | US Congress | Hukum hak sipil yang melarang diskriminasi disabilitas, diterapkan pada layanan digital. | 5.3 Aksesibilitas |
| ISO/IEC 40500 | ISO / IEC | Adopsi internasional WCAG 2.0 sebagai standar formal. | 5.3 Aksesibilitas |

## Tata kelola AI

| Kerangka / regulasi | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Kerangka sukarela untuk mengatur, memetakan, mengukur, dan mengelola risiko AI. | 6.1, 6.5 Strategi AI dan AI yang bertanggung jawab |
| ISO/IEC 42001 | ISO / IEC | Persyaratan untuk AI Management System (AIMS). | 6.1, 6.5 Tata kelola AI |
| ISO/IEC 23894 | ISO / IEC | Panduan manajemen risiko khusus AI. | 6.5 AI yang bertanggung jawab dan tepercaya |
| EU AI Act | European Union | Kewajiban hukum berjenjang risiko bagi penyedia dan pengerah sistem AI. | 6.1, 6.3, 6.5 Aplikasi dan tata kelola AI |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Prinsip berbasis nilai untuk AI tepercaya, berpengaruh pada kebijakan. | 6.5, 10.5 AI yang bertanggung jawab dan etika |

## Kualitas dan proses

| Standar / kerangka | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Model kualitas produk perangkat lunak (kesesuaian fungsional, keandalan, keamanan, dll.). | 2.2, 2.4 Desain dan pengujian |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Proses siklus hidup perangkat lunak. | 1.4, 10.1 Cara kerja dan manajemen program |
| ISO 9001 | ISO | Persyaratan untuk Quality Management System umum. | 10.2 Risiko, audit, dan jaminan |
| CMMI | ISACA / CMMI Institute | Model kematangan untuk kapabilitas dan perbaikan proses. | 10.1, 10.2 Manajemen program dan jaminan |
| Metrik DORA | DevOps Research and Assessment (Google Cloud) | Empat metrik kinerja penyampaian utama untuk tim perangkat lunak. | 8.1, 8.4, 9.1 Penyampaian, platform, keandalan |
| Kerangka SPACE | Peneliti Microsoft / GitHub | Model multidimensi untuk mengukur produktivitas developer. | 1.3, 8.4 Pertumbuhan dan pengalaman developer |
| ITIL | AXELOS / PeopleCert | Kerangka praktik manajemen layanan TI. | 9.1, 9.3 Keandalan dan manajemen insiden |

## Arsitektur

| Standar / kerangka | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Standar untuk deskripsi arsitektur dan sudut pandang. | 2.7, 3.1 Dokumentasi dan dasar-dasar arsitektur |
| TOGAF | The Open Group | Kerangka arsitektur enterprise dan metode pengembangan. | 3.1, 10.1 Arsitektur dan manajemen portofolio |
| Model C4 | Komunitas (Simon Brown) | Pendekatan empat tingkat untuk memvisualisasikan arsitektur perangkat lunak. | 2.7, 3.1 Dokumentasi dan arsitektur |
| arc42 | Komunitas (Starke / Hruschka) | Templat untuk menyusun dokumentasi arsitektur. | 2.7, 3.1 Dokumentasi dan arsitektur |
| ADR | Praktik komunitas | Catatan ringan keputusan arsitektur signifikan. | 1.5, 2.7, 3.1 Pengambilan keputusan dan dokumentasi |

## Cloud dan DevOps

| Standar / kerangka | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| CIS Benchmarks | Centre for Internet Security | Garis dasar konfigurasi aman berbasis konsensus untuk sistem dan cloud. | 4.3, 8.2 Keamanan infrastruktur dan IaC |
| Lanskap dan proyek CNCF | Cloud Native Computing Foundation | Ekosistem dan standar untuk komputasi cloud-native (mis. Kubernetes). | 8.3 Kontainer dan cloud native |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Standar terbuka untuk format image dan runtime kontainer. | 8.3 Kontainer dan cloud native |
| OpenTelemetry | Cloud Native Computing Foundation | Standar netral-vendor untuk telemetri (jejak, metrik, log). | 9.2 Observabilitas dan pemantauan |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Mesin kebijakan serba guna untuk policy as code. | 4.6, 8.2, 8.3 Kepatuhan, IaC, orkestrasi |
| Praktik SRE | Google (diadopsi luas) | Pendekatan berbasis SLI/SLO/anggaran galat untuk mengoperasikan layanan andal. | 9.1 Rekayasa keandalan situs |
| FinOps Framework | FinOps Foundation | Praktik untuk manajemen keuangan cloud dan akuntabilitas biaya. | 9.4 Biaya, keberlanjutan, perangkat lunak hijau |

## Data

| Standar / kerangka | Badan penerbit | Cakupan (satu baris) | Bab / domain utama |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Body of knowledge yang mengorganisasi disiplin manajemen data. | 7.1 Strategi dan tata kelola data |
| ISO/IEC 38505 | ISO / IEC | Tata kelola data sebagai aset organisasi. | 7.1 Tata kelola data |
| ISO 8000 | ISO | Standar kualitas data dan data induk. | 7.1, 7.2 Tata kelola dan rekayasa data |
| Data mesh | Komunitas (Zhamak Dehghani) | Pendekatan terdesentralisasi berorientasi domain untuk data sebagai produk. | 7.1, 7.2 Strategi dan rekayasa data |
| DCAM | EDM Council | Model penilaian kapabilitas manajemen data. | 7.1 Strategi dan tata kelola data |

## Catatan tentang cakupan dan perubahan

Standar dan regulasi berevolusi. Nomor versi (misalnya WCAG 2.1 versus 2.2, atau
tahun revisi ISO) dan katalog kendali berubah seiring waktu, dan hukum baru
(seperti regulasi AI dan ketahanan khusus sektor) terus bermunculan. Perlakukan
lampiran ini sebagai peta awal: konfirmasi versi, yurisdiksi, dan keberlakuan
terkini sebelum mengandalkan entri mana pun untuk keputusan kepatuhan atau
pengadaan. Di mana bab buku panduan dan lampiran ini berbeda dalam detail, dokumen
sumber otoritatif selalu yang mengatur.


---

# Bacaan yang direkomendasikan

Lampiran ini adalah daftar bacaan terkurasi dan beranotasi yang membentang setiap
domain buku panduan. Ia mengutamakan karya yang telah membentuk praktik pada skala
besar: klasik yang diakui, rujukan ketat, dan standar serta laporan yang menjadi
tolok ukur tim besar, enterprise, dan pemerintah.

Setiap entri memberi judul dan penulis, diikuti satu kalimat tentang mengapa ia
penting. Daftar diorganisasi menurut sepuluh bagian buku. Bacalah secara selektif:
pilih dua atau tiga karya yang paling dekat dengan nyeri Anda saat ini, bukan
seluruh rak. Di mana sebuah karya membentang domain, ia ditempatkan di tempat ia
paling berguna; banyak yang termasuk dalam beberapa bagian.

Catatan tentang standar: badan seperti NIST, OWASP, W3C/WCAG, ISO, dan program DORA
menerbitkan dokumen hidup yang direvisi berkala. Kutip dan baca versi terkini;
anotasi di bawah menggambarkan tujuan abadinya.

## Fondasi: budaya, orang, dan proses

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Fondasi riset yang menunjukkan bahwa kinerja penyampaian memprediksi kinerja organisasi, dan mendefinisikan metrik (kini disebut DORA) untuk mengukurnya.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Novel bisnis yang membuat aliran, kerja-dalam-proses, dan "Three Ways" DevOps intuitif bagi pemimpin maupun skeptis.
- **Team Topologies: Organising Business and Technology Teams for Fast Flow**. Matthew Skelton dan Manuel Pais. Kosakata praktis (tim berselaras aliran, platform, pemungkin, dan subsistem rumit) untuk merancang organisasi yang menghasilkan perangkat lunak baik.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Kerangka teruji lapangan untuk menentukan ukuran tim, mengelola pertumbuhan organisasi, dan membuat keputusan berulang kepemimpinan rekayasa.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Mendefinisikan arketipe staff-plus dan jalur kepemimpinan teknis bagi mereka yang menginginkan dampak tanpa menjadi manajer.
- **The Manager's Path**. Camille Fournier. Panduan tahap demi tahap dari tech lead hingga eksekutif yang menjangkarkan tangga karier dan transisi ke manajemen.
- **The Staff Engineer's Path**. Tanya Reilly. Pendamping literatur staff-plus yang berfokus pada kerja sehari-hari kepemimpinan teknis, pengaruh, dan mengarahkan tanpa otoritas.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco dan Timothy Lister. Argumen abadi bahwa masalah sentral perangkat lunak bersifat sosiologis, bukan teknis.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. Asal Hukum Brooks dan pembedaan kerumitan esensial-versus-aksidental yang masih mengatur penstafan dan penjadwalan.
- **The Fearless Organisation: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Fondasi riset untuk budaya tanpa menyalahkan dan rasa aman yang memungkinkan belajar dari kegagalan.
- **Thinking, Fast and Slow**. Daniel Kahneman. Catatan definitif tentang bias kognitif, esensial untuk wawancara terstruktur, kalibrasi, dan pengambilan keputusan jujur.

## Keahlian pemrograman dan kualitas kode

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt dan David Thomas. Katalog fondasional kebiasaan profesional (DRY, ortogonalitas, tracer bullet) yang mendefinisikan arti keahlian.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. Katalog kanonik transformasi yang mempertahankan perilaku dan disiplin perbaikan kode kontinu berbantuan tes.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Standar yang dipakai luas (dan diperdebatkan) untuk penamaan, fungsi, dan keterbacaan yang membentuk ekspektasi tinjauan banyak tim.
- **Code Complete**. Steve McConnell. Buku pegangan komprehensif praktik konstruksi yang merujuk bukti, tetap garis dasar menyeluruh untuk kualitas pemrograman.
- **Test-Driven Development: By Example**. Kent Beck. Pengantar langsung asli ke siklus red-green-refactor dan desain tes-dulu.
- **Working Effectively with Legacy Code**. Michael Feathers. Perangkat definitif untuk menambahkan tes ke, dan mengubah dengan aman, kode yang tak punya tes, dan sangat diperlukan untuk sistem berumur panjang.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman dan Nat Pryce. Demonstrasi kerja TDD luar-ke-dalam, mocking, dan mengembangkan desain lewat tes.
- **A Philosophy of Software Design**. John Ousterhout. Pembahasan tajam dan beropini tentang kerumitan, modul dalam, dan penyembunyian informasi yang secara produktif menantang sebagian ortodoksi "clean code."

## Arsitektur dan sistem

- **Designing Data-Intensive Applications**. Martin Kleppmann. Rujukan modern terbaik tunggal tentang trade-off penyimpanan, replikasi, partisi, konsistensi, dan pemrosesan aliran pada skala besar.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards dan Neal Ford. Tinjauan luas dan terkini tentang gaya arsitektur, karakteristik, serta peran dan pengambilan keputusan arsitek.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Pembahasan berfokus keputusan tentang trade-off arsitektur terdistribusi, granularitas layanan, dan kepemilikan data.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Memperkenalkan fitness function dan arsitektur yang dirancang untuk berubah dengan aman seiring waktu.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. Asal bounded context, ubiquitous language, dan aggregate: kosakata desain layanan modern.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. Rujukan untuk dekomposisi, batas layanan, deployment, dan implikasi organisasi dari microservice.
- **Monolith to Microservices**. Sam Newman. Katalog pola untuk dekomposisi inkremental, seperti strangler fig dan branch by abstraction, tanpa penulisan ulang big-bang yang berisiko.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. Rujukan pola bernama (repository, unit of work, dan lainnya) yang memberi bahasa bersama bagi sistem enterprise.
- **Enterprise Integration Patterns**. Gregor Hohpe dan Bobby Woolf. Katalog definitif pola pesan yang mendasari arsitektur berbasis peristiwa dan asinkron.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. Sumber circuit breaker, bulkhead, dan pola stabilitas lain untuk sistem yang bertahan di produksi nyata.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). Katalog pola berorientasi objek yang menentukan secara historis dan kosakata desain bersama.

## Keamanan, privasi, dan kepercayaan

- **Threat Modelling: Designing for Security**. Adam Shostack. Panduan praktis dan komprehensif tentang STRIDE dan pemodelan ancaman terstruktur sebagai praktik rekayasa rutin.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. Rujukan ensiklopedis tentang bagaimana sistem nyata gagal dan bagaimana membangun yang tahan serangan.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Tur ketat model keamanan browser dan cara-cara halus platform web mengkhianati asumsi naif.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Panduan praktisi untuk memakai kriptografi dengan benar dan menghindari kesalahan umum yang berbahaya.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). Sintesis Google tentang keamanan dan keandalan sebagai properti yang saling terjalin dan dirancang masuk sejak awal.
- **Zero Trust Networks**. Evan Gilman dan Doug Barth. Pembahasan jelas prinsip dan mekanika arsitektur jaringan jangan-pernah-percaya, selalu-verifikasi.
- **OWASP Top 10**. OWASP Foundation. Garis dasar konsensus risiko keamanan aplikasi web paling kritis, dirujuk oleh kebijakan dan audit di seluruh dunia.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Daftar periksa persyaratan keamanan berjenjang dan dapat diuji yang cocok untuk kontrak dan kriteria penerimaan.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organisations**. NIST. Katalog kendali di jantung keamanan federal AS dan dasar otorisasi FedRAMP dan FISMA.
- **NIST Cybersecurity Framework (CSF)**. NIST. Struktur identifikasi-lindungi-deteksi-respons-pulihkan yang diadopsi luas untuk mengorganisasi program keamanan.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. Definisi rujukan dan arsitektur rujukan yang menjangkarkan sebagian besar program zero-trust enterprise dan pemerintah.

## UX, UI, dan desain produk

- **The Design of Everyday Things**. Don Norman. Teks fondasional tentang affordance, signifier, umpan balik, dan desain berpusat manusia yang berlaku jauh melampaui objek fisik.
- **Don't Make Me Think, Revisited**. Steve Krug. Argumen ringkas dan abadi untuk kebergunaan yang jelas dengan sendirinya dan nilai uji kebergunaan murah dan sering.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. Rujukan komprehensif tentang desain interaksi, persona, dan desain berarah sasaran.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Catatan membumi tentang membangun sistem komponen konsisten yang dapat dipakai ulang dan bahasa bersama di baliknya.
- **Refactoring UI**. Adam Wathan dan Steve Schoger. Panduan praktis berbasis contoh untuk poles visual bagi insinyur yang mendesain antarmuka tanpa pelatihan formal.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. Panduan definitif desain konten bahasa sederhana yang berfokus tugas.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. Pendamping praktis untuk membangun antarmuka yang berfungsi bagi seluruh rentang kemampuan manusia.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton dan Whitney Quesenbery. Jembatan berbasis prinsip antara standar aksesibilitas dan pengalaman pengguna yang baik.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. Standar yang dirujuk internasional (dapat dipersepsi, dapat dioperasikan, dapat dipahami, tangguh) di balik sebagian besar hukum aksesibilitas.
- **U.S. Web Design System (USWDS)**. Pemerintah AS. Contoh kerja design system yang dapat diakses dan berbasis standar yang dibangun untuk layanan publik pada skala besar.

## Kecerdasan buatan dan machine learning

- **Designing Machine Learning Systems**. Chip Huyen. Panduan praktis terkemuka untuk membangun sistem ML produksi ujung-ke-ujung: data, fitur, deployment, dan pemantauan.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Memperluas disiplin SRE (SLO, pemantauan, respons insiden) ke sistem machine learning.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. Rujukan akademik standar untuk teori dan metode yang mendasari jaringan saraf modern.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Panduan terkini untuk merancang, mengevaluasi, dan mengoperasikan aplikasi yang dibangun di atas model fondasi besar.
- **Weapons of Maths Destruction**. Cathy O'Neil. Kasus hidup untuk akuntabilitas algoritmik dan kerugian dunia nyata dari model yang tak diperiksa, esensial untuk AI sektor publik.
- **Interpretable Machine Learning**. Christoph Molnar. Rujukan komprehensif yang tersedia bebas tentang metode penjelasan untuk model dan prediksinya.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Kerangka rujukan untuk mengatur, memetakan, mengukur, dan mengelola risiko AI, makin dikutip dalam kebijakan dan pengadaan.

## Data, analitik, dan wawasan

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling**. Ralph Kimball dan Margy Ross. Rujukan kanonik tentang skema bintang dan pemodelan dimensional untuk analitik.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. Panduan otoritatif menjalankan eksperimen yang menghasilkan hasil andal dan dapat ditindaklanjuti pada skala besar.
- **Fundamentals of Data Engineering**. Joe Reis dan Matt Housley. Peta netral-vendor siklus hidup data modern dan praktik rekayasa di baliknya.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. Teks pendiri pendekatan berorientasi domain dan berpusat produk untuk mengorganisasi data pada skala besar.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Panduan praktis visualisasi data yang jujur dan jelas serta mengomunikasikan wawasan kepada pengambil keputusan.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. Karya fondasional tentang integritas grafis, data-ink, dan etika menampilkan data dengan jujur.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Kerangka rujukan komprehensif untuk tata kelola data, kepengurusan, kualitas, dan katalogisasi.
- **The Book of Why**. Judea Pearl dan Dana Mackenzie. Pengantar mudah dibaca tentang inferensi kausal, vital untuk bergerak dari korelasi ke keputusan yang dapat dipertahankan.

## Otomasi, DevOps, dan rekayasa platform

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. Buku panduan komprehensif yang menerjemahkan "Three Ways" menjadi praktik konkret untuk aliran, umpan balik, dan pembelajaran berkelanjutan.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble dan David Farley. Teks fondasional tentang jalur deployment, otomasi, dan merilis perangkat lunak dengan aman dan sering.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. Rujukan tentang memperlakukan infrastruktur sebagai perangkat lunak: modul, pengujian, ketakberubahan, dan drift.
- **Team Topologies**. Matthew Skelton dan Manuel Pais. (Lihat Fondasi.) Juga esensial di sini untuk membentuk tim platform dan pengalaman developer yang mereka sediakan.
- **Kubernetes Patterns**. Bilgin Ibryam dan Roland Huß. Katalog pola yang dapat dipakai ulang untuk merancang aplikasi cloud-native di Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Bagaimana praktik rekayasa seperti pengujian, tinjauan, perkakas, dan manajemen dependensi berskala ke puluhan ribu insinyur selama puluhan tahun.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Manifesto ringkas dan berpengaruh untuk membangun layanan portabel, berskala, dan cloud-native.
- **DORA State of DevOps Report**. DORA / Google Cloud (tahunan). Program riset berkelanjutan di balik empat metrik penyampaian utama dan kapabilitas yang mendorong kinerja.

## Operasi, keandalan, dan observabilitas

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (ed.). Teks fondasional yang mendefinisikan SLI, SLO, anggaran galat, dan disiplin merekayasa keandalan.
- **The Site Reliability Workbook**. Betsy Beyer et al. (ed.). Pendamping praktis dengan contoh praktis, SLO terkerjakan, dan panduan implementasi.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. Definisi modern observabilitas, data kardinalitas tinggi, dan men-debug hal-tak-diketahui-yang-tak-diketahui di produksi.
- **Implementing Service Level Objectives**. Alex Hidalgo. Panduan menyeluruh dan praktis untuk merancang, mengukur, dan memakai SLO serta anggaran galat dengan baik.
- **Release It!**. Michael T. Nygard. (Lihat Arsitektur.) Juga fondasional di sini untuk pola stabilitas produksi dan mengoperasikan sistem tangguh.
- **The Art of Capacity Planning**. Arun Kejariwal dan John Allspaw. Pendekatan berbasis data untuk meramalkan permintaan dan merencanakan kapasitas bagi sistem yang tumbuh.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal dan Nora Jones. Pembahasan definitif tentang menyuntikkan kegagalan dengan sengaja untuk membangun keyakinan pada ketahanan sistem.
- **Google SRE Book, Chapter on Postmortems**. Google. Model yang ditiru luas untuk postmortem tanpa menyalahkan dan belajar dari insiden.

## Enterprise, pemerintah, dan kepentingan publik

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. Studi esensial tentang bagaimana sumber terbuka sebenarnya dipertahankan, dan beban pemelihara di balik dependensi yang diandalkan enterprise.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Catatan berpandangan jernih tentang mengapa teknologi sektor publik gagal dan bagaimana reformasi berfokus penyampaian dapat memperbaikinya.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Pelajaran dari UK Government Digital Service tentang mentransformasi layanan publik dengan menyampaikan, bukan merencanakan.
- **Project to Product**. Mik Kersten. Flow Framework untuk menggeser enterprise besar dari pendanaan berbasis proyek ke aliran nilai produk tahan lama.
- **Escaping the Build Trap**. Melissa Perri. Bagaimana organisasi mengira keluaran sebagai hasil, dan bagaimana manajemen produk memperbaikinya, dengan relevansi langsung bagi tata kelola portofolio dan program.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Himpunan ringkas langkah untuk menyampaikan layanan digital pemerintah yang efektif dan berpusat pada pengguna.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. Standar terbit yang bekerja untuk membangun layanan publik yang baik, ditiru luas oleh pemerintah lain.
- **NIST SP 800-37: Risk Management Framework**. NIST. Kerangka proses di balik authorisation to operate (ATO) dan pemantauan berkelanjutan di sistem federal AS.
- **The FinOps Foundation Framework**. FinOps Foundation. Model rujukan untuk visibilitas biaya cloud, optimasi, dan akuntabilitas lintas keuangan dan rekayasa.

## Cara memakai daftar ini

- **Mulailah dari nyeri Anda.** Jika deployment lambat dan menakutkan, baca *Accelerate*, *Continuous Delivery*, dan laporan *DORA* sebelum yang lain.
- **Baca untuk dekade, bukan sprint.** Pilih karya yang menjelaskan prinsip abadi daripada yang terikat versi perkakas tertentu.
- **Verifikasi edisi terkini standar.** NIST, OWASP, WCAG, ISO, dan DORA merevisi terbitannya; selalu kerjakan dari rilis terbaru dan catat versinya dalam kebijakan Anda sendiri.
- **Bangun rak bersama.** Tim yang telah membaca dua atau tiga buku ini bersama berdebat lebih sedikit dan memutuskan lebih cepat, karena berbagi kosakata dan seperangkat titik rujukan.
- **Lihat juga bab 12.5** untuk indeks lengkap standar dan kerangka rujukan, dan **bab 12.6** untuk cara mengurutkan adopsi praktik yang dijelaskan karya-karya ini.
