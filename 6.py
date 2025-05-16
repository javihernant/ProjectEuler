import math

def solve():
    i = 1 
    a = 0
    while i <= 100:
        a += i
        i+=1
    a = a**2

    b = 0
    i=1
    while i <= 100:
        b += i**2
        i+=1
    return a - b

def main():
    print(solve())

if __name__ == '__main__':
    main()
