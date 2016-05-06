
s = 0
for i in range(1,1001):
    s = s + i**i

strval = str(s)
last10 = strval[-10:]
print("Last 10 are: " + last10)