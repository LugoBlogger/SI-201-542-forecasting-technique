# Assignment 02

Analisa _time series_ dari data saham PT Bank Rakyat Indonesia 
yang diberikan di `datasets/BBRI-2019-01-01-2023-12-31.csv` untuk
kolom "Close"

Data yang diberikan adalah data per hari transaksi (ada beberapa hari, 
seperti hari libur, tidak ada transaksi). Ubahlah data _time series_ tersebut
ke dalam data bulanan, dan lakukan prediksi dengan `HORIZON` dua bulan.

Gunakan Jupyter Notebook pertemuan minggu 06 (atau sebelumnya)
untuk melakukan _forecast_ dengan model berikut:
1. rata-rata
2. nilai akhir
3. ARMA (jika memungkinkan)

Untuk model ARMA ikuti langkah-langkah yang telah disediakan di dalam  
Jupyter Notebook.

Bandingkan hasil dari ketiga model tersebut menggunakan MAPE,
carilah model terbaik dan jelaskan mengapa model yang dipilih
adalah model terbaik. Pembagian data `train` dan `test`
adalah 80%, 20%.

Contoh pengerjaan sama seperti _template_ sebelumnya di `template-assignment.md`

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
