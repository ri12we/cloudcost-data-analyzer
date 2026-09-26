# Cloud Cost Data Analyzer

A beginner-to-intermediate Python data analytics project designed to practice analyzing cloud spending data.

> **Note:** The dataset in this project is fictional and is used only for learning. It is not real company billing data.

## What this project does

The program:

- Loads cloud-cost data from a CSV file
- Checks for missing values
- Calculates total cloud spending
- Groups costs by service and department
- Calculates monthly spending
- Calculates month-over-month percentage changes
- Identifies the highest-cost service
- Creates charts for cloud spending

## Technologies

- Python
- Pandas
- Matplotlib
- CSV data
- Basic data analysis

## How to run

1. Install Python.
2. Open this folder in VS Code.
3. Open the terminal.
4. Install the required libraries:

```bash
pip install -r requirements.txt
```

5. Run:

```bash
python cloud_cost_analyzer.py
```

## Example questions this project answers

- Which cloud service costs the most?
- How much did the organization spend overall?
- Which department has the highest spending?
- How does spending change each month?
- Are cloud costs increasing or decreasing?

## Skills demonstrated

This project demonstrates beginner-to-intermediate skills in:

- Data cleaning and validation
- Data aggregation
- Grouping and sorting
- Percentage-change calculations
- Data visualization
- Python programming
- Interpreting data

## Possible next steps

Future versions could add:

- SQL
- A SQLite database
- A small dashboard
- More cloud providers
- Cost alerts
- Snowflake for cloud data warehousing
