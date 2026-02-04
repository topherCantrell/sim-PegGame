import pegs

hit_boards = pegs.load_board_hits()

def print_board_totals():
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
    for i in range(20):
        board_num, total_count = flat[-(i+1)]
        print(f'Board {board_num} hit {total_count} times.')

def print_per_start_hole_stats():
    for start_hole in range(15):
        boards_for_start = hit_boards.get(str(start_hole))
        print(f"Start hole {start_hole:X}: {len(boards_for_start)} boards hit.")        

def print_stats_for_board(board_num):
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

# print_per_start_hole_stats()
# print_board_totals()

brd = """
      X
     . .
    . X .
   . . . .
  . . X . .
"""
bd = pegs.get_board_from_visual(brd)
bn = pegs.get_board_number_from_board(bd)
print_stats_for_board(bn)
print()

total = 0
num = 0
nf = []

for i in range(2**15):    
    if bin(i).count('1') !=4:
        continue
    num += 1
    found = False
    for start, stats in hit_boards.items():
        if str(i) in stats:
            total += stats[str(i)][0]
            found = True
    if not found:
        nf.append(i)
        #print(">>> NOT FOUND BOARD:", i)
        #pegs.print_board(pegs.get_board_from_board_number(i))
        #print()

#print(">>>",num, total, nf)

pegs.print_boards(nf)

# interesting_2 = [
#     17, 384, 576, 4097, 4112, 130, 272
# ]

# print("\n\n")
# pegs.print_boards(interesting_2)

# interesting_3 = [
#     7,11,22,56,385,21504,3073,4102,4136,7168,10241,14336
# ]
# print("\n\n")
# pegs.print_boards(interesting_3)

interesting_4 = [960,10816,27648,401]

brd = """
      X
     . .
    X . X
   . . . .
  . . X . .
"""
bd = pegs.get_board_from_visual(brd)
bn = pegs.get_board_number_from_board(bd)
print_stats_for_board(bn)
print()