#complete. members list 내의 변수 int 자료형 변환 위해 map 함수 참고함.
k,members = int(input()),list(map(int, input().split()))

mem_set = set(members)

print(((sum(mem_set)*k)-(sum(members)))//(k-1))