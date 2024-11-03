letter=input("please enter sentence: ")
va="aoieuAOIEU"
list1=[]
for item in va:
    if item in letter and item not in list1:
        list1.append(item)
print(list1)        
        