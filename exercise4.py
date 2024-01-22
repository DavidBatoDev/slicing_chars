# Define a function that takes two parameter
# first parameter is the word, second parameter is the target index
def remove_chars(word, index):
    return word[index:]
# simply return the sliced word starting from the given index 

remove_chars("pynative", 4) # Output: tive
remove_chars("pynative", 2) # Output native