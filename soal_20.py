name = input("Masukan nama anda : ")

arr_name = list(name)
arr_name[0]="*"
arr_name[1]="*"
arr_name[2]="*"

for i in arr_name:
    print(i,end="")