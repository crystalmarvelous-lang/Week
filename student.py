class Students:
    def __init__(self, name, grade, age, naughtiness):
        self.name = name
        self.grade = grade
        self.age = age
        self.naughtiness = naughtiness
        self.subject = []

    def register(self, subject_name,):
        self.subject.append({
            "subject": subject_name,
            "score": 0,
            "grade": "F"
        })

def askQuestion(question, choices, correct_answer):
     print(question)
     for choice in choices:
          print(choice)
     answer = input("Enter your answer a/b/c/d: ")
     if answer.upper() == correct_answer.upper():
          print("Correct")
          return 1
     else:
          print("Wrong")
          return 0

def runEasymathquestions(student):
        score = 0
        score += askQuestion("What is 16 × 4 ?", ["A.32", "B.64", "C.12", "D.24"], "B")
        score += askQuestion("What is 15 + 6 ?", ["A.21", "B.61", "C.02", "D.08"], "A")
        score += askQuestion("What is 16 ÷ 2 ?", ["A.89", "B.04", "C.08", "D.54"], "C")
        score += askQuestion("What is 56 + 123?", ["A.123", "B.86", "C.11", "D.179"], "D")
        score += askQuestion("What is 5 × 5 ?", ["A.08", "B.25", "C.01", "D.100"], "B")
        for subject in student.subject:
             if subject == "Math":
                  subject.score += score



def runEasyenglishquestions():
        pass

student1 = Students("Emma", "P2", 7, 5)
student2 = Students("Alan", "U3", 19, 0)

student1.register("Math")
student1.register("English")
studentask = input("Alan or Emma: ").capitalize()
answer = studentask
if answer == "Emma":
    subject_name = input("Math or English: ").capitalize()
    if subject_name == "Math":
        runEasymathquestions(student1)
    else:
        runEasyenglishquestions(student1)
else:
     pass