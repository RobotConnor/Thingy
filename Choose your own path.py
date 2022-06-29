import random
#num=random.randint(1, 10)
name=input("Dungeon Master: What is your name? ")
print("Dungeon Master: Okay, "+name+". To select a path, type in the exact wording of the choice you want to select.")
rename=input("Choose: rename or continue? ")
while rename == "rename":
    name=input("Dungeon Master: What is your name? ")
    rename=input("Choose: rename or continue? ")
print("DM: You awake in a dark cave with nothing but a pickaxe in your hand.")
playerdamage=1
playerweapon="pickaxe"
print("DM: You have no memeory of how you got here. No memory of a before. As you stand up, you hear giggling. You see a goblin coming around the corner.")
battlechoice=input("Choose: diplomacy or attack. ")
if battlechoice == "diplomacy":
    print(name+": Don't attack! I'm unarmed!")
    print("Goblin: *Indecipherable snickers and snorts*")
    print("DM: The goblin clearly doesn't understand you. You see it unsheathe a dagger.")
print("DM: You pull out your "+playerweapon+", and ready for combat.")
enemylive="true"
playerlive="true"
enemyhealth=2
enemyhealth=int
while enemylive == "true" and playerlive == "true":
    playerattackchoice=input("Choose: attack, defend, or retreat. ")
    if playerattackchoice=="retreat":
        print("DM: You try to escape, but the goblin blocks the one way out!")
    elif playerattackchoice=="defend":
        print("DM: You brace yourself for the incoming attack.")
    else:
        enemyhealth-1=newenemyhealth
        if newenemyhealth==0:
            enemylive="false"
        print("DM: You attack the goblin, dealing 1 damage!")
    enemymiss=random.randint(1, 3)
    if enemymiss > 1:
        print("DM: The goblin stabs the air right next to you")
    else:
        print("DM: The goblin stabs you, dealing 1 damage!")
    playerattackchoice=input("Choose: attack, defend, or retreat. ")
    if playerattackchoice=="retreat":
        print("DM: You try to escape, but the goblin blocks the one way out!")
    elif playerattackchoice=="defend":
        print("DM: You brace yourself for the incoming attack.")
    else:
        newenemyhealth-1=enemyhealth
        if enemyhealth==0:
            enemylive="false"
        print("DM: You attack the goblin, dealing 1 damage!")
    enemymiss=random.randint(1, 3)
    if enemymiss > 1:
        print("DM: The goblin stabs the air right next to you")
    else:
        print("DM: The goblin stabs you, dealing 1 damage!")
if enemylive == "false":
    print("DM: The Goblin falls to the ground unconcious.")
    


    
    
