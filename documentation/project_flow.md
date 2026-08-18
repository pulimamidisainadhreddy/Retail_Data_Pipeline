# Project Flow

## End-to-End Architecture

```text
Olist Raw CSV Files
        ↓
01_load_data.py
        ↓
Raw Data Validation
        ↓
02_clean_data.py
        ↓
Data Cleaning & Transformation
        ↓
Cleaned CSV Files
        ↓
PostgreSQL
        ↓
SQL Business Queries
        ↓
SQL Views
        ↓
Power BI Dashboard