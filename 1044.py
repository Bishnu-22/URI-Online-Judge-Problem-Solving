#a, b = input().split()
#a = float(a)
#b = float(b)
#if a%b==0 or b%a==0 :
 #   print("Sao Multiplos")
#else :
#    print("Nao sao Multiplos")
#1047 er code ta :

a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

g = c-a
if c-a<0 :
   g = 24+c-a

e = d-b
if d-b<0 :
    e = 60+d-b
    g = g-1

if c==a and d==b :
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else :
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(g,e))