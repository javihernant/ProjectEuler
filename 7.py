import math

def solve():
    ls = list([2, 3])
    i = 4
    while (len(ls) < 10001):
        b = True
        for e in ls:
            if e < i and i%e == 0:
                b = False
                break
        if b:
            ls.append(i)
        i +=1 
    
    return ls[10000]

def main():
    print(solve())

if __name__ == '__main__':
    main()
