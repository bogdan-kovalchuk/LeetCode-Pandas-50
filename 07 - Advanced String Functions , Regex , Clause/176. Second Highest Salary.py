# TYPE YOUR CODE HERE
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sec_salary = None
    employee = employee.drop_duplicates(subset="salary")
    if employee.shape[0] >= 2:
        employee.sort_values(by="salary", ascending=False, inplace=True)
        sec_salary = employee["salary"].iloc[1]
    return pd.DataFrame({"SecondHighestSalary": [sec_salary]})
