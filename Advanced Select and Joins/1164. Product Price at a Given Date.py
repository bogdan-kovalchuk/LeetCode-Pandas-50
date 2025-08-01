import pandas as pd
from datetime import datetime

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    valid_prices = (
        products[products["change_date"] <= datetime(2019, 8, 16)]
        .sort_values("change_date")
        .groupby("product_id", as_index=False)["new_price"]
        .last()
    )

    result = (
        products[["product_id"]]
        .drop_duplicates()
        .merge(valid_prices, on="product_id", how="left")
        .fillna({"new_price": 10})
        .rename(columns={"new_price": "price"})
    )

    return result