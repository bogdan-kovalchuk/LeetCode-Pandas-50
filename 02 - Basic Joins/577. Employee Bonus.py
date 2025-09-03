import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(bonus, how="left", on="empId")
    print(merged)
    return merged[(merged["bonus"].isna()) | (merged["bonus"] < 1000)][["name", "bonus"]]
