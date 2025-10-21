import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['consecutive'] = (logs['num'] == logs['num'].shift(1)) & (logs['num'] == logs['num'].shift(2))
    return logs[logs['consecutive']][['num']].rename(columns={"num": "ConsecutiveNums"}).drop_duplicates()
    