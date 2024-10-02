import time
print(time.time())
t = time.localtime(time.time())
print(t)
localtime = time.asctime(t)
str = "Current Time: " + time.asctime(t)

print(str)