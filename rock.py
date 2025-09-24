health = 10
happiness = 5
fatigue = 5
name = input("What is the name of your creation: ")
while health >=0 or happiness >=0 or fatigue <=10:
    print("your rock", name)
    print("rock stats: ")
    print(" health:", health, "/10")
    print(" happiness", happiness, "/10")
    print(" fatigue", fatigue, "/10")
    print("Rock options: ")
    print("1: play with  the rock")
    print("2: make your rock go to sleep")
    print("3: do nothing with your rock")
    print("4: destroy your rock")
    choice = input("Which option would you like to select")
    if choice == "1":
        print("you played with your rock it became happier")
        if happiness <= 8:
            happiness += 2
            fatigue += 1
        elif happiness == 9:
            happiness += 1
        elif happiness == 10:
            happiness += 0
    if choice == "2":
        print("you made your rock go to sleep it seemed less fatigued for a rock")
        if fatigue >= 2:
            happiness -= 1
            fatigue -= 2
        elif fatigue == 1:
            happiness -= 1
            fatigue -= 1
        elif fatigue == 0:
            happiness -= 1
            fatigue -= 0
    if choice == "3":
        print("you did nothing and the rock somehow hurt itself in it's confusion")
        health -= 2
        happiness -= 2
        fatigue += 2
    if choice == "4":
        print("you run the rock over with your car and smash both the rock and your front axel")
        health -= 10
        happiness -= 10
        fatigue += 10
    else:
        print("your rock looked at you and was confused by the alien words that you just spoke to it")
        happiness -= 2
        fatigue += 2
    