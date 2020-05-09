from configparser import ConfigParser
import time
import json
import random, os, sys
from Bio import SeqIO #NEED TO INSTALL: pip install biopython

# Parser function
# Return the args key & values as dictionary.
def parse_configurations(parser, sectionName): #parser(config.ini), sectionName
    args = dict()
    key_list = list(dict(parser.items(sectionName)).keys())
    print("Section Name:", sectionName)
    print("Keys List: ", key_list)  

    for key in key_list: #key_list:  ['lamba_min', 'lamba_max', 'lamba', 'generations', 'numrows']
        args[key]=parser[sectionName][key]
    return args


# Print the specified arg.
def print_parse_args(argsName):
    if argsName is not None:
        try:
            argsName=str(argsName) 
            print(argsName)
        except:
            sys.exit(5)

# Parse fasta: 
# Bio.SeqIO.parse() which takes a file handle (or filename) and format name, and returns a SeqRecord iterator.
'''
ID: NC_010473.1
Name: NC_010473.1
Description: NC_010473.1 Escherichia coli str. K12 substr. DH10B, complete genome
Number of features: 0
Seq('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAG...TTC', SingleLetterAlphabet())
Record Id:  NC_010473.1
'''
def parse_file(filename, formatname, length): 
    '''
        filename: file path
        formatname: 'fasta', 'abi', 'genbank or gb' etc...
    '''
    with open(filename, "rU") as handle:
        for record in SeqIO.parse(handle, formatname) :
            if len(record.seq)>length:
                base_top1000 = record.seq[:length]
        return record, base_top1000