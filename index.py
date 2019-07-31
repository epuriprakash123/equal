def ind(x):
	r=[]
	for i in range(n):
		if i==x[i]:
			r.append(x[i])
	return r
n=int(input())
l=list(map(int,input().split()))
k=ind(l)
if len(k)==0:
	print("-1")
else:
	print(*k)
