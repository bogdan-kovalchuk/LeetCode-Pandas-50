import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby("managerId").size().reset_index(name="count")
    managers = managers[managers["count"] >= 5]["managerId"]
    return employee[employee["id"].isin(managers)][["name"]]
