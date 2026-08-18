-- ============================================
-- RETAIL DATA PIPELINE
-- ANALYTICAL VIEWS
-- ============================================

DROP VIEW IF EXISTS vw_monthly_orders;
DROP VIEW IF EXISTS vw_payment_revenue;
DROP VIEW IF EXISTS vw_customer_state;
DROP VIEW IF EXISTS vw_order_status;
DROP VIEW IF EXISTS vw_category_revenue;
DROP VIEW IF EXISTS vw_retail_kpis;


-- 1. Monthly Orders
CREATE VIEW vw_monthly_orders AS
SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY DATE_TRUNC('month', order_purchase_timestamp);


-- 2. Revenue by Payment Type
CREATE VIEW vw_payment_revenue AS
SELECT
    payment_type,
    ROUND(SUM(payment_value)::NUMERIC, 2) AS revenue,
    COUNT(*) AS payment_count
FROM payments
GROUP BY payment_type;


-- 3. Customers by State
CREATE VIEW vw_customer_state AS
SELECT
    customer_state,
    COUNT(*) AS customers
FROM customers
GROUP BY customer_state;


-- 4. Order Status
CREATE VIEW vw_order_status AS
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;


-- 5. Revenue by Product Category
CREATE VIEW vw_category_revenue AS
SELECT
    COALESCE(p.product_category_name, 'Unknown') AS product_category,
    ROUND(SUM(oi.price)::NUMERIC, 2) AS revenue,
    COUNT(*) AS total_items
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY COALESCE(p.product_category_name, 'Unknown');


-- 6. Main Retail KPIs
CREATE VIEW vw_retail_kpis AS
SELECT
    (SELECT COUNT(*) FROM orders) AS total_orders,

    (SELECT ROUND(SUM(price)::NUMERIC, 2)
     FROM order_items) AS total_revenue,

    (SELECT ROUND(AVG(payment_value)::NUMERIC, 2)
     FROM payments) AS average_payment,

    (SELECT COUNT(DISTINCT customer_unique_id)
     FROM customers) AS unique_customers,

    (SELECT COUNT(*)
     FROM products) AS total_products;