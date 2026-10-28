import pandas as pd
import numpy as np

def daily_returns(prices):
    """
    calculate daily returns from a series of prices,
    changes percent change on the prices,
    drops the first empty row in data
    
    """
    percentages = prices.pct_change()
    cleaned = percentages.dropna()

    return cleaned

def portfolio_returns(weights, returns):
    """
    calculate portfolio returns from a series of weights and returns,
    weights are the allocation of each asset in the portfolio,
    returns are the daily returns of each asset in the portfolio
    
    """
    weighted_returns = returns * weights 
    portfolio_returns = weighted_returns.sum(axis=1)

    return portfolio_returns

def annual_return(daily):
    """
    calculate annual return from daily returns,
    daily returns are the daily returns of the portfolio
    
    """
    mu = daily.mean()
    annual_returns = mu * 252

    return annual_returns

def annual_volatility(daily):
    """
    calculate annual volatility from daily returns,
    daily returns are the daily returns of the portfolio
    """
    sigma = daily.std()
    annual_volatility = sigma * np.sqrt(252)
    return annual_volatility

def sharpe(daily, risk_free=0):
    """
    calculate sharpe ratio from daily returns and risk free rate,
    daily returns are the daily returns of the portfolio,
    risk free rate is the risk free rate of return
    
    """
    sharpe_value = (annual_return(daily) - risk_free)/annual_volatility(daily)
    return sharpe_value

def max_drawdown(daily):

    """
    calculates how much would have lost if a stock was 
    bought at the worst possible moment
    """
    growth = (1 + daily).cumprod()
    highest = growth.cummax()

    drawdown = growth/highest - 1

    return drawdown.min()