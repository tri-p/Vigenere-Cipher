# Vigenere-Cipher
## About the project
It is a program written in Python that will translates the message and key to numbers corresponding with the letters in the alphabet (0-25). It will then add the values. If the values exceeded 25 (equivalent of Z), it will start counting back from 0 (equivalent of A). It then translates the numbers back into corresponding letter values in the alphabet, resulting to the ciphertext.

### To run the program
1. Open the file.
2. Input a message and a key.
3. Run the code and the output will be the ciphertext.

### Sample output
```
Message: LETSGOTOTHESHOW
Key: TICKET

Key Stream: TICKETTICKETTIC
Converted Message: 11 4 19 18 6 14 19 14 19 7 4 18 7 14 22
Converted Key: 19 8 2 10 4 19 19 8 2 10 4 19 19 8 2
Add: 30 12 21 28 10 33 38 22 21 17 8 37 26 22 24
Mod: 4 12 21 2 10 7 12 22 21 17 8 11 0 22 24

Ciphertext: E M V C K H M W V R I L A W Y
```
