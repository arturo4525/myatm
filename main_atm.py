running = True
accounts = [1234, 3333, 4444] 
amounts = [100, 500, 0]
currentlyLoggedIn = None 
currentChoice = "menu" 

def checkInput(userInput) : 
    try :
        intInput = int(userInput) 
        if intInput >= 0 : 
            return True 
        else: 
            return False 
    except ValueError:
        return False 

def createAccount() :
    bankAccount = input("Open a new Bank account: ")
    if checkInput(bankAccount) :
        for account in accounts:
            if account == int(bankAccount): 
                print("Bank account number already exists.")
                
        try: 
            accounts.append(int(bankAccount))
            amounts.append(0)
        except:
            pass
        print("Your new account has been created")
        return "loggedIn"
        
    else:
        print("Enter a number")
        return "menu"

def loggedIn() :
    logIn = input("Please log in to your account: ")
    if checkInput(logIn) :
        index = 0 
        for accountOwner in accounts:
            if accountOwner == int(logIn):
                print("You are now logged in.")
                return index
            index += 1
        print("Please create a new account or log in with an existing account")
        return -1
    else: 
        print("Enter a number")
        return -1

def accountMenu(): 
    print(" *** Account Menu *** ")
    print("1. Withdrawl ")
    print("2. Checkings ")
    print("3. Show Balance ")
    print("4. Logout ")
    option = input()
    if checkInput(option):
        if option == "1":
            return "withdrawl"
        elif option == "2":
            return "checkings"
        elif option == "3":
            return  "balance"
        elif option == "4":
            return "menu"
        else:
            print("You need to enter a number")
            return "accountMenu"
    else: 
        print("You need to enter a number")
        return "accountMenu"

def withdrawl():
    print(amounts[currentlyLoggedIn])
    currentWithdrawl = input("How much would you like to withdrawl?: ")
    if checkInput(currentWithdrawl) : 
        if amounts[currentlyLoggedIn] <= int(currentWithdrawl):
            print("Not sufficient funds: ")
        else:
            amounts[currentlyLoggedIn] = amounts[currentlyLoggedIn] - int(currentWithdrawl)
            print("This is the remaining balance: ", amounts[currentlyLoggedIn])
        return "accountMenu"
    else:
        print("Enter a number")
        return "accountMenu"    


def checkings():
    depositMoney = input("How much would you like to deposit to your account?: ")
    if checkInput(depositMoney) :
        amounts[currentlyLoggedIn] = amounts[currentlyLoggedIn] + int(depositMoney)
        print("This is your current balance in your account: ", amounts[currentlyLoggedIn])
        return "accountMenu" 
    else:
        print("Enter a number")
        return "accountMenu"    


def balance():
    print("This is your current balance in your account: ", amounts[currentlyLoggedIn])
    return "accountMenu" 


def menu():
    print("*** Main Menu ***")
    print("1. Open new Bank account ")
    print("2. Log in to account ")
    print("3. Terminate ")

    choice = input("Please chose an option to proceed: ")
    if checkInput(choice): 
        if choice == "1":
            return "createAccount"
        elif choice == "2":
            return "loggedIn"
        elif choice == "3":
            return "terminate"
        else:
            print("Wrong entry, please make a new selection") 
    else:
        print("Wrong entry, please enter a number:") 
        return "menu"


while running:
    

    if currentChoice == "menu": 
        currentChoice = menu() 
    elif currentChoice == "createAccount":
        currentChoice = createAccount()
    elif currentChoice == "loggedIn": 
        currentlyLoggedIn = loggedIn() 
        if currentlyLoggedIn >= 0 : 
            currentChoice = accountMenu()
        else:
            currentChoice = "menu" 
    elif currentChoice == "withdrawl":
        currentChoice = withdrawl()
    elif currentChoice == "checkings":
        currentChoice = checkings()
    elif currentChoice == "balance":
        currentChoice = balance()
    elif currentChoice == "accountMenu":
        currentChoice = accountMenu()
    elif currentChoice == "terminate":
        print(" Goodbye have a nice day!")
        running = False
    else: 
        currentChoice = "menu"

    




