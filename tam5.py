letter=input("please enter sentence: ")
va="aoieuAOIEU"
list1=[]
for item in letter:
    if item in va and item not in list1:
        list1.append(item)
print(list1)        
        