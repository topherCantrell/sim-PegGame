import json
import random

#    Hex
#     0
#    1 2
#   3 4 5
#  6 7 8 9
# A B C D E

# 36 possible moves (when the pegs are right)
MOVES = [
    [0, 1, 3], [0, 2, 5], 
    [1, 4, 8], [1, 3, 6], 
    [2, 4, 7], [2, 5, 9], 
    [3, 1, 0], [3, 4, 5], [3, 7, 12], [3, 6, 10], 
    [4, 8, 13], [4, 7, 11], 
    [5, 2, 0], [5, 4, 3], [5, 8, 12], [5, 9, 14], 
    [6, 3, 1], [6, 7, 8], 
    [7, 4, 2], [7, 8, 9], 
    [8, 7, 6], [8, 4, 1], 
    [9, 5, 2], [9, 8, 7], 
    [10, 6, 3], [10, 11, 12], 
    [11, 7, 4], [11, 12, 13], 
    [12, 11, 10], [12, 7, 3], [12, 8, 5], [12, 13, 14], 
    [13, 12, 11], [13, 8, 4], 
    [14, 13, 12], [14, 9, 5]
]

def get_board_number_from_board(board):
    s = ''
    for v in board:
        s = str(v) + s
    return int(s,2)

def get_board_from_board_number(num):
    s = bin(num)[2:]
    s = s.rjust(15,'0')
    board = [int(c) for c in s[::-1]]
    return board

def get_board_from_visual(s):
    s = s.replace('\n','').replace(' ','')
    ret = []
    for c in s:
        if c=='.':
            ret.append(0)
        else:
            ret.append(1)    
    return ret

def print_boards(boards):
    while boards:
        to_run = boards[:7]
        bds = []
        for board in to_run:
            b = get_board_from_board_number(board)
            bds.append(repr_board(b).split('\n'))
        r = ''
        for i in range(6):
            for bd in bds:
                r += bd[i] + '   '
            r += '\n'
        print(r)
        boards = boards[7:]

def repr_board(board,value=None):
    v = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E']
    for i in range(15):
        if board[i]==0:
            v[i]='.'    
    g = "    "+v[0]+"    \n"
    g+="   "+v[1]+" "+v[2]+"   \n"
    g+="  "+v[3]+" "+v[4]+" "+v[5]+"  \n"
    g+=" "+v[6]+" "+v[7]+" "+v[8]+" "+v[9]+" \n"
    g+=v[10]+" "+v[11]+" "+v[12]+" "+v[13]+" "+v[14]+"\n"
    if value is not None:
        bn = (str(value))
    else:
        bn = str(get_board_number_from_board(board))
    while len(bn)<9:
        bn=' '+bn+' '
    g+=bn[:9]    
    return g


def save_basics(end_stats):
    with open("end_stats.json", "w") as f:
        json.dump(end_stats, f, indent=4)

def load_basics():    
    with open("end_stats.json", "r") as f:
        end_stats = json.load(f)
    return end_stats

def save_board_hits(hit_boards):
    with open("hit_boards.json", "w") as f:
        json.dump(hit_boards, f, indent=4)

def load_board_hits():    
    with open("hit_boards.json", "r") as f:
        hit_boards = json.load(f)
    return hit_boards

def board_to_game_number(board):
    s = ''
    for v in board:
        s = str(v) + s
    return int(s,2)

def has_moves(board):
    for mv in MOVES:
        if board[mv[0]] == 1 and board[mv[1]] == 1 and board[mv[2]] == 0:
            return True
    return False

if __name__ == "__main__":
    brd = """
      X
     . .
    . . .
   . . . .
  X . . . X
"""
    board = get_board_from_visual(brd)
    print(board)
    print_board(board)
    print("Board number:", board_to_game_number(board))
    
    b = get_board_from_board_number(1024)
    print_board(b)

    