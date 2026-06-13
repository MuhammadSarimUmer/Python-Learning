from functools import reduce




# squares = [x**2 for x in range(10) ]
# print(squares)

# evens = [x for x in range(10) if x%2==0]
# print(evens)


# odd = [x for x in range(10) if x%2==0]
# print(odd)

add = lambda x,y : x+y
numbers = [2,3,4,5,6]
# squares = map(lambda x: x**2,numbers)
# print(list(squares))
# # print(add(3,4))
# evenList = filter(lambda x : x%2==0,numbers)
# print(list(evenList))
products = reduce(lambda x,y: x*y,numbers)
print(products)
 