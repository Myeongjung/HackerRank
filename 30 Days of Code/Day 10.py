#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = bin(int(input()))[2:]
    count = max(n.split('0')).count('1')
    
    print(count)