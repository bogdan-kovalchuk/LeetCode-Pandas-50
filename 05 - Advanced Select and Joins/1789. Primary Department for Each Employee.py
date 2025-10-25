import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee["entry_count"] = employee.groupby("employee_id")["employee_id"].transform("count")
    return employee[(employee["primary_flag"] == "Y") | (employee["entry_count"] == 1)][
        ["employee_id", "department_id"]
    ]
