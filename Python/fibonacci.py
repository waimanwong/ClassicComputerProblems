import array

from functools import lru_cache

# Recursive approach
@lru_cache(maxsize=None)
def fib1(n: int) -> int:
    if n < 0: return None
    if n <= 1: return n

    return fib1(n-1) + fib1(n-2)

#iterative approach
def fib2(n:int) -> int:
    if n <= 0: return n
    
    last = 0 # fib(n-2)
    next = 1 # fib(n-1)

    for _ in range(1, n):
        # next = fib(n-2) + fib(n-1)
        # last = fib(n-1)  
        last, next = next, last + next

    return next

#sequence generator
def fib3(n: int) -> int:
    yield 0
    
    if n > 1: yield 1

    last = 0 # fib(n-2)
    next = 1 # fib(n-1)

    for _ in range(1, n):
        last, next = next, last + next
        yield next

def main():
    for i in range(0,50):
        print(f'{str(i)} -> {fib1(i)}, {fib2(i)}')

    for x in fib3(50):
        print (x)
    

if __name__ == '__main__':
    main()