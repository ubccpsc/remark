# Remark Script

The Remark multiple choice system exports an extremely wide spreadsheet. This script ingests a CSV-based version of the complete marking output (`answers.csv`) and compares each row against a rubric spreadsheet (`rubric.csv`). 

## Preparation

Make sure there are no extra columns in `answers.csv` or `rubric.csv`. This often happens if the grade sheet had extra entries that were not used for an exam. Ensure the structure of `answers.csv` is one-row-per-student. The first column of this sheet should be student numbers, the second column should be exam version (typically ignored), and each subsequent column should correspond to an exam question.

In `grades.py`:

* Set your values for `right`, `wrong`, and `blank`. (2, -1, 0 is common, as is 1, 0, 0).

* Determine your question groups; these are mainly useful if you have meta questions that you do not want negative scores to flow across (e.g., Q1-Q5 might be all answers for question A, so you would enter `[1,5]`). If you do not have negative values you can just enter the numeric values according to `[1,NumQuestions]`.

* Enter a list of free questions if you determine a question should be just marked as correct for all students.


## Execution

To invoke the script, simply call the student spreadsheet `answers.csv` and your answer key `rubric.csv` and run `python grade.py`. This will emit several other spreadsheets, along with a plethora of debug information on the console.

## Analysis

* `results.csv` contains the exam grades.

* `individualgrades.csv` can be used to generate per-question statistics for an exam. For example, you could add a formula row across all columns that contains `XXX`; this would give you the class percentage on each question (% that got it right out of the class, this ignores any penalties etc). You can also verify your freebies by making sure the cells in the freebie columns are only `right`.

* `questionmarks.csv` contains the scores for the grouped questions.

## Tips

* Restructuring all-that-apply multiple choice questions into true/false is often easiest to reason about and is the way this script has been used.

* Adding a row to `answers.csv` that is 100% correct, and another that is 100% incorrect can be a good way to do a sanity check on your `rubric.csv`.