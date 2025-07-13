import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    mask = (cinema["id"] % 2 != 0) & (cinema["description"] != "boring")
    return cinema[mask].sort_values("rating", ascending=False)
