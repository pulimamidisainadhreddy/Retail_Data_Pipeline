from pathlib import Path
import pandas as pd
from logger_config import logger


# ============================================================
# PROJECT DIRECTORIES
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = ROOT_DIR / "data" / "raw"
CLEANED_DIR = ROOT_DIR / "data" / "cleaned"

CLEANED_DIR.mkdir(parents=True, exist_ok=True)

logger.info("Data cleaning started")


# ============================================================
# 1. CUSTOMERS
# ============================================================

customers = pd.read_csv(
    RAW_DIR / "olist_customers_dataset.csv"
)

customers = customers.drop_duplicates()

customers.columns = customers.columns.str.strip()

customers["customer_city"] = (
    customers["customer_city"]
    .fillna("Unknown")
    .str.strip()
)

customers = customers.dropna(
    subset=["customer_id", "customer_unique_id"]
)

customers.to_csv(
    CLEANED_DIR / "customers_cleaned.csv",
    index=False
)

logger.info(
    f"Customers cleaning completed: {len(customers):,} rows"
)

print("Customers cleaned successfully!")


# ============================================================
# 2. ORDERS
# ============================================================

orders = pd.read_csv(
    RAW_DIR / "olist_orders_dataset.csv"
)

orders = orders.drop_duplicates()

orders.columns = orders.columns.str.strip()

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

orders = orders.dropna(
    subset=["order_id", "customer_id"]
)

orders.to_csv(
    CLEANED_DIR / "orders_clean.csv",
    index=False
)

logger.info(
    f"Orders cleaning completed: {len(orders):,} rows"
)

print("Orders cleaned successfully!")


# ============================================================
# 3. ORDER ITEMS
# ============================================================

order_items = pd.read_csv(
    RAW_DIR / "olist_order_items_dataset.csv"
)

order_items = order_items.drop_duplicates()

order_items.columns = order_items.columns.str.strip()

order_items = order_items[
    order_items["price"] >= 0
]

order_items = order_items[
    order_items["freight_value"] >= 0
]

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

order_items = order_items.dropna(
    subset=[
        "order_id",
        "order_item_id",
        "product_id"
    ]
)

order_items.to_csv(
    CLEANED_DIR / "order_items_clean.csv",
    index=False
)

logger.info(
    f"Order Items cleaning completed: "
    f"{len(order_items):,} rows"
)

print("Order Items cleaned successfully!")


# ============================================================
# 4. PRODUCTS
# ============================================================

products = pd.read_csv(
    RAW_DIR / "olist_products_dataset.csv"
)

products = products.drop_duplicates()

products.columns = products.columns.str.strip()

products["product_category_name"] = (
    products["product_category_name"]
    .fillna("Unknown")
)

numeric_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

products[numeric_columns] = (
    products[numeric_columns].fillna(0)
)

products.to_csv(
    CLEANED_DIR / "products_clean.csv",
    index=False
)

logger.info(
    f"Products cleaning completed: {len(products):,} rows"
)

print("Products cleaned successfully!")


# ============================================================
# 5. PAYMENTS
# ============================================================

payments = pd.read_csv(
    RAW_DIR / "olist_order_payments_dataset.csv"
)

payments = payments.drop_duplicates()

payments.columns = payments.columns.str.strip()

payments = payments[
    payments["payment_value"] >= 0
]

payments["payment_type"] = (
    payments["payment_type"]
    .fillna("Unknown")
)

payments = payments.dropna(
    subset=[
        "order_id",
        "payment_sequential"
    ]
)

payments.to_csv(
    CLEANED_DIR / "payments_clean.csv",
    index=False
)

logger.info(
    f"Payments cleaning completed: {len(payments):,} rows"
)

print("Payments cleaned successfully!")


# ============================================================
# 6. REVIEWS
# ============================================================

reviews = pd.read_csv(
    RAW_DIR / "olist_order_reviews_dataset.csv"
)

reviews = reviews.drop_duplicates()

reviews.columns = reviews.columns.str.strip()

reviews["review_comment_title"] = (
    reviews["review_comment_title"]
    .fillna("No Title")
)

reviews["review_comment_message"] = (
    reviews["review_comment_message"]
    .fillna("No Comment")
)

reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)

reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
)

reviews = reviews.dropna(
    subset=["review_id", "order_id"]
)

reviews.to_csv(
    CLEANED_DIR / "reviews_clean.csv",
    index=False
)

logger.info(
    f"Reviews cleaning completed: {len(reviews):,} rows"
)

print("Reviews cleaned successfully!")


# ============================================================
# FINISHED
# ============================================================

print()
print("=" * 60)
print("ALL DATASETS CLEANED SUCCESSFULLY!")
print("=" * 60)
print(f"Cleaned files saved to: {CLEANED_DIR}")

logger.info("Data cleaning completed")
logger.info("All datasets cleaned successfully")