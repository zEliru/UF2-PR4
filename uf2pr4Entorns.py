#imports here
import os, msvcrt 
#top 
def eduFunction():
    print("hola soc l'edu")

















#edu until here

def olegFunction():
    print("You've choosen the RIGTH path")
    print("Your game narrated by Oleg starts here!")
    print("You open your eyes, you where kidnapped...")
    print("you realize that now you aren't in the zoo of NY...")
    print("you are in the african jungle.")
    input()
    os.system('cls')
    print("PRESS START!")
    msvcrt.getch()
    os.system('cls')
    print("Welcome to the jungle!")
    print("You see two roads and have to choose one of them pressing the number they have.")
    print("The first road starts with a field of flowers with butterflies flying around. (1)")
    print("The second path is a field of rocks (2)")
    isValid = False
    choice = int(input("Which one do you choose?"))
    while(not isValid):
        if (choice == 1): # the path of flowers
            isValid=True
            olegPathOneOne()
        elif (choice == 2): # the path of rocks
            isValid=True
            olegPathOneTwo()
        else:
            print("Error. Please choose wisely. Either 1 or 2. Please.")
    msvcrt.getch()
    os.system('cls')

#os.system('cls')

def olegPathOneOne():
    print("Not a good choice!")
    print("You forgot about your allergies...")
    print("you can't breath... a giraffe in trouble!")
    msvcrt.getch()
    os.system('cls')

def olegPathOneTwo():
    print("Ohhh! good choice!")
    print("The rocks are made from marshmellow...")
    print("you're having a sweet time.")
    msvcrt.getch()
    os.system('cls')














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










