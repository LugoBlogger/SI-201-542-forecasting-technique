# Assignment 01

Analisa _time series_ dari data saham PT Bank Rakyat Indonesia 
yang diberikan di `datasets/BBRI_JK_2019_01_2022_12.csv`.

Gunakan jupyter notebook pertemuan minggu 04 (atau sebelumnya)
untuk menentukan:
1. Data stasioner atau tidak (gunakan _first difference_)
2. ADF statistik dan $p$-value
3. Plot ACF
4. Lakukan prediksi baik di _first difference_ dan data
   _time series_ sebelum ditransformasi menggunakan tiga model:
   (a) rata-rata, (b) nilai-akhir, dan (c) _moving average_

Bandingkan hasil dari ketiga model tersebut menggunakan MSE,
carilah model terbaik dan jelaskan mengapa model yang dipilih
adalah model terbaik. Pembagian data `train` dan `test`
adalah 80%, 20%.

Silahkan lihat contoh pengerjaan di `template-assignment.md`


## Mark scheme
<table>
   <tr>
      <td> <b>Range</b>
      <td> <b>Description</b>
   <tr>
      <td> 86 <= score <= 100
      <td> All problems are solved, provided step-by-step, logically correct,
           summary is correct.
   <tr>
      <td> 76 <= score < 86 
      <td> Solving all problems but logically incorrect.
   <tr>
      <td> 66 <= score < 76 
      <td> Solving Problem 1, 2, and 3.
   <tr>
      <td> 56 <= score < 66 
      <td> Solving problem 1 and 2.
   <tr>
      <td> 51 <= score < 56 
      <td> Solving problem 1.
   <tr>
      <td> 0 <= score < 51 
      <td> No assignment submission by the student.
</table>

