import math

def zcount(lis: list) -> float:
    count = 0
    for l in lis:
        count += 1
    return count

zmean = lambda lis: sum(lis) / zcount(lis)

def zmode(lis: list) -> float:
    max_count = 0
    max_freq = 0
    # making a new list as a set to be iterated through
    new_lis = [x for x in lis if x == x]
    for ls in new_lis:
        counter = 0
        for l in lis:
            if l == ls:
                counter += 1
        if counter > max_count:
            max_count = counter
            max_freq = ls
    return max_freq


zmedian = lambda lis: lis[zcount(lis) // 2]


def zvariance(lis: list) -> float:
    new_lis1 = [x - zmean(lis) for x in lis]
    new_lis2 = [x*x for x in new_lis1]
    return sum(new_lis2) / (zcount(lis) - 1)


zstddev = lambda lis: math.sqrt(zvariance(lis))

zstderr = lambda lis: math.sqrt(zstddev(lis) * zstddev(lis)) / math.sqrt(zcount(lis))

zcorr = lambda listx, listy: (zcount(listx) / zmean(listx)) / (zcount(listy) / zmean(listy))

