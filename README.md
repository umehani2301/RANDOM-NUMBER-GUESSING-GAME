# 🎲 Random Number Guessing Game

Welcome to the **Random Number Guessing Game** – a simple yet fun project made with just *core Python*.  
The goal? Guess the number the computer's thinking of. The twist? You only find out if you're too high, too low, or spot-on. 🔥

---

## 📌 Features

- Random number generated using `random` module
- User input handled with proper validations
- Keeps count of how many attempts you take
- Loop continues until the user guesses correctly
- Fully terminal/console based – no GUI, pure desi Python 🐍

---

## 🧠 How It Works

1. The computer picks a random number between 1 and 100.
2. You, the player, start guessing.
3. The program will guide you by telling you:
   - `"Too low!"` if your guess is less than the number
   - `"Too high!"` if your guess is more than the number
   - `"Bingo!"` if your guess is correct 🎯
4. It tracks how many guesses you took before winning.

---

## 🚀 How to Run

```bash
# Make sure Python is installed
python random_guess_game.py
