import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    temp = seat["student"].copy()

    seat.loc[seat.index % 2 == 0, "student"] = temp.shift(-1)[seat.index % 2 == 0]
    seat.loc[seat.index % 2 == 1, "student"] = temp.shift(1)[seat.index % 2 == 1]

    return seat.sort_values("id")
