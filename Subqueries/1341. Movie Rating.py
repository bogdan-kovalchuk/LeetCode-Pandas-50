import pandas as pd


def movie_rating(
    movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame
) -> pd.DataFrame:
    merged = movie_rating.merge(movies, on="movie_id", how="left")
    merged = merged.merge(users, on="user_id", how="left")

    user_counts = merged.groupby("name").size().reset_index(name="rating_count")
    top_user = user_counts.sort_values(
        by=["rating_count", "name"], ascending=[False, True]
    ).iloc[0]["name"]

    feb_ratings = merged[
        (merged["created_at"].dt.year == 2020) & (merged["created_at"].dt.month == 2)
    ]

    movie_avg = feb_ratings.groupby("title")["rating"].mean().reset_index()
    top_movie = movie_avg.sort_values(
        by=["rating", "title"], ascending=[False, True]
    ).iloc[0]["title"]

    return pd.DataFrame({"results": [top_user, top_movie]})
