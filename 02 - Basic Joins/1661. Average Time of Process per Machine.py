import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    pivot = activity.pivot_table(
        index=["machine_id", "process_id"], columns="activity_type", values="timestamp"
    ).reset_index()
    pivot["processing_time"] = pivot["end"] - pivot["start"]
    return pivot.groupby("machine_id", as_index=False).mean()[["machine_id", "processing_time"]].round(3)
