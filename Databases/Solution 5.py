# Map Reduce Advanced - Count number of friends

import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
   	self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print "{\"key\":\""+item[0]+"\",\"value\":\"" + str(item[1]) + "\"}"

mapReducer = MapReduce()

def mapper(record):
    v1, v2 = record.split()
    mapReducer.emitIntermediate(v1, v2)
    mapReducer.emitIntermediate(v2, v1)

def reducer(key, list_of_values):
    mapReducer.emit([key, len(list_of_values)])

if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)
  
  
# Map Reduce Advanced - Relational Join

import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
   	self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print item

mapReducer = MapReduce()

def mapper(record):
    words = record.rstrip().split(',')
    if words[0]=='Department':
        mapReducer.emitIntermediate(words[1],('D',words[2]))
    elif words[0]=='Employee':
        mapReducer.emitIntermediate(words[2],('P',words[1]))
        
def reducer(key, list_of_values):
    list_of_values.sort()
    name = list_of_values[-1][-1]
    for d in list_of_values:
        if d[0]!='P':
            mapReducer.emit((key,name, d[-1]))

if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)
  
  
# Map Reduce Advanced - Matrix Multiplication
 
 import sys
from collections import OrderedDict


class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)


    def emit(self, value):
        self.result[value[0]][value[1]] = value[2]


    def execute(self, matrix1, matrix2, mapper, reducer):
        n = len(matrix1)
        m = len(matrix2[0])
        for i in xrange(0, n):
            self.result.append([0] * m)

        mapper(matrix1, matrix2)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for i in xrange(0, n):
            row = ""
            for j in xrange(0, m):
                row += str(self.result[i][j]) + " "
            print(row)

mapReducer = None

def mapper(matrix1, matrix2):
    r1 = len(matrix1)
    c1 = len(matrix1[0])
    c2 = len(matrix2[0])

    for h in range(r1):
        for i in range(c2):
            l = []
            for j in range(c1):
                l.append(matrix1[h][j]*matrix2[j][i])
            mapReducer.emitIntermediate(str(h)+' '+str(i), l)

def reducer(key, list_of_values):
    h, i = map(int, key.split())
    mapReducer.emit([h, i, sum(list_of_values[0])])

if __name__ == '__main__':
    testcases = int(raw_input())
    for _ in xrange(testcases):
        mapReducer = MapReduce()
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        matrix1 = []
        matrix2 = []
        
        for i in range(row):
            read_row = sys.stdin.readline().strip()
            matrix1.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix1[i].append(int(row_elems[j]))
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        
        for i in range(row):
            read_row = sys.stdin.readline().strip()
            matrix2.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix2[i].append(int(row_elems[j]))
        
        mapReducer.execute(matrix1, matrix2, mapper, reducer)