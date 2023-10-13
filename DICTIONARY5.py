'''
---Program 20---
Write a in python to create the following dictionary and display the total score and grade as dictionary.

d={s1:{'name':'AA','marks':{'eng':[15,20,18],'math':[20,15,19],'comp':[18,20,20]}},s2:.....}

Dictgrade={s1: {m1:[98.00,’A’],m2:[88,’A2’],m3:[75,’B1’],s2:.....}
'''

import math
import statistics
import json
main = {}
main1 = {}
z = int(input("Enter the number of students:"))
print("\n")
for d in range(z):
      student = {}
      student1 = {}
      st = {}
      sst = {}
      student['name'] = input("Enter your name:")
      for c in range(3):
            l=[]
            l1 = []
            a = input("Enter the subject name:")
            b =  input("Enter 3 scores (out of 20) with space:").split()
            print("\n")
            for e in range(3):
                  l.append(int(b[e]))
            if statistics.mean(l)*5 >= 91:
                  grade = 'A1'
            elif statistics.mean(l)*5 >= 81:
                  grade = 'A2'
            elif statistics.mean(l)*5 >= 71:
                  grade = 'B1'
            else:
                  grade = 'B2'
            l1 = [math.ceil(statistics.mean(l))*5,grade]
            st[a] = l
            student1[a] = l1
      student['marks'] = st
      main.setdefault('s'+str(d+1),student)
      main1['s'+str(d+1)] = student1
print(json.dumps(main,indent = 2),"\n")
print(json.dumps(main1,indent = 2))
