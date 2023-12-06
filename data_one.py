import pandas as pd
import main

df = pd.read_csv('dataOne.csv')

listx = list(df['x'])
listy = list(df['y'])

print(f'The count of x is {main.zcount(listx)}')
print(main.zcount(listy))

print(main.zmean(listx))

print(main.zvariance(listx))



