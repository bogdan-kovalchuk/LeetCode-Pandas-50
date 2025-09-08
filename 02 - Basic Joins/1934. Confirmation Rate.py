import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    merged = signups.merge(confirmations, on="user_id", how="left")
    merged["confirmation_rate"] = (merged["action"] == "confirmed").astype(int)
    return (
        merged.groupby("user_id", as_index=False)["confirmation_rate"]
        .mean()
        .round(2)
    )
