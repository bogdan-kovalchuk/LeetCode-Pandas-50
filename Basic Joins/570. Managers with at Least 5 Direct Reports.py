import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee["managerId"].value_counts().reset_index()
    managers = managers[managers["count"] >= 5]["managerId"]
    return employee[employee["id"].isin(managers)][["name"]]
