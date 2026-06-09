from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date

from .models import (
    RoleChoices,
    SubscriptionTypeChoices
)


# =========================
# USER
# =========================

class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    avatar: Optional[str]
    user_role: RoleChoices


class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    avatar: Optional[str]
    user_role: RoleChoices
    created_at: datetime


class UserLoginSchema(BaseModel):
    username: str
    password: str


# =========================
# GENRE
# =========================

class GenreInputSchema(BaseModel):
    name: str


class GenreOutSchema(BaseModel):
    id: int
    name: str


# =========================
# MOVIE
# =========================

class MovieInputSchema(BaseModel):
    title: str
    description: str
    release_date: date
    duration_minutes: int
    trailer_url: Optional[str]
    genre_id: int


class MovieOutSchema(BaseModel):
    id: int
    title: str
    description: str
    release_date: date
    duration_minutes: int
    trailer_url: Optional[str]
    genre_id: int


# =========================
# MOVIE IMAGE
# =========================

class MovieImageInputSchema(BaseModel):
    movie_id: int
    image: str


class MovieImageOutSchema(BaseModel):
    id: int
    movie_id: int
    image: str


# =========================
# SERIES
# =========================

class SeriesInputSchema(BaseModel):
    title: str
    description: str
    release_date: date
    genre_id: int


class SeriesOutSchema(BaseModel):
    id: int
    title: str
    description: str
    release_date: date
    genre_id: int


# =========================
# EPISODE
# =========================

class EpisodeInputSchema(BaseModel):
    series_id: int
    episode_number: int
    title: str
    duration_minutes: int
    video_url: str


class EpisodeOutSchema(BaseModel):
    id: int
    series_id: int
    episode_number: int
    title: str
    duration_minutes: int
    video_url: str


# =========================
# REVIEW
# =========================

class ReviewInputSchema(BaseModel):
    user_id: int
    movie_id: int
    rating: int
    comment: str


class ReviewOutSchema(BaseModel):
    id: int
    user_id: int
    movie_id: int
    rating: int
    comment: str
    created_at: datetime


# =========================
# SUBSCRIPTION PLAN
# =========================

class SubscriptionPlanInputSchema(BaseModel):
    name: SubscriptionTypeChoices
    price: int
    max_devices: int
    video_quality: str


class SubscriptionPlanOutSchema(BaseModel):
    id: int
    name: SubscriptionTypeChoices
    price: int
    max_devices: int
    video_quality: str


# =========================
# USER SUBSCRIPTION
# =========================

class UserSubscriptionInputSchema(BaseModel):
    user_id: int
    plan_id: int
    start_date: date
    end_date: date


class UserSubscriptionOutSchema(BaseModel):
    id: int
    user_id: int
    plan_id: int
    start_date: date
    end_date: date
    created_at: datetime


# =========================
# FAVORITE
# =========================

class FavoriteInputSchema(BaseModel):
    user_id: int
    movie_id: int


class FavoriteOutSchema(BaseModel):
    id: int
    user_id: int
    movie_id: int


# =========================
# WATCH HISTORY
# =========================

class WatchHistoryInputSchema(BaseModel):
    user_id: int
    movie_id: int
    watched_minutes: int


class WatchHistoryOutSchema(BaseModel):
    id: int
    user_id: int
    movie_id: int
    watched_minutes: int
    watched_at: datetime


# =========================
# REFRESH TOKEN
# =========================

class RefreshTokenInputSchema(BaseModel):
    user_id: int
    token: str


class RefreshTokenOutSchema(BaseModel):
    id: int
    user_id: int
    token: str
    created_at: datetime