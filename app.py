from utils import password_generator, collect_details

container = []
status = True

while status:
    details = collect_details()
    password = password_generator(details)
    print(password)
    is_password_okay = input('Do you like the generated password? Yes or No? ')

    while True:
        if is_password_okay.capitalize() == 'Yes':
            details.append(password)
            container.append(details)
            break
        else:
            user_password = input('Enter a password longer than or equal to 7 characters: ')
            password_length = 7
            while len(user_password) < password_length:
                print('Your password is less than 7')
                user_password = input('Enter password greater than or equal to 7: ')
            else:
                details.append(user_password)
                container.append(details)
            break

    new_user = input('Would you like to enter a new user? Yes or No? ')
    if new_user.capitalize() == 'No':
        status = False
        for item in container:
            print(item)
    else:
        status = True
