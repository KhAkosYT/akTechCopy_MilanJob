# AI-Risk (Kódkupa 2025-26) - Solution

## Problem Summary

Tommaso and Filippo play AI-Risk with 3 territories:
- Tommaso has N soldiers, Filippo has M soldiers
- Tommaso distributes his soldiers first across 3 territories
- Filippo sees Tommaso's distribution and responds optimally
- Each player gets 1 point for each territory where they have ≥ soldiers than opponent
- Winner is who gets more points (2+ out of 3)
- Both players play optimally

## Key Insights

### Game Theory Analysis

1. **Filippo's Advantage**: Filippo has perfect information and moves second, giving him a strategic advantage.

2. **Tommaso's Optimal Strategy**: Since Filippo will respond optimally, Tommaso should distribute his soldiers as evenly as possible across the 3 territories. This forces Filippo to need maximum soldiers to win 2 territories.

3. **Optimal Distribution**: 
   - If N = 3k: [k, k, k]
   - If N = 3k+1: [k+1, k, k]
   - If N = 3k+2: [k+1, k+1, k]
   
   In general: [⌈N/3⌉, ⌈N/3⌉, ⌊N/3⌋] (sorted in descending order)

4. **Filippo's Response**: Filippo will target the 2 smallest territories to win with minimum soldiers.

### Mathematical Formula

For Filippo to **win** (get 2 points while Tommaso gets < 2):
- Filippo needs to beat (have strictly more soldiers than) 2 territories
- The 2 smallest territories in Tommaso's optimal distribution have ⌈N/3⌉ and ⌊N/3⌋ soldiers
- To beat them, Filippo needs (⌈N/3⌉ + 1) + (⌊N/3⌋ + 1) = N - ⌈N/3⌉ + 2 soldiers

**Winning Conditions**:
- **Filippo wins** if: `M >= N - ⌈N/3⌉ + 2`
- **Tommaso wins** if: `N >= M - ⌈M/3⌉ + 2`
- **Draw** otherwise

Note: When both conditions are true, Filippo wins because he moves second and can always force a win when he has enough soldiers.

### Why This Works

Example 1: N=3, M=3
- Filippo threshold: 3 - 1 + 2 = 4
- Tommaso threshold: 3 - 1 + 2 = 4
- M=3 < 4 and N=3 < 4, so **draw**
- Verification: Tommaso [1,1,1], Filippo [1,1,1] → both get 3 points → draw

Example 2: N=7, M=6
- Filippo threshold: 7 - 3 + 2 = 6
- Tommaso threshold: 6 - 2 + 2 = 6
- M=6 >= 6, so **Filippo wins**
- Verification: Tommaso [3,2,2], Filippo [0,3,3] → Filippo gets territories 2,3 → Filippo wins 2-1

## Implementation

The solution is straightforward:

```python
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
```

## Complexity

- **Time Complexity**: O(1) per test case
- **Space Complexity**: O(1)

This solution handles all constraints including N, M up to 1,000,000,000.

## Files Provided

- `risk.py` - Python solution
- `risk.cpp` - C++ solution
- `risk.java` - Java solution
- `test_input.txt` - Sample test cases from problem
- `test_extended.txt` - Additional test cases
- `verify_solution.py` - Verification script with detailed analysis
