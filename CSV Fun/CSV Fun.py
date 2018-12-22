'''
The purpose of this program is to read and edit a CSV (comma separated value) 
file so that we can easily calculate the total earnings from each run of barrows
by simply adding it into the program
'''

import csv 

user_input = 0 # will keep track of the user input
name = 0 # name of the CSV file
i = 0 # incrementing variable
column_names = [] # list of column names

# This first loop will ask the user if they want to edit or create a CSV file
while user_input != 1 and user_input != 2 and user_input != 3:
	print("\nDo you want to create, or edit an existing CSV file?")
	print("Input 1 to create, 2 to edit/add, or 3 to quit program")
	user_input = input()
	user_input = int(user_input)

if user_input == 1:
	print("\nWhat do you want to name the new CSV file")
	name = str(input())

	with open(name + ".csv", "w+") as csvfile:
		filewriter = csv.writer(csvfile, delimiter = ",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
		
		print("\nHow many columns do you want to create?")
		user_input = int(input())

		while i < user_input:
			print("\nInput name for column " + str(i + 1) + ": ")

			column_names.append(str(input()))
			i = i + 1
		
		filewriter.writerow(column_names)

	print("\nIf you did not get an error message, a new CSV file was created!")
	print("The program will end now, you can restart it to add new lines and do calculations.")	

elif user_input == 2:
	print("\nWhat is the name of the the CSV file you want to open (include .csv at the end)")
	name = str(input())

	with open(name, "r") as csvfile:
			reader = csv.reader(csvfile, delimiter=',')

			print("\nThis is how to CSV file currently looks like: \n")

			for row in reader:
				if i == 0:
					print("This is what each column represents: " + str(row))
				else:
					print("row " + str(i) + ": " + str(row))
				
				i = i + 1

			print("Add new entry? 1 for yes, 2 for no: ")

			user_input = 0

			while user_input != 1 and user_input != 2:
				user_input = int(input())

				if user_input != 1 and user_input != 2:
					print("Invalid input, input 1 for yes, 2 for no")

			

elif user_input == 3:
	exit()