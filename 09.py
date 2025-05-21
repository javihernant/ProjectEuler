import math

def solve():
    i = 0
    while i <= 1000:
        j = i + 1
        while i + j <= 1000:
            k = 1000 - i - j
            if k <= j:
                break
            if i**2 + j**2 == k**2:
                return i * j * k
            j +=1
        i +=1

def main():
    print(solve())

if __name__ == '__main__':
    main()
