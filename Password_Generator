import random


if __name__ == '__main__':

    numbers = '0123456789'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = upper_case.lower()
    symbols = '!@#$%^&*(){}[]?/><.,`~'

    length = int(input('Enter a length of the password: '))

    all_vars = numbers + upper_case + lower_case + symbols

    temp = random.sample(all_vars, length)

    password = ''.join(temp)

    print(f'The password is: {password}')

