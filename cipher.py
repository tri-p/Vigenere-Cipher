# PABUNA, KATRINA B.
# PROBLEM 3: THE VIGENERE CIPHER
# Pseudocode
# Take user's inputs for message and key. Convert them into uppercase letter. The input message or key should not have spaces
input_str = ""
while input_str != 1:
    message = input("Enter your Message: ").upper()
    key = input("Enter your Key: ").upper()
    if " " in message or " " in key:
        print("ERROR. There should be no spaces on both inputs. Try again.")
        continue
    else:
        break

print("Message:", message)
print("Key:", key)

# Create a dictionary to map each alphabet to a number
# Create a dictionary to map each number to an alphabet
# Match the length of the key to the length of the message by repeating it
# Convert each character in message to its corresponding number and append to a list
# Convert each character in key to its corresponding number and append to a list
# Add each value in the converted message and key and append to a list
# If the sum of the values exceed 25, reduce it to its modular value and append to a list
# Convert each value in modular values to its corresponding alphabet and append to a list
# Print the key stream and the converted message and key
# Print the added and modular values and the final ciphertext