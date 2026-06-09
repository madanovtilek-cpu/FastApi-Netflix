from sqladmin import ModelView
from mysite.database.models import (
    UserProfile,
    Genre,
    Movie,
    MovieImage,
    Series,
    Episode,
    Review,
    SubscriptionPlan,
    UserSubscription,
    Favorite,
    WatchHistory,
    RefreshToken,
)


class UserProfileAdmin(ModelView, model=UserProfile):
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-users"

    column_list = [
        UserProfile.id,
        UserProfile.username,
        UserProfile.email,
        UserProfile.first_name,
        UserProfile.last_name,
        UserProfile.user_role,
        UserProfile.created_at,
    ]
    column_searchable_list = [UserProfile.username, UserProfile.email]
    column_sortable_list = [UserProfile.id, UserProfile.username, UserProfile.created_at]
    column_details_exclude_list = [UserProfile.password]
    form_excluded_columns = [UserProfile.password]


class GenreAdmin(ModelView, model=Genre):
    name = "Genre"
    name_plural = "Genres"
    icon = "fa-solid fa-tags"

    column_list = [Genre.id, Genre.name]
    column_searchable_list = [Genre.name]
    column_sortable_list = [Genre.id, Genre.name]


class MovieAdmin(ModelView, model=Movie):
    name = "Movie"
    name_plural = "Movies"
    icon = "fa-solid fa-film"

    column_list = [
        Movie.id,
        Movie.title,
        Movie.genre_id,
        Movie.release_date,
        Movie.duration_minutes,
    ]
    column_searchable_list = [Movie.title]
    column_sortable_list = [Movie.id, Movie.title, Movie.release_date, Movie.duration_minutes]


class MovieImageAdmin(ModelView, model=MovieImage):
    name = "Movie Image"
    name_plural = "Movie Images"
    icon = "fa-solid fa-image"

    column_list = [MovieImage.id, MovieImage.movie_id, MovieImage.image]


class SeriesAdmin(ModelView, model=Series):
    name = "Series"
    name_plural = "Series"
    icon = "fa-solid fa-tv"

    column_list = [
        Series.id,
        Series.title,
        Series.genre_id,
        Series.release_date,
    ]
    column_searchable_list = [Series.title]
    column_sortable_list = [Series.id, Series.title, Series.release_date]


class EpisodeAdmin(ModelView, model=Episode):
    name = "Episode"
    name_plural = "Episodes"
    icon = "fa-solid fa-clapperboard"

    column_list = [
        Episode.id,
        Episode.series_id,
        Episode.episode_number,
        Episode.title,
        Episode.duration_minutes,
    ]
    column_searchable_list = [Episode.title]
    column_sortable_list = [Episode.id, Episode.episode_number, Episode.duration_minutes]


class ReviewAdmin(ModelView, model=Review):
    name = "Review"
    name_plural = "Reviews"
    icon = "fa-solid fa-star"

    column_list = [
        Review.id,
        Review.user_id,
        Review.movie_id,
        Review.rating,
        Review.created_at,
    ]
    column_sortable_list = [Review.id, Review.rating, Review.created_at]


class SubscriptionPlanAdmin(ModelView, model=SubscriptionPlan):
    name = "Subscription Plan"
    name_plural = "Subscription Plans"
    icon = "fa-solid fa-credit-card"

    column_list = [
        SubscriptionPlan.id,
        SubscriptionPlan.name,
        SubscriptionPlan.price,
        SubscriptionPlan.max_devices,
        SubscriptionPlan.video_quality,
    ]
    column_searchable_list = [SubscriptionPlan.name]
    column_sortable_list = [SubscriptionPlan.id, SubscriptionPlan.name, SubscriptionPlan.price]


class UserSubscriptionAdmin(ModelView, model=UserSubscription):
    name = "User Subscription"
    name_plural = "User Subscriptions"
    icon = "fa-solid fa-id-card"

    column_list = [
        UserSubscription.id,
        UserSubscription.user_id,
        UserSubscription.plan_id,
        UserSubscription.start_date,
        UserSubscription.end_date,
        UserSubscription.created_at,
    ]
    column_sortable_list = [
        UserSubscription.id,
        UserSubscription.start_date,
        UserSubscription.end_date,
        UserSubscription.created_at,
    ]


class FavoriteAdmin(ModelView, model=Favorite):
    name = "Favorite"
    name_plural = "Favorites"
    icon = "fa-solid fa-heart"

    column_list = [Favorite.id, Favorite.user_id, Favorite.movie_id]
    column_sortable_list = [Favorite.id, Favorite.user_id, Favorite.movie_id]


class WatchHistoryAdmin(ModelView, model=WatchHistory):
    name = "Watch History"
    name_plural = "Watch History"
    icon = "fa-solid fa-clock-rotate-left"

    column_list = [
        WatchHistory.id,
        WatchHistory.user_id,
        WatchHistory.movie_id,
        WatchHistory.watched_minutes,
        WatchHistory.watched_at,
    ]
    column_sortable_list = [WatchHistory.id, WatchHistory.watched_minutes, WatchHistory.watched_at]


class RefreshTokenAdmin(ModelView, model=RefreshToken):
    name = "Refresh Token"
    name_plural = "Refresh Tokens"
    icon = "fa-solid fa-key"

    column_list = [RefreshToken.id, RefreshToken.user_id, RefreshToken.created_at]
    column_sortable_list = [RefreshToken.id, RefreshToken.created_at]
