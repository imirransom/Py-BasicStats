import math

def zcount(lis: list) -> float:
    count = 0
    for elem in lis:
        count += 1
    return count

zmean = lambda lis: sum(lis) / zcount(lis)

def zmode(lis: list) -> float:
    max_count = 0
    max_freq = 0
    # making a new list as a set to be iterated through
    new_lis = [c for c in lis if c == c]
    for ls in new_lis:
        counter = 0
        for li in lis:
            if li == ls:
                counter += 1
        if counter > max_count:
            max_count = counter
            max_freq = ls
    return max_freq


zmedian = lambda lis: lis[zcount(lis) // 2]


def zvariance(lis: list) -> float:
    new_lis1 = [a - zmean(lis) for a in lis]
    new_lis2 = [b*b for b in new_lis1]
    return sum(new_lis2) / (zcount(lis) - 1)


zstddev = lambda lis: math.sqrt(zvariance(lis))

zstderr = lambda lis: math.sqrt(zstddev(lis) * zstddev(lis)) / math.sqrt(zcount(lis))


def zcov(listx: list, listy: list) -> float:
    ans = 0
    for i in range(0, zcount(listx)):
        ans += ((listx[i] - zmean(listx)) * (listy[i] - zmean(listy)))
    return ans / (zcount(listx) - 1)


zcorr = lambda listx, listy: zcov(listx, listy) / (zstddev(listy) * zstddev(listy))

