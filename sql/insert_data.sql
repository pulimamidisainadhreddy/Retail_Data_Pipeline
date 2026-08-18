-- ============================================
-- RETAIL DATA PIPELINE
-- DATA LOADING SCRIPT
-- ============================================
--
-- NOTE:
-- The main project loads data using:
--     python/roadtopostgreysql.py
--
-- This SQL file is provided as an alternative/reference
-- for loading the cleaned CSV files with PostgreSQL psql.
--
-- Run from the project root:
--     psql -U postgres -d retail_data_pipeline -f sql/insert_data.sql
--
-- IMPORTANT:
-- \copy is a psql client command. Do not execute this file
-- in pgAdmin Query Tool.
-- ============================================

BEGIN;

-- Customers
\copy customers FROM 'data/cleaned/customers_cleaned.csv' WITH (FORMAT csv, HEADER true, NULL '');

-- Products
\copy products FROM 'data/cleaned/products_clean.csv' WITH (FORMAT csv, HEADER true, NULL '');

-- Orders
\copy orders FROM 'data/cleaned/orders_clean.csv' WITH (FORMAT csv, HEADER true, NULL '');

-- Order Items
\copy order_items FROM 'data/cleaned/order_items_clean.csv' WITH (FORMAT csv, HEADER true, NULL '');

-- Payments
\copy payments FROM 'data/cleaned/payments_clean.csv' WITH (FORMAT csv, HEADER true, NULL '');

-- Reviews
\copy reviews FROM 'data/cleaned/reviews_clean.csv' WITH (FORMAT csv, HEADER true, NULL '');

COMMIT;

-- ============================================
-- DATA VALIDATION
-- ============================================

SELECT 'Customers' AS table_name, COUNT(*) AS total_records FROM customers
UNION ALL
SELECT 'Orders', COUNT(*) FROM orders
UNION ALL
SELECT 'Products', COUNT(*) FROM products
UNION ALL
SELECT 'Order Items', COUNT(*) FROM order_items
UNION ALL
SELECT 'Payments', COUNT(*) FROM payments
UNION ALL
SELECT 'Reviews', COUNT(*) FROM reviews
ORDER BY table_name;
