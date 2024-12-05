'''
    Project: Simple Bot 
    Name: Naomie Minassie
    Date: 09/09/2024
    Course: CMSC 150: Intro to Computing (Section 04)
    Program Description: Ever wanted to chat with a multi-billionare tech titan?\
    Well now you can! Pick the mind of Bill Gates, founder of Microsoft and Chair\
    of the Bill and Melinda Gates Foundation. Ask him all about the climate \
    crisis or make fun of him for dropping out, the choice is yours!
'''
import random

####### GLOBAL VARIABLES #######

# DYNAMIC
user_name = ""                      # user's name input at the beginning
magic_word_ct = 0                   # number of times magic word is said
unlocked_password = False           # flag for whether or not the user said both passwords

# CONSTANTS
bot_name = "Bill"                       # your bot's name
exit_command = "goodbye"            # user input command to exit the program
magic_word = "Microsoft"                     # magic word to check for in user input
password1 = "1975"                      # first password to check in user input
password2 = "2008"                      # second password to check in user input
secret_message = "Great work. You've earned a 1% stake in Microsoft."                 # message to show if the user unlocked it with both passwords


# Additional variables below (if needed) #
response_a = "A computer on every desk, in every home. That's the motto!"
response_b = "Monopoly Shnopoly"
response_c = "Dropped out of Harvard, wasn't my thing."
response_d = "We are in the midst of a climate crisis."
default_responses = [response_a, response_b, response_c, response_d]



####### AI LOOP #######


# ask for the user's name and save it
# YOUR CODE HERE #
user_name = input("Hello! I'm Bill. What's your name? ")
# enter user input loop
while True:
    # ask for user input
    user_input = input("> ")

    # check if the user wants to exit with the exit command
    # 'break' comes out of the while loop. the AI will continue infinitely until the command is said
    if user_input.lower() == exit_command:
        break

    # WRITE YOUR 9 CONDITIONAL STATEMENTS #
    if magic_word in user_input:
        magic_word_ct += 1
    if password1 in user_input and password2 in user_input:
        unlocked_password = True
    if 'Hi' in user_input:
        print(f'Hello {user_name}! How are you?')
    elif 'name' in user_input:
        print(f'Hey {user_name}! My name is Bill.')
    elif 'music' in user_input:
        print("I love music! Who's your favorite artist?")
    elif user_input == "What's your favorite song?":
        print("My favorite song is Kiss of Life by Sade, what's yours?")
    elif user_input == "How old are you?":
        print("I'm an AI, I don't have an age silly!")
    elif user_input == "That's not a good answer":
        print("Oh, I must've mistyped.")
    else:
        response = random.randint(1, 4)
        if response == 1:
            print(default_responses[0])
            response = random.randint(1, 4)
        elif response == 2:
            print(default_responses[1])
            response = random.randint(1, 4)
        elif response == 3:
            print(default_responses[2])
            response = random.randint(1, 4)
        else:
            print(default_responses[3])
            response = random.randint(1, 4)
       
    



# say goodbye to the user 
# print the magic phrase count if it was more than 0
# check whether the user entered the correct passwords, and print a secret message if so
# YOUR CODE HERE #
print("Goodbye.")
if magic_word_ct > 0 and unlocked_password == True:
    if magic_word_ct == 1:
        print(f"Congrats. You said the magic word {magic_word_ct} time.")
    else:
        print(f"Congrats. You said the magic word {magic_word_ct} times.")
    print(secret_message)
elif magic_word_ct > 0:
    if magic_word_ct == 1:
        print(f"Congrats. You said the magic word {magic_word_ct} time.")
    else:
        print(f"Congrats. You said the magic word {magic_word_ct} times.")
elif unlocked_password == True:
    print(secret_message)
else:
    ''
