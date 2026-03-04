a = int(input("Enter a lucky number between 1 to 10: "))

match a:
    case 1:
        print("Hey! you won a camera")
    case 5:
        print("Congratulations! you won $5")
    case 7:
        print("A Big Big Congratulations! you won a Dubai Trip")
    case _:
        print("Sorry!!! Better Luck Next Time")            