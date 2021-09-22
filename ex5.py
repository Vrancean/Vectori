x=[1,2,3,4,5]
s=0
for i in range(0,4):
    s+=i
print(s)
y=x
print(sum(y))
z=1
for i in range(0,len(x)):
    z=z*x[i]
print(z)
print(y[2])
print(x[0]+y[0])