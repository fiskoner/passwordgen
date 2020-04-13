import random
import re
import string

# letters = string.ascii_letters
# numbers = '0123456789'


def main():
    password_length = asking_password_length()
    print('Password length = ' + password_length)
    password_amount_of_numbers = asking_amount_of_numbers(password_length)
    print('Amount of numbers = ' + password_amount_of_numbers)
    password = generating_password(password_length, password_amount_of_numbers)
    print(password)


def asking_password_length():
    print('How many symbols do you want (6-16)?')
    password_length_pattern = re.compile("([6-9]|1[0-6])")

    running = True
    while running:
        password_length_try = input()
        if password_length_pattern.match(password_length_try):
            password_length = password_length_try
            break
        elif int(password_length_try) > 16:
            print('Enter smaller length')
        else:
            print('Choose length correctly, try again')
    return password_length


def asking_amount_of_numbers(password_length):
    print('How many numbers do you want? Another characters will be random generated letters')
    password_amount_of_numbers_pattern = re.compile("([0-9]|1[0-6])")

    running = True
    while running:
        password_amount_of_numbers_try = input()
        if password_amount_of_numbers_pattern.match(password_amount_of_numbers_try):
            if(int(password_amount_of_numbers_try) < 0):
                print('Chosen amount of number is smaller than 0. Type bigger amount!')
            elif(int(password_amount_of_numbers_try) > int(password_length)):
                print('Chosen amount of number is bigger than password length. Type smaller amount!')
            else:
                password_amount_of_numbers = password_amount_of_numbers_try
                break
        else:
            print('Enter correct length')
    return password_amount_of_numbers


def generating_password(password_length, amount_of_numbers):
    # if int(amount_of_numbers) > (int(password_length) - int(amount_of_numbers)):
    #     selected_char = random.randrange(0, int(password_length))
    if (int(password_length) - int(amount_of_numbers)) >= int(amount_of_numbers):
        result = ''.join(random.choices(string.digits, k=int(password_length)))
        listresult = list(result)
        i = 0
        # for i in range(0, int(amount_of_numbers)):
        while i < int(int(password_length) - int(amount_of_numbers)):
            random_char = random.randrange(0, int(password_length))
            if result[random_char].isdigit():
                listresult[int(random_char)] = random.choice(string.ascii_letters)
                result = ''.join(listresult)
                i += 1
        return result
    else:
        result = ''.join(random.choices(string.ascii_letters, k=int(password_length)))
        listresult = list(result)
        i = 0
        # for i in range(0, int(amount_of_numbers)):
        while i < int(amount_of_numbers):
            random_char = random.randrange(0, int(password_length))
            if not (result[random_char].isdigit()):
                listresult[int(random_char)] = random.choice(string.digits)
                result = ''.join(listresult)
                i += 1
        return result


main()
