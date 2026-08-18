# Business Insights

## Overview

This document summarizes the main business findings obtained from the Olist retail dataset after cleaning and loading the data into PostgreSQL.

## Key KPIs

| KPI | Value |
|---|---:|
| Total Orders | 99,441 |
| Total Item Revenue | 13,591,643.70 |
| Average Payment | 154.10 |
| Unique Customers | 96,096 |
| Products | 32,951 |

## Customer Insights

- São Paulo (`SP`) has the largest customer base.
- Rio de Janeiro (`RJ`) and Minas Gerais (`MG`) are among the next largest customer markets.
- Customer distribution by state can be analyzed using the `customer_state` field.

## Payment Insights

- Credit card is the dominant payment method.
- Credit card payments generate the highest payment value.
- Payment performance can be analyzed using the `payments` table and `vw_payment_revenue` view.

## Product Insights

- Beauty & Health (`beleza_saude`) is one of the highest-revenue product categories in the dataset.
- Product performance can be analyzed using `order_items` joined with `products`.

## Order Insights

- 99,441 orders are present in the dataset.
- 96,478 orders are marked as delivered.
- Monthly order trends can be analyzed using the purchase timestamp.

## Business Value

The pipeline converts raw e-commerce data into structured information that can support:

- Sales analysis
- Customer analysis
- Payment analysis
- Product performance analysis
- Geographic analysis
- Order-status monitoring

> Note: Revenue in this project is calculated from the `price` field in `order_items`. Payment revenue is calculated separately from `payment_value` in `payments`.
