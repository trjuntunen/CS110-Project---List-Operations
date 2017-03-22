mainList = ["USF","California","USA"]
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

def main():

	# Menu
	print("---------")
	print("1. Append")
	print("2. Check if in list")
	print("3. Index check")
	print("4. Remove")
	print("5. Insert")
	print("6. Join")
	print("---------")

	option = int(input("(1-6): "))

	# Option input validation
	while option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6:
		print("Enter a number 1-6")
		option = int(input("(1-6): "))

	if option == 1:
		item = input("Enter a value to append to the list: ")
		mainList.append(item)
		print(item,"added to the list.")
		continueOperations = input("Continue? (y/n): ")

		# Option 1 input validation
		while continueOperations != "y" and continueOperations != "n":
			print("You must enter 'y' or 'n'")
			continueOperations = input("Continue? (y/n): ")
		if continueOperations == "y":
			main()
		if continueOperations == "n":
			print("Shutting down")
			exit(0)

	if option == 2:
		item = input("Enter a value to check if it's in the list: ")
		while item not in mainList:
			print(item,"not in list")
			item = input("Enter a value to check if it's in the list: ")
		inList(mainList, item)
		continueOperations = input("Continue? (y/n): ")

		# Option 2 input validation
		while continueOperations != "y" and continueOperations != "n":
			print("You must enter 'y' or 'n'")
			continueOperations = input("Continue? (y/n): ")
		if continueOperations == "y":
			main()
		if continueOperations == "n":
			print("Shutting down")
			exit(0)

	if option == 3:
		if len(mainList) == 0:
			print("List does not have any items in it")
			main()
		item = input("Item to search?: ")
		whatIndex(mainList, item)
		continueOperations = input("Continue? (y/n): ")

		# Option 3 input validation
		while continueOperations != "y" and continueOperations != "n":
			print("You must enter 'y' or 'n'")
			continueOperations = input("Continue? (y/n): ")
		if continueOperations == "y":
			main()
		if continueOperations == "n":
			print("Shutting down")
			exit(0)

	if option == 4:
		item = input("Item to remove?: ")

		# Remove item input validation
		while item not in mainList:
			print(item,"not in list")
			item = input("Item to remove?: ")

		remove(mainList, item)
		print(item,"removed from list")
		continueOperations = input("Continue? (y/n): ")

		# Option 4 input validation
		while continueOperations != "y" and continueOperations != "n":
			print("You must enter 'y' or 'n'")
			continueOperations = input("Continue? (y/n): ")
		if continueOperations == "y":
			main()
		if continueOperations == "n":
			print("Shutting down")
			exit(0)

	if option == 5:
		item = input("Item to insert?: ")
		index = int(input("Index to insert item at?: "))

		while index > len(mainList):
			print("Index out of range")
			index = int(input("Index to insert item at?: "))
		insert(mainList, item, index)
		continueOperations = input("Continue? (y/n): ")

		while continueOperations != "y" and continueOperations != "n":
			print("You must enter 'y' or 'n'")
			continueOperations = input("Continue? (y/n): ")
		if continueOperations == "y":
			main()
		if continueOperations == "n":
			print("Shutting down")
			exit(0)


	if option == 6:
		join(list1,list2)

		continueOperations = input("Continue? (y/n): ")

		while continueOperations != "y" and continueOperations != "n":
			print("You must enter 'y' or 'n'")
			continueOperations = input("Continue? (y/n): ")
		if continueOperations == "y":
			main()
		if continueOperations == "n":
			print("Shutting down")
			exit(0)


		
def inList(mainList, item):
	counter = 0
	for i in mainList:
		if i == item:
			counter += 1
	if counter > 0:
		print(item,"is in the list")
		return True
	else:
		print(item,"is not in list")
		return False

def whatIndex(mainList, item):
	while item not in mainList:
		print(item,"not in list")
		item = input("Item to search?: ")
	counter = -1
	for i in mainList:
		counter += 1
		if i == item:
			print(item,"is at index",counter)

def remove(mainList, item):
	newList = []
	for i in mainList:
		if i != item:
			newList.append(i)
	print(newList)

def insert(mainList, item, index):
	counter = 0
	newList = []
	for i in range(len(mainList)):
		if counter == index:
			newList.append(item)
		newList.append(mainList[i])
		counter += 1
	print(newList)

def join(list1,list2):
	mergedList = list1 + list2
	print(mergedList)
	return mergedList

main()