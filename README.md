# Comp472 - Project 1 - Indonesian Dot Puzzle
## Due Date
Due dates D1: Sunday Feb 9 + D2: Sunday March 1, 2020
Late Submissions 20% per day per late deliverable

## Team <team_name>
```
- Hongbo Liu: 29566228
- Thanh Tung Nguyen: 40042891
```
Teams must submit only 1 copy of the project via the team leader’s account.
Purpose In this project, you will implement and analyse a heuristic search.

### To run the program
```python3 player.py -i <input_file_name> -s <search_algo_type>```

## Project Approach Requirements
Implement a solution for the Indonesian Dot for any size of boards (n) from [3 to 10].

### 2.1 Search Algorithms
The project must implement the following 3 search (Heuristic Search) algorithms:


```
1. Depth-first search (DFS)
2. Best-first search (BFS)
3. Algorithm A*
```

### 2.2 Programming Environment:
PyCharm on MacOS

### 2.3 The Input

Your code should be able to receive the path of an input file that contains test cases. The input file will contain
a sequence of lines, containing:

```
1. the size of the puzzle (n)
2. the maximum depth search for DFS (max d)
3. the maximum search path length (maxl) for BFS and A?
4. the values of the initial puzzle’s n × n tokens, where each token will be represented by a 1 (•) or a 0 (◦).
The order of the tokens will be left-to-right, top-down.
```
When using DFS, you can ignore max_l and when using BFS or A?
, you can ignore max_d.
For example, the input file could contain (Figure 1):

```
4 9 50 1110100111000111
3 100 2000 011001100
```

puzzle #0: puzzle of Figure 1 with max_d = 9 and max_l = 50
puzzle #1: a 3 × 3 puzzle with max_d = 100 and max_l = 2000


Note: There is no need to check the validity of the input file; you can assume that it will be correct