--Test: Student Analysis
select a.roll_number, a.name
from student_information a join examination_marks b
on a.roll_number = b.roll_number
where (b.subject_one + b.subject_two + b.subject_three) <100;