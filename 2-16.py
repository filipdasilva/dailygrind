#counting pattern
#function that counts words

#defines dictionary
many = dict()
print('Enter a line of text: ')
#input the text in below line
dis = input('')

#splits the input by spaces
words = dis.split()

#prints the splits
print('Words: ', words)

print('Counting...')

#adds word to dictionary and counts it
#dont really understand .get assuming it just retrieves quantity?
for word in words:
    #the 0 after word counts it 0 times before it is shown, making it 1 just counts an extra
    many[word] = many.get(word,0) + 1
print('Counts', many)

#print based on key value, which key value is counts (many) in this case
for key in many:
    if many[key] > 1:
        print(key, many[key])
        
#key is the word and value is the number

#pull keys values or pairs for dict
print(many.keys())
print(many.values())
      
print(many.items())

#quick loop for key-value pair list it
for aaa,bbb in many.items():
    print(aaa,bbb)
    
    
#counting the number of words in a file

try:
    filename = input('Enter file: ')

except:
    print('Incorrect File name try again')
    
handle = open(filename)

paragraph = dict()
for line in handle:
    words = line.split()
    for word in words:
        paragraph[word] = paragraph.get(word, 0) + 1
        
bigcount = None
bigword = None
for word,count in paragraph.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    
print(bigword, bigcount)

for word in paragraph:
    if paragraph[word] > 7:
        print(word, paragraph[word])



