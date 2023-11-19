# Mid-term exam

Diberikan 5 dataset _time series_ saham perusahaan yang terdaftar di LQ45 
(Januari 2023) selama 10 tahun terakhir dari 01-Januari-2013 hingga
31-Desember-2022:
- Bank Rakyat Indonesia (Persero) Tbk. ([dataset](../datasets/BBRI.JK_2013_01_2022_12.csv))
- Sumber Alfaria Trijaya Tbk. ([dataset](../datasets/AMRT.JK_2013_01_2022_12.csv))
- Astra International Tbk. ([dataset](../datasets/ASII.JK_2013_01_2022_12.csv))
- Aneka Tambang Tbk. ([dataset](../datasets/ANTM.JK_2013_01_2022_12.csv))
- Telkom Indonesa (Persero) Tbk. ([dataset](../datasets/TLKM.JK_2013_01_2022_12.csv))

1. Buatlah _forecast_ untuk tiap bulan untuk _closed price_
   berdasarkan data pada 
   bulan-bulan sebelumnya. Silahkan gunakan model-model yang telah 
   dijelaskan di kuliah (yaitu sampai model ARMA).

   _Forecast_ dilakukan tiap tanggal pertama terjadi transaksi 
   (hari Senin) di awal bulan dari bulan
   Feburari 2013 hingga Desember 2022
   
   Misal dilakukan _forecast_ untuk bulan Februari 2013, maka
   digunakan data Januari 2013 (data satu bulan) untuk melakukan 
   peramalan di tanggal pertama terjadi transaksi (hari Senin) di bulan 
   Februari 2013.
   
   Untuk bulan Maret 2013 digunakan data 2 bulan sebelumnya Januari 
   dan Februari 2013, demikian seterusnya hingga prediksi di bulan
   Desember 2022 menggunakan seluruh data dari Januari 2013 hingga 
   November 2022.

2. Hitung total _error_ MAE yang kalian dapatkan selama melakukan 
   _forecast_.

3. Tulis kesimpulan yang kalian dapatkan dari melakukan perhitungan di poin
   (1) dan (2) terhadap 5 dataset yang diberikan.

Jawaban ditulis menggunakan template seperti sebelumnya (di 
Assignment 01 dan 02) tapi usahakan
lebh ringkas dan tidak menyertakan hasil-hasil yang tidak relevan.

Silahkan mengerjakan secara individu atau berkelompok namun jawaban tetap harus 
ditulis menggunakan bahasa sendiri (bukan _copy-paste_ dari jawaban
teman).