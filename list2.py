# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:17:42 2021

@author: yulia 2e 
"""



print("================================")
print("BENGKEL MOTOR UD")
print ("Pembelian Diatas 200 ribu diskon 5% ")
print("================================")






def total(harga,jumlah):
#fungsi untuk menghitung Total bay
       return harga*jumlah
#input data
harga= int(input("masukan harga barang: "))
jumlah= int(input("masukan jumlah barang yang dibeli: "))
Total=total(harga,jumlah)
#diskon 5% tiap pembelian di atas Rp.200rb
if Total>200000:
      Total=Total-0.05*Total
print("Total Harga = ", "Rp.",Total)
Bayar=int(input("Jumlah Nominal Uang =" ))
Kembalian= (Bayar-Total)
print("Uang Kembalian = ", "Rp.",Kembalian)