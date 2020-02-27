import timeit
import os
code_c = '''
T = [2,6,2,2,5,3,44,2,5,8,7,0]

A = [0 for i in range(max(T)+1)]
    
for i in range(len(T)):
    A[T[i]]+=1
H = []
for i in range(len(A)):
    if A[i]>0:
        j = 0
        while j<A[i]:
            H.append(i)
            j+=1
print(H)



'''
code_b = '''
T = [2,6,2,2,5,3,44,2,5,8,7,0]
for i in range(len(T)):
    for j in range(len(T)):
        if T[j]>T[i]:
            z = T[i]
            T[i] = T[j] 
            T[j] = z
print(T)
'''
code_s = '''
T = [2,6,2,2,5,3,44,2,5,8,7,0]
for i in range(len(T)):
    min_inx = i
    for j in range(i+1,len(T)):
        if T[j]<T[min_inx]:
            min_inx = j
    T[i],T[min_inx] = T[min_inx],T[i]
print(T)
'''
code_i = '''
T = [2,6,2,2,5,3,44,2,5,8,7,0]
for i in range(1,len(T)):
    key = T[i]
    j = i-1
    while j>=0 and key<T[j]:
        T[j+1] = T[j]
        j-=1
    T[j+1] = key
print(T)
'''
b = timeit.timeit(stmt=code_b,number=10000)
c = timeit.timeit(stmt=code_c,number=10000)
i = timeit.timeit(stmt=code_i,number=10000)
s = timeit.timeit(stmt=code_s,number=10000)
T = [b,c,i,s]
T = sorted(T)
T = T[::-1]
print('''Ranking szybkości algorytmów sortowania\n''')
dict = {'Bubble sort':b,'Counting sort':c,'Insertion sort':i,'Selection sort':s}
dict = sorted(dict,key=lambda x: x[1])

print(dict)