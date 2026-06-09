from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import get_db
from mysite.database.models import WatchHistory
from mysite.database.schema import WatchHistoryInputSchema, WatchHistoryOutSchema

router = APIRouter(prefix="/watch-history", tags=["Watch History"])


@router.get("/", response_model=List[WatchHistoryOutSchema])
def get_watch_history(db: Session = Depends(get_db)):
    return db.query(WatchHistory).all()


@router.get("/{history_id}", response_model=WatchHistoryOutSchema)
def get_watch_history_item(history_id: int, db: Session = Depends(get_db)):
    item = db.query(WatchHistory).filter(WatchHistory.id == history_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Watch history record not found")
    return item


@router.post("/", response_model=WatchHistoryOutSchema, status_code=status.HTTP_201_CREATED)
def create_watch_history(data: WatchHistoryInputSchema, db: Session = Depends(get_db)):
    item = WatchHistory(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{history_id}", response_model=WatchHistoryOutSchema)
def update_watch_history(history_id: int, data: WatchHistoryInputSchema, db: Session = Depends(get_db)):
    item = db.query(WatchHistory).filter(WatchHistory.id == history_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Watch history record not found")
    for key, value in data.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{history_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_watch_history(history_id: int, db: Session = Depends(get_db)):
    item = db.query(WatchHistory).filter(WatchHistory.id == history_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Watch history record not found")
    db.delete(item)
    db.commit()
