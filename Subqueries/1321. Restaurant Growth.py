import pandas as pd


def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    result = customer.groupby("visited_on")["amount"].sum()
    result = result.rolling(window=7).sum().dropna().reset_index()
    result["average_amount"] = (result["amount"] / 7).round(2)
    return result
