import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    temp = seat.copy()
    seat.loc[::2, "student"] = temp["student"].shift(-1)
    seat.loc[1::2, "student"] = temp["student"].shift(1)
    if seat.shape[0] % 2 != 0:
        seat.iloc[-1] = temp.iloc[-1]
    return seat
