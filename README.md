# CS664 Artificial Intelligence — Boston University

Coursework from CS664 (Artificial Intelligence, Boston University Metropolitan College, Fall 2026), by Wei Zhao.
Course text: Russell & Norvig, *Artificial Intelligence: A Modern Approach* (4th ed.).

## Final project: Genetic Algorithm Portfolio Weights

**Can portfolio weights trained on old data survive the modern market?**

A genetic algorithm searches for Sharpe-maximizing weights across 7 ETFs (EEM, EFA, GLD, IWM, SPY, TLT, VNQ) using 2005–2019 data. The weights are then frozen and tested on 2020–2026 against an equal-weight portfolio and 100% SPY.

| | Training Sharpe (2005–2019) | Testing Sharpe (2020–2026) |
|---|---|---|
| GA portfolio | 1.051 | 0.558 |
| Equal weight | 0.587 | 0.646 |
| 100% SPY | 0.565 | 0.817 |

The GA ranked first in training and last in testing. Its 47% allocation to long-term Treasuries was hit hard when stocks and bonds fell together in 2022, although it still had the lowest volatility of the three. Each function is unit-tested, and the GA is checked against a brute-force search on a two-fund problem.

See [`final-project-ga-portfolio/`](final-project-ga-portfolio/) for the code, setup instructions and figures.

## Homework

| Folder | Topic |
|---|---|
| [`hw1-intelligent-agents`](hw1-intelligent-agents/) | Agents and environments |
| [`hw2-search-and-games`](hw2-search-and-games/) | Search problems and adversarial game search |
| [`hw3-constraint-satisfaction`](hw3-constraint-satisfaction/) | Constraint satisfaction problems |
| [`hw4-logic`](hw4-logic/) | Logic and knowledge bases (Python and Prolog) |
| [`hw5-neural-networks-and-mdp`](hw5-neural-networks-and-mdp/) | Neural networks (PyTorch) and Markov decision processes |
| [`hw6-natural-language-processing`](hw6-natural-language-processing/) | Text classification (NLTK) and document similarity (spaCy, TF-IDF) |

Helper modules in each folder (`*_helpers_*.py`) were provided with the assignments and adapted from the AIMA and Poole & Mackworth code.
