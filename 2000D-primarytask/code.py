def important_integer(n):
    n=str(n)
    if len(n)<=2:
        return 'no'
    elif len(n)==3:
        if n[0]=='1' and n[1]=='0' and n[2]!='0' and n[2]!='1':
            return 'yes'
        else:
            return 'no'
    elif len(n)>=4:
        if n[0]=='1' and n[1]=='0' and n[2]!='0':
            return 'yes'
        else:
            return 'no'
t=int(input())
for _ in range(t):
    n=int(input())
    ans=important_integer(n)
    print(ans)
