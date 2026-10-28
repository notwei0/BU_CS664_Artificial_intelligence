# CS664 Final Project — GA Fund Allocator Simulator

Seed: **6449**
Folder: `C:\git\cs664\CS664_Final_Project_Zhao_Wei`

Wei Zhao
CS664

This project uses a genetic algorithm (GA) to optimize portfolio weights across seven exchange-traded funds (ETFs) and compare the result to common benchmark strategies.

The model is trained on historical data from 2005-2019 and then evaluated on a later test window from 2020-2026. The core question is whether a GA-optimized portfolio using data from 2005-2019 can outperform simpler alternatives such as:

- Equal-weight allocation across all 7 funds
- 100% allocation to SPY (S&P 500)

---

## Project overview

The project uses daily adjusted closing prices for seven ETFs:

- EEM
- EFA
- GLD
- IWM
- SPY
- TLT
- VNQ

The GA searches for portfolio weights that maximize the Sharpe ratio. The optimized portfolio is then compared with baseline strategies using annual return, annual volatility, Sharpe ratio, and maximum drawdown.

---

## Step 1 — Setup

### 1.1 Create the virtual environment

```bash
python -m venv .venv
```

Then activate it:

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 1.2 Install project dependencies

```bash
pip install -r requirements.txt
```

### 1.3 Open the notebooks in VS Code

For every notebook in this project:

1. Open the notebook in VS Code.
2. Select the `.venv` kernel in the top-right corner.
3. Click `Restart`.
4. Click `Run All`.

This ensures all code runs in the same environment as the installed dependencies.

---

## Step 2 — Data and model setup

### 2.1 Download data

Open `get_data.ipynb` and run it in the `.venv` kernel.

This downloads the seven ETF datasets from Yahoo Finance and saves the daily adjusted close prices to:

- `data/data.csv`

### 2.2 Train the GA

Open `run_ga.ipynb` and run all cells.

This trains the genetic algorithm using the 2005-2019 period and saves the optimized weights to:

- `data/weights.csv`

### 2.3 Evaluate the strategy

Open `evaluate.ipynb` and run all cells.

This compares the GA portfolio to equal-weight and SPY-only portfolios on the 2020-2026 test period.

---

## Files in this project

- `get_data.ipynb` — downloads ETF price data and saves it to `data/data.csv`
- `project_helpers_metrics.py` — portfolio math and performance metrics
- `project_helpers_ga.py` — genetic algorithm logic
- `run_ga.ipynb` — trains the GA on the 2005-2019 period
- `evaluate.ipynb` — evaluates the GA portfolio against benchmarks
- `verification_tests.ipynb` — tests helper functions and checks the GA with a brute-force comparison
- `LLM.ipynb` — uses a local LLM via Ollama to summarize results
- `data/data.csv` — full price dataset
- `data/weights.csv` — optimized GA weights
- `data/results.csv` — result table for each strategy
- `figures/ga_fitness_history.png` — GA fitness across generations
- `figures/growth_test_period.png` — portfolio growth during the test period
- `figures/ga_weights.png` — optimized allocation visualization
- `requirements.txt` — project dependencies

---

## Metrics used

The project evaluates each strategy using:

- Annual return
- Annual volatility
- Sharpe ratio
- Maximum drawdown
- Seed(6449)

These are computed using the functions in `project_helpers_metrics.py`.

---

## LLM setup

To use the local LLM notebook, install Ollama from https://ollama.com.

Then run:

```bash
ollama pull llama3.2
```

---

## Notes

- The GA is designed to maximize Sharpe ratio rather than raw return alone.
- Weights are constrained to be non-negative and sum to 1.
- The project is a portfolio optimization experiment and is intended for academic or research-style analysis rather than financial advice.
- Seed(6449) was used for reproducability.

CS664 course project BU MET, Prof. Kalathur

AI generated README, was looked over and checked for accuracy