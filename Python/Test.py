# Test: Reverse Words and Swap Cases
def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(' ')[::-1]
    results = ""
    
    for word in words:
        for character in word:
            if character.isupper():  
                results += character.lower()
            else:
                results += character.upper()
        results+= " "
    return(results)
	
#Simpler
#def swap_case(word):
#    return ''.join([character.lower() if character.isupper() else character.upper() for character in word])

#def reverse_words_order_and_swap_cases(sentence):
#    words = sentence.split(' ')[::-1]
#    return ' '.join([swap_case(word) for word in words])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = raw_input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
	
#Test: Multiset Implemenation

import math
import os
import random
import re
import sys


class Multiset(object):
    def __init__(self):
        self.m = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.m.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.m:
            self.m.remove(val)
    
    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.m:
            return True
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.m)
        
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(raw_input())
    operations = []
    for _ in xrange(q):
        operations.append(raw_input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()