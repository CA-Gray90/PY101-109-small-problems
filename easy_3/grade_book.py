# Write a function that determines the mean (average) of the three scores
# passed to it, and returns the letter associated with that grade.

# GET the mean from the 3 scores: add all 3, then divide sum by 3
# SUBPROCESS Determine where the grade falls within the letter grade list:
#   IF 90 <= mean <= 100: 'A'
#   IF 80 <= mean < 90: 'B'
#   etc... 

# def get_grade(score_1, score_2, score_3):
#     mean = (score_1 + score_2 + score_3) / 3
#     if mean >= 90:
#         return 'A'
#     elif mean >= 80:
#         return 'B'
#     elif mean >= 70:
#         return 'C'
#     elif mean >= 60:
#         return 'D'
#     else:
#         return 'F'
    
# def get_grade(score_1, score_2, score_3):
#     mean = (score_1 + score_2 + score_3) / 3

#     grades = {
#         'A' : 90,
#         'B' : 80,
#         'C' : 70,
#         'D' : 60,
#         'F' : 0,
#     }

#     for grade in grades:
#         if mean >= grades[grade]:
#             return grade
        
# def get_grade(score_1, score_2, score_3):
#     mean = (score_1 + score_2 + score_3) / 3
    
#     match mean:
#         case _ if mean in range(90, 101):
#             return 'A'
#         case _ if mean in range(80, 90):
#             return 'B'
#         case _ if mean in range(70, 80):
#             return 'C'
#         case _ if mean in range(60, 70):
#             return 'D'
#         case _:
#             return 'F'

# def get_grade(sc1, sc2, sc3):
#     mean = (sc1 + sc2 + sc3) / 3

#     grades_list = [
#         ('A', 90),
#         ('B', 80),
#         ('C', 70),
#         ('D', 60),
#         ('F', 0)
#     ]

#     for grade, pass_mark in grades_list:
#         if mean >= pass_mark:
#             return grade

# Solution in which you can pass multiple scores:

def get_grade(*scores):
    mean = sum(scores) / len(scores)

    grades_list = [
        ('A', 90),
        ('B', 80),
        ('C', 70),
        ('D', 60),
        ('F', 0)
    ]

    for grade, pass_mark in grades_list:
        if mean >= pass_mark:
            return grade

# LS Solution, takes advantage of Pythons ability to use multiple comparison
# operators in one line instead of more wordy expressions using `and` or `or`

# def get_grade(grade1, grade2, grade3):
#     average = (grade1 + grade2 + grade3) / 3

#     if 90 <= average <= 100:
#         return 'A'
#     elif 80 <= average < 90:
#         return 'B'
#     elif 70 <= average < 80:
#         return 'C'
#     elif 60 <= average < 70:
#         return 'D'
#     else:
#         return 'F'
    
print(get_grade(95, 90, 93, 91, 87) == "A")      # True
print(get_grade(50, 50, 95, 58, 56, 60) == "D")      # True
print(get_grade(65, 85, 95) == "B")      # True
print(get_grade(10, 30) == "F")      # True

# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True
# print(get_grade(65, 85, 95) == "B")      # True
# print(get_grade(10, 30, 65) == "F")      # True