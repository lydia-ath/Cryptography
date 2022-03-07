
import text_preparation
import freq_analysis as freq

import string
from sys import maxsize
from declarations import EN_INDEX_OF_COINCIDENCE

# Index of concidence method
def index_of_coincidence(letter_counts):
    numerator = sum([letter_counts[l]*(letter_counts[l]-1) for l in string.ascii_uppercase])
    text_size = sum(occurrences for occurrences in letter_counts.values())
    denominator = text_size*(text_size-1)
    return numerator/denominator

# this method attempts to find the length of the key
def find_key_length(cyphertext, max_key_len):
    min_diff = maxsize
    key_len = 0
    for candidate_length in range(1, max_key_len + 1):
        groups, last_group = text_preparation.get_blocks(text=cyphertext, size=candidate_length)
        columns, last_column = text_preparation.get_columns(groups, last_group)
        ics = [index_of_coincidence(letter_counts=freq.getLetterCounts(text=column)) for column in columns]
        delta_bar_ic = sum(ics) / len(ics)
        if EN_INDEX_OF_COINCIDENCE-delta_bar_ic < min_diff:
            min_diff = EN_INDEX_OF_COINCIDENCE-delta_bar_ic
            key_len = candidate_length
        
        #print results
        print('The length of the key is : ' + str(candidate_length) + '\n')
        print('Index of Coincidence by column: '+str(ics))
        print('Index of Coincidence delta bar: '+str(delta_bar_ic)+'\n')

    return key_len
