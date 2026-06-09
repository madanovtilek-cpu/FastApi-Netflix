from fastapi import FastAPI
import uvicorn

from mysite.database.db import Base, engine
from mysite.database.models import *
from mysite.admin.setup import create_admin
from mysite.admin.views import (
    UserProfileAdmin,
    GenreAdmin,
    MovieAdmin,
    MovieImageAdmin,
    SeriesAdmin,
    EpisodeAdmin,
    ReviewAdmin,
    SubscriptionPlanAdmin,
    UserSubscriptionAdmin,
    FavoriteAdmin,
    WatchHistoryAdmin,
    RefreshTokenAdmin,
)

from mysite.api.auth import auth_router
from mysite.api.user import router as user_router
from mysite.api.genre import router as genre_router
from mysite.api.movie import router as movie_router, image_router as movie_image_router
from mysite.api.series import router as series_router, episode_router
from mysite.api.review import router as review_router
from mysite.api.subscription import router as subscription_plan_router, user_subscription_router
from mysite.api.favorite import router as favorite_router
from mysite.api.watch_history import router as watch_history_router

Base.metadata.create_all(bind=engine)

netflix_app = FastAPI(
    title="FastNetflix API",
    description="Streaming platform API",
    version="1.0.0",
)

admin = create_admin(netflix_app)

admin.add_view(UserProfileAdmin)
admin.add_view(GenreAdmin)
admin.add_view(MovieAdmin)
admin.add_view(MovieImageAdmin)
admin.add_view(SeriesAdmin)
admin.add_view(EpisodeAdmin)
admin.add_view(ReviewAdmin)
admin.add_view(SubscriptionPlanAdmin)
admin.add_view(UserSubscriptionAdmin)
admin.add_view(FavoriteAdmin)
admin.add_view(WatchHistoryAdmin)
admin.add_view(RefreshTokenAdmin)

netflix_app.include_router(auth_router)
netflix_app.include_router(user_router)
netflix_app.include_router(genre_router)
netflix_app.include_router(movie_router)
netflix_app.include_router(movie_image_router)
netflix_app.include_router(series_router)
netflix_app.include_router(episode_router)
netflix_app.include_router(review_router)
netflix_app.include_router(subscription_plan_router)
netflix_app.include_router(user_subscription_router)
netflix_app.include_router(favorite_router)
netflix_app.include_router(watch_history_router)

if __name__ == '__main__':
    uvicorn.run(netflix_app, host='127.0.0.1', port=8000)
