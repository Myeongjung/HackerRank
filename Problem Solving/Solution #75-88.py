#75. Caesar Cipher
def caesarCipher(s, k):
    abc = "abcdefghijklmnopqrstuvwxyz"
    pos = {c: i for i, c in enumerate(abc)}

    ciphered = []
    for c in s:
        cl = c.lower()
        if cl in abc:
            new_ind = (pos[cl] + k) % 26
            cipher_letter = abc[new_ind] if c.islower() else abc[new_ind].upper()
            ciphered.append(cipher_letter)
        else:
            ciphered.append(c)
            
    return ("".join(ciphered))

#76. Mars Exploration
def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if s[i] != 'SOS'[i%3]:
            count += 1
            
    return count

#77. HackerRank in a String!
def hackerrankInString(s):
    return 'YES' if re.search(r'.*?'.join(list("hackerrank")), s) else 'NO'

#78. Pangrams
from collections import Counter

def pangrams(s):
    c = Counter(s.lower().replace(" ", ""))
    
    return "pangram" if len(c.keys()) == 26 else "not pangram"

