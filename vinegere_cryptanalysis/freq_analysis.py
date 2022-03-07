import text_preparation
import string
from declarations import EN_REL_FREQ

#This function counts how many times appears each letter of the alphabet in the ciphertext
def get_letter_counts(text):
    #ciphertext
    text_upper = text.upper()
    #letter counter
    letter_counts = {}
    for index, letter in enumerate(string.ascii_uppercase):
        letter_counts[letter] = text_upper.count(letter)
    return letter_counts

#This function calculates the frequency of each character found in the ciphertext
def _get_letter_frequencies(text):
    letter_counts = get_letter_counts(text)
    #for each key=letter and value=count compute the frequency of each letter
    frequencies = {letter: count/len(text) for letter, count in letter_counts.items()}
    return frequencies

#Makes right shift of the ciphertext
def shift(text, amount):
    shifted = ''
    letters = string.ascii_uppercase
    for letter in text:
        shifted += letters[(letters.index(letter)-amount) % len(letters)]
    return shifted

# Correlation function
def _corr(text, lf):
    return sum([(lf[letter]*EN_REL_FREQ[letter]) for letter in text])

# This function calculates each letter of the ciphertext's key
def _find_key_letter(text, lf):
    key_letter = ''
    max_corr = 0
    print('string ascii uppercase: ', string.ascii_uppercase)
    for count, letter in enumerate(string.ascii_uppercase):
        shifted = shift(text=text, amount=count)
        corr = _corr(text=shifted, lf=lf)
        if corr > max_corr:
            max_corr = corr
            key_letter = letter
    return key_letter


def restore_key(cyphertext, key_len):
    key = ''
    blocks, last_block = text_preparation.get_blocks(text=cyphertext, size=key_len)
    columns, last_column = text_preparation.get_columns(blocks, last_block)
    frequencies = _get_letter_frequencies(text=cyphertext)
    print('text letters freqs: ', {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1])})
    print('actual letters freqs: ', {k: v for k, v in sorted(EN_REL_FREQ.items(), key=lambda item: item[1])})
    counter = 1
    for column in columns:
        column_frequencies = _get_letter_frequencies(text=column)
        print('text letters freqs for column' + str(counter) +  ' : ', {k: v for k, v in sorted(column_frequencies.items(), key=lambda item: item[1])})
        key += _find_key_letter(text=column, lf=frequencies)
        counter += 1
    return key
