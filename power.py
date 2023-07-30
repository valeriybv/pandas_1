import pandas as pd


'''
Задание 2
По данным файла power.csv (находится в архиве в разделе Материалы к лекции «Библиотека Pandas» - 
файл “Дополнительные файлы для домашнего задания”) посчитайте суммарное потребление стран Прибалтики 
(Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 год. 
Не учитывайте в расчётах отрицательные значения quantity.
'''

power = pd.read_csv('raw_data/10._Основы_pandas/power.csv')
power_filtered = power.loc[((power['category'] == 4)|(power['category'] == 12)|(power['category'] == 21))
                            & ((power['country'] == 'Latvia') | (power['country'] == 'Lithuania') | (power['country'] == 'Estonia'))
                            & (power['year'] >= 2005)
                            & (power['year'] <= 2010)
                            & (power['quantity'] >= 0)]

print("Суммарное потребление стран Прибалтики = ",power_filtered['quantity'].sum())