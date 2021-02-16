#list - linear collection of values that stay in order
#dictionary - a bag of values, each with its own label

crypto = dict()
crypto['BTC'] = 'Bitcoin'
crypto['LINK'] = 'ChainLink'
crypto['MANA'] = 'Decentraland'
crypto['ETH'] = 7


print(crypto)

crypto['LINK'] = 4
crypto['ETH'] = 6

print(crypto)

crypto['ETH'] = 'Ethereum'
crypto['NOT'] = 'SIKE'

print(crypto)



#dictionaries are like lists ecept that they use keys instead of numbers to look up values

#in lists the keys are always the position

#empty dictionary b like
ooo = { }
print(ooo)
{}

#dictionaries are used for counting the frequency of things
n = 1
ccc = dict()
ccc['Flip'] = 1
ccc['Flop'] = 1
print(ccc)
while n < 10:
    ccc['Flip'] = ccc['Flip'] + 1
    print(ccc)
    n = n + 1
print(ccc)
print(ccc)
print(ccc)

print('Flop' in ccc)
#counter
hoesonme = dict()
names= ['Stephanie', 'Melanie', 'Melody','Megan', 'Leslie','Leslie','Leslie']
for name in names:
    if name not in hoesonme:
        hoesonme[name] = 1
    else:
        hoesonme[name] = hoesonme[name] + 1
print(hoesonme)

if name in hoesonme:
    x = hoesonme[name]
else:
    x = 0
    
print(hoesonme.get(name, 0))    

try:    
    print(x = hoesonme.get('Leslie', 0))

    print(x = hoesonme.get('Jenny',0))
except:
    print('Nevamind')
    
    
#use get() to provide a default value of zero when the key is not yet in the dictionary

for name in names:
    hoesonme[name] = hoesonme.get(name,0) + 1
print(hoesonme)