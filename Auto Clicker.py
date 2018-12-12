'''
This program will make an auto clicker that is customized
at runtime by user. Think of it as a template.

NOTE: Cannot click beyond 1920x1080 monitor
'''

import pyautogui
import time

numb_locations = 0 # Stores the number of locations the user wants to auto click
i = 0 # Counter variable
loop_counter = 0 # Counter to count the amount of loops
response = 0 # flag variable to store user response
is_ready = 0 # flag variable to store if the user is ready
num_clicks = 0 # stores the amount of clicks for each location the user wants
time_delay = .75 # time delay between each click in seconds
loop_delay = 5 # time delay between each cycle of location clicks to be able to CNTRL + C when done
positions = [] # going to hold the positions as tuple
right_clicks = [] # stores the right click location numbers

# Introduction to main code
print("\nAuto Clicker! Press CTRL + C anytime to quit\n")
print("Please input the number of different locations that are going to be clicked")

numb_locations = input('Please enter a singular integer then press "ENTER": ')

print("\nGoing to generate an autoclick for " + numb_locations + " different locations")

# For loop that scans in the locations whenever the user types in r
while i < int(numb_locations):
	print("\nHover over (but do not click) where you want to autoclick for location " + str(i + 1))

	while is_ready != 'r':
		is_ready = input("Press \"r\" then press the enter key when you are ready: ")

		if is_ready != 'r':
			print("Invalid input\n")

	positions.append(pyautogui.position())

	is_ready = 0
	i = i + 1

# Prompts user and asks them if they want any of the locations to be right click, while loop stores those
# locations that will be right clicked into a list
print("\nThis program's default is to left click everything.")
response = input("Do you want to right click anything? Input \"y\" for yes or \"n\" for no: ")

while response == 'y':
	i = int(input("\nEnter the location  number that was stored that you want to right click: "))
	right_clicks.append(i-1)
	response = input("Do you want to right click anything else? Input \"y\" for yes or \"n\" for no:  ")

# Prompts user and asks them if they want to change the default time delay which is currently
# set at .75 seconds of time delay. 
print("\nDefault time delay is .75 seconds, do you want to change that?")
response = input("Input \"y\" for yes or \"n\" for no: ")

if response == 'y':
	time_delay = input("Enter the new delay (in seconds) between each click: ")

# Prompts user and asks them how many times they want each location to be clicked
num_clicks = input("\nHow many times do you want each location to be clicked?: ")

# while loops to execute the clicks
while loop_counter < int(num_clicks):
	i = 0

	while i < int(numb_locations):
		if i in right_clicks:
			pyautogui.rightClick(positions[i])
		else:
			pyautogui.click(positions[i])

		time.sleep(int(time_delay))
		i = i + 1

	loop_counter = loop_counter + 1
