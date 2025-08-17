import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    single_dep = employee.groupby("employee_id").filter(lambda x: len(x) == 1)
    primary_dep = employee[employee["primary_flag"] == "Y"]
    return pd.concat([single_dep, primary_dep])[["employee_id", "department_id"]]
