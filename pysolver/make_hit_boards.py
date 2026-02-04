import pegs

"""make the basic stats and save to file

Stats include:
    - for each starting hole, how many games end with N pegs left (N=1..10)
"""

# def end_of_game(brd, state, end_counts):    
#     count = brd.count(1)    
#     if count not in end_counts:
#         end_counts[count] = 1
#     else:
#         end_counts[count] += 1

HIT_BOARDS = {}

def note_board(board, state, stats):
    s = pegs.get_board_number_from_board(board)
    if s in stats:
        stats[s][0] += 1
    else:
        stats[s] = [1,state]   

def solve_board(board, end_counts, state):    
    note_board(board, state, end_counts)
    # made_move = False
    for mv in pegs.MOVES:
        if board[mv[0]] == 1 and board[mv[1]] == 1 and board[mv[2]] == 0:
            new_board = board[:]
            new_board[mv[0]] = 0
            new_board[mv[1]] = 0
            new_board[mv[2]] = 1           
            mrep = f":{mv[0]:X}{mv[2]:X}"            
            new_state = state + mrep
            solve_board(new_board, end_counts, new_state)
            # made_move = True
    # if not made_move:
    #     end_of_game(board, state, end_counts)

def solve_all_boards():
    end_stats = {}
    for start_hole in range(15):
        print(f"Start hole {start_hole:X}")        
        b = [1]*15
        b[start_hole] = 0        
        s = {}
        state = f"{start_hole:X}"
        # pegs.repr_board(b)
        solve_board(b, s,state)
        end_stats[start_hole] = s
    return end_stats

stats = solve_all_boards()
pegs.save_board_hits(stats)
