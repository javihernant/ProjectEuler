import math

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2 or n == 3):
        return True
    i = 2
    top = math.sqrt(n)+1
    while (i< top):
        if (n % i == 0):
            return False
        i +=1
    return True


def solve():
    num = 600851475143
    i = 2
    while (i < num):
        if (num % i == 0):
            mul = num/i 
            if (is_prime(mul)):
                    return mul
        i+=1
    return i

def main():
    print(solve())

if __name__ == '__main__':
    main()
