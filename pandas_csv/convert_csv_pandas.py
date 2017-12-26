#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# Parsing, loading and simple processing using pandas

import numpy as np
import pandas as pd
from datetime import datetime

CSV = "../linear_regression_class/data_2d.csv"

X = pd.read_csv(CSV, header=None)

print(X)
X.info()
print(X.head(10)) # First 10 rows
print(X.iloc[0])  # First row (indexed) # Equivalent: X.loc[0]
#X.loc["a"]       # Row labeled with "a"
print(X[0])       # First column
print(X[[0, 2]])  # Columns 0 and 2
print(X[ X[0] < 5 ])  # All rows with first column value less than five
print(X[0] < 5)   # Boolean column
print(X.as_matrix())  # Convert to NumPy Array

CSV = "../airline/international-airline-passengers.csv"

"""
1 Header
Last 3 rows are irrelevant / trash
"""

print("AIRLINE")

df = pd.read_csv(CSV, engine="python", skipfooter=3)

# Check types
print(df.dtypes)

# Get some statistics
print(df.describe())

# Print the attributes
print(df.columns)

# Rename columns
df.columns = ["month", "passengers"]
print(df.columns)

# Retrieve column by label
print(df['passengers']) # Equivalent: df.passengers

# Add a column with fixed value
df['one'] = 1
df['two'] = 2
print(df.head())

# Remove columns without overwrite
print(df.drop(['one', 'two'], axis=1).head())

# Remove rows in place (overwrite)
df.drop(df.index[:3], inplace=True) # First 3 rows
print(df.head())

# Add columns based on the other column values
df['product'] = df.apply(lambda row: row.passengers * row.two, axis=1)

print(type(df.month[3]))
df.month = df.apply(lambda row: datetime.strptime(row.month, "%Y-%m"), axis=1)
print(df.head())
df.info()
print(type(df.month[3]))

# JOIN

CSV_1 = "../numpy_class/table1.csv"
CSV_2 = "../numpy_class/table2.csv"

t1 = pd.read_csv(CSV_1)
print(t1)

t2 = pd.read_csv(CSV_2)
print(t2)

m = t1.merge(t2, on='user_id')
print(m)
