a, b = input().split()
a = int(a)
b = int(b)
c= b-a
if c<0 :
    c = 24 + (b - a)
if a==b :
    print("O JOGO DUROU 24 HORA(S)")
else :
    print("O JOGO DUROU %d HORA(S)"%c)
