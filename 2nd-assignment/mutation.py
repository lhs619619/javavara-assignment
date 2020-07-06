#필수과제 3 성공
str = input()
index = int(input())
input_char = input()

if len(str) <= index:
    print("The number you gave is too large!")
else:
    print(str[:index] + input_char + str[index+1:])