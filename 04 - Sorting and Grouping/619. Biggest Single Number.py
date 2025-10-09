import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers["num"].value_counts().reset_index()
    counts.columns = ["num", "count"]
    single = counts[counts["count"] == 1]
    if single.empty:
        return pd.DataFrame({"num": [None]})
    return single.sort_values("num", ascending=False).head(1)[["num"]]
