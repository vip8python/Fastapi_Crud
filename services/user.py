from models.user import User
from sqlalchemy.orm import Session
from dto import user


def create_user(data: user.User, db: Session):
    new_user = User(name=data.name)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        print(e)
    return new_user


def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def update(data: user.User, db: Session, user_id: int):
    existing_user = db.query(User).filter(User.id == user_id).first()
    existing_user.name = data.name
    db.merge(existing_user)
    db.commit()
    db.refresh(existing_user)
    return existing_user


def remove(db: Session, user_id: int):
    deleted_user = db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return deleted_user
