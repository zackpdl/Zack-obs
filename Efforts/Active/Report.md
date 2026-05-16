

## Task 1 (mincoin)

### v1
- **mincoin1.in**:
  - Result: 4
  - Time: 0.2523s

### v2
- **mincoin1.in**:
  - Result: 4
  - Time: 0.0000s
- **mincoin2.in**:
  - Result: 2
  - Time: 0.0003s
- **mincoin3.in**:
  - Result: 6
  - Time: 0.0001s
- **mincoin4.in**:
  - Result: RecursionError: maximum recursion depth exceeded

## Task 2 (cutrod)

### v1
- **1.in**:
  - Result: 29
  - Time: 0.0002s

### v2
- **1.in**:
  - Result: 29
  - Time: 0.0000s
- **2.in**:
  - Result: 52
  - Time: 0.0000s
- **3.in**:
  - Result: 160
  - Time: 0.0001s
- **4.in**:
  - Result: 366
  - Time: 0.0007s


Analysis
- Without memoization, the recursive algorithm repeats the same work many times, so it becomes slow and can even crash. In MinCoin and CutRod, the first version gets slower as inputs grow, while the memoized version stays fast because it remembers past results. This makes the algorithm much more efficient.
