str = input()
l=len(str)
flag=True
for i in range(l):
	if str[i]!=str[l-1-i]:
		flag= False
if flag:
	print("Palindrome")
else:
	print("Not a Palindrome")
