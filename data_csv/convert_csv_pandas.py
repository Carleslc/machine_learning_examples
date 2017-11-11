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

df = pd.read_csv(CSV, engine="python", skipfooter=3)

print(df.columns)

# Rename columns
df.columns = ["month", "passengers"]
print(df.columns)

# Retrieve column by label
print(df['passengers']) # Equivalent: df.passengers

# Add a column with fixed value
df['two'] = 2
print(df.head())

# Add columns based on the other column values
df['product'] = df.apply(lambda row: row.passengers * row.two, axis=1)

type(df.month[0])
df.month = df.apply(lambda row: datetime.strptime(row.month, "%Y-%m"), axis=1)
print(df.head())
df.info()
type(df.month)

# JOIN

CSV_1 = "../numpy_class/table1.csv"
CSV_2 = "../numpy_class/table2.csv"

t1 = pd.read_csv(CSV_1)
print(t1)

t2 = pd.read_csv(CSV_2)
print(t2)

m = t1.merge(t2, on='user_id')
print(m)
