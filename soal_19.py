nim = input("Masukan NIM kamu : ")

arr_nim = list(nim)

for x in arr_nim:
    int_nim = int(x)
    if(int_nim %2 == 0):
        print(int_nim, " is even")
    else:
        print(int_nim, "is odd")