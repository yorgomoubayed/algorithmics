#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python implementation of the Huffman Coding

.Implementation of both the compression and decompression. 
.Decompressing the compressed input string brought back the original state of it, without any data loss.

The key steps in the implementation are:
-Building a frequency dictionary.
-Selecting 2 minimum frequency symbols and merge them repeatedly.
-Building a Huffman tree of the above process: used heap to maintain a tree structure.
-Traversing the tree, assigning the corresponding codes and storing them in a dictionary.
-Encoding the input text.
"""

from heapq import heappop, heappush

################################
# Frequencies and Huffman tree #
################################

def store_frequencies(sequence):
    
    """
    Creates a dictionary with corresponding characters frequencies
    """
    
    frequency_table = {} #create empty frequency dictionary

    for e in sequence:
        
        if e in frequency_table:
            frequency_table[e] = frequency_table[e] + 1 #if element present add 1 
        
        else:
            frequency_table[e] = 1 #if element not present leave at 1
    
    return frequency_table

def huffman_tree(occurrences):
   
    """
    Creates the Huffman tree
    """
    
    tas = [[weight, [letter, ""]] 
    for letter, weight in occurrences.items()]

    while len(tas) > 1:
        low = heappop(tas) #node with the lowest weight
        high = heappop(tas) #node with the second lowest weight
        
        for e in low[1:]:
            e[1] = "0" + e[1] #assign '0' for the node with the lowest value
        
        for e in high[1:]:
            e[1] = "1" + e[1]
            
        heappush(tas, [low[0] + high[0]] + low[1:] + high[1:])
        
    return sorted(heappop(tas)[1:])

def format_huffman_tree(tree):
    
    """
    Stores the characters in a dictionary with corresponding new binary values
    """
    
    huffman_tree_dictionary = {}
    
    for e in tree:
        huffman_tree_dictionary[e[0]] = e[1]
        
    return huffman_tree_dictionary

def encode_sequence(sequence, binary_dictionary):
    
    """
    Transforms and prints the original string into binary according to the frequencies dictionary
    """
    
    binary_result = ""  
    
    for e in sequence:
        binary_result = binary_result + binary_dictionary[e]
                
    return binary_result

def pad_encoded_text(encoded_text):
    
    """
    Pads the coded text if its length is not a multiple of 8
    """
    
    extra_padding = 8 - len(encoded_text) % 8 #determine the number of bits to add
    
    for i in range(extra_padding): 
        encoded_text += "0" #add '0's to the required number of bytes

    padded_info = "{0:08b}".format(extra_padding)
    
    encoded_text = padded_info + encoded_text
    return encoded_text

def compression(encoded_pad):
    
    """
    Compression from binary into characters according to the padded text
    """
    
    i = 0
    acc2 = ''
    
    while i < len(encoded_pad):
        temp = chr(int(encoded_pad[i:i+8], 2)) #transform to characters from 8bits
        acc2 += temp
        i += 8
    return(acc2)

def remove_padding(padded_encoded_text):
    
    """
    Removes padding from the binary sequence
    """
    
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2) #recover the number of bytes that enabled the padding
    padded_encoded_text = padded_encoded_text[8:] #recover the sequence
    encoded_text = padded_encoded_text[:-1*extra_padding] #remove the padding
    
    return encoded_text

def swap_dictionary(dictionary):
    
    """
    Swaps the key into value and vice-versa in the binary_dictionary
    """
    
    novel_dictionary = {}

    for key, value in dictionary.items():
        if value in novel_dictionary:
            novel_dictionary[value].append(key)
        else:
            novel_dictionary[value] = key
    
    return novel_dictionary

def decode_sequence(encoded_sequence, dictionary_swap):
    
    """
    Recovers the original sequence from the encoded sequence and the swapped dictionary 
    """
    
    decode_sequence = ""
    current_sequence = "" #current_seq sera l'élément qui contiendra le pattern de bytes à chercher dans le dictionnaire
        
    for bit in encoded_sequence: 
        current_sequence += bit 
        
        if current_sequence in dictionary_swap:
            char = dictionary_swap[current_sequence] #Add letter
            decode_sequence += char
            current_sequence = "" #intilize the current sequence
    
    return decode_sequence

def decompression(compress):
    
    """
    Recovers binary sequence from characters
    """
    
    decompress = ""
    
    for x in compress:
        decompress += ''.join([str(format(ord(x), '08b'))]) #transform characters into binary
    return decompress

if __name__ == "__main__":
    
    sequence = "ATGCTAGTTTACGTCCGGTTCAGC"
    print(f"The original sequence is: \n{sequence}\n")
    dictionary = store_frequencies(sequence)

    ###############
    # Compression #
    ###############
    
    #verify the creation of the Huffman tree
    tree = huffman_tree(dictionary)
#    print(f"The Huffman tree: \n{tree}\n")
    
    #verify the tree's nodes setup
    binary_dictionary = format_huffman_tree(tree) 
    print(f"The binary dictionary from the Huffman tree: \n{binary_dictionary}\n")
    
    #verify the sequence encoding
    binary_sequence = encode_sequence(sequence, binary_dictionary)
    print(f"The encoded binary sequence is: \n{binary_sequence} \n")
    
    #verify sequence padding
    binary_sequence_padded = pad_encoded_text(binary_sequence)
    print(f"The padded binary sequence is: \n{binary_sequence_padded}\n")
    
    #verify compression
    compressed = compression(binary_sequence_padded)
    print(f"Compression characters output from binary: {compressed}\n")
    
    #################
    # Decompression #
    #################
    
    #decode
    dictionary_swap = swap_dictionary(binary_dictionary)
    decompress = decompression(compressed)
    
    #verify sequence padding
    #print(f"The decompressed binary sequence is (before padding removal): \n{decompress}\n")
    
    #verify sequence padding removal
    print(f"The decompressed binary sequence is (after padding removal): \n{remove_padding(decompress)}\n")
    
    #verify binary_sequence dexcompression
    print(f"The original sequence is: \n{decode_sequence(binary_sequence, dictionary_swap)}\n")
