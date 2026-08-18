from pathlib import Path
import pandas as pd
from logger_config import logger


# ============================================================
# PROJECT DIRECTORIES
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = ROOT_DIR / "data" / "raw"

RAW_FILES = {
    "customers": RAW_DIR / "olist_customers_dataset.csv",
    "orders": RAW_DIR / "olist_orders_dataset.csv",
    "order_items": RAW_DIR / "olist_order_items_dataset.csv",
    "products": RAW_DIR / "olist_products_dataset.csv",
    "payments": RAW_DIR / "olist_order_payments_dataset.csv",
    "reviews": RAW_DIR / "olist_order_reviews_dataset.csv",
}


# ============================================================
# LOAD RAW DATA
# ============================================================

def load_raw_data():

    data = {}

    for name, file_path in RAW_FILES.items():

        if not file_path.exists():

            logger.error(
                f"Required raw file was not found: {file_path}"
            )

            raise FileNotFoundError(
                f"Required raw file was not found: {file_path}"
            )

        df = pd.read_csv(file_path)

        data[name] = df

        logger.info(
            f"{name} loaded successfully: "
            f"{len(df):,} rows, {len(df.columns)} columns"
        )

        print(
            f"{name:<12} | "
            f"{len(df):>8,} rows | "
            f"{len(df.columns):>2} columns"
        )

    return data


# ============================================================
# MAIN
# ============================================================

def main():

    logger.info("Pipeline started")
    logger.info("Raw data loading started")

    print("=" * 65)
    print("OLIST RETAIL DATA - RAW DATA LOADING")
    print("=" * 65)

    print(f"Raw data directory: {RAW_DIR}")
    print()

    try:

        data = load_raw_data()

        print()
        print("-" * 65)
        print("Raw data loaded successfully.")
        print("-" * 65)

        logger.info("Raw files loaded successfully")

    except Exception as e:

        logger.exception(
            f"Pipeline failed during raw data loading: {e}"
        )

        raise


if __name__ == "__main__":
    main()