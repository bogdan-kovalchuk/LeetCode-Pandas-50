import pandas as pd
from datetime import timedelta


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    num_unique_players = activity["player_id"].nunique()
    g = activity.groupby("player_id", as_index=False)["event_date"].min()
    g["event_date"] = g["event_date"] + timedelta(days=1)
    m = g.merge(activity, how="left", on=["player_id", "event_date"])[
        "games_played"
    ].dropna()
    return pd.DataFrame({"fraction": [round(m.index.size / num_unique_players, 2)]})
