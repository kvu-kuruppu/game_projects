import random

top_range = input('Please enter a number for range: ')

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('Please enter a number larger than zero')
        quit()

else:
    print('Invalid Input - Please enter a "number"')
    quit()

random_number = random.randint(1, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print('Please enter a number larger than zero ')
            continue

    else:
        print('Invalid Input - Please enter a "number" ')
        continue

    if user_guess == random_number:
        print(f'You input {user_guess} & the generated number is {random_number}')
        print('You won')
        break
    else:
        print('You lose')

print(f'Number of times you tried: {guesses}')
