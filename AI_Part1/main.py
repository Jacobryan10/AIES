# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np

df = pd.read_csv('toxity_per_attribute.csv', low_memory=False)
print(df.head())
