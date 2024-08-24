name = input("Type your name : ")
print("Welcome to the adventure game " + name + "!")

answer = input("You are on a road choose left or right : ").lower()

if answer == "left":
    answer1 = input("You are standing in front of a river. Type swim to swim across the river or type walk to walk across the river by bridge (swim/walk) : ").lower()
    if answer1 == "swim":
        print("Yow were swimming across the river and got attacked be an crocodile")
        print("You LOSE!!")
    elif answer1 == "walk":
        print("While walking you got chased by a Lion.")
        print("You LOSE!!")
    else:
      print("Option is Invalid")
      print("You LOSE!!")

elif answer == "right":
    answer2 = input("You stood in front of a mountain.To climb the mountain you either climb or drive by car.(climb/take a car)")
    if answer2 == "climb":
        print("You got exhausted and Lost the way")
        print("You LOSE!!")
    elif answer2 == "take a car":
        print("You reach the top of a mountain.")
        print("You WIN !!")
    else :
        print("Option not Valid ")
        print("You LOSE!!")
else:
    print("Option not Valid ")

print("Thank you for Playing the Game", name)