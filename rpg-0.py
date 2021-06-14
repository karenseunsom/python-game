from character import Character
from weapons import Weapons
import random

# ----------------

inventory = []
banana = Weapons('Banana', 2)
sword = Weapons('Sword', 8)
monkey_bomb = Weapons('Monkey Bomb', 6)
duck = Weapons('DigitalCrafts Duck', 5)
bootcamp = Weapons('Coding Bootcamp',10)



def main():
    user_hero = input('What would you like to name your hero? ')
    # hero = Character(user_hero)
    goblin = Character('Goblin', health=20, power=4)
    mamagoblin = Character('Mama Goblin', health=50, power=12)
    special  = int(input(f"""
What special would you like, {user_hero}?
1. MAX HP
2. + 10 Power
3. Cuddly Pet
> """))
    if special == 1:
        hero = Character(user_hero, health=500)
        print("\nYOU NOW HAVE A MAX HP OF 500.")
    elif special == 2:
        hero = Character(user_hero, power=15)
        print("\n*10 POWER HAS BEEN ADDED*")
    elif special == 3:
        hero = Character(user_hero)
        cuddlypet = Character('Cuddly Pet', health=99999, power=500)
        # inventory.append(cuddlypet.name)
        print(f"\n{cuddlypet.name} stored in inventory.")

    while hero.is_alive and goblin.is_alive:
        print(f'''
~~~~~~~~~~CURRENT STATS~~~~~~~~~~~
{hero}
{goblin}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        print("> ",)
        print("""What do you want to do?
1: Punch goblin
2: Nothing
3. Flee """)
        user_input = input('> ')
        if user_input == '1':
            hero.attack(goblin)
            if goblin.health <= 0:
                print("The goblin is dead.")
                # exit()
                break
        elif user_input == '2':
            pass
        elif user_input == '3':
            print(f"You escaped goblin.")
            break
        else:
            print(f"Invalid input: {user_input}")
        if goblin.is_alive:
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")
                exit()
    
    if goblin.health <= 0:
        print("\nMama Goblin did not like that.")
    else: print("\nWhile fleeing, you encountered another fiend.")

    while hero.is_alive and mamagoblin.is_alive:
        print(f'''
~~~~~~~~~~CURRENT STATS~~~~~~~~~~~
{hero}
{mamagoblin}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        user_input_2 = int(input('''What would you like to do? 
1. Spin mystery box 
2. Use Cuddly Pet to attack
3. Attempt to hug Mama Goblin
> '''))
        if user_input_2 == 1:
            mystery_box = [sword, banana, monkey_bomb, bootcamp]
            choice = random.choice(mystery_box)
            print(f'{choice.use(mamagoblin)}')
            if choice == bootcamp:
                print("It was super effective!")
            if mamagoblin.health <= 0:
                print('Mama Goblin is ded')
                exit()
        elif user_input_2 == 2 and special == 3:
            cuddlypet.attack(mamagoblin)
            if mamagoblin.health <= 0:
                print("""OVERKILL! Cuddly Pet is OP and needs a nerf!
Mama Goblin was demolished.""")
                exit()                
        if user_input_2 == 2 and special != 3:
            print("You do not have Cuddly Pet in your inventory.")
        elif user_input_2 == 3:
            mamagoblin.attack(hero)
            print("Hug attempt not very effective.")
        if mamagoblin.is_alive and user_input_2 != 3:
            mamagoblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")
                exit()
    
        

            
            


    

# Need to add try and except for invalid inputs ?

main()
