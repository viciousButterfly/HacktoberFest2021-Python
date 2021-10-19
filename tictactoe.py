grid=[]
for val in range(9):
    grid.append("-".strip())
player_playing='X'
game=True
winner=None

def show_grid():
    print()
    print(grid[0],'|',grid[1],'|',grid[2],'       ','1 | 2 | 3')
    print('--+---+--','       ','--+---+--')
    print(grid[3],'|',grid[4],'|',grid[5],'       ','4 | 5 | 6')
    print('--+---+--','       ','--+---+--')
    print(grid[6],'|',grid[7],'|',grid[8],'       ','7 | 8 | 9')
    print()

def user(player):
    print(player+'\'s Turn')
    user_input=input(f"Enter Position for {player}:")
    active=False
    while not active:
        while user_input not in ['1','2','3','4','5','6','7','8','9']:
            print('Invalid Input')
            user_input=input("Choose a position from 1-9: ")
        user_input=int(user_input)-1
        if grid[user_input]=='-':
            active=True
        else:
            print('You Cannot go There')
    grid[user_input] = player
    show_grid()

def check():
    win_check()
    tie_check()

def win_check():
    global winner
    rw=row_win()
    cw=col_win()
    dw=diag_win()
    if rw:
        winner=rw
    elif cw:
        winner=cw
    elif dw:
        winner=dw

def row_win():
    global game
    row_1=grid[0]==grid[1]==grid[2]!="-"
    row_2=grid[3]==grid[4]==grid[5]!="-"
    row_3=grid[6]==grid[7]==grid[8]!="-"
    if row_1 or row_2 or row_3:
        game=False
    if row_1:
        return grid[0]
    elif row_2:
        return grid[3]
    elif row_3:
        return grid[6]
    else:
        return None

def col_win():
    global game
    col_1=grid[0]==grid[3]==grid[6]!="-"
    col_2=grid[1]==grid[4]==grid[7]!="-"
    col_3=grid[2]==grid[5]==grid[8]!="-"
    if col_1 or col_2 or col_3:
        game=False
    if col_1:
        return grid[0]
    elif col_2:
        return grid[1]
    elif col_3:
        return grid[2]
    else:
        return None

def diag_win():
    global game
    diag_1=grid[0]==grid[4]==grid[8]!="-"
    diag_2=grid[2]==grid[4]==grid[6]!="-"
    if diag_1 or diag_2:
        game=False
    if diag_1:
        return grid[0]
    elif diag_2:
        return grid[2]
    else:
        return None

def tie_check():
    global game
    if '-' not in grid:
        game=False

def swap():
    global player_playing
    if player_playing=='X':
        player_playing='O'
    elif player_playing=='O':
        player_playing="X"

def play_ttt():
    show_grid()
    while game:
        user(player_playing)
        check()
        swap()
    if winner=='X':
        print('\'X\' wins this game of Tic-Tac-Toe')
    elif winner=='O':
        print('\'O\' wins this game of Tic-Tac-Toe')
    elif winner==None:
        print('It\'s a Tie')

if __name__ == '__main__':
    play_ttt()