list1=["pride",206,"i20","i8"]
list2=["pride",207,"i30","i8"]
list3=[]
for item in list1:
    if item not in list2:
        list3.append(item)
print(list3)        