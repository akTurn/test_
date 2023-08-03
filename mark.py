# def print_student_marks( name,*student_marks):
#     print(name)
# for marks in student_marks:
#     print(marks)
# # function invocation
#     print_student_marks('ditto', 90,80,70)
#     print_student_marks('Marshall', 90, 88)


def my_sum2(name, *student_marks):
    print('Hi ', name, ", ", 'Your total score is: ', sum(student_marks))

my_sum2("ditto", 90,80,70)
my_sum2("Marshall", 90, 88)
