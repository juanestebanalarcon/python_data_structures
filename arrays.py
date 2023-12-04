'''
Author: juanestebanalarcon
Exercise: List/Array operations
'''
print("Add a new element using append(): ",end=" ")
def addFruit():
    fruits_list = []
    new_fruit = input("Please type the name of your new fruit: ").upper()
    fruits_list.append(new_fruit)
    if new_fruit is '':
        new_fruit = input("Please type the name of your new fruit: ").upper()
    return fruits_list
def insertElementPosition(fruitList:list,pos:int,fruitName:str):
    fruitList.insert(pos,fruitName)
    print(f"Current elements in fruit list: {fruitList}")
    return fruitList
    pass 
try:
    fruitList=addFruit()
    isAdd = input("Do you want to add another fruit?: Y/N").upper()
    if isAdd is 'Y':
        fruitList=addFruit()

except Exception as e:
    print(f"Error encountred while trying to add a new fruit: {e}")
print("Order the fruits list using sort(): ",end=" ")
print(fruitList.sort())
print("Delete the last element in the list using the method pop(): ",end=" ")
fruitList.pop()
print(f"Fruit list: {fruitList}",end="")
print("Insert element in the list using the method insert(): ",end=" ")
pos =int(input("Type the position to insert the element in the list: "))
fruitName=input("Type the name of the fruit: ",end="")
fruitList=insertElementPosition(fruitList,pos,fruitName)
print(f"Fruit list: {fruitList}",end="")
print("Delete the last element in the list using the method renove(): ",end=" ")
fruitList.remove(input("Type the name of the fruit that you want to delete: ").upper())
print(f"Fruit list: {fruitList}",end="")

