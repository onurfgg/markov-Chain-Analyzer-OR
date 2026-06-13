# 🎲 Markov Chain Analyzer for Operations Research

This repository provides a Python-based stochastic operations research tool to analyze and simulate Markov Chains. It allows users to calculate steady-state (long-run) probabilities and simulate discrete-time state transitions using a given probability transition matrix.

## 🚀 Features
* **Matrix Validation:** Automatically verifies if the input matrix is a valid stochastic matrix (rows sum to 1).
* **Steady-State Calculation:** Solves linear equations to find the long-run probabilities of the system.
* **Step-by-Step Simulation:** Simulates the system's probabilities over $n$ steps given an initial state.

## 🧮 Mathematical Background

Let $P$ be the transition matrix of a Markov chain. The steady-state probability vector $\pi$ satisfies the following equation:
$$\pi P = \pi$$

To find a unique solution, the sum of all probabilities must equal 1:
$$\sum_{i} \pi_i = 1$$

The algorithm in this repository solves this system of linear equations using NumPy's least-squares approximation.

## 🛠️ Installation

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/onurfgg/Markov-Chain-Analyzer-OR.git](https://github.com/onurfgg/Markov-Chain-Analyzer-OR.git)
cd Markov-Chain-Analyzer-OR
pip install numpy
