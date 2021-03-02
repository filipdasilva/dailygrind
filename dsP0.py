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

print('\nPriority Zero')

P0 = 'API that will automatatically post products from W to users FM account'

BP0 = '\nBenefit is that this will allow for many products to be posted in order to test which products will work'

#there are multiple parts to this

Part1 = 'Scrape a webpage on Walmart.com for the Product Title, Price, Description, and 1-5 pictures'

Part1b = 'The scraper needs to be able to scrape all URLs for given product category'

Part2 = 'Set guidelines for the way the data is filtered and prepared for posting'

Part3 = 'The data needs to be re-entered on Facebook'

Goal = 'Automate whatever possible to streamline this process'

print(Part1)

