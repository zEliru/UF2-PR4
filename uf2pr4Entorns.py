#imports here
import os 
#top 
def eduFunction():
    print("hola")

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










