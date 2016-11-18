# Dice-Game

A simple dice-based game written in Python


## Base Game

This game must:

Task 1: **Menu**

- [ ] Have a menu from which the user can:
 - [ ] Play the Game 
 - [ ] View Highscores
 - [ ] Quit

Task 2: **The Turn**

- [ ] The user starts the game with 0 gold and nothing in the pot.
- [ ] They start the turn with a choice, collect all of the gold in the pot or roll a die.
 - [ ] If the number on the die is greater than 3, then add that number to the pot multiplied by the number of turns it has been since they collected the gold in the pot.
 - [ ] If the number is less than or equal to 3, they lose the amount in the pot multiplied by the number they rolled.

Task 3: **Scores**

- [ ] The game ends if:
 - [ ] The user decides to on their turn. - A win
 - [ ] Gold drops below 0 - A lose
- [ ] If they win, the user's score is recorded. It is calculated by the user's gold total subtract the number of turns they spent playing the game.

Task 4: **Highscores**

- [ ] The user inputs a name (Less than 20 characters)
- [ ] They are then shown a list of the top 5 players and their scores along with the user's own name, score and position
- [ ] When they are finished, they are then taken back to the menu 


## Extension: AI

The next step in the development of this program is to remove all <del>humans</del> human input.

Using my version of the code (`master` branch):

Create any sort of AI (it can be connected directly to my code) and enter it into one or more of the following categories: 


## Participation

This is availiable to anyone, simply **fork** this repositiory and create your AI. 
Post your scores for each section of the above checklist on the [`Scoreboard` Issue](https://github.com/fabcooldog/Dice-Game/issues/2)
