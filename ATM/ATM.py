def show_balance(balance):
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount = float(input("enter a amount to deposit: "))

    if amount < 0:
        print("thats not a valid amount")
        return 0 
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount to be withdrawn: "))

    if amount > balance:
        print("u dont have enought money")
        return 0 
    elif amount < 0:
        print("amount should bemore than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0 
    is_running = True

    while is_running:
        print("welcome to Banking program")


        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")

        choice = input("enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("thats not valid choice")
            
        
    print("thanks have a nice day")

if __name__ == "__main__":
    main()