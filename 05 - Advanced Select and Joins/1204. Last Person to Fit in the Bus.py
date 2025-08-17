import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values(by="turn")
    queue["cumsum"] = queue["weight"].cumsum()
    queue = queue[queue["cumsum"] <= 1000]
    return queue.iloc[[-1]][["person_name"]]
    