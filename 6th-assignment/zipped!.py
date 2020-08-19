#complete
n, x = map(int, input().split())
ans = [0.0]*n
for i in range(x):
    score = map(float, input().split())
    ans = [sum(i) for i in zip(ans, score)]
ans = map(str, [round(i/x, 1) for i in ans])
print("\n".join(ans))