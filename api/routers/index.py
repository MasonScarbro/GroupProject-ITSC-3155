from . import orders, order_details, pantry, customer, payment_info, menu, menu_item, review


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(pantry.router)
    app.include_router(customer.router)
    app.include_router(payment_info.router)
    app.include_router(menu.router)
    app.include_router(menu_item.router)
    app.include_router(review.router)
