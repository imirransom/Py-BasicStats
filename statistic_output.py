import pandas as pd
from statzcw import zcount, zmean, zvariance, zstddev, zmode, zmedian, zstderr, zcov, zcorr

def csv_to_df(csv: str):
    return pd.read_csv(csv)


def statistics(listx, listy):
    wordx = lambda x: f'The {x} of x is '
    wordy = lambda y: f'The {y} of y is '

    print(wordx('count'), zcount(listx))
    print(wordy('count'), zcount(listy))

    print(wordx('mean'), zmean(listx))
    print(wordy('mean'), zmean(listy))

    print(wordx('variance'), zvariance(listx))
    print(wordy('variance'), zvariance(listy))

    print(f'The correlation for x and y is {zcorr(listx, listy)}')

    print(wordx('median'), zmedian(listx))
    print(wordy('median'), zmedian(listy))

    print(wordx('mode'), zmode(listx))
    print(wordy('mode'), zmode(listy))

    print(wordx('standard deviation'), zstddev(listx))
    print(wordy('standard deviation'), zstddev(listy))

    print(wordx('standard error of the mean'), zstderr(listx))
    print(wordy('standard error of the mean'), zstderr(listy))
