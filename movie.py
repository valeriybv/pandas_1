import pandas as pd
import numpy as np
'''
Задание 1
Скачайте с сайта датасет любого размера. Определите, какому фильму было выставлено больше всего оценок 5.0.
'''
ratings = pd.read_csv('raw_data/ratings.csv')
df_5 = ratings.loc[np.where(ratings['rating'] == 5.0)]
print(df_5.groupby('movieId').count().sort_values('movieId', ascending=True).head())
