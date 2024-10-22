from uuid import UUID
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_db
from app.db.models import User
from app.schemas.user import User as UserSchema, UserCreate

router = APIRouter()


@router.get("/", response_model=List[UserSchema])
async def get_list(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@router.get("/{id}", response_model=UserSchema)
async def get_detail(id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/", response_model=UserSchema)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user = User(**user.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
