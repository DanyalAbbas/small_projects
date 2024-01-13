theboard = {1 : '', 2 : '', 3 : '',
            4 : '', 5 : '', 6 : '',
            7 : '', 8 : '', 9 : '' }
board = f'  {theboard[1]}  |  {theboard[2]}  |  {theboard[3]}\n-----------------\n  {theboard[4]}  |  {theboard[5]}  |  {theboard[6]}\n-----------------\n  {theboard[7]}  |  {theboard[8]}  |  {theboard[9]}'
print(board)
while True:
    player_one = input("\nPlayer one!\n Please mark your place : ")
    player_one = int(player_one)
    for i in theboard:
        if player_one == i:
            if theboard[player_one] == '':
                theboard[i] = 'X'
            else:
                player_one = int(input('This place is already taken : '))
                continue
    board = f'  {theboard[1]}  |  {theboard[2]}  |  {theboard[3]}\n-----------------\n  {theboard[4]}  |  {theboard[5]}  |  {theboard[6]}\n-----------------\n  {theboard[7]}  |  {theboard[8]}  |  {theboard[9]}'
    print(board)
    if theboard[1] == 'X' and theboard[2] == 'X' and theboard[3] == 'X':
        print('\nPlayer one has won')
        break
    elif theboard[4] == 'X' and theboard[5] == 'X' and theboard[6] == 'X':
        print('\nPlayer one has won')
        break
    elif theboard[7] == 'X' and theboard[8] == 'X' and theboard[9] == 'X':
        print('\nPlayer one has won')
        break
    elif theboard[1] == 'X' and theboard[4] == 'X' and theboard[7] == 'X':
        print('\nPlayer one has won')
        break
    elif theboard[2] == 'X' and theboard[5] == 'X' and theboard[8] == 'X':
        print('\nPlayer one has won')
        break
    elif theboard[3] == 'X' and theboard[6] == 'X' and theboard[9] == 'X':
        print('\nPlayer one has won')
        break
    elif theboard[1] == 'X' and theboard[5] == 'X' and theboard[9] == 'X':
        print('Player one has won')
        break
    elif theboard[3] == 'X' and theboard[5] == 'X' and theboard[7] == 'X':
        print('\nPlayer one has won')
        break
    else:
        drawer = []
        for i in theboard:
            if theboard[i] == '':
                drawer.append(False)
            else:
                drawer.append(True)
        if all(drawer):
            print ('\nDraw!')
            break
    player_two = input("\nPlayer two!\n Please mark your place : ")
    player_two = int(player_two)
    for i in theboard:
        if player_two == i:
            if theboard[player_two] == '':
                theboard[i] = 'O'
            else:
                player_two = int(input('This place is already taken : '))
                continue
    board = f'  {theboard[1]}  |  {theboard[2]}  |  {theboard[3]}\n-----------------\n  {theboard[4]}  |  {theboard[5]}  |  {theboard[6]}\n-----------------\n  {theboard[7]}  |  {theboard[8]}  |  {theboard[9]}'
    print(board)
    if theboard[1] == 'O' and theboard[2] == 'O' and theboard[3] == 'O':
        print('\nPlayer two has won')
        break
    elif theboard[4] == 'O' and theboard[5] == 'O' and theboard[6] == 'O':
        print('\nPlayer two has won')
        break
    elif theboard[7] == 'O' and theboard[8] == 'O' and theboard[9] == 'O':
        print('\nPlayer two has won')
        break
    elif theboard[1] == 'O' and theboard[4] == 'O' and theboard[7] == 'O':
        print('\nPlayer two has won')
        break
    elif theboard[2] == 'O' and theboard[5] == 'O' and theboard[8] == 'O':
        print('\nPlayer two has won')
        break
    elif theboard[3] == 'O' and theboard[6] == 'O' and theboard[9] == 'O':
        print('\nPlayer two has won')
        break
    elif theboard[1] == 'O' and theboard[5] == 'O' and theboard[9] == 'O':
        print('Player two has won')
        break
    elif theboard[3] == 'O' and theboard[5] == 'O' and theboard[7] == 'O':
        print('\nPlayer two has won')
        break
    else:
        drawer = []
        for i in theboard:
            if theboard[i] == '':
                drawer.append(False)
            else:
                drawer.append(True)
        if all(drawer):
            print ('\nDraw!')
            break
    continue