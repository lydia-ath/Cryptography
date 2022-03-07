
from declarations import (SEQ_LEN, MAX_KEY_LENGTH)

import text_preparation
import index_of_coincidence
import kasiski_method

import freq_analysis as freq

import string

# This function takes as parameters the ciphetext and the key and decrypts the ciphertext
def decypher(cyphertext, key):

    # Letters are the characters of the english alphabet
    letters = string.ascii_uppercase #all the leters are uppercase withour spaces 
    print('letters: ', letters)

    # The shift is the position of each letter of the key in the alphabet
    shifts = [letters.index(letter) for letter in key]
    print('shifts: ', shifts)

    # Creates the blocks' list
    blocks, last_block = text_preparation.get_blocks(text=cyphertext,size=len(key))

    # Creates the columns' list of the ciphertext
    cols, last_col = text_preparation.get_columns(blocks, last_block=last_block)
    print('block length: '+str(len(blocks))+' column length '+str(len(cols)))

    decyphered_blocks = text_preparation.to_blocks([freq.shift(col, shift) for col, shift in zip(cols, shifts)])
    
    #decypher last block separetely
    last_decyphered_block = text_preparation.to_blocks([freq.shift(last_col, shift) for last_col, shift in zip(last_col, shifts)])
    decyphered = ''.join(decyphered_blocks)
    print('decyphered 1:', decyphered)
    print('decyphered last:', last_decyphered_block)

    #merge decyphered text and the last block-word that decyphered separetely 
    decyphered = decyphered + ''.join(last_decyphered_block)
   
    return decyphered

#Main method
#Reads the ciphertext from the file and applies the chosen method each time Kasiski or Index of Coincidence
def decipher(file, method):
    with open(file) as f:
        cyphertext = f.readlines()
        key_len = 0
        #prints the ciphertext
        print('Cyphertext: '+cyphertext[0])
        #prints the ciphertext's length
        print('Cyphertext Length: '+str(len(cyphertext[0])))
        #Kasiski method
        if method == 'kasiski':
            print('Applying kasiski examination\n')
            key_len = kasiski_method.find_key_length(cyphertext=cyphertext[0], seq_len=SEQ_LEN, max_key_len=MAX_KEY_LENGTH)
        #Index of coincidence method
        elif method == 'index_of_coincidence':
            print('Applying index of coincidence examination\n')
            key_len = index_of_coincidence.find_key_length(cyphertext=cyphertext[0], max_key_len=MAX_KEY_LENGTH)
        key = freq.key_refactor(cyphertext[0], key_len)
        decyphered = decypher(cyphertext[0], key)

        #print results of decryption 
        print('Chosen key length: '+str(key_len))
        print('Restored key: '+str(key))
        print('Plaintext: '+str(decyphered))
        print('Plaintext Length:'+str(len(decyphered)))


# Apply main method with Kasiski method
decipher('ciphertext.txt', 'kasiski')
# Apply main method with Index of Coincidence method
decipher('ciphertext.txt', 'index_of_coincidence')
