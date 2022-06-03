# Rock, paper, scissors

import random

print("Hey there! \nLet's play Rock-Paper-Scissors")

print("'r' stands for rock \n'p' for paper \n's' for scissors")

#define the winning moves
def win_logic(a_move, b_move):
    if a_move == b_move:
        return 'tie'
    elif a_move == 'r' and b_move == 's':
        return 'win'
    elif a_move == 's' and b_move == 'p':
        return 'win'
    elif a_move == 'p' and b_move == 'r':
        return 'win'
    else:
        return 'lose'


def game_play():
    options = ['r', 'p', 's']
    options_names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    while True:
        print("Choose your move 'r', 'p', or 's'?")
        player_move = str(input("what's your move?\n")).lower()
        if player_move not in options:
            print('Please enter a valid move')
            continue
        else:
            cpu_move = random.choice(options)
            print(f'Player ({options_names[player_move]}) : CPU ({options_names[cpu_move]})')
            status = win_logic(player_move, cpu_move)
            if status == 'win':
                print('You win!')
            elif status == 'lose':
                print('Oops, you lose!')
            elif status == 'tie':
                print('It\'s a tie, you get to play again!')
                game_play()
            break

game_play()
