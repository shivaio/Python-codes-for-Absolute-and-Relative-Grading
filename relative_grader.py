from tabulate import tabulate
import random
import matplotlib.pyplot as plt

roll_list = []
marks = []
grade_list = []
num_students = int(input("Enter number of students in the class:" + "\n"))

#Generating student data instead of using excel sheet containing data
for index in range(1,num_students+1):
    roll_list.append("CSE20B" + str(index))
    if index % 2 == 0:
        random_number = random.randint(20, 50)
        marks.append(random_number)
    else:
        random_number = random.randint(50, 100)
        marks.append(random_number)

head = ["Roll_NUmber","Marks"]
table = []

#Table to display Original Student data
for index in range(num_students):
    table.append([roll_list[index],marks[index]])

print(tabulate(table, headers=head, tablefmt="grid"))

mean_marks = sum(marks) / num_students

passing_minimum = (1/2)*mean_marks

max_mark = max(marks)

passing_student_list_mark = []
passing_student_roll_number = []

for mark in marks:
    if mark >= passing_minimum :
        passing_student_list_mark.append(mark)
        passing_student_roll_number.append(roll_list[marks.index(mark)])

passing_student_mean = sum(passing_student_list_mark) / len(passing_student_roll_number)

X = passing_student_mean - passing_minimum

S_cutoff = max_mark - 0.1 * (max_mark - passing_student_mean)

Y = S_cutoff - passing_student_mean

A_cutoff = passing_student_mean + Y * (5/8)

B_cutoff = passing_student_mean + Y * (2/8)

C_cutoff = passing_student_mean - X * (2/8)

D_cutoff = passing_student_mean - X * (5/8)

E_cutoff = passing_minimum




for mark in marks:
    if mark >= S_cutoff:
        grade_list.append("S")
    elif mark >= A_cutoff:
        grade_list.append("A")
    elif mark >= B_cutoff:
        grade_list.append("B")
    elif mark >= C_cutoff:
        grade_list.append("C")
    elif mark >= D_cutoff:
        grade_list.append("D")
    elif mark >= passing_minimum:
        grade_list.append("E")
    else:
        grade_list.append("F")

print(grade_list)
head = ["Roll_NUmber","Marks","Grade"]
table = []

#Table to display Student data  with  calculated grade
for index in range(num_students):
    table.append([roll_list[index],marks[index],grade_list[index]])

print(tabulate(table, headers=head, tablefmt="grid"))

print(f" Average Marks Scored by {num_students} students in the class is {mean_marks}")

print(f" Passing minimum for the class is {passing_minimum}")


grade_s_count = grade_list.count("S")

grade_a_count = grade_list.count("A")


grade_b_count = grade_list.count("B")


grade_c_count = grade_list.count("C")

grade_d_count = grade_list.count("D")

grade_e_count = grade_list.count("E")

grade_f_count = grade_list.count("F")

bar_data = {'S': grade_s_count,'A':grade_a_count,'B': grade_b_count,'C': grade_c_count,'D':grade_d_count,'E':grade_e_count,'F':grade_f_count}
act_grades_list = list(bar_data.keys())
grade_count_list = list(bar_data.values())

head = ["Grades","Count"]
frequency_table = []

#Frequency table showing grades and count values
for index in range(len(act_grades_list)):
    frequency_table.append([act_grades_list[index],grade_count_list[index]])

# print(tabulate(frequency_table, headers=head, tablefmt="pretty"))

string = tabulate(frequency_table, headers=head, tablefmt="tsv")
text_file=open("output_rel.csv","w")
text_file.write(string)
text_file.close()

fig = plt.figure(figsize=(10, 5))

plt.bar(act_grades_list, grade_count_list, color='green',width=0.4)

plt.xlabel("Grades")
plt.ylabel("No. of students")
plt.title(" Grades of Students in the course")
plt.show()
