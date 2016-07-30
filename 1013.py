#value = input().split(" ")
#a, b, c = value
#a = int(a)
#b = int(b)
#c = int(c)
#AB = (a + b + abs(a-b))/2
#print("%d eh o maior" %((AB + c + abs(AB-c))/2))
import math
input1 = input()
input1 = input1.split()
a = int(input1[0])
b = int(input1[1])
c = int(input1[2])
Maior = ((a + b + abs(a - b)) / 2)
Maior2 = (((Maior + c + abs(Maior - c)) / 2))
print(int(Maior2), "eh o maior")
