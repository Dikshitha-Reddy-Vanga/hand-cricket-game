# Hand Cricket Game (Python CLI)

A command-line based Hand Cricket game built using Python. This project simulates the popular hand cricket game played using numbers, where the user competes against an AI opponent.

---

## Project Overview

The Hand Cricket Game is a simple interactive terminal game where the player plays against the computer. The game begins with a toss (Odd/Even), followed by batting and bowling phases. The objective is to score more runs than the opponent without getting out.

---

## Features

* Toss system (Odd or Even)
* Choice to bat or bowl based on toss result
* Batting and bowling gameplay mechanics
* Random AI moves using Python's random module
* Real-time score updates
* Match result display (Win/Loss/Tie)

---

## Tech Stack

* Python 3
* Random module (for AI behavior)

---

## Project Structure

```id="h3k9sd"
Hand Cricket.py
README.md
```

---

## How to Run

1. Make sure Python is installed on your system
2. Download or clone the repository
3. Open terminal or command prompt
4. Navigate to the project folder

Run the program using:

```id="l2p8qs"
python "Hand Cricket.py"
```

---

## How to Play

* Choose Odd or Even for toss
* Enter a number between 1 and 6
* If you win the toss, choose to bat or bowl
* During batting:

  * Enter numbers between 1 and 6
  * If your number matches AI's number, you are out
* During bowling:

  * Try to match AI’s number to get it out
* Player with the higher score wins

---

## Future Improvements

* Add input validation for better user experience
* Implement multiple difficulty levels
* Add scoreboard history
* Convert into GUI-based game using Tkinter or Pygame
* Add multiplayer mode

---

## Author

Dikshitha Reddy Vanga

---

## License

This project is open-source and available under the MIT License.
