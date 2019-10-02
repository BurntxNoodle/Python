cipher_text = input("input string here: ")

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

freq = []

### a = 97, z = 122
i = 97
temp = i
counter = 0

while i < 123:
	temp = chr(i)		
	for elem in cipher_text:
		if elem == temp:
			counter = counter + 1
	counter = str(counter) + " --> " + chr(i)	
	freq.append(counter)
	i = i + 1
	counter = 0

i = 97

print("\nFrequency analysis below:")
'''
for elem in freq:
	print(chr(i) + " --> " + str(elem))
	i = i + 1
'''

for elem in freq:
	print(elem)





