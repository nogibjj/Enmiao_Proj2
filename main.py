import pandas as pd
from pandasql import sqldf
import typer
from psycopg2.extras import NamedTupleCursor
from tabulate import tabulate

app = typer.Typer()

@app.command()
def display():
    """display table"""
    df = pd.read_csv('ds_salaries.csv')
    print(df)

@app.command()
def sortbysalary():
    """return sorted list by salary"""
    df = pd.read_csv('ds_salaries.csv')
    sorted = df.sort_values(by=['salary'],ascending = False)
    print(sorted)

if __name__ == "__main__":
    app()