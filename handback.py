import html_writer as HTML
import csv

prefix="CPSC310-2018W1-HB-"
dash="-"
extension=".html"
path='handback-files/'
path_to_pdf="https://www.ugrad.cs.ubc.ca/~cs310/handback/index2.php?file=CPSC310-2018WT1-MT1/CPSC310-2018WT1-MT1"
pdf_extension=".pdf"

snum_to_csid={}
snum_to_midterm={}
snum_to_answers={}
snum_to_grades={}
snum_to_key={}
testlength=50
right="E0E9CF"
wrong="pink"

rightScore='2'
wrongScore='-1'
blankScore='BLANK'

with open('totals.csv', 'rb') as recfile:
	recfile_reader = csv.reader(recfile)
	headerrow=None
	for row in recfile_reader:
		if not headerrow:
			headerrow = row
		else:
			snum=row[0]
			csid=row[1]
			midterm=row[3]
			snum_to_midterm[snum]=midterm
			snum_to_csid[snum]=csid


with open('realanswers.csv', 'rb') as recfile:
	recfile_reader = csv.reader(recfile)
	headerrow=None
	for row in recfile_reader:
		if not headerrow:
			headerrow = row
		else:
			snum=row[0]
			key=row[1]
			answers=row[2:]
			snum_to_key[snum]=key
			snum_to_answers[snum]=answers

with open('grades.csv', 'rb') as recfile:
	recfile_reader = csv.reader(recfile)
	headerrow=None
	for row in recfile_reader:
		if not headerrow:
			headerrow = row
		else:
			snum=row[0]
			grades=row[4:]
			snum_to_grades[snum]=grades

def writeMTResultsTable(start,end):
	handback.startTableRow()
	for i in range(start,end):
		handback.writeCell(i+1)
	handback.endTableRow()
	handback.startTableRow()
	for i in range(start,end):
		color='white'
		if grades[i]==rightScore:
			color=right
		if grades[i]==wrongScore:
			color=wrong
		if answers[i]==blankScore:
			answers[i]=""
			color='white'

		handback.writeColorCell(answers[i],color)
	handback.endTableRow()


for snum in snum_to_csid:	
	csid = snum_to_csid[snum]
	midterm = snum_to_midterm[snum]
	answers = snum_to_answers[snum]
	grades = snum_to_grades[snum]
	key = snum_to_key[snum]


	handback=HTML.Writer(path+prefix+csid+dash+snum+extension)
	handback.startTable()
	handback.writeTableTitle(csid+" : "+snum+"<h1>",1)
	handback.startTableRow()
	handback.writeCell("Midterm grade: "+str(midterm)+"/"+str(testlength*2)+''
		# 'https://www.ugrad.cs.ubc.ca/~cs410/handback/index2.php?file=CPSC410-2018WT1-MT1/CPSC410-2018WT1-MT1-63522163-ebani.pdf'
		' | <a href="https://www.ugrad.cs.ubc.ca/~cs310/handback/index2.php">Your scanned answer sheet</a>'
		' | <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSFJXhZOkBJvRbon1ejaprPpF0OWQrSP3Le5lzgBXB9hptY7frJKKsRYChM_2vHvQ8o2wAoqUFSdBwo/pubhtml">Grading key</a>'
		' | Your grading key was: '+key+' -- Please look in the correct column for question numbers!!'
		' -- please check the grading key for discarded questions')
	handback.endTableRow()
	handback.endTable()

	handback.startTable()
	writeMTResultsTable(0,testlength/2)
	writeMTResultsTable(testlength/2,testlength)

	handback.endTable()