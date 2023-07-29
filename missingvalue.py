import numpy as np
import pandas as pd
from pandas import DataFrame, Series

myseries = Series(['강', '이', np.nan, '광'])
print(myseries)
print(myseries[myseries.notnull()])
print(myseries.dropna())

