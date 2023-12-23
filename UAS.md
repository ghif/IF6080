# Tugas UAS Praktek Semester I 2023 / 2024 - IF6080 Pembelajaran Mesin Probabilistik
Total nilai: 40 - open book/reference

Waktu pengerjaan: 5 jam

## Latar Belakang
Pada tahun 2012, deep learning menghasilkan terobosan pada bidang Computer Vision dimana model deep learning bernama AlexNet menjadi pemenang pada perlombaan ImageNet object recognition. Setelah itu berbagai model deep learning serupa dengan arsitektur yang lebih kompleks banyak bermunculan dan tersedia di Internet, sebagai contoh, GoogleNet, VGGNet, ResNet, XCeption, ViT, dan sebagainya.

Model-model yang sudah di pralatih dengan dataset ImageNet kemudian dikenal dengan istilah backbone atau foundational model, yang ternyata sangat efektif untuk digunakan dalam konteks transfer learning: mengaplikasikan model backbone pralatih pada domain atau dataset lain yang biasanya memiliki jumlah data jauh lebih sedikit dibandingkan ImageNet.

Secara umum, terdapat 2 pendekatan untuk melakukan transfer learning:
1.	Metode **feature extraction**: menggunakan backbone model hanya sebagai feature extractor, lalu melatih classifier pada domain/dataset yang dituju.
2.	Metode **finetuning**: menggunakan backbone model yang bobotnya dilakukan retraining atau tuning pada dataset yang dituju. 

Pada tugas ini Anda menguji efektifitas transfer learning pada dataset Modern-Office-31. Secara singkat, Office-31 merupakan dataset image recognition berisi gambar-gambar objek dengan 31 kelas di lingkungan perkantoran yang terdiri dari 3 domain berbeda: **Amazon (A)**, **DSLR (D)**, **Webcam (W)**.

## Tantangan
Implementasikan solusi transfer learning dengan memanfaatkan backbone model deep learning yang telah di pralatih dengan setting sebagai berikut: 
- **Amazon (A) -> DSLR (D)**: menggunakan Amazon sebagai data latih transfer learning (baik dengan cara feature extraction maupun finetuning) dan DSLR sebagai data uji. 
- **DSLR (D) -> Amazon (A)**: kebalikan dari setting di atas

Anda dibebaskan memilih model backbone yang tersedia di Internet. Pada Keras terdapat berbagai pilihan yang dapat dilihat di
- https://keras.io/api/applications/
- https://keras.io/api/keras_cv/models/backbones/efficientnetv2/ 

Dataset dapat diunduh pada tautan: https://drive.google.com/file/d/1p7ecv9kP3YbmdiY49vSjTaG0Aw51n26x/view?usp=sharing.

Contoh kode pembacaan dataset Modern-Office-31: https://github.com/ghif/keras-poc/blob/main/transfer_learning/load_office31_dataset.py.

## Kriteria Penilaian (Total: 40 poin)
1.	Implementasi data/image preprocessing beserta penjelasannya (**5 poin**)
2.	Implementasi arsitektur dan pelatihan model beserta penjelasannya (**25 poin**)
3.	Visualisasi progress pelatihan (sumbu x: epoch, sumbu y: loss dan accuracy) (**5 poin**)
4.	Pencapaian performa model:
    - Akurasi uji A -> D mencapai >= 75% (**2.5 poin**)
    - Akurasi uji D -> A mencapai >= 65% (**2.5 poin**)

Prasyarat: nilai-nilai di atas hanya akan dihitung apabila akurasi uji yang didapatkan dari seluruh percobaan minimal 10%.