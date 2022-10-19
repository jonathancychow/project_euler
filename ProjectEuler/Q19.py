
import time, sys, os
import calendar


if __name__ == "__main__":
    tstart = time.time()
    answer = sum([1 for year in range(1901, 2000+1) for month in range(1,12+1) if calendar.monthcalendar(year,month)[0][calendar.SUNDAY] == 1])
    print('Answer = ',answer)
    tend = time.time()
    print('Run time for Q19 = ', tend - tstart, 's')

