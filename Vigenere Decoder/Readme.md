# Brute Force Vigenere

Given a wordlist of common english words and text that you know was coded using the Vigenere cipher, it is possible to brute force it with this program.

Attached in this directory, is a wordlist containing 1000 common english words. Y

##### How to run

```python3 vigenere_decoder.py```

Then input the location of the potential wordlist and then input the string you want to decode.

I suggest outputting the program to a txt file so you can CTRL + F for some common plaintext words such as ```the```, ```and```, ```this``` and ```is```: ```python3 vigenere_decoder.py > output.txt```

Alternatively you can use ```grep``` by piping the output: ```python3 vigenere_decoder | grep the```

