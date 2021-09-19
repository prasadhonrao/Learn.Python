def Fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
inpu = int(input("Enter a Limit:"))
for j in range(inpu + 1):
    print(f"{j}! = ",Fact(j))
