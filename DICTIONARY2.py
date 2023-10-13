
'''
---Program 17---
Write a menu driven program to perform the following on a dictionary
            Menu
    1. Create a dictionary
    2. Maximum value
    3. Remove duplicate values
    4. Sort  based on keys/values
    5. Exit

'''

d = {}
while True:
      print('''        Menu
#1 Create a Dictionary
#2 Maximum Value
#3 Remove duplicate values
#4 Sort the keys/values
#5 Exit''')
      z = input("Enter your choice:")
      print("\n")
      if z =='1':
            l = input("Enter key followed by value:").split()
            d = dict(zip(l[0::2],l[1::2]))
            print("\n")
            print("The entered dictionary: ",d,"\n")

      if z == '2':
            maxx = 0
            for c in d.keys():
                  if int(d[c]) > maxx:
                        maxx = int(d[c])
                        k = c
            print("\t",k,":",maxx,"\n")
      if z == '3':
            d1 =  {}
            for c in d.keys():
                  if int(d[c]) not in  d1.values():
                        d1[c] = int(d[c])
            print(d1,"\n")
            d = d1
      if z == '4':
            o = input("Enter 'k' to sort keys and 'v' to sort values:")
            print("\n")
            if o == 'k':
                  print("The sorted keys:",{f:d[f] for f in sorted(d)},"\n")
                  d = {f:d[f] for f in sorted(d)}
            elif o == 'v':
                  d2 = {}
                  for c in sorted(d.values()):
                        for k in d.keys():
                              if d[k] == c:
                                    d2[k] = c
                  print(d2,"\n")
                  d = d2
      if z == '5':
            print("Exiting now...")
            break
