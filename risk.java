import java.util.Scanner;

public class risk {
    public static String solve(long N, long M) {
        // Filippo wins if M >= N - ceil(N/3) + 2
        // Tommaso wins if N >= M - ceil(M/3) + 2
        // Otherwise draw
        
        long filippo_threshold = N - (N + 2) / 3 + 2;
        long tommaso_threshold = M - (M + 2) / 3 + 2;
        
        if (M >= filippo_threshold) {
            return "filippo";
        } else if (N >= tommaso_threshold) {
            return "tommaso";
        } else {
            return "draw";
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        
        for (int i = 0; i < T; i++) {
            long N = scanner.nextLong();
            long M = scanner.nextLong();
            System.out.println(solve(N, M));
        }
        
        scanner.close();
    }
}
