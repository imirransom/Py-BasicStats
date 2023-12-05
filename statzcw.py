import math

zcount = lambda lis: sum(lis)

zmean = lambda lis: zcount(lis) / len(lis)

def zmode(lis: list) -> float:
    max_count = 0
    max_freq = 0
    for ls in set(lis):
        counter = 0
        for l in sorted(lis):
            if l == ls:
                counter += 1
        if counter > max_count:
            max_count = counter
            max_freq = ls
    return max_freq


zmedian = lambda lis: lis[len(lis) // 2]

def zvariance(lis: list) -> float:
    new_lis1 = [x - zmean(lis) for x in lis]
    new_lis2 = [x*x for x in new_lis1]
    return zcount(new_lis2) / (len(lis) - 1)


zstddev = lambda lis: math.sqrt(zvariance(lis))

