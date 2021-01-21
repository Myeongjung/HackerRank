#69. Hex Color Code
import re

re_exp = r"(?<!^)(#(?:[0-9a-f]{3}){1,2})"

for _ in range(int(input())):
    m = re.findall(re_exp, input(), re.I)
    if m : print('\n'.join(m))

	
#70. HTML Parser - Part 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("->", i[0], ">" , i[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print("->", i[0], ">" , i[1])

if __name__ == "__main__":
    parser = MyHTMLParser()
    
    for _ in range(int(input())):
        parser.feed(input())
		
	parser.close()

	
#71. HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.strip())
            
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
  
  

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()	

	
#72. Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">" , i[1])

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()    


#73. XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return (len(node.attrib)+sum(get_attr_number(child) for child in node))

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

	
#74. XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
	
	
#75. Validating UID
import re

size = re.compile(r"[A-Za-z0-9]{10}")
upper = re.compile(r"([A-Z].*){2}")
digit = re.compile(r"([0-9].*){3}")
dup = re.compile(r".*(.).*\1")

for _ in range(int(input())):
    tmp = input()
    
    if size.search(tmp) and upper.search(tmp) and digit.search(tmp) and not dup.search(tmp):
        print('Valid')
    else:
        print('Invalid')


#76. Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f("+91 "+c[-10:-5]+" "+c[-5:] for c in l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#77. Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda x:int(x[2]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#78. Shape and Reshape
import numpy as np

myArray = np.array(list(map(int, input().split())))
print(np.reshape(myArray, (3,3)))

#One line
#print(np.array(input().split(),int).reshape(3,3))

#79. Transpose and Flatten
import numpy as np

N, M = map(int, input().split())

myArray = np.array([input().strip().split() for _ in range(N)], int)

print(myArray.transpose())
print(myArray.flatten())

#80. Concatenate
import numpy as np

n, m, p = map(int, input().split())

firstArray = np.array([input().split() for _ in range(n)], int)
secondArray = np.array([input().split() for _ in range(m)], int)

print(np.concatenate((firstArray, secondArray), axis=0))