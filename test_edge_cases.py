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

# Edge cases
edge_cases = [
    # (N, M, expected_result, description)
    (1, 1, "draw", "Minimum values"),
    (1, 2, "filippo", "Filippo has advantage"),
    (2, 1, "tommaso", "Tommaso has advantage"),
    (3, 3, "draw", "Equal, divisible by 3"),
    (4, 4, "filippo", "Equal, not divisible by 3"),
    (5, 5, "filippo", "Equal, not divisible by 3"),
    (6, 6, "filippo", "Equal, divisible by 3"),
    (7, 6, "filippo", "Example from problem"),
    (10, 5, "tommaso", "Tommaso has more"),
    (5, 10, "filippo", "Filippo has more"),
    (1000000000, 1000000000, "filippo", "Maximum values equal"),
    (1000000000, 999999999, "filippo", "Maximum values, Tommaso slightly more"),
    (999999999, 1000000000, "filippo", "Maximum values, Filippo slightly more"),
]

print("Edge Case Testing:")
print("=" * 80)

all_pass = True
for N, M, expected, description in edge_cases:
    result = solve(N, M)
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_pass = False
    
    print(f"{status} N={N:10d}, M={M:10d} -> {result:8s} (expected: {expected:8s}) | {description}")

print("=" * 80)
if all_pass:
    print("All tests passed! ✓")
else:
    print("Some tests failed! ✗")
