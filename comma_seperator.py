with open("numbers.txt", "r") as rf:
    with open("hello.txt", "w") as wf:
        for i in rf.readlines():
            wf.write(i.replace("\n", ","))

        
        