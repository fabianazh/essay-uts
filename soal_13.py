pin = int(input("Masukan PIN anda : "))
my_pin = 222


if(pin != my_pin):
    print("PIN Incorrect!")
    second_try = int(input("Masukan PIN anda : "))

    if(second_try != my_pin):
        print("PIN Incorrect!")
        third_try = int(input("Masukan PIN anda : "))

        if(third_try != my_pin):
            print("PIN Access Incorect 3 times. Access Blocked.")
        else:
            print("PIN Correct!")
    else:
        print("PIN Correct!")
else:
    print("PIN Correct!")