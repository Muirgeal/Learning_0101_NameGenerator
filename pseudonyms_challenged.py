"""Generate funny names by randomly combining names from 3 separate lists."""

import sys
import random

print("\n")
print("Welcome to the Psych 'Sidekick Name Picker' \n")
print("A name just like Sean would pick for Gus: \n \n")

first = ('Baby Oil', 'Bad News', 'Big Burps', 'Bill',
         'Bob', 'Bowel Noises', 'Boxelder', 'Bud',
         'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
         'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
         'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
         'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
         'Huggy', 'Ignatious', 'Jimbo', 'Joe', 'Johnny',
         'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
         '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
         'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
         'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
         'Sid', 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
         'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
         'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
         'Winston', 'Worms')

middle = ('"Beenie-Weenie"', '"Stinkbug"', '"Lite"', '"Pottin Soil"',
          '"The Squirts"', '"Jazz Hands"', '"The Big News"', '"Grunts"',
          '"Tinkie Winkie"', '"Howling Dog"', '"Hot Shot"', '"Wait-for-it"')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
        'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
        'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
        'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
        'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
        'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
        'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
        'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
        'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
        'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette',
        'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
        'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

while True:

    first_name = random.choice(first)

    last_name = random.choice(last)

    print("\n")

    # Middle name is chosen only 30% of the time.
    if random.random() > 0.3:
        # Trick IDLE by using "fatal error" setting to print name in red.
        print("{} {}".format(first_name, last_name), file = sys.stderr)
    else:
        middle_name = random.choice(middle)
        print("{} {} {}".format(first_name, middle_name, last_name), file = sys.stderr)

    print("\n")

    try_again = input("Try again? (Press ENTER else N to quit.)\n")
    if try_again.lower() == "n":
        break

input("\nPress ENTER to exit.")
