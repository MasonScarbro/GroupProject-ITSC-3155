from . import orders, order_details, pantry, customer, payment_info


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(pantry.router)
    app.include_router(customer.router)
    app.include_router(payment_info.router)
