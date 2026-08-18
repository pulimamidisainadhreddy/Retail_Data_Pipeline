from pathlib import Path
import pandas as pd


# Project directories
ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT_DIR / "data" / "raw"


RAW_FILES = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "products": "olist_products_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
}


def load_raw_data():
    """Read all required raw CSV files."""

    data = {}

    for name, filename in RAW_FILES.items():

        file_path = RAW_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Required raw file was not found: {file_path}"
            )

        df = pd.read_csv(file_path)
        data[name] = df

        print(
            f"{name:<12} | "
            f"{len(df):>8,} rows | "
            f"{len(df.columns):>2} columns"
        )

    return data


def main():
    print("=" * 65)
    print("OLIST RETAIL DATA - RAW DATA LOADING")
    print("=" * 65)

    print(f"Raw data directory: {RAW_DIR}")
    print()

    load_raw_data()

    print()
    print("-" * 65)
    print("Raw data loaded successfully.")
    print("-" * 65)


if __name__ == "__main__":
    main()