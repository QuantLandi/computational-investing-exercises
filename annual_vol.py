# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:56:43 2024

@author: User
"""

import pandas as pd
import numpy as np
import yfinance as yf


sp500 = yf.download("ES=F")
# print(f"sp500 {sp500}")

prices = sp500["Adj Close"]
sp500["log_returns"] = np.log(prices).diff()
annual_vol = sp500["log_returns"].std() * np.sqrt(252)

print()
print(f"annualized volatility: {annual_vol}")