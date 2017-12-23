
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
    protected String [] getMoves() {return MOVES;}
    
    public PegBoard(int oneMissing)
    {
        board = new boolean[getBoardSize()];
        moves = new ArrayList<String>();
        
        for(int x=0;x<board.length;++x) {
            board[x] = true;
        }
        
        board[oneMissing] = false;
    }
    
    public PegBoard(PegBoard other)
    {
        board = new boolean[other.board.length];
        for(int x=0;x<board.length;++x) {
            board[x] = other.board[x];
        }        
        moves = new ArrayList<String>(other.moves.size());    
        for(String s : other.moves) {
        	moves.add(s);
        }        
    }
    
    public boolean isMoveValid(String m)
    {    	        
        int a = m.charAt(0)-'A';
        int b = m.charAt(1)-'A';
        int c = m.charAt(2)-'A';
        if(board[a] && board[b] && !board[c]) {
            return true;
        }
        return false;
    }
    
    public boolean getPossibleMove()
    {  
        String [] validMoves = getMoves();
        for(int x=0;x<validMoves.length;++x) {
            if(isMoveValid(validMoves[x])) {
                return true;
            }
        }
        return false;
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
    	String n = ""+getNumberOfPegs();
    	if(n.length()<2) n="0"+n;
        String ret = n+": ";
        for(int x=0;x<moves.size();++x) {
            ret = ret + moves.get(x);
            if(x!=(moves.size()-1)) {
                ret = ret +",";
            }
        }
        return ret;
    }
    
    public static void runBoard(PegBoard p, List<String> ends)
    {        
        if(!p.getPossibleMove()) {
        	ends.add(p.toString());            
            return;
        }
        
        String [] pm = p.getMoves();
        for(int x=0;x<pm.length;++x) {
            if(p.isMoveValid(pm[x])) {
                PegBoard nb = new PegBoard(p);
                nb.makeMove(pm[x]);
                runBoard(nb,ends);
            }
        }        
    }
    
    private static void printStats(char mc, List<String> ends) {
		Collections.sort(ends);
		
		int [] nums = new int[11];
		
		for(String s : ends) {
			int i = s.indexOf(":");
			int a = Integer.parseInt(s.substring(0, i));
			++nums[a];
		}
        
        System.out.println("Starting empty "+mc+" "+ends.size()+" endings "+Arrays.toString(nums));
        System.out.println(ends.get(0));
        System.out.println(ends.get(ends.size()-1));
		
	}
    
    private static void doRun(char mc) {
    	int mp = mc-'A';
        PegBoard p = new PegBoard(mp);
        List<String> ends = new ArrayList<String>();
        runBoard(p,ends);
        
        printStats(mc,ends);       
    }
    
    // TODO this is really, really old code. Revisit this to make sure it is doing what you think.
    
    public static void main(String [] args) 
    {       
    	
    	doRun('A');
    	doRun('B');
    	doRun('D');
    	doRun('E');         
        
    }
	
    
}
