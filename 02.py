def solve():
    a=1
    b=2
    sumv=0
    while (a <= 4000000):
        if (a % 2 == 0):
            sumv+=a
        tmp = a
        a = b
        b = tmp + b
    return sumv

def main():
    print(solve())

if __name__ == '__main__':
    main()
