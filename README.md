# Quran Search

## Dataset

Dataset yang akan digunakan dalam tugas akhir berasal dari kaggle. Dataset tersebut merupakan dataset Al Quran besarta terjemahannya dalam Bahasa Indonesia.

Link Dataset : https://www.kaggle.com/datasets/zusmani/the-holy-quran/data 

## Permasalahan dan Tujuan Ekperimen
Al-Qur'an adalah pedoman yang berisi semua informasi yang diperlukan bagi umat Islam. Al-Quran terdiri dari 30 Juz, 114 surah dan 6326 ayat sehingga akan sangat sulit mencari kata-kata yang sesuai dengan topik yang diinginkan. Untuk mempermudah dan mempelajari Al-Quran secara efektif, diperlukan  sistem pencarian teks Al-Quran dalam bahasa Indonesia.

## Model dan Alur Eksperimen
Metode yang digunakan dalam penelitian ini dimulai dengan pembobotan dokumen menggunakan metode tf/idf. Prosesnya diawali dengan preprocessing dan ekstraksi dengan tujuan untuk mendapatkan syarat-syarat pada setiap dokumen. Term dokumen akan diproses sehingga diperoleh integrasi antara term frekuensi (tf) dan inverse document frekuensi (idf). Pencarian kemudian dilakukan dengan cara membandingkan kata kunci indeks dengan data tabel indeks.
Pemeringkatan dokumen harus dilakukan sedemikian rupa sehingga hasil yang ditampilkan diurutkan dari dokumen yang memiliki tingkat kemiripan paling tinggi hingga dokumen yang tingkat kemiripannya  paling rendah.
![image](https://github.com/mmahfud8/Quran-Search/assets/90414487/5fab43eb-f55e-4609-8df4-4b41b2aa0a68)


## Uji Model
Pengujian dilakukan dengan memasukan input term sebagai kata kunci dan mencocokannya data tabel indeks pada model dan mengurutkannya berdasarkan score atau nilai dengan kemiripan paling tinggi seperti pada gambar berikut.

![Screenshot 2024-01-07 050628](https://github.com/mmahfud8/Quran-Search/assets/90414487/c718b3e6-f7d2-46e0-b57a-a46dc17cee78)


## Proses Deployment
Deployment aplikasi mengunakan Flask dan saya hostingkan  di www.pythonanywhere.com .
Cara pengunaan aplikasi web ini yaitu dengan memasukkan kata atau kalimat kunci pada kolom input lalu klik submit maka akan muncul 50  hasil pencarian ayat Al-Quran yang mengandung kata atau kalimat yang dicari.

URL Deployment : https://bit.ly/4aKPfu4 
