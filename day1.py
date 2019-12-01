with open("day1_input.txt","r") as x:
    s = x.read()
    s = s.split()
    T = []
    for i in range(len(s)):
        T.append(int(s[i]))

    def transform(n):
        n = n/3
        n = n//1
        n-=2
        return n

    r = 0
    for i in T:
        r+=transform(i)
    print(int(r))
