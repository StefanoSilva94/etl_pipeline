# ETL Pipeline for Weekly Influenza Data

## Project Overview

This project implements a reproducible ETL (Extract, Transform, Load) pipeline to process weekly influenza data sourced from the WHO. The pipeline is orchestrated using Apache Airflow and performs the following tasks:

1. **Download**: Retrieve the latest weekly influenza data in CSV format.
2. **Read and Clean**: Load the CSV file into a Pandas DataFrame and perform data cleaning.
3. **Transform**: Aggregate and engineer features to prepare the data for analysis.
4. **Load**: Store the cleaned and transformed data in a PostgreSQL database.
5. **EDA**: Conduct exploratory data analysis (EDA) to understand the data characteristics.
6. **Visualization**: Generate visualizations to present the data insights.


## Setup and Installation

### Prerequisites

- Python 3.8+ (required for Airflow)
- PostgreSQL
- Apache Airflow

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/stefanosilva94/etl_pipeline.git
   cd etl_pipeline

2. **Install Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. **Configure Airflow**
   Follow the Airflow documentation: https://airflow.apache.org/docs/apache-airflow/stable/start.html

4. **Configure PostgreSQL**
   Set up a PostgreSQL instance and upgrade to the latest version of the database by running:
   ```bash
   alembic upgrade head
   
5. **Configure Environment Variables**
   A config file is used to load enviornment variables. Set up your .env file to match the variables shown in config.py

6. **Run the pipeline**
   Start Airflow and trigger the pipeline DAG:

   ```bash
   airflow standalone


   Alternatively, the code can be run locally by running src/clean_and_transform.py and then running src/load.py

   
