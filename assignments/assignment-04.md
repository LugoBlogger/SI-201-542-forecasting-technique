# Assignment 04

Pada tugas berikut, kalian diminta untuk mennggunakan tutorial 
[`time-series-foreacsting.ipynb`](./tensorflow-time-series/time-series-forecasting.ipynb)
dan [_notebook_](../week-14.ipynb) di minggu ke-14. Data yang digunakan adalah 
[`fixed_form_internet-user.csv`](../datasets/fixed_form_internet-users.csv) dan 
[`fixed_form_population.csv`](../datasets/fixed_form_population.csv), dan lakukan pembentukan
`dataset` supaya dapat digunakan untuk peramalan menggunakan _deep learning_.

Dalam tugas ini, kalian tidak perlu membuat model _deep learning_, cukup
melakukan tahapan _data preparation_. Perlu juga diingat bahwa
jumlah data yang digunakan dalam Assignment 04 ini sangatlah sedikit.
Namun tetap kita gunakan sebagai ilustrasi untuk memahami data windowing.
Dalam praktek, data yang digunakan harus memiliki cukup besar jumlah 
baris data, seperti yang telah ditunjukkan pada _notebook_ minggu ke-14.

Untuk menyelesaikan tugas ini, kalian cukup mengumpulkan _file_
jupyter notebook `.ipynb`

Berikutnya ikuti langkah-langkah berikut untuk pengerjaan
_Assignment 04_

1. Bacalah data [`fixed_form_internet-user.csv`](../datasets/fixed_form_internet-users.csv) dan 
   [`fixed_form_population`](../datasets/fixed_form_population.csv), sehingga didapatkan 
   objek `DataFrame` sebagai berikut, menggunakan pandas
   ![01-read-df.png](./assignment-04-test/01-read-df.png)

   _Petunjuk_:   
   a. Di dalam `fixed_form_internet-user.csv`, kolom `DATE` terdiri dari
   bulan dan tahun, ambil data dengan bulan terakhir di tahun tersebut.   
   b. Di dalam `fixed_form_population.csv`, kolom `Year` digunakan sebagai 
   kolom untuk dilakukan operasi `JOIN` (ingat kembali kuliah tentang 
   basis data) dengan kolom `DATE` yang sudah diambil tahunnya saja
   di petunjuk (a). Baris data yang terambil setelah operasi `JOIN` hanyalah
   yang memiliki irisan.   
   c. Apabila mengalami kendala kesulitan, dapat dilakukan operasi `JOIN`
   secara manual menggunakan Excel.

2. Buatlah _plot_ dari dua kolom **NUMBER OF USERS IN MILLIONS** 
   dan **Total population in thousands**.
   ![02-a-plot-num-of-users.png](./assignment-04-test/02-a-plot-users-and-population.png)

   _Petunjuk_:
   a. Perhatikan bahwa skala (_ticks_) untuk sumbu-x memiliki posisi yang sama
   di kedua plot.
   b. Skala untuk sumbu-y adalah _millions_ untuk kedua plot.

3. Terdapat total baris data sebanyak 28. Gunakan semua data tersebut sebagai
   training set. Untuk validasi dan test set, gunakan DataFrame kosong
   (`pd.DataFrame()`). Setelah itu lakukan _scaling_ menggunakan 
   `MinMaxScaler` (lihat [_notebook_](../week-13.ipynb) minggu ke-13). 
   Terdapat tiga kolom yang akan di-_scaling_ yaitu:
   `DATE`, `NUMBER OF USERS IN MILLIONS` dan `Total population in thousands`.
   Jika proses diatas dilakukan dengan benar, akan didapatkan `DataFrame`
   sebagai berikut:
   ![03-scaling-train-df.png](./assignment-04-test/03-scaling-train-df.png)
   
   
4. Menggunakan class `DataWindow()` di _notebook_ minggu ke-14 atau 
   berkas `DataWindow.py`, buatlah windowed dataset
   dengan lebar input 5 (lima tahun), lebar label 2 (dua tahun), 
   dan _shift_ 2 (jarak pergeseran lebar label terhadap tahun terakhir
   input)

   Namakan windowed dataset tersebut dengan nama `window_data`. Jika proses
   diatas dilakukan dengan benar maka akan menghasilkan _print out_ `window_data`
   sebagai berikut:
   ![04-window-data-output.png](./assignment-04-test/04-window-data-output.png)

   Periksa juga `window_data`, dengan perintah
   ```py
   window_data.plot(plot_col="NUMBER OF USERS IN MILLIONS", figsize=(12, 10), 
                     max_subplots=3, xlabel="Time (year)")
   ```
   Jika proses diatas dilakukan dengan benar, maka akan didapatkan plot
   _windowed data_ sebagai berikut:
   ![05-window-data-plot.png](./assignment-04-test/05-window-data-plot.png)

   Tiga plot diatas untuk tiap _running_ dapat berbeda-beda karena
   setiap proses _plotting_ dilakukan _sampling windowed data_ secara random.
   Yang terpenting adalah posisi label dan input data sesuai dengan 
   ukuran yang telah ditentukan pada pembentukan variabel `window_data`.
