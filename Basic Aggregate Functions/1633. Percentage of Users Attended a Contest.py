import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    num_users = users.shape[0]
    result = (
        register.groupby("contest_id")
        .size()
        .div(num_users)
        .mul(100)
        .reset_index(name="percentage")
        .sort_values(by=["percentage", "contest_id"], ascending=[False, True])
        .round(2)
    )
    return result
