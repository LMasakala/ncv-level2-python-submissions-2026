mark = float (input("Please enter a mark: "))

if mark >= 50 and mark <= 100:
    if mark >= 75:
        print("Congrats you have achieved a Distinction")
    else:
        print("You have passed")
else:
    print("You have failed")
