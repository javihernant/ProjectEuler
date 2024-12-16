def solve():
    top = 1000
    sumv=0
    i=3
    while (i<top):
        if (i % 3 == 0 or i % 5 == 0):
            sumv+=i
        i+=1
    return sumv

def main():
    print(solve())

if __name__ == '__main__':
    main()
