# list1 = [1, 5, 56, 67, "Anish", True, False, 4.56]
# print (list1)
# print(len(list1))
# print(type(list1))
# print(type(list1[7]))

# if "Anish" in list1:
#     print ("Yes")
# else:
#     print ("No")

#the elements of the list1 will get printed from the index of first number to the index of (last number - 1) with the jump in index
# print (list1[2:8:2])

# list2 = [i for i in range (5)]
# print (list2)

# list3 = [i*i for i in range(11) if i%2==0]
# print (list3)

list4 = [23, 11, 45, 67, 1, 3, 8, 10]
list5 = [1, 3, 2, 3, 4, 5, 1, 3, 2, 4, 6, 3, 4, 2, 7, 8, 3, 10]
list4.sort() # ascending order for the mixed list..... write list4.sort(reverse=True) for descending order
print (list4)
list4.append(99) # used to add a given element to the end of a list
print(list4)
# print(list5.index(2)) # used to return the index of the first occurence of a particular element in a list.
# print(list5.count(3)) # counts the number of occurences of a particular element in a list

list6 = [1, 2, 3, 4, 5]
m = list6.copy() # used to copy the list to another variable as it is without making any changes to the original list.
m[0] = 9
print (list6)
print(m)

list6.insert(2, 49) # used to insert a particular element at a particular index
print(list6)

list7 = [900, 1000, 1100]
list6.extend(list7) # used to add the elements of list 7 at the back of the list 6
print (list6)

list8 = [1,2,3]
list9 = ["a","b", "c"]
list10 = list8 + list9
print(list10)