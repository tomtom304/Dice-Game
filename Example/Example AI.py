"""
This version of the game is complete with a basic AI using very basic machine learning.
The rules are detailed in the README.
"""

from random import randrange  # For a die roll


def turn(gold, pot, turns, opted):
    """
    Runs one turn:
        - Takes in an option
        - Collects or rolls based on that option
    :param gold: The player gold value from the start of the turn
    :param pot: The amount of gold already in the pot at the start of the turn
    :param turns: The number of turns that have gone since the pot was emptied
    :param opted: The option inputted by the user
    :return: Updated game values from the start of the turn
    """
    # print('Gold: ' + str(gold))
    # print('Pot: ' + str(pot))
    if opted == 1:
        gold += pot
        return gold, 0, 0, opted
    elif opted == 2:
        turns += 1
        roll = randrange(1, 7)
        # print('Roll: ' + str(roll))
        if roll > 3:
            pot += roll * turns
            return gold, pot, turns, opted
        elif roll <= 3:
            gold -= pot * roll
            turns = pot = 0
            return gold, pot, turns, opted
    elif opted == 3:
        pot = 'end'
        return gold, pot, turns, opted


def play_game():
    """
    Main game function
    """
    # Set base variables
    pot = gold = total = 0
    turns = 1
    # I import data from previous games to use as upon which experience to draw
    data = open('data.txt').readlines()
    values = {}
    for line in data:
        key = ''
        value = []
        reading = 'key'
        datum = ''
        for char in line:
            if char == '#':
                break
            elif char not in [':', ' ', '\n'] and reading == 'key':
                key += char
            elif char == ':' and reading == 'key':
                reading = 'value'
            elif reading == 'value':
                if char in ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    datum += char
                elif char == ',':
                    value.append(int(datum))
                    datum = ''
        if key != '': values[int(key)] = value
    while True:
        old = pot
        try:
            # If it seems more worthwhile to collect, do so; if not, roll.
            opted = 2 if pot <= sum(values[pot]) / len(values[pot]) or pot == 0 else 1
        except KeyError:
            # If there is not record of the pot being at this value, roll
            opted = 2
        # Run the turn with the variables needed
        gold, pot, turns, opted = turn(gold, pot, turns, opted)
        if opted == 2 and old != 0:
            # If the user rolled and the pot wasn't 0, record the outcome
            try:
                values[old].append((gold + pot) - old)
            except KeyError:
                values[old] = [(gold + pot) - old]
            finally:
                pass
        total += 1
        # print(values)
        if total % 50000 == 0:  # Save all of the data collected in this run to the data storage file
            print(gold)
            print(values)
            f = open('data.txt', 'r+')
            comments = len([j for i in f.readlines() if i[0] == '#' for j in [*i, '\n']])
            f.seek(comments)
            for i in values.keys():
                f.write('\n{} : {},'.format(i, ", ".join([str(j) for j in values[i]])))
            quit()

play_game()
