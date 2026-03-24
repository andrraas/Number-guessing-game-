# Number-guessing-game-
A simple game in which the user has to guess a number.

## How to Play
The computer generates a random number between 1 and 100. Your task is to guess the number with as few attempts as possible. After each guess, you'll receive a hint:
- "Too low!" if your guess is lower than the secret number
- "Too high!" if your guess is higher than the secret number
- "Congratulations!" when you guess correctly

## Requirements
- Python 3.x

## Running the Game
```bash
python3 game.py
```

## Example Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Can you guess what it is?
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Congratulations! You guessed it in 3 attempts.
```