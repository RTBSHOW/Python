fruits=["Apple" ,"Banana" ,"Cherry" ,"Date" ,"Elderberry"]
print(fruits)
fruits[0]="Mango"
print(fruits) #Hence the list is mutable as we can change the value of an element in the list.
# unlike strings which are immutable and we cannot change the value of a character in a string.
print(fruits[1:3]) # This will print the second element of the list which is "Banana"
fruits.append("Lichie") # This will add "Lichie" to the end of the list
print(fruits) # This will print the modified list with "Lichie" added to
l1=[5,78,54,2,89,3]
l1.insert(3,234) # This will insert the value 234 at index 3 in the list
l1.sort() # This will sort the list in ascending order
print(l1) # This will print the sorted list in ascending order
l1.sort(reverse=True)
print(l1) # This will print the sorted list in ascending order
l1.pop(2) # This will remove the element at index 2 from the list
print(l1) # This will print the modified list with the element at index 2 removed
l1.remove(54) # This will remove the first occurrence of the value 54 from the list
print(l1) # This will print the modified list with the value 54 removed