import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    usr = (
        movie_rating.groupby("user_id")["movie_id"]
        .size()
        .reset_index(name="cnt")
        .merge(users, on="user_id", how="left")
        .sort_values(["cnt", "name"], ascending=[False, True])
    )
    best_user = usr["name"].iloc[0]

    feb_2020 = movie_rating[(movie_rating["created_at"].dt.year == 2020) & (movie_rating["created_at"].dt.month == 2)]

    movie = (
        feb_2020.groupby("movie_id")["rating"]
        .mean()
        .reset_index()
        .merge(movies, on="movie_id", how="left")
        .sort_values(["rating", "title"], ascending=[False, True])
    )
    best_movie = movie["title"].iloc[0]

    return pd.DataFrame({"results": [best_user, best_movie]})
