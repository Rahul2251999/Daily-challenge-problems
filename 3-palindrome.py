k = int(input())
s = ""
if k==1:
	print('a')
elif k==2:
	print('aa')
elif k==3:
	print('bba')
else:
	for i in range(k/4):
		s+="aabb"
	h = k%4
	if h==0:
		pass
	elif h==1:
		s+='a'
	elif h==2:
		s+='aa'    #shfue
	elif h==3:
		s+='aab'
print(s)
