# Assignment 03

Analisa _time series_ dari data saham PT Bank Rakyat Indonesia 
yang diberikan di `datasets/BBRI_JK_2019_01_2022_12.csv` untuk
kolom "Close" dan gunakan data inflasi di `dataset/Data Inflasi.xlsx`
sebagai variabel _exogenous_

Gunakan jupyter notebook pertemuan minggu 10 (atau sebelumnya)
untuk melakukan _forecast_ dengan model berikut:  
1. nilai akhir
2. SARIMAX 

Untuk model SARIMAX ikuti langkah-langkah yang telah disediakan di dalam  
jupyter notebook `week-10.ipynb`.

Data saham perlu diubah unitnya supaya sama dengan unit waktu di data inflasi.

Bandingkan hasil dari kedua model tersebut menggunakan MAPE,
carilah model terbaik dan jelaskan mengapa model yang dipilih
adalah model terbaik. Pembagian data `train` dan `test`
adalah 80%, 20%.

Contoh pengerjaan sama seperti _template_ sebelumnya di `template-assignment.md`

Untuk panduan penjelasan _coding_ notebook `week-10.ipynb` dapat
dilihat di `assignments/program-desc-week-10.md`.

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
      <td> Solving problem 1 and 2.
   <tr>
      <td> 56 <= score < 66 
      <td> Solving problem 1.
   <tr>
      <td> 51 <= score < 56 
      <td> Solving problem 1 partially.
   <tr>
      <td> 0 <= score < 51 
      <td> No assignment submission by the student.
</table>

