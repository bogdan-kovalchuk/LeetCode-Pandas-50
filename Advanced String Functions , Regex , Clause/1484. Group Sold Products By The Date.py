import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return (
        activities.groupby("sell_date")["product"]
        .agg(
            num_sold=lambda s: s.nunique(), products=lambda s: ",".join(sorted(set(s)))
        )
        .reset_index()
        .sort_values(by="sell_date")
    )
