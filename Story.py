#Here will take place the wole story
from Character import Character
def clear_console():
    print("\033c", end="")
    
def CreateCharacter():
    hero = ""
    while hero != "A" and hero != "W":
        print("You're about to experience a journey in a fantasy world.\nChoose your hero:")
        print("Do you want to be a Warrior ? (W)")
        print("Do you want to be an Archer ? (A)")
        hero = input().upper()

    print("Choose the name of your hero:")
    myname = str(input())
    character = Character(hero, name=myname)
    character.set_attributes()
    character.assign_inventory()
    return character

def displayStatistics():
    hero.display_attributes()




hero = CreateCharacter()
displayStatistics()

