# AI-Risk - Visual Explanation

## Game Flow

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1: Tommaso distributes N soldiers                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │Territory │  │Territory │  │Territory │             │
│  │    1     │  │    2     │  │    3     │             │
│  │   [a]    │  │   [b]    │  │   [c]    │             │
│  └──────────┘  └──────────┘  └──────────┘             │
│  where a + b + c = N                                   │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 2: Filippo sees Tommaso's distribution           │
│          and responds with M soldiers                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │Territory │  │Territory │  │Territory │             │
│  │    1     │  │    2     │  │    3     │             │
│  │ T:[a]    │  │ T:[b]    │  │ T:[c]    │             │
│  │ F:[x]    │  │ F:[y]    │  │ F:[z]    │             │
│  └──────────┘  └──────────┘  └──────────┘             │
│  where x + y + z = M                                   │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  STEP 3: Score each territory                          │
│  - Player gets 1 point if soldiers >= opponent         │
│  - Both can get point if equal                         │
│  - Winner needs 2+ points                              │
└─────────────────────────────────────────────────────────┘
```

## Example 1: N=3, M=3 → Draw

```
Tommaso's optimal distribution: [1, 1, 1]

┌──────────┬──────────┬──────────┐
│Territory │Territory │Territory │
│    1     │    2     │    3     │
├──────────┼──────────┼──────────┤
│  T: 1    │  T: 1    │  T: 1    │
└──────────┴──────────┴──────────┘

Filippo's best response: [1, 1, 1] or [2, 1, 0]

Option A: [1, 1, 1]
┌──────────┬──────────┬──────────┐
│Territory │Territory │Territory │
│    1     │    2     │    3     │
├──────────┼──────────┼──────────┤
│  T: 1    │  T: 1    │  T: 1    │
│  F: 1    │  F: 1    │  F: 1    │
├──────────┼──────────┼──────────┤
│  T: ✓    │  T: ✓    │  T: ✓    │
│  F: ✓    │  F: ✓    │  F: ✓    │
└──────────┴──────────┴──────────┘
Score: T=3, F=3 → DRAW

Option B: [2, 1, 0]
┌──────────┬──────────┬──────────┐
│Territory │Territory │Territory │
│    1     │    2     │    3     │
├──────────┼──────────┼──────────┤
│  T: 1    │  T: 1    │  T: 1    │
│  F: 2    │  F: 1    │  F: 0    │
├──────────┼──────────┼──────────┤
│  T: ✗    │  T: ✓    │  T: ✓    │
│  F: ✓    │  F: ✓    │  F: ✗    │
└──────────┴──────────┴──────────┘
Score: T=2, F=2 → DRAW
```

## Example 2: N=7, M=6 → Filippo Wins

```
Tommaso's optimal distribution: [3, 2, 2]

┌──────────┬──────────┬──────────┐
│Territory │Territory │Territory │
│    1     │    2     │    3     │
├──────────┼──────────┼──────────┤
│  T: 3    │  T: 2    │  T: 2    │
└──────────┴──────────┴──────────┘

Filippo's winning response: [0, 3, 3]

┌──────────┬──────────┬──────────┐
│Territory │Territory │Territory │
│    1     │    2     │    3     │
├──────────┼──────────┼──────────┤
│  T: 3    │  T: 2    │  T: 2    │
│  F: 0    │  F: 3    │  F: 3    │
├──────────┼──────────┼──────────┤
│  T: ✓    │  T: ✗    │  T: ✗    │
│  F: ✗    │  F: ✓    │  F: ✓    │
└──────────┴──────────┴──────────┘
Score: T=1, F=2 → FILIPPO WINS
```

## Why Even Distribution is Optimal for Tommaso

```
Bad distribution: [7, 0, 0]
→ Filippo can easily win with [3, 2, 1]
→ Filippo wins territories 2 & 3

Good distribution: [3, 2, 2]
→ Filippo needs 6 soldiers to beat territories 2 & 3
→ Forces Filippo to use all resources

Best distribution: [⌈N/3⌉, ⌈N/3⌉, ⌊N/3⌋]
→ Maximizes the cost for Filippo to win 2 territories
→ Makes the 2 smallest territories as large as possible
```

## The Mathematical Insight

```
Tommaso distributes: [⌈N/3⌉, ⌈N/3⌉, ⌊N/3⌋]

For Filippo to WIN 2 territories (not just tie):
- Must beat territory 2: needs ⌈N/3⌉ + 1 soldiers
- Must beat territory 3: needs ⌊N/3⌋ + 1 soldiers
- Total needed: ⌈N/3⌉ + ⌊N/3⌋ + 2 = N - ⌈N/3⌉ + 2

Therefore:
  Filippo wins if M >= N - ⌈N/3⌉ + 2
  Tommaso wins if N >= M - ⌈M/3⌉ + 2
  Otherwise: Draw
```

## Second-Mover Advantage

```
When N = M and both can theoretically win:
→ Filippo wins because he moves second
→ He can see Tommaso's distribution and respond optimally
→ This is why when N = M = 6, Filippo wins (not draw)

Exception: N = M = 3 (and N = M = 3k in general)
→ Even with perfect information, Filippo can only force a draw
→ The threshold is exactly at the boundary
```
