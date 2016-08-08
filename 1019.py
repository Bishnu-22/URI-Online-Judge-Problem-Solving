n = int(input())
h = n/3600
bi_rest = n%3600
m = bi_rest/60
bi_rest = n%60
s = bi_rest
print("%d:%d:%d" %(h,m,s))
