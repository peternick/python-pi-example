
myList= [1,2,3,4]
strMy= ['1','2','3','4']
conc = myList.__add__(myList)

print('concatanated list: ' + str(conc))
print()

sumOfList = sum(myList)
print('sum of values in the list: '+ str(sumOfList))
print()

for index, element in enumerate(myList):
    print(index, element)
print()

strList= '-'.join(str(myList))
print(strList)
print(strList[7])
stringList = '-'.join(strMy)
print(stringList)
print("fetch this shiiit")
