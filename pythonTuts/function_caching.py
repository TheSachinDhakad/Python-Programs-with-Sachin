import datetime
import time
from functools import lru_cache
@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("now runing some work...")

    some_work(3)
    print("Done ... Calling Again")
    some_work(3)
    print("Called Again....")