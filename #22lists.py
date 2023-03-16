mylist = ['2']
mylist.append(4)
mylist.append(5) #append is used to add on value at the end
mylist.extend([23, 56, 89]) #insert is used to add more than one value
mylist.insert(3, 222) #insert is used to add a value at a particular index
mylist.remove(222) #insert removes the particular value given in the parenthesis
mylist.pop(3) #pop removes the value of particular index
for i in range (7, 15):
    mylist.append(i)
print(mylist)