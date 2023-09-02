import pandas
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))


mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

print((lambda x,y,z: (x+y+z)/3)(10,20,30))