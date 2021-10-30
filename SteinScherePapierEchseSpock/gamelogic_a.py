import random
import UserI

#import replit as replit


def numbertoString(n):
    if n == 0:
        return "stone"
    if n == 1:
        return "paper"
    if n == 2:
        return "scissors"
    if n == 3:
        return "spock"
    if n == 4:
        return "lizard"


def logic(n, u):
    type(n)
    type(u)
    compare = n - u + 5
    if compare % 5 == 0:
        return "draw"
    if (compare % 5 + 1) % 2 == 0:
        return "win"
    if (compare % 5) % 2 == 0:
        return "lose"


def game(level):
    gameover = False
    while gameover == False:
        userinputs = 7
        user = True
        try:
            while int(userinputs) < 0 or int(userinputs) > 4:
                userinputs = input("stone(0), paper (1), scissor(2), spock(3), lizard(4):")
                user = True
        except:
            print("user input has to be a hole number")
            user = False
        compinput = 0
        if level == "e":
            compinput = random.randint(0, 4)
        elif level == "m":
            pass
        elif level == "h":
            pass
        userinput = (int(userinputs))
        if (user == True):
            print("User: " + numbertoString(userinput))
            print("BOT: " + numbertoString(compinput))
            print(logic(userinput,compinput))
            userinputs = input("Continue playing [c] or back to menu [m]")
            if (userinputs.lower() == "m"):
                gameover = True
    UserI.mainmenu()
