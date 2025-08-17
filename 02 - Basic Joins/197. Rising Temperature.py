import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by="recordDate")
    return weather[(weather["temperature"].diff() > 0) & (weather["recordDate"].diff().dt.days == 1)][["id"]]
