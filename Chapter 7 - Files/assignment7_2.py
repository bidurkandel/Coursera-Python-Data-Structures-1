#!/usr/bin/python

# Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as shown
# below. Do not use the sum() function or a variable named sum in your solution.

# You can download the sample data at
# http://www.pythonlearn.com/code/mbox-short.txt when you are testing below
# enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
num_lines = 0
tot_value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num_lines = num_lines + 1
    value = float(line.split(':', 1)[1].strip())
    tot_value = tot_value + value
print "Average spam confidence: " + str(tot_value / num_lines)