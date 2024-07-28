# ETL Pipeline for Weekly Influenza Data

## Project Overview

This project implements an ETL (Extract, Transform, Load) pipeline designed to process player data from CSV files related to Premier League match gameweeks. The pipeline utilizes Airflow as the orchestrator, PostgreSQL as the database, and SQLAlchemy for ORM. 

## Architecture

### Components

- **Airflow**: Manages and schedules ETL workflows using Directed Acyclic Graphs (DAGs). It is set up to trigger the pipeline after each gameweek using cron scheduling.
  
- **PostgreSQL**: Stores the transformed data. SQLAlchemy is used to define the database models and handle database interactions.
  
- **SQLAlchemy**: An Object-Relational Mapping (ORM) tool used to interact with the PostgreSQL database.
  
- **Python Modules**: Includes modules for data manipulation, transformation, and loading.
  
- **Testing Framework**: Uses pytest for unit testing to ensure the reliability of the code.
  
- **Alembic**: Utilized for database schema management and migrations. It ensures that the database schema evolves correctly with application changes by generating and applying migration scripts.

## Workflow

1. **Extraction**:
   The pipeline extracts data from CSV files placed in the `data/raw/` directory.
  
2. **Transformation**:
   Data is cleaned, positions are standardized, columns are renamed, and new columns are added as required.
  
3. **Loading**:
   Transformed data is loaded into the PostgreSQL database using SQLAlchemy.
  
4. **File Management**:
    The processed file is moved to the `data/archived/` directory and archived.
  
5. **Orchestration**:
     Airflow triggers the ETL process based on a predefined schedule (e.g., after every gameweek).


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

   
