# Missionaries & Cannibals Problem

This project implements a solution to the classic Missionaries and Cannibals problem using state-space search algorithms in Python.

## Problem Description
Three missionaries and three cannibals must cross a river using a boat that can carry at most two people. At no point should cannibals outnumber missionaries on either side of the river, or the missionaries will be eaten.

**This project implements TWO versions of the problem:**

### Version 1: Classic Two-Side Problem
The traditional version where people cross directly from the left side to the right side of the river.

### Version 2: Three-Location Problem with Island
An extended version where there's an intermediate island in the river. People can move between:
- Left side ↔ Island
- Island ↔ Right side
- The boat can be on the left side (L), island (I), or right side (R)

## Features
- Two different state representations for both problem versions
- Search algorithms to find optimal solutions
- Heuristics for informed search
- Performance comparison between versions

## File Overview
- `main.py`: Entry point to run the program
- `MCState.py`: Classic two-side problem state representation
- `MCIslandState.py`: Extended three-location problem with island
- `search.py`: Implements search algorithms (A*, etc.)
- `search_node.py`: Node structure for search trees
- `heuristics.py`: Heuristic functions for informed search

## How to Run
1. Ensure you have Python 3 installed.
2. Run the main program:
   ```powershell
   python main.py
   ```

## Requirements
No external dependencies required.

## Output
The program will:
- Solve the classic two-side version of the problem
- Display the number of steps found vs. the theoretical optimal solution
- Show performance timing information

To see the detailed solution path, uncomment the lines in `main.py` that print each step.

## Problem Variants
- **Classic Version**: Uses `MCState` class for direct left-to-right crossing
- **Island Version**: Uses `MCIslandState` class for three-location problem (left ↔ island ↔ right)
