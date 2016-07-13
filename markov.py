from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()


    return contents


def make_chains(contents):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # take the string, and break it into a list of words
    text = contents.split()
    # Loop over every single element in text and grap each word base on their index + the next word (same as next line)
    for i in range(len(text)-2): #iterate over every word over the length of text, give each word an index using range
        print text[i], text[i+1] #print each word, and the next word as a pair
        text_tuple = (text[i], text[i+1]) #create a tupe with each pair of words (text_tuple)
        chains[text_tuple] = chains.get(text_tuple, []) #Look up each text_tuple in the dictionary to see if it exists as key. If it's not there, add text_tuple as key, set value to empty list. 
        chains[text_tuple].append(text[i+2]) #add value to new keys, using .append method - because previous step set value as empty list

    print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""



# get a random key
    random_key = choice(chains.keys())
    # print '*'*10, type(random_key)
    # create empty string
    random_text = random_key[0]
    # run a while loop until new key cannot be found in Chains dictionary
    while random_key in chains:
    # get the random value
        random_value = choice(chains[random_key])
    # concacnating key and value into text
        random_text = random_text + " " + random_key[1] + " " + random_value
    # rebind key to second word in previous key + value
        random_key = (random_key[1], random_value)

         
    print random_text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

#Produce random_text
random_text = make_text(chains)

print random_text
