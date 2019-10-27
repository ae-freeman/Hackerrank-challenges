class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores


    def calculate(self):
        result = sum(scores)/len(scores)


        if result >= 90 and result <= 100:
            letterGrade = "O"
        elif result >= 80 and result < 90:
            letterGrade = "E"
        elif result >= 70 and result < 80:
            letterGrade = "A"
        elif result >= 55 and result < 70:
            letterGrade = "P"
        elif result >= 40 and result < 55:
            letterGrade = "D"
        elif result < 40:
            letterGrade = "T"

        return letterGrade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
