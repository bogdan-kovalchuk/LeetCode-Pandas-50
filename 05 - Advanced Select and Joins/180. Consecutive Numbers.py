import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["consec3"] = (logs["num"] == logs["num"].shift(1)) & (logs["num"] == logs["num"].shift(2))
    result = logs[logs["consec3"]][["num"]].drop_duplicates().rename(columns={"num": "ConsecutiveNums"})
    return result