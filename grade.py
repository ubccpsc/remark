import csv

def myprint(x):
	print x

solutions={}
students={}

# score for a right answer
right=2
# score for a wrong answer
wrong=-1
# score for a blank answer
blank=0

# number of questions
testlength=50

# number of points to adjust the exam (raw score)
gradeadjustment=0

# if points don't roll over, specify question boundary
# start at 1, end at n+1
questionbounds = {
	'A':[1,5,8,12,16,19,23,27,31,37,42,47,51],
	'B':[1,6,11,15,19,22,26,30,34,40,44,47,51],
	'X':[1,5,8,12,16,19,23,27,31,37,42,47,51]
}

# list of questions to skip grading (aka pretend they don't exist)
skipgrades={
	'A':[37, 41],
	'B':[1, 5],
	'X':[37, 41]
}

SNUMtoCSID={}
SNUMtoName={}

# get classlist (change XXX to you're corse number e.g., 310):
# ssh remote.cs.ubc.ca '/cs/local/bin/classlist -T -L -f "\"%LN, %FN\",%SN,%ACCT" XXX' > classlist.csv

with open("classlist.csv",'rb') as infile:
	csv_reader = csv.reader(infile)
	header=None
	for row in csv_reader:
		# print "grading key is: "+str(row)
		if not header:
			header = row
			# print "header is: "+str(row)
		if not row[0] in solutions:
			SNUMtoCSID[row[1]] = row[2]
			SNUMtoName[row[1]] = row[0]


#rubric schema: rubricID , 1...n

with open("rubricAB.csv",'rU') as infile:
	csv_reader = csv.reader(infile)
	header=None
	for row in csv_reader:
		print "grading key is: "+str(row)
		if not header:
			header = row
			print "rubric header is: "+str(row)
		if not row[0] in solutions:
			solutions[row[0]] = row[1:]

#print "all solutions is: "+str(solutions)


answers=[]
	
with open("realanswers.csv",'rU') as infile:
	csv_reader = csv.reader(infile)
	header=None
	for row in csv_reader:
		if not header:
			header = row
			print "answers header is: "+str(row)
		else:
			answers.append(row)


grades=[]

for answer in answers:
	student_rec = []
	student_rec.append(answer[0]) #keep track of their SNUM
	student_rec.append(answer[1]) #keep track of their key
	print "Grading student: ",answer
	key = solutions[answer[1]]
	sanswer = answer[2:]
	print "Comparing against "+str(answer[1])+":"+str(key)

	for i,(k,a) in enumerate(zip(key,sanswer)):
		if i+1 in skipgrades[answer[1]]:
			student_rec.append(1)
			print ">>>>>>>>>>>SKIPPED"			
		elif k=="x":
			student_rec.append(1)
		elif a == "BLANK":
			student_rec.append(0)
		elif k==a:
			student_rec.append(1)
		else:
			student_rec.append(-.5)


	grades.append(student_rec)

	
	
for grade in grades:
	print grade
	


marks = []

for grade in grades:
	student_mark = []
	key=grade[1]
	snum=grade[0]
	student_mark.append(snum)
	student_mark.append(key)
	print grade
	bounds=questionbounds[grade[1]]
	sgrades=grade[2:]
	print "len sgrades"
	print len(sgrades)
	for i in range(0,len(bounds)):
		print "bounds index is: "+str(i)+" at question "+str(bounds[i])
		if bounds[i]>=testlength:
			break
		# print "question is: ",question
		qmark = 0
		for j in range(bounds[i],bounds[i+1]):
			qmark = qmark+sgrades[j-1]  #question bounds are indexed from 1 so must subtract 1
			print j
		print "Qmark: ",qmark
		if qmark<0:
			qmark=0
		student_mark.append(qmark)
	marks.append(student_mark)
	
for mark in marks:
	print mark


totals = []
the_total=0
for mark in marks:
	student_total=[]
	student_total.append(mark[0])
	sum=0
	for i in range(2,len(mark)):
		sum=sum+mark[i]
	student_total.append(sum+gradeadjustment)
	totals.append(student_total)
	the_total=the_total+float(sum)
# 	print "the total: ", the_total


def cvsexport(name,records,header):
	with open(name,'wb') as out_file:
		csvwriter = csv.writer(out_file)
		csvwriter.writerow(header)
		for i in range(0,len(grades)):
			outrow=[]
			outrow.append(records[i][0])
			outrow.append(SNUMtoCSID[records[i][0]])
			outrow.append(SNUMtoName[records[i][0]])
			outrow=outrow+records[i][1:]
			# csvwriter.writerow(records[i])
			csvwriter.writerow(outrow)

cvsexport('totals.csv',totals,["SNUM","CSID","Name","Grade"])
marksheader=[i for i in range(0,len(marks[0]))]
cvsexport('qmarks.csv',marks,["SNUM","CSID","Name","Key"]+marksheader)
questionsheader=[i for i in range(1,testlength)]
cvsexport('grades.csv',grades,["SNUM","CSID","Name","Key"]+questionsheader)



total=0
for t in totals:
	total += t[1]


print "AVERAGE: ",str(total/len(totals)/testlength)


