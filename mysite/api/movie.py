from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import get_db
from mysite.database.models import Movie, MovieImage
from mysite.database.schema import (
    MovieInputSchema, MovieOutSchema,
    MovieImageInputSchema, MovieImageOutSchema,
)

router = APIRouter(prefix="/movies", tags=["Movies"])


# ---------- Movie ----------

@router.get("/", response_model=List[MovieOutSchema])
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@router.get("/{movie_id}", response_model=MovieOutSchema)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.post("/", response_model=MovieOutSchema, status_code=status.HTTP_201_CREATED)
def create_movie(data: MovieInputSchema, db: Session = Depends(get_db)):
    movie = Movie(**data.model_dump())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


@router.put("/{movie_id}", response_model=MovieOutSchema)
def update_movie(movie_id: int, data: MovieInputSchema, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in data.model_dump().items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie


@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()


# ---------- MovieImage ----------

image_router = APIRouter(prefix="/movie-images", tags=["Movie Images"])


@image_router.get("/", response_model=List[MovieImageOutSchema])
def get_movie_images(db: Session = Depends(get_db)):
    return db.query(MovieImage).all()


@image_router.get("/{image_id}", response_model=MovieImageOutSchema)
def get_movie_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(MovieImage).filter(MovieImage.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image


@image_router.post("/", response_model=MovieImageOutSchema, status_code=status.HTTP_201_CREATED)
def create_movie_image(data: MovieImageInputSchema, db: Session = Depends(get_db)):
    image = MovieImage(**data.model_dump())
    db.add(image)
    db.commit()
    db.refresh(image)
    return image


@image_router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(MovieImage).filter(MovieImage.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    db.delete(image)
    db.commit()
