#complete
lower,upper,odd,even=[],[],[],[]
for i in sorted(input()):
    if i.isalpha():
        upper.append(i) if i.isupper() else lower.append(i)
    else:
        odd.append(i) if int(i)%2 else even.append(i)
print("".join(lower+upper+odd+even))