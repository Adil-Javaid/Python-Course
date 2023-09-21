import numpy as np
from scipy import linalg

#Test has 30 questions and worth 150 marks
#True and false questions worth 4 marks each
#Mcqs worth 9 points each
#let x is the number of true/false question
#let y is the number of mcqs

# (x + y = 30)
# (4x = 9y = 150)

testQuestionVariable = np.array([[1,1],[4,9]])
testQuestionValue = np.array([30,150])

print(linalg.solve(testQuestionVariable,testQuestionValue))