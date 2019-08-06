# python3 genome_simulation.py --ini='bacteria.ini' --data='Escherichia_coli_DH10B.fasta'

from configparser import ConfigParser
import optparse
import simulationLib.parserLib as pl
import simulationLib.transitLib as tl
import random, os, sys
import logging
from datetime import datetime

#1. Initialize the config parser.
parser = ConfigParser()     # defining the parser
parser.read("config.ini")   # reading the config file
print("Step 1: Print the arguments of lamba section: ")
args_lambda = pl.parse_configurations(parser, 'lamba')
args_fasta = pl.parse_configurations(parser, 'fasta')
args_mutation = pl.parse_configurations(parser, 'mutation')

# 2. Get parameters dictionary which will act as metadata for this file and print.
lamba_min=args_lambda["lamba_min"]
lamba_max=args_lambda["lamba_max"]
lamba=args_lambda["lamba"]
generations=args_lambda["generations"]
numrows = args_lambda["numrows"]

fasta_filepath = args_fasta["fasta_filepath"]
fasta_top_num = args_fasta["fasta_top_num"]

print("\nlamba_min:", pl.print_parse_args(lamba_min))
print("\nlamba_max:", pl.print_parse_args(lamba_max))

print("\nlamba:", pl.print_parse_args(lamba))
print("\ngenerations:", pl.print_parse_args(generations))
print("\nnumber of rows:",pl.print_parse_args(numrows))

# 3. Parse Fasta.
print("\nStep 2: Parse Fasta: \nfasta_filepath:\n", pl.print_parse_args(fasta_filepath))
print("\nPerforming fasta parsing...:")

record, base_top = pl.parse_file(fasta_filepath, "fasta", int(fasta_top_num))
print("\nrecord: \n", record)
print("---------------------------------------")
print("Original Sequence: \n", base_top)
#print("\ntype(Original Sequence:): \n", type(base_top))

# 4. Transit all T->C, A->G.
str_base_top_TC = tl.transit(str(base_top), "T", "C")
str_base_top = tl.transit(str_base_top_TC, "A","G")

print("\nRound 1: After transit ALL T->C, A->G:\n", str_base_top)

# 5. Transit based on probability: C-> 50/50 G or A, G-> 50/50 C or T
#print(args_mutation)
target_prob_to_g=args_mutation["target_prob_to_g"]
target_prob_to_a=args_mutation["target_prob_to_a"]
target_prob_to_c=args_mutation["target_prob_to_c"]
target_prob_to_t=args_mutation["target_prob_to_t"]
if_mutate = args_mutation["if_mutate"]

target_prob_to_g=float(target_prob_to_g)
target_prob_to_a=float(target_prob_to_a)
target_prob_to_c=float(target_prob_to_c)
target_prob_to_t=float(target_prob_to_t)
if_mutate=int(if_mutate)

print("\nRound 2: Mutation with probability: Transit based on probability: C-> {} G or {} A; G-> {} C or {} T: ".format(target_prob_to_g, target_prob_to_a,target_prob_to_c, target_prob_to_t))

if if_mutate==1:
    str_base_top_list = list(str_base_top)
    i=0
    while i<len(str_base_top_list):
        if str_base_top_list[i]=='C':
            str_base_top_list[i]=tl.transit_prob(['G','A'],target_prob_to_g, target_prob_to_a)
            
        elif str_base_top_list[i]=='G':
            str_base_top_list[i]=tl.transit_prob(['C','T'],target_prob_to_c, target_prob_to_t)
        i+=1

else:
    print('\nSkip mutation.')
    sys.exit(5)

mutated_seq_str=''.join(str_base_top_list)
print('Round 2: Final mutated simulation:\n', mutated_seq_str)

# 6. Compare the 2 sequences:
difference_list=tl.transit_compare(base_top, mutated_seq_str)
print('\nCompare the 2 sequences:\n', difference_list)
