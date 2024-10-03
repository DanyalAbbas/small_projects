# FIBONACCI SEQUENCE
# 0 1 1 2 3 5 8 13 etc
def fibo_seq(num):
    a = 0
    b = 1
    umm = []
    if num == 1:
        print(a)
    elif num == 2:
        print(a,b)
    else:
        umm.append(str(a))
        umm.append(str(b))
        for i in range(0,num - 2):
            umm.append(str(a+b))
            c = a+b
            a = b
            b = c
    return " ".join(umm)

print(fibo_seq(8))

