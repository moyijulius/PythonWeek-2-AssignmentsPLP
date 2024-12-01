#create empty list
my_list=[]
#append items one by one
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 15 at second position in the list
my_list.insert(1,15)
#extend my_list to other list
my_list.extend([50, 60, 70])
#deleting last element from my_list
my_list.pop()
#sort my_list in ascending order
my_list.sort()
 #Find the index of the value 30 in my_list
index_of_30=my_list.index(30)
#print the index of 30 in my_list
print("The index of 30 is:",index_of_30)
print("The final list is:",my_list)
