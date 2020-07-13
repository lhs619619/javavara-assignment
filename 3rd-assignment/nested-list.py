#complete
n = int(input())
stu_dict = {}
stu_list = []
check_score = 0
for i in range(n):
    stu_name = input()
    stu_score = input()
    stu_dict[stu_name] = float(stu_score)
stu_dict = sorted(stu_dict.items(), key = lambda x : x[1])
for i in range(n):
    score = stu_dict[0][1]
    if score < stu_dict[i][1]:
        if check_score != 0 and check_score < stu_dict[i][1]:
            break
        check_score = stu_dict[i][1]
        stu_list.append(stu_dict[i][0])
print("\n".join(sorted(stu_list)))