import pandas as pd


def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    concat = pd.concat(
        [request_accepted["requester_id"], request_accepted["accepter_id"]]
    )
    return (
        concat.value_counts()
        .reset_index(name="num")
        .iloc[[0]]
        .rename(columns={"index": "id"})
    )
