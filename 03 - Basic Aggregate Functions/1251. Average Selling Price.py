import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged = prices.merge(units_sold, on="product_id")
    merged = merged[(merged["purchase_date"] >= merged["start_date"]) & (merged["purchase_date"] <= merged["end_date"])]

    merged["revenue"] = merged["units"] * merged["price"]
    grouped = (
        merged.groupby("product_id").agg(total_revenue=("revenue", "sum"), total_units=("units", "sum")).reset_index()
    )

    grouped["average_price"] = (grouped["total_revenue"] / grouped["total_units"]).round(2)
    result = grouped[["product_id", "average_price"]]

    all_products = pd.DataFrame({"product_id": prices["product_id"].unique()})
    final = all_products.merge(result, on="product_id", how="left")
    final["average_price"] = final["average_price"].fillna(0)

    return final
