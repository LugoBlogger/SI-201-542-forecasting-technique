# Assignment 03

Analyze the time series of the number of unemployment 
and the number of people living in poverty in Indonesia from 2007
to 2024
You can download those time series data from 
[here](https://www.bps.go.id/id/statistics-table/2/NTQzIzI=/tingkat-pengangguran-terbuka--februari-2024.html)
and [here](https://www.bps.go.id/id/statistics-table/2/MTg1IzI=/jumlah-penduduk-miskin--ribu-jiwa--menurut-provinsi-dan-daerah.html)

**Note**: The webpage above only shows the data for a selected year.
You need to download the data for all the years.

Use Jupyter notebook in Week 11 to do forecasting with the following model
1. last value
2. VAR 

Compare those two models using MAPE, and decide which model gives
the best result and explain why you choose that model.
Data division of `train` and `test` is 80% and 20%. 

**Hint**: The data of the number of people living in poverty is
very small. What is the best strategy to have the same the same 
number of data in for each month? Use this strategy to increase 
the number of your data points.

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

