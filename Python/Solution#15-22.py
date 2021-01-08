#15. String Split and Join
def split_and_join(line):
    string = "-".join(line.split(" "))
    return string
	
	#use replace
	return line.replace(" ","-")
	
#16. What's Your Name?
def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a,b))
	
#17. Find a string
def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        string = string[string.find(sub_string)+1:]
        count += 1
    return count
	
#18. String Validators
if __name__ == '__main__':
    s = input()
        
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
	
#19. Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
	
#20. Text Wrap
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    return "\n".join(wrapper.wrap(string))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
	
#21. Designer Door Mat
if __name__ == '__main__':
    N, M = map(int, input().split())
    
    for i in range(1,N,2): 
        print((i * ".|.").center(M, "-"))
        
    print("WELCOME".center(M,"-"))
    
    for i in range(N-2,-1,-2): 
        print((i * ".|.").center(M, "-"))

#22. Capitalize!
def solve(s):
    string = s.split()
    for st in string:
        s = s.replace(st, st.capitalize())

    return s

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()