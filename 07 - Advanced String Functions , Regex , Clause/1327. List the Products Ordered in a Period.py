import pandas as pd


def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders["order_date"].dt.year == 2020) & (orders["order_date"].dt.month == 2)]
    orders = orders.groupby("product_id")["unit"].sum().reset_index()
    orders = orders[orders["unit"] >= 100]
    return orders.merge(products, how="left", on="product_id")[["product_name", "unit"]]
