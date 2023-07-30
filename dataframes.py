import pandas as pd
from datetime import datetime

dataframes = pd.read_html('https://fortrader.org/quotes', converters={'Обновлено' : str})
print(len(dataframes))
print(dataframes[0].head())