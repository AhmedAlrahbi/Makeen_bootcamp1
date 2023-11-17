#In-class-activity, bank system
pin = 0
balance = 100
while True:
    try:

        pin = int(input("Enter the 4 digits pin: "))
        if pin == 1111:
            while True:
                try:
                    mainMenu = int(input("""Enter the following options:
                1.Check balance.
                2.Withdraw money.
                3.deposit money.
                >"""))
                    
                    if mainMenu == 1:
                        balance = 100
                        print("Your current balance is $", balance)
                        exit("")
                    elif mainMenu == 2:
                        print("Your balance is $", balance)
                        withDraw = int(input("Enter amount to withdraw from balance: $"))
                        print("Your new balance is $",balance - withDraw)
                    elif mainMenu == 3:
                        print("Your balance is $", balance)
                        deposit = int(input("Enter amount to deposit it on balance: $"))
                        print("Your new balance is $", balance + deposit)
                    else:
                        print("Enter from (1-3) please")
                    continue
                except:
                    exit("")
        else:   
            pin != 1111
            print("Wrong pin!!, Try again.")
            continue 
    except:
        exit("Something wrong happened!")