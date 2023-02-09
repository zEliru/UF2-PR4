#imports here
import os 
#top 
def eduFunction():
    print("You take the path on the left. After 5 minutes of walking, you can see a castle behind the trees, to your left.")
    print("However, you are attacked by bandits. What would you want to do?")
    print("1 - I'm going to fight them, I'm sure I can take them on.")
    print("2 - I'm running for my life. I'll jump from a cliff I can see from here.")
    choice = int(input())
    if (choice == 1):
        eduPathOneOne()      
    elif (choice == 2):
        eduPathOneTwo()   
    else:
        print("Error. Choose wisely.")

def eduPathOneOne():
    print("You chose to fight.")
    print("You smack the bandits hard and they die. Then you rob their dead bodies. You looted a diamond ring.")
    print("You can see a castle, as well as a clearing in the woods, with an apple on the groud, right in the very middle of it.")
    print("1 - Castle here I go")
    print("2 - I want that red and shiny apple.")
    choice = int(input())
    if (choice == 1): 
        eduPathTwoOne()
    elif (choice == 2):
        eduPathTwoTwo()
    else:
        print("Error. Choose wisely.")
    

def eduPathOneTwo():
    print("You chose to run.")
    print("You run as fast as you can, you get ready for the most important jump of your life and you take your shot.")
    print("Something went wrong. You fell off the cliff only to meet the rocks below with your head. You die.")

def eduPathTwoOne():
    print("You walk towards the castle. They spot a giraffe trying to invade it, all whilst carrying the diamond ring that used to belong to the princess.")
    print("Cage the giraffe!")
    print("You're caged. End of the story.")

def eduPathTwoTwo():
    print("You eat the apple.")
    print("It was poisoned.")
    print("You die.")


#edu until here
def olegFunction():
    print("fuck you")

















#oleg until here



def startOfGame():
    isValid = False
    name = str(input("Hello. What is your name?"))
    print(f"Hi {name}.")
    while (not isValid):
        
        choice = int(input("You are a giraffe and you are walking on a sand road. \
            Your path is divided. Would you like to go left(1) or right(2)?"))
        if (choice == 1):
            isValid=True
            eduFunction()
        elif (choice == 2):
            isValid=True
            olegFunction()
        else:
            print("Error. Please choose wisely. Either 1 or 2. Please.")

#here starts the game
startOfGame()
#game ends


input()










