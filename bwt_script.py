#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python implementation of the Burrows-Wheeler transform (BWT)

.Implementation of both the transformation and the reverse.
.Reversing the transfromation of an input string brought back the original state of it, without any data loss.

Algorithm presented in:
Burrows M, Wheeler DJ: A Block Sorting Lossless Data Compression Algorithm.
Technical Report 124. Palo Alto, CA: Digital Equipment Corporation; 1994.
"""

def bwt_sort_characters(original_string):
    
    """
    Adds characters into a list and sorts them accordingly
    """
    
    assert "$" not in original_string  # Input string cannot contain $
    character = original_string + "$"
    
    main_list = []
    for i in range(0, len(original_string) +  1):
        main_list = main_list + [character[-i:] + character[:-i]] #slide to the left
        print(main_list)
    print(sorted(main_list))
    return sorted(main_list) #sort the list

def bwt_transformation(main_list):
    
    """
    Recovers the last column from the sorted list
    """
    
    accumulator = ""
    for e in main_list:
        accumulator = accumulator + e[-1] #recover the last element from each line of the sorted list
    return accumulator

def bwt_seperator(transformation):
    
    """
    Seperates characters and returns a list
    """
    
    accumulator = []
    for e in transformation:
        accumulator = accumulator + [e] #seperate characters
    return accumulator

def bwt_linker(matrix, main_list_reverse):
    
    """
    Concatenation of each element to the left of the list
    """
    
    for i in range(0, len(main_list_reverse)):
        matrix[i] = main_list_reverse[i] + matrix[i] #add index to the matrix
        
    return matrix
    
def bwt_reverse(transformation):
    
    """
    Prints the original string from the bwt string
    """
    
    transformation_seperation = bwt_seperator(transformation) #seperate characters
    main_list_accumulator = transformation_seperation 
    
    for i in range(0, len(transformation)- 1):
        
        main_list_accumulator = sorted(main_list_accumulator) #sort elements
        print(main_list_accumulator)
        main_list_accumulator = bwt_linker(main_list_accumulator, transformation_seperation) #add transformed list to the accumulator

    for e in main_list_accumulator: 
        if e[-1] == '$': #recover the last element with the '$' symbol
            return e[0:len(e)-1] #remove the '$' symbol and return the orginal string
    
if __name__  == "__main__":    
    input_string = bwt_sort_characters("ATGCTAGTTTACGTCCGGTTCAGC") #User input string
#    print(input_string)
    
    transformation = bwt_transformation(input_string)
    print("\n" + "BWT string : " + transformation + "\n")    
#    print(bwt_seperator(transformation))
    
#    print(bwt_linker(sorted(bwt_seperator(transformation)), bwt_seperator(transformation)))
    print("\n" + "Reconstructed string : " + bwt_reverse(transformation))
