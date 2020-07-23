def calculatePi(n:int) -> float:
    pi : float = 0.0
    numerator = 4
    for i in range(n):
        sign = 1 if i % 2 == 0 else -1
        denominator = sign * (2*i + 1)
        pi += (numerator / denominator)
    
    return pi

if __name__ == "__main__":
    pi = calculatePi(1000000)
    print (pi)
