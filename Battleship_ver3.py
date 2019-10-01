import random
from os import system, name

def new_board():
    sea = []
    for x in range(11):
        sea.append(["*"] * 11)
    sea[0][1] = ' A'
    sea[0][2] = 'B'
    sea[0][3] = 'C'
    sea[0][4] = 'D'
    sea[0][5] = 'E'
    sea[0][6] = 'F'
    sea[0][7] = 'G'
    sea[0][8] = 'H'
    sea[0][9] = 'I'
    sea[0][10] = 'J'
    for x in range(1,10):
        sea[x][0] = str(x)+" "
    sea[10][0] = '10'  
    sea[0][0] = " "  
        
    return sea
        
def print_board(board):
    for row in board:
        print(" ".join(row))

def testing_board():
    test_board = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], ['1', '1', 'O', '1', '1', '1', 'O', 'O', 'O', 'O', 'O'], ['2', '1', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['3', '1', 'O', '1', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['4', 'O', 'O', '1', 'O', 'O', 'O', 'O', '1', 'O', 'O'], ['5', '1', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['6', 'O', 'O', '1', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['7', '1', 'O', '1', 'O', 'O', '0', 'O', 'O', 'O', 'O'], ['8', '1', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '1', 'O'], ['9', '1', 'O', '1', 'O', 'O', '1', 'O', 'O', 'O', 'O'], ['T', '1', 'O', '1', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
    return test_board

def input_user_col(user_board):
    sign_tuple = ('A','B','C','D','E','F','G','H')
    converted = False
    cords_int = -1
    print('Czas na oddanie strzału.')
    while not converted:
        cords = input('Podaj kolumne:')   
        if cords.upper() in sign_tuple:
                converted = True
        else:
            print_all(user_board)
        cords_int = sign_tuple.index(cords-1) + 1
    return cords_int

def input_user_row(user_board):
    converted = False
    while not converted:
        cords = input('Podaj wiersz:')
        if (len(cords) == 2 and cords == '10') or (len(cords) == 1 and (cords == '1' or cords == '2' or cords == '3' or cords == '4' or cords == '5' or cords == '6' or cords == '7' or cords == '8' or cords == '9' or cords == 't' or cords == 'T')):
            converted = True
        else:
            print_all(user_board)
    cords_int = int(cords)
    return cords_int

def check_out_cords(cords_col, cords_row, cpu_board, user_board):
    good_shoot = False
    if cpu_board[cords_row][cords_col] == 'T':
        print('Trafienie!!!')
        user_board[cords_row][cords_col] = 'T'
        good_shoot = True
    else:
        print('Pudło!!!')
        user_board[cords_row][cords_col] = '0'
    return good_shoot

def draw_around_ship(cords, board):
    # obrysowywanie statku
    for i in range(0,len(cords), 2):
        board = draw_around_point(cords[i],cords[i+1],board)
    return board    

def draw_around_point(x, y, board):
    # obrysowywanie pojedynczego punktu
    block = "-"
    if can_draw_around_point(x-1, y-1, board):
        board[x-1][y-1] = block
    if can_draw_around_point(x-1, y, board):
        board[x-1][y] = block
    if can_draw_around_point(x-1, y+1, board):
        board[x-1][y+1] = block
    if can_draw_around_point(x, y-1, board):
        board[x][y-1] = block
    if can_draw_around_point(x, y+1, board):
        board[x][y+1] = block
    if can_draw_around_point(x+1, y-1, board):
        board[x+1][y-1] = block
    if can_draw_around_point(x+1, y, board):
        board[x+1][y] = block
    if can_draw_around_point(x+1, y+1, board):
        board[x+1][y+1] = block
    return board

def can_draw_around_point(x, y, board):
    # sprawdzenie czy koordynaty sa wewnat planszy
    if 10 >= x >= 1 and 10 >= y >= 1:
        if board[x][y] == "*":
            return True

def ship_placement():
    cords = []
    ship_cords = []
    board = new_board()
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for i in range(len(ships)):
        cords = coord_of_ship(ships[i], board)
        board = draw_ship_on_board(board, cords)
        board = draw_around_ship(cords, board)
        ship_cords.append(cords)   
    return board, ship_cords

def draw_ship_on_board(board, cords):
    for i in range(0, len(cords), 2):
        board[cords[i]][cords[i+1]] = "T"
    return board

def ship_origin():
    coord_row = random.randint(1,10)
    coord_cols = random.randint(1,10)
    direction = random.randint(1,4)
    return coord_cols, coord_row, direction

def ship_position_check_on_map(cords):
    temp = []
    for i in range(len(cords)):
        if cords[i] <= 10 and cords[i] >= 1:
            temp.append(1)
        else:
            temp.append(0)
    if sum(temp) == len(temp):
        return True
    else:
        return False
    
def coord_of_ship(ship, board):
    converted = False
    while not converted:
        cords_origin = ship_origin()
        cords = []
        if cords_origin[2] == 2:
            for i in range(ship):
                cords.append(cords_origin[1])
                cords.append(cords_origin[0]-(ship-1)+i)
        elif cords_origin[2] == 4:
            for i in range(ship):
                cords.append(cords_origin[1])
                cords.append(cords_origin[0]+i)
        elif cords_origin[2] == 1:
            for i in range(ship):
                cords.append(cords_origin[1]-(ship-1)+i)
                cords.append(cords_origin[0])
        elif cords_origin[2] == 3:
            for i in range(ship):
                cords.append(cords_origin[1]+i)
                cords.append(cords_origin[0])
        if ship_position_check_on_map(cords):
            if ship_position_possible_vs_ship(board, cords):
                converted = True
                return cords
               
def ship_position_possible_vs_ship(board, cords):
    temp = []
    for i in range(0, len(cords), 2):
        if board[cords[i]][cords[i+1]] == "*":
            temp.append(1)
        else:
            temp.append(0)
    if sum(temp) == len(temp):
        return True
    else:
        return False

def check_all_ships(user_board, ship_cords):
    result_board = user_board
    for i in range(len(ship_cords)):
        result_board = check_if_ship_destroyed(user_board, ship_cords[i])
    return result_board        

def check_if_ship_destroyed(board, cords):
    temp = []
    result_board = board
    for i in range(0, len(cords), 2):
        if board[cords[i]][cords[i+1]] == "T":
            temp.append(1)
        else:
            temp.append(0)
    if sum(temp) == len(temp):
        result_board = draw_around_ship_for_user_board(cords,result_board)
        for i in range(0, len(cords), 2):
            board[cords[i]][cords[i+1]] = "X"

    return result_board

def draw_around_ship_for_user_board(cords, board):
    # obrysowywanie statku
    for i in range(0,len(cords), 2):
        board = draw_around_point(cords[i],cords[i+1],board)
    return board 

def user_input(user_board):
    converted = False
    while not converted:
        cords_col = input_user_col(user_board)
        cords_row = input_user_row(user_board)
        if user_board[cords_row][cords_col] == "*":
            converted = True
        else:
            print_all(user_board)
            print('Nie możesz oddać strzału w to miejsce')
    return cords_col, cords_row

def clear():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')

def print_all(user_board):
    clear()
    print('T - trafienie')
    print('X - zniszczony statek')
    print('0 - pudlo')
    print_board(user_board)

def main_game():
    data_from_placement = ship_placement()
    cpu_board = data_from_placement[0]
    coord_of_ship = data_from_placement[1]
    user_board = new_board()
    print_board(user_board)
    
    good_shoots = 0

    while good_shoots < 20:
        print_all(user_board)
        cords_form_user = user_input(user_board)
        cords_col = cords_form_user[0]
        cords_row = cords_form_user[1]
        shoot = check_out_cords(cords_col, cords_row, cpu_board, user_board)
        user_board = check_all_ships(user_board, coord_of_ship)
        print_board(user_board)
        if shoot is True:
            good_shoots += 1
    clear()
    print('Gratulacje :) zniszczyles wszystkie statki przeciwnika')
    
def main():
    main_game()

if __name__ == "__main__":
    main()