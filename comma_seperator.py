# with open("numbers.txt", "r") as rf:
#     with open("hello.txt", "w") as wf:
#         for i in rf.readlines():
#             wf.write(i.replace("\n", ","))


with open("numbers.txt", "r") as rf:
    with open("hello.txt", "w") as wf:
        for i in rf.readlines():
            j = i.split("; ")[1]
            wf.write(j.replace("\n", ","))

        
        