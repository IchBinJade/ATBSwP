# Translate text from English to Pig Latin

message_in = input("Enter the English phrase: ")

VOWELS = ("a", "e", "i", "o", "u", "y")

# A list of the words in Pig Latin
message_out = []

for word in message_in.split():
    # Separate the non-letters at the start of this word:
    prefix_non_alpha = ""
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_alpha += word[0]
        word = word[1:]
    if len(word) == 0:
        message_out.append(prefix_non_alpha)
        continue

    # Separate the non-letters at the end of this word:
    suffix_non_alpha = ""
    while not word[-1].isalpha():
        suffix_non_alpha += word[-1]
        word = word[-1]

    # Remember if the word was in uppercase or title case
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower() # Make it lowercase for translation

    # Separate the consonants at the start of this word:
    prefix_consonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefix_consonants != "":
        word += prefix_consonants + "ay"
    else:
        word += "yay"

    # Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    message_out.append(prefix_non_alpha + word + suffix_non_alpha)

# Join all the words back together into a single string:
print(" ".join(message_out))
