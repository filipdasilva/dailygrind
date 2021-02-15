x = list()
type(x)
# dir lets me know what i can do to this variable
dir(x)

print(type(x))
print(dir(x))

#add variables to a list
x.append('Filip')
x.append('Day')
x.append(101)
print(x)

#is this in my list
print(1 in x)
print(101 in x)

y = list()
y.append(3)
y.append(1)
y.append(70)
y.append(15)

print(y)
#sorts list of int or str
y.sort()
print(y)
#this wouldn't show up in the list because we already printed y
y.append(600)
#v = 'VAda'
#print(v.lower)

print('Max:',max(y))
print('Min:',min(y))
print('Total:',sum(y))
print('Average',sum(y)/len(y))

print('When finished type "TELL ME"')
count = 1
try:
    What_it_is = list()
    while True :
    #how can i include a variable in the input? whats the *count* number
        inp = input('WHATS THA NUMBA: \n')
        if inp == 'TELL ME' : break
    #doesnt work elif inp.type == str : print('Error')
        try: 
            value = float(inp)
            What_it_is.append(value)
            count = count + 1
        except:
            print('AINT NO NUMBA MF')
    average = sum(What_it_is) /         len(What_it_is)

    print('Average:', average)
except:
    print('OK DEN')
abc = 'Three different ASINS'
#split em up in a list)
new = abc.split()
print(new)

for nuts in new :
    print(nuts)
#when you do not specify a delimiter, multiple spaces are treated like one delimiter, you can specify what delimiter character to use in the splitting    
test = abc.split('e')
print(test)

#this should work with open file
fhand = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#fhand = open('textfile')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
    
line = fhand
chew = line.split()
email = chew[1]
pieces = email.split('@')
print(pieces[1])



    
