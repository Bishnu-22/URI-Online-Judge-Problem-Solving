n =int(input())
b_hundred = n/100

b_rest = n % 100
b_fifty = b_rest / 50
b_rest = b_rest % 50
b_twenty = b_rest / 20
b_rest = b_rest % 20
b_ten = b_rest / 10
b_rest = b_rest % 10
b_five = b_rest / 5
b_rest = b_rest % 5
b_two = b_rest / 2
b_rest = b_rest % 2
b_one = b_rest / 1
print(n)
print("%d nota(s) de R$ 100,00" %b_hundred)
print("%d nota(s) de R$ 50,00" %b_fifty)
print("%d nota(s) de R$ 20,00" %b_twenty)
print("%d nota(s) de R$ 10,00" %b_ten)
print("%d nota(s) de R$ 5,00" %b_five)
print("%d nota(s) de R$ 2,00" %b_two)
print("%d nota(s) de R$ 1,00" %b_one)