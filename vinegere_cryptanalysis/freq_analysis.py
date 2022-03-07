import text_preparation

from declarations import EN_FREQ
import string

#This function counts how many times appears each letter of the alphabet in the ciphertext
def getLetterCounts(text):
    #ciphertext
    text_upper = text.upper()
    #letter counter
    letter_counts_array = {}

    for index, letter in enumerate(string.ascii_uppercase):
        letter_counts_array[letter] = text_upper.count(letter)

    return letter_counts_array

#This function calculates the frequency of each character found in the ciphertext
def letterFrequencies(text):
    letter_counts = getLetterCounts(text)

    #for each key=letter and value=count compute the frequency of each letter
    frequencies = {letter: count/len(text) for letter, count in letter_counts.items()}

    return frequencies

#Makes right shift of the ciphertext
def shift(text, amount):

    letters = string.ascii_uppercase
    shifted = ''
    for letter in text:
        shifted += letters[(letters.index(letter)-amount) % len(letters)]
    return shifted

# Correlation function
def correlation(text, lf):
    return sum([(lf[letter]*EN_FREQ[letter]) for letter in text])

# This function calculates each letter of the ciphertext's key
def find_letter_key(text, lf):

    letter_key = ''
    max_cor = 0

    print('string ascii uppercase: ', string.ascii_uppercase)
    for count, letter in enumerate(string.ascii_uppercase):
        shifted = shift(text=text, amount=count)
        cor = correlation(text=shifted, lf=lf)
        if cor > max_cor:
            max_cor = cor
            letter_key = letter
    return letter_key

# this method find the actual key
def key_refactor(cyphertext, key_len):
    key = ''
    blocks, last_block = text_preparation.get_blocks(text=cyphertext, size=key_len)
    columns, last_column = text_preparation.get_columns(blocks, last_block)
    frequencies = letterFrequencies(text=cyphertext)
    counts = getLetterCounts(text=cyphertext)

    #print reuslts 
    print('text letters freqs: ', {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1])})
    print('actual letters freqs: ', {k: v for k, v in sorted(EN_FREQ.items(), key=lambda item: item[1])})
    
    #print frequencies of all letters of the ciphertext
    counter = 1
    for column in columns:
        column_frequencies = letterFrequencies(text=column)
        column_counts = getLetterCounts(text=column)
        print('text letters freqs for column' + str(counter) +  ' : ',
              {k: v for k, v in sorted(column_frequencies.items(), key=lambda item: item[1])})
        print()
        print('text letters counts for column' + str(counter) + ' : ',
              {k: v for k, v in sorted(column_counts.items(), key=lambda item: item[1])})
        print()
        print('-------------------------------------------------------------------------------------------------')
        print()
        key += find_letter_key(text=column, lf=frequencies)
        counter += 1

    return key
