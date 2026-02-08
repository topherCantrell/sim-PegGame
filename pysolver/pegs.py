import json
from pysolver.svg_maker import SVGMaker

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

def save_basics(end_stats):
    """save the basic stats to a file"""
    with open("end_stats.json", "w") as f:
        json.dump(end_stats, f, indent=4)

def load_basics():    
    """load the basic stats from a file"""
    with open("end_stats.json", "r") as f:
        end_stats = json.load(f)
    return end_stats

def save_board_hits(hit_boards):
    """save the board hits to a file"""
    with open("hit_boards.json", "w") as f:
        json.dump(hit_boards, f, indent=4)

def load_board_hits():    
    """load the board hits from a file"""
    with open("hit_boards.json", "r") as f:
        hit_boards = json.load(f)
    return hit_boards

def get_board_number_from_board(board):
    """get the board number (int) from the board state
    Args:
        board: list of 15 ints (0/1) representing the board state
    Returns:
        int: board number
    """
    s = ''
    for v in board:
        s = str(v) + s
    return int(s,2)

def get_board_from_board_number(num):
    """get the board state from the board number (int)
    Args:
        num: int board number
    Returns:
        list of 15 ints (0/1) representing the board state
    """
    s = bin(num)[2:]
    s = s.rjust(15,'0')
    board = [int(c) for c in s[::-1]]
    return board

def get_board_from_visual(s):
    """get the board state from the visual string representation
    Args:
        s: str visual representation of the board
    Returns:
        list of 15 ints (0/1) representing the board state
    """
    s = s.replace('\n','').replace(' ','')
    ret = []
    for c in s:
        if c=='.':
            ret.append(0)
        else:
            ret.append(1)    
    return ret

def has_moves(board):
    """check if there are any valid moves left on the board

    Args:
        board: list of 15 ints (0/1) representing the board state
    Returns:
        True if there are valid moves, False otherwise
    """
    for mv in MOVES:
        if board[mv[0]] == 1 and board[mv[1]] == 1 and board[mv[2]] == 0:
            return True
    return False

def print_boards(boards, filename, labels=None):
    """print multiple boards side by side
    
    Args:
        boards: list of int board numbers
    """
    svg = SVGMaker()
    svg_boards = []
    pos = 0
    for brd in boards:
        board = get_board_from_board_number(brd)
        sbrd = svg.make_board()
        if labels:
            sbrd.set_text(labels[pos])
            pos += 1
        else:
            sbrd.set_text(str(brd))
        for i in range(15):
            if board[i]:
                sbrd.set_peg(f"{i:X}")
            else:
                sbrd.set_peg(f"{i:X}", False)
        svg_boards.append(sbrd)
    svg.make_svg(filename, svg_boards, 0.5)
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
    """get the visual string representation of a board

    Args:
        board: list of 15 ints (0/1) representing the board state
        value: optional int to show as the board number
    Returns:
        str: visual representation of the board
    """
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

def find_move(m):
    for move in MOVES:
        if move[0] == int(m[0], 16) and move[2] == int(m[1], 16):
            return move
    return None

def print_game_play(game, filename=None):
    svg = SVGMaker()
    svg_boards = []
    board = [1]*15
    board[int(game[0], 16)] = 0
    seq = [board[:]]
    moves = []
    game = game[2:]
    game = game.split(':')
    for g in game:
        sbrd = svg.make_board()
        for i in range(15):
            if board[i]:
                sbrd.set_peg(f"{i:X}")
            else:
                sbrd.set_peg(f"{i:X}", False)
        move = find_move(g)
        smove = f"{move[0]:X}{move[1]:X}{move[2]:X}"
        sbrd.set_move(smove)
        sbrd.set_text('')
        moves.append(move)
        board[move[0]] = 0
        board[move[1]] = 0
        board[move[2]] = 1
        seq.append(board[:])
        svg_boards.append(sbrd)
    moves.append(None)  # No move on the last board
    sbrd = svg.make_board()
    sbrd.set_text('')
    for i in range(15):
        if board[i]:
            sbrd.set_peg(f"{i:X}")
        else:
            sbrd.set_peg(f"{i:X}", False)
    svg_boards.append(sbrd)
    print_rows = ["", "", "", "", ""]
    for i in range(len(seq)):
        brd = seq[i]
        mv = moves[i]
        if mv:
            for j in range(15):
                if brd[j]:
                    brd[j] = '+'
                else:
                    brd[j] = '.'
            brd[mv[0]] = hex(mv[0])[2].upper()
            brd[mv[1]] = hex(mv[1])[2].upper()
            brd[mv[2]] = '*'
        else:
            for j in range(15):
                if brd[j]:
                    brd[j] = hex(j)[2].upper()
                else:
                    brd[j] = '.'
        print_rows[0] += "    "+brd[0]+"    |"
        print_rows[1] += "   "+brd[1]+" "+brd[2]+"   |"
        print_rows[2] += "  "+brd[3]+" "+brd[4]+" "+brd[5]+"  |"
        print_rows[3] += " "+brd[6]+" "+brd[7]+" "+brd[8]+" "+brd[9]+" |"
        print_rows[4] += brd[10]+" "+brd[11]+" "+brd[12]+" "+brd[13]+" "+brd[14]+"|"
    for i in range(len(print_rows)):
        print_rows[i] = print_rows[i][:-1]

    svg.make_svg(filename, svg_boards, 0.5)
    print('\n'.join(print_rows))

def _solve_board(board, state):    
    """generate all possible game states from the given game state

    This is a private recursive helper.

    Args:
        board: list of 15 ints (0/1) representing the board state
        state: string representing the moves made so far
    Yields:
        (board, state, is_end): board is the current board state,
            state is the move history, is_end is True if no moves possible
    """
    made_move = False
    for mv in MOVES:
        if board[mv[0]] == 1 and board[mv[1]] == 1 and board[mv[2]] == 0:
            new_board = board[:]
            new_board[mv[0]] = 0
            new_board[mv[1]] = 0
            new_board[mv[2]] = 1           
            mrep = f":{mv[0]:X}{mv[2]:X}"            
            new_state = state + mrep
            made_move = True
            yield from _solve_board(new_board, new_state)
    yield board, state, not made_move

def game_board_generator(start_hole):
    """generate all possible game states from a given starting hole

    Args:
        start_hole: int (0..14) representing the hole to start with empty
    Yields:
        (board, state, is_end): board is the current board state,
            state is the move history, is_end is True if no moves possible
    """
    b = [1]*15
    b[start_hole] = 0        
    state = f"{start_hole:X}"    
    yield from _solve_board(b, state)

if __name__ == '__main__':
    #print_game_play("0:30:53:05:61:92:B4:C5:18:29:E5:5C:DB:AC",'test.svg')
    
    #print_boards([0b0101011001101111], 'test.svg')
    #print_game_play("4:B4:27:D4:72",'test.svg')

    #print_boards([0b0101011001101111,0b0100011001101111], 'test.svg',['Valid','Not Valid'])

    #print_boards([40,4104,4128],'test.svg')

    #print_boards([16383,13542],'onehit.svg')

    # print_boards([17,         384,         576,         4097,        4112,        130],'pegs2.svg')
    print_boards([7,           11,          22,          56,         385,        21504,        3073, 4102,        4136,        7168,       10241,       14336],'pegs3.svg')
    print_boards([960,        10816,       27648,        401],'pegs4.svg')
    print_boards([4497,        346,         391,         598,        12932,       14353],'pegs5.svg')
    print_boards([31745,       31760,       28224,       14736],'pegs6.svg')
    print_boards([32128,       31616,       31750,       27670],'pegs7.svg')
    print_boards([32321,       32336,       31785],'pegs8.svg')
    print_boards([32704,       32360,       32145,       31767],'pegs9.svg')
    print_boards([31806,       31791],'pegs10.svg')
    print_boards([32598,       32185],'pegs11.svg')
    print_boards([32367,       32382,       32190,       28665],'pegs12.svg')
    print_boards([32750,       32727,       28655],'pegs13.svg')