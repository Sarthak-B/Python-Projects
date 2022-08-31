import main

while True:
    print(
        '\nWelcome to Tic Tac Toe Mania \nPlz select one from the following options \n1. ONE V ONE \n2. ONE V NONE \n3. Exit \nnote: O will always play first')
    try:
        res = int(input('selection: '))
    except ValueError:
        print('plz give an integer b/w 1~3')
        continue
    if not (1 <= res <= 3):
        print('not in range')
        continue
    if res == 1:
        main.oneVone()
    elif res == 2:
        while True:
            rev = input('plz confirm the mode: 1. you as first or 2. computer as first 3. go back: ')
            if rev == '1':
                main.oneVnone()
            elif rev == '2':
                main.oneVnone(rev=True)
            elif rev == '3':
                print('returning back')
                break
            else:
                print('incorrect input')
                continue
    elif res == 3:
        print('See you soon, exiting...')
        break
