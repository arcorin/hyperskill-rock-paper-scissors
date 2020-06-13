# Stage 5/5
# More options

import random
import math

start_list = "Tim 350\nJane 200\nAlex 400\n"

rating = open("rating.txt", "w")
rating.write(start_list)
rating.close()

name = input("Enter your name: ")
print(f"Hello, {name}")

choice_list = ["scissors", "rock", "paper"]
users_list = input("Game words: ")
if users_list not in ["", " "]:
    choice_list = users_list.split(',')

score = 0

# check if user_name is in rating.txt file
rating = open("rating.txt", "r+")
scores_list = rating.read().splitlines()
for s in scores_list:
    s = s.split()
    s[1] = int(s[1])
    if s[0] == name:
        score = s[1]
print("Okay, let's start")
print(f"Your rating: {score}")

def ask_user():
    global user_choice
    user_choice = input("Choose a word (or !rating, or !exit): ")

    if user_choice == "!exit":
        print("Bye!")
        exit()

    elif user_choice == "!rating":
        print(f"Your rating: {score}")

    elif user_choice not in choice_list:
        print("Invalid input")

    else:
        return user_choice

def play_game(a):

    global score

    if a in choice_list:
        global result

        # coose computer option
        random.seed()
        computer_answer = random.choice(choice_list)

        # find win and lose options
        x = choice_list.index(a)
        result = choice_list[x + 1:]
        result.extend(choice_list[:x])
        n = len(result)
        w = math.ceil(n / 2)

        if computer_answer == a:
            print(f"There is a draw ({computer_answer})")
            score += 50
            for s in scores_list:
                if s[0] == name:
                    s[1] += 50

        elif computer_answer in result[w:]:
            print(f"Well done. Computer chose {computer_answer} and failed")
            score += 100
            for s in scores_list:
                if s[0] == name:
                    s[1] += 100

        elif computer_answer in result[:w]:
            print(f"Sorry, but computer chose {computer_answer}")

    ask_user()

user_choice = ""

while user_choice != "!exit":
    play_game(user_choice)

rating.close()
