import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee, how="left", on="employee_id")
    return (
        merged.groupby("project_id")["experience_years"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"experience_years": "average_years"})
    )
