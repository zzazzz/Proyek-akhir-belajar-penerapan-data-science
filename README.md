# Business Understanding

## Latar Belakang Bisnis
Jaya Jaya Institut adalah institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang sangat baik dalam mencetak lulusan. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut menghadapi tantangan terkait tingginya angka siswa yang *dropout*. Jumlah *dropout* yang tinggi dapat merusak reputasi institusi, mengurangi pendapatan, serta menurunkan kepercayaan masyarakat dan calon mahasiswa terhadap kualitas pendidikan yang ditawarkan.

Untuk itu, Jaya Jaya Institut ingin mengidentifikasi siswa yang berpotensi *dropout* lebih awal agar dapat memberikan bimbingan atau intervensi yang tepat waktu. Dengan pendekatan berbasis data, institusi ini berharap dapat mengurangi jumlah siswa yang *dropout* dan menjaga reputasi serta kualitas pendidikan.

## Permasalahan Bisnis
1. **Tingginya Jumlah Siswa yang Dropout**  
   Jumlah *dropout* yang tinggi menjadi masalah bagi reputasi dan daya tarik institusi. Hal ini berpotensi merusak citra pendidikan yang diberikan serta menurunkan pendaftar baru.

2. **Tidak Ada Sistem Pemantauan yang Efektif**  
   Tanpa sistem yang dapat memantau performa siswa secara real-time, institusi kesulitan dalam mendeteksi siswa yang berpotensi *dropout* lebih awal. Hal ini menghambat proses intervensi yang dapat mencegah *dropout*.

3. **Kesulitan dalam Mengidentifikasi Faktor-faktor Penyebab Dropout**  
   Jaya Jaya Institut belum memiliki pemahaman yang jelas tentang faktor-faktor yang mempengaruhi keputusan siswa untuk *dropout*. Tanpa pemahaman yang mendalam, sulit untuk menemukan solusi yang tepat.

## Cakupan Proyek
1. **Data Preparation & Exploratory Data Analysis (EDA)**  
   Mengumpulkan, membersihkan, dan menganalisis data untuk memahami faktor-faktor yang berpengaruh terhadap *dropout*.

2. **Modeling**  
   Mengembangkan model prediktif menggunakan machine learning untuk memprediksi siswa yang berpotensi *dropout*.

3. **Model Evaluation**  
   Mengevaluasi kinerja model untuk memastikan bahwa model dapat memprediksi dengan akurat siswa yang berisiko *dropout*.

4. **Dashboard Development**  
   Membuat dashboard interaktif untuk membantu Jaya Jaya Institut dalam memantau performa siswa secara real-time dan melakukan intervensi dengan lebih efektif.

5. **Rekomendasi Tindakan**  
   Memberikan rekomendasi berdasarkan hasil analisis untuk mengurangi jumlah *dropout* dan meningkatkan kualitas pendidikan di Jaya Jaya Institut.

### Persiapan

Sumber data: [Dicoding](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

#### Setup Environment

Ikuti langkah-langkah berikut untuk menyiapkan environment pada proyek ini:

#### 1. Unduh dan Ekstrak File
Unduh file zip dari repositori ini dan ekstrak di direktori pilihan Anda.

#### 2. Buka Terminal atau Command Prompt (CMD)
Buka terminal atau command prompt di komputer Anda.

#### 3. Buat Virtual Environment Baru
Buat virtual environment baru menggunakan conda dengan perintah berikut:

```bash
conda create --name <nama-venv> python=3.10
```
#### 4. Aktifkan Virtual Environment
Aktifkan environment yang baru dibuat dengan perintah berikut:

```bash
conda activate <nama-venv>
```

#### 5. Install Semua Library yang Dibutuhkan
Install semua library yang diperlukan untuk proyek ini dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
```

## Business Dashboard: Prediksi Dropout Mahasiswa - Jaya Jaya Institut

### Deskripsi Proyek

Proyek ini bertujuan untuk membangun sebuah sistem prediksi yang dapat membantu Jaya Jaya Institut dalam mengidentifikasi mahasiswa yang berisiko mengalami dropout. Sistem ini menggunakan berbagai faktor yang berhubungan dengan karakteristik mahasiswa, kinerja akademis, dan kondisi sosial-ekonomi untuk memprediksi apakah seorang mahasiswa berisiko untuk keluar dari institusi pendidikan.

Salah satu bagian dari sistem ini adalah **Business Dashboard**, yang akan membantu pihak institut dalam memvisualisasikan data dan membuat keputusan berbasis data mengenai risiko dropout mahasiswa.

#### Penjelasan Dashboard

Dashboard ini akan memberikan gambaran visual yang jelas tentang faktor-faktor yang berpotensi mempengaruhi status dropout mahasiswa di Jaya Jaya Institut. Dengan menggunakan data yang telah dikumpulkan, dashboard bertujuan untuk membantu pihak institut dalam mengidentifikasi dan memonitor faktor-faktor yang berhubungan dengan kemungkinan seorang mahasiswa untuk tidak menyelesaikan pendidikannya.

#### Kolom Data yang Digunakan

1. Faktor Demografis dan Sosial
- **Marital_status**: Status pernikahan mahasiswa. Mahasiswa yang sudah menikah mungkin memiliki lebih banyak tanggung jawab, yang bisa mempengaruhi kelangsungan studi mereka.
- **Gender**: Jenis kelamin mahasiswa, yang mungkin berpengaruh terhadap dinamika sosial dan ekonomi mahasiswa.
- **Nacionality**: Kewarganegaraan mahasiswa. Mahasiswa internasional mungkin menghadapi tantangan tambahan dalam menyesuaikan diri dengan kehidupan akademis dan sosial di kampus.
- **Age_at_enrollment**: Usia mahasiswa pada saat pendaftaran. Mahasiswa yang lebih tua atau lebih muda dari rata-rata mungkin memiliki tantangan yang berbeda dalam menyelesaikan studi.

2. Latar Belakang Pendidikan
- **Mothers_occupation**, **Fathers_occupation**: Pekerjaan orang tua. Pekerjaan orang tua dapat mempengaruhi status ekonomi keluarga dan tingkat dukungan yang tersedia untuk mahasiswa.
- **Debtor**: Status keuangan mahasiswa, apakah mereka memiliki utang yang perlu dibayar. Ini dapat mempengaruhi kemampuan mahasiswa untuk melanjutkan pendidikan jika mereka kesulitan dalam hal finansial.
- **Tuition_fees_up_to_date**: Status pembayaran uang kuliah mahasiswa. Mahasiswa yang memiliki masalah dalam pembayaran uang kuliah berisiko lebih tinggi untuk keluar dari sekolah.

3. Kehadiran dan Kinerja Akademik
- **Curricular_units_1st_sem_enrolled**, **Curricular_units_2nd_sem_enrolled**: Jumlah unit mata kuliah yang diambil selama semester pertama dan kedua. Jumlah mata kuliah yang diambil dapat menunjukkan beban akademik dan kesulitan dalam menyelesaikan studi.

4. Kondisi Ekonomi dan Sosial
- **Unemployment_rate**: Tingkat pengangguran di daerah tempat mahasiswa tinggal. Mahasiswa dari daerah dengan tingkat pengangguran tinggi mungkin menghadapi kesulitan dalam membiayai pendidikan mereka.
- **Inflation_rate**: Tingkat inflasi yang mempengaruhi biaya hidup dan biaya pendidikan. Inflasi yang tinggi dapat meningkatkan beban keuangan mahasiswa.
- **GDP**: Produk Domestik Bruto (PDB) yang dapat memberikan gambaran tentang stabilitas ekonomi dan ketersediaan peluang pekerjaan.

#### Target yang Diperoleh
- **Status (Y)**: Kolom ini menunjukkan status mahasiswa, apakah mereka menyelesaikan pendidikannya atau mengalami dropout. Dengan memprediksi nilai dari kolom ini, institusi dapat mengidentifikasi mahasiswa yang berisiko untuk dropout dan memberikan perhatian serta dukungan yang diperlukan.

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototipe machine learning yang telah dibuat, Anda dapat melakukannya baik di lokal maupun melalui tautan Streamlit. Berikut adalah langkah-langkah yang perlu diikuti untuk menjalankan prototipe secara lokal:

1. Buka terminal pada virtual environment yang telah Anda buat sebelumnya.
2. Pastikan Anda berada di direktori yang berisi berkas-berkas yang telah diekstrak sebelumnya, terutama berkas **app.py**. Jika belum berada di direktori yang tepat, Anda bisa menggunakan perintah berikut:

```
cd path/to/destination/directory
```

3. Setelah direktorinya sesuai, bisa menjalankan perintah di bawah

```
streamlit run app.py
```

4. Setelah berhasil dijalankan, masukkan data yang sesuai kemudian klik tombol **Predict** untuk mengetahui status siswa tersebut.

Jika Anda lebih memilih untuk menjalankan aplikasi melalui link, Anda dapat mengaksesnya di [Jaya Jaya Institute App](https://proyek-akhir-belajar-penerapan-data-science-dwy4ygvksyoszytbfp.streamlit.app/)

## Conclusion

Dari analisis dan pemodelan yang telah dilakukan, dapat disimpulkan bahwa **dropout mahasiswa** di **Jaya Jaya Institut** dipengaruhi oleh berbagai faktor yang dapat dibagi dalam beberapa kategori utama, antara lain:

1. **Faktor Demografis dan Sosial**: Status pernikahan, jenis kelamin, kewarganegaraan, dan usia pada saat pendaftaran ternyata dapat mempengaruhi risiko seorang mahasiswa untuk mengalami dropout. Misalnya, mahasiswa yang sudah menikah atau lebih tua dari rata-rata memiliki kecenderungan lebih tinggi untuk menghadapi kesulitan dalam melanjutkan studi karena adanya tanggung jawab tambahan di luar akademik.

2. **Latar Belakang Pendidikan**: Pekerjaan orang tua dan status keuangan mahasiswa juga merupakan faktor penting dalam menganalisis risiko dropout. Mahasiswa dengan orang tua yang tidak memiliki pekerjaan tetap atau dengan masalah keuangan lebih rentan untuk mengalami kesulitan dalam melanjutkan pendidikan mereka. Selain itu, masalah pembayaran uang kuliah menjadi indikator penting yang perlu diperhatikan.

3. **Kehadiran dan Kinerja Akademik**: Jumlah mata kuliah yang diambil setiap semester juga berpengaruh terhadap tingkat kelulusan mahasiswa. Mahasiswa dengan beban mata kuliah yang lebih tinggi atau yang mengalami kesulitan dalam menyelesaikan tugas akademik lebih cenderung mengalami masalah dalam mempertahankan studi mereka.

4. **Kondisi Ekonomi dan Sosial**: Faktor eksternal seperti tingkat pengangguran, inflasi, dan PDB wilayah tempat mahasiswa tinggal juga berperan dalam membentuk kemampuan mahasiswa untuk melanjutkan pendidikan mereka. Kondisi ekonomi yang buruk di daerah asal dapat meningkatkan kesulitan finansial mahasiswa.

Dengan mempertimbangkan faktor-faktor ini, proyek ini dapat memberikan **insight yang berharga** untuk membantu pihak Jaya Jaya Institut dalam mengidentifikasi mahasiswa yang berisiko untuk dropout dan memberikan intervensi lebih awal.

Dengan adanya **dashboard interaktif**, pihak institut dapat lebih mudah memonitor faktor-faktor risiko dan mengambil langkah-langkah yang tepat untuk membantu mahasiswa yang membutuhkan dukungan lebih. Melalui prediksi berbasis data, Jaya Jaya Institut dapat lebih proaktif dalam merancang program yang dapat meningkatkan tingkat kelulusan mahasiswa.

### Tujuan

Dashboard ini akan membantu pihak Jaya Jaya Institut untuk:
- Memantau faktor-faktor yang berkontribusi terhadap dropout mahasiswa.
- Mengidentifikasi mahasiswa yang berisiko dan memberikan bimbingan atau dukungan yang sesuai.
- Membuat keputusan yang berbasis data untuk meningkatkan tingkat kelulusan mahasiswa.

Dengan adanya dashboard yang komprehensif dan interaktif, diharapkan Jaya Jaya Institut dapat lebih proaktif dalam menangani masalah dropout mahasiswa dan meningkatkan tingkat kelulusan mereka.
