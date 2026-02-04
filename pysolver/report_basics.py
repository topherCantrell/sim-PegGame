import pegs

def print_stats(stats):
    total_games = 0
    totals_per = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    for _,counts in stats.items():
        for pegs_left, num_games in counts.items():
            totals_per[int(pegs_left)] += num_games
            total_games += num_games
    print(f"Total possible games: {total_games}")
    print(f"Pegs Left :  Number of games")
    for pegs_left, total in sorted(totals_per.items()):    
        pegs_left = str(pegs_left).rjust(2)    
        print(f"    {pegs_left}    :  {total}")

end_stats = pegs.load_basics()
print_stats(end_stats)
