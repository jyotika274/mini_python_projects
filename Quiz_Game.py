name = input("What is your name? \n")
print("Welcome to the computer quiz " + name + " !")
playing= input("Do you want to play the game? ")

if playing.lower() == "yes":
    print("Let's Begin!!")

    score = 0

    answer1 = input("What does CPU stand for? ")
    if answer1.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else :
        print("Incorrect")
    
    answer2 = input("What does GPU stand for? ")
    if answer2.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else :
        print("Incorrect")
    
    answer3 = input("What does a RAM stands for? ")
    if answer3.lower() == "random access memory":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    answer4 = input("What does PSU stand for? ")
    if answer4.lower() == "power supply" :
        print('Correct!')

        score += 1
    else:
        print("Incorrect!")
    print("Your total score is " +str(score))
else :
    print("Try next time")


