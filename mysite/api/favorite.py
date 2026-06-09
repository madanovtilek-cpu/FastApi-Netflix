from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import get_db
from mysite.database.models import Favorite
from mysite.database.schema import FavoriteInputSchema, FavoriteOutSchema

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.get("/", response_model=List[FavoriteOutSchema])
def get_favorites(db: Session = Depends(get_db)):
    return db.query(Favorite).all()


@router.get("/{favorite_id}", response_model=FavoriteOutSchema)
def get_favorite(favorite_id: int, db: Session = Depends(get_db)):
    favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return favorite


@router.post("/", response_model=FavoriteOutSchema, status_code=status.HTTP_201_CREATED)
def create_favorite(data: FavoriteInputSchema, db: Session = Depends(get_db)):
    favorite = Favorite(**data.model_dump())
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite


@router.delete("/{favorite_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_favorite(favorite_id: int, db: Session = Depends(get_db)):
    favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    db.delete(favorite)
    db.commit()
