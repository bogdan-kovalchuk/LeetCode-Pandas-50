import pandas as pd


def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values(by="turn")
    queue["cumsum"] = queue["weight"].cumsum()
    person_name = queue[queue["cumsum"] <= 1000].tail(1)["person_name"]
    return pd.DataFrame({"person_name": person_name})
