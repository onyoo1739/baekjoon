a,b=map(int,input().split())
c=(((a%100)%10)*100)+(((a%100)//10)*10)+(a//100)

d=(((b%100)%10)*100)+(((b%100)//10)*10)+(b//100)
print(max(c,d))
