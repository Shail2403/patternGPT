#1
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

""" for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print() """
    
    
#2
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

""" for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print() """
    

#3
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

""" for i in range(5):
    for j in range(i+1):
        print(i+1,end=" ")
    print() """    
    

#4
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

""" for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print() """
    
    
#5
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

""" for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print() """
    

#6
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

""" for i in range(5):
    for j in range(5-i):
        print(j+1,end=" ")
    print() """


#7
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

""" for i in range(1, 6):
    print(' ' * (5 - i) + '* ' * i)
 """
 

#8
'''
    *
   ***
  *****
 *******
*********
'''

""" n=5
for i in range(1,n+1):
    print(' '*(n-i)+"*"*(i)+"*"*(i-1))         #  [2*i-1] """
    
    
#9
'''
*******
 *****
  ***
   *
'''

""" n=5
for i in range(1,n+1):
    print(' '*(i-1)+"*"*(n-i)+"*"*(n-i-1)) """  

"""    
#n = 5
for i in range(n):
    print(" " * i + "*" * (2 * (n - i - 1)))
"""


#10
'''
    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    *    
'''

""" n=9
for i in range(1,n+1):
    i=i-(n//2+1)
    if i<0:
        i=-i
    line= " "*i+"*"*(n-i*2)+" "*i
    print(line)
    if i==0:
        print(line) """
        
    
#11
'''
* 
** 
*** 
**** 
***** 
**** 
*** 
** 
* 
'''

""" n=9
for i in range(1,n+1):
    if i<=n//2+1:
        print("*"*i,end=" ")
    
    else:
        print("*"*(n-i+1),end=" ")
    print() """
    
    
#12
'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
'''

""" one=None

for i in range(1,6):
    if i%2==0:
        one=False
        for j in range(i):
            if one==True:
                print("1",end=" ")
                one=False
            else:
                print("0",end=" ")
                one=True
        print()
    else:
        one=True
        for j in range(i):
            if one==True:
                print("1",end=" ")
                one=False
            else:
                print("0",end=" ")
                one=True
        print() """
        
        
""" n = 5

for row in range(1, n + 1):
    current_value = 1 if row % 2 != 0 else 0

    for col in range(row):
        print(current_value, end=" ")
        current_value = 1 - current_value
    print() """
    

#13
'''
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 
'''

""" for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print("  "*(2*(4-i)), end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print() """
    
    
#14
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''

""" k=1
for i in range(1,6):
    for j in range(i):
        print(k,end=" ")
        k=k+1
    print() """
    
""" n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    start = i*(i-1)//2 + 1
    print(*range(start, start+i)) """
    
    
#15
'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''

""" letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k=0
for i in range(1,6):
    for j in range(1,i+1):
        print(letters[k],end=" ") 
        k=k+1       
    print() """
    

""" import string

letters = string.ascii_uppercase
k = 0

for i in range(1, 6):
    print(" ".join(letters[k:k+i]))
    k += i """
    

#16
'''
A
A B
A B C
A B C D
A B C D E
'''
    
""" import string 
letters = string.ascii_uppercase

for i in range(1,6):
    print(" ".join(letters[0:i])) """
    

#17
'''
A B C D E
A B C D
A B C
A B
A
'''

""" import string
letters= string.ascii_uppercase
#print(string.ascii_letters)

for i in range(1,6):
    print(" ".join(letters[0:6-i])) """
    

#18
'''
A
BB
CCC
DDDD
EEEEE
'''

""" for i in range(5):
    letter = chr(65 + i)
    print(letter * (i + 1)) """
    

#19
'''
        A 
       A B A
     A B C B A
   A B C D C B A
 A B C D E D C B A
'''
    
""" import string
letters = string.ascii_uppercase

for i in range(5):
    print(" "*2*(5-i-1),end=" ")
    print(" ".join(letters[0:i+1]),end=" ")
    print(" ".join(letters[:i][::-1])) """
    
'''alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for line in range(5):
    letters_needed = alphabet[:line + 1] 
    forward_part = list(letters_needed)
    print(*forward_part)'''

    
#20
'''
E
D E
C D E
B C D E
A B C D E
'''
""" import string
letters=string.ascii_uppercase
for i in range(1,6):
    print(" ".join(letters[6-i-1:5])) """
    

#21
'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

""" n=10  
for i in range(1,n+1):
    if i<=n//2:
        print("*"*((n//2)-i+1),end="")
        print(" "*2*(i-1),end="")
        print("*"*((n//2)-i+1))
    else:
        print("*"*(i-n//2),end="")
        print(" "*2*(n-i),end="")
        print("*"*(i-n//2)) """
        
''''n = 10

for i in range(1, n+1):
    # Find the "mirror index" for symmetry
    k = i if i > n//2 else n//2 - i + 1
    
    # Stars on both sides
    stars = "*" * k
    # Spaces in the middle
    spaces = " " * (2 * (n//2 - k))
    
    print(stars + spaces + stars)'''
    

#22
'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

""" n=10
for i in range(0,n):
    if i<n//2:
        print("*"*(i+1),end="")
        print(" "*2*(n//2-i-1),end="")
        print("*"*(i+1))
    if i>n//2:
        print("*"*(n-i),end="")
        print(" "*2*(i-n//2),end="")
        print("*"*(n-i)) """
        

#23
'''
****
*  *
*  *
****
'''

""" n=4
for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*") """
        

#24-concentric square number pattern
'''
4444444
4333334
4322234
4321234
4322234
4333334
4444444
'''

""" n=7      #here n is n*n square

grid = [[0 for _ in range(n)] for _ in range(n)]
max_layer_no=(n+1)//2

for i in range(n):
    for j in range(n):
        distance_from_edge=min(i,j,n-1-i,n-1-j)
        grid[i][j]=max_layer_no-distance_from_edge
        
for row in grid:
    for num in row:
        print(f"{num}",end="")
    print() """
    

""" n=4         #here n is max outsquare number

grid_size=2*n-1
grid = grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

for i in range(grid_size):
    for j in range(grid_size):
        distance_from_edge=min(i,j,grid_size-1-i,grid_size-1-j)
        grid[i][j]=n-distance_from_edge
        
for row in grid:
    for num in row:
        print(f"{num}",end="")
    print() """
    
   
#24-concentric square number pattern where n at center ie inner to outer 
'''
1111111
1222221
1233321
1234321
1233321
1222221
1111111
'''

""" n=4
grid_size=2*n-1
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

for i in range(grid_size):
    for j in range(grid_size):
        distance_from_edge=min(i,j,grid_size-1-i,grid_size-1-j)
        grid[i][j]=distance_from_edge+1
        
for row in grid:
    for num in row:
        print(f"{num}",end="")
    print() """
    

#25-border diamond
'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''

""" n=9
half=n//2
for i in range(1,half+2):
    if i==1:
        spaces=" "*half
        print(spaces+"*")
    else:
        spaces=" "*(half+1-i)
        middle_spaces=" "*(2*(i-1)-1)
        print(spaces+"*"+middle_spaces+"*")
for i in range(half,0,-1):
    if i==1:
        spaces=" "*half
        print(spaces+"*")
    else:
        spaces=" "*(half+1-i)
        middle_spaces=" "*(2*(i-1)-1)
        print(spaces+"*"+middle_spaces+"*") """      


#25
'''
P
Py
Pyt
Pyth
Pytho
Python
'''

""" word = "Python"
x = ""
for i in word:
    x += i
    print(x) """


#26
'''
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
'''

""" rows = 5
last_num = 2 * rows
even_num = last_num
for i in range(1, rows + 1):
    even_num = last_num
    for j in range(i):
        print(even_num, end=' ')
        even_num -= 2
    print("\r") """
    

#27
'''
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
'''

""" for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print() """


#28
'''
0 
0 1 
0 2 4 
0 3 6 9 
0 4 8 12 16 
0 5 10 15 20 25 
0 6 12 18 24 30 36 
'''

""" n=7
for i in range(0,n):
    for j in range(0,i+1):
        print(i*j,end=" ")
    print() """
    

#29
'''
0 
2 4 
4 8 8 
8 16 16 16
'''

""" n=4
counter=0
for i in range(0,n):
    for j in range(0,i+1):
        print(counter,end=" ")
        counter=2**(i+1)
    print() """
    
    
#30-pascal's triangle
'''
   1 
   1    2    1 
   1    2    4    2    1 
   1    2    4    8    4    2    1 
   1    2    4    8   16    8    4    2    1 
   1    2    4    8   16   32   16    8    4    2    1 
   1    2    4    8   16   32   64   32   16    8    4    2    1 
   1    2    4    8   16   32   64  128   64   32   16    8    4    2    1 
'''

""" n=9
for i in range(1,n):
    ascending=[2**j for j in range(i)]
    descending=ascending[:-1][::-1]
    row=ascending+descending
    print("   " + "".join(f"{num:4}" for num in row))     #* (n - i)
print() """


#31
'''
   1 
   2    1 
   4    2    1 
   8    4    2    1 
  16    8    4    2    1 
  32   16    8    4    2    1 
  64   32   16    8    4    2    1 
 128   64   32   16    8    4    2    1 
'''

""" n=9
for i in range(0,9):
    number=2**(i-1)
    for j in range(i):
        print(int(number),end=" ")
        number=number/2
    print() """          


#32
'''
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
'''

""" rows=10
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print() """
 

#33
'''
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
'''  

""" n=5
for i in range(1,6):
    for j in range(1,6):
        print(max(i,j),end=" ")
    print() """
    

#34-reverse numbers
'''
1
3 2
6 5 4
10 9 8 7
'''

""" n=10
k=1
for i in range(1,n+1):
    r=range(k,k+i)[::-1]
    print(*r)
    k+=i """
    

#35
'''
*
***
*****
*******
*********
'''

""" n=5 
for i in range(1,n+1):
    print("*"*(2*i-1))"""
    
    
#36
'''
1	0	0	0
0	1	0	0
0	0	1	0
0	0	0	1
'''

""" n=4
for i in range(0,n):
    for j in range(n):
        if i==j:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print() """
    

#37
'''
                  1
                232
              34543
            4567654
          567898765
        67890109876
      7890123210987
    890123454321098
  90123456765432109
0123456789876543210
'''

""" n = 10
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(i,2*i):
        print(j%10,end="")
    for j in range(2*i-2,i-1,-1):
        print(j%10,end="")
    print() """
    


""" #37
'''
16 15 13 10
14 12 9 6
11 8 5 3 
7 4 2 1
'''

n=4
num=n*n

for i in range(n):
    for j in range(n-i): """
    

#37
'''
1  
2 6  
3 7 10  
4 8 11 13  
5 9 12 14 1
'''

""" n = 5
for i in range(1, n+1):
    current = i 
    print(current, end=" ")
    
    gap = 4
    for j in range(i-1): 
        current = current + gap
        print(current, end=" ")
        gap = gap - 1
    print() """
    
    
#38
'''
n=3
@@@ @@@
@@@***@
@@@ @@@

n=5
@@@@@ @@@@@
@@@@@ @
@@@@@*****@
@@@@@ @
@@@@@ @@@@@
'''

"""n=5
for i in range(1,n+1):
    if i==(n+1)//2:
        print("@"*n,end="")
        print("*"*n,end="")
        print("@")
    elif i%2==0:
        print("@"*n,end=" ")
        print("@")
    else:
        print("@"*n,end=" ")
        print("@"*n)
    print()"""