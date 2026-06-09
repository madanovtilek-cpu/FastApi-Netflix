from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import get_db
from mysite.database.models import Genre
from mysite.database.schema import GenreInputSchema, GenreOutSchema

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.get("/", response_model=List[GenreOutSchema])
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()


@router.get("/{genre_id}", response_model=GenreOutSchema)
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


@router.post("/", response_model=GenreOutSchema, status_code=status.HTTP_201_CREATED)
def create_genre(data: GenreInputSchema, db: Session = Depends(get_db)):
    genre = Genre(**data.model_dump())
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre


@router.put("/{genre_id}", response_model=GenreOutSchema)
def update_genre(genre_id: int, data: GenreInputSchema, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    for key, value in data.model_dump().items():
        setattr(genre, key, value)
    db.commit()
    db.refresh(genre)
    return genre


@router.delete("/{genre_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    db.delete(genre)
    db.commit()
