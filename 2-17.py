#tuples are another kind of sequence that functions much like a list - elements indexed starting at 0

x = ('Due', 'Diligence', 'Good')
print(x[2])

#can tell it is tuple because it has parenthesis and not brackets

#tuples are immutable - once you create you cannot alter its contents - similar to a string

#list is changeable but string or tuple are not
x = [9,8,7]
x[2] = 6
print(x)

y = 'ABC'
try:
    y[2] = 'D'
except: 
    print(y)

z = (5,4,3)
try:
    z[2] = 0
except:
    print(z)
    
#tuple cannot .sort .append or .reverse like a list

#only count and index
t = tuple()
print(dir(t))

l = list()
print(dir(l))


#tuples are simpler and more efficient in terms of memory use and performance than lists

#can put a tuple on left hand side of assignment statement
(x,y) = (4, 'Fred')
print(y)

#the items method in dictionaries returns a list of (key,value) tuples

d = dict()
d['Jimmy'] = 4
d['Bobby'] = 6
for (a,b) in d.items():
    print(x)

tups = d.items()
print(tups)

#tups is two sets of tuples


#tuples are comparable
print((0,1,2) > (6,12,5))
print((6,5,7) > (2,8,9))

#this only compares the first number, goes left to right and the first one that is true or false that is the answer

print(('Jim', 'Bobby') > ('John', 'Jameson'))

#Z is largest and A is smallest, this compares I to O


