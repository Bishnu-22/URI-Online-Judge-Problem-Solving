#import math
#input1 = input()
#input1 = input1.split()
#p = float(input1[0])
#q = float(input1[1])
#input2 = input()
#input2 = input2.split()
#r = float(input2[0])
#s = float(input2[1])
#t=2
#D = ((q-p)*(q-p)+(s-r)*(s-r))
#print("%.4f"%(math.sqrt(D))

import math
p1 = input().split(" ")
p2 = input().split(" ")
x1, y1 = p1
x2, y2 = p2
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
print('%.4f' %(math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))))


