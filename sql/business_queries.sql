-- ============================================
-- RETAIL DATA PIPELINE
-- BUSINESS ANALYSIS QUERIES
-- ============================================

-- 1. Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- 2. Total Revenue
SELECT
    ROUND(SUM(price)::NUMERIC, 2) AS total_revenue
FROM order_items;


-- 3. Top 10 Products by Sales
SELECT
    product_id,
    COUNT(*) AS total_sales
FROM order_items
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;


-- 4. Top 10 Customers by Orders
SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC
LIMIT 10;


-- 5. Revenue by Payment Type
SELECT
    payment_type,
    ROUND(SUM(payment_value)::NUMERIC, 2) AS revenue
FROM payments
GROUP BY payment_type
ORDER BY revenue DESC;


-- 6. Monthly Orders
SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;


-- 7. Average Payment
SELECT
    ROUND(AVG(payment_value)::NUMERIC, 2) AS average_payment
FROM payments;


-- 8. Total Products
SELECT
    COUNT(DISTINCT product_id) AS total_products
FROM order_items;


-- 9. Order Status
SELECT
    order_status,
    COUNT(*) AS total
FROM orders
GROUP BY order_status
ORDER BY total DESC;


-- 10. Customers by State
SELECT
    customer_state,
    COUNT(*) AS customers
FROM customers
GROUP BY customer_state
ORDER BY customers DESC;


-- 11. Record Counts
SELECT 'Customers' AS table_name, COUNT(*) AS total_records
FROM customers

UNION ALL

SELECT 'Orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'Products', COUNT(*)
FROM products

UNION ALL

SELECT 'Order Items', COUNT(*)
FROM order_items

UNION ALL

SELECT 'Payments', COUNT(*)
FROM payments

UNION ALL

SELECT 'Reviews', COUNT(*)
FROM reviews

ORDER BY table_name;


-- 12. Revenue by Product Category
SELECT
    COALESCE(p.product_category_name, 'Unknown') AS product_category,
    ROUND(SUM(oi.price)::NUMERIC, 2) AS revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY COALESCE(p.product_category_name, 'Unknown')
ORDER BY revenue DESC
LIMIT 10;