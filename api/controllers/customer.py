from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import  payment_info as payment_info_model
from ..models import customer as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.Customer(
        name =request.name,
        email =request.email,
        phone_number =request.phone_number,
        address =request.address,
        payment_info_id =request.payment_info_id
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

        #populates payment info's customer id if its used
        if new_item.payment_info_id:
            payment_info = db.query(payment_info_model.PaymentInfo).filter(
                payment_info_model.PaymentInfo.id == new_item.payment_info_id
            ).first()

            if payment_info:
                payment_info.customer_id = new_item.id
                db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def delete(db: Session, customer_id: int):
    # Retrieve the customer to delete
    item = db.query(model.Customer).filter(model.Customer.id == customer_id).first()

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")

    try:
        db.delete(item)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return {"detail": "Customer deleted successfully"}

def delete_all(db: Session):
    try:
        # Delete all customer records
        db.query(model.Customer).delete()
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return {"detail": "All customers deleted successfully"}

def update(db: Session, customer_id: int, request):
    try:
        # Fetch the customer record by ID
        item = db.query(model.Customer).filter(model.Customer.id == customer_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")

        # Convert the request data to a dictionary, excluding unset fields
        update_data = request.dict(exclude_unset=True)
        # Update the customer record with the provided data
        item.update(update_data, synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return item.first()