# input and initialize count for loop
amount = 1000
operation = int(input("Enter any provided option: "))

# Begin the loop process
while operation <=4:  
    print("Menu:\n")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
  

    # check amount 
    if operation == 1:
        print(f"Your current balance is: {amount}")

    # add money to the account
    elif operation == 2:
        deposit_money = float(input("Enter amount to deposit: "))
        amount += deposit_money
        print(f"You have deposited {deposit_money}. New account balance: {amount}")

    # take money from the account
    elif operation == 3:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= amount:
            amount -= withdraw_amount
            print(f"You have withdrawn {withdraw_amount}. New account balance: {amount}")
        else:
            print("Insufficient funds.")

    # exit the program
    elif operation == 4:
        print("Exit the program.")
        break
    else:
        print("Invalid option. Please choose a valid option.")


