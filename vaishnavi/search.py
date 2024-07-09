N=int(input("enter a number:"))
k=int(input("enter a key:"))
n=[1,2,3,4,5]
i=0
while i<N:
	if k==n[i]:
		print("found at",i,"th position")
		break
	i=i+1
else:
	print("not found")
