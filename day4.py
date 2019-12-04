#147981-691423 range
T = [str(a) for a in range(147981,691424)]
c = False #kryterium
r = 0
for i in range(len(T)):
    for j in range(len(T[i])-1):
        if int(T[i][j])>int(T[i][j+1]):
            c = False
            break
        if T[i][j]==T[i][j+1]:
            c = True
    if c==True:
        r+=1
        c = False
print(r)
