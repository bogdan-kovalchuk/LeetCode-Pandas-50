import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer["referee_id"].isnull()) | (customer["referee_id"] != 2)][
        ["name"]
    ]
