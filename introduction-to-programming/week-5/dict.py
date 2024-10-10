"""
Dictionaries
"""

# You can make a dict like this:
NiceDict = {
    'Vince' : 17,
    'Kelvin' : 18,
    'Frem' : 20
}

# Or like this:
NewDict = dict([('Coding', 6), ('Is', 2), ('Cool', 4)])

# Lemme print it.
print(NiceDict, NewDict)

# I print specific value
print(NiceDict['Frem'])

# We can add new key-value pairs to an existing dict
NiceDict['Den'] = 17
print(NiceDict)

# Modify values
NiceDict['Vince'] = 18 # Happy birthday
print(NiceDict)

# POP IT OFFFF
NiceDict.pop('Frem')
print(NiceDict)

# You can put a dict in a list, and a list in a dict. WHATEJLKJDFASJD
# Merge dicts using update
NiceDict.update(NewDict)
print(NiceDict)