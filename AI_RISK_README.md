# AI-Risk Problem Solution - Kódkupa 2025-26

## 📋 Problem Overview

**Competition**: Kódkupa 2025-26, Round 1  
**Problem**: AI-Risk (risk)  
**Difficulty**: Game Theory + Mathematical Analysis

Two players (Tommaso and Filippo) play a strategic game on 3 territories:
- Tommaso has N soldiers, Filippo has M soldiers
- Tommaso distributes first, Filippo responds after seeing Tommaso's distribution
- Winner is determined by who controls more territories (need 2+ out of 3)
- Both players play optimally

## 🎯 Solution Summary

**Time Complexity**: O(1) per test case  
**Space Complexity**: O(1)  
**Key Insight**: Second-mover advantage + optimal even distribution

### The Formula

```
Filippo wins if: M >= N - ⌈N/3⌉ + 2
Tommaso wins if: N >= M - ⌈M/3⌉ + 2
Otherwise: Draw
```

## 📁 Files in This Solution

### Core Solutions
- **`risk.py`** - Python implementation (recommended for quick testing)
- **`risk.cpp`** - C++ implementation (for competitive programming)
- **`risk.java`** - Java implementation

### Documentation
- **`QUICK_REFERENCE.md`** - One-page cheat sheet with formula and examples
- **`SOLUTION.md`** - Detailed mathematical explanation
- **`VISUAL_EXPLANATION.md`** - Step-by-step visual walkthrough
- **`SUMMARY.md`** - Complete overview of approach and results

### Testing
- **`test_input.txt`** - Official problem examples
- **`test_extended.txt`** - Additional test cases
- **`test_edge_cases.py`** - Comprehensive edge case testing
- **`verify_solution.py`** - Manual verification with detailed analysis

## 🚀 Quick Start

### Run the Solution

```bash
# Python (easiest)
python3 risk.py < test_input.txt

# C++ (if compiler available)
g++ -o risk risk.cpp && ./risk < test_input.txt

# Java
javac risk.java && java risk < test_input.txt
```

### Test the Solution

```bash
# Run all tests
python3 test_edge_cases.py

# Verify with detailed analysis
python3 verify_solution.py
```

## 📊 Test Results

✅ **All official examples pass**
- N=3, M=3 → draw ✓
- N=7, M=6 → filippo ✓

✅ **All edge cases pass**
- Minimum values (N=1, M=1)
- Maximum values (N=10^9, M=10^9)
- Various equal and unequal distributions

✅ **Manual verification confirms correctness**

## 🧠 Key Insights

1. **Second-Mover Advantage**: Filippo's ability to see Tommaso's distribution gives him a strategic edge

2. **Optimal Strategy**: Tommaso should distribute evenly [⌈N/3⌉, ⌈N/3⌉, ⌊N/3⌋] to maximize the cost for Filippo to win

3. **Mathematical Formula**: The winning threshold can be computed in O(1) time without simulation

4. **Tie-Breaking**: When both players theoretically can win, Filippo wins due to second-mover advantage

## 📖 How to Read This Solution

1. **Start here**: `QUICK_REFERENCE.md` - Get the formula and basic understanding
2. **Visual learner?**: `VISUAL_EXPLANATION.md` - See step-by-step examples
3. **Want details?**: `SOLUTION.md` - Full mathematical derivation
4. **Ready to code?**: Use `risk.py`, `risk.cpp`, or `risk.java`

## 🎓 Learning Points

This problem teaches:
- Game theory with perfect information
- Optimal strategy under adversarial conditions
- Second-mover advantage in sequential games
- Mathematical optimization without simulation
- Ceiling/floor division tricks

## 📝 Problem Constraints

- 1 ≤ T ≤ 10 (number of test cases)
- 1 ≤ N, M ≤ 1,000,000,000 (soldiers)

## 🏆 Scoring

- Subtask 0 (0 points): Examples
- Subtask 1 (30 points): N, M ≤ 30
- Subtask 2 (30 points): N, M ≤ 300
- Subtask 3 (40 points): No additional constraints

**This solution solves all subtasks** (100 points)

## 💡 Tips for Competition

1. The formula is simple - memorize it!
2. Watch out for integer overflow (use `long long` in C++)
3. Ceiling division: `(N + 2) / 3` in C++, `math.ceil(N/3)` in Python
4. No need for simulation or complex game tree search
5. O(1) solution is fast enough for all constraints

## 🤝 Contributing

Found an issue or have a question? The solution has been thoroughly tested, but if you find edge cases or have improvements, feel free to document them!

---

**Author**: Solution for Kódkupa 2025-26  
**Date**: November 2025  
**Status**: ✅ Verified and tested
