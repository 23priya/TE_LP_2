def chatBotSystem():
    menuOptions = ["Americano", "Espresso", "Capuccino", "Latte", "iced coffee"]
    qCount = [0] * len(menuOptions)
    while True:
        for i in range(len(menuOptions)):
            print("Option " + str(i+1) + " : " + menuOptions[i])
        opt = int(input("\nI would like to have option : "))
        if opt > len(menuOptions):
            print("Display relevent query\n")0
            continue
        print("\nYou Confirm order : " + menuOptions[opt-1])
        qCount[opt-1] += 1
        if qCount[opt-1] >= 5:
            break
        order = input("Do you want anything else (yes/no): ")
        print()
        if order.upper() == "YES":
            continue
        else:
            break
    yourOrder(menuOptions, qCount)

def yourOrder(menuOptions, qCount):
    print("Your Order : ")
    for i in range(len(menuOptions)):
        if qCount[i] > 0:
            print(menuOptions[i] + " : " + str(qCount[i]))

def main():
    print("Enter Your Name : ")
    name = input()
    print("Hello " + name + " Welcome to Bristo Cafe\n")
    print("What would you like to order " +  name +" \n")
    chatBotSystem()

if __name__ == "__main__":
    main()
