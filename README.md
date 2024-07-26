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

- Python 3.8+
- PostgreSQL
- Apache Airflow
- Docker (optional, for containerization)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/stefanosilva94/etl_pipeline.git
   cd etl_pipeline
```
