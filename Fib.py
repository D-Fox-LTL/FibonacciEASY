import sys
import time
a: int = 0
b: int = 1
while(True):
    print(f"{a}, ")
    a = a+b
    time.sleep(1)
    print(f"{b}, ")
    b = b+a
    time.sleep(1)
