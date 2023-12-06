import pandas as pd
import main


def csv_to_df(csv: str):
    return pd.read_csv(csv)


df = csv_to_df('dataOne.csv')

lisx = list(df['x'])
lisy = list(df['y'])


def statistics(listx, listy):
    wordx = lambda x: f'The {x} of x is '
    wordy = lambda y: f'The {y} of y is '

    print(wordx('count'), main.zcount(listx))
    print(wordy('count'), main.zcount(listy))


    print(wordx('mean'), main.zmean(listx))
    print(wordy('mean'), main.zmean(listy))

    print(wordx('variance'), main.zvariance(listx))
    print(wordy('variance'), main.zvariance(listy))

    print(f'The correlation for x and y is {main.zcorr(listx, listy)}')

    print(wordx('median'), main.zmedian(listx))
    print(wordy('median'), main.zmedian(listy))

    print(wordx('mode'), main.zmode(listx))
    print(wordy('mode'), main.zmode(listy))

    print(wordx('standard deviation'), main.zstddev(listx))
    print(wordy('standard deviation'), main.zstddev(listy))

    print(wordx('standard error of the mean'), main.zstderr(listx))
    print(wordy('standard error of the mean'), main.zstderr(listy))


print(statistics(lisx, lisy))
