def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('pass.txt','a') as f:
        f.write(f"{name} | {pwd}\n")

def view():
    with open('pass.txt','r') as f:
        for line in f.readlines():
            print(line.rstrip())


master_pwd = input('Enter your master password: ')
if master_pwd == 'Saad':
        print('Welcome back!')
else:
    break_2 = False
    attempts = 0
    for i in range(attempts, 3):
        user_input = input(f'Attempt {attempts + 1} done. Enter your master password again: ')
        if user_input == 'Saad':
            print('Welcome back!')
            break_2 = True
            if break_2 == True:
                break
        else:
            print('Incorrect password. Try again.')
            attempts += 1
    else:
        print('Too many failed attempts.')
        quit()


while True:
    mode = input('Choose mode: (1) Quit, (2) Add password, (3) View passwords: ').lower()
    if mode == '1' or mode == 'quit':
        break
    if mode == '2' or mode == 'add':
        add()
    elif mode == '3' or mode == 'view':
        view()
    else:
        print('Invalid mode.')