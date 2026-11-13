# 12.3 Templat

Templat ini adalah titik awal siap salin-tempel. Angkat templat mana pun ke wiki, repositori, atau sistem tiket Anda dan isi placeholder dalam tanda kurung siku. Catatan miring dan komentar sebaris menjelaskan apa yang termasuk dalam tiap bagian; hapus setelah bagian terisi. Jaga templat tetap ringan: templat yang lebih cepat dilewati daripada diselesaikan tidak akan dipakai. Sesuaikan judul dan bagian dengan organisasi Anda, tetapi pertahankan maksud tiap bagian.

Beberapa konvensi yang dipakai di bawah:

- Teks dalam `[kurung siku]` adalah placeholder untuk diganti.
- Teks dalam _huruf miring_ atau `<!-- komentar -->` adalah panduan untuk dihapus.
- Jaga dokumen jadi sependek mungkin sambil tetap menjawab pertanyaannya.

## Architecture Decision Record (ADR)

```markdown
# ADR [NNNN]: [Judul singkat keputusan]

- Status: [Diusulkan | Diterima | Usang | Digantikan oleh ADR-XXXX]
- Tanggal: [YYYY-MM-DD]
- Pengambil keputusan: [nama atau peran]
- Dikonsultasikan: [nama atau peran]

## Konteks

<!-- Apa masalah, gaya, atau kendala yang menggerakkan keputusan ini?
     Nyatakan fakta dan persyaratan secara netral. Sertakan hanya apa
     yang dibutuhkan pembaca masa depan untuk memahami mengapa
     keputusan diperlukan. -->

## Keputusan

<!-- Nyatakan pilihan dalam satu atau dua kalimat jelas: "Kami akan ..." -->

## Alternatif yang dipertimbangkan

<!-- Daftar opsi realistis yang Anda timbang dan mengapa masing-masing
     dipilih atau tidak. Setidaknya dua alternatif harus muncul di sini. -->

- Opsi A: [ringkasan]; ditolak karena [alasan].
- Opsi B: [ringkasan]; ditolak karena [alasan].
- Opsi terpilih: [ringkasan]; dipilih karena [alasan].

## Konsekuensi

<!-- Hasil jujur dari keputusan, baik dan buruk. -->

- Positif: [manfaat yang diperoleh]
- Negatif: [biaya, risiko, atau keterbatasan yang diterima]
- Tindak lanjut: [migrasi, kerja baru, atau keputusan yang dipicunya]

## Terkait

<!-- Tautan ke ADR, RFC, tiket, atau dokumen sebelumnya yang terkait. -->
```

## RFC / dokumen desain

```markdown
# RFC: [Judul]

- Penulis: [nama]
- Status: [Draf | Dalam tinjauan | Disetujui | Ditolak | Diimplementasikan]
- Peninjau: [nama atau peran]
- Dibuat: [YYYY-MM-DD]
- Terakhir diperbarui: [YYYY-MM-DD]
- Tiket / pelacakan: [tautan]

## Ringkasan

<!-- Satu paragraf: apa yang diusulkan dan mengapa penting. Pembaca
     harus menangkap intinya dari bagian ini saja. -->

## Masalah dan motivasi

<!-- Masalah apa yang kita selesaikan? Siapa yang terdampak? Apa yang
     terjadi jika kita tidak melakukan apa-apa? Sertakan latar belakang
     dan kendala yang relevan. -->

## Sasaran dan non-sasaran

- Sasaran: [seperti apa keberhasilan, terukur bila memungkinkan]
- Non-sasaran: [secara eksplisit di luar cakupan, untuk mencegah scope creep]

## Desain yang diusulkan

<!-- Inti dokumen. Jelaskan pendekatan, arsitektur, model data,
     antarmuka, dan alur kunci. Pakai diagram di mana memperjelas.
     Jelaskan bagaimana ia bekerja, bukan hanya apa ia. -->

## Alternatif yang dipertimbangkan

<!-- Pendekatan lain dan mengapa tidak dipilih. Menunjukkan kepada
     pembaca bahwa ruang desain telah dijelajahi. -->

## Dampak dan risiko

- Keamanan dan privasi: [implikasi dan mitigasi]
- Kinerja dan skala: [beban dan perilaku yang diharapkan]
- Kemampuan dioperasikan: [pemantauan, mode kegagalan, peluncuran, rollback]
- Biaya: [dampak infrastruktur atau lisensi]
- Kompatibilitas mundur: [migrasi dan deprekasi]

## Rencana pengujian dan peluncuran

<!-- Bagaimana perubahan akan divalidasi dan dirilis dengan aman. -->

## Pertanyaan terbuka

<!-- Isu belum terselesaikan yang Anda ingin peninjau pertimbangkan. -->
```

## Postmortem / tinjauan insiden (tanpa menyalahkan)

```markdown
# Postmortem: [Judul insiden]

- ID insiden: [ID]
- Tanggal insiden: [YYYY-MM-DD]
- Penulis: [nama]
- Status: [Draf | Final]
- Keparahan: [SEV1 | SEV2 | SEV3]

> Tinjauan ini tanpa menyalahkan. Kami berfokus pada sistem dan faktor
> penyumbang, bukan pada individu. Tujuannya belajar dan mencegah
> pengulangan.

## Ringkasan

<!-- Dua atau tiga kalimat: apa yang terjadi, dampaknya, dan
     penyelesaiannya, dapat dibaca non-pakar. -->

## Dampak

- Durasi: [waktu mulai hingga waktu pemulihan, dengan zona waktu]
- Pengguna terdampak: [cakupan dan jumlah]
- Dampak bisnis: [pendapatan, SLA, reputasi, atau lainnya]

## Linimasa

<!-- Urutan peristiwa faktual berstempel waktu. Sertakan deteksi,
     eskalasi, tindakan kunci, dan pemulihan. -->

- [JJ:MM] [peristiwa]
- [JJ:MM] [peristiwa]

## Faktor penyumbang

<!-- Rantai kondisi yang menyebabkan insiden. Pilih "faktor penyumbang"
     daripada satu akar masalah. -->

## Deteksi dan respons

- Bagaimana terdeteksi? [peringatan, laporan pelanggan, dll.]
- Apa yang membantu respons?
- Apa yang memperlambat respons?

## Apa yang berjalan baik

<!-- Akui tindakan efektif dan pengaman yang berfungsi. -->

## Butir tindakan

<!-- Spesifik, berpemilik, dan bertanggal. Tangani pencegahan, deteksi,
     dan mitigasi. Lacak di backlog normal. -->

| Tindakan | Pemilik | Tanggal jatuh tempo | Jenis (cegah/deteksi/mitigasi) | Tiket |
|----------|---------|---------------------|--------------------------------|-------|
| [tindakan] | [nama] | [tanggal] | [jenis] | [tautan] |

## Pelajaran yang dipetik

<!-- Apa yang harus dibawa pulang organisasi yang lebih luas. -->
```

## Model ancaman (berbasis STRIDE)

```markdown
# Model ancaman: [Nama sistem atau fitur]

- Penulis: [nama]
- Tanggal: [YYYY-MM-DD]
- Peninjau: [kontak keamanan, pemilik]
- Cakupan: [apa yang tercakup dan tidak]

## Gambaran sistem

<!-- Deskripsi singkat sistem, tujuannya, dan penggunanya. -->

## Aset

<!-- Apa yang layak dilindungi: data, kredensial, fungsionalitas,
     reputasi. Catat kepekaan masing-masing. -->

## Batas kepercayaan dan aliran data

<!-- Jelaskan atau diagramkan komponen, penyimpanan data, entitas
     eksternal, dan batas di mana kepercayaan berubah. -->

## Ancaman (STRIDE)

<!-- Untuk setiap elemen, pertimbangkan kategori STRIDE. Catat setiap
     ancaman yang kredibel, risikonya, dan mitigasi atau risiko yang
     diterima. -->

| Ancaman | Kategori STRIDE | Elemen terdampak | Risiko (R/S/T) | Mitigasi | Status |
|---------|-----------------|------------------|----------------|----------|--------|
| [ancaman] | Spoofing (pemalsuan identitas) | [elemen] | [risiko] | [kendali] | [terbuka/dimitigasi/diterima] |
| [ancaman] | Tampering (perusakan data) | [elemen] | [risiko] | [kendali] | [status] |
| [ancaman] | Repudiation (penyangkalan) | [elemen] | [risiko] | [kendali] | [status] |
| [ancaman] | Information disclosure (pengungkapan informasi) | [elemen] | [risiko] | [kendali] | [status] |
| [ancaman] | Denial of service (penolakan layanan) | [elemen] | [risiko] | [kendali] | [status] |
| [ancaman] | Elevation of privilege (peningkatan hak istimewa) | [elemen] | [risiko] | [kendali] | [status] |

## Asumsi dan dependensi

<!-- Asumsi keamanan yang diandalkan dan kendali eksternal yang dipercaya. -->

## Isu terbuka dan tindak lanjut

<!-- Ancaman yang membutuhkan kerja lebih lanjut, dilacak sebagai tiket. -->
```

## Runbook

```markdown
# Runbook: [Nama tugas atau skenario]

- Layanan: [nama layanan]
- Pemilik: [tim]
- Terakhir ditinjau: [YYYY-MM-DD]
- Peringatan terkait: [nama peringatan]

## Tujuan

<!-- Kapan memakai runbook ini dan apa yang dicapainya. -->

## Prasyarat

<!-- Akses, perkakas, dan izin yang dibutuhkan sebelum memulai. -->

## Deteksi / gejala

<!-- Apa yang diamati operator: peringatan, tanda galat, dasbor. -->

## Diagnosis

<!-- Pemeriksaan langkah demi langkah untuk memastikan masalah dan
     mempersempit penyebab. Sertakan perintah, query, atau tautan
     dasbor yang persis. -->

1. [langkah dan hasil yang diharapkan]
2. [langkah dan hasil yang diharapkan]

## Resolusi

<!-- Langkah konkret berurutan untuk memperbaiki atau memitigasi. Catat
     langkah apa pun yang berisiko atau tak dapat dibalik, dan cara
     memverifikasi keberhasilan. -->

1. [langkah]
2. [verifikasi pemulihan]

## Rollback

<!-- Cara membatalkan tindakan jika resolusi memperburuk keadaan. -->

## Eskalasi

<!-- Siapa yang dihubungi dan kapan mengeskalasi. On-call sekunder,
     tim pemilik, dan kontak vendor. -->

## Referensi

<!-- Dasbor, runbook terkait, dokumen arsitektur. -->
```

## README layanan / entri katalog layanan

```markdown
# [Nama layanan]

- Tim pemilik: [tim]
- On-call: [tautan rotasi]
- Tingkat / kekritisan: [Tingkat 1 | 2 | 3]
- Repositori: [tautan]
- Status: [Aktif | Usang]

## Apa yang dilakukannya

<!-- Satu paragraf tentang tanggung jawab layanan dan konsumennya. -->

## Arsitektur

<!-- Komponen kunci, dependensi (hulu dan hilir), dan tautan ke
     dokumen desain atau diagram. -->

## Antarmuka

- API / endpoint: [tautan ke spesifikasi]
- Peristiwa diterbitkan / dikonsumsi: [topik]
- Penyimpanan data: [basis data, cache, bucket]

## Runtime dan deployment

- Lingkungan: [dev, staging, prod]
- Cara men-deploy: [tautan jalur dan proses]
- Konfigurasi dan feature flag: [di mana dan bagaimana]

## Observabilitas

- Dasbor: [tautan]
- Peringatan: [tautan]
- Log: [tempat menemukannya]
- SLO: [tautan]

## Operasi

- Runbook: [tautan]
- Tugas umum: [penskalaan, restart, backfill]
- Isu dan keterbatasan yang diketahui: [catatan]

## Memulai (untuk kontributor baru)

<!-- Cara membangun, menguji, dan menjalankan secara lokal. -->

## Kontak

- Kanal Slack / obrolan: [tautan]
- Eskalasi: [jalur]
```

## Kebijakan SLO / anggaran galat

```markdown
# Kebijakan SLO dan anggaran galat: [Nama layanan atau perjalanan]

- Pemilik: [tim]
- Tanggal berlaku: [YYYY-MM-DD]
- Irama tinjauan: [mis. kuartalan]

## Service level indicator (SLI)

<!-- Definisikan setiap SLI secara presisi: besaran terukur, cara
     mengukurnya, dan dari mana (idealnya dari sudut pandang pengguna). -->

| SLI | Definisi | Sumber data |
|-----|----------|-------------|
| Ketersediaan | [mis. permintaan berhasil / total permintaan] | [sumber] |
| Latensi | [mis. proporsi permintaan di bawah X ms] | [sumber] |

## Objective (SLO)

| SLI | Target | Jendela pengukuran |
|-----|--------|--------------------|
| Ketersediaan | [mis. 99,9%] | [mis. 28 hari bergulir] |
| Latensi | [mis. 95% di bawah 300 ms] | [28 hari bergulir] |

## Anggaran galat

<!-- Ketidakandalan yang diizinkan: 100% dikurangi target, selama
     jendela. Nyatakan anggaran dalam istilah konkret (mis. menit/bulan). -->

- Anggaran: [jatah turunan]

## Kebijakan ketika anggaran habis

<!-- Konsekuensi yang disepakati. Jadikan konkret dan dapat ditegakkan. -->

- [mis. Bekukan rilis fitur non-kritis sampai anggaran pulih.]
- [mis. Prioritaskan kerja keandalan pada siklus perencanaan berikutnya.]
- [mis. Eskalasi ke pimpinan rekayasa jika dilanggar dua jendela berturut-turut.]

## Kebijakan ketika anggaran sehat

<!-- Risiko tambahan yang boleh diambil tim, mis. peluncuran lebih cepat. -->

## Peringatan

<!-- Peringatan laju pembakaran dan ambang yang terikat pada SLO ini. -->
```

## Entri register risiko

```markdown
## Risiko: [Judul singkat risiko]

- ID risiko: [ID]
- Tanggal diangkat: [YYYY-MM-DD]
- Pemilik: [nama atau peran yang bertanggung jawab mengelola risiko ini]
- Kategori: [keamanan | operasional | kepatuhan | keuangan | penyampaian | vendor]
- Status: [Terbuka | Dimitigasi | Diterima | Ditutup]

### Deskripsi

<!-- Nyatakan risiko sebagai: sebab -> peristiwa -> konsekuensi. Apa yang
     dapat terjadi, dan mengapa penting. -->

### Penilaian

- Kemungkinan: [Rendah | Sedang | Tinggi]
- Dampak: [Rendah | Sedang | Tinggi]
- Peringkat keseluruhan: [diturunkan dari kemungkinan x dampak]

### Kendali saat ini

<!-- Apa yang sudah mengurangi risiko ini hari ini. -->

### Rencana mitigasi

<!-- Tindakan terencana untuk mengurangi kemungkinan atau dampak, dengan
     pemilik dan tanggal. Jika menerima risiko, catat siapa yang
     menerimanya dan mengapa. -->

| Tindakan | Pemilik | Tanggal jatuh tempo | Status |
|----------|---------|---------------------|--------|
| [tindakan] | [nama] | [tanggal] | [status] |

### Tinjauan

- Tanggal tinjauan berikutnya: [YYYY-MM-DD]
- Keputusan / catatan: [persetujuan penerimaan atau perubahan apa pun]
```

## Satu halaman proyek / brief produk

```markdown
# [Nama proyek atau produk]: satu halaman

- Sponsor: [nama]
- Pemimpin: [nama]
- Tanggal: [YYYY-MM-DD]
- Status: [Gagasan | Disetujui | Berjalan | Terkirim]

## Masalah

<!-- Satu paragraf: masalah pelanggan atau bisnis, dan bukti bahwa ia
     nyata dan layak diselesaikan. -->

## Audiens

<!-- Siapa yang punya masalah ini dan siapa yang diuntungkan oleh
     penyelesaiannya. -->

## Solusi yang diusulkan

<!-- Deskripsi singkat apa yang akan kita bangun atau ubah. Jaga pada
     tingkat maksud, bukan detail implementasi. -->

## Mengapa sekarang

<!-- Alasan melakukannya sekarang dan bukan nanti. -->

## Metrik keberhasilan

<!-- Bagaimana kita tahu ini berhasil. Pilih hasil terukur. -->

- [metrik dan target]

## Cakupan

- Dalam cakupan: [apa yang akan kita lakukan]
- Di luar cakupan: [apa yang tidak akan kita lakukan]

## Risiko dan pertanyaan terbuka

<!-- Ketidakpastian utama dan dependensi. -->

## Rencana kasar dan tonggak

<!-- Fase tingkat tinggi dan perkiraan waktu. -->

## Biaya dan sumber daya

<!-- Orang, waktu, dan anggaran yang dibutuhkan. -->
```

## Catatan serah terima on-call

```markdown
# Serah terima on-call: [YYYY-MM-DD]

- Yang keluar: [nama]
- Yang masuk: [nama]
- Layanan: [nama]

## Status keseluruhan

<!-- Satu baris: tenang, berisik, atau ada isu berjalan. -->

## Insiden terbuka

<!-- Insiden aktif atau baru diselesaikan yang harus diketahui penanggap
     berikutnya, dengan tautan. -->

- [insiden, status, dan apa yang tersisa]

## Perubahan berjalan atau terencana

<!-- Deploy, migrasi, jendela pemeliharaan, atau eksperimen berjalan
     yang dapat memicu peringatan. -->

## Peringatan berisik atau flaky

<!-- Peringatan yang menyala dan arti sebenarnya, agar orang berikutnya
     tidak disesatkan. Catat pembisuan sementara dan masa berlakunya. -->

## Butir untuk diawasi

<!-- Metrik atau sistem yang cenderung ke arah mengkhawatirkan. -->

## Tindak lanjut tertunda

<!-- Tugas yang diserahkan ke giliran berikutnya, dengan tautan ke tiket. -->

## Catatan

<!-- Hal berguna lainnya: keanehan akses, isu vendor, konteks. -->
```

## Permintaan perubahan (untuk kontrol perubahan teregulasi)

```markdown
# Permintaan perubahan: [Judul perubahan]

- ID perubahan: [ID]
- Peminta: [nama]
- Tanggal diajukan: [YYYY-MM-DD]
- Jenis: [Standar | Normal | Darurat]
- Prioritas: [Rendah | Sedang | Tinggi]
- Status: [Diajukan | Disetujui | Ditolak | Diimplementasikan | Ditutup]

## Deskripsi perubahan

<!-- Apa yang berubah dan mengapa. Rujuk tiket atau persyaratan. -->

## Sistem dan komponen terdampak

<!-- Layanan, data, lingkungan, dan pengguna yang terdampak. -->

## Pembenaran dan dampak bisnis

<!-- Alasan perubahan dan dampak jika tidak dilakukan. -->

## Penilaian risiko

- Tingkat risiko: [Rendah | Sedang | Tinggi]
- Dampak potensial jika perubahan gagal: [deskripsi]
- Dampak pada keamanan, privasi, atau kepatuhan: [deskripsi]

## Rencana implementasi

<!-- Langkah berurutan, pihak bertanggung jawab, dan waktu. -->

## Rencana pengujian dan validasi

<!-- Bagaimana keberhasilan akan diverifikasi sebelum dan sesudah perubahan. -->

## Rencana pembatalan / rollback

<!-- Cara membalik perubahan jika gagal, dan waktu pemulihan. -->

## Jadwal

- Jendela yang diusulkan: [mulai dan selesai, dengan zona waktu]
- Downtime yang diharapkan: [durasi atau tidak ada]

## Persetujuan

| Peran | Nama | Keputusan | Tanggal |
|-------|------|-----------|---------|
| Pemilik perubahan | [nama] | [setuju/tolak] | [tanggal] |
| Peninjau teknis | [nama] | [setuju/tolak] | [tanggal] |
| Dewan penasihat perubahan | [nama] | [setuju/tolak] | [tanggal] |

## Tinjauan pasca-implementasi

<!-- Hasil, isu yang dijumpai, dan apakah pembatalan diperlukan. -->
```

## Garis besar Data Protection Impact Assessment (DPIA)

```markdown
# Data Protection Impact Assessment: [Nama aktivitas pemrosesan]

- Penilai: [nama]
- Tanggal: [YYYY-MM-DD]
- Peninjau: [DPO / kontak privasi]
- Status: [Draf | Ditinjau | Disetujui]

## 1. Deskripsi pemrosesan

<!-- Data pribadi apa yang diproses, bagaimana, oleh siapa, dan untuk
     tujuan apa. Sertakan aliran data dari pengumpulan hingga penghapusan. -->

- Subjek data: [siapa yang dibicarakan data]
- Kategori data: [jenis data pribadi, catat kategori khusus apa pun]
- Tujuan: [mengapa data diproses]
- Penerima dan prosesor: [siapa yang menerima atau menangani data]
- Periode retensi: [berapa lama data disimpan dan metode penghapusan]
- Transfer internasional: [tujuan dan mekanisme transfer]

## 2. Keperluan dan proporsionalitas

<!-- Apakah pemrosesan diperlukan untuk tujuan? Apakah ia opsi paling
     tidak mengganggu? Apa dasar hukum atau otoritasnya? -->

- Dasar hukum / otoritas: [dasar untuk setiap tujuan]
- Minimisasi data: [mengapa setiap kolom diperlukan]
- Justifikasi akurasi dan retensi: [catatan]
- Bagaimana hak subjek data didukung: [akses, penghapusan, dll.]

## 3. Konsultasi

<!-- Pemangku kepentingan, dan bila relevan subjek data, yang dikonsultasikan. -->

## 4. Risiko terhadap individu

<!-- Identifikasi risiko privasi dan beri peringkat masing-masing. -->

| Risiko terhadap individu | Kemungkinan | Keparahan | Keseluruhan |
|--------------------------|-------------|-----------|-------------|
| [mis. akses tidak sah ke data sensitif] | [R/S/T] | [R/S/T] | [peringkat] |

## 5. Langkah mengurangi risiko

<!-- Untuk setiap risiko, mitigasi dan risiko residual sesudahnya. -->

| Risiko | Langkah | Risiko residual | Diterima oleh |
|--------|---------|-----------------|---------------|
| [risiko] | [kendali] | [R/S/T] | [nama] |

## 6. Hasil dan persetujuan

- Risiko residual dapat diterima: [Ya | Tidak]
- Langkah disetujui oleh: [nama, peran]
- Konsultasi dengan otoritas pengawas diperlukan: [Ya | Tidak]
- Tanggal tinjauan: [YYYY-MM-DD]
```
