input1 = input()
input1 = input1.split()
a = int(input1[0])
b = int(input1[1])
c = int(input1[2])
d = int(input1[3])
e = c+d
f = a+b
if (b>c) and (d>a) and (e>f) and (c,d>0)  and (a%2 == 0) :
    print('Valores aceitos')
else :
    print("Valores nao aceitos")






