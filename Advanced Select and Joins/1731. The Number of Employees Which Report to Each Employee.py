import pandas as pd
import numpy as np


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    reports_summary = employees.groupby("reports_to", as_index=False).agg(
        average_age=("age", "mean"), reports_count=("reports_to", "count")
    )
    reports_summary["average_age"] = np.floor(
        reports_summary["average_age"] + 0.5
    ).astype(int)
    reports_summary = reports_summary.rename(columns={"reports_to": "employee_id"})
    result = reports_summary.merge(employees, how="left")
    result = result[["employee_id", "name", "reports_count", "average_age"]]
    return result
