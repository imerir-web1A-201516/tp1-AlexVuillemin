import random

grades = [] # make an empty list

# for i from 0 to 9, add random grades to the list
for i in range(10):
  grades.append(random.randint(0,20))

print "All the grades:"
print grades

def average(items):
 s = 0.0
 for i in items:
   s += i
 return s/len(items)

def bubbleSort(items):
 s = 0.0
 for i in items:
   s += i
 return s/len(items)

# compute the average

print "Average:", average(grades)

def printGrades(items):
 for idx,value in enumerate(grades):
   print "grades[%d] -> %d" % (idx, value)

printGrades(grades)

def swap(items, i, j):
 tmp = items[i]
 items[i] = items[j]
 items[j] = tmp

swap(grades, 0, 1)

printGrades(grades)