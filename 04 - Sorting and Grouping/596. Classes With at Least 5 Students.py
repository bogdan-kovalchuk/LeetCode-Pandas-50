import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    g = courses.groupby("class").size()
    g = g[g >= 5]
    return g.reset_index()[["class"]]
