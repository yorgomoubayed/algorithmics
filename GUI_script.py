#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Graphical user interafce of the python implementation of both:
    .Burrows-Wheeler transform
    .Huffman coding
"""

from tkinter import LabelFrame, Label, Tk, Entry, StringVar, Button, GROOVE, filedialog
import main_script as main

###################
# Interface setup #                                                                                                                                                                                                                                        
###################

interface = Tk()
interface.title("Lossless data compression") #to set the interface title
interface.geometry("800x530") #to set the interface dimensions

#############
# Functions #                                                                                                                                                                                                                                        
#############

def transform():
    
    """
    Takes the string input in the original string field to reverse the transformation
    """
    
    print(main.transformation_bwt(bwt_string.get()))
    result = transformation_result.set(main.transformation_bwt(bwt_string.get())) #takes the string input in the 'Oirginal string' field and passes it as an argument to the transformation_bwt function
    return result

def reverse():
    
    """
    Takes the string input in the BWT string field to reverse the transformation
    """
    
    print(main.reverse_transformation_bwt(original_string.get()))
    result = reverse_result.set(main.reverse_transformation_bwt(original_string.get())) #takes the string input in the 'BWT string' field and passes it as an argument to the reverse_transfo_bwt function
    return result

def compression():
    
    """
    Takes the string input in the 'To compress' field to compress it
    """
    
    print(main.encode_without_file(compress.get()))
    result = compress_result.set(main.encode_without_file(compress.get())) #takes the string input in the 'To compress' field and passes it as an argument to the encode_without_file function 
    return result

def decompression():
    
    """
    Takes the string input in the 'To decompress' field to decompress it
    """
    
    print(main.decode_without_file(decompress.get()))
    result = decompress_result.set(main.decode_without_file(decompress.get())) #takes the string input in the 'To decompress' field and passes it as an argument to the decode_without_file function
    return result

def save():
    
    """
    Saves results from the burrows wheeler transform (from orginal string) and 
    results from the reverse (from the BWT string)
    """
    
    f = filedialog.asksaveasfile(mode = "w", defaultextension= ".txt") #popup to save the file 
    
    f.write("Burrows-Wheeler transform output is " + transformation_result.get() + "\n") #writes the BWT result on the first line of the file
    f.write("The original string input was " + reverse_result.get() + "\n") #writes the original string on the second line of the file
    f.close() #to close the file after writing
    
def open_file():
    
    """
    Browses and opens file from the user's computer
    """
    
    filename = interface.filedialog.askopenfilename(intialdir = '/', filetype = (("txt", "*.txt"), ("All files", "*.*")),  mode = "r")
    print(filename)
    f = open(filename, "r")
    f.read() #to read the file
    f.close() #to close the file after reading

def clear_bwt():
    
    """
    Clears fields included in the Burrows-Wheeler transform frame
    """
    
    bwt_string.set("") #clears the 'BWT string' field
    original_string.set("") #clears the 'Original string' field
    transformation_result.set("") #clears the transformation result field
    reverse_result.set("") #clears the reverse result field

def clear_huffman():
    
    """
    Clears fields included in the Huffman coding frame
    """
    
    compress.set("") #clears the 'To compress' field
    compress_result.set("") #clears the compression result field
    decompress.set("") #clears the 'To decompress' field
    decompress_result.set("") #clears the decompression result field
 
#############
# Variables #                                                                                                                                                                                                                                        #
#############
    
bwt_string = StringVar() #string input in the 'BWT string' field
transformation_result = StringVar() #string input in the transformation result field 

original_string = StringVar() #string input in the 'Original string' field 
reverse_result = StringVar() #string input in the reverse result field

compress = StringVar() #string input in the 'To compress' field
compress_result = StringVar() #string input in the result of compression field

decompress = StringVar() #string input in the 'To decompress' field
decompress_result = StringVar() #string input in the result of decompression field

alerte_decompression = StringVar()

#########################################
# Burrows-wheeler transform frame setup #                                                                                                                                                                                                                                        #
#########################################

#build the bwt frame with title
bwt_frame = LabelFrame(interface, borderwidth = 2, relief = GROOVE, bg = "white", text="Burrows-Wheeler transform", font=('arial', 12, 'bold')).place(width = 790, height = 175, x = 3, y = 0)

#add label and entry box for the orginal string
orginal_string_label = Label(bwt_frame, text= "Original", bg = "white", font=('arial', 10, 'bold')).grid(padx = 5, pady = 5, row = 2, column = 0)
original_string_entry = Entry(bwt_frame, textvariable = bwt_string).grid(padx = 5, pady= 5, row = 2, column = 1)

#add label and entry box for BWT string
bwt_string_label = Label(bwt_frame, text= "BWT", bg = "white", font=('arial', 10, 'bold')).grid(padx = 5, pady= 5, row = 3, column = 0)
bwt_string_entry = Entry(bwt_frame, textvariable = original_string).grid(padx = 5, pady= 5, row = 3, column = 1)

#add entry box for the transformation result
#transformation_result_entry = Entry(interface, textvariable = transformation_result).place(width = 200, height = 25, x = 450, y = 7)
transformation_result_entry = Entry(interface, textvariable = transformation_result).grid(padx = 5, pady = 5, row = 2, column = 3)

#add entry box for the reverse result
#reverse_result_entry = Entry(interface, textvariable = reverse_result).place(width = 200, height = 25, x = 580, y = 50)
reverse_string_label = Label(bwt_frame, text= "Reconstructed", bg = "white", font = ('arial', 10, 'bold')).grid(padx = 5, pady = 5, row = 4, column = 0)
reverse_result_entry = Entry(interface, textvariable = reverse_result).grid(padx = 5, pady = 5, row = 4, column = 1)

#save button to save outputs in the results fields 
save_button = Button(interface, command = save, text = "Save", font = ('arial', 10, 'bold')).grid(row = 7, column = 4)

#open button to browse files from the user's computer
open_button = Button(interface, command = open_file , text = "Open", font = ('arial', 10, 'bold')).grid(row = 7, column = 5) 

#transform button to call the BWT functions
transformation_button = Button(bwt_frame, text = "Transform", command = transform, font = ('arial', 10, 'bold')).grid(padx = 5, pady = 5, row = 1, column = 2)

#reverse button to call the reverse BWT functions
reverse_button = Button(bwt_frame, text = "Reverse", command = reverse, font = ('arial', 10, 'bold')).grid(padx = 5, pady = 5, row = 3, column = 2)

#clear button to clear the interface fields in the BWT frame
bwt_clear_button = Button(interface, command = clear_bwt, text = "Clear fields", font = ('arial', 10, 'bold')).grid(row = 7, column = 6)

#bwt_matrix_entry = Entry(interface).place(width = 450, height = 175, x = 330 , y = 175)
#scroll_bar_entry = Scrollbar(entry_matrix_bwt).place( x = 780, y = 150, width = 20, height = 200)

##############################
# Huffman coding frame setup #                                                                                                                                                                                                                                        #
##############################

#build the huffman coding frame with title
huffman_frame = LabelFrame(interface, borderwidth = 2, relief = GROOVE, bg = "white", text = "Huffman coding", font = ('arial', 12, 'bold')).place(width = 790, height = 150, x = 3, y = 380)

#add label and entry box for compression
compression_label = Label(huffman_frame, text = "To compress", bg = "white", font = ('arial', 10, 'bold')).place(width = 150 , height = 25, x = 5, y = 410)
compression_entry = Entry(huffman_frame, textvariable = compress).place(width = 200, height = 25, x = 160, y = 410) 

#add label and entry box for compression
decompression_label = Label(huffman_frame, text = "To decompress", bg = "white", font = ('arial', 10, 'bold')).place(width = 156 , height = 25, x = 5, y = 450)
decompression_entry = Entry(huffman_frame, textvariable = decompress).place(width = 200, height = 25, x = 160, y = 450) 

#add entry box for the compression result
compression_result_entry = Entry(huffman_frame, textvariable = compress_result).place(width = 200, height = 25, x = 490, y = 410) 

#add entry box for the decompression result
decompression_result_entry = Entry(huffman_frame, textvariable = decompress_result).place(width = 200, height = 25, x = 490, y = 450) 

#compression button to call the compression functions
compression_button = Button(huffman_frame, text = "Compress", command = compression, font = ('arial', 10, 'bold')).place(x = 385, y = 410) 

#decompression button to cal the decompression functions
decompression_button = Button(huffman_frame, text = "Decompress", command = decompression, font = ('arial', 10, 'bold')).place(x = 380, y = 450) 

#clear button to clear the fields in the Huffman coding frame
huffman_clear_button = Button(interface, command = clear_huffman, text = "Clear fields", font = ('arial', 10, 'bold')).place(x = 690, y = 490)

#etiquette_information = Label(interface, text = "Ne pas décompresser sans avoir compresser avant! ", fg = "Red").place(y = 450, x = 5)
#etiquette_information_sauvegarde = Label(interface, text = "Bouton sauvegarder fonctionnel pour uniquement la transformation ", fg = "Red", bg ="white").place(x = 330, y = 120)

interface.mainloop()

Algorithm presented in:
Burrows M, Wheeler DJ: A Block Sorting Lossless Data Compression Algorithm.
    Technical Report 124. Palo Alto, CA: Digital Equipment Corporation; 1994.