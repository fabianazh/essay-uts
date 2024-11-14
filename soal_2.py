jumlah_kemeja = int(input("Masukan jumlah kemeja : "))
harga = 15000
total_harga = jumlah_kemeja * harga

if(jumlah_kemeja >= 25):
    diskon = 20/100
    besar_diskon = diskon * total_harga
    harga_diskon = total_harga - besar_diskon
    print("Harga kemeja setelah diskon adalah Rp. ",harga_diskon)
else:

    print("Total harga adalah Rp. ", total_harga)