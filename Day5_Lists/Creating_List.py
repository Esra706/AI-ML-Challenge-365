#creating list 
fruits=["Apple","Banana","Cherry","Mango","Blueberry"]
print(fruits[0]) #Apple
print(fruits[1]) #Banana
print(fruits[2]) #Cherry
print(fruits[3]) #Mango
print(fruits[4]) #Blueberry
print(fruits[-1]) #Blueberry
print(fruits[1:4])

#Methods
#.append() (adding item in last)
fruits.append("Orange")
print(fruits) #['Apple', 'Banana', 'Cherry', 'Mango', 'Blueberry', 'Orange']

#.remove()  (Remove item from list)
fruits.remove("Banana")
print(fruits) #['Apple', 'Cherry', 'Mango', 'Blueberry', 'Orange']


# .pop()  (Remove item according to index number)
fruits.pop(0)
print(fruits) #removed apple


#.sort() sorted list A-Z
fruits.sort()
print(fruits)