SELECT IF(Grades.grade < 8, NULL, Students.Name), Grades.Grade, Students.Marks FROM Students JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark
ORDER BY Grades.grade DESC, Students.Name, Students.Marks;
