import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    return pd.merge(employees, employee_uni, how="left")[["unique_id", "name"]]
