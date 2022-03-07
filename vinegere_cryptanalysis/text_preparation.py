
#This function splits the ciphettext into blocks and
# creates a list of substrings whose length equals to the block's length (size)
def get_blocks(text, size):

    #size is the block's length
    blocks = [text[i:i+size] for i in range(0, len(text)-size, size)]

    #prints the list's blocks
    for i in range(0, len(blocks)):
        print('Block ' + str(i) + ' : ' + blocks[i])

    print(len(text))
    print(size)
    last_block = text[len(text)%size + len(text)-size:]

    print('Last block: ' + last_block)
    print(len(blocks))
    return blocks, last_block

#This function separates the ciphertext into columns and each column has the size of it's block
def get_columns(text_blocks, last_block=''):
    group_size = len(text_blocks[0])
    columns = []
    last_column = []
    for letter_count in range(group_size):
        column = ''
        for group_count in range(len(text_blocks)):
            column += text_blocks[group_count][letter_count]

        columns.append(column)
        last_block_list = list(last_block)

        print('Last block list: ', last_block)
        print((len(last_block_list), letter_count))

        #Append last block of the list to the last column if length of the last block is bigger than the letter's position in the alphabet
        if len(last_block_list) > letter_count:
            last_column.append(last_block_list[letter_count])

    print('last column 1: ',  column)
    last_column = ''.join(last_column)
    print('last column 2: ', last_column)
    print('help print '+str(group_size)+' for text s blocks '+str(len(text_blocks)))

    # Returns the ciphertext in columns
    return columns, last_column

#This function creates the blocks and fills their content with characters
def to_blocks(cols):
    col_size = len(cols[0])
    blocks = []

    print('to blocks sizes(col_size, cols)', (col_size, len(cols)))
    for letter in range(col_size):
        block = ''
        for col in range(len(cols)):
            block += cols[col][letter]

        blocks.append(block)
        
    return blocks

