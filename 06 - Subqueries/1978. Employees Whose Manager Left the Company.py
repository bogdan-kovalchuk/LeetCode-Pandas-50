import pandas as pd


def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employees_less_30000 = employees[employees["salary"] < 30000].dropna()
    result = employees_less_30000[~employees_less_30000["manager_id"].isin(employees["employee_id"])]
    return result[["employee_id"]].sort_values(by="employee_id")
