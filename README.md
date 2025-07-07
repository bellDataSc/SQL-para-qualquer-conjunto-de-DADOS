# SQL for Budget Data Analysis in the Government of São Paulo

By Isabel Gonçalves Cruz

**Updates**: Add the code from the **Google Colab** notebook in XML in the Oracle database.

**Transforming XML queries** into **SQL**

## This repository documents and makes available SQL and XML scripts
used in the analysis of budget and financial data of the Government of the State of São Paulo. The focus is the manipulation and extraction of data from SIGEO (Budget Execution Management Information System), a database that enables the management and transparency of public spending through SQL queries and report generation.

## Tools used:
Oracle Business Intelligence, PostgreSQL, Pandas, Power BI

## Objective:
Facilitate the extraction and analysis of budget data to support strategic decisions in public management

Oracle Business Intelligence Database

**Commands used as a Technical Data Analyst PL by the Government of the State of São Paulo [Nov/2024 - present]
**NOTE: JANUARY 2025/ add searches used in SQL and XML in **SIGEO** (SIGEO: Budget Execution Management Information System), practically the federal government's database that enables the management and transparency of public spending, through the preparation of queries and reports.
**When I created the repository, I was working for the State of Minas Gerais, also as a Data Analyst PL; both the state governments of MG and SP use the same system.

## Repository Structure

- queries/: Contains SQL queries for data extraction

- notebooks/: Jupyter notebooks with exploratory analyses

- datasets/: Simulated data sets for testing

- docs/: Detailed documentation on each query and methodology

## Main Analyses Performed
## Importing and Connecting to the Database

The first step in data analysis is to establish the connection to the SIGEO database.

Database: Oracle Business Intelligence

## Data Cleaning and Processing

Initial inspection: Viewing the first rows and checking for missing values

Handling null values: Replacing them with an average or removing them as needed

Removing duplicates: Ensuring data integrity

Type conversion: Adjustments to facilitate analysis and visualization

Creating derived columns: Classifying indicators

## Extracting Key Indicators

Querying to obtain relevant information, such as:

Budget execution by agency

Comparison between initial and executed allocations

Distribution of commitments and payments by region and sector

Identifying patterns and anomalies in spending

## Viewing and Generating Reports

The processed and aggregated data is exported to Power BI, enabling interactive dashboards to monitor budget execution.

## Code Examples

SQL query to check the amounts committed by agency:

SELECT organ, SUM(valor_empromado) AS total_empromado
FROM execucao_orcamentaria
WHERE ano = 2024
GROUP BY organ
ORDER BY total_empromado DESC;

## Loading data into Pandas:

from sqlalchemy import create_engine
import pandas as pd

//Connect to the database
engine = create_engine('postgresql://usuario:senha@host:porta/database')
query = """
SELECT * FROM execucao_orcamentaria WHERE ano = 2024;
"""
df = pd.read_sql(query, engine)

Contact

For questions or collaborations, contact us via LinkedIn or email.

Author: Bel - Technical Data Analyst PL - Government of the State of São Paulo


