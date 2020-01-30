def fastPowerModP(k, m):
    if not (isinstance(k, int) and isinstance(m, int)):
        raise ValueError('Please only enter positive integers.')
    p = 10**9 + 7
    if m == 0:
        return 1
    if m == 1:
        return k
    if m % 2 == 0:
        return (fastPowerModP(k, m/2)**2) % p
    return k*fastPowerModP(k, m - 1) % p

def choose(n, r):
    p = 10**9 + 7
    out = 1
    rFactorial = 1
    for i in range(r):
        out = (out * (n - i)) % p
        rFactorial = rFactorial * (i + 1) % p
    return (out * fastPowerModP(rFactorial, p - 2)) % p

import time
def performance(func):
    def wrap(*args, **kwargs):
        start = time.time()
        try:
            func(*args, **kwargs)
        except ValueError as valErr:
            print(valErr)
        except TypeError as tE:
            print(tE)
        else:
            end = time.time()
            return -(start - end)
    return wrap

check = performance(choose)

@performance
def test1(n):
    for i in range(n):
        i*5

@performance
def test2(n):
    for i in list(range(n)):
        i*5

def iter_for(iterable):
    D = {}
    iterator = iter(iterable)
    while True:
        try:
            num = next(iterator)
            D[num] = num**2
        except:
            break
    return D

class Range:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = first
    def __init__(self, last):
        self.first = 0
        self.last = last
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.last:
            self.current += 1
            return self.current - 1
        raise StopIteration

def makeList():
    s = input()
    return(s.split(','))

if __name__ == '__main__':
    print('Testing123')

print(__name__)







