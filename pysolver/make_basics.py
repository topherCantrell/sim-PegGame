import pegs
import datetime

"""make the basic stats and save them to afile

Stats include:
    - for each starting hole, how many games end with N pegs left (N=1..10)
    - an example game for each N pegs left
"""

def solve_all_boards():
    total = 0
    before = datetime.datetime.now()
    ret = {}
    for start_hole in range(15):
        print(f"Start hole {start_hole:X}")
        end_stats = {}
        for board, state, end in pegs.game_board_generator(start_hole):
            total += 1
            if end:
                count = board.count(1)    
                if count not in end_stats:
                    end_stats[count] = [1, state]
                else:
                    end_stats[count][0] += 1
        ret[start_hole] = end_stats 
    after = datetime.datetime.now()
    print(f"Solved all boards in {after-before}")   
    print("Total states",total)
    return ret

stats = solve_all_boards()
pegs.save_basics(stats)


