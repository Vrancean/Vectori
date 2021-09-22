h=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[1,3,5,7,9,11,13,15,17,19,21,23,22,20,18,16,14,12,10,8,6,4,2,0]
print('Temperatura medie= ', round(sum(t)/24,1))
print('Maximul= ',max(t))
print('Minimul= ',min(t))
print('Ora la care s-a inregistrat temperatura maxima: ',h[t.index(max(t))])
print('Ora la care s-a inregistrat temperatura minima: ',h[t.index(min(t))])