import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    condition = (
        (triangle["x"] + triangle["y"] > triangle["z"]) &
        (triangle["x"] + triangle["z"] > triangle["y"]) &
        (triangle["y"] + triangle["z"] > triangle["x"])
    )
    triangle["triangle"] = condition.map({True: "Yes", False: "No"})
    return triangle