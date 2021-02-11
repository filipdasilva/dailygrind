#the \n creates a space
stuff = 'hello\nWorld'
print(stuff)

#the open() opens a file to be used - can use 'r' to read file or 'w' to write in file
fhand = open('210.py')

#count lines in file
count = 0 
for line in fhand:
    count = count +1
    
print('Line Count', count)

#pull the lines starting with a certain phrase
fhand = open('210.py')
for line in fhand:
    
#this prevents a space in between the lines printed
    line = line.rstrip()
    if line.startswith('T'):
        print(line)

#need to open file each time        
#fhand = open('210.py')

# [Harrison] You can use the seek function on a file to 'seek' the beginning of the file.
# [Harrison] 0 represents the start of the file.
fhand.seek(0)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('U'):                              #skips a line (unsure)        
        continue
    print(line)

# [Harrison] Python will do this for you after the program runs,
# [Harrison] but it's good practice to close the file.
fhand.close()

