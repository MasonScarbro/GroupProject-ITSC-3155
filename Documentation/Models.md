# Documentation for Models and Relationships

## **Pantry**
- Represents the ingredients and their quantities available in the inventory.
- **Relationships**:
  - `menu_item`: Links to the `MenuItem` model to identify which menu items use these ingredients.

---

## **MenuItem**
- Represents a specific dish on the menu with its details (e.g., dish name, price, calories).
- **Relationships**:
  - `menu`: Links to the `Menu` model to associate the menu item with a menu.
  - `ingredients`: Links to the `Pantry` model to identify the ingredients required for the menu item.

---

## **Menu**
- Represents a collection of available dishes, prices, categories, and other details.
- **Relationships**:
  - `menu_items`: Links to the `MenuItem` model, representing the items listed in the menu.

---

## **Customer**
- Represents a customer who can place orders and make payments.
- **Relationships**:
  - `payment_info`: Links to the `PaymentInfo` model to store customer payment information.
  - `orders`: Links to the `Order` model to track orders placed by the customer.

---

## **PaymentInfo**
- Stores payment-related details for a customer.
- **Relationships**:
  - `customer`: Links back to the `Customer` model.

## **Order**
- Represents a purchase made by a customer.
- **Relationships**:
  - `order_details`: Links to multiple `OrderDetail` items.
  - `customer`: Links to the `Customer` who placed the order.

---

## **OrderDetail**
- Represents a specific item in an order.
- **Relationships**:
  - `order`: Links to the `Order` model.
  - `sandwich`: Links to the `Sandwich` or specific menu item being ordered.


---
