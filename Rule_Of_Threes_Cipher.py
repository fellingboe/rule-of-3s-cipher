import string

# Function for doing the actual caesar shift
def caesar(plaintext, shift):
    plaintext = plaintext.lower()   # converts to lowercase
    alphabet = string.ascii_lowercase   # Getting the alphabet we will be using (a-z lower case)
    shift = shift % 26                  # since only 26 letters, shifitng more than 26 just loops it
    shiftedAlphabet = alphabet[shift:] + alphabet[:shift] # shifting that alphabet to the right
    table = str.maketrans(alphabet, shiftedAlphabet)   # making a table for how letters should be translated
    return plaintext.translate(table)    # Actually shifting the text


# Function for finding how far we will shift the ciphered sentence, based off the english sentence
def findShiftValue(text):
    words = text.split()    # splitting the words by their spaces
    if len(words) < 3 or len(words[2]) < 3:     # If the english sentence is less than 3 words long, or the 3rd word has less than 3 letters
        raise Exception("Third word must be ≥ 3 letters")
    return ord(words[2][2].lower()) - 96  # a=1     # returns the number of the 3rd letter of the 3rd word


# function for getting in an uncyphered string and 
def cypherText(text):
    segments = text.split(" | ")    # Splits the input sentences by the |
    output = []
    for i in range(0, len(segments)-1, 2):  # Looping through input sentence, iterating 2 at a time because there is both english and ciphered sentences
        english = segments[i]               # this gets the english text
        toShift = segments[i+1]            # and this gets the cyphered text
        shift = findShiftValue(english)     # getting how far the shift should start at
        result = ""
        for j in range(0, len(toShift), 3):            # for every character in our sentence (split into sections of 3)
            result += caesar(toShift[j:j+3], shift)    # add the next 3 characters to our ciphered sentence
            shift += 3                                  # increase how far we shift by 3
        output.append(english + " | " + result)          # Adds the "|" between the 2 sentences and appends them to the output
    return " | ".join(output)                           # combines the array of sentences and places the "|" between them

# same as above just has a negative shift
def deCypherText(text):
    segments = text.split(" | ")
    output = []
    for i in range(0, len(segments)-1, 2):
        english = segments[i]
        toShift = segments[i+1]
        shift = findShiftValue(english)
        result = ""
        for j in range(0, len(toShift), 3):
            result += caesar(toShift[j:j+3], -shift)
            shift += 3
        output.append(english + " | " + result)
    return " | ".join(output)


#testing this with one | other stuff | second round for testing | totally normal
#testing this with one | inbbo stuii | second round for testing | lglvggw lpsnep

print("Please input 1 if you wish to encrypt you own message \nOr input 2 if you wish to de-crypt a received message")
encryptOrDecrypt = input()
if encryptOrDecrypt == "1":
    print("Please input the message you wish to encrypt. \n" 
          + "It should be in the form:     not important text | text to encrypt | not important text | text to encrypt\n" 
          + "Please note the third word of your \"not important text\" must be 3 or more letters long.\n"
          + "Having new lines is fine\n"
          + "*IMPORTANT* Type END on a new line when you’re finished:\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip() != "":  # if its not just an empty line for nice formatting
            lines.append(line)
    inputString = " | ".join(lines)
    
    print ("\n\n" + cypherText(inputString))  # Printing the new encrypted result
    
elif encryptOrDecrypt == "2":
    print("Please input the message you wish to de-crypt. \n"
          + "Having new lines is fine\n "
          + "*IMPORTANT* Type END on a new line when you’re finished:\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip() != "":  # if its not just an empty line for nice formatting
            lines.append(line)
    inputString = " | ".join(lines)
    
    print ("\n\n" + deCypherText(inputString))  # Printing the newly decrypted result

else:
    raise Exception("Please ensure you only type \"1\" or \"2\"")