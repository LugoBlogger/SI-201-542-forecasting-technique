# Template Assignment

Nama: Nam lengkap    
NIM: Nomor_induk_mahasiswa

> **Catatan**  
> Silahkan gunakan bahasa dan tulisan kalian sendiri.
> Kalimat dan penjelasan berikut hanyalah contoh pengerjaan tugas.
> Usahakan menggunakan penjelasan yang saling berbeda antara satu
> mahasiswa dengan mahasiswa yang lain.

Pada tugas berikut kita akan melakukan peramalan data penjualan _widget_ suatu 
perusahaan XYZ yang dinyatakan dalam ribu dollar dari tanggal 
01 Januari 2019 sebanyak 500 hari kedepan. Berikut adalah grafik data tersebut

<img src="../figures/template-assign-df-plot.png" width=600>

Disini terlihat kita bahwa grafik memiliki bentuk tidak stasioner
yaitu ada _trend_ turun dari bulan Januari 2019 hingga Maret 2019.
Lalu _trend_ naik dari Mei 2019 hingga Maret 2020. Secara kuantitatif
bentuk tidak stasioner ini dapat kita hitung dengan melakukan transformasi
ke _first difference_ yaitu _time series_, $y'_t = y_t - y_{t-1}$,
dengan $y_t$ adalah nilai penjualan saat waktu $t$ dan $y'_t$ adalah
_first difference_ dari $y_t$. Berikut adalah plot untuk _first difference_
penjualan _widget_ 

<img src="../figures/template-assign-df-plot-first-diff.png" width=600>

Pada plot di atas terlihat _first difference_ memiliki bentuk stasioner
yaitu bergerak secara fluktuatif disekitar 0. Kita dapat membandingkan
nilai ADF statistik dan $p$-value-nya dari kedua plot di atas:
- Plot asli ($y_t$):
  - ADF statistik: $-1.51$
  - $p$-value: $0.527$
- Plot _first difference_ ($y'_t$):
  - ADF statistik: $-10.58$
  - $p$-value: $7.077 \times 10^{-19} \approx 0$

Berdasarkan uji ADF statistik dengan acuan $p$-value di bawah $0.005$
menyatakan bahwa nilai ADF statistik untuk _first difference_ sangat
negatif dibanding data _time series_ asli yang memiliki $p$-value
masih di sekitaran $p$-value acuan. Sehingga dapat kita simpulkan
data _first difference_ bersifat stasioner menurut uji ADF statistik.

Dikarenakan data _first difference_ stasioner, kita dapat melakukan 
peramalan untuk data tersebut. Pertama-tama kita bagi data menjadi
dua bagian data `train` dan `test`.