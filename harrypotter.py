def play_again():
    print('\nDo you want to play again? (y or n)')

    answer = input('>').lower()

    if 'y' in answer:
        start()
    else:
        exit()

def game_over(reason):
    print('\n' + reason)
    print('Game over!')
    play_again()

def galleon_room():
    print('\nYou are now in a room filled with Galleons!')
    print('And there is a door too.')
    print('What would you like to do? (1 or 2)')
    print('1. Take some Galleons and go through the door.')
    print('2. Just go through the door.')

    answer = input('>')

    if answer == '1':
        game_over('The galleons were cursed. Now you cannot mgo outside.')
    elif answer == '2':
        print('Honesty is the best policy.....You won :)')
        play_again()
    else:
        game_over('First learn how to write numbers.')

def monster_room():
    print('\nYou entered the room of a monster.')
    print('The monster is drinking unicorn bloog, there is an another door. What would you like to do? (1 or 2)')
    print('1. Go through the doors silently.')
    print('2. Kill the monster and show your courage.')

    answer = input('>')

    if answer == '1':
        galleon_room()
    elif answer =='2':
        game_over('The monster was hungry, he ate you.')
    else:
        game_over('Go and learn how to type a number?')


def fluffy_room():
    print('\nThere is a three-headed dog here.')
    print('Behind the dog is another door.')
    print('Fluffy is eating zombie flesh.')
    print('What would you like to do? (1 or 2)')
    print('1. Take the flesh.')
    print('2. Play flute.')

    answer = input('>')

    if answer == '1':
        game_over('Fluffy killed you.')
    elif answer == '2':
        print('Congratulations, Fluffy slept. You can go through the doors now.')
        galleon_room()
    else:
        game_over('Dont you know, how to type a number')

def start():
    print('\nYou are in a dark room.')
    print('There is a door to your left and right, which one do you take? (l or r)')

    answer = input('>').lower()

    if 'l' in answer:
        fluffy_room()
    elif 'r' in answer:
        monster_room()
    else:
        game_over('Dont you know how to type something properly?')

start()
