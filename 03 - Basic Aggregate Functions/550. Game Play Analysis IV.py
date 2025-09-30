import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first_day"] = activity.groupby("player_id")["event_date"].transform(min)
    second_day = activity[activity["first_day"] + pd.DateOffset(1) == activity["event_date"]]
    return pd.DataFrame({"fraction": [round(len(second_day) / activity.player_id.nunique(), 2)]})