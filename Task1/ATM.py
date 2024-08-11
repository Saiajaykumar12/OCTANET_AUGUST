import time

print("Please enter your card")

time.sleep(5)

balance = 10000

password = 9834

print("Please enter your pin: ")
pin = int(input())

if pin == password:
    print("""
          1 == Balance Enquiry
          2 == Withdraw
          3 == Deposit amount
          4 == Exit"""
          )
    try:
        option = int(input("Please enter your choice: "))
    except:
        print("Please enter valid option")

    while  True:

        if option == 1:
            print(f"Your current balance is {balance}")
            break

        if option == 2:
            print("Please enter the amount")
            withdrawal_amount = int(input())
            balance = balance - withdrawal_amount
            print(f"{withdrawal_amount} is debited from your account")
            print(f"Your current balance is {balance}")
            break

        if option == 3:
            print(f"Please enter your deposit amount")
            deposit_amount = int(input())
            print(f"{deposit_amount} is credited to your account")
            balance = balance + deposit_amount
            print(f"Your current balance is {balance}")
            break

        if option == 4:
            break


else:
    print("Please enter the valid pin")