import sys
attempts = 0
my_pin = "1234"
while True:
    PIN = int(input("Type your PIN: "))

    if PIN == my_pin:
        print("You are logged in successfully")
        break
    else:
        print("Wrong password!")
        attempts = attempts + 1
        if attempts == 3:
            sys.exit()


# Initialization 
menu = input("\s\s~~~Menu~~~\n- Press 1 for deposit\n- Press 2 for withdrawal\n Choice:")
money_account =223.21

if menu =="1": # Deposit 
    money_transaction = float(input("Give the amount of money you want to deposit: "))
    # Check 
    if money_transaction > 0 :
        money_account+=money_transaction
    print(f"Your account balannce is {money_account} ")
    

elif menu =="2": # Withdrawal
    money_transaction = float(input("Give the amount of money you want to withdraw: "))
    # Check 
    if money_account >= money_transaction :
        money_account-=money_transaction
    else:
        print(f"Withdrawal failed!\nYou don't have enough to withdraw {money_transaction}")
    print(f"Your account balannce is {money_account} ")
    
else:
    print("Wrong choice!")
    ("Bye")
