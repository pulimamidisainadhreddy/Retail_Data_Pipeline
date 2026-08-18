# Data Dictionary

This project uses selected tables from the Brazilian E-Commerce Public Dataset by Olist.

## 1. Customers

| Column | Description |
|---|---|
| `customer_id` | Unique identifier for an order-level customer record |
| `customer_unique_id` | Identifier representing the customer across orders |
| `customer_zip_code_prefix` | Customer ZIP-code prefix |
| `customer_city` | Customer city |
| `customer_state` | Customer state |

**Primary Key:** `customer_id`

---

## 2. Orders

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `customer_id` | Customer associated with the order |
| `order_status` | Current order status |
| `order_purchase_timestamp` | Date/time when the order was purchased |
| `order_approved_at` | Date/time when payment was approved |
| `order_delivered_carrier_date` | Date/time when the order was handed to the carrier |
| `order_delivered_customer_date` | Date/time when the customer received the order |
| `order_estimated_delivery_date` | Estimated delivery date |

**Primary Key:** `order_id`

**Foreign Key:** `customer_id → customers.customer_id`

---

## 3. Products

| Column | Description |
|---|---|
| `product_id` | Unique product identifier |
| `product_category_name` | Product category |
| `product_name_lenght` | Product name length |
| `product_description_lenght` | Product description length |
| `product_photos_qty` | Number of product photos |
| `product_weight_g` | Product weight in grams |
| `product_length_cm` | Product length in centimeters |
| `product_height_cm` | Product height in centimeters |
| `product_width_cm` | Product width in centimeters |

**Primary Key:** `product_id`

---

## 4. Order Items

| Column | Description |
|---|---|
| `order_id` | Order containing the item |
| `order_item_id` | Sequential item number within an order |
| `product_id` | Product purchased |
| `seller_id` | Seller identifier |
| `shipping_limit_date` | Seller shipping deadline |
| `price` | Item price |
| `freight_value` | Freight/shipping value |

**Composite Primary Key:** `(order_id, order_item_id)`

**Foreign Keys:**
- `order_id → orders.order_id`
- `product_id → products.product_id`

---

## 5. Payments

| Column | Description |
|---|---|
| `order_id` | Order associated with the payment |
| `payment_sequential` | Sequence number of the payment |
| `payment_type` | Payment method |
| `payment_installments` | Number of installments |
| `payment_value` | Payment amount |

**Composite Primary Key:** `(order_id, payment_sequential)`

**Foreign Key:** `order_id → orders.order_id`

---

## 6. Reviews

| Column | Description |
|---|---|
| `review_id` | Review identifier |
| `order_id` | Order associated with the review |
| `review_score` | Customer review score |
| `review_comment_title` | Review title |
| `review_comment_message` | Review message |
| `review_creation_date` | Review creation timestamp |
| `review_answer_timestamp` | Timestamp when the review was answered |

**Composite Primary Key:** `(review_id, order_id)`

**Foreign Key:** `order_id → orders.order_id`

---

## Main Relationships

```text
customers  1 ──── * orders
orders     1 ──── * order_items
products   1 ──── * order_items
orders     1 ──── * payments
orders     1 ──── * reviews
```
