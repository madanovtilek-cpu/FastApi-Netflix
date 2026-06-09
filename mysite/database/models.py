from .db import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    Integer,
    String,
    Text,
    ForeignKey,
    Date,
    DateTime,
    Enum
)

from typing import List, Optional
from enum import Enum as PyEnum
from datetime import datetime, date


# =========================
# ENUMS
# =========================

class RoleChoices(str, PyEnum):
    user = "user"
    admin = "admin"


class SubscriptionTypeChoices(str, PyEnum):
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


# =========================
# USERS
# =========================

class UserProfile(Base):
    __tablename__ = "user_profile"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    password: Mapped[str] = mapped_column(String)

    avatar: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True
    )

    user_role: Mapped[RoleChoices] = mapped_column(
        Enum(RoleChoices, create_constraint=False),
        default=RoleChoices.user
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    reviews: Mapped[List["Review"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    subscriptions: Mapped[List["UserSubscription"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    watch_history: Mapped[List["WatchHistory"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    tokens: Mapped[List["RefreshToken"]] = relationship(
        back_populates="token_user",
        cascade="all, delete-orphan"
    )


# =========================
# GENRES
# =========================

class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    movies: Mapped[List["Movie"]] = relationship(
        back_populates="genre"
    )

    series: Mapped[List["Series"]] = relationship(
        back_populates="genre"
    )


# =========================
# MOVIES
# =========================

class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(200)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    release_date: Mapped[date] = mapped_column(
        Date
    )

    duration_minutes: Mapped[int] = mapped_column(
        Integer
    )

    trailer_url: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True
    )

    genre_id: Mapped[int] = mapped_column(
        ForeignKey("genre.id")
    )

    genre: Mapped["Genre"] = relationship(
        back_populates="movies"
    )

    images: Mapped[List["MovieImage"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan"
    )

    reviews: Mapped[List["Review"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan"
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan"
    )

    watch_history: Mapped[List["WatchHistory"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan"
    )


# =========================
# MOVIE IMAGES
# =========================

class MovieImage(Base):
    __tablename__ = "movie_image"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id")
    )

    image: Mapped[str] = mapped_column(String)

    movie: Mapped["Movie"] = relationship(
        back_populates="images"
    )


# =========================
# SERIES
# =========================

class Series(Base):
    __tablename__ = "series"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(200)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    release_date: Mapped[date] = mapped_column(
        Date
    )

    genre_id: Mapped[int] = mapped_column(
        ForeignKey("genre.id")
    )

    genre: Mapped["Genre"] = relationship(
        back_populates="series"
    )

    episodes: Mapped[List["Episode"]] = relationship(
        back_populates="series",
        cascade="all, delete-orphan"
    )


# =========================
# EPISODES
# =========================

class Episode(Base):
    __tablename__ = "episode"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    series_id: Mapped[int] = mapped_column(
        ForeignKey("series.id")
    )

    episode_number: Mapped[int] = mapped_column(
        Integer
    )

    title: Mapped[str] = mapped_column(
        String(200)
    )

    duration_minutes: Mapped[int] = mapped_column(
        Integer
    )

    video_url: Mapped[str] = mapped_column(
        String
    )

    series: Mapped["Series"] = relationship(
        back_populates="episodes"
    )


# =========================
# REVIEWS
# =========================

class Review(Base):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_profile.id")
    )

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id")
    )

    rating: Mapped[int] = mapped_column(
        Integer
    )

    comment: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user: Mapped["UserProfile"] = relationship(
        back_populates="reviews"
    )

    movie: Mapped["Movie"] = relationship(
        back_populates="reviews"
    )


# =========================
# SUBSCRIPTIONS
# =========================

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plan"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[SubscriptionTypeChoices] = mapped_column(
        Enum(
            SubscriptionTypeChoices,
            create_constraint=False
        )
    )

    price: Mapped[int] = mapped_column(
        Integer
    )

    max_devices: Mapped[int] = mapped_column(
        Integer
    )

    video_quality: Mapped[str] = mapped_column(
        String(50)
    )

    subscriptions: Mapped[List["UserSubscription"]] = relationship(
        back_populates="plan"
    )


class UserSubscription(Base):
    __tablename__ = "user_subscription"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_profile.id")
    )

    plan_id: Mapped[int] = mapped_column(
        ForeignKey("subscription_plan.id")
    )

    start_date: Mapped[date] = mapped_column(
        Date
    )

    end_date: Mapped[date] = mapped_column(
        Date
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user: Mapped["UserProfile"] = relationship(
        back_populates="subscriptions"
    )

    plan: Mapped["SubscriptionPlan"] = relationship(
        back_populates="subscriptions"
    )


# =========================
# FAVORITES
# =========================

class Favorite(Base):
    __tablename__ = "favorite"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_profile.id")
    )

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id")
    )

    user: Mapped["UserProfile"] = relationship(
        back_populates="favorites"
    )

    movie: Mapped["Movie"] = relationship(
        back_populates="favorites"
    )


# =========================
# WATCH HISTORY
# =========================

class WatchHistory(Base):
    __tablename__ = "watch_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_profile.id")
    )

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id")
    )

    watched_minutes: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    watched_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user: Mapped["UserProfile"] = relationship(
        back_populates="watch_history"
    )

    movie: Mapped["Movie"] = relationship(
        back_populates="watch_history"
    )


# =========================
# REFRESH TOKENS
# =========================

class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_profile.id")
    )

    token: Mapped[str] = mapped_column(
        String
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    token_user: Mapped["UserProfile"] = relationship(
        back_populates="tokens"
    )