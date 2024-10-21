# Mid-term exam

Diberikan 5 dataset _time series_ saham perusahaan yang terdaftar di LQ45 
(Juli 2024) selama 10 tahun terakhir dari 01 Oktober 2014 hingga
01-Oktober-2024:
- Bank Rakyat Indonesia (Persero) Tbk. ([dataset](../datasets/IDX_BBRI-2014-10-01-2024-10-01.csv))
- Sumber Alfaria Trijaya Tbk. ([dataset](../datasets/IDX_AMRT-2014-10-01-2024-10-01.csv))
- Astra International Tbk. ([dataset](../datasets/IDX_ASII-2014-10-01-2024-10-01.csv))
- Aneka Tambang Tbk. ([dataset](../datasets/IDX_ANTM-2014-10-01-2024-10-01.csv))
- Telkom Indonesa (Persero) Tbk. ([dataset](../datasets/IDX_TLKM-2014-10-01-2024-10-01.csv))

1. Buatlah _forecast_ untuk tiap bulan untuk _closed price_ berdasarkan data 
   pada bulan-bulan sebelumnya. Silahkan gunakan model-model yang telah 
   dijelaskan di kuliah (yaitu sampai model ARIMA).

   _Forecast_ dilakukan tiap tanggal pertama terjadi transaksi (hari Senin) 
   di awal bulan dari bulan Oktober 2014 hingga Oktober 2024
   
   Misal dilakukan _forecast_ untuk bulan Desember 2014, maka digunakan data 
   dari bulan Oktober 2014 hingga bulan November 2014 untuk melakukan peramalan 
   di tanggal pertama terjadi transaksi (hari Senin) di bulan Desember 2014.
   
   Untuk bulan Januari 2015 digunakan data bulan-bulan sebelumnya yaitu dari 
   Oktober 2014 hingga Desember 2014, demikian seterusnya hingga prediksi 
   di bulan November 2014 menggunakan seluruh data dari Oktober 2014 hingga 
   Oktober 2024.

2. Evaluasi model menggunakan MAPE terhadap data yang kalian dapatkan 
   selama melakukan _forecast_ di data yang ada. Untuk _forecast_ di periode
   November 2024 dan Desember 2024, kita akan bandingkan setelah kuliah ini 
   berakhir.

3. Tulis kesimpulan yang kalian dapatkan dari melakukan perhitungan di poin
   (1) dan (2) terhadap 5 dataset yang diberikan.

Jawaban ditulis menggunakan template seperti sebelumnya (di Assignment 01 
dan 02) tapi usahakan lebh ringkas dan tidak menyertakan hasil-hasil yang 
tidak relevan.

Silahkan mengerjakan secara individu atau satu kelompok (maksimal dua orang).
Jika mengerjakan berkelompok cukup mengumpulkan satu jawaban di LMS.
Jawaban ditulis menggunakan bahasa sendiri (bukan _copy-paste_ dari jawaban
teman atau _copy-paste_ dari ChatGPT).