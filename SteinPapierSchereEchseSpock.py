import random

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
def logic(n,u):
    type(n)
    type(u)
    compare = n-u + 5
    if compare % 5 == 0:
        return "draw"
    if (compare % 5 +1) % 2 == 0:
        return "win"
    if (compare % 5) % 2 == 0:
        return "lose"

if __name__ == "__main__":
    d= 0
    w = 0
    l = 0
    userinput = input("Choose your elements: ")
    elements = ["scissor","paper","rock","lizard","spock"]
    if userinput in elements:
        random.shuffle(elements)
        comp = elements[0]
        print("Computer: " + comp)
        if userinput == comp or \
        userinput == "spock" and comp == "paper" or \
        userinput == "paper" and comp == "spock":
            print("Draw between user and computer")
            d = d+1
        if userinput == "lizard" and comp == "paper" or \
        userinput == "scissor" and comp == "lizard" or \
        userinput == "spock" and comp == "rock" or \
        userinput == "spock" and comp == "scissor" or \
        userinput == "lizard" and comp == "spock" or \
        userinput == "scissor" and comp == "paper" or \
        userinput == "rock" and comp == "lizard" or \
        userinput == "rock" and comp == "scissor" or \
        userinput == "paper" and comp == "rock":
            print("User wins")
            w = w+1
        if userinput == "paper" and comp == "lizard" or \
        userinput == "lizard" and comp == "scissor" or \
        userinput == "rock" and comp == "spock" or \
        userinput == "scissor" and comp == "spock" or \
        userinput == "paper" and comp == "scissor" or \
        userinput == "spock" and comp == "lizard" or \
        userinput == "rock" and comp == "paper" or \
        userinput == "scissor" and comp == "rock" or \
        userinput == "lizard" and comp == "rock":
            print("Computer wins")
            l = l+1
        print(w)
        print(l)
        print(d)
    else:
        print("Wrong input")
