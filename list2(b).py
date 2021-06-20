# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 16:01:13 2021

@author: yulia2e cadangan 
"""

print("================================")
print("BENGKEL MOTOR UD")
print ("Pembelian Diatas 200 ribu diskon 5% ")
print("================================")



def total(harga,jumlah):
#fungsi untuk menghitung Total bayar 
       return harga*jumlah
#input data
harga= int(input("masukan harga barang: "))


u =input(" Masukkan Banyak barang = ")
n=int(u)
harga = n * 53000
harga = n * 50000
harga = n * 54000
harga = n * 45000
harga = n * 46000

print(" Total Harga Pembelian barang = Rp.",harga)
if (harga)>20000 :
        print("---------- Mendapat diskon 5% --------------")
        diskon = harga * 0.05
else :
        diskon = 0
    
totharga = harga - diskon
print(" Diskon = Rp.",diskon)    
print(" Total Harga = Rp.",totharga)

ulang = input(" Ulang program? y/t = ")
if ulang=="t" or ulang=="T":
   "break" 
    