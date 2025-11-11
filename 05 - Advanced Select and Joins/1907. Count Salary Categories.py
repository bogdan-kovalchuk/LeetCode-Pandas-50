import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def categorize(income):
        if income < 20000:
            return "Low Salary"
        elif income <= 50000:
            return "Average Salary"
        else:
            return "High Salary"

    accounts["category"] = accounts["income"].map(categorize)
    count = accounts["category"].value_counts().rename_axis("category").reset_index(name="accounts_count")

    category_df = pd.DataFrame({"category": ["Low Salary", "Average Salary", "High Salary"]})

    return category_df.merge(count, on="category", how="left").fillna(0)
