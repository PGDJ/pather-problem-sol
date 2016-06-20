import sys
import re
import bisect

try:
	fi = open(sys.argv[1])
	try:
		input = fi.read()
	finally:
		fi.close()
except IOError:
	print "Could not open input file!"
try:
	fo = open(sys.argv[2], 'w')
except IOError:
	print "Could not open output file!"
lines = input.split('\n')
num_points = len([m.start() for m in re.finditer('#', input)])
point_found = False
x = 0
for line in lines:
	if num_points > 0:
		marks_line = [m.start() for m in re.finditer('#', line)]
		len_marks_line = len(marks_line)
		if(len_marks_line >  1):
			if point_found:
				try:
					point=marks_line.index(x)
				except ValueError:
					bisect.insort_left(marks_line,x)
					for i in range(0, len_marks_line+1):
						if(i == 0):
							if(marks_line[0] == x):
								fo.write(line[:(marks_line[0])]+"*")
							else:
								fo.write(line[:(marks_line[0]+1)])
						elif(marks_line[i] == x):
							fo.write(('*' * (marks_line[i]-marks_line[i-1])))
						else:
							fo.write(('*' * (marks_line[i]-marks_line[i-1]-1)) + '#')
					fo.write(line[marks_line[len_marks_line]+1:] +'\n')
					if x == marks_line[len_marks_line]:
						x = marks_line[0]
					else:
						x = marks_line[len_marks_line]
				else:
					end = marks_line[len_marks_line-1]
					fo.write(line[:(marks_line[0]+1)])
					for i in range(1, len_marks_line):
						fo.write(('*' * (marks_line[i]-marks_line[i-1]-1)) + '#')
					fo.write(line[end+1:] +'\n')
					if (x == end):
						x = marks_line[0]
					else:
						x = end
			else:
				x = marks_line[len_marks_line-1]
				fo.write(line[:(marks_line[0]+1)])
				for i in range(1, len_marks_line):
					fo.write(('*' * (marks_line[i]-marks_line[i-1]-1)) + '#')
				fo.write(line[x+1:] +'\n')
			point_found = True
			num_points -= len_marks_line
		elif(len_marks_line > 0):
			if (point_found):
				if x > marks_line[0]:
					fo.write(line[:(marks_line[0]+1)]+('*' *(x-marks_line[0]-1)) + '*' + line[(x+1):] +'\n')
				else:
					fo.write(line[:(x)]+'*'+('*' * (marks_line[0] - x - 1)) + line[marks_line[0]:] +'\n')
			else:
				fo.write(line+'\n')
				point_found = True
			x = marks_line[0]
			num_points -= 1
		elif (point_found and len_marks_line == 0):
			fo.write(line[:x]+'*'+line[(x+1):]+'\n')
		else:
			fo.write(line+'\n')
	elif (line):
		fo.write(line+'\n')
