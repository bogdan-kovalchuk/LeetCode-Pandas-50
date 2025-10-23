import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    product_idx = products[["product_id"]].drop_duplicates()
    products = products[products["change_date"] <= "2019-08-16"]
    products = products.sort_values(by="change_date", ascending=False)

    latest_prices = (
        products
        .drop_duplicates(subset="product_id", keep="first")
        [["product_id", "new_price"]]
    )

    result = (
        product_idx
        .merge(latest_prices, on="product_id", how="left")
        .fillna(10)
        .rename(columns={"new_price": "price"})
    )

    return result