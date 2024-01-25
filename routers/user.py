from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from databasy import get_db
from services import user as user_service
from dto import user as user_dto

router = APIRouter()


@router.post('/', tags=['user'])
async def create(data: user_dto.User = None, db: Session = Depends(get_db)):
    return user_service.create_user(data, db)


@router.get('{user_id}', tags=['user'])
async def get(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(user_id, db)


@router.put('/{user_id}', tags=['user'])
async def update(user_id: int, data: user_dto.User = None, db: Session = Depends(get_db)):
    return user_service.update(data, db, user_id)


@router.delete('/{user_id', tags=['user'])
async def delete(user_id: int, db: Session = Depends(get_db)):
    return user_service.remove(db, user_id)
