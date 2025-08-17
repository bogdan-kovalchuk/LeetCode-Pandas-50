import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee, how="left")
    grouped = merged.groupby("project_id", as_index=False)["experience_years"].mean()
    grouped = grouped.round(2)
    return grouped.rename(columns={"experience_years": "average_years"})
