import random


# Output Board
def draw(a, b, c, d, e, f, g, h, i):
    x = ('\n ___ ___ ___')
    y = ('\n| {0} | {1} | {2} |')
    print(x, y.format(a, b, c), x, y.format(d, e, f), x, y.format(g, h, i), x)


# Convention
cv = {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}


# Winner decider
def winner(in_b, sym):
    a, b, c, d, e, f, g, h, i = in_b[0], in_b[1], in_b[2], in_b[3], in_b[4], in_b[5], in_b[6], in_b[7], in_b[8]
    pairs = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]
    for comb in pairs:
        if comb[0] == comb[1] == comb[2] == sym:
            return f'\n>>>>>>{sym} wins<<<<<<'
    if ' ' not in in_b:
        return '>>>>>>>draw<<<<<<< good job everyone'
    else:
        return 'you can do this!'


# Input verifier for both player and computer
def input_checker(in_b, sym, diff_in_b=None, choice=None):
    while True:
        try:
            if choice or choice == 0:  # for computer
                in_b[choice] = diff_in_b[choice] = sym
                break
            else:
                play = int(input(f'sq {sym} : '))
            if (0 < play < 10) and in_b[cv[play]] == ' ':  # for player
                in_b[cv[play]] = sym
                if diff_in_b:
                    diff_in_b[cv[play]] = sym
                break
            else:
                print('invalid move')
                continue
        except:
            print('invalid input')


def oneVone():
    x, o, _ = 'X', 'O', ' '
    in_b = [_, _, _,  # inner board
            _, _, _,
            _, _, _]
    print('lets begin')
    draw(*in_b)  # list unpacking
    while winner(in_b, x) == 'you can do this!':  # checking win for X and using it as a Statement
        input_checker(in_b, o)
        print(winner(in_b, o))
        if winner(in_b, o) == 'you can do this!':  # checking win for O
            draw(*in_b)
        else:
            draw(*in_b)
            break

        input_checker(in_b, x)
        draw(*in_b)
        print(winner(in_b, x))


# Algo for computer to play
def choice(in_b, sym_w, sym_l): # here in_b is used for different inner board
    x, o, _ = 'X', 'O', ' '
    # a,b,c for simplicity
    a, b, c, d, e, f, g, h, i = in_b[0], in_b[1], in_b[2], in_b[3], in_b[4], in_b[5], in_b[6], in_b[7], in_b[8]
    pairs = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]

    for comb in pairs:
        if comb[0] == comb[2] == sym_w and not (bool(comb[1].strip())):
            return in_b.index(comb[1])
        elif comb[0] == comb[1] == sym_w and not (bool(comb[2].strip())):
            return in_b.index(comb[2])
        elif comb[1] == comb[2] == sym_w and not (bool(comb[0].strip())):
            return in_b.index(comb[0])

    for comb in pairs:
        if comb[0] == comb[2] == sym_l and not (bool(comb[1].strip())):
            return in_b.index(comb[1])
        elif comb[0] == comb[1] == sym_l and not (bool(comb[2].strip())):
            return in_b.index(comb[2])
        elif comb[1] == comb[2] == sym_l and not (bool(comb[0].strip())):
            return in_b.index(comb[0])

    for comb in random.sample(pairs, len(pairs)):
        if not (bool(comb[0].strip())) and not (bool(comb[1].strip())) and comb[2] == sym_w:
            return random.choice([in_b.index(comb[0]), in_b.index(comb[1])])
        elif not (bool(comb[1].strip())) and not (bool(comb[2].strip())) and comb[0] == sym_w:
            return random.choice([in_b.index(comb[1]), in_b.index(comb[2])])
        elif not (bool(comb[0].strip())) and not (bool(comb[2].strip())) and comb[1] == sym_w:
            return random.choice([in_b.index(comb[0]), in_b.index(comb[2])])

    indexes = [i for i in range(len(in_b)) if not (bool(in_b[i].strip()))]
    return random.choice(indexes)


def oneVnone(rev=False):
    x, o, _ = 'X', 'O', ' '
    in_b = [_, _, _,
            _, _, _,
            _, _, _]
    # different inner board for computer
    diff_in_b = [' ', '  ', '   ',
                 '    ', '     ', '      ',
                 '       ', '        ', '         ']

    print('lets begin')
    if not (rev):  # for computer to be first
        draw(*in_b)
    while winner(in_b, x) == 'you can do this!':
        if rev:  # player 1 as computer
            input_checker(in_b, o, diff_in_b, choice(diff_in_b, o, x))
            print(winner(in_b, o))
            if winner(in_b, o) == 'you can do this!':
                draw(*in_b)
            else:
                draw(*in_b)
                break
            input_checker(in_b, x, diff_in_b)
            print(winner(in_b, x))
            draw(*in_b)
        else:  # player 2 as computer
            input_checker(in_b, o, diff_in_b)
            print(winner(in_b, o))
            if winner(in_b, o) == 'you can do this!':
                draw(*in_b)
            else:
                draw(*in_b)
                break
            input_checker(in_b, x, diff_in_b, choice(diff_in_b, x, o))
            draw(*in_b)
            print(winner(in_b, x))
