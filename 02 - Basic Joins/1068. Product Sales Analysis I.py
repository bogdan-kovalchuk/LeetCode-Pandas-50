import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales.merge(product, how="left", on="product_id")[
        ["product_name", "year", "price"]
    ]
