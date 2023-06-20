#print list
list1=[2020,2021,2022]
print("list out the pandamic years:",list1)
#length
print(list.__len__(list1))
# insert,append,extend diff datatypes in list
list1.append("ohh pandamic is over")
print("ok man",list1)
list1.insert(4,True)
print("ok man",list1)

#increasing,decreasing orders
list3=[7,8,9,6,5,4]
list3.sort(reverse=True)
print("the list was sorted",list3)
#remove list item
del list3[0] 
print(list3)
del list3 
#copy list   
list4=["chitesh","kumar","prasad"]
print("ok lets 'copy' the list",list4.copy())
print("using 'list' to copy",list(list1))
#sort list
print(list4.append("anna ayyii"),list4)
print(list1+list4) #join list 
print("ok sorted",list4.sort(),list4)                        
#reverse list
list2=[1,2,3,4,5]
print("lets reverse it",list.reverse(list2),list2)
list5=["chitesh","chitesh",1,1,3,4]
print(" haaa'count' my name",list5.count("chitesh"))
print("haaa'count'the num",list5.count(1))
#index of the list
print("ok index",list5.index(1))

