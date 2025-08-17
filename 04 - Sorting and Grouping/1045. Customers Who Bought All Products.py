import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    valid_products = product["product_key"]

    result = (
        customer.groupby("customer_id")["product_key"]
        .apply(lambda g: valid_products.isin(g).all())
        .reset_index(name="all_valid")
    )

    return result[result["all_valid"]][["customer_id"]]
