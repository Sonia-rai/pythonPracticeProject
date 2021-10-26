# using multiple function at same time!!!
def square(a):
     return a*a

def cube(a):
    return a*a*a

func = [cube,square]
#num = [2,3,5,6,76,3,3,2]
for i in range(5):
     val = list(map(lambda x:x(i), func))
     print(val,end='')
