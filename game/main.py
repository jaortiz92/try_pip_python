import random

OPTIONS = ('r', 'rock', 'p', 'paper', 's', 'scissors')

OPTIONS_DICT = {
    OPTIONS[1]: OPTIONS[0],
    OPTIONS[3]: OPTIONS[2],
    OPTIONS[5]: OPTIONS[4],
}

LIST_KEYS_OPTIONS = list(OPTIONS_DICT.keys())
LIST_VALUES_OPTIONS = list(OPTIONS_DICT.values())

def print_status(rounds, victories_computer, victories_user):
    print('*' * 40)
    print('ROUND', rounds)
    print('*' * 40)
    print('Victories computer:', victories_computer)
    print('Victories user:', victories_user)

def print_results(user_option, computer_option, winner):
    user_option = LIST_KEYS_OPTIONS[LIST_VALUES_OPTIONS.index(user_option)]
    computer_option = LIST_KEYS_OPTIONS[LIST_VALUES_OPTIONS.index(computer_option)]
    print('User option =>', user_option.capitalize())
    print('Computer option =>', computer_option.capitalize())
    if winner != 'Draw':
        print(f'The player {winner} Wins')
    else:
        print(f'Draw')

    print('_' * 40)

def print_final(winner):
    print(f'The winner is the {winner}!!!')
    if winner == 'User':
        print('Congratulations!!!')
    else:
        print('Try again!!!')

def standardize_parameter(option):
    if option in LIST_KEYS_OPTIONS:
        option = OPTIONS_DICT[option]
    return option

def input_user():
    flag = True
    while flag:
        user_option = input('Rock (R), Paper (P) o Scissors (S) => ')
        user_option = user_option.lower()
        if user_option in OPTIONS:
            flag = False
        else: 
            print(f'The option "{user_option}" is not right')
    user_option = standardize_parameter(user_option)
    return user_option

def input_computer():
    computer_option = random.choice(OPTIONS)
    computer_option = standardize_parameter(computer_option)
    return computer_option

def choose_options():
    return input_user(), input_computer()

def processes_round(user_option, computer_option):
    if user_option == computer_option:
        result = 0
    elif user_option in OPTIONS[0]:
        if computer_option in OPTIONS[2]:
            result = -1
        else:
            result = 1
    elif user_option in OPTIONS[2]:
        if computer_option in OPTIONS[0]:
            result = 1
        else:
            result = -1
    else:
        if computer_option in OPTIONS[0]:
            result = -1
        else:
            result = 1
    return result

def game(max_victories):
    victories_computer = 0
    victories_user = 0
    rounds = 1

    while victories_computer < max_victories and victories_user < max_victories:
        print_status(rounds, victories_computer, victories_user)
        user_option, computer_option = choose_options()
        result = processes_round(user_option, computer_option)
        if result == 1:
            victories_user += 1
            winner = 'User'
        elif result == -1:
            victories_computer += 1
            winner = 'Computer'
        else:
            winner = 'Draw'
        rounds += 1
        print_results(user_option, computer_option, winner)
    
    print_final(winner)
        

def run():
    game(2)


if __name__ == '__main__':
    run()