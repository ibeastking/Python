
#! tip to use zip
#! when there are multiple lists to iterate, then use the below approach

list1 = [1,2,3,4]
list2 = ["OM","Rahul","Sanket"]

#* for i in range(len(list1)):
#*     print(list1[i],list2[i])
#! the above code will show error bcoz one list is greater than other

for i,j in zip(list1,list2):
    print(i,j)