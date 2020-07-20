import array

def fib1(n: int) -> int:
    if n < 0:
        return None

    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fib1(n-1) + fib1(n-2)


def main():
    for i in range(0,10):
        print(f'{str(i)} -> {fib1(i)}')

if __name__ == '__main__':
    main()