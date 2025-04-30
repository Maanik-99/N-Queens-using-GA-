# 🧬 N-Queens Problem Solved Using Genetic Algorithm

This project implements a Genetic Algorithm (GA) to solve the classic **N-Queens problem** — placing N queens on an N×N chessboard so that no two queens attack each other.

## 📌 Problem Statement

Given an integer N, place N queens on an N×N chessboard such that:

- No two queens are in the same row,
- No two queens are in the same column,
- No two queens are in the same diagonal.

## 🚀 Genetic Algorithm Approach

The Genetic Algorithm mimics natural evolution. Here's how it's applied to the N-Queens problem:

- **Chromosome Representation**: A permutation of numbers from 0 to N-1 (each index is a column, value is the row).
- **Fitness Function**: Number of diagonal conflicts (lower is better).
- **Selection**: Tournament Selection.
- **Crossover**: Ordered Crossover (OX).
- **Mutation**: Swap Mutation.
- **Elitism**: Top individuals are carried over to the next generation.

## 🛠️ Features

- Configurable board size (N)
- Adjustable population size, mutation rate, and max generations
- Logs best solution and generation
- Prints number of diagonal conflicts

## 📄 Sample Output

![image](https://github.com/user-attachments/assets/202d3434-4f58-4255-918e-0b892efb19f8)
## Run the script:
- **python nqueens_ga.py**
### 📘 References
- **Goldberg, D.E. "Genetic Algorithms in Search, Optimization and Machine Learning"**

- **Holland, J.H. "Adaptation in Natural and Artificial Systems"**
