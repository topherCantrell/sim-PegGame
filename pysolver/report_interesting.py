import pegs

hit_boards = pegs.load_board_hits()

def count_not_covered(num_pegs):
    """count how many boards with num_pegs pegs are not covered in hit_boards"""
    total = 0
    nf = []

    for i in range(2**15):    
        if bin(i).count('1') !=num_pegs:
            continue
        total += 1
        found = False
        for _, stats in hit_boards.items():
            if str(i) in stats:
                found = True
        if not found:
            
            nf.append(i)
    return total, len(nf), nf

# Uncomment these to print the not-covered boards. Then look for interesting ones manually.
# total, count, nf = count_not_covered(2)
# print(f"Boards with 2 pegs: total {total}, not covered {count}")
# pegs.print_boards(nf)

# interesting_1 -- all boards are covered
interesting_2 = [17, 384, 576, 4097, 4112, 130, 272]
interesting_3 = [7, 11, 22, 56, 385, 21504, 3073, 4102, 4136, 7168, 10241, 14336]
interesting_4 = [960, 10816, 27648, 401]
interesting_5 = [4497, 346, 391, 598, 12932, 14353]
interesting_6 = [31745, 31760, 28224, 14736]
interesting_7 = [32128, 31616, 31750, 27670, 27674]
interesting_8 = [32321, 32336, 31785]
interesting_9 = [32704, 32360, 32145, 31767]
interesting_10 = [31806, 31791]
interesting_11 = [32598, 32185]
interesting_12 = [32367, 32382, 32190, 28665]
interesting_13 = [32750, 32727, 28655]
# interesting_14 -- all boards are covered

print(f"\nInteresting 2s {count_not_covered(2)[:2]}:")
pegs.print_boards(interesting_2)
print(f"\nInteresting 3s {count_not_covered(3)[:2]}:")
pegs.print_boards(interesting_3)
print(f"\nInteresting 4s {count_not_covered(4)[:2]}:")
pegs.print_boards(interesting_4)
print(f"\nInteresting 5s {count_not_covered(5)[:2]}:")
pegs.print_boards(interesting_5)
print(f"\nInteresting 6s {count_not_covered(6)[:2]}:")
pegs.print_boards(interesting_6)
print(f"\nInteresting 7s {count_not_covered(7)[:2]}:")
pegs.print_boards(interesting_7)
print(f"\nInteresting 8s {count_not_covered(8)[:2]}:")
pegs.print_boards(interesting_8)
print(f"\nInteresting 9s {count_not_covered(9)[:2]}:")
pegs.print_boards(interesting_9)
print(f"\nInteresting 10s {count_not_covered(10)[:2]}:")
pegs.print_boards(interesting_10)
print(f"\nInteresting 11s {count_not_covered(11)[:2]}:")
pegs.print_boards(interesting_11)
print(f"\nInteresting 12s {count_not_covered(12)[:2]}:")
pegs.print_boards(interesting_12)
print(f"\nInteresting 13s {count_not_covered(13)[:2]}:")
pegs.print_boards(interesting_13)
