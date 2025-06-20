# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal luas berkat reputasinya dalam mencetak lulusan-lulusan berkualitas. Selama lebih dari dua dekade berkiprah, institusi ini telah menghasilkan banyak alumni sukses yang berkontribusi di berbagai sektor profesional.

Namun demikian, di tengah keberhasilannya, Jaya Jaya Institut menghadapi tantangan serius berupa tingginya angka mahasiswa yang tidak menyelesaikan studi atau dropout. Fenomena ini bukan hanya berdampak pada reputasi akademik institusi, tetapi juga pada efektivitas sistem pembelajaran, distribusi sumber daya, serta keberhasilan program pendidikan secara menyeluruh.

Sebagai bentuk komitmen terhadap peningkatan mutu pendidikan dan keberhasilan peserta didik, Jaya Jaya Institut berinisiatif untuk mengembangkan sistem pendeteksian dini terhadap mahasiswa yang berpotensi dropout. Dengan pendekatan berbasis data, institusi berharap dapat melakukan intervensi yang lebih cepat dan tepat bagi mahasiswa yang berisiko, melalui pemberian bimbingan atau dukungan yang disesuaikan.

Untuk mendukung upaya tersebut, pihak institusi menyediakan dataset yang berisi informasi akademik, demografis, dan sosial ekonomi mahasiswa, serta catatan performa akademik pada tahun pertama. Melalui data ini, diharapkan dapat dilakukan analisis untuk mengidentifikasi pola-pola yang menjadi indikator risiko putus studi.

### Permasalahan Bisnis
Meskipun Jaya Jaya Institut telah menunjukkan reputasi yang baik dalam menghasilkan lulusan berkualitas sejak tahun 2000, institusi ini kini menghadapi tantangan serius berupa tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout). Fenomena ini tidak hanya berdampak pada citra dan reputasi akademik, tetapi juga menimbulkan inefisiensi dalam penggunaan sumber daya pendidikan seperti beasiswa, fasilitas pembelajaran, serta alokasi tenaga pengajar.

Saat ini, pihak institusi belum memiliki sistem yang efektif untuk mendeteksi secara dini mahasiswa yang berpotensi mengalami dropout. Ketidaktepatan dalam mengidentifikasi risiko ini menyebabkan keterlambatan intervensi yang dapat memperparah tingkat kegagalan studi.

### Cakupan Proyek
Berikut cakupan proyek yan akan dikerjakan: 
1. Melakukan analisa terhadap dataset untuk melihat karakteristik mahasiswa DO dan mencari faktor-faktor yang mempengaruhi dropout
2. Membuat sebuah model machine learning untuk mengklasifikasikan siswa apakah akan ada kemungkinan dropout atau tidak
3. Membuat aplikasi sederhana untuk memprediksi status mahasiswa yang akan di deploy ke streamlit
4. Membangun dashboard untuk memvisualisasikan dataset yang ada agar mudah untuk melakukan analisa
5. Membuat sebuah rekomendasi atau action item untuk yang dapat dilakukan.

### Persiapan
Sumber data: Persiapan https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance 

**Setup environment**:
1. setup environment - Anaconda
```
conda create --name data_analisys python=3.10
conda activate data_analisys
pip install -r requirements.txt
```
2. setup environment - Shell/terminal
```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard
Dashboard Students Performance dengan Looker Studio 
link : https://lookerstudio.google.com/s/gOuP4UrF0_Q 
![dashboard](https://github.com/user-attachments/assets/6bc232d8-b2cf-4dd8-a26f-273d0c8fd575)
### Bagian-Bagian Dashboard

#### Filter Interaktif
Tersedia filter yang memungkinkan pengguna untuk menyaring data berdasarkan:
- **Marital_status**: Status pernikahan
- **Age_at_enrollment**: Usia saat mendaftar
- **Beasiswa**: Status penerimaan beasiswa
- **Prodi**: Program studi
- **Hutang**: Status tunggakan

#### 2. Ringkasan Status Siswa
- **Total Siswa**: 4.424
- **Enroll**: 794 siswa masih aktif/terdaftar
- **Graduate**: 2.209 siswa telah lulus
- **Dropout**: 1.421 siswa tidak menyelesaikan studi

> Ini menunjukkan bahwa sekitar **32%** dari siswa mengalami dropout – angka yang cukup signifikan.

#### 3. Pie Chart – Persentase Status Siswa
Menampilkan perbandingan persentase antara mahasiswa yang lulus, dropout, dan masih aktif secara visual.

#### 4. Distribusi Berdasarkan Gender
- **Perempuan** memiliki jumlah mahasiswa lebih banyak.
- Baik laki-laki maupun perempuan sama-sama menunjukkan dropout yang tinggi.

#### 5. Distribusi Berdasarkan Beasiswa
- Mahasiswa **tanpa beasiswa** memiliki dropout lebih tinggi.
- Mahasiswa **dengan beasiswa** cenderung lebih banyak yang lulus.

#### 6. Distribusi Berdasarkan Tunggakan
- Mahasiswa **dengan tunggakan** menunjukkan dropout yang signifikan.
- Mahasiswa **tanpa tunggakan** lebih banyak yang berhasil menyelesaikan studi.

#### 7. Jumlah Dropout Berdasarkan Course
Top 5 program studi dengan dropout tertinggi:
1. **Management (Evening)** - 136
2. **Management (Reguler)** - 134
3. **Nursing** - 118
4. **Journalism and Communication** - 101
5. **Tourism** - 96

---

#### Insight Umum
- **Tingkat dropout cukup tinggi** (32%) → butuh intervensi khusus.
- **Faktor finansial** seperti beasiswa dan tunggakan berpengaruh terhadap dropout.
- Beberapa **program studi perlu evaluasi lebih dalam** terkait tingkat keberhasilan akademik.
"""


## Menjalankan Sistem Machine Learning
Berikut langkah-langkah untuk menjalankan Sistem Machine Learning yang telah dibangun
1. Silakan buka link streamlite pada link berikut: https://submissionnds2.streamlit.app/
2. pada halaman awal Anda akan diminta untuk memilih course
   ![image](https://github.com/user-attachments/assets/48eeec62-216c-4de9-bc0c-5e5a8d8fb8ec)
3. Selanjutnya silakan isi isian dan pilian dari inputan variabel tersebut, dimana terdapat 15 inputan variabel seperti dibawa ini:
![2a](https://github.com/user-attachments/assets/0b32035c-7642-453c-a86d-eb2dec2bf936)
4. jika suda liat pada bagian bawah terdapat tabel summari dari inputan diatas:
   ![2c](https://github.com/user-attachments/assets/4fe58ed9-c7a3-4e29-9c48-6f2f3a753654)
5. Klik tombol predict pada bagian bawa, maka sistem akan memunculkan hasil prediksinya:
   ![2d](https://github.com/user-attachments/assets/3714b676-5d51-4d3d-b4c3-c89a01647c28)
   
## Conclusion
Berdasarkan hasil analisa yang tela dilakukan Proyek ini berhasil mengidentifikasi dan menganalisis faktor-faktor utama yang memengaruhi tingkat dropout mahasiswa di Jaya Jaya Institut, berdasarkan data akademik, sosial, dan ekonomi yang tersedia sejak awal pendaftaran. 
Beberapa temuan utama dari analisis dan dashboard yang dibangun meliputi:
1. Tingkat dropout mahasiswa cukup tinggi, yaitu sekitar 32% dari total mahasiswa yang dianalisis.
2. Mahasiswa yang tidak menerima beasiswa dan memiliki tunggakan pembayaran cenderung lebih rentan terhadap risiko dropout.
3. Program studi seperti Manajemen (Reguler & Evening), Keperawatan, serta Jurnalistik menunjukkan angka dropout tertinggi, sehingga memerlukan perhatian dan evaluasi khusus.
4. Dashboard interaktif berbasis Looker Studio yang telah dikembangkan memungkinkan pihak kampus untuk menyaring dan memantau performa mahasiswa berdasarkan berbagai filter penting seperti usia, status sosial, hingga program studi.

Selain itu, sistem prediksi berbasis machine learning juga berhasil dibangun dan di-deploy melalui aplikasi Streamlit untuk membantu mendeteksi potensi dropout sejak dini.


### Rekomendasi Action Items
Berikut rekomendasi Item yang dapat dilakukan oleh jaya-jaya institute: 
1. Meningkatkan akses terhadap beasiswa bagi mahasiswa dari kelompok rentan secara sosial-ekonomi.
2. Menyediakan program bimbingan dan mentoring khusus untuk mahasiswa yang masuk dalam kelompok berisiko tinggi dropout.
3. Melakukan evaluasi akademik pada program studi dengan tingkat dropout tinggi untuk memahami tantangan pembelajaran yang dihadapi mahasiswa.
4. Melibatkan unit layanan konseling dan keuangan untuk memberikan edukasi serta pendampingan dalam hal pembayaran biaya kuliah.
5. Mengevaluasi course yang memiliki tingkat dropout tinggi agar segera dievaluasi baik dari segi kurikulum, kesempatan kesempatan kerja setelah lulus dan faktor-faktor lainnya

