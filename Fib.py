import sys
import time


a: int = 0
b: int = 1
c: int = 1

while(True):
    print(f"{a}, ")
    a = b+c
    time.sleep(1)
    print(f"{b}, ")
    b = a+c
    time.sleep(1)
    print(f"{c}, ")
    c = a+b
    time.sleep(1)
