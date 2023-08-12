

# Hacker Rank solutions--
# Ques 1--
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    list1 = list(student_marks[query_name])
    addition = sum(list1)
    result = addition/len(list1)
    
    print('%.2f'% result)
#-----------------------------------------------------------------------------------------------

# Ques 2--

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#-----------------------------------------------------------------------------------------------

# Ques 3--


n = int(input())
arr = map(int, input().split())
l = []
for i in arr:
    l.append(i)
mx = max(l)
a = []
while mx in l:    
    l.remove(mx)
print(max(l))
#-----------------------------------------------------------------------------------------------

# Ques 5--

def swap_case(s):
    string = ''
    for i in s:
        if i.isupper() == True:
            string += (i.lower())
        else:
            string += (i.upper())
    return string            
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#-----------------------------------------------------------------------------------------------

# Ques 6--

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a+b)
print(a-b)
print(a*b)
#-----------------------------------------------------------------------------------------------

# Ques 7---

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)
#-----------------------------------------------------------------------------------------------

# Ques 8--

n = int(input().strip())
if __name__ == '__main__':
    if n%2!=0:
        print("Weird")
    elif n%2==0 and n>=2 and n<=5:
        print("Not Weird")
    elif n%2==0 and n>=6 and n<=20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")      

#-----------------------------------------------------------------------------------------------

# Ques 10--

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)

#-----------------------------------------------------------------------------------------------

# Ques 9--        

if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))


# Ques 11--

def is_leap(year):
    leap = False
    
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        leap = True
            
    return leap

year = int(input())
print(is_leap(year))

# Ques 12--

def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Ques 13--

if __name__ == '__main__':

    N = int(input())

    List=[];

    for i in range(N):

        command=input().split();

        if command[0] == "insert":

            List.insert(int(command[1]),int(command[2]))

        elif command[0] == "append":

            List.append(int(command[1]))

        elif command[0] == "pop":

            List.pop();

        elif command[0] == "print":

            print(List)

        elif command[0] == "remove":

            List.remove(int(command[1]))

        elif command[0] == "sort":

            List.sort();

        else:

            List.reverse();






                          
