import math


def primes():
    ls = list([2, 3])
    i = 4
    while (i<=20):
        b = True
        for e in ls:
            if e < i and i%e == 0:
                b = False
                break
        if b:
            ls.append(i)
        i +=1 
    
    return ls

def solve():
    ls_pms = primes()
    mp = dict([(p,0) for p in ls_pms])
    for n in range(2,21):
        for div in ls_pms:
            cnt = 0
            while (n % div == 0):
                n /= div
                cnt +=1
            if mp[div] < cnt:
                mp[div] = cnt
    sol = 1
    for p, power in mp.items():
        sol *= p**power

    return sol

def main():
    print(solve())

if __name__ == '__main__':
    main()
