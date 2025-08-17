import pandas as pd
from datetime import datetime, timedelta


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    end_day = datetime(2019, 7, 27)
    start_day = end_day - timedelta(days=30)
    activity = activity[
        (activity["activity_date"] > start_day) & (activity["activity_date"] <= end_day)
    ]
    activity = activity.rename(columns={"activity_date": "day"})
    return activity.groupby("day", as_index=False).agg(
        active_users=("user_id", "nunique")
    )
