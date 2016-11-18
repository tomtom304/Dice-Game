"""
This version of the game is designed for human interaction.
The rules are detailed in the README.
"""

from random import randrange  # For a die roll


def turn(gold, pot, turns):
    """
    Runs one turn:
        - Takes in an option
        - Collects or rolls based on that option
    :param gold: The player gold value from the start of the turn
    :param pot: The amount of gold already in the pot at the start of the turn
    :param turns: The number of turns that have gone since the pot was emptied
    :return: Updated game values from the start of the turn
    """
    print('Gold: ' + str(gold))
    print('Pot: ' + str(pot))
    opted = int(input("""
    1> Collect
    2> Roll
    3> End
    """))
    if opted == 1:
        gold += pot
        return gold, 0, 0
    elif opted == 2:
        turns += 1
        roll = randrange(1, 7)
        print('Roll: ' + str(roll))
        if roll >= 3:
            pot += roll * turns
            return gold, pot, turns
        elif roll <= 2:
            gold -= pot * roll
            turns = pot = 0
            return gold, pot, turns
    elif opted == 3:
        pot = 'end'
        return gold, pot, turns


def playgame():
    """
    Main game function
    """
    # Set base variables
    pot = gold = total = 0
    turns = 1
    while pot != 'end':
        # Runs one turn
        gold, pot, turns = turn(gold, pot, turns)
        total += 1
    print('Score: {} \n ({} - {})'.format(str(gold - total), gold, total))
    quit()

playgame()
