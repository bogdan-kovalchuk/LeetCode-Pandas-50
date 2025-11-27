import pandas as pd


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(
        department,
        how="left",
        left_on="departmentId",
        right_on="id",
        suffixes=("_emp", "_dep"),
    )

    employee = employee.rename(
        columns={
            "id_emp": "id",
            "name_emp": "Employee",
            "salary": "Salary",
            "name_dep": "Department",
        }
    )

    res = (
        employee.groupby("Department")["Salary"]
        .apply(lambda s: s.sort_values(ascending=False).unique()[:3])
        .explode()
        .reset_index(name="Salary")
    )

    return res.merge(employee, how="left")[["Department", "Employee", "Salary"]]
