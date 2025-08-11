import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    coords = insurance.drop_duplicates(subset=["lat", "lon"], keep=False).pid
    tiv = insurance.loc[insurance.duplicated(subset="tiv_2015", keep=False)].pid
    df = insurance.loc[insurance.pid.isin(coords) & insurance.pid.isin(tiv)]
    return df[["tiv_2016"]].sum().to_frame("tiv_2016").round(2)
