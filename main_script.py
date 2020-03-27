#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main_sctipt is a combination of both the Huffman coding and the Burrows-Wheeler
transform Python implementations (check other scripts for details)
"""
import huffman_script as huffman
import bwt_script as bwt

def encode_file(file):
    
    """
    Combines encoding and compression functions to enable encoding a file content
    """
    #open file
    file_1 = open(file, "r")
    
    #read file and removes line breaks
    line = file_1.readline().rstrip('\n')
    
    #imports the store_frequencies from the huffman_script.py script
    dictionary = huffman.store_frequencies(line) 
    
    #imports the store_frequencies from the huffman_script.py script
    tree = huffman.huffman_tree(dictionary)

    #imports the store_frequencies from the huffman_script.py script
    binary_dictionary = huffman.format_huffman_tree(tree)

    #imports the store_frequencies from the huffman_script.py script
    binary_sequence = huffman.encode_sequence(line, binary_dictionary) 

    #imports the store_frequencies from the huffman_script.py script
    binary_sequence_pad = huffman.pad_encoded_text(binary_sequence)

    #imports the store_frequencies from the huffman_script.py script
    compressed = huffman.compression(binary_sequence_pad)
    
    #close file
    file_1.close()
    
    #recover compression and binary dictionary to write them in a file
    return compressed, binary_dictionary

def write_compressed(name_file, encode):
    
    """
    Writes the compression output into a file
    """
    
    file_2 = open(name_file, "w") #open the file
    file_2.write(encode) #write in the file
    file_2.close() #close the file

def write_dictionary(name_file, dictionary):
    
    """
    Stores a dictionary in given file
    """
    
    file_3 = open(name_file, "w") 
    
    for e in dictionary:
        string = e + ":" + dictionary[e] + "\n" #add element to dictionary
        
        file_3.write(string) #write in the file
    file_3.close() #close the file

def decode_file(file, file_dictionary):
    
    """
    Decodes the given file (in the same directory as the present script)
    """
    
    file_1 = open(file, "r")
    line = file_1.readline().rstrip('\n')
    decompress = huffman.decompression(line)    
    the_dictionary_swap = {}

    with open(file_dictionary) as myfile:
        for line in myfile:
            key, value = line.partition(":")[::2]
            the_dictionary_swap[key.strip()] = value.rstrip('\n')

    #print(my_dictionnaire_swap)            
    dictionary_swap = huffman.swap_dictionary(the_dictionary_swap) #swap keys and values
    
    #imports the remove_padding function from the huffman_script.py file
    remove_padded_sequence = huffman.remove_padding(decompress)
    #print(remove_padded_sequence)
    
    #imports the decode_sequence function from the huffman_script.py file
    decode = huffman.decode_sequence(remove_padded_sequence, dictionary_swap)
    #print(decode)
    
    return decode
    file_1.close()

def transformation_bwt(sequence):
    
    """
    Imports the bwt_sort_characters and bwt_transformation functions from the BWT.py file
    """
    
    add_character = bwt.bwt_sort_characters(sequence)
    transformation = bwt.bwt_transformation(add_character) 
    return transformation

def reverse_transformation_bwt(BWT_convert):
    
    """
    Imports the bwt_reverse function from the BWT.py file
    """
    reconstructed_string = bwt.bwt_reverse(BWT_convert)
    return reconstructed_string

def write_bwt(file_name):
    
    file_4 = open(file_name, "w") #open file to write    
    file_4.write("Burrows-Wheeler transform output is : " + transformation_result + "\n") #writes the BWT result on the first line of the file
    file_4.write("The original string input was : " + reconstructed_string + "\n") #writes the original string on the second line of the file
    file_4.close() #to close the file after writing
    

if __name__ == "__main__":
    
    ##################
    # Huffman coding #
    ##################
    
    encode = encode_file("/home/yorgo/Desktop/M1_DLAD/S2/Algorithmique/Projet/projet_algorithmique_yorgo_el_moubayed/main_test_file.txt") #input the file to compressed with adapted path
    write_compressed("compressed_file.txt", encode[0]) #writes the compression in a file
    write_dictionary("compressed_file_dictionary.txt", encode[1]) #writes the compression dictionary in a file

    decode = decode_file("compressed_file.txt", "compressed_file_dictionary.txt") #newly compressed file with corresponding dictionary 
    write_compressed("decompressed_file.txt", decode) #newly decompressed file

    #######
    # BWT #
    #######
    
    transformation_result = transformation_bwt("ATGCTAGTTTACGTCCGGTTCAGC") #input sequence to transform
    reconstructed_string = reverse_transformation_bwt("CTCT$GTTCAGATCCGATCTGATGG") #input the bwt string to reconstruct
    write_bwt("/home/yorgo/Desktop/M1_DLAD/S2/Algorithmique/Projet/projet_algorithmique_yorgo_el_moubayed/bwt.txt") #change path for your own computer
