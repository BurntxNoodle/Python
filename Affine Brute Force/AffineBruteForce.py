'''
Affine brute force

A can't be a factor of 26
B can assume 0-25
'''

A = [1 ,3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] ### possible values of a
B = 0 ### can be any of 26
cipher_text = input("Input here what you want to decode: ")
decoded = ""
number = 1

def find_inverse(inverse, mod):
    inverse = inverse % mod
    ### for var in range(1, mod)
    var = 1
    flag = 0
    while flag == 0:
        if ((inverse * var) % mod) == 1:
            flag = 1
            ### print("Calculated the modular inverse is: " + str(var))
            return var
        
        var = var + 1
        ### print(var)        
    return 1 ### last case scenario 

def calculate_char(mod_inverse, beta, character):
    plaintext = (mod_inverse * (character - beta)) % 26
    return plaintext
    
for x in A:
    for y in range(26):
        for elem in cipher_text:
                temp = ord(elem) - 97 ### converting A -> 0
                temp2 = find_inverse(x, 26)
                temp3 = calculate_char(temp2, y, temp)
                temp = temp3 + 97
                temp = chr(temp)
                decoded += temp
                
        print("Possibility #" + str(number) + ": " + "String for Alpha=" + str(x) + " and Beta=" + str(y) + ": " + decoded)
        decoded = "" ### reset
        number = number + 1

### test = find_inverse(7, 26)
### print("calculated the modular inverse is: " + str(test))
