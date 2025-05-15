import math

def pali(num):
    count = None
    if num // 100000 == 0: 
        count = 2
        f = 10000
    else:
        count = 3
        f = 100000
    tmp_num = num
    while count > 0:
        a = (num // f) % 10
        b = tmp_num % 10
        #print(a, b)
        if (a != b):
            return False
        tmp_num //= 10
        f /= 10
        count -= 1
    return True

def solve():
    num = 0
    i = 100
    while (i <= 999):
        j = i
        while (j <= 999):
            tmp = i * j
            if (tmp > num and pali(tmp)):
                num = tmp
            j+=1
        i+=1
    return num

def main():
    print(solve())

if __name__ == '__main__':
    main()
