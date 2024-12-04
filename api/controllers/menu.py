from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_menu = model.Menu(
        available_items=request.available_items,
        prices=request.prices,
        calories=request.calories,
        categories=request.categories,
    )

    try:
        db.add(new_menu)
        db.commit()
        db.refresh(new_menu)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_menu


def read_all(db: Session):
    try:
        result = db.query(model.Menu).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, menu_id):
    try:
        menu = db.query(model.Menu).filter(model.Menu.id == menu_id).first()
        if not menu:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return menu


def update(db: Session, menu_id, request):
    try:
        menu = db.query(model.Menu).filter(model.Menu.id == menu_id)
        if not menu.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        menu.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return menu.first()


def delete(db: Session, menu_id):
    try:
        menu = db.query(model.Menu).filter(model.Menu.id == menu_id)
        if not menu.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        menu.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
