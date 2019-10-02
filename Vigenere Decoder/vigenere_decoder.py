'''
Given a list of words, use that list of words
to bruteforce vigenere ciphertext

Python3
'''

wordlist = input("Input name of txt with wordlist: ")

words = []

fp = open(wordlist, 'r')
words = fp.readlines()
fp.close()

length = len(words)
i = 0

while i < length:
	words[i] = words[i].strip()
	i = i + 1

'''
for elem in words:
	print(elem)
'''

ciphertext = input("Input ciphertext to brute force: ")

# Initializing variables/values:
decoded = ""
character = 0
temp = 0
temp2 = 0
i = 0

print("\n")

for word in words:
	length = len(word) # reset value
	i = 0 # reset value
	decoded = "" # reset value 
	print(word + ":")

	for elem in ciphertext:
		temp = ord(elem) - 97 # encrypted char
		temp2 = ord(word[i]) - 97 # key char
		character = (temp - temp2 + 26) % 26 # calculating decoded char
		decoded += chr(character + 97) # add the calculated decoded char

		i = i + 1 # increment to the next char in the key
		if i == length: # if statement to reset back to the first char
			i = 0

	print(decoded)
	print("\n")
