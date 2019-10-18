def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] > 37:
            if (grades[i] % 5) > 2:
                grades[i] += (5 - (grades[i]% 5))
    return(grades)
