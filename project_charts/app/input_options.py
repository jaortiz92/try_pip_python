print_mistake = 'Valor ingresado es incorrecto, intentelo de nuevo\n' + '*' * 70

def get_number(text):
    flag = True
    while flag:
        number = input(text).replace(' ', '')
        if number.isnumeric():
            flag = False
            number = float(number)
        else:
            print(print_mistake)

    return number

def get_text_from_list(text, allowed_values):
    flag = True
    while flag:
        text_input = input(text).replace(' ', '').lower()
        if text_input in allowed_values:
            flag = False
        else:
            print(print_mistake)
    return text_input

def get_text(text):
    flag = True
    while flag:
        text_input = input(text).title().strip()
        if len(text_input) > 3:
            flag = False
        else:
            print(print_mistake)
    return text_input