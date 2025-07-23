import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    g = courses.groupby("class", as_index=False)["student"].count()
    return g[g["student"] >= 5][["class"]]
    