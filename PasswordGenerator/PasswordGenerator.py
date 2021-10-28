import secrets
import string

def show_menu():
    print('\n1. With digits\n2. Without digits\n')

show_menu()

def generate_password(lenght):
    symbols = string.ascii_letters + string.digits
    rand_pass = ''.join(secrets.choice(symbols) for i in range (lenght))
    print("\n\nYour password: " + str(rand_pass) + "\n\n")
    print('Enter password lenght\n')

def generate_password_without_digits(lenght):
    symbols = string.ascii_letters
    rand_pass = ''.join(secrets.choice(symbols) for i in range (lenght))
    print("\n\nYour password: " + str(rand_pass) + "\n\n")
    print('Enter password lenght\n')

while True:
    menu_input=input()
    if menu_input=='1':
        print('\nEnter password lenght\n')
        lenght_input = input()
        while lenght_input!='Menu' and lenght_input!='menu':
            lenght_input = int(lenght_input)
            generate_password(lenght_input)
            lenght_input = input()
        else:
            show_menu()

    if menu_input=='2':
        print('\nEnter password lenght\n')
        lenght_input = input()
        while lenght_input!='Menu' and lenght_input!='menu':
            lenght_input = int(lenght_input)
            generate_password_without_digits(lenght_input)
            lenght_input = input()
        else:
            show_menu()