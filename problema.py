x=""
with open('input.txt','r')as f:
    x=f.readline()
x=str(x)
l=x.split()
for i in range(len(l)):
    l[i]=int(l[i])
print(l)
print(sorted(l))
y=(sorted(l))
y.reverse()
print(y)
print(len(l))
print(max(l))
print(min(l))
y=l.copy()
y.append(111)
print(y)
y=l
y.insert(1,222)
print(y)


