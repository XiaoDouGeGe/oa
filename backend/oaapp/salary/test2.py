#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pandas as pd

file_path = './xxx.xls'
data_frame = pd.read_excel(file_path, sheet_name=0, header=None, dtype=str)

for index, row in data_frame.iterrows():
    for column in data_frame.columns:
        cell_data = row[column]
        print(f"Cell at ({index}, {column}): {cell_data}")
