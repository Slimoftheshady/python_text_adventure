import random
import sys, time

check = 0
end = False

#code to make cool printy text
def output(string='', duration:float=0.5): #time in seconds
    string = str(string)
    averageTime = 0
    if len(string) != 0:
        averageTime = duration/len(string)
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(averageTime)
    print()

#split up inventory to make easier to see
class PlayerInventory:
    melee = "fist"
    rangedweap = "none"
    ammo = "0"

#player class- record
playinv = PlayerInventory()
class Player:
    Level = 1
    Health = 22
    Money = 0
    locationX = 1 
    locationY = 1
    inventory = PlayerInventory

Playe = Player()

#enemy record
class Enemy:
    health = 0
    damage = 0
    xp = 0
    money = 0

#function to create an enemy
def createEnemy(player):
    enemy_info = Enemy()
    enemy_info.health = random.randint(player.Health - 5, player.Health + 5)
    enemy_info.damage = random.randint(2, player.Health - 10)
    enemy_info.xp = random.randint(1, 7)
    enemy_info.money = random.randint(5,500)
    return enemy_info

#map
def CoolMap():
    # Define the dimensions of the map
    width = 9
    height = 7

    # Create an empty list to hold the map data
    map_data = [[f'({j+1},{i+1})' for j in range(width)] for i in range(height)]

    # Define the x,y coordinates of the points you want to plot on the map
    points = [(2, 3), (4, 5), (7, 2)]

    # Convert the (x,y) coordinates to (row,column) indices for the map data
    for x, y in points:
        col = x - 1
        row = y - 1

    # Print the map
    for row in reversed(map_data):
        output(' | '.join(row))


#function for combat
def fight():
    battle = 0
    output("A soldier of The Datukruption suddenly appears!")
    enemy = createEnemy(Playe)
    print("They have {} health.".format(enemy.health))
    #line that replaces brackets with enemy.health variable
    output("Would you like to *attack*, or *defend*, or try to escape?")
    choice = input("")
    while battle == 0:
        if choice.lower() == 'escape' and random.random() < 0.5: #escape based on luck
            output("Quickly, you turn on your feet and sprint.\nThe soldier yells at you.")
            output("You managed to run away.")
            battle += 1
        elif choice.lower() == 'defend': #defense choice
            if random.random() < 0.5:
                Playe.Health = Playe.Health - (enemy.damage/2)
                if Playe.Health > 0:
                    output(f"Nice, you managed to defend the hit and only lost {(enemy.damage/2)} health.")
                    output(f"You are now at {Playe.Health} health, and the soldier is at {enemy.health} health.")
                    output("Would you like to *attack*, or *defend*, or try to escape?")
                    choice = input("")
                else:
                    output("Unfortunately, you were struck down.")
                    exit()
            else:
                Playe.Health = Playe.Health - (enemy.damage)
                output(f"Oh no, you didn't defend and lost {enemy.damage} health.")
                if Playe.Health > 0:               
                    output(f"You are now at {Playe.Health} health, and the soldier is at {enemy.health} health.")
                    output("Would you like to *attack*, or *defend*, or try to escape?")
                    choice = input("")
                else:
                    output("Unfortunately, you were struck down, and have died.")
                    exit()
        elif choice.lower() == 'attack': #attack choice
            if Playe.inventory.rangedweap == 'none' or Playe.inventory.ammo == 0:
                output(f"The only attack you have, is your {Playe.inventory.melee}")
                output("Do you still wish to *fight* it out?\n Or *run*")
                lastcheck = input("")
                if lastcheck.lower() == "run" and random.random() < 0.5:
                    output("Quickly, you turn on your feet and sprint.\nThe soldier yells at you.")
                    output("You managed to run away.")
                    battle += 1
                elif lastcheck.lower() == "fight":
                    if Playe.inventory.melee == 'fist':
                        enemy.health = enemy.health - 2
                        if enemy.health <= 0:
                            Playe.Money = Playe.Money + enemy.money
                            Playe.Level = Playe.Level + enemy.xp
                            output("You have slain the soldier!")
                            output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                            battle += 1
                        else:
                            output(f"The soldier is now at {enemy.health} health.")
                            Playe.Health = Playe.Health - enemy.damage
                            output(f"You have been struck for {enemy.damage} health.")
                            if Playe.Health <= 0:
                                output("Unfortunately, you have been killed.")
                                output("Better luck in a next reincarnation.")
                                exit()
                            else:
                                output("Would you like to *attack*, or *defend*, or try to escape?")
                                choice = input("")

                    if Playe.inventory.melee == 'dagger':
                        enemy.health = enemy.health - 3
                        if enemy.health <= 0:
                            Playe.Money = Playe.Money + enemy.money
                            Playe.Level = Playe.Level + enemy.xp
                            output("You have slain the soldier!")
                            output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                            battle += 1
                        else:
                            output(f"The soldier is now at {enemy.health} health.")
                            Playe.Health = Playe.Health - enemy.damage
                            output(f"You have been struck for {enemy.damage} health.")
                            if Playe.Health <= 0:
                                output("Unfortunately, you have been killed.")
                                output("Better luck in a next reincarnation.")
                                exit()
                            else:
                                output("Would you like to *attack*, or *defend*, or try to escape?")
                                choice = input("")

                    if Playe.inventory.melee == 'sword':
                        enemy.health = enemy.health - 4
                        if enemy.health <= 0:
                            Playe.Money = Playe.Money + enemy.money
                            Playe.Level = Playe.Level + enemy.xp
                            output("You have slain the soldier!")
                            output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                            battle += 1
                        else:
                            output(f"The soldier is now at {enemy.health} health.")
                            Playe.Health = Playe.Health - enemy.damage
                            output(f"You have been struck for {enemy.damage} health.")
                            if Playe.Health <= 0:
                                output("Unfortunately, you have been killed.")
                                output("Better luck in a next reincarnation.")
                                exit()
                            else:
                                output("Would you like to *attack*, or *defend*, or try to escape?")
                                choice = input("")
                        
                    if Playe.inventory.melee == 'spear':
                        enemy.health = enemy.health - 5
                        if enemy.health <= 0:
                            Playe.Money = Playe.Money + enemy.money
                            Playe.Level = Playe.Level + enemy.xp
                            output("You have slain the soldier!")
                            output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                            battle += 1
                        else:
                            output(f"The soldier is now at {enemy.health} health.")
                            Playe.Health = Playe.Health - enemy.damage
                            output(f"You have been struck for {enemy.damage} health.")
                            if Playe.Health <= 0:
                                output("Unfortunately, you have been killed.")
                                output("Better luck in a next reincarnation.")
                                exit()
                            else:
                                output("Would you like to *attack*, or *defend*, or try to escape?")
                                choice = input("")

                    if Playe.inventory.melee == 'axe':
                        enemy.health = enemy.health - 2
                        if enemy.health <= 0:
                            Playe.Money = Playe.Money + enemy.money
                            Playe.Level = Playe.Level + enemy.xp
                            output("You have slain the soldier!")
                            output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                            battle += 1
                        else:
                            output(f"The soldier is now at {enemy.health} health.")
                            Playe.Health = Playe.Health - enemy.damage
                            output(f"You have been struck for {enemy.damage} health.")
                            if Playe.Health <= 0:
                                output("Unfortunately, you have been killed.")
                                output("Better luck in a next reincarnation.")
                                exit()
                            else:
                                output("Would you like to *attack*, or *defend*, or try to escape?")
                                choice = input("")


                else:   
                    output("You are struck down where you stand for not making good choices.")
                    exit()
            else:
                output(f"You have your *{Playe.inventory.melee}*, or your *{Playe.inventory.rangedweap}*.")
                output("Which will you pick?")
                weapon = input("")
                if weapon.lower() == Playe.inventory.rangedweap:
                    if Playe.inventory.ammo > 0:
                        if Playe.inventory.rangedweap == "pistol":
                            enemy.health = enemy.health - 5
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if enemy.health <= 0:
                                Playe.Money = Playe.Money + enemy.money
                                Playe.Level = Playe.Level + enemy.xp
                                output("You have slain the soldier!")
                                output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                battle += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"The soldier is now at {enemy.health} health.")
                                Playe.Health = Playe.Health - enemy.damage
                                output(f"You have been struck for {enemy.damage} health.")
                                if Playe.Health <= 0:
                                    output("Unfortunately, you have been killed.")
                                    output("Better luck next time.")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*, or try to escape?")
                                    choice = input("")
                        
                        elif Playe.inventory.rangedweap == "revolver":
                            enemy.health = enemy.health - 10
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if enemy.health <= 0:
                                Playe.Money = Playe.Money + enemy.money
                                Playe.Level = Playe.Level + enemy.xp
                                output("You have slain the soldier!")
                                output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                battle += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"The soldier is now at {enemy.health} health.")
                                Playe.Health = Playe.Health - enemy.damage
                                output(f"You have been struck for {enemy.damage} health.")
                                if Playe.Health <= 0:
                                    output("Unfortunately, you have been killed.")
                                    output("Better luck next time.")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*, or try to escape?")
                                    choice = input("")

                        elif Playe.inventory.rangedweap == "shotgun":
                            enemy.health = enemy.health - 15
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if enemy.health <= 0:
                                Playe.Money = Playe.Money + enemy.money
                                Playe.Level = Playe.Level + enemy.xp
                                output("You have slain the soldier!")
                                output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                battle += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"The soldier is now at {enemy.health} health.")
                                Playe.Health = Playe.Health - enemy.damage
                                output(f"You have been struck for {enemy.damage} health.")
                                if Playe.Health <= 0:
                                    output("Unfortunately, you have been killed.")
                                    output("Better luck next time.")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*, or try to escape?")
                                    choice = input("")
                        
                        if Playe.inventory.rangedweap == "rifle":
                            enemy.health = enemy.health - 20
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if enemy.health <= 0:
                                Playe.Money = Playe.Money + enemy.money
                                Playe.Level = Playe.Level + enemy.xp
                                output("You have slain the soldier!")
                                output(f"You have recieved {enemy.money} dollars and have levelled up to {Playe.Level}")
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                battle += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"The soldier is now at {enemy.health} health.")
                                Playe.Health = Playe.Health - enemy.damage
                                output(f"You have been struck for {enemy.damage} health.")
                                if Playe.Health <= 0:
                                    output("Unfortunately, you have been killed.")
                                    output("Better luck next time.")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*, or try to escape?")
                                    choice = input("")

                    else:
                        output("You went for your weapon, not realising it had no ammo.")
                        output("Laughing, the soldier cut you down like the trash you are.")
                        exit()
                            
        else:
            output("That's not a valid input.")
            output("Would you like to *attack*, or *defend*, or try to escape?")
            choice = input("") 

#function to change location
def locationswap():
    count = 0
    while count == 0:
        output("The map is as follows:")
        output("---------------------------------------------------------------------")
        CoolMap()
        output(f"You are currently at ({Player.locationX},{Player.locationY})")
        output("---------------------------------------------------------------------")
        output("Do you want to travel *east*, *west*, *north* or *south*?")
        loc = input("")
        if loc.lower() == "east" and Player.locationX < 9:
            Player.locationX = Player.locationX + 1
            count += 1
            if check >= 3 and random.random() < 0.5:
                fight()

        elif loc.lower() == "west" and Player.locationX > 1:
            Player.locationX = Player.locationX - 1
            count += 1
            if check >= 3 and random.random() < 0.5:
                fight()
        elif loc.lower() == "north" and Player.locationY < 7:
            Player.locationY = Player.locationY + 1
            count += 1
            if check >= 3 and random.random() < 0.5:
                fight()
        elif loc.lower() == "south" and Player.locationX > 1:
            Player.locationY = Player.locationY - 1
            count += 1
            if check >= 3 and random.random() < 0.5:
                fight()            
        else:
            output("I'm sorry, you can't do that, please enter a valid input")

        output(f"You are now at ({Player.locationX},{Player.locationY})")

#help menu
helps = {"quit": exit,
        "help": "help",
        "stats" : "stats",
        "location" : locationswap,
        }

def options():
    output("Here are your options:")
    print("------------------------------------------")
    output("\x1B[3m" + "quit: quit the game" + "\x1B[0m")
    output("\x1B[3m" + "help: pulls up this menu" + "\x1B[0m")
    output("\x1B[3m" + "stats: check your character's statistics" + "\x1B[0m")
    output("\x1B[3m" + "location: changes location" + "\x1B[0m")


class Boss:
    health = 55
    damage = random.randint(11,18)

def Shop():
    purchase = False
    output(f"Welcome to Shop {random.randint(1,100)}")
    output("Here we give items for the best prices.")
    output("What would you like to buy?")
    output(f"You have ${Playe.Money}")
    output("*melee* or *ranged* weapons, *health* or *ammo*?")
    while purchase != True:
        buy = input("")
        if buy.lower() == 'melee': #check if the user wants to buy a melee weapon
            output("Which of the following would you like to purchase:")
            output("*Dagger*- $10")
            output("*Sword*- $20")
            output("*Spear*- $30")
            output("*Axe*-$50")
            weap = input("")
            if weap.lower() == "dagger" and Playe.Money >= 10:
                Playe.inventory.melee = "dagger"
                Playe.Money = Playe.Money - 10
                output("You have bought the dagger for $10!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                #buying dagger
            
            elif weap.lower() == "sword" and Playe.Money >= 20:
                Playe.inventory.melee = "sword"
                Playe.Money = Playe.Money - 20
                output("You have bought the sword for $20!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                #buying sword

            elif weap.lower() == "spear" and Playe.Money >= 30:
                Playe.inventory.melee = "spear"
                Playe.Money = Playe.Money - 30
                output("You have bought the sword for $30!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                #buying spear

            elif weap.lower() == "axe" and Playe.Money >= 50:
                Playe.inventory.melee = "axe"
                Playe.Money = Playe.Money - 50
                output("You have bought the axe for $50!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                    #buying axe
                    
            else: #code to check user enters valid input
                output("You can't do that i'm afraid.")
                output("What would you like to buy?")
                output("*melee* or *ranged* weapons, *health* or *ammo*?")


        elif buy.lower() == "ranged": #buying a gun
            output("Which of the following would you like to purchase:")
            output("*Pistol*- $50")
            output("*Revolver*- $150")
            output("*Shotgun*- $300")
            output("*Rifle*-$450")
            weap = input("")
            if weap.lower() == "pistol" and Playe.Money >= 50:
                Playe.inventory.melee = "pistol"
                Playe.Money = Playe.Money - 50
                output("You have bought the pistol for $50!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                #buying pistol
            
            elif weap.lower() == "revolver" and Playe.Money >= 150:
                Playe.inventory.melee = "revolver"
                Playe.Money = Playe.Money - 150
                output("You have bought the revolver for $150!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                #buying revolver

            elif weap.lower() == "shotgun" and Playe.Money >= 300:
                Playe.inventory.melee = "shotgun"
                Playe.Money = Playe.Money - 300
                output("You have bought the shotgun for $300!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                #buying shotgun
                    
            elif weap.lower() == "rifle" and Playe.Money >= 450:
                Playe.inventory.melee = "rifle"
                Playe.Money = Playe.Money - 450
                output("You have bought the rifle for $450!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
                #buying rifle
            else:
                output("You can't do that i'm afraid.")
                output("What would you like to buy?")
                output("*melee* or *ranged* weapons, *health* or *ammo*?")
                #code to check user enters valid input

        
        elif buy.lower() == "health": #buying health
            chec = 0
            output(f"You currently have {Playe.Health} health.")
            output("It costs $10 for 1 health")
            output("How much health would you like to get?")
            amount = int(input(""))
            chec = amount * 10
            if chec <= Playe.Money:
                Playe.Money = Playe.Money - chec
                Playe.Health = Playe.Health + amount
                output(f"You have sucessfully bought {amount} health!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
            
            else:
                output("You can't do that i'm afraid.")
                output("What would you like to buy?")
                output("*melee* or *ranged* weapons, *health* or *ammo*?")
            
        elif buy.lower() == "ammo": #buying ammo
            checu = 0
            output(f"You currently have {Playe.inventory.ammo} ammo.")
            output("It costs $8 for 1 ammo")
            output("How much ammo would you like to get?")
            amount = int(input(""))
            checu = amount * 8
            if checu <= Playe.Money:
                Playe.Money = Playe.Money - checu
                Playe.inventory.ammo = Playe.inventory.ammo + amount
                output(f"You have sucessfully bought {amount} ammo!")
                output(f"Your new balance is {Playe.Money}")
                output("Would you like to buy again? (*yes*,*no*)")
                checkag = input("")
                if checkag.lower() == 'yes':
                    output("What would you like to buy?")
                    output("*melee* or *ranged* weapons, *health* or *ammo*?")
                elif checkag.lower() == 'no':
                    output("Have a good day!")
                    purchase = True
            
            else:
                output("You can't do that i'm afraid.")
                output("What would you like to buy?")
                output("*melee* or *ranged* weapons, *health* or *ammo*?")       
        
        
        
        
        else:
            output("You can't do that i'm afraid.")
            output("What would you like to buy?")
            output("*melee* or *ranged* weapons, *health* or *ammo*?")
            #code to check user enters valid input


if __name__ == "__main__":
    
    print("""
         .AMMMMMMMMMMA.          
       .AV. :::.:.:.::MA.        
      A' :..        : .:`A       
     A'..              . `A.     
    A' :.    :::::::::  : :`A    
    M  .    :::.:.:.:::  . .M    
    M  :   ::.:.....::.:   .M    
    V : :.::.:........:.:  :V    
   A  A:    ..:...:...:.   A A   
  .V  MA:.....:M.::.::. .:AM.M   
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
:M .  .`VMMMMMMV.:A `VMMMMV .:M: 
 V.:.  ..`VMMMV.:AM..`VMV' .: V  
  V.  .:. .....:AMMA. . .:. .V   
   VMM...: ...:.MMMM.: .: MMV    
       `VM: . ..M.:M..:::M'      
         `M::. .:.... .::M       
          M:.  :. .... ..M       
          V:  M:. M. :M .V       
          `V.:M.. M. :M.V'
""")
    output("Welcome to Last Hope.\nWe hope you enjoy your stay...")
    time.sleep(2)
    print()
    print()
    
    #prologue
    output("(You wake up, feeling dizzy and disoriented)")   
    output("Hey man, you’re finally awake!")
    output("I really thought they were gonna get you eh Omar?")
    output("Wait, you don't remember me??")
    output("I'm Caleb, your best...")
    time.sleep(0.5)
    output("And only friend!")
    output("Oh ok, I'll play along with your little game.\nOur District is being controlled by The Datukruption, those evil guys that beat you up two days ago.")
    output("Luckily they didn't realise that you were part of The Liberty, otherwise you would be rotting away in prison.")
    output("Remember, everyone in The Liberty was chose because they had a special trait... speaking of, what was yours again? ")

    print("*damage*- you do more damage, *health*- you gain more health, *luck*- you become more lucky")
    
    trait = input("")
    count = 0
    while count == 0:
     if "damage" in trait.lower():
        output("That's right, I remember now. You were known as the strongest man in the land. \nI remember when you knocked out Jess with a single hit!")
        count += 1
     elif "health" in trait.lower():
        output("That's right, I remember now. You were known as the healthiest man in the land.\n I remember that you challenged everyone to knock you down, but you never fell!")
        count += 1
     elif "luck" in trait.lower():
        output("That's right, I remember now. You were known as the luckiest man in the land. \nI remember when you were the only one to find a four leaf clover!")
        count += 1
     else:
        output("I don't think that was your trait...")
        output("What was it again?")
        trait = input("")
    #boost user interaction

    output("You've really forgetten everything, haven't you?")
    output("Type *help* to get some options")
    inp = input("")
    count = 0
    while inp.lower() != "help":
        output("That doesn't seem to be a valid command yet.")
        time.sleep(1)
        output("Maybe you should type *help*?")
        inp = input("")
    options()
    
    #italic text
    print("------------------------------------------")
    output("Why don't you try *location*?")
    count = 0
    while count == 0:
        loc = input("")
        if loc.lower() == "location":
            locationswap()
            count += 1
            check = check + 1
        else:
            output("Why don't you try *location*?")
            loc = input("")
    output("As you saw, the map is made up of X and Y coordinates. Your aim is to reach (9,7)")
    
    output("Anyway, I've got to go, i'll meet you at (2,2).")
    while Player.locationX != 2 or Player.locationY != 2:
        location = input("")
        if location.lower() == "location":
            locationswap()
            check = check + 1
        elif location.lower() == "help":
            options()
        else:
            output("Why don't you go to (2,2)?")
            output("Remeber, you can always type *help* if you're unsure.")
   
    
    output("Nice, you made it!")
    output("Listen, everytime you move, you have the chance to encounter an enemy soldier or a shop.")
    output("Defeating an enemy gives you money, which allows you to buy things.")
    output("Also, as you level up, you have access to more items in the store.")
    output("Good luck, i'll see you soon.")
    while end == False: #ending location for boss fight
        if Player.locationX == 9 and Player.locationY == 7:
            end = True
        
        #shop locations
        elif Player.locationX == 5 and Player.locationY == 1:
            Shop()
        elif Player.locationX == 1 and Player.locationY == 4:
            Shop()
        elif Player.locationX == 3 and Player.locationY == 5:
            Shop()
        elif Player.locationX == 7 and Player.locationY == 3:
            Shop()
        elif Player.locationX == 8 and Player.locationY == 2:
            Shop()
        elif Player.locationX == 9 and Player.locationY == 6:
            Shop()
        elif Player.locationX == 6 and Player.locationY == 7:
            Shop()          
        else:
            ent = input("")
            if ent.lower() == "help":
                options()
            elif ent.lower() == "location":
                locationswap()
                check = check + 1
            elif ent.lower() == "stats":
                for key, value in Player.__dict__.items():
                    if not key.startswith("__") and key not in ['locationX', 'locationY', 'inventory']:
                        if key == 'Money':
                            output(key + ' $' + str(value))
                        elif key == 'Health':
                            output(key + ' ' + str(value) + 'HP')
                        elif key == 'Level':
                            output('Level ' + str(value))
                output("Current Location ({},{})".format(Playe.locationX, Playe.locationY))
                #this code prints out the player statistics, and removes some code in a Class e.g __doc__

            elif ent.lower() == "quit":
                exit()
            else:
                output("Remember, you can always type help.")

    output("You have finally reached the end.")
    time.sleep(1)
    output("This is where the final battle is.")
    time.sleep(1)
    output("The young man from the slums.")
    time.sleep(1)
    output("Versus The Datukruption.")
    time.sleep(1)
    output("It all comes down to this.")
    time.sleep(1)

    boss = Boss()
    output("You look in front of you, and looming in the darkness, is the Leader...")
    time.sleep(2)
    output("Datuk the Destroyer!")
    output("Datuk has {} health and {} damage.".format(boss.health, boss.damage))
    
    final = 0
    output("Would you like to *attack*, or *defend*")
    choice = input("")
    while final != 1:
        if choice.lower() == 'defend':
            if random.random() < 0.5:
                Playe.Health = Playe.Health - (boss.health/2)
                if Playe.Health > 0:
                    output(f"Nice, you managed to defend the hit and only lost {(boss.damage/2)} health.")
                    output(f"You are now at {Playe.Health} health, and Datuk is at {boss.health} health.")
                    output("Would you like to *attack*, or *defend*?")
                    choice = input("")
                else:
                    output("Laughing, Datuk cut you down.")
                    output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                    exit()
            else:
                Playe.Health = Playe.Health - (boss.damage/2)
                output(f"Oh no, you didn't defend and lost {boss.health} damage.")
                if Playe.Health > 0:               
                    output(f"You are now at {Playe.Health} health, and Datuk is at {boss.health} health.")
                    output("Would you like to *attack*, or *defend*?")
                    choice = input("")
                else:
                    output("Laughing, Datuk cut you down.")
                    output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                    exit()
                    
        elif choice.lower() == 'attack':
            if Playe.inventory.rangedweap == 'none' or Playe.inventory.ammo == 0:
                if Playe.inventory.melee == 'fist':
                    boss.health = boss.health - 2
                    if boss.health <= 0:
                        output("You have given Datuk a fatal wound!")
                        final += 1
                    else:
                        output(f"Datuk is now at {boss.health} health.")
                        Playe.Health = Playe.Health - boss.damage
                        output(f"You have been struck for {boss.damage} health.")
                        if Playe.Health <= 0:
                            output("Laughing, Datuk cut you down.")
                            output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                            exit()
                        else:
                            choice = input("Would you like to *attack*, or *defend*? ")

                elif Playe.inventory.melee == 'dagger':
                        boss.health = boss.health - 3
                        if boss.health <= 0:
                            Playe.Money = Playe.Money + boss.money
                            Playe.Level = Playe.Level + boss.xp
                            output("You have given Datuk a fatal wound!")
                            final += 1
                        else:
                            output(f"Datuk is now at {boss.health} health.")
                            Playe.Health = Playe.Health - boss.damage
                            output(f"You have been struck for {boss.damage} health.")
                            if Playe.Health <= 0:
                                output("Laughing, Datuk cut you down.")
                                output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                exit()

                            else:
                                output("Would you like to *attack*, or *defend*?")
                                choice = input("")

                elif Playe.inventory.melee == 'sword':
                        boss.health = boss.health - 4
                        if boss.health <= 0:
                            Playe.Money = Playe.Money + boss.money
                            Playe.Level = Playe.Level + boss.xp
                            output("You have give Datuk a fatal wound!")
                            final += 1
                        else:
                            output(f"Datuk is now at {boss.health} health.")
                            Playe.Health = Playe.Health - boss.damage
                            output(f"You have been struck for {boss.damage} health.")
                            if Playe.Health <= 0:
                                output("Laughing, Datuk cut you down.")
                                output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                exit()

                            else:
                                output("Would you like to *attack*, or *defend*?")
                                choice = input("")
                        
                elif Playe.inventory.melee == 'spear':
                        boss.health = boss.health - 5
                        if boss.health <= 0:
                            Playe.Money = Playe.Money + boss.money
                            Playe.Level = Playe.Level + boss.xp
                            output("You have give Datuk a fatal wound!")
                            final += 1
                        else:
                            output(f"Datuk is now at {boss.health} health.")
                            Playe.Health = Playe.Health - boss.damage
                            output(f"You have been struck for {boss.damage} health.")
                            if Playe.Health <= 0:
                                output("Laughing, Datuk cut you down.")
                                output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                exit()
                            else:
                                output("Would you like to *attack*, or *defend*?")
                                choice = input("")

                elif Playe.inventory.melee == 'axe':
                        boss.health = boss.health - 2
                        if boss.health <= 0:
                            Playe.Money = Playe.Money + boss.money
                            Playe.Level = Playe.Level + boss.xp
                            output("You have given Datuk a fatal wound!")
                            final += 1
                        else:
                            output(f"Datuk is now at {boss.health} health.")
                            Playe.Health = Playe.Health - boss.damage
                            output(f"You have been struck for {boss.damage} health.")
                            if Playe.Health <= 0:
                                output("Laughing, Datuk cut you down.")
                                output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                exit()
                            else:
                                output("Would you like to *attack*, or *defend*?")
                                choice = input("")
            
            else:
                output(f"You have your *{Playe.inventory.melee}*, or your *{Playe.inventory.rangedweap}*.")
                output("Which will you pick?")
                weapon = input("")
                if weapon.lower() == Playe.inventory.rangedweap:
                    if Playe.inventory.ammo > 0:
                        if Playe.inventory.rangedweap == "pistol":
                            boss.health = boss.health - 5
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if boss.health <= 0:
                                Playe.Money = Playe.Money + boss.money
                                Playe.Level = Playe.Level + boss.xp
                                output("You have given Datuk a fatal wound!")
                                
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                final += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"Datuk is now at {boss.health} health.")
                                Playe.Health = Playe.Health - boss.damage
                                output(f"You have been struck for {boss.damage} health.")
                                if Playe.Health <= 0:
                                    output("Laughing, Datuk strikes you down where you stand for not making good choices.")
                                    output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*?")
                                    choice = input("")
                        
                        elif Playe.inventory.rangedweap == "revolver":
                            boss.health = boss.health - 10
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if boss.health <= 0:
                                Playe.Money = Playe.Money + boss.money
                                Playe.Level = Playe.Level + boss.xp
                                output("You have given Datuk a fatal wound!")
                                
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                final += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"Datuk is now at {boss.health} health.")
                                Playe.Health = Playe.Health - boss.damage
                                output(f"You have been struck for {boss.damage} health.")
                                if Playe.Health <= 0:
                                    output("Laughing, Datuk strikes you down where you stand for not making good choices.")
                                    output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*?")
                                    choice = input("")

                        elif Playe.inventory.rangedweap == "shotgun":
                            boss.health = boss.health - 15
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if boss.health <= 0:
                                Playe.Money = Playe.Money + boss.money
                                Playe.Level = Playe.Level + boss.xp
                                output("You have given Datuk a fatal wound!")
                                
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                final += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"Datuk is now at {boss.health} health.")
                                Playe.Health = Playe.Health - boss.damage
                                output(f"You have been struck for {boss.damage} health.")
                                if Playe.Health <= 0:
                                    output("Laughing, Datuk strikes you down where you stand for not making good choices.")
                                    output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*?")
                                    choice = input("")
                        
                        if Playe.inventory.rangedweap == "rifle":
                            boss.health = boss.health - 20
                            Playe.inventory.ammo = Playe.inventory.ammo - 1

                            if boss.health <= 0:
                                Playe.Money = Playe.Money + boss.money
                                Playe.Level = Playe.Level + boss.xp
                                output("You have given Datuk a fatal wound!")
                                
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                final += 1
                            else:
                                output(f"You now have {Playe.inventory.ammo} ammo left.")
                                output(f"Datuk is now at {boss.health} health.")
                                Playe.Health = Playe.Health - boss.damage
                                output(f"You have been struck for {boss.damage} health.")
                                if Playe.Health <= 0:
                                    output("Laughing, Datuk strikes you down where you stand for not making good choices.")
                                    output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                                    exit()
                                else:
                                    output("Would you like to *attack*, or *defend*")
                                    choice = input("")

                    else:
                        output("You went for your weapon, not realising it had no ammo.")
                        output("Laughing, the Datuk cut you down.")
                        output(f"\x1B[3m" + "Datuk: How dare a street urchin dare challenge me." + "\x1B[0m")
                        exit()
        else:
            output("That is not a valid command.")
            output("Would you like to *attack*, or *defend*")
            choice = input("")
        

    output(f"\x1B[3m" + "Datuk: Well, you've somehow beaten me." + "\x1B[0m")
    output(f"\x1B[3m" + "Datuk: Would you like to finish this in a game of coin flip?" + "\x1B[0m")
    lastchoice = input("")
    #fun little game of chance to finish off game.

    if lastchoice.lower() == 'no':
        output(f"\x1B[3m" + "Datuk: Oh well, it was worth a try." + "\x1B[0m")
        output("Congratuations player, you have slain Datuk and toppled The Corruption!")
        exit()

    elif lastchoice.lower() == 'yes':
        output(f"\x1B[3m" + "Datuk: What will it be?\nDatuk: I shall pick heads." + "\x1B[0m")
        coin_faces = ["Heads", "Tails"]
        for i in range(random.randint(5, 15)):
            if random.random() < 0.5:
                output("Heads")
            else:
                output("Tails")

        output("The coin stops spinning.")
        time.sleep(4)
        result = random.choice(coin_faces)
        output(result)
        if result == 'Heads':
            output("""
                            ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \
            /   /     ||--+--|--+-/-|     \   \
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
""")
    output(f"\x1B[3m" + "Datuk: Ah yes, I always win." + "\x1B[0m")
    output(f"\x1B[3m" + "You feel a buring sensation in your stomach\nAs you look down, you spot a silver dagger portruding from your chest." + "\x1B[0m")
    output(f"\x1B[3m" + "Unfortunately, you left your life to chance, and she has not smiled upon you." + "\x1B[0m")
    output(f"\x1B[3m" + "You have been slain." + "\x1B[0m")
    exit()
else:
    output(f"\x1B[3m" + "Datuk: How could I lost to a mere vangrat?" + "\x1B[0m")
    output("Congratuations player, you have slain Datuk and toppled The Corruption!")
    exit()
