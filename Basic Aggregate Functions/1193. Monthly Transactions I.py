import pandas as pd
import numpy as np


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["approved"] = np.where(transactions["state"] == "approved", transactions["amount"], np.nan)
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    return (
        transactions.groupby(["month", "country"], dropna=False)
        .agg(
            trans_count=("state", "count"),
            approved_count=("approved", "count"),
            trans_total_amount=("amount", "sum"),
            approved_total_amount=("approved", "sum"),
        )
        .reset_index()
    )
