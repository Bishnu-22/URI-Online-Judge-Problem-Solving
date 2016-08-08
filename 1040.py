number = input().split(" ")
N1, N2, N3, N4 = number
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
media = (N1*2 + N2*3 + N3*4 + N4*1)/(2+3+4+1)
print("Media: %.1f" %media)
if media<5.0:
    print('Aluno reprovado.')
elif media>=5.0 and media<=6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" %exame)
    final = (exame + media)/2
    if final >=5.0:
        print("Aluno aprovado.")
    else:
        print('Aluno reprovado.')
    print("Media final: %.1f" %final)
else:
    print("Aluno aprovado.")