# Peg Game

What are the holidays without breakfast at Cracker Barrel? And while you are sitting there in awkward silence with
extended family, what better way to pass the time than with that triangle of wood filled with golf tees.

![](art/game.jpg)

# The Model

I modeled the board as 15 holes numbered in hexadecimal from 0 to E. Hole 0 is the top most hole then left to right top to
bottom as you can see in the photo and here:

```
    0
   1 2
  3 4 5
 6 7 8 9
A B C D E
```

A "move" is a series of 3 holes in a line. The move [3,1,0] means the peg in hole 3 jumps the peg in hole 1
and ends up in hole 0, which was empty at the start of the move. Most holes only begin two moves. Hole 0,
for instance, is the start of [0,1,3] and [0,2,5]. The holes in the middle on the outside (holes 3, 5, and C)
are the starting point for four moves each. Hole 3, for instance, starts moves [3,1,0], [3,4,5], [3,7,C],
and [3,6,A].

I enumerated all 36 possible moves in my code (the holes are defined with decimal constants instead of hex):

```python
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
```

# Starting Hole

Every game begins with 14 pegs and one empty hole. You could leave a corner open: 0, A, or E. You can rotate the board
and these are all essentially the same empty hole.

Likewise, the outer middles are rotationally equivalent: 3, 5, and C. So are the inner holes 4, 7, and 8.

In addition to rotating the board, you could play backwards (throgh a mirror). The remaining holes are thus equivalent:
1, 2, 6, 9, B, D.

My simulation does not reduce the game space with mirroring and/or rotation. In my simulation, there are 14 possible starting 
holes, and all games that start with 0 are different from all games that start with E (for instance).

![](art/starts.jpg)

# Game Statistics

The code in [make_basics](pysolver/make_basics.py) plays all possible games from all possible starting empty holes. The algorithm checks
each of the 36 moves one at a time. If the move is valid, the algorithm is called recursively with the new board. It takes about 43 seconds
for my computer to cover all posibilities. Here are the statistics:

```
Total possible games: 7,335,390
Pegs Left :  Number of games : Example game
     1    :  438,984         : 0:30:53:05:61:92:B4:C5:18:29:E5:5C:DB:AC
     2    :  1,776,648       : 0:30:53:05:61:92:B4:27:C3:16:A3:D4:35
     3    :  3,302,124       : 0:30:53:05:61:86:92:A3:16:CA:A3:EC
     4    :  1,605,348       : 0:30:53:05:61:86:A3:30:CA:EC:5E
     5    :  197,670         : 0:30:53:05:61:92:B4:27:D4:72
     6    :  11,160          : 0:30:53:61:03:B4:C5:50:E5
     7    :  3,438           : 0:30:53:05:61:B4:97:4B
     8    :  12              : 0:30:C3:97:68:5C:05
     9    :  0               : none
    10    :  6               : 4:B4:27:D4:72
```

The table shows the number of games that leave a specific number of pegs and an example game for each ending count.

There are 7,335,390 possible games you can play. If you sat down and made random moves, you'd end up making the
moves in one of these 7.3 million games.

Nearly half the possible games end up with three pegs (3,302,124). About 22% of the games end with 2 pegs. Another
22% with 4 pegs.

There are 438,984 games that end in one peg. If you sat down at a board and picked a random starting hole and made
random moves, you leave one peg about 6% of the time. 6 out of 100 games would be winners.

Note that there are no games that end with 9 pegs remaining. And the real challenge is not to leave 1 peg -- playing
at random gets you that 6% of the time.

The REAL challenge is play a game that leaves 10 pegs. There are only 6 games out the possible 7.3 million that end 
with ten. The example game above ends up like this (dots are empty holes):

```
    0
   1 2
  3 . 5
 6 . . 9
A . C . E
```

# Board Configurations

You can think of the board as a 15-bit binary number with each bit representing a peg. There are thus 2**15 = 32,768
possible states the board could be in. I talk board configuration by its binary-to-decimal number. Board 0 (all empty holes)
is not valid since we must have at least one peg. And board 327676 (all filled holes) is not valid since we must
start with one empty hole.

TODO lots more here