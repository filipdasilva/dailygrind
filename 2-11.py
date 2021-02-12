fhand = open('210.py')
for line in fhand:
    line = line.rstrip()
#criteria to find a line in another file
    if not 'U' in line:
#continue continues next iteration of the loop before going to next line
        continue
    print(line)
    
print('Did it work')

#user input count lines in the file
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened',fname)
 #need to quit or else it will continue down file
    quit()
    
count = 0
for line in fhand:
    #if line.startswith('T'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

#algorithms - a set of rules or steps used to solve a problem
#data structures - a particular way of organizing data in a computer

#a collection allows us to put may values in a single "Variable"
#example

friends = [ 'Hey', 'whats', 'up']
for friend in friends:
    print('Happy New Year', friend)
print(friends)
print(['1',['2','6'],'3'])

print(friends[2])

print(len(friends))

print(range(len(friends)))

for i in range(len(friends)):
    friend = friends[i]
    print('Happy', friend)
    
#concatenating lists you can add lists a + b to create one big list

a = [1,4,5,6,3,45,6,42,426,426,46,460,40,20]
b = [542,42,738,86,4646,4,68]
c = a + b
print(c)

print(a[3:6])
print(a[5:])
print(c[:6])
      
#check if variable is in a list   
x = 9 in a
print(x)


#had a problem at work today, wanted to check what the OPS of certain ASINs was in 2021 that were not in 2020

g = 'Not'

list = ['ALL','ASINS','FROM','2021']
oldlist = ['FROM','2020']

for x in list:
    if x in oldlist:
        print(x)
    else:
        print(g)
    

    


