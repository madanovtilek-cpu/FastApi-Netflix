from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import get_db
from mysite.database.models import Series, Episode
from mysite.database.schema import (
    SeriesInputSchema, SeriesOutSchema,
    EpisodeInputSchema, EpisodeOutSchema,
)

router = APIRouter(prefix="/series", tags=["Series"])


# ---------- Series ----------

@router.get("/", response_model=List[SeriesOutSchema])
def get_all_series(db: Session = Depends(get_db)):
    return db.query(Series).all()


@router.get("/{series_id}", response_model=SeriesOutSchema)
def get_series(series_id: int, db: Session = Depends(get_db)):
    series = db.query(Series).filter(Series.id == series_id).first()
    if not series:
        raise HTTPException(status_code=404, detail="Series not found")
    return series


@router.post("/", response_model=SeriesOutSchema, status_code=status.HTTP_201_CREATED)
def create_series(data: SeriesInputSchema, db: Session = Depends(get_db)):
    series = Series(**data.model_dump())
    db.add(series)
    db.commit()
    db.refresh(series)
    return series


@router.put("/{series_id}", response_model=SeriesOutSchema)
def update_series(series_id: int, data: SeriesInputSchema, db: Session = Depends(get_db)):
    series = db.query(Series).filter(Series.id == series_id).first()
    if not series:
        raise HTTPException(status_code=404, detail="Series not found")
    for key, value in data.model_dump().items():
        setattr(series, key, value)
    db.commit()
    db.refresh(series)
    return series


@router.delete("/{series_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_series(series_id: int, db: Session = Depends(get_db)):
    series = db.query(Series).filter(Series.id == series_id).first()
    if not series:
        raise HTTPException(status_code=404, detail="Series not found")
    db.delete(series)
    db.commit()


# ---------- Episode ----------

episode_router = APIRouter(prefix="/episodes", tags=["Episodes"])


@episode_router.get("/", response_model=List[EpisodeOutSchema])
def get_episodes(db: Session = Depends(get_db)):
    return db.query(Episode).all()


@episode_router.get("/{episode_id}", response_model=EpisodeOutSchema)
def get_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found")
    return episode


@episode_router.post("/", response_model=EpisodeOutSchema, status_code=status.HTTP_201_CREATED)
def create_episode(data: EpisodeInputSchema, db: Session = Depends(get_db)):
    episode = Episode(**data.model_dump())
    db.add(episode)
    db.commit()
    db.refresh(episode)
    return episode


@episode_router.put("/{episode_id}", response_model=EpisodeOutSchema)
def update_episode(episode_id: int, data: EpisodeInputSchema, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found")
    for key, value in data.model_dump().items():
        setattr(episode, key, value)
    db.commit()
    db.refresh(episode)
    return episode


@episode_router.delete("/{episode_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found")
    db.delete(episode)
    db.commit()
