#sorting lists of tuples using items() and sorted() functions

import re

#import re.search() or re.findall()

d = {'a':12, 'b':22, 'c':35}
d.items()

x = sorted(d.items())

print(x)

#(value,key)
for deez,nuts in x:
    print(deez,nuts)
    
tmp = list()
for deez,nuts in x:
    tmp.append( (deez,nuts) )

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

#how to use get literally pulls from tuple
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

#top 10 most common words in the file

#dictionary for counting
fhand = open('balancesheet.txt')
thecount = dict()

#split up each line
for line in fhand:
    spaces = line.split()
#idiom to count words
    for word in spaces:
        thecount[word] = thecount.get(word, 0) + 1

#now sort our key, values        
        
lst = list()
for key, val in thecount.items():
    newtup = (val, key)
    lst.append(newtup)
    
#now we have list of tuples in VK order

lst = sorted(lst, reverse=True)

#go through first 10 of list
for val, key in lst[:10] :
    print(key, val)
              

#lambdas where it all happens in one line

#create an expression that acts as a generator of all the elements

print( sorted( [ (v,k) for k,v in d.items() ] ) )

#stamp stamp stamp and producing list, list manufactured in the moment, sorted moves the list around and gives the sorted list, now sorted by key

#Regular Expressions

ghand = open('balancesheet.txt')
for line in ghand:
    line = line.rstrip()
#if doesnt find will return -1
    if line.find('financial') >=0:
        print(line)
print('NEXT UP')
#how to incorporate regex? ex \s or ^ or *
hand = open('balancesheet.txt')
for dweeb in hand:
    dweeb = dweeb.rstrip()
    if re.search('calculate', dweeb) :
        print(dweeb)
        
print('OK NOW WE GETTIN IT')


ghand = open('balancesheet.txt')
for line in ghand:
    line = line.rstrip()
    if line.startswith('The') >=0:
        print(line)
print('YOU SEE IT')
#the current is like saying at the beginning of line
hand = open('balancesheet.txt')
for dweeb in hand:
    dweeb = dweeb.rstrip()
    if re.search('^The.*', dweeb) :
        print(dweeb)

#regex expressions are to look for something 
#^ - to match start of a line
#. - to match any character
#* - many times

#^X.*: then include -\S only if any non-whitespace character
#for X-Sieve: CMU Sieve 2.3

#use regex to pull data from strings