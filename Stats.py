import pandas as pd
import numpy as np

tickers = ["SPY", "AGG", "F", "GM", "UBER",
           "TSLA", "GOOG", "SNAP", "VOW3.DE", "EXSA.DE", 
           "MA", "MCD", "BNP.PA", "MBG.DE", "EURUSD=X", "GD=F"]

# Write a function for getting descriptive statistics dataframe
def get_stats(f):
    # Read csv file
    df = pd.read_csv(f)

    # .describe() function will give max, min, mean automatically 
    desc_stats = df.describe().T

    # Compute Total Return
    first_value = df.fillna(method='bfill', axis=0).iloc[0, :][1:]
    last_value = df.fillna(method='ffill', axis=0).iloc[-1, :][1:]
    returns = (last_value - first_value)/first_value

    # Add returns to the dataframe
    desc_stats["Total Return"] = returns

    return desc_stats


