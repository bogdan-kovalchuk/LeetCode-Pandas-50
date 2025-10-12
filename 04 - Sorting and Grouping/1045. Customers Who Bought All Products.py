import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    n_products = product.size
    g = customer.groupby("customer_id")["product_key"].nunique().reset_index()
    return g[g["product_key"] == n_products][["customer_id"]]
