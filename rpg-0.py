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
people_at_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tip = [1.01, 2.05, 2.42, 2.54, 2.95, 3.78, 3.67, 4.74, 5.30, 6.29, 7.85, 7.94, 8.93, 10.45, 11.24, 12.56, 13.59, 14.32, 15.04]
kids = {'Billy': 'Where do babies come from?',
'Sally': 'Why is the sky blue?',
'Rodolfo': 'Why is the moon made out of cheese?',
'Bravo': "Why can't I see my eyes?",
'Charlie': 'Where do thoughts come from?',
'Badger': 'Is santa real?',
'Steph': "Why don't crabs have eyebrows?"}
coffee_list = ['Venti Caramel Ribbon Crunch Frappuccino with five bananas, extra caramel drizzle, extra whipped cream, extra ice, extra Cinnamon Dolce Sprinkles, seven pumps of Dark Caramel Sauce, extra Caramel Crunch Topping, one pump Honey Blend, extra Salted Butter Topping, five pumps of Frappuccino Roast, and seven Frappuccino Chips, made with heavy cream and double-blended',
'iced Americano with six different kinds of milk, seven different sweeteners, eight pumps of syrup... and light ice', 'trenta green tea with 35 pumps of sugar and no water', 'venti 9 shot, 1 pump mocha, nonfat, no whip, with exactly 4 shakes of cinnamon stirred in',
'venti vanilla latte, nonfat milk, whipped cream, 7 Splendas; 6 mixed in, one sprinkled on top of the whipped cream',
'iced, Ristretto, 10 shot, venti, with breve, 5 pump vanilla, 7 pump caramel, 4 Splenda, ahd poured, not shaken',
'half caramel machiatto, half hazelnut latte', 'venti 7 pump vanilla soy 12 scoop matcha 180 degree NO FOAM green tea latte',
'A venti berry hibiscus refresher with 25 Equals',
'Grande in a venti cup, 20-pump vanilla, 20-pump hazelnut, whole milk, 190 degree, add whip and extra caramel drizzle latte']


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
1: Fight goblin
2: Nothing
3. Flee """)
        user_input = input('> ')
        if user_input == '1':
            hero.attack(goblin)
            if goblin.health <= 0:
                print("\nThe goblin is dead.")
                input("\nDLC pack needed to continue. OK to purchase? ")
                break
        elif user_input == '2':
            pass
        elif user_input == '3':
            print(f"You escaped goblin.")
            input("\nDLC pack needed to continue. OK to purchase? ")
            break
        else:
            print(f"""INVALID INPUT! '{user_input}'
Goblin attacks anyways.""")
        if goblin.is_alive:
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")
                exit()
    if goblin.health <= 0:
        print("\nMama Goblin did not enjoy the death of their child.")
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
                break
        elif user_input_2 == 2 and special == 3:
            cuddlypet.attack(mamagoblin)
            if mamagoblin.health <= 0:
                print("""OVERKILL! Looks like Cuddly Pet needs a nerf.""")
                break               
        elif user_input_2 == 2 and special != 3:
            print("You do not have Cuddly Pet in your inventory.")
        elif user_input_2 == 3:
            mamagoblin.attack(hero)
            print("Hug attempt not very effective.")
        else: print(f"""INVLID INPUT: {user_input_2} !
Mama Goblin attacks anyways.""")
        if mamagoblin.is_alive and user_input_2 != 3:
            mamagoblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")
                exit()
    print(f"\n{hero.name} has decided it's time to take a step back from the violent life.")
    user_input_3 = int(input("""What new job would you like?
1: Server at a Brazillian Steakhouse
2: Grade School Teacher
3: Barista at Local Coffee Shop
> """))
    if user_input_3 == 1:
        print("*** AT THE BRAZILLIAN STEAKHOUSE ***")
        index = 0
        tables = int(input("How many tables would you like to serve today? "))
        while index < tables:
        # table = input("\nDo you want to wait a table? ")
        # while table == 'Yes' or 'yes':
            total_tip = float(random.choice(tip))
            hero.money += total_tip
            print(f'\nA table of {random.choice(people_at_table)} left you a ${total_tip} tip.')
            index += 1
        print('\nYou made a GRAND TOTAL of $%.2f today!' % hero.money)
        print(f"\n  Thanks for playing, {hero.name}.\n")
    if user_input_3 == 2:
        print("*** IN THE CLASSROOM ***")
        while True:
            choices = int(input("""\nWhat would you like to do?
1. View student list
2. Hear questions from students
3. Leave classroom
> """))
            if choices == 1:
                for key in kids:
                    print(key)
            if choices == 2:
                student = input("Who's question would you like to hear? ")
                print(f'\n{kids[student]}')
            if choices == 3:
                print("The kids appreciate you taking their questions.")
                print(f"\n  Thanks for playing, {hero.name}.\n")
                break
    if user_input_3 == 3:
        print("*** First Day of Training at Coffee Shop ***")
        while True: 
            coffee_choice = int(input("""
1. Take customer order
2. Quit Job
> """))
            if coffee_choice == 1:
                print(f"\nCustomer: Hi, I would like a {random.choice(coffee_list)}.")
            if coffee_choice == 2:
                print('Sorry about your first day on the job.')
                print(f"\n  Thanks for playing, {hero.name}.\n")
                break

# Need to add try and except for invalid inputs ?

main()
