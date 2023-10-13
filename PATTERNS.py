
'''
---Program 3---

Write a menu driven program to display the following pattern

   Menu
   1. Full diamond.
   2. Empty diamond
   3. Alphabet pattern.
   4. Exit

    *               *           A
   * *             * *          BB
  * * *           *   *         CCC
 * * * *         *     *        DDDD
* * * * *       *       *       EEEEE
 * * * *         *     *        FFFFFF
  * * *           *   *         GGGGGGG
   * *             * *          HHHHHHHH
    *               *

'''



while True:
    print('''      Menu
#1 - Full Diamond
#2 - Empty Diamond
#3 - Alphabet Pattern
#4 - Exit\n''')
    z = input("Enter your choice:")
    print("\n")
    if z == '1':
        a = int(input("Enter the number of rows:"))
        print("\n")
        for b in range(1,a+1):
            for c in range(a-b):
                print(' ', end='')
            for d in range(b):
                print('* ',end='')
            print()
        for e in range(1,a):
            for f in range(1,e+1):
                print(' ', end='')
            for g in range(a-e):
                print('* ',end='')
            print()
        print("\n")
    elif z == '2':
        r = int(input('Enter number of rows:'))
        print("\n")
        for i in range(1, r+1):
            for c in range(1,r-i+1):
                print(" ", end="")
            for c in range(1, 2*i):
                if c==1 or c==2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        for i in range(r-1,0, -1):
            for j in range(1,r-i+1):
                print(' ', end='')
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        print("\n")
    elif z == '3':
        a = input("Enter till which letter:")
        print("\n")
        if 'A'<=a<='Z':
          for c in range(65,ord(a)+1):
              for d in range(65,c+1):
                  print(chr(c),end=' ')
              print()
        else:
          for c in range(97,ord(a)+1):
              for d in range(97,c+1):
                  print(chr(d),end=' ')
              print()
        print("\n")
    elif z == '4':
        print("Exiting now....")
        break
