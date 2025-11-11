#!/usr/bin/env python3
import math

def solve(N, M):
    """
    Determine the winner of AI-Risk game.
    
    Key insight:
    - Tommaso distributes N soldiers optimally across 3 territories
    - Filippo responds optimally with M soldiers
    - Optimal strategy for Tommaso: distribute as evenly as possible
    - This forces Filippo to need maximum soldiers to win 2 territories
    
    Tommaso's optimal distribution: make the two smallest territories as large as possible
    - If N = 3k: [k, k, k]
    - If N = 3k+1: [k+1, k, k]
    - If N = 3k+2: [k+1, k+1, k]
    
    The two smallest territories will have at least floor(N/3) soldiers each.
    
    For Filippo to win 2 territories:
    - He needs to beat/match the two smallest territories
    - Minimum needed: 2 * ceil(N/3) to guarantee winning 2 territories
    
    Actually, let's think more carefully:
    - Tommaso puts [a, b, c] with a >= b >= c
    - Filippo will target the 2 smallest (b and c) to win with minimum soldiers
    - To win territory with x soldiers, Filippo needs x soldiers (to tie and win)
    - To win 2 territories with b and c soldiers, Filippo needs b + c soldiers
    
    Tommaso's optimal: maximize (b + c) to make it hard for Filippo
    - Best is to make them as equal as possible
    - Optimal: [ceil(N/3), ceil(N/3), floor(N/3)] or similar
    
    Let's compute:
    - third = N // 3
    - remainder = N % 3
    - If remainder == 0: [third, third, third] -> b+c = 2*third
    - If remainder == 1: [third+1, third, third] -> b+c = 2*third
    - If remainder == 2: [third+1, third+1, third] -> b+c = 2*third + 1
    
    So Filippo needs:
    - If N % 3 == 0 or N % 3 == 1: M >= 2*(N//3) to tie on 2 territories
    - If N % 3 == 2: M >= 2*(N//3) + 1 to tie on 2 territories
    
    But to WIN, Filippo needs to get 2 points while Tommaso gets at most 1.
    
    Let me reconsider the scoring:
    - A player gets a point if they have >= soldiers on a territory
    - So if both have equal soldiers, both get the point
    
    Wait, re-reading: "Minden egyes területért egy pont jár annak a játékosnak, 
    akinek ott legalább annyi katonája van, mint a másiknak."
    
    This means: a player gets a point for a territory if they have >= soldiers than opponent.
    So if equal, BOTH get a point!
    
    This changes things:
    - If Tommaso: [1,1,1] and Filippo: [1,1,1], both get 3 points -> draw
    - If Tommaso: [3,0,0] and Filippo: [1,1,1], Filippo gets 2 points (territories 2,3), 
      Tommaso gets 1 point (territory 1)
    
    New analysis:
    - Tommaso wants to maximize his guaranteed points
    - Filippo will respond to maximize his points (minimize Tommaso's)
    
    If Tommaso distributes evenly [ceil(N/3), ceil(N/3), floor(N/3)]:
    - Filippo can match/beat 2 territories if he has enough soldiers
    - To beat 2 territories, Filippo needs > sum of 2 smallest
    - To match 2 territories, Filippo needs = sum of 2 smallest
    
    Let's denote Tommaso's distribution as [a, b, c] with a >= b >= c.
    - Filippo will try to maximize his score
    - Best strategy for Filippo: focus on 2 territories
    
    If Filippo puts [0, b, c] to match/beat territories 2 and 3:
    - Filippo gets points for territories where his soldiers >= Tommaso's
    - Tommaso gets points for territories where his soldiers >= Filippo's
    
    Key insight: 
    - If M > N, Filippo can always win
    - If M = N and Tommaso distributes evenly, it's a draw
    - If M < N, Tommaso can win
    
    Let me think about the threshold:
    - Tommaso optimal: [ceil(N/3), ceil(N/3), floor(N/3)]
    - Sum of 2 smallest = ceil(N/3) + floor(N/3)
    
    If N = 3k: sum = k + k = 2k = 2N/3
    If N = 3k+1: sum = k+1 + k = 2k+1 = 2(N-1)/3 + 1 = (2N+1)/3
    If N = 3k+2: sum = k+1 + k+1 = 2k+2 = 2(N-2)/3 + 2 = (2N+2)/3
    
    Simplified: sum of 2 smallest = 2*ceil(N/3)
    
    For Filippo to win (get 2 points while Tommaso gets < 2):
    - Filippo needs to beat 2 territories
    - This requires M > 2*ceil(N/3) - 1, i.e., M >= 2*ceil(N/3)
    
    Wait, let me verify with examples again:
    
    Example 1: N=3, M=3
    - ceil(3/3) = 1
    - 2*ceil(3/3) = 2
    - M = 3 >= 2, so Filippo should win?
    - But answer is draw!
    
    Let me reconsider...
    
    If Tommaso: [1,1,1] and Filippo has 3 soldiers:
    - Filippo can do [2,1,0]: Filippo gets territory 1 (2>1), both get territory 2 (1=1), 
      Tommaso gets territory 3 (1>0)
    - Filippo: 2 points (territories 1,2), Tommaso: 2 points (territories 2,3) -> Draw!
    
    Ah! When soldiers are equal, BOTH get the point!
    
    So if Filippo matches exactly on 2 territories:
    - Both get those 2 points
    - The third territory goes to whoever has more
    - Result: Draw if Filippo uses all soldiers to match
    
    New strategy:
    - To WIN, Filippo needs to strictly beat 2 territories
    - To strictly beat territory with x soldiers, need x+1 soldiers
    - To win, Filippo needs M >= 2*ceil(N/3) + 1
    
    Let's verify:
    Example 1: N=3, M=3
    - 2*ceil(3/3) + 1 = 2*1 + 1 = 3
    - M = 3, not > 3, so not Filippo win
    - Check if Tommaso wins: similar logic, N >= 2*ceil(M/3) + 1 = 3
    - N = 3, not > 3, so not Tommaso win
    - Result: Draw ✓
    
    Example 2: N=7, M=6
    - 2*ceil(7/3) + 1 = 2*3 + 1 = 7
    - M = 6 < 7, so Filippo doesn't strictly win
    - But wait, answer is Filippo wins!
    
    Hmm, let me reconsider the game more carefully...
    
    Actually, I think the issue is that Filippo can be smarter.
    
    If Tommaso: [3,2,2] (total 7)
    Filippo can: [0,3,3] (total 6)
    - Territory 1: Tommaso 3, Filippo 0 -> Tommaso gets point
    - Territory 2: Tommaso 2, Filippo 3 -> Filippo gets point
    - Territory 3: Tommaso 2, Filippo 3 -> Filippo gets point
    - Result: Filippo 2, Tommaso 1 -> Filippo wins!
    
    So Filippo needs M >= 2*ceil(N/3) to win (not +1).
    
    Let's verify again:
    Example 1: N=3, M=3
    - 2*ceil(3/3) = 2
    - M = 3 >= 2, so Filippo should win?
    - But if Tommaso: [1,1,1], Filippo: [2,1,0]
    - Territory 1: T=1, F=2 -> F wins
    - Territory 2: T=1, F=1 -> Both win
    - Territory 3: T=1, F=0 -> T wins
    - Score: F=2, T=2 -> Draw!
    
    The issue is that when Filippo matches exactly, both get points.
    
    So for Filippo to WIN (not draw):
    - Filippo needs to get 2 points while Tommaso gets < 2 points
    - If Filippo matches 2 territories exactly, both get 2 points -> draw
    - Filippo needs to beat at least one territory strictly
    
    Let me think about this differently:
    - Tommaso: [a, b, c] with a >= b >= c, a+b+c = N
    - Filippo: [x, y, z] with x+y+z = M
    - Filippo wants to maximize his score
    
    Filippo's best strategy:
    - Put just enough to beat/match territories, prioritizing smaller ones
    - If M is large enough, beat 2 smallest territories
    - If M is limited, match what he can
    
    For Filippo to guarantee winning:
    - He needs to beat 2 territories
    - Beating means having strictly more soldiers
    - To beat territories with b and c soldiers: need b+1 and c+1, total b+c+2
    
    Tommaso's optimal makes b+c as large as possible:
    - [ceil(N/3), ceil(N/3), floor(N/3)]
    - b+c = ceil(N/3) + floor(N/3) = N - ceil(N/3)
    
    For Filippo to win: M >= N - ceil(N/3) + 2
    
    Let's verify:
    Example 1: N=3, M=3
    - N - ceil(3/3) + 2 = 3 - 1 + 2 = 4
    - M = 3 < 4, so Filippo doesn't win
    - Similarly for Tommaso: M=3, N=3, same calc, doesn't win
    - Result: Draw ✓
    
    Example 2: N=7, M=6
    - N - ceil(7/3) + 2 = 7 - 3 + 2 = 6
    - M = 6 >= 6, so Filippo wins ✓
    
    Great! So the formula is:
    - Filippo wins if: M >= N - ceil(N/3) + 2
    - Tommaso wins if: N >= M - ceil(M/3) + 2
    - Otherwise: Draw
    
    Simplifying: M >= N - ceil(N/3) + 2
    = M >= N + 2 - ceil(N/3)
    = M > N + 1 - ceil(N/3)
    
    Let's simplify further:
    - ceil(N/3) = (N + 2) // 3
    - N + 2 - ceil(N/3) = N + 2 - (N+2)//3
    
    For N = 3k: N + 2 - k = 2k + 2 = 2N/3 + 2
    For N = 3k+1: N + 2 - (k+1) = 3k+1+2-k-1 = 2k+2 = 2(N-1)/3 + 2 = (2N+4)/3
    For N = 3k+2: N + 2 - (k+1) = 3k+2+2-k-1 = 2k+3 = 2(N-2)/3 + 3 = (2N+5)/3
    
    Actually, simpler formula:
    - N - ceil(N/3) + 2 = N - (N+2)//3 + 2
    
    Let me code this:
    """
    
    # Filippo wins if M >= N - math.ceil(N/3) + 2
    filippo_threshold = N - math.ceil(N / 3) + 2
    tommaso_threshold = M - math.ceil(M / 3) + 2
    
    if M >= filippo_threshold:
        return "filippo"
    elif N >= tommaso_threshold:
        return "tommaso"
    else:
        return "draw"


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(solve(N, M))


if __name__ == "__main__":
    main()
