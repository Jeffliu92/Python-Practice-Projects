#WRITE A FUNCTION THAT TAKES A LIST OF TEST SCORES AND RETURNS
def average_score(grades):
    sum = 0
    for grade in grades:
        sum += grade
    return round(sum/len(grades),2)

#CREATE A FUNCTION TO CATOGORIZE THE GRADE TO LETTER GRADE A, B, C, D AND F
def letter_grade(grades):
    empty_dict = {"A":0, "B":0, "C":0, "D":0, "F":0}
    #The letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: below 60)
    for grade in grades:
        if grade >= 90:
            empty_dict["A"] += 1
        elif 80<grade<89:
            empty_dict["B"] += 1
        elif 70<grade<79:
            empty_dict["C"] += 1
        elif 60<grade<69:
            empty_dict["D"] += 1
        else:
            empty_dict["F"] += 1
    return empty_dict


print(average_score([90, 85, 78,67, 95, 96, 86]))
print(letter_grade([90, 85, 78, 67, 95, 96, 86]))
