while True:
    num = int(input("Enter a number > 0: "))
    if num > 0:
        print("Valid input:", num)
        break
    else:
        print("Invalid. Try again.")
