# Peg Game

What's the holidays without breakfast at Cracker Barrel? And while you are sitting there in awkward silence with
extended family, what better way to pass the time than with that triangle of wood filled with golf tees.

![https://github.com/topherCantrell/PegGame/blob/master/art/MovesFromD.jpg](https://github.com/topherCantrell/PegGame/blob/master/art/MovesFromD.jpg)

The board has 15 holes I am labeling 'A' through 'O'. A 'move' is a series of 3 holes in a line. The diagram above
shows all four moves that begin with hole 'D'. It is easy enough to enumerate all possible moves on the board. There
are 36 different moves on the board:

```java

    //       A
    //      B C
    //     D E F
    //    G H I J
    //   K L M N O
    
    static final String [] MOVES = {
        "ABD","ACF",
        "BEI","BDG",
        "CEH","CFJ",
        "DBA","DEF","DHM","DGK",
        "EIN","EHL",
        "FCA","FED","FIM","FJO",
        "GDB","GHI",
        "HEC","HIJ",
        "IHG","IEB",
        "JFC","JIH",
        "KGD","KLM",
        "LHE","LMN",
        "MLK","MHD","MIF","MNO",
        "NML","NIE",
        "ONM","OJF"
    };
    
```

## Starting Configuration

The game begins with one empty hole. There are 15 different choices for the first empty hole, but they all
collapse by mirroring or folding to one of these 4 possibilities:

![https://github.com/topherCantrell/PegGame/blob/master/art/Starts.jpg](https://github.com/topherCantrell/PegGame/blob/master/art/Starts.jpg)
