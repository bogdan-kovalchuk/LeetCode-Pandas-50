import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers["num"].value_counts()
    singles = counts[counts == 1].index
    max_single = max(singles) if not singles.empty else None
    return pd.DataFrame({"num": [max_single]})
