singleQuotes = 'Single quotes'
doubleQuotes = "Double quotes"
mixed = "I don't know"

firstLetter = singleQuotes[0]
print('firstLetter:', firstLetter)

# Negative indexing
lastLetter = mixed[-1]
print('lastLetter: ', lastLetter)

lastLetter = mixed[len(mixed)-1]
print('lastLetter with len: ', lastLetter)

# escape sequence
print('new \nline')

# length
length = len(singleQuotes)
print('length: ', length)

# slice[start,stop,step]
sliced = singleQuotes[0: 6]
print('sliced: ', sliced)

slicedStepped = singleQuotes[0: 6: 2]
print('slicedStepped: ', slicedStepped)

steppedOnly = singleQuotes[::2]
print('steppedOnly: ', steppedOnly)

reversed = mixed[::-1]
print('reversed: ', reversed)
