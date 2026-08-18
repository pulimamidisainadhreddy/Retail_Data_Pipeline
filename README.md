🛒 Retail Data Pipeline
An end-to-end **retail data engineering and business intelligence project** built using **Python, Pandas, PostgreSQL, SQL, and Power BI**.
The project demonstrates how raw e-commerce data is **cleaned, transformed, loaded into PostgreSQL, analyzed using SQL, and visualized through Power BI**.
---
📌 Project Overview
This project uses the **Brazilian E-Commerce Public Dataset (Olist)** to build a complete retail data pipeline.
Pipeline
Raw CSV Data
↓
Python / Pandas
↓
Data Cleaning & Transformation
↓
Cleaned CSV Data
↓
PostgreSQL
↓
SQL Analysis & Views
↓
Power BI Dashboard
---
🎯 Project Objectives
•	Clean and transform raw retail data
•	Build a relational PostgreSQL database
•	Load cleaned data into PostgreSQL
•	Analyze business performance using SQL
•	Create reusable SQL views
•	Build an interactive Power BI dashboard
•	Generate useful business insights
---
🛠️ Tech Stack
•	Python
•	Pandas
•	SQLAlchemy
•	PostgreSQL
•	SQL
•	Power BI
•	Git & GitHub
•	VS Code
---
🔄 Data Pipeline
Pipeline Flow: `screenshots/pipeline_flow.png`
Pipeline Steps
1. Extract
Raw CSV files are read from the Olist dataset.
2. Clean & Transform
Python and Pandas are used to:
•	Remove duplicate records
•	Handle missing values
•	Clean column names
•	Convert date columns
•	Remove invalid prices and freight values
•	Standardize data
•	Save cleaned CSV files
3. Load
The cleaned CSV files are loaded into PostgreSQL using Python and SQLAlchemy.
4. Analyze
SQL queries are used to answer business questions and create analytical views.
5. Visualize
Power BI is used to create an interactive retail dashboard.
---
📂 Dataset
**Brazilian E-Commerce Public Dataset by Olist**
Dataset on Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
Main Tables
•	Customers
•	Orders
•	Order Items
•	Products
•	Payments
•	Reviews
---
📊 Dataset Size
| Table | Records |
|---|---:|
| Customers | 99,441 |
| Orders | 99,441 |
| Products | 32,951 |
| Order Items | 112,650 |
| Payments | 103,886 |
| Reviews | 99,224 |
---
🗄️ Database Design
The cleaned data is stored in **PostgreSQL** using relational tables.
Database Schema: `database/schema.png`
Main Relationships
•	`customers.customer_id → orders.customer_id`
•	`orders.order_id → order_items.order_id`
•	`products.product_id → order_items.product_id`
•	`orders.order_id → payments.order_id`
•	`orders.order_id → reviews.order_id`
The database uses **primary keys, foreign keys, and indexes** to maintain relationships and support efficient analysis.
---
🧹 Data Cleaning
Python/Pandas is used for data preprocessing.
Customers
•	Remove duplicates
•	Handle missing customer city
•	Remove records without customer IDs
•	Clean text fields
Orders
•	Remove duplicates
•	Clean column names
•	Convert date columns
•	Remove records without order/customer IDs
Order Items
•	Remove duplicates
•	Remove invalid prices
•	Remove invalid freight values
•	Convert shipping dates
•	Validate required IDs
Products
•	Remove duplicates
•	Fill missing product categories
•	Fill missing numeric values
Payments
•	Remove duplicates
•	Remove invalid payment values
•	Handle missing payment types
Reviews
•	Remove duplicates
•	Handle missing review titles and messages
•	Convert review dates
•	Validate review and order IDs
---
📁 Project Structure
Retail-Data-Pipeline/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── python/
│   ├── 01_load_data.py
│   ├── 02_clean_data.py
│   └── roadtopostgreysql.py
│
├── sql/
│   ├── create_tables.sql
│   ├── insert_data.sql
│   ├── business_queries.sql
│   └── views.sql
│
├── powerbi/
│   ├── Retail_Dashboard.pbix
│   └── dashboard.png
│
├── database/
│   └── schema.png
│
├── screenshots/
│   ├── dash.png
│   ├── pipeline_flow.png
│   └── sql_results.png
│
├── documentation/
│   ├── business_insights.md
│   ├── data_dictionary.md
│   └── project_flow.md
│
├── requirements.txt
├── .gitignore
└── README.md
---
🐍 Python Processing
The Python pipeline contains three main stages.
Load Raw Data
`python python/01_load_data.py`
This verifies and loads the required raw CSV files.
Clean Data
`python python/02_clean_data.py`
This cleans and saves the datasets into:
`data/cleaned/`
Load PostgreSQL
`python python/roadtopostgreysql.py`
This loads the cleaned datasets into PostgreSQL.
---
🗃️ SQL
Create Database Tables
Run:
`sql/create_tables.sql`
This creates the PostgreSQL tables, relationships, constraints, and indexes.
Load Data
The main project uses:
`python/roadtopostgreysql.py`
to load the cleaned CSV files.
`insert_data.sql` is included as an alternative/reference loading script for PostgreSQL `psql`.
Business Analysis
Run:
`sql/business_queries.sql`
The queries analyze:
•	Total orders
•	Total revenue
•	Average payment
•	Top-selling products
•	Revenue by payment type
•	Monthly orders
•	Customers by state
•	Order status distribution
•	Product categories
Analytical Views
Run:
`sql/views.sql`
The views provide reusable datasets for reporting and Power BI.
---
📈 Key Results
Based on the project analysis:
| KPI | Value |
|---|---:|
| Total Orders | 99,441 |
| Total Revenue | 13,591,643.70 |
| Average Payment | 154.10 |
| Unique Customers | 96,096 |
| Products | 32,951 |
---
💡 Business Insights
Customer Distribution
São Paulo (`SP`) has the highest number of customers, followed by Rio de Janeiro (`RJ`) and Minas Gerais (`MG`).
Payment Methods
Credit card is the dominant payment method and generates the highest payment revenue.
Product Categories
The highest-revenue product categories include:
1. Beauty & Health
2. Watches & Gifts
3. Bed, Bath & Table
4. Sports & Leisure
5. Computers & Accessories
Order Status
The majority of orders have a **delivered** status.
---
📊 Power BI Dashboard
The project includes an interactive Power BI dashboard for retail performance analysis.
Dashboard: `screenshots/dash.png`
Dashboard KPIs
•	Total Orders
•	Total Revenue
•	Average Payment
•	Total Customers
Dashboard Visualizations
•	Monthly Orders
•	Customers by State
•	Top Product Categories
•	Revenue by Payment Type
•	Order Performance
---
🗃️ SQL Results
Sample PostgreSQL analysis results:
SQL Results: `screenshots/sql_results.png`
---
🚀 How to Run
1. Clone the repository
`git clone https://github.com/pulimamidisainadhreddy/Retail-Data-Pipeline.git`
`cd Retail-Data-Pipeline`
2. Create a virtual environment
`python -m venv .venv`
Activate on Windows:
`.venv\Scripts\activate`
3. Install dependencies
`pip install -r requirements.txt`
4. Configure PostgreSQL
Create a PostgreSQL database named:
`retail_data_pipeline`
5. Configure environment variables
Create `.env` in the project root:
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=retail_data_pipeline
**Never commit `.env` to GitHub.**
6. Load raw data
`python python/01_load_data.py`
7. Clean the data
`python python/02_clean_data.py`
8. Create PostgreSQL tables
Run:
`sql/create_tables.sql`
in PostgreSQL/pgAdmin.
9. Load cleaned data
`python python/roadtopostgreysql.py`
10. Run SQL analysis
Execute:
`sql/business_queries.sql`
11. Create analytical views
Execute:
`sql/views.sql`
12. Open Power BI
Open:
`powerbi/Retail_Dashboard.pbix`
---
🔐 Database Security
Database credentials are stored using environment variables.
Variables:
•	`POSTGRES_USER`
•	`POSTGRES_PASSWORD`
•	`POSTGRES_HOST`
•	`POSTGRES_PORT`
•	`POSTGRES_DB`
The `.env` file should be excluded from Git using `.gitignore`.
---
📦 Requirements
The project uses:
•	pandas
•	SQLAlchemy
•	psycopg2-binary
•	python-dotenv
Install them with:
`pip install -r requirements.txt`
---
🎓 Skills Demonstrated
•	Python
•	Pandas
•	SQLAlchemy
•	Data Cleaning
•	Data Transformation
•	ETL
•	PostgreSQL
•	SQL
•	SQL Joins
•	SQL Views
•	Relational Data Modeling
•	Database Constraints
•	Business Analysis
•	Power BI
•	Data Visualization
•	Git & GitHub
---
🔮 Future Improvements
•	Automate the ETL pipeline
•	Add data validation
•	Add logging
•	Add automated testing
•	Dockerize the application
•	Implement Apache Airflow
•	Deploy the pipeline to AWS/Azure
•	Add automated Power BI refresh
---
📚 Key Learnings
This project provided practical experience in building an end-to-end data pipeline:
Data Extraction
↓
Data Cleaning
↓
Data Transformation
↓
PostgreSQL
↓
SQL Analysis
↓
Power BI
The project demonstrates how raw retail data can be transformed into **structured, analyzable, and business-ready information**.
---
🔗 Repository
GitHub:
https://github.com/pulimamidisainadhreddy/Retail-Data-Pipeline
