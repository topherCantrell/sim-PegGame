import pegs

def print_stats(stats):
    print("Overall Stats:")
    total_games = 0
    totals_per = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    for _,counts in stats.items():
        for pegs_left, (num_games, _) in counts.items():
            totals_per[int(pegs_left)] += num_games
            total_games += num_games
    print(f"Total possible games: {total_games}")
    print(f"Pegs Left :  Number of games")
    for pegs_left, total in sorted(totals_per.items()):    
        pegs_left = str(pegs_left).rjust(2)  
        tot = str(total).rjust(8)  
        print(f"    {pegs_left}    :  {tot}")

def print_single_stats(stats, start_hole):
    print("Single Start Hole Stats:")
    counts = stats[str(start_hole)]
    total_games = 0
    print(f"Start hole {start_hole:X}")
    print(f"Pegs Left :  Number of games")
    for pegs_left in range(1,12):
        num_games, example = counts.get(str(pegs_left), (0,""))
        total_games += num_games
        pegs_left_str = str(pegs_left).rjust(2)  
        tot = str(num_games).rjust(8)  
        print(f"    {pegs_left_str}    :  {tot}   Example: {example}")
    print(f"Total games from start hole {start_hole:X}: {total_games}")

end_stats = pegs.load_basics()
print_stats(end_stats)
print()
print_single_stats(end_stats, 0)
print_single_stats(end_stats, 1)
print_single_stats(end_stats, 3)
print_single_stats(end_stats, 4)
