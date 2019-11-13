def common_number(list1, list2):
 	list3=[]

	for i in list1: 
 		for j in list2:
 			if i==j:
 				list3.append(i)
 	print list3
list1=[1,2,34,6,7,89,54]
list2=[43,2,89,0,5]
print common_number(list1,list2)






#print(list3)

