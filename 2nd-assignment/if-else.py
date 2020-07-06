#필수과제 1 성공
n = int(input().strip())
val = "Weird"
if n % 2 == 0:
    if n > 20 :
        val = "Not Weird"
    elif n >= 6:
        val = val
    else :
        val = "Not Weird"
print(val)