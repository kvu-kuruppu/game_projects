import random

user_win = 0
pc_win = 0

print('--- Rock Paper Scissor ---\n')
print('Instructions')
print('\tType "r" for rock')
print('\tType "p" for paper')
print('\tType "s" for scissor')
print('\tType "q" for quit\n')

while True:
    user_input = input('What\'s your choice: ').lower()
    if user_input == 'q':
        break

    if user_input not in ['r', 'p', 's']:
        print('Invalid input. Please read the instructions')
        continue

    pc_input = random.choice(['r', 'p', 's'])

    print(f'PC input {pc_input}')

    if user_input == 'r' and pc_input == 's':
        print('You Won')
        user_win += 1
    elif user_input == 'p' and pc_input == 'r':
        print('You Won')
        user_win += 1
    elif user_input == 's' and pc_input == 'p':
        print('You Won')
        user_win += 1
    elif user_input == pc_input:
        print('Tie')
    else:
        print('You lost')
        pc_win += 1

print(f'Number of times user won: {user_win}\nNumber of times pc won: {pc_win}')