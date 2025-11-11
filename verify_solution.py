#!/usr/bin/env python3
import math

def solve(N, M):
    filippo_threshold = N - math.ceil(N / 3) + 2
    tommaso_threshold = M - math.ceil(M / 3) + 2
    
    if M >= filippo_threshold:
        return "filippo"
    elif N >= tommaso_threshold:
        return "tommaso"
    else:
        return "draw"

# Manual verification
test_cases = [
    (3, 3, "draw"),
    (7, 6, "filippo"),
    (1, 1, "draw"),
    (1, 2, "filippo"),
    (2, 1, "tommaso"),
    (10, 10, "filippo"),  # Let's verify this
]

print("Verification:")
for N, M, expected in test_cases:
    result = solve(N, M)
    filippo_th = N - math.ceil(N / 3) + 2
    tommaso_th = M - math.ceil(M / 3) + 2
    
    print(f"N={N}, M={M}")
    print(f"  Filippo threshold: {filippo_th}, M >= {filippo_th}? {M >= filippo_th}")
    print(f"  Tommaso threshold: {tommaso_th}, N >= {tommaso_th}? {N >= tommaso_th}")
    print(f"  Result: {result}, Expected: {expected}, Match: {result == expected}")
    
    # Manual game analysis
    if N == 10 and M == 10:
        print(f"  Manual: Tommaso optimal: [4,3,3], Filippo can do [0,4,4] or [1,4,4]")
        print(f"  With [0,4,4]: T gets territory 1, F gets territories 2,3 -> F wins 2-1")
    
    print()
