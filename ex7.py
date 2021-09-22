z = ['Lu', 'Ma', 'Mi', 'J', 'Vi', 'S', 'D']
v = [125,195,95,109,116,318,217] 
print(' venitul saptamanal:', sum(v))
print(' media venitului zilnic:', sum(v)/7)
print(' ziua cu cel mai mare venit:',z[v.index(max(v))])
print(' ziua cu cel mai mic venit:',z[v.index(min(v))])