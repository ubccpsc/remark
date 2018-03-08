import csv

# define your scoring approach here
# values should be numeric
right=2
wrong=-1
blank=0

# these are question blocks -- so 1-4 was one question, 5-7 was another question, etc.
# basically, boundaries of how far negative marks can go.
questions=[] 
questions.append([1,5])
questions.append([6,10])
questions.append([11,14])
questions.append([15,18])
questions.append([19,21])
questions.append([22,25])
questions.append([26,31])
questions.append([32,35])
questions.append([36,38])
questions.append([39,41])
questions.append([42,45])
questions.append([46,50])

# define the questions you wish to give free marks for here
# e.g., questions that in retrospect were in error (e.g., [] or [12] or [1, 24]).
freebies=[50]

def myprint(x):
	print x

solutions=[]
with open("rubric.csv",'rb') as infile:
	csv_reader = csv.reader(infile)
	header=None
	for row in csv_reader:
		if not header:
			header = row
		else:
			solutions.append(row)
	
answers=[]
with open("answers.csv",'rb') as infile:
	csv_reader = csv.reader(infile)
	header=None
	for row in csv_reader:
		if not header:
			header = row
		else:
			answers.append(row)


grades=[]
for answer in answers:
	student_rec = []
	student_rec.append(answer[0])
	print "Grading student: ",answer[0]
	for i in range(2,len(answer)):
 		print solutions[0][i],"---------", answer[i]
		if i in freebies:
			student_rec.append(right)
		elif solutions[0][i]==answer[i]:
			student_rec.append(right)
		elif answer[i]=="BLANK":
			student_rec.append(blank)
		else:
			student_rec.append(wrong)
# 	print solution
# 	print answer
# 	print student_rec
	grades.append(student_rec)

# print "-----"
# for grade in grades:
# 	print grade

marks = []
for grade in grades:
	student_mark = []
	student_mark.append(grade[0])
	print grade
	for question in questions:
# 		print "question is: ",question
		qmark = 0
		for i in range(question[0],question[1]+1):
# 			print str(i-1),":",grade[i], "...", header[i]
			qmark = qmark+grade[i]
# 		print "Qmark: ",qmark
		if qmark<0:
			qmark=0
		student_mark.append(qmark)
	marks.append(student_mark)
	
# for mark in marks:
# 	print mark

totals = []
the_total=0
for mark in marks:
	student_total=[]
	student_total.append(mark[0])
	sum=0
	for i in range(1,len(mark)):
		sum=sum+mark[i]
	student_total.append(sum)
	totals.append(student_total)
	the_total=the_total+float(sum)
# 	print "the total: ", the_total

for i in range(0,len(grades)):
# 	print "======"
# 	print solution
# 	print answers[i]
# 	print grades[i]
# 	print marks[i]
	print "totals: " , totals[i]

# print "AVERAGE: ",str(average)

results_header = ['username', 'exam type', 'points', 'Final Exam [Total Pts: 40] |1742451']
with open("results.csv", 'wb') as out_file:
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(results_header)
    for total in totals:
        csv_writer.writerow(total)

results_header = ['username','put one column per question']
with open("questionmarks.csv", 'wb') as out_file:
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(results_header)
    for mark in marks:
        csv_writer.writerow(mark)

with open("individualgrades.csv", 'wb') as out_file:
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(results_header)
    for grade in grades:
        csv_writer.writerow(grade)

