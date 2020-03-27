###########
# Authors #
###########

Yorgo EL MOUBAYED
Aix-Marseille University - Master's degree in Bioinformatics: software development and data analysis.

#######################
# Project description #
#######################

This project was submitted for the algorithmics module. The objective was to provide the following:
	-A Python implementation of the Burrows-Wheeler transform algorithm.
	-A Python implementation of Huffman coding.
	-A graphical user interface (GUI) that uses the above mentionned implementations.

Unfortunately, 2/3 of the objectives were fulfilled. The GUI was not submitted because of technical difficulties.

##############
# Repository #
##############

The repository contains three Python scripts and two text files:
	-bwt_script.py.
	-huffman_script.py.
	-main_script.py.
	-main_test_file.txt.
	-README.txt (current file).

IMPORTANT NOTICE: ALL SCRIPTS MUST REMAIN IN THE SAME DIRECTORY UPON EXECUTION.

#################
# Prerequisites #
#################

To run the scripts, the user has two options:
	-Install a Python IDE with a Python 3+ installation to manually input his data.
	-Use the following command line on the terminal: python3 -python filename, to run scripts with default input strings. 

#################
# bwt_script.py #
#################

The bwt_script.py script is a Python implementation of the Burrows-Wheeler transform (BWT):
	-Implementation of both the transformation and the reverse.
	-Reversing the transformation of an input string brought back the original state of it, without any data loss.

The user is provided with a default string "ATGCTAGTTTACGTCCGGTTCAGC". To change it, he needs to manually input his string in the "input_string" variable of the if __name__ == "main" block on line 83. When executed, the user gets the following outputs printed in the terminal:
	-The Burrows-Wheeler transorm matrix.
	-The Burrows-Wheeler transform string.
	-The Burrows-Wheeler transform matrix to reverse the transformation.
	-The reconstruction of the original input string.

#####################
# huffman_script.py #
#####################

The huffman_script.py script is a Python implementation of the Huffman Coding:
	-Implementation of both the compression and decompression. 
	-Decompressing the compressed input string brought back the original state of it, without any data loss.

The key steps in the implementation are:
	-Building a frequency dictionary.
	-Selecting 2 minimum frequency symbols and merge them repeatedly.
	-Building a Huffman tree of the above process: used heap to maintain a tree structure.
	-Traversing the tree, assigning the corresponding codes and storing them in a dictionary.
	-Encoding the input text.

The user is provided with a default string "ATGCTAGTTTACGTCCGGTTCAGC". To change it, he needs to manually input his string in the "sequence" variable of the if __name__ == "main" block on line 184. 

When executed, the user gets the following outputs printed in the terminal:
	-Compression outputs:
		.The huffman tree binary dictionary.
		.The input sequence binary encoding.
		.The compression characters output from the binary encoding.

	-Decompression outputs:
		.The decompressed binary sequence after padding removal.
		.The original decompressed sequence.

##################
# main_script.py #
##################

The main_script.py script combines both the Huffman coding and the Burrows-Wheeler transform Python implementations (check other scripts for details). 
The main difference is that through the script, the user is able to compress/decompress data that is contained in a file as well as saving the BWT results.

#Huffman coding
The user is provided with a default test file "main_test_file.txt". He needs to manually input the file with the corresponding file path in the encode variable of the if __name__ == "main" block on line 132.

When executed, the user gets the following compression/decompression outputs in the working directory:
	-compressed_file.txt
	-compression_file_dictionary.txt
	-decompressed_file.txt

#Burrows-Wheeler transform
The user is provided with a default string "ATGCTAGTTTACGTCCGGTTCAGC". To change it, he needs to manually input his string in the "transformation_result" variable of the if __name__ == "main" block on line 142.

The user is provided with a default string "CTCT$GTTCAGATCCGATCTGATGG". To change it, he needs to manually input his BWT_string in the "reconstructed_string" variable of the if __name__ == "main" block on line 143.

The user needs to change the file path on line 144. The output is bwt.txt

IMPORTANT NOTICE: TO ENSURE FUNCTIONALITY, COMPRESSION AND DECOMPRESSION STEPS ARE COUPLED. THEREFORE, THE USER IS OBLIGED TO COMPRESS HIS INPUT FILE BEFORE DECOMPRESSING IT.

###################
# acknowledgement #
###################

The author would like express his special thanks of gratitude to prof. Sebastien TEMPEL for his technical guidance throughout the project.

