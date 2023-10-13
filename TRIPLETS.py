
'''
---Program 15---
Write  a program in python to input  a tuple of integers, find all triplets of numbers that add up to a particular number.
'''

while True:
      l = []
      t = ()
      count = 0
      n = int(input("Enter the number of numbers:"))
      print("\n")
      for c in range(n):
            t = t + (int(input("Enter the numbers: ")),)
      print("\n")
      z = int(input("Enter the number to check:"))
      for c in range(n-2):
            for d in range(c+1,n-1):
                  for e in range(d+1,n):
                        summ = t[c] + t[d] + t[e]
                        if summ == z:
                              count += 1
                              check = str(t[c])+str(t[d])+str(t[e])
                              if not (''.join(sorted(str(check)))) in l:
                                    l.append(''.join(sorted(str(check))))
                                    print("Triplet:",t[c],t[d],t[e])
      print("No of possibilities:",count,"\n")
      y = input("Enter 'y' to continue(or any other key to exit)")
      print("\n")
      if y == 'y':
            continue
      else:
            print("Exiting now...")
            break
