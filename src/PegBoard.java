
import java.util.*;

public class PegBoard implements Cloneable
{
    
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

    List<String> moves;
    boolean [] board;
    
    // Subclass this to provide different types of boards and associated moves
    protected int getBoardSize() {return 15;}    
    protected String [] getValidMoves() {return MOVES;}
    //
    
    public PegBoard(int missing)
    {
        board = new boolean[getBoardSize()];
        moves = new ArrayList<String>();
        
        for(int x=0;x<board.length;++x) {
            board[x] = true;
        }
        board[missing] = false;
    }
    
    public Object clone() throws CloneNotSupportedException
    {
        PegBoard ob = (PegBoard)super.clone();
        ob.board = new boolean[getBoardSize()];
        for(int x=0;x<board.length;++x) {
            ob.board[x] = board[x];
        }        
        ob.moves = new ArrayList<String>();        
        for(int x=0;x<moves.size();++x) {
            ob.moves.add(moves.get(x));
        }
        return ob;
    }
    
    public boolean isMoveValid(String m)
    {
        if(m.length()<3) {
            return false;
        }
        int a = m.charAt(0)-'A';
        int b = m.charAt(1)-'A';
        int c = m.charAt(2)-'A';
        if(board[a] && board[b] && !board[c]) {
            return true;
        }
        return false;
    }
    
    public String getPossibleMove()
    {  
        String [] validMoves = getValidMoves();
        for(int x=0;x<validMoves.length;++x) {
            if(isMoveValid(validMoves[x])) {
                return validMoves[x];
            }
        }
        return null;
    }
    
    public boolean makeMove(String m)
    {
        if(!isMoveValid(m)) {
            return false;
        }
        int a = m.charAt(0)-'A';
        int b = m.charAt(1)-'A';
        int c = m.charAt(2)-'A';
        board[a] = false;
        board[b] = false;
        board[c] = true;        
        moves.add(m);
        return true;
    }
    
    public int getNumberOfPegs()
    {
        int cnt = 0;
        for(int x=0;x<board.length;++x) {
            if(board[x]) {
                ++cnt;
            }
        }
        return cnt;
    }
    
    public String toString()
    {
        String ret = ""+getNumberOfPegs()+": ";
        for(int x=0;x<moves.size();++x) {
            ret = ret + moves.get(x);
            if(x!=(moves.size()-1)) {
                ret = ret +",";
            }
        }
        return ret;
    }
    
    public static void runBoard(PegBoard p) throws Exception 
    {        
        if(p.getPossibleMove() == null) {
            System.out.println(p);
            return;
        }
        String [] pm = p.getValidMoves();
        for(int x=0;x<pm.length;++x) {
            if(p.isMoveValid(pm[x])) {
                PegBoard nb = (PegBoard)p.clone();
                nb.makeMove(pm[x]);
                runBoard(nb);
            }
        }        
    }
    
    public static void main(String [] args) throws Exception
    {       
        if(args.length!=1 || args[0].length()<1 || 
          args[0].charAt(0)<'A' || args[0].charAt(0)>'O') {
            System.out.println("Arguments: MissingPeg position (A-O)");
            return;
        }
        
        int mp = args[0].charAt(0)-'A';
        PegBoard p = new PegBoard(mp);
        runBoard(p);
    }
    
}
