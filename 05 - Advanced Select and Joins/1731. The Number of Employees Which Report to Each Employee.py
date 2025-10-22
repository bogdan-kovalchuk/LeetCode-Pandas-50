import pandas as pd
import math


def round_half_up(n: float) -> int:
    return math.floor(n + 0.5)


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    gb = (
        employees.groupby("reports_to")
        .agg(reports_count=("employee_id", "nunique"), average_age=("age", lambda x: round_half_up(x.mean())))
        .reset_index()
        .rename(columns={"reports_to": "employee_id"})
    )
    gb = gb.merge(employees[["employee_id", "name"]], on="employee_id", how="left")
    return gb[["employee_id", "name", "reports_count", "average_age"]]
