import gamelogic_a
import gamelogic_m
def againstAI():
    print("Difficulty of the AI")
    print("e ... Easy AI")              # using Random numbers
    print("m ... Medium AI")            # 20 entries in database
    print("h ... Hard AI")              # database
    print("b ... back to game menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "e":
        gamelogic_a.game("e")
    elif usinput == "m":
        gamelogic_a.game("m")
    elif usinput == "h":
        gamelogic_a.game("h")
    elif usinput == "b":
        mainmenu()
    else:
        print("Wrong input please try again")
        againstAI()
def multiplayer():
    print("Multiplayer Mode")
    print("m ... play against a friend [1v1]")
    print("b ... back to game menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "m":
        gamelogic_m.game()
    elif usinput == "b":
        gamemenu()
    else:
        print("Wrong input please try again")
        multiplayer()
    pass
def gamemenu():
    print("Choose your playmode")
    print("a ... Against AI")
    print("m ... Against other players on the same PC")
    print("b ... Back to the menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "a":
        againstAI()
    elif usinput == "m":
        multiplayer()
    elif usinput == "b":
        mainmenu()
    else:
        print("Wrong input please try again")
        gamemenu()
def mainmenu():
    print("Welcome to scissors-stone-paper-lizard-spock")
    print("p ... playing th game")
    print("e ... exiting the game")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "e":
        print("Goodbye have a nice day")
    elif usinput == "p":
        gamemenu()
    else:
        print("Wrong input please try again")
        mainmenu()