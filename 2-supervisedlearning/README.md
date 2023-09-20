# Supervised Learning

*Supervised learning* (SL) merupakan paradigma *machine learning* yang hingga saat ini masih menjadi yang dominan dalam penyelesaian berbagai hal. 
SL bertujuan untuk mempelajari sebuah fungsi parametrik (hipotesis)
$$
f_\theta : \mathcal{X} \rightarrow \mathcal{Y}
$$
dimana $\mathcal{X}$ merupakan ruang input dan $\mathcal{Y}$ merupakan ruang output.

Terdapat berbagai macam algoritma SL untuk mencari bentuk optimal dari $f_\theta$ yang belajar dari suatu himpunan data: $$D = \{x^{(i)}, y^{(i)}\}_{i=1}^n$$.

Dari karakteristik ruang output $\mathcal{Y}$, SL terbagi menjadi 2 tipe problem:
- Regresi ($\mathcal{Y} \subseteq \mathbb{R}$): output berupa bilangan riil
- Klasifikasi ($\mathcal{X} \subseteq \mathbb{Z}$): output berupa bilangan bulat/diskrit

Beberapa topik yang dibahas pada bagian ini antara lain:

1. Linear Regression -- interpretasi probabilistik
    - Distribusi Gaussian atau normal
    - Maximum Likelihood Estimation (MLE)
2. Logistic Regression / Binary Classification
    - Fungsi sigmoid
    - Gradient descent
3. Multi-class Classification
    - Fungsi softmax
    - Use case: image classification