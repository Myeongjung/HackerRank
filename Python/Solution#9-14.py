#9. Lists
if __name__ == '__main__':
    N = int(input())
    List = []
    
	#9.1 simple nested if, elif
    for _ in range(N): 
        inputs = input().split()
        cmd = inputs[0]
        args = inputs[1:]
        
        if cmd=="insert":
            List.insert(int(args[0]),int(args[1]))
        elif cmd=="remove":
            List.remove(int(args[0]))
        elif cmd=="append":
            List.append(int(args[0]))
        elif cmd=="sort":
            List.sort()
        elif cmd=="pop":
            List.pop()
        elif cmd=="reverse":
            List.reverse()
        elif cmd=="print":
            print(List)
			
		#9.2 Use eval
		for _ in range(N): 
        inputs = input().split()
        cmd = inputs[0]
        args = inputs[1:]
        
        if cmd != "print":
            cmd += "(" + ",".join(args)+")"
            # print(cmd)
            eval("List." + cmd)
        else:
            print(List)

#10. Nested Lists
if __name__ == '__main__':
    record = {}
    scores = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        record[name] = score
        scores.append(score)
        
    temp = sorted(set(scores))[1]
    
    for key, value in record.items():
        if value == temp:
            names.append(key)
            
    print(*[name for name in sorted(names)], sep='\n')

#11. Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    print(hash(tuple(integer_list)))
	
#12. Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
	
#13. Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    print("{:.02f}".format(sum(scores)/len(scores)))