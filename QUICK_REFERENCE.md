# AI-Risk Solution - Quick Reference

## The Formula (One-Liner)

```
Filippo wins if M >= N - ⌈N/3⌉ + 2
Tommaso wins if N >= M - ⌈M/3⌉ + 2  
Otherwise: Draw
(If both true, Filippo wins)
```

## Why It Works

1. **Tommaso's best move**: Split evenly [⌈N/3⌉, ⌈N/3⌉, ⌊N/3⌋]
2. **Filippo's response**: Beat the 2 smallest territories
3. **Cost to beat**: Need (⌈N/3⌉ + 1) + (⌊N/3⌋ + 1) = N - ⌈N/3⌉ + 2

## Examples

| N | M | Result | Why |
|---|---|--------|-----|
| 3 | 3 | draw | Both need 4 to win, neither has it |
| 7 | 6 | filippo | Filippo needs 6, has 6 ✓ |
| 10 | 5 | tommaso | Tommaso needs 6, has 10 ✓ |
| 6 | 6 | filippo | Both need 6, Filippo wins (2nd mover) |

## Code (Python)

```python
import math
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    f_th = N - math.ceil(N/3) + 2
    t_th = M - math.ceil(M/3) + 2
    if M >= f_th: print("filippo")
    elif N >= t_th: print("tommaso")
    else: print("draw")
```

## Code (C++)

```cpp
#include <iostream>
using namespace std;
int main() {
    int T; cin >> T;
    while(T--) {
        long long N, M; cin >> N >> M;
        long long f_th = N - (N+2)/3 + 2;
        long long t_th = M - (M+2)/3 + 2;
        if(M >= f_th) cout << "filippo\n";
        else if(N >= t_th) cout << "tommaso\n";
        else cout << "draw\n";
    }
}
```

## Key Points

✓ O(1) time per test case
✓ Works for N, M up to 10^9
✓ No simulation needed
✓ Pure mathematical solution
✓ Filippo has second-mover advantage
