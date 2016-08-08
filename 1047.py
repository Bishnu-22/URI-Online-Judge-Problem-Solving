#a, b, c, d = input().split()
#a = int(a)
#b = int(b)
#c = int(c)
#d = int(d)

#g = c-a
#if c-a<0 :
 #  g = 24+(c-a)

#e = d-b
#if d-b<0 :
  #  e = 60+(d-b)
 #   g = g+1

#if c==a and d==b :
#    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
#else :
#    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%g %e)


#Code By Tawhidi Bari:
def CalculateDuration(start, End):
    Duration = [0, 0]
    if start == End:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        while start == End:
            start[1] += 1
            Duration[1] += 1
            if start[1] == 60:
                start[0] += 1
                start[1] = 0
            if Duration[1] == 60:
                Duration[0] += 1
                Duration[1] = 0
            if start[0] == 24:
                start[0] = 0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(Duration[0], Duration[1]))
if __name__ == "__main__":
    data = [int(i) for i in input().split()]
start = [data[0], data[1]]
End = [data[2], data[3]]
CalculateDuration(start,End)