n = int(input())
y = n/365
m = n%365/30
f = n%365%30
print("%d ano(s)"%y)
print("%d mes(es)"%m)
print("%d dia(s)"%f)