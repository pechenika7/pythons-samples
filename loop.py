# урок про циклы
def ExampleList():
    list_ = [1, 3, 5, 9]
    for i in list_:
        print (i)
    a = input('введите число')
    if a in list_:
        print('Из этого списка')
    else:
        print('Не из этого списка')

def task ():
    sum = 0
    i = 2
    n = 1
    while n < 21:
        sum += i
        i += 2
        n += 1
    return sum



print (task())

#for i in range(1, 1001):
    #if (i % 17 == 0 or i % 19 == 0):
     #   print (i)

for i in (7, 3, 33):
    print (i)