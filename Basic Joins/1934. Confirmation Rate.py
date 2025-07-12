import pandas as pd


def confirmation_rate(
    signups: pd.DataFrame, confirmations: pd.DataFrame
) -> pd.DataFrame:
    confirmations = signups[["user_id"]].merge(confirmations, how="left")
    confirmations["confirmation_rate"] = confirmations["action"] == "confirmed"
    confirmations["confirmation_rate"] = confirmations["confirmation_rate"].replace(
        {False: 0, True: 1}
    )
    return (
        confirmations.groupby("user_id")["confirmation_rate"]
        .mean()
        .reset_index()
        .round(2)
    )
