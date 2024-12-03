from . import (orders, order_details, pantry, menu, menu_item, customer,
               payment_info, review, recipes)

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    pantry.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    payment_info.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)

