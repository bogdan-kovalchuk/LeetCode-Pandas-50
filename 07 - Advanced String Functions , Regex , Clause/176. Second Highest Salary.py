import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    result = None
    employee = employee.drop_duplicates(subset="salary")
    if employee.shape[0] > 1:
        result = employee.sort_values(by="salary", ascending=False)["salary"].iloc[1]
    return pd.DataFrame({"SecondHighestSalary": [result]})
