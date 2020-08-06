def calc(x1, y1, x2, y2) :
    abs_2 = x2**2+y2**2
    print("{0:.2f}{1:+.2f}i".format(x1+x2, y1+y2))
    print("{0:.2f}{1:+.2f}i".format(x1-x2, y1-y2))
    print("{0:.2f}{1:+.2f}i".format(x1*x2-y1*y2, x1*y2+x2*y1))
    print("{0:.2f}{1:+.2f}i".format((x1*x2+y1*y2)/abs_2, (-x1*y2+x2*y1)/abs_2))
    print("{0:.2f}{1:+.2f}i".format((x1**2+y1**2)**0.5, 0))
    print("{0:.2f}{1:+.2f}i".format(abs_2**0.5, 0))

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
calc(x1, y1, x2, y2)