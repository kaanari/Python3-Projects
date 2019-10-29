class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score


def print_names(students):
    indexes = find_lowest(students)
    print(indexes)
    for i in indexes:
        print(students[i].name)


def find_lowest(liste):

    minValue = 100
    minValue_index = 0
    seconValue_index = 0
    secondValue = 100
    secondValue_lists = []
    minValue_lists = []

    for i in range(len(liste)):
        if liste[i].score < minValue and liste[i].score < secondValue:
            secondValue = minValue
            seconValue_index = minValue_index
            minValue = liste[i].score
            minValue_index = i
            secondValue_lists.clear()
            secondValue_lists = minValue_lists.copy()
            minValue_lists.clear()

        elif liste[i].score == minValue:
            minValue_lists.append(i)

        elif liste[i].score > minValue and liste[i].score < secondValue:
            secondValue = liste[i].score
            seconValue_index = i
            secondValue_lists.clear()
        elif liste[i].score > minValue and liste[i].score == secondValue:
            secondValue_lists.append(i)


    secondValue_lists.append(seconValue_index)

    return secondValue_lists


students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append(Student(name,score))

print_names(students)

