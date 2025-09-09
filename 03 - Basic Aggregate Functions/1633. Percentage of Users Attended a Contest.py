import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    g = register.groupby("contest_id")["user_id"].nunique().reset_index(name="unique_users")

    g["percentage"] = (100 * g["unique_users"] / users["user_id"].nunique()).round(2)

    return g[["contest_id", "percentage"]].sort_values(by=["percentage", "contest_id"], ascending=[False, True])
