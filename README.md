# Number-guessing-game-
A simple game in which the user has to guess a number between 1 and 100.

## How to Play
The computer generates a random number between 1 and 100. Your task is to guess the number with as few attempts as possible. After each guess, you'll receive a hint:
- "Let's try a higher number." if your guess is lower than the secret number
- "Nope.The number is lower." if your guess is higher than the secret number
- "Correct!" when you guess correctly

## Requirements
- Python 3.x

## Running the Game
```bash
python3 game.py
```

## Example Gameplay
```
Guess a number between 1 and 100!
Enter your guess: 50
Let's try a higher number.
Enter your guess: 25
Nope.The number is lower.
Enter your guess: 37
Correct! You needed 3 attempts to guess the number.
```