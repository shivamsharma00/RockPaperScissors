# This is a game of rock paper scissors with computer.
# It finalize winner on the basis of outcome of three play.

import random
from time import sleep

if __name__ == "__main__":

    rps_dict = {1:'R', 2:'P', 3:'S'}
    rps_val = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}
    user_count = 0
    system_count = 0
    user_w = 'User won !!!'
    system_w = 'System won !!!'

    print('You are going to play opposite to system.')
    print('Press R for Rock, P for Paper and S for Scissor.')
        
    for i in range(1, 4):

        s = ''
        print(f'Round {i}')
        user_in = str(input('GO... ')).upper()
        system_in = rps_dict[random.randint(1,3)]
        
        if user_in == system_in:
            pass
        else:
            if user_in == 'R':
                if system_in == 'P':
                    system_count += 1
                else:
                    user_count += 1
            elif user_in == 'P':
                if system_in == 'R':
                    user_count += 1
                else:
                    system_count += 1
            else:
                if system_in == 'R':
                    system_count += 1
                else:
                    user_count += 1

        s = '-'*25 + '\n' + '|   User  |   System    |' + '\n' + '-'*25 + '\n' + f'|   {rps_val[user_in]}  |   {rps_val[system_in]}  |' + '\n' + '-'*25 + '\n'
        print(s)
    print()
    print(user_w if user_count > system_count else system_w)

        
        
