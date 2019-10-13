

# ===== PROBLEM1 =====

# Exercise 1 - Introduction - Say "Hello, World!" With Python

print("Hello, World!")

# Exercise 2 - Introduction - Python If-Else

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else:
        if 2 <= n < 5 or n > 20:
            print("Not Weird")
        else:
            print("Weird")

# Exercise 3 - Introduction - Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Exercise 4 - Introduction - Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Exercise 5 - Introduction - Loops

if __name__ == '__main__':
    n = int(input())
    i = 0
    while i < n:
        print(i**2)
        i+=1

# Exercise 6 - Introduction - Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4 == 0):
        leap = True;
        if(year%100 == 0):
            leap = False
            if(year%400 == 0):
                leap = True
    
    return leap

# Exercise 7 - Introduction - Print Function

if __name__ == '__main__':
    n = int(input())
    i = 1
    while(i <= n):
        print(i, end = '')
        i+=1

# Exercise 8 - Basic data types - List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k != n)])

# Exercise 9 - Basic data types - Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    l = []
    for elem in arr:
        l.append(elem)

    massimo = max(l)
    res = -100;
    for i in range(len(l)):
        if l[i] > res and l[i] != massimo:
            res = l[i]

    print(res)

# Exercise 10 - Basic data types - Nested Lists

if __name__ == '__main__':
    l = []
    minimo = 100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        if score < minimo: 
            minimo = score
    res = []
    mini = 100
    for elem in l:
        if elem[1] != minimo:
            if elem[1] == mini:
                res.append(elem[0])
            elif elem[1] < mini:
                res = [elem[0]]
                mini = elem[1]
    res.sort()
    for elem in res:
        print(elem)

# Exercise 11 - Basic data types - Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print("%0.2f" % ((student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2])/3))

# Exercise 12 - Basic data types - Lists

if __name__ == '__main__':
    N = int(input())
    l = []

    for i in range(N):
        name, *line = input().split()
        values = list(map(int, line))
        if name == 'insert' :
            l.insert(values[0], values[1])
        elif name == 'print':
            print(l)
        elif name == 'remove':
            l.remove(values[0])
        elif name == 'append':
            l.append(values[0])
        elif name == 'sort':
            l.sort()
        elif name == 'pop':
            l.pop()
        elif name == 'reverse':
            l.reverse()

# Exercise 13 - Basic data types - Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    l = []
    for elem in integer_list:
        l.append(elem)
    t = tuple(l)

    print(hash(t))

# Exercise 14 - Strings - sWAP cASE

def swap_case(s):
    res=''
    for c in s:
        if c.isupper():
            res += c.lower()
        else:
            res += c.upper()
    return res

# Exercise 15 - Strings - String Split and Join

def split_and_join(line):
    line = line.split()
    line = "-".join(line)
    return line

# Exercise 16 - Strings - What's Your Name?

def print_full_name(a, b):
    print("Hello "+a+" "+b+"! You just delved into python.")

# Exercise 17 - Strings - Mutations

def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string

# Exercise 18 - Strings - Find a string

def count_substring(string, sub_string):
    cont = 0
    for i in range(0,len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string :
            cont += 1
    return cont

# Exercise 19 - Strings - String Validators

if __name__ == '__main__':
    s = input()
    alphanum = False
    alphabet = False
    isdig = False
    islow = False
    isupp = False

    for c in s:
        if c.isalnum():
            alphanum = True
        if c.isalpha():
            alphabet = True
        if c.isdigit():
            isdig = True
        if c.islower():
            islow = True
        if c.isupper():
            isupp = True
        
        if (alphanum and alphabet and isdig and islow and isupp):
            break
    
    print(alphanum)
    print(alphabet)
    print(isdig)
    print(islow)
    print(isupp)

# Exercise 20 - Strings - Text Alignment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Exercise 21 - Strings - Text Wrap

def wrap(string, max_width):
    l = textwrap.wrap(string, max_width)
    s = "\n".join(l)
    return s

# Exercise 22 - Strings - Designer Door Mat

l = input().split()
n = int(l[0])
m = int(l[1])
for i in range(n):
    if i > n/2:
        i = n-i-1
    for j in range(m):
        if(i == n//2):
            if(j < m//2 - 3 or j > m//2 + 3):
                print('-', end = '')
            elif (j == m//2 - 3):
                print("WELCOME", end = '')
        elif( j < m/2 - 3*i - 2) or (j > m/2 + 3*i + 1 ):
            print('-', end = '')
        elif((j-1) % 3 == 0):
            print('|', end = '')
        else:
            print('.', end = '')
    print()

# Exercise 23 - Strings - String Formatting

def print_formatted(number):
    for i in range (1, number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = len("{0:b}".format(number))))

# Exercise 24 - Strings - Alphabet Rangoli

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    used_chars = alphabet[:size]

    for i in range(size):
        s = used_chars[::-1][:i+1] + used_chars[size-i:][:i]
        print(('-'.join(s)).center(4*size-3, '-'))

    for i in range(1, size):
        i = size - i - 1
        s = used_chars[::-1][:i+1] + used_chars[size-i:][:i]
        print(('-'.join(s)).center(4*size-3, '-'))

# Exercise 25 - Strings - Capitalize!

import string
def solve(s):
    s = str(s)
    ret = string.capwords(s, " ")
    return ret

# Exercise 26 - Strings - The Minion Game

import string

def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if(string[i] in vowels):
            kevin += len(string) - i
        else:
            stuart += len(string)-i
    
    if(kevin > stuart):
        print("Kevin {}".format(kevin))
    elif(stuart > kevin):
        print("Stuart {}".format(stuart))
    else:
        print("Draw")

# Exercise 27 - Strings - Merge the Tools!

def merge_the_tools(string, k):
    l = []
    for i in range(len(string)//k):
        l.append(string[k*i:i*k+k])
    for elem in l:
        res = ""
        for i in range(len(elem)):
            if(elem[i] not in res):
                res += elem[i]
        print(res)

# Exercise 28 - Sets - Introduction to Sets

def average(array):
    s = set(array)
    return sum(s)/len(s)

# Exercise 29 - Sets - No Idea!

n, m = map(int,input().split())
i = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happyness = 0
for elem in i:
    if elem in a:
        happyness += 1
    elif elem in b:
        happyness -= 1
print(happyness)

# Exercise 30 - Sets - Symmetric Difference

n = int(input())
nset = set(map(int,input().split()))
m = int(input())
mset = set(map(int,input().split()))

sd = list(nset.symmetric_difference(mset))
sd.sort()

for elem in sd:
    print(elem)

# Exercise 31 - Sets - Set .add()

n = int(input())
s = set()
for i in range(n):
    s.add(input())
print(len(s))

# Exercise 32 - Sets - Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
ncom = int(input())
for i in range(ncom):
    line = input().split()
    com = line[0]
    if(com == "pop"):
        s.pop()
    elif(com == "remove"):
        s.remove(int(line[1]))
    elif(com == "discard"):
        s.discard(int(line[1]))
print(sum(s))

# Exercise 33 - Sets - Set .union() Operation

n = int(input())
nstud = set(map(int,input().split()))
m = int(input())
mstud = set(map(int,input().split()))
subs = nstud.union(mstud)
print(len(subs))

# Exercise 34 - Sets - Set .intersection() Operation

n = int(input())
nstud = set(map(int,input().split()))
m = int(input())
mstud = set(map(int,input().split()))
subs = nstud.intersection(mstud)
print(len(subs))

# Exercise 35 - Sets - Set .difference() Operation

n = int(input())
nstud = set(map(int,input().split()))
m = int(input())
mstud = set(map(int,input().split()))
subs = nstud.difference(mstud)
print(len(subs))

# Exercise 36 - Sets - Set .symmetric_difference() Operation

n = int(input())
nstud = set(map(int,input().split()))
m = int(input())
mstud = set(map(int,input().split()))
subs = nstud.symmetric_difference(mstud)
print(len(subs))

# Exercise 37 - Sets - Set Mutations

na = int(input())
a = set(map(int,input().split()))
n = int(input())
for i in range(n):
    com, x= input().split()
    nset = set(map(int,input().split()))
    getattr(a, com)(nset)
print(sum(a))

# Exercise 38 - Sets - The Captain's Room

k = int(input())
a = list(map(int,input().split()))
rooms = set(a)

cap = (sum(rooms)*k - sum(a))//(k-1)  
print(cap)

# Exercise 39 - Sets - Check Subset

ntest = int(input())
for i in range(ntest):
    na, a = int(input()), set(map(int, input().split()))
    nb, b = int(input()), set(map(int, input().split()))
    inter = a.intersection(b)
    if(inter == a):
        print(True)
    else:
        print(False)

# Exercise 40 - Sets - Check Strict Superset

a = set(map(int, input().split()))
n = int(input())
cont = 0
for i in range(n):
    nset = set(map(int, input().split()))
    diff = nset.difference(a)
    if(len(diff) == 0 and nset != a):
        cont += 1
if cont == n:
    print(True)
else:
    print(False)

# Exercise 41 - Collections - collections.Counter()

from collections import Counter
x = int(input())
l = list(map(int, input().split()))
shoes_cont = Counter(l)
earn = 0
ncust = int(input())
for i in range(ncust):
    size, price = map(int, input().split())
    if size in shoes_cont:
        if shoes_cont[size] > 0:
            earn += price
            shoes_cont[size] -= 1
print(earn)

# Exercise 42 - Collections - DefaultDict Tutorial

from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)
for i in range(n):
    word = input()
    a[word].append(i+1)
for i in range(m):
    word = input()
    if word not in a:
        print(-1)
    else:
        print(*a[word])

# Exercise 43 - Collections - Collections.namedtuple()

from collections import namedtuple
N = int(input())
Stud = namedtuple("Student", ','.join(input().split()))
marks = 0
for i in range(N):
    s = Stud(*input().split())
    marks += int(s.MARKS)
print("%0.2f" % (marks/N))

# Exercise 44 - Collections - Collections.OrderedDict()

from collections import OrderedDict
N = int(input())
sold = OrderedDict()
for i in range(N):
    l = input().split()
    name = ' '.join(l[:-1])
    net_price = int(l[-1])
    if name not in sold:
        sold[name] = net_price
    else:
        sold[name] += net_price
for elem in sold:
    print(elem + " {}".format(sold[elem]))

# Exercise 45 - Collections - Word Order

from collections import OrderedDict
n = int(input())
words = OrderedDict()
for i in range(n):
    w = input()
    if w not in words:
        words[w] = 1
    else:
        words[w] += 1
print(len(words))
for elem in words:
    print(words[elem] , end = '')
    print(' ', end = '')

# Exercise 46 - Collections - Collections.deque()

from collections import deque

N = int(input())
d = deque()
for i in range(N):
    l = input().split()
    com = []
    arg = []
    if(len(l)>1):
        com.append(l[0])
        arg.append(l[-1])
    else:
        com.append(l[0])
    getattr(d, *com)(*arg)
print(*d)

# Exercise 47 - Collections - Company Logo

import math
import os
import random
import re
import sys
from collections import OrderedDict, Counter


if __name__ == '__main__':
    s = sorted(input())
    d = OrderedDict()
    for elem in s:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1
    c = Counter(d).most_common(3)
    for elem in c:
        print(*elem)

# Exercise 48 - Collections - Piling Up!

from collections import deque
T = int(input())
for i in range(T):
    n = int(input())
    hor = deque(map(int, input().split()))
    ver = []
    if (hor[0] >= hor[-1]):
        ver.append(hor[0])
        hor.popleft()
    else:
        ver.append(hor[-1])
        hor.pop()
    flag = True
    v = False
    while(flag):
        if(hor[0] > ver[-1] and hor[-1] >  ver[-1]):
            flag = False
        else:
            if hor[0] >= hor[-1]:
                if(hor[0] <= ver[-1]):
                    ver.append(hor[0])
                    hor.popleft()
                else:
                    ver.append(hor[-1])
                    hor.pop()
            else:
                if(hor[-1] <= ver[-1]):
                    ver.append(hor[-1])
                    hor.pop()
                else:
                    ver.append(hor[0])
                    hor.popleft()
        if(len(ver) == n):
            flag = False
            v = True
    if v:
        print("Yes")
    else:
        print("No")

# Exercise 49 - Date time - Calendar Module

import datetime

l = list(map(int, input().split()))
date = datetime.datetime(l[2],l[0],l[1])
print(date.strftime("%A").upper())

# Exercise 50 - Date time - Time Delta

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    diff = abs(t1-t2)
    return str(int(diff.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Exercise 51 - Exceptions -

T = int(input())
for i in range(T):
    a ,b = map(str, input().split())
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e1:
        print("Error Code:",e1)
    except ValueError as e2:
        print("Error Code:",e2)

# Exercise 52 - Built-ins - Zipped!

N, X = map(int,input().split())
stud = []
for i in range(X):
    grades = list(map(float, input().split()))
    stud.append(grades)
alls = zip(*stud)
for elem in alls:
    print(sum(elem)/len(elem))

# Exercise 53 - Built-ins - Athlete Sort

import math
import os
import random
import re
import sys

from collections import OrderedDict

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    d = OrderedDict()

    for i in range(n):
        d[i] = list(map(int, input().rstrip().split()))

    k = int(input())
    l = sorted(d.values(), key = lambda item : item[k])
    for elem in l:
        print(*elem)

# Exercise 54 - Built-ins - Ginorts

s = input()
lower = []
upper = []
odd = []
even = []
for c in s:
    if c.islower():
        lower.append(c)
    elif c.isupper():
        upper.append(c)
    elif c.isdecimal():
        if(int(c)%2 == 0):
            even.append(c)
        else:
            odd.append(c)
lower.sort()
upper.sort()
odd.sort()
even.sort()
print(''.join(lower)+''.join(upper)+''.join(odd)+''.join(even))

# Exercise 55 - Map and lambda function

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            x = fib[i-1] + fib[i-2]
            fib.append(x)
    return fib

# Exercise 56 - Regex - Detect Floating Point Number

import re
T = int(input())
for i in range(T):
    n = input()
    print(bool(re.match('^[+-]?[0-9]*\.[0-9]+$', n)))

# Exercise 57 - Regex - Re.split()

regex_pattern = r"\,|\."	# Do not delete 'r'.

# Exercise 58 - Regex - Group(), Groups() & Groupdict()

import re
m = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(m.group(1) if m else -1)

# Exercise 59 - Regex - Re.findall() & Re.finditer()

import re
l = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', input())
if len(l) == 0:
    print(-1)
else:
    for elem in l:
        print(elem)

# Exercise 60 - Regex - Re.start() & Re.end()

import re
S = input()
k = input()
m = re.finditer('(?='+k+')', S)
if not re.search('(?='+k+')', S): # search for 0 matches, returns none
    print((-1, -1))
for elem in m:
    s, e = elem.span()   #span return start end
    print((s, e + len(k)-1))

# Exercise 61 - Regex - Regex Substitution

import re
N = int(input())
for i in range(N):
    line = input()
    line = re.sub('(?<= )([&]{2})( )', 'and ', line)
    line = re.sub('(?<= )([|]{2})( )', 'or ', line)
    print(line)

# Exercise 62 - Regex - Validating Roman Numerals

regex_pattern = r"^(M{0,3})(D?C{0,3}|C[MD])(L?X{0,3}|X[LC])(V?I{0,3}|I[XV])$"	#aggiunto ^ e $ per inizio e fine stringa se no la match fallisce

# Exercise 63 - Regex - Validating phone numbers

import re
N = int(input())
for i in range(N):
    number = input()
    if bool(re.match(r'^[789]{1}[0-9]{9}$', number)):
        print("YES")
    else:
        print("NO")

# Exercise 64 - Regex - Validating and Parsing Email Addresses

import re
import email.utils

n = int(input())
for i in range(n):
    name, e = input().split()
    if bool(re.match('^<([A-Za-z]{1}[0-9a-zA-Z\.\-\_]*)@([a-zA-Z]+)\.([a-zA-Z]{1,3})>$', e)):
        print(email.utils.formataddr(email.utils.parseaddr(name+e)))

# Exercise 65 - Regex - Hex Color Code

import re
N = int(input())
for i in range(N):
    line = input()
    # color on {} line in one test
    if(len(line.split()) > 1 and '{' not in line and '}' not in line):
        colors = re.findall('(#[a-fA-F0-9]{3,6})', line)
        for elem in colors:
            print(elem)

# Exercise 66 - Regex - HTML Parser - Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))

N = int(input())
parser = MyHTMLParser()
for i in range(N):
    line = input()
    parser.feed(line)

# Exercise 67 - Regex - HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        l = str(data).split('\n')
        if(len(l) == 1):
            print('>>> Single-line Comment')
            print(l[0])
        elif(len(l) > 1):
            print('>>> Multi-line Comment')
            for elem in l:
                print(elem)
    def handle_data(self, data):
        if(len(data)>1):
            print (">>> Data")
            print(str(data))
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values

# same as previous ex
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))

N = int(input())
parser = MyHTMLParser()  #fuori dal for se no prende tutto ###
html = ""
for i in range(N):
    html += input()
parser.feed(html)

# Exercise 69 - Regex - Validating UID

import re
T = int(input())
for i in range(T):
    # sort input to match sep
    uid = ''.join(sorted(input()))
    # all rules individually
    valid_upper = bool(re.match(r'.*([A-Z]{2,}).*', uid))
    valid_digits = bool(re.match(r'.*([0-9]{3,}).*', uid))
    # look on google for no repetition
    # need another match for repetition (not for no rep)
    valid_rep = not bool(re.match(r'.*(.).*\1', uid))
    valid_all = bool(re.match(r'^[0-9a-zA-Z]{10}$', uid))
    if valid_upper and valid_digits and valid_rep and valid_all:
        print('Valid')
    else:
        print('Invalid')

# Exercise 70 - Regex - Validating Credit Card Numbers

import re
N = int(input())

for i in range(N):
    s = input()
    # match rules sep
    valid_all = bool(re.match('^([456][0-9]{3}[0-9]{4}[0-9]{4}[0-9]{4})|([456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4})$', s))
    a = ''.join(s.split('-'))
    valid_rep = not re.search(r'(.)(-?\1){3}', a)
    if(valid_rep and valid_all):
        print('Valid')
    else:
        print('Invalid')

# Exercise 71 - Regex - Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"([0-9])(?=[0-9]\1)"	  # \1 look back on group 1

# Exercise 72 - Regex - Matrix Script

import math
import os
import random
import re
import sys
import re



first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
mat_t = [""]*m                 # create transopsed matrix

for _ in range(n):
    matrix_item = input()
    for i in range(m):
        mat_t[i] += matrix_item[i]

script = ''.join(mat_t)        # script to decode

decoded = re.sub('(?<=[a-zA-Z0-9])([ !@#$%&]+)(?=[a-zA-Z0-9])', ' ', script)
print(decoded)

# Exercise 73 - Xml - XML 1 - Find the Score

def get_attr_number(node):
    i = node.iter()
    res = 0
    for elem in i:
        res += len(elem.attrib)
    return res

# Exercise 74 - Xml - XML 2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if(level + 1 > maxdepth):    # +1 cause we start at -1
        maxdepth  = level + 1
    for child in elem:
        depth(child, level+1)

# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            l[i] = '+91 '+ l[i][-10:-5] + ' ' + l[i][-5:]
        return f(l)     # it works but i'm not sure why
    return fun

# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key = lambda x: int(x[2])))
        # apply f to each elem of the sorted list
        # int(x[2]) added int to make it work with ages > 100 (seen in discussion)

    return inner

# Exercise 77 - Numpy - Arrays

numpy.set_printoptions(legacy='1.13') 

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr, float)
    a = numpy.flip(a)
    return a

# Exercise 78 - Numpy - Shape and Reshape

import numpy

l = list(map(int, input().split()))
arr = numpy.array(l)
arr.shape = (3, 3)
print(arr)

# Exercise 79 - Numpy - Transpose and Flatten

import numpy

n, m = map(int, input().split())

l = []
for i in range(n):
    l.append(list(map(int, input().split())))
arr = numpy.array(l)
print(numpy.transpose(arr))
print(arr.flatten())

# Exercise 80 - Numpy - Concatenate

import numpy

n, m, p = map(int, input().split())

l1 = []
for i in range(n):
    l1.append(list(map(int, input().split())))
l2 = []
for i in range(m):
    l2.append(list(map(int,input().split())))

arr1 = numpy.array(l1)
arr2 = numpy.array(l2)

print(numpy.concatenate((arr1, arr2)))

# Exercise 81 - Numpy - Zeros and Ones

import numpy

i = tuple(map(int, input().split()))

print(numpy.zeros(i, dtype = numpy.int))
print(numpy.ones(i, dtype = numpy.int))

# Exercise 82 - Numpy - Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m, k = 0))

# Exercise 83 - Numpy - Array Mathematics

import numpy

n, m = map(int, input().split())

arr1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr2 = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)

# Exercise 84 - Numpy - Floor, Ceil and Rint

import numpy
numpy.set_printoptions(legacy='1.13')

arr = numpy.array(list(map(float, input().split())))
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

# Exercise 85 - Numpy - Sum and Prod

import numpy

n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.prod(numpy.sum(arr, axis = 0)))

# Exercise 86 - Numpy - Min and Max

import numpy

n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.max(numpy.min(arr, axis = 1)))

# Exercise 87 - Numpy - Mean, Var, and Std

import numpy

numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr))

# Exercise 88 - Numpy - Dot and Cross

import numpy

n = int(input())

mat1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
mat2 = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.dot(mat1, mat2))

# Exercise 89 - Numpy - Inner and Outer

import numpy

arr1 = numpy.array(list(map(int, input().split())))
arr2 = numpy.array(list(map(int, input().split())))

print(numpy.inner(arr1, arr2))
print(numpy.outer(arr1, arr2))

# Exercise 90 - Numpy - Polynomials

import numpy

coeff = numpy.array(list(map(float, input().split())))
x = float(input())

print(numpy.polyval(coeff, x))

# Exercise 91 - Numpy - Linear Algebra

import numpy

numpy.set_printoptions(legacy='1.13')   #pd

n = int(input())

mat = numpy.array([input().split() for _ in range(n)], float)

print(numpy.linalg.det(mat))

​

# ===== PROBLEM2 =====

​

# Exercise 92 - Challenges - Birthday Cake Candles

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    return(ar.count(max(ar)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()

# Exercise 93 - Challenges - Kangaroo

import math
import os
import random
import re
import sys
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    flag = False
    i = 1
    while(i < 10000):
        if x1 == x2:
            flag = True
            break
        x1 += v1
        x2 += v2
        i += 1
    if flag:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Exercise 94 - Challenges - Viral Advertising

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    like = 0
    share = 5
    for i in range(n):
        like += share//2
        share = (share//2)*3
    return like
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Exercise 95 - Challenges - Recursive Digit Sum

import math
import os
import random
import re
import sys

def superDigit(n, k):
    if len(n) == 1:
        return n
    l = list(map(int, n))
    return superDigit(str(sum(l)*k), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Exercise 96 - Challenges - Insertion Sort - Part 1

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    k = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > k:
            arr[i+1] = arr[i]
            print(*arr)
            if(i == 0):
                arr[i] = k
                break
        else:
            arr[i+1] = k
            break
    print(*arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Exercise 97 - Challenges - Insertion Sort - Part 2

import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    k = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > k:
            arr[i+1] = arr[i]
            if(i == 0):
                arr[i] = k
                break
        else:
            arr[i+1] = k
            break
    return arr

def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        a = insertionSort1(i+1, arr[:i+1])
        for k in range(len(a)):
            arr[k] = a[k]
        print(*arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

