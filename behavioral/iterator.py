# Iterators are built into Python.
# It can be engaged, using 'iter(arg*)' function
# arg* - can be list, tuple, dic, set and string.
# Below is the example of using it.

# fruits_tuple = {'apple', 'blueberry', 'cherry', 'pineapple'}
# fruits_tuple = ('apple', 'blueberry', 'cherry', 'pineapple')
# fruits_tuple = ['apple', 'blueberry', 'cherry', 'pineapple']
fruits_tuple = 'apples'

fruits_iterator = iter(fruits_tuple)
print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
print(fruits_iterator.__next__())

# Loop through an iterator

fruits_tuple = ('apple', 'blueberry', 'cherry', 'pineapple')

for f in fruits_tuple:
    print(f)

#
# To create an iterator manually we need to implement iter and next
# in __iter__ we initialize iterator, same as in __init__, and return iterator

class Iterator:
    def __iter__(self):
        self.a = 2
        return self # must always return iterator object

    def __next__(self):
        if self.a < 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # to stop iterator in loop


iterable_obj = Iterator()

# iterator = iter(iterable_obj)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for i in iterable_obj:
    print(i)