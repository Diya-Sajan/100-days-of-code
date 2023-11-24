import sys
def doSomething(inval):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    other_count = 0
    total_characters = len(inval)
    for char in inval:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit() :
            digit_count += 1
        else:
            other_count += 1

    uppercase_percentage = (uppercase_count/total_characters)*100
    lowercase_percentage = (lowercase_count/total_characters)*100
    digit_percentage = (digit_count/total_characters)*100
    other_percentage = (other_count/total_characters)*100

    return "{:.3f}%\n{:.3f}%\n{:.3f}%\n{:.3f}%". format (uppercase_percentage, lowercase_percentage, digit_percentage, other_percentage)


inputVal = input()
outputVal = doSomething(inputVal)
print (outputVal)

''' 
Exercise-1

Input :

Support1@litwork.in

Output :

5.263%
78.947%
5.263%
10.526%

Exercise-2

Input:

Client.1234@litwork.in

Output:

4.545%
63.636%
18.182%
13.636%
'''