#!/bin/python3

import math
import os
import random
import re
import sys

re_exp = r"^[\w.-]+\@gmail\.com$"

def email(s):
    return re.match(re_exp, s)

if __name__ == '__main__':
    N = int(input())
    result = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if email(emailID):
            result.append(firstName)

    print(*sorted(result), sep='\n')