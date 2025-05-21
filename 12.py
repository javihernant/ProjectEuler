import math

def count_divs(num):
    cnt = 0
    i = 1
    while ( i*i <= num):
        if num % i == 0:
            if i*i != num:
                cnt += 2
            else:
                cnt += 1
        i += 1
    return cnt

def solve():
    n = 2
    while True:
        if n%2 == 0:
            a = n // 2
            b = n+1
            if (count_divs(a) * count_divs(b) > 500):
                return (a * b)
        else:
            a = ( n + 1) // 2
            b = n
            if (count_divs(a) * count_divs(b) > 500):
                return (a * b)
        n +=1



def main():
    print(solve())

if __name__ == '__main__':
    main()
