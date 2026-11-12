#5. Create a Number Guessing Game where:
  # ● The program generates a random number between 1 and 50 using random.
  # ● The user has 5 attempts to guess the number.


import random
import math
guess_number = random.randint(1,50)

print("you have 5 attempts guess the random number 1 to 50")

for attempt in range(5):
    guess = int(input("guess the number between 1 to 50"))

    difference =math.fabs(guess_number - guess)
    print("you are",difference,"away from the guess number")

    

    if guess == guess_number:
                print("correct")
                break

    elif guess > guess_number:
        print("very high")

    else:
        print("very low")

else:
    print("no attempts left,the number is :",guess_number)
