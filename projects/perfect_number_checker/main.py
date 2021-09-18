inpu = int(input("Enter a Number to Check:"))
factors=0
for i in range(1,inpu):
	if(inpu%i == 0):
		factors +=i
if(inpu == factors):
	print(f"{inpu} is Perfect Number")
else:
	print(f"{inpu} is not a Perfect Number")
