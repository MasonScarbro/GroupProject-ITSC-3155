---

## **Customer**
Represents a customer using the system.

### Attributes:
- `id` (int): Unique identifier for the customer.
- `name` (str): Full name of the customer.
- `email` (str): Contact email address.
- `phone_number` (str): Contact phone number.
- `address` (Optional[str]): Residential address of the customer.
- `payment_info` (Optional[PaymentInfo]): Linked payment information.
- `orders` (List[Order]): List of orders placed by the customer.

### Purpose:
Tracks user information, payment methods, and their order history.

---

## **PaymentInfo**
Represents payment-related information for a customer.

### Attributes:
- `id` (int): Unique identifier for the payment information.
- `card_information` (str): Masked card details.
- `transaction_status` (str): Current status of the transaction (e.g., pending, completed).
- `payment_type` (str): Payment method (e.g., credit card, PayPal).
- `customer_id` (Optional[int]): ID of the associated customer.

### Purpose:
Manages payment methods and transaction statuses for customers.

---

## **Order**
Represents a purchase made by a customer.

### Attributes:
- `id` (int): Unique identifier for the order.
- `order_date` (Optional[datetime]): Date and time when the order was placed.
- `customer_name` (str): Name of the customer placing the order.
- `description` (Optional[str]): Additional order details or notes.
- `order_details` (List[OrderDetail]): List of items in the order.

### Purpose:
Tracks orders and associated details for each customer.

---

## **OrderDetail**
Represents a specific item in an order.

### Attributes:
- `id` (int): Unique identifier for the order detail.
- `order_id` (int): ID of the associated order.
- `amount` (int): Quantity of the item ordered.
- `sandwich` (Optional[Sandwich]): The item (or sandwich) being ordered.

### Purpose:
Details the items in a customer's order, including quantities and specific products.

---

## **Pantry**
Represents the storage of ingredients and resources available for creating menu items.

### Attributes:
- `id` (int): Unique identifier for the pantry entry.
- `ingredient` (str): Name of the ingredient.
- `quantity` (int): Available amount of the ingredient.
- `menu_item` (Optional[MenuItem]): Related menu item that uses the ingredient.

### Purpose:
Tracks inventory levels for ingredients used in menu items.

---

## **Menu**
Represents the menu available to customers.

### Attributes:
- `id` (int): Unique identifier for the menu.
- `available_items` (str): List of available items in the menu.
- `prices` (str): Price information for the menu items.
- `calories` (str): Caloric information for the menu items.
- `categories` (str): Categories of the menu items (e.g., drinks, main dishes).
- `menu_items` (List[MenuItem]): List of menu items available.

### Purpose:
Serves as the interface to display menu information to customers.

---

## **MenuItem**
Represents a specific item on the menu.

### Attributes:
- `id` (int): Unique identifier for the menu item.
- `dish` (str): Name of the dish.
- `calories` (int): Caloric content of the dish.
- `price` (float): Price of the dish.
- `menu_id` (int): ID of the menu to which the item belongs.
- `ingredients` (List[Pantry]): List of ingredients (from Pantry) required for the item.

### Purpose:
Defines details of a specific dish or item on the menu.

---

# Model Relationships

### **Customer**
- Has optional `PaymentInfo`.
- Can place multiple `Order`s.

### **PaymentInfo**
- Linked to a single `Customer`.

### **Order**
- Contains multiple `OrderDetail`s.
- Linked to a `Customer`.

### **OrderDetail**
- Linked to a single `Order`.
- References a `Sandwich` or menu item.

### **Pantry**
- Tracks ingredients and their quantities.
- References `MenuItem` for associated dishes.

### **Menu**
- Contains multiple `MenuItem`s.

### **MenuItem**
- Linked to a `Menu`.
- Contains references to `Pantry` ingredients.

---

## Notes:
