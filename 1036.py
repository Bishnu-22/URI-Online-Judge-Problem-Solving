#import math
#a = float( input( ) )
#b = float( input( ) )
#c = float( input( ) )
#d= ( b*b ) - ( 4*a*c )
#math.sqrt(d)
#R1= ( ( -b + d ) % ( 2 * a ) )
#math.sqrt(d)
#R2= ( ( -b -d ) % ( 2 * a ) )
#if (a == 0) and (d>0) :
#    print ( "R1 = %.5f" %R1 )
#    print ( "R2 = %.5f" %R2 )
#else :
#    print ( "Impossivel calcular" )

##n=New Way Solution By Using "Impossivel calcular" in first:


#import  math
#input1 = input()
#input1 = input1.split()
#a = float( input1[0] )
#b = float( input1[1] )
#c = float( input1[2] )
#d= ( b*b ) - ( 4*a*c )
#R1 = ((-b + math.sqrt(d)) / (2*a))
#R2 = ((-b - math.sqrt(d)) / (2*a))
#if (a != 0) or (d < 0) :
#    print("Impossivel calcular")
#else :
 #   print("R1 = %.5f"%R1)
  #  print("R2 = %.5f"%R2)
## Bari Submit this:
import  math
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
if (A != 0):
    delta = (B * B) - (4 * A * C)
    if (delta > 0):
        x1 = (-B + math.sqrt(delta)) / (2 * A)
        x2 = (-B - math.sqrt(delta)) / (2 * A)
        print("R1 = %.5f" % x1)
        print("R2 = %.5f" % x2)
    elif (delta < 0):
        print("Impossivel calcular")
else:
    print("Impossivel calcular")