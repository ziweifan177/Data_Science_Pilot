from configparser import ConfigParser
import numpy as np
import time
import json
import random, os, sys
from Bio import SeqIO #NEED TO INSTALL: pip install biopython
from scipy import stats

# Transit withouth probability.
def transit(ori_string, original_base, updated_base):
	'''
	ori_string: original sequencing string need to be transited.
	original_base: original indivdual base A/G/C/T needs to be transited.
	updated_base: the new base after updating.
	'''
	return ori_string.replace(original_base, updated_base)


#Transit with probability:
# C-> 50/50 G or A: C->G is p, C->A is (1-p)
# G-> 50/50 C or T: G->C is p, G->T is (1-p)
#def transit_half_prob(ori_string, original_base, target_base, prob): 
def transit_prob(target_bases_list, prob1, prob2): 
    picked_base = np.random.choice(target_bases_list, 1, p=[prob1, prob2])
    return (''.join(picked_base))

def transit_compare(original_seq, mutated_seq):
    difference_list=[]
    original_seq_list=list(original_seq)
    mutated_seq_list=list(mutated_seq)

    #print("original_seq_list: \n", original_seq_list)
    #print("mutated_seq_list: \n", mutated_seq_list)

    if len(original_seq_list)==len(mutated_seq_list):
        for ori_base, mut_base in zip(original_seq_list, mutated_seq_list):
            if (ori_base != mut_base):
                difference_list.append(mut_base)
            else:
                difference_list.append('_') #Same base with original
        return ''.join(difference_list)
    else:
        print('The sequences have different length.')
        sys.exit(5)