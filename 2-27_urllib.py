import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
#pull files from internet

#need to decode when treating it like a file
#Word counter not working - help
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print(counts)


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://google.com')
for line in fhand:
    print(line.decode().strip())

#word counter not working
d = {}
for line in fhand:
    d[word] = d.get(word,0) + 1
    
    
word_freq = []
for key,val in d.items():
    word_freq.append((val,key))

word_freq.soty(reverse=True)
print(word_freq)
print(count)

for line in fhand:
    spaces = line.split()
    for word in spaces:
        count[word] = count.get(word, 0) + 1
        
print(count)

#program, find links in page, retrieve those links