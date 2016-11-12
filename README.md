# Dice-Game

A simple dice-based game written in Python


## Specification

This game must:

Task 1: **Menu**

- [ ] Have a menu from which the user can:
 - [ ] Play the Game 
 - [ ] View Highscores
 - [ ] Quit

Task 2: **The Turn**

- [ ] The user starts the game with 0 gold and nothing in the pot.
- [ ] They start the turn with a choice, collect all of the gold in the pot or roll a die.
 - [ ] If the number on the die is greater than 3, they add that number to the pot multiplied by the number of turns it has been since they collected the gold in the pot.
 - [ ] If the number is less than or equal to 3, they lose the amound in the pot multiplied by the number they rolled.

Task 3: **Scores**

- [ ] The game ends if:
 - [ ] The user decides to on their turn. - A win
 - [ ] Gold drops below 0 - A lose
- [ ] If they win, the user's score is recorded. It is calculated by the user's gold total subtract the number of turns they spent playing the game.

Task 4: **Highscores**

- [ ] The user inputs a name (Less than 20 characters)
- [ ] They are then shown a list of the top 5 players and their scores along with the user's own name, score and position
- [ ] When they are finished, they are then taken back to the menu 
