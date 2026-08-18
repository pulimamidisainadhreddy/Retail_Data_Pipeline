import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

# PostgreSQL connection
engine = create_engine(
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Project data files
customers = pd.read_csv("data/cleaned/customers_cleaned.csv")
orders = pd.read_csv("data/cleaned/orders_clean.csv")
products = pd.read_csv("data/cleaned/products_clean.csv")
order_items = pd.read_csv("data/cleaned/order_items_clean.csv")
payments = pd.read_csv("data/cleaned/payments_clean.csv")
reviews = pd.read_csv("data/cleaned/reviews_clean.csv")

# Clear existing data
with engine.begin() as connection:
    connection.execute(text("""
        TRUNCATE TABLE
            reviews,
            payments,
            order_items,
            orders,
            products,
            customers
        RESTART IDENTITY CASCADE;
    """))

# Load data
customers.to_sql("customers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)
orders.to_sql("orders", engine, if_exists="append", index=False)
order_items.to_sql("order_items", engine, if_exists="append", index=False)
payments.to_sql("payments", engine, if_exists="append", index=False)
reviews.to_sql("reviews", engine, if_exists="append", index=False)

print("All data loaded successfully!")

print(f"Customers: {len(customers):,}")
print(f"Orders: {len(orders):,}")
print(f"Products: {len(products):,}")
print(f"Order Items: {len(order_items):,}")
print(f"Payments: {len(payments):,}")
print(f"Reviews: {len(reviews):,}")