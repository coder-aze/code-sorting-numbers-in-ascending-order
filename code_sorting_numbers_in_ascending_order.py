list=[]
result=""
x=input("numbers: ")
#we separate the numbers
for i in x:
	list.append(i)
#we sort from small to large
while True:
	if len(list)==0:
		break
	else:
		result+=min(list)
		list.remove(min(list))
print(result)