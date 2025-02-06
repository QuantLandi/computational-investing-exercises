# Futures Price Analysis

This repository contains a Python script for analyzing historical price data of futures contracts using `yfinance`. The script performs various calculations such as cumulative returns, rolling mean returns, volatility, and drawdowns, and visualizes the results using `matplotlib`.

## Features
- **Download historical price data** using `yfinance`.
- **Calculate daily and annual returns**.
- **Compute cumulative returns**.
- **Analyze rolling mean returns** over different time periods (1, 3, 5, and 10 years).
- **Measure annual volatility and downside risk**.
- **Visualize key metrics** including:
  - Cumulative returns
  - Rolling mean returns
  - Rolling volatility
  - Drawdowns

## Installation
Ensure you have Python installed along with the necessary dependencies. You can install them using:

```bash
pip install yfinance matplotlib numpy pandas
```

## Outputs
The script generates multiple plots including:
1. **Price Chart** – Historical closing prices of the futures contract.
2. **Cumulative Returns** – Growth of $1 invested over time.
3. **Rolling Mean Returns** – Moving average of annualized returns.
4. **Rolling Volatility** – Annualized standard deviation of returns.
5. **Drawdowns** – Maximum percentage decline from peak value.

## Example
The script fetches data for `ES=F` (E-mini S&P 500 Futures) and computes:

- **Annual Return:** Displayed as a percentage.
- **Annual Volatility:** A measure of risk.
- **Downside Volatility:** Only considering negative returns.
- **Rolling Volatility:** 1-year standard deviation over time.
- **Drawdowns:** Percentage decline from historical peaks.
