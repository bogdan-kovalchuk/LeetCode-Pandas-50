import pandas as pd
import numpy as np


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery = delivery.sort_values(by="order_date")
    delivery = delivery.drop_duplicates("customer_id")
    delivery["order_type"] = np.where(delivery["order_date"] == delivery["customer_pref_delivery_date"], 1, 0)
    return pd.DataFrame({"immediate_percentage": [np.round(100 * delivery["order_type"].mean(), 2)]})
