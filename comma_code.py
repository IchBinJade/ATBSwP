# Function to return a sentence/string from a list

def list_to_string(list_in):
    list_length = len(list_in)

    if list_length == 0:
        return "You gave me an empty list!"
    elif list_length == 1:
        return str(list_in[0])

    sentence_out = ", ".join(list_in[:-1]) + ", and " + list_in[-1]

    return sentence_out


spam = ["apples", "bananas", "tofu", "cats"]
spam2 = ["Lions", "tigers", "bears oh my!"]
print(list_to_string(spam2))
