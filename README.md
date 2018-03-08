# Remark Script

The Remark multiple choice system exports an extremely wide spreadsheet. This script ingests a CSV-based version of the complete marking output (`answers.csv`) and compares each row against a rubric spreadsheet (`rubric.csv`). 

## Preparation

Make sure there are no extra columns in `answers.csv` or `rubric.csv`. This often happens if the grade sheet had extra entries that were not used for an exam. Ensure the structure of `answers.csv` is one-row-per-student. The first column of this sheet should be student numbers, the second column should be exam version (typically ignored), and each subsequent column should correspond to an exam question.

## Execution

To invoke the script, simply call the student spreadsheet `answers.csv` and your answer key `rubric.csv` and run `python grade.py`. This will emit several other spreadsheets, along with a plethora of debug information on the console.

## Analysis

TBD

## Tips

* Restructuring all-that-apply multiple choice questions into true/false is often easiest to reason about and is the way this script has been used.

* Adding a row to `answers.csv` that is 100% correct, and another that is 100% incorrect can be a good way to do a sanity check on your `rubric.csv`.