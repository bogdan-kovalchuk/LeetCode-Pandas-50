import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    temp = seat["student"].copy()

    seat.loc[::2, "student"] = temp.shift(-1)[::2]
    seat.loc[1::2, "student"] = temp.shift(1)[1::2]

    if seat.shape[0] % 2 != 0:
        seat.loc[seat.index[-1], "student"] = temp.iloc[-1]

    return seat
