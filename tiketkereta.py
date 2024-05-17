#Input
pembeli=input("Input Nama Pembeli: ")
no_hp=input("Input No. Handphone : ")
jurusan=input("Input Jurusan[SBY/BL/LMP] : ")
print("[1]\tVIP\n[2]\tExecutive\n[3]\tEkonomi")
kelas=input("Masukan Nama Kelas[1/2/3] : ")

#Proses
if jurusan=="SBY" or "sby": 
    namajurusan="Surabaya"
    if kelas=="1":
        harga = 1000000
    elif kelas=="2":
        harga = 600000
    else:
        harga = 300000

elif jurusan=="BL" or "bl":
    namajurusan="Bali"
    if kelas=="1":
        harga = 1500000
    elif kelas=="2":
        harga = 1000000
    else:
        harga = 700000
else : 
    namajurusan="Lampung" 
    if kelas=="1" :
        harga = 600000
    elif kelas=="2":
        harga = 400000
    else:
        harga = 200000


#Input Jumlah Beli 
jumlah=int(input("Masukkan JumlahBeli: "))

#proses potongan
if jumlah>=3 : potongan=(jumlah*harga)*0.1 
else: potongan=0
total=(jumlah*harga)-potongan 

#CetakHasil 
print("------------------------------------")
print("        PENJUALAN TIKET BUS")
print("               XYZ")
print("------------------------------------")
print("Nama Pembeli: "+str(pembeli))
print("No. Handphone : "+str(no_hp))
print("KodeJurusanyang dipilih: "+str(jurusan))
print("Nama Kota Tujuan: "+str(namajurusan))
if kelas==1:
    print("Kode jurusan Pilihan: VIP")
elif kelas==2:
    print("Kode Jurusan Pilihan : Executiv")
else:
    print("Kode Jurusan Pilihan : Ekonomi")
print("Harga: ",+(harga))
print("JumlahBeli: ",+(jumlah))
print("------------------------------------")
print("potonganyang didapat: ",+(potongan))
print("Total Bayar   : ",+(total)) 
ubay=int(input("Masukkan UangBayar : "))
uangkembali=ubay-total
print("UangKembali: ",+uangkembali)
