from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import get_db
from mysite.database.models import SubscriptionPlan, UserSubscription
from mysite.database.schema import (
    SubscriptionPlanInputSchema, SubscriptionPlanOutSchema,
    UserSubscriptionInputSchema, UserSubscriptionOutSchema,
)

router = APIRouter(prefix="/subscription-plans", tags=["Subscription Plans"])


# ---------- SubscriptionPlan ----------

@router.get("/", response_model=List[SubscriptionPlanOutSchema])
def get_plans(db: Session = Depends(get_db)):
    return db.query(SubscriptionPlan).all()


@router.get("/{plan_id}", response_model=SubscriptionPlanOutSchema)
def get_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(SubscriptionPlan).filter(SubscriptionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Subscription plan not found")
    return plan


@router.post("/", response_model=SubscriptionPlanOutSchema, status_code=status.HTTP_201_CREATED)
def create_plan(data: SubscriptionPlanInputSchema, db: Session = Depends(get_db)):
    plan = SubscriptionPlan(**data.model_dump())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


@router.put("/{plan_id}", response_model=SubscriptionPlanOutSchema)
def update_plan(plan_id: int, data: SubscriptionPlanInputSchema, db: Session = Depends(get_db)):
    plan = db.query(SubscriptionPlan).filter(SubscriptionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Subscription plan not found")
    for key, value in data.model_dump().items():
        setattr(plan, key, value)
    db.commit()
    db.refresh(plan)
    return plan


@router.delete("/{plan_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(SubscriptionPlan).filter(SubscriptionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Subscription plan not found")
    db.delete(plan)
    db.commit()


# ---------- UserSubscription ----------

user_subscription_router = APIRouter(prefix="/user-subscriptions", tags=["User Subscriptions"])


@user_subscription_router.get("/", response_model=List[UserSubscriptionOutSchema])
def get_user_subscriptions(db: Session = Depends(get_db)):
    return db.query(UserSubscription).all()


@user_subscription_router.get("/{subscription_id}", response_model=UserSubscriptionOutSchema)
def get_user_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = db.query(UserSubscription).filter(UserSubscription.id == subscription_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="User subscription not found")
    return subscription


@user_subscription_router.post("/", response_model=UserSubscriptionOutSchema, status_code=status.HTTP_201_CREATED)
def create_user_subscription(data: UserSubscriptionInputSchema, db: Session = Depends(get_db)):
    if data.end_date <= data.start_date:
        raise HTTPException(status_code=400, detail="end_date must be after start_date")
    subscription = UserSubscription(**data.model_dump())
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription


@user_subscription_router.put("/{subscription_id}", response_model=UserSubscriptionOutSchema)
def update_user_subscription(subscription_id: int, data: UserSubscriptionInputSchema, db: Session = Depends(get_db)):
    subscription = db.query(UserSubscription).filter(UserSubscription.id == subscription_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="User subscription not found")
    if data.end_date <= data.start_date:
        raise HTTPException(status_code=400, detail="end_date must be after start_date")
    for key, value in data.model_dump().items():
        setattr(subscription, key, value)
    db.commit()
    db.refresh(subscription)
    return subscription


@user_subscription_router.delete("/{subscription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = db.query(UserSubscription).filter(UserSubscription.id == subscription_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="User subscription not found")
    db.delete(subscription)
    db.commit()
