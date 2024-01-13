def dec1(n):
    bin = []
    reverbin = []
    while n >= 1:
        bin.append(n%2)
        n = n//2
    while len(bin) >= 1:
        reverbin.append(bin.pop())
    reverb = ''
    for i in reverbin:
        reverb += str(i)
    reverb = int(reverb)
    return reverb

dec_to_bin = int(input("Enter any number that you want to be converted in binary : "))
print(dec1(dec_to_bin))


