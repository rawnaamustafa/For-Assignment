import math
import random

lower_num = int(input("Pleae enter lower number: "))
upper_num = int(input("Pleae enter upper number: "))

number = random.randint(lower_num , upper_num)
print("You only have " , round(math.log(upper_num - lower_num + 1 , 2)))

c=0
while c < math.log(upper_num - lower_num + 1 , 2):
    c = c+ 1
    guess = int(input("What is the number you guessed : "))
    if guess == number:
        print("Congratulations, you won")
        break
    elif guess < number:
        print("You guessed a small number , Please try again")
    else:
        print("You guessed a big number , Please try again")

