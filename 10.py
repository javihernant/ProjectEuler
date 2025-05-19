def solve():
    ls = [ 1 for i in range(2000000)]
    i = 2
    while (i < 2000000):
        j = i+i
        while ( j < 2000000):
            ls[j] = 0
            j += i
        i += 1

    sm = 0
    i= 2
    while (i < 2000000):
        if ls[i]:
            sm += i
        i+=1
    return sm

def main():
    print(solve())

if __name__ == '__main__':
    main()
