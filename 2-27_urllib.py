import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
#pull files from internet

#need to decode when treating it like a file

counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print(counts)


#word counter not working
count = {}
for line in fhand:
    words = line.split('i')
    for word in words:
        count = count + 1
print(count)

for line in fhand:
    spaces = line.split()
    for word in spaces:
        count[word] = count.get(word, 0) + 1
        
print(count)