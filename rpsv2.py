""" rock vs water---> water  wins coz high psi
    rock vs fire ---> fire  wins coz lava
    paper vs water--> water  wins coz spill water on your book
    paper vs fire---> fire  wins coz ashes
    scissor vs water->water  wins coz rust
    scissor vs fire-> fire wins coz molten iron """

import random

# using a nested dict
result = {
    "rock": {"rock": "draw", "paper": "You WIN!", "scissor": "You LOSE!", "fire": "You WIN!", "water": "You WIN!"},
    "paper": {"rock": "You LOSE!", "paper": "draw", "scissor": "You WIN!", "fire": "You WIN!", "water": "You WIN!"},
    "scissor": {"rock": "You WIN!", "paper": "You LOSE!", "scissor": "draw", "fire": "You WIN!", "water": "You WIN!"},
    "water": {"rock": "computer You LOSE!", "paper": "You LOSE!", "scissor": "You LOSE!", "fire": "You LOSE!", "water": "draw"},
    "fire": {"rock": "You LOSE!", "paper": "You LOSE!", "scissor": "You LOSE!", "fire": "draw", "water": "You WIN!"},

}

user_input = input('What do you pick-->  ')
user_input2 = user_input.lower()

# list to open the dictionary
result_items = list(result.items())

# variable to store a randomly selected
comp_choice = random.choice(result_items)

# key and value variables to store the respective choices from the dict
random_key, random_value = comp_choice

# to make sure user enters a relevant option
options = ["rock", "paper", "scissor", "fire", "water"]

if user_input2 in options:
    print('The computer chose--->', random_key)
else:
    print('Wrong Input, Try Again')

# conditionals to get the outcome of the game
# idk how to better optimize it by not repeating code

if user_input2 == "rock":
    if random_key == "rock":
        x = random_value.get("rock")
        print(x)
    elif random_key == "paper":
        y = random_value.get("rock")
        print(y)
    elif random_key == "scissor":
        z = random_value.get("rock")
        print(z)
    elif random_key == "fire":
        c = random_value.get("rock")
        print(c)
    elif random_key == "water":
        v = random_value.get("rock")
        print(v)

if user_input2 == "paper":
    if random_key == "rock":
        x = random_value.get("paper")
        print(x)
    elif random_key == "paper":
        y = random_value.get("paper")
        print(y)
    elif random_key == "scissor":
        z = random_value.get("paper")
        print(z)
    elif random_key == "fire":
        c = random_value.get("paper")
        print(c)
    elif random_key == "water":
        v = random_value.get("paper")
        print(v)

if user_input2 == "scissor":
    if random_key == "rock":
        x = random_value.get("scissor")
        print(x)
    elif random_key == "paper":
        y = random_value.get("scissor")
        print(y)
    elif random_key == "scissor":
        z = random_value.get("scissor")
        print(z)
    elif random_key == "fire":
        c = random_value.get("scissor")
        print(c)
    elif random_key == "water":
        v = random_value.get("scissor")
        print(v)

if user_input2 == "fire":
    if random_key == "rock":
        x = random_value.get("fire")
        print(x)
    elif random_key == "paper":
        y = random_value.get("fire")
        print(y)
    elif random_key == "scissor":
        z = random_value.get("fire")
        print(z)
    elif random_key == "fire":
        c = random_value.get("fire")
        print(c)
    elif random_key == "water":
        v = random_value.get("fire")
        print(v)

if user_input2 == "water":
    if random_key == "rock":
        x = random_value.get("water")
        print(x)
    elif random_key == "paper":
        y = random_value.get("water")
        print(y)
    elif random_key == "scissor":
        z = random_value.get("water")
        print(z)
    elif random_key == "fire":
        c = random_value.get("water")
        print(c)
    elif random_key == "water":
        v = random_value.get("water")
        print(v)

print('Thank you for the playing RPSv2')
