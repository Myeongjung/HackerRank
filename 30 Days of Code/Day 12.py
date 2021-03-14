class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        Person.__init__(self, firstName, lastName, idNum)
        self.scores = scores
    
    def calculate(self):
        avg = sum(scores) // len(scores)
        
        if avg >= 90:
            return "O"
        elif avg in range(80,90):
            return "E"
        elif avg in range(70,80):
            return "A"
        elif avg in range(55,70):
            return "P"
        elif avg in range(40,55):
            return "D"
        else:
            return "T"


line = input().split()