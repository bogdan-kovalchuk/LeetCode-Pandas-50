import pandas as pd

round2 = lambda x: round(x + 1e-9, 2)


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["quality"] = queries.rating / queries.position
    queries["poor_query_percentage"] = (queries.rating < 3) * 100
    result = queries.groupby("query_name")[["quality", "poor_query_percentage"]].mean()
    return result.apply(round2).reset_index()
