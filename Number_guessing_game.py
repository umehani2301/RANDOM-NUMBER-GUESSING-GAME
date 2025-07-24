import random

random_number = random.randint(1,100)
attempts = 0

print("\n--------WELCOME TO NUMBER GUESSING GAME--------")
print("\n\n I'm Thinking of a number between 1..100 🤔")

while True:
    guess = int(input("\nTake a Guess: "))

    if guess > random_number:
        print("The number you have guess is too high📈")
        attempts+=1

    elif guess < random_number:
        print("The number you have guessed is too low📉")
        attempts+=1

    else:
        print(f"CONGRATULATION 🎉 You have finally guess the number in {attempts} attempts👏 ")
        break
    


    