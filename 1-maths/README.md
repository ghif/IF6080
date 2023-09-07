# Aljabar Linear dengan NumPy

Aljabar linear merupakan *jantung* dari machine learning, yaitu "bahasa utama" untuk menjelaskan machine learning secara matematis, sekaligus jembatan untuk mengimplementasikannya dalam kode program.

Bagian ini membahas beberapa konsep dasar aljabar linear beserta implementasinya dengan menggunakan Python, terutama dengan memanfaatkan library NumPy. 

NumPy (Numerical Python) merupakan sebuah library Python yang digunakan untuk memanipulasi *arrays* secara efisien, dikembangkan pertama kali pada tahun 2005 oleh Travis Oliphant. NumPy memiliki berbagai fungsionalitas untuk mengimplementasikan aljabar linear dan probabilitas. 

NumPy dikembangkan untuk mengatasi permasalahan *list*. Walaupun keduanya sama-sama dirancang untuk kebutuhan manipulasi *arrays*, objek utama pada NumPy, yaitu *ndarray*, memiliki komputasi hingga 50x lebih cepat dibandingkan *list*. 

Hal ini dikarenakan *array* dari NumPy disimpan pada sebuah tempat yang kontinu sehingga sebuah proses dan mengakses dan memanipulasi objek array NumPy lebih efisien. Ditambah pula dengan implementasi *backend* pada NumPy yang sebagian besar ditulis dalam C/C++.

Konsep fundamental yang dibahas mencakup:

1. Vektor
    - Penjumlahan / pengurangan
    - Perkalian skalar-vektor
    - Perkalian vektor-vektor: outer product, inner product

2. Fungsi linear
    - Definisi dan sifat fungsi linear
    - Aproksimasi Taylor

3. Fungsi regresi

4. Norm
    - Jarak
    - Nearest neighbor

5. Matriks

6. Metode Least squares