#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
import string

P = 131
MOD = 10**9 + 7
VALID_CHARS = string.ascii_letters + string.digits

# Hash function
def compute_hash(password):
    hash_value = 0
    for char in password:
        hash_value = (hash_value * P + ord(char)) % MOD
    return hash_value

def generate_hashes(password):
    base_hash = compute_hash(password)
    hashes = {base_hash}
    for char in VALID_CHARS:
        extended_password = password + char
        extended_hash = compute_hash(extended_password)
        hashes.add(extended_hash)
    return hashes

def authEvents(events):
    current_hashes = set()
    results = []

    for event in events:
        action, param = event

        if action == "setPassword":
            current_hashes = generate_hashes(param)
        elif action == "authorize":
            query_hash = int(param)
            results.append(1 if query_hash in current_hashes else 0)

    return results

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
