import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged = units_sold.merge(prices, on="product_id", how="left")
    merged = merged[(merged["purchase_date"] >= merged["start_date"]) & (merged["purchase_date"] <= merged["end_date"])]
    merged["revenue"] = merged["units"] * merged["price"]
    grouped = merged.groupby("product_id")[["revenue", "units"]].sum().reset_index()
    grouped["average_price"] = (grouped["revenue"] / grouped["units"]).round(2)
    all_units = prices[["product_id"]].drop_duplicates().merge(grouped, how="left")
    return all_units[["product_id", "average_price"]].fillna(0)
