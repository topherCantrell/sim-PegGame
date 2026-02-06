import pegs

hit_boards = pegs.load_board_hits()

def print_board_totals():
    print("Overall Board Hit Totals:")
    totals = {}
    for start_hole in range(15):
        boards_for_start = hit_boards.get(str(start_hole))
        for board_num, (count, state) in boards_for_start.items():
            bn = int(board_num)
            if bn not in totals:
                totals[bn] = count
            else:
                totals[bn] += count

    flat = []
    for board_num, total_count in totals.items():
        flat.append( (board_num, total_count) )        

    flat.sort(key=lambda x: x[1], reverse=True)
    for i in range(20):
        board_num, total_count = flat[i]
        print(f'Board {board_num} hit {total_count} times.')   
    print("...")
    for i in range(20):
        board_num, total_count = flat[-(i+1)]
        print(f'Board {board_num} hit {total_count} times.')

def print_per_start_hole_stats():
    print("Per Start Hole Board Hit Stats:")
    for start_hole in range(15):
        boards_for_start = hit_boards.get(str(start_hole))
        print(f"Start hole {start_hole:X}: {len(boards_for_start)} boards hit.")        

def print_stats_for_board(board_num):
    """print stats for a specific board number"""
    total_hits = 0
    example_state = None
    for start_hole in range(15):
        boards_for_start = hit_boards.get(str(start_hole))
        if str(board_num) in boards_for_start:
            count, state = boards_for_start[str(board_num)]
            total_hits += count
            example_state = state
    print(f"Board {board_num} hit {total_hits} times. Example game: {example_state}")
    db = pegs.get_board_from_board_number(int(board_num))    
    r = pegs.repr_board(db)
    print(r)

def find_all_rem_10_games():
    """find all games that hit a specific board number"""
    print("Finding all games that end with 10 pegs remaining:")
    for start_hole in range(15):
        print(f"Start hole {start_hole:X}")
        for board, state, is_end in pegs.game_board_generator(start_hole):
            if not is_end:
                continue
            if board.count(1) != 10:
                continue
            print(f"  Rem-10 game: {state}")

print_per_start_hole_stats()
print()
print_board_totals()
print()

#find_all_rem_10_games()
print("Example winning play")
pegs.print_game_play("0:30:53:05:61:92:B4:C5:18:29:E5:5C:DB:AC")

print("Example leave-10 play")
pegs.print_game_play("4:B4:27:D4:72")

# In case you are looking for a particular board:

# brd = """
#       X
#      . .
#     . X .
#    . . . .
#   . . X . .
# """
# bd = pegs.get_board_from_visual(brd)
# bn = pegs.get_board_number_from_board(bd)
# print_stats_for_board(bn)
