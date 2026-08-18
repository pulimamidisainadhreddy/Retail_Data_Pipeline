from pathlib import Path
import pandas as pd


# ============================================================
# PROJECT DIRECTORIES
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[1]

CLEANED_DIR = ROOT_DIR / "data" / "cleaned"


# ============================================================
# LOAD CLEANED DATA
# ============================================================

customers = pd.read_csv(
    CLEANED_DIR / "customers_cleaned.csv"
)

orders = pd.read_csv(
    CLEANED_DIR / "orders_clean.csv"
)

order_items = pd.read_csv(
    CLEANED_DIR / "order_items_clean.csv"
)

products = pd.read_csv(
    CLEANED_DIR / "products_clean.csv"
)

payments = pd.read_csv(
    CLEANED_DIR / "payments_clean.csv"
)

reviews = pd.read_csv(
    CLEANED_DIR / "reviews_clean.csv"
)


# ============================================================
# VALIDATION FUNCTIONS
# ============================================================

def check_no_duplicate_orders():
    duplicates = orders["order_id"].duplicated().sum()

    assert duplicates == 0, (
        f"Found {duplicates} duplicate order IDs"
    )

    print("✓ No duplicate order IDs")


def check_customer_ids():
    nulls = customers["customer_id"].isna().sum()

    assert nulls == 0, (
        f"Found {nulls} NULL customer IDs"
    )

    print("✓ No NULL customer IDs")


def check_order_customer_ids():
    missing = orders["customer_id"].isna().sum()

    assert missing == 0, (
        f"Found {missing} orders with NULL customer IDs"
    )

    print("✓ All orders have customer IDs")


def check_prices():
    invalid = (order_items["price"] < 0).sum()

    assert invalid == 0, (
        f"Found {invalid} negative prices"
    )

    print("✓ No negative prices")


def check_freight():
    invalid = (order_items["freight_value"] < 0).sum()

    assert invalid == 0, (
        f"Found {invalid} negative freight values"
    )

    print("✓ No negative freight values")


def check_foreign_keys():
    customer_ids = set(customers["customer_id"])

    invalid_customers = (
        ~orders["customer_id"].isin(customer_ids)
    ).sum()

    assert invalid_customers == 0, (
        f"Found {invalid_customers} orders with invalid customer IDs"
    )

    print("✓ Customer foreign keys are valid")


def check_row_counts():
    expected = {
        "customers": 99441,
        "orders": 99441,
        "products": 32951,
        "order_items": 112650,
    }

    actual = {
        "customers": len(customers),
        "orders": len(orders),
        "products": len(products),
        "order_items": len(order_items),
    }

    for table, expected_count in expected.items():

        actual_count = actual[table]

        assert actual_count == expected_count, (
            f"{table}: expected {expected_count}, "
            f"found {actual_count}"
        )

        print(
            f"✓ {table}: {actual_count:,} rows"
        )


# ============================================================
# RUN ALL TESTS
# ============================================================

def main():

    print("=" * 60)
    print("DATA QUALITY VALIDATION")
    print("=" * 60)

    check_no_duplicate_orders()
    check_customer_ids()
    check_order_customer_ids()
    check_prices()
    check_freight()
    check_foreign_keys()
    check_row_counts()

    print()
    print("=" * 60)
    print("ALL DATA QUALITY TESTS PASSED!")
    print("=" * 60)


if __name__ == "__main__":
    main()