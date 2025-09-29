def createGenerator() :
    mylist = range(1,3)
    for i in mylist :
        yield i/i

mygenerator = createGenerator() # создаём генератор
print(mygenerator)
for i in mygenerator:
    print(i)