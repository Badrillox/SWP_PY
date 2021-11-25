#import replit
import UserI


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
        return "draw between users"
    if (compare % 5 + 1) % 2 == 0:
        if n > u:
            return "User 1 wins, User 2 lost"
        else:
            return "User 1 lost, User 2 wins"
    if (compare % 5) % 2 == 0:
        if n > u:
            return "User 1 wins, User 2 lost"
        else:
            return "User 1 lost, User 2 wins"

def game():
    gameover = False
    while gameover == False:
        print("User 1 has to choose on number")
        userinputs1 = 7
        user = True
        try:
            while int(userinputs1) < 0 or int(userinputs1) > 4:
                userinputs1 = input("stone(0), paper (1), scissor(2), spock(3), lizard(4):")
                user = True
        except:
            print("user input has to be a hole number")
            user = False
        print("User 2 has to choose on number")
        userinputs2 = 8
        try:
            while int(userinputs2) < 0 or int(userinputs2) > 4:
                userinputs2 = input("stone(0), paper (1), scissor(2), spock(3), lizard(4):")
                user = True
        except:
            print("user input has to be a hole number")
            user = False
        userinput1 = (int(userinputs1))
        userinput2 = (int(userinputs2))
        if (user == True):
            print("User 1: " + numbertoString(userinput1))
            print("User 2: " + numbertoString(userinput2))
            print(logic(userinput1, userinput2))
            userinputs = input("Continue playing [c] or back to menu [m]")
            #replit.clear()
            if (userinputs.lower() == "m"):
                gameover = True
    UserI.mainmenu()
