balance = 10000

def Check_bal():
    print("Total Amount:", balance)

def deposite():
    global balance
    amount = int(input("Enter deposite amount:"))
    if amount <= 0:
        print("invalid amount")
    else:
        balance = balance + amount
        print("Deposited Successfully")
        print("Total amount:", balance)

def with_draw():
    global balance
    with_draw = int(input("enter withdraw amount:"))
    if with_draw >= balance:
        print("you entered more than balanace")

    else:
        balance = balance - with_draw
        print("Money Drawn Successfully")
        print("Remaining amount:", balance)

while True:
    print("--- Simple ATM System ---")
    print("1.check Balance:")
    print("2.deposite")
    print("3.With_Draw")
    print("4.Exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        Check_bal()
    elif choice == 2:
        deposite()
    elif choice == 3:
        with_draw()
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("invalid")
