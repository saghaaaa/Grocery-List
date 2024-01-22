#Sagha Axelsson Audrey Ringle
#1/11/24
#Grocery List

#Initiation
print("Welcome to your personal Grocery list")
Grocery = []

#Functions
def menu():
    for i in range(55):
        print("Please choose an option: Type in a number between 1-6")
        print("1. Add an item to the Grocery list \n2. View the current Grocery list \n3. Mark an item as complete \n4. Remove an item from the Grocery list \n5. Remove every item from the list \n6. Sort the list alphabetically \n7. Print the # of items on the list \n8. Quit the program")
        option=int(input("Option: "))
        if option ==1:
          newitem = input("What would you like to add?: ") 
          Grocery.append(newitem)
        if option==2:
            print(Grocery)
        if option ==3:
            completeitem = input("What item would you like to mark as complete?:")
            y = Grocery.index(completeitem)
            Grocery[y] = "X "+Grocery[y]
        if option == 4:
           removeitem = input("What would you like to remove?: ")
           Grocery.remove(removeitem)
        if option ==5:
            Grocery.clear()
        if option == 6:
            Grocery.sort(key=str.lower)
        if option == 7:
            print("This grocery list has "+str(len(Grocery))+" items on it.")
        if option ==8:
           print("Come back soon!")
           break
           
#Main
menu()