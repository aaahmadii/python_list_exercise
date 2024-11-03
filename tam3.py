list1=["amirali","ps5",12,"tehran"]
list2=["amirali","ps3",12,"shiraz"]
list3=[]
for item in list1:
    if item in list2:
        list3.append(item)
print(list3)        