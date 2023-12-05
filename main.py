from statzcw import zcount
from statzcw import zvariance
from statzcw import zstddev
from statzcw import zmode
from statzcw import zmedian
from statzcw import zstderr
from statzcw import zcorr

print(zcount([2, 4, 5, 456]))

print(zvariance([46, 69, 32, 60, 52, 41]))

print(zstddev([9, 24, 31]))

print(zmode([1, 2, 3, 7, 7, 7, 4, 4, 5, 6,  8, 8]))

print(zmedian([12, 34, 54, 45, 34]))

print(zstderr([67, 78, 89, 90]))

print(zcorr([1, 2, 3], [10, 20, 27]))