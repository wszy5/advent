#147981-691423 range
T = [str(a) for a in range(147981,691424)]
c = False #standard
r = 0
for i in range(len(T)):
    for j in range(len(T[i])-1):
        if int(T[i][j])>int(T[i][j+1]):
            c = False
            break
        if T[i][j]==T[i][j+1] and T[i].count(T[i][j])==2: #modify for 2 part
            c = True
    if c==True:
        r+=1
        c = False

print(r)
