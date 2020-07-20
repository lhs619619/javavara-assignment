#complete

#recursion 1 - time error
"""def super_digit(P):
    if P < 10:
        print(P)
        return 0
    sum = 0
    while 1:
        sum += P%10
        P //= 10
        if P < 10:
            super_digit(sum+P)
            break"""

#recursion-optimized - time error
"""def super_digit(P):
    if P < 10:
        print(P)
        return 0
    return super_digit(sum(map(int, str(P))))

P, k = input().split()
super_digit(int(P*int(k)))"""

#Math is ddabong
P, k = map(int, input().split())
print(P*k % 9 if P*k % 9 else 9)