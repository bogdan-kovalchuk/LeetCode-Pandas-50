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

    result = accounts["category"].value_counts().to_dict()

    all_categories = ["Low Salary", "Average Salary", "High Salary"]
    output = pd.DataFrame(
        {
            "category": all_categories,
            "accounts_count": [result.get(cat, 0) for cat in all_categories],
        }
    )

    return output
