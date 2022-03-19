print('TIC TAC TOE')
print('player 1 symbol = X')
print('player 2 symbol = O\n\n')
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show():
    game = f' {l[0]} | {l[1]} | {l[2]} \n' \
           f'-----------\n' \
           f' {l[3]} | {l[4]} | {l[5]} \n' \
           f'-----------\n' \
           f' {l[6]} | {l[7]} | {l[8]} \n'
    print(game)


show()
p1 = True
n1 = n2 = []
for i in range(9):
    try:
        if p1:
            n = int(input('Player 1 select number: ')) - 1
            if n in n2:
                print('\nNumber {n+1} box already filled by player 2')
            else:
                n1.append(n)
                l[n] = 'X'
                show()
                p1 = False
        else:
            n = int(input('Player 2 select number: ')) - 1
            if n in n1:
                print('\nNumber {n+1} box already filled by player 1')
            else:
                n2.append(n)
                l[n] = 'O'
                show()
                p1 = True
    except ValueError:
        print("\nYou have not typed anything")
    except IndexError:
        print('\nNumber must be between 1 and 9')

    if l[0] == l[1] == l[2] or l[3] == l[4] == l[5] or l[6] == l[7] == l[8] or \
        l[0] == l[3] == l[6] or l[1] == l[4] == l[7] or l[2] == l[5] == l[8] or \
        l[0] == l[4] == l[8] or l[2] == l[4] == l[6]:
        if p1:
            print('Player 2(0) won')
        else:
            print('Player 1(X) won')
        break
    elif i == 8:
        print('Match Draw')

