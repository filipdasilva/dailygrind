#import ds

P0 = 'P0'

dataLog = []
with open('ds.py', 'r') as ds:
    data = ds.readlines()
for line in data:
    if line.__contains__('P0'):
        print(line)
        dataLog.append(line)
print(dataLog)

#how do I pull these lines so that they are executed in this file, I don't want the code I want the code to execute