import random

# using a nested dict
result = {
    "rock": {"rock": "draw", "paper": "You WIN!", "scissor": "You LOSE!", "fire": "You WIN!", "water": "You WIN!"},
    "paper": {"rock": "You LOSE!", "paper": "draw", "scissor": "You WIN!", "fire": "You WIN!", "water": "You WIN!"},
    "scissor": {"rock": "You WIN!", "paper": "You LOSE!", "scissor": "draw", "fire": "You WIN!", "water": "You WIN!"},
    "water": {"rock": "You LOSE!", "paper": "You LOSE!", "scissor": "You LOSE!", "fire": "You LOSE!", "water": "draw"},
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


if user_input2 in options:
    outcome = random_value.get(user_input2)
    print(outcome)

print('Thank you for the playing RPSv2!')
