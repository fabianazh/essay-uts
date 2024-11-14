menu_awal = int(input("Menu \n 1. Luas \n 2. Volume \n Pilih menu : "))

# Luas
if(menu_awal == 1):
    menu_luas =input("Menu \n a. Persegi \n b. Segitiga \n Pilih menu : ")
    # Persegi
    if(menu_luas == "a" or menu_luas == "A"):
        sisi = int(input("Masukan sisi persegi : "))
        luas_persegi = sisi * sisi
        print(luas_persegi)
    # Segitiga
    elif(menu_luas=="b" or menu_luas == "B"):
        alas = float(input("Masukan alas segitiga : "))
        tinggi = float(input("Masukan tinggi segitiga : "))
        luas_segitiga = 0.5 * alas * tinggi
        print(luas_segitiga)
    else:
        print("Menu tidak valid")
# Volume
elif(menu_awal==2):
    menu_volume =input("Menu \n a. Kubus \n b. Segitiga \n Pilih menu : ")
    # Kubus
    if(menu_volume == "a" or menu_volume == "A"):
        sisi = int(input("Masukan sisi kubus : "))
        volume_kubus = sisi * sisi * sisi
        print(volume_kubus)
    # Tabung
    elif(menu_volume =="b" or menu_volume == "B"):
        jari_jari = float(input("Masukan jari-jari tabung : "))
        tinggi = float(input("Masukan tinggi tabung : "))
        volume_tabung = 3.14 * (jari_jari *jari_jari)* tinggi
        print(volume_tabung)
    else:
        print("Menu tidak valid")
else:
    print("Menu tidak valid")  