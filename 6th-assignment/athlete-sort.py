#compléter
import operator

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
k = int(input())

arr.sort(key=lambda x: x[k])
for _ in arr:
    print(*_)

"""#잔해물
n, m = map(int, input().split()) #input
arr = [input() for _ in range(n)]
k = int(input())

for i in range(n): #dictionary
    dic[int((arr[i].split())[k])] = arr[i]
dic = dict(sorted(dic.items(), key=lambda x:x[0]))

for key, value in dic.items():
    print(value)
"""