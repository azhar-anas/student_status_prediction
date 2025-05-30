# Proyek Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik dalam menghasilkan lulusan berkualitas. Namun, dalam beberapa tahun terakhir, institusi menghadapi tantangan serius berupa meningkatnya jumlah siswa yang tidak menyelesaikan pendidikannya atau dropout. Hal ini tidak hanya memengaruhi reputasi akademik institusi, tetapi juga mencerminkan kurang optimalnya intervensi dini terhadap siswa yang berpotensi gagal.

Untuk mengatasi hal tersebut, pihak manajemen Jaya Jaya Institut berinisiatif untuk memanfaatkan data siswa yang telah dikumpulkan guna mendeteksi secara dini siswa yang berisiko mengalami dropout. Dengan pendekatan berbasis data science, pihak institusi berharap dapat mengambil langkah proaktif seperti bimbingan akademik, konseling, dan bantuan finansial untuk meningkatkan tingkat kelulusan.

### Permasalahan Bisnis
Berdasarkan pemahaman bisnis yang telah diuraikan, berikut adalah permasalahan utama yang dihadapi:
1. Tingginya angka dropout siswa yang berdampak negatif terhadap reputasi institusi.
2. Tidak adanya sistem deteksi dini berbasis data untuk mengidentifikasi siswa yang berisiko dropout.
3. Minimnya insight berbasis data untuk pengambilan keputusan strategis dalam mendukung siswa.

### Cakupan Proyek
Proyek ini meliputi beberapa tahap utama berikut:
1. **Eksplorasi dan Analisis Awal Data**: Menelaah dataset `data.csv` dari [Students Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) untuk memahami profil dan data siswa serta distribusi dan korelasinya terhadap status akhir (graduate, enrolled, dropout). Hal-hal tersebut seperti:
   - d
   - Melakukan analisis statistik (seperti uji chi-squared) untuk mengidentifikasi fitur yang signifikan terhadap status siswa.
   - Menyusun visualisasi untuk menunjukkan hubungan antara status siswa dan berbagai faktor latar belakang serta performa akademik.
2. **Pembersihan dan Persiapan Data**: Menyiapkan data agar siap dianalisis, termasuk penanganan data yang berkorelasi rendah, encoding fitur kategorikal, normalisasi fitur numerik, dan upsampling data.
3. **Pembuatan Dashboard Analitik**: Menyediakan dashboard interaktif yang menyajikan insight terkait performa siswa, fitur risiko dropout, serta filter untuk eksplorasi lebih lanjut oleh pihak institusi.
4. **Pembuatan Model Prediksi**: Mengembangkan model machine learning yang mampu memprediksi status akhir siswa (graduate, enrolled, dropout) secara akurat menggunakan data yang ada serta membuat prototype-nya menggunakan Streamlit Cloud Community.
5. **Kesimpulan dan Rekomendasi Strategis**: Menyusun laporan hasil analisis serta strategi rekomendasi berbasis data untuk membantu institusi dalam menekan angka dropout.

### Persiapan
**Sumber data**:
Dataset yang digunakan dalam proyek ini adalah [Dataset Students Performance](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) sebagaimana direkomendasikan dalam petunjuk submission proyek. Dataset ini berisi detail siswa seperti nilai, jumlah SKS lulus, biodata, dan status siswa seperti Dropout (dikeluarkan), Enrolled (masih melanjutkan studi), dan Graduate (Sudah lulus). Berikut detail deskripsi setiap fiturnya:
1. `Marital status` (Kategorikal): Status pernikahan siswa (1–single, 2–married, dst.).
2. `Application mode` (Kategorikal): Metode pendaftaran yang digunakan siswa.
3. `Application order` (Kategorikal): Urutan pilihan program studi saat mendaftar (0 = pilihan pertama, 9 = pilihan terakhir).
4. `Course` (Kategorikal): Program studi yang diambil siswa.
5. `Daytime/evening attendance` (Kategorikal): Waktu kehadiran kuliah (1 = siang, 0 = malam).
6. `Previous qualification` (Kategorikal): Kualifikasi terakhir sebelum kuliah (mis. SMA, S1, S2, dll).
7. `Previous qualification (grade)` (Numerikal): Nilai dari kualifikasi sebelumnya (0–200).
8. `Nacionality` (Kategorikal): Kewarganegaraan siswa.
9. `Mother's qualification` (Kategorikal): Tingkat pendidikan ibu siswa.
10. `Father's qualification` (Kategorikal): Tingkat pendidikan ayah siswa.
11. `Mother's occupation` (Kategorikal): Pekerjaan ibu siswa.
12. `Father's occupation` (Kategorikal): Pekerjaan ayah siswa.
13. `Admission grade` (Numerikal): Nilai masuk universitas (0–200).
14. `Displaced` (Kategorikal): Apakah siswa berasal dari luar daerah (1 = ya, 0 = tidak).
15. `Educational special needs` (Kategorikal): Apakah siswa memiliki kebutuhan khusus (1 = ya, 0 = tidak).
16. `Debtor` (Kategorikal): Apakah siswa memiliki tunggakan pembayaran (1 = ya, 0 = tidak).
17. `Tuition fees up to date` (Kategorikal): Apakah pembayaran uang kuliah siswa lancar (1 = ya).
18. `Gender` (Kategorikal): Jenis kelamin siswa (1 = laki-laki, 0 = perempuan).
19. `Scholarship holder` (Kategorikal): Apakah siswa menerima beasiswa (1 = ya).
20. `Age at enrollment` (Numerikal): Usia siswa saat mendaftar.
21. `International` (Kategorikal): Apakah siswa merupakan siswa internasional (1 = ya).
22. `Curricular units 1st sem (credited)` (Numerikal): Jumlah mata kuliah yang diakui di semester 1.
23. `Curricular units 1st sem (enrolled)` (Numerikal): Jumlah mata kuliah yang diambil di semester 1.
24. `Curricular units 1st sem (evaluations)` (Numerikal): Jumlah mata kuliah yang dinilai di semester 1.
25. `Curricular units 1st sem (approved)` (Numerikal): Jumlah mata kuliah yang lulus di semester 1.
26. `Curricular units 1st sem (grade)` (Numerikal): Rata-rata nilai semester 1 (0–20).
27. `Curricular units 1st sem (without evaluations)` (Numerikal): Jumlah mata kuliah tanpa penilaian di semester 1.
28. `Curricular units 2nd sem (credited)` (Numerikal): Jumlah mata kuliah yang diakui di semester 2.
29. `Curricular units 2nd sem (enrolled)` (Numerikal): Jumlah mata kuliah yang diambil di semester 2.
30. `Curricular units 2nd sem (evaluations)` (Numerikal): Jumlah evaluasi mata kuliah di semester 2.
31. `Curricular units 2nd sem (approved)` (Numerikal): Jumlah mata kuliah yang lulus di semester 2.
32. `Curricular units 2nd sem (grade)` (Numerikal): Rata-rata nilai semester 2 (0–20).
33. `Curricular units 2nd sem (without evaluations)` (Numerikal): Jumlah mata kuliah tanpa penilaian di semester 2.
34. `Unemployment rate` (Numerikal): Persentase tingkat pengangguran (%).
35. `Inflation rate` (Numerikal): Persentase tingkat inflasi (%).
36. `GDP` (Numerikal): Produk Domestik Bruto (Gross Domestic Product).
37. `Target` (Kategorikal, Target): Status akhir siswa (dropout, enrolled, graduate).


**Setup Environtment**:
   - Setup Environment - Anaconda -> Install Anaconda Manager terlebih dahulu lalu buka terminal dan jalankan perintah berikut:
      ```bash
      conda create --name ml_kit python=3.11
      conda activate ml_kit
      pip install -r requirements.txt
      ```
   - Setup Environment - Shell/Terminal (Tidak perlu dilakukan jika sudah install dari Anaconda)
      ```bash
      pip install pipenv
      pipenv install
      pipenv shell
      pip install -r requirements.txt
      ```
   - Setup Environment - Docker & Metabase -> Install docker terlebih dahulu lalu buka terminal dari docker dan jalankan perintah berikut:
      ```bash
      docker pull metabase/metabase:v0.46.4
      docker run -p 3000:3000 --name metabase metabase/metabase:v0.46.4
      ```

## Business Dashboard
Dashboard telah dirancang untuk memantau performa siswa berdasarkan berbagai indikator akademik dan status pendidikan yang ditemukan saat proses analisis. Berikut adalah penjelasan tiap komponennya:

#### 1. Rata-rata Usia siswa saat Pendaftaran
Menunjukkan bahwa siswa yang dropout memiliki usia rata-rata tertinggi, diikuti oleh yang masih enrolled dan graduate. Ini mengindikasikan bahwa usia saat masuk mungkin mempengaruhi keberhasilan studi.

#### 2. Distribusi Status siswa
Visualisasi donut/pie chart menunjukkan proporsi siswa dengan status:
- **Graduate**: 50%
- **Dropout**: 32%
- **Enrolled**: 18%

Total siswa: 4.424 orang.

#### 3. Rata-rata SKS Lulus
Menampilkan perbandingan SKS yang lulus pada semester 1 dan 2. siswa yang **graduate** memiliki SKS paling banyak yang lulus di kedua semester, sedangkan **dropout** paling sedikit.

#### 4. Rata-rata Nilai Semester
siswa yang **graduate** memiliki nilai rata-rata tertinggi di kedua semester, disusul **enrolled** dan **dropout**. Ini menunjukkan korelasi antara performa akademik awal dengan kelulusan.

#### 5. Status Siswa berdasarkan Program Studi
Stacked bar chart menunjukkan perbandingan status siswa pada tiap program studi. Beberapa program seperti *Journalism and Communication* dan *Biofuel Production Technologies* memiliki proporsi dropout yang tinggi, sedangkan program seperti *Informatics Engineering* memiliki banyak graduate.

Dashboard diharapkan dapat membantu pihak akademik dalam mendeteksi program studi dengan tingkat dropout yang tinggi, menilai korelasi antara usia, SKS, dan nilai terhadap kelulusan, serta mengambil keputusan berbasis data untuk melakukan intervensi akademik yang lebih tepat sasaran.Berikut cara untuk Mengakses Dashboard Metabase yang telah dibuat:

1. Buka Docker, lalu buka terminalnya dan ketik perintah berikut: 
   ```bash
   docker start -a metabase
   ```
2. Buka browser lalu ketik `http://localhost:3000/`
3. Login dengan detail credential berikut:
   - username:`azharanas2202@gmail.com`
   - password: `root123`
4. Load file `metabase.db.mv.db`

## Menjalankan Sistem Machine Learning
Sistem Machine Learning dapat diakses dengan cara berikut:
   - Menjalankan secara lokal:
      ```bash
      streamlit run App.py
      ```
   - Menjalankan secara remote/online melalui Streamlit Cloud Comunity:
      
      Akses URL berikut: [Prediksi Status Siswa Jaya Jaya Institut](https://studentstatusprediction-gufymrfudm2uux6fuj9ydc.streamlit.app/)

## Conclusion
Berdasarkan proses EDA, analisis korelasi fitur numerik, analisis Uji Chi-Squared fitur kategorikal, dan hasil feature importance dari model Random Forest yang telah melalui proses feature selection menggunakan RFE, ditemukan bahwa:
1. **Fitur akademik (grade dan approval)** di semester pertama dan kedua, khususnya `Curricular_units_2nd_sem_approved` dan `Curricular_units_2nd_sem_grade`, memiliki pengaruh paling dominan terhadap prediksi status akhir siswa. Hal Ini menunjukkan bahwa **kinerja akademik** merupakan indikator utama kelulusan.
2. **Nilai tes masuk (`Admission_grade`)** dan **usia saat mendaftar (`Age_at_enrollment`)** juga turut berperan penting. Usia yang lebih tinggi cenderung berkorelasi negatif dengan kelulusan, mungkin terkait dengan tanggung jawab eksternal atau faktor ekonomi.
3. Dari sisi fitur kategorikal, uji Chi-Squared menunjukkan bahwa **faktor sosial-ekonomi dan administratif** seperti `Tuition_fees_up_to_date`, `Debtor`, `Scholarship_holder`, dan `Parental_education/occupation` memiliki asosiasi yang signifikan terhadap `Status`. Hal ini memperkuat peran **dukungan finansial dan lingkungan sosial** dalam keberhasilan studi siswa.

## Rekomendasi Action Items

1. **Intervensi Dini bagi siswa dengan Kinerja Akademik Rendah**
   - Terapkan sistem peringatan dini berdasarkan fitur penting seperti `Curricular_units_2nd_sem_approved` dan `Curricular_units_2nd_sem_grade`. Sistem tersebut dapat menggunakan machine learning.
   - Sediakan mentoring atau program remedial bagi siswa yang memiliki kinerja rendah di semester awal.

2. **Pendampingan Khusus untuk siswa Berisiko Tinggi**
   - Identifikasi siswa dengan usia lebih tua, sudah menikah, atau berasal dari latar belakang ekonomi rentan (misalnya memiliki tunggakan atau bukan penerima beasiswa).
   - Berikan konseling akademik dan finansial secara berkala.

3. **Kebijakan Dukungan Keuangan**
   - Pertimbangkan untuk memperluas skema beasiswa dan insentif pembayaran uang kuliah tepat waktu.
   - Edukasi keuangan sejak awal perkuliahan untuk mencegah munculnya status `Debtor`.

4. **Evaluasi Kurikulum dan Metode Pengajaran**
   - Tinjau kembali beban kurikulum pada semester awal, karena performa awal terbukti krusial terhadap status akhir siswa.

5. **Analitik Berbasis Data untuk Pengambilan Keputusan**
   - Gunakan model machine learning dan dashboard yang telah dibangun untuk mendukung kebijakan institusi pendidikan dalam deteksi dini dan intervensi berbasis data (data-driven decision making).
