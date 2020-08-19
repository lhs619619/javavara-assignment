#complete
def fibo(val):
    if val == 0:
        return 0
    elif val < 3:
        return 1
    else:
        return fibo(val-1) + fibo(val-2)

ans = []
for i in range(int(input())):
    ans.append(fibo(i)**3)
print(ans)

'''
#hackerrank.ver
cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        ret = [0,1]
        i = 2
        while(n>i):
            ret.append(ret[i-1] + ret[i-2])
            i += 1
        return ret

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
'''