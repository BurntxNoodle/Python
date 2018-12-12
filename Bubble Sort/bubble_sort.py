# Bubblesort.py
# a program that will sort an integer array using Bubble Sort
# this program will also show the steps and each pass of the Bubble Sort

# bubble is the function that will sort the array 
def bubble(array):
    i = 0
    j = 0
    flag = 0
    pass_numb = 1
    length = len(array)

    while i < (length - 1):
        j = 0
        flag = 0

        while j < (length - (i + 1)):
            if int(array[j]) > int(array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = 1

            j = j + 1

            if j == (length - (i + 1)) and flag == 1:
                print("After pass " + str(pass_numb) + ": " + str(array))

        i = i + 1
        pass_numb = pass_numb +1 

    return array

# fancy introduction text block, code starts here
print("")
print("--------------")
print("|Bubble Sort!|")
print("--------------")
print("------------------------------------------------------")
print("|Please input a set of integers separated by spaces: |")
print("------------------------------------------------------")
print("")

number_array = input()
number_array = number_array.split(" ")

print("\nThe current array you have inputed: " + str(number_array) + "\n")

sorted_array = bubble(number_array)

print("\nThe number(s) after being sorted: " + str(sorted_array))