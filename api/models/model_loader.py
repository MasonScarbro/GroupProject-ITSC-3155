from . import orders, order_details, recipes, sandwiches, resources,  pantry, menu, menu_item, customer, payment_info

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    pantry.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    payment_info.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
