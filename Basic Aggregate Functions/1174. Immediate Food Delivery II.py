import pandas as pd


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    gb = delivery.sort_values("order_date").groupby("customer_id").first().reset_index()
    gb["immediate"] = gb["order_date"] == gb["customer_pref_delivery_date"]
    return pd.DataFrame(
        {"immediate_percentage": [round(gb["immediate"].mean() * 100, 2)]}
    )
