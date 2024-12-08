from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu_item as model
from sqlalchemy.exc import SQLAlchemyError
from ..models.pantry import Pantry

def create(db: Session, request):


    new_item = model.MenuItem(
        dish=request.dish,
        calories=request.calories,
        price=request.price,
        menu_id=request.menu_id,

    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    if request.ingredients:
        for ingredient_id in request.ingredients:
            pantry_item = db.query(Pantry).filter(Pantry.id == ingredient_id).first()
            if pantry_item:
                pantry_item.menu_id = new_item.id
                # Explicitly add the pantry item to the menu_item's ingredients
                new_item.ingredients.append(pantry_item)
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Ingredient with ID {ingredient_id} not found"
                )

        # Commit the changes
        db.commit()

    try:
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.MenuItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
